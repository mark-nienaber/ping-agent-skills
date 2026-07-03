---
title: Authentication methods
description: The Consent Service supports the following HTTP authentication methods and the use of token validators for authorization.
component: pingdirectory
version: 11.1
page_id: pingdirectory:consent_solution_guide:pd_cs_authn_methods
canonical_url: https://docs.pingidentity.com/pingdirectory/11.1/consent_solution_guide/pd_cs_authn_methods.html
llms_txt: https://docs.pingidentity.com/pingdirectory/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: September 13, 2023
section_ids:
  supported-http-authentication-methods: Supported HTTP authentication methods
  configuring-token-validators: Configuring token validators
---

# Authentication methods

The Consent Service supports the following HTTP authentication methods and the use of token validators for authorization.

## Supported HTTP authentication methods

The Consent Service supports the following HTTP authentication methods that are enabled by default:

* Basic authentication

  With basic authentication, the client provides an encoded username-password pair in the HTTP Authorization request header. When the Consent Service receives a request using basic authentication, it maps the username credential to a distinguished name (DN) using an identity mapper. This DN is designated the `auth DN` and is used to make subsequent authorization decisions. The Consent Service then performs an Lightweight Directory Access Protocol (LDAP) *(tooltip: \<div class="paragraph">
  \<p>An open, cross platform protocol used for interacting with directory services.\</p>
  \</div>)* bind using the DN and password to determine if the request can be processed.

* Bearer token authentication

  With bearer token authentication, the client provides an access token *(tooltip: \<div class="paragraph">
  \<p>A data object by which a client authenticates to a resource server and lays claim to authorizations for accessing particular resources.\</p>
  \</div>)* in the HTTP Authorization request header. The access token is always obtained by the client from an external OAuth 2 authorization server and encapsulates information "claims" about a user identity, the client identity, and the requests that the client is authorized to make.

The Consent servlet looks at the request's Authorization header to determine which authentication type is being used by the client.

## Configuring token validators

The PingDirectory server must be configured to accept access tokens using one or both of the following access token validators:

* PingFederate access token validator

  Supports access tokens issued by a PingFederate authorization server. This validator verifies an access token and discovers its claims by making a request to the PingFederate server's token introspection endpoint.

|   |                                                                                                                                                                                                                                                                                                                                                                                                                         |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | If you are using PingFederate 10.0 or earlier, ensure that PingFederate is configured to respond to OAuth and OpenID Connect (OIDC) requests by selecting the checkboxes mentioned in steps 2 and 3 in [Enabling the OAuth AS role](https://cdn-docs.pingidentity.com/archive/pdf/pingfederate/pingfederate-100.pdf) in the PingFederate documentation.Starting with PingFederate 10.1, these items are always enabled. |

* JWT access token validator

  Supports signed or encrypted JSON Web Token (JWT) *(tooltip: \<div class="paragraph">
  \<p>An IETF standard container format for a JSON object used for the secure exchange of content, such as identity or entitlement information. You can find the industry standard in \<a href="https\://datatracker.ietf.org/doc/html/rfc7519">RFC 7519\</a>.\</p>
  \</div>)* access tokens issued by an arbitrary authorization server. This validator checks an access token by cryptographically verifying the token's signature using a trusted public certificate. The token's claims are encoded in the token itself, so discovering the token's claims does not require an outgoing token introspection request.

The token validator uses its identity mapper to map the subject claim to a DN. This DN is designated the `auth DN` and is used along with the token's claims to make subsequent authorization decisions.

If the PingDirectory server is configured with at least one access token validator, the Consent Service uses this access token validator. If the PingDirectory server is configured with more than one access token validator, the validators are consulted in order until one is able to successfully authenticate the request. If the PingDirectory server is configured with multiple access token validators, but only one should be used by the Consent Service, the access token validator can be configured by setting the `access-token-validator` property of the Consent HTTP Servlet Extension.

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | Configuring an access token validator for the Consent Service requires the following from the authorization server configuration:- The values that the authorization server sets for `subject` claims must be mappable to a DN in the PingDirectory server.

- The authorization server must be configured to authorize clients and grant scopes appropriately for privileged or unprivileged Consent API access.

- The authorization server must be configured to issue tokens with scopes corresponding to the Consent Service's `unprivileged-scope-name` and `privileged-scope-name` configuration.See the authorization server's documentation for guidance. |

---

---
title: Authorization
description: The Consent Service's distinction between privileged and unprivileged requesters determines the type of operations that can be performed by requesters.
component: pingdirectory
version: 11.1
page_id: pingdirectory:consent_solution_guide:pd_cs_authorization
canonical_url: https://docs.pingidentity.com/pingdirectory/11.1/consent_solution_guide/pd_cs_authorization.html
llms_txt: https://docs.pingidentity.com/pingdirectory/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: September 13, 2023
section_ids:
  bearer-token-check: Bearer token check
  basic-authentication-check: Basic authentication check
---

# Authorization

The Consent Service's distinction between `privileged` and `unprivileged` requesters determines the type of operations that can be performed by requesters.

During the authorization phase, the Consent servlet performs checks on both the bearer token claims, if present, and the `auth DN` to determine if the requester is privileged or unprivileged. These are summarized in the following table.

**Available operations per requester type**

| Requester type | Description                                                                      | Access determined by                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | Can create consent records                                                             | Can update consent records                       | Can delete consent records |
| -------------- | -------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | ------------------------------------------------ | -------------------------- |
| `Unprivileged` | Requesters with no authority to operate on consent records other than their own. | A requester is considered `unprivileged` if it does not meet any of the criteria for a `privileged` requester.If using bearer token authentication, the access token *(tooltip: \<div class="paragraph">&#xA;\<p>A data object by which a client authenticates to a resource server and lays claim to authorizations for accessing particular resources.\</p>&#xA;\</div>)* must include a scope named by the `unprivileged-consent-scope` property of the Consent Service configuration. Also, an unprivileged requester can only perform actions on consent records where the subject distinguished name (DN) matches the requester DN. | Yes.The subject/subjectDN and actor/actorDN values will be set based on the requester. | Yes, if the requester DN matches the subject DN. | No                         |
| `Privileged`   | A requester with the authority to perform any operation on any consent record.   | When using basic authentication, a requester is considered `privileged` if the requester DN either has the `bypass-acl` privilege or is listed in the `service-account-dn` property of the Consent Service configuration.If using bearer token authentication, the access token must include a scope named by the `privileged-consent-scope` property of the Consent Service configuration.                                                                                                                                                                                                                                               | Yes                                                                                    | Yes                                              | Yes                        |

## Bearer token check

If a bearer token was used, the following checks are performed:

* If the Consent Service's `audience` property is configured, the bearer token's audience claim must match the configured value.

* If the bearer token contains a scope matching the Consent Service's `privileged-scope-name` property, then the requester is considered privileged.

* If the bearer token doesn't contain a scope matching the Consent Service's `privileged-scope-name` property, the bearer token must have a scope matching the Consent Service's `unprivileged-scope-name` property, and the requester is considered unprivileged.

## Basic authentication check

If basic authentication is used, the following checks are performed:

* If the `auth DN` has the Lightweight Directory Access Protocol (LDAP) *(tooltip: \<div class="paragraph">
  \<p>An open, cross platform protocol used for interacting with directory services.\</p>
  \</div>)* privilege `bypass-acl`, the requester is `privileged`.

* If the `auth DN` is listed in the Consent Service's `service-account-dn` property, the requester is `privileged`.

* If the `auth DN` isn't listed in the Consent Service's `service-account-dn` property, the requester is considered `unprivileged`.

---

---
title: Configuration overview
description: Your Consent Service configuration can vary depending on client application capabilities, authentication methods used, and other factors.
component: pingdirectory
version: 11.1
page_id: pingdirectory:consent_solution_guide:pd_cs_config_overview
canonical_url: https://docs.pingidentity.com/pingdirectory/11.1/consent_solution_guide/pd_cs_config_overview.html
llms_txt: https://docs.pingidentity.com/pingdirectory/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: September 13, 2023
---

# Configuration overview

Your Consent Service configuration can vary depending on client application capabilities, authentication methods used, and other factors.

By default, the Consent Service is not enabled. The setup and configuration process varies depending on the following factors:

* Whether client applications allow an individual to self-manage consents

* Whether some or all client applications can be privileged with the ability to manage all consents

* The HTTP authentication method used by client applications

* Whether consent records exist in the same directory as user entries

---

---
title: Configuration reference
description: Use this section as a reference for information about the Consent Service properties and configuration.
component: pingdirectory
version: 11.1
page_id: pingdirectory:consent_solution_guide:pd_cs_config_reference
canonical_url: https://docs.pingidentity.com/pingdirectory/11.1/consent_solution_guide/pd_cs_config_reference.html
llms_txt: https://docs.pingidentity.com/pingdirectory/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: September 13, 2023
---

# Configuration reference

Use this section as a reference for information about the Consent Service properties and configuration.

There are many configuration options for the Consent Service and application integration. The configuration scripts included with PingDirectory server provide a starting point. Additional information about the Consent Service properties and configuration is provided as reference.

---

---
title: Configuring an identity mapper
description: The Consent Service uses identity mappers to map requester identities, subject values, and actor values to distinguished names (DNs).
component: pingdirectory
version: 11.1
page_id: pingdirectory:consent_solution_guide:pd_cs_config_identity_mapper
canonical_url: https://docs.pingidentity.com/pingdirectory/11.1/consent_solution_guide/pd_cs_config_identity_mapper.html
llms_txt: https://docs.pingidentity.com/pingdirectory/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: September 13, 2023
section_ids:
  the-consent-record-identity-mapper: The consent record identity mapper
  identity-mapper-configuration-options: Identity mapper configuration options
---

# Configuring an identity mapper

The Consent Service uses identity mappers to map requester identities, subject values, and actor values to distinguished names (DNs).

An identity mapper takes a user identifier string and correlates the identifier with the DN of a user entry. The PingDirectory server provides four different types of identity mappers.

**Identity mapper types and descriptions**

| Identity mapper type               | Description                                                                                                            |
| ---------------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| Exact match identity mapper        | Maps a user identifier to a DN by searching for an entry with an attribute that exactly matches the identifier.        |
| Regular expression identity mapper | Similar to an exact match identity mapper, but allows a regular expression to be specified for more flexible matching. |
| Third-party identity mapper        | A custom Java identity mapper implementation written using the Server SDK.                                             |
| Groovy scripted identity mapper    | A custom Groovy identity mapper implementation written using the Server SDK.                                           |

The Consent Service can be configured to use identity mappers for each of the following scenarios:

* Requesters authenticating using basic authentication

  Use the Consent HTTP Servlet Extension `identity-mapper` property to configure an identity mapper that takes the HTTP Basic authorization username string to find the corresponding user's identity in the PingDirectory server.

* Requesters authenticating using bearer token authentication

  Use the Access Token Validator `identity-mapper` property to configure an identity mapper that takes the subject or other claim value from the OAuth token to find the corresponding user's identity in the PingDirectory server.

* Consent record actor and subject values

  Use the Consent Service `consent-record-identity-mapper` property to configure an identity mapper that takes these consent record attribute values and uses them to find the corresponding users' identities in the PingDirectory server.

## The consent record identity mapper

By default, the Consent Service sets the `subject`, `subjectDN`, `actor`, and `actorDN` values to the identity of the authenticated requester. If the requester uses basic authentication, then all values are set to the auth DN determined by the basic authentication identity mapper. If the requester uses bearer token authentication, then the `subject` and `actor` values are set to the bearer token's subject claim value, while the `subjectDN` and `actorDN` values are set to the auth DN determined by the access token *(tooltip: \<div class="paragraph">
\<p>A data object by which a client authenticates to a resource server and lays claim to authorizations for accessing particular resources.\</p>
\</div>)* validator identity mapper.

Privileged clients can manually set a consent record's `subject` and `actor` values. In those cases, the Consent Service's `consent-record-identity-mapper` property is used to map a consent record's `subject` and `actor` values to `subjectDN` and `actorDN` values, respectively.

## Identity mapper configuration options

The Consent Service configuration script configures a single identity mapper to be used for all three scenarios. The provided identity mapper searches by `uid`, `cn`, or `entryUUID` attributes under the base DNs `cn=config and ou=people,dc=example,dc=com`.

The following configuration provides an example of an identity mapper that matches a user identifier to an Lightweight Directory Access Protocol (LDAP) *(tooltip: \<div class="paragraph">
\<p>An open, cross platform protocol used for interacting with directory services.\</p>
\</div>)* entry with the same value in its `uid` attribute.

```shell
$ bin/dsconfig create-identity-mapper --mapper-name "User ID Exact Match" \
  --type exact-match \
  --set enabled:true \
  --set match-attribute:uid
```

This configuration shows another typical example: an identity mapper that matches a user identifier to an LDAP entry with the same value in its `entryUUID` attribute.

```shell
$ bin/dsconfig create-identity-mapper --mapper-name "EntryUUID Exact Match" \
  --type exact-match \
  --set enabled:true \
  --set match-attribute:entryUUID
```

This final example creates an identity mapper that matches a user identifier to an LDAP entry with the same value in either its `uid`, `cn`, or `entryUUID` attribute. This identity mapper also constrains its search to the `cn=config and ou=people,dc=example,dc=com` and `cn=config` base DNs. By default, the `cn=config` base DN is not searched and must be explicitly listed to be searched.

```shell
$ bin/dsconfig create-identity-mapper \
  --mapper-name "User ID Identity Mapper" \
  --type exact-match \
  --set enabled:true \
  --set match-attribute:uid \
  --set match-attribute:cn \
  --set match-attribute:entryUUID \
  --set match-base-dn:cn=config \
  --set match-base-dn:ou=people,dc=example,dc=com
```

---

---
title: Configuring basic authentication
description: Disable or enable basic authentication and configure an identity mapper for basic authentication.
component: pingdirectory
version: 11.1
page_id: pingdirectory:consent_solution_guide:pd_cs_config_basic_authn
canonical_url: https://docs.pingidentity.com/pingdirectory/11.1/consent_solution_guide/pd_cs_config_basic_authn.html
llms_txt: https://docs.pingidentity.com/pingdirectory/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: September 13, 2023
section_ids:
  about-this-task: About this task
  steps: Steps
  example: Example:
  example-2: Example:
  example-3: Example:
  example-4: Example:
---

# Configuring basic authentication

Disable or enable basic authentication and configure an identity mapper for basic authentication.

## About this task

By default, basic authentication is enabled. The settings are configured in the Consent HTTP Servlet Extension configuration.

|   |                                                                                                                                           |
| - | ----------------------------------------------------------------------------------------------------------------------------------------- |
|   | All of these configuration changes require the Consent servlet to be reloaded before they can take effect. To do this, see the last step. |

## Steps

* To disable basic authentication, use the following command.

  ### Example:

  ```shell
  $ bin/dsconfig set-http-servlet-extension-prop \
    --extension-name Consent \
    --set basic-auth-enabled:false
  ```

* To enable basic authentication, use the following command.

  ### Example:

  ```shell
  $ bin/dsconfig set-http-servlet-extension-prop \
    --extension-name Consent \
    --set basic-auth-enabled:true
  ```

* To configure an identity mapper for basic authentication, use the following command.

  ### Example:

  ```shell
  $ bin/dsconfig set-http-servlet-extension-prop \
    --extension-name Consent \
    --set "identity-mapper:User ID Exact Match"
  ```

* To restart the connection handler that hosts the Consent servlet, use the following commands.

  ### Example:

  ```shell
  $ bin/dsconfig set-connection-handler-prop \
    --handler-name "HTTPS Connection Handler" \
    --set enabled:false
  ```

  ```shell
  $ bin/dsconfig set-connection-handler-prop \
    --handler-name "HTTPS Connection Handler" \
    --set enabled:true
  ```

---

---
title: Configuring bearer token authentication
description: Configure an access token validator.
component: pingdirectory
version: 11.1
page_id: pingdirectory:consent_solution_guide:pd_cs_config_bearer_token_authn
canonical_url: https://docs.pingidentity.com/pingdirectory/11.1/consent_solution_guide/pd_cs_config_bearer_token_authn.html
llms_txt: https://docs.pingidentity.com/pingdirectory/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: September 13, 2023
section_ids:
  about-this-task: About this task
  steps: Steps
  example: Example:
  example-2: Example:
---

# Configuring bearer token authentication

Configure an access token validator.

## About this task

|   |                                                                  |
| - | ---------------------------------------------------------------- |
|   | You can configure the Consent Service to use a single validator. |

## Steps

* Configure an access token validator using `dsconfig`.

  ### Example:

  This example shows an access token validator configured on a PingDirectory server for a PingFederate server.

  ```shell
  $ bin/dsconfig create-external-server \
    --server-name PingFederate \
    --type http \
    --set base-url:https://my-ping-federate-server:1443/
  ```

  ```shell
  $ bin/dsconfig create-access-token-validator \
    --validator-name "PingFederate Token Validator" \
    --type ping-federate \
    --set enabled:true \
    --set "identity-mapper:User ID Exact Match" \
    --set authorization-server:PingFederate \
    --set client-id:id \
    --set client-secret:secret
  ```

* (Optional) If more than one access token validator is configured on a PingDirectory server, you can configure the Consent Service to use a single validator with the following command.

  ### Example:

  ```shell
  $ bin/dsconfig set-http-servlet-extension-prop \
    --extension-name Consent \
    --set "access-token-validator:PingFederate Token Validator"
  ```

---

---
title: Configuring Consent Service scopes
description: Configure the privileged-consent-scope and unprivileged-consent-scope for the Consent Service.
component: pingdirectory
version: 11.1
page_id: pingdirectory:consent_solution_guide:pd_cs_config_consent_service_scopes
canonical_url: https://docs.pingidentity.com/pingdirectory/11.1/consent_solution_guide/pd_cs_config_consent_service_scopes.html
llms_txt: https://docs.pingidentity.com/pingdirectory/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: September 13, 2023
section_ids:
  about-this-task: About this task
  steps: Steps
  example: Example:
---

# Configuring Consent Service scopes

Configure the` privileged-consent-scope` and `unprivileged-consent-scope` for the Consent Service.

## About this task

The Consent Service checks access tokens for a `subject` claim and uses an identity mapper to map the value to a distinguished name (DN), called the request DN or auth DN. If no request DN can be mapped, the request is rejected.

The Consent Service only accepts an access token with a scope that it is configured to recognize.

* `unprivileged-consent-scope`

  An unprivileged consent scope designates the requester as unprivileged. The scope's name is configured with the Consent Service's `unprivileged-consent-scope` property.

* `privileged-consent-scope`

  A privileged consent scope designates the requester as privileged. This is configured using the Consent Service's `privileged-consent-scope` property.

|   |                                                                                     |
| - | ----------------------------------------------------------------------------------- |
|   | The authorization server must also be configured to issue tokens with these scopes. |

## Steps

* Configure the` privileged-consent-scope` and `unprivileged-consent-scope` for the Consent Service.

  ### Example:

  ```shell
  $ bin/dsconfig set-consent-service-prop \
    --set unprivileged-consent-scope:consent \
    --set privileged-consent-scope:consent_admin
  ```

---

---
title: Configuring the Consent Service
description: This section provides information for installing and configuring the components to support the Consent Service.
component: pingdirectory
version: 11.1
page_id: pingdirectory:consent_solution_guide:pd_cs_config_consent_service
canonical_url: https://docs.pingidentity.com/pingdirectory/11.1/consent_solution_guide/pd_cs_config_consent_service.html
llms_txt: https://docs.pingidentity.com/pingdirectory/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: September 13, 2023
---

# Configuring the Consent Service

This section provides information for installing and configuring the components to support the Consent Service.

Installing and configuring the Consent Service includes the following topics:

* [Configuration overview](pd_cs_config_overview.html)

* [Example configuration scenarios](pd_cs_config_scenarios.html)

* [Setting up with the configuration scripts](pd_cs_set_up_with_config_scripts.html)

* [Setting up in a replicated PingDirectory server environment](pd_cs_set_up_replicated_ds_env.html)

* [Configuration reference](pd_cs_config_reference.html)

* [Authorization](pd_cs_authorization.html)

For more configuration information, see [PingDataSync Server Administration Guide](../pingdatasync_server_administration_guide/pd_sync_intro_pds.html).

---

---
title: Consent API overview
description: PingDirectory and PingDirectoryProxy provide a REST application programming interface (API) for managing an individual's consent to handle their data.
component: pingdirectory
version: 11.1
page_id: pingdirectory:consent_solution_guide:pd_cs_consent_api_overview
canonical_url: https://docs.pingidentity.com/pingdirectory/11.1/consent_solution_guide/pd_cs_consent_api_overview.html
llms_txt: https://docs.pingidentity.com/pingdirectory/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: September 13, 2023
---

# Consent API overview

PingDirectory and PingDirectoryProxy provide a REST application programming interface (API) *(tooltip: \<div class="paragraph">
\<p>A specification of interactions available for building software to access an application or service.\</p>
\</div>)* for managing an individual's consent to handle their data.

The PingDirectory Consent API enables the following authorization services for managing an individual's consent and data:

* Captures a user's consent for sharing or processing data

* Confirms a user's consent to share or process data has been granted

* The user can manage the consent that they have granted

The Consent REST API can be used as a component of a larger solution, such as a General Data Protection Regulation (GDPR) compliance system.

Learn more in the [PingDirectory Consent API Reference](https://developer.pingidentity.com/pingdirectory/consent/introduction.html) and [How applications use the Consent API](pd_cs_how_apps_use_consent_api.html).

---

---
title: Consent definitions and localizations
description: The Consent Service requires consent definitions and localizations, which collect and share a use's data and define the purpose for collecting and sharing this data.
component: pingdirectory
version: 11.1
page_id: pingdirectory:consent_solution_guide:pd_cs_consent_defs_localization
canonical_url: https://docs.pingidentity.com/pingdirectory/11.1/consent_solution_guide/pd_cs_consent_defs_localization.html
llms_txt: https://docs.pingidentity.com/pingdirectory/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: September 13, 2023
---

# Consent definitions and localizations

The Consent Service requires consent definitions and localizations, which collect and share a use's data and define the purpose for collecting and sharing this data.

Companies can centrally manage the language used when prompting a user to give consent to ensure a consistent user experience across multiple applications, such as mobile and web.

The Consent Service requires one or more consent definitions to be defined in the PingDirectory server configuration. Each consent definition represents the combination of:

* The data to be collected or shared

* The purpose for collecting or sharing the data

For example, a consent definition could represent users' email addresses that are used to deliver a third party's email newsletter. A consent definition could also represent access to a user's network-connected IoT device that could be used for a home automation task controlled by a third party.

Each consent definition must have one or more localizations. A localization is a versioned object consisting of the data that a Consent API client needs to prompt a user for consent. When a consent record is accepted or denied by a Consent Service client, it must include a reference to a consent definition, locale, and version.

---

---
title: Consent Service overview
description: The Consent Service is an HTTP-based REST API hosted by the PingDirectory server or by the PingDirectoryProxy server.
component: pingdirectory
version: 11.1
page_id: pingdirectory:consent_solution_guide:pd_cs_consent_service_overview
canonical_url: https://docs.pingidentity.com/pingdirectory/11.1/consent_solution_guide/pd_cs_consent_service_overview.html
llms_txt: https://docs.pingidentity.com/pingdirectory/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: September 13, 2023
---

# Consent Service overview

The Consent Service is an HTTP-based REST API hosted by the PingDirectory server or by the PingDirectoryProxy server.

Enterprises can integrate the following Consent Service features into their applications to give users transparency and control of their data privacy:

* The collection of consent from application users

* The enforcement of consent

* A user's management of his or her consent

* Auditing of consent actions

The following terms are used throughout this guide:

* Collaborators

  A list of individuals for whom access to this consent record is shared.

* Consent definition

  The terms of the fine-grained contract, which describes the data that can be processed or shared, and a purpose for processing or sharing the data. The consent definition is stored in the server configuration.

* Consent localization

  A child object of a definition that contains versioned, localized text for the consent definition, to be used when prompting an individual. This is stored in the server configuration.

* Consent record

  A record of a consent interaction with a user. Consent records are stored in the directory tree.

* Subject

  The individual whose data can be collected, processed, or shared.

* Actor

  The individual who granted, denied, or revoked consent. This is usually the same as the subject.

* Audience

  The entity, application, or service that is granted or denied access to a subject's data for a specific purpose.

---

---
title: Correlating user and consent data
description: An organization that has been granted consent by a group of users can perform an LDAP search so that they can use the consent data in the aggregate.
component: pingdirectory
version: 11.1
page_id: pingdirectory:consent_solution_guide:pd_cs_correlate_user_consent_data
canonical_url: https://docs.pingidentity.com/pingdirectory/11.1/consent_solution_guide/pd_cs_correlate_user_consent_data.html
llms_txt: https://docs.pingidentity.com/pingdirectory/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: September 13, 2023
section_ids:
  about-this-task: About this task
  steps: Steps
  example: Example:
  result: Result:
---

# Correlating user and consent data

An organization that has been granted consent by a group of users can perform an LDAP search so that they can use the consent data in the aggregate.

## About this task

For this task, consider the example scenario where a marketing group has collected consent to send a newsletter by email. To find all the users that have granted consent to receive emails, the marketing group performs a search that lists all of the consent records where the consent definition is `email` and the status is `accepted`. Then, the marketing group must correlate these consent records to user entries and retrieve each user's email address.

Every consent record contains a `subject` field, the user whose data is collected and stored. You can configure the Consent Service so that it stores the subject's distinguished name (DN) in the `subjectDN` field.

## Steps

* Perform a search using the `ldapsearch` command.

  ### Example:

  |   |                                                                                                                                                                                                                                                                                                                                                                                                                     |
  | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | The example includes the following modifications in the `ldapsearch` command:- To correlate the consent record entries to user entries and retrieve each user entry's `mail` attribute value, `ping-consent-subject-dn` is used.

  - To find all of the relevant consent record entries, the LDAP search specifies values where `ping-consent-definition.id` is `email` and the `ping-consent-status` is `accepted`. |

  ```shell
  $ bin/ldapsearch \
     --baseDN "ou=consents,dc=example,dc=com" \
     --searchScope sub \
     --joinRule "dn:ping-consent-subject-dn" \
     --joinBaseDN "ou=people,dc=example,dc=com" \
     --joinScope sub \
     --joinRequestedAttribute mail
     '&(ping-consent-definition:jsonObjectFilterExtensibleMatch:={ "filterType" : "equals", "field" : "id", "value" : "email" })(ping-consent-state=accepted)' \
     1.1
  ```

  * A consent record's `subjectDN` field is the `ping-consent-subject-dn` attribute.

  * A consent record's status is in the `ping-consent-state` JSON attribute field.

  * A consent record's definition ID is in the `ping-consent-definition.id` JSON attribute field.

  * A user entry's email address is in the `mail` attribute.

    ### Result:

    The example LDAP search returns the following results.

    ```
    # Join Result Control:
       #      OID:  1.3.6.1.4.1.30221.2.5.9
       #      Join Result Code:  0 (success)
       #      Joined With Entry:
       #           dn: uid=user.0,ou=People,dc=example,dc=com
       #           mail: user.0@example.com
       dn: entryUUID=9e481010-8330-425a-bbf1-6637de053d48,ou=Consents,dc=example,dc=com

       # Result Code:  0 (success)
       # Number of Entries Returned:  1
    ```

    |   |                                                               |
    | - | ------------------------------------------------------------- |
    |   | The `Join Result Control:` output specifies the `mail` value. |

---

---
title: Creating a consent definition and localization
description: Create and update a consent definition and localization.
component: pingdirectory
version: 11.1
page_id: pingdirectory:consent_solution_guide:pd_cs_create_consent_def_localization
canonical_url: https://docs.pingidentity.com/pingdirectory/11.1/consent_solution_guide/pd_cs_create_consent_def_localization.html
llms_txt: https://docs.pingidentity.com/pingdirectory/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: September 13, 2023
section_ids:
  steps: Steps
  example: Example:
  example-2: Example:
  example-3: Example:
---

# Creating a consent definition and localization

Create and update a consent definition and localization.

## Steps

* Create a consent definition using `dsconfig create-consent-definition`.

  ### Example:

  ```shell
  $ bin/dsconfig create-consent-definition \
    --definition-name email_newsletter \
    --set "display-name:Email newsletter"
  ```

* Create a localization for the consent definition using `dsconfig create-consent-definition-localization`.

  ### Example:

  ```shell
  $ bin/dsconfig create-consent-definition-localization \
    --definition-name email_newsletter \
    --localization-name en-US \
    --set version:1.0 \
    --set "data-text:Your email address" \
    --set "purpose-text:To receive newsletter updates"
  ```

* Update a localization and the version using `dsconfig set-consent-definition-localization-prop` and `set version`.

  ### Example:

  The following example updates a localization and its version.

  ```shell
  $ bin/dsconfig set-consent-definition-localization-prop \
    --definition-name email_newsletter \
    --localization-name en-US \
    --set version:1.1 \
    --set "data-text:Your preferred email address"
  ```

---

---
title: Creating a container entry for consent records
description: Each consent record is a distinct entry in the PingDirectory server. The Consent Service requires that these entries are stored under a common base distinguished name (DN).
component: pingdirectory
version: 11.1
page_id: pingdirectory:consent_solution_guide:pd_cs_create_container_entry_consent_records
canonical_url: https://docs.pingidentity.com/pingdirectory/11.1/consent_solution_guide/pd_cs_create_container_entry_consent_records.html
llms_txt: https://docs.pingidentity.com/pingdirectory/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: September 13, 2023
section_ids:
  about-this-task: About this task
  steps: Steps
  example: Example:
  example-2: Example:
---

# Creating a container entry for consent records

Each consent record is a distinct entry in the PingDirectory server. The Consent Service requires that these entries are stored under a common base distinguished name (DN).

## About this task

The `base-dn` property of the Consent Service configuration defines the base DN. The Consent Service LDIF file sets the base DN.

To choose a different location to store consent records:

## Steps

1. To create the Consent Service base DN, open a text editor and save the following to the `consent-service-base-dn.ldif` file.

   ### Example:

   ```
   dn: ou=consents,dc=example,dc=com
   objectClass: top
   objectClass: organizationalUnit
   ou: consents
   ```

2. Use `ldapmodify` to add the entry.

   ### Example:

   ```shell
   $ bin/ldapmodify --defaultAdd --filename consent-service-base-dn.ldif
   ```

---

---
title: Creating an internal service account
description: Create an internal LDAP connection to operate against consent records that are stored as LDAP entries.
component: pingdirectory
version: 11.1
page_id: pingdirectory:consent_solution_guide:pd_cs_create_internal_service_acct
canonical_url: https://docs.pingidentity.com/pingdirectory/11.1/consent_solution_guide/pd_cs_create_internal_service_acct.html
llms_txt: https://docs.pingidentity.com/pingdirectory/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: September 13, 2023
section_ids:
  about-this-task: About this task
  steps: Steps
  example: Example:
  example-2: Example:
---

# Creating an internal service account

Create an internal LDAP connection to operate against consent records that are stored as LDAP entries.

## About this task

The Consent Service uses an internal LDAP connection to operate against consent records that are stored as LDAP entries. The Consent Service authenticates the LDAP connection using a service account that must be created and dedicated solely to the Consent Service.

The Consent Service configuration script configures the internal service account using a topology administrator user. If needed, this can be changed to a root distinguished name (DN) user or a user DN whose entry is in the user backend. In all cases, the service account should exist in every LDAP server in the topology.

This service account must have:

* Full read and write access to the Consent Service base DN.

* The ability to read users' `isMemberOf` attribute.

* The right to use the following LDAP controls:

  * IntermediateClientRequestControl (1.3.6.1.4.1.30221.2.5.2)

  * NameWithEntryUUIDRequestControl (1.3.6.1.4.1.30221.2.5.44)

  * RejectUnindexedSearchRequestControl (1.3.6.1.4.1.30221.2.5.54)

  * PermissiveModifyRequestControl (1.2.840.113556.1.4.1413)

  * PostReadRequestControl (1.3.6.1.1.13.2)

For more information about configuring access, see [Managing access control](../managing_access_control/pd_ds_manage_access_control.html).

## Steps

1. To ensure the correct access, create a user with the `bypass-acl` privilege.

   ### Example:

   The following `dsconfig` command creates a topology admin user with the `bypass-acl` privilege.

   ```shell
   $ dsconfig create-topology-admin-user \
     --user-name "Consent Service Account" \
     --set "description:Consent API service account" \
     --set "alternate-bind-dn:cn=consent service account" \
     --set first-name:Consent \
     --set inherit-default-root-privileges:false \
     --set last-name:Service \
     --set password:CHANGE-ME \
     --set privilege:bypass-acl
   ```

   |   |                                                                                                                                          |
   | - | ---------------------------------------------------------------------------------------------------------------------------------------- |
   |   | The `bypass-acl` privilege grants a broad level of access, so you might not want to grant this privilege to the Consent Service account. |

2. Set this user as the `bind-dn` for the Consent Service.

3. To enable a targeted set of functionality for the Consent Service, add the following access control instruction (ACI).

   ### Example:

   The following example grants the access to the `cn=consent service account` DN using global ACIs.

   ```
   # Grant access to the consent record base DN ou=consents,dc=example,dc=com
   dsconfig set-access-control-handler-prop --add 'global-aci:(target="ldap:///ou=consents,dc=example,dc=com")(targetattr="*||+")(version 3.0; acl "Consent Service account access to consent record data"; allow(all) userdn="ldap:///cn=consent service account";)'

   # Grant access to the LDAP request controls used by the Consent Service.
   dsconfig set-access-control-handler-prop --add 'global-aci:(targetcontrol="1.3.6.1.4.1.30221.2.5.2||1.3.6.1.4.1.30221.2.5.44||1.3.6.1.4.1.30221.2.5.54||1.2.840.113556.1.4.1413||1.3.6.1.1.13.2")(version 3.0; acl "Consent Service account access to selected controls"; allow (read) userdn="ldap:///cn=consent service account";)'
   ```

---

---
title: Error cases
description: The following topic discusses troubleshooting possible error cases and solutions.
component: pingdirectory
version: 11.1
page_id: pingdirectory:consent_solution_guide:pd_cs_error_cases
canonical_url: https://docs.pingidentity.com/pingdirectory/11.1/consent_solution_guide/pd_cs_error_cases.html
llms_txt: https://docs.pingidentity.com/pingdirectory/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: September 13, 2023
section_ids:
  consent-service-is-unavailable: Consent Service is unavailable
  requester-lacks-sufficient-rights-to-perform-operation: Requester lacks sufficient rights to perform operation
  subject-and-actor-do-not-match: Subject and actor do not match
  unindexed-search: Unindexed search
  search-size-limit-exceeded: Search size limit exceeded
---

# Error cases

The following topic discusses troubleshooting possible error cases and solutions.

## Consent Service is unavailable

If the Consent Service is unavailable, check the following:

* Ensure that the service is enabled and that communication with the service is available.

* Confirm that the service account for the Consent Service has been properly provisioned.

* If the Consent Service resides on a PingDirectoryProxy server, make sure that the service account exists on the PingDirectoryProxy server and all PingDirectory servers behind the PingDirectoryProxy server.

## Requester lacks sufficient rights to perform operation

A request might be rejected with a 403 for the following reasons:

* The bearer token does not contain a required scope. Check the `privileged-consent-scope` and `unprivileged-consent-scope` properties of the Consent Service configuration.

* The bearer token does not contain a required `audience` claim. Check the `audience` property of the Consent Service configuration.

* Authentication was successful, but the requester is `unprivileged` and attempted to perform an operation that only a `privileged` requester can perform. For example, the requester attempted to act upon a consent record that it does not own, or it attempted to delete a consent record.

When using basic authentication, the requester must be listed in the Consent Service configuration `service-account-dn` property to be considered `privileged`.

## Subject and actor do not match

Only a `privileged` requester can `create` or `modify` a consent record whose `subject` and `actor` values do not match.

## Unindexed search

The Consent Service doesn't allow a client to make an unindexed search. In most cases, a client should be able to fix this by refining the search. For example, if a search by `subject` is unindexed, perform a search by `subject` and `definition` ID.

## Search size limit exceeded

The Consent Service caps the maximum number of records that can be returned in a search result using its `search-size-limit` configuration property. This limit can be increased, or the client might be able to refine the search to produce fewer results.

---

---
title: Example configuration scenarios
description: Review the following client application scenarios to determine how to configure the Consent Service to meet your business needs.
component: pingdirectory
version: 11.1
page_id: pingdirectory:consent_solution_guide:pd_cs_config_scenarios
canonical_url: https://docs.pingidentity.com/pingdirectory/11.1/consent_solution_guide/pd_cs_config_scenarios.html
llms_txt: https://docs.pingidentity.com/pingdirectory/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 3, 2024
section_ids:
  directly-managed-consents: Directly managed consents
  indirectly-managed-consents-basic-authentication: Indirectly managed consents (basic authentication)
---

# Example configuration scenarios

Review the following client application scenarios to determine how to configure the Consent Service to meet your business needs.

## Directly managed consents

In this scenario, one or more client applications provide an interface for individuals to directly manage their own consent records. These applications can only manage consents for the currently authenticated user. In addition, there's a client application for consent administrators.

An OAuth 2 authorization server grants access tokens that the applications use to access the Consent API.

Configuration for this scenario includes:

1. Configure an OAuth 2 authorization server to issue a `urn:pingdirectory:consent` scope to individuals and a `urn:pingdirectory:consent_admin` scope to consent administrators.

2. Create an identity mapper to map subject identifiers used by the authorization server to Lightweight Directory Access Protocol (LDAP) *(tooltip: \<div class="paragraph">
   \<p>An open, cross platform protocol used for interacting with directory services.\</p>
   \</div>)* distinguished names (DNs) used by the PingDirectory server.

3. Configure an access token *(tooltip: \<div class="paragraph">
   \<p>A data object by which a client authenticates to a resource server and lays claim to authorizations for accessing particular resources.\</p>
   \</div>)* validator to validate tokens issued by the OAuth 2 authorization server.

4. Configure the Consent HTTP Servlet Extension to disable HTTP basic authentication and restart the HTTPS Connection Handler.

5. Configure the Consent Service to use the OAuth scopes and token validator.

## Indirectly managed consents (basic authentication)

In this scenario, an application uses a privileged service account to manage its users' consents. The application's privileged account can access any consent record, which gives the application the ability to perform operations that an individual user can't.

The following configuration steps describe the setup needed for the PingDirectory server's Open Banking Account Requests service to use the Consent Service as its backend.

Configuration for this scenario includes:

1. Create a service account for the application.

2. Configure the Consent HTTP Servlet Extension to enable HTTP basic authentication and restart the HTTPS Connection Handler.

3. Create an identity mapper to map the consent record subject and actor attribute values to LDAP DNs.

4. Configure the Consent Service to use the application's service account.

5. Configure the Consent Service to use the identity mapper.

---

---
title: General Consent Service configuration
description: The Consent Service configuration is used to control authorization behavior and determines where consent records are stored in the PingDirectory server.
component: pingdirectory
version: 11.1
page_id: pingdirectory:consent_solution_guide:pd_cs_general_consent_service_config
canonical_url: https://docs.pingidentity.com/pingdirectory/11.1/consent_solution_guide/pd_cs_general_consent_service_config.html
llms_txt: https://docs.pingidentity.com/pingdirectory/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: September 13, 2023
---

# General Consent Service configuration

The Consent Service configuration is used to control authorization behavior and determines where consent records are stored in the PingDirectory server.

You configure the Consent Service properties using the `dsconfig set-consent-service-prop` command. You can use the Consent Service configuration script to configure the Consent Service properties, as show in the following example.

```shell
$ bin/dsconfig set-consent-service-prop \
  --set enabled:true \
  --set base-dn:ou=consents,dc=example,dc=com \
  --set "bind-dn:cn=consent service account" \
  --set unprivileged-consent-scope:urn:pingdirectory:consent \
  --set privileged-consent-scope:urn:pingdirectory:consent_admin \
  --set "consent-record-identity-mapper:User ID Identity Mapper"
```

**Consent Service properties**

| Property                         | Description                                                                                                                                                                                                              | Required to enable service |
| -------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------- |
| `enabled`                        | If set to `true`, the property enables the Consent Service for handling client requests.                                                                                                                                 | Yes                        |
| `base-dn`                        | Specifies a container distinguished name (DN) for consent record entries.                                                                                                                                                | Yes                        |
| `bind-dn`                        | Specifies an internal service account used by the Consent Service to perform LDAP operations.                                                                                                                            | Yes                        |
| `service-account-dn`             | Specifies one or more DNs of requesters that are considered privileged when using basic authentication.If not defined, a requester is only considered privileged if it's mapped to a DN with the `bypass-acl` privilege. | No                         |
| `unprivileged-consent-scope`     | Specifies the name of the scope required for bearer tokens representing unprivileged requesters.                                                                                                                         | Yes                        |
| `privileged-consent-scope`       | Specifies the name of the scope required for bearer tokens representing privileged requesters.                                                                                                                           | Yes                        |
| `consent-record-identity-mapper` | Specifies one or more identity mappers used to map consent record `subject` and `actor` values to DNs.By default, these values are inferred from the authentication context, such as the bearer token subject.           | No                         |
| `audience`                       | Specifies an `audience` claim value that the Consent Service requires to be present in bearer tokens that it accepts.                                                                                                    | No                         |

For the Consent Service to report itself as available to clients:

* The Consent Service must be enabled.

* The Consent Service base DN must be configured and must exist.

* The internal service account must be configured and exist.

* The internal service account must have the right to read, add, modify, and delete entries under the Consent Service base DN.

---

---
title: How applications use the Consent API
description: The following example illustrates both consent capture and consent enforcement using the Consent API.
component: pingdirectory
version: 11.1
page_id: pingdirectory:consent_solution_guide:pd_cs_how_apps_use_consent_api
canonical_url: https://docs.pingidentity.com/pingdirectory/11.1/consent_solution_guide/pd_cs_how_apps_use_consent_api.html
llms_txt: https://docs.pingidentity.com/pingdirectory/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: September 13, 2023
---

# How applications use the Consent API

The following example illustrates both consent capture and consent enforcement using the Consent API.

This example follows a user's journey on a website during which the company must gather consent to track the user's browsing behavior.

1. A user launches the company's application and authenticates.

2. The application wants to record the page visit but first checks if the user has granted consent to do so.

3. The application makes a call to the Consent API to determine if the `browsing-behavior` consent record exists for this user and whether consent been granted.

4. The API returns a result indicating that no consent record exists.

5. The application prompts the user for his or her consent.

6. The application calls the Consent API to retrieve the localization for the `browsing-behavior` consent, which includes the language that the application uses to produce a prompt for the user.

7. After the user makes a decision, the application stores the user's decision by creating a new consent record through a call to the Consent API.

8. Later, the user visits another page in the company's site, and the application wants to record the page visit, so it checks whether the user has granted consent to do so.

9. The application makes a call to the Consent API to get the `browsing-behavior` consent record for this user.

10. If the user's consent record agrees to have the company track his or her browsing behavior, the application can then make the appropriate calls to track browsing behavior.