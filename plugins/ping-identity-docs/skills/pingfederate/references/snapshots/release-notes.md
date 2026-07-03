---
title: PingFederate 11.0 (December 2021)
description: New features and improvements in PingFederate 11.0.
component: pingfederate
version: 13.1
page_id: pingfederate:release_notes:pf_release_notes_110
canonical_url: https://docs.pingidentity.com/pingfederate/13.1/release_notes/pf_release_notes_110.html
llms_txt: https://docs.pingidentity.com/pingfederate/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 1, 2024
section_ids:
  new-features-and-enhancements: New features and enhancements
  pingone-ldap-gateway-datastore: PingOne LDAP Gateway datastore
  pingone-unified-admin-integration: PingOne unified admin integration
  management-of-configuration-encryption-keys: Management of configuration encryption keys
  secret-managers: Secret Managers
  fapi-1-advanced-final-certifications: FAPI 1 Advanced Final certifications
  flexibility-in-id-token-issuance: Flexibility in ID token issuance
  encrypted-request-objects: Encrypted request objects
  authorization-server-issuer-identification: Authorization server issuer identification
  better-private-key-jwt-validation: Better private key JWT validation
  message-customization-in-oidc-idp-connection: Message customization in OIDC IdP connection
  multi-valued-attribute-format: Multi-valued attribute format
  streamlined-initial-setup-experience: Streamlined initial setup experience
  individual-policy-management-by-api: Individual policy management by API
  console-heartbeat: Console heartbeat
  datastore-enhancements: Datastore enhancements
  migration-of-templates: Migration of templates
  new-configuration-for-dynamic-discovery-settings: New configuration for dynamic discovery settings
  email-ownership-verification-by-otp: Email ownership verification by OTP
  request-context-to-authentication-api-applications: Request context to authentication API applications
  kerberos-authentication-improvement: Kerberos authentication improvement
  contextual-information-in-session-management-api-responses: Contextual information in Session Management API responses
  security-enhancements: Security enhancements
  other-improvements: Other improvements
  resolved-issues: Resolved issues
  cluster-dynamic-oauthopenid-connect-keys: Cluster dynamic OAuth/OpenID Connect keys
  provisioning: Provisioning
  configuring-the-favicon-ico-url: Configuring the favicon.ico URL
  retrieving-oauth-clients-from-oracle-databases: Retrieving OAuth clients from Oracle databases
  unnecessary-dependency-error-banners: Unnecessary dependency error banners
  localizing-end-user-messages-from-the-authentication-api: Localizing end user messages from the authentication API
  device-authorization-flow-using-idp-connection-oauth-attribute-mapping: Device authorization flow using IdP connection OAuth attribute mapping
  multiple-sign-on-delay-template-redirects: Multiple Sign-On Delay template redirects
  logging-xmlcipherdecryptelement-called-without-a-key-and-unable-to-resolve: Logging XMLCipher::decryptElement called without a key and unable to resolve
  security-vulnerability: Security vulnerability
  response-headers-for-pf-ws-and-pf-scim-endpoints: Response headers for /pf-ws and /pf-scim endpoints
  upgrade-utility: Upgrade utility
  custom-template-specified-for-the-html-form-adapter: Custom template specified for the HTML Form Adapter
  partial-matches-for-resource-uris-with-oauth-2-0-token-exchange: Partial matches for resource URIs with OAuth 2.0 Token Exchange
  adding-attributes-to-data-source-lookups: Adding attributes to data source lookups
  microsoft-active-directory-ldif-script-for-persistent-grant-storage: Microsoft Active Directory LDIF script for persistent grant storage
  notification-publisher: Notification publisher
  target-resources-that-dont-start-with-http-or-https: Target resources that don't start with http:// or https://
  response-code-for-an-invalid-transport-method: Response code for an invalid transport method
  custom-idp-adapters-that-use-the-class-for-filterable-dropdown-controls: Custom IDP adapters that use the class for filterable dropdown controls
  memory-usage-during-certificate-revocation-list-crl-parsing: Memory usage during certificate revocation list (CRL) parsing
  known-issues-and-limitations: Known issues and limitations
  administrative-console-and-administrative-api: Administrative console and administrative API
  tlsv1-3: TLSv1.3
  tls-cipher-suite-customization: TLS cipher suite customization
  updating-java-8-to-java-11: Updating Java 8 to Java 11
  hardware-security-modules-hsm: Hardware security modules (HSM)
  sso-and-slo: SSO and SLO
  composite-adapter-configuration: Composite Adapter configuration
  self-service-password-reset: Self-service password reset
  oauth: OAuth
  customer-identity-and-access-management: Customer identity and access management
  provisioning-2: Provisioning
  logging: Logging
  database-logging: Database logging
  radius-nas-ip-address: RADIUS NAS-IP-Address
  deprecated-features: Deprecated features
  microsoft-internet-explorer-11: Microsoft Internet Explorer 11
  configcopy-tool-connection-management-service-sso-directory-service: Configcopy tool, Connection Management Service, SSO Directory Service
  oracle-directory-server-enterprise-edition: Oracle Directory Server Enterprise Edition
  snmp: SNMP
  roles-and-protocols: Roles and protocols
  s3_ping-discovery-protocol: S3_PING discovery protocol
  red-hat-enterprise-linux-install-script: Red Hat Enterprise Linux install script
---

# PingFederate 11.0 (December 2021)

New features and improvements in PingFederate 11.0.

## New features and enhancements

### PingOne LDAP Gateway datastore

New PingOne

PingFederate in the cloud can now connect to on-premise directory servers through the [PingOne LDAP gateway](https://docs.pingidentity.com/pingone/integrations/p1_ldap_gateways.html). This new capability reduces the complexity of moving to the cloud, while maintaining connectivity to on-premise end-user data.

### PingOne unified admin integration

New PingOne

Administrators can now open the PingOne unified admin from any configuration window in the PingFederate administrative console. To activate the new Home icon, enter the PingOne region and the environment ID in the `run.properties` file.

### Management of configuration encryption keys

New

PingFederate maintains a set of configuration encryption keys to encrypt sensitive configuration information provided by the administrators and decrypt them later as needed. While we continue recommending customers to protect their configuration encryption keys by [AWS KMS](../administrators_reference_guide/pf_implement_masterkey_encrypt_aws_kms.html) or custom solutions based on the PingFederate SDK (the `MasterKeyEncryptor` interface), we are introducing two enhancements in this area.

* Key rotatation: Administrators or key-management processes can now insert a new configuration encryption key into the system with one click in the administrative console or a single administrative API request. Once rotated, PingFederate starts using this new encryption key when it needs to encrypt sensitive configuration data.

* Re-encryption of configuration data: Version 11 also comes with a new `configkeymgr` command-line utility. Administrators can optionally scan, review, re-encrypt, and delete older configuration encryption keys in their systems. Furthermore, administrators can now choose to re-encrypt sensitive information when importing an archive from a different environment; this is most useful when administrators do not want to share configuration encryption keys between the two environments.

### Secret Managers

New

The new Secret Managers support allows customers to store certain credentials, such as data store credentials, in external secret management systems and have PingFederate retrieve them as needed. It helps customers comply with internal IT policies or meet and exceed their industry standards. Version 11 integrates out-of-the-box with CyberArk Credential Provider. Customers can also develop custom solutions based on the PingFederate SDK (the `SecretManager` interface), to connect to other secret management systems.

### FAPI 1 Advanced Final certifications

New

Ping Identity remains a solid contributor to the financial-grade API initiatives from the OpenID Foundation. We're proud that PingFederate is a certified implementation of various FAPI 1 Advanced Final profiles, including all profiles under Australia CDR and UK Open Banking and four profiles under Brazil Open Banking. Deploy Open Banking solutions with confidence and rest assured that we will continue to invest in OAuth, OpenID Connect, and FAPI specifications. For more information about OpenID certifications, visit <https://openid.net/certification/#FAPI_OPs>.

### Flexibility in ID token issuance

New

When processing an OpenID Connect hybrid flow, in addition to issuing an ID token from the token endpoint, PingFederate may also return an ID token from the authorization endpoint, depending on the requested response type. Administrators now have the flexibility to separate these two ID token issuances and configure their fulfillment differently. These enhancements allow our customers to comply with the regulatory requirements and open standards set by the Australian CDR and FAPI specifications.

### Encrypted request objects

New

PingFederate now supports encrypted request objects that OAuth clients send to its [Authorization endpoint](../developers_reference_guide/pf_authorization_endpoint.html) and the [Pushed authorization requests endpoint](../developers_reference_guide/pf_pushed_authoriz_request_endpoint.html). As needed, administrators can make encrypted request objects mandatory. This new capability further secures the confidentiality of authentication request parameters.

### Authorization server issuer identification

New

The OAuth 2.0 Authorization Server Issuer Identification [draft specification](https://datatracker.ietf.org/doc/html/draft-ietf-oauth-iss-auth-resp) intends to mitigate the scenario where mix-up attacks are a potential threat to all OAuth clients interacting with multiple authorization servers. As needed, administrators can enable this optional capability.

### Better private key JWT validation

New

In the context of OAuth client authentication, when processing private key JWTs from applications, PingFederate now ensures that the issuer (`iss`) claim value matches the client ID. This enhancement removes the need to use issuance criteria to enforce this validation requirement.

### Message customization in OIDC IdP connection

New

PingFederate 11 can now take the request parameters from the SAML 2.0 SP or the OpenID Connect relying party (OIDC RP) into account when building its OIDC authentication request to the third-party OpenID Provider (OP). This capability allows administrators to selectively configure the values in the outbound OIDC authentication requests if their use cases or the third-party OPs have the need to gather more information from the originating SP or RP.

### Multi-valued attribute format

New

Administrators can optionally indicate that PingFederate should always return an array for an attribute value regardless of whether the attribute contains one or multiple values. This flexibility simplifies the logic required to consume attribute values from access tokens or ID tokens.

### Streamlined initial setup experience

New

We're pleased to introduce a brand new initial setup experience, where administrators can finish their initial setup in as little as four steps, rapidly making our rock-solid capabilities available after starting PingFederate for the first time.

### Individual policy management by API

New

Administrators can now focus solely on one policy without including other policies as part of the API request when managing an individual authentication policy through the administrative API. This simplification improves the API experience and eliminates the risk of making unexpected changes in other authentication policies.

### Console heartbeat

New

Monitoring the status of the console node is now more straightforward with the addition of the `/pf/heartbeat.ping` heartbeat endpoint to the administrative port. Like its runtime counterpart, the administrative heartbeat endpoint is also capable of returning additional information. If administrators want detailed information in the responses, set the `pf.heartbeat.system.monitoring` property to `true` in the `run.properties` file.

### Datastore enhancements

New

* We expanded the REST API datastore with HTTP POST support. Administrators can connect to data repositories that prefer or require the HTTP POST method.

* Administrators can add attribute options in their LDAP directory searches. This enhancement expands what PingFederate can retrieve from the directory servers that support attribute options, PingDirectory being one of them.

* When configuring an LDAP search filter that uses one or more variables, an administrator can optionally specify default values for them, most useful in the scenarios where these variables may not contain any values at runtime.

### Migration of templates

New

Our upgrade tools now copy customized default templates from the previous installation to the new one. This improvement preserves the end-user experience and branding, making it easier to verify and move forward with version 11 and beyond.

### New configuration for dynamic discovery settings

New

Previously, administrators could only define dynamic discovery settings to discover cluster membership in the `server/default/conf/tcp.xml` file. Version 11 provides a new configuration file for these settings, `jgroups.properties` in the `bin` directory. This new approach streamlines future upgrade experiences. For new installations, we recommend defining dynamic discovery settings in the `jgroups.properties` file. While upgraded environments will continue to look for dynamic discovery settings from the `tcp.xml` file, we recommend performing a one-time migration to ease the upgrade experiences in the future.

### Email ownership verification by OTP

New

For customer identities, in addition to email ownership verification by one-time link, administrators can now enable email ownership verification by one-time passcode (OTP). This new option offers a modern verification experience. It also helps customers who prefer not to send hyperlinks via email to their consumers.

### Request context to authentication API applications

New

Administrators can optionally configure PingFederate to pass contextual information, such as the OAuth client ID or tracked HTTP parameters, from the sign-on requests to the authentication API applications. This allows developers to build applications that offer tailored experiences and satisfy branding requirements from their organizations based on contextual information from the sign-on requests.

### Kerberos authentication improvement

New

Administrators can now ensure Kerberos authentication remains functional for service tickets associated with older Kerberos service account passwords after updating the **Domain/Realm Password** field with a new password in PingFederate. This optional capability increases productivity because workforce identities are no longer required to restart their Windows sessions in order to authenticate via Kerberos.

### Contextual information in Session Management API responses

New

The Session Management API now includes IP address and User-Agent information in its responses. Clients with access to this API can learn more about their users and provide suitable offerings based on this new insight.

### Security enhancements

New

* PingFederate now supports Amazon EC2 Instance Metadata Service version 2 (IMDSv2) when AWS\_PING is the chosen dynamic discovery method. No PingFederate configuration changes are required, and IMDSv1 remains supported.

* PingFederate now records administrative timed-out events in the administrator audit log (`admin.log`).

* The **Change Password** and **Password Reset** end user-facing pages now time out after 30 minutes. This is the new default behavior for new and upgraded installations. As needed, administrators can configure a different **Password Update Timeout** value per HTML Form Adapter instance to suit the needs of their organizations.

### Other improvements

New

* PingFederate now includes HTTP/2 support for inbound requests for better performance.

* Administrators can optionally configure PingFederate to mask values obtained from tracked parameters in the server log. Look for the `MaskTrackedParams` setting in the `org.sourceid.saml20.domain.mgmt.impl.TrackedHttpParamManagerImpl.xml` file.

* Administrators are free to enable the refresh token grant type independently on a per-client basis regardless of whether session validation is enabled in any Access Token Managers.

* Administrators can optionally configure PingFederate to redirect end-users back to the **Sign On** page after successfully updating their soon-to-expire password as part of their SSO requests.

* The **Reuse Existing Persistent Access Grants for Grant Types** authorization server setting is now overridable per client.

* PingFederate now supports RSAES OAEP using SHA-256 and MGF1 with SHA-256 (RSA-OAEP-256) when minting outbound ID tokens or processing inbound encrypted request objects

* Administrators can optionally restrict access to the redirectless mode per authentication API application. Additionally, administrators can further limit each application to an OAuth client to improve security around the redirectless mode of the authentication API.

* We upgraded the framework of our administrative API documentation to Swagger 2.0.

* PingFederate now preserves line breaks and indentations of OGNL expressions.

* The following templates now share the following Velocity template variables, which makes branding end-user experiences easier.

  | Templates                                                                                                                                                                                                           | Variables                                                                                                                                                                                                                                                                                                                                                                                 |
  | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  | * `identifier.first.template.html`

  * `html.form.login.challenge.template.html`

  * `html.form.login.template.html`

  * `html.form.message.template.html`

  * `html.form.password.expiring.notification.template.html` | - `$client_id` - The ID of the OAuth client used by the request

  - `$entityId` - The entity ID of the SP connection used by the request

  - `$connectionName` - The name of the SP connection used by the request

  - `$baseUrl` - The base URL of PingFederate instance

  - `$adapterId` - The IdP adapter ID used by the request

  - `$spAdapterId` - The SP adapter ID used by the request |

* Updated the following bundled components and third-party dependencies:

  * Jetty 9.4.44

  * JGroups 4.2.16

  * jose4j 0.7.9

  * Log4j 2.16.0

  * PingFederate Agentless Integration Kit 2.0.4

  * PingID Integration Kit 2.15.0

  * PingOne Integration Kit 2.4.1

  * Spring Framework 5.3.5

## Resolved issues

### Cluster dynamic OAuth/OpenID Connect keys

Fixed PF-20709

Resolved an issue that sometimes caused a cluster's dynamic OAuth/OpenID Connect keys to fail to synchronize when a node restarts.

### Provisioning

Fixed PF-27519

Resolved an issue that prevented a PingFederate provisioner from using a group of GUIDs as the source to detect new and removed records.

### Configuring the `favicon.ico` URL

Fixed PF-28074

Now PingFederate correctly applies customizations of `response-header-runtime-config.xml` to the `favicon.ico` URL.

### Retrieving OAuth clients from Oracle databases

Fixed PF-28842

Reduced the time it takes for PingFederate to retrieve OAuth clients from Oracle databases.

### Unnecessary dependency error banners

Fixed PF-29189

Unnecessary dependency error banners no longer appear in the administrative console when you use the administrative API to modify selectors or service provider adapters.

### Localizing end user messages from the authentication API

Fixed PF-29202

Now you can localize end user messages from the authentication API for registration failure scenarios.

### Device authorization flow using IdP connection OAuth attribute mapping

Fixed PF-29294

Resolved an issue that stopped PingFederate from completing a device authorization flow when using IdP connection OAuth attribute mapping.

### Multiple Sign-On Delay template redirects

Fixed PF-29318

When a proxy is in front of PingFederate, the Multiple Sign-On Delay template now redirects to the correct port.

### Logging `XMLCipher::decryptElement` called without a key and unable to resolve

Fixed PF-29352

As a service provider (SP), when PingFederate can't decrypt an assertion using the primary encryption certificate, it now logs the following message at the WARN level instead of the ERROR level: "`XMLCipher::decryptElement called without a key and unable to resolve`".

### Security vulnerability

Fixed PF-29381

Resolved a potential security vulnerability caused by web server URI mishandling.

### Response headers for `/pf-ws` and `/pf-scim` endpoints

Fixed PF-29392

Introduced the ability to add response headers to the `/pf-ws` and `/pf-scim` endpoints.

### Upgrade utility

Fixed PF-29470

Fixed the upgrade utility so that, in non-interactive mode, it retains cipher related settings that are different from the default settings in the source version. PingFederate changes to new default settings on upgrade only if the settings have not been changed from the defaults in the source install.

### Custom template specified for the HTML Form Adapter

Fixed PF-29509

Resolved an issue that caused PingFederate to render the default `forgot-password-error.html` template instead of the custom template specified in the **Password Reset Error Template** field for the HTML Form Adapter.

### Partial matches for resource URIs with OAuth 2.0 Token Exchange

Fixed PF-29668

Resolved an issue that prevented the use of partial matches for resource URIs with OAuth 2.0 Token Exchange and produced the error message: "`Unable to find a token generation policy instance to issue a token`".

### Adding attributes to data source lookups

Fixed PF-29795

Now, when administrators add an attribute to a data source lookup but do not use the attribute anywhere, such as for contract mapping or issuance criteria, the attribute persists in the administrative console and API.

### Microsoft Active Directory LDIF script for persistent grant storage

Fixed PF-29847

The Microsoft Active Directory LDIF script for persistent grant storage now creates an index for the `accessGrantGuid` attribute.

### Notification publisher

Fixed PF-29870

Resolved the following notification publisher issues:

* When the SMTP server queues a message but has not sent it yet, the log now indicates that the message was queued, not that it was sent.

* PingFederate now respects the **Connection Timeout** setting for the notification publisher's SMTP server.

* Deprecated the **Retry Attempt** and **Retry Delay** fields for the notification publisher's SMTP server and removed them from the administrative console. PingFederate can still handle API configurations with those fields but they do nothing.

### Target resources that don't start with `http://` or `https://`

Fixed PF-30002

Now target resources that don't start with `http://` or `https://` are also available for mapping and issuance criteria.

### Response code for an invalid transport method

Fixed PF-30039

Now various endpoints return `400 Bad Request `instead of `500 Internal Server Error` when they receive requests with an invalid transport method. For example, calling the ACS endpoint with a `GET` instead of a `POST` now returns `400 Bad Request`.

### Custom IDP adapters that use the class for filterable dropdown controls

Fixed PF-30232

The administrative console no longer shows an error message when you try to create an instance of a custom IDP adapter that uses the class for filterable dropdown controls, `ConnectionSelectionFieldDescriptor`.

### Memory usage during certificate revocation list (CRL) parsing

Fixed PF-30272

Reduced memory usage during certificate revocation list (CRL) parsing, which speeds up CRL retrieval and avoids memory exhaustion in the case of very large CRLs.

## Known issues and limitations

### Administrative console and administrative API

Issue

* /sp/idpConnections: For identity provider (IdP) connections, the administrative API connection support is limited to Browser SSO, WS-Trust STS, and OAuth Assertion Grant connections. As a result, when updating an IdP connection using the administrative API, it is possible to lose inbound provisioning settings previously configured using the administrative console.

* /bulk: Only resource types currently supported by the administrative API are included in the exported data. Resources not yet supported include:

  * Identity Store Provisioners

  * Inbound provisioning settings from IdP connections

  * SMS Provider settings

* Previously, the administrative API did not accurately reflect a **Persistent Grant Max Lifetime** setting of 29 days (or shorter) with the selection of the **Grants Do Not Timeout Due To Inactivity** option. As a result, if you have configured such OAuth authorization server settings and have generated a bulk export in version 10.0 through 10.0.2, we recommend that you re-generate a new bulk export after upgrading to version 10.0.3 (or a more recent version). The newly exported data does not contain the aforementioned flaw, and you can safely import it to version 10.0.3 (or a more recent version).

* When enabling mutual TLS certificate-based authentication, administrators often configure a list of acceptable client certificate issuers. When an administrator uses a browser to access the console or the administrative API documentation, PingFederate returns to the browser the list of acceptable issuers as part of the TLS handshake. If the browser's client certificate store contains multiple client certificates, the browser often presents to the user only the certificates whose issuer matches one of the acceptable issuers. However, when PingFederate runs in a Java 11 environment, Chrome presents to the administrator all its configured client certificates, regardless of whether the issuer matches one of the acceptable issuers or not.

* Prior to toggling the status of a connection with the administrative API, an administrator must ensure that any expired certificates or no longer available attributes are replaced with valid certificates or attributes; otherwise, the update request fails.

* When creating or updating a child instance of a hierarchical plugin, the administrative API retains objects with an `"inherited": false` name/value pair (or without such name/value pair altogether), ignores those with a value of `true`, and returns a 200 HTTP status code. No error messages are returned for the ignored objects.

* Using the browser's navigation mechanisms (for example, the **Back** button) causes inconsistent behavior in the administrative console. Use the navigation buttons provided at the bottom of windows in the PingFederate console.

* Using the PingFederate console in multiple tabs on one browser might cause inconsistent behavior which could corrupt its configuration.

* If authenticated to the PingFederate administrative console using certificate authentication, a session that has timed out might not appear to behave as expected. Normally (when using password authentication), when a session has timed out and a user attempts some action in the console, the browser is redirected to the login page, and then back to the administrative console after authentication is complete. Similar behavior applies for certificate authentication, in principle. However, because the browser might automatically resubmit the certificate for authentication, the browser might redirect to the administrative console and not the login page.

### TLSv1.3

Issue

For Java versions that don't support TLSv1.3 (meaning versions earlier than 8u261), PingFederate fails on start up with a `NoSuchAlgorithmException` exception. To resolve this error, remove `TLSv1.3` from the following settings in the `run.properties` file:

* `pf.tls.client.protocols`

* `pf.tls.runtime.server.protocols`

* `pf.tls.admin.server.protocols`

### TLS cipher suite customization

Issue

PingFederate's TLS cipher suites can be customized by modifying `com.pingidentity.crypto.SunJCEManager.xml` (or a similarly-named file if BCFIPS or a hardware security module (HSM) is configured). After updating the file and replicating, all cluster nodes must be restarted for the change to take effect.

### Updating Java 8 to Java 11

Issue

Updating Java version 8 to version 11 results in an error when PingFederate is already installed and running. To work around this issue, uninstall and reinstall the PingFederate Windows service by running the `UninstallPingFederateService.bat` and `InstallPingFederateService.bat` files located in `<pf_install>/pingfederate/sbin/wrapper`.

### Hardware security modules (HSM)

Issue

* For Entrust HSMs or AWS CloudHSM, PingFederate must be deployed with Oracle Server JRE 8 or Amazon Corretto 8.

* For Entrust HSMs, it is not possible to use an elliptic curve (EC) certificate as an SSL server certificate.

* For keys stored in Thales HSMs, JWT token decryption fails when using RSAES OAEP with AES-CBC-192 or AES-CBC-256. This issue only arises if PingFederate is configured with static OAuth and OpenID Connect keys and is consuming a token encrypted with one of these keys.

* When PingFederate is configured in hybrid mode with a Thales HSM, it is not possible to export a locally-stored EC key pair.

* When PingFederate is configured in hybrid mode with a Thales HSM, JWT token decryption using ECDH-ES may fail. This issue only arises if PingFederate is configured with static OAuth and OpenID Connect keys, a static key is stored locally, and PingFederate is consuming a token encrypted with this key.

* TLS 1.3 is not currently supported with any HSM.

### SSO and SLO

Issue

* When consuming SAML metadata, PingFederate does not report an error when neither the `validUntil` nor the `cacheDuration` attribute is included in the metadata. Note that PingFederate does reject expired SAML metadata as indicated by the `validUntil` attribute value, if it is provided.

* The anchored-certificate trust model cannot be used with the SLO redirect binding because the certificate cannot be included with the logout request.

* If an IdP connection is configured for multiple virtual server IDs, PingFederate will always use the default virtual server ID for IdP Discovery during an SP-initiated SSO event.

### Composite Adapter configuration

Issue

SLO is not supported when users are authenticated through a Composite Adapter instance that contains another instance of the Composite Adapter.

### Self-service password reset

Issue

Passwords can be reset for Microsoft Active Directory user accounts without the permission to change password.

### OAuth

Issue

PingFederate does not support a case-sensitive naming convention for OAuth client ID values when client records are stored in a directory server. For example, after creating a client with an ID value of `sampleClient`, PingFederate does not allow the creation of another client with an ID value of `SampleClient`.

Although it's possible to create clients using the same ID values with different casings when client records are stored in XML files, a database server, or custom storage, we recommend not doing so to avoid potential record migration issues.

### Customer identity and access management

Issue

Some browsers display a date-picker user interface for fields that have been designed for date-specific inputs. Some browsers do not. If one or more date-specific fields are defined on the registration page or the profile management page (or both), end users must enter the dates manually if their browsers do not display a date-picker user interface for those fields.

### Provisioning

Issue

* LDAP referrals return an error and cause provisioning to fail if the `user` or `group` objects are defined at the DC level, and not within an OU or within the Users CN.

* The `totalResults` value in SCIM responses indicates the number of results returned in the current response, not the total number of estimated results on the LDAP server.

### Logging

Issue

* If a source attribute has been configured for masking in an IdP adapter or IdP connection and the source attribute is mapped to OAuth's persistent grant `USER_KEY` attribute, the `USER_KEY` attribute will not be masked in the server logs. Other persistent grant attributes will be masked.

* Even if a source attribute has been configured for masking in an IdP adapter and the source attribute is mapped as the adapter's unique user key, the user key attribute is not masked in the server or audit logs.

### Database logging

Issue

* If a source attribute has been configured for masking in an IdP adapter or IdP connection and the source attribute is mapped to OAuth's persistent grant `USER_KEY` attribute, the `USER_KEY` attribute will not be masked in the server logs. Other persistent grant attributes will be masked.

* Even if a source attribute has been configured for masking in an IdP adapter and the source attribute is mapped as the adapter's unique user key, the user key attribute is not masked in the server or audit logs.

### RADIUS NAS-IP-Address

Issue

The RADIUS NAS-IP-Address is only included in Access-Request packets when the `pf.bind.engine.address` is set with an IPv4 address. IPv6 is not supported.

## Deprecated features

### Microsoft Internet Explorer 11

Info

Ping Identity commits to deliver the best experience for administrators and users. As we continue to improve our products, we encourage our customers to migrate off of Microsoft Internet Explorer 11. Starting with PingFederate 11.0, Internet Explorer 11 is no longer included in the PingFederate qualification process for administrators or users. For a list of supported browsers, see [System requirements](../installing_and_uninstalling_pingfederate/pf_system_requirements.html).

### Configcopy tool, Connection Management Service, SSO Directory Service

Info

As of PingFederate 10.2, these features have been deprecated and will be removed in a future release.

### Oracle Directory Server Enterprise Edition

Info

As Oracle ended its Premier Support for Oracle Directory Server Enterprise Edition (ODSEE 11g) in December 2019, we no longer include ODSEE as part of the PingFederate qualification process (starting with PingFederate 10.2). We continue to qualify against [Oracle Unified Directory](https://www.oracle.com/security/identity-management/directory-services/) and other supported directory servers. For a full list, see [System requirements](../installing_and_uninstalling_pingfederate/pf_system_requirements.html).

### SNMP

Info

Starting with PingFederate 10.2, monitoring and reporting through the Simple Network Management Protocol (SNMP) has been removed.

### Roles and protocols

Info

Starting with PingFederate 10.1, roles and protocols are always enabled and no longer configurable through the administrative console and API.

### S3\_PING discovery protocol

Info

Starting with PingFederate 10.1, the S3\_PING discovery protocol has been deprecated. Customers running on AWS infrastructure should instead use NATIVE\_S3\_PING.

### Red Hat Enterprise Linux install script

Info

Starting with PingFederate 10.0, the Red Hat Enterprise Linux install script is no longer available. To install PingFederate 10.0 for Linux, you must download and extract the product distribution `.zip` file.
