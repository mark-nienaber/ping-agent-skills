---
title: Getting support
description: There are multiple ways to get support when using Ping CLI.
component: pingcli
version: 1.11
page_id: pingcli::getting-support
canonical_url: https://developer.pingidentity.com/pingcli/1.11/getting-support.html
llms_txt: https://developer.pingidentity.com/pingcli/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 2, 2026
---

# Getting support

There are multiple ways to get support when using Ping CLI.

* Community Forum: The Ping Identity [developer community forum](https://support.pingidentity.com/s/community-home) provides a quick and simple way to interact with an active community of subject matter experts, including Ping Identity technical staff, customers, and partner specialists. The community forum is ideal for specific questions on how best to use Ping CLI to meet deployment and development use cases.

* GitHub project issues: Ping CLI has a GitHub repository at [github.com/pingidentity/pingcli](https://github.com/pingidentity/pingcli) and has the GitHub issues feature enabled. With a GitHub account, anyone can create issues on the relevant project by filling in the provided template. Using GitHub project issues is ideal when requesting new features and enhancements or reporting unexpected errors or bugs. The GitHub issues are closely monitored and it's a quick and easy way to interact directly with the project team.

* Ping Identity support: For customers with an active product license, support tickets can be raised according to the normal Ping Identity support process. Raising a support ticket is ideal when there is a potential issue with the underlying product or the issue should be tracked by the account team.

General feedback can be provided to the project team directly using the `pingcli feedback` command.

---

---
title: Ping CLI
description: Ping CLI is a unified Command Line Interface (CLI) tool for developers to manage Ping Identity product deployments and is available on macOS, Linux, and Windows through multiple installation methods, and as a Docker image. Select your platform to get started.
component: pingcli
version: 1.11
page_id: pingcli::pingcli_landing_page
canonical_url: https://developer.pingidentity.com/pingcli/1.11/pingcli_landing_page.html
llms_txt: https://developer.pingidentity.com/pingcli/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 2, 2026
page_aliases: ["_@pingcli::index.adoc"]
section_ids:
  how-it-works: How it works
  capabilities: Capabilities
  features: Features
  get-started: Get started
---

# Ping CLI

Ping CLI is a unified Command Line Interface (CLI) tool for developers to manage Ping Identity product deployments and is available on macOS, Linux, and Windows through multiple installation methods, and as a Docker image. Select your platform to get started.

[icon: apple, set=fab, size=3x]

#### [macOS](install/macos.html)

Install using Homebrew (recommended) or as a standalone binary.

[icon: linux, set=fab, size=3x]

#### [Linux](install/linux.html)

Install using Homebrew, a native package (.apk, .deb, .rpm), or a standalone binary.

[icon: windows, set=fab, size=3x]

#### [Windows](install/windows.html)

Install using a standalone binary download using PowerShell.

[icon: docker, set=fab, size=3x]

#### [Docker](install/docker.html)

Pull the official Ping CLI Docker image from Docker Hub.

## How it works

Ping CLI is a tool for terminal interfaces that is designed to connect to multiple Ping Identity products simultaneously (including PingOne, DaVinci, PingOne MFA, PingOne Protect, PingFederate and more) to manage integrated products as one coherent platform through a common developer interface.

With Ping CLI, developers can automate configuration and management tasks through the use of scripts or embed configuration functions within CI/CD pipelines to facilitate use cases such as configuration promotion, configuration validation, and use case development.

**Get started** by first [installing Ping CLI](using_pingcli/getting-started.html), then use the [interactive setup wizard](using_pingcli/getting-started.html) to configure your first connection, or [manually connect Ping Identity services](using_pingcli/connecting-ping-services.html).

## Capabilities

Ping CLI can do the following:

* [Create, update, delete, and read](using_pingcli/command-structure.html) Ping Identity resources directly from the command line.

* Simplify [making API requests](using_pingcli/making-api-requests.html) from the command line with automatic authentication, base URL injection, and retry handling.

* [Authenticate to all connected services](using_pingcli/authenticating-to-services.html) at once using platform-level auth commands.

## Features

* **Configuration profiles**: Configure and easily switch between one or more configuration profiles when having to manage multiple environments simultaneously.

* **Interactive setup wizard**: Use `pingcli init` to interactively configure connected services without needing to know configuration key names.

* **Multiple authentication flows**: Connect to PingOne using authorization code, client credentials, or device code OAuth 2.0 flows to suit your environment and security requirements.

* **Tab autocompletion**: Use the tab key to prompt autocompletion of configuration settings, product services, and more.

## Get started

Select a service to get step-by-step instructions for connecting Ping CLI and running your first commands.

[icon: id-card, set=fas, size=3x]

#### [PingOne](pingone/getting-started.html)

Connect Ping CLI to a PingOne tenant, configure authentication, and run your first commands.

[icon: terminal, set=fas, size=3x]

#### [General setup](using_pingcli/getting-started.html)

Verify your installation, connect services, authenticate, and understand command structure.

[icon: list, set=fas, size=3x]

#### [Release notes](release_notes/pingcli_release_notes.html)

See what's new in each Ping CLI release, or subscribe to the RSS feed.

---

---
title: Product compatibility
description: The following is a matrix of current compatibility with Ping Identity products. As the Ping CLI project evolves, this matrix will be updated to reflect new compatible products, features and enhancements.
component: pingcli
version: 1.11
page_id: pingcli::product-compatibility
canonical_url: https://developer.pingidentity.com/pingcli/1.11/product-compatibility.html
llms_txt: https://developer.pingidentity.com/pingcli/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 8, 2026
section_ids:
  authentication: Authentication
  feature-resource-management: "Feature: Resource management"
  feature-custom-api-request: "Feature: Custom API request"
---

# Product compatibility

The following is a matrix of current compatibility with Ping Identity products. As the Ping CLI project evolves, this matrix will be updated to reflect new compatible products, features and enhancements.

## Authentication

The following matrix shows which authentication use cases are supported per connector. Refer to each connector's documentation for full configuration details:

| Connector           | Interactive | Automated / CI/CD | Headless | Notes                                |
| ------------------- | ----------- | ----------------- | -------- | ------------------------------------ |
| PingOne             | Yes         | Yes               | Yes      |                                      |
| DaVinci             | Yes         | Yes               | Yes      | Inherited from the PingOne connector |
| PingOne Authorize   | Yes         | Yes               | Yes      | Inherited from the PingOne connector |
| PingOne Credentials | Yes         | Yes               | Yes      | Inherited from the PingOne connector |
| PingOne MFA         | Yes         | Yes               | Yes      | Inherited from the PingOne connector |
| PingOne Protect     | Yes         | Yes               | Yes      | Inherited from the PingOne connector |
| PingOne Verify      | Yes         | Yes               | Yes      | Inherited from the PingOne connector |
| PingFederate        | Yes         | Yes               | Yes      |                                      |

## Feature: Resource management

Ping CLI supports create, read, update, and delete (CRUD) operations for Ping Identity resources directly from the command line. Learn more in [Command structure](using_pingcli/command-structure.html).

|   |                                                                                                                                                                                                                                                                                                                                                                            |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The PingOne universal service connectors (`authorize`, `credentials`, `davinci`, `mfa`, `protect`, `verify`) are accessible both as top-level commands (for example, `pingcli davinci`) and as subcommands of the `pingone` connector (for example, `pingcli pingone davinci`). All universal service connectors use the PingOne connector credentials for authentication. |

| Product             | CLI Connector Name | Available | Example                                                              |
| ------------------- | ------------------ | --------- | -------------------------------------------------------------------- |
| PingOne             | `pingone`          | Yes       | `pingcli pingone <resource> create\|replace\|delete\|get\|list`      |
| DaVinci             | `davinci`          | Yes       | `pingcli davinci <resource> create\|replace\|delete\|get\|list`      |
| PingOne Authorize   | `authorize`        | Yes       | `pingcli authorize <resource> create\|replace\|delete\|get\|list`    |
| PingOne Credentials | `credentials`      | Yes       | `pingcli credentials <resource> create\|replace\|delete\|get\|list`  |
| PingOne MFA         | `mfa`              | Yes       | `pingcli mfa <resource> create\|replace\|delete\|get\|list`          |
| PingOne Protect     | `protect`          | Yes       | `pingcli protect <resource> create\|replace\|delete\|get\|list`      |
| PingOne Verify      | `verify`           | Yes       | `pingcli verify <resource> create\|replace\|delete\|get\|list`       |
| PingFederate        | `pingfederate`     | Yes       | `pingcli pingfederate <resource> create\|replace\|delete\|get\|list` |

## Feature: Custom API request

Ping CLI provides the ability to make custom API requests to a configured Ping Identity product connector, similar to tools such as `curl`. Learn more in [Custom API requests](using_pingcli/making-api-requests.html).

Connectors that support this feature expose an `api` subcommand, for example `pingcli pingone api` or `pingcli pingfederate api`.

Products not listed are not compatible. To request custom API request capability for a specific product not listed, [raise an enhancement request](https://github.com/pingidentity/pingcli/issues/new?template=feature_request.md).

| Product             | Available | Example                                                      |
| ------------------- | --------- | ------------------------------------------------------------ |
| PingOne             | Yes       | `pingcli pingone api`                                        |
| DaVinci             | Yes       | `pingcli pingone api` (Inherited from the PingOne connector) |
| PingOne Authorize   | Yes       | `pingcli pingone api` (Inherited from the PingOne connector) |
| PingOne Credentials | Yes       | `pingcli pingone api` (Inherited from the PingOne connector) |
| PingOne MFA         | Yes       | `pingcli pingone api` (Inherited from the PingOne connector) |
| PingOne Protect     | Yes       | `pingcli pingone api` (Inherited from the PingOne connector) |
| PingOne Verify      | Yes       | `pingcli pingone api` (Inherited from the PingOne connector) |
| PingFederate        | Yes       | `pingcli pingfederate api`                                   |