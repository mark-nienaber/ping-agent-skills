---
title: Contributing to the Ping Identity DevOps Program
description: Explains how to report bugs or suggest enhancements for the Ping Identity Helm charts
component: helm
page_id: helm::getting-started/feedback
canonical_url: https://developer.pingidentity.com/helm/getting-started/feedback.html
llms_txt: https://developer.pingidentity.com/helm/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  reporting-bugs: Reporting Bugs
  suggesting-enhancements: Suggesting Enhancements
  contributing-code-changes: Contributing Code Changes
---

# Contributing to the Ping Identity DevOps Program

Thanks for taking the time to help us improve our Helm chart!

You can contribute in various ways.

## Reporting Bugs

Bugs are tracked as [GitHub issues](https://github.com/pingidentity/helm-charts/issues/). You can report a bug by submitting an issue in the project's issue tracker. To help the maintainers understand and reproduce the problem, please try to provide detailed information, including:

* A clear and descriptive title.

* A description of what happened and what you expected to happen.

* An example with the exact steps needed to reproduce the problem. If relevant, sample code is helpful.

Please understand that bug reports are reviewed and prioritized internally, and we may not be able to address all bug reports or provide an estimated time for resolution.

## Suggesting Enhancements

As with bugs, requests are tracked as [GitHub issues](https://github.com/pingidentity/helm-charts/issues/). You can suggest an enhancement by submitting an issue in the project's issue tracker.

Please understand that enhancement requests are handled in the same way as bug reports, and we may not be able to address all enhancement requests or provide an estimated time for resolution.

|   |                                                                                                                                                      |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | If you would rather not have your issue discussed in public, you can email bug reports or enhancement requests to <devops_program@pingidentity.com>. |

## Contributing Code Changes

Ping Identity does not accept third-party code submissions.

---

---
title: Getting Started
description: Install Helm, add the Ping Identity repository, and deploy the ping-devops chart for the first time
component: helm
page_id: helm::getting-started/getting-started
canonical_url: https://developer.pingidentity.com/helm/getting-started/getting-started.html
llms_txt: https://developer.pingidentity.com/helm/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
page_aliases: ["getting-started:index.adoc"]
section_ids:
  prerequisites: Prerequisites
  creating-ping-devops-secret: Creating Ping DevOps Secret
  installing-helm-3: Installing Helm 3
  adding-helm-ping-devops-repo: Adding Helm Ping DevOps Repo
  listing-ping-devops-charts: Listing Ping DevOps Charts
  updating-local-machine-with-the-latest-charts: Updating Local Machine with the Latest Charts
  installing-the-ping-devops-chart: Installing the Ping DevOps Chart
  accessing-deployments: Accessing Deployments
  uninstalling-releases: Uninstalling Releases
---

# Getting Started

[Helm](https://helm.sh) is a package deployment tool for [Kubernetes](https://kubernetes.io). It can be used with [Ping DevOps](https://developer.pingidentity.com/devops/) to deploy all the components of the solution with a simple command.

## Prerequisites

* Kubernetes Cluster

* Helm 3

* Ping Identity DevOps user/key

|   |                                                                                                                                                              |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | Ping Helm charts support OpenShift. See [OpenShift Configuration](../configs/openshift-config.html) to learn how to configure the values.yaml file to do so. |

## Creating Ping DevOps Secret

The charts use a secret called `devops-secret` to obtain an evaluation license for running images.

* Eval License — Use your `PING_IDENTITY_DEVOPS_USER/PING_IDENTITY_DEVOPS_KEY` credentials along with your `PING_IDENTITY_ACCEPT_EULA` setting.

* For more information on obtaining credentials, click [here](https://developer.pingidentity.com/devops/how-to/devopsRegistration.html).

* For more information on using the `pingctl` utility, click [here](https://developer.pingidentity.com/devops/tools/pingctlUtil.html).

  ```none
  pingctl k8s generate devops-secret | kubectl apply -f -
  ```

## Installing Helm 3

Ensure that you have Helm 3 installed.

* Installing on macOS (or Linux with Brew):

  `brew install helm`

* Installing on other OS:

  <https://helm.sh/docs/intro/install/>

## Adding Helm Ping DevOps Repo

```none
helm repo add pingidentity https://helm.pingidentity.com/
```

## Listing Ping DevOps Charts

```none
helm search repo pingidentity
```

## Updating Local Machine with the Latest Charts

```none
helm repo update
```

## Installing the Ping DevOps Chart

Install the `ping-devops` chart using the example below. In this case, it is installing a release called `pf`:

* PingFederate Admin instance

* PingFederate Engine instance

```none
helm install pf pingidentity/ping-devops \
   --set pingfederate-admin.enabled=true \
   --set pingfederate-engine.enabled=true
```

or, if you have a `ping-devops-values.yaml` file:

```[yaml]
# ping-devops-values.yaml
pingfederate-admin:
  enabled: true

pingfederate-engine:
enabled: true
```

```none
helm install pf pingidentity/ping-devops \
-f ping-devops-values.yaml
```

## Accessing Deployments

[By default](../configs/global.html), the components of a release are prefixed with the release name. Continuing this example, everything will be prefixed with `pf`. Use `kubectl` to see the pods created.

View Kubernetes resources installed:

```none
# get just pods
kubectl get pods --selector=app.kubernetes.io/instance=pf

# or get even more
kubectl get all --selector=app.kubernetes.io/instance=pf
```

View logs (from deployment):

```none
kubectl logs deployment/pf-pingfederate-admin
```

## Uninstalling Releases

To uninstall a release from Helm, use the following command (using `pf` as an example release):

```none
helm uninstall pf
```