---
title: Release notes
description: Release notes for Ping CLI, including new features, enhancements, and resolved issues for each release.
component: pingcli
version: 1.11
page_id: pingcli:release_notes:pingcli_release_notes
canonical_url: https://developer.pingidentity.com/pingcli/1.11/release_notes/pingcli_release_notes.html
llms_txt: https://developer.pingidentity.com/pingcli/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: November 2, 2026
section_ids:
  ping-cli-1-11-0-november-2-2026: Ping CLI 1.11.0 (November 2, 2026)
  general: General
  pingone: PingOne
  ping-cli-1-10-0-october-19-2026: Ping CLI 1.10.0 (October 19, 2026)
  pingfederate: PingFederate
  pingone-2: PingOne
  ping-cli-1-9-0-october-6-2026: Ping CLI 1.9.0 (October 6, 2026)
  general-2: General
  pingone-3: PingOne
  ping-cli-1-8-0-september-21-2026: Ping CLI 1.8.0 (September 21, 2026)
  pingfederate-2: PingFederate
  pingone-4: PingOne
  ping-cli-1-7-0-september-8-2026: Ping CLI 1.7.0 (September 8, 2026)
  general-3: General
  pingfederate-3: PingFederate
  ping-cli-1-6-0-august-31-2026: Ping CLI 1.6.0 (August 31, 2026)
  pingfederate-4: PingFederate
  ping-cli-1-5-0-august-18-2026: Ping CLI 1.5.0 (August 18, 2026)
  pingfederate-5: PingFederate
  pingone-5: PingOne
  davinci: DaVinci
  pingone-authorize: PingOne Authorize
  pingone-mfa: PingOne MFA
  pingone-protect: PingOne Protect
  ping-cli-1-4-0-august-3-2026: Ping CLI 1.4.0 (August 3, 2026)
  pingfederate-6: PingFederate
  pingone-6: PingOne
  davinci-2: DaVinci
  pingone-credentials: PingOne Credentials
  pingone-mfa-2: PingOne MFA
  pingone-verify: PingOne Verify
  ping-cli-1-3-0-july-20-2026: Ping CLI 1.3.0 (July 20, 2026)
  general-4: General
  pingfederate-7: PingFederate
  pingone-7: PingOne
  ping-cli-1-2-0-july-6-2026: Ping CLI 1.2.0 (July 6, 2026)
  general-5: General
  pingfederate-8: PingFederate
  pingone-8: PingOne
  davinci-3: DaVinci
  pingone-authorize-2: PingOne Authorize
  pingone-protect-2: PingOne Protect
  ping-cli-1-1-0-june-22-2026: Ping CLI 1.1.0 (June 22, 2026)
  general-6: General
  prevrel: Previous releases
---

# Release notes

Release notes for Ping CLI, including new features, enhancements, and resolved issues for each release.

Subscribe to get automatic updates: [icon: rss-square, set=fa][Ping CLI release notes RSS feed](pingcli_release_notes.xml)

## Ping CLI 1.11.0 (November 2, 2026)

### General

New

* Reserved `-i` as the consistent shorthand for each resource's own identifier in CRUD commands. Existing shorthand flags for self-identifiers are maintained for backwards-compatibility, but have been marked as deprecated.

Fixed

* Fixed `--profile` with a profile that does not exist running guided setup prompts or reporting that authentication is not configured, so commands now report that the profile does not exist and how to create it

* Fixed `pingcli config get`, `config set`, and `config unset` ignoring the `PINGCLI_PROFILE` environment variable, so with it exported `config set` and `config unset` now modify that profile instead of the active profile

* Fixed authentication sessions being stored under the active profile instead of the profile selected with `--profile` or `PINGCLI_PROFILE`, so login, logout, and later commands now use the same session

* Fixed guided authentication setup saving its answers to the active profile instead of the profile selected with `--profile` or `PINGCLI_PROFILE`, and it now stops before prompting when that profile does not exist

* Fixed the `api` command sending an empty request body when the file passed to `--data` does not exist; it now reports an error before sending the request

* When the API returned a successful response with an empty body, a small subset of commands crashed; they now display an empty result

Improved

* Removed the unused `telemetry.tls.insecureSkipVerify` configuration option (environment variable `OTEL_EXPORTER_OTLP_INSECURE`); the setting was registered but never read by the CLI

* Restored shell autocompletion for the `--profile` and `--output-format` global flags, the `--http-method` flag of `pingcli <product> request`, and the profile-name arguments of `config profiles use`, `config profiles delete`, and `config profiles show`; shell completion for `use` and `delete` omits the active profile

### PingOne

Fixed

* Fixed `pingone auth refresh` reporting an expired session for failures that are not expiry, so a missing refresh token now explains how to enable refresh tokens and other failures, such as network errors or incorrect client credentials, show their underlying cause

Improved

* Added a warning to `pingone auth login` when it reuses a still-valid session that has no refresh token, with the steps to enable refresh tokens

[View release on GitHub](https://github.com/pingidentity/pingcli/releases/tag/v1.11.0)

## Ping CLI 1.10.0 (October 19, 2026)

### PingFederate

New

Added management commands for the following resources:

* OAuth CIMD (Client ID Metadata Document) policies

### PingOne

Improved

* Added commands to update an environment's status (activate or soft-delete) and promote an environment from sandbox to production

[View release on GitHub](https://github.com/pingidentity/pingcli/releases/tag/v1.10.0)

## Ping CLI 1.9.0 (October 6, 2026)

### General

Fixed

* Fixed login failures with "data passed to Set was too big" by storing oversized authentication sessions across multiple OS keychain entries instead of a single entry

Improved

* Added a notice when a newer Ping CLI release is available, shown after interactive commands and by `pingcli --version`; opt out by setting `skipUpdateCheck` in a configuration profile or the `PINGCLI_SKIP_UPDATE_CHECK` environment variable

* Added suggestions for the closest matching command when a subcommand is mistyped anywhere in the CLI

* Improved token exchange error messages by validating authorization server token responses and surfacing the server's error details, including under --debug

### PingOne

Fixed

* Removed the non-functional `--client-credentials`, `--authorization-code`, and `--device-code` flags from `pingone auth login`, which were listed in help but never changed how authentication worked

Improved

* Made `--environment-id` optional on commands scoped to a PingOne environment, resolving it from `PINGCLI_PINGONE_ENVIRONMENT_ID` or the active profile's `service.pingOne.endpoint.environmentID` when omitted

[View release on GitHub](https://github.com/pingidentity/pingcli/releases/tag/v1.9.0)

## Ping CLI 1.8.0 (September 21, 2026)

### PingFederate

New

* Added `advanced-services pingfederate` commands for managing PingFederate deployed as a private tenant in PingOne Advanced Services, with client credentials, authorization code, and device code OAuth authentication

Improved

* Added `--id` as a settable create-body flag for PingFederate resources that accept caller-supplied instance IDs

### PingOne

Info

* The `pingone languages agreement-revisions` command is deprecated and will be removed in a future release; use `pingone agreements languages revisions` instead

[View release on GitHub](https://github.com/pingidentity/pingcli/releases/tag/v1.8.0)

## Ping CLI 1.7.0 (September 8, 2026)

### General

Breaking Changes

* The `apply` command no longer accepts ID flags such as `--id` (they are removed from help text, and passing one returns an error). The ID is assigned automatically when the resource already exists

Fixed

* Fixed the CLI always rejecting empty request bodies

### PingFederate

Breaking Changes

* Added a required `--from-file` flag to `invoke-action` for IDP adapters, data stores, and secret managers to support actions that require parameters

New

Added management commands for the following resources:

* access token manager descriptors

* authentication policy contract to SP adapter mappings

* authentication policy move action

* cluster status

* IdP adapter descriptors

* IdP STS request parameters contracts

* IdP-to-SP adapter mappings

* OAuth authorization detail processor descriptors

* OAuth client registration policy descriptors

* OAuth client revoke-secondary-secrets action

* OAuth token exchange generator settings

* out-of-band authenticator plugin descriptors and instance actions, including action invocation

* outbound provisioning settings

* PingOne for Enterprise settings

* protocol metadata lifetime settings

* protocol metadata signing settings

* server settings notifications

* service authentication

* SP adapter descriptors and adapter actions

* SP token generator descriptors

* token exchange generator groups

* token exchange processor policy to token generator mappings

* token exchange processor settings

* token generators

* WS-Trust STS Settings and issuer certificates

[View release on GitHub](https://github.com/pingidentity/pingcli/releases/tag/v1.7.0)

## Ping CLI 1.6.0 (August 31, 2026)

Breaking Changes

* Renamed the `--id` flag to `--name` on OAuth common scope get, replace, and delete commands to match the underlying scope identifier

### PingFederate

New

Added management commands for the following resources:

* authentication policies

* authentication session policies

* certificate revocation settings

* change-password action for administrative accounts

* identity store provisioner descriptors

* IdP default URLs

* incoming proxy settings

* Kerberos realm settings

* Kerberos realms

* license

* license agreement

* metadata URLs

* notification publisher plugin descriptors

* notification publishers and notification publisher settings

* OAuth CIBA server policy request policies and settings

* OAuth common scope groups

* OAuth exclusive scope groups

* OAuth exclusive scopes

* OCSP certificates

* PingOne for Enterprise identity repository

* PingOne for Enterprise key pairs

* redirect validation settings

* resource-owner-credentials-mappings

* system keys

* the application session policy

* the default authentication policy

* token exchange processor policies

* token processor descriptors

* token processors

Improved

* Added support for supplying the new password via --from-file to the administrative accounts change-password and reset-password actions

[View release on GitHub](https://github.com/pingidentity/pingcli/releases/tag/v1.6.0)

## Ping CLI 1.5.0 (August 18, 2026)

### PingFederate

New

Added management commands for the following resources:

* attribute requester mappings

* authentication selectors

* cluster admin node status

* collect support data archives

* identity store provisioners

* OAuth access token mappings

* OAuth authentication policy contract mappings

* OAuth authorization detail processors

* OAuth authorization server settings

* OAuth common scopes

* OAuth IdP adapter mappings

* OAuth out-of-band authenticator plugins

* OAuth processor policy mappings

* OAuth/OpenID Connect keys settings and additional key sets

* password credential validator descriptors

* PingOne connections

* secret manager descriptors

* secret managers

* SP default URLs

* SP target URL mappings

* SSL server key pairs

* token processor to token generator mappings

* exporting the configuration archive

* rotating the configuration encryption key

* key pair key algorithms

* cluster replication

* cluster admin node role

* connection metadata SAML export

* connection metadata SAML-to-JSON conversion

* import action command for config-archive

* configuration encryption keys

* custom data store descriptors

* IdP connector descriptors

Improved

* Added authorization_code and device_code OAuth grant types, with browser-based and device-flow login, session status, and automatic session refresh

* Added CLI flags for common request body fields

### PingOne

New

Added management commands for the following resources:

* keys

* user credentials

Improved

* Added CLI flags for common request body fields

### DaVinci

Improved

* Added CLI flags for common request body fields

### PingOne Authorize

Improved

* Added CLI flags for common request body fields

### PingOne MFA

Improved

* Added CLI flags for common request body fields

### PingOne Protect

Improved

* Added CLI flags for common request body fields

[View release on GitHub](https://github.com/pingidentity/pingcli/releases/tag/v1.5.0)

## Ping CLI 1.4.0 (August 3, 2026)

### PingFederate

New

Added management commands for the following resources:

* administrative API CORS settings

* audit log settings

* authentication policies settings

* bulk configuration export

* bulk configuration import

* CA certificates

* CAPTCHA provider settings

* CAPTCHA providers

* certificate group certificates

* cluster settings

* config store settings

* log settings

* OAuth access token manager settings

* OAuth access token managers

* OAuth authorization detail types

* OAuth virtual issuers

* signing key pairs

* SP adapters

* SP connections, including credentials certificates, decryption keys, and signing settings

* SP IdP connections, including certificates, decryption keys, and signing settings

* SSL client key pairs

Improved

* Added read-only commands for captcha provider descriptors

* Added import, export, CSR, and rotation settings management commands for signing key pairs

### PingOne

New

Added management commands for the following resources:

* Authorize application resources

* bill of materials

* branding settings

* certificates

* credential type versions

* forms

* gateway role assignments

* language localization status

* notifications settings phone delivery settings

* notifications settings SMTP email delivery configuration

* organizations, license names, and license active identity counts

* population default identity provider

* resource attributes

* resource client secrets

* trusted email addresses

* user enabled status

Improved

* Added read commands for flow policies

* Updated polymorphic resources like applications to accept the same JSON shape as that returned by the API from GET calls, rather than a shape that is custom to the CLI. The prior template shape is deprecated. The template command for these resources now supports a --template-type flag to retrieve a template for the desired type (for example: oidc, saml, etc. for applications). If not provided, --template-type will be set to a default for the resource (oidc for applications).

### DaVinci

New

Added management commands for the following resources:

* flow versions

Improved

* Added `enable` and `disable` action commands for flows

* Added clone action for connector instances

* Added DaVinci flow-policy/flow-policy-events list command

### PingOne Credentials

Improved

* Added CLI flags for common request body fields

### PingOne MFA

Improved

* Added `send-logs` and `update-nickname` action commands to `mfa user-devices`

### PingOne Verify

Improved

* Added CLI flags for common request body fields

[View release on GitHub](https://github.com/pingidentity/pingcli/releases/tag/v1.4.0)

## Ping CLI 1.3.0 (July 20, 2026)

### General

Info

* Removed the --template output flag and its custom text/template rendering

Fixed

* Fix some API error detail not being returned by the CLI for PingOne Authorize and PingOne Verify endpoints.

Improved

* Add support for the `apply` command to all singleton resources as an alias for `replace`. Also add `apply` to the PingFederate data-stores and PingOne application-resource-permissions resources where it was missing.

* Renamed several nested subcommands to drop the redundant parent prefix (for example, `group group-nestings` is now `group nestings`, `verify verify-policies` is now `verify policies`, etc), while keeping the previous names available as aliases

### PingFederate

New

Added management commands for the following resources:

* authentication policy fragments

* federation info

* OAuth client registration policies

* OAuth client settings

* OAuth/OpenID Connect policies

* OAuth/OpenID Connect settings

* session quotas

* session settings

### PingOne

New

Added management commands for the following resources:

* alert channels

* credential issuance rule usage counts and usage details

* email domains

* identity propagation plans

* images

* integrations

* rate limit IP configurations

* reCAPTCHA v2 configuration

Improved

* Added `gateways gateway-credentials get` command to read a single gateway credential

* Added a list command for resource application permissions

* Added notifications-settings management commands

* Added pingone applications attribute-mappings management commands

* Failing paged export read operations now attach the HTTP response so `--debug` renders the response body and JSON error output reports the failing request's status and request ID

[View release on GitHub](https://github.com/pingidentity/pingcli/releases/tag/v1.3.0)

## Ping CLI 1.2.0 (July 6, 2026)

### General

New

* Added `credential-issuer-profile` resource to the PingOne Credentials connector, supporting `get`, `replace`, and `template` commands

New

|   |                                                                                                                                                                   |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | * PingOne and PingFederate: Refresh the access token when authentication credentials change so a cached token issued for previous credentials is no longer reused |

Fixed

* auth: Added a connector section header to each `auth status` block so statuses for multiple services are clearly distinguishable

* Fixed template command example text for replace-only resources to show `replace --from-file` instead of `create --from-file`

Improved

* Updated output schema reference generator with editorial fixes and subfolder restructure

### PingFederate

New

Added management commands for the following resources:

* administrative accounts

* authentication API applications

* authentication API settings

* data stores

* extended properties

* IdP adapters

* local identity profiles

* OAuth clients

* password credential validators

* server settings

* virtual host names

Info

* Removed the `--pingfederate-*` and `--as-pingfederate-*` authentication CLI flags (such as `--pingfederate-client-id`); configure PingFederate authentication via environment variables, the configuration file, or the init wizard instead

* The `accessTokenAuth` authentication type is deprecated and will be removed in a future release; use the `basicAuth` or `oauth` authentication type instead

Improved

* Added management command for version

### PingOne

New

Added management commands for the following resources:

* admin config

* credential issuance rules

* custom domains

* FIDO2 policies

* user digital wallets

Fixed

* Fixed the `--template` flag on `pingone api` so template field traversal works against JSON response data

### DaVinci

Fixed

* Fixed template for application resources to correctly omit server-set read-only fields (`apiKey.value`, `oauth.clientSecret`) that were previously included in the generated template skeleton

### PingOne Authorize

New

Added management commands for the following resources:

* decision endpoints

### PingOne Protect

New

Added management commands for the following resources:

* risk policy sets

[View release on GitHub](https://github.com/pingidentity/pingcli/releases/tag/v1.2.0)

## Ping CLI 1.1.0 (June 22, 2026)

### General

Fixed

* Both `PINGCLI_PINGONE_*` and bare `PINGONE_*` environment variable names are now fully supported (e.g. both `PINGCLI_PINGONE_ENVIRONMENT_ID` and `PINGONE_ENVIRONMENT_ID` resolve), fixing a silent breaking change for pipelines using the pre-v1 names. `PINGCLI_LOGIN_STORAGE_TYPE` is honoured alongside `PINGCLI_AUTH_STORAGE_TYPE`.

* Config migration now correctly relocates PingFederate `clientCredentialsAuth` credentials (client ID, client secret, token URL, scopes) to the canonical `oauth.clientCredentials.*` keys and removes the legacy subtree, including for configs written all-lowercase by older (v0.8.x) Ping CLI versions, which were previously left untouched.

* Config migration now preserves PingOne authentication values written by older (v0.8.x) Ping CLI versions: the legacy `service.pingone.*` worker layout (worker client credentials, `regioncode`, `type: worker`) is migrated to the current `service.pingOne.*` schema instead of being silently dropped, with `regioncode` translated to the equivalent `endpoint.rootDomain`. The PingOne environment ID and authorization-code `redirectUri` path/port are also relocated to their canonical keys rather than being lost.

Improved

* Config migration now removes the deprecated `export.*` configuration subtree, which is no longer persisted to the configuration file (the export command's settings are flag/environment-only).

[View release on GitHub](https://github.com/pingidentity/pingcli/releases/tag/v1.1.0)

### Previous releases

* [1.0](https://github.com/pingidentity/pingcli/releases/tag/v1.0.0)

* [0.8](https://github.com/pingidentity/pingcli/releases/tag/v0.8.0)