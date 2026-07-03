---
title: About ForgeOps deployment monitoring
description: Prometheus, Alertmanager, and Grafana, used for monitoring ForgeOps deployments, are deployed if you run the prometheus-deploy.sh script after performing a ForgeOps deployment. This script installs Helm charts from the prometheus-operator project into the monitoring namespace of a ForgeOps deployment. The Prometheus operator project provides monitoring definitions for Kubernetes services and deployment, and management of Prometheus instances.
component: forgeops
version: 2026.2
page_id: forgeops:prepare:monitoring/monitoring-intro
canonical_url: https://docs.pingidentity.com/forgeops/2026.2/prepare/monitoring/monitoring-intro.html
llms_txt: https://docs.pingidentity.com/forgeops/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
---

# About ForgeOps deployment monitoring

Prometheus, Alertmanager, and Grafana, used for monitoring ForgeOps deployments, are deployed if you run the prometheus-deploy.sh script after performing a ForgeOps deployment. This script installs Helm charts from the [prometheus-operator](https://github.com/coreos/prometheus-operator) project into the `monitoring` namespace of a ForgeOps deployment. The Prometheus operator project provides monitoring definitions for Kubernetes services and deployment, and management of Prometheus instances.

The Helm charts deploy [Kubernetes pods that run the Prometheus and Grafana services](pods.html). The Prometheus operator then watches for service monitor CRDs—Kubernetes custom resource definitions. CRDs are Kubernetes class types that you manage with the kubectl command. The service monitor CRDs define targets to be scraped.

In ForgeOps deployments, the Prometheus operator configuration is defined in the [prometheus-operator.yaml](https://github.com/ForgeRock/forgeops/blob/2026.2.1/cluster/addons/prometheus/prometheus-operator.yaml) file in the `forgeops` repository. For information about how to customize Prometheus, Alertmanager, and Grafana, refer to the [Prometheus README file in the `forgeops` repository](https://github.com/ForgeRock/forgeops/blob/2026.2.1/cluster/addons/prometheus/README.md).

After a ForgeOps deployment is done, you can access the monitoring dashboards. For details, refer to [ForgeOps deployment monitoring](../../deploy/access.html#cdm-monitoring).

|   |                                                                                                                                                                                                                                                                                                                                                                                                      |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Out-of-the-box ForgeOps deployments use Prometheus, Grafana, and Alertmanager for monitoring, reporting, and sending alerts. If you prefer to use different tools, deploy infrastructure in Kubernetes to support those tools.Prometheus and Grafana are evolving technologies. Descriptions of these technologies were accurate at the time of this writing, but might differ when you deploy them. |
