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

---

---
title: PingFederate 11.0.1 (January 2022)
description: Improved
component: pingfederate
version: 13.1
page_id: pingfederate:release_notes:pf_release_notes_1101
canonical_url: https://docs.pingidentity.com/pingfederate/13.1/release_notes/pf_release_notes_1101.html
llms_txt: https://docs.pingidentity.com/pingfederate/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 1, 2024
section_ids:
  new-features-and-enhancements: New features and enhancements
  rolling-grace-period-for-refresh-tokens: Rolling grace period for refresh tokens
  performance-improvement: Performance improvement
  url-region-of-the-pingone-home-button: URL region of the PingOne home button
  aws-cloudhsm-client: AWS CloudHSM client
  resolved-issues: Resolved issues
  resolved-a-potential-security-vulnerability: Resolved a potential security vulnerability
  updated-apache-log4j2: Updated Apache Log4j2
  authenticating-pingdirectory-users: Authenticating PingDirectory users
  certificate-revocation-list-checks: Certificate revocation list checks
---

# PingFederate 11.0.1 (January 2022)

## New features and enhancements

### Rolling grace period for refresh tokens

Improved

When PingFederate rotates a refresh token, if the client fails to get the new token, now PingFederate can accept the previous token for the short period that you specify with the **Refresh Token Rolling Grace Period** setting.

### Performance improvement

Info

Improved performance of the administrative console when a large number of OAuth clients are stored in LDAP or JDBC datastores.

### URL region of the PingOne home button

Info PingOne

When configuring the URL of the PingOne home button in the PingFederate administrative console, now `pf.pingone.admin.url.region` in `run.properties` supports `Canada` as a region.

### AWS CloudHSM client

Info

PingFederate can be successfully integrated with AWS CloudHSM client version 3.4.4.

## Resolved issues

### Resolved a potential security vulnerability

Security PF-30450

Resolved a potential security vulnerability that is described in security bulletin [SECBL021](https://support.pingidentity.com/s/article/SECBL021-PingFederate-Password-Reset-via-Authentication-API-Mishandling).

### Updated Apache Log4j2

Security PF-30536

Resolved a potential security vulnerability by updating Apache Log4j2 to version 2.17.1.

### Authenticating PingDirectory users

Fixed PF-30557 PingDirectory

Resolved an issue that allowed PingDirectory users to authenticate with expired passwords.

### Certificate revocation list checks

Fixed PF-30637

Resolved an issue that caused certificate revocation list (CRL) checks to return "`issuer not found in trusted CAs store`" even though the issuer certificate is present.

---

---
title: PingFederate 11.0.10 - April 2024
description: Security PF-34720
component: pingfederate
version: 13.1
page_id: pingfederate:release_notes:pf_release_notes_11010
canonical_url: https://docs.pingidentity.com/pingfederate/13.1/release_notes/pf_release_notes_11010.html
llms_txt: https://docs.pingidentity.com/pingfederate/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: April 30, 2024
section_ids:
  resolved-issues: Resolved issues
  rest-datastore-security-vulnerability: Rest datastore security vulnerability
  runtime-nodes-security-vulnerability: Runtime nodes security vulnerability
  openid-connect-policy-management-editor-security-vulnerability: OpenID Connect policy management editor security vulnerability
  slow-log-consumption-affects-performance: Slow log consumption affects performance
---

# PingFederate 11.0.10 - April 2024

## Resolved issues

### Rest datastore security vulnerability

Security PF-34720

Fixed a JSON injection vulnerability in REST datastores described in security advisory [SECADV044](https://support.pingidentity.com/s/article/SECADV044-PingFederate-Security-Rollup).

### Runtime nodes security vulnerability

Security PF-34896

Fixed a path traversal vulnerability in Runtime nodes described in security advisory [SECADV044](https://support.pingidentity.com/s/article/SECADV044-PingFederate-Security-Rollup).

### OpenID Connect policy management editor security vulnerability

Security PF-35081

Fixed a Cross-Site Scripting vulnerability in the OpenID Connect Policy Management Editor described in security advisory [SECADV044](https://support.pingidentity.com/s/article/SECADV044-PingFederate-Security-Rollup).

### Slow log consumption affects performance

Fixed PF-33368

Fixed a defect that caused performance issues for PingFederate when third-party logging services were slow to consume logging events.

---

---
title: PingFederate 11.0.2 (March 2022)
description: Info PingOne MFA
component: pingfederate
version: 13.1
page_id: pingfederate:release_notes:pf_release_notes_1102
canonical_url: https://docs.pingidentity.com/pingfederate/13.1/release_notes/pf_release_notes_1102.html
llms_txt: https://docs.pingidentity.com/pingfederate/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 1, 2024
section_ids:
  new-features-and-enhancements: New features and enhancements
  updated-pingone-mfa-adapter: Updated PingOne MFA adapter
  resolved-issues: Resolved issues
  ldap-connections: LDAP connections
  bulk-export: Bulk export
  single-sign-on-from-browsers-on-ios: Single sign-on from browsers on iOS
  ncipher-mode: nCipher mode
  tls-1-3-for-inbound-connections: TLS 1.3 for inbound connections
  symantec-vip-adapter: Symantec VIP Adapter
  ldap-related-performance: LDAP-related performance
  signature-verification-for-certificate-revocation-lists: Signature verification for certificate revocation lists
---

# PingFederate 11.0.2 (March 2022)

## New features and enhancements

### Updated PingOne MFA adapter

Info PingOne MFA

Updated the bundled PingOne MFA adapter to version 1.6.

## Resolved issues

### LDAP connections

Fixed PF-30804

Resolved an issue that caused LDAP connections to periodically fail during provisioning.

### Bulk export

Fixed PF-30863

Bulk export no longer fails to include all XML OAuth clients in the response payload.

### Single sign-on from browsers on iOS

Fixed PF-31057

Resolved an issue that caused single sign-on from browsers on iOS to fail when an authentication policy terminates on Kerberos Adapter fallback that has an existing session.

### nCipher mode

Fixed PF-31064

When running PingFederate in nCipher mode, now the administrative API successfully generates elliptic curve (EC) keys when the optional signatureAlgorithm field is not provided.

### TLS 1.3 for inbound connections

Fixed PF-31112

PingFederate now supports TLS 1.3 for inbound connections when running on Java 8 versions 8u261 and newer.

### Symantec VIP Adapter

Fixed PF-31123

Resolved an issue that prevented PingFederate from using the Symantec VIP Adapter.

### LDAP-related performance

Fixed PF-31146

Resolved an LDAP-related performance issue.

### Signature verification for certificate revocation lists

Fixed PF-31159

Resolved an issue where signature verification for certificate revocation lists could take more than 10 seconds on Windows. When LDAP-based authentication was enabled in the administrative console, this could prevent administrative users from signing on.

---

---
title: PingFederate 11.0.3 (May 2022)
description: Fixed PF30776
component: pingfederate
version: 13.1
page_id: pingfederate:release_notes:pf_release_notes_1103
canonical_url: https://docs.pingidentity.com/pingfederate/13.1/release_notes/pf_release_notes_1103.html
llms_txt: https://docs.pingidentity.com/pingfederate/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 1, 2024
section_ids:
  resolved-issues: Resolved issues
  intermittent-failure-to-respond-after-restart-caused-by-ldap-sdk: Intermittent failure to respond after restart caused by LDAP SDK
  tls-1-3-for-outbound-connections: TLS 1.3 for outbound connections
  updated-spring-framework: Updated Spring Framework
---

# PingFederate 11.0.3 (May 2022)

## Resolved issues

### Intermittent failure to respond after restart caused by LDAP SDK

Fixed PF30776

To resolve an issue in which PingFederate occasionally stopped responding after a restart, the UnboundID LDAP SDK for Java was updated to version 6.0.4.

### TLS 1.3 for outbound connections

Fixed PF-31303

PingFederate now supports TLS 1.3 for outbound connections when running on Java 8 versions 8u261 and newer.

### Updated Spring Framework

Info PF-31169

Updated Spring Framework to version 5.3.18.

---

---
title: PingFederate 11.0.4 (August 2022)
description: Fixed PF-31795
component: pingfederate
version: 13.1
page_id: pingfederate:release_notes:pf_release_notes_1104
canonical_url: https://docs.pingidentity.com/pingfederate/13.1/release_notes/pf_release_notes_1104.html
llms_txt: https://docs.pingidentity.com/pingfederate/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 1, 2024
section_ids:
  resolved-issues: Resolved issues
  masterkeyencryptor-and-cluster-replication: MasterKeyEncryptor and cluster replication
  rule-matching-for-fragment-nodes-and-nullpointerexception: Rule matching for fragment nodes and NullPointerException
  zero-byte-archives: Zero byte archives
  jwt-access-token-lifetimes: JWT access token lifetimes
---

# PingFederate 11.0.4 (August 2022)

## Resolved issues

### MasterKeyEncryptor and cluster replication

Fixed PF-31795

When PingFederate uses a custom MasterKeyEncryptor that relies on an SSL call to an external service, cluster replication no longer causes cascading failures because PingFederate cannot open Java key store files.

### Rule matching for fragment nodes and NullPointerException

Fixed PF-31929

When using rule matching for fragment nodes, PingFederate no longer raises a NullPointerException (NPE) if a fragment fails.

### Zero byte archives

Fixed PF-31966

Resolved an issue that caused PingFederate to generate a zero byte archive when it couldn't read a file in the `<pf_install>/pingfederate/server/default/data` directory.

### JWT access token lifetimes

Fixed PF-31989

When using centralized and dynamically rotating keys for OAuth and OpenID Connect, PingFederate now prevents you from setting the JWT access token lifetime to be longer than the `dynamic-rotation-period-in-days` specified in `<pf_install>/pingfederate/server/default/data/config-store/jwks-endpoint-configuration.xml`.

---

---
title: PingFederate 11.0.5 (October 2022)
description: Fixed PF-31735
component: pingfederate
version: 13.1
page_id: pingfederate:release_notes:pf_release_notes_1105
canonical_url: https://docs.pingidentity.com/pingfederate/13.1/release_notes/pf_release_notes_1105.html
llms_txt: https://docs.pingidentity.com/pingfederate/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 22, 2024
section_ids:
  resolved-issues: Resolved issues
  ipv6-address-issue: IPV6 address issue
  administrative-console-login: Administrative console login
  user-registration-defect-resolution: User registration defect resolution
---

# PingFederate 11.0.5 (October 2022)

## Resolved issues

### IPV6 address issue

Fixed PF-31735

Resolved an issue that sometimes occurred when IPV6 addresses were specified in the **HTTP Header for Client IP Addresses** field on the **Incoming Proxy Settings** window.

### Administrative console login

Fixed PF-32001

PingFederate now recovers from initial connection failure when logging into the administrative console using external LDAP authentication.

### User registration defect resolution

Fixed PF-32241

During user registration, PingFederate now sends all passwords to PingDirectory, resolving an issue where passwords consisting of only spaces would not properly register a PingDirectory password.

---

---
title: PingFederate 11.0.6 (February 2023)
description: Fixed PF-32805
component: pingfederate
version: 13.1
page_id: pingfederate:release_notes:pf_release_notes_1106
canonical_url: https://docs.pingidentity.com/pingfederate/13.1/release_notes/pf_release_notes_1106.html
llms_txt: https://docs.pingidentity.com/pingfederate/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 22, 2024
section_ids:
  resolved-issues: Resolved issues
  potential-security-vulnerability: Potential security vulnerability
---

# PingFederate 11.0.6 (February 2023)

## Resolved issues

### Potential security vulnerability

Fixed PF-32805

We've resolved a potential security vulnerability that is described in security advisory [SECADV033](https://support.pingidentity.com/s/article/SECADV033-Cross-Site-Request-Forgery-on-PingFederate-Local-Identity-Profiles-Endpoint).

---

---
title: PingFederate 11.0.7 (February 2023)
description: Fixed PF-33037
component: pingfederate
version: 13.1
page_id: pingfederate:release_notes:pf_release_notes_1107
canonical_url: https://docs.pingidentity.com/pingfederate/13.1/release_notes/pf_release_notes_1107.html
llms_txt: https://docs.pingidentity.com/pingfederate/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 22, 2024
section_ids:
  resolved-issues: Resolved issues
  server-log-warnings: Server log warnings
---

# PingFederate 11.0.7 (February 2023)

## Resolved issues

### Server log warnings

Fixed PF-33037

We've added a warning to server logs if the *ds-pwp-state-json* attribute is not present in PingDirectory's LDAP Response. This warning appears in the log every time a user interacts with the profile management page. Please enable this attribute to adhere to PingDirectory's security configuration best practices. PingDirectory version 8.1 and later supports this attribute, and customers running older versions are encouraged to upgrade to a supported version as soon as possible.

---

---
title: PingFederate 11.0.8 (August 2023)
description: Fixed PF-34017
component: pingfederate
version: 13.1
page_id: pingfederate:release_notes:pf_release_notes_1108
canonical_url: https://docs.pingidentity.com/pingfederate/13.1/release_notes/pf_release_notes_1108.html
llms_txt: https://docs.pingidentity.com/pingfederate/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 22, 2024
section_ids:
  resolved-issues: Resolved issues
  logging-validation: Logging validation
  potential-security-vulnerability: Potential security vulnerability
  potential-security-vulnerability-2: Potential security vulnerability
---

# PingFederate 11.0.8 (August 2023)

## Resolved issues

### Logging validation

Fixed PF-34017

We've improved logging validation.

### Potential security vulnerability

Fixed PF-33449

We've resolved a potential security vulnerability that is described in security advisory [SECADV037](https://support.pingidentity.com/s/article/SECADV037-PingFederate-Security-Rollup-Denial-of-Service-Information-Disclosure-Authentication-Bypass-Vulnerabilities).

### Potential security vulnerability

Fixed PF-34017

We've resolved a potential security vulnerability that is described in security advisory [SECADV037](https://support.pingidentity.com/s/article/SECADV037-PingFederate-Security-Rollup-Denial-of-Service-Information-Disclosure-Authentication-Bypass-Vulnerabilities).

---

---
title: PingFederate 11.0.9 (December 2023)
description: Fixed PF-29706
component: pingfederate
version: 13.1
page_id: pingfederate:release_notes:pf_release_notes_1109
canonical_url: https://docs.pingidentity.com/pingfederate/13.1/release_notes/pf_release_notes_1109.html
llms_txt: https://docs.pingidentity.com/pingfederate/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 22, 2024
section_ids:
  resolved-issues: Resolved issues
---

# PingFederate 11.0.9 (December 2023)

## Resolved issues

Fixed PF-29706

Fixed a Server-Side Request Forgery vulnerability in the Initial Setup Wizard described in security advisory [SECADV041](https://support.pingidentity.com/s/article/SECADV041-PingFederate-Server-Side-Request-Forgery).

---

---
title: PingFederate 11.1 (June 2022)
description: New features and improvements in PingFederate 11.1.
component: pingfederate
version: 13.1
page_id: pingfederate:release_notes:pf_release_notes_111
canonical_url: https://docs.pingidentity.com/pingfederate/13.1/release_notes/pf_release_notes_111.html
llms_txt: https://docs.pingidentity.com/pingfederate/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 1, 2024
section_ids:
  new-features-and-enhancements: New features and enhancements
  pingone-integration: PingOne integration
  jwt-secured-authorization-response-mode-jarm: JWT Secured Authorization Response Mode (JARM)
  jwt-response-for-oauth-token-introspection: JWT Response for OAuth Token Introspection
  client-secret-management: Client secret management
  api-support-for-device-authorization-grant: API support for Device Authorization Grant
  amazon-dynamodb-for-grants: Amazon DynamoDB for grants
  revocation-of-self-contained-access-tokens: Revocation of self-contained access tokens
  a-new-alert-system: A new alert system
  copy-and-paste-authentication-policies-and-fragments: Copy-and-paste authentication policies and fragments
  administrative-api-to-move-individual-policies: Administrative API to move individual policies
  cluster-configuration-management: Cluster configuration management
  passthrough-idp-adapter: Passthrough IdP Adapter
  kerberos-authentication-and-objectsid: Kerberos authentication and ObjectSID
  kerberos-authentication-and-re-authentication: Kerberos authentication and re-authentication
  more-error-handling-options: More error handling options
  extended-properties-for-end-user-interactions: Extended properties for end-user interactions
  better-documentation-in-velocity-templates: Better documentation in Velocity templates
  enhancements-in-thales-hsm-integration: Enhancements in Thales HSM integration
  secondary-signing-certificate: Secondary signing certificate
  administrative-api-improvements: Administrative API improvements
  other-improvements: Other improvements
  resolved-issues: Resolved Issues
  h2-database-engine-upgrade: H2 database engine upgrade
  a-username-in-the-url-during-change-password-flows: A username in the URL during change password flows
  guava-upgrade: Guava upgrade
  oauth-client-issuer-dn: OAuth client Issuer DN
  time-stamp-for-last-update: Time stamp for last update
  number-and-boolean-data-types-in-json-responses-from-rest-api-data-source-lookups: Number and Boolean data types in JSON responses from REST API data source lookups
  notyetconnectedexception-warning-messages-from-jgroup-in-the-server-log: NotYetConnectedException warning messages from JGroup in the server.log
  matching-oauth-clients-redirection-uris: Matching OAuth client's redirection URIs
  potential-security-vulnerability: Potential security vulnerability
  logging-invalid-assertion-errors: Logging invalid assertion errors
  null-pointer-exception-in-authentication-api-password-reset-flow: Null pointer exception in authentication API password reset flow
  determining-authentication-instants-for-flows: Determining authentication instants for flows
  templates-for-pingone-mfa-1-6-1: Templates for PingOne MFA 1.6.1
  dependency-errors-for-saml-token-processors-and-generators: Dependency errors for SAML token processors and generators
  preserving-the-order-of-map-type-configurations: Preserving the order of map type configurations
  warning-about-using-the-administrative-console-in-multiple-tabs: Warning about using the administrative console in multiple tabs
  saving-authorization-server-settings-overwrites-scope-whitelist: Saving authorization server settings overwrites scope.whitelist
  oauth-client-ids-added-to-admin-log-entries: OAuth client IDs added to admin.log entries
  honoring-the-property-for-maximum-http-request-body-size: Honoring the property for maximum HTTP request body size
  known-issues-and-limitations: Known issues and limitations
  administrative-console-and-administrative-api: Administrative console and administrative API
  tlsv1-3: TLSv1.3
  tls-cipher-suite-customization: TLS cipher suite customization
  java: Java
  hardware-security-modules-hsm: Hardware security modules (HSM)
  sso-and-slo: SSO and SLO
  composite-adapter-configuration: Composite Adapter configuration
  self-service-password-reset: Self-service password reset
  oauth: OAuth
  customer-identity-and-access-management: Customer identity and access management
  provisioning: Provisioning
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

# PingFederate 11.1 (June 2022)

New features and improvements in PingFederate 11.1.

## New features and enhancements

### PingOne integration

New PingOne

We've added Kerberos authentication via PingOne and the PingOne LDAP Gateway Data Store. This new capability allows PingFederate in the cloud, without a direct connection to Active Directory, to complete Kerberos authentication for browser-based SSO requests and STS transactions through PingOne.

### JWT Secured Authorization Response Mode (JARM)

New

We're proud to support [JWT Secured Authorization Response Mode](https://openid.net/specs/openid-financial-api-jarm.html) (JARM) in version 11.1. JARM allows authorization servers to transmit authorization responses in JSON web tokens (JWTs), providing digital signature and encryption, sender authentication, and audience restriction. As JARM becomes a requirement in FAPI 2, you can deploy open banking solutions confidently.

### JWT Response for OAuth Token Introspection

New

We're also introducing support for [JWT Response for OAuth Token Introspection](https://datatracker.ietf.org/doc/html/draft-ietf-oauth-jwt-introspection-response), a draft specification on track to become one of the authorization server requirements in the FAPI 2 Advanced Profile. JWT-secured introspection responses provide stronger assurance to the introspection requesters, most relevant when the requester, such as a resource server, expects to receive verified claims from the authorization server.

### Client secret management

New

Seamless client secret rotation no longer requires real-time coordination between PingFederate administrators and the application development teams. You can now configure PingFederate to retain previous secrets for a configurable period, during which the application teams can work on updating the client secrets in their apps. This enhancement drastically lowers the costs of securing applications that use client secrets for authentication. For more information, see "Client Secret Retention Period" in the topic [Managing client configuration defaults](../administrators_reference_guide/help_clientsettingstasklet_oauthdynamicclientregistrationdefaultsstate.html).

### API support for Device Authorization Grant

New

In addition to template-driven user experience, the user authorization step from Device Authorization Grant supports API now. You can also decide whether PingFederate should check the device activation code before or after authentication. These new capabilities enable you to build applications with the desired user experience for input-constrained devices, such as smart TVs or telepresence equipment.

### Amazon DynamoDB for grants

New

You can store OAuth persistent grants in Amazon DynamoDB, which allows you to take advantage of a NoSQL database where it matters most: delivering responsive experiences to globally distributed users and offering high availability at ease.

### Revocation of self-contained access tokens

New

You can optionally enable direct revocation for self-contained access tokens (JWT access tokens). This flexibility provides a secure way to invalidate access tokens without revoking the underlying refresh tokens or persistent grants. For more information, see [Configuring an access token management instance](../administrators_reference_guide/pf_configuring_access_token_management_instance.html) and its description of the **Enable Token Revocation** checkbox.

### A new alert system

New

PingFederate 11.1 centralizes alerts, such as the reminder to replicate configuration, under the new **bell** icon in the top menu. You can review important alerts from any configuration window.

![the bell icon displays important alerts](../_images/oqv1655324045023.png)

### Copy-and-paste authentication policies and fragments

New

Previously, if you wanted to update an authentication policy or a reusable policy fragment midstream, they had to reconfigure all downstream paths, which can take some effort. With PingFederate 11.1, you can copy a subtree of policy paths before removing a step (such as an IdP adapter), adding a new step (such as a selector or another IdP adapter), and then pasting the subtree back to the policy. This new capability applies to reusable policy fragments and between authentication policies and reusable policy fragments.

### Administrative API to move individual policies

New

You can use the administrative API to move an individual policy to a specific location. This enhancement makes re-organizing policies by API requests easier and safer.

### Cluster configuration management

New

PingFederate engine nodes now capture common configuration replication issues in their server logs and send replication status back to the console node. The **Cluster Management** window provides live updates when you select **Replicate Configuration** in the **Cluster Management** window. If an error occurs, you can act on it immediately and recover from potential outages faster.

### Passthrough IdP Adapter

New

You can now associate authentication sessions with user identities passed through the new Passthrough Identity Provider (IdP) Adapter. By placing the Passthrough IdP Adapter downstream from an IdP connection in a policy tree, you can take advantage of additional capabilities associated with defining a user key. For example, you can use the user key to query or revoke a user's authentication sessions.

### Kerberos authentication and ObjectSID

New

The Kerberos Adapter and the Kerberos Token Processor now return the `ObjectSID` attribute value. Because `ObjectSID` uniquely identifies the user in Active Directory, leveraging it helps streamline the **Attribute Source & Lookup** configuration.

### Kerberos authentication and re-authentication

New

You can configure the Kerberos Adapter to fail when the service provider asks for re-authentication by including `ForceAuthn=true` (SAML 2.0) or `prompt=login` (OpenID Connect) in their authentication requests. For example, suppose user interactions are required when the partners ask for re-authentication. In that case, you can add the HTML Form Adapter to the **Fail** policy path of the Kerberos Adapter.

### More error handling options

New

* You now can configure individual authentication policies to handle authentication failures locally without redirecting to the service providers or returning error messages to the OAuth clients. This flexibility addresses the scenario where an IdP-oriented end-user experience is desirable.

* PingFederate now includes error results from issuance criteria in error responses. Partners can use the error results to resolve issues as needed. If the invoked policy is configured to handle failures locally, you can do the same to improve the end-user experience.

* You can now optionally configure the HTML Form Adapter not to return control to PingFederate when an account lockout occurs. Instead, PingFederate returns a "please try again later" message to the browser or the authentication API application.

### Extended properties for end-user interactions

New

You can now leverage extended properties in Velocity templates when customizing template-driven end-user interactions. You can reference extended properties in the templates instead of creating multiple `If`/`ElseIf`/`Else` directives, significantly reducing the initial effort. New and updated experiences can be inherited from extended property values from the OAuth client records and Browser SSO connections, eliminating most of the maintenance costs. PingFederate also passes extended property values to authentication API applications. As a result, application developers who create and maintain end-user UX for customer identities will benefit from this new enhancement.

### Better documentation in Velocity templates

New

We've also improved inline documentation in our Velocity templates. Moving forward, we will maintain variable names and their definitions consistently to communicate changes, such as introducing new variables.

### Enhancements in Thales HSM integration

New

Both Java 11 and 8 environments are supported when integrating with Thales Luna Cloud Hardware Security Module (HSM) Services or Luna Network HSMs. For more information about Thales Luna HSM Client, see the [Luna Cloud HSM Service Client Guide](https://thalesdocs.com/dpod/services/luna_cloud_hsm/extern/client_guides/Content/CRN/Luna/client/10-4-1.htm) and [Luna Network HSM Documentation Archive](https://thalesdocs.com/gphsm/luna/7/docs/network/Content/CRN/Luna/client/10-4-0.htm).

### Secondary signing certificate

New

You can now add a secondary signing certificate to your connections. If configured, PingFederate includes it in both the metadata exports and the metadata URL responses. This flexibility allows you to notify your partners about upcoming changes more easily through metadata.

### Administrative API improvements

New

We improved the PingFederate administrative API to manage the following configurations:

* JIT provisioning settings in IdP connections

* **System > Data & Credential Stores > Identity Store Provisioners**

* **System > Server > General Settings**

* **System > Server > WS-Trust Settings**

### Other improvements

New

* We significantly improved our metrics exposed through HTTP (at the heartbeat endpoint) and JMX to help you detect and diagnose performance issues. Both channels include HTTP response code counts, data source response time statistics, and Jetty queue size information; these metrics help troubleshoot latency issues associated with datastores or traffic volume.

* PingFederate now uses OCSP to obtain certificate revocation status by default on new installations. As part of this enhancement, PingFederate uses the OCSP responder URL provided in the certificate first, followed by the now optional Default OCSP Responder URL, and lastly, CRL, making the certificate validation process more efficient.

* The administrative console now provides guidance when you attempt to import a configuration archive obtained from a different version of PingFederate.

* PingFederate 11.1 supports Amazon IAM roles for service accounts, which increases security posture with credential isolation and auditability.

* PingOne Verify is now part of the PingFederate distribution `.zip` file and Windows installer.

* We also updated the following bundled components and third-party dependencies:

  * PingID Integration Kit 2.17

  * PingOne Fraud Integration Kit 1.0

  * PingOne Protect Integration Kit 1.2

  * Jackson-Databind 2.12.7

  * Log4j2 2.17.2

  * Spring Framework 5.3.20

## Resolved Issues

### H2 database engine upgrade

Fixed PF-21198

Upgraded the H2 database engine to version 2.1.210.

### A username in the URL during change password flows

Fixed PF-24501

The username no longer appears in the URL during change password flows.

### Guava upgrade

Fixed PF-28932

Upgraded the Guava dependency to version 30.1.1.

### OAuth client Issuer DN

Fixed PF-29368

If the administrative API was used to create an OAuth client that has the Client Certificate authentication type, and the client's Issuer DN does not have a normalized DN value, the administrative console's **Client** window no longer fails to show the Issuer DN as the default value. This issue didn't affect runtime behavior.

### Time stamp for last update

Fixed PF-29761

When a user record in a datastore mistakenly has a future date for the last update time, PingFederate no longer uses that date as the value of `attrib_last_timestamp` in the `channel_variable` table. Instead, PingFederate sets the value to the maximum time stamp that is not in the future.

### Number and Boolean data types in JSON responses from REST API data source lookups

Fixed PF-29835

The JSON response from REST API data source lookups now retains number and Boolean data types instead of converting them to strings.

### `NotYetConnectedException` warning messages from JGroup in the `server.log`

Fixed PF-30075

Resolved an issue that caused the `NotYetConnectedException` warning message to repeatedly appear in the `server.log` when using AWS\_PING for dynamic cluster discovery.

### Matching OAuth client's redirection URIs

Fixed PF-30146

If the OAuth client's redirection URI contains a wild card in the authority part of the URI, and the `redirect_uri` parameter of the token request contains userinfo in the authority part, then PingFederate will no longer consider the redirection URI a match.

### Potential security vulnerability

Fixed PF-30255

Resolved a potential security vulnerability.

### Logging invalid assertion errors

Fixed PF-30495

In a specific case, when PingFederate logs an invalid assertion error, the error message no longer fails to include a remark about why the assertion or response is invalid.

### Null pointer exception in authentication API password reset flow

Fixed PF-30558

When an OAuth client is performing a password reset through the authentication API, if PingFederate does not find any session attributes, now PingFederate logs an error state instead of a null pointer exception.

### Determining authentication instants for flows

Fixed PF-30770

Resolved an issue that prevented PingFederate from correctly determining the authentication instant for the flow when the initial OIDC authorization request specifies a max\_age, the flow falls through to legacy authentication source selection (policies are disabled or no policy applies), and the user chooses an upstream OIDC IdP connection.

### Templates for PingOne MFA 1.6.1

Fixed PF-30806 PingOne MFA

PingFederate now includes all the templates for PingOne MFA 1.6.1.

### Dependency errors for SAML token processors and generators

Fixed PF-31054

When saving SAML token processors or generators, PingFederate now correctly handles dependency errors caused by misconfigured settings on the **Protocol Settings** window's **Federation Info** tab.

### Preserving the order of map type configurations

Fixed PF-31145

Now PingFederate preserves the order of map type configurations under `<pf_install>/pingfederate/server/default/data/config-store` when performing a bulk export or a GET operation at the `/configStore` administrative API endpoint.

### Warning about using the administrative console in multiple tabs

Fixed PF-31280

Now if you use the PingFederate administrative console in multiple tabs on one browser, it warns you that doing so might cause inconsistent behavior which could corrupt its configuration.

### Saving authorization server settings overwrites scope.whitelist

Fixed PF-31304

Resolved an issue that caused PingFederate to overwrite the `scope.whitelist` in the `\data\config-store\org.sourceid.oauth20.domain.AuthzServerManagerImpl.xml` file when you save the authorization server settings.

### OAuth client IDs added to admin.log entries

Fixed PF-31561

Now OAuth client MODIFY, CREATE, and DELETE event log entries in the `admin.log` include the client ID.

### Honoring the property for maximum HTTP request body size

Fixed PF-31575

Now PingFederate honors the value of `http.maxRequestBodySize` in the `run.properties` file, which specifies the maximum HTTP request body size of any incoming request to PingFederate's web services and administrative API.

## Known issues and limitations

### Administrative console and administrative API

Issue

* /bulk: Only resource types currently supported by the administrative API are included in the exported data. We don't intend to introduce administrative API support to the following areas:

  * [SAML 2.0 IdP Discovery](../administrators_reference_guide/pf_configuring_standard_idp_discovery.html)

  * [SAML 2.0 SP Affiliation](../administrators_reference_guide/help_affiliationstasklet_affiliationmgmtstate.html)

  * [SMS Provider](../administrators_reference_guide/help_smsprovidersettingstasklet_smsprovidersettingsstate.html)

* Previously, the administrative API did not accurately reflect a **Persistent Grant Max Lifetime** setting of 29 days (or shorter) with the selection of the **Grants Do Not Timeout Due To Inactivity** option. As a result, if you have configured such OAuth authorization server settings and have generated a bulk export in version 10.0 through 10.0.2, we recommend that you re-generate a new bulk export after upgrading to version 10.0.3 (or a more recent version). The newly exported data does not contain the aforementioned flaw, and you can safely import it to version 10.0.3 (or a more recent version).

* When enabling mutual TLS certificate-based authentication, administrators often configure a list of acceptable client certificate issuers. When you use a browser to access the console or the administrative API documentation, PingFederate returns to the browser the list of acceptable issuers as part of the TLS handshake. If the browser's client certificate store contains multiple client certificates, the browser often presents you only the certificates whose issuer matches one of the acceptable issuers. However, when PingFederate runs in a Java 11 environment, Chrome presents you all its configured client certificates, regardless of whether the issuer matches one of the acceptable issuers or not.

* Prior to toggling the status of a connection with the administrative API, you must ensure that any expired certificates or no longer available attributes are replaced with valid certificates or attributes; otherwise, the update request fails.

* When creating or updating a child instance of a hierarchical plugin, the administrative API retains objects with an `"inherited": false` name/value pair (or without such name/value pair altogether), ignores those with a value of `true`, and returns a 200 HTTP status code. No error messages are returned for the ignored objects.

* Using the browser's navigation mechanisms (for example, the **Back** button) causes inconsistent behavior in the administrative console. Use the navigation buttons provided at the bottom of windows in the PingFederate console.

* Using the PingFederate console in multiple tabs on one browser might cause inconsistent behavior which could corrupt its configuration.

* If authenticated to the PingFederate administrative console using certificate authentication, a session that has timed out might not appear to behave as expected. Normally (when using password authentication), when a session has timed out and a user attempts some action in the console, the browser is redirected to the sign-on page, and then back to the administrative console after authentication is complete. Similar behavior applies for certificate authentication, in principle. However, because the browser might automatically resubmit the certificate for authentication, the browser might redirect to the administrative console and not the sign on page.

### TLSv1.3

Issue

For Java versions that don't support TLSv1.3 (meaning versions earlier than 8u261), PingFederate fails on start up with a `NoSuchAlgorithmException` exception. To resolve this error, remove `TLSv1.3` from the following settings in the `run.properties` file:

* `pf.tls.client.protocols`

* `pf.tls.runtime.server.protocols`

* `pf.tls.admin.server.protocols`

### TLS cipher suite customization

Issue

PingFederate's TLS cipher suites can be customized by modifying `com.pingidentity.crypto.SunJCEManager.xml` (or a similarly-named file if BCFIPS or a hardware security module (HSM) is configured). After updating the file and replicating, all cluster nodes must be restarted for the change to take effect.

### Java

Issue

* As of PingFederate 11.1, BC-FIPS and HSMs are not supported when using Java 17.

* Updating Java version 8 to version 11 results in an error when PingFederate is already installed and running. To work around this issue, uninstall and reinstall the PingFederate Windows service by running the `UninstallPingFederateService.bat` and `InstallPingFederateService.bat` files located in `<pf_install>/pingfederate/sbin/wrapper`.

### Hardware security modules (HSM)

Issue

* For Entrust HSMs, it is not possible to use an elliptic curve (EC) certificate as an SSL server certificate.

* For Entrust HSMs, PingFederate must be deployed with Oracle Server JRE 8 or Amazon Corretto 8.

* For keys stored in AWS CloudHSMs, JWT token signing fails when using RSASSA-PSS SHA-512.

* For keys stored in Thales HSMs, JWT token decryption fails when using RSAES OAEP with AES-CBC-192 or AES-CBC-256. This issue only arises if PingFederate is configured with static OAuth and OpenID Connect keys and is consuming a token encrypted with one of these keys.

* When PingFederate is configured in hybrid mode with a Thales HSM, it is not possible to export a locally-stored EC key pair.

* When PingFederate is configured in hybrid mode with a Thales HSM, JWT token decryption using ECDH-ES may fail. This issue only arises if PingFederate is configured with static OAuth and OpenID Connect keys, a static key is stored locally, and PingFederate is consuming a token encrypted with this key.

* TLS 1.3 is not currently supported with any HSM.

### SSO and SLO

Issue

* When consuming SAML metadata, PingFederate does not report an error when neither the `validUntil` nor the `cacheDuration` attribute is included in the metadata. Note that PingFederate does reject expired SAML metadata as indicated by the `validUntil` attribute value, if it is provided.

* The anchored-certificate trust model cannot be used with the Single log off (SLO) redirect binding because the certificate cannot be included with the logout request.

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

Ping Identity commits to deliver the best experience for administrators and users. As we continue to improve our products, we encourage you to migrate off of Microsoft Internet Explorer 11. Starting with PingFederate 11.0, Internet Explorer 11 is no longer included in the PingFederate qualification process for administrators or users. For a list of supported browsers, see [System requirements](../installing_and_uninstalling_pingfederate/pf_system_requirements.html).

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

---

---
title: PingFederate 11.1.1 (July 2022)
description: Fixed PF-29706 PingDirectory
component: pingfederate
version: 13.1
page_id: pingfederate:release_notes:pf_release_notes_1111
canonical_url: https://docs.pingidentity.com/pingfederate/13.1/release_notes/pf_release_notes_1111.html
llms_txt: https://docs.pingidentity.com/pingfederate/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 1, 2024
section_ids:
  resolved-issues: Resolved issues
  security-around-password-expiration: Security around password expiration
  issuance-criteria-in-authentication-policy-contracts: Issuance criteria in authentication policy contracts
  http-header-for-client-ip-addresses: HTTP header for client IP addresses
  error-descriptions: Error descriptions
  masterkeyencryptor-failure-during-cluster-replication: MasterKeyEncryptor failure during cluster replication
  updating-the-client-secret-with-the-oauth-client-management-service: Updating the client secret with the OAuth client management service
  oauth-authorization-requests-with-response_modepi-flow: OAuth authorization requests with response_mode=pi.flow
  administrative-api-enhancement: Administrative API enhancement
  message-customization-enhancement: Message customization enhancement
  cluster-management-enhancement: Cluster management enhancement
---

# PingFederate 11.1.1 (July 2022)

## Resolved issues

### Security around password expiration

Fixed PF-29706 PingDirectory

Improved the security around password expiration when using PingDirectory as a user store.

### Issuance criteria in authentication policy contracts

Fixed PF-31485

Issuance criteria in authentication policy contracts no longer cause the logs to indicate invalid XML errors. This issue did not cause runtime errors.

### **HTTP header for client IP addresses**

Fixed PF-31735

Resolved an issue that sometimes occurred when IPV6 addresses were specified in the **HTTP Header for Client IP Addresses** field on the **Incoming Proxy Settings** window.

### Error descriptions

Fixed PF-31753

PingFederate error descriptions no longer disclose details of java classes.

### MasterKeyEncryptor failure during cluster replication

Fixed PF-31795

When PingFederate is using a custom MasterKeyEncryptor that relies on an SSL call to an external service, cluster replication no longer causes cascading failures because PingFederate is unable to open Java key store files.

### Updating the client secret with the OAuth client management service

Fixed PF-31851

When updating the client secret with the OAuth client management service, PingFederate now correctly creates the secondary secrets.

### OAuth authorization requests with `response_mode=pi.flow`

Fixed PF-31942

Now when PingFederate receives an OAuth authorization request with `response_mode=pi.flow`, password change and account recovery flows using an authentication policy work correctly.

### Administrative API enhancement

Info

Improved the administrative API to manage the System for Cross-domain Identity Management (SCIM) inbound provisioning settings in identity provider (IdP) connections.

### Message customization enhancement

Info

Enhanced PingFederate message customization by adding the following FedHub-specific context variables:

* `FedHubSpConnApplicationName`

* `FedHubSpConnName`

* `FedHubOAuthClientId`

* `FedHubOAuthClientName`

### Cluster management enhancement

Info

Revised the **Cluster Management** window to make it more obvious when changes to the configuration on the administrative node have not been replicated to the engine nodes.

---

---
title: PingFederate 11.1.10 (April 2024)
description: Security PF-34720
component: pingfederate
version: 13.1
page_id: pingfederate:release_notes:pf_release_notes_11110
canonical_url: https://docs.pingidentity.com/pingfederate/13.1/release_notes/pf_release_notes_11110.html
llms_txt: https://docs.pingidentity.com/pingfederate/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 22, 2024
section_ids:
  resolved-issues: Resolved issues
  rest-datastore-security-vulnerability: Rest datastore security vulnerability
  runtime-nodes-security-vulnerability: Runtime nodes security vulnerability
  openid-connect-policy-management-editor-security-vulnerability: OpenID Connect policy management editor security vulnerability
  slow-log-consumption-affects-performance: Slow log consumption affects performance
---

# PingFederate 11.1.10 (April 2024)

## Resolved issues

### Rest datastore security vulnerability

Security PF-34720

Fixed a JSON injection vulnerability in REST datastores described in security advisory [SECADV044](https://support.pingidentity.com/s/article/SECADV044-PingFederate-Security-Rollup).

### Runtime nodes security vulnerability

Security PF-34896

Fixed a path traversal vulnerability in Runtime nodes described in security advisory [SECADV044](https://support.pingidentity.com/s/article/SECADV044-PingFederate-Security-Rollup).

### OpenID Connect policy management editor security vulnerability

Security PF-35081

Fixed a Cross-Site Scripting vulnerability in the OpenID Connect Policy Management Editor described in security advisory [SECADV044](https://support.pingidentity.com/s/article/SECADV044-PingFederate-Security-Rollup).

### Slow log consumption affects performance

Fixed PF-33368

Fixed a defect that caused performance issues for PingFederate when third-party logging services were slow to consume logging events.

---

---
title: PingFederate 11.1.11 (January 2025)
description: Fixed PF-33441
component: pingfederate
version: 13.1
page_id: pingfederate:release_notes:pf_release_notes_11111
canonical_url: https://docs.pingidentity.com/pingfederate/13.1/release_notes/pf_release_notes_11111.html
llms_txt: https://docs.pingidentity.com/pingfederate/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  resolved-issues: Resolved issues
  eliminating-redundant-group-updates: Eliminating redundant group updates
  provisioner-uses-the-wrong-time-zone-when-data-source-and-pingfederate-are-in-different-time-zones: Provisioner uses the wrong time zone when data source and PingFederate are in different time zones
  group-membership-loss-during-provisioning: Group membership loss during provisioning
---

# PingFederate 11.1.11 (January 2025)

## Resolved issues

### Eliminating redundant group updates

Fixed PF-33441

We've fixed a defect that caused PingFederate, when configured with PingDirectory as an outbound provisioning data source, to send redundant group updates in each provisioning cycle when the entry remains unchanged.

### Provisioner uses the wrong time zone when data source and PingFederate are in different time zones

Fixed PF-35286

We've fixed a defect that caused redundant user provisioner updates when the data source and PingFederate were in different time zones.

### Group membership loss during provisioning

Fixed PF-36874

We've fixed a defect that caused PingFederate to lose user group membership information when it lost contact with the data store during provisioning operations.

---

---
title: PingFederate 11.1.2 (October 2022)
description: Fixed PF-31870
component: pingfederate
version: 13.1
page_id: pingfederate:release_notes:pf_release_notes_1112
canonical_url: https://docs.pingidentity.com/pingfederate/13.1/release_notes/pf_release_notes_1112.html
llms_txt: https://docs.pingidentity.com/pingfederate/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 1, 2024
section_ids:
  resolved-issues: Resolved issues
  bulk-import-for-idp-connections: Bulk import for IdP connections
  connection-failures-on-external-ldap-authentication-login: Connection failures on external LDAP authentication login
  hiding-user-information-from-authentication-api-responses: Hiding user information from authentication API responses
  errors-on-policy-fragments-configured-to-handle-failures-locally: Errors on policy fragments configured to handle failures locally
  outbound-tls-connection-failures: Outbound TLS connection failures
  pingdirectory-user-registration: PingDirectory user registration
  configurations-with-no-connection-type-in-kerberos-realm: Configurations with no connection type in Kerberos realm
---

# PingFederate 11.1.2 (October 2022)

## Resolved issues

### Bulk import for IdP connections

Fixed PF-31870

Resolved an issue where bulk import fails for identity provider (IdP) connections that fulfill Persistent Grant Extended Attributes.

### Connection failures on external LDAP authentication login

Fixed PF-32001

PingFederate now recovers from initial connection failure when logging into the administrative console using external LDAP authentication.

### Hiding user information from authentication API responses

Fixed PF-32028

You can now configure the setting `IncludeUserInfoInResponses` in the `<install dir>/server/default/data/config-store/org.sourceid.saml20.domain.mgmt.impl.AuthnApiManagerImpl.xml` file to hide user information from authentication API responses.

### Errors on policy fragments configured to handle failures locally

Fixed PF-32073

When an error occurs on policies containing fragments and configured to handle failures locally, PingFederate no longer redirects a user to the service provider (SP) error page on SP-initiated single sign-on (SSO).

### Outbound TLS connection failures

Fixed PF-32199

The certificate path-building algorithm now uses PingFederate's custom revocation checker. This fix resolves a bug where outbound TLS connections failed for servers that presented out-of-order certificate chains.

### PingDirectory user registration

Fixed PF-32241

During user registration, PingFederate now sends all passwords to PingDirectory, resolving an issue where passwords consisting of only spaces would not properly register a PingDirectory password.

### Configurations with no connection type in Kerberos realm

Fixed PF-32274

When reading the `pingfederate-kerberos-realms.xml` file, PingFederate no longer raises an error for configurations with no connection type in the Kerberos realm.

---

---
title: PingFederate 11.1.3 (December 2022)
description: Fixed PF-32395
component: pingfederate
version: 13.1
page_id: pingfederate:release_notes:pf_release_notes_1113
canonical_url: https://docs.pingidentity.com/pingfederate/13.1/release_notes/pf_release_notes_1113.html
llms_txt: https://docs.pingidentity.com/pingfederate/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 1, 2024
section_ids:
  resolved-issues: Resolved issues
  improvements-to-custom-revocation-checker: Improvements to custom revocation checker
  cluster-replication-notifications: Cluster replication notifications
  null-pointer-exception-during-dependency-error-detection: Null pointer exception during dependency error detection
  pingfederate-updates-to-hsm-ordering: PingFederate updates to HSM ordering
---

# PingFederate 11.1.3 (December 2022)

## Resolved issues

### Improvements to custom revocation checker

Fixed PF-32395

We've improved PingFederate's custom revocation checker, ensuring that when the server returns stapled Online Certificate Status Protocol (OCSP) responses, PingFederate invokes the checker. Previously, PingFederate used the default revocation checker to validate these responses, which could cause single sign-on (SSO) failures with BCFIPS mode enabled. For more information, see [Configuring certificate revocation](../administrators_reference_guide/help_certificaterevocationcheckingtasklet_managecertificaterevocationstate.html).

### Cluster replication notifications

Fixed PF-32398

We've improved notifications to signal to administrators that in the event of a replication failure or any changes to cluster configuration require replication. For more information, see [Cluster management](../administrators_reference_guide/pf_cluster_management.html).

### Null pointer exception during dependency error detection

Fixed PF-32553

During PingFederate dependency error detection, OGNL expressions in adapter-to-adapter mappings no longer raise a null pointer exception (NPE).

### PingFederate updates to HSM ordering

Fixed PF-32556

We've updated the recommended security provider ordering for the Thales Luna Network hardware security module (HSM) to address an issue where temporary keys and sessions could accumulate on the HSM, eventually resulting in resource exhaustion. A limitation of the new ordering is that EC certificates can no longer operate as SSL server certificates. For details on the new order, see [Integrating with Thales Luna Network HSM](../getting_started_with_pingfederate/pf_integrating_thales_luna_network_hsm.html).

---

---
title: PingFederate 11.1.4 (February 2023)
description: Fixed PF-32790
component: pingfederate
version: 13.1
page_id: pingfederate:release_notes:pf_release_notes_1114
canonical_url: https://docs.pingidentity.com/pingfederate/13.1/release_notes/pf_release_notes_1114.html
llms_txt: https://docs.pingidentity.com/pingfederate/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 22, 2024
section_ids:
  resolved-issues: Resolved issues
  oauth-client-management: OAuth client management
  potential-security-vulnerability: Potential security vulnerability
  informing-adapters-of-end-policy-result: Informing adapters of end policy result
  managing-certificates-within-metadata-export: Managing certificates within Metadata Export
  cluster-data-replication: Cluster data replication
---

# PingFederate 11.1.4 (February 2023)

## Resolved issues

### OAuth client management

Fixed PF-32790

When managing OAuth clients, we've resolved a defect where selecting the **Require JWT Secured Authorization Response Mode** text toggled the incorrect checkbox.

### Potential security vulnerability

Fixed PF-32805

We've resolved a potential security vulnerability that is described in security advisory [SECADV033](https://support.pingidentity.com/s/article/SECADV033-Cross-Site-Request-Forgery-on-PingFederate-Local-Identity-Profiles-Endpoint).

### Informing adapters of end policy result

Fixed PF-32890

When processing policy fragments, all adapters invoked in the fragment now correctly execute their respective post-processing step (if applicable) to inform the adapter of the end policy result.

### Managing certificates within Metadata Export

Fixed PF-32965

Managing certificates within the **Metadata Export** flow no longer displays or saves an empty list of certificates, clearing out existing ones in the process. For more information, see [Metadata export](../administrators_reference_guide/pf_metadata_export.html).

### Cluster data replication

Fixed PF-32983

We've resolved a defect where cluster data replication could remove keys from engine node's `pf.jwk` file instead of merging and retaining the keys.

---

---
title: PingFederate 11.1.5 (February 2023)
description: Fixed PF-33037
component: pingfederate
version: 13.1
page_id: pingfederate:release_notes:pf_release_notes_1115
canonical_url: https://docs.pingidentity.com/pingfederate/13.1/release_notes/pf_release_notes_1115.html
llms_txt: https://docs.pingidentity.com/pingfederate/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 22, 2024
section_ids:
  resolved-issues: Resolved issues
  server-log-warnings: Server log warnings
---

# PingFederate 11.1.5 (February 2023)

## Resolved issues

### Server log warnings

Fixed PF-33037

We've added a warning to server logs if the *ds-pwp-state-json* attribute is not present in PingDirectory's LDAP Response. This warning appears in the log every time a user interacts with the profile management page. Please enable this attribute to adhere to PingDirectory's security configuration best practices. PingDirectory version 8.1 and later supports this attribute, and customers running older versions are encouraged to upgrade to a supported version as soon as possible.

---

---
title: PingFederate 11.1.6 (February 2023)
description: Fixed PF-33017
component: pingfederate
version: 13.1
page_id: pingfederate:release_notes:pf_release_notes_1116
canonical_url: https://docs.pingidentity.com/pingfederate/13.1/release_notes/pf_release_notes_1116.html
llms_txt: https://docs.pingidentity.com/pingfederate/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 22, 2024
section_ids:
  resolved-issues: Resolved issues
  log-improvements: Log improvements
  other-improvements: Other improvements
---

# PingFederate 11.1.6 (February 2023)

## Resolved issues

### Log improvements

Fixed PF-33017

In order to reduce re-encryption and file scanning log verbosity, when a configuration is imported or replicated to a cluster, PingFederate no longer scans files in the `etc` directory.

### Other improvements

Info

* We also updated the following bundled components and third-party dependencies:

  * PingID Integration Kit 2.24

  * PingID Adapter 2.13.2

  * PingID PCV (with integrated RADIUS server) 3.0.3