---
title: Agent Skills
description: Agent Skills are structured reference files that give coding agents targeted knowledge of Ping CLI commands and capabilities. Installing an Agent Skill means your agent can reason about the CLI directly, understanding available commands, flags, and service connectors without having to discover them through --help output at runtime.
component: pingcli
version: 1.11
page_id: pingcli:using_pingcli:agent-skills
canonical_url: https://developer.pingidentity.com/pingcli/1.11/using_pingcli/agent-skills.html
llms_txt: https://developer.pingidentity.com/pingcli/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 5, 2026
section_ids:
  what-agent-skills-provide: What Agent Skills provide
  discovering-available-agent-skills: Discovering available Agent Skills
  installing-an-agent-skill: Installing an Agent Skill
  using-ping-cli-without-agent-skills: Using Ping CLI without Agent Skills
  learn-more: Learn more
  learn-more-2: Learn more
---

# Agent Skills

Agent Skills are structured reference files that give coding agents targeted knowledge of Ping CLI commands and capabilities. Installing an Agent Skill means your agent can reason about the CLI directly, understanding available commands, flags, and service connectors without having to discover them through `--help` output at runtime.

Agent Skills follow the [Agent Skills open format](https://agentskills.io) and are distributed from the remote Ping CLI repository.

## What Agent Skills provide

An installed Ping CLI Agent Skill enables your coding agent to:

* Know the full set of available commands, subcommands, and their purpose.

* Understand flags, their types, and default values.

* Use the correct output format options (`text`, `json`, `ndjson`).

* Understand how service connectors are structured and how to authenticate to them.

* Know when certain commands require an active profile or authenticated session.

* Construct valid `pingcli` invocations without trial and error.

## Discovering available Agent Skills

To see all Agent Skills available from the remote Ping CLI repository:

```console
pingcli agent-skills list
```

The output includes the name and description of each available skill.

## Installing an Agent Skill

Install an Agent Skill to the default location (`.claude/skills/` in your current working directory):

```console
pingcli agent-skills install pingcli-usage
```

To install to a custom directory:

```console
pingcli agent-skills install pingcli-usage --output-dir /path/to/skills
```

The output directory is created automatically if it does not exist. The skill is placed at `<output-dir>/<skill-name>`.

|   |                                                                                                                                                                                                         |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | After installing an Agent Skill, your coding agent will reference it automatically when you ask about or use Ping CLI commands in that project. The skill file does not need to be referenced manually. |

## Using Ping CLI without Agent Skills

Installing an Agent Skill is optional. Coding agents can still use Ping CLI by running `pingcli --help` or any subcommand with `--help` to discover available options at runtime. Agent Skills reduce that friction by making CLI knowledge available upfront.

## Learn more

[icon: terminal, set=fas, size=3x]

#### [Command reference](../command_reference/pingcli_agent-skills.html)

Browse the `pingcli agent-skills` command and its subcommands.

[icon: rocket, set=fas, size=3x]

#### [Get started with Ping CLI](getting-started.html)

Install Ping CLI, connect to services, and run your first commands.

## Learn more

* [pingcli agent-skills list](../command_reference/pingcli_agent-skills_list.html)

* [pingcli agent-skills install](../command_reference/pingcli_agent-skills_install.html)

---

---
title: Authenticating to services
description: "Ping CLI supports two authentication approaches: interactive user sign-on for workstation use, and service authentication for automated environments. The right choice depends on whether a human is present during the CLI session."
component: pingcli
version: 1.11
page_id: pingcli:using_pingcli:authenticating-to-services
canonical_url: https://developer.pingidentity.com/pingcli/1.11/using_pingcli/authenticating-to-services.html
llms_txt: https://developer.pingidentity.com/pingcli/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 9, 2026
section_ids:
  interactive-user-sign-on: Interactive user sign-on
  service-authentication: Service authentication
  learn-more: Learn more
---

# Authenticating to services

Ping CLI supports two authentication approaches: interactive user sign-on for workstation use, and service authentication for automated environments. The right choice depends on whether a human is present during the CLI session.

| ***Approach***           | ***Grant types***               | ***Typical context***                         | ***Browser required***         | ***MFA applies*** |
| ------------------------ | ------------------------------- | --------------------------------------------- | ------------------------------ | ----------------- |
| Interactive user sign-on | Authorization code, Device code | Developer workstation, ad-hoc admin tasks     | Auth code: yes Device code: no | Yes               |
| Service authentication   | Client credentials              | CI/CD pipelines, automation, service accounts | No                             | No                |

## Interactive user sign-on

Interactive sign-on authenticates a human user against configured services using OAuth 2.0. Two grant types are available: authorization code for environments with a browser, and device code for remote or headless terminals. When a session ends, reauthentication is required at the next login.

|   |                                                                                                                                                                                                                                                                                                                                    |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | PingOne requires all administrator accounts to complete multi-factor authentication (MFA) during interactive sign-on. This policy is enforced by PingOne and cannot be disabled. Administrators using an external identity provider (IdP) for primary authentication satisfy this requirement through that provider's MFA instead. |

[Interactive user sign-on](authenticating-interactive.html)

## Service authentication

Service authentication uses the OAuth 2.0 client credentials flow to authenticate as an application rather than a user. No browser or human interaction is required. This is the recommended approach for CI/CD pipelines, scheduled jobs, and any context where a human operator is not present.

[Service authentication](authenticating-service.html)

## Learn more

* [Connect Ping Identity services](connecting-ping-services.html)

* [Interactive user sign-on](authenticating-interactive.html)

* [Service authentication](authenticating-service.html)

* [Configuration settings reference](../settings_reference/configuration-settings-reference.html)

---

---
title: Command structure
description: Ping CLI commands use a consistent multipart structure that must be specified in order.
component: pingcli
version: 1.11
page_id: pingcli:using_pingcli:command-structure
canonical_url: https://developer.pingidentity.com/pingcli/1.11/using_pingcli/command-structure.html
llms_txt: https://developer.pingidentity.com/pingcli/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  parts-of-a-command: Parts of a command
  product-commands: Product commands
  resource-actions: Resource action commands
  examples: Examples
  list-configuration-keys: List configuration keys
  list-pingone-environments: List PingOne environments
  learn-more: Learn more
---

# Command structure

Ping CLI commands use a consistent multipart structure that must be specified in order.

## Parts of a command

```
pingcli <command> <subcommand> [options and parameters]
```

| ***Part***                 | ***Description***                                                                                                                                                                                                        |
| -------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `pingcli`                  | The base call to the Ping CLI binary.                                                                                                                                                                                    |
| `<command>`                | The top-level command. This is either a core CLI capability (such as `config` or `auth`) or the root of a product namespace (such as `pingone` or `pingfederate`). Refer to [Product commands](#product-commands) below. |
| `<subcommand>`             | The operation to perform within the command. Product commands often have multiple levels of subcommand (for example, `pingcli pingone environments list`).                                                               |
| `[options and parameters]` | Flags and values accepted by the operation. These can be specified in any order after the first three parts. If a flag is specified more than once, only the last value applies.                                         |

## Product commands

Some top-level commands are the root of a product namespace: they group all operations for a specific Ping Identity product or service. A product command by itself does nothing; you must follow it with one or more subcommands that name the resource type and operation.

Product commands available in Ping CLI:

| ***Command*** | ***Product or service***                |
| ------------- | --------------------------------------- |
| `pingone`     | PingOne platform and universal services |
| `davinci`     | DaVinci universal service               |

|   |                                                                                                                                                    |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Some core commands, such as `auth` and `config`, are not product-specific. They operate at the CLI level and apply across any configured products. |

## Resource action commands

Every resource type exposes a consistent set of action commands. For example, `pingcli pingone applications` supports:

| ***Action*** | ***Aliases***              | ***Description***                                                                                                                                                    |
| ------------ | -------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `list`       | `ls`, `get-all`, `all`     | Returns all resources of this type in the environment.                                                                                                               |
| `get`        | `read`, `show`, `describe` | Returns a specific resource by ID.                                                                                                                                   |
| `create`     | `new`                      | Creates a new resource from a JSON body supplied using `--from-file`.                                                                                                |
| `replace`    | `update`                   | Replaces an existing resource (HTTP PUT) from a JSON body supplied using `--from-file`. Requires the resource ID.                                                    |
| `delete`     | `remove`, `rm`, `del`      | Deletes a specific resource by ID.                                                                                                                                   |
| `template`   | —                          | Generates a JSON body skeleton to use as the starting point for `create` or `replace`. Refer to [Generating resource templates](generating-resource-templates.html). |

## Examples

### List configuration keys

The following example lists all available Ping CLI configuration keys.

```bash
pingcli config list-keys
```

For more information, refer to [pingcli config list-keys](../command_reference/pingcli_config_list-keys.html).

### List PingOne environments

The following example lists all environments in your PingOne organization.

```bash
pingcli pingone environments list
```

For more information, refer to [pingcli pingone environments list](../command_reference/pingcli_pingone_environments_list.html).

## Learn more

* [Configuration settings reference](../settings_reference/configuration-settings-reference.html)

* [pingcli](../command_reference/pingcli.html)

---

---
title: Configure CLI settings
description: The pingcli config command provides four subcommands for reading, writing, and removing configuration values stored in the Ping CLI configuration file. You can find a complete list of available configuration keys and their descriptions in the Configuration settings reference.
component: pingcli
version: 1.11
page_id: pingcli:using_pingcli:configure-settings
canonical_url: https://developer.pingidentity.com/pingcli/1.11/using_pingcli/configure-settings.html
llms_txt: https://developer.pingidentity.com/pingcli/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 8, 2026
section_ids:
  runtime-configuration-options: Runtime configuration options
  configuration-file-location: Configuration file location
  list-available-configuration-keys: List available configuration keys
  set-a-configuration-value: Set a configuration value
  read-a-configuration-value: Read a configuration value
  remove-a-configuration-value: Remove a configuration value
  working-with-sensitive-values: Working with sensitive values
  learn-more: Learn more
---

# Configure CLI settings

The `pingcli config` command provides four subcommands for reading, writing, and removing configuration values stored in the Ping CLI configuration file. You can find a complete list of available configuration keys and their descriptions in the [Configuration settings reference](../settings_reference/configuration-settings-reference.html).

|   |                                                                                                                                                                                                                                                                                                |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Configuration values are stored per-profile. All commands operate on the active profile unless you specify a profile with the `--profile` / `-P` flag. For information about creating and managing profiles, refer to [Managing Configuration Profiles](managing-configuration-profiles.html). |

## Runtime configuration options

Ping CLI supports multiple ways to supply configuration values at runtime:

* **Inline parameters**: Pass values directly when invoking a command. Refer to the [Command Reference](../command_reference/pingcli.html) for a full list of available parameters for each command.

* **Configuration file**: Persist values in the Ping CLI configuration file, attached to a named configuration profile. Use the commands on this page to read, write, and remove configuration file values.

* **Environment variables**: Set values in the shell before running a command. This is most useful in CI/CD environments. Variable names follow the pattern `PINGCLI_*`, for example `PINGCLI_OUTPUT_FORMAT`.

When the same key is set in multiple places, inline parameters take precedence over environment variables, which take precedence over the configuration file.

## Configuration file location

The Ping CLI configuration file is created at `.pingcli/config.yaml` in the user's home directory. Configuration is stored in a version-controlled format (configuration model version 2). When Ping CLI is run for the first time after upgrading from a previous major version, any existing configuration is automatically migrated to the current model version.

## List available configuration keys

Before setting values, use the `pingcli config list-keys` command to see every key that Ping CLI can store:

```console
pingcli config list-keys
```

To output the keys in YAML format (useful for scripting or comparing with a configuration file):

```console
pingcli config list-keys --yaml
```

For descriptions of each key and its accepted values, see [Configuration settings reference](../settings_reference/configuration-settings-reference.html).

## Set a configuration value

Use the `pingcli config set` command to persist a value for a configuration key.

Set a value on the active profile:

```console
pingcli config set outputFormat=json
```

Set a value on a named profile without changing the active profile:

```console
pingcli config set --profile prod outputFormat=text
```

Set a service-specific setting, for example the PingOne endpoint root domain for a non-default region:

```console
pingcli config set service.pingOne.endpoint.rootDomain=pingone.eu
```

## Read a configuration value

Use the `pingcli config get` command to retrieve a stored value.

Read a single key from the active profile:

```console
pingcli config get outputFormat
```

Read all configuration values under a namespace by passing a prefix. For example, to read all PingOne settings:

```console
pingcli config get pingone
```

Read a key from a named profile:

```console
pingcli config get --profile prod service.pingOne.endpoint.rootDomain
```

## Remove a configuration value

Use the `pingcli config unset` command to remove a stored value. After unsetting, the key reverts to its built-in default.

Remove a value from the active profile:

```console
pingcli config unset outputFormat
```

Remove a value from a named profile:

```console
pingcli config unset --profile prod service.pingOne.endpoint.rootDomain
```

|   |                                                                                                                                                                                               |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The `default` profile cannot be deleted, but any setting within it can be unset. To clear all credentials from the default profile, use `pingcli config unset` for each setting individually. |

## Working with sensitive values

Ping CLI masks secret values (such as passwords and client secrets) in command output by default. To reveal the actual value, add the `--unmask-values` / `-U` flag.

Read a client secret with its value unmasked:

```console
pingcli config get --unmask-values service.pingOne.authentication.clientCredentials.clientSecret
```

Set a password and confirm the stored value in a single step:

```console
pingcli config set --unmask-values service.pingFederate.authentication.basicAuth.password=mysecret
```

|   |                                                                                                                                                                                           |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Unmasked output displays credentials in plain text in your terminal and shell history. Avoid using `--unmask-values` in shared sessions or CI/CD environments where output may be logged. |

## Learn more

* [Configuration settings reference](../settings_reference/configuration-settings-reference.html)

* [Managing Configuration Profiles](managing-configuration-profiles.html)

* [pingcli config set](../command_reference/pingcli_config_set.html)

* [pingcli config get](../command_reference/pingcli_config_get.html)

* [pingcli config unset](../command_reference/pingcli_config_unset.html)

* [pingcli config list-keys](../command_reference/pingcli_config_list-keys.html)

---

---
title: Connect Ping Identity services
description: "Ping CLI can connect to multiple Ping Identity products simultaneously, each with its own endpoint and authentication configuration. Connection settings are organized into profiles: each profile holds one connection for each supported product. For example, a development profile might point to a PingOne development tenant and a PingFederate development instance, while a separate sandbox profile connects to sandbox tenants of the same products."
component: pingcli
version: 1.11
page_id: pingcli:using_pingcli:connecting-ping-services
canonical_url: https://developer.pingidentity.com/pingcli/1.11/using_pingcli/connecting-ping-services.html
llms_txt: https://developer.pingidentity.com/pingcli/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 2, 2026
section_ids:
  initialize-a-connection: Initialize a connection
  pingone-universal-service-connectors: PingOne universal service connectors
  learn-more: Learn more
---

# Connect Ping Identity services

Ping CLI can connect to multiple Ping Identity products simultaneously, each with its own endpoint and authentication configuration. Connection settings are organized into **profiles**: each profile holds one connection for each supported product. For example, a `development` profile might point to a PingOne development tenant and a PingFederate development instance, while a separate `sandbox` profile connects to sandbox tenants of the same products.

Multiple profiles let you represent different logical environments and switch between them with a single command, without changing any individual service configuration:

```console
pingcli config profiles use sandbox
```

![connecting-overview](https://kroki.io/plantuml/svg/eNqdkcFKAzEQhu95iqFeWqQFD_XgoVBXC4JoQY9e0uxkDc1mliS7torP5d0nc3bbbhe7IDgLS2by5Z8_k7A2rpBe5qAoL8ihi09xaxE8qihdZlGEFklRy9LGZ9zEuTWZy5kGxT_0HWruPb0lZMnD2bSJzmZy6HIt1TrzVLp0jy6a6EXJp-j32LyJDrZkIZnhqd60_nrArlrSRAd6oIh91pLby99UV-eGg10JqSKng6VxGST3dwOQAZQ1QhS75rzlSRuLVzzMCi0VzQyHfM5UOBrAh4DjS-yEHh2-uOE5lI4RH6SFgL4yCsOo0S8uWOr02ALZnoy4Y3TNfPb5CNKlK9r8s3VY_dmZEW7MU4DxeLZ322b6kE0ms0aufeG2qDtF4XjysKIYKQfS7d1TWRmnDHx_gSzjK3nzjnWiPHtx0UgbmMq1rIuFZxEV6yXfyuitQJdCrSx-ACyiDU8=)

## Initialize a connection

The recommended first step when setting up a new profile is the interactive initialization wizard:

```console
pingcli init
```

The wizard prompts you to select which products to connect, choose an authentication method for each, and enter the required credentials. Your answers are saved to the active profile in `~/.pingcli/config.yaml`.

|   |                                                                                                                                                                                                               |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Each product connector also exposes its own `init` subcommand to reconfigure just that product without re-running the full wizard:```console
pingcli pingone init
``````console
pingcli pingfederate init
``` |

For detailed connection instructions for each product, see the product-specific topics in this section.

## PingOne universal service connectors

Several Ping Identity services are **universal service connectors**: they don't require their own separate connection setup. Instead, they inherit the credentials and endpoint from the PingOne connector already configured in the profile. To use any of these services, configure the PingOne connector using `pingcli pingone init`.

| Service             | CLI connector name | Connected via     |
| ------------------- | ------------------ | ----------------- |
| DaVinci             | `davinci`          | PingOne connector |
| PingOne Authorize   | `authorize`        | PingOne connector |
| PingOne Credentials | `credentials`      | PingOne connector |
| PingOne MFA         | `mfa`              | PingOne connector |
| PingOne Protect     | `protect`          | PingOne connector |
| PingOne Verify      | `verify`           | PingOne connector |

Universal service connectors are accessible as top-level commands (for example, `pingcli davinci`) and as subcommands of the `pingone` connector (for example, `pingcli pingone davinci`).

[icon: cloud, set=fas, size=3x]

#### [PingOne and universal services](../pingone/getting-started.html)

Connect to PingOne and the services that inherit its credentials, including DaVinci, PingOne Authorize, PingOne Credentials, PingOne MFA, PingOne Protect, and PingOne Verify.

## Learn more

* [pingcli config profiles use](../command_reference/pingcli_config_profiles_use.html)

* [pingcli init](../command_reference/pingcli_init.html)

* [pingcli pingone init](../command_reference/pingcli_pingone_init.html)

* [pingcli pingfederate init](../command_reference/pingcli_pingfederate_init.html)

* [Configuration settings reference](../settings_reference/configuration-settings-reference.html)

---

---
title: Custom API requests
description: Ping CLI can make API requests to supported Ping Identity products, similar to using curl, using the connector's api subcommand. For example, pingcli pingone api.
component: pingcli
version: 1.11
page_id: pingcli:using_pingcli:making-api-requests
canonical_url: https://developer.pingidentity.com/pingcli/1.11/using_pingcli/making-api-requests.html
llms_txt: https://developer.pingidentity.com/pingcli/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 8, 2026
section_ids:
  benefits-of-using-ping-cli-over-curl: Benefits of using Ping CLI over cURL
  ping-cli-manages-the-api-authentication: Ping CLI manages the API authentication
  ping-cli-manages-the-base-url: Ping CLI manages the base URL
  ping-cli-performs-automatic-retries-of-transient-errors: Ping CLI performs automatic retries of transient errors
  ping-cli-works-with-early-access-and-feature-flagged-apis: Ping CLI works with early access and feature-flagged APIs
  making-a-request: Making a request
  available-flags: Available flags
  example-get-request: Example GET request
  example-post-request-using-data-from-a-file: Example POST request (using data from a file)
  example-post-request-using-inline-data: Example POST request (using inline data)
  example-post-request-using-a-custom-header: Example POST request (using a custom header)
  example-put-request-using-data-from-a-file: Example PUT request (using data from a file)
  example-delete-request: Example DELETE request
  example-filtering-output-in-scripts: "Example: filtering output in scripts"
  more-information: More information
---

# Custom API requests

Ping CLI can make API requests to supported Ping Identity products, similar to using `curl`, using the connector's `api` subcommand. For example, `pingcli pingone api`.

|   |                                                                                                                                                                                                                                                                                                                                       |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | A configured and authenticated service connection is required before running this command. If you have not yet connected a service, refer to [Connect Ping Identity services](connecting-ping-services.html). To authenticate after connecting, use `pingcli auth login` or the per-product `pingcli <connector> auth login` command. |

## Benefits of using Ping CLI over cURL

Using Ping CLI to make direct API requests against a Ping Identity deployment offers a number of benefits over using a tool like `curl` directly.

### Ping CLI manages the API authentication

With commands similar to `curl`, it is typically up to the developer to provide credentials in the required format or a valid OAuth bearer token with the request. With Ping CLI, the API authentication is managed by the CLI tool and injected into the API request without the developer needing to add it manually. This capability allows the developer to focus on the structure and content of the request and ultimately focus on managing the Ping Identity deployment.

For example, the PingOne API requires a valid OAuth 2.0 bearer token that is typically short lived and can expire. When using Ping CLI, the developer needs to configure the PingOne connection details in the Ping CLI configuration and issue the API request without needing to add any authentication to the request syntax. The Ping CLI tool manages getting a valid access token and, if necessary, the refresh of an existing access token, and adds the token to the request on behalf of the developer.

### Ping CLI manages the base URL

With commands similar to `curl`, it's typically up to the developer to provide the full URL in the request. This requirement typically means the developer has to create variables for the host name or port to be able to use the same script for development, test, or production. Ping CLI injects the base URL value according to the developer's CLI configuration, meaning the same requests can be used between multiple environments without the need for custom variables.

### Ping CLI performs automatic retries of transient errors

APIs of any hosted or deployed service may respond with transient errors, for example rate limiting, server congestion, or network issues. There are cases when the developer needs to handle these errors and invoke custom logic. However, errors that are considered transient should be retried automatically.

Ping CLI automatically retries transient errors silently to the developer, so if they are encountered on the rare occasion, the developer doesn't need to retry an API request manually or, if embedded in a script, need to code specific retry logic.

For example, if PingOne returns a `429` HTTP response code as a result of rate limiting, Ping CLI handles the `Retry-After` header and, if needed, invokes an exponential backoff retry method according to documented best practice on the [PingOne API documentation](https://developer.pingidentity.com/pingone-api/before-you-begin/retry-best-practices.html). This repeated request process happens silently to the developer and allows for resilience in scripting environment management.

### Ping CLI works with early access and feature-flagged APIs

The `api` subcommand is not limited to APIs that Ping CLI supports natively. If a Ping Identity product exposes an early access or feature-flagged endpoint that the CLI doesn't yet have a dedicated command for, it can still be called using the `api` subcommand. Because authentication and base URL handling are still managed automatically, developers get the same ergonomics for bleeding-edge endpoints as they do for fully-supported ones, with no need to fall back to `curl`.

## Making a request

The format for making a request is `pingcli <connector> api [flags] API_URI`, where `<connector>` is the name of the connected product. For example:

* `pingcli pingone api <uri>`: requests against the PingOne management API

The **API_URI** is required and must be the API URI path omitting the base API path of the service. For example, with PingOne, a full URL might be documented in the [API documentation](https://developer.pingidentity.com/pingone-api/platform/applications/applications-1/read-all-applications.html) as:

`{{apiPath}}/environments/{{envID}}/applications`

Since Ping CLI injects the `apiPath` value, the **API_URI** value to provide is `environments/{{envID}}/applications`. For example:

`pingcli pingone api environments/$ENVIRONMENT_ID/applications`

### Available flags

| Flag              | Short form | Description                                                                                                                                                          |
| ----------------- | ---------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `--http-method`   | `-m`       | The HTTP method to use for the request. (default `GET`) Options are: `GET`, `POST`, `PUT`, `PATCH`, `DELETE`.                                                        |
| `--data`          | (none)     | Path to a JSON file containing the request body. Required for `POST`, `PUT`, and `PATCH` requests.                                                                   |
| `--data-raw`      | (none)     | Inline JSON string to send as the request body. An alternative to `--data` when you don't want to create a file. Example: `--data-raw '{"name": "My environment"}'`. |
| `--header`        | `-r`       | A custom header to add to the request. Repeatable for multiple headers. Example: `--header "Content-Type: application/vnd.pingidentity.user.import+json"`.           |
| `--output-format` | `-O`       | The console output format. Options are: `json`, `ndjson`, `text`. (default `text`)                                                                                   |
| `--fail`          | `-f`       | Return a non-zero exit code when the HTTP response indicates a failure status (4xx or 5xx).                                                                          |

### Example `GET` request

The following example reads all applications for a PingOne environment.

As a prerequisite, Ping CLI must be configured and authenticated to the PingOne tenant. Learn more in [Getting started with Ping CLI and PingOne](../pingone/getting-started.html).

```console
pingcli pingone api \
  environments/$PINGONE_ENVIRONMENT_ID/applications
```

> **Collapse: Expand example response**
>
> ```json
> {
>   "schemaVersion": "1.0",
>   "status": "success",
>   "message": "Custom request successful",
>   "data": {
>     "_links": {
>       "self": {
>         "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/applications"
>       }
>     },
>     "_embedded": {
>       "applications": [
>         {
>           "_links": {
>             "environment": {
>               "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6"
>             },
>             "self": {
>               "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/applications/fb955fe0-9b00-4bd3-a64e-6054dc95eae3"
>             }
>           },
>           "environment": {
>             "id": "abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6"
>           },
>           "id": "fb955fe0-9b00-4bd3-a64e-6054dc95eae3",
>           "name": "PingOne Admin Console",
>           "enabled": true,
>           "type": "PING_ONE_ADMIN_CONSOLE",
>           "protocol": "OPENID_CONNECT"
>         }
>       ]
>     },
>     "size": 1
>   },
>   "errors": [],
>   "meta": {
>     "command": "pingcli pingone api",
>     "api": { "httpStatus": 200 }
>   }
> }
> ```

### Example `POST` request (using data from a file)

The following example creates a new application in a PingOne environment. The API request payload is supplied from a JSON file.

```console
pingcli pingone api \
  -m POST \
  --data ./my-application.json \
  environments/$PINGONE_ENVIRONMENT_ID/applications
```

> **Collapse: Expand  contents**
>
> ```
> {
>     "enabled": true,
>     "name": "OIDC-Web-App",
>     "description": "Test Description - OIDC App (Web)",
>     "type": "WEB_APP",
>     "protocol": "OPENID_CONNECT",
>     "homePageUrl": "https://example.com/homePage",
>     "loginPageUrl": "https://example.com/loginPage",
>     "grantTypes": [
>         "AUTHORIZATION_CODE"
>     ],
>     "redirectUris": [
>         "https://example.com"
>     ],
>     "responseTypes": [
>         "CODE"
>     ],
>     "tokenEndpointAuthMethod": "CLIENT_SECRET_BASIC",
>     "pkceEnforcement": "REQUIRED"
> }
> ```

> **Collapse: Expand example response**
>
> ```json
> {
>   "schemaVersion": "1.0",
>   "status": "success",
>   "message": "Custom request successful",
>   "data": {
>     "_links": {
>       "self": {
>         "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/applications/403b2bb3-a151-42b2-99d5-5eae2b151215"
>       }
>     },
>     "environment": {
>       "id": "abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6"
>     },
>     "id": "403b2bb3-a151-42b2-99d5-5eae2b151215",
>     "name": "OIDC-Web-App",
>     "enabled": true,
>     "type": "WEB_APP",
>     "protocol": "OPENID_CONNECT"
>   },
>   "errors": [],
>   "meta": {
>     "command": "pingcli pingone api",
>     "api": { "httpStatus": 201 }
>   }
> }
> ```

### Example `POST` request (using inline data)

The following example creates a new PingOne environment using inline JSON data. The `--data-raw` flag is useful in scripts when creating a temporary file is not desirable.

```console
pingcli pingone api \
  -m POST \
  --data-raw '{"name": "My New Environment", "region": {"id": "NA"}, "type": "SANDBOX"}' \
  environments
```

> **Collapse: Expand example response**
>
> ```json
> {
>   "schemaVersion": "1.0",
>   "status": "success",
>   "message": "Custom request successful",
>   "data": {
>     "_links": {
>       "self": {
>         "href": "https://api.pingone.com/v1/environments/c1e92b4a-3d7e-4f1a-a2c5-9b8d0e6f3a21"
>       }
>     },
>     "id": "c1e92b4a-3d7e-4f1a-a2c5-9b8d0e6f3a21",
>     "name": "My New Environment",
>     "region": {
>       "id": "NA"
>     },
>     "type": "SANDBOX"
>   },
>   "errors": [],
>   "meta": {
>     "command": "pingcli pingone api",
>     "api": { "httpStatus": 201 }
>   }
> }
> ```

### Example `POST` request (using a custom header)

Some PingOne APIs require a specific `Content-Type` header. The following example imports users using the bulk user import API, which requires a custom content type header.

```console
pingcli pingone api \
  -m POST \
  --header "Content-Type: application/vnd.pingidentity.user.import+json" \
  --data ./users.json \
  environments/$PINGONE_ENVIRONMENT_ID/users
```

### Example `PUT` request (using data from a file)

The following example updates an existing application in a PingOne environment.

```console
pingcli pingone api \
  -m PUT \
  --data ./my-application.json \
  environments/$PINGONE_ENVIRONMENT_ID/applications/$PINGONE_MY_APPLICATION_ID
```

> **Collapse: Expand  contents**
>
> ```
> {
>     "name": "AppName",
>     "description": "This is my UPDATED app description",
>     "protocol": "OPENID_CONNECT",
>     "type": "WEB_APP"
> }
> ```

> **Collapse: Expand example response**
>
> ```json
> {
>   "schemaVersion": "1.0",
>   "status": "success",
>   "message": "Custom request successful",
>   "data": {
>     "_links": {
>       "self": {
>         "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/applications/d64c5a69-51ed-4c73-b8bc-8a3fafa6d0ea"
>       }
>     },
>     "environment": {
>       "id": "abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6"
>     },
>     "id": "d64c5a69-51ed-4c73-b8bc-8a3fafa6d0ea",
>     "name": "AppName",
>     "description": "this is my UPDATED app description",
>     "enabled": false,
>     "type": "WEB_APP",
>     "protocol": "OPENID_CONNECT"
>   },
>   "errors": [],
>   "meta": {
>     "command": "pingcli pingone api",
>     "api": { "httpStatus": 200 }
>   }
> }
> ```

### Example `DELETE` request

The following example deletes an application from a PingOne environment.

```console
pingcli pingone api \
  -m DELETE \
  environments/$PINGONE_ENVIRONMENT_ID/applications/$PINGONE_APPLICATION_ID
```

> **Collapse: Expand example response**
>
> ```json
> {
>   "schemaVersion": "1.0",
>   "status": "success",
>   "message": "Custom request successful",
>   "data": null,
>   "errors": [],
>   "meta": {
>     "command": "pingcli pingone api",
>     "api": { "httpStatus": 204 }
>   }
> }
> ```

### Example: filtering output in scripts

Use `-O json` to get machine-readable JSON output and pipe it to [jq](https://jqlang.org/) to extract specific fields. With `-O json`, the API response body is in the `data` field of the output envelope. This is useful in automation scripts where you need to extract a specific field for use in a subsequent command.

The following example lists all applications and extracts just their IDs.

```bash
pingcli pingone api \
  -O json \
  environments/$PINGONE_ENVIRONMENT_ID/applications \
  | jq -r '.data._embedded.applications[].id'
```

Use `--fail` to cause the command to return a non-zero exit code on any 4xx or 5xx response, making it compatible with `set -e` in shell scripts. When a request fails, the envelope's `errors` array contains structured error details.

```bash
set -e

pingcli pingone api \
  -O json \
  --fail \
  environments/$PINGONE_ENVIRONMENT_ID/applications \
  | jq -r '.data._embedded.applications[].id'
```

## More information

* [pingcli pingone api](../command_reference/pingcli_pingone_api.html)

* [Product compatibility](../product-compatibility.html)

* [Authenticating to services](authenticating-to-services.html)

* [JSON output schema reference](../output_schema_reference/output-schema-reference.html)

* [PingOne platform API reference](https://developer.pingidentity.com/pingone-api/introduction.html)

---

---
title: Filtering and transforming output
description: "Ping CLI gives you two ways to filter and reshape command output: the built-in --query flag for JMESPath expressions, and standard Unix pipes to jq for more expressive transformations. This page covers both tools in depth: when to reach for each, and how to combine them."
component: pingcli
version: 1.11
page_id: pingcli:using_pingcli:filtering-output
canonical_url: https://developer.pingidentity.com/pingcli/1.11/using_pingcli/filtering-output.html
llms_txt: https://developer.pingidentity.com/pingcli/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 8, 2026
section_ids:
  query-and-jmespath: "--query and JMESPath"
  extracting-a-single-field: Extracting a single field
  projecting-multiple-fields: Projecting multiple fields
  accessing-nested-fields: Accessing nested fields
  jmespath-and-string-comparisons: JMESPath and string comparisons
  when-jmespath-is-not-enough: When JMESPath is not enough
  jq: jq
  filtering-with-select: Filtering with select()
  compound-filters: Compound filters
  reshaping-records: Reshaping records
  counting-results: Counting results
  tab-separated-output-for-shell-scripts: Tab-separated output for shell scripts
  filtering-ndjson: Filtering ndjson
  choosing-between-query-and-jq: Choosing between --query and jq
  learn-more: Learn more
---

# Filtering and transforming output

Ping CLI gives you two ways to filter and reshape command output: the built-in `--query` flag for JMESPath expressions, and standard Unix pipes to `jq` for more expressive transformations. This page covers both tools in depth: when to reach for each, and how to combine them.

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | Both `--query` and `jq` require `json` or `ndjson` output. If you are using the default `text` format, switch to `json` first: add `-O json` to your command.`--query` applies its expression to the full JSON output envelope. Command results are under the `data` key: use `data[]` for array results and `data` for single-object results. Refer to [JSON output schema reference](../output_schema_reference/output-schema-reference.html) for the complete envelope structure. |

## --query and JMESPath

The `--query` flag evaluates a [JMESPath](https://jmespath.org/) expression against the JSON response before printing it. Because the expression runs inside Ping CLI, you don't need to install any additional tools; it works wherever Ping CLI runs.

JMESPath is well-suited for:

* Extracting a single field or a list of fields from every record.

* Projecting a subset of fields to reduce noise.

* Simple equality filters on known values.

### Extracting a single field

To get just the `name` of every environment, project the field across the `data` array:

```bash
pingcli pingone environments list -O json --query 'data[].name'
```

```json
[
  "Policy Change Feature Development",
  "Integration Testing",
  "Helpdesk Training",
  "Sandbox Testing",
  "Administrators"
]
```

### Projecting multiple fields

Use a multi-value projection to select a named subset of fields from each record:

```bash
pingcli pingone environments list -O json --query 'data[].{id: id, name: name, type: type}'
```

```json
[
  {
    "id": "03414408-42f9-4011-b45c-b46c7cc8028b",
    "name": "Policy Change Feature Development",
    "type": "SANDBOX"
  },
  {
    "id": "5e35b284-e3e4-4b5d-b378-d70674940ac3",
    "name": "Helpdesk Training",
    "type": "PRODUCTION"
  }
]
```

The keys on the left of `:` become the output field names, so you can rename fields in the same step.

### Accessing nested fields

Use dot notation to reach into nested objects. For example, to extract the license ID (nested under `license.id`):

```bash
pingcli pingone environments list -O json --query 'data[].{name: name, license: license.id}'
```

```json
[
  {
    "name": "Policy Change Feature Development",
    "license": "3eb902be-3d37-4926-9c8f-150716e955d3"
  },
  {
    "name": "Helpdesk Training",
    "license": "54776175-9a9f-4c21-a4c7-ecb975aa9b56"
  }
]
```

### JMESPath and string comparisons

String literals in JMESPath filter expressions must be wrapped in backticks and double-quoted:

```bash
pingcli pingone environments list -O json --query 'data[?type==`"PRODUCTION"`].name'
```

|   |                                                                                                                                                                                                                                                                                 |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The unusual quoting (a backtick-wrapped, double-quoted string) is a requirement of the JMESPath specification, not a shell quirk. When a filter comparison against a string value returns no results, check that you have both the outer backticks and the inner double quotes. |

### When JMESPath is not enough

JMESPath does not support:

* Substring matching or regular expressions.

* Sorting or ordering results.

* Counting or aggregating values.

* Reshaping data (for example, flattening nested arrays, computing derived fields).

For these tasks, reach for `jq`.

## jq

`jq` is a standalone JSON processor you pipe output into. It is more expressive than JMESPath and is the right choice when you need substring matching, sorting, counting, or any transformation that JMESPath cannot express.

If `jq` is not installed, see the [jq download page](https://jqlang.org/download/).

### Filtering with select()

Use `select()` to keep only records that match a condition. For example, to list only `PRODUCTION` environments:

```bash
pingcli pingone environments list -O json | jq '.data[] | select(.type == "PRODUCTION") | .name'
```

```text
"Helpdesk Training"
"Terraform Data Protection Test Environment"
"DaVinci Administrators"
"Administrators"
```

Add the `-r` flag to strip the surrounding quotes from string output:

```bash
pingcli pingone environments list -O json | jq -r '.data[] | select(.type == "PRODUCTION") | .name'
```

```text
Helpdesk Training
Terraform Data Protection Test Environment
DaVinci Administrators
Administrators
```

### Compound filters

Combine conditions with `and` and `or`:

```bash
# Sandbox environments whose name contains "Terraform"
pingcli pingone environments list -O json | \
  jq -r '.data[] | select(.type == "SANDBOX" and (.name | test("Terraform"))) | .name'
```

```text
Terraform Test
Terraform Demo
```

`test("pattern")` applies a regular expression: use this wherever JMESPath would fall short.

### Reshaping records

Build a new object from selected fields using `{key: expression}` syntax:

```bash
pingcli pingone environments list -O json | \
  jq '[.data[] | select(.type == "PRODUCTION") | {id, name}]'
```

```json
[
  {
    "id": "5e35b284-e3e4-4b5d-b378-d70674940ac3",
    "name": "Helpdesk Training"
  },
  {
    "id": "e7e7e106-9547-438c-a30b-0882cb267c10",
    "name": "DaVinci Administrators"
  },
  {
    "id": "4c33a4c6-7489-43fe-aa3c-87bd55520427",
    "name": "Administrators"
  }
]
```

Wrapping the expression in `[…​]` collects results into an array instead of printing them as separate lines.

### Counting results

```bash
# Count all environments
pingcli pingone environments list -O json | jq '.data | length'
```

```text
29
```

```bash
# Count production environments only
pingcli pingone environments list -O json | \
  jq '[.data[] | select(.type == "PRODUCTION")] | length'
```

```text
6
```

### Tab-separated output for shell scripts

Use string interpolation to produce tab-separated values you can feed to other shell commands:

```bash
pingcli pingone environments list -O json | \
  jq -r '.data[] | select(.type == "PRODUCTION") | "\(.name)\t\(.id)"'
```

```text
Helpdesk Training	5e35b284-e3e4-4b5d-b378-d70674940ac3
Terraform Data Protection Test Environment	0c442e65-9bab-4017-8d44-71fe0c9be286
DaVinci Administrators	e7e7e106-9547-438c-a30b-0882cb267c10
Administrators	4c33a4c6-7489-43fe-aa3c-87bd55520427
```

## Filtering ndjson

Both `--query` and `jq` work with `ndjson`, but the expression targets a single record rather than an array.

With bare `-O ndjson`, each line is a raw record with no envelope wrapper. Reference fields directly: do not use `data.` prefix:

```bash
# Print only the name field from every record
pingcli pingone environments list -O ndjson --query 'name'
```

With `jq`, use `select()` directly on the stream (`jq` processes each line independently):

```bash
pingcli pingone environments list -O ndjson | \
  jq -r 'select(.type == "PRODUCTION") | .name'
```

```text
Helpdesk Training
Terraform Data Protection Test Environment
DaVinci Administrators
Administrators
```

If you need envelope fields (such as `status` or `meta`) alongside each record, use `-O ndjson-wrapped` instead. With `ndjson-wrapped`, records are wrapped in the full envelope and field access uses `.data.name`, `.data.type`, and so on:

```bash
pingcli pingone environments list -O ndjson-wrapped | \
  jq -r 'select(.data.type == "PRODUCTION") | .data.name'
```

## Choosing between --query and jq

|                                                        |                 |                                                               |
| ------------------------------------------------------ | --------------- | ------------------------------------------------------------- |
| ***Need***                                             | ***Use***       | ***Why***                                                     |
| Extract or project fields                              | `--query`       | Zero dependencies; shorter command line                       |
| Equality filter on a known value                       | `--query`       | Straightforward; works without installing `jq`                |
| Substring or regex match                               | `jq`            | JMESPath has no `contains()` for strings or regex support     |
| Sort, count, or aggregate                              | `jq`            | JMESPath does not support these operations                    |
| Compute derived fields or reshape output significantly | `jq`            | `jq` can construct arbitrary new JSON structures              |
| Process one record at a time in a shell loop           | `ndjson` + `jq` | No need to parse a full JSON document; loop with `while read` |

## Learn more

* [pingcli pingone environments list](../command_reference/pingcli_pingone_environments_list.html)

* [Output formats](output-formats.html)

* [JSON output schema reference](../output_schema_reference/output-schema-reference.html)

* [Return codes](return-codes.html)

---

---
title: Generating resource templates
description: Most resource types in Ping CLI support a template action that generates a complete JSON body skeleton. Use it as a starting point when creating or replacing a resource rather than authoring the request body from scratch.
component: pingcli
version: 1.11
page_id: pingcli:using_pingcli:generating-resource-templates
canonical_url: https://developer.pingidentity.com/pingcli/1.11/using_pingcli/generating-resource-templates.html
llms_txt: https://developer.pingidentity.com/pingcli/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  how-it-works: How it works
  basic-workflow: Basic workflow
  resources-with-multiple-type-variants: Resources with multiple type variants
  learn-more: Learn more
---

# Generating resource templates

Most resource types in Ping CLI support a `template` action that generates a complete JSON body skeleton. Use it as a starting point when creating or replacing a resource rather than authoring the request body from scratch.

## How it works

Running `pingcli <product> <resource> template` prints a JSON object to stdout containing every field that `create` and `replace` accept, with all values set to their zero defaults. You edit the skeleton to supply the values you want, then feed the file back to `create` or `replace` using `--from-file`.

```bash
pingcli pingone groups template
```

Output:

```json
{
  "customData": {},
  "description": "",
  "displayName": "",
  "externalId": "",
  "name": "",
  "population": {
    "id": ""
  },
  "sourceId": "",
  "sourceType": "",
  "userFilter": ""
}
```

Fields set to empty strings, zero, `false`, or empty arrays are optional or will use service defaults. You only need to populate the fields relevant to your use case.

## Basic workflow

1. Generate the skeleton and save it to a file:

   ```bash
   pingcli pingone groups template > group.json
   ```

2. Edit the file to supply your values. Remove or leave blank any fields you don't need:

   ```json
   {
     "name": "Developers",
     "description": "Internal developer group",
     "population": {
       "id": "<population-id>"
     }
   }
   ```

3. Pass the edited file to `create`:

   ```bash
   pingcli pingone groups create --environment-id <env-id> --from-file group.json
   ```

You can also write directly to a file using `--output-file` instead of shell redirection:

```bash
pingcli pingone groups template --output-file group.json
```

## Resources with multiple type variants

Some resources support multiple configuration types in a single template output. For example, `pingcli pingone applications template` emits all four protocol variants (`oidc`, `saml`, `wsfed`, and `externalLink`) as separate top-level blocks:

```bash
pingcli pingone applications template > application.json
```

Partial output:

```json
{
  "externalLink": {
    "enabled": false,
    "homePageUrl": "",
    "name": "",
    "protocol": "",
    "type": ""
  },
  "oidc": {
    "clientId": "",
    "enabled": false,
    "grantTypes": [],
    "name": "",
    "protocol": "",
    "redirectUris": [],
    "type": ""
  },
  ...
}
```

For these resources, populate exactly one protocol block and delete the others before passing the body to `create` or `replace`. Supplying more than one block will result in an error.

## Learn more

* [pingcli pingone groups template](../command_reference/pingcli_pingone_groups_template.html)

* [pingcli pingone groups create](../command_reference/pingcli_pingone_groups_create.html)

* [pingcli pingone applications template](../command_reference/pingcli_pingone_applications_template.html)

* [Command structure](command-structure.html)

* [Managing resources](managing-resources-overview.html)

---

---
title: Getting started
description: Ping CLI is a cross-platform command-line tool for managing the configuration of Ping Identity services. This guide walks you through verifying your installation, connecting to services, and running your first commands.
component: pingcli
version: 1.11
page_id: pingcli:using_pingcli:getting-started
canonical_url: https://developer.pingidentity.com/pingcli/1.11/using_pingcli/getting-started.html
llms_txt: https://developer.pingidentity.com/pingcli/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 5, 2026
section_ids:
  install-the-cli: Install the CLI
  connect-to-ping-identity-services: Connect to Ping Identity services
  authenticate: Authenticate
  understand-command-structure: Understand command structure
  get-help-for-any-command: Get help for any command
  global-options: Global options
  enable-shell-completion: Enable shell completion
  output-formats: Output formats
  send-feedback: Send feedback
  next-steps: Next steps
  learn-more: Learn more
---

# Getting started

Ping CLI is a cross-platform command-line tool for managing the configuration of Ping Identity services. This guide walks you through verifying your installation, connecting to services, and running your first commands.

## Install the CLI

To begin, select the appropriate method of installation instructions for your platform:

[icon: apple, set=fab, size=3x]

#### [macOS](../install/macos.html)

Install using Homebrew (recommended) or as a standalone binary.

[icon: linux, set=fab, size=3x]

#### [Linux](../install/linux.html)

Install using Homebrew, a native package (.apk, .deb, .rpm), or a standalone binary.

[icon: windows, set=fab, size=3x]

#### [Windows](../install/windows.html)

Install using a standalone binary download using PowerShell.

|   |                                                                                                                         |
| - | ----------------------------------------------------------------------------------------------------------------------- |
|   | Ping CLI can also be run as a container. Refer to [Docker installation](../install/docker.html) for setup instructions. |

Confirm Ping CLI is installed and check the version:

```console
pingcli --version
```

If the command returns a version number, Ping CLI is ready to use. If the command is not found, return to the installation instructions for your platform and ensure the executable is in your system's PATH.

## Connect to Ping Identity services

Ping CLI supports connections to multiple Ping Identity products and services simultaneously. Connection settings are organized into **profiles**: each profile represents a distinct logical environment, such as sandbox, development, or testing.

Within a profile, one instance of each supported product can be connected. For example, a `development` profile might point to your PingOne development tenant and a PingFederate development instance, while a separate `sandbox` profile connects to sandbox tenants of the same products. Switching the active profile redirects all CLI commands to the corresponding set of product instances without changing any individual service configuration.

This model lets you maintain separate credentials and service endpoints for each environment and switch between them quickly with a single command:

```console
pingcli config profiles use sandbox
```

The active profile is used automatically by every command that does not specify `--profile` explicitly.

To configure your first profile, use the interactive setup wizard:

```console
pingcli init
```

The wizard prompts you to select the services you want to connect, choose an authentication method, and enter the required credentials. Your answers are saved to `.pingcli/config.yaml` in your home directory.

|   |                                                                                                                                                                                                                                                                                                                           |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Individual service connectors expose their own `init` subcommand. For example, to configure only the PingOne connection for the active profile:```console
pingcli pingone init
```For a step-by-step walkthrough of connecting PingOne, see [Getting started with Ping CLI and PingOne](../pingone/getting-started.html). |

For advanced setup (including scripted environments, multiple profiles, and CI/CD pipelines), see [Configure CLI settings](configure-settings.html). For a full guide to creating and switching between profiles, see [Managing Configuration Profiles](managing-configuration-profiles.html).

## Authenticate

After configuring your connections, log in to all configured services at once:

```console
pingcli auth login
```

Verify that authentication succeeded:

```console
pingcli auth status
```

The status command shows which services are authenticated, which have expired tokens, and which are not yet configured. When you are done, revoke and clear stored tokens with:

```console
pingcli auth logout
```

For token storage options and per-connector authentication, see [Authenticating to services](authenticating-to-services.html).

## Understand command structure

Ping CLI commands follow a consistent pattern:

```
pingcli [global options] <command> [subcommand] [flags]
```

Top-level commands correspond to functional areas:

| Command                | Purpose                                                                      |
| ---------------------- | ---------------------------------------------------------------------------- |
| `pingcli init`         | Run the guided setup wizard to connect Ping CLI to services.                 |
| `pingcli auth`         | Authenticate to all configured services, or check and revoke authentication. |
| `pingcli pingone`      | Administration tools for the PingOne platform and its universal services.    |
| `pingcli davinci`      | Administration tools for the DaVinci universal service.                      |
| `pingcli config`       | Manage the CLI configuration and profiles.                                   |
| `pingcli agent-skills` | Find and install agent skills for Ping CLI.                                  |
| `pingcli completion`   | Generate shell completion scripts.                                           |
| `pingcli feedback`     | Report issues and send feedback on the CLI.                                  |

Service connectors expose their own subcommands for operations, API requests, and authentication. For example, `pingcli pingone environments list` lists all PingOne environments, and `pingcli pingone api` sends a custom REST request to the PingOne management API.

## Get help for any command

Append `--help` to any command or subcommand to see its options and examples:

```console
pingcli --help
pingcli pingone --help
pingcli pingone environments --help
```

The help output lists available subcommands, flags, and usage examples. For a complete reference of every command and parameter, see the [Command reference](../command_reference/pingcli.html).

## Global options

The following options are available on all Ping CLI commands:

| Option                    | Description                                                                  |
| ------------------------- | ---------------------------------------------------------------------------- |
| `-h, --help`              | Display help for the command.                                                |
| `-O, --output-format`     | Set the output format: `text` (default), `json`, or `ndjson`.                |
| `-P, --profile`           | Specify a named configuration profile to use for the command.                |
| `-C, --config`            | Path to a custom configuration file (default: `$HOME/.pingcli/config.yaml`). |
| `--no-color`              | Disable colored text output.                                                 |
| `-D, --detailed-exitcode` | Return distinct exit codes for success (0), errors (1), and warnings (2).    |
| `--debug`                 | Enable debug output, including stack traces and transaction IDs.             |
| `--log-level`             | Set the console log level: `DEBUG`, `INFO`, `WARN` (default), or `ERROR`.    |

You can find a full list of configuration keys and their environment variable equivalents in [Configuration settings reference](../settings_reference/configuration-settings-reference.html).

## Enable shell completion

Ping CLI supports tab completion for bash, zsh, fish, and PowerShell. To enable it for your current session:

* bash

* zsh

* fish

* PowerShell

```console
source <(pingcli completion bash)
```

```console
source <(pingcli completion zsh)
```

```console
pingcli completion fish | source
```

```console
pingcli completion powershell | Out-String | Invoke-Expression
```

For instructions on making completion persistent across sessions, see [pingcli completion](../command_reference/pingcli_completion.html).

## Output formats

By default, Ping CLI outputs results as human-readable text. For machine processing or scripting, switch to JSON or newline-delimited JSON:

```console
pingcli --output-format json pingone environments list
```

The `--output-format` flag is available on all commands and can be set as a persistent default in your configuration:

```console
pingcli config set "outputFormat=json"
```

For more on the different output formats available, see [Output formats](output-formats.html) and for examples of handling and filtering output, see [Filtering and transforming output](filtering-output.html).

## Send feedback

To report issues or share feedback directly from the CLI:

```console
pingcli feedback
```

The command prints links to the Ping CLI issue tracker and feedback channels.

## Next steps

[icon: plug, set=fas, size=3x]

#### [Connect to services](connecting-ping-services.html)

Configure connections to PingOne, PingFederate, and other Ping Identity services.

[icon: key, set=fas, size=3x]

#### [Authenticate](authenticating-to-services.html)

Learn about interactive login, client credentials, token storage options, and non-interactive flows.

[icon: terminal, set=fas, size=3x]

#### [Command reference](../command_reference/pingcli.html)

Browse every command, subcommand, and flag available in Ping CLI.

## Learn more

* [pingcli config profiles use](../command_reference/pingcli_config_profiles_use.html)

* [pingcli init](../command_reference/pingcli_init.html)

* [pingcli pingone init](../command_reference/pingcli_pingone_init.html)

* [pingcli auth login](../command_reference/pingcli_auth_login.html)

* [pingcli auth status](../command_reference/pingcli_auth_status.html)

* [pingcli auth logout](../command_reference/pingcli_auth_logout.html)

* [pingcli completion](../command_reference/pingcli_completion.html)

* [pingcli config set](../command_reference/pingcli_config_set.html)

* [Configuration settings reference](../settings_reference/configuration-settings-reference.html)

---

---
title: Interactive user sign-on
description: Interactive sign-on authenticates a human user against configured services using OAuth 2.0. Two grant types are available; choose based on whether a browser is accessible in the environment.
component: pingcli
version: 1.11
page_id: pingcli:using_pingcli:authenticating-interactive
canonical_url: https://developer.pingidentity.com/pingcli/1.11/using_pingcli/authenticating-interactive.html
llms_txt: https://developer.pingidentity.com/pingcli/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 9, 2026
section_ids:
  benefits-for-administrators: Benefits for administrators
  authorization-code: Authorization code
  device-code: Device code
  multi-factor-authentication: Multi-factor authentication
  running-authentication-commands: Running authentication commands
  platform-level-login: Platform-level login
  check-authentication-status: Check authentication status
  log-out: Log out
  per-connector-authentication: Per-connector authentication
  token-storage: Token storage
  learn-more: Learn more
---

# Interactive user sign-on

Interactive sign-on authenticates a human user against configured services using OAuth 2.0. Two grant types are available; choose based on whether a browser is accessible in the environment.

## Benefits for administrators

Administrators can configure interactive user sign-on as the authentication method for CLI users to promote accountability and auditability. When users authenticate interactively, all configuration changes made through Ping CLI are audited against the individual user's account. This creates a clear audit trail linking each change to the specific person who made it, essential for compliance and governance.

In contrast, client credentials authentication (service account or static credential) cannot attribute changes to individual users; all activity appears under a shared service account identity, obscuring who performed specific actions. Interactive sign-on ensures that every CLI-driven configuration change is traceable to a named user, supporting your organization's accountability requirements.

## Authorization code

The authorization code flow opens a browser to complete sign-on. Ping CLI starts a local listener, redirects the browser to the service's authorization endpoint, and exchanges the returned code for tokens.

Use the authorization code flow when:

* You are working on a developer workstation with a local browser.

* The service is configured with a redirect URI pointing to `localhost`.

## Device code

The device code flow does not require a browser on the machine running Ping CLI. Instead, the CLI displays a short code and a URL. You open the URL on any device with a browser (such as your phone or another computer), enter the code, and complete sign-on there. After confirmation, Ping CLI automatically receives tokens.

Use the device code flow when:

* You are working over SSH or in a remote terminal without a browser.

* You are running Ping CLI in a headless server environment where interactive sessions are still user-initiated.

## Multi-factor authentication

Where authorization code flow and device code flow are used for interactive login, administrators can configure users to require multi-factor authentication (MFA) when signing on to the CLI.

|   |                                                                                                                                                                                                                                                                                                                                                        |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | PingOne enforces mandatory MFA for all administrator accounts. This requirement is applied by PingOne and cannot be disabled, and applies to both the authorization code and device code flows.Administrators who authenticate through an external identity provider (IdP) satisfy this requirement through that provider's MFA configuration instead. |

## Running authentication commands

### Platform-level login

Authenticate to all configured services at once:

```console
pingcli auth login
```

Ping CLI authenticates to each configured service in turn using the authentication type defined in the active profile. For authorization code, a browser window opens. For device code, a code and URL are displayed on the terminal.

### Check authentication status

Verify the current authentication state across all configured services:

```console
pingcli auth status
```

The status command shows which services are authenticated, which have expired tokens, and which are not yet configured.

### Log out

Revoke and clear stored tokens for all configured services:

```console
pingcli auth logout
```

### Per-connector authentication

The PingOne connector exposes its own `auth` subcommand for cases where you need to authenticate to a single service independently:

```console
pingcli pingone auth login
pingcli pingone auth logout
pingcli pingone auth status
```

## Token storage

Ping CLI stores authentication tokens according to the `auth.storage.type` configuration key:

| ***Storage type***       | ***Description***                                                                                                                                                         |
| ------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `secure_local` (default) | Tokens are stored in the operating system's native secure storage (macOS Keychain, Windows Credential Manager, or equivalent on Linux). Recommended for workstation use.  |
| `file`                   | Can be used where the operating system's native secure storage is not available. Tokens are stored locally. Do not use in production or shared environments.              |
| `none`                   | Tokens are not persisted. Authentication must be completed before each CLI session. Useful in ephemeral CI/CD environments where tokens are generated fresh for each run. |

To configure the storage type:

```console
pingcli config set "auth.storage.type=secure_local"
```

## Learn more

* [pingcli auth login](../command_reference/pingcli_auth_login.html)

* [pingcli auth logout](../command_reference/pingcli_auth_logout.html)

* [pingcli auth status](../command_reference/pingcli_auth_status.html)

* [pingcli pingone auth login](../command_reference/pingcli_pingone_auth_login.html)

* [pingcli pingone auth logout](../command_reference/pingcli_pingone_auth_logout.html)

* [pingcli pingone auth status](../command_reference/pingcli_pingone_auth_status.html)

* [pingcli config set](../command_reference/pingcli_config_set.html)

* [Configuration settings reference](../settings_reference/configuration-settings-reference.html)

* [Overview](authenticating-to-services.html)

* [Service authentication](authenticating-service.html)

* [Connect Ping Identity services](connecting-ping-services.html)

---

---
title: Logging
description: Ping CLI supports diagnostic logging to help developers troubleshoot issues and understand the CLI's internal behavior. The default log level is WARN. To see more detailed output, set PINGCLI_LOG_LEVEL to DEBUG or INFO.
component: pingcli
version: 1.11
page_id: pingcli:using_pingcli:logging
canonical_url: https://developer.pingidentity.com/pingcli/1.11/using_pingcli/logging.html
llms_txt: https://developer.pingidentity.com/pingcli/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 5, 2026
section_ids:
  enabling-logging: Enabling logging
  log-levels: Log levels
  writing-logs-to-a-file: Writing logs to a file
  using-flags: Using flags
  persisting-log-settings-in-a-profile: Persisting log settings in a profile
  learn-more: Learn more
---

# Logging

Ping CLI supports diagnostic logging to help developers troubleshoot issues and understand the CLI's internal behavior. The default log level is `WARN`. To see more detailed output, set `PINGCLI_LOG_LEVEL` to `DEBUG` or `INFO`.

## Enabling logging

Set the `PINGCLI_LOG_LEVEL` environment variable to control log verbosity:

```console
export PINGCLI_LOG_LEVEL=DEBUG
pingcli pingone environments list
```

Log output is written to stderr by default.

## Log levels

The following log levels are available, listed from most verbose to least verbose:

| Level   | Description                                                                                                                                             |
| ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `DEBUG` | Detailed operational messages useful for debugging, including API request and response metadata.                                                        |
| `INFO`  | General informational messages confirming that Ping CLI is operating as expected.                                                                       |
| `WARN`  | Warnings about conditions that are not errors but may indicate unexpected behavior or configuration that should be reviewed. This is the default level. |
| `ERROR` | Error conditions that caused a command to fail or behave unexpectedly.                                                                                  |

## Writing logs to a file

To write log output to a file, set the `PINGCLI_LOG_FILE` environment variable:

```console
export PINGCLI_LOG_LEVEL=DEBUG
export PINGCLI_LOG_FILE=./pingcli.log
pingcli pingone environments list
```

When `PINGCLI_LOG_FILE` is set, log messages are written to the specified file in NDJSON format with structured fields including `timestamp`, `level`, `message`, `cli_function`, and `connector`. This makes file logs suitable for ingestion into observability tooling.

File logging uses its own independent log level, controlled by `PINGCLI_LOG_FILE_LEVEL` (default: `DEBUG`). This lets you capture verbose file logs while keeping console output at a higher level.

|   |                                                                                                                     |
| - | ------------------------------------------------------------------------------------------------------------------- |
|   | If `PINGCLI_LOG_FILE_LEVEL` is set without `PINGCLI_LOG_FILE`, the CLI emits a warning and the value has no effect. |

## Using flags

All three log settings are also available as persistent flags on every command:

| Flag               | Environment variable     | Default  |
| ------------------ | ------------------------ | -------- |
| `--log-level`      | `PINGCLI_LOG_LEVEL`      | `WARN`   |
| `--log-file`       | `PINGCLI_LOG_FILE`       | Disabled |
| `--log-file-level` | `PINGCLI_LOG_FILE_LEVEL` | `DEBUG`  |

Precedence, from highest to lowest: flag > environment variable > profile configuration > default.

## Persisting log settings in a profile

To avoid setting environment variables on every command, persist log settings using `pingcli config set`:

```console
pingcli config set log.level=DEBUG
pingcli config set log.file=/path/to/file.ndjson
pingcli config set log.fileLevel=INFO
```

To configure settings for a specific profile, add the `--profile` flag:

```console
pingcli config set --profile myprofile log.level=DEBUG
```

You can find a complete list of configuration keys in [Configuration settings reference](../settings_reference/configuration-settings-reference.html).

## Learn more

* [pingcli config set](../command_reference/pingcli_config_set.html)

* [Configuration settings reference](../settings_reference/configuration-settings-reference.html)

* [OpenTelemetry](telemetry.html)

---

---
title: Managing Configuration Profiles
description: A configuration profile is a named context that holds a complete set of service connection settings for one environment. Switching profiles changes which environment all subsequent pingcli commands target, without you needing to re-enter credentials or specify flags on every command.
component: pingcli
version: 1.11
page_id: pingcli:using_pingcli:managing-configuration-profiles
canonical_url: https://developer.pingidentity.com/pingcli/1.11/using_pingcli/managing-configuration-profiles.html
llms_txt: https://developer.pingidentity.com/pingcli/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 5, 2026
section_ids:
  create-a-configuration-profile: Create a configuration profile
  view-and-switch-the-active-profile: View and switch the active profile
  set-configuration-values-on-a-profile: Set configuration values on a profile
  delete-a-configuration-profile: Delete a configuration profile
  learn-more: Learn more
---

# Managing Configuration Profiles

A configuration profile is a named context that holds a complete set of service connection settings for one environment. Switching profiles changes which environment all subsequent `pingcli` commands target, without you needing to re-enter credentials or specify flags on every command.

When Ping CLI is first installed, a `default` profile is created and set as the active profile. You can use this profile if you only ever work in a single environment, but most developers benefit from creating at least one profile for each environment: for example, `dev`, `test`, and `prod`.

Common reasons to use multiple profiles:

* Switching between development, test, and production environments without re-configuring credentials each time.

* Experimenting in a sandbox and keeping those settings separate from a shared development environment.

* Managing multiple demonstration environments independently.

* Organising related work into named workspaces.

|   |                                                                                                                                                                                                           |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Before running any `pingcli` command, confirm which profile is active with: `pingcli config get activeProfile` This prints only the active profile name (the quickest way to check your current context). |

## Create a configuration profile

Use the `pingcli config profiles create` command to add a new profile.

Running the command without flags starts an interactive guided experience:

```console
pingcli config profiles create
```

To create and immediately activate a profile in a single step, pass the name, an optional description, and the `--set-active` flag:

```console
pingcli config profiles create --name dev --description "Development environment" --set-active
```

Confirm the profile was created with the `pingcli config profiles list` command:

```console
pingcli config profiles list
```

## View and switch the active profile

All `pingcli` commands use the active profile unless you override it with the `--profile` / `-P` global flag on a specific command.

|   |                                                                                                                                           |
| - | ----------------------------------------------------------------------------------------------------------------------------------------- |
|   | The `--profile` / `-P` flag overrides the active profile for that single command only. It does not permanently change the active profile. |

To switch the active profile, use the `pingcli config profiles use` command:

```console
pingcli config profiles use test
```

After switching, verify the change:

```console
pingcli config get activeProfile
```

|   |                                                                                                             |
| - | ----------------------------------------------------------------------------------------------------------- |
|   | Making "switch → verify" a habit helps prevent accidentally running commands against the wrong environment. |

## Set configuration values on a profile

Configuration values are stored per-profile using the `pingcli config set` command. When `--profile` / `-P` is not specified, the value is written to the active profile.

The following example activates the `dev` profile and sets its output format:

```console
pingcli config profiles use dev
pingcli config set "outputFormat=json"
```

To write a value to a different profile without changing the active profile, use `--profile`:

```console
pingcli config set --profile test "outputFormat=text"
```

To see all stored configuration for the active profile:

```console
pingcli config profiles show
```

To view a specific named profile:

```console
pingcli config profiles show prod
```

You can find a full list of available configuration settings in the [Configuration settings reference](../settings_reference/configuration-settings-reference.html).

## Delete a configuration profile

When a profile is no longer needed, use the `pingcli config profiles delete` command. All configuration settings for that profile are permanently removed from the filesystem.

|   |                                                                                                                                  |
| - | -------------------------------------------------------------------------------------------------------------------------------- |
|   | The `default` profile cannot be deleted. To remove credentials from it, use `pingcli config unset` to clear individual settings. |

## Learn more

* [pingcli config profiles create](../command_reference/pingcli_config_profiles_create.html)

* [pingcli config profiles use](../command_reference/pingcli_config_profiles_use.html)

* [pingcli config profiles list](../command_reference/pingcli_config_profiles_list.html)

* [pingcli config profiles show](../command_reference/pingcli_config_profiles_show.html)

* [pingcli config profiles delete](../command_reference/pingcli_config_profiles_delete.html)

* [pingcli config get](../command_reference/pingcli_config_get.html)

* [pingcli config set](../command_reference/pingcli_config_set.html)

* [Configuration settings reference](../settings_reference/configuration-settings-reference.html)

---

---
title: Managing resources
description: Ping CLI provides multiple methods for managing resources across connected Ping Identity services. Choose the approach that matches your goal.
component: pingcli
version: 1.11
page_id: pingcli:using_pingcli:managing-resources-overview
canonical_url: https://developer.pingidentity.com/pingcli/1.11/using_pingcli/managing-resources-overview.html
llms_txt: https://developer.pingidentity.com/pingcli/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 5, 2026
---

# Managing resources

Ping CLI provides multiple methods for managing resources across connected Ping Identity services. Choose the approach that matches your goal.

[icon: terminal, set=fas, size=3x]

#### [Command structure](command-structure.html)

Learn how Ping CLI commands are constructed: product namespaces, resource actions, and available options. This is the foundation for all resource management tasks.

[icon: file-code, set=fas, size=3x]

#### [Generate a resource template](generating-resource-templates.html)

Auto-generate a JSON skeleton for any resource type to use as a starting point when creating or replacing a resource.

[icon: plug, set=fas, size=3x]

#### [Custom API requests](making-api-requests.html)

Call any Ping Identity API endpoint directly from the CLI, with automatic authentication, base URL management, and built-in retry logic. Useful for endpoints not yet exposed as native commands or when building automation scripts.

---

---
title: OpenTelemetry
description: Ping CLI includes optional support for exporting telemetry data using the OpenTelemetry (OTel) standard. When enabled, Ping CLI exports trace spans and metrics for commands and API calls to an OTLP-compatible collector, providing observability into CLI usage patterns in automated environments.
component: pingcli
version: 1.11
page_id: pingcli:using_pingcli:telemetry
canonical_url: https://developer.pingidentity.com/pingcli/1.11/using_pingcli/telemetry.html
llms_txt: https://developer.pingidentity.com/pingcli/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 2, 2026
section_ids:
  enabling-telemetry: Enabling telemetry
  configuring-the-otlp-endpoint: Configuring the OTLP endpoint
  protocol: Protocol
  metrics: Metrics
  tls-configuration: TLS configuration
  enabling-tls: Enabling TLS
  trusting-a-custom-ca-certificate: Trusting a custom CA certificate
  mutual-tls-mtls: Mutual TLS (mTLS)
  trust-any-certificate-insecure: Trust any certificate (insecure)
  data-scope: Data scope
  learn-more: Learn more
---

# OpenTelemetry

Ping CLI includes optional support for exporting telemetry data using the [OpenTelemetry](https://opentelemetry.io/) (OTel) standard. When enabled, Ping CLI exports trace spans and metrics for commands and API calls to an OTLP-compatible collector, providing observability into CLI usage patterns in automated environments.

Telemetry is **disabled by default**. No data is collected or transmitted unless you explicitly enable it.

## Enabling telemetry

Telemetry can be enabled using the `telemetry.enabled` configuration key or the equivalent environment variable:

```console
pingcli config set "telemetry.enabled=true"
```

Or using an environment variable for session-scoped activation:

```console
export PINGCLI_TELEMETRY_ENABLED=true
```

## Configuring the OTLP endpoint

Telemetry data is exported to an OTLP-compatible collector endpoint. Set the endpoint URL using the `telemetry.otlp.endpoint` configuration key or the standard OTel environment variable:

```console
pingcli config set "telemetry.otlp.endpoint=http://localhost:4318"
```

Or:

```console
export OTEL_EXPORTER_OTLP_ENDPOINT=http://localhost:4318
```

## Protocol

Ping CLI supports two OTLP export protocols:

| Protocol         | Description                                                                                                       |
| ---------------- | ----------------------------------------------------------------------------------------------------------------- |
| `http` (default) | Exports data over HTTP using protobuf encoding. Suitable for most standard collector configurations.              |
| `grpc`           | Exports data using gRPC transport. Use this option when your collector is configured to receive gRPC connections. |

To configure the protocol:

```console
pingcli config set "telemetry.otlp.protocol=grpc"
```

Or:

```console
export OTEL_EXPORTER_OTLP_PROTOCOL=grpc
```

## Metrics

In addition to trace spans, Ping CLI exports OTLP metrics covering command invocations and connector operations. The following instruments are emitted:

| Instrument                                | Unit           | Attributes                                                                                 |
| ----------------------------------------- | -------------- | ------------------------------------------------------------------------------------------ |
| `pingcli.command.invocations`             | `{invocation}` | `pingcli.command`, `pingcli.error.type` (on error)                                         |
| `pingcli.command.duration`                | `s`            | same                                                                                       |
| `pingcli.connector.operation.invocations` | `{invocation}` | `pingcli.connector`, `pingcli.resource`, `pingcli.action`, `pingcli.error.type` (on error) |
| `pingcli.connector.operation.duration`    | `s`            | same                                                                                       |

The metric export interval defaults to 60 seconds. To change it:

```console
pingcli config set "telemetry.metric.exportInterval=30s"
```

Or:

```console
export OTEL_METRIC_EXPORT_INTERVAL=30s
```

## TLS configuration

When connecting to an OTLP endpoint over HTTPS or gRPC with TLS, first enable TLS explicitly, then configure certificate trust and mutual TLS (mTLS) as needed.

### Enabling TLS

TLS must be enabled before any certificate configuration takes effect:

```console
pingcli config set "telemetry.tls.enabled=true"
```

Or using an environment variable:

```console
export OTEL_EXPORTER_OTLP_TLS_ENABLED=true
```

### Trusting a custom CA certificate

If your OTLP collector uses a certificate issued by a private CA, configure Ping CLI to trust it by providing the PEM-encoded CA certificate file:

```console
pingcli config set "telemetry.tls.caFile=/path/to/ca.pem"
```

### Mutual TLS (mTLS)

For environments that require client certificate authentication, configure the client certificate and key:

```console
pingcli config set "telemetry.tls.certFile=/path/to/client.pem"
pingcli config set "telemetry.tls.keyFile=/path/to/client-key.pem"
```

### Trust any certificate (insecure)

For development and testing environments using self-signed certificates:

|   |                                                                                                                                                                                                  |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | The `telemetry.tls.insecureSkipVerify` configuration key, when set to `true`, is insecure and is intended for development and testing only. You shouldn't enable this option for production use. |

```console
pingcli config set "telemetry.tls.insecureSkipVerify=true"
```

## Data scope

When telemetry is enabled, Ping CLI exports trace spans and metrics covering the execution of CLI commands and API calls. Only proprietary Ping CLI operational data is included in trace spans. No authentication credentials, request payloads, or response bodies are included in telemetry data.

## Learn more

* [pingcli config set](../command_reference/pingcli_config_set.html)

* [Configuration settings reference](../settings_reference/configuration-settings-reference.html)

* [Logging](logging.html)

---

---
title: Output formats
description: "Ping CLI can produce output in four formats: text, json, ndjson, and ndjson-wrapped. Use the -O flag (or --output-format) to choose. The format you pick determines what downstream tools you can combine with and how much processing you need to do."
component: pingcli
version: 1.11
page_id: pingcli:using_pingcli:output-formats
canonical_url: https://developer.pingidentity.com/pingcli/1.11/using_pingcli/output-formats.html
llms_txt: https://developer.pingidentity.com/pingcli/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 8, 2026
section_ids:
  text: text
  json: json
  filtering-with-query: Filtering with --query
  piping-to-jq: Piping to jq
  ndjson: ndjson
  when-to-prefer-ndjson-over-json: When to prefer ndjson over json
  processing-ndjson-in-a-shell-loop: Processing ndjson in a shell loop
  filtering-ndjson-with-query: Filtering ndjson with --query
  ndjson-wrapped: ndjson-wrapped
  setting-a-default-output-format: Setting a default output format
  learn-more: Learn more
---

# Output formats

Ping CLI can produce output in four formats: `text`, `json`, `ndjson`, and `ndjson-wrapped`. Use the `-O` flag (or `--output-format`) to choose. The format you pick determines what downstream tools you can combine with and how much processing you need to do.

```bash
pingcli <command> -O json
pingcli <command> -O ndjson
pingcli <command> -O ndjson-wrapped
pingcli <command> -O text
```

|                  |                                                           |                                                       |
| ---------------- | --------------------------------------------------------- | ----------------------------------------------------- |
| ***Format***     | ***Best for***                                            | ***Works with***                                      |
| `text` (default) | Reading output at the terminal                            | Human eyes; no tooling required                       |
| `json`           | Scripting, automation, complete response inspection       | `jq`, `--query` (JMESPath), Python, any JSON parser   |
| `ndjson`         | Streaming, log pipelines, processing one record at a time | `jq`, `while read`, grep, awk, log shippers           |
| `ndjson-wrapped` | Streaming with full envelope metadata for each record     | `jq`, log shippers that expect a consistent structure |

## text

Text is the default. Ping CLI formats the response as an aligned table with column headers (easy to scan, but not designed for parsing).

```bash
pingcli config profiles list
```

```text
NAME                      DESCRIPTION                                  ACTIVE
default                   Default profile created by Ping CLI          false
development-environment   CLI profile for the feature development environment          true
testing-environment       CLI profile for the testing environment                      false
```

Text output does not support `--query`. If you need to filter or extract values, switch to `json` or `ndjson`.

## json

JSON wraps every command result in a consistent envelope. The six core fields (`schemaVersion`, `status`, `message`, `data`, `errors`, `meta`) are always present. A `warnings` field is included only when the command completes with non-fatal warnings.

```bash
pingcli config profiles list -O json
```

```json
{
  "schemaVersion": "1.0",
  "status": "success",
  "message": "",
  "data": [
    {
      "name": "default",
      "description": "Default profile created by Ping CLI",
      "active": false
    },
    {
      "name": "development-environment",
      "description": "CLI profile for the feature development environment",
      "active": true
    },
    {
      "name": "testing-environment",
      "description": "CLI profile for the testing environment",
      "active": false
    }
  ],
  "errors": [],
  "meta": {
    "command": "pingcli config profiles list",
    "count": 3
  }
}
```

`data` holds the command payload: an array when the command returns multiple records, a single object for single-resource commands, or `null` on error. `meta.count` is automatically set whenever `data` is an array. Refer to [JSON output schema reference](../output_schema_reference/output-schema-reference.html) for the complete field reference and JSONSchema.

### Filtering with --query

The `--query` flag applies a [JMESPath](https://jmespath.org/) expression to the full JSON envelope. This is the fastest way to extract a specific field or filter records without installing additional tools. Because `--query` targets the envelope, reference `data` as the root for command results.

```bash
# Get the name of every active profile
pingcli config profiles list -O json --query 'data[?active].name'
```

```json
[
  "development-environment"
]
```

Refer to [Filtering and transforming output](filtering-output.html) for more `--query` examples and JMESPath syntax.

### Piping to jq

For transformations that go beyond what JMESPath supports, pipe to `jq`:

```bash
# Extract all profile names as a plain list
pingcli config profiles list -O json | jq -r '.data[].name'
```

```text
default
development-environment
testing-environment
```

## ndjson

Newline-delimited JSON (NDJSON) emits one raw JSON record for each line as each result is produced. Each line is a plain JSON object; there is no envelope wrapper.

```bash
pingcli config profiles list -O ndjson
```

```text
{"name":"default","description":"Default profile created by Ping CLI","active":false}
{"name":"development-environment","description":"CLI profile for the feature development environment","active":true}
{"name":"testing-environment","description":"CLI profile for the testing environment","active":false}
```

|   |                                                                                                                                                              |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | Errors are always wrapped in the full envelope regardless of which NDJSON format you use. Use `-O ndjson-wrapped` if you need a full envelope on every line. |

### When to prefer ndjson over json

* **Streaming**: Records appear as they arrive rather than after the full response is buffered. Useful for long-running commands.

* **Log pipelines**: NDJSON feeds directly into log shippers (Fluentd, Logstash, Vector) without any wrapping.

* **Line-by-line processing**: Standard shell tools (`grep`, `awk`, `while read`) work on individual lines without needing to parse a document.

### Processing ndjson in a shell loop

```bash
pingcli config profiles list -O ndjson | while IFS= read -r line; do
  name=$(echo "$line" | jq -r '.name')
  active=$(echo "$line" | jq -r '.active')
  echo "Profile: $name  active=$active"
done
```

```text
Profile: default  active=false
Profile: development-environment  active=true
Profile: testing-environment  active=false
```

### Filtering ndjson with --query

With bare `-O ndjson`, `--query` applies a JMESPath expression to each raw record individually. Because there is no envelope, reference fields directly by name:

```bash
# Print only the name field from every record
pingcli config profiles list -O ndjson --query 'name'
```

## ndjson-wrapped

`-O ndjson-wrapped` behaves like `ndjson` but wraps each record in the full envelope. Use this format when downstream tools need envelope metadata (such as `status` or `meta.command`) alongside every record.

```bash
pingcli config profiles list -O ndjson-wrapped
```

```text
{"schemaVersion":"1.0","status":"success","message":"","data":{"name":"default","description":"Default profile created by Ping CLI","active":false},"errors":[],"meta":{"command":"pingcli config profiles list","count":1}}
{"schemaVersion":"1.0","status":"success","message":"","data":{"name":"development-environment","description":"CLI profile for the feature development environment","active":true},"errors":[],"meta":{"command":"pingcli config profiles list","count":1}}
{"schemaVersion":"1.0","status":"success","message":"","data":{"name":"testing-environment","description":"CLI profile for the testing environment","active":false},"errors":[],"meta":{"command":"pingcli config profiles list","count":1}}
```

With `--query` or `jq`, reference fields through the envelope:

```bash
pingcli config profiles list -O ndjson-wrapped --query 'data.name'
```

```bash
pingcli config profiles list -O ndjson-wrapped | jq -r 'select(.data.active) | .data.name'
```

## Setting a default output format

To avoid specifying `-O` on every command, set a default in your configuration:

```bash
pingcli config set outputFormat json
```

You can override the configured default at any time with the `-O` flag on individual commands.

## Learn more

* [pingcli config profiles list](../command_reference/pingcli_config_profiles_list.html)

* [pingcli config set](../command_reference/pingcli_config_set.html)

* [Configuration settings reference](../settings_reference/configuration-settings-reference.html)

* [Filtering and transforming output](filtering-output.html)

* [JSON output schema reference](../output_schema_reference/output-schema-reference.html)

* [Return codes](return-codes.html)

---

---
title: Return codes
description: Ping CLI exits with a numeric return code after every command. Scripts and CI/CD pipelines can use these codes to branch on success, failure, or success-with-warnings without parsing output text.
component: pingcli
version: 1.11
page_id: pingcli:using_pingcli:return-codes
canonical_url: https://developer.pingidentity.com/pingcli/1.11/using_pingcli/return-codes.html
llms_txt: https://developer.pingidentity.com/pingcli/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 5, 2026
section_ids:
  enabling-detailed-exit-codes: Enabling detailed exit codes
  when-warnings-occur: When warnings occur
  using-return-codes-in-shell-scripts: Using return codes in shell scripts
  fail-on-error-continue-on-warning: Fail on error, continue on warning
  treat-any-non-zero-result-as-a-failure: Treat any non-zero result as a failure
  using-detailed-exit-codes-in-github-actions: Using detailed exit codes in GitHub Actions
  learn-more: Learn more
---

# Return codes

Ping CLI exits with a numeric return code after every command. Scripts and CI/CD pipelines can use these codes to branch on success, failure, or success-with-warnings without parsing output text.

|            |                       |                                                                                                                                                                     |
| ---------- | --------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ***Code*** | ***Meaning***         | ***When you see it***                                                                                                                                               |
| `0`        | Success               | The command completed with no errors or warnings. Also returned for non-operational commands: `--help`, `--version`, and `completion`.                              |
| `1`        | Failure               | The command encountered an error and did not complete successfully. Check `stderr` or the [log file](logging.html) for details.                                     |
| `2`        | Success with warnings | The command completed, but one or more non-fatal issues were encountered. Only returned when `--detailed-exitcode` is enabled; otherwise these commands return `0`. |

## Enabling detailed exit codes

By default, Ping CLI returns `0` for any command that completes, even if warnings were produced. To distinguish a clean success from a success-with-warnings, pass the `--detailed-exitcode` (`-D`) flag:

```bash
pingcli --detailed-exitcode <command>
```

With `--detailed-exitcode` enabled:

* A clean run returns `0`.

* A run that completed but produced warnings returns `2`.

* A run that failed returns `1`.

Without the flag, both clean runs and runs-with-warnings return `0`.

## When warnings occur

Warnings are non-fatal: the command finishes, but something worth noting happened. Common causes include:

* **Partial API access**: a resource couldn't be read because the API returned 403 Forbidden or 204 No Content for that item, while other items succeeded.

* **Partial bulk operation failures**: a batch operation completed for most items but failed for some.

* **Missing resources during cleanup**: a delete or cleanup operation encountered a resource that no longer existed.

In all cases the command exits with `0` by default, or `2` when `--detailed-exitcode` is set.

|   |                                                                                                      |
| - | ---------------------------------------------------------------------------------------------------- |
|   | Pipe `stderr` to your log file or CI output to capture the warning messages alongside the exit code. |

## Using return codes in shell scripts

Checking `$?` after a `pingcli` command lets you branch on the result without inspecting output text.

### Fail on error, continue on warning

```bash
pingcli --detailed-exitcode pingone groups list
exit_code=$?

if [ "$exit_code" -eq 1 ]; then
  echo "Command failed. Check the logs." >&2
  exit 1
elif [ "$exit_code" -eq 2 ]; then
  echo "Command completed with warnings. Review output before continuing."
else
  echo "Success."
fi
```

### Treat any non-zero result as a failure

If you want to stop on warnings as well as errors, use `--detailed-exitcode` and check for any non-zero code:

```bash
set -e
pingcli --detailed-exitcode pingone environments list
```

Or check explicitly:

```bash
pingcli --detailed-exitcode pingone environments list
if [ $? -ne 0 ]; then
  echo "Unexpected result — aborting." >&2
  exit 1
fi
```

## Using detailed exit codes in GitHub Actions

The `2` (warning) exit code is useful in CI when you want to flag issues without failing the build. The example below captures warnings as a job summary but lets the workflow continue:

```yaml
jobs:
  sync:
    runs-on: ubuntu-latest
    steps:
      - name: Export PingOne configuration
        id: export
        run: |
          pingcli --detailed-exitcode pingone environments list
          echo "exit_code=$?" >> "$GITHUB_OUTPUT"
        continue-on-error: true

      - name: Fail on error
        if: steps.export.outputs.exit_code == '1'
        run: |
          echo "::error::Ping CLI command failed. Check the step logs for details."
          exit 1

      - name: Annotate warnings
        if: steps.export.outputs.exit_code == '2'
        run: |
          echo "::warning::Ping CLI completed with warnings. Review the export output."
```

In this pattern:

* `continue-on-error: true` prevents GitHub Actions from immediately failing the job so the subsequent steps can inspect the exit code.

* Exit code `1` causes an explicit job failure with an error annotation.

* Exit code `2` surfaces a warning annotation in the Actions UI without failing the pipeline.

## Learn more

* [pingcli pingone groups list](../command_reference/pingcli_pingone_groups_list.html)

* [pingcli pingone environments list](../command_reference/pingcli_pingone_environments_list.html)

* [Configuration settings reference](../settings_reference/configuration-settings-reference.html)

* [Output formats](output-formats.html)

* [Logging](logging.html)

---

---
title: Service authentication
description: Service authentication uses the OAuth 2.0 client credentials flow to authenticate as an application rather than a user. No browser or human interaction is required, making it the right choice for automated and unattended environments.
component: pingcli
version: 1.11
page_id: pingcli:using_pingcli:authenticating-service
canonical_url: https://developer.pingidentity.com/pingcli/1.11/using_pingcli/authenticating-service.html
llms_txt: https://developer.pingidentity.com/pingcli/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 9, 2026
section_ids:
  when-to-use-service-authentication: When to use service authentication
  configuration: Configuration
  no-login-step-required: No login step required
  verify-credentials: Verify credentials
  learn-more: Learn more
---

# Service authentication

Service authentication uses the OAuth 2.0 client credentials flow to authenticate as an application rather than a user. No browser or human interaction is required, making it the right choice for automated and unattended environments.

## When to use service authentication

Use service authentication when:

* Ping CLI is running inside a CI/CD pipeline (for example, GitHub Actions, Jenkins, or similar).

* You are running scheduled or scripted operations where no human operator is present.

* You are using a service account or a dedicated application client rather than a personal administrator account.

## Configuration

Service authentication is configured for each connector when you connect a service to Ping CLI. The relevant setting is `service.<connector>.authentication.type`, which must be set to `client_credentials`. Client credentials (client ID and client secret) are also set at this stage.

If you have not yet connected a service, see [Connect Ping Identity services](connecting-ping-services.html) first.

## No login step required

When client credentials are correctly provided, either through environment variables or a pre-seeded configuration file, Ping CLI authenticates automatically using those credentials whenever it needs to call a service. There is no need to run `auth login` or `auth logout` in this flow; those commands are for interactive user authentication and do not apply to service authentication.

### Verify credentials

To confirm that credentials are present and valid without running a full command, use:

```console
pingcli auth status
```

## Learn more

* [pingcli auth status](../command_reference/pingcli_auth_status.html)

* [Configuration settings reference](../settings_reference/configuration-settings-reference.html)

* [Overview](authenticating-to-services.html)

* [Interactive user sign-on](authenticating-interactive.html)

* [Connect Ping Identity services](connecting-ping-services.html)