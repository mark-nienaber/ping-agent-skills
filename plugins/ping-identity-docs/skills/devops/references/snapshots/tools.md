---
title: pingctl kubernetes
description: Deprecated. Reference the pingctl kubernetes command for generating Kubernetes secrets and inspecting cached kubectl OIDC tokens
component: devops
page_id: devops::tools/commands/kubernetes
canonical_url: https://developer.pingidentity.com/devops/tools/commands/kubernetes.html
llms_txt: https://developer.pingidentity.com/devops/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  devops-pingctl-kubernetes: Generate kubernetes resources
  devops-description: Description
  devops-usage: Usage
  devops-options: Options
---

# pingctl kubernetes

|   |                                                                                                                                                                                                                                                                                                                                                                                                        |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | The `pingctl` utility referenced here has been deprecated and is no longer being maintained. It is recommended to use the [Ping CLI](https://developer.pingidentity.com/pingcli/pingcli_landing_page.html) utility under active development and support.With few exceptions, many `pingctl` commands can be replicated using the `pingcli` utility, with gaps being addressed based on prioritization. |

## Generate kubernetes resources

### Description

Manage Ping related Kubernetes resources.

* Generate `devops-secret` secret containing Ping DevOps variables `PING_IDENTITY_DEVOPS_KEY` and `PING_IDENTITY_DEVOPS_SECRET`

* Generate `tls-secret` secret containing a self-signed certificate and key for a specified domain.

* Generate `ssh-id-secret` secret containing a file with ssh id (i.e. \~/.ssh/id\_rsa)

* Generate `license-secret` secret containing a Ping Identity product license file or generated eval license

* Provide details about a cached kubectl oidc token

  * Display the entire jwt token

  * Display a specific claim

  * Clear the kubectl oidc cache

### Usage

```
pingctl kubernetes generate devops-secret
pingctl kubernetes generate tls-secret {domain}
pingctl kubernetes generate ssh-id-secret {ssh id_rsa file}
pingctl kubernetes generate license-secret {license file}
pingctl kubernetes generate license-secret {product} {ver}

pingctl kubernetes oidc clear
pingctl kubernetes oidc {claim}
pingctl kubernetes oidc info
```

### Options

---

---
title: pingctl license
description: Deprecated. Reference the pingctl license command for retrieving Ping Identity evaluation license keys by product name and version
component: devops
page_id: devops::tools/commands/license
canonical_url: https://developer.pingidentity.com/devops/tools/commands/license.html
llms_txt: https://developer.pingidentity.com/devops/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  devops-pingctl-license: Ping Identity license tool
  devops-description: Description
  devops-usage: Usage
  devops-options: Options
---

# pingctl license

|   |                                                                                                                                                                                                                                                                                                                                                                                                        |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | The `pingctl` utility referenced here has been deprecated and is no longer being maintained. It is recommended to use the [Ping CLI](https://developer.pingidentity.com/pingcli/pingcli_landing_page.html) utility under active development and support.With few exceptions, many `pingctl` commands can be replicated using the `pingcli` utility, with gaps being addressed based on prioritization. |

## Ping Identity license tool

### Description

Provides access to Ping Identity evaluation license keys.

* Retrieve license based on product name and version

### Usage

`pingctl license {product} {ver}`

### Options

* product: name of the product

  This name is generally a collapsed one-word representation of the product name. For example: PingFederate is `pingfederate`

* ver: version of the product

  This value is the `major.minor` representation of the version of the product in question. For example, if a product had a point release of `10.2.3` you would provide `10.2`

---

---
title: pingctl pingone
description: Deprecated. Reference the pingctl pingone command for listing, adding, and deleting PingOne resources such as users, populations, and groups
component: devops
page_id: devops::tools/commands/pingone
canonical_url: https://developer.pingidentity.com/devops/tools/commands/pingone.html
llms_txt: https://developer.pingidentity.com/devops/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  devops-pingctl-pingone: Managing PingOne environments
  devops-description: Description
  devops-usage: Usage
  devops-options: Options
  devops-all-subcommands: All subcommands
  devops-get: get
  devops-add: add
---

# pingctl pingone

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The `pingctl` utility referenced here has been deprecated and is no longer being maintained. It is recommended to use the [Ping CLI](https://developer.pingidentity.com/pingcli/pingcli_landing_page.html) utility under active development and support.With few exceptions, `pingctl pingone` commands can be replicated using the `pingcli request --service pingone` subcommand. See [this page](https://developer.pingidentity.com/pingcli/command_reference/pingcli_request.html) for details.Gaps between `pingctl` and `pingcli` are being addressed based on prioritization and equivalent commands from other tools. |

## Managing PingOne environments

### Description

Provides ability to manage PingOne environments. Capabilities of this command include:

* Listing, searching and retrieving PingOne resources (i.e. user, populations, groups)

* Adding PingOne resources

* Deleting PingOne resources

To manage PingOne resources using credentials other than your own, a PingOne Worker App is required. See [this configuration page](../../reference/pingone-config.html) for more details.

### Usage

```none
pingctl pingone get                  # Get PingOne resource(s)
pingctl pingone add                  # Add PingOne resource
pingctl pingone delete               # Delete PingOne resource

pingctl pingone add-user-group       # Add group to user
pingctl pingone delete-user-group    # Delete group from user

pingctl pingone token                # Obtain access token
```

### Options

#### All subcommands

```none
 -r
     Provide REST Calls
```

#### get

```none
-o [ table | csv | json ]
    Output format (default: table)
    also set with env variable: PINGCTL_DEFAULT_OUTPUT

-i {id}
    Search based on object guid

-n {name}
    Search based on exact filter

-f {filter}
    PingOne filter (SCIM based)
        ex: '.name.given eq "john"'
            '.email sw "john"'

-c {columns}
    Columns to output based on "heading:jsonAttr"
    An example of available jsonAttrs can be found by using a json output first.
        ex: 'LastName:name.family,FirstName:name.given'

-s {sort column}
    Columns to sort output on based on "jsonAttr"
    The jsonAttr MUST be listed in the list of columns (-c option).
        ex: 'name.family'

-p {population name}
    Population from which to retrieve a user/group
    If not provided, the 'Default' population is used
```

#### add

```none
 -p {population name}
     Population into which to add a user/group
     If not provided, the 'Default' population is used
```

---

---
title: The <code>ldap-sdk-tools</code> utility
description: Describe the ldap-sdk-tools Docker image that provides LDAP Client SDK tools for use with PingDirectory
component: devops
page_id: devops::tools/ldapsdkUtil
canonical_url: https://developer.pingidentity.com/devops/tools/ldapsdkUtil.html
llms_txt: https://developer.pingidentity.com/devops/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  devops-setting-up-the-utility: Setting up the utility
---

# The `ldap-sdk-tools` utility

The `ldap-sdk-tools` Docker image gives you easy access to our LDAP Client SDK tools for use with PingDirectory.

For complete documentation, see the [`pingidentity/ldapsdk` repository](https://github.com/pingidentity/ldapsdk).

## Setting up the utility

1. From your local `pingidentity-devops-getting-started` directory, enter:

   ```sh
   ./ldapsdk
   ```

   When you run the `ldapsdk` script for the first time, you're prompted to configure your settings.

   To edit the settings in the future, enter:

   `sh ldapsdk configure`

2. To start the `ldap-sdk-tools` Docker image, enter:

   ```sh
   docker run  -it --rm  --network pingnet  pingidentity/ldap-sdk-tools:latest
   ```

3. To list the available tools, enter `ls`.

---

---
title: The pingctl Utility
description: Deprecated. Describe the pingctl command-line utility for DevOps tasks and recommend migrating to the Ping CLI utility
component: devops
page_id: devops::tools/pingctlUtil
canonical_url: https://developer.pingidentity.com/devops/tools/pingctlUtil.html
llms_txt: https://developer.pingidentity.com/devops/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  devops-dependent-utilities: Dependent Utilities
  devops-installation-and-upgrades: Installation and Upgrades
  devops-usage: Usage
  devops-options: Options
  devops-available-commands: Available Commands
---

# The pingctl Utility

|   |                                                                                                                                                                                                                                                                                                                                                                            |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | `pingctl` has been deprecated and is no longer being maintained. It is recommended to use the [Ping CLI](https://developer.pingidentity.com/pingcli/pingcli_landing_page.html) utility under active development and support.With few exceptions, many `pingctl` commands can be replicated using the `pingcli` utility, with gaps being addressed based on prioritization. |

`pingctl` is our general DevOps command-line utility.

## Dependent Utilities

To perform all of its operations, `pingctl` has a dependency on the following utilities:

* openssl

* base64

* kubectl

* envsubst

* jq

* jwt

## Installation and Upgrades

Using Homebrew to install `pingctl` on MacOS, Windows via [Windows Subsystem for Linux](https://docs.microsoft.com/en-us/windows/wsl/install), or Linux.

1. To install, enter:

   ```sh
   brew install pingidentity/tap/pingctl
   ```

   The dependent utilities for `pingctl` are also installed or upgraded during this process.

Using sh to install `pingctl` on Linux and WSL.

1. To install, enter:

   ```sh
   curl -sL https://bit.ly/pingctl-install | sh
   ```

2. Ensure you have the dependent utilities for `pingctl` installed.

## Usage

```
pingctl <command> [options]

Available Commands:
    info            Print pingctl config
    config          Manage pingctl config
    version         Version Details and Check
    clean           Remove ~/.pingidentity/pingctl

    kubernetes      Kubernetes Tools
    license         Ping Identity Licensing Tools
    pingone         PingOne Tools
```

Use `pingctl` for info on available commands.

Use `pingctl <command>` for info on a specific command.

## Options

```
-h
```

Provide usage details.

### Available Commands

* [kubernetes](commands/kubernetes.html)

* [LICENSE](commands/license.html)

* [pingone](commands/pingone.html)

* info

  Provides a summary of variables defined with pingctl.

* config

  Provides an interactive process in which the user can provide all the `pingctl` standard variables (i.e. PingOne and Ping DevOps) as well as custom variables

* version

  Displays the current version of the tool, and checks to see if an update is available.

* clean

  Cleans the cached pingctl work directory containing the latest PingOne Access Token