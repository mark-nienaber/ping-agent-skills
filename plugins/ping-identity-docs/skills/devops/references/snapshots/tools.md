---
title: pingctl kubernetes
description: The pingctl utility referenced here has been deprecated and is no longer being maintained. It is recommended to use the Ping CLI utility under active development and support.
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
