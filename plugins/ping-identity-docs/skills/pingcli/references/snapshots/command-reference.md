---
title: pingcli
description: A CLI tool for managing the configuration of Ping Identity products.
component: pingcli
version: 1.11
page_id: pingcli:command_reference:pingcli
canonical_url: https://developer.pingidentity.com/pingcli/1.11/command_reference/pingcli.html
llms_txt: https://developer.pingidentity.com/pingcli/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: October 1, 2026
section_ids:
  synopsis: Synopsis
  options: Options
  subcommands: Subcommands
---

# pingcli

A CLI tool for managing the configuration of Ping Identity products.

## Synopsis

A CLI tool for managing the configuration of Ping Identity products.

Configuration: Settings resolve in priority order: command-line flag, environment variable, configuration file, then built-in default.

```
Every configuration key is settable by environment variable. The variable name
is the key in upper snake case, prefixed with PINGCLI_ and with each path segment
separated by an underscore. For example, the key
service.pingOne.authentication.clientCredentials.clientID maps to
PINGCLI_SERVICE_PINGONE_AUTHENTICATION_CLIENTCREDENTIALS_CLIENTID. Short aliases
such as PINGCLI_PINGONE_CLIENT_CREDENTIALS_CLIENT_ID and PINGCLI_PINGONE_ENVIRONMENT_ID
are also honoured, as are their bare PINGONE_* equivalents. Invalid
environment-variable values are rejected with an error, the same as invalid flag
values.
```

```
Use --profile (-P) to select a configured profile for a single command without
changing the active profile.
```

```
pingcli
```

## Options

```
  -C, --config string           The relative or full path to a custom Ping CLI configuration file. (default $HOME/.pingcli/config.yaml)
  -h, --help                    help for pingcli
  -D, --detailed-exitcode       Enable detailed exit code output. (default false) 0 - pingcli command succeeded with no errors or warnings. 1 - pingcli command failed with errors. 2 - pingcli command succeeded with warnings.
  -O, --output-format string    Specify the console output format. (default text) Options are: json, ndjson, ndjson-typed, ndjson-wrapped, text.
  -P, --profile string          The name of a configuration profile to use.
      --debug                   Enable debug output for error messages, including stack traces and transaction IDs. (default false)
      --log-file string         Write logs to a file at the given path. File logging is disabled when not set.
      --log-file-level string   Set the file log level. Options are: DEBUG, INFO, WARN, ERROR. (default DEBUG)
      --log-level string        Set the console log level. Options are: DEBUG, INFO, WARN, ERROR. (default WARN)
      --no-color                Disable text output in color. (default false)
      --query string            JMESPath expression to filter JSON output. Requires -O json, ndjson, ndjson-typed, or ndjson-wrapped. Example: --query 'data[?enabled].name'
```

## Subcommands

* [pingcli advanced-services](pingcli_advanced-services.html) - Administration tools for your PingOne Advanced Services tenant.

* [pingcli agent-skills](pingcli_agent-skills.html) - Find and install agent skills for Ping CLI.

* [pingcli auth](pingcli_auth.html) - Authenticate (or refresh authentication) for multiple connected products and services at once.

* [pingcli authorize](pingcli_authorize.html) - Administration tools for the PingOne Authorize universal service.

* [pingcli completion](pingcli_completion.html) - Prints shell completion scripts

* [pingcli config](pingcli_config.html) - Manage the CLI configuration.

* [pingcli credentials](pingcli_credentials.html) - Administration tools for the PingOne Credentials universal service.

* [pingcli davinci](pingcli_davinci.html) - Administration tools for the PingOne DaVinci universal service.

* [pingcli feedback](pingcli_feedback.html) - Help us improve the CLI. Report issues or send us feedback on using the CLI tool.

* [pingcli init](pingcli_init.html) - Initialize Ping CLI with a guided setup wizard.

* [pingcli mfa](pingcli_mfa.html) - Administration tools for the PingOne MFA universal service.

* [pingcli pingfederate](pingcli_pingfederate.html) - Administration tools for PingFederate deployed as software

* [pingcli pingone](pingcli_pingone.html) - Administration tools for the PingOne platform.

* [pingcli protect](pingcli_protect.html) - Administration tools for the PingOne Protect universal service.

* [pingcli verify](pingcli_verify.html) - Administration tools for the PingOne Verify universal service.

---

---
title: pingcli advanced-services
description: Administration tools for your PingOne Advanced Services tenant.
component: pingcli
version: 1.11
page_id: pingcli:command_reference:pingcli_advanced-services
canonical_url: https://developer.pingidentity.com/pingcli/1.11/command_reference/pingcli_advanced-services.html
llms_txt: https://developer.pingidentity.com/pingcli/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: August 28, 2026
section_ids:
  synopsis: Synopsis
  options-inherited-from-parent-commands: Options inherited from parent commands
  more-information: More information
  subcommands: Subcommands
---

# pingcli advanced-services

Administration tools for your PingOne Advanced Services tenant.

## Synopsis

Administration tools for your PingOne Advanced Services tenant.

```
pingcli advanced-services
```

## Options inherited from parent commands

```
  -C, --config string           The relative or full path to a custom Ping CLI configuration file. (default $HOME/.pingcli/config.yaml)
  -D, --detailed-exitcode       Enable detailed exit code output. (default false) 0 - pingcli command succeeded with no errors or warnings. 1 - pingcli command failed with errors. 2 - pingcli command succeeded with warnings.
  -O, --output-format string    Specify the console output format. (default text) Options are: json, ndjson, ndjson-typed, ndjson-wrapped, text.
  -P, --profile string          The name of a configuration profile to use.
      --debug                   Enable debug output for error messages, including stack traces and transaction IDs. (default false)
      --log-file string         Write logs to a file at the given path. File logging is disabled when not set.
      --log-file-level string   Set the file log level. Options are: DEBUG, INFO, WARN, ERROR. (default DEBUG)
      --log-level string        Set the console log level. Options are: DEBUG, INFO, WARN, ERROR. (default WARN)
      --no-color                Disable text output in color. (default false)
      --query string            JMESPath expression to filter JSON output. Requires -O json, ndjson, ndjson-typed, or ndjson-wrapped. Example: --query 'data[?enabled].name'
```

## More information

* [pingcli](pingcli.html) - A CLI tool for managing the configuration of Ping Identity products.

## Subcommands

* [pingcli advanced-services pingfederate](pingcli_advanced-services_pingfederate.html) - Administration tools for PingFederate deployed as a private tenant service in PingOne Advanced Services

---

---
title: pingcli advanced-services pingfederate
description: Administration tools for PingFederate deployed as a private tenant service in PingOne Advanced Services
component: pingcli
version: 1.11
page_id: pingcli:command_reference:pingcli_advanced-services_pingfederate
canonical_url: https://developer.pingidentity.com/pingcli/1.11/command_reference/pingcli_advanced-services_pingfederate.html
llms_txt: https://developer.pingidentity.com/pingcli/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: September 3, 2026
section_ids:
  synopsis: Synopsis
  options-inherited-from-parent-commands: Options inherited from parent commands
  more-information: More information
  subcommands: Subcommands
---

# pingcli advanced-services pingfederate

Administration tools for PingFederate deployed as a private tenant service in PingOne Advanced Services

## Synopsis

Administration tools for PingFederate deployed as a private tenant service in PingOne Advanced Services.

When multiple products are configured in the CLI, the platform command can be used to manage one or more products collectively.

The --profile command switch can be used to specify the profile of Ping products to be managed.

```
pingcli advanced-services pingfederate
```

## Options inherited from parent commands

```
  -C, --config string           The relative or full path to a custom Ping CLI configuration file. (default $HOME/.pingcli/config.yaml)
  -D, --detailed-exitcode       Enable detailed exit code output. (default false) 0 - pingcli command succeeded with no errors or warnings. 1 - pingcli command failed with errors. 2 - pingcli command succeeded with warnings.
  -O, --output-format string    Specify the console output format. (default text) Options are: json, ndjson, ndjson-typed, ndjson-wrapped, text.
  -P, --profile string          The name of a configuration profile to use.
      --debug                   Enable debug output for error messages, including stack traces and transaction IDs. (default false)
      --log-file string         Write logs to a file at the given path. File logging is disabled when not set.
      --log-file-level string   Set the file log level. Options are: DEBUG, INFO, WARN, ERROR. (default DEBUG)
      --log-level string        Set the console log level. Options are: DEBUG, INFO, WARN, ERROR. (default WARN)
      --no-color                Disable text output in color. (default false)
      --query string            JMESPath expression to filter JSON output. Requires -O json, ndjson, ndjson-typed, or ndjson-wrapped. Example: --query 'data[?enabled].name'
```

## More information

* [pingcli advanced-services](pingcli_advanced-services.html) - Administration tools for your PingOne Advanced Services tenant.

## Subcommands

* [pingcli advanced-services pingfederate administrative-accounts](pingcli_advanced-services_pingfederate_administrative-accounts.html) - PingFederate Administrative Accounts

* [pingcli advanced-services pingfederate administrative-api](pingcli_advanced-services_pingfederate_administrative-api.html) - Manage PingFederate Administrative API resources

* [pingcli advanced-services pingfederate api](pingcli_advanced-services_pingfederate_api.html) - Send a custom REST API request to the management API of PingFederate (Advanced Services).

* [pingcli advanced-services pingfederate auth](pingcli_advanced-services_pingfederate_auth.html) - Authenticate Ping CLI to the PingFederate (Advanced Services) management APIs.

* [pingcli advanced-services pingfederate authentication-api](pingcli_advanced-services_pingfederate_authentication-api.html) - Manage PingFederate Authentication API resources

* [pingcli advanced-services pingfederate authentication-policies](pingcli_advanced-services_pingfederate_authentication-policies.html) - Manage PingFederate Authentication Policies resources

* [pingcli advanced-services pingfederate authentication-policy-contracts](pingcli_advanced-services_pingfederate_authentication-policy-contracts.html) - PingFederate Authentication Policy Contracts

* [pingcli advanced-services pingfederate authentication-selectors](pingcli_advanced-services_pingfederate_authentication-selectors.html) - PingFederate Authentication Selectors

* [pingcli advanced-services pingfederate bulk](pingcli_advanced-services_pingfederate_bulk.html) - Manage PingFederate Bulk resources

* [pingcli advanced-services pingfederate captcha-providers](pingcli_advanced-services_pingfederate_captcha-providers.html) - PingFederate CAPTCHA Providers

* [pingcli advanced-services pingfederate certificates](pingcli_advanced-services_pingfederate_certificates.html) - Manage PingFederate Certificates resources

* [pingcli advanced-services pingfederate cluster](pingcli_advanced-services_pingfederate_cluster.html) - Manage PingFederate Cluster resources

* [pingcli advanced-services pingfederate collect-support-data](pingcli_advanced-services_pingfederate_collect-support-data.html) - Manage PingFederate Collect Support Data (CSD) resources

* [pingcli advanced-services pingfederate config-archive](pingcli_advanced-services_pingfederate_config-archive.html) - Manage the PingFederate configuration archive

* [pingcli advanced-services pingfederate config-store-settings](pingcli_advanced-services_pingfederate_config-store-settings.html) - PingFederate Configuration Store Settings

* [pingcli advanced-services pingfederate configuration-encryption-keys](pingcli_advanced-services_pingfederate_configuration-encryption-keys.html) - PingFederate Configuration Encryption Keys

* [pingcli advanced-services pingfederate connection-metadata](pingcli_advanced-services_pingfederate_connection-metadata.html) - Manage PingFederate connection metadata

* [pingcli advanced-services pingfederate data-stores](pingcli_advanced-services_pingfederate_data-stores.html) - PingFederate Data Stores

* [pingcli advanced-services pingfederate extended-properties](pingcli_advanced-services_pingfederate_extended-properties.html) - PingFederate Extended Properties

* [pingcli advanced-services pingfederate identity-store-provisioners](pingcli_advanced-services_pingfederate_identity-store-provisioners.html) - PingFederate Identity Store Provisioners

* [pingcli advanced-services pingfederate idp](pingcli_advanced-services_pingfederate_idp.html) - Manage PingFederate IdP resources

* [pingcli advanced-services pingfederate idp-to-sp-adapter-mappings](pingcli_advanced-services_pingfederate_idp-to-sp-adapter-mappings.html) - PingFederate IdP-to-SP Adapter Mappings

* [pingcli advanced-services pingfederate incoming-proxy-settings](pingcli_advanced-services_pingfederate_incoming-proxy-settings.html) - PingFederate incoming proxy settings

* [pingcli advanced-services pingfederate init](pingcli_advanced-services_pingfederate_init.html) - Initialize Ping CLI for the PingFederate (Advanced Services) management APIs.

* [pingcli advanced-services pingfederate kerberos](pingcli_advanced-services_pingfederate_kerberos.html) - Manage PingFederate Kerberos resources

* [pingcli advanced-services pingfederate key-pairs](pingcli_advanced-services_pingfederate_key-pairs.html) - Manage PingFederate Key Pairs resources

* [pingcli advanced-services pingfederate license](pingcli_advanced-services_pingfederate_license.html) - PingFederate license

* [pingcli advanced-services pingfederate local-identity](pingcli_advanced-services_pingfederate_local-identity.html) - Manage PingFederate Local Identity resources

* [pingcli advanced-services pingfederate metadata-urls](pingcli_advanced-services_pingfederate_metadata-urls.html) - PingFederate metadata URLs

* [pingcli advanced-services pingfederate notification-publishers](pingcli_advanced-services_pingfederate_notification-publishers.html) - PingFederate notification publishers

* [pingcli advanced-services pingfederate oauth](pingcli_advanced-services_pingfederate_oauth.html) - Manage PingFederate OAuth resources

* [pingcli advanced-services pingfederate password-credential-validators](pingcli_advanced-services_pingfederate_password-credential-validators.html) - PingFederate Password Credential Validators

* [pingcli advanced-services pingfederate ping-one-connections](pingcli_advanced-services_pingfederate_ping-one-connections.html) - PingFederate PingOne connections

* [pingcli advanced-services pingfederate pingone-for-enterprise](pingcli_advanced-services_pingfederate_pingone-for-enterprise.html) - Manage the PingFederate connection to PingOne for Enterprise

* [pingcli advanced-services pingfederate protocol-metadata](pingcli_advanced-services_pingfederate_protocol-metadata.html) - Manage PingFederate Protocol Metadata resources

* [pingcli advanced-services pingfederate redirect-validation](pingcli_advanced-services_pingfederate_redirect-validation.html) - PingFederate Redirect Validation Settings

* [pingcli advanced-services pingfederate secret-managers](pingcli_advanced-services_pingfederate_secret-managers.html) - PingFederate Secret Managers

* [pingcli advanced-services pingfederate server-settings](pingcli_advanced-services_pingfederate_server-settings.html) - PingFederate Server Settings

* [pingcli advanced-services pingfederate service-authentication](pingcli_advanced-services_pingfederate_service-authentication.html) - PingFederate Service Authentication

* [pingcli advanced-services pingfederate session](pingcli_advanced-services_pingfederate_session.html) - Manage PingFederate Session resources

* [pingcli advanced-services pingfederate sp](pingcli_advanced-services_pingfederate_sp.html) - Manage PingFederate SP resources

* [pingcli advanced-services pingfederate token-processor-to-token-generator-mappings](pingcli_advanced-services_pingfederate_token-processor-to-token-generator-mappings.html) - PingFederate Token Processor to Token Generator Mappings

* [pingcli advanced-services pingfederate version](pingcli_advanced-services_pingfederate_version.html) - PingFederate Version

* [pingcli advanced-services pingfederate virtual-host-names](pingcli_advanced-services_pingfederate_virtual-host-names.html) - PingFederate Virtual Host Names

---

---
title: pingcli advanced-services pingfederate administrative-accounts
description: PingFederate Administrative Accounts
component: pingcli
version: 1.11
page_id: pingcli:command_reference:pingcli_advanced-services_pingfederate_administrative-accounts
canonical_url: https://developer.pingidentity.com/pingcli/1.11/command_reference/pingcli_advanced-services_pingfederate_administrative-accounts.html
llms_txt: https://developer.pingidentity.com/pingcli/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: August 28, 2026
section_ids:
  synopsis: Synopsis
  options-inherited-from-parent-commands: Options inherited from parent commands
  more-information: More information
  subcommands: Subcommands
---

# pingcli advanced-services pingfederate administrative-accounts

PingFederate Administrative Accounts

## Synopsis

PingFederate Administrative Accounts

```
pingcli advanced-services pingfederate administrative-accounts [flags]
```

## Options inherited from parent commands

```
  -C, --config string           The relative or full path to a custom Ping CLI configuration file. (default $HOME/.pingcli/config.yaml)
  -D, --detailed-exitcode       Enable detailed exit code output. (default false) 0 - pingcli command succeeded with no errors or warnings. 1 - pingcli command failed with errors. 2 - pingcli command succeeded with warnings.
  -O, --output-format string    Specify the console output format. (default text) Options are: json, ndjson, ndjson-typed, ndjson-wrapped, text.
  -P, --profile string          The name of a configuration profile to use.
      --debug                   Enable debug output for error messages, including stack traces and transaction IDs. (default false)
      --log-file string         Write logs to a file at the given path. File logging is disabled when not set.
      --log-file-level string   Set the file log level. Options are: DEBUG, INFO, WARN, ERROR. (default DEBUG)
      --log-level string        Set the console log level. Options are: DEBUG, INFO, WARN, ERROR. (default WARN)
      --no-color                Disable text output in color. (default false)
      --query string            JMESPath expression to filter JSON output. Requires -O json, ndjson, ndjson-typed, or ndjson-wrapped. Example: --query 'data[?enabled].name'
```

## More information

* [pingcli advanced-services pingfederate](pingcli_advanced-services_pingfederate.html) - Administration tools for PingFederate deployed as a private tenant service in PingOne Advanced Services

## Subcommands

* [pingcli advanced-services pingfederate administrative-accounts apply](pingcli_advanced-services_pingfederate_administrative-accounts_apply.html) - Create or update an administrative account

* [pingcli advanced-services pingfederate administrative-accounts change-password](pingcli_advanced-services_pingfederate_administrative-accounts_change-password.html) - Change the currently-authenticated administrative account's password

* [pingcli advanced-services pingfederate administrative-accounts create](pingcli_advanced-services_pingfederate_administrative-accounts_create.html) - Create a new administrative account

* [pingcli advanced-services pingfederate administrative-accounts delete](pingcli_advanced-services_pingfederate_administrative-accounts_delete.html) - Delete an administrative account

* [pingcli advanced-services pingfederate administrative-accounts get](pingcli_advanced-services_pingfederate_administrative-accounts_get.html) - Read a specific administrative account

* [pingcli advanced-services pingfederate administrative-accounts list](pingcli_advanced-services_pingfederate_administrative-accounts_list.html) - List all administrative accounts

* [pingcli advanced-services pingfederate administrative-accounts replace](pingcli_advanced-services_pingfederate_administrative-accounts_replace.html) - Update an administrative account

* [pingcli advanced-services pingfederate administrative-accounts reset-password](pingcli_advanced-services_pingfederate_administrative-accounts_reset-password.html) - Reset a PingFederate administrative account password

* [pingcli advanced-services pingfederate administrative-accounts template](pingcli_advanced-services_pingfederate_administrative-accounts_template.html) - Generate an administrative account JSON template

---

---
title: pingcli advanced-services pingfederate administrative-accounts apply
description: Create or update an administrative account
component: pingcli
version: 1.11
page_id: pingcli:command_reference:pingcli_advanced-services_pingfederate_administrative-accounts_apply
canonical_url: https://developer.pingidentity.com/pingcli/1.11/command_reference/pingcli_advanced-services_pingfederate_administrative-accounts_apply.html
llms_txt: https://developer.pingidentity.com/pingcli/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: October 15, 2026
section_ids:
  synopsis: Synopsis
  examples: Examples
  options: Options
  options-inherited-from-parent-commands: Options inherited from parent commands
  more-information: More information
---

# pingcli advanced-services pingfederate administrative-accounts apply

Create or update an administrative account

## Synopsis

Idempotently create or update a PingFederate administrative account looked up by the "username" field in the JSON body. If no account with the given username exists it is created; if it exists it is updated.

```
pingcli advanced-services pingfederate administrative-accounts apply [flags]
```

## Examples

```
  # Create or update an administrative account (body supplies username and other fields)
  pingcli advanced-services pingfederate administrative-accounts apply --from-file account.json

  # Read body from stdin
  pingcli advanced-services pingfederate administrative-accounts apply --from-file - < account.json

  # Create or update an administrative account with flags
  pingcli advanced-services pingfederate administrative-accounts apply --description "Support engineer" --active --from-file account.json
```

## Options

```
  -f, --from-file string       Path to a JSON file containing the request body, or "-" to read from stdin.
  -h, --help                   help for apply
  -i, --username string        The PingFederate administrative account username
      --active                 Whether the account is active
      --auditor                Whether the account is an auditor
      --department string      Department name of the account user
      --description string     Description of the account
      --email-address string   Email address associated with the account
      --phone-number string    Phone number associated with the account
      --roles []string         Administrator roles; repeatable or comma-separated
```

## Options inherited from parent commands

```
  -C, --config string           The relative or full path to a custom Ping CLI configuration file. (default $HOME/.pingcli/config.yaml)
  -D, --detailed-exitcode       Enable detailed exit code output. (default false) 0 - pingcli command succeeded with no errors or warnings. 1 - pingcli command failed with errors. 2 - pingcli command succeeded with warnings.
  -O, --output-format string    Specify the console output format. (default text) Options are: json, ndjson, ndjson-typed, ndjson-wrapped, text.
  -P, --profile string          The name of a configuration profile to use.
      --debug                   Enable debug output for error messages, including stack traces and transaction IDs. (default false)
      --log-file string         Write logs to a file at the given path. File logging is disabled when not set.
      --log-file-level string   Set the file log level. Options are: DEBUG, INFO, WARN, ERROR. (default DEBUG)
      --log-level string        Set the console log level. Options are: DEBUG, INFO, WARN, ERROR. (default WARN)
      --no-color                Disable text output in color. (default false)
      --query string            JMESPath expression to filter JSON output. Requires -O json, ndjson, ndjson-typed, or ndjson-wrapped. Example: --query 'data[?enabled].name'
```

## More information

* [pingcli advanced-services pingfederate administrative-accounts](pingcli_advanced-services_pingfederate_administrative-accounts.html) - PingFederate Administrative Accounts

---

---
title: pingcli advanced-services pingfederate administrative-accounts change-password
description: "Change the currently-authenticated administrative account's password"
component: pingcli
version: 1.11
page_id: pingcli:command_reference:pingcli_advanced-services_pingfederate_administrative-accounts_change-password
canonical_url: https://developer.pingidentity.com/pingcli/1.11/command_reference/pingcli_advanced-services_pingfederate_administrative-accounts_change-password.html
llms_txt: https://developer.pingidentity.com/pingcli/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: August 28, 2026
section_ids:
  synopsis: Synopsis
  examples: Examples
  options: Options
  options-inherited-from-parent-commands: Options inherited from parent commands
  more-information: More information
---

# pingcli advanced-services pingfederate administrative-accounts change-password

Change the currently-authenticated administrative account's password

## Synopsis

Change the password of the currently-authenticated PingFederate native administrative account (self-service; no --username, unlike reset-password). Supply --current-password/--new-password, --from-file (decoded as a UserCredentials JSON body), or both — flags override the file's values. At least one must effectively supply a non-empty new password.

```
pingcli advanced-services pingfederate administrative-accounts change-password [flags]
```

## Examples

```
  # Change the password of the currently-authenticated administrative account
  pingcli advanced-services pingfederate administrative-accounts change-password --current-password <current-password> --new-password <new-password>

  # Change the password from a JSON file
  pingcli advanced-services pingfederate administrative-accounts change-password --from-file password.json
```

## Options

```
  -f, --from-file string          Path to a JSON file containing a UserCredentials body ("currentPassword" and "newPassword" keys) for the change-password request, or "-" to read from stdin. --current-password/--new-password override the file's values if supplied.
  -h, --help                      help for change-password
      --current-password string   The current password for the currently-authenticated PingFederate administrative account
      --new-password string       The new password for the PingFederate administrative account
```

## Options inherited from parent commands

```
  -C, --config string           The relative or full path to a custom Ping CLI configuration file. (default $HOME/.pingcli/config.yaml)
  -D, --detailed-exitcode       Enable detailed exit code output. (default false) 0 - pingcli command succeeded with no errors or warnings. 1 - pingcli command failed with errors. 2 - pingcli command succeeded with warnings.
  -O, --output-format string    Specify the console output format. (default text) Options are: json, ndjson, ndjson-typed, ndjson-wrapped, text.
  -P, --profile string          The name of a configuration profile to use.
      --debug                   Enable debug output for error messages, including stack traces and transaction IDs. (default false)
      --log-file string         Write logs to a file at the given path. File logging is disabled when not set.
      --log-file-level string   Set the file log level. Options are: DEBUG, INFO, WARN, ERROR. (default DEBUG)
      --log-level string        Set the console log level. Options are: DEBUG, INFO, WARN, ERROR. (default WARN)
      --no-color                Disable text output in color. (default false)
      --query string            JMESPath expression to filter JSON output. Requires -O json, ndjson, ndjson-typed, or ndjson-wrapped. Example: --query 'data[?enabled].name'
```

## More information

* [pingcli advanced-services pingfederate administrative-accounts](pingcli_advanced-services_pingfederate_administrative-accounts.html) - PingFederate Administrative Accounts

---

---
title: pingcli advanced-services pingfederate administrative-accounts create
description: Create a new administrative account
component: pingcli
version: 1.11
page_id: pingcli:command_reference:pingcli_advanced-services_pingfederate_administrative-accounts_create
canonical_url: https://developer.pingidentity.com/pingcli/1.11/command_reference/pingcli_advanced-services_pingfederate_administrative-accounts_create.html
llms_txt: https://developer.pingidentity.com/pingcli/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: October 15, 2026
section_ids:
  synopsis: Synopsis
  examples: Examples
  options: Options
  options-inherited-from-parent-commands: Options inherited from parent commands
  more-information: More information
---

# pingcli advanced-services pingfederate administrative-accounts create

Create a new administrative account

## Synopsis

Create a new PingFederate administrative account

```
pingcli advanced-services pingfederate administrative-accounts create [flags]
```

## Examples

```
  # Create a new administrative account from a JSON file
  pingcli advanced-services pingfederate administrative-accounts create --from-file account.json

  # Create a new administrative account from stdin
  pingcli advanced-services pingfederate administrative-accounts create --from-file - < account.json

  # Create a new administrative account, overriding scalar fields with flags
  pingcli advanced-services pingfederate administrative-accounts create --username jdoe --description "Support engineer" --active --roles ADMINISTRATOR,CRYPTO_ADMINISTRATOR --from-file password.json
```

## Options

```
  -f, --from-file string       Path to a JSON file containing the request body, or "-" to read from stdin.
  -h, --help                   help for create
  -i, --username string        The PingFederate administrative account username
      --active                 Whether the account is active
      --auditor                Whether the account is an auditor
      --department string      Department name of the account user
      --description string     Description of the account
      --email-address string   Email address associated with the account
      --phone-number string    Phone number associated with the account
      --roles []string         Administrator roles; repeatable or comma-separated
```

## Options inherited from parent commands

```
  -C, --config string           The relative or full path to a custom Ping CLI configuration file. (default $HOME/.pingcli/config.yaml)
  -D, --detailed-exitcode       Enable detailed exit code output. (default false) 0 - pingcli command succeeded with no errors or warnings. 1 - pingcli command failed with errors. 2 - pingcli command succeeded with warnings.
  -O, --output-format string    Specify the console output format. (default text) Options are: json, ndjson, ndjson-typed, ndjson-wrapped, text.
  -P, --profile string          The name of a configuration profile to use.
      --debug                   Enable debug output for error messages, including stack traces and transaction IDs. (default false)
      --log-file string         Write logs to a file at the given path. File logging is disabled when not set.
      --log-file-level string   Set the file log level. Options are: DEBUG, INFO, WARN, ERROR. (default DEBUG)
      --log-level string        Set the console log level. Options are: DEBUG, INFO, WARN, ERROR. (default WARN)
      --no-color                Disable text output in color. (default false)
      --query string            JMESPath expression to filter JSON output. Requires -O json, ndjson, ndjson-typed, or ndjson-wrapped. Example: --query 'data[?enabled].name'
```

## More information

* [pingcli advanced-services pingfederate administrative-accounts](pingcli_advanced-services_pingfederate_administrative-accounts.html) - PingFederate Administrative Accounts

---

---
title: pingcli advanced-services pingfederate administrative-accounts delete
description: Delete an administrative account
component: pingcli
version: 1.11
page_id: pingcli:command_reference:pingcli_advanced-services_pingfederate_administrative-accounts_delete
canonical_url: https://developer.pingidentity.com/pingcli/1.11/command_reference/pingcli_advanced-services_pingfederate_administrative-accounts_delete.html
llms_txt: https://developer.pingidentity.com/pingcli/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: October 15, 2026
section_ids:
  synopsis: Synopsis
  examples: Examples
  options: Options
  options-inherited-from-parent-commands: Options inherited from parent commands
  more-information: More information
---

# pingcli advanced-services pingfederate administrative-accounts delete

Delete an administrative account

## Synopsis

Delete a PingFederate administrative account

```
pingcli advanced-services pingfederate administrative-accounts delete [flags]
```

## Examples

```
  # Delete an administrative account
  pingcli advanced-services pingfederate administrative-accounts delete --username <username>
```

## Options

```
  -i, --username string   The PingFederate administrative account username
  -h, --help              help for delete
```

## Options inherited from parent commands

```
  -C, --config string           The relative or full path to a custom Ping CLI configuration file. (default $HOME/.pingcli/config.yaml)
  -D, --detailed-exitcode       Enable detailed exit code output. (default false) 0 - pingcli command succeeded with no errors or warnings. 1 - pingcli command failed with errors. 2 - pingcli command succeeded with warnings.
  -O, --output-format string    Specify the console output format. (default text) Options are: json, ndjson, ndjson-typed, ndjson-wrapped, text.
  -P, --profile string          The name of a configuration profile to use.
      --debug                   Enable debug output for error messages, including stack traces and transaction IDs. (default false)
      --log-file string         Write logs to a file at the given path. File logging is disabled when not set.
      --log-file-level string   Set the file log level. Options are: DEBUG, INFO, WARN, ERROR. (default DEBUG)
      --log-level string        Set the console log level. Options are: DEBUG, INFO, WARN, ERROR. (default WARN)
      --no-color                Disable text output in color. (default false)
      --query string            JMESPath expression to filter JSON output. Requires -O json, ndjson, ndjson-typed, or ndjson-wrapped. Example: --query 'data[?enabled].name'
```

## More information

* [pingcli advanced-services pingfederate administrative-accounts](pingcli_advanced-services_pingfederate_administrative-accounts.html) - PingFederate Administrative Accounts

---

---
title: pingcli advanced-services pingfederate administrative-accounts get
description: Read a specific administrative account
component: pingcli
version: 1.11
page_id: pingcli:command_reference:pingcli_advanced-services_pingfederate_administrative-accounts_get
canonical_url: https://developer.pingidentity.com/pingcli/1.11/command_reference/pingcli_advanced-services_pingfederate_administrative-accounts_get.html
llms_txt: https://developer.pingidentity.com/pingcli/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: October 15, 2026
section_ids:
  synopsis: Synopsis
  examples: Examples
  options: Options
  options-inherited-from-parent-commands: Options inherited from parent commands
  more-information: More information
---

# pingcli advanced-services pingfederate administrative-accounts get

Read a specific administrative account

## Synopsis

Read a specific PingFederate administrative account

```
pingcli advanced-services pingfederate administrative-accounts get [flags]
```

## Examples

```
  # Read a specific administrative account
  pingcli advanced-services pingfederate administrative-accounts get --username <username>
```

## Options

```
  -i, --username string   The PingFederate administrative account username
  -h, --help              help for get
```

## Options inherited from parent commands

```
  -C, --config string           The relative or full path to a custom Ping CLI configuration file. (default $HOME/.pingcli/config.yaml)
  -D, --detailed-exitcode       Enable detailed exit code output. (default false) 0 - pingcli command succeeded with no errors or warnings. 1 - pingcli command failed with errors. 2 - pingcli command succeeded with warnings.
  -O, --output-format string    Specify the console output format. (default text) Options are: json, ndjson, ndjson-typed, ndjson-wrapped, text.
  -P, --profile string          The name of a configuration profile to use.
      --debug                   Enable debug output for error messages, including stack traces and transaction IDs. (default false)
      --log-file string         Write logs to a file at the given path. File logging is disabled when not set.
      --log-file-level string   Set the file log level. Options are: DEBUG, INFO, WARN, ERROR. (default DEBUG)
      --log-level string        Set the console log level. Options are: DEBUG, INFO, WARN, ERROR. (default WARN)
      --no-color                Disable text output in color. (default false)
      --query string            JMESPath expression to filter JSON output. Requires -O json, ndjson, ndjson-typed, or ndjson-wrapped. Example: --query 'data[?enabled].name'
```

## More information

* [pingcli advanced-services pingfederate administrative-accounts](pingcli_advanced-services_pingfederate_administrative-accounts.html) - PingFederate Administrative Accounts

---

---
title: pingcli advanced-services pingfederate administrative-accounts list
description: List all administrative accounts
component: pingcli
version: 1.11
page_id: pingcli:command_reference:pingcli_advanced-services_pingfederate_administrative-accounts_list
canonical_url: https://developer.pingidentity.com/pingcli/1.11/command_reference/pingcli_advanced-services_pingfederate_administrative-accounts_list.html
llms_txt: https://developer.pingidentity.com/pingcli/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: August 14, 2026
section_ids:
  synopsis: Synopsis
  examples: Examples
  options-inherited-from-parent-commands: Options inherited from parent commands
  more-information: More information
---

# pingcli advanced-services pingfederate administrative-accounts list

List all administrative accounts

## Synopsis

List all PingFederate administrative accounts

```
pingcli advanced-services pingfederate administrative-accounts list [flags]
```

## Examples

```
  # List all PingFederate administrative accounts
  pingcli advanced-services pingfederate administrative-accounts list
```

## Options inherited from parent commands

```
  -C, --config string           The relative or full path to a custom Ping CLI configuration file. (default $HOME/.pingcli/config.yaml)
  -D, --detailed-exitcode       Enable detailed exit code output. (default false) 0 - pingcli command succeeded with no errors or warnings. 1 - pingcli command failed with errors. 2 - pingcli command succeeded with warnings.
  -O, --output-format string    Specify the console output format. (default text) Options are: json, ndjson, ndjson-typed, ndjson-wrapped, text.
  -P, --profile string          The name of a configuration profile to use.
      --debug                   Enable debug output for error messages, including stack traces and transaction IDs. (default false)
      --log-file string         Write logs to a file at the given path. File logging is disabled when not set.
      --log-file-level string   Set the file log level. Options are: DEBUG, INFO, WARN, ERROR. (default DEBUG)
      --log-level string        Set the console log level. Options are: DEBUG, INFO, WARN, ERROR. (default WARN)
      --no-color                Disable text output in color. (default false)
      --query string            JMESPath expression to filter JSON output. Requires -O json, ndjson, ndjson-typed, or ndjson-wrapped. Example: --query 'data[?enabled].name'
```

## More information

* [pingcli advanced-services pingfederate administrative-accounts](pingcli_advanced-services_pingfederate_administrative-accounts.html) - PingFederate Administrative Accounts

---

---
title: pingcli advanced-services pingfederate administrative-accounts replace
description: Update an administrative account
component: pingcli
version: 1.11
page_id: pingcli:command_reference:pingcli_advanced-services_pingfederate_administrative-accounts_replace
canonical_url: https://developer.pingidentity.com/pingcli/1.11/command_reference/pingcli_advanced-services_pingfederate_administrative-accounts_replace.html
llms_txt: https://developer.pingidentity.com/pingcli/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: October 15, 2026
section_ids:
  synopsis: Synopsis
  examples: Examples
  options: Options
  options-inherited-from-parent-commands: Options inherited from parent commands
  more-information: More information
---

# pingcli advanced-services pingfederate administrative-accounts replace

Update an administrative account

## Synopsis

Update (replace) a PingFederate administrative account

```
pingcli advanced-services pingfederate administrative-accounts replace [flags]
```

## Examples

```
  # Update an administrative account from a JSON file (--username is still required)
  pingcli advanced-services pingfederate administrative-accounts replace --username <username> --from-file account.json

  # Update an administrative account from stdin
  pingcli advanced-services pingfederate administrative-accounts replace --username <username> --from-file - < account.json

  # Update an administrative account, overriding scalar fields with flags
  pingcli advanced-services pingfederate administrative-accounts replace --username <username> --description "updated" --active --department Support --from-file account.json
```

## Options

```
  -f, --from-file string       Path to a JSON file containing the request body, or "-" to read from stdin.
  -h, --help                   help for replace
  -i, --username string        The PingFederate administrative account username
      --active                 Whether the account is active
      --auditor                Whether the account is an auditor
      --department string      Department name of the account user
      --description string     Description of the account
      --email-address string   Email address associated with the account
      --phone-number string    Phone number associated with the account
      --roles []string         Administrator roles; repeatable or comma-separated
```

## Options inherited from parent commands

```
  -C, --config string           The relative or full path to a custom Ping CLI configuration file. (default $HOME/.pingcli/config.yaml)
  -D, --detailed-exitcode       Enable detailed exit code output. (default false) 0 - pingcli command succeeded with no errors or warnings. 1 - pingcli command failed with errors. 2 - pingcli command succeeded with warnings.
  -O, --output-format string    Specify the console output format. (default text) Options are: json, ndjson, ndjson-typed, ndjson-wrapped, text.
  -P, --profile string          The name of a configuration profile to use.
      --debug                   Enable debug output for error messages, including stack traces and transaction IDs. (default false)
      --log-file string         Write logs to a file at the given path. File logging is disabled when not set.
      --log-file-level string   Set the file log level. Options are: DEBUG, INFO, WARN, ERROR. (default DEBUG)
      --log-level string        Set the console log level. Options are: DEBUG, INFO, WARN, ERROR. (default WARN)
      --no-color                Disable text output in color. (default false)
      --query string            JMESPath expression to filter JSON output. Requires -O json, ndjson, ndjson-typed, or ndjson-wrapped. Example: --query 'data[?enabled].name'
```

## More information

* [pingcli advanced-services pingfederate administrative-accounts](pingcli_advanced-services_pingfederate_administrative-accounts.html) - PingFederate Administrative Accounts

---

---
title: pingcli advanced-services pingfederate administrative-accounts reset-password
description: Reset a PingFederate administrative account password
component: pingcli
version: 1.11
page_id: pingcli:command_reference:pingcli_advanced-services_pingfederate_administrative-accounts_reset-password
canonical_url: https://developer.pingidentity.com/pingcli/1.11/command_reference/pingcli_advanced-services_pingfederate_administrative-accounts_reset-password.html
llms_txt: https://developer.pingidentity.com/pingcli/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: October 15, 2026
section_ids:
  synopsis: Synopsis
  examples: Examples
  options: Options
  options-inherited-from-parent-commands: Options inherited from parent commands
  more-information: More information
---

# pingcli advanced-services pingfederate administrative-accounts reset-password

Reset a PingFederate administrative account password

## Synopsis

Reset the password for a PingFederate administrative account. Supply the new password via --new-password, --from-file (decoded as a UserCredentials JSON body; only "newPassword" is read), or both — --new-password overrides the file's value. At least one must effectively supply a non-empty new password.

```
pingcli advanced-services pingfederate administrative-accounts reset-password [flags]
```

## Examples

```
  # Reset password for an administrative account
  pingcli advanced-services pingfederate administrative-accounts reset-password --username <username> --new-password <new-password>

  # Reset password for an administrative account from a JSON file
  pingcli advanced-services pingfederate administrative-accounts reset-password --username <username> --from-file password.json
```

## Options

```
  -f, --from-file string      Path to a JSON file containing a UserCredentials body (the "newPassword" key is used; "currentPassword" is ignored) for the reset-password request, or "-" to read from stdin. --new-password overrides the file's newPassword if both are supplied.
  -h, --help                  help for reset-password
  -i, --username string       The PingFederate administrative account username
      --new-password string   The new password for the PingFederate administrative account
```

## Options inherited from parent commands

```
  -C, --config string           The relative or full path to a custom Ping CLI configuration file. (default $HOME/.pingcli/config.yaml)
  -D, --detailed-exitcode       Enable detailed exit code output. (default false) 0 - pingcli command succeeded with no errors or warnings. 1 - pingcli command failed with errors. 2 - pingcli command succeeded with warnings.
  -O, --output-format string    Specify the console output format. (default text) Options are: json, ndjson, ndjson-typed, ndjson-wrapped, text.
  -P, --profile string          The name of a configuration profile to use.
      --debug                   Enable debug output for error messages, including stack traces and transaction IDs. (default false)
      --log-file string         Write logs to a file at the given path. File logging is disabled when not set.
      --log-file-level string   Set the file log level. Options are: DEBUG, INFO, WARN, ERROR. (default DEBUG)
      --log-level string        Set the console log level. Options are: DEBUG, INFO, WARN, ERROR. (default WARN)
      --no-color                Disable text output in color. (default false)
      --query string            JMESPath expression to filter JSON output. Requires -O json, ndjson, ndjson-typed, or ndjson-wrapped. Example: --query 'data[?enabled].name'
```

## More information

* [pingcli advanced-services pingfederate administrative-accounts](pingcli_advanced-services_pingfederate_administrative-accounts.html) - PingFederate Administrative Accounts

---

---
title: pingcli advanced-services pingfederate administrative-accounts template
description: Generate an administrative account JSON template
component: pingcli
version: 1.11
page_id: pingcli:command_reference:pingcli_advanced-services_pingfederate_administrative-accounts_template
canonical_url: https://developer.pingidentity.com/pingcli/1.11/command_reference/pingcli_advanced-services_pingfederate_administrative-accounts_template.html
llms_txt: https://developer.pingidentity.com/pingcli/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: August 14, 2026
section_ids:
  synopsis: Synopsis
  examples: Examples
  options: Options
  options-inherited-from-parent-commands: Options inherited from parent commands
  more-information: More information
---

# pingcli advanced-services pingfederate administrative-accounts template

Generate an administrative account JSON template

## Synopsis

Generate a JSON skeleton template for administrative account create or replace bodies

```
pingcli advanced-services pingfederate administrative-accounts template [flags]
```

## Examples

```
  # Generate a template and save to a file
  pingcli advanced-services pingfederate administrative-accounts template > body.json

  # Edit the template, then create the administrative account
  pingcli advanced-services pingfederate administrative-accounts create --from-file body.json
Use the JSON template as a starting point:
  1. Run the template command to generate the body skeleton.
  2. Edit the file, replacing placeholder values with real data.
  3. Feed the edited file back to the create or replace action via --from-file.

Example workflow:
  pingcli advanced-services pingfederate administrative-accounts template > body.json
  # edit body.json
  pingcli advanced-services pingfederate administrative-accounts create --from-file body.json
```

## Options

```
  -o, --output-file string   Write the JSON template to PATH instead of stdout. Overwrites any existing file.
  -h, --help                 help for template
```

## Options inherited from parent commands

```
  -C, --config string           The relative or full path to a custom Ping CLI configuration file. (default $HOME/.pingcli/config.yaml)
  -D, --detailed-exitcode       Enable detailed exit code output. (default false) 0 - pingcli command succeeded with no errors or warnings. 1 - pingcli command failed with errors. 2 - pingcli command succeeded with warnings.
  -O, --output-format string    Specify the console output format. (default text) Options are: json, ndjson, ndjson-typed, ndjson-wrapped, text.
  -P, --profile string          The name of a configuration profile to use.
      --debug                   Enable debug output for error messages, including stack traces and transaction IDs. (default false)
      --log-file string         Write logs to a file at the given path. File logging is disabled when not set.
      --log-file-level string   Set the file log level. Options are: DEBUG, INFO, WARN, ERROR. (default DEBUG)
      --log-level string        Set the console log level. Options are: DEBUG, INFO, WARN, ERROR. (default WARN)
      --no-color                Disable text output in color. (default false)
      --query string            JMESPath expression to filter JSON output. Requires -O json, ndjson, ndjson-typed, or ndjson-wrapped. Example: --query 'data[?enabled].name'
```

## More information

* [pingcli advanced-services pingfederate administrative-accounts](pingcli_advanced-services_pingfederate_administrative-accounts.html) - PingFederate Administrative Accounts

---

---
title: pingcli advanced-services pingfederate administrative-api
description: Manage PingFederate Administrative API resources
component: pingcli
version: 1.11
page_id: pingcli:command_reference:pingcli_advanced-services_pingfederate_administrative-api
canonical_url: https://developer.pingidentity.com/pingcli/1.11/command_reference/pingcli_advanced-services_pingfederate_administrative-api.html
llms_txt: https://developer.pingidentity.com/pingcli/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: August 14, 2026
section_ids:
  synopsis: Synopsis
  options-inherited-from-parent-commands: Options inherited from parent commands
  more-information: More information
  subcommands: Subcommands
---

# pingcli advanced-services pingfederate administrative-api

Manage PingFederate Administrative API resources

## Synopsis

Manage PingFederate Administrative API resources

```
pingcli advanced-services pingfederate administrative-api
```

## Options inherited from parent commands

```
  -C, --config string           The relative or full path to a custom Ping CLI configuration file. (default $HOME/.pingcli/config.yaml)
  -D, --detailed-exitcode       Enable detailed exit code output. (default false) 0 - pingcli command succeeded with no errors or warnings. 1 - pingcli command failed with errors. 2 - pingcli command succeeded with warnings.
  -O, --output-format string    Specify the console output format. (default text) Options are: json, ndjson, ndjson-typed, ndjson-wrapped, text.
  -P, --profile string          The name of a configuration profile to use.
      --debug                   Enable debug output for error messages, including stack traces and transaction IDs. (default false)
      --log-file string         Write logs to a file at the given path. File logging is disabled when not set.
      --log-file-level string   Set the file log level. Options are: DEBUG, INFO, WARN, ERROR. (default DEBUG)
      --log-level string        Set the console log level. Options are: DEBUG, INFO, WARN, ERROR. (default WARN)
      --no-color                Disable text output in color. (default false)
      --query string            JMESPath expression to filter JSON output. Requires -O json, ndjson, ndjson-typed, or ndjson-wrapped. Example: --query 'data[?enabled].name'
```

## More information

* [pingcli advanced-services pingfederate](pingcli_advanced-services_pingfederate.html) - Administration tools for PingFederate deployed as a private tenant service in PingOne Advanced Services

## Subcommands

* [pingcli advanced-services pingfederate administrative-api cors-settings](pingcli_advanced-services_pingfederate_administrative-api_cors-settings.html) - PingFederate Administrative API CORS Settings

---

---
title: pingcli advanced-services pingfederate administrative-api cors-settings
description: PingFederate Administrative API CORS Settings
component: pingcli
version: 1.11
page_id: pingcli:command_reference:pingcli_advanced-services_pingfederate_administrative-api_cors-settings
canonical_url: https://developer.pingidentity.com/pingcli/1.11/command_reference/pingcli_advanced-services_pingfederate_administrative-api_cors-settings.html
llms_txt: https://developer.pingidentity.com/pingcli/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: August 14, 2026
section_ids:
  synopsis: Synopsis
  options-inherited-from-parent-commands: Options inherited from parent commands
  more-information: More information
  subcommands: Subcommands
---

# pingcli advanced-services pingfederate administrative-api cors-settings

PingFederate Administrative API CORS Settings

## Synopsis

PingFederate Administrative API CORS Settings

```
pingcli advanced-services pingfederate administrative-api cors-settings [flags]
```

## Options inherited from parent commands

```
  -C, --config string           The relative or full path to a custom Ping CLI configuration file. (default $HOME/.pingcli/config.yaml)
  -D, --detailed-exitcode       Enable detailed exit code output. (default false) 0 - pingcli command succeeded with no errors or warnings. 1 - pingcli command failed with errors. 2 - pingcli command succeeded with warnings.
  -O, --output-format string    Specify the console output format. (default text) Options are: json, ndjson, ndjson-typed, ndjson-wrapped, text.
  -P, --profile string          The name of a configuration profile to use.
      --debug                   Enable debug output for error messages, including stack traces and transaction IDs. (default false)
      --log-file string         Write logs to a file at the given path. File logging is disabled when not set.
      --log-file-level string   Set the file log level. Options are: DEBUG, INFO, WARN, ERROR. (default DEBUG)
      --log-level string        Set the console log level. Options are: DEBUG, INFO, WARN, ERROR. (default WARN)
      --no-color                Disable text output in color. (default false)
      --query string            JMESPath expression to filter JSON output. Requires -O json, ndjson, ndjson-typed, or ndjson-wrapped. Example: --query 'data[?enabled].name'
```

## More information

* [pingcli advanced-services pingfederate administrative-api](pingcli_advanced-services_pingfederate_administrative-api.html) - Manage PingFederate Administrative API resources

## Subcommands

* [pingcli advanced-services pingfederate administrative-api cors-settings apply](pingcli_advanced-services_pingfederate_administrative-api_cors-settings_apply.html) - Update administrative API CORS settings

* [pingcli advanced-services pingfederate administrative-api cors-settings get](pingcli_advanced-services_pingfederate_administrative-api_cors-settings_get.html) - Read administrative API CORS settings

* [pingcli advanced-services pingfederate administrative-api cors-settings replace](pingcli_advanced-services_pingfederate_administrative-api_cors-settings_replace.html) - Update administrative API CORS settings

* [pingcli advanced-services pingfederate administrative-api cors-settings template](pingcli_advanced-services_pingfederate_administrative-api_cors-settings_template.html) - Generate an administrative API CORS settings JSON template

---

---
title: pingcli advanced-services pingfederate administrative-api cors-settings apply
description: Update administrative API CORS settings
component: pingcli
version: 1.11
page_id: pingcli:command_reference:pingcli_advanced-services_pingfederate_administrative-api_cors-settings_apply
canonical_url: https://developer.pingidentity.com/pingcli/1.11/command_reference/pingcli_advanced-services_pingfederate_administrative-api_cors-settings_apply.html
llms_txt: https://developer.pingidentity.com/pingcli/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: August 14, 2026
section_ids:
  synopsis: Synopsis
  examples: Examples
  options: Options
  options-inherited-from-parent-commands: Options inherited from parent commands
  more-information: More information
---

# pingcli advanced-services pingfederate administrative-api cors-settings apply

Update administrative API CORS settings

## Synopsis

Idempotently update the PingFederate Administrative API CORS Settings. Apply is an alias for replace on this singleton resource.

```
pingcli advanced-services pingfederate administrative-api cors-settings apply [flags]
```

## Examples

```
  # Update administrative API CORS settings from a JSON file
  pingcli advanced-services pingfederate administrative-api cors-settings apply --from-file settings.json

  # Update administrative API CORS settings from stdin
  pingcli advanced-services pingfederate administrative-api cors-settings apply --from-file - < settings.json

  # Update administrative API CORS settings from flags, without --from-file
  pingcli advanced-services pingfederate administrative-api cors-settings apply --enabled --allowed-origins-list https://example.com,https://example.org
```

## Options

```
  -f, --from-file string                Path to a JSON file containing the request body, or "-" to read from stdin.
  -h, --help                            help for apply
      --allowed-origins-list []string   List of allowed CORS origins; repeatable or comma-separated
      --enabled                         Whether cross-origin resource sharing (CORS) is enabled for the Administrative API
```

## Options inherited from parent commands

```
  -C, --config string           The relative or full path to a custom Ping CLI configuration file. (default $HOME/.pingcli/config.yaml)
  -D, --detailed-exitcode       Enable detailed exit code output. (default false) 0 - pingcli command succeeded with no errors or warnings. 1 - pingcli command failed with errors. 2 - pingcli command succeeded with warnings.
  -O, --output-format string    Specify the console output format. (default text) Options are: json, ndjson, ndjson-typed, ndjson-wrapped, text.
  -P, --profile string          The name of a configuration profile to use.
      --debug                   Enable debug output for error messages, including stack traces and transaction IDs. (default false)
      --log-file string         Write logs to a file at the given path. File logging is disabled when not set.
      --log-file-level string   Set the file log level. Options are: DEBUG, INFO, WARN, ERROR. (default DEBUG)
      --log-level string        Set the console log level. Options are: DEBUG, INFO, WARN, ERROR. (default WARN)
      --no-color                Disable text output in color. (default false)
      --query string            JMESPath expression to filter JSON output. Requires -O json, ndjson, ndjson-typed, or ndjson-wrapped. Example: --query 'data[?enabled].name'
```

## More information

* [pingcli advanced-services pingfederate administrative-api cors-settings](pingcli_advanced-services_pingfederate_administrative-api_cors-settings.html) - PingFederate Administrative API CORS Settings

---

---
title: pingcli advanced-services pingfederate administrative-api cors-settings get
description: Read administrative API CORS settings
component: pingcli
version: 1.11
page_id: pingcli:command_reference:pingcli_advanced-services_pingfederate_administrative-api_cors-settings_get
canonical_url: https://developer.pingidentity.com/pingcli/1.11/command_reference/pingcli_advanced-services_pingfederate_administrative-api_cors-settings_get.html
llms_txt: https://developer.pingidentity.com/pingcli/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: August 14, 2026
section_ids:
  synopsis: Synopsis
  examples: Examples
  options-inherited-from-parent-commands: Options inherited from parent commands
  more-information: More information
---

# pingcli advanced-services pingfederate administrative-api cors-settings get

Read administrative API CORS settings

## Synopsis

Read the PingFederate Administrative API CORS Settings singleton

```
pingcli advanced-services pingfederate administrative-api cors-settings get [flags]
```

## Examples

```
  # Read administrative API CORS settings
  pingcli advanced-services pingfederate administrative-api cors-settings get
```

## Options inherited from parent commands

```
  -C, --config string           The relative or full path to a custom Ping CLI configuration file. (default $HOME/.pingcli/config.yaml)
  -D, --detailed-exitcode       Enable detailed exit code output. (default false) 0 - pingcli command succeeded with no errors or warnings. 1 - pingcli command failed with errors. 2 - pingcli command succeeded with warnings.
  -O, --output-format string    Specify the console output format. (default text) Options are: json, ndjson, ndjson-typed, ndjson-wrapped, text.
  -P, --profile string          The name of a configuration profile to use.
      --debug                   Enable debug output for error messages, including stack traces and transaction IDs. (default false)
      --log-file string         Write logs to a file at the given path. File logging is disabled when not set.
      --log-file-level string   Set the file log level. Options are: DEBUG, INFO, WARN, ERROR. (default DEBUG)
      --log-level string        Set the console log level. Options are: DEBUG, INFO, WARN, ERROR. (default WARN)
      --no-color                Disable text output in color. (default false)
      --query string            JMESPath expression to filter JSON output. Requires -O json, ndjson, ndjson-typed, or ndjson-wrapped. Example: --query 'data[?enabled].name'
```

## More information

* [pingcli advanced-services pingfederate administrative-api cors-settings](pingcli_advanced-services_pingfederate_administrative-api_cors-settings.html) - PingFederate Administrative API CORS Settings

---

---
title: pingcli advanced-services pingfederate administrative-api cors-settings replace
description: Update administrative API CORS settings
component: pingcli
version: 1.11
page_id: pingcli:command_reference:pingcli_advanced-services_pingfederate_administrative-api_cors-settings_replace
canonical_url: https://developer.pingidentity.com/pingcli/1.11/command_reference/pingcli_advanced-services_pingfederate_administrative-api_cors-settings_replace.html
llms_txt: https://developer.pingidentity.com/pingcli/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: August 14, 2026
section_ids:
  synopsis: Synopsis
  examples: Examples
  options: Options
  options-inherited-from-parent-commands: Options inherited from parent commands
  more-information: More information
---

# pingcli advanced-services pingfederate administrative-api cors-settings replace

Update administrative API CORS settings

## Synopsis

Update (replace) the PingFederate Administrative API CORS Settings

```
pingcli advanced-services pingfederate administrative-api cors-settings replace [flags]
```

## Examples

```
  # Update administrative API CORS settings from a JSON file
  pingcli advanced-services pingfederate administrative-api cors-settings replace --from-file settings.json

  # Update administrative API CORS settings from stdin
  pingcli advanced-services pingfederate administrative-api cors-settings replace --from-file - < settings.json

  # Update administrative API CORS settings from flags, without --from-file
  pingcli advanced-services pingfederate administrative-api cors-settings replace --enabled --allowed-origins-list https://example.com,https://example.org
```

## Options

```
  -f, --from-file string                Path to a JSON file containing the request body, or "-" to read from stdin.
  -h, --help                            help for replace
      --allowed-origins-list []string   List of allowed CORS origins; repeatable or comma-separated
      --enabled                         Whether cross-origin resource sharing (CORS) is enabled for the Administrative API
```

## Options inherited from parent commands

```
  -C, --config string           The relative or full path to a custom Ping CLI configuration file. (default $HOME/.pingcli/config.yaml)
  -D, --detailed-exitcode       Enable detailed exit code output. (default false) 0 - pingcli command succeeded with no errors or warnings. 1 - pingcli command failed with errors. 2 - pingcli command succeeded with warnings.
  -O, --output-format string    Specify the console output format. (default text) Options are: json, ndjson, ndjson-typed, ndjson-wrapped, text.
  -P, --profile string          The name of a configuration profile to use.
      --debug                   Enable debug output for error messages, including stack traces and transaction IDs. (default false)
      --log-file string         Write logs to a file at the given path. File logging is disabled when not set.
      --log-file-level string   Set the file log level. Options are: DEBUG, INFO, WARN, ERROR. (default DEBUG)
      --log-level string        Set the console log level. Options are: DEBUG, INFO, WARN, ERROR. (default WARN)
      --no-color                Disable text output in color. (default false)
      --query string            JMESPath expression to filter JSON output. Requires -O json, ndjson, ndjson-typed, or ndjson-wrapped. Example: --query 'data[?enabled].name'
```

## More information

* [pingcli advanced-services pingfederate administrative-api cors-settings](pingcli_advanced-services_pingfederate_administrative-api_cors-settings.html) - PingFederate Administrative API CORS Settings

---

---
title: pingcli advanced-services pingfederate administrative-api cors-settings template
description: Generate an administrative API CORS settings JSON template
component: pingcli
version: 1.11
page_id: pingcli:command_reference:pingcli_advanced-services_pingfederate_administrative-api_cors-settings_template
canonical_url: https://developer.pingidentity.com/pingcli/1.11/command_reference/pingcli_advanced-services_pingfederate_administrative-api_cors-settings_template.html
llms_txt: https://developer.pingidentity.com/pingcli/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: August 14, 2026
section_ids:
  synopsis: Synopsis
  examples: Examples
  options: Options
  options-inherited-from-parent-commands: Options inherited from parent commands
  more-information: More information
---

# pingcli advanced-services pingfederate administrative-api cors-settings template

Generate an administrative API CORS settings JSON template

## Synopsis

Generate a JSON skeleton template for administrative API CORS settings replace bodies

```
pingcli advanced-services pingfederate administrative-api cors-settings template [flags]
```

## Examples

```
  # Generate a template and save to a file
  pingcli advanced-services pingfederate administrative-api cors-settings template > body.json

  # Edit the template, then update the administrative API CORS settings
  pingcli advanced-services pingfederate administrative-api cors-settings replace --from-file body.json
Use the JSON template as a starting point:
  1. Run the template command to generate the body skeleton.
  2. Edit the file, replacing placeholder values with real data.
  3. Feed the edited file back to the replace action via --from-file.

Example workflow:
  pingcli advanced-services pingfederate administrative-api cors-settings template > body.json
  # edit body.json
  pingcli advanced-services pingfederate administrative-api cors-settings replace --from-file body.json
```

## Options

```
  -o, --output-file string   Write the JSON template to PATH instead of stdout. Overwrites any existing file.
  -h, --help                 help for template
```

## Options inherited from parent commands

```
  -C, --config string           The relative or full path to a custom Ping CLI configuration file. (default $HOME/.pingcli/config.yaml)
  -D, --detailed-exitcode       Enable detailed exit code output. (default false) 0 - pingcli command succeeded with no errors or warnings. 1 - pingcli command failed with errors. 2 - pingcli command succeeded with warnings.
  -O, --output-format string    Specify the console output format. (default text) Options are: json, ndjson, ndjson-typed, ndjson-wrapped, text.
  -P, --profile string          The name of a configuration profile to use.
      --debug                   Enable debug output for error messages, including stack traces and transaction IDs. (default false)
      --log-file string         Write logs to a file at the given path. File logging is disabled when not set.
      --log-file-level string   Set the file log level. Options are: DEBUG, INFO, WARN, ERROR. (default DEBUG)
      --log-level string        Set the console log level. Options are: DEBUG, INFO, WARN, ERROR. (default WARN)
      --no-color                Disable text output in color. (default false)
      --query string            JMESPath expression to filter JSON output. Requires -O json, ndjson, ndjson-typed, or ndjson-wrapped. Example: --query 'data[?enabled].name'
```

## More information

* [pingcli advanced-services pingfederate administrative-api cors-settings](pingcli_advanced-services_pingfederate_administrative-api_cors-settings.html) - PingFederate Administrative API CORS Settings

---

---
title: pingcli advanced-services pingfederate api
description: Send a custom REST API request to the management API of PingFederate (Advanced Services).
component: pingcli
version: 1.11
page_id: pingcli:command_reference:pingcli_advanced-services_pingfederate_api
canonical_url: https://developer.pingidentity.com/pingcli/1.11/command_reference/pingcli_advanced-services_pingfederate_api.html
llms_txt: https://developer.pingidentity.com/pingcli/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: August 14, 2026
section_ids:
  synopsis: Synopsis
  examples: Examples
  options: Options
  options-inherited-from-parent-commands: Options inherited from parent commands
  more-information: More information
---

# pingcli advanced-services pingfederate api

Send a custom REST API request to the management API of PingFederate (Advanced Services).

## Synopsis

Send a custom REST API request to the management API of PingFederate (Advanced Services)

The custom REST API request is most powerful when product connection details have been configured in the CLI configuration file.

The command offers a cURL-like experience to interact with the Ping products and services, with authentication and environment details dynamically filled by the CLI.

```
pingcli advanced-services pingfederate api [flags] API_URI
```

## Examples

```
    Send a custom API request to the configured PingFederate (Advanced Services) server, making a GET request against the /serverSettings endpoint.
    pingcli advanced-services pingfederate api serverSettings

  Send a custom API request to the configured PingFederate (Advanced Services) server, making a GET request to retrieve JSON configuration for authentication policies.
    pingcli advanced-services pingfederate api --http-method GET --output-format json authenticationPolicies/default

  Send a custom API request to the configured PingFederate (Advanced Services) server, making a POST request to create a new data store with JSON data sourced from a file.
    pingcli advanced-services pingfederate api --http-method POST --data ./my-data-store.json dataStores

  Send a custom API request to the configured PingFederate (Advanced Services) server, making a PUT request using raw JSON data.
    pingcli advanced-services pingfederate api --http-method PUT --data-raw '{"name": "My data store"}' dataStores/my-data-store-id

  Send a custom API request to the configured PingFederate (Advanced Services) server, making a DELETE request to remove a data store.
    pingcli advanced-services pingfederate api --http-method DELETE dataStores/my-data-store-id
```

## Options

```
  -f, --fail                                                  Return non-zero exit code when HTTP custom API request returns a failure status code.
  -h, --help                                                  help for api
  -m, --http-method string                                    The HTTP method to use for the request. (default GET) Options are: DELETE, GET, PATCH, POST, PUT. Example: 'POST'
  -r, --header []string                                       A custom header to send in the request. Example: --header "Content-Type: application/vnd.pingidentity.user.import+json"
      --as-pingfederate-admin-api-path string                 The PingFederate admin API URL path for the Advanced Services private tenant. (default /pf-admin-api/v1)
      --as-pingfederate-ca-certificate-pem-files []string     Relative or full paths to PEM-encoded certificate files for the Advanced Services PingFederate server. (default []) Accepts a comma-separated string to delimit multiple PEM files.
      --as-pingfederate-https-host string                     The PingFederate HTTPS host for the Advanced Services private tenant. Example: 'https://pingfederate-admin.bxretail.org'
      --as-pingfederate-insecure-trust-all-tls                Trust any certificate when connecting to the PingFederate Advanced Services admin API. (default false) This is insecure and shouldn't be enabled outside of testing.
      --as-pingfederate-software-version string               The PingFederate software version for the Advanced Services private tenant. (default 13.0)
      --as-pingfederate-x-bypass-external-validation-header   Bypass connection tests when configuring PingFederate in Advanced Services (the X-BypassExternalValidation header). (default false)
      --data string                                           The file containing data to send in the request.  Example: './data.json'
      --data-raw string                                       The raw data to send in the request.  Example: '{"name": "My environment"}'
```

## Options inherited from parent commands

```
  -C, --config string           The relative or full path to a custom Ping CLI configuration file. (default $HOME/.pingcli/config.yaml)
  -D, --detailed-exitcode       Enable detailed exit code output. (default false) 0 - pingcli command succeeded with no errors or warnings. 1 - pingcli command failed with errors. 2 - pingcli command succeeded with warnings.
  -O, --output-format string    Specify the console output format. (default text) Options are: json, ndjson, ndjson-typed, ndjson-wrapped, text.
  -P, --profile string          The name of a configuration profile to use.
      --debug                   Enable debug output for error messages, including stack traces and transaction IDs. (default false)
      --log-file string         Write logs to a file at the given path. File logging is disabled when not set.
      --log-file-level string   Set the file log level. Options are: DEBUG, INFO, WARN, ERROR. (default DEBUG)
      --log-level string        Set the console log level. Options are: DEBUG, INFO, WARN, ERROR. (default WARN)
      --no-color                Disable text output in color. (default false)
      --query string            JMESPath expression to filter JSON output. Requires -O json, ndjson, ndjson-typed, or ndjson-wrapped. Example: --query 'data[?enabled].name'
```

## More information

* [pingcli advanced-services pingfederate](pingcli_advanced-services_pingfederate.html) - Administration tools for PingFederate deployed as a private tenant service in PingOne Advanced Services