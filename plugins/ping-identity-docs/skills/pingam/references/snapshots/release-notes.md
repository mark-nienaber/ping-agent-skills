---
title: PingAM Release Notes
description: PingAM software is available to download from the Ping Identity Download Center.
component: pingam
version: release-notes
page_id: pingam::single-page
canonical_url: https://docs.pingidentity.com/pingam/release-notes/single-page.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  requirements: Requirements
  files-to-download: Files to download
  operating-systems: Operating systems
  agents: Web and Java agents
  prerequisites-java: Java
  prerequisites-application-servers: Application containers
  directory-servers: Identity stores
  commons-third-party: Third-party software
  supported-clients: Supported browsers
  special-requests: Special requests
  whats_new: What's new
  new_in_am_8_1_x: New in AM 8.1.x
  am_8_1_1: AM 8.1.1
  dcr-script-bindings-81: New methods for DCR script binding
  customize-session-quota-actions-81: Customize session quota exhaustion actions
  oauth_2_0_oidc_improvements: OAuth 2.0 / OIDC improvements
  audience-introspection-81: Allow audience members to introspect tokens
  oauth2-introspection-rfc-9701: Stricter compliance with RFC 9701 JWT Response for OAuth Token Introspection
  am_8_1_0: AM 8.1.0
  node-versioning: Node versioning
  node-definitions-endpoint: Node definitions endpoint
  ai-agents: Identity for AI
  fips-compliance: FIPS compliance
  webauthn-conditional-ui: WebAuthn conditional UI
  android-key-webauthn: Support for Android key attestation
  radius-authentication: RADIUS authentication
  transactional-auth-tree: Transactional authentication trees
  new-auth-nodes: New authentication nodes
  ad-decision-node: AD Decision node
  backchannel-auth-nodes: Backchannel authentication nodes
  jwt-password-replay-node: JWT Password Replay node
  policy-decision-node: Policy nodes
  radius-auth-nodes: RADIUS authentication nodes
  rsa-securid-node: RSA SecurID authentication node
  logout-details: Set Logout Details node
  new-policy-cache: Policy cache
  new-cache-manager: Cache script values
  saml2-scripted-sp-account-mapper: Next-generation scripting support
  nextgen-saml-scripts: SAML 2.0 customization scripts
  nextgen-oauth2-custom-scripts: OAuth 2.0 customization scripts
  social_identity_provider_scripts: Social Identity Provider scripts
  new-nextgen-bindings: Next-generation script bindings
  new-nextgen-common-bindings: Common bindings
  scripted_decision_node_bindings: Scripted Decision node bindings
  dynamic_client_registration_scripting: Dynamic client registration scripting
  scope-validation-script-improvements: Scope validation scripting improvements
  new-global-library-scripts: Create global library scripts
  proxy-per-request: Support for configuring proxy settings per request
  saml2-improvements-8-1: SAML 2.0 IdP-initiated SSO in integrated mode
  new-redirect-tree-sp: Redirect to a tree on the remote SP
  new-saml2node-idpentityid: SAML2 Authentication node
  new-samlapp-getassertion: Scripted access to the SAML 2.0 assertion
  saml2-audit: SAML 2.0 audit logging (hosted IdP)
  application_authorization: Application authorization
  pd-support: PingDirectory support
  custom-cts-dn: Custom CTS DN for FBC installs
  authentication_node_enhancements: Authentication node enhancements
  pingone_nodes: PingOne nodes
  set-detail-nodes: Set Detail nodes
  social-provider-handler-node: Social Provider Handler nodes
  persistent-cookie-nodes: Persistent Cookie nodes
  device-binding-nodes: Device Binding nodes
  new-node-versions-8-1: New node versions
  oauth_2_0_oidc_improvements_2: OAuth 2.0 / OIDC improvements
  alignment-with-par-and-jar-specs: Closer alignment with PAR and JAR specifications
  realm-allow-unauthenticated-user-code-entry: Allow unauthenticated user code entry at the realm level
  map-custom-kids: Map custom key IDs to secrets
  oauth2-accepted-jwt-issuers: Perform OAuth 2.0 client authentication with a third-party issuer
  oauth2-enable-app-context: Enable application context for OAuth 2.0 / OIDC flows
  new-oauth2-require-exp: Require exp claim in JWT request object
  scope-validator-custom-refresh: Customize refresh token scopes with scope validation scripts
  aud-param-on-token-exchange: Support for audience parameter on token exchange requests
  test-pingone-worker-connection: Test the PingOne worker connection
  cdsso-login-template-ig: CDSSO login template for PingGateway
  uss-secrets: Secret store integration for user self-service features
  rar-support: Support for Rich Authorization Requests (RAR)
  new_in_am_8_0_x: New in AM 8.0.x
  am_8_0_2: AM 8.0.2
  fips-compliance-8: FIPS compliance
  new-private-key-jwt-aud: Private key JWT audience setting
  map-custom-kids-8: Mapping custom key IDs to secrets
  alignment-with-par-and-jar-specs-8: Closer alignment with PAR and JAR specifications
  pd-ldifs: PingDirectory LDIFs
  am_8_0_1: AM 8.0.1
  new-refresh-device-ids: Ability to refresh device IDs
  am_8_0_0: AM 8.0.0
  fbc-in-product: FBC in production deployments
  node-designer: Node Designer
  new-scripted-dcr: Dynamic client registration script
  new-der-certs-for-oauth-clients: Support for DER-formatted certificates for OAuth 2.0 client authentication
  new-radius-property: RADIUS server configuration update
  new-idm-policy-condition: IDM policy condition
  new-backchannel-auth: Backchannel authentication
  new-fido-certified: FIDO certification
  webauthn_metadata_service: WebAuthn Metadata service
  webauthn_nodes: WebAuthn nodes
  device_profile_settings: Device profile settings
  new-distributed-tracing: Ability to trace the request flow through Ping Advanced Identity Software
  new-transaction-auth-api: Improved REST API for transactional authorization
  new-pem-certs-on-cert-collector-node: Certificate Collector node supports DER certificates
  new-oauthapp-journeys: OAuth 2.0 application journeys
  new-samlapp-journeys: SAML 2.0 application journeys
  new-saml-custom-nameid: Customize SAML NameID mapping with a script
  new-httpclient-service: Http Client service
  default-trees: Default trees
  new-config-mustrun: Configure trees to run to completion
  nosession-trees: Configure no session trees
  session-duration-timeouts: Session duration and timeout control
  new-social-provider-line: LINE login support
  new-script-binding-improvements-8: Next-generation script bindings
  common_bindings: Common bindings
  scripted_decision_node_bindings_2: Scripted decision node bindings
  library_scripts: Library scripts
  next_generation_script_types: Next-generation script types
  access_pingone_verify_transaction_data: Access PingOne Verify transaction data
  new-enable-device-mgmt-node: Enable Device Management node
  new-flow-control-node: Flow Control node
  json-response-authentication: Customize the JSON in the authentication response
  set_success_details_node: Set Success Details node
  set_failure_details_node: Set Failure Details node
  set_error_details_node: Set Error Details node
  new-idtoken-clock-skew: Configurable clock skew for OIDC ID token expiry time
  new-update-cert-sp-metadata: Update signing certificate in remote SP metadata
  new-exclude-cert-sp-metadata: Configure client certificate in SP metadata
  refresh-token-changes: Changes to refresh tokens
  consistent-errors-refreshing-tokens: Consistent errors when refreshing tokens
  refresh-token-grace-period: Refresh token grace period
  config-provider-improvements: Configuration Provider node
  backchannel_logout_token_contains_exp_claim: Backchannel logout token contains exp claim
  new_ssoadm_commands_update_attributes_in_a_realm_service: New ssoadm commands update attributes in a realm service
  system_property_for_social_provider_sub_claim_uniqueness: System property for social provider sub claim uniqueness
  new_in_am_7_5_x: New in AM 7.5.x
  am_7_5_2: AM 7.5.2
  am_7_5_1: AM 7.5.1
  new-script-binding-improvements: New utility script binding
  backchannel_logout_token_contains_exp_claim_2: Backchannel logout token contains exp claim
  system_property_for_social_provider_sub_claim_uniqueness_2: System property for social provider sub claim uniqueness
  new_ssoadm_commands_update_attributes_in_a_realm_service_2: New ssoadm commands update attributes in a realm service
  am_7_5_0: AM 7.5.0
  new-secrets-api-support: Support for storing secrets in secret stores
  new-mtls-support: Support for mTLS connections
  affinity-to-idrepo: Configurable affinity for connections to the DS identity repository
  new-request-header-node: Request Header node
  new-scalable-clients: Scalable OAuth 2.0 clients
  new-saml-sp-mapping: SAML v2.0 NameID mapping configurable on the service provider (SP)
  new-accept-failure: Use a tree hook to run actions on journey failure
  new-identified-identities: Storing identified identities in the authentication session
  new-identity-assertion-node: Identity Assertion node and Identity Assertion service
  new-ping-protect-node: PingOne Protect nodes and PingOne Worker service
  new-inner-nodes-auditing: Nodes in a Page node log individual audit events
  new_in_am_7_4_x: New in AM 7.4.x
  am_7_4_2: AM 7.4.2
  backchannel_logout_token_contains_exp_claim_3: Backchannel logout token contains exp claim
  new_ssoadm_commands_update_attributes_in_a_realm_service_3: New ssoadm commands update attributes in a realm service
  system_property_for_social_provider_sub_claim_uniqueness_3: System property for social provider sub claim uniqueness
  improvements_to_jwt_operations_in_scripts: Improvements to JWT operations in scripts
  am_7_4_1: AM 7.4.1
  storing_identified_identities_in_the_authentication_session: Storing identified identities in the authentication session
  am_7_4_0: AM 7.4.0
  new-device-nodes: Bind and verify user devices
  new-oauth2-device-endpoint: Support for JSON output from /oauth2/device/user endpoint
  new-oauth2-subname-claim-toggle: Setting to disable the subname claim
  new-allow-client-credentials-in-token-endpoint-query-parameters: Setting to permit client credentials in token endpoint query parameters
  new-restrict-inner-trees: Restriction of access to inner trees
  new-nodestate-method: New nodeState.getObject method
  http-header-support-scripts: X-ForgeRock-TransactionID available in HTTP client script binding
  customize_account_lockout_message: Customize account lockout message
  scripting-enhancements: Scripting enhancements
  scripting_logger_name_change: Scripting logger name change
  access-request-headers: Access request header values from OAuth 2.0 scripts
  fbc-migration-tool: File-based configuration migration utililty
  support-mtls: Support for mTLS authentication
  new-query-param-node: Query Parameter node
  new-html-in-email-suspend-node: Support for HTML in Email Suspend node
  fixes: Fixes
  fixes_in_am_8_1_x: Fixes in AM 8.1.x
  am_8_1_1_2: AM 8.1.1
  am_8_1_0_2: AM 8.1.0
  am_8_0_x: AM 8.0.x
  am_7_5_x: AM 7.5.x
  am_7_4_x: AM 7.4.x
  am_7_3_x: AM 7.3.x
  fixes_in_am_8_0_x: Fixes in AM 8.0.x
  am_8_0_2_2: AM 8.0.2
  am_8_0_1_2: AM 8.0.1
  am_8_0_0_2: AM 8.0.0
  am_7_5_x_2: AM 7.5.x
  am_7_4_x_2: AM 7.4.x
  am_7_3_x_2: AM 7.3.x
  fixes_in_am_7_5_x: Fixes in AM 7.5.x
  am_7_5_2_2: AM 7.5.2
  am_7_5_1_2: AM 7.5.1
  am_7_5_0_2: AM 7.5.0
  am_7_4_x_3: AM 7.4.x
  am_7_3_x_3: AM 7.3.x
  fixes_in_am_7_4_x: Fixes in AM 7.4.x
  am_7_4_2_2: AM 7.4.2
  am_7_4_1_2: AM 7.4.1
  am_7_4_0_2: AM 7.4.0
  am_7_3_x_4: AM 7.3.x
  removed-functionality: Removed
  am_8_1_0_3: AM 8.1.0
  am_8_0: AM 8.0
  am_7_5: AM 7.5
  changes: Changes
  changes_in_am_8_1_x: Changes in AM 8.1.x
  am_8_1: AM 8.1
  opentelemetry_changes: OpenTelemetry changes
  scope_validation_plugin_script: Scope validation plugin script
  saml2-sso-flows: SAML v2.0 SSO flows
  certificate-nodes: Certificate nodes
  idm_configuration_cache_enabled: IDM configuration cache enabled
  guice-servlet-filter: Servlet and filter declarations
  default-kid-values-in-gsm-stores: Default kid values for GSM certificates
  parallel_updates_for_cts_sessions: Parallel updates for CTS sessions
  changes_in_am_8_0_x: Changes in AM 8.0.x
  am_8_0_3: AM 8.0
  tomcat-10: Support for Tomcat 10
  modules-and-chains: Authentication modules and chains
  tls-client-cert-header: Providing OAuth 2.0 client certificates to AM
  webauthn-flow-behaviour: Change in behavior for WebAuthn flows
  prometheus-monitoring-endpoint: Endpoint for monitoring server activity with Prometheus
  session-terminology: Sessions terminology
  change-social-idp-wellknownendpoint: Change to custom OIDC Social IDP configuration
  change-audit-logging: Changes to audit logging
  ws_federation_com_sun_identity_wsfederation_logout_wreply_url_validation: WS-Federation com.sun.identity.wsfederation.logout.wreply URL validation
  change-linkedin-config: Changes to LinkedIn social identity provider configuration
  soap_sts_service: SOAP STS service
  the_accountid_field_in_jwt_script_binding_operations: The accountId field in JWT script binding operations
  device_authorization_grant_behavior: Device authorization grant behavior
  changes_in_am_7_5_x: Changes in AM 7.5.x
  am_7_5_3: AM 7.5
  change-cert-collector-node: Change in behavior for journeys containing a Certificate Collector node
  change-padinputs: Default setting for AES key wrap encryption
  change-introspected: Change to OAuth 2.0 refresh token introspection response types
  changes_in_am_7_4_x: Changes in AM 7.4.x
  am_7_4_2_3: AM 7.4.2
  the_accountid_field_in_jwt_script_binding_operations_2: The accountId field in JWT script binding operations
  am_7_4_1_3: AM 7.4.1
  ws_federation_com_sun_identity_wsfederation_logout_wreply_url_validation_2: WS-Federation com.sun.identity.wsfederation.logout.wreply URL validation
  ws_federation_com_sun_identity_wsfederation_logout_wreply_url_validation_3: WS-Federation com.sun.identity.wsfederation.logout.wreply URL validation
  change_in_behavior_for_journeys_containing_a_certificate_collector_node: Change in behavior for journeys containing a Certificate Collector node
  change_to_oauth_2_0_refresh_token_introspection_response_types: Change to OAuth 2.0 refresh token introspection response types
  am_7_4: AM 7.4
  change-dsameuserpwd: Removal of dsameuserpwd from default keystore
  change-enable-data-store: Preconfigure policy and application data stores
  change-delete-auth-tree: Change in behavior when an authentication tree is deleted
  change-subjectattributes: Change in behavior of subjectattributes endpoint
  change-amadmin-password-secret-cache: Rotatable secrets for amAdmin password
  amster: Amster
  deprecated-functionality: Deprecated
  deprecated_since_pingam_8_1: Deprecated since PingAM 8.1
  saml_v2_0_jsps: SAML v2.0 JSPs
  authentication_by_module_instance_policy_condition_type: Authentication by Module Instance policy condition type
  node-versioning-endpoints: Node versioning REST endpoints
  deprecated_since_pingam_8_0: Deprecated since PingAM 8.0
  prometheus-monitoring-endpoint-deprecated: Monitoring
  deprecated-audit-event-handlers: Audit event handlers
  deprecated_since_am_7_5: Deprecated since AM 7.5
  secret_label_mappings: Secret label mappings
  configuration_replaced_by_secret_labels: Configuration replaced by secret labels
  changes_to_action_class: Changes to Action class
  legacy_social_provider_node: Legacy Social Provider node
  doc-updates: Documentation updates
  am_8_1_x: AM 8.1.x
  am_8_1_1_3: AM 8.1.1
  am_8_1_0_4: AM 8.1.0
  am_8_0_x_2: AM 8.0.x
  am_8_0_2_3: AM 8.0.2
  am_8_0_1_3: AM 8.0.1
  am_8_0_0_3: AM 8.0.0
  am_7_5_x_3: AM 7.5.x
  am_7_5_2_3: AM 7.5.2
  am_7_5_1_3: AM 7.5.1
  am_7_5_0_3: AM 7.5.0
  known-issues: Known issues
  am_8_1_x_2: AM 8.1.x
  am_8_1_1_4: AM 8.1.1
  am_8_1_0_5: AM 8.1.0
  am_8_0_x_3: AM 8.0.x
  am_8_0_2_4: AM 8.0.2
  am_8_0_1_4: AM 8.0.1
  am_8_0_0_4: AM 8.0.0
  am_7_5_x_4: AM 7.5.x
  am_7_5_2_4: AM 7.5.2
  am_7_5_1_4: AM 7.5.1
  am_7_5_0_4: AM 7.5.0
  limitations: Limitations
  redundant_files: Redundant files
  evaluation_installations: Evaluation installations
  identity_and_data_store_scaling: Identity and data store scaling
  webauthn-limitations: Web Authentication (WebAuthn)
  am_admin_ui_access_requires_the_realm_admin_privilege: AM admin UI access requires the Realm Admin privilege
  specifying_keys_in_jwt_headers: Specifying keys in JWT headers
  different_am_versions_within_a_site: Different AM versions within a site
  special_characters_in_policy_application_or_referral_names: Special characters in policy, application, or referral names
  xacml_policy_import_and_export_from_different_vendors: XACML policy import and export from different vendors
  uma: UMA
  amster-limitations: Amster
  stability: Interface stability
  release-levels: Product release levels
  interface-stability: Product stability labels
  getting-support: Getting support
  security-advisories: Security advisories
  release_timeline: Release timeline
---

# PingAM Release Notes

## Requirements

### Files to download

PingAM software is available to download from the [Ping Identity Download Center](https://backstage.pingidentity.com/downloads/browse/am/all).

The following table describes the files available for download.

**PingAM software**

| File               | Description                                                                                                                                                                                                         |
| ------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `AM-8.1.1.zip`     | Cross-platform distribution including all software components.Find a list of the files in the `.zip` archive in [Download AM](https://docs.pingidentity.com/pingam/8.1/installation/download-openam-software.html). |
| `AM-8.1.1.war`     | Deployable web application archive file.                                                                                                                                                                            |
| `Amster-8.1.1.zip` | The .zip file that contains the Amster command-line interface.                                                                                                                                                      |

> **Collapse: Files for previous versions**
>
> | File                          | AM 7.5                            | AM 8.0                            |
> | ----------------------------- | --------------------------------- | --------------------------------- |
> | **AM `.zip`**                 | AM-7.5.2.zip                      | AM-8.0.2.zip                      |
> | **AM `.war`**                 | AM-7.5.2.war                      | AM-8.0.2.war                      |
> | **AM SSO Admin Tools**        | SSOAdminTools-5.1.3.30.zip        | SSOAdminTools-5.1.3.30.zip        |
> | **AM SSO Configurator Tools** | SSOConfiguratorTools-5.1.3.30.zip | SSOConfiguratorTools-5.1.3.30.zip |
> | **Amster `.zip`**             | Amster-7.5.2.zip                  | Amster-8.0.2.zip                  |

### Operating systems

**AM 8 and later** software is supported on actively maintained versions of the following operating systems:

* Amazon Linux

* Debian

* Red Hat Enterprise Linux

* Rocky Linux

* SUSE Linux Enterprise

* Ubuntu Linux

* Windows Server 2019, 2022 and 2025

**AM 7.5 and earlier** software is supported on the following operating systems:

| Operating system             | AM 7.5                                     |
| ---------------------------- | ------------------------------------------ |
| **Amazon Linux**             | 2023                                       |
| **Debian Linux**             | 11                                         |
| **Red Hat Enterprise Linux** | 8, 9                                       |
| **Rocky Linux**              | 8, 9                                       |
| **SuSE**                     | 15                                         |
| **Ubuntu**                   | 18.04 LTS, 20.04 LTS, 22.04 LTS, 24.04 LTS |
| **Windows Server**           | 2016, 2019, 2022                           |

### Web and Java agents

The following table summarizes the minimum recommended version of web and Java agents:

| Agent           | Version   |
| --------------- | --------- |
| **Web agents**  | 2024.11.2 |
| **Java agents** | 2024.11.1 |

AM supports several versions of web agents and Java agents. You can find information about supported container versions and other platform requirements related to agents in the [Web Agents Release Notes](https://docs.pingidentity.com/web-agents/release-notes/requirements.html) and the [Java Agents Release Notes](https://docs.pingidentity.com/java-agents/release-notes/requirements.html).

### Java

PingAM software is supported on the following Java environments:

| Vendor          | AM 7.5 | AM 8.0        | AM 8.1     |
| --------------- | ------ | ------------- | ---------- |
| **OpenJDK** (1) | 17     | 17, 21, 25(2) | 17, 21, 25 |
| **Oracle Java** | 17     | 17, 21, 25(2) | 17, 21, 25 |

(1) AM supports OpenJDK-based distributions, including:

* AdoptOpenJDK/Eclipse Temurin Java Development Kit (Adoptium)

* Amazon Corretto

* Azul Zulu

* Red Hat OpenJDK

Ping Identity tests most extensively with AdoptOpenJDK/Eclipse Temurin. Use the HotSpot JVM, if possible.

(2) AM supports Java 25 from 8.0.2. AM 8.0.0 and 8.0.1 support only Java 17 and 21.

|   |                                                  |
| - | ------------------------------------------------ |
|   | Always use a JVM with the latest security fixes. |

### Application containers

This table summarizes supported web application containers and their required versions:

| Container                                 | AM 7.5   | AM 8.0   | AM 8.1   |
| ----------------------------------------- | -------- | -------- | -------- |
| **Apache Tomcat**                         | 8.5, 9   | 10       | 10, 11   |
| **IBM WebSphere Liberty**                 | 22.0.0.4 | 24.0.0.6 | 24.0.0.6 |
| **JBoss Enterprise Application Platform** | 7.4      | 8.x      | 8.x      |
| **Wildfly**                               | 26       | 30       | 30, 39   |

The web application container must be able to write to its own home directory, where AM stores configuration files.

|   |                                                                                                                                                                                                                                                                                                                                                                 |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Java Agents and Web Agents require the WebSocket protocol to communicate with AM.Make sure the container where AM runs, the web server/container where the agents run, and your network infrastructure all support the WebSocket protocol.Read your network infrastructure and web server/container documentation for more information about WebSocket support. |

### Identity stores

You can configure AM to use any LDAPv3-compliant directory server as an identity store. This table lists the supported directory servers for storing AM identities.

You can find information on configuring these directory servers in [identity stores](https://docs.pingidentity.com/pingam/8.1/setup/setting-up-identity-stores.html).

|   |                                                                                                                                                                                                                                                                                                                    |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | * Policies, applications, CTS tokens, and UMA-related information can *only* be stored in a PingDS directory server.

* Static configuration can be stored in a PingDS directory server or, from AM 8.0, in [JSON files](https://docs.pingidentity.com/pingam/8.1/installation/fbc.html) on the local file system. |

**Supported identity stores**

| Directory server                                                                                         | AM 7.5      | AM 8.0           | AM 8.1          |
| -------------------------------------------------------------------------------------------------------- | ----------- | ---------------- | --------------- |
| **Embedded PingDS** (1)(2)                                                                               | 7.5         | N/A              |                 |
| **[External PingDS](https://docs.pingidentity.com/pingam/8.1/installation/prepare-ext-stores.html)** (2) | 6 and later | 7.3.1 and later  | 7.4.4 and later |
| **PingDirectory**                                                                                        | 9.3         |                  |                 |
| **Oracle Unified Directory**                                                                             | 11g R2      | 12c              |                 |
| **Oracle Directory Server Enterprise Edition**                                                           | 11g         | N/A              |                 |
| **Microsoft Active Directory**                                                                           | 2016, 2019  | 2019, 2022, 2025 |                 |
| **IBM Tivoli Directory Server**                                                                          | 6.4         | N/A              |                 |

(1) Demo and test environments only in AM 7.x. Unsupported since AM 8.\
(2) PingDS, formerly named ForgeRock Directory Server.

### Third-party software

Ping Identity supports using the following third-party software when logging Common Audit events:

**Third-party logging software**

| Software                      | Version              |
| ----------------------------- | -------------------- |
| Java Message Service (JMS)    | 2.0 API              |
| MySQL JDBC Driver Connector/J | 8 (at least 8.0.19)  |
| Splunk                        | 8.0 (at least 8.0.2) |

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Elasticsearch and Splunk have native or third-party tools to collect, transform, and route logs. Examples include [Logstash](https://www.elastic.co/logstash) and [Fluentd](https://www.fluentd.org/).Consider using these alternatives as they have advanced, specialized features focused on getting log data into the target system. They decouple the solution from the Ping Advanced Identity Software systems and version, and provide inherent persistence and reliability. You can configure the tools to avoid losing audit messages if a Ping Advanced Identity Software service goes offline, or delivery issues occur.These tools can work with Common Audit logging:- Configure the server to log messages to standard output, and route from there.

- Configure the server to log to files, and use log collection and routing for the log files. |

Ping Identity supports using the following third-party software when monitoring AM servers:

**Third-party monitoring software**

| Software   | Version            |
| ---------- | ------------------ |
| Grafana    | 5 (at least 5.0.2) |
| Graphite   | 1                  |
| Prometheus | 2.0                |

For hardware security module (HSM) support, AM requires a client library that conforms to the PKCS#11 standard v2.20 or later.

### Supported browsers

AM supports the latest, stable versions of the following browsers:

* Google Chrome

* Microsoft Edge

* Firefox

* Safari

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | Ping Identity doesn't provide support for these browsers:* Internet Explorer 11

* Microsoft Edge in Internet Explorer compatibility mode

* Embedded browsers within any application (for example, within Citrix environments or Office 365)Ping Identity optimizes its platform for modern browsers to ensure the best user experience, security, and performance. If you encounter issues while using the Ping Advanced Identity Software, ensure you use a supported, up-to-date browser for the optimal experience. |

### Special requests

If you have a special request regarding support for a combination not listed here, contact support.

## What's new

### New in AM 8.1.x

#### AM 8.1.1

AM 8.1.1 is a maintenance release that introduces functional enhancements and fixes.

##### New methods for DCR script binding

The `clientIdentity` binding in Dynamic Client Registration (DCR) scripts includes two new methods for managing AI agent identity attributes when AM is integrated with PingIDM:

* `getAiAgentIdentityAttributes()`: Returns the AI agent identity attributes for the client as a map, or `null` if the client isn't an AI agent.

* `updateAiAgentIdentityAttributes(attributes)`: Patches the underlying PingIDM object with the supplied attributes. The supplied attributes are merged with existing ones, so you don't need to retrieve the full attribute set first. Supply `null` as a value to remove an existing key.

Learn more in [DCR script API](https://docs.pingidentity.com/pingam/8.1/am-scripting/dcr-api.html).

##### Customize session quota exhaustion actions

Customizing session quota exhaustion actions no longer requires ssoadm. Instead, the custom plugin is now dynamically loaded by AM using the [ServiceLoader](https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/ServiceLoader.html) mechanism. Additionally, the implementation class is now annotated with @I18nKey("customActionI18nKey") to let you customize and localize the action name.

Learn more in [Customize session quota exhaustion actions](https://docs.pingidentity.com/pingam/8.1/security/custom-quota-exhaustion-action.html).

##### OAuth 2.0 / OIDC improvements

###### Allow audience members to introspect tokens

AM now supports a new Allow audience members to introspect tokens setting on the OAuth 2.0 provider. When enabled, a client whose `client_id` appears anywhere in a token's `aud` claim can introspect that token, and not just the issuing client. This lets resource servers that receive tokens through token exchange validate them directly without requiring a special scope.

Learn more in [Introspection requirements](https://docs.pingidentity.com/pingam/8.1/am-oauth2/oauth2-introspect-endpoint.html#introspection-requirements).

###### Stricter compliance with RFC 9701 JWT Response for OAuth Token Introspection

[RFC 9701](https://www.rfc-editor.org/rfc/rfc9701.html) defines a JSON Web Token (JWT) response format for OAuth 2.0 token introspection. AM now includes stricter compliance with this specification, ensuring that the introspection response adheres to the JWT format when configured to do so.

Find more information in [RFC 9701 token\_introspection claim](https://docs.pingidentity.com/pingam/8.1/am-oauth2/oauth2-introspect-endpoint.html#rfc-9701-token-introspection-claim).

#### AM 8.1.0

AM 8.1.0 is a minor release that introduces new features, functional enhancements, and fixes.

##### Node versioning

We've made changes to AM to provide node versioning functionality. When we make changes to a node in the future, we'll create a new version of the node. This release introduces five [new node versions](#new-node-versions-8-1).

Learn more about node versioning in [Node versions](https://docs.pingidentity.com/pingam/8.1/am-authentication/node-versions.html).

You can create versioned nodes for your [custom Java nodes](https://docs.pingidentity.com/pingam/8.1/auth-nodes/create-versioned-nodes.html). Additionally, you can choose the version of the node to imitate in the Configuration Provider node.

Other node versioning changes include:

* Resource version `3.0` for `authenticationtrees` REST endpoint

  We've added a version-aware `3.0` resource to the `realm-config/authentication/authenticationtrees` endpoint. When sending a request to this endpoint, set the `Accept-API-Version` header to `protocol=2.1,resource=3.0`.

  Resource versions 1.0 and 2.0 are [deprecated](deprecation.html#node-versioning-endpoints).

  Learn more in [Create a tree over REST](https://docs.pingidentity.com/pingam/8.1/am-authentication/create-auth-trees.html#create-authn-tree-rest).

* Versioned node endpoints

  The `realm-config/authentication/authenticationtrees/nodes` endpoint is now versioned. Specify the version of the node in the request URL, for example: `https://am.example.com:8443/am/json/realms/root/realms/alpha/realm-config/authentication/authenticationtrees/nodes/UsernameCollectorNode/2.0`.

  Versionless node endpoints are [deprecated](deprecation.html#node-versioning-endpoints).

  Learn more in [Create a tree over REST](https://docs.pingidentity.com/pingam/8.1/am-authentication/create-auth-trees.html#create-authn-tree-rest).

* Audit logging

  The node version is logged in the [Authentication log](https://docs.pingidentity.com/pingam/8.1/monitoring/audit-logging-ref.html#authentication-log-format) under the `AM-NODE-LOGIN-COMPLETED` event.

  By default, `version` is logged only for node versions greater than `1.0`. To log `version` for all node versions, add the [`org.forgerock.am.auth.node.versioning.enable.v1.audit.detail`](https://docs.pingidentity.com/pingam/8.1/setup/server-advanced.html#org.forgerock.am.auth.node.versioning.enable.v1.audit.detail) advanced server property and set it to `true`.

##### Node definitions endpoint

A new `listLatestNodeDefinitions` action on the `realm-config/authentication/authenticationtrees/nodes` endpoint provides a list of node definitions for the *latest* version of each node.

This action combines the responses from the following separate actions into a single response:

* `getAllTypes` action on the `realm-config/authentication/authenticationtrees/nodes` endpoint

* `schema`, `template` and `listOutcomes` actions on the `realm-config/authentication/authenticationtrees/nodes/node-name` endpoint

Learn more in [List latest node definitions](https://docs.pingidentity.com/pingam/8.1/am-authentication/list-latest-node-definitions.html).

##### Identity for AI

We've added support for AI agents in AM. AI agents are specialized OAuth 2.0 identities that securely perform tasks on behalf of end users through a delegated token exchange process, ensuring distinct accountability and granular access control.

You can use AI agents to securely build [digital assistants](https://developer.pingidentity.com/identity-for-ai/glossary/idai-glossary.html#digital-assistant) that operate on behalf of end users, such as a chatbot on a retail website helping a user navigate products, or an internal workforce assistant acting on behalf of an employee to access enterprise tools like Salesforce.

Learn more in [AI agents](https://docs.pingidentity.com/pingam/8.1/am-oauth2/ai-agents.html).

##### FIPS compliance

AM can be configured to run in a FIPS-approved mode of operation with Bouncy Castle FIPS keystores to comply with [FIPS 140-3](https://csrc.nist.gov/pubs/fips/140-3/final).

Find more information in [FIPS 140–3 compliance](https://docs.pingidentity.com/pingam/8.1/security/fips.html).

##### WebAuthn conditional UI

AM now supports the WebAuthn *conditional UI*, also known as *passkey autofill*. This lets users sign in with a passkey if they've previously saved one in their browser. If they don't have a suitable passkey, the browser lets them authenticate using a different method, such as their username and password or social authentication.

This feature provides a more seamless login experience to end users and can help increase the adoption of passkeys.

Learn more in [Configure WebAuthn conditional UI](https://docs.pingidentity.com/pingam/8.1/am-authentication/authn-mfa-webauthn.html#webauthn-conditional-ui).

##### Support for Android key attestation

AM now supports the [Android Key Attestation Statement Format](https://www.w3.org/TR/webauthn/#sctn-android-key-attestation) in WebAuthn requests.

Find more information in the documentation for the [WebAuthn Registration node](https://docs.pingidentity.com/auth-node-ref/8.1/webauthn-registration.html).

##### RADIUS authentication

The RADIUS server service in AM now supports authentication trees. You can create a journey that's compatible with the RADIUS protocol, and then configure clients within the RADIUS server service to use that journey for authentication. Learn more in [AM as a RADIUS server](https://docs.pingidentity.com/pingam/8.1/am-authentication/radius-server.html).

Additionally, there are [new nodes](#radius-auth-nodes) to support RADIUS authentication from within a journey, where AM is acting as the RADIUS client.

##### Transactional authentication trees

A transactional authentication tree only runs when AM starts a transaction, which happens when AM does one of the following:

* Initializes [backchannel authentication](https://docs.pingidentity.com/pingam/8.1/am-authentication/backchannel-authentication.html) using either the `/authenticate/backchannel/initialize` endpoint or the [Backchannel Initialize node](https://docs.pingidentity.com/auth-node-ref/8.1/backchannel-initialize.html).

* Runs a [SAML 2.0 app](https://docs.pingidentity.com/pingam/8.1/am-saml2/configure-providers.html#samlapp-tree) tree for a remote SP.

* Runs an [OAuth 2.0 app](https://docs.pingidentity.com/pingam/8.1/am-oauth2/oauth2-register-client.html#oauth2app-tree) tree when AM is acting as an authorization server.

* Enforces a [transactional authorization](https://docs.pingidentity.com/pingam/8.1/am-authorization/transactional-authorization.html) policy.

You can only configure transactional authentication trees using the REST API. Set the `transactionalOnly` property to `true` in the tree configuration.

Learn more in [Configure a transactional authentication tree](https://docs.pingidentity.com/pingam/8.1/am-authentication/configure-auth-trees.html#configure-transactional-auth-tree).

##### New authentication nodes

###### AD Decision node

The [AD Decision node](https://docs.pingidentity.com/auth-node-ref/8.1/ad-decision.html) lets you verify credentials against a specified Active Directory data store.

The node also checks whether the user account is locked, disabled, or has expired.

###### Backchannel authentication nodes

The following new nodes provide [backchannel authentication](https://docs.pingidentity.com/pingam/8.1/am-authentication/backchannel-authentication.html) functionality from within a journey:

* [Backchannel Initialize node](https://docs.pingidentity.com/auth-node-ref/8.1/backchannel-initialize.html)

* [Backchannel Notification node](https://docs.pingidentity.com/auth-node-ref/8.1/backchannel-notification.html)

* [Backchannel Status node](https://docs.pingidentity.com/auth-node-ref/8.1/backchannel-status.html)

###### JWT Password Replay node

The [JWT Password Replay](https://docs.pingidentity.com/auth-node-ref/8.1/jwt-password-replay.html) node secures the user's password within an encrypted JSON Web Token (JWT). Applications, such as PingGateway, can then use a shared secret to decrypt the JWT and replay the credentials for authentication.

Learn more in [Password replay with AM](https://docs.pingidentity.com/pinggateway/2026/gateway-guide/credentials-am.html).

###### Policy nodes

* Policy Decision node

  A new [Policy Decision node](https://docs.pingidentity.com/auth-node-ref/8.1/policy-decision.html) lets you evaluate an authorization policy against resources within an authentication journey.

  You can configure the node to target a specific policy or application, or use a Configuration Provider node script to determine the policy dynamically.

  The node sets the outcome based on the policy's decision. It doesn't handle advices.

* App Policy Decision node

  The [App Policy Decision node](https://docs.pingidentity.com/auth-node-ref/8.1/app-policy-decision.html) is a specialized version of the Policy Decision node designed to simplify the evaluation of application access policies within a journey.

  It automatically identifies the policy set and resource (OAuth 2.0 client ID or SAML SP entity ID) from the journey context.

###### RADIUS authentication nodes

Two new nodes provide RADIUS authentication functionality from within a journey, where AM is acting as the [RADIUS client](https://docs.pingidentity.com/pingam/8.1/am-authentication/radius-client.html):

* [RADIUS Decision node](https://docs.pingidentity.com/auth-node-ref/8.1/radius-decision.html)

* [RADIUS Challenge Collector node](https://docs.pingidentity.com/auth-node-ref/8.1/radius-challenge-collector.html)

These nodes replace the RADIUS authentication module.

###### RSA SecurID authentication node

A new [RSA SecurID node](https://docs.pingidentity.com/auth-node-ref/8.1/rsa-securid.html) lets you perform multi-factor authentication (MFA) by integrating with RSA SecurID.

This node replaces the SecurID authentication module.

###### Set Logout Details node

A new [Set Logout Details node](https://docs.pingidentity.com/auth-node-ref/8.1/set-logout-details.html) lets you add details to the JSON response when a journey ends with the user logging out. You can also use this to add a `goto` parameter that redirects the user to a specified URL on logout.

The ability to add details to the logout response is made possible with new [logout hooks](https://docs.pingidentity.com/pingam/8.1/am-authentication/create-logout-hook.html), which let you run custom server-side logic on logout.

##### Policy cache

The ability to store policy definitions in cache memory results in improved performance for policy evaluation.

Find more information in [Tune policy evaluation](https://docs.pingidentity.com/pingam/8.1/am-authorization/what-is-authz-decision.html#tune-policy-evaluation).

##### Cache script values

The cache manager service lets you cache, retrieve, and manage data using the `cacheManager` binding in a Scripted Decision node script. This improves performance by storing frequently used or computationally expensive values, such as access tokens from an external service, reducing the need to fetch or calculate them on every execution.

The service automatically runs a `load()` function from a configured cache when a script requests a value that isn't in the cache. Subsequent requests return the stored value until it expires.

Learn more in [Cache script values](https://docs.pingidentity.com/pingam/8.1/am-scripting/cache-manager.html).

##### Next-generation scripting support

We've added support for next-generation scripting to the following scripting contexts:

###### SAML 2.0 customization scripts

All the SAML 2.0 customization scripts are now enabled for next-generation:

* [IdP adapter](https://docs.pingidentity.com/pingam/8.1/am-saml2/custom-idp-adapter.html) ([API](https://docs.pingidentity.com/pingam/8.1/am-scripting/saml2-idp-adapter-api.html))

  Alter the processing of the authentication request.

* [IdP attribute mapper](https://docs.pingidentity.com/pingam/8.1/am-saml2/custom-idp-attribute-mapper.html) ([API](https://docs.pingidentity.com/pingam/8.1/am-scripting/saml2-idp-attribute-mapper-api.html))

  Map user attributes to SAML assertion attributes.

* [SP account mapper](https://docs.pingidentity.com/pingam/8.1/am-saml2/custom-sp-account-mapper.html) ([API](https://docs.pingidentity.com/pingam/8.1/am-scripting/saml2-sp-account-mapper-api.html))

  Map assertions to user accounts on the SP side.

* [SP adapter](https://docs.pingidentity.com/pingam/8.1/am-saml2/custom-sp-adapter.html) ([API](https://docs.pingidentity.com/pingam/8.1/am-scripting/saml2-sp-adapter-api.html))

  Modify the processing of the authentication request on the SP side.

###### OAuth 2.0 customization scripts

All the OAuth 2.0 scripted extension points can now use the next-generation scripting engine:

* [Access token modification](https://docs.pingidentity.com/pingam/8.1/am-oauth2/modifying-access-tokens-scripts.html) ([API](https://docs.pingidentity.com/pingam/8.1/am-scripting/access-token-modification-api.html))

  You can now also access the redirect URIs through the `clientProperties` script binding.

* [Authorize endpoint data provider](https://docs.pingidentity.com/pingam/8.1/am-oauth2/plugins-auth-endpoint-data-provider.html) ([API](https://docs.pingidentity.com/pingam/8.1/am-scripting//authorize-endpoint-data-provider-api.html))

* [May act](https://docs.pingidentity.com/pingam/8.1/am-oauth2/token-exchange.html) ([API](https://docs.pingidentity.com/pingam/8.1/am-scripting/may-act-api.html))

* [OIDC claims](https://docs.pingidentity.com/pingam/8.1/am-oauth2/plugins-user-info-claims.html) ([API](https://docs.pingidentity.com/pingam/8.1/am-scripting/user-info-claims-api.html))

* [Scope evaluation](https://docs.pingidentity.com/pingam/8.1/am-oauth2/plugins-scope-evaluation.html) ([API](https://docs.pingidentity.com/pingam/8.1/am-scripting/scope-evaluation-api.html))

* [Scope validation](https://docs.pingidentity.com/pingam/8.1/am-oauth2/plugins-scope-validation.html) ([API](https://docs.pingidentity.com/pingam/8.1/am-scripting/scope-validation-api.html))

* [Scripted JWT issuer](https://docs.pingidentity.com/pingam/8.1/am-oauth2/oauth2-jwt-bearer-grant.html#configure-scripted-jwt-issuer)

Learn more in [Migrate OAuth scripts to next-generation scripts](https://docs.pingidentity.com/pingam/8.1/am-scripting/access-token-modification-migrate.html).

###### Social Identity Provider scripts

We've introduced next-generation script contexts for social identity provider components. While these functions previously relied on a single legacy social identity profile transformation script, you can now use specialized scripts for:

* [Social IdP service](https://docs.pingidentity.com/pingam/8.1/am-authentication/social-idp-client-reference.html#transform-script) to transform the IdP's raw profile into a normalized object.

* [Social Provider Handler node](https://docs.pingidentity.com/auth-node-ref/8.1/social-provider-handler.html) to transform the normalized profile into an identity or managed object.

* [OIDC ID Token Validator node](https://docs.pingidentity.com/auth-node-ref/8.1/oidc-idtoken-validator.html) to map ID token attributes to local attributes.

##### Next-generation script bindings

The following improvements have been made to script bindings for this release:

* `journey`: Use this new binding to identify the current journey and access information about journey configuration.

* `locales`: Use this new binding to return the localized version of a string from a translation map.

These bindings are available to the Configuration Provider node, Scripted Decision node, and Device Match node scripts.

###### Common bindings

* `utils.crypto.subtle`:

  * You can now use the ECDSA algorithm to generate keys, and to sign and verify signatures.

  * Use the new `crypto.subtle.deriveKey` method to derive a key given a base key and some random salt.

* `utils.base64url` now supports byte operations with the following new methods:

  * `String base64url.encode(byte[] toEncode)`

  * `byte[] base64url.decodeToBytes(String toDecode)`

- `httpClient`:

  * Reference an instance of the Http Client service to route requests through a proxy connection.

  * You can now access this binding from SAML 2.0 IdP scripts.

Learn more in [Script bindings](https://docs.pingidentity.com/pingam/8.1/am-scripting/script-bindings.html).

###### Scripted Decision node bindings

* `samlApplication`:

  * This binding has a new method, `getAssertion()`, that returns the assertion as a JSON map.

  * The `samlApplication` object is present in SAML 2.0 trees or set as the redirect tree on the hosted SP.

    You can also make sure the binding is available for all SAML flows by enabling the application context in the [hosted IdP](https://docs.pingidentity.com/pingam/8.1/am-saml2/saml2-reference.html#saml-idp-enable-app-context) or [remote SP](https://docs.pingidentity.com/pingam/8.1/am-saml2/saml2-reference.html#saml-sp-app-context-enabled) entity configuration.

* `identity`:

  The identity object returned by `idRepository.getIdentity()` now includes an `exists()` method. This lets you check whether the identity exists before performing further operations on the object.

Learn more in the [Scripted Decision node API](https://docs.pingidentity.com/pingam/8.1/am-scripting/scripting-api-node.html).

###### Dynamic client registration scripting

The `clientIdentity` binding has new methods to make it easier to set attributes without requiring LDAP formatting.

Learn more in the [Dynamic client registration scripting API](https://docs.pingidentity.com/pingam/8.1/am-scripting/dcr-api.html).

###### Scope validation scripting improvements

The following next-generation scripting changes have been made to improve customization and control over scope validation:

* `scopeValidatorHelper`:

  This new binding has methods that let you [customize refresh token scopes](#scope-validator-custom-refresh) and that let you trigger an `InvalidScopeException` for unauthorized or malformed scope requests.

* `availableScopes`:

  You can use this new binding to access all the scopes currently configured on the OAuth 2.0 client making the request.

Learn more in the [Scope validation API](https://docs.pingidentity.com/pingam/8.1/am-scripting/scope-validation-api.html).

##### Create global library scripts

To create a global library script that can be accessed from all realms, perform an HTTP POST using the `/json/scripts` endpoint, with an `_action` parameter set to `createGlobal`.

Learn more in [Create a global library script](https://docs.pingidentity.com/pingam/8.1/am-scripting/rest-api-scripts-create.html#rest-api-scripts-create-global).

##### Support for configuring proxy settings per request

AM now lets you define proxy settings at the request level.

Route a request through a proxy by configuring the `httpClient` binding to reference an instance of the Http Client service.

The service settings override the `*.system.proxy.*` advanced properties.

Learn more in [Http Client service](https://docs.pingidentity.com/pingam/8.1/setup/services-configuration.html#global-httpclient).

##### SAML 2.0 IdP-initiated SSO in integrated mode

AM 8.1.0 introduces the following improvements to enable an IdP-initiated SSO flow using trees:

###### Redirect to a tree on the remote SP

Configure the hosted SP to redirect to a tree when a response is received from the IdP.

Learn more in [Redirect Tree](https://docs.pingidentity.com/pingam/8.1/am-saml2/saml2-reference.html#config-redirect-tree).

###### SAML2 Authentication node

Use the new configuration option to check that the IdP entity ID in the incoming SAML assertion matches the IdP entity ID configured for the node.

Learn more in [SAML2 Authentication node](https://docs.pingidentity.com/auth-node-ref/8.1/saml2.html).

###### Scripted access to the SAML 2.0 assertion

The `samlApplication` binding, available to Scripted Decision nodes, now includes the `getAssertion()` method, which returns the SAML assertion as a JSON map.

Learn more in [Query SAML application and authentication request](https://docs.pingidentity.com/pingam/8.1/am-scripting/scripting-api-node.html#samlapp-binding).

##### SAML 2.0 audit logging (hosted IdP)

Details about the IdP and SP are now added to the Access log under the `AM-ACCESS-OUTCOME` event. The entity information is logged for SAML 2.0 flows where AM is the hosted IdP and the user has successfully authenticated. These additional details let you identify the SAML 2.0 application used in an authentication attempt.

Learn more in [Access log format](https://docs.pingidentity.com/pingam/8.1/monitoring/audit-logging-ref.html#access-log-format).

##### Application authorization

To support authorization for OIDC and SAML applications within authentication journeys, the following features have been introduced:

* A new Authentication resource type includes a wildcard pattern to support unique identifiers such as OAuth 2.0 client IDs or SAML entity IDs.

* A new Customer Application Policy Set that uses the resource type is now included as a default policy set.

* Two new nodes, the [Policy nodes](#policy-decision-node) and the [\[app-policy-decision-node\]](#app-policy-decision-node), let you evaluate and enforce authorization policies directly within a journey.

Find more information in [Policy sets](https://docs.pingidentity.com/pingam/8.1/am-authorization/policy-sets.html) and [Resource types](https://docs.pingidentity.com/pingam/8.1/am-authorization/resource-types.html).

##### PingDirectory support

PingDirectory is now a supported type when you're configuring an identity store.

LDIF files are also available for PingDirectory, which can be used to create the schemas required by AM.

Learn more in [Identity stores](https://docs.pingidentity.com/pingam/8.1/setup/setting-up-identity-stores.html) and [Set up directory schemas with LDIF](https://docs.pingidentity.com/pingam/8.1/installation/supported-ldifs.html).

##### Custom CTS DN for FBC installs

When you're installing AM with a file-based configuration (FBC), you can now specify a custom DN for the CTS. Previous versions supported only the default CTS DN (`ou=famrecords,ou=openam-session,ou=tokens`).

Find more information in [Additional startup properties](https://docs.pingidentity.com/pingam/8.1/installation/passive-install-fbc.html#additional-startup-properties) in the FBC installation topic.

##### Authentication node enhancements

###### PingOne nodes

A number of improvements have been made to the nodes that allow integration with PingOne.

[](#pingone_protect_initialize_node)PingOne Protect Initialize node

The following configuration properties have been added to the [PingOne Protect Initialize](https://docs.pingidentity.com/auth-node-ref/8.1/pingone/pingone-protect-initialize.html) node:

* Enable Universal Device Identification lets you tie the device payload to a non-extractable crypto key stored in the browser for content authenticity verification.

* Enable Agent Identification lets the PingOne Signals (Protect) SDK collect device attributes from the PingID Device Trust Agent.

* Timeout for Agent lets you specify the maximum time for establishing a connection with the PingID Device Trust Agent.

* Port Number for Agent lets you specify the port number to use when connecting to the PingID Device Trust Agent.

* Additional Signals SDK Initialization Options lets you pass additional signals (not included in the existing node configuration properties) to the PingOne Signals (Protect) SDK.

A number of configuration attributes that are no longer supported in PingOne Protect have been removed from this node.

###### Set Detail nodes

The [Set Success Details](https://docs.pingidentity.com/auth-node-ref/8.1/set-success-details.html), [Set Failure Details](https://docs.pingidentity.com/auth-node-ref/8.1/set-failure-details.html), and [Set Error Details](https://docs.pingidentity.com/auth-node-ref/8.1/set-error-details.html) nodes now let you set custom response headers in addition to customizing the JSON response.

###### Social Provider Handler nodes

We've made the following changes to the [Social Provider Handler node](https://docs.pingidentity.com/auth-node-ref/8.1/social-provider-handler.html):

* Added support for handling connection timeouts.

* Added the ability to specify the attribute to use to search for an existing user. This option only applies when you have an AM standalone deployment that uses an identity store other than PingDS.

  This option is also available in the [Legacy Social Provider Handler node](https://docs.pingidentity.com/auth-node-ref/8.1/legacy-social-provider-handler.html).

###### Persistent Cookie nodes

The [Persistent Cookie Decision](https://docs.pingidentity.com/auth-node-ref/8.1/persistent-cookie-decision.html) and [Set Persistent Cookie](https://docs.pingidentity.com/auth-node-ref/8.1/set-persistent-cookie.html) nodes now include support for configuring the `SameSite` attribute for persistent cookies.

###### Device Binding nodes

The [Device Binding](https://docs.pingidentity.com/auth-node-ref/8.1/device-binding.html) and [Device Signing Verifier](https://docs.pingidentity.com/auth-node-ref/8.1/device-signing-verifier.html) nodes now let you specify a clock skew between the client device and AM. This helps prevent binding failures caused by clocks being out of sync.

###### New node versions

This release introduces new node versions for the following nodes:

| Node                                                                                                         | Version | Description of change                                                                                                                                |
| ------------------------------------------------------------------------------------------------------------ | ------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Page node](https://docs.pingidentity.com/auth-node-ref/8.1/page.html)                                       | v2.0    | Adds support for standalone nodes within a Page node. Standalone nodes are self-contained and can be included after the final multiple outcome node. |
| [Username Collector node](https://docs.pingidentity.com/auth-node-ref/8.1/am-only/username-collector.html)   | v2.0    | Adds an option to prepopulate the username if it's available in the shared state.                                                                    |
| [Platform Username node](https://docs.pingidentity.com/auth-node-ref/8.1/platform-username.html)             | v2.0    | Adds an option to prepopulate the username if it's available in the shared state.                                                                    |
| [WebAuthn Authentication node](https://docs.pingidentity.com/auth-node-ref/8.1/webauthn-authentication.html) | v2.0    | Adds support for the WebAuthn conditional UI, also known as passkey autofill, and removes the ability to return the challenge as JavaScript.         |
| [WebAuthn Registration node](https://docs.pingidentity.com/auth-node-ref/8.1/webauthn-registration.html)     | v2.0    | Removes the ability to return the challenge as JavaScript.                                                                                           |

##### OAuth 2.0 / OIDC improvements

###### Closer alignment with PAR and JAR specifications

A new advanced server property, [`am.oauth2.request.object.restrictions.enforced`](https://docs.pingidentity.com/pingam/8.1/setup/server-advanced.html#am.oauth2.request.object.restrictions.enforced) aligns AM behavior with the following specifications:

* OAuth 2.0 Pushed Authorization Requests (PAR) ([RFC 9126](https://www.rfc-editor.org/rfc/rfc9126.html))

* OAuth 2.0 Authorization Framework: JWT-Secured Authorization Request (JAR) ([RFC 9101](https://www.rfc-editor.org/rfc/rfc9101.html#section-5.2)).

These specifications indicate the following:

* The authorization server should ignore authorize parameters outside the `request_uri`.

* When sending a JWT-Secured Authorization Request (JAR), the `request_uri` *must* be an `https` URI.

###### Allow unauthenticated user code entry at the realm level

A new setting on the OAuth2 Provider service lets you manage the device code flow configuration at the realm level.

Enabling Allow unauthenticated user code entry (under Realms > *Realm Name* > Services > OAuth2 Provider > Device Code lets users access and input a user code without first logging in during an OAuth 2.0 device code flow.

If you set the value in the global service configuration (on the Global Attributes tab) *and* in the realm service configuration (on the Device Flow tab), the realm-level setting takes precedence. If AM can't determine the realm value (for example, if the realm isn't provided in the verification URL), it uses the value set on the Global Attributes tab.

###### Map custom key IDs to secrets

You can now map custom `kid` header values for JWTs signed with the signing key to a specific secret alias.

Find more information in [Map custom key IDs to secrets](https://docs.pingidentity.com/pingam/8.1/am-oidc1/managing-jwk_uri.html#map-custom-kids).

###### Perform OAuth 2.0 client authentication with a third-party issuer

You can now configure an OAuth 2.0 client to accept a JWT from an issuer other than the client ID.

Add the alternative issuer to the [Accepted JWT Issuers](https://docs.pingidentity.com/pingam/8.1/am-oauth2/oauth2-register-client.html#accepted-jwt-issuers) list for OAuth 2.0 authentication to succeed.

###### Enable application context for OAuth 2.0 / OIDC flows

You can now access the application context for *all* OAuth 2.0 / OIDC flows through the `oauthApplication` binding by setting `Enable Application Context` in the OAuth 2.0 provider or at the client level.

Find more information in the [OAuth2 provider](https://docs.pingidentity.com/pingam/8.1/setup/services-configuration.html#enable-application-context) configuration.

###### Require `exp` claim in JWT request object

You can now enforce the inclusion of the (expiration time) `exp` claim in the request object specified at the `/oauth2/authorize` or `/oauth2/par` endpoints.

Enable the `Require exp claim in Request Object` setting in the [OAuth2 provider configuration](https://docs.pingidentity.com/pingam/8.1/setup/services-configuration.html#global-oauth-oidc).

###### Customize refresh token scopes with scope validation scripts

We've added support for dynamically adjusting the scopes granted to refresh tokens during the refresh flow.

Use a next-generation scripted scope validator to call `scopeValidatorHelper.inheritAccessTokenScopesOnRefresh()` to ensure a refresh token inherits the newly evaluated scopes granted to the access token. Previously, refresh tokens always retained their originally granted scopes.

Learn more about scope validation scripting changes in the [Scope validation API](https://docs.pingidentity.com/pingam/8.1/am-scripting/scope-validation-api.html).

###### Support for audience parameter on token exchange requests

AM now supports the `aud` (audience) parameter on token exchange requests to specify the intended audience for the issued token.

Find more information in [Token exchange](https://docs.pingidentity.com/pingam/8.1/am-oauth2/token-exchange.html).

##### Test the PingOne worker connection

You can now test the connection from AM to PingOne after you configure the worker service to verify the details. Use either the AM admin UI or the `testConnection` action on the `realm-config/services/pingOneWorkerService/workers/pingone-worker-service-name` endpoint.

Learn more in [Test the connection](https://docs.pingidentity.com/pingam/8.1/setup/services-configuration.html#test-connection).

##### CDSSO login template for PingGateway

The PingGateway agent in AM can now be configured to redirect to a specified URL when CDSSO fails. Add the new `gotoOnFailure` parameter to the existing template in Login URL Template for CDSSO.

Learn more in [Register PingGateway with AM](https://docs.pingidentity.com/pinggateway/2026/gateway-guide/preface.html#register-agent-am).

##### Secret store integration for user self-service features

User self-service features can now use a secret store for managing the keys used to sign and encrypt snapshot tokens (JWTs).

Learn more in [Create a user self-service instance](https://docs.pingidentity.com/pingam/8.1/user-self-service/configuring-uss.html#create-uss-service).

##### Support for Rich Authorization Requests (RAR)

AM 8.1.0 provides initial support for RAR, as specified in [RFC 9396: OAuth 2.0 Rich Authorization Requests](https://www.rfc-editor.org/rfc/rfc9396.html).

Learn more in [Remote consent](https://docs.pingidentity.com/pingam/8.1/am-oauth2/oauth2-remote-consent.html).

|   |                                                                                                                                                                                                                                                                                                                                             |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The interface stability for RAR support is Technology Preview. Technology previews offer access to new technology that is not yet supported in production. Technology preview features may be functionally incomplete and subject to change without notice. Find more details in [Interface stability](stability.html#interface-stability). |

### New in AM 8.0.x

#### AM 8.0.2

AM 8.0.2 is a maintenance release that introduces functional enhancements and fixes.

##### FIPS compliance

AM can be configured to run in a FIPS-approved mode of operation with Bouncy Castle FIPS keystores to comply with [FIPS 140-3](https://csrc.nist.gov/pubs/fips/140-3/final).

Find more information in [FIPS 140–3 compliance](https://docs.pingidentity.com/pingam/8/security/fips.html).

##### Private key JWT audience setting

You can now configure the audience of the private key JWT when performing social authentication using an OIDC provider.

You can find more information in the [Social identity provider client configuration](https://docs.pingidentity.com/pingam/8/am-authentication/social-idp-client-reference.html).

##### Mapping custom key IDs to secrets

You can now map custom `kid` header values for JWTs signed with the signing key to a specific secret alias.

Find more information in [Map custom key IDs to secrets](https://docs.pingidentity.com/pingam/8/am-oidc1/managing-jwk_uri.html#map-custom-kids).

##### Closer alignment with PAR and JAR specifications

A new advanced server property, [`am.oauth2.request.object.restrictions.enforced`](https://docs.pingidentity.com/pingam/8/am-reference/deployment-configuration-reference.html#am.oauth2.request.object.restrictions.enforced) aligns AM behavior with the following specifications:

* OAuth 2.0 Pushed Authorization Requests (PAR) ([RFC 9126](https://www.rfc-editor.org/rfc/rfc9126.html))

* OAuth 2.0 Authorization Framework: JWT-Secured Authorization Request (JAR) ([RFC 9101](https://www.rfc-editor.org/rfc/rfc9101.html#section-5.2)).

These specifications indicate the following:

* The authorization server should ignore authorize parameters outside the `request_uri`.

* When sending a JWT-Secured Authorization Request (JAR), the `request_uri` *must* be an `https` URI.

##### PingDirectory LDIFs

LDIF files are now available for PingDirectory, which can be used to create the schemas required by AM.

Learn more in [Set up directory schemas with LDIF](https://docs.pingidentity.com/pingam/8/installation/supported-ldifs.html).

#### AM 8.0.1

AM 8.0.1 is a maintenance release that introduces functional enhancements and fixes.

##### Ability to refresh device IDs

The Push Notification service and the Ping SDKs now support the ability to refresh device IDs in user device profiles, rather than having to delete and recreate device profiles when a device ID changes.

You can find more information in [Refresh push device IDs](https://docs.pingidentity.com/pingam/8/authentication-guide/authn-mfa-reset-devices.html#refresh-push-device-ids).

#### AM 8.0.0

AM 8.0.0 is a major release that introduces new features, functional enhancements, and fixes.

|   |                                                                                                                                                                                                                                                                                                                                                                      |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | AM 8 introduces many new features and changes, but some key changes to be aware of are:- Tomcat 10 is the only supported Tomcat version.

- Authentication modules and chains have been removed.

- Embedded DS has been removed.Make sure you review [Incompatible changes](changes.html) and [Removed](removed.html) in addition to this section before upgrading. |

##### FBC in production deployments

Previous versions of AM provided a technology preview of the file-based configuration (FBC) migration utility.

In AM 8, FBC is supported in production deployments.

Learn more in the following topics:

* [Store configuration data in JSON files](https://docs.pingidentity.com/pingam/8/install-guide/fbc.html)

* [Passive install with FBC](https://docs.pingidentity.com/pingam/8/install-guide/passive-install-fbc.html)

* [Migrate to file-based configuration](https://docs.pingidentity.com/pingam/8/upgrade-guide/migrate-to-fbc.html)

##### Node Designer

AM 8 introduces a new way to create authentication node types that can be reused and shared across journeys and deployments.

The Node Designer lets you create scripted node types that have the following benefits:

* Configurable bindings

* Access to next-generation script bindings

* Potential for less code repetition

* Easier and quicker to innovate custom node types with scripting

Learn more in [Custom scripted nodes](https://docs.pingidentity.com/pingam/8/authentication-guide/node-designer.html).

##### Dynamic client registration script

You can configure AM to run a custom script after dynamic client registration. Create a next-generation script to modify a client profile after a successful create, update, or delete operation.

Learn more in [Customize dynamic client registration](https://docs.pingidentity.com/pingam/8/oidc1-guide/dynamic-client-registration-script.html).

##### Support for DER-formatted certificates for OAuth 2.0 client authentication

AM now accepts X.509 certificates in both PEM and DER format to authenticate OAuth 2.0 clients.

Learn more in [Authenticate clients with mutual TLS](https://docs.pingidentity.com/pingam/8/oauth2-guide/client-auth-mtls.html).

##### RADIUS server configuration update

The [RADIUS server service](https://docs.pingidentity.com/pingam/8/am-reference/services-configuration.html#global-radiusserverservice) has a new configuration property that enforces the inclusion of the `Message-Authenticator` attribute in requests and responses.

Use this attribute to verify incoming RADIUS access requests to prevent spoofing.

##### IDM policy condition

Authorization policies have a new [environment condition type](https://docs.pingidentity.com/pingam/8/authorization-guide/policies-ui.html#environments) named IDM User. This condition type lets you query an IDM resource to form the basis of the policy evaluation. AM must be part of a Ping Advanced Identity Software deployment to use this environment condition.

##### Backchannel authentication

Backchannel authentication lets a third-party federation service initiate authentication with AM on behalf of a user. The federation service collects the user data and transmits this data directly to AM. AM redirects the user to complete the authentication process without having to re-enter the collected data.

Learn more in [Backchannel authentication](https://docs.pingidentity.com/pingam/8/authentication-guide/backchannel-authentication.html).

##### FIDO certification

PingAM is now a [FIDO Certified Provider](https://fidoalliance.org/certification/fido-certified-products/). PingAM has passed the FIDO Alliance's rigorous testing program and meets their requirements regarding security and interoperability with other FIDO components.

Changes to PingAM in this regard include the new WebAuthn Metadata service and enhancements to the WebAuthn nodes.

Find more information about configuring AM for FIDO in [Web authentication (WebAuthn)](https://docs.pingidentity.com/pingam/8/authentication-guide/authn-mfa-webauthn.html).

###### WebAuthn Metadata service

The WebAuthn Metadata service lets you configure how AM obtains FIDO2 metadata at the journey level.

Use the WebAuthn Registration node's FIDO Certification Level setting to force AM to check the metadata service for the device's accepted certification level.

Learn more in [WebAuthn Metadata service](https://docs.pingidentity.com/pingam/8/reference/services-configuration.html#webauthn-metadata-service).

###### WebAuthn nodes

The following improvements have been made to the WebAuthn nodes:

* [WebAuthn Authentication node](https://docs.pingidentity.com/auth-node-ref/8.1/webauthn-authentication.html)

  * On successful authentication, the WebAuthn Authentication node now adds a `webauthnAssertionInfo` object to transient state that stores [authenticator data](https://www.w3.org/TR/webauthn-1/#sec-authenticator-data).

  * A new node setting, Detect sign count mismatch, lets you compare the authenticator's sign count ([signature counter](https://www.w3.org/TR/webauthn-2/#signcount)) with the sign count stored in the user's profile.

    The sign count is useful for detecting potentially cloned devices.

    If the authenticator sign count is less than or equal to the stored value, evaluation continues to the new `Sign Count Mismatch` outcome.

* [WebAuthn Registration node](https://docs.pingidentity.com/auth-node-ref/8.1/webauthn-registration.html)

  * On successful registration, the WebAuthn Registration node now adds the following objects to transient state:

    * `webauthnAttestationInfo`: Stores [authenticator data](https://www.w3.org/TR/webauthn-1/#sec-authenticator-data).

    * `webauthnDeviceAaguid`: Stores the Authenticator Attestation Global Unique Identifier (AAGUID).

  * The new FIDO Certification Level setting lets you use the configured WebAuthn Metadata service to check the device's FIDO certification level meets a minimum level requirement during registration.

###### Device profile settings

The following attributes are now stored in device profiles:

* WebAuthn device profile

  * `signCount` The device sign count (signature counter).

- Push / WebAuthn / Oath device profiles

  * `createdDate`: The date the device was registered and the profile created.

  * `lastAccessDate`: The date the device was last used to sign in successfully.

##### Ability to trace the request flow through Ping Advanced Identity Software

When a user interacts with Ping Advanced Identity Software, the request can travel through multiple services before it completes. *Distributed tracing* lets you monitor the request flow through Ping Advanced Identity Software.

Tracing provides a single view of a request's journey and makes it easier to locate bottlenecks and errors.

Learn more in [Trace incoming and outgoing requests](https://docs.pingidentity.com/pingam/8/maintenance-guide/trace-requests.html).

##### Improved REST API for transactional authorization

For [transactional authorization](https://docs.pingidentity.com/pingam/8/authorization-guide/transactional-authorization.html) requests, you can now provide an `authIndexType` of `transaction` and an `authIndexValue` of `transactionId` to the `authenticate` endpoint. This new parameter lets you complete transactional authorization without sending URL-encoded XML over REST.

For example:

```bash
curl \
--cookie "iPlanetDirectoryPro=sso-cookie" \
--request POST \
--header "Content-Type: application/json" \
--header "Accept-API-Version: resource=2.0, protocol=1.0" \
'https://am.example.com:8443/am/json/realms/root/authenticate?authIndexType=transaction&authIndexValue=transactionId'
```

The behavior of the new parameter is identical to the existing parameter:

```bash
…​/authenticate?authIndexType=composite_advice&authIndexValue=URL-encoded-XML,
```

The existing parameter remains supported.

##### Certificate Collector node supports DER certificates

For certificates supplied in HTTP headers, the [Certificate Collector node](https://docs.pingidentity.com/auth-node-ref/8.1/certificate-collector.html) now supports certificates in DER format in addition to PEM format. There are no configuration changes in the node itself.

The certificate format is inferred from the encoded certificate contents. The supported DER format encoding is compliant with [RFC 9440](https://www.rfc-editor.org/rfc/rfc9440.html#name-encoding).

##### OAuth 2.0 application journeys

You can now associate an OAuth 2.0 client with a specific authentication journey (tree). The associated journey is always run, regardless of existing sessions or configured authentication context class reference (`acr`) values.

You can only associate a tree with OAuth 2.0 applications configured for the `Authorization Code`, `Implicit`, and `Device Code` grant types.

To access information about the incoming OAuth 2.0 request, configure your tree to include a [Scripted Decision node](https://docs.pingidentity.com/auth-node-ref/8.1/scripted-decision.html) that queries the [`oauthApplication`](https://docs.pingidentity.com/pingam/8/scripting-guide/scripting-api-node.html#oauthapp-binding) script binding.

Learn more in [client application registration](https://docs.pingidentity.com/pingam/8/oauth2-guide/oauth2-register-client.html#oauth2-config-treename).

##### SAML 2.0 application journeys

Configure the remote SP so that a specific authentication journey (tree) is always run for users authenticating with your SAML 2.0 app. The federation flow invokes the associated journey regardless of any existing sessions or configured authentication context.

You can access the requested authentication context and configured mappings by including a [Scripted Decision node](https://docs.pingidentity.com/auth-node-ref/8.1/scripted-decision.html) in the journey that queries the new [`samlApplication` script binding](https://docs.pingidentity.com/pingam/8/scripting-guide/scripting-api-node.html#samlapp-binding).

Learn more in [Configure a SAML 2.0 application journey](https://docs.pingidentity.com/pingam/8/saml2-guide/saml2-providers-and-cots.html#samlapp-tree).

Additionally, details about the SAML v2.0 app tree flow are added to the [Access log](https://docs.pingidentity.com/pingam/8/security-guide/sec-maint-audit-ref.html#access-log-format) under the `AM-ACCESS-OUTCOME` event.

##### Customize SAML NameID mapping with a script

You can now use a script to customize the NameID attribute in the SAML 2.0 assertion per SP. Create a next-generation script of type `Saml2 NameID Mapper` and configure the remote SP entity to use the custom script.

You can find more information in [NameID mapper](https://docs.pingidentity.com/pingam/8/saml2-guide/custom-nameid-mapper.html).

##### Http Client service

The new Http Client service lets you create named instances that you can reference from a next-generation script using [the `httpclient` binding](https://docs.pingidentity.com/pingam/8/scripting-guide/script-bindings.html#httpclient-mtls).

On each instance, define secret labels that map to certificates in secret stores and are used during mTLS connections.

The service also provides settings to override connection and response timeouts for HTTP requests and to configure certificate checks per instance.

Learn more in [Http Client service](https://docs.pingidentity.com/pingam/8/reference/services-configuration.html#global-httpclient).

##### Default trees

The following new default trees have been added to AM:

* `ldapService`: replaces the `ldapService` authentication chain.

* `Agent`: replaces the `Application` module.

* `amsterService`: replaces the `amsterService` authentication chain.

These trees provide direct replacements for the corresponding default modules and chains. This ensures any authentication processes that rely on them are unaffected by the [removal](changes-8.0.html#modules-and-chains) of modules and chains in this release.

Learn more about these trees in [Default trees](https://docs.pingidentity.com/pingam/8/authentication-guide/authn-introduction-authn.html#default-trees).

##### Configure trees to run to completion

Set the `mustRun` property to force trees to always run to completion regardless of the existing user sessions.

Learn more in [Configure an authentication tree to always complete](https://docs.pingidentity.com/pingam/8/authentication-guide/configure-authentication-trees.html#enable-tree-completion).

##### Configure no session trees

Set the `noSession` property to create trees that don't result in an authenticated session when they successfully complete.

Learn more in [Configure a no session tree](https://docs.pingidentity.com/pingam/8/authentication-guide/configure-authentication-trees.html#configure-nosession-tree).

##### Session duration and timeout control

We've made changes to AM to provide greater control over journey session duration and authenticated session timeouts.

* Journey session duration

  You can now override global and realm level duration values in a tree or a node:

  * For the maximum duration, you can override timeout settings using the new [Update Journey Timeout node](https://docs.pingidentity.com/auth-node-ref/8.1/update-journey-timeout.html) or by setting the `treeTimeout` property in the [tree configuration](https://docs.pingidentity.com/pingam/8/authentication-guide/configure-authentication-trees.html#configure-journey-session-duration-tree).

  * For the suspended duration, you can override the suspended duration in the [Email Suspend node](https://docs.pingidentity.com/auth-node-ref/8.1/email-suspend.html) or in a Scripted Decision node using the `action` object. Learn more in [Suspend and resume journeys](https://docs.pingidentity.com/pingam/8/scripting-guide/scripting-api-node.html#scripting-api-node-suspend).

  Find out how AM derives the journey session duration as a result of these changes in [Configure suspended authentication](https://docs.pingidentity.com/pingam/8/authentication-guide/authn-suspended.html#configure-suspended-auth).

* Authenticated session timeouts

  You can now override global and realm level timeout settings (`maximum session time` and `maximum idle time`) in a tree or a node.

  * In nodes, you can override the session timeouts in the [Set Session Properties node](https://docs.pingidentity.com/auth-node-ref/8.1/set-session-properties.html) or in a Scripted Decision node using the `withMaxIdleTime` and `withMaxSessionTime` methods. Learn more in [Set authenticated session timeouts](https://docs.pingidentity.com/pingam/8/scripting-guide/scripting-api-node.html#scripting-api-node-session-timeouts).

  * In a tree, you can override the session timeouts by setting the `maximumSessionTime` and `maximumIdleTime` properties in the [tree configuration](https://docs.pingidentity.com/pingam/8/authentication-guide/configure-authentication-trees.html#configure-auth-session-timeouts-tree).

  Find out how AM derives the authenticated session timeouts as a result of these changes in [Configure authenticated session timeout settings](https://docs.pingidentity.com/pingam/8/sessions-guide/session-state-session-termination.html#auth-session-termination-config).

##### LINE login support

You can now configure a social provider authentication with LINE login. There are two new social provider configuration profiles, LINE (Browser) and LINE (Native), for browser and mobile app integrations.

The LINE (Browser) integration must not reference a well-known endpoint to ensure AM verifies signatures using the client secret instead.

##### Next-generation script bindings

The following next-generation script bindings have been improved for this release:

###### Common bindings

* `cookieName`: Access the name of the cookie as a string to perform session actions such as ending all sessions for a user.

* `httpClient`:

  * Use the new `form` attribute to send url-encoded form requests.

  * Reference an instance of the new [Http Client service](#new-httpclient-service) to enable mTLS connections to external services.

* `policy`: Lets you access the policy engine API and evaluate policies from within scripts.

* `secrets`: Reference secrets and credentials stored in secret stores.

* `utils`: Use this new utility binding to perform functions such as:

  * Base64 encode/decode strings

  * Generate random values and UUIDs

  * Encrypt and decrypt values

  * Compute hash values

  * Sign and verify data

|   |                                                                                                                                                                                                                                                                                                                                                                                            |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | Make sure you don't use the same name for a local variable as that of a common binding in your script. These names are reserved for common bindings only.If you have already defined a local variable with the same name as one that's added to common bindings in a more recent version of PingAM; for example, `utils`, you must rename the variable in your scripts before you upgrade. |

Learn more in [Script bindings](https://docs.pingidentity.com/pingam/8/scripting-guide/script-bindings.html).

###### Scripted decision node bindings

* `action`:

  * Use the new `suspend(String message)` and `suspend(String message, SuspensionLogic logic)` methods to suspend the current authentication session and send a message to the user.

    You can also implement custom logic with the resume URI, for example, to send an email or SMS using the HTTP client service.

  * You can now access the following methods through the ActionWrapper object to return additional information to the client:

    * `withHeader(String header)`

    * `withDescription(String description)`

    * `withStage(String stage)`

* `jwtAssertion` and `jwtValuation`:

  * You can now generate JWT assertions with custom non-registered claims.

  * Data fields are more aligned with the JWT specification, so you can now specify separate values for `issuer` and `subject`. These replace the existing `accountId`.

  * The bindings work with `RS256` or `HS256` signed JWTs, and JWTs that are encrypted using the A128CBC-HS256 algorithm.

* `nodeState`: You can now merge data, including `objectAttributes` values, into existing state with the new `mergeShared` and `mergeTransient` methods.

* `oauthApplication`: Access request and application information if the node is part of a journey associated with an OAuth 2.0 client application.

* `requestCookies`: Use this new decision node script binding to access request cookies directly.

* `samlApplication`: Access request and application information if the node is part of a journey associated with a SAML 2.0 client application.

Learn more in the [Scripted Decision node API](https://docs.pingidentity.com/pingam/8/scripting-guide/scripting-api-node.html).

###### Library scripts

Library scripts now have access to all common bindings.

Learn more in [Library scripts](https://docs.pingidentity.com/pingam/8/scripting-guide/library-scripts.html).

###### Next-generation script types

The following existing script types are now enabled for the next-generation script engine:

* [Configuration Provider node](https://docs.pingidentity.com/auth-node-ref/8.1/config-provider.html) scripts

* [Device Match node](https://docs.pingidentity.com/auth-node-ref/8.1/device-match.html) scripts

* [Policy condition](https://docs.pingidentity.com/pingam/8/scripting-guide/policy-condition-scripting-api.html) scripts

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | [Scripted Decision node](https://docs.pingidentity.com/auth-node-ref/8.1/scripted-decision.html) and [Device Match node](https://docs.pingidentity.com/auth-node-ref/8.1/device-match.html) scripts now have different context types depending on the script engine. For legacy scripts, the context is `AUTHENTICATION_TREE_DECISION_NODE`, and for next-generation scripts, the contexts are `SCRIPTED_DECISION_NODE` and `DEVICE_MATCH_NODE` respectively. |

###### Access PingOne Verify transaction data

The `verifyTransactionsHelper` next-generation binding lets you manage [PingOne Verify](https://www.pingidentity.com/en/platform/capabilities/identity-verification/pingone-verify.html) user transactions and PingOne user accounts.

Learn more in [Access PingOne Verify transactions and manage associated user](https://docs.pingidentity.com/pingam/8/scripting-guide/script-bindings.html#common-verifytransactionshelper)

##### Enable Device Management node

The [Enable Device Management node](https://docs.pingidentity.com/auth-node-ref/8.1/enable-device-management.html) lets you relax or remove restrictions placed upon users who want to reset or remove registered MFA devices.

Use this node in a journey to change the authentication strategy required for removing registered devices.

##### Flow Control node

The [Flow Control node](https://docs.pingidentity.com/auth-node-ref/8.1/flow-control.html) lets you control the authentication flow by randomly sending traffic down different paths of a tree (journey). This means you can use the node to evaluate changes before rolling them out to a production environment.

For example, configure the node to direct a percentage of requests to a new authentication journey to observe the user experience and check for potential failures.

##### Customize the JSON in the authentication response

The following nodes are new for this release.

###### Set Success Details node

The [Set Success Details node](https://docs.pingidentity.com/auth-node-ref/8.1/set-success-details.html) lets you add details to the JSON response on successful authentication.

You can add either or both of the following:

* Success Details: Lets you add static `key:value` fields to the JSON response.

* Session Properties: Lets you add `key:value` fields to the JSON response, where `value` corresponds to the value of the specified session property.

###### Set Failure Details node

The [Set Failure Details node](https://docs.pingidentity.com/auth-node-ref/8.1/set-failure-details.html) lets you add details to the JSON response on authentication failure.

You can add either or both of the following:

* Failure Message: Lets you add a custom, localized message to display to the user and return in the JSON response.

* Failure Details: Lets you add `key:value` fields to the JSON response.

###### Set Error Details node

The [Set Error Details node](https://docs.pingidentity.com/auth-node-ref/8.1/set-error-details.html) lets you add details to the JSON response when a journey ends in an error.

You can add either or both of the following:

* Error Message: Lets you add a custom, localized message to display to the user and return in the JSON response.

* Error Details: Lets you add `key:value` fields to the JSON response.

##### Configurable clock skew for OIDC ID token expiry time

The [org.forgerock.openam.oauth2.tokenexpiry.skewAllowance](https://docs.pingidentity.com/pingam/8/reference/deployment-configuration-reference.html#org.forgerock.openam.oauth2.tokenexpiry.skewAllowance) advanced server property lets you configure the period, in seconds, during which an OIDC ID token remains valid *after* its expiry time.

This property allows for clock skews between servers.

In previous releases, the clock skew for ID token expiry times was hard coded to 5 minutes. For compatibility purposes, this is the default value of the new property.

##### Update signing certificate in remote SP metadata

You can now update the signing or encryption certificate for an existing SP without needing to delete and recreate the entire SP configuration.

Learn more in [Update remote SP certificate](https://docs.pingidentity.com/pingam/8/saml2-guide/saml2-providers-and-cots.html#update-metadata).

##### Configure client certificate in SP metadata

You can now configure the hosted SP to exclude the client certificate from metadata.

To override the default behavior, enable the Exclude Client Certificate from Metadata option in the SP's [configuration](https://docs.pingidentity.com/pingam/8/saml2-guide/saml2-reference.html#sp-hosted-client-auth).

##### Changes to refresh tokens

###### Consistent errors when refreshing tokens

The following new methods ensure consistent error messages when refreshing tokens:

* `com.sun.identity.idm.IdRepoListener`

  * `objectChanged(String name, String previous, IdType idType, int changeType, Map cMap)`

* `com.sun.identity.idm.IdEventListener`

  * `identityRenamed(String universalId, String previousUniversalId)`

If a token is refreshed but the username has changed since the original refresh token was issued, the following error is now shown with these methods:

```json
{
   "error_description" : "grant is invalid",
   "error" : "invalid_grant"
}
```

###### Refresh token grace period

The refresh token grace period now applies to client-side refresh tokens as well as server-side refresh tokens. You define the grace period in the OAuth 2.0 provider configuration in a realm and can override it for specific OAuth 2.0 clients.

Before this release, an OAuth 2.0 client could have a grace period of `0` (the default), which would mean that the grace period would be inherited from the OAuth 2.0 provider. That inherited value had no effect on client-side refresh tokens, however. From this release, client-side tokens inherit the refresh token grace period set on the OAuth 2.0 provider if no specific grace period is set in the client configuration.

##### Configuration Provider node

The following improvements have been made to the [Configuration Provider node](https://docs.pingidentity.com/auth-node-ref/8.1/config-provider.html):

* Previously, you could only use the Configuration Provider node to imitate nodes with fixed outcomes. Now, you can also imitate nodes with variable outcomes from a predefined list.

  This change makes the following nodes available to the Configuration Provider node:

  * [MFA Registration Options node](https://docs.pingidentity.com/auth-node-ref/8.1/mfa-registration-options.html)

  * [OATH Token Verifier node](https://docs.pingidentity.com/auth-node-ref/8.1/oath-token-verifier.html)

  * [Polling Wait node](https://docs.pingidentity.com/auth-node-ref/8.1/polling-wait.html)

  * [Push Sender node](https://docs.pingidentity.com/auth-node-ref/8.1/push-sender.html)

  * [Select Identity Provider node](https://docs.pingidentity.com/auth-node-ref/8.1/select-identity-provider.html)

  * [WebAuthn Authentication node](https://docs.pingidentity.com/auth-node-ref/8.1/webauthn-authentication.html)

  * [WebAuthn Device Storage node](https://docs.pingidentity.com/auth-node-ref/8.1/webauthn-device-storage.html)

  * [WebAuthn Registration node](https://docs.pingidentity.com/auth-node-ref/8.1/webauthn-registration.html)

  To ensure custom nodes are available to the Configuration Provider node, write an outcome provider class that implements the `StaticOutcomeProvider` or `BoundedOutcomeProvider` interfaces.

* The following nodes with fixed outcomes are also now available to the Configuration Provider node:

  * [Enable Device Management node](https://docs.pingidentity.com/auth-node-ref/8.1/enable-device-management.html)

  * [Identity Assertion node](https://docs.pingidentity.com/auth-node-ref/8.1/identity-assertion-node.html)

  * [Push Wait node](https://docs.pingidentity.com/auth-node-ref/8.1/push-wait.html)

* You can now generate configuration provider template scripts with default values.

  Call the node API endpoint with the `configProviderScript` action to generate a JavaScript or Groovy script for the type of node you want to imitate.

  Learn more in the [Configuration Provider node](https://docs.pingidentity.com/auth-node-ref/8.1/config-provider.html).

##### Backchannel logout token contains `exp` claim

The logout token generated during backchannel logout now contains an `exp` claim.

Learn more in [Backchannel logout](https://docs.pingidentity.com/pingam/8/oidc1-guide/backchannel-logout.html).

##### New `ssoadm` commands update attributes in a realm service

A fix to the deprecated `ssoadm` tool adds the following new commands:

* `add-realm-default-attributes`

* `set-realm-default-attributtes`

* `remove-realm-default-attributes`

* `get-realm-default-attributes`

These commands work on realm defaults from AM 7 onwards.

##### System property for social provider `sub` claim uniqueness

A new system property (`org.forgerock.openam.oidc.SocialProvider.sub.claim.is.not.unique`) indicates that the OIDC social provider doesn't return a unique value for the `sub` claim.

This is false by default.

### New in AM 7.5.x

#### AM 7.5.2

There are no new features in AM or Amster 7.5.2, only bug fixes.

#### AM 7.5.1

AM 7.5.1 is a maintenance release that introduces functional enhancements and fixes.

##### New utility script binding

Use the `utils` binding to base64 encode/decode strings and generate random values and UUIDs in your next-generation scripts.

Learn more in [Script bindings](https://docs.pingidentity.com/pingam/7.5/scripting-guide/script-bindings.html).

##### Backchannel logout token contains `exp` claim

The logout token generated during backchannel logout now contains an `exp` claim. Learn more in [Backchannel logout](https://docs.pingidentity.com/pingam/7.5/oidc1-guide/backchannel-logout.html).

##### System property for social provider `sub` claim uniqueness

A new system property (`org.forgerock.openam.oidc.SocialProvider.sub.claim.is.not.unique`) indicates that the OIDC social provider doesn't return a unique value for the `sub` claim.

This is false by default.

##### New `ssoadm` commands update attributes in a realm service

A fix to the deprecated `ssoadm` tool adds the following new commands:

* `add-realm-default-attributes`

* `set-realm-default-attributtes`

* `remove-realm-default-attributes`

* `get-realm-default-attributes`

These commands work on realm defaults from AM 7 onwards.

#### AM 7.5.0

AM 7.5.0 is a minor release that introduces new features, functional enhancements, and fixes.

##### Support for storing secrets in secret stores

The following features now support storing their secrets in a [secret store](https://docs.pingidentity.com/pingam/7.5/security-guide/secret-stores.html) instead of in the configuration. For greater security, move these secrets to a secret store when convenient.

* Services

  * [PUSH notification service](https://docs.pingidentity.com/pingam/7.5/reference/global-services-configuration.html#global-pushnotification)

  * [Prometheus monitoring service](https://docs.pingidentity.com/pingam/7.5/maintenance-guide/monitoring-prometheus.html)

  * [Social provider service](https://docs.pingidentity.com/pingam/7.5/authentication-guide/social-idp-client-reference.html)

  * [Email service](https://docs.pingidentity.com/pingam/7.5/reference/global-services-configuration.html#global-email)

  * [Device Binding service](https://docs.pingidentity.com/pingam/7.5/reference/global-services-configuration.html#global-devicebindingservice)

  * [Device ID service](https://docs.pingidentity.com/pingam/7.5/reference/global-services-configuration.html#global-deviceidservice)

  * [Device Profiles service](https://docs.pingidentity.com/pingam/7.5/reference/global-services-configuration.html#global-deviceprofilesservice)

  * [OATH service](https://docs.pingidentity.com/pingam/7.5/reference/global-services-configuration.html#global-authenticatoroathservice)

  * [Push service](https://docs.pingidentity.com/pingam/7.5/reference/global-services-configuration.html#global-authenticatorpushservice)

  * [WebAuthn service](https://docs.pingidentity.com/pingam/7.5/reference/global-services-configuration.html#global-authenticatorwebauthnservice)

* Authentication nodes

  * [CAPTCHA node](https://docs.pingidentity.com/auth-node-ref/8.1/captcha.html)

  * [OIDC ID Token Validator](https://docs.pingidentity.com/auth-node-ref/8.1/oidc-idtoken-validator.html)

  * [OTP Email Sender node](https://docs.pingidentity.com/auth-node-ref/8.1/otp-email-sender.html) and [OTP SMS Sender node](https://docs.pingidentity.com/auth-node-ref/8.1/otp-sms-sender.html)

  * [Persistent Cookie Decision node](https://docs.pingidentity.com/auth-node-ref/8.1/persistent-cookie-decision.html) and [Set Persistent Cookie node](https://docs.pingidentity.com/auth-node-ref/8.1/set-persistent-cookie.html) signing and encryption

  * [Custom authentication node](https://docs.pingidentity.com/pingam/7.5/auth-nodes/core-config.html#the_attribute_annotation)

* Agents

  * [PingGateway](https://docs.pingidentity.com/pinggateway/2026)

  * [Web agents](https://docs.pingidentity.com/web-agents/2025.11)

  * [Java agents](https://docs.pingidentity.com/java-agents/2025.11)

* Authentication

  * [Authentication signing secret](https://docs.pingidentity.com/pingam/7.5/authentication-guide/authn-core-settings.html#authentication-signing-secret)

  * AM password encryption key

  * HTTP outbound request authentication password (advanced server setting)

  * Password capture and replay

  * Client-side sessions:

    * The HMAC signing key

    * The `am.global.services.session.clientbased.signing` mapping is deprecated and replaced by [algorithm-specific mappings](https://docs.pingidentity.com/pingam/7.5/security-guide/secret-mapping.html#general-default-secret-labels)

    * The `am.global.services.session.clientbased.encryption` mapping is deprecated and replaced by `am.global.services.session.clientbased.encryption.RSA` and `am.global.services.session.clientbased.encryption.AES`

* SAML v2.0

  * Remote SP and IDP basic authentication for SOAP-based binding

  * SP authentication with mTLS for artifact resolve requests

* OAuth 2.0

  * OAuth 2.0 client authentication secrets

  * OAuth 2.0 client mTLS self-signed certificate

  * OAuth 2.0 client ID token public encryption key

  * OAuth 2.0 client JWT bearer public key

  * OAuth 2.0 provider salting of hashes

In addition, you can now rotate secrets in file system secret volumes.

Learn more in [Map and rotate secrets](https://docs.pingidentity.com/pingam/7.5/security-guide/secret-mapping.html).

##### Support for mTLS connections

The following services now support certificate-based connections to the backend LDAP store using mTLS:

* [Certificate Validation node](https://docs.pingidentity.com/auth-node-ref/8.1/certificate-validation.html)

* [Certificate revocation list caching](https://docs.pingidentity.com/pingam/7.5/reference/deployment-configuration-reference.html#security-revocation)

##### Configurable affinity for connections to the DS identity repository

The DS identity repository configuration now includes an [Affinity Level](https://docs.pingidentity.com/pingam/7.5/setup-guide/data-stores-opendj.html#affinity-level) setting that lets you specify the operations for which AM should use affinity-based load balancing.

In previous AM releases, you configured affinity only with the Affinity Enabled property, so it was either *on* or *off*. With Affinity Enabled set to `true`, `ALL` operations to the DS repository used affinity. With Affinity Enabled set to `false`, the equivalent affinity level was `NONE` (no operations used affinity).

The new setting introduces the `BIND` level as a middle ground. When you set the affinity level to `BIND`, only user authentication requests use affinity. This setting provides a small but significant performance improvement in deployments with multiple replicated DS identity stores.

In addition, the [LDAP Decision node](https://docs.pingidentity.com/auth-node-ref/8.1/ldap-decision.html) has been updated with a new property, `affinityLevel` (`NONE`, `BIND`, and `ALL`). This is separate to the configuration setting.

|   |                                                                                                                                                                                                                                                                                    |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The [Data Store Decision node](https://docs.pingidentity.com/auth-node-ref/8.1/data-store-decision.html) uses the identity repository configuration. As such, affinity settings configured for the identity repository will impact connections to the DS server made by this node. |

##### Request Header node

The new Request Header node lets customers inject values into shared state based on request header values. You can use the node to get information about a journey or the user from an external system or even customize the branding of a journey.

Learn more in [Request Header node](https://docs.pingidentity.com/auth-node-ref/8.1/request-header.html).

##### Scalable OAuth 2.0 clients

The scalable OAuth 2.0 clients feature lets you create and manage large numbers of OAuth 2.0 clients without impacting system performance. Once you have enabled the feature, create clients as usual through dynamic registration or in the AM admin UI, and then use the AM administration OAuth 2.0 client REST endpoint to search for clients and filter and page query results.

Learn more in [Scalable OAuth 2.0 clients](https://docs.pingidentity.com/pingam/7.5/oauth2-guide/rest-api-oauth2-client-admin-endpoint.html#scalable-clients).

##### SAML v2.0 NameID mapping configurable on the service provider (SP)

You can now configure NameID mapping on a remote SP. The SP configuration overrides the NameID Value Map on the IDP, letting you define different name requirements for each SP.

Learn more about NameID value mapping in the [Remote service provider configuration properties](https://docs.pingidentity.com/pingam/7.5/saml2-guide/saml2-reference.html#saml2-remote-sp-configuration).

##### Use a tree hook to run actions on journey failure

Override the new `acceptFailure` method to run actions on journey failure.

Learn more about the `TreeHook` interface in the [Public API Javadoc](https://docs.pingidentity.com/pingam/7.5/_attachments/apidocs/org/forgerock/openam/auth/node/api/TreeHook.html).

##### Storing identified identities in the authentication session

The following new methods let you record users and agents verified to exist in an identity store:

* `org.forgerock.openam.auth.node.api.Action`

  * `public ActionBuilder withIdentifiedIdentity(AMIdentity id)`

  * `public ActionBuilder withIdentifiedIdentity(String username, IdType id)`

* `org.forgerock.openam.auth.nodes.script.ActionWrapper`

  * `public ActionWrapper withIdentifiedAgent(String agentName)`

  * `public ActionWrapper withIdentifiedUser(String username)`

A new advanced server property, `org.forgerock.am.auth.trees.authenticate.identified.identity` determines whether AM uses these stored identified identities when deciding which user to log in.

This lets custom nodes and decision node scripts correctly resolve identities that have the same username. For more information, refer to [advanced server properties](https://docs.pingidentity.com/pingam/7.5/reference/deployment-configuration-reference.html#org.forgerock.am.auth.trees.authenticate.identified.identity).

##### Identity Assertion node and Identity Assertion service

The new Identity Assertion node and supporting service lets AM use PingGateway to manage authentication through a third party such as Windows Desktop SSO or Kerberos.

Learn more in [Identity Assertion node](https://docs.pingidentity.com/auth-node-ref/8.1/identity-assertion-node.html) and [Identity Assertion service](https://docs.pingidentity.com/pingam/7.5/reference/global-services-configuration.html#global-identity-assertion).

##### PingOne Protect nodes and PingOne Worker service

The new PingOne Protect nodes and supporting PingOne Worker service let you integrate with PingOne Protect. Leverage risk predictors and route your journeys based on calculated risk scores.

You can add these nodes to your authentication, registration, and self-service journeys to combat account takeover, new account fraud, and MFA fatigue.

Learn more:

* [PingOne Protect Evaluation node](https://docs.pingidentity.com/auth-node-ref/8.1/pingone/pingone-protect-evaluation.html)

* [PingOne Protect Initialization node](https://docs.pingidentity.com/auth-node-ref/8.1/pingone/pingone-protect-initialize.html)

* [PingOne Protect Result node](https://docs.pingidentity.com/auth-node-ref/8.1/pingone/pingone-protect-result.html)

* [PingOne Worker service](https://docs.pingidentity.com/pingam/7.5/reference/global-services-configuration.html#realm-pingone-worker-service)

##### Nodes in a Page node log individual audit events

Nodes contained in a Page node now log individual `AM-NODE-LOGIN-COMPLETED` audit events.

Learn more about audit logging in [Audit log events](https://docs.pingidentity.com/pingam/7.5/security-guide/sec-maint-audit-ref.html#audit-log-event-names).

### New in AM 7.4.x

#### AM 7.4.2

AM 7.4.2 is a minor release that introduces new features, functional enhancements, and fixes.

##### Backchannel logout token contains `exp` claim

The logout token generated during backchannel logout now contains an `exp` claim.

Learn more in [Backchannel logout](https://docs.pingidentity.com/pingam/7.4/oidc1-guide/backchannel-logout.html).

##### New `ssoadm` commands update attributes in a realm service

A fix to the deprecated `ssoadm` tool adds the following new commands:

* `add-realm-default-attributes`

* `set-realm-default-attributtes`

* `remove-realm-default-attributes`

* `get-realm-default-attributes`

These commands work on realm defaults from AM 7 onwards.

##### System property for social provider `sub` claim uniqueness

A new system property (`org.forgerock.openam.oidc.SocialProvider.sub.claim.is.not.unique`) indicates that the OIDC social provider doesn't return a unique value for the `sub` claim.

This is false by default.

##### Improvements to JWT operations in scripts

The `jwtAssertion` and `jwtValidator` script bindings now let you include non-registered claims.

The values that you can specify to generate and validate JWTs have been updated to include new fields such as `issuer` and `subject`. These replace the existing `accountId` to let you specify different values for these fields.

The bindings work with `RS256` or `HS256` signed JWTs, and JWTs that are encrypted using the A128CBC-HS256 algorithm.

Learn more in [Generate and validate JWTs](https://docs.pingidentity.com/pingam/7.4/scripting-guide/scripting-api-node.html#jwt-support).

#### AM 7.4.1

AM 7.4.1 is a maintenance release.

##### Storing identified identities in the authentication session

The following new methods let you record users and agents verified to exist in an identity store:

* `org.forgerock.openam.auth.node.api.Action`

  * `public ActionBuilder withIdentifiedIdentity(AMIdentity id)`

  * `public ActionBuilder withIdentifiedIdentity(String username, IdType id)`

* `org.forgerock.openam.auth.nodes.script.ActionWrapper`

  * `public ActionWrapper withIdentifiedAgent(String agentName)`

  * `public ActionWrapper withIdentifiedUser(String username)`

A new advanced server property, `org.forgerock.am.auth.trees.authenticate.identified.identity` determines whether AM uses these stored identified identities when deciding which user to log in.

This lets custom nodes and decision node scripts correctly resolve identities that have the same username.

#### AM 7.4.0

AM 7.4.0 is a minor release that introduces new features, functional enhancements, and fixes.

##### Bind and verify user devices

The ForgeRock SDKs for Android and iOS can cryptographically bind a mobile device to a user account.

Registered devices generate a key pair and a key ID. The SDK sends the *public* key and key ID to your AM server for storage in the user's profile.

The SDK stores the private key on the device in the Android KeyStore or the iOS Secure Enclave. Access to the private keys is protected by biometric security or a PIN.

A user can bind multiple devices to their account, and each device can bind to multiple users.

After binding a device, your authentication journeys can verify ownership of the bound device by requesting that it signs a challenge using its private key, and verifying it corresponds to the public key.

For details, refer to the [Device Binding node](https://docs.pingidentity.com/auth-node-ref/8.1/device-binding.html), [Device Binding Storage node](https://docs.pingidentity.com/auth-node-ref/8.1/device-binding-storage.html), and [Device Signing Verifier node](https://docs.pingidentity.com/auth-node-ref/8.1/device-signing-verifier.html).

##### Support for JSON output from `/oauth2/device/user` endpoint

REST calls to the `/oauth2/device/user` endpoint return an HTML response by default.

This release adds support for an `Accept: application/json` header that returns the response in JSON format.

For details, refer to the [Device authorization grant](https://docs.pingidentity.com/pingam/7.4/oauth2-guide/oauth2-device-flow.html).

##### Setting to disable the `subname` claim

AM adds the `subname` claim to access and ID tokens by default. You can now change this behavior by disabling the OAuth2 Provider service property, [Include subname claim in tokens issued by the OAuth2 Provider](https://docs.pingidentity.com/pingam/7.4/reference/global-services-configuration.html#include-subname-claim-in-tokens-issued-by-the-oauth-2-provider).

The value of the `subname` claim matches the value of the `sub` claim used in versions of AM earlier than 7.1. It also matches the value of the `sub` claim if you disable the `org.forgerock.security.oauth2.enforce.sub.claim.uniqueness` property.

##### Setting to permit client credentials in token endpoint query parameters

The OAuth 2.0 Provider service includes a new advanced property, [Allow Client Credentials in Token Endpoint Query Parameters](https://docs.pingidentity.com/pingam/7.4/reference/global-services-configuration.html#allow-client-credentials-in-token-endpoint-query-parameters), that lets you include client credentials as query parameters in OAuth 2.0 token endpoint requests.

In previous AM versions, you could supply client credentials (the `client_id` and `client_secret`) as query parameters in POST requests to the `/oauth2/access_token` endpoint. From AM 7.4 onwards, this is prohibited by default and you must include the credentials within the POST request body.

The new Allow Client Credentials in Token Endpoint Query Parameters setting controls this behavior and is `false` by default in new deployments. For security reasons, keep this property disabled to prevent client credentials from being included as query parameters.

When you upgrade an existing deployment to AM 7.4, this property is initially set to `true` for legacy support. After upgrading, you should update your scripts and clients to support the new behavior then set the property to `false`.

##### Restriction of access to inner trees

The new `innerTreeOnly` property of an authentication tree lets you specify that the tree is *only* an inner tree and can't be accessed directly.

For details, refer to [Disable direct access through an inner tree](https://docs.pingidentity.com/pingam/7.4/authentication-guide/about-authentication-trees.html#disable-inner-tree).

##### New `nodeState.getObject` method

The new `nodeState.getObject(String key)` method lets scripted decision nodes retrieve variables stored in both shared and secure state.

For details, refer to [Access shared state data](https://docs.pingidentity.com/pingam/7.4/scripting-guide/scripting-api-node.html#scripting-api-node-nodeState).

##### `X-ForgeRock-TransactionID` available in HTTP client script binding

The `httpClient` script binding now automatically adds the current transaction ID as an HTTP header. This lets you correlate caller and receiver logs when you use `httpClient` from a script, such as a decision node script, to make requests to other proprietary products and services.

For details, refer to [Access HTTP services](https://docs.pingidentity.com/pingam/7.4/scripting-guide/script-bindings.html#httpclient).

##### Customize account lockout message

Use the new `ActionBuilder.withLockoutMessage(String lockoutMessage)` method in a [Scripted Decision node](https://docs.pingidentity.com/auth-node-ref/8.1/scripted-decision.html) to customize the message displayed to an end user when their account is locked or inactive.

For details, refer to [Set script outcome](https://docs.pingidentity.com/pingam/7.4/scripting-guide/scripting-api-node.html#action-set-outcome).

##### Scripting enhancements

AM 7.4 introduces the Next Generation scripting engine, which offers the following benefits:

* Stability

  * A stable set of enhanced bindings, available to decision node scripts, that reduces the need to allowlist Java classes to access common functionality.

* Ease of use

  * Simplify your scripts with fewer imports and more intuitive return types that require less code.

  * Debug efficiently with clear log messages and a simple logging interface based on SLF4J.

  * Make requests to other APIs from within scripts more easily with a more intuitive HTTP client.

* Reduced complexity

  * Simplify and modularize your scripts with library scripts by reusing common code snippets as CommonJS modules.

    Reference library scripts from a decision node script.

  * Access identity management information seamlessly through the `openidm` binding.

For more information, refer to:

* [Scripted decision node API](https://docs.pingidentity.com/pingam/7.4/scripting-guide/scripting-api-node.html)

* [Next generation scripts](https://docs.pingidentity.com/pingam/7.4/scripting-guide/next-generation-scripts.html)

* [Reuse scripts](https://docs.pingidentity.com/pingam/7.4/scripting-guide/library-scripts.html)

##### Scripting logger name change

Scripts that log debug messages create loggers that now include the name of the script.

The name of a scripting logger uses the format `scripts.<context>.<script UUID>.(<script name>)`; for example, `scripts.OIDC_CLAIMS.36863ffb-40ec-48b9-94b1-9a99f71cc3b5.(OIDC Claims Script)`.

Refer to [Debug logging](https://docs.pingidentity.com/pingam/7.5/maintenance-guide/debug-logging.html).

##### Access request header values from OAuth 2.0 scripts

You can now access the `requestHeaders` binding in the following OAuth 2.0 scripts:

* [OIDC user info claims](https://docs.pingidentity.com/pingam/7.4/oauth2-guide/plugins-user-info-claims.html) (`OIDC_CLAIMS`)

* [Access token modification](https://docs.pingidentity.com/pingam/7.4/oauth2-guide/modifying-access-tokens-scripts.html) (`OAUTH2_ACCESS_TOKEN_MODIFICATION`)

* [Token exchange](https://docs.pingidentity.com/pingam/7.4/oauth2-guide/token-exchange.html) (`OAUTH2_MAY_ACT`)

For details, refer to the available objects for each script type.

##### File-based configuration migration utililty

In a future release, AM will read its configuration *only* from JSON files, not directory servers. Using LDAP data stores for configuration will be deprecated and file-based configuration (FBC) will be the only supported configuration storage mechanism. Dynamic data will continue to be stored in LDAP directories.

To prepare to migrate your configuration from LDAP directories to JSON files, AM 7.4 provides a *technology preview* of a configuration migration utility based on the existing `amupgrade` command. The purpose of this technology preview is to let you *test* migrating custom configuration to FBC.

For details, refer to [Migrate to a file-based configuration](https://docs.pingidentity.com/pingam/7.4/upgrade-guide/migrate-to-fbc.html).

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The interface stability for the file-based configuration (FBC) migration utility is *Technology Preview*. Technology previews offer access to new technology that is not yet supported. Technology preview features may be functionally incomplete and subject to change without notice. For details, refer to [Interface stability](stability.html).The purpose of this technology preview is to allow you to test the migration of your configuration data. The technology preview *should* function correctly but may highlight areas that need improvement before the supported release of this feature.AM configuration stored in DS remains supported as [documented for AM 7.4](https://docs.pingidentity.com/pingam/7.4/install-guide/prepare-configuration-store.html). In a future AM release, LDAP configuration stores will be deprecated in favor of FBC. |

##### Support for mTLS authentication

AM now supports mTLS authentication to the following external data stores:

* [Identity stores](https://docs.pingidentity.com/pingam/7.4/security-guide/secure-data-stores.html#mtls-identity-stores)

* [Configuration stores](https://docs.pingidentity.com/pingam/7.4/security-guide/secure-data-stores.html#mtls-config-stores)

* [Policy and application stores](https://docs.pingidentity.com/pingam/7.4/security-guide/secure-data-stores.html#mtls-policy-application-stores)

* [CTS stores](https://docs.pingidentity.com/pingam/7.4/security-guide/secure-data-stores.html#mtls-cts-stores)

* [UMA stores](https://docs.pingidentity.com/pingam/7.4/security-guide/secure-data-stores.html#mtls-uma-stores)

mTLS uses certificates to authenticate and is more secure than username/password authentication. For more security, you should rotate certificates periodically.

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Due to a known [issue in OpenJDK](https://bugs.openjdk.org/browse/JDK-8220723), you can't configure mTLS authentication to data stores if you're using Java version 11.0.2. If you're using this Java version and attempt to authenticate with mTLS, the connection fails and the DS server generates the following error in the `ldap-access.audit.json` log:```bash
"failureReason":"The SASL EXTERNAL bind request could not be processed because the client did not present a certificate
chain during SSL/TLS negotiation"
```AM then enters an invalid state.To work around this issue, upgrade to Java 11.0.3 or higher, or authenticate using simple authentication. |

##### Query Parameter node

The [Query Parameter node](https://docs.pingidentity.com/auth-node-ref/8.1/query-parameter.html) lets you insert query parameter values from a journey URL into configurable node state properties. This lets you customize journeys based on the query parameter values.

##### Support for HTML in Email Suspend node

The |Email Suspend Message of the [Email Suspend node](https://docs.pingidentity.com/auth-node-ref/8.1/email-suspend.html) now supports HTML code in addition to plain text.

This lets you add HTML components, including links and graphics, to the message displayed to end users.

## Fixes

### Fixes in AM 8.1.x

This page lists the cumulative fixes in AM 8.1.x releases:

#### AM 8.1.1

|              |                                                                                                                                                           |
| ------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
| OPENAM-28063 | Fixed token introspection failing for client-side (JWT) access tokens with a multi-valued `aud` claim                                                     |
| OPENAM-28053 | Fixed a policy evaluation thread hang that occurred under certain conditions                                                                              |
| OPENAM-28052 | Fixed an issue where JSON object changes to `authnRequest` in the SP adapter next-generation script did not persist                                       |
| OPENAM-28050 | Fixed inactive circles of trust remaining active after being disabled                                                                                     |
| OPENAM-28049 | Fixed `evaluateTree` not being available for use in policy evaluation scripts                                                                             |
| OPENAM-28048 | Fixed journey configurations that were not conformant with the expected schema                                                                            |
| OPENAM-28047 | Fixed occasional failures resolving the `passwordPurpose` attribute for a secret ID                                                                       |
| OPENAM-28044 | Fixed an inability to delete Node Designer nodes in AM                                                                                                    |
| OPENAM-28043 | Fixed the `aud` claim being omitted from the JSON introspection response due to an incorrect RFC 9701 configuration check                                 |
| OPENAM-27978 | Fixed an issue in OAuth 2.0 token exchange where `accessToken.addExtraData` calls in the Token Modification script were ignored                           |
| OPENAM-27951 | Fixed an issue where the default XUI login page showed a null label after migrating to file-based configuration                                           |
| OPENAM-27796 | Fixed an upgrade failure from AM 7.4.1 to AM 8.1.0 when mTLS was enabled between AM and the policy and application store                                  |
| OPENAM-27708 | Fixed an upgrade failure where the SAML2 node upgrade step rejected valid IdP Entity ID attributes during data validation                                 |
| OPENAM-27685 | Fixed an issue where authentication was re-triggered on subsequent OIDC flows after a failed `prompt=login` request                                       |
| OPENAM-27534 | Fixed the `/aiagent/register` endpoint returning a 500 error when a Dynamic Client Registration script is configured                                      |
| OPENAM-27463 | Fixed an upgrade failure caused by a missing upgrade step in the NodesPlugin for the Username Collector when the `autocompleteValues` attribute was added |
| OPENAM-27398 | Fixed the upgrader to automatically update PingOne Protect Node class references when upgrading from AM 7.5 to AM 8.0.x                                   |
| OPENAM-26694 | Fixed an Amster export failure returning a 400 Bad Request error for Custom and Node Designer nodes                                                       |
| OPENAM-26427 | Fixed JWT introspection responses to use the `token_introspection` claim as required by RFC 9701                                                          |
| OPENAM-26360 | Fixed an `invalid_request` error on `/authorize` requests that include `authorization_details` when the Remote Consent Service (RCS) is not configured    |
| OPENAM-26265 | Fixed a race condition in session quota enforcement that caused a login failure under concurrent authentication requests                                  |
| OPENAM-26240 | Fixed SAML persistent Name ID value mapping not being honored                                                                                             |
| OPENAM-26232 | Added a pluggable mechanism for installing and configuring custom session `QuotaExhaustionAction` implementations                                         |
| OPENAM-26036 | Fixed the `aud` claim in JWT access tokens not being correctly validated for the `/access_token` endpoint                                                 |
| OPENAM-25994 | Fixed policy evaluation with `LDAPFilterCondition` to use the identity store user instead of the config store user                                        |
| OPENAM-25911 | Resolved a performance regression where nested Inner Tree Evaluator nodes caused a significant drop in authentication throughput                          |
| OPENAM-25735 | Fixed loss of `OAUTH_REQUEST_ATTRIBUTES` context when the `max_age` parameter is used in authorization requests                                           |

#### AM 8.1.0

|              |                                                                                                                                                                              |
| ------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| OPENAM-25901 | Added `clientScopes` binding to next-generation OAuth2 Scope Validator script for refresh token validation                                                                   |
| OPENAM-25821 | Introspection fails for tokens generated by token exchange when the subject is an OAuth client                                                                               |
| OPENAM-25803 | Fixed a bug that caused errors when changing the `am.server.fqdn` value                                                                                                      |
| OPENAM-25797 | Resolved a caching issue that occurred when creating services via the REST API                                                                                               |
| OPENAM-25779 | Fixed an issue where the SAML application object couldn't be retrieved from the CTS store                                                                                    |
| OPENAM-25777 | Fixed a bug where log data was lost following a configuration change                                                                                                         |
| OPENAM-25752 | Resolved a performance regression where nested Inner Tree Evaluator nodes caused a significant drop in authentication throughput                                             |
| OPENAM-25738 | Fixed SAML IdP authentication failures occurring after a tenant upgrade                                                                                                      |
| OPENAM-25702 | PingOne Protect Evaluation node now correctly populates username preventing Email Reputation predictor errors                                                                |
| OPENAM-25691 | Fixed a failure in FBC-to-FBC upgrades caused by missing upgrade rule for `CustomAuthNode` service                                                                           |
| OPENAM-25686 | Resolved an unsupported operation when creating an allowlist                                                                                                                 |
| OPENAM-25680 | Updated `clientIdentity` script binding to work without requiring manual LDAP formatting                                                                                     |
| OPENAM-25677 | Replaced `enableTrust` option with `universalDeviceIdentification` in PingOneProtectInitializeCallback                                                                       |
| OPENAM-25651 | Fixed a journey execution failure when users launch multiple different journeys in quick succession                                                                          |
| OPENAM-25646 | Updated PingOne Protect Initialize node to support modified callback structures                                                                                              |
| OPENAM-25642 | Next-generation scripting now supports native `ConsString` types within callback builder arrays                                                                              |
| OPENAM-25583 | Improved FBC shutdown sequence to handle connectivity failures to application or policy stores                                                                               |
| OPENAM-25577 | Fixed an FBC startup failure occurring when no Bind DN is provided for application or policy stores                                                                          |
| OPENAM-25554 | Resolved a race condition in Session Quota logic during high-concurrency `/json/authenticate` calls                                                                          |
| OPENAM-25535 | Removed the requirement to manually copy `noninteractive-installproperties` during FBC upgrades                                                                              |
| OPENAM-25526 | PAR endpoints now correctly support `aud` claims when used with the BaseURL Provider service                                                                                 |
| OPENAM-25510 | Fixed an issue where the Protect Evaluation node sent an empty Risk Policy Set ID if not found in the state                                                                  |
| OPENAM-25487 | Clarified the `Use Node State Attribute For Risk Policy Set ID` setting in the PingOne Protect Evaluation node                                                               |
| OPENAM-25462 | Fixed an issue where `defaultValue` set in the Node Designer didn't propagate to the Tree Editor                                                                             |
| OPENAM-25406 | Added `identity.exists()` to next-generation identity scripting binding to indicate failure for unknown users                                                                |
| OPENAM-25392 | Suppressed noisy `JDMK runtime not found` logs when Policy Monitoring is disabled                                                                                            |
| OPENAM-25371 | Added option on the PingOne Verify Evaluation node to enable automatic redirection back to the journey after a user completes verification when using redirect delivery mode |
| OPENAM-25359 | Added an advanced property for configuring Session Cache expiry (TTL) to fix issues with stale sessions in cache                                                             |
| OPENAM-25326 | Resolved errors caused by successful logins with an unknown user when account lockout enabled                                                                                |
| OPENAM-25321 | Fixed `queryFilter` in scripts to correctly support the description field                                                                                                    |
| OPENAM-25179 | Deleting a tree now correctly cleans up versioned nodes to prevent orphaned entries                                                                                          |
| OPENAM-24573 | Added XUI support for PingOne Protect nodes                                                                                                                                  |
| OPENAM-24494 | Updated `accessTokenLifetime` changes in Agent Groups to apply immediately                                                                                                   |
| OPENAM-24481 | Improved performance when using outbound mTLS with the `httpClient` binding                                                                                                  |
| OPENAM-24471 | Added an error message for cases where SP and IdP MetaAlias values are identical                                                                                             |
| OPENAM-24401 | CAPTCHA node now prevents submission after expiry                                                                                                                            |
| OPENAM-24400 | Default links in Get Authenticator App node now prioritize PingID over the ForgeRock Authenticator                                                                           |
| OPENAM-24393 | Fixed InnerTreeEvaluator failures during REST-based access without an `authId` (affects Kerberos)                                                                            |
| OPENAM-24385 | WeChat social authentication now correctly supports client secret identifiers and references                                                                                 |
| OPENAM-24379 | Improved audit logging tree journey with failure reason                                                                                                                      |
| OPENAM-24360 | Added detailed failure reasons to audit logs generated by the Device Binding node                                                                                            |
| OPENAM-24349 | SAML 2.0 now able to select encryption algorithm with PKCS11 HSM keys                                                                                                        |
| OPENAM-24348 | Fixed an issue where AM failed to add trees to a session if tree names shared a prefix                                                                                       |
| OPENAM-24335 | Fixed `_queryFilter` for `advancedOAuth2ClientConfig` when scalable OAuth2 clients is enabled                                                                                |
| OPENAM-24327 | Set server name to cookie domain if global configuration of cookie domain is null                                                                                            |
| OPENAM-24309 | PingOne Verify Evaluation node now supports multiple values for Biographic Matching elements                                                                                 |
| OPENAM-24302 | Updated Apache Commons FileUpload to version 1.6                                                                                                                             |
| OPENAM-24297 | Updated PingOne Verify Evaluation node to handle timeout errors separately                                                                                                   |
| OPENAM-24219 | Fixed an issue with session allowlisting and the Update Journey Timeout node                                                                                                 |
| OPENAM-24159 | Resolved an issue preventing the use of two Identity Assertion nodes within a single login flow                                                                              |
| OPENAM-24156 | Fixed `getGenericSecret()` failures when using PEM-formatted files in File System Secret Volumes                                                                             |
| OPENAM-24154 | Corrected the behavior of the Number Matching function in the Push Notification Service                                                                                      |
| OPENAM-24125 | Service schema are now loaded from the main configuration store to fix performance issue with OAuth2 and Agent retrieval                                                     |
| OPENAM-24115 | Optimized the Social Provider Handler Node to reduce redundant outbound calls to `./well-known` endpoints                                                                    |
| OPENAM-24109 | Updated LDAPFilterCondition to correctly respect search request timeout settings                                                                                             |
| OPENAM-24091 | Fixed an issue in FBC where an incorrect encryption key was used for service attributes                                                                                      |
| OPENAM-24085 | For FBC deployments, you can now specify a base DN for your CTS store with the environment variable `am.stores.cts.root.suffix`                                              |
| OPENAM-24065 | Improved consistency for error responses so that `/authenticate` now correctly returns a 400 (Bad Request) instead of a 500 (Internal Server Error) for invalid arguments    |
| OPENAM-24061 | Fixed a permission issue where delegated admins in the root realm couldn't edit policy sets in sub-realms                                                                    |
| OPENAM-24020 | Added support for AdminTokenAction in AgentIdentityImpl                                                                                                                      |
| OPENAM-23964 | Added the missing expiry (`exp`) claim to request objects in social identity client requests                                                                                 |
| OPENAM-23945 | Fixed distributed tracing initialization for non-FBC scenarios                                                                                                               |
| OPENAM-23941 | Resolved an issue where interactive installation failed for FBC deployments                                                                                                  |
| OPENAM-23929 | Updated the IDM Provisioning Service `Configuration Cache Duration` default value from 0 (off) to 1 (minute) to improve performance                                          |
| OPENAM-23928 | Backchannel authentication with no subject now works when the back-channel user already has a session                                                                        |
| OPENAM-23918 | Resolved a race condition between OATH Device Storage and Registration nodes that caused lost recovery codes                                                                 |
| OPENAM-23869 | Ensured scripted PingOne Verify Completion Decision nodes can use new binding methods                                                                                        |
| OPENAM-23851 | Added missing file to `AM-8.*.zip` required to build base Docker image                                                                                                       |
| OPENAM-23850 | Fixed issue in QR code flows to allow users to continue verification on their current device                                                                                 |
| OPENAM-23802 | The `openidm` next-generation binding now supports IDM endpoints that return objects other than JSON objects                                                                 |
| OPENAM-23770 | Cancelling a WebAuthn flow now results in a `Client Error` outcome rather than an internal failure                                                                           |
| OPENAM-23767 | The `acr_sig` value is now correctly read from query parameters instead of the PAR object                                                                                    |
| OPENAM-23766 | Fixed Adapter Environment settings under the SP role in the admin interface                                                                                                  |
| OPENAM-23726 | Fixed a bug where misrouted IdP requests failed when using trees                                                                                                             |
| OPENAM-23718 | Added multiple requested Java libraries to the SAML2 SP Adapter scripting allowlist                                                                                          |
| OPENAM-23717 | Fixed a failure in access token requests (`grant_type=password`) when persistent cookie tree is set to default                                                               |
| OPENAM-23687 | Fixed an issue where `nodeState.mergeShared()` failed when used inside a Page Node                                                                                           |
| OPENAM-23665 | Added missing error context for the usernameless flow in the Device Signing Verifier node                                                                                    |
| OPENAM-23595 | Fixed a bug where `redirect_uri` using a URN resulted in a malformed redirect location                                                                                       |
| OPENAM-23588 | Updated ROPC grant error responses to comply with RFC 6749                                                                                                                   |
| OPENAM-23341 | Added error logging for OIDC and OAuth2 error responses                                                                                                                      |
| OPENAM-23283 | Enabled SecretReferenceCache for OAuth2 client secret labels                                                                                                                 |
| OPENAM-23137 | Social Provider Handler node now uses the configured identity store attribute instead of a hard-coded value                                                                  |
| OPENAM-23107 | Updated `/authorize` responses to comply with JARM specifications for the `code` response type                                                                               |
| OPENAM-22920 | Critical claims in JWT headers can now be ignored with a switch                                                                                                              |
| OPENAM-22848 | Fixed an issue where calling a Persistent Cookie node in an inner tree caused duplicate `set-cookie` actions                                                                 |
| OPENAM-22654 | Corrected the XUI rendering of checkboxes for the BooleanAttributeInputCallback                                                                                              |
| OPENAM-22609 | Fixed a bug where non-array clientName values sent via REST corrupted the OAuth2 client configuration                                                                        |
| OPENAM-21910 | Fixed an issue where `client_id` was incorrectly required when using JAR and `private_key_jwt`                                                                               |
| OPENAM-21881 | Updated Page node to remove `pageNodeCallbacks` from shared state after completing                                                                                           |
| OPENAM-20809 | Resolved compatibility issues with IE11 across multiple AM versions                                                                                                          |
| OPENAM-20776 | OIDC social authentication configuration now correctly uses the token endpoint for `private_key_jwt` audience verification                                                   |
| OPENAM-20582 | Fixed JWT client authentication to ensure `iss` and `sub` claim values match                                                                                                 |
| OPENAM-20389 | Corrected the description text for the LDAP Operations Timeout setting in the LDAP Decision node                                                                             |

#### AM 8.0.x

> **Collapse: AM 8.0.2**
>
> |              |                                                                                                                                                          |
> | ------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
> | AME-32756    | Address issue with stale policy index cache                                                                                                              |
> | AME-32195    | Node Designer doesn't work for non-English system and user locale                                                                                        |
> | AME-32279    | Scripting context upgrade step should preserve property name prefix                                                                                      |
> | OPENAM-25527 | Make sure PAR endpoint computed correctly for JWT audience validation                                                                                    |
> | OPENAM-25462 | In Node Designer, the `defaultValue` property doesn't work for custom nodes when using AM 8.0.1 with Java 21                                             |
> | OPENAM-24543 | The PingOne Protect Initialization node displays an unnecessary form to the end user                                                                     |
> | OPENAM-24400 | Update Get Authenticator App node to point to PingID instead of ForgeRock Authenticator                                                                  |
> | OPENAM-24393 | InnerTreeEvaluator node in the journey doesn't work when accessed using REST without authId (affects KerberosNode)                                       |
> | OPENAM-24349 | "Unable to determine key size for key" error occurs when signing an assertion with an explicit signing algorithm configured in the Service Provider (SP) |
> | OPENAM-24335 | The `_queryFilter` Parameter does not work for advancedOAuth2ClientConfig when scalable OAuth2 Clients are enabled                                       |
> | OPENAM-24228 | Add support for eu-west-2 SNS Client Region in the Push Notification Service                                                                             |
> | OPENAM-24219 | Suspended authentication doesn't work with journey session allowlist                                                                                     |
> | OPENAM-24125 | OAuth 2.0 or agent service fails to recover after schema reload required for external app store                                                          |
> | OPENAM-24109 | LDAPFilterCondition doesn't use search request timeout settings properly (timeout using heartbeat timeout)                                               |
> | OPENAM-24091 | Invalid encryption key used for service attributes during FBC setup                                                                                      |
> | OPENAM-24061 | A delegated admin logged into a root realm can't edit/create a policy set in the sub realm                                                               |
> | OPENAM-24059 | Add support for "android-key" webauthn attestation format                                                                                                |
> | OPENAM-24020 | AgentIdentityImpl to use AdminTokenAction to reduce stress on policy store                                                                               |
> | OPENAM-23945 | Distributed tracing fails to initialize in non-FBC scenario                                                                                              |
> | OPENAM-23851 | The AM-8.\*.zip is missing required file in order to build a base docker-image                                                                           |
> | OPENAM-23767 | The `acr_sig` value being read from the PAR object instead of the query parameter                                                                        |
> | OPENAM-23766 | Adapter Environment under SP role in the GUI isn't working properly                                                                                      |
> | OPENAM-23595 | A `redirect_uri` using a URN results in a malformed redirect location                                                                                    |
> | OPENAM-23341 | No error logging on AM side when OIDC or OAuth2 error responses are generated                                                                            |
> | OPENAM-23283 | SecretReferenceCache not used for `am.applications.oauth2.client.%s.secret` labels                                                                       |
> | OPENAM-23107 | Make `/authorize` response compliant with JARM specification when response type `code`                                                                   |
> | OPENAM-21910 | PAR `client_id` parameter treated as mandatory when using JAR and `private_key_jwt` auth method                                                          |
> | OPENAM-20776 | Social IdP with OIDC configuration uses token endpoint for private key JWT `aud` value                                                                   |
> | OPENAM-20809 | IE11 doesn't work with AM 7.2.1-RC1 and AM 7.3.0                                                                                                         |
> | OPENAM-20582 | The `iss` claim value must match `sub` claim value for JWT client authentication                                                                         |

> **Collapse: AM 8.0.1**
>
> |              |                                                                                                     |
> | ------------ | --------------------------------------------------------------------------------------------------- |
> | AME-31120    | Prevent using library scripts in Node Designer scripts                                              |
> | AME-31114    | Change the case of the SNS push message `GCM_PRIORITY` field to lowercase                           |
> | AME-31109    | Amster 8.0 import fails with `NoSuchMethodError`                                                    |
> | OPENAM-23770 | WebAuthn node flow causes exception instead of `Client Error` outcome when passkey prompt cancelled |

> **Collapse: AM 8.0**
>
> |              |                                                                                                              |
> | ------------ | ------------------------------------------------------------------------------------------------------------ |
> | OPENAM-23581 | Configuration Provider node doesn't accept duration values as integers                                       |
> | OPENAM-23537 | Configuration Provider node fails to get inputs for Inner Tree node                                          |
> | OPENAM-23519 | Android devices without a screen lock throw an error with WebAuthn registration                              |
> | OPENAM-23518 | AuthenticateToTreeConditionAdvice doesn't work with Inner Tree as first node                                 |
> | OPENAM-23516 | Timeout node configuration properties no longer accept negative numbers                                      |
> | OPENAM-23441 | Enabling OAuth2 client option "Allow wildcard ports in redirect URIs" prevents application URIs from working |
> | OPENAM-23427 | Composite advice with Auth Level fails when the realm contains a broken journey                              |
> | OPENAM-23228 | Fix file leak when receiving large response from next-generation scripting `httpClient` request              |
> | OPENAM-23095 | Reduced default OAuth2 denylist poll interval to ensure access token is correctly reported invalid           |
> | OPENAM-23091 | Fix for `systemEnv.getProperty()` in next-generation scripting                                               |
> | OPENAM-23077 | The `/access_token` endpoint sets the wrong error code when `code_verifier` isn't supplied                   |
> | OPENAM-23059 | `ssoadm` doesn't work against realm defaults                                                                 |
> | OPENAM-22988 | Failover doesn't occur when heartbeat interval is set to 0                                                   |
> | OPENAM-22966 | AM should accept `NONE` as a valid client authentication method for social IdPs                              |
> | OPENAM-22955 | Set Persistent Cookie node before tree failure causes 500 error instead of 401                               |
> | OPENAM-22865 | Stateful refresh token revoke race condition                                                                 |
> | OPENAM-22846 | External app/policy store active/passive LB isn't working                                                    |
> | OPENAM-22811 | Unable to modify `objectAttributes` when present in shared and transient state                               |
> | OPENAM-22708 | Loop back to the same node causes exception when the journey runs                                            |
> | OPENAM-22688 | Page node localization for header, description and footer isn't working as expected                          |
> | OPENAM-22675 | Next-generation scripting `callbacksBuilder` can't set value for NameCallback                                |
> | OPENAM-22657 | JWT validation fails when signed using the RS256 algorithm                                                   |
> | OPENAM-22652 | Some authentication nodes missing from am-external after IDM node seperation                                 |
> | OPENAM-22630 | Empty webhooks property key results in NullPointerException                                                  |
> | OPENAM-22608 | Non-extractable secrets in HSM fails to work on AM for SAML2 XML signing                                     |
> | OPENAM-22298 | NullPointerException in `SAML2Utils.verifyNameIDFormat` method                                               |
> | OPENAM-22297 | Saml2Node doesn't log whether SP and IDP descriptor were retrieved                                           |
> | OPENAM-22270 | No OAuth clients shown when scalable agents enabled                                                          |
> | OPENAM-22264 | AM doesn't use global service schema properties set by `ssoadm`                                              |
> | OPENAM-22171 | Forgotten Password flow fails when AM searches for the identity to modify                                    |
> | OPENAM-22146 | Request object failure not logged even when debug logging is set to highest level                            |
> | OPENAM-22120 | Backchannel logout tokens now include the `exp` claim                                                        |
> | OPENAM-22009 | Providing an invalid alias to a secret store mapping breaks AM                                               |
> | OPENAM-21974 | Social Identity Provider Service: LinkedIn template is out of date                                           |
> | OPENAM-21913 | When doing Session upgrade the Session property `Host` doesn't change from original value                    |
> | OPENAM-21617 | Exception thrown by scope validator script not whitelisted in script engine configuration                    |
> | OPENAM-21545 | Unable to create a circle of trust in file-based configuration with external data store                      |
> | OPENAM-21003 | IE11 not working during SAML tree authentication due to use of Arrow function                                |
> | OPENAM-18252 | Let nodes update the universal ID for impersonation and peer authentication                                  |
> | OPENAM-15834 | Access token call fails when an unsupported claim is requested                                               |
> | OPENAM-15410 | Audience claim not able to customize if scope with openid and profile                                        |
> | OPENAM-14438 | Ensure OAuth2ClientAgentGroups are imported before OAuth2ClientAgents in Amster                              |
> | OPENAM-14217 | Add more debug when getSessionInfo v2.1 fails with Internal Server Error                                     |

#### AM 7.5.x

> **Collapse: AM 7.5.2**
>
> |              |                                                                                                                                         |
> | ------------ | --------------------------------------------------------------------------------------------------------------------------------------- |
> | OPENAM-24543 | The PingOne Protect Initialization node displays an unnecessary form to the end user                                                    |
> | OPENAM-24349 | "Unable to determine key size for key" error occurs when signing an assertion with an explicit signing algorithm configured in the SP   |
> | OPENAM-24335 | The `_queryFilter` Parameter doesn't work for `advancedOAuth2ClientConfig` when scalable OAuth 2.0 clients are enabled                  |
> | OPENAM-24125 | OAuth 2.0 or agent service fails to recover after schema reload required for external app store                                         |
> | OPENAM-24109 | LDAPFilterCondition uses search time limit for request timeout                                                                          |
> | OPENAM-23716 | Policy lookup doesn't error when cache isn't populated and policy store is down                                                         |
> | OPENAM-23595 | Redirect using a URN loses the scheme-specific part                                                                                     |
> | OPENAM-23767 | The `acr_sig` value is read from the PAR object instead of the query parameter                                                          |
> | OPENAM-23766 | Adapter Environment under SP role in the GUI isn't working properly                                                                     |
> | OPENAM-23519 | Android devices without a screen lock not working with WebAuthn registration                                                            |
> | OPENAM-23518 | AuthenticateToTreeConditionAdvice does not work with innerTree as first node                                                            |
> | OPENAM-23441 | Enabling OAuth 2.0 client option "Allow wildcard ports in redirect URIs" prevents application URIs from working                         |
> | OPENAM-23341 | AM doesn't log errors for OIDC or OAuth 2.0 failures                                                                                    |
> | OPENAM-23283 | SecretReferenceCache not used for `am.applications.oauth2.client.%s.secret` labels                                                      |
> | OPENAM-23091 | Fix for `systemEnv.getProperty()` in next-generation scripting                                                                          |
> | OPENAM-22988 | Failover doesn't occur when heartbeat interval is set to `0`                                                                            |
> | OPENAM-22846 | External app/policy store active/passive LB isn't working                                                                               |
> | OPENAM-22657 | JWT validation fails when signed using the RS256 algorithm                                                                              |
> | OPENAM-22654 | BooleanAttributeInputCallback renders an enabled checkbox in AM XUI                                                                     |
> | OPENAM-22630 | Empty webhooks property key results in a NullPointerException                                                                           |
> | OPENAM-22608 | Non-extractable secrets in HSM fails to work on AM for SAML2 XML signing                                                                |
> | OPENAM-22520 | WebAuthN (FIDO Certification): TPM attestation failing when `pubArea.nameAlg` doesn't match the hash used to generate the attested name |
> | OPENAM-22346 | The RP `form_post` endpoint doesn't handle POST data well when OP returns error                                                         |
> | OPENAM-22298 | NullPointerException in `SAML2Utils.verifyNameIDFormat` method                                                                          |
> | OPENAM-22281 | NameIdFormat values populated for remote IdP                                                                                            |
> | OPENAM-22120 | Backchannel logout tokens now include the `exp` claim                                                                                   |
> | OPENAM-20776 | Enable private key jwt audience to be configurable                                                                                      |
> | OPENAM-20239 | Setting the `keepalive` or `heartbeat` interval to a negative value in the IdRepo config causes an error                                |
> | OPENAM-20089 | Configuration Provider nodes don't take integer values                                                                                  |
> | OPENAM-15834 | Access token call fails when an unsupported claim is requested                                                                          |
> | OPENAM-15410 | Audience claim not customizable when scope set to `openid` and `profile`                                                                |

> **Collapse: AM 7.5.1**
>
> |              |                                                                                                                       |
> | ------------ | --------------------------------------------------------------------------------------------------------------------- |
> | IAM-5473     | Always save UI environment variables to `.env` file when using yarn start                                             |
> | IAM-6429     | Failure URL node not working as expected on Safari when used with a Message node                                      |
> | OPENAM-23059 | SSOADM doesn't work for realm defaults                                                                                |
> | OPENAM-22955 | Set Persistent Cookie node causes 500 error before failure                                                            |
> | OPENAM-22847 | Nodes that use a tree hook with an injection annotation cause an error when the tree fails                            |
> | OPENAM-22836 | Unable to update KBA security questions using XUI                                                                     |
> | OPENAM-22753 | Destroy All session may fail to work                                                                                  |
> | OPENAM-22717 | SP-initiated SSO fails with "Illegal character in scheme name" when the IdP entity name has a special character       |
> | OPENAM-22715 | `PlaceholderAnnotationUtils.insertDefaultValueIntoPlaceholder` isn't escaping values correctly                        |
> | OPENAM-22708 | Loop back to the same node causes exception when tree is executed                                                     |
> | OPENAM-22696 | Persistent search notification invalidation on AD identity store doesn't invalidate user cached attributes            |
> | OPENAM-22676 | `SecretsProviderFacadeFactory` is not a supported API but is the only valid way to create the `SecretsProviderFacade` |
> | OPENAM-22675 | Unable to set a default value for NameCallback in next-generation `callbacksBuilder`                                  |
> | OPENAM-22672 | Configuring SAML entities with invalid secret label mappings break SAML flows for other entities                      |
> | OPENAM-22656 | Setting `JWKs URI content cache timeout` to a small value throws an error                                             |
> | OPENAM-22632 | `AMSetupServlet` installation error on Windows multi-domain environment                                               |
> | OPENAM-22620 | Slow response from access token endpoint using client credentials grant                                               |
> | OPENAM-22602 | OIDC ID Token Validator Node isn't using inbuilt `httpClient` settings to connect to JWK or well-known URL            |
> | OPENAM-22465 | Unexpected error when `request_uri` client doesn't match request parameter client in PAR authorise request            |
> | OPENAM-22391 | Issues with `evaluateTree` when using wildcard policies                                                               |
> | OPENAM-22322 | ArtifactResponse Assertion that is signed cannot be verified and fails                                                |
> | OPENAM-22318 | OAUTH\_REQUEST\_ATTRIBUTES cookie isn't getting deleted after authentication                                          |
> | OPENAM-22289 | Session quota action may fail when the session is not updateable but should be fine to proceed.                       |
> | OPENAM-22281 | NameIdFormat values populated for remote IdP                                                                          |
> | OPENAM-22181 | Approve UMA request fails with 500 error when AM deployed as a platform                                               |
> | OPENAM-22171 | Forgotten password fails when AM searches for the identity to modify                                                  |
> | OPENAM-22146 | OAuth 2.0 request object failure not logged for POST requests even when full debug logging is enabled                 |
> | OPENAM-22120 | Backchannel logout tokens now include the `exp` claim                                                                 |
> | OPENAM-22109 | The expiry time of OPS token in 7.x fails to update correctly                                                         |
> | OPENAM-22009 | Providing an invalid alias to a secret store mapping breaks AM                                                        |
> | OPENAM-21972 | SAML artifact binding is failing in load-balanced deployments                                                         |
> | OPENAM-21951 | No option to set the `selectedIndex` on a ChoiceCallback                                                              |
> | OPENAM-21897 | Creation order determines policy evaluate and evaluateTree results                                                    |
> | OPENAM-21864 | No option to enable the `trackingCookie` with next-generation `callbacksBuilder`                                      |
> | OPENAM-21852 | Failure when reading input from next-generation SelectIDPCallback                                                     |
> | OPENAM-21609 | OAuth2Provider service created immediately after install/restart isn't available in code flow                         |
> | OPENAM-21191 | Web agent sessions have a long session lifetime of 42 years                                                           |
> | OPENAM-21158 | Windows Hello registration fails on TPM attestation parsing on Windows 11 22H2                                        |
> | OPENAM-20945 | Unable to trace token revocation back to resource owner because of missing `trackingID` field                         |
> | OPENAM-20609 | Inconsistent error message getting access token when using refresh token after changing username                      |
> | OPENAM-20314 | Social Provider Handler node and Social IdP service use the `sub` claim to search for links to existing accounts      |
> | OPENAM-14438 | Ensure OAuth2ClientAgentGroups are imported before OAuth2ClientAgents in Amster                                       |

> **Collapse: AM 7.5**
>
> |              |                                                                                                                                                       |
> | ------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
> | OPENAM-22206 | AM upgrade fails for 7.1.4 and older: Creating UMA PCT Encryption Secret Failed                                                                       |
> | OPENAM-22191 | JUnit jars are bundled in the AM.war release                                                                                                          |
> | OPENAM-22119 | "Access to Java class ScriptedLoggerWrapper prohibited" exception                                                                                     |
> | OPENAM-22101 | UI admin tests are failing since updating secret ID to secret label                                                                                   |
> | OPENAM-22060 | am-config-upgrader: poor performance                                                                                                                  |
> | OPENAM-22035 | Page Nodes don't delete contained nodes when a tree is deleted                                                                                        |
> | OPENAM-22017 | ConfigProviderNode creates node class dynamically leading to native memory leak                                                                       |
> | OPENAM-21976 | Single point of locking contention when doing Client-based session logout                                                                             |
> | OPENAM-21941 | Unable to edit policies in the UI                                                                                                                     |
> | OPENAM-21937 | Quota Enforcement affecting agents sessions that authenticate by tree                                                                                 |
> | OPENAM-21936 | Unable to use Legacy and Next Generation Script in the same authentication tree                                                                       |
> | OPENAM-21912 | OAuth2/OIDC signing slow with RSA keys when using Google Secret Manager                                                                               |
> | OPENAM-21856 | Introspecting stateless token with IG/Web agents will cause OAuth2ChfException                                                                        |
> | OPENAM-21854 | TermsAndConditionsCallback fails with error on XUI                                                                                                    |
> | OPENAM-21840 | Warning for missing mapping in dynamic secret doesn't warn for missing secret label identifier                                                        |
> | OPENAM-21803 | CertificateUserExtractorNode cannot resolve wrong name when UPN SubjectAltNameExt                                                                     |
> | OPENAM-21780 | Next generation scripting `httpClient` adds "null" as entity to GET requests                                                                          |
> | OPENAM-21748 | Next generation scripting missing "get" wrapper function for HiddenValueCallback                                                                      |
> | OPENAM-21747 | Amster not working after connecting when AM REST call has extra `set-cookie` headers                                                                  |
> | OPENAM-21739 | Running the am-config-upgrader on an empty directory results in unexpected addition of library scripting service                                      |
> | OPENAM-21707 | file-functional-tests: OAuth2Provider doesn't allow setting of default consent agent when scalableAgents are enabled                                  |
> | OPENAM-21693 | Remove default global library script                                                                                                                  |
> | OPENAM-21664 | Upgrade fails to AM 7.4 with an uncaught exception when initialising the PrivilegeIndexStore class                                                    |
> | OPENAM-21506 | Inner Evaluator Tree with Data Store Decision node fails with correct password on first pass when used with Retry Decision node                       |
> | OPENAM-21484 | OAuth2 tokenintrospection response has different claim value types when refresh tokens are introspected                                               |
> | OPENAM-21473 | Certificate collector node: getPortalStyleCert throws exception when cert/header not present                                                          |
> | OPENAM-21389 | Searching algorithm for calculating the reachability of a node in a tree returns incorrect result                                                     |
> | OPENAM-21277 | Running Amster in debug mode doesn't work on Windows                                                                                                  |
> | OPENAM-21053 | User ID is missing from access.audit.json for JWT client authentication flow using `org.forgerock.security.oauth2.enforce.sub.claim.uniqueness=false` |
> | OPENAM-20924 | Reentry cookie when set causes the user to redirect to an incorrect IdP                                                                               |
> | OPENAM-20490 | AESWrapEncryption shows "WARN: AESWrap-encrypted data is less than 16 bytes"                                                                          |
> | OPENAM-20329 | Forgerock JWT Secured Authorization Response Mode for OAuth 2.0 (JARM) not spec compliant                                                             |
> | OPENAM-19999 | ID token as AM session doesn't work with `/authorize` when openid scope is requested                                                                  |
> | OPENAM-19889 | Policy evaluation fails with Agent access token JWT as subject                                                                                        |
> | OPENAM-17816 | 500 Internal Server Error (from NPE) returned for a missing Content-Type header                                                                       |
> | OPENAM-17315 | Update defaults scripts with the change introduced in COMMONS-628                                                                                     |

#### AM 7.4.x

> **Collapse: AM 7.4.2**
>
> |              |                                                                                                                  |
> | ------------ | ---------------------------------------------------------------------------------------------------------------- |
> | OPENAM-23441 | Enabling OAuth2 client option "Allow wildcard ports in redirect URIs" prevents application URIs from working     |
> | OPENAM-23091 | Fix for `systemEnv.getProperty()` in next-generation scripting                                                   |
> | OPENAM-23059 | `ssoadm` doesn't work against realm defaults                                                                     |
> | OPENAM-22988 | Failover doesn't occur when `heartbeat` interval is set to 0                                                     |
> | OPENAM-22846 | External app/policy store active/passive LB isn't working                                                        |
> | OPENAM-22836 | Unable to update KBA security questions using XUI                                                                |
> | OPENAM-22717 | SP-initiated SSO fails with "Illegal character in scheme name" when the IdP entity name has a special character  |
> | OPENAM-22657 | JWT validation fails when signed using the RS256 algorithm                                                       |
> | OPENAM-22632 | AMSetupServlet install error with Windows multi-domain environment                                               |
> | OPENAM-22608 | Non-extractable secrets in HSM fails to work on AM for SAML2 XML signing                                         |
> | OPENAM-22465 | Unexpected error when request\_uri client doesn't match request parameter client in PAR authorise request        |
> | OPENAM-22391 | Issues with `evaluateTree` when using wildcard policies                                                          |
> | OPENAM-22346 | The RP `form_post` endpoint doesn't handle POST data well when OP returns error                                  |
> | OPENAM-22322 | Signed ArtifactResponse Assertion can't be verified and fails                                                    |
> | OPENAM-22318 | OAUTH\_REQUEST\_ATTRIBUTES cookie isn't getting deleted after authentication                                     |
> | OPENAM-22298 | NullPointerException in `SAML2Utils.verifyNameIDFormat` method                                                   |
> | OPENAM-22264 | Add global attribute handling to `ssoadm`                                                                        |
> | OPENAM-22120 | Backchannel logout tokens now include the `exp` claim                                                            |
> | OPENAM-21951 | No option to set the `selectedIndex` on a ChoiceCallback                                                         |
> | OPENAM-21926 | Lockout message is not applied when using Identity Store Decision node                                           |
> | OPENAM-21897 | Creation order determines policy `evaluate` and `evaluateTree` results                                           |
> | OPENAM-21864 | No option to enable the `trackingCookie` with `callbacksBuilder`                                                 |
> | OPENAM-21748 | Next-generation scripting missing "get" wrapper function for HiddenValueCallback                                 |
> | OPENAM-21609 | OAuth2Provider service created immediately after install/restart isn't available in code flow                    |
> | OPENAM-21545 | Unable to create a circle of trust in file-based configuration with external data store                          |
> | OPENAM-20945 | Unable to trace token revocation back to resource owner because of missing `trackingID` field                    |
> | OPENAM-20314 | Social Provider Handler node and Social IdP service use the `sub` claim to search for links to existing accounts |
> | OPENAM-20239 | Setting the `keepalive` or `heartbeat` interval to a negative value in the IdRepo config causes an error         |
> | OPENAM-15834 | Access token call fails when an unsupported claim is requested                                                   |
> | OPENAM-14438 | Ensure OAuth2ClientAgentGroups are imported before OAuth2ClientAgents in Amster                                  |

> **Collapse: AM 7.4.1**
>
> |              |                                                                                                            |
> | ------------ | ---------------------------------------------------------------------------------------------------------- |
> | OPENAM-22753 | Destroy All session may fail to work                                                                       |
> | OPENAM-22715 | PlaceholderAnnotationUtils.insertDefaultValueIntoPlaceholder is not escaping values correctly              |
> | OPENAM-22696 | Persistent search notification invalidation on AD identity store doesn't invalidate user cached attributes |
> | OPENAM-22620 | Slow response from access token endpoint using client credentials grant                                    |
> | OPENAM-22602 | OIDC ID Token Validator node uses own httpClient settings to connect to JWK or well-known URL              |
> | OPENAM-22421 | Webauthn: Windows Hello TPM Attestation failing for Windows 11 22H2                                        |
> | OPENAM-22289 | Session quota action may fail when the session isn't updatable but should be fine to proceed               |
> | OPENAM-22181 | Approve UMA request fails with 500 error when AM deployed as a platform                                    |
> | OPENAM-22171 | Forgotten password fails when AM searches for the identity to modify                                       |
> | OPENAM-22119 | "Access to Java class ScriptedLoggerWrapper prohibited" exception                                          |
> | OPENAM-22109 | The expiry time of OPS token in 7.x doesn't change with the time of tokens created                         |
> | OPENAM-22017 | Configuration Provider node creates node class dynamically leading to native memory leak                   |
> | OPENAM-21976 | Single point of locking contention when doing client-based session logout                                  |
> | OPENAM-21972 | SAML artifact binding is using crosstalk for artifact resolution                                           |
> | OPENAM-21941 | Unable to edit policies in the UI                                                                          |
> | OPENAM-21937 | Quota enforcement affects agent sessions that authenticate by tree                                         |
> | OPENAM-21936 | Unable to use legacy and next-generation scripts in the same authentication tree                           |
> | OPENAM-21868 | ssoadm `create-sub-cfg` not working for AM 7.2+ due to the `context=` field                                |
> | OPENAM-21854 | TermsAndConditionsCallback fails with error on XUI                                                         |
> | OPENAM-21803 | Certificate User Extractor node cannot resolve wrong name when UPN SubjectAltNameExt                       |
> | OPENAM-21780 | Next-generation `httpClient` script binding adds "null" as entity to GET requests                          |
> | OPENAM-21747 | Amster not working after connecting when AM REST call has extra `set-cookie` headers                       |
> | OPENAM-21664 | Upgrade fails to AM 7.4.0 with an uncaught exception when initializing the PrivilegeIndexStore class       |
> | OPENAM-21484 | OAuth 2.0 token introspection response has different claim value types when introspecting refresh tokens   |
> | OPENAM-21473 | Certificate Collector node: getPortalStyleCert throws exception when cert/header not present               |
> | OPENAM-21466 | AM using OIDC social authentication fails to verify ID token if remote JWK\_URIs have duplicate KID        |
> | OPENAM-21277 | Running Amster in debug mode doesn't work on Windows                                                       |
> | OPENAM-21191 | Web agent sessions have a long session lifetime of 42 years                                                |
> | OPENAM-20609 | Inconsistent error message when generating access token using refresh token after changing username        |
> | OPENAM-19999 | ID token as AM session doesn't work with `/authorize` when openid scope is requested                       |
> | OPENAM-19889 | Policy evaluation fails with agent access token JWT as subject                                             |
> | OPENAM-17816 | 500 Internal Server Error (from NPE) returned for a missing Content-Type header                            |

> **Collapse: AM 7.4**
>
> |              |                                                                                                                                                  |
> | ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------ |
> | OPENAM-21476 | Persistent Cookie isn't created when using Configuration Provider node                                                                           |
> | OPENAM-21421 | Scripting logger name isn't based on logging hierarchy convention                                                                                |
> | OPENAM-21390 | Fix caching error when a journey switches backend instances to correctly provide data to `nodeState`                                             |
> | OPENAM-21360 | Add `java.util.concurrent.ExecutionException` to AM scripting class allowlist                                                                    |
> | OPENAM-21323 | LDAP (inline) upgrade fails due to policy creation of UssSelfWriteAttributes                                                                     |
> | OPENAM-21304 | Retain request URI values specified during dynamic client registration                                                                           |
> | OPENAM-21164 | Fix type issue of XML String in SAML responses when using a custom adapter                                                                       |
> | OPENAM-21160 | Make sure secure state values are retained when navigating the authentication tree                                                               |
> | OPENAM-21158 | Windows Hello registration fails on TPM attestation parsing on Windows 11 22H2                                                                   |
> | OPENAM-21085 | Undefined bindings are incorrectly evaluated in Groovy scripts                                                                                   |
> | OPENAM-21069 | WindowsDesktopSSO authentication is failing                                                                                                      |
> | OPENAM-21053 | Missing `userId` from Access audit log when `org.forgerock.security.oauth2.enforce.sub.claim.uniqueness=false` in JWT client authentication flow |
> | OPENAM-21030 | Amster CLI doesn't work on Windows                                                                                                               |
> | OPENAM-21010 | Social authentication user profile corrupted when remote OIDC server provides non-English identity claims                                        |
> | OPENAM-21004 | AM will always look for valid session when `scope=openid`                                                                                        |
> | OPENAM-21001 | SAML IdPAccountMapper isn't correctly determined                                                                                                 |
> | OPENAM-20980 | OIDC social provider uses configured issuer instead of wellknown endpoint issuer when using regex comparison                                     |
> | OPENAM-20953 | Return subject attributes correctly when evaluating a policy using a `JwtClaim` as subject type                                                  |
> | OPENAM-20920 | Improve handling of SAML2 IDP metadata that uses SSO endpoint entries other than HTTP-POST or HTTP-Redirect bindings when binding is null        |
> | OPENAM-20897 | Debug logs not showing info for ERROR: Unsupported Callback, "{0}" and others                                                                    |
> | OPENAM-20895 | Newly created Maven archetype project for building custom authentication nodes fails to build                                                    |
> | OPENAM-20851 | Existing registered devices unable to use push notifications when AWS SNS credentials are updated                                                |
> | OPENAM-20784 | TestUMAPolicy fails for users that will cause LocalizedIllegalArgumentException                                                                  |
> | OPENAM-20756 | Social authentication request for Apple fails due to duplicated `response_mode=form_post` request parameter                                      |
> | OPENAM-20691 | Fix rare race condition in session quota destroy next expiring action that can lead to the oldest session not being destroyed                    |
> | OPENAM-20682 | Unable to encrypt from `jwk_uri` where there are multiple JWKs with the same `kid` but different algorithms                                      |
> | OPENAM-20490 | AESWrapEncryption shows "WARN: AESWrap-encrypted data is less than 16 bytes"                                                                     |
> | OPENAM-20451 | Fix to display user-friendly account name during WebAuthn device registration                                                                    |
> | OPENAM-20299 | Fix to make agent authentication honor `com.iplanet.am.session.agentSessionIdleTime`                                                             |
> | OPENAM-20230 | Class allowlisting denies access to permitted classes after running for an extended period of time                                               |
> | OPENAM-20026 | Social IDP with trailing whitespace in the name can't be deleted using the UI                                                                    |
> | OPENAM-20024 | Improve debug logging when login to XUI fails with HTTP 404 JsonValueException from endpoint                                                     |
> | OPENAM-19282 | Recovery Code Display Node works only immediately after Registration node                                                                        |
> | OPENAM-19261 | Fix incorrectly logged errors when introspecting tokens using OAuth 2.0 client credentials grant                                                 |
> | OPENAM-18709 | New `nodeState.getObject` method added to return values stored in both shared and secure state                                                   |
> | OPENAM-18685 | New realm-level configuration setting to remove or skip `subname` claim                                                                          |
> | OPENAM-18004 | Support sequential transaction IDs to improve audit logging for HTTP requests to IDM                                                             |
> | OPENAM-17331 | Push Notifications: User with disabled endpoint is not able to login                                                                             |
> | OPENAM-17179 | Deleting an authentication tree leaves orphaned nodes that prevent deletion of referenced scripts                                                |

#### AM 7.3.x

> **Collapse: AM 7.3.2**
>
> |              |                                                                                                                  |
> | ------------ | ---------------------------------------------------------------------------------------------------------------- |
> | OPENAM-22836 | Unable to update KBA Security questions using XUI                                                                |
> | OPENAM-22753 | Destroy All session may fail to work                                                                             |
> | OPENAM-22717 | SP-initiated SSO fails with "Illegal character in scheme name" when IdP name contains a special character        |
> | OPENAM-22696 | Persistent search notification invalidation on AD identity store doesn't invalidate user cached attributes       |
> | OPENAM-22656 | Setting `JWKs URI content cache timeout` to a small value throws an error                                        |
> | OPENAM-22632 | AMSetupServlet install error with Windows multi-domain environment                                               |
> | OPENAM-22602 | OIDC ID Token Validator node uses own `httpClient` settings to connect to JWK or well-known URL                  |
> | OPENAM-22421 | Webauthn: Windows Hello TPM Attestation failing for Windows 11 22H2                                              |
> | OPENAM-22391 | Issues with `evaluateTree` when using wildcard policies                                                          |
> | OPENAM-22322 | Unable to verify signed ArtifactResponse Assertion leading to failure                                            |
> | OPENAM-22318 | OAUTH\_REQUEST\_ATTRIBUTES cookie isn't getting deleted after authentication                                     |
> | OPENAM-22289 | Session quota action may fail when the session isn't updatable but should be fine to proceed                     |
> | OPENAM-22288 | Amster upgrade 7.3.0-to-7.3.x fails with Groovy Exception                                                        |
> | OPENAM-22181 | Approve UMA request fails with 500 error when AM deployed as a platform                                          |
> | OPENAM-22120 | Backchannel logout token doesn't contain `exp` claim                                                             |
> | OPENAM-21972 | SAML artifact binding is failing in load-balanced deployments                                                    |
> | OPENAM-21937 | Quota enforcement affects agent sessions that authenticate by tree                                               |
> | OPENAM-21897 | Creation order determines policy evaluate and evaluateTree results                                               |
> | OPENAM-21473 | Certificate collector node: `getPortalStyleCert` throws exception when cert/header not present                   |
> | OPENAM-21322 | AM console allows creation of entity provider with space at the end of the name                                  |
> | OPENAM-21191 | Web agent sessions have a long session lifetime of 42 years                                                      |
> | OPENAM-21085 | Undefined bindings are incorrectly evaluated in Groovy scripts                                                   |
> | OPENAM-20945 | Unable to trace token revocation back to resource owner because of missing `trackingID` field                    |
> | OPENAM-20314 | Social Provider Handler node and Social IdP service use the `sub` claim to search for links to existing accounts |
> | OPENAM-20299 | Fix to make agent authentication honor `com.iplanet.am.session.agentSessionIdleTime`                             |
> | OPENAM-19261 | Fix incorrectly logged errors when introspecting tokens using OAuth 2.0 client credentials grant                 |

> **Collapse: AM 7.3.1**
>
> |              |                                                                                                                |
> | ------------ | -------------------------------------------------------------------------------------------------------------- |
> | OPENAM-22017 | ConfigProviderNode creates node class dynamically leading to native memory leak                                |
> | OPENAM-21976 | Single point of locking contention when performing client-based session logout                                 |
> | OPENAM-21941 | Unable to edit policies in the UI                                                                              |
> | OPENAM-21854 | TermsAndConditionsCallback fails with error on XUI                                                             |
> | OPENAM-21747 | Rest SDK and Amster send cookies if request has cookie header                                                  |
> | OPENAM-21728 | Certificate module fails using JDK 11.0.21 and later with undefined access to private method                   |
> | OPENAM-21484 | Introspecting OAuth 2.0 refresh tokens results in different claim value types in the response                  |
> | OPENAM-21421 | Scripting logger name isn't based on logging hierarchy convention                                              |
> | OPENAM-21390 | ConsumedStateDataCache can cache an incomplete set of reachability data when on multi-AM environment           |
> | OPENAM-21304 | OAuth 2.0 dynamic client registrations don't retain `request_uri` values when creating                         |
> | OPENAM-21277 | Running Amster in debug mode doesn't work on Windows                                                           |
> | OPENAM-21164 | Calling `toXMLString` in custom SAML adapter can return incorrectly formatted XML leading to invalid signature |
> | OPENAM-21160 | Inconsistent values in secure state when navigating an authentication tree                                     |
> | OPENAM-21158 | Windows Hello registration fails on TPM attestation parsing on Windows 11 22H2                                 |
> | OPENAM-21069 | WindowsDesktopSSO authentication is failing                                                                    |
> | OPENAM-21030 | Amster 7.3.0 CLI isn't working on Windows                                                                      |
> | OPENAM-21010 | Social authentication for remote OIDC server for user profile non-english words corrupted                      |
> | OPENAM-21004 | AM will always look for valid session when scope=openid                                                        |
> | OPENAM-21001 | IdPAccountMapper is not correctly determined                                                                   |
> | OPENAM-20980 | Unable to use issuer comparison check regex in oidc social provider                                            |
> | OPENAM-20897 | Debug logs not showing info for `ERROR: Unsupported Callback, "{0}"` and others                                |
> | OPENAM-20895 | Newly-created Maven archetype project fails to build                                                           |
> | OPENAM-20756 | OIDC social authentication request (Apple) fails due to duplicate `response_mode=form_post` request parameter  |
> | OPENAM-20691 | Destroy oldest session may fail to work                                                                        |
> | OPENAM-20682 | Unable to encrypt from `jwk_uri` when there are duplicate `kid`                                                |
> | OPENAM-20490 | AESWrapEncryption shows "WARN: AESWrap-encrypted data is less than 16 bytes"                                   |
> | OPENAM-20026 | Trailing whitespace prevents social provider deletion via UI                                                   |
> | OPENAM-19999 | ID token as AM session doesn't work with `/authorize` when openid scope is requested                           |
> | OPENAM-19889 | Policy evaluation fails with agent access token JWT as subject                                                 |
> | OPENAM-19282 | Recovery Code Display Node works only immediately after Registration node                                      |
> | OPENAM-18599 | Allow for custom error message if user account is locked                                                       |

> **Collapse: AM 7.3**
>
> |              |                                                                                                                     |
> | ------------ | ------------------------------------------------------------------------------------------------------------------- |
> | OPENAM-20396 | Authentication tree is selected by order of acr to tree mapping, not the default values, and order is not preserved |
> | OPENAM-20360 | Ampersand is double encoded in the Destination of a SAML Assertion                                                  |
> | OPENAM-20260 | Unable to log into AM when external application store is down                                                       |
> | OPENAM-20230 | Class allowlisting fails with permission denied after an extended period                                            |
> | OPENAM-20181 | AD account notification fails                                                                                       |
> | OPENAM-20159 | Upgrader adds requestObjectProcessing to OAuth2Provider subconfigs                                                  |
> | OPENAM-20104 | The `fragment` response\_mode for the /oauth2/authorize endpoint is not working                                     |
> | OPENAM-20085 | STS token generation does not work with clustered docker pods                                                       |
> | OPENAM-20082 | Locked out users are shown a misleading error message                                                               |
> | OPENAM-19868 | Correctly handle multi-line text in Email Suspend nodes                                                             |
> | OPENAM-19866 | Excessive logging when accessing protected resources                                                                |
> | OPENAM-19726 | The `par` endpoint doesn't return a `request_uri` when using JAR and claims are provided                            |
> | OPENAM-19665 | Wrong Java version in Amster README file                                                                            |
> | OPENAM-19515 | Unable to update session service with read only identity store                                                      |
> | OPENAM-19411 | Amster installation failure with authorizedKey parameter when trying to overwrite an existing configuration         |
> | OPENAM-18818 | Persistent search error message shows wrong DS identifier                                                           |
> | OPENAM-18488 | Windows Hello with TPM/platform authenticator returns two certificates                                              |
> | OPENAM-18172 | Multiple instances of "No Social Authentication Service found for realm" logged at WARNING level                    |
> | OPENAM-17215 | Policy debug log fills up at very high pace if the config store is not found                                        |
> | OPENAM-13766 | No configuration found for login with SessionConditionAdvice=deny                                                   |

### Fixes in AM 8.0.x

This page lists the cumulative fixes in AM 8.0.x releases:

#### AM 8.0.2

|              |                                                                                                                                                          |
| ------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
| AME-32756    | Address issue with stale policy index cache                                                                                                              |
| AME-32195    | Node Designer doesn't work for non-English system and user locale                                                                                        |
| AME-32279    | Scripting context upgrade step should preserve property name prefix                                                                                      |
| OPENAM-25527 | Make sure PAR endpoint computed correctly for JWT audience validation                                                                                    |
| OPENAM-25462 | In Node Designer, the `defaultValue` property doesn't work for custom nodes when using AM 8.0.1 with Java 21                                             |
| OPENAM-24543 | The PingOne Protect Initialization node displays an unnecessary form to the end user                                                                     |
| OPENAM-24400 | Update Get Authenticator App node to point to PingID instead of ForgeRock Authenticator                                                                  |
| OPENAM-24393 | InnerTreeEvaluator node in the journey doesn't work when accessed using REST without authId (affects KerberosNode)                                       |
| OPENAM-24349 | "Unable to determine key size for key" error occurs when signing an assertion with an explicit signing algorithm configured in the Service Provider (SP) |
| OPENAM-24335 | The `_queryFilter` Parameter does not work for advancedOAuth2ClientConfig when scalable OAuth2 Clients are enabled                                       |
| OPENAM-24228 | Add support for eu-west-2 SNS Client Region in the Push Notification Service                                                                             |
| OPENAM-24219 | Suspended authentication doesn't work with journey session allowlist                                                                                     |
| OPENAM-24125 | OAuth 2.0 or agent service fails to recover after schema reload required for external app store                                                          |
| OPENAM-24109 | LDAPFilterCondition doesn't use search request timeout settings properly (timeout using heartbeat timeout)                                               |
| OPENAM-24091 | Invalid encryption key used for service attributes during FBC setup                                                                                      |
| OPENAM-24061 | A delegated admin logged into a root realm can't edit/create a policy set in the sub realm                                                               |
| OPENAM-24059 | Add support for "android-key" webauthn attestation format                                                                                                |
| OPENAM-24020 | AgentIdentityImpl to use AdminTokenAction to reduce stress on policy store                                                                               |
| OPENAM-23945 | Distributed tracing fails to initialize in non-FBC scenario                                                                                              |
| OPENAM-23851 | The AM-8.\*.zip is missing required file in order to build a base docker-image                                                                           |
| OPENAM-23767 | The `acr_sig` value being read from the PAR object instead of the query parameter                                                                        |
| OPENAM-23766 | Adapter Environment under SP role in the GUI isn't working properly                                                                                      |
| OPENAM-23595 | A `redirect_uri` using a URN results in a malformed redirect location                                                                                    |
| OPENAM-23341 | No error logging on AM side when OIDC or OAuth2 error responses are generated                                                                            |
| OPENAM-23283 | SecretReferenceCache not used for `am.applications.oauth2.client.%s.secret` labels                                                                       |
| OPENAM-23107 | Make `/authorize` response compliant with JARM specification when response type `code`                                                                   |
| OPENAM-21910 | PAR `client_id` parameter treated as mandatory when using JAR and `private_key_jwt` auth method                                                          |
| OPENAM-20776 | Social IdP with OIDC configuration uses token endpoint for private key JWT `aud` value                                                                   |
| OPENAM-20809 | IE11 doesn't work with AM 7.2.1-RC1 and AM 7.3.0                                                                                                         |
| OPENAM-20582 | The `iss` claim value must match `sub` claim value for JWT client authentication                                                                         |

#### AM 8.0.1

|              |                                                                                                     |
| ------------ | --------------------------------------------------------------------------------------------------- |
| AME-31120    | Prevent using library scripts in Node Designer scripts                                              |
| AME-31114    | Change the case of the SNS push message `GCM_PRIORITY` field to lowercase                           |
| AME-31109    | Amster 8.0 import fails with `NoSuchMethodError`                                                    |
| OPENAM-23770 | WebAuthn node flow causes exception instead of `Client Error` outcome when passkey prompt cancelled |

#### AM 8.0.0

|              |                                                                                                              |
| ------------ | ------------------------------------------------------------------------------------------------------------ |
| OPENAM-23581 | Configuration Provider node doesn't accept duration values as integers                                       |
| OPENAM-23537 | Configuration Provider node fails to get inputs for Inner Tree node                                          |
| OPENAM-23519 | Android devices without a screen lock throw an error with WebAuthn registration                              |
| OPENAM-23518 | AuthenticateToTreeConditionAdvice doesn't work with Inner Tree as first node                                 |
| OPENAM-23516 | Timeout node configuration properties no longer accept negative numbers                                      |
| OPENAM-23441 | Enabling OAuth2 client option "Allow wildcard ports in redirect URIs" prevents application URIs from working |
| OPENAM-23427 | Composite advice with Auth Level fails when the realm contains a broken journey                              |
| OPENAM-23228 | Fix file leak when receiving large response from next-generation scripting `httpClient` request              |
| OPENAM-23095 | Reduced default OAuth2 denylist poll interval to ensure access token is correctly reported invalid           |
| OPENAM-23091 | Fix for `systemEnv.getProperty()` in next-generation scripting                                               |
| OPENAM-23077 | The `/access_token` endpoint sets the wrong error code when `code_verifier` isn't supplied                   |
| OPENAM-23059 | `ssoadm` doesn't work against realm defaults                                                                 |
| OPENAM-22988 | Failover doesn't occur when heartbeat interval is set to 0                                                   |
| OPENAM-22966 | AM should accept `NONE` as a valid client authentication method for social IdPs                              |
| OPENAM-22955 | Set Persistent Cookie node before tree failure causes 500 error instead of 401                               |
| OPENAM-22865 | Stateful refresh token revoke race condition                                                                 |
| OPENAM-22846 | External app/policy store active/passive LB isn't working                                                    |
| OPENAM-22811 | Unable to modify `objectAttributes` when present in shared and transient state                               |
| OPENAM-22708 | Loop back to the same node causes exception when the journey runs                                            |
| OPENAM-22688 | Page node localization for header, description and footer isn't working as expected                          |
| OPENAM-22675 | Next-generation scripting `callbacksBuilder` can't set value for NameCallback                                |
| OPENAM-22657 | JWT validation fails when signed using the RS256 algorithm                                                   |
| OPENAM-22652 | Some authentication nodes missing from am-external after IDM node seperation                                 |
| OPENAM-22630 | Empty webhooks property key results in NullPointerException                                                  |
| OPENAM-22608 | Non-extractable secrets in HSM fails to work on AM for SAML2 XML signing                                     |
| OPENAM-22298 | NullPointerException in `SAML2Utils.verifyNameIDFormat` method                                               |
| OPENAM-22297 | Saml2Node doesn't log whether SP and IDP descriptor were retrieved                                           |
| OPENAM-22270 | No OAuth clients shown when scalable agents enabled                                                          |
| OPENAM-22264 | AM doesn't use global service schema properties set by `ssoadm`                                              |
| OPENAM-22171 | Forgotten Password flow fails when AM searches for the identity to modify                                    |
| OPENAM-22146 | Request object failure not logged even when debug logging is set to highest level                            |
| OPENAM-22120 | Backchannel logout tokens now include the `exp` claim                                                        |
| OPENAM-22009 | Providing an invalid alias to a secret store mapping breaks AM                                               |
| OPENAM-21974 | Social Identity Provider Service: LinkedIn template is out of date                                           |
| OPENAM-21913 | When doing Session upgrade the Session property `Host` doesn't change from original value                    |
| OPENAM-21617 | Exception thrown by scope validator script not whitelisted in script engine configuration                    |
| OPENAM-21545 | Unable to create a circle of trust in file-based configuration with external data store                      |
| OPENAM-21003 | IE11 not working during SAML tree authentication due to use of Arrow function                                |
| OPENAM-18252 | Let nodes update the universal ID for impersonation and peer authentication                                  |
| OPENAM-15834 | Access token call fails when an unsupported claim is requested                                               |
| OPENAM-15410 | Audience claim not able to customize if scope with openid and profile                                        |
| OPENAM-14438 | Ensure OAuth2ClientAgentGroups are imported before OAuth2ClientAgents in Amster                              |
| OPENAM-14217 | Add more debug when getSessionInfo v2.1 fails with Internal Server Error                                     |

#### AM 7.5.x

> **Collapse: AM 7.5.2**
>
> |              |                                                                                                                                         |
> | ------------ | --------------------------------------------------------------------------------------------------------------------------------------- |
> | OPENAM-24543 | The PingOne Protect Initialization node displays an unnecessary form to the end user                                                    |
> | OPENAM-24349 | "Unable to determine key size for key" error occurs when signing an assertion with an explicit signing algorithm configured in the SP   |
> | OPENAM-24335 | The `_queryFilter` Parameter doesn't work for `advancedOAuth2ClientConfig` when scalable OAuth 2.0 clients are enabled                  |
> | OPENAM-24125 | OAuth 2.0 or agent service fails to recover after schema reload required for external app store                                         |
> | OPENAM-24109 | LDAPFilterCondition uses search time limit for request timeout                                                                          |
> | OPENAM-23716 | Policy lookup doesn't error when cache isn't populated and policy store is down                                                         |
> | OPENAM-23595 | Redirect using a URN loses the scheme-specific part                                                                                     |
> | OPENAM-23767 | The `acr_sig` value is read from the PAR object instead of the query parameter                                                          |
> | OPENAM-23766 | Adapter Environment under SP role in the GUI isn't working properly                                                                     |
> | OPENAM-23519 | Android devices without a screen lock not working with WebAuthn registration                                                            |
> | OPENAM-23518 | AuthenticateToTreeConditionAdvice does not work with innerTree as first node                                                            |
> | OPENAM-23441 | Enabling OAuth 2.0 client option "Allow wildcard ports in redirect URIs" prevents application URIs from working                         |
> | OPENAM-23341 | AM doesn't log errors for OIDC or OAuth 2.0 failures                                                                                    |
> | OPENAM-23283 | SecretReferenceCache not used for `am.applications.oauth2.client.%s.secret` labels                                                      |
> | OPENAM-23091 | Fix for `systemEnv.getProperty()` in next-generation scripting                                                                          |
> | OPENAM-22988 | Failover doesn't occur when heartbeat interval is set to `0`                                                                            |
> | OPENAM-22846 | External app/policy store active/passive LB isn't working                                                                               |
> | OPENAM-22657 | JWT validation fails when signed using the RS256 algorithm                                                                              |
> | OPENAM-22654 | BooleanAttributeInputCallback renders an enabled checkbox in AM XUI                                                                     |
> | OPENAM-22630 | Empty webhooks property key results in a NullPointerException                                                                           |
> | OPENAM-22608 | Non-extractable secrets in HSM fails to work on AM for SAML2 XML signing                                                                |
> | OPENAM-22520 | WebAuthN (FIDO Certification): TPM attestation failing when `pubArea.nameAlg` doesn't match the hash used to generate the attested name |
> | OPENAM-22346 | The RP `form_post` endpoint doesn't handle POST data well when OP returns error                                                         |
> | OPENAM-22298 | NullPointerException in `SAML2Utils.verifyNameIDFormat` method                                                                          |
> | OPENAM-22281 | NameIdFormat values populated for remote IdP                                                                                            |
> | OPENAM-22120 | Backchannel logout tokens now include the `exp` claim                                                                                   |
> | OPENAM-20776 | Enable private key jwt audience to be configurable                                                                                      |
> | OPENAM-20239 | Setting the `keepalive` or `heartbeat` interval to a negative value in the IdRepo config causes an error                                |
> | OPENAM-20089 | Configuration Provider nodes don't take integer values                                                                                  |
> | OPENAM-15834 | Access token call fails when an unsupported claim is requested                                                                          |
> | OPENAM-15410 | Audience claim not customizable when scope set to `openid` and `profile`                                                                |

> **Collapse: AM 7.5.1**
>
> |              |                                                                                                                       |
> | ------------ | --------------------------------------------------------------------------------------------------------------------- |
> | IAM-5473     | Always save UI environment variables to `.env` file when using yarn start                                             |
> | IAM-6429     | Failure URL node not working as expected on Safari when used with a Message node                                      |
> | OPENAM-23059 | SSOADM doesn't work for realm defaults                                                                                |
> | OPENAM-22955 | Set Persistent Cookie node causes 500 error before failure                                                            |
> | OPENAM-22847 | Nodes that use a tree hook with an injection annotation cause an error when the tree fails                            |
> | OPENAM-22836 | Unable to update KBA security questions using XUI                                                                     |
> | OPENAM-22753 | Destroy All session may fail to work                                                                                  |
> | OPENAM-22717 | SP-initiated SSO fails with "Illegal character in scheme name" when the IdP entity name has a special character       |
> | OPENAM-22715 | `PlaceholderAnnotationUtils.insertDefaultValueIntoPlaceholder` isn't escaping values correctly                        |
> | OPENAM-22708 | Loop back to the same node causes exception when tree is executed                                                     |
> | OPENAM-22696 | Persistent search notification invalidation on AD identity store doesn't invalidate user cached attributes            |
> | OPENAM-22676 | `SecretsProviderFacadeFactory` is not a supported API but is the only valid way to create the `SecretsProviderFacade` |
> | OPENAM-22675 | Unable to set a default value for NameCallback in next-generation `callbacksBuilder`                                  |
> | OPENAM-22672 | Configuring SAML entities with invalid secret label mappings break SAML flows for other entities                      |
> | OPENAM-22656 | Setting `JWKs URI content cache timeout` to a small value throws an error                                             |
> | OPENAM-22632 | `AMSetupServlet` installation error on Windows multi-domain environment                                               |
> | OPENAM-22620 | Slow response from access token endpoint using client credentials grant                                               |
> | OPENAM-22602 | OIDC ID Token Validator Node isn't using inbuilt `httpClient` settings to connect to JWK or well-known URL            |
> | OPENAM-22465 | Unexpected error when `request_uri` client doesn't match request parameter client in PAR authorise request            |
> | OPENAM-22391 | Issues with `evaluateTree` when using wildcard policies                                                               |
> | OPENAM-22322 | ArtifactResponse Assertion that is signed cannot be verified and fails                                                |
> | OPENAM-22318 | OAUTH\_REQUEST\_ATTRIBUTES cookie isn't getting deleted after authentication                                          |
> | OPENAM-22289 | Session quota action may fail when the session is not updateable but should be fine to proceed.                       |
> | OPENAM-22281 | NameIdFormat values populated for remote IdP                                                                          |
> | OPENAM-22181 | Approve UMA request fails with 500 error when AM deployed as a platform                                               |
> | OPENAM-22171 | Forgotten password fails when AM searches for the identity to modify                                                  |
> | OPENAM-22146 | OAuth 2.0 request object failure not logged for POST requests even when full debug logging is enabled                 |
> | OPENAM-22120 | Backchannel logout tokens now include the `exp` claim                                                                 |
> | OPENAM-22109 | The expiry time of OPS token in 7.x fails to update correctly                                                         |
> | OPENAM-22009 | Providing an invalid alias to a secret store mapping breaks AM                                                        |
> | OPENAM-21972 | SAML artifact binding is failing in load-balanced deployments                                                         |
> | OPENAM-21951 | No option to set the `selectedIndex` on a ChoiceCallback                                                              |
> | OPENAM-21897 | Creation order determines policy evaluate and evaluateTree results                                                    |
> | OPENAM-21864 | No option to enable the `trackingCookie` with next-generation `callbacksBuilder`                                      |
> | OPENAM-21852 | Failure when reading input from next-generation SelectIDPCallback                                                     |
> | OPENAM-21609 | OAuth2Provider service created immediately after install/restart isn't available in code flow                         |
> | OPENAM-21191 | Web agent sessions have a long session lifetime of 42 years                                                           |
> | OPENAM-21158 | Windows Hello registration fails on TPM attestation parsing on Windows 11 22H2                                        |
> | OPENAM-20945 | Unable to trace token revocation back to resource owner because of missing `trackingID` field                         |
> | OPENAM-20609 | Inconsistent error message getting access token when using refresh token after changing username                      |
> | OPENAM-20314 | Social Provider Handler node and Social IdP service use the `sub` claim to search for links to existing accounts      |
> | OPENAM-14438 | Ensure OAuth2ClientAgentGroups are imported before OAuth2ClientAgents in Amster                                       |

> **Collapse: AM 7.5.0**
>
> |              |                                                                                                                                                       |
> | ------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
> | OPENAM-22206 | AM upgrade fails for 7.1.4 and older: Creating UMA PCT Encryption Secret Failed                                                                       |
> | OPENAM-22191 | JUnit jars are bundled in the AM.war release                                                                                                          |
> | OPENAM-22119 | "Access to Java class ScriptedLoggerWrapper prohibited" exception                                                                                     |
> | OPENAM-22101 | UI admin tests are failing since updating secret ID to secret label                                                                                   |
> | OPENAM-22060 | am-config-upgrader: poor performance                                                                                                                  |
> | OPENAM-22035 | Page Nodes don't delete contained nodes when a tree is deleted                                                                                        |
> | OPENAM-22017 | ConfigProviderNode creates node class dynamically leading to native memory leak                                                                       |
> | OPENAM-21976 | Single point of locking contention when doing Client-based session logout                                                                             |
> | OPENAM-21941 | Unable to edit policies in the UI                                                                                                                     |
> | OPENAM-21937 | Quota Enforcement affecting agents sessions that authenticate by tree                                                                                 |
> | OPENAM-21936 | Unable to use Legacy and Next Generation Script in the same authentication tree                                                                       |
> | OPENAM-21912 | OAuth2/OIDC signing slow with RSA keys when using Google Secret Manager                                                                               |
> | OPENAM-21856 | Introspecting stateless token with IG/Web agents will cause OAuth2ChfException                                                                        |
> | OPENAM-21854 | TermsAndConditionsCallback fails with error on XUI                                                                                                    |
> | OPENAM-21840 | Warning for missing mapping in dynamic secret doesn't warn for missing secret label identifier                                                        |
> | OPENAM-21803 | CertificateUserExtractorNode cannot resolve wrong name when UPN SubjectAltNameExt                                                                     |
> | OPENAM-21780 | Next generation scripting `httpClient` adds "null" as entity to GET requests                                                                          |
> | OPENAM-21748 | Next generation scripting missing "get" wrapper function for HiddenValueCallback                                                                      |
> | OPENAM-21747 | Amster not working after connecting when AM REST call has extra `set-cookie` headers                                                                  |
> | OPENAM-21739 | Running the am-config-upgrader on an empty directory results in unexpected addition of library scripting service                                      |
> | OPENAM-21707 | file-functional-tests: OAuth2Provider doesn't allow setting of default consent agent when scalableAgents are enabled                                  |
> | OPENAM-21693 | Remove default global library script                                                                                                                  |
> | OPENAM-21664 | Upgrade fails to AM 7.4 with an uncaught exception when initialising the PrivilegeIndexStore class                                                    |
> | OPENAM-21506 | Inner Evaluator Tree with Data Store Decision node fails with correct password on first pass when used with Retry Decision node                       |
> | OPENAM-21484 | OAuth2 tokenintrospection response has different claim value types when refresh tokens are introspected                                               |
> | OPENAM-21473 | Certificate collector node: getPortalStyleCert throws exception when cert/header not present                                                          |
> | OPENAM-21389 | Searching algorithm for calculating the reachability of a node in a tree returns incorrect result                                                     |
> | OPENAM-21277 | Running Amster in debug mode doesn't work on Windows                                                                                                  |
> | OPENAM-21053 | User ID is missing from access.audit.json for JWT client authentication flow using `org.forgerock.security.oauth2.enforce.sub.claim.uniqueness=false` |
> | OPENAM-20924 | Reentry cookie when set causes the user to redirect to an incorrect IdP                                                                               |
> | OPENAM-20490 | AESWrapEncryption shows "WARN: AESWrap-encrypted data is less than 16 bytes"                                                                          |
> | OPENAM-20329 | Forgerock JWT Secured Authorization Response Mode for OAuth 2.0 (JARM) not spec compliant                                                             |
> | OPENAM-19999 | ID token as AM session doesn't work with `/authorize` when openid scope is requested                                                                  |
> | OPENAM-19889 | Policy evaluation fails with Agent access token JWT as subject                                                                                        |
> | OPENAM-17816 | 500 Internal Server Error (from NPE) returned for a missing Content-Type header                                                                       |
> | OPENAM-17315 | Update defaults scripts with the change introduced in COMMONS-628                                                                                     |

#### AM 7.4.x

> **Collapse: AM 7.4.2**
>
> |              |                                                                                                                  |
> | ------------ | ---------------------------------------------------------------------------------------------------------------- |
> | OPENAM-23441 | Enabling OAuth2 client option "Allow wildcard ports in redirect URIs" prevents application URIs from working     |
> | OPENAM-23091 | Fix for `systemEnv.getProperty()` in next-generation scripting                                                   |
> | OPENAM-23059 | `ssoadm` doesn't work against realm defaults                                                                     |
> | OPENAM-22988 | Failover doesn't occur when `heartbeat` interval is set to 0                                                     |
> | OPENAM-22846 | External app/policy store active/passive LB isn't working                                                        |
> | OPENAM-22836 | Unable to update KBA security questions using XUI                                                                |
> | OPENAM-22717 | SP-initiated SSO fails with "Illegal character in scheme name" when the IdP entity name has a special character  |
> | OPENAM-22657 | JWT validation fails when signed using the RS256 algorithm                                                       |
> | OPENAM-22632 | AMSetupServlet install error with Windows multi-domain environment                                               |
> | OPENAM-22608 | Non-extractable secrets in HSM fails to work on AM for SAML2 XML signing                                         |
> | OPENAM-22465 | Unexpected error when request\_uri client doesn't match request parameter client in PAR authorise request        |
> | OPENAM-22391 | Issues with `evaluateTree` when using wildcard policies                                                          |
> | OPENAM-22346 | The RP `form_post` endpoint doesn't handle POST data well when OP returns error                                  |
> | OPENAM-22322 | Signed ArtifactResponse Assertion can't be verified and fails                                                    |
> | OPENAM-22318 | OAUTH\_REQUEST\_ATTRIBUTES cookie isn't getting deleted after authentication                                     |
> | OPENAM-22298 | NullPointerException in `SAML2Utils.verifyNameIDFormat` method                                                   |
> | OPENAM-22264 | Add global attribute handling to `ssoadm`                                                                        |
> | OPENAM-22120 | Backchannel logout tokens now include the `exp` claim                                                            |
> | OPENAM-21951 | No option to set the `selectedIndex` on a ChoiceCallback                                                         |
> | OPENAM-21926 | Lockout message is not applied when using Identity Store Decision node                                           |
> | OPENAM-21897 | Creation order determines policy `evaluate` and `evaluateTree` results                                           |
> | OPENAM-21864 | No option to enable the `trackingCookie` with `callbacksBuilder`                                                 |
> | OPENAM-21748 | Next-generation scripting missing "get" wrapper function for HiddenValueCallback                                 |
> | OPENAM-21609 | OAuth2Provider service created immediately after install/restart isn't available in code flow                    |
> | OPENAM-21545 | Unable to create a circle of trust in file-based configuration with external data store                          |
> | OPENAM-20945 | Unable to trace token revocation back to resource owner because of missing `trackingID` field                    |
> | OPENAM-20314 | Social Provider Handler node and Social IdP service use the `sub` claim to search for links to existing accounts |
> | OPENAM-20239 | Setting the `keepalive` or `heartbeat` interval to a negative value in the IdRepo config causes an error         |
> | OPENAM-15834 | Access token call fails when an unsupported claim is requested                                                   |
> | OPENAM-14438 | Ensure OAuth2ClientAgentGroups are imported before OAuth2ClientAgents in Amster                                  |

> **Collapse: AM 7.4.1**
>
> |              |                                                                                                            |
> | ------------ | ---------------------------------------------------------------------------------------------------------- |
> | OPENAM-22753 | Destroy All session may fail to work                                                                       |
> | OPENAM-22715 | PlaceholderAnnotationUtils.insertDefaultValueIntoPlaceholder is not escaping values correctly              |
> | OPENAM-22696 | Persistent search notification invalidation on AD identity store doesn't invalidate user cached attributes |
> | OPENAM-22620 | Slow response from access token endpoint using client credentials grant                                    |
> | OPENAM-22602 | OIDC ID Token Validator node uses own httpClient settings to connect to JWK or well-known URL              |
> | OPENAM-22421 | Webauthn: Windows Hello TPM Attestation failing for Windows 11 22H2                                        |
> | OPENAM-22289 | Session quota action may fail when the session isn't updatable but should be fine to proceed               |
> | OPENAM-22181 | Approve UMA request fails with 500 error when AM deployed as a platform                                    |
> | OPENAM-22171 | Forgotten password fails when AM searches for the identity to modify                                       |
> | OPENAM-22119 | "Access to Java class ScriptedLoggerWrapper prohibited" exception                                          |
> | OPENAM-22109 | The expiry time of OPS token in 7.x doesn't change with the time of tokens created                         |
> | OPENAM-22017 | Configuration Provider node creates node class dynamically leading to native memory leak                   |
> | OPENAM-21976 | Single point of locking contention when doing client-based session logout                                  |
> | OPENAM-21972 | SAML artifact binding is using crosstalk for artifact resolution                                           |
> | OPENAM-21941 | Unable to edit policies in the UI                                                                          |
> | OPENAM-21937 | Quota enforcement affects agent sessions that authenticate by tree                                         |
> | OPENAM-21936 | Unable to use legacy and next-generation scripts in the same authentication tree                           |
> | OPENAM-21868 | ssoadm `create-sub-cfg` not working for AM 7.2+ due to the `context=` field                                |
> | OPENAM-21854 | TermsAndConditionsCallback fails with error on XUI                                                         |
> | OPENAM-21803 | Certificate User Extractor node cannot resolve wrong name when UPN SubjectAltNameExt                       |
> | OPENAM-21780 | Next-generation `httpClient` script binding adds "null" as entity to GET requests                          |
> | OPENAM-21747 | Amster not working after connecting when AM REST call has extra `set-cookie` headers                       |
> | OPENAM-21664 | Upgrade fails to AM 7.4.0 with an uncaught exception when initializing the PrivilegeIndexStore class       |
> | OPENAM-21484 | OAuth 2.0 token introspection response has different claim value types when introspecting refresh tokens   |
> | OPENAM-21473 | Certificate Collector node: getPortalStyleCert throws exception when cert/header not present               |
> | OPENAM-21466 | AM using OIDC social authentication fails to verify ID token if remote JWK\_URIs have duplicate KID        |
> | OPENAM-21277 | Running Amster in debug mode doesn't work on Windows                                                       |
> | OPENAM-21191 | Web agent sessions have a long session lifetime of 42 years                                                |
> | OPENAM-20609 | Inconsistent error message when generating access token using refresh token after changing username        |
> | OPENAM-19999 | ID token as AM session doesn't work with `/authorize` when openid scope is requested                       |
> | OPENAM-19889 | Policy evaluation fails with agent access token JWT as subject                                             |
> | OPENAM-17816 | 500 Internal Server Error (from NPE) returned for a missing Content-Type header                            |

> **Collapse: AM 7.4.0**
>
> |              |                                                                                                                                                  |
> | ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------ |
> | OPENAM-21476 | Persistent Cookie isn't created when using Configuration Provider node                                                                           |
> | OPENAM-21421 | Scripting logger name isn't based on logging hierarchy convention                                                                                |
> | OPENAM-21390 | Fix caching error when a journey switches backend instances to correctly provide data to `nodeState`                                             |
> | OPENAM-21360 | Add `java.util.concurrent.ExecutionException` to AM scripting class allowlist                                                                    |
> | OPENAM-21323 | LDAP (inline) upgrade fails due to policy creation of UssSelfWriteAttributes                                                                     |
> | OPENAM-21304 | Retain request URI values specified during dynamic client registration                                                                           |
> | OPENAM-21164 | Fix type issue of XML String in SAML responses when using a custom adapter                                                                       |
> | OPENAM-21160 | Make sure secure state values are retained when navigating the authentication tree                                                               |
> | OPENAM-21158 | Windows Hello registration fails on TPM attestation parsing on Windows 11 22H2                                                                   |
> | OPENAM-21085 | Undefined bindings are incorrectly evaluated in Groovy scripts                                                                                   |
> | OPENAM-21069 | WindowsDesktopSSO authentication is failing                                                                                                      |
> | OPENAM-21053 | Missing `userId` from Access audit log when `org.forgerock.security.oauth2.enforce.sub.claim.uniqueness=false` in JWT client authentication flow |
> | OPENAM-21030 | Amster CLI doesn't work on Windows                                                                                                               |
> | OPENAM-21010 | Social authentication user profile corrupted when remote OIDC server provides non-English identity claims                                        |
> | OPENAM-21004 | AM will always look for valid session when `scope=openid`                                                                                        |
> | OPENAM-21001 | SAML IdPAccountMapper isn't correctly determined                                                                                                 |
> | OPENAM-20980 | OIDC social provider uses configured issuer instead of wellknown endpoint issuer when using regex comparison                                     |
> | OPENAM-20953 | Return subject attributes correctly when evaluating a policy using a `JwtClaim` as subject type                                                  |
> | OPENAM-20920 | Improve handling of SAML2 IDP metadata that uses SSO endpoint entries other than HTTP-POST or HTTP-Redirect bindings when binding is null        |
> | OPENAM-20897 | Debug logs not showing info for ERROR: Unsupported Callback, "{0}" and others                                                                    |
> | OPENAM-20895 | Newly created Maven archetype project for building custom authentication nodes fails to build                                                    |
> | OPENAM-20851 | Existing registered devices unable to use push notifications when AWS SNS credentials are updated                                                |
> | OPENAM-20784 | TestUMAPolicy fails for users that will cause LocalizedIllegalArgumentException                                                                  |
> | OPENAM-20756 | Social authentication request for Apple fails due to duplicated `response_mode=form_post` request parameter                                      |
> | OPENAM-20691 | Fix rare race condition in session quota destroy next expiring action that can lead to the oldest session not being destroyed                    |
> | OPENAM-20682 | Unable to encrypt from `jwk_uri` where there are multiple JWKs with the same `kid` but different algorithms                                      |
> | OPENAM-20490 | AESWrapEncryption shows "WARN: AESWrap-encrypted data is less than 16 bytes"                                                                     |
> | OPENAM-20451 | Fix to display user-friendly account name during WebAuthn device registration                                                                    |
> | OPENAM-20299 | Fix to make agent authentication honor `com.iplanet.am.session.agentSessionIdleTime`                                                             |
> | OPENAM-20230 | Class allowlisting denies access to permitted classes after running for an extended period of time                                               |
> | OPENAM-20026 | Social IDP with trailing whitespace in the name can't be deleted using the UI                                                                    |
> | OPENAM-20024 | Improve debug logging when login to XUI fails with HTTP 404 JsonValueException from endpoint                                                     |
> | OPENAM-19282 | Recovery Code Display Node works only immediately after Registration node                                                                        |
> | OPENAM-19261 | Fix incorrectly logged errors when introspecting tokens using OAuth 2.0 client credentials grant                                                 |
> | OPENAM-18709 | New `nodeState.getObject` method added to return values stored in both shared and secure state                                                   |
> | OPENAM-18685 | New realm-level configuration setting to remove or skip `subname` claim                                                                          |
> | OPENAM-18004 | Support sequential transaction IDs to improve audit logging for HTTP requests to IDM                                                             |
> | OPENAM-17331 | Push Notifications: User with disabled endpoint is not able to login                                                                             |
> | OPENAM-17179 | Deleting an authentication tree leaves orphaned nodes that prevent deletion of referenced scripts                                                |

#### AM 7.3.x

> **Collapse: AM 7.3.3**
>
> |              |                                                                                                              |
> | ------------ | ------------------------------------------------------------------------------------------------------------ |
> | OPENAM-23519 | Android devices without a screen lock not working with WebAuthn registration                                 |
> | OPENAM-23518 | AuthenticateToTreeConditionAdvice doesn't work with Inner Tree as first node                                 |
> | OPENAM-23441 | Enabling OAuth2 client option "Allow wildcard ports in redirect URIs" prevents application URIs from working |
> | OPENAM-22846 | External app/policy store active/passive LB isn't working                                                    |
> | OPENAM-22654 | BooleanAttributeInputCallback renders an enabled checkbox in AM XUI                                          |
> | OPENAM-22608 | Non-extractable secrets in HSM fails to work on AM for SAML2 XML signing                                     |
> | OPENAM-21026 | OAuth Clients don't work when the redirect uri list contains an invalid uri                                  |
> | OPENAM-20451 | Fix to display user-friendly account name during WebAuthn device registration                                |
> | OPENAM-15834 | Access token call fails when an unsupported claim is requested                                               |

> **Collapse: AM 7.3.2**
>
> |              |                                                                                                                  |
> | ------------ | ---------------------------------------------------------------------------------------------------------------- |
> | OPENAM-22836 | Unable to update KBA Security questions using XUI                                                                |
> | OPENAM-22753 | Destroy All session may fail to work                                                                             |
> | OPENAM-22717 | SP-initiated SSO fails with "Illegal character in scheme name" when IdP name contains a special character        |
> | OPENAM-22696 | Persistent search notification invalidation on AD identity store doesn't invalidate user cached attributes       |
> | OPENAM-22656 | Setting `JWKs URI content cache timeout` to a small value throws an error                                        |
> | OPENAM-22632 | AMSetupServlet install error with Windows multi-domain environment                                               |
> | OPENAM-22602 | OIDC ID Token Validator node uses own `httpClient` settings to connect to JWK or well-known URL                  |
> | OPENAM-22421 | Webauthn: Windows Hello TPM Attestation failing for Windows 11 22H2                                              |
> | OPENAM-22391 | Issues with `evaluateTree` when using wildcard policies                                                          |
> | OPENAM-22322 | Unable to verify signed ArtifactResponse Assertion leading to failure                                            |
> | OPENAM-22318 | OAUTH\_REQUEST\_ATTRIBUTES cookie isn't getting deleted after authentication                                     |
> | OPENAM-22289 | Session quota action may fail when the session isn't updatable but should be fine to proceed                     |
> | OPENAM-22288 | Amster upgrade 7.3.0-to-7.3.x fails with Groovy Exception                                                        |
> | OPENAM-22181 | Approve UMA request fails with 500 error when AM deployed as a platform                                          |
> | OPENAM-22120 | Backchannel logout token doesn't contain `exp` claim                                                             |
> | OPENAM-21972 | SAML artifact binding is failing in load-balanced deployments                                                    |
> | OPENAM-21937 | Quota enforcement affects agent sessions that authenticate by tree                                               |
> | OPENAM-21897 | Creation order determines policy evaluate and evaluateTree results                                               |
> | OPENAM-21473 | Certificate collector node: `getPortalStyleCert` throws exception when cert/header not present                   |
> | OPENAM-21322 | AM console allows creation of entity provider with space at the end of the name                                  |
> | OPENAM-21191 | Web agent sessions have a long session lifetime of 42 years                                                      |
> | OPENAM-21085 | Undefined bindings are incorrectly evaluated in Groovy scripts                                                   |
> | OPENAM-20945 | Unable to trace token revocation back to resource owner because of missing `trackingID` field                    |
> | OPENAM-20314 | Social Provider Handler node and Social IdP service use the `sub` claim to search for links to existing accounts |
> | OPENAM-20299 | Fix to make agent authentication honor `com.iplanet.am.session.agentSessionIdleTime`                             |
> | OPENAM-19261 | Fix incorrectly logged errors when introspecting tokens using OAuth 2.0 client credentials grant                 |

> **Collapse: AM 7.3.1**
>
> |              |                                                                                                                |
> | ------------ | -------------------------------------------------------------------------------------------------------------- |
> | OPENAM-22017 | ConfigProviderNode creates node class dynamically leading to native memory leak                                |
> | OPENAM-21976 | Single point of locking contention when performing client-based session logout                                 |
> | OPENAM-21941 | Unable to edit policies in the UI                                                                              |
> | OPENAM-21854 | TermsAndConditionsCallback fails with error on XUI                                                             |
> | OPENAM-21747 | Rest SDK and Amster send cookies if request has cookie header                                                  |
> | OPENAM-21728 | Certificate module fails using JDK 11.0.21 and later with undefined access to private method                   |
> | OPENAM-21484 | Introspecting OAuth 2.0 refresh tokens results in different claim value types in the response                  |
> | OPENAM-21421 | Scripting logger name isn't based on logging hierarchy convention                                              |
> | OPENAM-21390 | ConsumedStateDataCache can cache an incomplete set of reachability data when on multi-AM environment           |
> | OPENAM-21304 | OAuth 2.0 dynamic client registrations don't retain `request_uri` values when creating                         |
> | OPENAM-21277 | Running Amster in debug mode doesn't work on Windows                                                           |
> | OPENAM-21164 | Calling `toXMLString` in custom SAML adapter can return incorrectly formatted XML leading to invalid signature |
> | OPENAM-21160 | Inconsistent values in secure state when navigating an authentication tree                                     |
> | OPENAM-21158 | Windows Hello registration fails on TPM attestation parsing on Windows 11 22H2                                 |
> | OPENAM-21069 | WindowsDesktopSSO authentication is failing                                                                    |
> | OPENAM-21030 | Amster 7.3.0 CLI isn't working on Windows                                                                      |
> | OPENAM-21010 | Social authentication for remote OIDC server for user profile non-english words corrupted                      |
> | OPENAM-21004 | AM will always look for valid session when scope=openid                                                        |
> | OPENAM-21001 | IdPAccountMapper is not correctly determined                                                                   |
> | OPENAM-20980 | Unable to use issuer comparison check regex in oidc social provider                                            |
> | OPENAM-20897 | Debug logs not showing info for `ERROR: Unsupported Callback, "{0}"` and others                                |
> | OPENAM-20895 | Newly-created Maven archetype project fails to build                                                           |
> | OPENAM-20756 | OIDC social authentication request (Apple) fails due to duplicate `response_mode=form_post` request parameter  |
> | OPENAM-20691 | Destroy oldest session may fail to work                                                                        |
> | OPENAM-20682 | Unable to encrypt from `jwk_uri` when there are duplicate `kid`                                                |
> | OPENAM-20490 | AESWrapEncryption shows "WARN: AESWrap-encrypted data is less than 16 bytes"                                   |
> | OPENAM-20026 | Trailing whitespace prevents social provider deletion via UI                                                   |
> | OPENAM-19999 | ID token as AM session doesn't work with `/authorize` when openid scope is requested                           |
> | OPENAM-19889 | Policy evaluation fails with agent access token JWT as subject                                                 |
> | OPENAM-19282 | Recovery Code Display Node works only immediately after Registration node                                      |
> | OPENAM-18599 | Allow for custom error message if user account is locked                                                       |

> **Collapse: AM 7.3.0**
>
> |              |                                                                                                                     |
> | ------------ | ------------------------------------------------------------------------------------------------------------------- |
> | OPENAM-20396 | Authentication tree is selected by order of acr to tree mapping, not the default values, and order is not preserved |
> | OPENAM-20360 | Ampersand is double encoded in the Destination of a SAML Assertion                                                  |
> | OPENAM-20260 | Unable to log into AM when external application store is down                                                       |
> | OPENAM-20230 | Class allowlisting fails with permission denied after an extended period                                            |
> | OPENAM-20181 | AD account notification fails                                                                                       |
> | OPENAM-20159 | Upgrader adds requestObjectProcessing to OAuth2Provider subconfigs                                                  |
> | OPENAM-20104 | The `fragment` response\_mode for the /oauth2/authorize endpoint is not working                                     |
> | OPENAM-20085 | STS token generation does not work with clustered docker pods                                                       |
> | OPENAM-20082 | Locked out users are shown a misleading error message                                                               |
> | OPENAM-19868 | Correctly handle multi-line text in Email Suspend nodes                                                             |
> | OPENAM-19866 | Excessive logging when accessing protected resources                                                                |
> | OPENAM-19726 | The `par` endpoint doesn't return a `request_uri` when using JAR and claims are provided                            |
> | OPENAM-19665 | Wrong Java version in Amster README file                                                                            |
> | OPENAM-19515 | Unable to update session service with read only identity store                                                      |
> | OPENAM-19411 | Amster installation failure with authorizedKey parameter when trying to overwrite an existing configuration         |
> | OPENAM-18818 | Persistent search error message shows wrong DS identifier                                                           |
> | OPENAM-18488 | Windows Hello with TPM/platform authenticator returns two certificates                                              |
> | OPENAM-18172 | Multiple instances of "No Social Authentication Service found for realm" logged at WARNING level                    |
> | OPENAM-17215 | Policy debug log fills up at very high pace if the config store is not found                                        |
> | OPENAM-13766 | No configuration found for login with SessionConditionAdvice=deny                                                   |

### Fixes in AM 7.5.x

This page lists the cumulative fixes in AM 7.5.x releases:

#### AM 7.5.2

|              |                                                                                                                                         |
| ------------ | --------------------------------------------------------------------------------------------------------------------------------------- |
| OPENAM-24543 | The PingOne Protect Initialization node displays an unnecessary form to the end user                                                    |
| OPENAM-24349 | "Unable to determine key size for key" error occurs when signing an assertion with an explicit signing algorithm configured in the SP   |
| OPENAM-24335 | The `_queryFilter` Parameter doesn't work for `advancedOAuth2ClientConfig` when scalable OAuth 2.0 clients are enabled                  |
| OPENAM-24125 | OAuth 2.0 or agent service fails to recover after schema reload required for external app store                                         |
| OPENAM-24109 | LDAPFilterCondition uses search time limit for request timeout                                                                          |
| OPENAM-23716 | Policy lookup doesn't error when cache isn't populated and policy store is down                                                         |
| OPENAM-23595 | Redirect using a URN loses the scheme-specific part                                                                                     |
| OPENAM-23767 | The `acr_sig` value is read from the PAR object instead of the query parameter                                                          |
| OPENAM-23766 | Adapter Environment under SP role in the GUI isn't working properly                                                                     |
| OPENAM-23519 | Android devices without a screen lock not working with WebAuthn registration                                                            |
| OPENAM-23518 | AuthenticateToTreeConditionAdvice does not work with innerTree as first node                                                            |
| OPENAM-23441 | Enabling OAuth 2.0 client option "Allow wildcard ports in redirect URIs" prevents application URIs from working                         |
| OPENAM-23341 | AM doesn't log errors for OIDC or OAuth 2.0 failures                                                                                    |
| OPENAM-23283 | SecretReferenceCache not used for `am.applications.oauth2.client.%s.secret` labels                                                      |
| OPENAM-23091 | Fix for `systemEnv.getProperty()` in next-generation scripting                                                                          |
| OPENAM-22988 | Failover doesn't occur when heartbeat interval is set to `0`                                                                            |
| OPENAM-22846 | External app/policy store active/passive LB isn't working                                                                               |
| OPENAM-22657 | JWT validation fails when signed using the RS256 algorithm                                                                              |
| OPENAM-22654 | BooleanAttributeInputCallback renders an enabled checkbox in AM XUI                                                                     |
| OPENAM-22630 | Empty webhooks property key results in a NullPointerException                                                                           |
| OPENAM-22608 | Non-extractable secrets in HSM fails to work on AM for SAML2 XML signing                                                                |
| OPENAM-22520 | WebAuthN (FIDO Certification): TPM attestation failing when `pubArea.nameAlg` doesn't match the hash used to generate the attested name |
| OPENAM-22346 | The RP `form_post` endpoint doesn't handle POST data well when OP returns error                                                         |
| OPENAM-22298 | NullPointerException in `SAML2Utils.verifyNameIDFormat` method                                                                          |
| OPENAM-22281 | NameIdFormat values populated for remote IdP                                                                                            |
| OPENAM-22120 | Backchannel logout tokens now include the `exp` claim                                                                                   |
| OPENAM-20776 | Enable private key jwt audience to be configurable                                                                                      |
| OPENAM-20239 | Setting the `keepalive` or `heartbeat` interval to a negative value in the IdRepo config causes an error                                |
| OPENAM-20089 | Configuration Provider nodes don't take integer values                                                                                  |
| OPENAM-15834 | Access token call fails when an unsupported claim is requested                                                                          |
| OPENAM-15410 | Audience claim not customizable when scope set to `openid` and `profile`                                                                |

#### AM 7.5.1

|              |                                                                                                                       |
| ------------ | --------------------------------------------------------------------------------------------------------------------- |
| IAM-5473     | Always save UI environment variables to `.env` file when using yarn start                                             |
| IAM-6429     | Failure URL node not working as expected on Safari when used with a Message node                                      |
| OPENAM-23059 | SSOADM doesn't work for realm defaults                                                                                |
| OPENAM-22955 | Set Persistent Cookie node causes 500 error before failure                                                            |
| OPENAM-22847 | Nodes that use a tree hook with an injection annotation cause an error when the tree fails                            |
| OPENAM-22836 | Unable to update KBA security questions using XUI                                                                     |
| OPENAM-22753 | Destroy All session may fail to work                                                                                  |
| OPENAM-22717 | SP-initiated SSO fails with "Illegal character in scheme name" when the IdP entity name has a special character       |
| OPENAM-22715 | `PlaceholderAnnotationUtils.insertDefaultValueIntoPlaceholder` isn't escaping values correctly                        |
| OPENAM-22708 | Loop back to the same node causes exception when tree is executed                                                     |
| OPENAM-22696 | Persistent search notification invalidation on AD identity store doesn't invalidate user cached attributes            |
| OPENAM-22676 | `SecretsProviderFacadeFactory` is not a supported API but is the only valid way to create the `SecretsProviderFacade` |
| OPENAM-22675 | Unable to set a default value for NameCallback in next-generation `callbacksBuilder`                                  |
| OPENAM-22672 | Configuring SAML entities with invalid secret label mappings break SAML flows for other entities                      |
| OPENAM-22656 | Setting `JWKs URI content cache timeout` to a small value throws an error                                             |
| OPENAM-22632 | `AMSetupServlet` installation error on Windows multi-domain environment                                               |
| OPENAM-22620 | Slow response from access token endpoint using client credentials grant                                               |
| OPENAM-22602 | OIDC ID Token Validator Node isn't using inbuilt `httpClient` settings to connect to JWK or well-known URL            |
| OPENAM-22465 | Unexpected error when `request_uri` client doesn't match request parameter client in PAR authorise request            |
| OPENAM-22391 | Issues with `evaluateTree` when using wildcard policies                                                               |
| OPENAM-22322 | ArtifactResponse Assertion that is signed cannot be verified and fails                                                |
| OPENAM-22318 | OAUTH\_REQUEST\_ATTRIBUTES cookie isn't getting deleted after authentication                                          |
| OPENAM-22289 | Session quota action may fail when the session is not updateable but should be fine to proceed.                       |
| OPENAM-22281 | NameIdFormat values populated for remote IdP                                                                          |
| OPENAM-22181 | Approve UMA request fails with 500 error when AM deployed as a platform                                               |
| OPENAM-22171 | Forgotten password fails when AM searches for the identity to modify                                                  |
| OPENAM-22146 | OAuth 2.0 request object failure not logged for POST requests even when full debug logging is enabled                 |
| OPENAM-22120 | Backchannel logout tokens now include the `exp` claim                                                                 |
| OPENAM-22109 | The expiry time of OPS token in 7.x fails to update correctly                                                         |
| OPENAM-22009 | Providing an invalid alias to a secret store mapping breaks AM                                                        |
| OPENAM-21972 | SAML artifact binding is failing in load-balanced deployments                                                         |
| OPENAM-21951 | No option to set the `selectedIndex` on a ChoiceCallback                                                              |
| OPENAM-21897 | Creation order determines policy evaluate and evaluateTree results                                                    |
| OPENAM-21864 | No option to enable the `trackingCookie` with next-generation `callbacksBuilder`                                      |
| OPENAM-21852 | Failure when reading input from next-generation SelectIDPCallback                                                     |
| OPENAM-21609 | OAuth2Provider service created immediately after install/restart isn't available in code flow                         |
| OPENAM-21191 | Web agent sessions have a long session lifetime of 42 years                                                           |
| OPENAM-21158 | Windows Hello registration fails on TPM attestation parsing on Windows 11 22H2                                        |
| OPENAM-20945 | Unable to trace token revocation back to resource owner because of missing `trackingID` field                         |
| OPENAM-20609 | Inconsistent error message getting access token when using refresh token after changing username                      |
| OPENAM-20314 | Social Provider Handler node and Social IdP service use the `sub` claim to search for links to existing accounts      |
| OPENAM-14438 | Ensure OAuth2ClientAgentGroups are imported before OAuth2ClientAgents in Amster                                       |

#### AM 7.5.0

|              |                                                                                                                                                       |
| ------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
| OPENAM-22206 | AM upgrade fails for 7.1.4 and older: Creating UMA PCT Encryption Secret Failed                                                                       |
| OPENAM-22191 | JUnit jars are bundled in the AM.war release                                                                                                          |
| OPENAM-22119 | "Access to Java class ScriptedLoggerWrapper prohibited" exception                                                                                     |
| OPENAM-22101 | UI admin tests are failing since updating secret ID to secret label                                                                                   |
| OPENAM-22060 | am-config-upgrader: poor performance                                                                                                                  |
| OPENAM-22035 | Page Nodes don't delete contained nodes when a tree is deleted                                                                                        |
| OPENAM-22017 | ConfigProviderNode creates node class dynamically leading to native memory leak                                                                       |
| OPENAM-21976 | Single point of locking contention when doing Client-based session logout                                                                             |
| OPENAM-21941 | Unable to edit policies in the UI                                                                                                                     |
| OPENAM-21937 | Quota Enforcement affecting agents sessions that authenticate by tree                                                                                 |
| OPENAM-21936 | Unable to use Legacy and Next Generation Script in the same authentication tree                                                                       |
| OPENAM-21912 | OAuth2/OIDC signing slow with RSA keys when using Google Secret Manager                                                                               |
| OPENAM-21856 | Introspecting stateless token with IG/Web agents will cause OAuth2ChfException                                                                        |
| OPENAM-21854 | TermsAndConditionsCallback fails with error on XUI                                                                                                    |
| OPENAM-21840 | Warning for missing mapping in dynamic secret doesn't warn for missing secret label identifier                                                        |
| OPENAM-21803 | CertificateUserExtractorNode cannot resolve wrong name when UPN SubjectAltNameExt                                                                     |
| OPENAM-21780 | Next generation scripting `httpClient` adds "null" as entity to GET requests                                                                          |
| OPENAM-21748 | Next generation scripting missing "get" wrapper function for HiddenValueCallback                                                                      |
| OPENAM-21747 | Amster not working after connecting when AM REST call has extra `set-cookie` headers                                                                  |
| OPENAM-21739 | Running the am-config-upgrader on an empty directory results in unexpected addition of library scripting service                                      |
| OPENAM-21707 | file-functional-tests: OAuth2Provider doesn't allow setting of default consent agent when scalableAgents are enabled                                  |
| OPENAM-21693 | Remove default global library script                                                                                                                  |
| OPENAM-21664 | Upgrade fails to AM 7.4 with an uncaught exception when initialising the PrivilegeIndexStore class                                                    |
| OPENAM-21506 | Inner Evaluator Tree with Data Store Decision node fails with correct password on first pass when used with Retry Decision node                       |
| OPENAM-21484 | OAuth2 tokenintrospection response has different claim value types when refresh tokens are introspected                                               |
| OPENAM-21473 | Certificate collector node: getPortalStyleCert throws exception when cert/header not present                                                          |
| OPENAM-21389 | Searching algorithm for calculating the reachability of a node in a tree returns incorrect result                                                     |
| OPENAM-21277 | Running Amster in debug mode doesn't work on Windows                                                                                                  |
| OPENAM-21053 | User ID is missing from access.audit.json for JWT client authentication flow using `org.forgerock.security.oauth2.enforce.sub.claim.uniqueness=false` |
| OPENAM-20924 | Reentry cookie when set causes the user to redirect to an incorrect IdP                                                                               |
| OPENAM-20490 | AESWrapEncryption shows "WARN: AESWrap-encrypted data is less than 16 bytes"                                                                          |
| OPENAM-20329 | Forgerock JWT Secured Authorization Response Mode for OAuth 2.0 (JARM) not spec compliant                                                             |
| OPENAM-19999 | ID token as AM session doesn't work with `/authorize` when openid scope is requested                                                                  |
| OPENAM-19889 | Policy evaluation fails with Agent access token JWT as subject                                                                                        |
| OPENAM-17816 | 500 Internal Server Error (from NPE) returned for a missing Content-Type header                                                                       |
| OPENAM-17315 | Update defaults scripts with the change introduced in COMMONS-628                                                                                     |

#### AM 7.4.x

> **Collapse: AM 7.4.2**
>
> |              |                                                                                                                  |
> | ------------ | ---------------------------------------------------------------------------------------------------------------- |
> | OPENAM-23441 | Enabling OAuth2 client option "Allow wildcard ports in redirect URIs" prevents application URIs from working     |
> | OPENAM-23091 | Fix for `systemEnv.getProperty()` in next-generation scripting                                                   |
> | OPENAM-23059 | `ssoadm` doesn't work against realm defaults                                                                     |
> | OPENAM-22988 | Failover doesn't occur when `heartbeat` interval is set to 0                                                     |
> | OPENAM-22846 | External app/policy store active/passive LB isn't working                                                        |
> | OPENAM-22836 | Unable to update KBA security questions using XUI                                                                |
> | OPENAM-22717 | SP-initiated SSO fails with "Illegal character in scheme name" when the IdP entity name has a special character  |
> | OPENAM-22657 | JWT validation fails when signed using the RS256 algorithm                                                       |
> | OPENAM-22632 | AMSetupServlet install error with Windows multi-domain environment                                               |
> | OPENAM-22608 | Non-extractable secrets in HSM fails to work on AM for SAML2 XML signing                                         |
> | OPENAM-22465 | Unexpected error when request\_uri client doesn't match request parameter client in PAR authorise request        |
> | OPENAM-22391 | Issues with `evaluateTree` when using wildcard policies                                                          |
> | OPENAM-22346 | The RP `form_post` endpoint doesn't handle POST data well when OP returns error                                  |
> | OPENAM-22322 | Signed ArtifactResponse Assertion can't be verified and fails                                                    |
> | OPENAM-22318 | OAUTH\_REQUEST\_ATTRIBUTES cookie isn't getting deleted after authentication                                     |
> | OPENAM-22298 | NullPointerException in `SAML2Utils.verifyNameIDFormat` method                                                   |
> | OPENAM-22264 | Add global attribute handling to `ssoadm`                                                                        |
> | OPENAM-22120 | Backchannel logout tokens now include the `exp` claim                                                            |
> | OPENAM-21951 | No option to set the `selectedIndex` on a ChoiceCallback                                                         |
> | OPENAM-21926 | Lockout message is not applied when using Identity Store Decision node                                           |
> | OPENAM-21897 | Creation order determines policy `evaluate` and `evaluateTree` results                                           |
> | OPENAM-21864 | No option to enable the `trackingCookie` with `callbacksBuilder`                                                 |
> | OPENAM-21748 | Next-generation scripting missing "get" wrapper function for HiddenValueCallback                                 |
> | OPENAM-21609 | OAuth2Provider service created immediately after install/restart isn't available in code flow                    |
> | OPENAM-21545 | Unable to create a circle of trust in file-based configuration with external data store                          |
> | OPENAM-20945 | Unable to trace token revocation back to resource owner because of missing `trackingID` field                    |
> | OPENAM-20314 | Social Provider Handler node and Social IdP service use the `sub` claim to search for links to existing accounts |
> | OPENAM-20239 | Setting the `keepalive` or `heartbeat` interval to a negative value in the IdRepo config causes an error         |
> | OPENAM-15834 | Access token call fails when an unsupported claim is requested                                                   |
> | OPENAM-14438 | Ensure OAuth2ClientAgentGroups are imported before OAuth2ClientAgents in Amster                                  |

> **Collapse: AM 7.4.1**
>
> |              |                                                                                                            |
> | ------------ | ---------------------------------------------------------------------------------------------------------- |
> | OPENAM-22753 | Destroy All session may fail to work                                                                       |
> | OPENAM-22715 | PlaceholderAnnotationUtils.insertDefaultValueIntoPlaceholder is not escaping values correctly              |
> | OPENAM-22696 | Persistent search notification invalidation on AD identity store doesn't invalidate user cached attributes |
> | OPENAM-22620 | Slow response from access token endpoint using client credentials grant                                    |
> | OPENAM-22602 | OIDC ID Token Validator node uses own httpClient settings to connect to JWK or well-known URL              |
> | OPENAM-22421 | Webauthn: Windows Hello TPM Attestation failing for Windows 11 22H2                                        |
> | OPENAM-22289 | Session quota action may fail when the session isn't updatable but should be fine to proceed               |
> | OPENAM-22181 | Approve UMA request fails with 500 error when AM deployed as a platform                                    |
> | OPENAM-22171 | Forgotten password fails when AM searches for the identity to modify                                       |
> | OPENAM-22119 | "Access to Java class ScriptedLoggerWrapper prohibited" exception                                          |
> | OPENAM-22109 | The expiry time of OPS token in 7.x doesn't change with the time of tokens created                         |
> | OPENAM-22017 | Configuration Provider node creates node class dynamically leading to native memory leak                   |
> | OPENAM-21976 | Single point of locking contention when doing client-based session logout                                  |
> | OPENAM-21972 | SAML artifact binding is using crosstalk for artifact resolution                                           |
> | OPENAM-21941 | Unable to edit policies in the UI                                                                          |
> | OPENAM-21937 | Quota enforcement affects agent sessions that authenticate by tree                                         |
> | OPENAM-21936 | Unable to use legacy and next-generation scripts in the same authentication tree                           |
> | OPENAM-21868 | ssoadm `create-sub-cfg` not working for AM 7.2+ due to the `context=` field                                |
> | OPENAM-21854 | TermsAndConditionsCallback fails with error on XUI                                                         |
> | OPENAM-21803 | Certificate User Extractor node cannot resolve wrong name when UPN SubjectAltNameExt                       |
> | OPENAM-21780 | Next-generation `httpClient` script binding adds "null" as entity to GET requests                          |
> | OPENAM-21747 | Amster not working after connecting when AM REST call has extra `set-cookie` headers                       |
> | OPENAM-21664 | Upgrade fails to AM 7.4.0 with an uncaught exception when initializing the PrivilegeIndexStore class       |
> | OPENAM-21484 | OAuth 2.0 token introspection response has different claim value types when introspecting refresh tokens   |
> | OPENAM-21473 | Certificate Collector node: getPortalStyleCert throws exception when cert/header not present               |
> | OPENAM-21466 | AM using OIDC social authentication fails to verify ID token if remote JWK\_URIs have duplicate KID        |
> | OPENAM-21277 | Running Amster in debug mode doesn't work on Windows                                                       |
> | OPENAM-21191 | Web agent sessions have a long session lifetime of 42 years                                                |
> | OPENAM-20609 | Inconsistent error message when generating access token using refresh token after changing username        |
> | OPENAM-19999 | ID token as AM session doesn't work with `/authorize` when openid scope is requested                       |
> | OPENAM-19889 | Policy evaluation fails with agent access token JWT as subject                                             |
> | OPENAM-17816 | 500 Internal Server Error (from NPE) returned for a missing Content-Type header                            |

> **Collapse: AM 7.4.0**
>
> |              |                                                                                                                                                  |
> | ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------ |
> | OPENAM-21476 | Persistent Cookie isn't created when using Configuration Provider node                                                                           |
> | OPENAM-21421 | Scripting logger name isn't based on logging hierarchy convention                                                                                |
> | OPENAM-21390 | Fix caching error when a journey switches backend instances to correctly provide data to `nodeState`                                             |
> | OPENAM-21360 | Add `java.util.concurrent.ExecutionException` to AM scripting class allowlist                                                                    |
> | OPENAM-21323 | LDAP (inline) upgrade fails due to policy creation of UssSelfWriteAttributes                                                                     |
> | OPENAM-21304 | Retain request URI values specified during dynamic client registration                                                                           |
> | OPENAM-21164 | Fix type issue of XML String in SAML responses when using a custom adapter                                                                       |
> | OPENAM-21160 | Make sure secure state values are retained when navigating the authentication tree                                                               |
> | OPENAM-21158 | Windows Hello registration fails on TPM attestation parsing on Windows 11 22H2                                                                   |
> | OPENAM-21085 | Undefined bindings are incorrectly evaluated in Groovy scripts                                                                                   |
> | OPENAM-21069 | WindowsDesktopSSO authentication is failing                                                                                                      |
> | OPENAM-21053 | Missing `userId` from Access audit log when `org.forgerock.security.oauth2.enforce.sub.claim.uniqueness=false` in JWT client authentication flow |
> | OPENAM-21030 | Amster CLI doesn't work on Windows                                                                                                               |
> | OPENAM-21010 | Social authentication user profile corrupted when remote OIDC server provides non-English identity claims                                        |
> | OPENAM-21004 | AM will always look for valid session when `scope=openid`                                                                                        |
> | OPENAM-21001 | SAML IdPAccountMapper isn't correctly determined                                                                                                 |
> | OPENAM-20980 | OIDC social provider uses configured issuer instead of wellknown endpoint issuer when using regex comparison                                     |
> | OPENAM-20953 | Return subject attributes correctly when evaluating a policy using a `JwtClaim` as subject type                                                  |
> | OPENAM-20920 | Improve handling of SAML2 IDP metadata that uses SSO endpoint entries other than HTTP-POST or HTTP-Redirect bindings when binding is null        |
> | OPENAM-20897 | Debug logs not showing info for ERROR: Unsupported Callback, "{0}" and others                                                                    |
> | OPENAM-20895 | Newly created Maven archetype project for building custom authentication nodes fails to build                                                    |
> | OPENAM-20851 | Existing registered devices unable to use push notifications when AWS SNS credentials are updated                                                |
> | OPENAM-20784 | TestUMAPolicy fails for users that will cause LocalizedIllegalArgumentException                                                                  |
> | OPENAM-20756 | Social authentication request for Apple fails due to duplicated `response_mode=form_post` request parameter                                      |
> | OPENAM-20691 | Fix rare race condition in session quota destroy next expiring action that can lead to the oldest session not being destroyed                    |
> | OPENAM-20682 | Unable to encrypt from `jwk_uri` where there are multiple JWKs with the same `kid` but different algorithms                                      |
> | OPENAM-20490 | AESWrapEncryption shows "WARN: AESWrap-encrypted data is less than 16 bytes"                                                                     |
> | OPENAM-20451 | Fix to display user-friendly account name during WebAuthn device registration                                                                    |
> | OPENAM-20299 | Fix to make agent authentication honor `com.iplanet.am.session.agentSessionIdleTime`                                                             |
> | OPENAM-20230 | Class allowlisting denies access to permitted classes after running for an extended period of time                                               |
> | OPENAM-20026 | Social IDP with trailing whitespace in the name can't be deleted using the UI                                                                    |
> | OPENAM-20024 | Improve debug logging when login to XUI fails with HTTP 404 JsonValueException from endpoint                                                     |
> | OPENAM-19282 | Recovery Code Display Node works only immediately after Registration node                                                                        |
> | OPENAM-19261 | Fix incorrectly logged errors when introspecting tokens using OAuth 2.0 client credentials grant                                                 |
> | OPENAM-18709 | New `nodeState.getObject` method added to return values stored in both shared and secure state                                                   |
> | OPENAM-18685 | New realm-level configuration setting to remove or skip `subname` claim                                                                          |
> | OPENAM-18004 | Support sequential transaction IDs to improve audit logging for HTTP requests to IDM                                                             |
> | OPENAM-17331 | Push Notifications: User with disabled endpoint is not able to login                                                                             |
> | OPENAM-17179 | Deleting an authentication tree leaves orphaned nodes that prevent deletion of referenced scripts                                                |

#### AM 7.3.x

> **Collapse: AM 7.3.3**
>
> |              |                                                                                                              |
> | ------------ | ------------------------------------------------------------------------------------------------------------ |
> | OPENAM-23519 | Android devices without a screen lock not working with WebAuthn registration                                 |
> | OPENAM-23518 | AuthenticateToTreeConditionAdvice doesn't work with Inner Tree as first node                                 |
> | OPENAM-23441 | Enabling OAuth2 client option "Allow wildcard ports in redirect URIs" prevents application URIs from working |
> | OPENAM-22846 | External app/policy store active/passive LB isn't working                                                    |
> | OPENAM-22654 | BooleanAttributeInputCallback renders an enabled checkbox in AM XUI                                          |
> | OPENAM-22608 | Non-extractable secrets in HSM fails to work on AM for SAML2 XML signing                                     |
> | OPENAM-21026 | OAuth Clients don't work when the redirect uri list contains an invalid uri                                  |
> | OPENAM-20451 | Fix to display user-friendly account name during WebAuthn device registration                                |
> | OPENAM-15834 | Access token call fails when an unsupported claim is requested                                               |

> **Collapse: AM 7.3.2**
>
> |              |                                                                                                                  |
> | ------------ | ---------------------------------------------------------------------------------------------------------------- |
> | OPENAM-22836 | Unable to update KBA Security questions using XUI                                                                |
> | OPENAM-22753 | Destroy All session may fail to work                                                                             |
> | OPENAM-22717 | SP-initiated SSO fails with "Illegal character in scheme name" when IdP name contains a special character        |
> | OPENAM-22696 | Persistent search notification invalidation on AD identity store doesn't invalidate user cached attributes       |
> | OPENAM-22656 | Setting `JWKs URI content cache timeout` to a small value throws an error                                        |
> | OPENAM-22632 | AMSetupServlet install error with Windows multi-domain environment                                               |
> | OPENAM-22602 | OIDC ID Token Validator node uses own `httpClient` settings to connect to JWK or well-known URL                  |
> | OPENAM-22421 | Webauthn: Windows Hello TPM Attestation failing for Windows 11 22H2                                              |
> | OPENAM-22391 | Issues with `evaluateTree` when using wildcard policies                                                          |
> | OPENAM-22322 | Unable to verify signed ArtifactResponse Assertion leading to failure                                            |
> | OPENAM-22318 | OAUTH\_REQUEST\_ATTRIBUTES cookie isn't getting deleted after authentication                                     |
> | OPENAM-22289 | Session quota action may fail when the session isn't updatable but should be fine to proceed                     |
> | OPENAM-22288 | Amster upgrade 7.3.0-to-7.3.x fails with Groovy Exception                                                        |
> | OPENAM-22181 | Approve UMA request fails with 500 error when AM deployed as a platform                                          |
> | OPENAM-22120 | Backchannel logout token doesn't contain `exp` claim                                                             |
> | OPENAM-21972 | SAML artifact binding is failing in load-balanced deployments                                                    |
> | OPENAM-21937 | Quota enforcement affects agent sessions that authenticate by tree                                               |
> | OPENAM-21897 | Creation order determines policy evaluate and evaluateTree results                                               |
> | OPENAM-21473 | Certificate collector node: `getPortalStyleCert` throws exception when cert/header not present                   |
> | OPENAM-21322 | AM console allows creation of entity provider with space at the end of the name                                  |
> | OPENAM-21191 | Web agent sessions have a long session lifetime of 42 years                                                      |
> | OPENAM-21085 | Undefined bindings are incorrectly evaluated in Groovy scripts                                                   |
> | OPENAM-20945 | Unable to trace token revocation back to resource owner because of missing `trackingID` field                    |
> | OPENAM-20314 | Social Provider Handler node and Social IdP service use the `sub` claim to search for links to existing accounts |
> | OPENAM-20299 | Fix to make agent authentication honor `com.iplanet.am.session.agentSessionIdleTime`                             |
> | OPENAM-19261 | Fix incorrectly logged errors when introspecting tokens using OAuth 2.0 client credentials grant                 |

> **Collapse: AM 7.3.1**
>
> |              |                                                                                                                |
> | ------------ | -------------------------------------------------------------------------------------------------------------- |
> | OPENAM-22017 | ConfigProviderNode creates node class dynamically leading to native memory leak                                |
> | OPENAM-21976 | Single point of locking contention when performing client-based session logout                                 |
> | OPENAM-21941 | Unable to edit policies in the UI                                                                              |
> | OPENAM-21854 | TermsAndConditionsCallback fails with error on XUI                                                             |
> | OPENAM-21747 | Rest SDK and Amster send cookies if request has cookie header                                                  |
> | OPENAM-21728 | Certificate module fails using JDK 11.0.21 and later with undefined access to private method                   |
> | OPENAM-21484 | Introspecting OAuth 2.0 refresh tokens results in different claim value types in the response                  |
> | OPENAM-21421 | Scripting logger name isn't based on logging hierarchy convention                                              |
> | OPENAM-21390 | ConsumedStateDataCache can cache an incomplete set of reachability data when on multi-AM environment           |
> | OPENAM-21304 | OAuth 2.0 dynamic client registrations don't retain `request_uri` values when creating                         |
> | OPENAM-21277 | Running Amster in debug mode doesn't work on Windows                                                           |
> | OPENAM-21164 | Calling `toXMLString` in custom SAML adapter can return incorrectly formatted XML leading to invalid signature |
> | OPENAM-21160 | Inconsistent values in secure state when navigating an authentication tree                                     |
> | OPENAM-21158 | Windows Hello registration fails on TPM attestation parsing on Windows 11 22H2                                 |
> | OPENAM-21069 | WindowsDesktopSSO authentication is failing                                                                    |
> | OPENAM-21030 | Amster 7.3.0 CLI isn't working on Windows                                                                      |
> | OPENAM-21010 | Social authentication for remote OIDC server for user profile non-english words corrupted                      |
> | OPENAM-21004 | AM will always look for valid session when scope=openid                                                        |
> | OPENAM-21001 | IdPAccountMapper is not correctly determined                                                                   |
> | OPENAM-20980 | Unable to use issuer comparison check regex in oidc social provider                                            |
> | OPENAM-20897 | Debug logs not showing info for `ERROR: Unsupported Callback, "{0}"` and others                                |
> | OPENAM-20895 | Newly-created Maven archetype project fails to build                                                           |
> | OPENAM-20756 | OIDC social authentication request (Apple) fails due to duplicate `response_mode=form_post` request parameter  |
> | OPENAM-20691 | Destroy oldest session may fail to work                                                                        |
> | OPENAM-20682 | Unable to encrypt from `jwk_uri` when there are duplicate `kid`                                                |
> | OPENAM-20490 | AESWrapEncryption shows "WARN: AESWrap-encrypted data is less than 16 bytes"                                   |
> | OPENAM-20026 | Trailing whitespace prevents social provider deletion via UI                                                   |
> | OPENAM-19999 | ID token as AM session doesn't work with `/authorize` when openid scope is requested                           |
> | OPENAM-19889 | Policy evaluation fails with agent access token JWT as subject                                                 |
> | OPENAM-19282 | Recovery Code Display Node works only immediately after Registration node                                      |
> | OPENAM-18599 | Allow for custom error message if user account is locked                                                       |

> **Collapse: AM 7.3.0**
>
> |              |                                                                                                                     |
> | ------------ | ------------------------------------------------------------------------------------------------------------------- |
> | OPENAM-20396 | Authentication tree is selected by order of acr to tree mapping, not the default values, and order is not preserved |
> | OPENAM-20360 | Ampersand is double encoded in the Destination of a SAML Assertion                                                  |
> | OPENAM-20260 | Unable to log into AM when external application store is down                                                       |
> | OPENAM-20230 | Class allowlisting fails with permission denied after an extended period                                            |
> | OPENAM-20181 | AD account notification fails                                                                                       |
> | OPENAM-20159 | Upgrader adds requestObjectProcessing to OAuth2Provider subconfigs                                                  |
> | OPENAM-20104 | The `fragment` response\_mode for the /oauth2/authorize endpoint is not working                                     |
> | OPENAM-20085 | STS token generation does not work with clustered docker pods                                                       |
> | OPENAM-20082 | Locked out users are shown a misleading error message                                                               |
> | OPENAM-19868 | Correctly handle multi-line text in Email Suspend nodes                                                             |
> | OPENAM-19866 | Excessive logging when accessing protected resources                                                                |
> | OPENAM-19726 | The `par` endpoint doesn't return a `request_uri` when using JAR and claims are provided                            |
> | OPENAM-19665 | Wrong Java version in Amster README file                                                                            |
> | OPENAM-19515 | Unable to update session service with read only identity store                                                      |
> | OPENAM-19411 | Amster installation failure with authorizedKey parameter when trying to overwrite an existing configuration         |
> | OPENAM-18818 | Persistent search error message shows wrong DS identifier                                                           |
> | OPENAM-18488 | Windows Hello with TPM/platform authenticator returns two certificates                                              |
> | OPENAM-18172 | Multiple instances of "No Social Authentication Service found for realm" logged at WARNING level                    |
> | OPENAM-17215 | Policy debug log fills up at very high pace if the config store is not found                                        |
> | OPENAM-13766 | No configuration found for login with SessionConditionAdvice=deny                                                   |

### Fixes in AM 7.4.x

This page lists the cumulative fixes in AM 7.4.x releases:

#### AM 7.4.2

|              |                                                                                                                  |
| ------------ | ---------------------------------------------------------------------------------------------------------------- |
| OPENAM-23441 | Enabling OAuth2 client option "Allow wildcard ports in redirect URIs" prevents application URIs from working     |
| OPENAM-23091 | Fix for `systemEnv.getProperty()` in next-generation scripting                                                   |
| OPENAM-23059 | `ssoadm` doesn't work against realm defaults                                                                     |
| OPENAM-22988 | Failover doesn't occur when `heartbeat` interval is set to 0                                                     |
| OPENAM-22846 | External app/policy store active/passive LB isn't working                                                        |
| OPENAM-22836 | Unable to update KBA security questions using XUI                                                                |
| OPENAM-22717 | SP-initiated SSO fails with "Illegal character in scheme name" when the IdP entity name has a special character  |
| OPENAM-22657 | JWT validation fails when signed using the RS256 algorithm                                                       |
| OPENAM-22632 | AMSetupServlet install error with Windows multi-domain environment                                               |
| OPENAM-22608 | Non-extractable secrets in HSM fails to work on AM for SAML2 XML signing                                         |
| OPENAM-22465 | Unexpected error when request\_uri client doesn't match request parameter client in PAR authorise request        |
| OPENAM-22391 | Issues with `evaluateTree` when using wildcard policies                                                          |
| OPENAM-22346 | The RP `form_post` endpoint doesn't handle POST data well when OP returns error                                  |
| OPENAM-22322 | Signed ArtifactResponse Assertion can't be verified and fails                                                    |
| OPENAM-22318 | OAUTH\_REQUEST\_ATTRIBUTES cookie isn't getting deleted after authentication                                     |
| OPENAM-22298 | NullPointerException in `SAML2Utils.verifyNameIDFormat` method                                                   |
| OPENAM-22264 | Add global attribute handling to `ssoadm`                                                                        |
| OPENAM-22120 | Backchannel logout tokens now include the `exp` claim                                                            |
| OPENAM-21951 | No option to set the `selectedIndex` on a ChoiceCallback                                                         |
| OPENAM-21926 | Lockout message is not applied when using Identity Store Decision node                                           |
| OPENAM-21897 | Creation order determines policy `evaluate` and `evaluateTree` results                                           |
| OPENAM-21864 | No option to enable the `trackingCookie` with `callbacksBuilder`                                                 |
| OPENAM-21748 | Next-generation scripting missing "get" wrapper function for HiddenValueCallback                                 |
| OPENAM-21609 | OAuth2Provider service created immediately after install/restart isn't available in code flow                    |
| OPENAM-21545 | Unable to create a circle of trust in file-based configuration with external data store                          |
| OPENAM-20945 | Unable to trace token revocation back to resource owner because of missing `trackingID` field                    |
| OPENAM-20314 | Social Provider Handler node and Social IdP service use the `sub` claim to search for links to existing accounts |
| OPENAM-20239 | Setting the `keepalive` or `heartbeat` interval to a negative value in the IdRepo config causes an error         |
| OPENAM-15834 | Access token call fails when an unsupported claim is requested                                                   |
| OPENAM-14438 | Ensure OAuth2ClientAgentGroups are imported before OAuth2ClientAgents in Amster                                  |

#### AM 7.4.1

|              |                                                                                                            |
| ------------ | ---------------------------------------------------------------------------------------------------------- |
| OPENAM-22753 | Destroy All session may fail to work                                                                       |
| OPENAM-22715 | PlaceholderAnnotationUtils.insertDefaultValueIntoPlaceholder is not escaping values correctly              |
| OPENAM-22696 | Persistent search notification invalidation on AD identity store doesn't invalidate user cached attributes |
| OPENAM-22620 | Slow response from access token endpoint using client credentials grant                                    |
| OPENAM-22602 | OIDC ID Token Validator node uses own httpClient settings to connect to JWK or well-known URL              |
| OPENAM-22421 | Webauthn: Windows Hello TPM Attestation failing for Windows 11 22H2                                        |
| OPENAM-22289 | Session quota action may fail when the session isn't updatable but should be fine to proceed               |
| OPENAM-22181 | Approve UMA request fails with 500 error when AM deployed as a platform                                    |
| OPENAM-22171 | Forgotten password fails when AM searches for the identity to modify                                       |
| OPENAM-22119 | "Access to Java class ScriptedLoggerWrapper prohibited" exception                                          |
| OPENAM-22109 | The expiry time of OPS token in 7.x doesn't change with the time of tokens created                         |
| OPENAM-22017 | Configuration Provider node creates node class dynamically leading to native memory leak                   |
| OPENAM-21976 | Single point of locking contention when doing client-based session logout                                  |
| OPENAM-21972 | SAML artifact binding is using crosstalk for artifact resolution                                           |
| OPENAM-21941 | Unable to edit policies in the UI                                                                          |
| OPENAM-21937 | Quota enforcement affects agent sessions that authenticate by tree                                         |
| OPENAM-21936 | Unable to use legacy and next-generation scripts in the same authentication tree                           |
| OPENAM-21868 | ssoadm `create-sub-cfg` not working for AM 7.2+ due to the `context=` field                                |
| OPENAM-21854 | TermsAndConditionsCallback fails with error on XUI                                                         |
| OPENAM-21803 | Certificate User Extractor node cannot resolve wrong name when UPN SubjectAltNameExt                       |
| OPENAM-21780 | Next-generation `httpClient` script binding adds "null" as entity to GET requests                          |
| OPENAM-21747 | Amster not working after connecting when AM REST call has extra `set-cookie` headers                       |
| OPENAM-21664 | Upgrade fails to AM 7.4.0 with an uncaught exception when initializing the PrivilegeIndexStore class       |
| OPENAM-21484 | OAuth 2.0 token introspection response has different claim value types when introspecting refresh tokens   |
| OPENAM-21473 | Certificate Collector node: getPortalStyleCert throws exception when cert/header not present               |
| OPENAM-21466 | AM using OIDC social authentication fails to verify ID token if remote JWK\_URIs have duplicate KID        |
| OPENAM-21277 | Running Amster in debug mode doesn't work on Windows                                                       |
| OPENAM-21191 | Web agent sessions have a long session lifetime of 42 years                                                |
| OPENAM-20609 | Inconsistent error message when generating access token using refresh token after changing username        |
| OPENAM-19999 | ID token as AM session doesn't work with `/authorize` when openid scope is requested                       |
| OPENAM-19889 | Policy evaluation fails with agent access token JWT as subject                                             |
| OPENAM-17816 | 500 Internal Server Error (from NPE) returned for a missing Content-Type header                            |

#### AM 7.4.0

|              |                                                                                                                                                  |
| ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------ |
| OPENAM-21476 | Persistent Cookie isn't created when using Configuration Provider node                                                                           |
| OPENAM-21421 | Scripting logger name isn't based on logging hierarchy convention                                                                                |
| OPENAM-21390 | Fix caching error when a journey switches backend instances to correctly provide data to `nodeState`                                             |
| OPENAM-21360 | Add `java.util.concurrent.ExecutionException` to AM scripting class allowlist                                                                    |
| OPENAM-21323 | LDAP (inline) upgrade fails due to policy creation of UssSelfWriteAttributes                                                                     |
| OPENAM-21304 | Retain request URI values specified during dynamic client registration                                                                           |
| OPENAM-21164 | Fix type issue of XML String in SAML responses when using a custom adapter                                                                       |
| OPENAM-21160 | Make sure secure state values are retained when navigating the authentication tree                                                               |
| OPENAM-21158 | Windows Hello registration fails on TPM attestation parsing on Windows 11 22H2                                                                   |
| OPENAM-21085 | Undefined bindings are incorrectly evaluated in Groovy scripts                                                                                   |
| OPENAM-21069 | WindowsDesktopSSO authentication is failing                                                                                                      |
| OPENAM-21053 | Missing `userId` from Access audit log when `org.forgerock.security.oauth2.enforce.sub.claim.uniqueness=false` in JWT client authentication flow |
| OPENAM-21030 | Amster CLI doesn't work on Windows                                                                                                               |
| OPENAM-21010 | Social authentication user profile corrupted when remote OIDC server provides non-English identity claims                                        |
| OPENAM-21004 | AM will always look for valid session when `scope=openid`                                                                                        |
| OPENAM-21001 | SAML IdPAccountMapper isn't correctly determined                                                                                                 |
| OPENAM-20980 | OIDC social provider uses configured issuer instead of wellknown endpoint issuer when using regex comparison                                     |
| OPENAM-20953 | Return subject attributes correctly when evaluating a policy using a `JwtClaim` as subject type                                                  |
| OPENAM-20920 | Improve handling of SAML2 IDP metadata that uses SSO endpoint entries other than HTTP-POST or HTTP-Redirect bindings when binding is null        |
| OPENAM-20897 | Debug logs not showing info for ERROR: Unsupported Callback, "{0}" and others                                                                    |
| OPENAM-20895 | Newly created Maven archetype project for building custom authentication nodes fails to build                                                    |
| OPENAM-20851 | Existing registered devices unable to use push notifications when AWS SNS credentials are updated                                                |
| OPENAM-20784 | TestUMAPolicy fails for users that will cause LocalizedIllegalArgumentException                                                                  |
| OPENAM-20756 | Social authentication request for Apple fails due to duplicated `response_mode=form_post` request parameter                                      |
| OPENAM-20691 | Fix rare race condition in session quota destroy next expiring action that can lead to the oldest session not being destroyed                    |
| OPENAM-20682 | Unable to encrypt from `jwk_uri` where there are multiple JWKs with the same `kid` but different algorithms                                      |
| OPENAM-20490 | AESWrapEncryption shows "WARN: AESWrap-encrypted data is less than 16 bytes"                                                                     |
| OPENAM-20451 | Fix to display user-friendly account name during WebAuthn device registration                                                                    |
| OPENAM-20299 | Fix to make agent authentication honor `com.iplanet.am.session.agentSessionIdleTime`                                                             |
| OPENAM-20230 | Class allowlisting denies access to permitted classes after running for an extended period of time                                               |
| OPENAM-20026 | Social IDP with trailing whitespace in the name can't be deleted using the UI                                                                    |
| OPENAM-20024 | Improve debug logging when login to XUI fails with HTTP 404 JsonValueException from endpoint                                                     |
| OPENAM-19282 | Recovery Code Display Node works only immediately after Registration node                                                                        |
| OPENAM-19261 | Fix incorrectly logged errors when introspecting tokens using OAuth 2.0 client credentials grant                                                 |
| OPENAM-18709 | New `nodeState.getObject` method added to return values stored in both shared and secure state                                                   |
| OPENAM-18685 | New realm-level configuration setting to remove or skip `subname` claim                                                                          |
| OPENAM-18004 | Support sequential transaction IDs to improve audit logging for HTTP requests to IDM                                                             |
| OPENAM-17331 | Push Notifications: User with disabled endpoint is not able to login                                                                             |
| OPENAM-17179 | Deleting an authentication tree leaves orphaned nodes that prevent deletion of referenced scripts                                                |

#### AM 7.3.x

> **Collapse: AM 7.3.3**
>
> |              |                                                                                                              |
> | ------------ | ------------------------------------------------------------------------------------------------------------ |
> | OPENAM-23519 | Android devices without a screen lock not working with WebAuthn registration                                 |
> | OPENAM-23518 | AuthenticateToTreeConditionAdvice doesn't work with Inner Tree as first node                                 |
> | OPENAM-23441 | Enabling OAuth2 client option "Allow wildcard ports in redirect URIs" prevents application URIs from working |
> | OPENAM-22846 | External app/policy store active/passive LB isn't working                                                    |
> | OPENAM-22654 | BooleanAttributeInputCallback renders an enabled checkbox in AM XUI                                          |
> | OPENAM-22608 | Non-extractable secrets in HSM fails to work on AM for SAML2 XML signing                                     |
> | OPENAM-21026 | OAuth Clients don't work when the redirect uri list contains an invalid uri                                  |
> | OPENAM-20451 | Fix to display user-friendly account name during WebAuthn device registration                                |
> | OPENAM-15834 | Access token call fails when an unsupported claim is requested                                               |

> **Collapse: AM 7.3.1**
>
> |              |                                                                                                                |
> | ------------ | -------------------------------------------------------------------------------------------------------------- |
> | OPENAM-22017 | ConfigProviderNode creates node class dynamically leading to native memory leak                                |
> | OPENAM-21976 | Single point of locking contention when performing client-based session logout                                 |
> | OPENAM-21941 | Unable to edit policies in the UI                                                                              |
> | OPENAM-21854 | TermsAndConditionsCallback fails with error on XUI                                                             |
> | OPENAM-21747 | Rest SDK and Amster send cookies if request has cookie header                                                  |
> | OPENAM-21728 | Certificate module fails using JDK 11.0.21 and later with undefined access to private method                   |
> | OPENAM-21484 | Introspecting OAuth 2.0 refresh tokens results in different claim value types in the response                  |
> | OPENAM-21421 | Scripting logger name isn't based on logging hierarchy convention                                              |
> | OPENAM-21390 | ConsumedStateDataCache can cache an incomplete set of reachability data when on multi-AM environment           |
> | OPENAM-21304 | OAuth 2.0 dynamic client registrations don't retain `request_uri` values when creating                         |
> | OPENAM-21277 | Running Amster in debug mode doesn't work on Windows                                                           |
> | OPENAM-21164 | Calling `toXMLString` in custom SAML adapter can return incorrectly formatted XML leading to invalid signature |
> | OPENAM-21160 | Inconsistent values in secure state when navigating an authentication tree                                     |
> | OPENAM-21158 | Windows Hello registration fails on TPM attestation parsing on Windows 11 22H2                                 |
> | OPENAM-21069 | WindowsDesktopSSO authentication is failing                                                                    |
> | OPENAM-21030 | Amster 7.3.0 CLI isn't working on Windows                                                                      |
> | OPENAM-21010 | Social authentication for remote OIDC server for user profile non-english words corrupted                      |
> | OPENAM-21004 | AM will always look for valid session when scope=openid                                                        |
> | OPENAM-21001 | IdPAccountMapper is not correctly determined                                                                   |
> | OPENAM-20980 | Unable to use issuer comparison check regex in oidc social provider                                            |
> | OPENAM-20897 | Debug logs not showing info for `ERROR: Unsupported Callback, "{0}"` and others                                |
> | OPENAM-20895 | Newly-created Maven archetype project fails to build                                                           |
> | OPENAM-20756 | OIDC social authentication request (Apple) fails due to duplicate `response_mode=form_post` request parameter  |
> | OPENAM-20691 | Destroy oldest session may fail to work                                                                        |
> | OPENAM-20682 | Unable to encrypt from `jwk_uri` when there are duplicate `kid`                                                |
> | OPENAM-20490 | AESWrapEncryption shows "WARN: AESWrap-encrypted data is less than 16 bytes"                                   |
> | OPENAM-20026 | Trailing whitespace prevents social provider deletion via UI                                                   |
> | OPENAM-19999 | ID token as AM session doesn't work with `/authorize` when openid scope is requested                           |
> | OPENAM-19889 | Policy evaluation fails with agent access token JWT as subject                                                 |
> | OPENAM-19282 | Recovery Code Display Node works only immediately after Registration node                                      |
> | OPENAM-18599 | Allow for custom error message if user account is locked                                                       |

> **Collapse: AM 7.3.0**
>
> |              |                                                                                                                     |
> | ------------ | ------------------------------------------------------------------------------------------------------------------- |
> | OPENAM-20396 | Authentication tree is selected by order of acr to tree mapping, not the default values, and order is not preserved |
> | OPENAM-20360 | Ampersand is double encoded in the Destination of a SAML Assertion                                                  |
> | OPENAM-20260 | Unable to log into AM when external application store is down                                                       |
> | OPENAM-20230 | Class allowlisting fails with permission denied after an extended period                                            |
> | OPENAM-20181 | AD account notification fails                                                                                       |
> | OPENAM-20159 | Upgrader adds requestObjectProcessing to OAuth2Provider subconfigs                                                  |
> | OPENAM-20104 | The `fragment` response\_mode for the /oauth2/authorize endpoint is not working                                     |
> | OPENAM-20085 | STS token generation does not work with clustered docker pods                                                       |
> | OPENAM-20082 | Locked out users are shown a misleading error message                                                               |
> | OPENAM-19868 | Correctly handle multi-line text in Email Suspend nodes                                                             |
> | OPENAM-19866 | Excessive logging when accessing protected resources                                                                |
> | OPENAM-19726 | The `par` endpoint doesn't return a `request_uri` when using JAR and claims are provided                            |
> | OPENAM-19665 | Wrong Java version in Amster README file                                                                            |
> | OPENAM-19515 | Unable to update session service with read only identity store                                                      |
> | OPENAM-19411 | Amster installation failure with authorizedKey parameter when trying to overwrite an existing configuration         |
> | OPENAM-18818 | Persistent search error message shows wrong DS identifier                                                           |
> | OPENAM-18488 | Windows Hello with TPM/platform authenticator returns two certificates                                              |
> | OPENAM-18172 | Multiple instances of "No Social Authentication Service found for realm" logged at WARNING level                    |
> | OPENAM-17215 | Policy debug log fills up at very high pace if the config store is not found                                        |
> | OPENAM-13766 | No configuration found for login with SessionConditionAdvice=deny                                                   |

## Removed

The functionality listed here was removed.

### AM 8.1.0

* Command-line tools

  The following command-line tools have been removed:

  * `ampassword`

  * `amverifyarchive`

  * `ssoadm`

  * `configurator.jar`

  * `upgrade.jar`

  `amverifyarchive` was deprecated in AM 5.5. The other tools were deprecated in AM 5.

  > **Collapse: Replacements for removed command-line tools**
  >
  > | Removed tool       | Replacement                                                                                                                                                                                                                                                                                                                                                                                            |
  > | ------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
  > | `ampassword`       | N/A.This tool was only used for password-based encryption prior to the introduction of secret stores.                                                                                                                                                                                                                                                                                                  |
  > | `amverifyarchive`  | N/A.This tool was only used with the deprecated CSV audit event handler.                                                                                                                                                                                                                                                                                                                               |
  > | `ssoadm`           | Use the REST API or Amster to configure AM.Learn more in the [REST API Explorer](https://docs.pingidentity.com/pingam/8.1/am-rest/about-api-explorer.html) and the [Amster entity reference](https://docs.pingidentity.com/pingam/8.1/entity-reference/preface.html).The table [below](removed.html#rest-endpoints-for-ssoadm) provides equivalent REST endpoints for commonly used `ssoadm` commands. |
  > | `configurator.jar` | Install AM with minimal user intervention using file-based configuration (FBC), the REST API, or Amster. Learn more in [Passive install](https://docs.pingidentity.com/pingam/8.1/installation/passive-install.html).                                                                                                                                                                                  |
  > | `upgrade.jar`      | Upgrade AM configuration using the `amupgrade` utility, the upgrade wizard, or over REST. Learn more in [Upgrade the server and configuration](https://docs.pingidentity.com/pingam/8.1/upgrade/upgrade-servers.html#upgrade-config).                                                                                                                                                                  |

  > **Collapse: Replacements for commonly used ssoadm commands**
  >
  > | `ssoadm` commands                                                                                                                                                                                                                                         | Equivalent REST endpoints                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
  > | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  > | `ssoadm clone-server`                                                                                                                                                                                                                                     | `/json/global-config/servers/server id?_action=clone`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
  > | `ssoadm create-server`                                                                                                                                                                                                                                    | `/json/global-config/servers?_action=create`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
  > | `ssoadm delete-server`                                                                                                                                                                                                                                    | `/json/global-config/servers/server id`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
  > | `ssoadm list-servers`                                                                                                                                                                                                                                     | `/json/global-config/servers?_queryFilter=true`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
  > | * `ssoadm remove-server-cfg`
  >
  > * `ssoadm update-server-cfg`
  >
  > * `ssoadm list-server-cfg`
  >
  > * `ssoadm import-server`
  >
  > * `ssoadm export-server`                                                                                                                | `/json/global-config/servers/server id/properties/property type`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
  > | - `ssoadm get-svrcfg-xml`
  >
  > - `ssoadm set-svrcfg-xml`
  >
  > - `ssoadm create-svrcfg-xml`                                                                                                                                                                        | `/json/global-config/servers/server id/properties/directoryConfiguration`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
  > | `ssoadm create-site`                                                                                                                                                                                                                                      | `/json/global-config/sites?_action=create`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
  > | `ssoadm list-sites`                                                                                                                                                                                                                                       | `/json/global-config/sites?_queryFilter=true`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
  > | * `ssoadm add-site-sec-urls`
  >
  > * `ssoadm remove-site-sec-urls`
  >
  > * `ssoadm set-site-pri-url`
  >
  > * `ssoadm set-site-sec-urls`
  >
  > * `ssoadm show-site`
  >
  > * `ssoadm delete-site`                                                                                    | `/json/global-config/sites/site id`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
  > | - `ssoadm add-site-members`
  >
  > - `ssoadm remove-site-members`
  >
  > - `ssoadm show-site-members`                                                                                                                                                                 | `/json/global-config/servers/server id/properties/general`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
  > | `ssoadm create-realm`                                                                                                                                                                                                                                     | `/json/global-config/realms?_action=create`Find more information in [Manage realms](https://docs.pingidentity.com/pingam/8.1/setup/sec-rest-realm-rest.html#rest-api-crud-realm).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
  > | * `ssoadm delete-realm`
  >
  > * `ssoadm set-realm-attrs`
  >
  > * `ssoadm delete-realm-attr`
  >
  > * `ssoadm get-realm`                                                                                                                                                   | `/json/global-config/realms/realm id`Find more information in [Manage realms](https://docs.pingidentity.com/pingam/8.1/setup/sec-rest-realm-rest.html#rest-api-crud-realm).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
  > | `ssoadm list-realms`                                                                                                                                                                                                                                      | `/json/global-config/realms?_queryFilter=true`Find more information in [Manage realms](https://docs.pingidentity.com/pingam/8.1/setup/sec-rest-realm-rest.html#rest-api-crud-realm).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
  > | - `ssoadm create-datastore`
  >
  > - `ssoadm delete-datastores`
  >
  > - `ssoadm list-datastores`
  >
  > - `ssoadm show-datastore`
  >
  > - `ssoadm update-datastore`                                                                                                             | `/json/realms/root/realms/realm name/realm-config/services/id-repositories/datastore type`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
  > | * `ssoadm list-datastore-types`
  >
  > * `ssoadm show-data-types`                                                                                                                                                                                               | `/json/realms/root/realms/realm name/realm-config/services/id-repositories?_action=getCreatableTypes`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
  > | - `ssoadm policy-export`
  >
  > - `ssoadm policy-import`                                                                                                                                                                                                        | The `ssoadm` commands exported and imported the policies, resource types, and policy sets together. Use the following endpoints to manage these individually:- `/json/realms/root/realms/realm name/policies`
  >
  > - `/json/realms/root/realms/realm name/resourcetypes`
  >
  > - `/json/realms/root/realms/realm name/applications`Find more information in [Policies over REST](https://docs.pingidentity.com/pingam/8.1/am-authorization/rest-api-authz-policies.html), [Resource types over REST](https://docs.pingidentity.com/pingam/8.1/am-authorization/rest-api-authz-resource-types.html), and [Policy sets over REST](https://docs.pingidentity.com/pingam/8.1/am-authorization/rest-api-authz-applications.html). |
  > | * `ssoadm create-xacml`
  >
  > * `ssoadm list-xacml`                                                                                                                                                                                                            | `/xacml/realm name/policies`Find more information in [Import and export policies](https://docs.pingidentity.com/pingam/8.1/am-authorization/import-export-policy.html).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
  > | - `ssoadm create-appl`
  >
  > - `ssoadm delete-appls`
  >
  > - `ssoadm list-appls`
  >
  > - `ssoadm set-appl`
  >
  > - `ssoadm show-appl`
  >
  > - `ssoadm delete-xacml`                                                                                                                | `/json/realms/root/realms/realm name/applications`Find more information in [Policy sets over REST](https://docs.pingidentity.com/pingam/8.1/am-authorization/rest-api-authz-applications.html).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
  > | * `ssoadm add-agent-to-grp`
  >
  > * `ssoadm agent-remove-props`
  >
  > * `ssoadm create-agent`
  >
  > * `ssoadm delete-agents`
  >
  > * `ssoadm list-agents`
  >
  > * `ssoadm remove-agent-from-grp`
  >
  > * `ssoadm show-agent`
  >
  > * `ssoadm show-agent-membership`
  >
  > * `ssoadm update-agent` | `/json/realms/root/realms/realm name/realm-config/agents/agent type`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
  > | - `ssoadm create-agent-grp`
  >
  > - `ssoadm delete-agent-grps`
  >
  > - `ssoadm list-agent-grp-members`
  >
  > - `ssoadm list-agent-grps`
  >
  > - `ssoadm show-agent-grp`
  >
  > - `ssoadm update-agent-grp`                                                                          | `/json/realms/root/realms/realm name/realm-config/agents/groups/agent type`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
  > | `ssoadm show-agent-types`                                                                                                                                                                                                                                 | `/json/realms/root/realms/realm name/realm-config/agents?_action=getCreatableTypes`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
  > | * `ssoadm create-identity`
  >
  > * `ssoadm delete-identities`
  >
  > * `ssoadm get-identity`
  >
  > * `ssoadm list-identities`
  >
  > * `ssoadm show-identity-ops`
  >
  > * `ssoadm show-identity-types`                                                                               | - `/json/realms/root/realms/realm name/users`
  >
  > - `/json/realms/root/realms/realm name/groups`Find more information in [Manage identities](https://docs.pingidentity.com/pingam/8.1/setup/sec-rest-realm-rest.html#rest-api-crud-identity).                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
  > | `ssoadm set-identity-attrs`                                                                                                                                                                                                                               | `/json/realms/root/realms/realm name/users/user id`Find more information in [Manage identities](https://docs.pingidentity.com/pingam/8.1/setup/sec-rest-realm-rest.html#rest-api-crud-identity).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
  > | `ssoadm add-privileges`                                                                                                                                                                                                                                   | * `/json/realms/root/realms/realm name/users`
  >
  > * `/json/realms/root/realms/realm name/groups`Find more information in [Delegate privileges over REST](https://docs.pingidentity.com/pingam/8.1/security/securing-administration.html#delegate-privileges-rest).                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
  > | - `ssoadm show-members`
  >
  > - `ssoadm show-privileges`                                                                                                                                                                                                       | `/json/realms/root/realms/realm name/groups/group name`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
  > | `ssoadm show-memberships`                                                                                                                                                                                                                                 | `/json/realms/root/realms/realm name/users/user id/groups`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
  > | * `ssoadm add-svc-identity`
  >
  > * `ssoadm get-identity-svcs`
  >
  > * `ssoadm remove-svc-identity`                                                                                                                                                                 | `/json/realms/root/realms/realm name/users/user id/services`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
  > | - `ssoadm set-identity-svc-attrs`
  >
  > - `ssoadm show-identity-svc-attrs`                                                                                                                                                                                     | `/json/realms/root/realms/realm name/users/user id/services/service name`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
  > | `ssoadm list-identity-assignable-svcs`                                                                                                                                                                                                                    | `/json/realms/root/realms/realm name/users/user id/services?_action=getAllTypes`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
  > | * `ssoadm add-cot-member`
  >
  > * `ssoadm create-cot`
  >
  > * `ssoadm list-cot-members`
  >
  > * `ssoadm remove-cot-member`                                                                                                                                               | `/json/realms/root/realms/realm name/realm-config/federation/circlesoftrust/cot name`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
  > | `ssoadm delete-cot`                                                                                                                                                                                                                                       | `/json/realms/root/realms/realm name/realm-config/federation/circlesoftrust/cot name`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
  > | `ssoadm delete-entity`                                                                                                                                                                                                                                    | `/json/realms/root/realms/realm name/realm-config/saml2/hosted/encoded entity name`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
  > | `ssoadm export-entity`                                                                                                                                                                                                                                    | `/json/realms/root/realms/realm name/realm-config/saml2/hosted/encoded entity name`Alternatively, use the `/ExportSamlMetadata` URL as described in [Export metadata](https://docs.pingidentity.com/pingam/8.1/am-saml2/saml2-providers-and-cots.html#saml-export-metadata).                                                                                                                                                                                                                                                                                                                                                                                                                                        |
  > | `ssoadm import-entity`                                                                                                                                                                                                                                    | `/json/realms/root/realms/realm name/realm-config/saml2/hosted?_action=create`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
  > | `ssoadm list-cots`                                                                                                                                                                                                                                        | `/json/realms/root/realms/realm name/realm-config/federation/circlesoftrust?_queryFilter=true`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
  > | `ssoadm list-entities`                                                                                                                                                                                                                                    | `/json/realms/root/realms/realm name/realm-config/saml2?_queryFilter=true`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
  > | `ssoadm update-entity-keyinfo`                                                                                                                                                                                                                            | `/json/realms/root/realms/realm name/realm-config/saml2/remote?_action=importEntity`Find more information in [Update remote SP certificate](https://docs.pingidentity.com/pingam/8.1/am-saml2/saml2-providers-and-cots.html#update-metadata).                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
  > | - `ssoadm do-bulk-federation`
  >
  > - `ssoadm import-bulk-fed-data`                                                                                                                                                                                            | Use the individual REST endpoints to manage federation entities.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
  > | `ssoadm create-metadata-templ`                                                                                                                                                                                                                            | Use the individual REST endpoints to create entity providers.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |

- SAML v2.0 JSPs

  The following deprecated JSPs have been removed and replaced by URL entry points:

  > **Collapse: JSPs replaced by URLs**
  >
  > | Old URL                                     | New URL               |
  > | ------------------------------------------- | --------------------- |
  > | `/saml2/jsp/exportmetadata.jsp`             | `/ExportSamlMetadata` |
  > | `/saml2/jsp/idpSingleLogoutInit.jsp`        | `/IDPSloInit`         |
  > | `/saml2/jsp/idpSingleLogoutRedirect.jsp`    | `/IDPSloRedirect`     |
  > | `/saml2/jsp/idpSingleLogoutPOST.jsp`        | `/IDPSloPOST`         |
  > | `/saml2/jsp/idpMNIRedirect.jsp`             | `/IDPMniRedirect`     |
  > | `/saml2/jsp/idpMNIRequestInit.jsp`          | `/IDPMniInit`         |
  > | `/saml2/jsp/idpSSOFederate.jsp`             | `/idpSSOFederate`     |
  > | `/saml2/jsp/spAssertionConsumer.jsp`        | `/Consumer`           |
  > | `/saml2/jsp/saml2AuthAssertionConsumer.jsp` | `/AuthConsumer`       |
  > | `/saml2/jsp/spSingleLogoutInit.jsp`         | `/SPSloInit`          |
  > | `/saml2/jsp/spSingleLogoutRedirect.jsp`     | `/SPSloRedirect`      |
  > | `/saml2/jsp/spSingleLogoutPOST.jsp`         | `/SPSloPOST`          |
  > | `/saml2/jsp/spMNIRedirect.jsp`              | `/SPMniRedirect`      |
  > | `/saml2/jsp/spMNIPOST.jsp`                  | `/SPMniPOST`          |
  > | `/saml2/jsp/spMNIRequestInit.jsp`           | `/SPMniInit`          |
  > | `/saml2/jsp/spSSOInit.jsp`                  | `/spssoinit`          |
  > | `/saml2/jsp/idpSSOInit.jsp`                 | `/idpssoinit`         |
  > | `/saml2/jsp/idpSSOFederate.jsp`             | `/idpSSOFederate`     |
  > | `/saml2/jsp/SA_IDP.jsp`                     | `/idpsaehandler`      |
  > | `/saml2/jsp/SA_SP.jsp`                      | `/spsaehandler`       |

  |   |                                                                                                                                             |
  | - | ------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | You can still invoke the JSPs because they're mapped to URLs for backward compatibility, but any customizations to these JSPs will be lost. |

### AM 8.0

* Authentication modules and chains

  We've removed authentication modules and chains. They were [deprecated in AM 7](archive-deprecated.html#deprecated-since-am-7).

  For this release only, it's possible to temporarily re-enable modules and chains for migration purposes. Learn more in [Authentication modules and chains](changes-8.0.html#modules-and-chains).

* Embedded DS

  The embedded DS server has been removed.

  It was [deprecated in AM 7](archive-deprecated.html#deprecated-since-am-7) for use in production.

* Legacy audit logging service

  The legacy audit logging service was [deprecated in AM 7.2](archive-deprecated.html#deprecated-since-am-7.2) and is no longer supported.

* SOAP STS service

  The SOAP STS service has been removed.

  It was [deprecated in AM 7](archive-deprecated.html#deprecated-since-am-7).

### AM 7.5

* Java 11

  AM 7.5 removes support for Java 11. Only Java 17 is supported in this release.

* SNMP monitoring

  SNMP monitoring was [deprecated in AM 7.3](archive-deprecated.html#deprecated-since-am-7.3) and is no longer supported.

## Changes

### Changes in AM 8.1.x

#### AM 8.1

##### OpenTelemetry changes

Root spans in `traceparent` headers now include the W3C Trace Context Level 2 [random trace ID flag](https://www.w3.org/TR/trace-context-2/#random-trace-id-flag) (`0×03` instead of `0×01`). This change is backward-compatible; no action is required unless you have integrations that check trace flag values exactly.

Find more information about collecting distributed tracing data in [Trace incoming and outgoing requests](https://docs.pingidentity.com/pingam/8.1/monitoring/trace-requests.html).

##### Scope validation plugin script

The OAuth 2.0 scope validation script now ensures that refresh tokens can only obtain access tokens with identical or narrower scopes.

This aligns more closely with the OAuth 2.0 specification and the Java implementation.

To re-enable the previous behavior, set the `am.oauth2.grant.validated.scopes.on.refresh` advanced server property to `false`.

##### SAML v2.0 SSO flows

In SAML v2.0 single sign-on (SSO) flows, the JSON web token (JWT) created in the browser's session storage no longer expires.

The time allowed to complete the SSO flow is now determined by the configurable [maximum duration](https://docs.pingidentity.com/pingam/8.1/authentication-guide/authn-suspended.html#maximum-duration) of the journey session instead of the JWT expiration.

Previously, the JWT expired when the cache was cleared. By default, the cache is cleared every 10 minutes, but this is configurable using the [Cache cleanup interval (in seconds)](https://docs.pingidentity.com/pingam/8.1/reference/services-configuration.html#global-saml2) setting.

##### Certificate nodes

We've made changes to the [Certificate Collector](https://docs.pingidentity.com/auth-node-ref/8.1/certificate-collector.html) and [Certificate Validation](https://docs.pingidentity.com/auth-node-ref/8.1/certificate-validation.html) nodes to collect and validate all certificates in a certificate chain by default.

|   |                                                                                                                                                                                                                                                                                                                      |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | In order to validate all certificates in a certificate chain, the intermediate and root certificates from the chain must be added to the truststore.If you send the whole certificate chain in the request, and intermediate or root certificates are missing from the truststore, certificate validation will fail. |

If required, you can revert to the previous behavior of collecting and validating only the user certificate by setting the `am.nodes.certificatechain.validation.enforced` [advanced server property](https://docs.pingidentity.com/pingam/8.1/setup/server-advanced.html#am.nodes.certificatechain.validation.enforced) to `false`.

##### IDM configuration cache enabled

Previously, static IDM configuration wasn't cached by default. The IDM Provisioning service property, [Configuration Cache Duration](https://docs.pingidentity.com/pingam/8.1/reference/services-configuration.html#config-cache-duration), is now set to a short duration of 1 minute by default to improve performance.

##### Servlet and filter declarations

Servlets and filters are now injected and mapped programmatically using Java-based Guice modules, replacing the static declarations in the deployment descriptor, `WEB-INF/web.xml`.

Learn more in [Configure access to endpoints](https://docs.pingidentity.com/pingam/8.1/am-reference/endpoints-reference.html#web-inf-endpoints).

##### Default `kid` values for GSM certificates

For certificates stored in a Google Secret Manager ([GSM secret store](https://docs.pingidentity.com/pingam/8.1/security/secret-stores.html#create-GSM-secret-stores)), the public key published in the JWK\_URI now has a `kid` value that includes the name of the secret. For example:

```json
"kid" : "secrets/secret-name/versions/1"
```

This is a change in behavior. Prior to AM 8.1, the `kid` value contained only the GSM secret *version*, for example:

```json
"kid" : "1"
```

Learn more in [Override default `kid` values](https://docs.pingidentity.com/pingam/8.1/am-oidc1/managing-jwk_uri.html#override-default-kid-values).

##### Parallel updates for CTS sessions

From AM 8.1, parallel updates can't be made for CTS sessions by default. AM checks that the state of the CTS token in the CTS store is different to the state previously read by the thread making the update. This prevents parallel replay attacks from circumventing authentication session allowlisting.

To re-enable the previous behavior, set the [am.cts.use.etag.assertion.on.update](https://docs.pingidentity.com/pingam/8.1/setup/server-advanced.html#am.cts.use.etag.assertion.on.update) advanced server property to `false`.

### Changes in AM 8.0.x

#### AM 8.0

##### Support for Tomcat 10

AM 8.0 supports Apache Tomcat 10 as a web application container. If you use Apache Tomcat, you *must upgrade* to at least version 10 before you upgrade to AM 8.0.

Find more information in [Upgrade Tomcat](https://docs.pingidentity.com/pingam/8/upgrade-guide/upgrade-servers.html#upgrade-tomcat).

As part of this change, you should rewrite scripts that used the `javax.servlet.request.X509Certificate` attribute in the servlet request to obtain the client certificate. Your updated scripts should use the `jakarta.servlet.request.X509Certificate` attribute instead.

##### Authentication modules and chains

Authentication modules and chains have been removed in AM 8.0. If you're still using modules and chains for authentication, you must migrate to nodes and trees as soon as possible. Learn more in [Migrate authentication modules and chains to trees](https://docs.pingidentity.com/pingam/8/am-authentication/migrate-to-auth-trees.html).

|   |                                                                                                                                                                                                                         |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | It's recommended that you migrate to nodes and trees *before* upgrading to AM 8.If that's not possible, and you need access to modules and chains for migration purposes, you can temporarily re-enable them in AM 8.0. |

> **Collapse: Re-enable modules and chains**
>
> 1. Go to Configure > Server Defaults > Advanced in the AM admin UI.
>
> 2. Add the `org.forgerock.am.authentication.chains.enabled` property and set it to `true`.
>
> 3. Save your changes.
>
> 4. Restart AM or the container where it runs.
>
> You can now access modules and chains through the REST endpoints. Modules and chains aren't accessible through the AM admin UI.

|   |                                                                                                                                                                           |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The option to re-enable modules and chains is only for migration purposes in AM 8.0. Authentication modules and chains will be removed completely in an upcoming release. |

##### Providing OAuth 2.0 client certificates to AM

Clients can provide mTLS certificates to AM using trusted headers. AM now supports certificates in Base64-encoded PEM and DER format.

The corresponding value of the TLS Client Certificate Header Format configuration property on the [OAuth2 Provider service](https://docs.pingidentity.com/pingam/8/reference/services-configuration.html#global-oauth-oidc-advanced) has therefore changed from `URLENCODED_PEM` to `BASE64_ENCODED_CERT`.

##### Change in behavior for WebAuthn flows

Previously, for WebAuthn flows, if an authenticator provided an attestation that included the certificate authority (CA) root certificate, AM would remove and silently ignore the certificate. This behavior has changed in AM 8.0.

Now, if the authenticator provides an attestation that contains an invalid certificate chain (including the root CA certificate in the chain), PingAM rejects the attestation and throws an `InvalidDataException` error. The root certificate must be issued and securely distributed by a CA.

##### Endpoint for monitoring server activity with Prometheus

To monitor server activity with Prometheus, use one of the new endpoints:

* `/metrics/prometheus`

  The path of this endpoint is format-agnostic, but the response payload is identical to that from the `/json/metrics/prometheus` endpoint.

  Although this endpoint is new, it is also *deprecated* in this release and support for its use will be removed in a future release. Move to the `/metrics/prometheus/0.0.4` endpoint as soon as convenient.

* `/metrics/prometheus/0.0.4`

  The path of this endpoint is format-agnostic, but the response payload is slightly different to that from the `/metrics/prometheus` endpoint.

Learn more in [Monitor with Prometheus](https://docs.pingidentity.com/pingam/8/maintenance-guide/monitoring-prometheus.html).

##### Sessions terminology

Sessions that are created to track progress through an authentication tree were previously referred to as *authentication sessions*, and sessions that are created after a user has authenticated were just referred to as *sessions*.

This release introduces the following new terminology to clarify and simplify the distinction between these session types:

* **Journey session** (previously called authentication session)

* **Authenticated session** (previously called session).

This change is reflected in the documentation.

##### Change to custom OIDC Social IDP configuration

You no longer need to specify a well-known endpoint when configuring a custom OIDC Social Identity Provider service.

If the well-known endpoint isn't specified, AM verifies signatures using the JWK location, keystore location, or the client secret.

##### Changes to audit logging

* The following events have been added to the audit log:

  * `AM-TREE-LOGIN-STARTED`

    Logged when authentication through a tree starts.

  * `AM-TREE-LOGIN-COMPLETED` with `exception`

  Learn more in the [Audit logging reference](https://docs.pingidentity.com/pingam/8/security-guide/sec-maint-audit-ref.html).

* The `org.forgerock.openam.audit.identity.activity.events.blacklist` advanced server property contains a comma-separated list of audit events that won't be logged. In previous releases, you could only add the `AM-ACCESS-ATTEMPT`, `AM-IDENTITY-CHANGE`, and `AM-GROUP-CHANGE` events to this list. From AM 8.0, you can prevent logging of any event.

  |   |                                                                                                      |
  | - | ---------------------------------------------------------------------------------------------------- |
  |   | Logging *all* events can impact performance. You should log only those events you intend to monitor. |

##### WS-Federation `com.sun.identity.wsfederation.logout.wreply` URL validation

To facilitate logging out of WS-Federation and multiprotocol environments (WS-Federation communicating with SAML 2.0), you must add the URL specified in the `com.sun.identity.wsfederation.logout.wreply` query parameter to the Valid goto URL Resources field in the validation service. If you don't add this URL, redirection fails.

Learn more in [Add a URL to the validation service](https://docs.pingidentity.com/pingam/8/authentication-guide/redirection-url-precedence.html#configure-validation-service).

##### Changes to LinkedIn social identity provider configuration

The OAuth 2.0 version of the LinkedIn social identity provider configuration profile is [deprecated by LinkedIn](https://learn.microsoft.com/en-us/linkedin/consumer/integrations/self-serve/sign-in-with-linkedin). This deprecated version has been renamed to `LinkedIn (Legacy)`.

To configure your social identity provider with the latest OIDC version of the LinkedIn profile, use the `LinkedIn` profile.

##### SOAP STS service

The SOAP STS service has been removed in this release. If you're still using the SOAP STS, you must migrate to the [REST STS](https://docs.pingidentity.com/pingam/8/sts-guide/preface.html).

When you upgrade to AM 8, the SOAP STS agents and configuration are deleted. Make sure you retain anything useful to your migration prior to upgrading.

##### The `accountId` field in JWT script binding operations

Two new fields, `subject` and `issuer`, replace the `accountId` field used by the `jwtAssertion` and `jwtValidator` script bindings. This lets you specify separate values for these JWT claims.

If specified, the `accountId` is now used as the values for `issuer`, `stableId`, and `subject` when these values aren't provided.

Learn more in [Generate and validate JWTs](https://docs.pingidentity.com/pingam/8/scripting-guide/scripting-api-node.html#jwt-support).

##### Device authorization grant behavior

The behavior of the device authorization grant has changed slightly. Previously, AM didn't consult the default ACRs until after consent was granted by the user. This meant that the user had already been prompted to authenticate through the default realm authentication mechanism and was sometimes required to authenticate twice if the default ACRs dictated a different mechanism.

The `/oauth2/device/user` endpoint checks for a `user_code` during the initial request. From AM 8.0, if a `user_code` is supplied, AM uses it to retrieve the associated device code to determine if any ACRs were requested. If ACRs were requested, they guide the authentication mechanism.

This change improves the user experience by reducing redundant authentication prompts.

You can find more information in [Device authorization grant](https://docs.pingidentity.com/pingam/8/oauth2-guide/oauth2-device-flow.html).

### Changes in AM 7.5.x

#### AM 7.5

##### Change in behavior for journeys containing a [Certificate Collector node](https://docs.pingidentity.com/auth-node-ref/8.1/certificate-collector.html)

Previously, for journeys containing a [Certificate Collector node](https://docs.pingidentity.com/auth-node-ref/8.1/certificate-collector.html), AM would throw an exception in the following scenario:

* You set the node's Certificate Collection Method property to `Either` or `Header`

* You specified an HTTP header name

* The certificate was missing from the browser (and from the request if `Either` was selected)

Now, in this scenario, the journey continues down the `Not Collected` path.

##### Default setting for AES key wrap encryption

The system property `org.forgerock.openam.encryption.padshortinputs` is now `true` by default.

This property pads short inputs (less than 8 bytes). If you're using [AES key wrap encryption](https://docs.pingidentity.com/pingam/7.5/install-guide/prepare-aeswrap.html), do one of the following *before you upgrade* to AM 7.5:

* Check that any passwords encrypted with AES key wrap encryption are longer than eight characters. AM won't be able to decrypt shorter values.

* Set `org.forgerock.openam.encryption.padshortinputs` to `true` and re-save any short passwords to update the padding.

##### Change to OAuth 2.0 refresh token introspection response types

Previously, introspecting a stateful refresh token returned some claims as an array containing a single string.

For consistency, the following claims are now returned as strings:

* `realm`

* `userName`

* `authGrantId`

* `clientID`

### Changes in AM 7.4.x

#### AM 7.4.2

##### The `accountId` field in JWT script binding operations

Two new fields, `subject` and `issuer`, replace the `accountId` field used by the `jwtAssertion` and `jwtValidator` script bindings. This lets you specify separate values for these JWT claims.

If specified, the `accountId` is now used as the values for `issuer`, `stableId`, and `subject` when these values aren't provided.

Learn more in [Generate and validate JWTs](https://docs.pingidentity.com/pingam/7.4/scripting-guide/scripting-api-node.html#jwt-support).

#### AM 7.4.1

##### WS-Federation `com.sun.identity.wsfederation.logout.wreply` URL validation

##### WS-Federation `com.sun.identity.wsfederation.logout.wreply` URL validation

To facilitate logging out of WS-Federation and multiprotocol environments (WS-Federation communicating with SAML 2.0), you must add the URL specified in the `com.sun.identity.wsfederation.logout.wreply` query parameter to the Valid goto URL Resources field in the validation service. If you don't add this URL, redirection fails.

Learn more in [Add a URL to the validation service](https://docs.pingidentity.com/pingam/7.4/authentication-guide/redirection-url-precedence.html#configure-validation-service).

##### Change in behavior for journeys containing a [Certificate Collector node](https://docs.pingidentity.com/auth-node-ref/8.1/certificate-collector.html)

Previously, for journeys containing a [Certificate Collector node](https://docs.pingidentity.com/auth-node-ref/8.1/certificate-collector.html), AM would throw an exception in the following scenario:

* You set the node's Certificate Collection Method property to `Either` or `Header`

* You specified an HTTP header name

* The certificate was missing from the browser (and from the request if `Either` was selected)

Now, in this scenario, the journey continues down the `Not Collected` path.

##### Change to OAuth 2.0 refresh token introspection response types

Previously, introspecting a stateful refresh token returned some claims as an array containing a single string.

For consistency, the following claims are now returned as strings:

* `realm`

* `userName`

* `authGrantId`

* `clientID`

#### AM 7.4

##### Removal of `dsameuserpwd` from default keystore

The alias of the `dsameuserpwd` has been removed from the default keystore. The `dsameUser` is an internal account that AM uses to connect to the configuration store. AM now generates the password for this account on startup, and you can't read or change it.

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | If you upgrade to AM 7.4 using the [upgrade wizard](https://docs.pingidentity.com/pingam/7.4/upgrade-guide/upgrade-servers.html#upgrade-wizard) and need to roll back the upgrade, you must *restore* the default keystore. The upgrade wizard removes the `dsameuserpwd` alias. If you don't restore this alias, the rolled back instance of AM won't start up.If you try to use a previous version of `ssoadm` with AM 7.4, the command will show an error `Can't open boot keystore` as it expects the `dsameuserpwd` to be there. To avoid this error, use the `ssoadm` version that is delivered with AM 7.4. |

##### Preconfigure policy and application data stores

You can now *disable* [policy and application data stores](https://docs.pingidentity.com/pingam/7.4/setup-guide/setting-up-policy-and-app-stores.html) until you are ready to use them. This means that you can preconfigure a data store before the directory server is ready. When you want to use the data store configuration, you can enable it, at which point AM verifies that it can connect to the configured store.

All default policy and application data store configurations are *enabled*. A new custom external data store configuration is *disabled* by default. When you upgrade to AM 7.4, existing data store configurations are *enabled* by default.

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The `dataStoreEnabled` property is mandatory if you're creating new data stores over REST (using `DataStoreService/config?_action=create`). It's also mandatory if you're updating data stores over REST with a PUT request. For backward compatibility, if you don't include this property in the JSON payload, the endpoint currently adds it to the configuration by default with a value of `true`.In the next AM release, the endpoint version will be incremented and the latest version will require the property to be present. |

##### Change in behavior when an authentication tree is deleted

From this release, when you delete an authentication tree, any nodes referenced by that tree are also deleted, provided they aren't referenced by another tree.

This change eliminates *orphaned* nodes in the configuration and lets you delete the scripts referenced by those nodes.

##### Change in behavior of `subjectattributes` endpoint

The behavior of queries to the `subjectattributes` endpoint has changed in this release.

To override the new behavior and revert to the previous behavior, set the [`org.forgerock.security.entitlement.enforce.realm`](https://docs.pingidentity.com/pingam/7.4/reference/deployment-configuration-reference.html#adv-property-entitlement-realm) advanced server property to `false`, then restart AM for the change to take effect.

For security reasons you should set this property back to `true` when you have updated your scripts.

##### Rotatable secrets for `amAdmin` password

AM now caches the special secret used to store the password of `amAdmin` user. The expiry time of the cache is 900 seconds (15 minutes) by default. To change the expiry time, set the [org.forgerock.openam.secrets.special.user.secret.refresh.seconds](https://docs.pingidentity.com/pingam/7.4/reference/deployment-configuration-reference.html#secrets.special.user.secret.refresh.seconds) advanced server property.

For more information, refer to [Store the amAdmin password in a secret store](https://docs.pingidentity.com/pingam/7.4/security-guide/securing-administration.html#amadmin-password-secret-store).

##### Amster

The .zip distribution now includes a root folder named `amster`.

This aligns the Amster delivery with the other products in the Ping Advanced Identity Software.

## Deprecated

The functionality listed here is deprecated, and likely to be removed in a future release.

### Deprecated since PingAM 8.1

#### SAML v2.0 JSPs

The JSPs provided for SAML v2.0 standalone mode are deprecated. Use the URL entry points described in [removed functionality](removed.html#removed-saml-jsps) instead.

|   |                                                                                                                                             |
| - | ------------------------------------------------------------------------------------------------------------------------------------------- |
|   | You can still invoke the JSPs because they're mapped to URLs for backward compatibility, but any customizations to these JSPs will be lost. |

#### Authentication by Module Instance policy condition type

The Authentication by Module Instance environment condition type is deprecated and will be removed in a future release.

For existing policies, this condition type evaluates to `false`. You should remove this condition type from all policies as soon as convenient.

#### Node versioning REST endpoints

Resource versions 1.0 and 2.0 are deprecated for the `realm-config/authentication/authenticationtrees` endpoint. Use resource version 3.0 instead.

Versionless node endpoints are also deprecated. Make sure you always specify the node version in the request URL.

Learn more about these changes in [Node versioning](whats-new-8.1.html#node-versioning).

### Deprecated since PingAM 8.0

#### Monitoring

* Interface endpoint for monitoring server activity with Prometheus

  The `/json/metrics/prometheus` endpoint is deprecated in this release.

  To monitor server activity with Prometheus, use one of the new endpoints instead:

  * `/metrics/prometheus`

  * `/metrics/prometheus/0.0.4`

  Although the `/metrics/prometheus` endpoint is new, it is also *deprecated* in this release and support for its use will be removed in a future release. Move to the `/metrics/prometheus/0.0.4` endpoint as soon as convenient.

  Learn more in [Monitor with Prometheus](https://docs.pingidentity.com/pingam/8/maintenance-guide/monitoring-prometheus.html).

* MBean and JMX interfaces

  Support for the legacy MBean and the JMX monitoring interfaces is deprecated in this release.

  AM supports other options for monitoring servers, including Graphite. Learn more in [Monitor AM instances](https://docs.pingidentity.com/pingam/8/maintenance-guide/monitoring-am.html).

#### Audit event handlers

The following audit event handlers are deprecated and will be removed in a future release:

* CSV

* Syslog

* JDBC

* JMS

Use the [JSON audit event handler](https://docs.pingidentity.com/pingam/8/security-guide/implementing-audit.html#configuring-json-audit-event-handlers) instead.

### Deprecated since AM 7.5

#### Secret label mappings

The following secret label mappings are deprecated in this release:

* `am.global.services.session.clientbased.encryption`

* `am.global.services.session.clientbased.signing`

Learn more about changes to secret label mappings in [Support for storing secrets in secret stores](whats-new-7.5.html#new-secrets-api-support).

#### Configuration replaced by secret labels

| Feature                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | Deprecated field                                                                             |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| [CAPTCHA node](https://docs.pingidentity.com/auth-node-ref/8.1/captcha.html)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | `CAPTCHA Secret Key`                                                                         |
| [Core authentication settings](https://docs.pingidentity.com/pingam/7.5/authentication-guide/authn-core-settings.html)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | `Persistent Cookie Encryption Certificate Alias``Organization Authentication Signing Secret` |
| Encrypted device storage services:- [Device Binding service](https://docs.pingidentity.com/pingam/7.5/reference/global-services-configuration.html#global-devicebindingservice)

- [Device ID service](https://docs.pingidentity.com/pingam/7.5/reference/global-services-configuration.html#global-deviceidservice)

- [Device Profiles service](https://docs.pingidentity.com/pingam/7.5/reference/global-services-configuration.html#global-deviceprofilesservice)

- [OATH service](https://docs.pingidentity.com/pingam/7.5/reference/global-services-configuration.html#global-authenticatoroathservice)

- [Push service](https://docs.pingidentity.com/pingam/7.5/reference/global-services-configuration.html#global-authenticatorpushservice)

- [WebAuthn service](https://docs.pingidentity.com/pingam/7.5/reference/global-services-configuration.html#global-authenticatorwebauthnservice) | `Key Store Password``Key-Pair Alias``Private Key Password`                                   |
| [OTP SMS Sender node](https://docs.pingidentity.com/auth-node-ref/8.1/otp-sms-sender.html) and [OTP Email Sender node](https://docs.pingidentity.com/auth-node-ref/8.1/otp-email-sender.html)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | `Mail Server Authentication Password`                                                        |
| [Password replay](https://docs.pingidentity.com/pinggateway/2026/gateway-guide/sso-cdsso.html#credentials-am)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | `Replay Password Key` (`com.sun.identity.agents.config.replaypasswd.key`)                    |
| [Persistent Cookie Decision node](https://docs.pingidentity.com/auth-node-ref/8.1/persistent-cookie-decision.html) and [Set Persistent Cookie node](https://docs.pingidentity.com/auth-node-ref/8.1/set-persistent-cookie.html)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | `HMAC Signing Key`                                                                           |
| [PUSH notification service](https://docs.pingidentity.com/pingam/7.5/reference/global-services-configuration.html#global-pushnotification)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | `SNS Access Key Secret`                                                                      |
| [SAML v2.0 remote SP and IDP configuration](https://docs.pingidentity.com/pingam/7.5/saml2-guide/saml2-reference.html#saml2-remote-idp-configuration)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | `Basic Authentication` settings                                                              |
| [Session service](https://docs.pingidentity.com/pingam/7.5/reference/global-services-configuration.html#global-session-client-based-sessions)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | `Encryption Symmetric AES Key``Signing HMAC Shared Secret`                                   |
| [Social Provider service](https://docs.pingidentity.com/pingam/7.5/authentication-guide/social-idp-client-reference.html)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | `Client Secret`                                                                              |

#### Changes to `Action` class

The following `org.forgerock.openam.auth.node.api.Action` methods are deprecated in this release:

* `public ActionBuilder withUniversalId(String universalId)`

* `public ActionBuilder withUniversalId(Optional<String> universalId)`

Use the new `public ActionBuilder withIdentifiedIdentity(String username, IdType identityType)` and `public ActionBuilder withIdentifiedIdentity(AMIdentity identity)` methods instead.

The `Optional <String> universalId` field is also deprecated, and is replaced by `Optional<IdentifiedIdentity> identifiedIdentity`.

#### Legacy Social Provider node

The [Legacy Social Provider Handler node](https://docs.pingidentity.com/auth-node-ref/8.1/legacy-social-provider-handler.html) has been marked as deprecated and will be removed in a future release. This node is replaced by a new [Social Provider Handler node](https://docs.pingidentity.com/auth-node-ref/8.1/social-provider-handler.html) that resolves issues related to reentry cookies. The legacy node remains supported in existing journeys. If you're creating new journeys, use the new Social Provider Handler node instead.

## Documentation updates

In addition to the changes described elsewhere in these release notes, the published documentation for each AM version includes the following important changes.

|   |                                                                                                                                     |
| - | ----------------------------------------------------------------------------------------------------------------------------------- |
|   | The Amster release notes have been combined into the AM release notes. These release notes now include Amster changes since AM 7.2. |

### AM 8.1.x

#### AM 8.1.1

|                                                        |                                                                                              |
| ------------------------------------------------------ | -------------------------------------------------------------------------------------------- |
| AME-35282                                              | Clarify that the `request` parameter is not mandatory on the `/oauth/par` endpoint           |
| AME-35010                                              | Document new AI agent methods on the `clientIdentity` binding                                |
| AME-34887                                              | Add autonomous agent use case documentation                                                  |
| AME-34872                                              | Document threat model mitigations for policies nodes                                         |
| AME-34637                                              | Add security note to the WebAuthn Authentication node for username enumeration risk          |
| AME-34539                                              | Update documentation for audience parameter validation in token exchange                     |
| AME-34503                                              | Update AIC/platform documentation to use AM policy                                           |
| AME-34219                                              | Improve BCFKS keystore setup documentation                                                   |
| OPENAM-27644                                           | Note that the interface stability for the OpenTelemetry integration is evolving              |
| OPENAM-26844                                           | Add caution against using default key aliases in production environments                     |
| OPENAM-26519                                           | Document `openidm` exception handling in the next-generation scripting API                   |
| OPENAM-26450                                           | Add detail about configuring the secret for the RADIUS Decision node                         |
| OPENAM-26391                                           | Update the PingOne Protect Evaluation node documentation with the custom session ID property |
| OPENAM-26223                                           | Update the Set Success Details node and related nodes for no-session journeys                |
| OPENAM-26231                                           | Update `am.cts.use.etag.assertion.on.update` documentation to reflect its narrowed scope     |
| OPENAM-26222                                           | Update the `noSession=true` authenticate endpoint example                                    |
| OPENAM-26117                                           | Add backchannel RCS flow diagram and consent channel choice section                          |
| OPENAM-26094                                           | Add warning about `ScriptTextOutputCallback` misuse in custom UI implementations             |
| OPENAM-26095, OPENAM-21056, OPENAM-21586, OPENAM-22830 | Address OAuth 2.0 flow diagram feedback                                                      |
| OPENAM-25757                                           | Clarify SAML IdP-initiated integrated journeys                                               |
| OPENAM-25666                                           | Note that `AM_TEST_MODE=true` is required for FBC evaluation installations                   |
| OPENAM-25616                                           | Clarify transient state encryption key behaviour                                             |
| OPENAM-25604                                           | Add a session upgrade scenario for navigating to a different top-level tree                  |
| OPENAM-25578                                           | Correct advice for changing default key aliases for sessions                                 |
| OPENAM-25394, OPENAM-19344                             | Update the `/users/user/oauth2/applications` endpoint documentation                          |
| OPENAM-24509                                           | Point readers to access token modification documentation for adding custom claims            |
| OPENAM-24439                                           | Clarify that the redirect URL should be the AM base URL without query parameters             |
| OPENAM-24364, OPENAM-23568                             | Add a JWT client authentication example and JAR key guidance                                 |
| OPENAM-23943, OPENAM-23993, OPENAM-26832               | Address backchannel authentication feedback                                                  |
| OPENAM-23831, OPENAM-20876                             | Address OAuth 2.0 registering clients documentation feedback                                 |
| OPENAM-23756                                           | Document certificate chain ordering for mTLS PEM file creation                               |
| OPENAM-23434, OPENAM-23256                             | Clarify parameter support in OAuth 2.0 endpoints                                             |
| OPENAM-23315                                           | Add `ForceAuth` to the Custom Login URL Template variables table                             |
| OPENAM-23255                                           | Clarify refresh token lifetime behavior on re-issuance                                       |
| OPENAM-22919                                           | Update OAuth 2.0 scope-related screenshots                                                   |
| OPENAM-22855                                           | Clarify State Metadata node usage requirements                                               |
| OPENAM-22369                                           | Add `selectIdPCallback` example to the `callbacksBuilder` documentation                      |
| OPENAM-22064, OPENAM-21099                             | Address secret store feedback, including adding steps for preparing the HSM                  |
| OPENAM-21953                                           | Document authorization requirements for OAuth 2.0 token introspection                        |
| OPENAM-21713                                           | Clarify the purpose of the Remote Consent Service secret                                     |
| OPENAM-20562                                           | Document URL normalization during policy evaluation                                          |
| OPENAM-20483                                           | Add passkey references to WebAuthn documentation                                             |
| OPENAM-19750                                           | Add caution regarding the use of multiple ID repositories                                    |
| OPENAM-18750                                           | Add HTTP response sections to OAuth 2.0 endpoint pages                                       |
| OPENAM-18451                                           | Clarify use of `form_post` in sub-realms for social identity provider configuration          |

#### AM 8.1.0

|                                          |                                                                                                              |
| ---------------------------------------- | ------------------------------------------------------------------------------------------------------------ |
| AME-33889                                | Document default Config Provider script in platform UI                                                       |
| AME-33875                                | Document new Headers option for success details node                                                         |
| AME-33874                                | Document new Headers option for failure details node                                                         |
| AME-33842                                | Document Allow Radius Node to handle Vendor Specific Attributes                                              |
| DF-1047                                  | Clarify that the percentage of requests must be an integer                                                   |
| DF-552                                   | Addressed feedback for suspend and resume journeys                                                           |
| DOCS-9732                                | Update reCAPTCHA Enterprise node documentation                                                               |
| DOCS-9616                                | Add details regarding modes and the variance property to the Device Match node                               |
| DOCS-9523                                | Move PingOne nodes to the Auth Nodes reference                                                               |
| DOCS-9443                                | Apply the documentation template to the Select Identity Provider node                                        |
| DOCS-9417                                | Apply the documentation template to the Polling Wait node                                                    |
| DOCS-8431                                | Include the API version header in the Config Provider node example                                           |
| OPENAM-25800                             | Add Skew Allowance to Device Binding nodes                                                                   |
| OPENAM-25765                             | Document the am.secrets.gsm.stableid.version.only advanced server property to change the default kid value   |
| OPENAM-25755                             | Address Device Binding node feedback and incorporate all device binding nodes into the template              |
| OPENAM-25741                             | Add a Callbacks section to selected nodes                                                                    |
| OPENAM-25736                             | Document the Node State Attribute For Username attribute in the PingOne Protect Evaluation node              |
| OPENAM-25682, OPENAM-25683, OPENAM-24932 | Address feedback on the OATH Token Verifier node                                                             |
| OPENAM-25678                             | Add callback information to the Push nodes                                                                   |
| OPENAM-25668                             | Document new locales binding                                                                                 |
| OPENAM-25660                             | Document automatic redirects in the PingOne Verify Evaluation node                                           |
| OPENAM-25641                             | Document the addition of redirectUris to OAuth 2.0 script bindings                                           |
| OPENAM-25623                             | Documentation for the RSA SecurID node                                                                       |
| OPENAM-25615                             | Document support for custom CTS DN during FBC installation                                                   |
| OPENAM-25599                             | Document sending groups with the PingOne Protect Evaluation node                                             |
| OPENAM-25593                             | Document the new JWT Password Replay node                                                                    |
| OPENAM-25584                             | Address feedback for the Social Provider Handler node                                                        |
| OPENAM-25551                             | Remove note regarding the inability to rename OATH and Push devices                                          |
| OPENAM-25548, OPENAM-25549               | Address feedback for the Device Profile Collector and Device Match nodes                                     |
| OPENAM-25538                             | Clarify documentation for the Set Persistent Cookie node                                                     |
| OPENAM-25532                             | Update FBC upgrade instructions                                                                              |
| OPENAM-25528                             | Document support for the android-key attestation type                                                        |
| OPENAM-25513                             | Address feedback on the Device Profile Save node                                                             |
| OPENAM-25509                             | Correct the path to the external identity store in the upgrade documentation                                 |
| OPENAM-25505                             | Address feedback and improve documentation for the HOTP Generator and OTP Collector Decision nodes           |
| OPENAM-25485                             | Document new PingID Agent fields on the PingOne Protect Initialize node                                      |
| OPENAM-25477                             | Document the new SameSite configuration option for Persistent Cookie nodes                                   |
| OPENAM-25471                             | Document targeted risk policies sent to PingOne                                                              |
| OPENAM-25465                             | Create a migration guide for moving from chains/modules to trees/nodes                                       |
| OPENAM-25464                             | Deprecation notices for Marketplace versions of PingOne nodes                                                |
| OPENAM-25459                             | Document the new Set Logout Details node                                                                     |
| OPENAM-25458                             | Document Logout Hooks in the Node Developer guide                                                            |
| OPENAM-25445                             | Clarify that attributes collected by the Attribute Collector node must be viewable                           |
| OPENAM-25439, OPENAM-25446               | Clarify next-generation session binding and Node Designer threading                                          |
| OPENAM-25430                             | Provide an example of using the IDMUser condition with multivalued fields                                    |
| OPENAM-25409                             | Document additional device context information in the PingOne Protect Evaluation node                        |
| OPENAM-25402                             | Document the `Accepted JWT Issuers` OAuth 2.0 client attribute                                               |
| OPENAM-25401                             | Validate steps for SAML SSO in integrated mode                                                               |
| OPENAM-24583                             | Clarify that a backchannel transaction never results in a DENIED status                                      |
| OPENAM-24576                             | Correct the state variable name in the Device Binding node                                                   |
| OPENAM-24540                             | Document the private key JWT audience attribute in the social authentication client configuration            |
| OPENAM-24538                             | Document the expiry claim required attribute in the social provider client configuration                     |
| OPENAM-24536                             | Document the `Allow same device verification` configuration                                                  |
| OPENAM-24525                             | Note that changing AWS credentials in the Push Notification service requires devices to be re-registered     |
| OPENAM-24491                             | Clarify Node Designer script capabilities                                                                    |
| OPENAM-24438                             | Clarify the Scalable Clients setting                                                                         |
| OPENAM-24435                             | Note that in FBC deployments, the default Stateless Session AES Encryption Key must be set post-installation |
| OPENAM-24399                             | Document the new FACIAL\_COMPARISON\_REFERENCE\_SELFIE data type in PingOne Verify Evaluation node metadata  |
| OPENAM-24396                             | Update Authenticator app documentation to reflect PingID as the default supported app                        |
| OPENAM-24395                             | Address feedback regarding importing and exporting policies                                                  |
| OPENAM-24374                             | Correct documentation regarding validator classes in the Node Developer guide                                |
| OPENAM-24357                             | Fix an error in the documentation for hiddenValueCallback                                                    |
| OPENAM-24345                             | Update the list of supported SNS regions for the Push Notification Service                                   |
| OPENAM-24329                             | Correct inaccurate documentation for the OIDC ID Token Validator node                                        |
| OPENAM-24324, OPENAM-23678               | Address feedback for validating id\_token and identifying users                                              |
| OPENAM-24320                             | Indicate support for third-party authenticator apps                                                          |
| OPENAM-24300                             | Update AM documentation regarding PKCS12 keystore support                                                    |
| OPENAM-24296                             | Document node state biographic matching in the PingOne Verify Evaluation node                                |
| OPENAM-24236                             | Improve Meter node documentation                                                                             |
| OPENAM-24225                             | Fully integrate Amster documentation into the AM documentation                                               |
| OPENAM-24196, OPENAM-21662               | SAML documentation improvements                                                                              |
| OPENAM-24163                             | Update Amster documentation to reflect user store configuration changes                                      |
| OPENAM-24158                             | Address feedback regarding the ForgeRock Authenticator app                                                   |
| OPENAM-24151                             | OIDC session management improvements                                                                         |
| OPENAM-24094                             | Remove product name change notices throughout AM documentation                                               |
| OPENAM-24092                             | Note that transactional authorization policies are not supported for the JwtClaim subject type               |
| OPENAM-24070                             | Document support for ECDSA in next-generation scripting signing algorithms                                   |
| OPENAM-24067, AME-30093                  | Add documentation on renaming MFA devices and update the Push diagram                                        |
| OPENAM-24036                             | Update steps in the Verify Evaluation guide                                                                  |
| OPENAM-24018                             | Improve the IdP adapter custom script documentation                                                          |
| OPENAM-24014                             | Fix the encoding for the HTTP Basic Authorization header example                                             |
| OPENAM-23997                             | Correct the invalid value for the backchannel authentication type parameter                                  |
| OPENAM-23982                             | Add relevant endpoints to the Auth Nodes guide for node versioning                                           |
| OPENAM-23979                             | Update Amster documentation for node versioning                                                              |
| OPENAM-23959                             | Fix an error in the default secret alias name                                                                |
| OPENAM-23955                             | Update the Config Provider node for node versioning                                                          |
| OPENAM-23929                             | Note that the Configuration Cache Duration default value should be non-zero                                  |
| OPENAM-23921                             | Document policy cache properties                                                                             |
| OPENAM-23920                             | Clarify requirements for environment conditions and differences from subject conditions                      |
| OPENAM-23907                             | Correct the URL in Step 5 of the PingAM Evaluation guide                                                     |
| OPENAM-23900                             | Fix an error in the Success URL node documentation                                                           |
| OPENAM-23881                             | Add AAGUID to transient state and incorporate WebAuthn changes into the release notes                        |
| OPENAM-23874                             | Specify that the ForceAuth parameter is case-sensitive                                                       |
| OPENAM-23872                             | Address feedback for /users/user/oauth2/applications                                                         |
| OPENAM-23861                             | Add missing descriptions to the SAML Fedlet reference                                                        |
| OPENAM-23855                             | Update the JDBC Audit log table note regarding VARCHAR limits                                                |
| OPENAM-23828                             | Correct parameters for the amUpgrade command when migrating to FBC                                           |
| OPENAM-23819                             | Improve documentation for setting up AM in JBoss and WildFly application containers                          |
| OPENAM-23792                             | Fix an issue with the Policy Condition script example                                                        |
| OPENAM-23755                             | Update Retry Limit Decision node documentation                                                               |
| OPENAM-23746                             | Correct the sub value in the mayAct script for delegation                                                    |
| OPENAM-23735                             | Specify where recovery codes are stored for the OATH Registration node                                       |
| OPENAM-23714                             | Indicate that only one secret can be active for any secret label mapping                                     |
| OPENAM-23616                             | Clarify that a client secret is not required for OAuth 2.0 client update requests                            |
| OPENAM-23485                             | Add information on how the locale is utilized                                                                |
| OPENAM-23393                             | Remove legacy ClientType from Success and Failure redirection URLs                                           |
| OPENAM-23281                             | Document bindings for the Social IdP Profile transformation script type                                      |
| OPENAM-23271                             | Update scripted policy condition documentation with a working example                                        |
| OPENAM-23263                             | Improve the Set Success Details node documentation                                                           |
| OPENAM-23126                             | Correct guidance regarding setSessionProperty                                                                |
| OPENAM-23113, OPENAM-23123               | Update JWT profile configuration documentation                                                               |
| OPENAM-22853                             | Add a description for Token Endpoint Authentication Method = none                                            |
| OPENAM-22849                             | Note that the DS rebuild-index command does not include a --useSsl option                                    |
| OPENAM-22828                             | Document the recommended setting for MaxMetaspaceSize                                                        |
| OPENAM-22823                             | Update Device Profile node documentation                                                                     |
| OPENAM-22576                             | Rework Push nodes documentation                                                                              |
| OPENAM-22433                             | Add details regarding Page Node limitations                                                                  |
| OPENAM-22173                             | Provide additional detail for the httpClient script binding                                                  |
| OPENAM-22124                             | Document outbound connections via proxy                                                                      |
| OPENAM-21858                             | Document the fields available for SAML Name ID mapping                                                       |
| OPENAM-21849                             | Install guide: Configure the same key for two AM instances using AES key wrap encryption                     |
| OPENAM-21817                             | Update recommendations for the default scripting service denylist                                            |
| OPENAM-21779                             | Fix errors in legacy OAuth 2.0 endpoint documentation                                                        |
| OPENAM-21669                             | Improve documentation for SAML attribute mapping                                                             |
| OPENAM-21655                             | Update documentation to reflect the correct default setting for HTTP-only cookies                            |
| OPENAM-21638                             | Clarify valid values for the default lockout attribute                                                       |
| OPENAM-21455, OPENAM-20849               | Add information regarding SAML 2.0 algorithms                                                                |
| OPENAM-21454                             | Provide sample SAML metadata files                                                                           |
| OPENAM-19503                             | Fix the idRepoClass() method name in CustomIdRepoConfig                                                      |
| OPENIG-9374                              | Add PingGateway instructions and routes for the Microsoft Intune node                                        |
| SDKS-3803                                | Document error codes and messages for the PingOne Verify Evaluation node                                     |
| SDKS-2793                                | Add bound devices to the list of upgrade LDIF files                                                          |

### AM 8.0.x

#### AM 8.0.2

|                 |                                                                                     |
| --------------- | ----------------------------------------------------------------------------------- |
| AME-32653       | Document support for PingDirectory as an identity store                             |
| AME-32274       | Restrict `ldapdelete` to just registered applications                               |
| AME-31765       | Add details about thread state to scripting metrics documentation                   |
| AME-31355       | Change in behavior for device authorization grant                                   |
| AME-31189       | Update docs after removal of modules and chains from XUI                            |
| AME-30047       | Document Logback Exception Length Configuration                                     |
| AME-27064       | Clarify directory settings for failover                                             |
| DOCS-9078       | Add use case for AM as Tenemos OIDC identity provider                               |
| DF-552 Feedback | Suspend and resume journeys                                                         |
| OPENAM-25333    | Update documentation for implicit grant flow                                        |
| OPENAM-25318    | Feedback: Identity stores                                                           |
| OPENAM-24540    | Document private key JWT audience attribute in social auth client configuration     |
| OPENAM-24438    | Clarify scalable clients setting                                                    |
| OPENAM-24395    | Address feedback for import and export policies                                     |
| OPENAM-24374    | Correct docs for validators in Auth Node dev guide                                  |
| OPENAM-24357    | Fix an error in the docs for getting `hiddenValueCallback`                          |
| OPENAM-24320    | Indicate support for other 3rd party authenticator apps                             |
| OPENAM-24300    | Update AM docs regarding PKCS12 keystore support                                    |
| OPENAM-24225    | Fully integrate Amster docs into AM docs                                            |
| OPENAM-24196    | SAML documentation improvements                                                     |
| OPENAM-24163    | Update Amster docs to reflect user store configuration changes                      |
| OPENAM-24158    | Address feedback on the ForgeRock Authenticator app                                 |
| OPENAM-24151    | OIDC Session management improvements                                                |
| OPENAM-24092    | Transactional authorization policies aren't supported for the JwtClaim subject type |
| OPENAM-24067    | Add documentation on how to rename MFA devices and update push diagram              |
| OPENAM-24036    | Verify evaluation guide steps                                                       |
| OPENAM-24018    | Improve IdP adapter custom script                                                   |
| OPENAM-24014    | Fix encoding for auth header example                                                |
| OPENAM-23997    | Backchannel authentication: Invalid value for type parameter                        |
| OPENAM-23959    | Fix error in default secret alias name                                              |
| OPENAM-23920    | Clarify policy environment and subject conditions descriptions                      |
| OPENAM-23907    | Incorrect URL in Step 5 of PingAM Evaluation guide                                  |
| OPENAM-23881    | Add missing WebAuthn changes to AM 8.0 release notes                                |
| OPENAM-23874    | Specify that the ForceAuth parameter is case-sensitive                              |
| OPENAM-23861    | Add descriptions to Fedlet reference                                                |
| OPENAM-23855    | Add note about VARCHAR limits for JDBC Audit log table                              |
| OPENAM-23828    | Migrate to FBC amUpgrade command has incorrect parameters                           |
| OPENAM-23819    | Improve documentation on setting up AM in JBoss and WildFly application containers  |
| OPENAM-23792    | Fix issue with Policy Condition script example                                      |
| OPENAM-23746    | Incorrect sub value in mayAct script for delegation                                 |
| OPENAM-23485    | Add more info on how locale is used                                                 |
| OPENAM-23393    | Remove legacy ClientType from Success and Failure redirection URLs                  |
| OPENAM-23281    | Document bindings for Social IdP Profile transformation script type                 |
| OPENAM-23126    | Incorrect guidance on setSessionProperty                                            |
| OPENAM-23113    | Update section on configuring JWT profile                                           |
| OPENAM-22853    | Add description for Token Endpoint Authentication Method = none                     |
| OPENAM-22849    | The DS rebuild-index command doesn't have a `--useSsl` option                       |
| OPENAM-22576    | Update MFA related screenshots                                                      |
| OPENAM-22173    | Provide more detail for `httpClient` script binding                                 |
| OPENAM-22124    | Outbound connection via proxy                                                       |
| OPENAM-21858    | Document the fields available to SAML Name ID Mapping                               |
| OPENAM-21849    | Configure same key for two AMs using AES key wrap encryption                        |
| OPENAM-21817    | Update recommendation on the default scriptingservice denylist                      |
| OPENAM-21779    | Fixed errors in legacy OAuth 2.0 endpoint docs                                      |
| OPENAM-21669    | Improve documentation for SAML attribute mapping                                    |
| OPENAM-21655    | Update docs to reflect the correct default setting for HTTP only cookies            |
| OPENAM-21638    | Clarified the valid values for the default lockout attribute                        |
| OPENAM-21455    | Added more info around SAML 2.0 algorithms                                          |
| OPENAM-21454    | Provide sample SAML metadata files                                                  |
| OPENAM-19503    | Fixed CustomIdRepoConfig idRepoClass() method name                                  |
| SDKS-2793       | Add bound devices to list of upgrade LDIF files                                     |

#### AM 8.0.1

|              |                                                                            |
| ------------ | -------------------------------------------------------------------------- |
| AME-31340    | Document ability of Push Notification service to reset device ID           |
| AME-31138    | Document removal of library scripts from custom scripted nodes             |
| OPENAM-23714 | Indicate that only one secret can be *active* for any secret label mapping |
| OPENAM-23616 | Client secret not required for OAuth 2.0 client update request             |

#### AM 8.0.0

|                                                     |                                                                                                 |
| --------------------------------------------------- | ----------------------------------------------------------------------------------------------- |
| AME-31026                                           | Deprecate audit event handlers                                                                  |
| AME-30978                                           | Add the Set Error Details node to nodes list and add details about the acceptException() method |
| AME-30936                                           | Mark legacy monitoring as deprecated                                                            |
| AME-30901                                           | Document dynamic client registration scripting                                                  |
| AME-30890 OPENAM-23637                              | Add documentation for No Session Trees and update session text where necessary                  |
| AME-30857                                           | Config Provider node script enabled for next-generation scripting engine                        |
| AME-30819                                           | Upgrade instructions for Tomcat 10                                                              |
| AME-30789                                           | Remove SNMP properties from the documentation                                                   |
| AME-30457                                           | Document updated TLS Client Certificate Header Format option value                              |
| AME-30442 OPENAM-22904                              | Overhaul STS guide - remove SOAP STS and modules and chains                                     |
| AME-30393                                           | Document new next-generation cookieName binding                                                 |
| AME-30392                                           | Document next-generation context for policy condition scripts                                   |
| AME-30344                                           | Document DER-formatted certificates for OAuth2 Client authentication                            |
| AME-30333                                           | Document IDM Environment Condition                                                              |
| AME-30291                                           | SAML certificate metadata update                                                                |
| AME-30249                                           | Document backchannel authentication                                                             |
| AME-30229                                           | Document the Message-Authenticator attribute config for RADIUS servers                          |
| AME-30173                                           | Update Evaluation guide to use external DS                                                      |
| AME-30154                                           | Document prevent use of mustRun trees as realm default                                          |
| AME-30046                                           | Document the Flow Control node                                                                  |
| AME-30026                                           | Document new next-generation scripting utils.crypto.subtle binding                              |
| AME-29963 AME-30155                                 | Document OIDC application journeys                                                              |
| AME-29951                                           | Document back-channel logout exp claim                                                          |
| AME-29759                                           | Document new next-generation script method to get random values                                 |
| AME-29757                                           | Document removal of custom Social IdP UI configuration properties                               |
| AME-29754                                           | Document new suspend and resume functionality in Scripted Decision node                         |
| AME-29685                                           | Revise the section about post-authentication tree hooks                                         |
| AME-29619                                           | Add navigation for the new Success Details node                                                 |
| AME-29538                                           | Update next-generation scripting documentation with exception handling scenarios                |
| AME-29511                                           | Document the WebAuthn metadata service and related secret label for FIDO certification          |
| AME-29485                                           | Document `samlApplication` script binding                                                       |
| AME-29415                                           | Document the Failure Details node                                                               |
| AME-29406 AME-29431                                 | Document new prometheus endpoints                                                               |
| AME-29326                                           | Document property to indicate OIDC provider doesn't return unique value for the `sub` claim     |
| AME-29179                                           | Document additional Config Provider node options                                                |
| AME-29168                                           | Add section on node security                                                                    |
| AME-29165                                           | Added "Send an HTTP request" section                                                            |
| AME-29164                                           | Update Maintain Authentication nodes                                                            |
| AME-29163                                           | Update Plugin Class                                                                             |
| AME-29162                                           | Update Handle Errors                                                                            |
| AME-29161 AME-29141                                 | Reorganise node developer guide                                                                 |
| AME-29160                                           | Update Action Class                                                                             |
| AME-29159                                           | Update Inject Objects into a node                                                               |
| AME-29155                                           | Document new NodeState merge state methods                                                      |
| AME-29133                                           | Config Interface @Attribute Improvements                                                        |
| AME-29132                                           | Node Metadata Improvements                                                                      |
| AME-29131                                           | Node Class Improvements                                                                         |
| AME-29129 AME-29127 AME-29130                       | Updates to nodes 'Prepare for development' page                                                 |
| AME-29072                                           | Document change in behavior for self-signed root CA provided in WebAuthN attestation            |
| AME-28883                                           | Document grace period for client-side sessions in one-to-one storage scheme                     |
| AME-28726                                           | Documentation for custom LINE OIDC config                                                       |
| AME-28682                                           | Outdated options in DS command-line examples                                                    |
| AME-28614                                           | Documentation of fix for validateJwtClaims failing when using a RS256 Alg signature             |
| AME-28596                                           | Document add entity configuration to enable journey association                                 |
| AME-28322                                           | Document new scripting monitoring metrics                                                       |
| AME-28264                                           | Document new advanced server property for configurable ID token clock skew time                 |
| AME-28256                                           | Document configure journey to always run to completion                                          |
| AME-28057                                           | Document Distributed Tracing                                                                    |
| AME-27982                                           | Add Customize account lockout message example from KB                                           |
| AME-27965                                           | Add KB content from How do I add a roles claim to the OIDC Claims Script in AM?                 |
| AME-27964                                           | Add KB content from How do I add a session property claim to the OIDC Claims Script?            |
| AME-27963                                           | Adding salient info from How do I add custom claims to the OIDC Claims Script in AM?            |
| AME-27962                                           | Add content from How do I override claims in the OIDC ID token in Identity Cloud or AM?         |
| AME-27953                                           | Documentation for enabling mTLS for HTTP Client script binding                                  |
| AME-27930                                           | Docs on preparing a truststore should use DS 7.x security model                                 |
| AME-27878                                           | Document customizing SAML NameID with a script                                                  |
| AME-27846                                           | Document the addition of encodeURI form body for `httpClient`                                   |
| AME-27845                                           | Document the Scripted Decision node access to `context.request.cookies`                         |
| AME-27844                                           | Document new functions added to ActionWrapper next-generation script binding                    |
| AME-27843                                           | Document rotation of the http proxy password without server restart                             |
| AME-27841                                           | Document availability of utility classes in library scripts                                     |
| AME-27840                                           | Documentation for new utility class script bindings                                             |
| AME-27838                                           | Document `secrets` binding for all next-generation scripts                                      |
| AME-27834                                           | Client certificate in SP metadata is configurable                                               |
| AME-27774 AME-27792                                 | Document audit logging changes for trees                                                        |
| AME-27726                                           | Add more information for activity audit log events                                              |
| AME-27697                                           | Document jwtAssertion and jwtValidator next-generation scripting improvements                   |
| AME-27609                                           | Document renaming of OAuth2 Client ID Token Public Encryption Key property                      |
| DOCS-7931                                           | Rename ForgeRock SDKs to Ping SDKs                                                              |
| OPENAM-28565                                        | Add note to docs about reserved binding names                                                   |
| OPENAM-23662                                        | Document the Amster Jwt Decision node                                                           |
| OPENAM-23660                                        | Update docs to include info on default trees that exist in AM 8                                 |
| OPENAM-23620                                        | Update REST version messages                                                                    |
| OPENAM-23558                                        | Provide more info on the am\_authentication\_count metric                                       |
| OPENAM-23549                                        | Error in documentation on scope validation                                                      |
| OPENAM-23547                                        | Remove deprecated openam-legacy-debug-slf4j module from docs                                    |
| OPENAM-23513                                        | Update supported directory stores                                                               |
| OPENAM-23463                                        | Docs for Journey Timeout settings for authenticated sessions                                    |
| OPENAM-23461                                        | Docs for Journey Timeout settings for pre-authentication sessions                               |
| OPENAM-23411                                        | Document changes to default denylist poll interval                                              |
| OPENAM-23410                                        | Document changes to mergeShared and mergeTransient nodeState methods                            |
| OPENAM-23407                                        | Updated Localize AM section to make it clearer that you have to download the UI first           |
| OPENAM-23362                                        | Success Redirect order is incorrect                                                             |
| OPENAM-23278                                        | Clarify docs on CTS token types                                                                 |
| OPENAM-23277                                        | Update Amster upgrade section to include 7.5                                                    |
| OPENAM-23188                                        | Correct steps for accessing am-external in auth node developer guide                            |
| OPENAM-23171                                        | Errors in SAML 2.0 profile OAuth 2 Grant docs                                                   |
| OPENAM-23104                                        | authLib script context missing from docs                                                        |
| OPENAM-23081                                        | Document improvements to transactional authorization                                            |
| OPENAM-23078                                        | Update steps for letting DS manage CTS tokens                                                   |
| OPENAM-23066                                        | Update amr claims section to use OIDC claims script instead of module mapping                   |
| OPENAM-23036                                        | Incorrect example used in Configure scr claims                                                  |
| OPENAM-23005                                        | Add section on creating trees using REST                                                        |
| OPENAM-22887- 22906                                 | Remove deprecated modules and chains from the documentation                                     |
| OPENAM-22899                                        | Add notes to the Radius guide about reenabling modules and chains                               |
| OPENAM-22878                                        | Document the settings for OCSP verification                                                     |
| OPENAM-22871                                        | Wrong default value for `STS Instance is running as remote instance`                            |
| OPENAM-22841                                        | Document new OIDC LinkedIn social identity provider configuration                               |
| OPENAM-22813                                        | Remove AM 6.x references including for supported upgrades                                       |
| OPENAM-22741                                        | Adding missing step in "Configure amr claims" procedure                                         |
| OPENAM-22641                                        | Corrected token terminology per feedback                                                        |
| OPENAM-22635                                        | Rework pruning CTS tokens                                                                       |
| OPENAM-22607                                        | Link to DS docs for appropriate tuning info                                                     |
| OPENAM-22549                                        | Add references for Set State node                                                               |
| OPENAM-22525                                        | Add HSM support info from KB                                                                    |
| OPENAM-22515                                        | Document Logout Webhook key WebhookEventType                                                    |
| OPENAM-22417                                        | Add link to max length property for goTo URL                                                    |
| OPENAM-22385                                        | Document default values for Session properties                                                  |
| OPENAM-22356                                        | Include a more useful link in Release Notes for custom auth node secrets enablement             |
| OPENAM-22343                                        | Document method return types for the script binding                                             |
| OPENAM-22339                                        | Provide example `systemd` script for AM                                                         |
| OPENAM-22327                                        | Remove mention of Internet Explorer from AM docs                                                |
| OPENAM-22254                                        | Update browser support table for WebAuthn                                                       |
| OPENAM-22157                                        | Clarify version support in upgrade instructions                                                 |
| OPENAM-22152                                        | Additional information required in token exchange impersonation                                 |
| OPENAM-22100 OPENAM-22049 OPENAM-22885 OPENAM-21325 | Various improvements to upgrading servers section                                               |
| OPENAM-22099                                        | Remove misleading information about unsupported custom callbacks                                |
| OPENAM-22045                                        | Corrected default log level                                                                     |
| OPENAM-21935                                        | Document the maximum JWT token liftime accepted by AM                                           |
| OPENAM-21907                                        | Added a tip to the setup guide for finding server and site IDs                                  |
| OPENAM-21857                                        | Document security hardening for UMA confusable homoglyphs                                       |
| OPENAM-21763                                        | Update terminology around "sessions" to use authenticated and pre-authentication                |
| OPENAM-21763                                        | Changed pre-authentication session terminology to journey session                               |
| OPENAM-21744                                        | Removed incorrect statement about invalidating client-side auth session                         |
| OPENAM-21591                                        | Document `checkIssuerForIdTokenInfo` advanced server property                                   |
| OPENAM-20673                                        | Clarify device reset with WebAuthn                                                              |
| OPENAM-20591                                        | Prevent ClassNotFoundException when removing `click-*` jars                                     |
| OPENAM-19899                                        | Remove all instances of /UI/login                                                               |
| OPENAM-19575                                        | Check algorithm statement for `/oauth2/connect/jwk_uri`                                         |
| OPENAM-19533                                        | Remove unnecessary images from installation steps                                               |
| OPENAM-19395                                        | Distinguish between general mail server and self-service mail service                           |
| SDKS-3759                                           | Added `verifyTransactionsHelper` script binding docs from AIC                                   |
| SDKS-3173                                           | The PingOne Worker service requires a configured OAuth2 provider service                        |
| SDKS-2959                                           | Document PingOne Protect-related callbacks                                                      |
| SDKS-2953                                           | Document PingOne Worker service                                                                 |
| SDKS-2864                                           | Adding new nodes to catalog page in AM                                                          |
| SDKS-2861                                           | Add PingOne Protect nodes to the list of nodes                                                  |

### AM 7.5.x

#### AM 7.5.2

> **Collapse: AM 7.5.2**
>
> |              |                                                                                       |
> | ------------ | ------------------------------------------------------------------------------------- |
> | AME-32653    | Document support for PingDirectory as an identity store                               |
> | OPENAM-24374 | Correct docs for validators in Auth Node dev guide                                    |
> | OPENAM-24320 | Indicate support for other third-party authenticator apps                             |
> | OPENAM-24300 | Update AM docs regarding PKCS12 keystore support                                      |
> | OPENAM-24225 | Fully integrate Amster docs into AM docs                                              |
> | OPENAM-24196 | SAML documentation improvements                                                       |
> | OPENAM-24158 | Address feedback on the ForgeRock Authenticator app                                   |
> | OPENAM-24092 | Transactional authorization policies aren't supported for the JwtClaim subject type   |
> | OPENAM-24067 | Created a single drawio.png which includes the vector                                 |
> | OPENAM-24067 | Add documentation on how to rename MFA devices & update push diagram                  |
> | OPENAM-24018 | Improve IdP adapter custom script                                                     |
> | OPENAM-24014 | Fix encoding for auth header example                                                  |
> | OPENAM-23959 | Fix error in default secret alias name                                                |
> | OPENAM-23920 | Clarify requirements for environment condition and difference from subject condition  |
> | OPENAM-23855 | JDBC Audit log table note about VARCHAR limits                                        |
> | OPENAM-23746 | Incorrect `sub` value in mayAct script for delegation                                 |
> | OPENAM-23714 | Indicate only one secret can be *active* for any secret label mapping                 |
> | OPENAM-23638 | Fix DATA\_STORE setting for silent install should be dirServer                        |
> | OPENAM-23620 | Update docs for error logging in Rest API                                             |
> | OPENAM-23616 | Client secret not required for OAuth 2.0 client update request                        |
> | OPENAM-23549 | Error in documentation on scope validation                                            |
> | OPENAM-23485 | Add more info on how locale is used                                                   |
> | OPENAM-23407 | Updated Localize AM section to make it clearer that you have to download the UI first |
> | OPENAM-23394 | Clarify usage of FBC at install time                                                  |
> | OPENAM-23362 | Success redirect order is incorrect                                                   |
> | OPENAM-23359 | Added note about FBC not being supported                                              |
> | OPENAM-23281 | Document bindings for Social IdP Profile transformation script type                   |
> | OPENAM-23126 | Incorrect guidance on setSessionProperty                                              |
> | OPENAM-22853 | Add description for Token Endpoint Authentication Method is none                      |
> | OPENAM-22849 | The DS rebuild-index command doesn't have a `--useSsl` option                         |
> | OPENAM-22576 | Updating links for the push auth nodes                                                |
> | OPENAM-22576 | Update MFA related screenshots                                                        |
> | OPENAM-22173 | Provide more detail for `httpClient` script binding                                   |
> | OPENAM-22100 | Improvements to upgrading servers section                                             |
> | OPENAM-21858 | Document the fields available for SAML Name ID Mapping                                |
> | OPENAM-21849 | Configure same key for two AMs using AES                                              |
> | OPENAM-21779 | Fixed errors in legacy OAuth 2.0 endpoint docs                                        |
> | OPENAM-21744 | Removed an incorrect statement about invalidating the client-side auth session        |
> | OPENAM-21655 | Updated docs to reflect correct default setting for HTTP only cookies                 |
> | OPENAM-21638 | Clarified the valid values for the default lockout attribute                          |
> | OPENAM-21455 | Added more info around SAML 2.0 algorithms                                            |
> | OPENAM-21454 | Provide sample SAML metadata files                                                    |
> | OPENAM-21452 | Made AES Keywrap note specific to SOAP STS                                            |
> | OPENAM-20974 | Update path to incremental upgrade for amUpgrade tool                                 |
> | OPENAM-19503 | Fixed CustomIdRepoConfig `idRepoClass` method name                                    |
> | SDKS-2793    | Add bound devices to list of upgrade LDIF files                                       |

#### AM 7.5.1

> **Collapse: AM 7.5.1**
>
> |               |                                                                                                     |
> | ------------- | --------------------------------------------------------------------------------------------------- |
> | AME-29538     | Update next-generation scripting documentation with exception handling scenarios                    |
> | AME-28883     | Add info from KB about different token types in the CTS                                             |
> | AME-28766     | Documentation for new utility class script binding                                                  |
> | AME-28682     | Update options in DS command-line examples                                                          |
> | AME-27982     | Add customize account lockout message example from Knowledge Base                                   |
> | AME-27930     | Documentation on preparing a truststore should use DS 7.x security model                            |
> | AME-27726     | Add more information for activity audit log events                                                  |
> | AME-22545     | `com.sun.identity.sm.filebased_embedded_enabled` must be set to false after migration               |
> | AMAGENTS-6487 | Update info about web agent and session cookie name in line with changes to web agent docs          |
> | FRAAS-20042   | Add content from How do I check what MFA devices are registered to a user in Identity Cloud and AM? |
> | OPENAM-23277  | Update Amster upgrade section to include 7.5                                                        |
> | OPENAM-23188  | Correct steps for accessing `am-external` in auth node developer guide                              |
> | OPENAM-23078  | Update steps for letting DS manage CTS tokens                                                       |
> | OPENAM-23005  | Add section on creating trees using REST                                                            |
> | OPENAM-22972  | Request to add a statement on async in doc                                                          |
> | OPENAM-22931  | Two callbacks are incorrectly named in the documentation                                            |
> | OPENAM-22871  | Wrong default value for `STS instance is running as remote instance`                                |
> | OPENAM-22741  | Add missing step in "Configure amr claims" procedure                                                |
> | OPENAM-22641  | Correct token terminology per feedback                                                              |
> | OPENAM-22635  | Rework pruning CTS tokens                                                                           |
> | OPENAM-22607  | Link to DS docs for appropriate tuning info                                                         |
> | OPENAM-22515  | Document Logout Webhook key WebhookEventType                                                        |
> | OPENAM-22356  | Include a more useful link in Release Notes for custom auth node secrets enablement                 |
> | OPENAM-22343  | Document method return types for the script binding                                                 |
> | OPENAM-22339  | Provide example systemd script for AM                                                               |
> | OPENAM-22327  | Remove mention of Internet Explorer from AM documentation                                           |
> | OPENAM-22254  | Update browser support table for WebAuthn                                                           |
> | OPENAM-22157  | Clarify version support in upgrade instructions                                                     |
> | OPENAM-22099  | Remove misleading information about unsupported custom callbacks                                    |
> | OPENAM-22045  | Correct default log level                                                                           |
> | OPENAM-21935  | Document the maximum JWT token lifetime accepted by AM                                              |
> | OPENAM-21907  | Added a tip to the Setup guide for finding server and site IDs                                      |
> | OPENAM-21778  | Error in documentation on modifying access tokens                                                   |
> | OPENAM-20673  | Clarify device reset with WebAuthn                                                                  |
> | OPENAM-20591  | Prevent ClassNotFoundException when removing click-\* jars                                          |
> | OPENAM-19899  | Remove all instances of /UI/login                                                                   |
> | OPENAM-19575  | Check algorithm statement for /oauth2/connect/jwk\_uri                                              |
> | OPENAM-19533  | Remove unnecessary images from installation steps                                                   |
> | OPENAM-19395  | Distinguish between general mail server and self-service mail service                               |
> | SDKS-3173     | The PingOne Worker service requires a configured OAuth 2.0 provider service                         |
> | SDKS-2861     | Add PingOne Protect nodes to the list of nodes                                                      |

#### AM 7.5.0

> **Collapse: AM 7.5.0**
>
> |              |                                                                                                |
> | ------------ | ---------------------------------------------------------------------------------------------- |
> | OPENAM-22207 | List HiddenValueCallback as interactive not read-only                                          |
> | OPENAM-22098 | Additional information required in JWT validation example                                      |
> | OPENAM-22065 | Fix Knowledge Base link in documentation                                                       |
> | OPENAM-22061 | The Get Session Data Node updates the objectAttributes                                         |
> | OPENAM-21964 | Update and align documentation for secret default mappings                                     |
> | OPENAM-21914 | Clarify deprecation and replacement of shared and transient state bindings                     |
> | OPENAM-21900 | The Identify Existing User Node updates the shared state username                              |
> | OPENAM-21885 | Clarify statement on realms in the API Explorer docs                                           |
> | OPENAM-21882 | Document minimum OTP length for HOTP Generator node                                            |
> | OPENAM-21851 | Clarify use of setting for the IdP                                                             |
> | OPENAM-21801 | Next generation scripting: Update nodeState.getObject                                          |
> | OPENAM-21798 | Next generation scripting: Document "get" wrapper functions                                    |
> | OPENAM-21759 | Clarify use of Java class allowlisting in next-generation scripting                            |
> | OPENAM-21754 | Add warning to library scrips about use of third party libraries                               |
> | OPENAM-21723 | Attribute Present Decision node: Add note about case-sensitivity                               |
> | OPENAM-21711 | Incorrect `acr_values` step in Backchannel request grant                                       |
> | OPENAM-21706 | Policy evaluation will succeed for failed transactional authorization under certain conditions |
> | OPENAM-21699 | Fix example for authenticating to specific services                                            |
> | OPENAM-21696 | Add a note to the Set Custom Cookie node docs around host vs domain cookies                    |
> | OPENAM-21670 | Setup guide: Check and update link to affinity load balancing                                  |
> | OPENAM-21667 | Sessions guide: Set JWT token expiry if you update max session TTL                             |
> | OPENAM-21622 | Retry limit decision node: Wrong shared state property name                                    |
> | OPENAM-21620 | Node development: Improve and correct Node class documentation                                 |
> | OPENAM-21603 | Missing spaces in catalina opts example prevents tomcat starting                               |
> | OPENAM-21504 | List Prometheus output with better description                                                 |
> | OPENAM-21418 | Fix numbering in JWT profile sequence diagram                                                  |
> | OPENAM-21413 | Sample script in SAML docs does not work                                                       |
> | OPENAM-21344 | Update profile data scripting examples with try-catch blocks                                   |
> | OPENAM-20906 | Artifact changes in AM 7.3 are not documented in Release Notes                                 |
> | OPENAM-20752 | OAuth2 scripted policy condition variables needs updating                                      |
> | OPENAM-20522 | State in docs that Sector Identifier URI is needed for Pairwise OAuth2Client profile           |
> | OPENAM-20349 | Add detail to the Device Match node docs                                                       |
> | OPENAM-19204 | Customer cannot rely on Transient Node data for WebAuthN Authentication Node                   |
> | OPENAM-18095 | Update documentation with all available audit log fields                                       |

## Known issues

The following important issues remained open at the time of the latest release for each version.

Releases are cumulative, so if an issue in a previous version isn't listed as [fixed](fixes.html), it remains open in the latest version.

### AM 8.1.x

#### AM 8.1.1

There are no new issues identified in AM 8.1.1.

#### AM 8.1.0

|              |                                                                                                                                 |
| ------------ | ------------------------------------------------------------------------------------------------------------------------------- |
| AME-33815    | Persistent Cookie tree generates a new cookie with different setup on success                                                   |
| AME-31157    | OAuth 2.0 `/access_token` endpoint respects `response_mode` for error responses                                                 |
| OPENAM-23778 | AM issues unindexed search when `ttlsupport.enabled=true`                                                                       |
| OPENAM-23703 | Custom and native claims in a refreshed, stateless access token don't match the parent modified stateless access token          |
| OPENAM-23680 | Server default settings may not be correctly updated on upgrade                                                                 |
| OPENAM-23607 | Composite advice `AuthenticateToTreeConditionAdvice` not behaving as expected                                                   |
| OPENAM-21682 | OAuth 2.0: AM doesn't redirect back to the client if consent is denied and no `redirect_uri` is present in the query parameters |
| OPENAM-18544 | AM access audit logging incorrectly reports a failure for responses that return an HTTP 302 redirect                            |

### AM 8.0.x

#### AM 8.0.2

|              |                                                                                            |
| ------------ | ------------------------------------------------------------------------------------------ |
| OPENAM-25535 | FBC to FBC upgrade requires manual copy of `noninteractive-install.properties` file        |
| OPENAM-25326 | Successful login with unknown user causes error when account lockout enabled               |
| OPENAM-24327 | Server name not set as cookie domain when cookie domain global setting is empty            |
| OPENAM-23940 | Safari displays Server Error page using authentication tree with SAML2 Authentication node |
| OPENAM-23680 | Upgrades may overwrite changes to server default properties                                |
| OPENAM-23573 | Amster exports only specific UMA server settings, not the server defaults                  |
| OPENAM-23565 | Global services requests fail after Amster import                                          |
| OPENAM-21100 | SAML 2.0 IDP SLO using HTTP redirect not working as expected on AM cluster                 |
| OPENAM-20226 | The Agent Admin privilege doesn't allow creating/updating/reading of Agent profiles        |

#### AM 8.0.1

There are no new issues identified in AM 8.0.1.

#### AM 8.0.0

|              |                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| ------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| AME-31109    | Amster 8.0 import fails with `NoSuchMethodError`                                                                                                                                                                                                                                                                                                                                                                                         |
| OPENAM-25462 | In Node Designer, the `defaultValue` property doesn't work for custom nodes when using AM 8.0.0 or 8.0.1 with Java 21                                                                                                                                                                                                                                                                                                                    |
| OPENAM-23960 | Unable to build AM 8.0 or 8.0.1 due to `click-nodeps:2.3.0-forgerock-jakarta-2` dependency on `commons-fileupload` SNAPSHOT version                                                                                                                                                                                                                                                                                                      |
| OPENAM-23851 | The `AM-8.0.0.zip` (and `AM-8.0.1.zip`) Distribution Kits are missing several files required to build the sample base Docker image (`am-empty`). As a result, the [steps to build your own AM Docker images](https://docs.pingidentity.com/forgeops/2025.2/reference/base-docker-images.html#base-images) will fail.+ NOTE: This issue only affects self-managed Docker environments where you're attempting to build your own AM image. |
| OPENAM-23770 | WebAuthn node flow causes exception instead of `Client Error` outcome when passkey prompt cancelled                                                                                                                                                                                                                                                                                                                                      |
| OPENAM-23763 | Next button not enabled on Configuration Data Store Settings page of install wizard                                                                                                                                                                                                                                                                                                                                                      |
| OPENAM-23717 | Access token requests fail when default tree uses Set Persistent Cookie node                                                                                                                                                                                                                                                                                                                                                             |
| OPENAM-23595 | A `redirect_uri` using a URN results in a malformed redirect location                                                                                                                                                                                                                                                                                                                                                                    |
| OPENAM-23582 | WebAuthn's `pubKeyCredParams` sequence isn't honored and changes on AM restart                                                                                                                                                                                                                                                                                                                                                           |
| OPENAM-23322 | Formatting errors in SAML metadata certificate export                                                                                                                                                                                                                                                                                                                                                                                    |
| OPENAM-23155 | Agent group inheritance settings are lost during Amster export/import                                                                                                                                                                                                                                                                                                                                                                    |
| OPENAM-17819 | AM admin UI doesn't show leading `.` for cookie domains                                                                                                                                                                                                                                                                                                                                                                                  |
| OPENAM-17818 | Domain cookie with leading `.` is configured although no cookie domain is specified during install                                                                                                                                                                                                                                                                                                                                       |

### AM 7.5.x

#### AM 7.5.2

|              |                                                                                                    |
| ------------ | -------------------------------------------------------------------------------------------------- |
| OPENAM-23998 | RhinoJS Date() doesn't calculate DaylightSavingTime correctly in a next-generation script          |
| OPENAM-23481 | Token is allowed in raw JSON in introspect request                                                 |
| OPENAM-23227 | OIDC ID Token Validator node doesn't work with proxy settings                                      |
| OPENAM-23035 | AM should preserve `setAttribute` multivalue update order                                          |
| OPENAM-22967 | Config upgrader uses OS file encoding causing issues with special characters                       |
| OPENAM-22952 | SMSEntry class should throw exception to avoid NullPointerException                                |
| OPENAM-22812 | Create Object node logs failure at debug level instead of error/warning                            |
| OPENAM-22777 | Deploying AM 7.5.0 on Wildfly 26.x with JDK 17 fails                                               |
| OPENAM-22770 | Configuring AES Key Wrap encryption for Tomcat doesn't work                                        |
| OPENAM-22700 | OAuth 2.0 introspect: Multi-audience token only checks against first value                         |
| OPENAM-22670 | DJLDAPv3Repo `getDN` may return broken cached DN                                                   |
| OPENAM-22663 | WS-Federation SLO calls cleanup directive if issued                                                |
| OPENAM-22530 | OAUTH\_REQUEST\_ATTRIBUTES cookie is set for HTTP GET `/authorize` requests                        |
| OPENAM-22505 | Scripted policy condition fails with "Exception from invocation expected to be handled by promise" |
| OPENAM-22386 | Next-generation `idRepository` binding doesn't return null if identity isn't found                 |
| OPENAM-22031 | LDAP Decision node no longer displays locked account message but redirects to failed login         |
| OPENAM-19968 | IdP-initiated SAML SLO doesn't invalidate SP-side session using integrated mode                    |

#### AM 7.5.1

|              |                                                                                                                                           |
| ------------ | ----------------------------------------------------------------------------------------------------------------------------------------- |
| OPENAM-23045 | Performance degradation and WS-Federation issues with Java 17                                                                             |
| OPENAM-23022 | Transaction condition for policy evaluation fails with JWT subject                                                                        |
| OPENAM-22927 | WebAuthn Registration node should be able to use `user.name` as display attribute                                                         |
| OPENAM-22616 | Upgrade from AM 6.5.5 to 7.5 using external CTS fails with error "Message:Service does not exist: GoogleSecretManagerSecretStoreProvider" |
| OPENAM-22457 | Amster doesn't delete all default scripts when using `--clean` true flag                                                                  |
| OPENAM-22406 | Product ZIP file contains files prefixed with `openam`                                                                                    |
| OPENAM-19453 | CTS authentication sessions may cause tree to fail if AM server is not configured for sticky load balancing                               |
| OPENAM-14790 | OAuth 2.0 scope policy set fails with LDAP filter environment condition                                                                   |

#### AM 7.5.0

|              |                                                                                       |
| ------------ | ------------------------------------------------------------------------------------- |
| OPENAM-22151 | Expiration of cache held in StatelessJWTCache could cause Internal Server Error       |
| OPENAM-22067 | Stateless Session denylist caching and bloomfilter layers removed on config change    |
| OPENAM-22031 | LDAP Decision node change of behavior when user is locked from password change screen |
| OPENAM-21820 | Set policy result TTL to `0` when using Environment Policy Active Session             |
| OPENAM-21819 | Default value for LinkedIn configuration uses out of data scopes                      |
| OPENAM-21683 | AM lets you create anonymous user when it already exists                              |
| OPENAM-15948 | Update DS profiles to add VLV indexes for CTS use                                     |

## Limitations

The following limitations are inherent to the design, not bugs to be fixed.

### Redundant files

The installation and upgrade wizards use three libraries that you should remove for security reasons.

When your installation or upgrade is complete, remove the following `.jar` files from the `WEB-INF/lib` directory:

* `click-extras-2.3.0.jar`

* `click-nodeps-2.3.0.jar`

* `velocity-1.7.jar`

These files are used *only* by the wizards. Removing them will have no effect on your installed instance.

### Evaluation installations

Sometimes, installing AM for evaluation purposes will fail with a message similar to the following if the JDK's default truststore's permissions are `444`:

```
$JAVA_HOME/lib/security/cacerts (Permission denied), refer to install.log under /path/to/install.log for more information.
```

To work around this issue, locate the truststore that your container is using and change its permissions to `644` before installing AM:

```
$ sudo chmod 644 $JAVA_HOME/lib/security/cacerts
```

You can change the permissions to their original settings after you have installed AM.

### Identity and data store scaling

The connection strings to the data or identity stores are static and not hot-swappable. This means that, if you expand or contract your DS affinity deployment, AM will not detect the change. To work around this, either:

* Manually add or remove the instances from the connection string and restart AM or the container where it runs.

* Configure a [DS proxy](https://docs.pingidentity.com/pingds/8.1/config-guide/proxy.html) in front of the DS instances to distribute data across many DS *shards*, and configure the proxy address in the connection string.

### Web Authentication (WebAuthn)

AM doesn't support the following functionality, as described in the [Web Authentication specification](https://www.w3.org/TR/webauthn/):

* Registration

  * AM doesn't support [Token Binding](https://datatracker.ietf.org/doc/html/draft-ietf-tokbind-protocol-19#token-binding).

  * [Web Authentication extensions](https://www.w3.org/TR/webauthn/#extensions) aren't supported.

  * [Credential ID](https://www.w3.org/TR/webauthn/#credential-id) values aren't verified against the credential IDs registered with all existing users.

  * The ECDAA signature of the [Packed attestation format](https://www.w3.org/TR/webauthn/#packed-attestation) isn't supported.

* Authentication

  * [Token Binding](https://datatracker.ietf.org/doc/html/draft-ietf-tokbind-protocol-19#token-binding) isn't supported.

  * [Web Authentication extensions](https://www.w3.org/TR/webauthn/#extensions) aren't supported.

  * [Signature counters](https://www.w3.org/TR/webauthn/#signature-counter) aren't supported.

Refer to [MFA: Web Authentication (WebAuthn)](https://docs.pingidentity.com/pingam/7.3/authentication-guide/authn-mfa-webauthn.html) for more information.

### AM admin UI access requires the `Realm Admin` privilege

In this version of AM, administrators can use the AM admin UI as follows:

* Delegated administrators with the `Realm Admin` privilege can access full AM admin UI functionality within the realms they administer. In addition, delegated administrators in the Top Level Realm who have this privilege can access AM's global configuration.

* Administrators with fewer privileges, such as the `Policy Admin` privilege, can't access the AM admin UI.

* The top-level administrator, such as `amAdmin`, has access to full AM admin UI functionality in all realms and can access AM's global configuration.

### Specifying keys in JWT headers

AM ignores keys specified in JWT headers, such as `jku` and `jwe`. Configure the public keys or certificates in AM instead, as explained in the relevant sections of the documentation.

### Different AM versions within a site

Different AM versions within a site aren't supported. Don't run different versions of AM together in the same AM site.

### Special characters in policy, application, or referral names

Don't use special characters in policy, application or referral names (for example, "my+referral"). AM returns a 400 Bad Request error. The special characters are:

* double quotes (")

* plus sign (+)

* comma (,)

* less than (<)

* equals (=)

* greater than (>)

* backslash (\\)

* null (\u0000)

### XACML policy import and export from different vendors

AM can only import XACML 3.0 files that were created by an AM instance, or that have had minor manual modifications, due to the reuse of some XACML 3.0 parameters for non-standard information.

### UMA

UMA is not currently supported in the Platform End User UI.

### Amster

Amster has the following known limitations:

* **No support for load balanced deployments**

  Amster can't connect to a load balancer URL. You must connect Amster directly to a single AM instance. Using a load balancer could send sequential commands to different AM instances, and could result in concurrency issues when writing to the underlying configuration store.

* **Bulk import to external application stores with affinity**

  If affinity is enabled for an external application data store, bulk import intermittently fails with errors similar to the following:

  `Resource path 'http////////eea87a38e3ca476fa93a3669375ada3a' contains empty path elements`

  Before using Amster for a bulk import to an application store, disable data store affinity, or remove the load balancer from the application store deployment. You can re-enable affinity when the import has completed.

* **Importing resources containing slash characters can fail**

  Some PingAM resources have names that can contain slash characters (`/`), for example policy names, application names, and SAML v2.0 entities. These slash characters can cause unexpected behavior and failures in Amster when importing into PingAM instances running on Apache Tomcat.

  To workaround this issue, configure Apache Tomcat 8.5 or 9 to allow encoded slash characters by updating the `CATALINA_OPTS` environment variable. For example:

  On Unix/Linux systems:

  ```
  $ export CATALINA_OPTS= \
    "-Dorg.apache.tomcat.util.buf.UDecoder.ALLOW_ENCODED_SLASH=true"
  $ startup.sh
  ```

  On Windows systems:

  ```
  C:\> set CATALINA_OPTS= ^
    "-Dorg.apache.tomcat.util.buf.UDecoder.ALLOW_ENCODED_SLASH=true"
  C:\> startup.bat
  ```

  |   |                                                                                                                                                                                                                                                               |
  | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | It's strongly recommended that you do *not* enable `org.apache.tomcat.util.buf.UDecoder.ALLOW_ENCODED_SLASH` when running AM in production as it introduces a security risk on Apache Tomcat. Additionally, this setting isn't supported on Apache Tomcat 10. |

  Learn more in [How do I safely enable the org.apache.tomcat.util.buf.UDecoder.ALLOW\_ENCODED\_SLASH setting in PingAM?](https://support.pingidentity.com/s/article/How-do-I-safely-enable-the-org-apache-tomcat-util-buf-UDecoder-ALLOWENCODEDSLASH-setting-in-PingAM) in the *Knowledge Base*.

* **\[INFO] messages showing on SuSE on Amster start up**

  Running Amster on SuSE may produce `[INFO]` messages, for example:

  ```
  # ./amster
  [INFO] Unable to bind key for unsupported operation: up-history
  [INFO] Unable to bind key for unsupported operation: down-history
  [INFO] Unable to bind key for unsupported operation: up-history
  [INFO] Unable to bind key for unsupported operation: down-history
  OpenAM Shell (version build build, JVM: version)
  Type ':help' or ':h' for help.
  -----------------------------------------------------
  am>
  ```

  These messages are caused by the keyboard mappings configured in the `/etc/inputrc` file and can safely be ignored, as they don't affect functionality.

## Interface stability

Interfaces labeled as *Evolving* in the documentation may change without warning. In addition, the following rules apply:

* All Java APIs are Evolving, except `com.*` packages, which are Internal/Undocumented.

* Interfaces that aren't described in released product documentation should be considered *Internal/Undocumented*.

* Also refer to the [Deprecated](deprecation.html) and [Removed](removed.html) features.

### Product release levels

Ping Identity defines Major, Minor, Maintenance, and Patch product release levels. The version number reflects the release level. The release level tells you what sort of compatibility changes to expect.

**Release level definitions**

| Release Label      | Version Numbers                                               | Characteristics                                                                                                                                                                                                                                                                                                                |
| ------------------ | ------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Major              | Version: x\[.0.0] (trailing 0s are optional)                  | * Bring major new features, minor features, and bug fixes.

* Can include changes even to Stable interfaces.

* Can remove previously Deprecated functionality, and in rare cases remove Evolving functionality that hasn't been explicitly Deprecated.

* Include changes present in previous Minor and Maintenance releases. |
| Minor              | Version: x.y\[.0] (trailing 0s are optional)                  | - Bring minor features, and bug fixes.

- Can include backwards-compatible changes to Stable interfaces in the same Major release, and incompatible changes to Evolving interfaces.

- Can remove previously Deprecated functionality.

- Include changes present in previous Minor and Maintenance releases.                  |
| Maintenance, Patch | Version: x.y.z\[.p]The optional *p* reflects a Patch version. | * Bring bug fixes

* Are intended to be fully compatible with previous versions from the same Minor release.                                                                                                                                                                                                                   |

### Product stability labels

Ping Advanced Identity Software supports many features, protocols, APIs, GUIs, and command-line interfaces. Some of these are standard and very stable. Others offer new functionality that's continuing to evolve.

Ping Identity acknowledges you invest in these features and interfaces and so need to understand when they're expected to change. For that reason, we define stability labels and use these definitions in Ping Advanced Identity Software products.

**Stability label definitions**

| Stability Label       | Definition                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| --------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Stable                | This documented feature or interface is expected to undergo backwards-compatible changes only for major releases.Changes may be announced at least one minor release before they take effect.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Evolving              | This documented feature or interface is continuing to evolve and so is expected to change, potentially in backwards-incompatible ways even in a minor release. Changes are documented at the time of product release.While new protocols and APIs are still in the process of standardization, they're Evolving. This applies, for example, to recent Internet-Draft implementations and to newly developed functionality.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Legacy                | This feature or interface has been replaced with an improved version, and is no longer receiving development effort from Ping Identity.You should migrate to the newer version, however the existing functionality will remain.Legacy features or interfaces will be marked as *Deprecated* if they're scheduled to be removed from the product.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| Deprecated            | This feature, interface, or node version is deprecated, and likely to be removed in a future release.For previously stable features, interfaces, or node versions, the change was likely announced in a previous release.Deprecated features, interfaces, or node versions will be removed from Ping Identity products.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Removed               | This feature, interface, or node version was deprecated in a previous release, and has now been removed from the product.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| Technology Preview    | Technology previews provide access to new features that are considered as new technology that isn't yet supported. Technology preview features may be functionally incomplete, and the function as implemented is subject to change without notice.*DON'T DEPLOY A TECHNOLOGY PREVIEW INTO A PRODUCTION ENVIRONMENT.*Customers are encouraged to test drive the technology preview features in a non-production environment, and are welcome to make comments and suggestions about the features in the associated forums.Ping Identity does not guarantee that a technology preview feature will be present in future releases, the final complete version of the feature is liable to change between preview and the final version. Once a technology preview moves into the completed version, said feature will become part of Ping Advanced Identity Software.Technology previews are provided on an "AS-IS" basis for evaluation purposes only, and Ping Identity accepts no liability or obligations for the use thereof. |
| Internal/Undocumented | Internal and undocumented features or interfaces can change without notice.If you depend on one of these features or interfaces, contact support to discuss your needs.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |

## Getting support

Ping Identity provides support services, professional services, training, and partner services to assist you in setting up and maintaining your deployments. Find a general overview of these services at <https://www.pingidentity.com>.

Ping Identity has staff members around the globe who support our international customers and partners. For details on Ping Identity's support offering, visit <https://www.pingidentity.com/support>.

Ping Identity publishes comprehensive documentation online:

* The Ping Identity [Knowledge Base](https://support.pingidentity.com/s/knowledge-base) offers a large and increasing number of up-to-date, practical articles that help you deploy and manage Ping Advanced Identity Software.

  While many articles are visible to everyone, Ping Identity customers have access to much more, including advanced information for customers using Ping Advanced Identity Software in a mission-critical capacity.

* Ping Identity product documentation, such as this document, aims to be technically accurate and complete with respect to the software documented. It is visible to everyone and covers all product features and examples of how to use them.

## Security advisories

Ping Identity issues security advisories in collaboration with our customers to address any security vulnerabilities transparently and rapidly.

Ping Identity's security advisory policy governs the process on how security issues are submitted, received, and evaluated as well as the timeline for the issuance of security advisories and patches.

You can find security advisories in the Ping Identity [Knowledge Base](https://support.pingidentity.com/s/product-roadmap?product=pingam\&tabset-84e58=3) (requires sign-on).

## Release timeline

| Release date   | AM version | Release type(1) |
| -------------- | ---------- | --------------- |
| 2026-06-30     | 8.1.1      | Maintenance     |
| **2026-03-31** | **8.1**    | **Minor**       |
| 2025-12-03     | 8.0.2      | Maintenance     |
| 2025-10-01     | 7.5.2      | Maintenance     |
| 2025-06-17     | 7.3.3      | Maintenance     |
| 2025-04-17     | 7.4.2      | Maintenance     |
| 2025-04-17     | 8.0.1      | Maintenance     |
| **2025-04-07** | **8.0**    | **Major**       |
| 2024-12-18     | 7.3.2      | Maintenance     |
| 2024-12-12     | 7.5.1      | Maintenance     |
| 2024-08-28     | 7.4.1      | Maintenance     |
| 2024-06-26     | 7.2.2      | Maintenance     |
| **2024-04-02** | **7.5**    | **Minor**       |
| 2024-02-26     | 7.3.1      | Maintenance     |
| **2023-10-02** | **7.4**    | **Minor**       |
| 2023-07-11     | 7.1.4      | Maintenance     |
| **2023-04-04** | **7.3**    | **Minor**       |
| 2023-04-04     | 7.2.1      | Maintenance     |
| 2022-10-13     | 7.1.3      | Maintenance     |
| 2022-08-02     | 6.5.5      | Maintenance     |
| **2022-06-27** | **7.2**    | **Minor**       |
| 2022-03-15     | 7.1.2      | Maintenance     |
| 2021-12-06     | 7.1.1      | Maintenance     |
| 2021-10-18     | 6.5.4      | Maintenance     |
| 2021-05-27     | 7.0.2      | Maintenance     |
| **2021-05-19** | **7.1**    | **Minor**       |
| 2020-11-03     | 7.0.1      | Maintenance     |
| 2020-09-16     | 6.5.3      | Maintenance     |
| **2020-08-10** | **7.0**    | **Major**       |
| 2020-04-30     | 5.5.2      | Maintenance     |
| 2020-04-03     | 5.5.3      | Maintenance     |
| 2020-02-17     | 6.5.2.3    | Patch           |
| 2019-10-31     | 6.5.2.2    | Patch           |
| 2019-08-27     | 6.5.2.1    | Patch           |
| 2019-06-20     | 6.5.2      | Maintenance     |
| 2019-06-04     | 6.0.0.7    | Patch           |
| 2019-04-30     | 6.5.0.2    | Maintenance     |
| 2019-04-11     | 6.5.1      | Maintenance     |
| 2019-01-15     | 6.5.0.1    | Maintenance     |
| 2018-12-06     | 6.0.0.6    | Patch           |
| **2018-11-28** | **6.5**    | **Minor**       |
| 2018-10-24     | 6.0.0.5    | Patch           |
| 2018-08-24     | 6.0.0.4    | Patch           |
| 2018-07-30     | 6.0.0.3    | Patch           |
| 2018-06-18     | 6.0.0.2    | Patch           |
| 2018-05-25     | 6.0.0.1    | Patch           |
| **2018-05-09** | **6.0**    | **Major**       |
| 2017-10-27     | 5.5.1      | Maintenance     |
| **2017-10-23** | **5.5**    | **Minor**       |

(1) For details about the scope of expected changes for different release types, see [Interface stability](stability.html).
