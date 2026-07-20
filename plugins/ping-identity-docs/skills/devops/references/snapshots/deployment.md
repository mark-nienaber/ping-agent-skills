---
title: Azure Kubernetes Service
description: Deploy the Ping Identity DevOps full-stack example to Azure Kubernetes Service (AKS) using the Azure CLI and Helm
component: devops
page_id: devops::deployment/deployK8s-AKS
canonical_url: https://developer.pingidentity.com/devops/deployment/deployK8s-AKS.html
llms_txt: https://developer.pingidentity.com/devops/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  devops-preparing-azure-kubernetes-service: Preparing Azure Kubernetes Service
  devops-prerequisites: Prerequisites
  devops-deploying-our-fullstack-example-in-aks: Deploying our fullstack example in AKS
---

# Azure Kubernetes Service

## Preparing Azure Kubernetes Service

This directory contains scripts and deployment files to help with the deployment, management, and scaling of Ping Identity DevOps Docker images to Microsoft Azure Kubernetes Service (AKS).

### Prerequisites

Before you begin, you must:

* Set up your DevOps environment and run a test deployment of the products. For more information, see [Get Started](../get-started/introduction.html).

* Create a Kubernetes cluster on AKS.

* Create a Kubernetes secret using your DevOps credentials. See the *For Kubernetes* topic in [Using your DevOps user and key](../how-to/devopsUserKey.html).

* Download and install the [Azure CLI](https://docs.microsoft.com/cli/azure/install-azure-cli).

We also highly recommend you are familiar with the information in these AKS articles:

* [Azure Kubernetes Service](https://docs.microsoft.com/en-us/azure/aks/intro-kubernetes)

### Deploying our fullstack example in AKS

1. Create an Azure Resource Group to put all resources into by entering:

   ```
   az group create \
      --name ping-devops-rg \
      --location westus
   ```

2. Create a two-node Azure AKS cluster by entering the following.

   ```
   az aks create \
      --resource-group ping-devops-rg \
      --name ping-devops-cluster \
      --node-count 2 \
      --enable-addons monitoring \
      --ssh-key-value ~/.ssh/id_rsa.pub
   ```

   You need a public certificate by default in \~/.ssh/id\_rsa.pub.

3. Import the AKS Credentials into `.kube/config` by entering:

   ```
   az aks get-credentials \
      --resource-group ping-devops-rg \
      --name ping-devops-cluster
   ```

4. At this point, the cluster should be ready for helm deployments.

5. To clean up the Azure Resource Group and all associated resources, including the AKS cluster created, enter the following command:

   |   |                                                                                      |
   | - | ------------------------------------------------------------------------------------ |
   |   | This will remove everything you created that is associated with this resource group. |

   ```
   az group delete \
     --name ping-devops-rg
   ```

---

---
title: Deploy a Kubernetes Cluster Metrics Stack
description: Deploy a sample Prometheus, Grafana, and Telegraf monitoring stack in Kubernetes to collect and visualize metrics from Ping products
component: devops
page_id: devops::deployment/deployK8sClusterMetrics
canonical_url: https://developer.pingidentity.com/devops/deployment/deployK8sClusterMetrics.html
llms_txt: https://developer.pingidentity.com/devops/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  devops-stack-components: Stack Components
  devops-prerequisites: Prerequisites
  devops-deploy-the-stack: Deploy the Stack
  devops-view-metrics: View Metrics
  devops-horizontalpodautoscaler: HorizontalPodAutoscaler
---

# Deploy a Kubernetes Cluster Metrics Stack

![cluster metrics stack](../_images/cluster-metrics-stack.png)

This document demonstrates the process of deploying and using a sample open-source monitoring stack in a Kubernetes cluster.

|   |                                                                                                                                                                                                                                                      |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The resulting environment is not production-ready. It is only intended to show how Ping software can produce metrics for consumption by a popular open-source monitoring system. This example stack is not maintained or directly supported by Ping. |

## Stack Components

**Open Source Tools**

* [kube-prometheus-stack](https://github.com/prometheus-community/helm-charts/tree/main/charts/kube-prometheus-stack), which includes:

  * [Prometheus](https://prometheus.io/) - Metrics collection and storage

  * [Grafana](https://grafana.com/) - Metrics visualization in Dashboards

  * [telegraf-operator](https://github.com/influxdata/helm-charts/tree/master/charts/telegraf-operator) - Metrics exposure and formatting

**Grafana Dashboard** - JSON file to import for dashboard definition

**Ping-provided values.yaml** - Values relevant to exposing metrics for Ping Identity software

## Prerequisites

* Familiarity with the prerequisites for the base [Helm examples](https://developer.pingidentity.com/helm/examples/index.html)

* Working knowledge of Prometheus, Grafana, and Telegraf

## Deploy the Stack

In the `pingidentity-devops-getting-started/30-helm/cluster-metrics directory` of this repository, edit the `01-prometheus-values.yaml` as needed. This file provides configurations beyond the default kube-prometheus-stack. In this sample deployment, the monitoring stack is granted read access to the entire cluster and is deployed into the `metrics` namespace.

|   |                                                                                                                                                                                                         |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Altering these settings or making the deployment production-ready is beyond the scope of this document. The full set of optional values can be found on the Github repository for the Prometheus chart. |

There are numerous lines that have `##CHANGEME`. These lines should be considered for configuration options to meet your needs.

After updating the file, deploy the `kube-prometheus-stack`. The path to the configuration file assumes you are in the root folder of a local copy of the [Getting Started](https://github.com/pingidentity/pingidentity-devops-getting-started) repository:

```sh
kubectl create namespace metrics

helm repo add prometheus-community https://prometheus-community.github.io/helm-charts

helm repo update

helm upgrade --install metrics prometheus-community/kube-prometheus-stack -f 30-helm/cluster-metrics/01-prometheus-values.yaml -n metrics --version 57.2.0
```

Deploy `telegraf-operator`:

```bash
helm repo add influxdata https://helm.influxdata.com/

helm upgrade --install telegraf influxdata/telegraf-operator -n metrics --version 1.3.11 -f 30-helm/cluster-metrics/02-telegraf-values.yaml
```

Telegraf operator makes it very easy to add monitoring sidecars to your deployments. All you need to do is add annotations, which are shown in `30-helm/cluster-metrics/03-ping-with-metrics-values.yaml`

These values can be copied to your `values.yaml` manually, or the file can be referenced at the end of your helm install command. For example:

`helm upgrade --install ping-metrics pingidentity/ping-devops -f my-values.yaml -f 30-helm/cluster-metrics/03-ping-with-metrics-values.yaml`

After the Ping software is healthy and producing metrics, there should be sidecars on Ping pods.

```
NAME                                                 READY   STATUS
ping-metrics-pingaccess-admin-0                      1/1     Running
ping-metrics-pingaccess-engine-68464d8cc8-mhlsv      2/2     Running
ping-metrics-pingdataconsole-559786c98f-8wsrm        1/1     Running
ping-metrics-pingdirectory-0                         2/2     Running
ping-metrics-pingfederate-admin-64fdb4b975-2xdjl     1/1     Running
ping-metrics-pingfederate-engine-64c5f896c7-fn99v    2/2     Running
```

Note the `2/2` indicator for pods with sidecars.

## View Metrics

Browse to Grafana using the Ingress URL or by running a `kubectl port-forward` command. For example: `kubectl port-forward svc/metrics-grafana --namespace metrics 9000:80`.

In your browser, navigate to `http://localhost:9000` and log in with the user `admin` and the password set in `01-prometheus-values.yaml`.

Finally, import the `04-ping-overview-dashboard.json` using the **New** button at the top right of the Dashboard landing page in Grafana.

The `Ping Identity Overview` dashboard will have a dropdown for namespace at the top. Select the namespace running Ping products to see something similar to this example:

![cluster metrics dashboard](../_images/cluster-metrics-dashboard.png)

Any of the panels can be edited, or new ones created to fit your needs.

## HorizontalPodAutoscaler

If you use the `autoscaling/v2` API version, you can configure a HorizontalPodAutoscaler to scale based on a custom metric not built in to Kubernetes or any Kubernetes component. If you are using our [Helm Charts](https://github.com/pingidentity/helm-charts), you can pass the custom metrics under `global.cluster.autoscalingMetricsTemplate`. The example code here will scale on a requests-per-second threshold of 10,000:

```
  - type: Pods
    pods:
     metric:
       name: custom-metric
     target:
       type: AverageValue
       averageValue: 10000m
  - type: Resource
    resource:
      name: cpu
      target:
        type: Utilization
        averageUtilization: 50
  - type: Object
    object:
      metric:
        name: requests-per-second
      describedObject:
        apiVersion: networking.k8s.io/v1
        kind: Ingress
        name: main-route
      current:
        value: 10k
```

In addition, you can define the behaviors for scaling up and down under `global.cluster.autoscaling.behavior`.

```
  scaleDown:
    stabilizationWindowSeconds: 300
    policies:
    - type: Percent
      value: 100
      periodSeconds: 15
  scaleUp:
    stabilizationWindowSeconds: 0
    policies:
    - type: Percent
      value: 100
      periodSeconds: 15
    - type: Pods
      value: 4
      periodSeconds: 15
    selectPolicy: Max
```

For more information on custom HPA metrics please visit [Kubernetes](https://kubernetes.io/docs/tasks/run-application/horizontal-pod-autoscale/#scaling-on-custom-metrics)

---

---
title: Deploy a local Kubernetes Cluster
description: Deploy a local Kubernetes cluster using kind or minikube with Traefik ingress to test and evaluate Ping product Helm deployments
component: devops
page_id: devops::deployment/deployLocalK8sCluster
canonical_url: https://developer.pingidentity.com/devops/deployment/deployLocalK8sCluster.html
llms_txt: https://developer.pingidentity.com/devops/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  kind-cluster: Kind cluster
  prerequisites: Prerequisites
  devops-install-and-confirm-the-cluster: Install and confirm the cluster
  devops-enable-ingress: Enable ingress with Traefik
  devops-deploy-the-example-stack: Deploy the Example Stack
  devops-stop-the-cluster: Stop the cluster
  minikube-cluster: Minikube cluster
  devops-prerequisites: Prerequisites
  devops-install-and-configure-minikube: Install and configure minikube
  devops-enable-ingress-with-traefik: Enable ingress with Traefik
  devops-deploy-the-example-stack-2: Deploy the Example Stack
  devops-optional-features: Optional features
  devops-dashboard: Dashboard
  devops-multiple-nodes: Multiple nodes
  devops-stop-the-cluster-2: Stop the cluster
---

# Deploy a local Kubernetes Cluster

If you do not have access to a managed Kubernetes cluster you can deploy one on your local machine or or a virtual machine (VM). This document describes deploying a cluster with [kind](https://kind.sigs.k8s.io/) and also for [minikube](https://minikube.sigs.k8s.io/docs/). Refer to the documentation of each product for additional information.

|   |                                                                                                         |
| - | ------------------------------------------------------------------------------------------------------- |
|   | The instructions in this document are for testing and learning, and not intended for use in production. |

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The processes outlined on this page will create either a Kubernetes in Docker ([kind](https://kind.sigs.k8s.io/)) or a [minikube](https://minikube.sigs.k8s.io/docs/) cluster. In both cases, the cluster you get is very similar in functionality to the Docker Desktop implementation of Kubernetes. However, a distinct advantage of both offerings is portability (not requiring Docker Desktop). As with the [Deploy an Example Stack](../get-started/getStartedExample.html) procedure, the files provided will enable and deploy an ingress controller for communicating with the services in the cluster from your local environment. |

|   |                                                                                                                                      |
| - | ------------------------------------------------------------------------------------------------------------------------------------ |
|   | To use the both examples below, you will need to ensure the Kubernetes feature of Docker Desktop is turned off, as it will conflict. |

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | This note applies only if using Docker as a backing for either solution. kind uses Docker by default, and it is also an option for minikube. Docker on Linux is typically installed with root privileges and thus has access to the full resources of the machine. Docker Desktop for Mac and Windows provides a way to set the resources allocated to Docker. For this documentation, a Macbook Pro with the Apple silicon chipset was configured to use 6 CPUs and 12 GB Memory. You can adjust these values as necessary for your needs. |

## Kind cluster

This section will cover the **kind** installation process. See the [Minikube cluster](#minikube-cluster) section for minikube instructions.

### Prerequisites

* [docker](https://docs.docker.com/get-docker/)

* [kubectl](https://kubernetes.io/docs/tasks/tools/#kubectl)

* ports 80 and 443 available on machine (optional but recommended for standard URLs)

|   |                                                                                         |
| - | --------------------------------------------------------------------------------------- |
|   | For this guide, Kubernetes 1.35.0 is used. It is deployed using version 0.31.0 of kind. |

|   |                                                                                                                         |
| - | ----------------------------------------------------------------------------------------------------------------------- |
|   | At the time of the writing of this guide, Docker Desktop was version `4.46.0 (204649)`, running Docker Engine `28.4.0`. |

|   |                                                                                        |
| - | -------------------------------------------------------------------------------------- |
|   | We install Traefik as the ingress controller to align with the Docker Desktop example. |

### Install and confirm the cluster

1. [Install kind](https://kind.sigs.k8s.io/docs/user/quick-start/#installation) on your platform.

2. Use the provided [sample kind.yaml](https://github.com/pingidentity/pingidentity-devops-getting-started/blob/master/20-kubernetes/kind.yaml) file to create a kind cluster named `ping`. The config maps host ports 80/443 into the kind control-plane node and forwards them to Traefik NodePorts (30080/30443) so Traefik can serve standard URLs. From the root of your copy of the repository code, run the wrapper script:

```shell
./20-kubernetes/create-kind-cluster.sh
```

|   |                                                                     |
| - | ------------------------------------------------------------------- |
|   | If the cluster already exists, the script deletes and recreates it. |

Output:

```shell
Creating cluster "ping" ...
 ✓ Ensuring node image (kindest/node:v1.35.0) 🖼
 ✓ Preparing nodes 📦
 ✓ Writing configuration 📜
 ✓ Starting control-plane 🕹️
 ✓ Installing CNI 🔌
 ✓ Installing StorageClass 💾
Set kubectl context to "kind-ping"
You can now use your cluster with:

kubectl cluster-info --context kind-ping

Have a nice day! 👋
```

1. Test cluster health by running the following commands:

   ```
   kubectl cluster-info

   # Output - port will vary
   Kubernetes control plane is running at https://127.0.0.1:64129
   CoreDNS is running at https://127.0.0.1:64129/api/v1/namespaces/kube-system/services/kube-dns:dns/proxy

   To further debug and diagnose cluster problems, use 'kubectl cluster-info dump'.

   ------------------

   kubectl version

   < output clipped >
   Server Version: v1.35.0

   ------------------

   kubectl get nodes

   NAME                 STATUS   ROLES           AGE     VERSION
   ping-control-plane   Ready    control-plane   55m     v1.35.0
   ```

### Enable ingress with Traefik

1. Install Traefik to handle Ingress resources:

   ```shell
   helm repo add traefik https://helm.traefik.io/traefik
   helm repo update
   helm upgrade --install traefik traefik/traefik \
     --namespace traefik --create-namespace \
     -f ./30-helm/ingress-traefik-values-kind.yaml
   ```

   |   |                                                                                                                                                                                                       |
   | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | The values file used to configure Traefik is set to skip backend TLS verification so the Ping product consoles with self-signed certificates work via Traefik. Do not use this setting in production. |

2. Wait for Traefik to be ready:

   ```shell
   kubectl get pods --namespace traefik
   ```

Our examples will use the Helm release name `myping` and DNS domain suffix `pingdemo.example` for accessing applications. After the Ingress resources exist, add all expected hosts to `/etc/hosts`. When using host ports 80/443 (recommended), map the hosts to `127.0.0.1`:

```shell
echo "127.0.0.1 myping-pingaccess-admin.pingdemo.example myping-pingaccess-engine.pingdemo.example myping-pingauthorize.pingdemo.example myping-pingauthorizepap.pingdemo.example myping-pingdataconsole.pingdemo.example myping-pingdelegator.pingdemo.example myping-pingdirectory.pingdemo.example myping-pingfederate-admin.pingdemo.example myping-pingfederate-engine.pingdemo.example myping-pingcentral.pingdemo.example" | sudo tee -a /etc/hosts > /dev/null
```

|   |                                                                                                                                          |
| - | ---------------------------------------------------------------------------------------------------------------------------------------- |
|   | If ports 80/443 are not available, remove the `extraPortMappings` from `kind.yaml` and use the Traefik NodePorts (30080/30443) directly. |

Setup is complete. This local Kubernetes environment should be ready to deploy our [Helm examples](https://developer.pingidentity.com/helm/examples/index.html).

### Deploy the Example Stack

1. Create a namespace for running the stack in your Kubernetes cluster:

   ```
   # Create the namespace
   kubectl create ns pinghelm

   # Set the kubectl context to the namespace
   kubectl config set-context --current --namespace=pinghelm

   # Confirm
   kubectl config view --minify | grep namespace:
   ```

2. Create a secret in the namespace you will be using to run the example (pinghelm) using the `pingctl` utility. This secret will obtain an evaluation license based on your Ping DevOps username and key:

   ```sh
   kubectl create secret generic devops-secret \
     --from-literal=PING_IDENTITY_DEVOPS_USER="$PING_IDENTITY_DEVOPS_USER" \
     --from-literal=PING_IDENTITY_DEVOPS_KEY="$PING_IDENTITY_DEVOPS_KEY" \
     --from-literal=PING_IDENTITY_ACCEPT_EULA="$PING_IDENTITY_ACCEPT_EULA" \
     --type=Opaque \
     --dry-run=client -o yaml | kubectl apply -f -
   ```

3. To install the chart, go to your local `"${PING_IDENTITY_DEVOPS_HOME}"/pingidentity-devops-getting-started/30-helm` directory and run the command shown here. In this example, the release (deployment into Kubernetes by Helm) is called `myping`, forming the prefix for all objects created. The `ingress-demo-kind.yaml` file configures the ingresses to use the Traefik ingress class:

   `helm upgrade --install myping pingidentity/ping-devops -f everything.yaml -f ingress-demo-kind.yaml`

At this point, the flow will be the same as found in the [Getting Started Example](../get-started/getStartedExample.html) after the products are deployed using helm. The URLs will be prefaced with `myping` rather than `demo`.

### Stop the cluster

When you are finished, you can remove the cluster by running the following command, which removes the cluster completely. You will be required to recreate the cluster to use `kind` again.

`kind delete cluster --name ping`

## Minikube cluster

In this section, a minikube installation with ingress is created. Minikube is simpler than kind overall to configure, but ends up needing one step to configured a tunnel to the cluster that must be managed. For this guide, the Docker driver will be used. As with `kind` above, Kubernetes in Docker Desktop must be disabled.

### Prerequisites

* Container or virtual machine manager, such as: [Docker](https://minikube.sigs.k8s.io/docs/drivers/docker/), [QEMU](https://minikube.sigs.k8s.io/docs/drivers/qemu/), [Hyperkit](https://minikube.sigs.k8s.io/docs/drivers/hyperkit/), [Hyper-V](https://minikube.sigs.k8s.io/docs/drivers/hyperv/), [KVM](https://minikube.sigs.k8s.io/docs/drivers/kvm2/), [Parallels](https://minikube.sigs.k8s.io/docs/drivers/parallels/), [Podman](https://minikube.sigs.k8s.io/docs/drivers/podman/), [VirtualBox](https://minikube.sigs.k8s.io/docs/drivers/virtualbox/), or [VMware Fusion/Workstation](https://minikube.sigs.k8s.io/docs/drivers/vmware/)

* [kubectl](https://kubernetes.io/docs/tasks/tools/#kubectl)

|   |                                                                                                                      |
| - | -------------------------------------------------------------------------------------------------------------------- |
|   | At the time of the writing of this guide, minikube was version `1.38.0`, which installs Kubernetes version `1.35.0`. |

### Install and configure minikube

1. Install minikube for your platform. See the product [Get Started!](https://minikube.sigs.k8s.io/docs/start/) page for details.

2. Configure the minikube resources and virtualization driver. For example, the following options were used on an Apple Macbook Pro with Docker as the backing platform:

   ```
   minikube config set cpus 6
   minikube config set driver docker
   minikube config set memory 12g
   ```

   |   |                                                                                                                       |
   | - | --------------------------------------------------------------------------------------------------------------------- |
   |   | See [the documentation](https://minikube.sigs.k8s.io/docs/handbook/config/) for more details on configuring minikube. |

3. Start the cluster. Optionally you can include a profile flag (`--profile <name>`). Naming the cluster enables you to run multiple minikube clusters simultaneously. If you use a profile name, you will need to include it on other minikube commands.

   `minikube start --kubernetes-version=v1.35.0`

   Output:

```shell
😄  minikube v1.38.0 on Darwin 26.2 (arm64)
✨  Using the docker driver based on user configuration
❗  Starting v1.39.0, minikube will default to "containerd" container runtime. See #21973 for more info.
📌  Using Docker Desktop driver with root privileges
👍  Starting "minikube" primary control-plane node in "minikube" cluster
🚜  Pulling base image v0.0.49 ...
🔥  Creating docker container (CPUs=6, Memory=12288MB) ...
🐳  Preparing Kubernetes v1.35.0 on Docker 29.2.0 ...
🔗  Configuring bridge CNI (Container Networking Interface) ...
🔎  Verifying Kubernetes components...
    ▪ Using image gcr.io/k8s-minikube/storage-provisioner:v5
🌟  Enabled addons: storage-provisioner, default-storageclass
🏄  Done! kubectl is now configured to use "minikube" cluster and "default" namespace by default
```

1. Test cluster health by running the following commands:

   ```
   kubectl cluster-info

   # Output - Port will vary
   Kubernetes control plane is running at https://127.0.0.1:51042
   CoreDNS is running at https://127.0.0.1:51042/api/v1/namespaces/kube-system/services/kube-dns:dns/proxy

   To further debug and diagnose cluster problems, use 'kubectl cluster-info dump'.

   ------------------

   kubectl version

   < output clipped >
   Server Version: v1.35.0

   ------------------

   kubectl get nodes

   NAME       STATUS   ROLES           AGE    VERSION
   minikube   Ready    control-plane   6m2s   v1.35.0
   ```

### Enable ingress with Traefik

1. Install ingress:

   ```
   helm upgrade --install traefik traefik/traefik \
       --namespace traefik --create-namespace \
       -f 30-helm/ingress-traefik-values.yaml

   Release "traefik" does not exist. Installing it now.
   NAME: traefik
   LAST DEPLOYED: Thu Feb 12 11:24:51 2026
   NAMESPACE: traefik
   STATUS: deployed
   REVISION: 1
   DESCRIPTION: Install complete
   TEST SUITE: None
   NOTES:
   traefik with docker.io/traefik:v3.6.7 has been deployed successfully on traefik namespace!
   ```

2. Confirm ingress is operational:

   ```
   kubectl get po -n traefik

   NAME                       READY   STATUS    RESTARTS   AGE
   traefik-79b96fcb9b-qp99r   1/1     Running   0          2m31s
   ```

3. Start a tunnel. This command will tie up the terminal:

   ```sh
   minikube tunnel

   ✅  Tunnel successfully started

   📌  NOTE: Please do not close this terminal as this process must stay alive for the tunnel to be accessible ...

   ❗  The service/ingress traefik requires privileged ports to be exposed: [80 443]
   🔑  sudo permission will be asked for it.
   🔗  Starting tunnel for service traefik.
   ```

   Our examples will use the Helm release name `myping` and DNS domain suffix `pingdemo.example` for accessing applications. You can add all expected hosts to `/etc/hosts`:

```sh
echo '127.0.0.1 myping-pingaccess-admin.pingdemo.example myping-pingaccess-engine.pingdemo.example myping-pingauthorize.pingdemo.example myping-pingauthorizepap.pingdemo.example myping-pingdataconsole.pingdemo.example myping-pingdelegator.pingdemo.example myping-pingdirectory.pingdemo.example myping-pingfederate-admin.pingdemo.example myping-pingfederate-engine.pingdemo.example myping-pingcentral.pingdemo.example' | sudo tee -a /etc/hosts > /dev/null
```

Setup is complete.

### Deploy the Example Stack

This local Kubernetes environment should be ready to deploy the stack as you did above for `kind`. The only difference is to use the other ingress-demo values file for minikube:

`helm upgrade --install myping pingidentity/ping-devops -f everything.yaml -f ingress-demo.yaml`

### Optional features

#### Dashboard

Minikube provides other add-ons that enhance your experience when working with your cluster. One such add-on is the Dashboard, which can also provide metrics as follows:

`minikube addons enable metrics-server minikube dashboard`

#### Multiple nodes

If you have enough system resources, you can create a multi-node cluster.

For example, to start a 3-node cluster:

`minikube start --nodes 3`

|   |                                                                                                                                                                                         |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Keep in mind that each node will receive the RAM/CPU/Disk configured for minikube. Using the example configuration provided above, a 3-node cluster would need 36GB of RAM and 18 CPUs. |

### Stop the cluster

When you are finished, you can stop the cluster by running the following command. Stopping retains the configuration and state of the cluster (namespaces, deployments, and so on) that will be restored when starting the cluster again.

`minikube stop`

You can also pause and unpause the cluster:

`minikube pause minikube unpause`

Alternatively, you can delete the minikube environment, which will do a reset and recreate everything the next time it is started.

`minikube delete`

---

---
title: Deploy a Local Openshift Cluster
description: Deploy a local Red Hat Openshift Local (crc) cluster for testing and install Ping products using Helm charts
component: devops
page_id: devops::deployment/deployLocalOpenshift
canonical_url: https://developer.pingidentity.com/devops/deployment/deployLocalOpenshift.html
llms_txt: https://developer.pingidentity.com/devops/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  devops-prerequisites: Prerequisites
  devops-configuration-and-setup: Configuration and Setup
  devops-stop-the-red-hat-openshift-local-instance: Stop the Red Hat Openshift Local instance
  devops-delete-the-red-hat-openshift-local-instance: Delete the Red Hat Openshift Local instance
---

# Deploy a Local Openshift Cluster

|   |                                                                                                         |
| - | ------------------------------------------------------------------------------------------------------- |
|   | The instructions in this document are for testing and learning, and not intended for use in production. |

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | Openshift is a licensed product following the open source model where "upstream" versions are available under community licensing, but the official release supported by [Red Hat](https://www.redhat.com/en) requires a subscription in order to access the software for installation. This guide assumes the user has access to such a license. Red Hat provides a [free Developer account](https://developers.redhat.com/blog/2016/03/31/no-cost-rhel-developer-subscription-now-available) that allows a participant to obtain a 60-day license of the Openshift product at no charge. |

|   |                                                                                                                                                                                         |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | A video demonstration of the process outlined on this page is available [here](https://videos.pingidentity.com/detail/videos/devops/video/6319613511112/openshift-local-demonstration). |

Some customers are using Openshift as their platform for running Ping containerized applications. If this is the case, access to an Openshift cluster is assumed. Even in those cases, there are times where a local implementation of Openshift for development and testing is convenient.

|   |                                                                                                                                                                          |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | For this guide, the Apple MacBook Pro M4 platform is used, and the release of the *Red Hat Openshift Local* offering is version 2.49.0, which installs Openshift 4.18.2. |

The [Openshift Local](https://developers.redhat.com/products/openshift-local/overview) offering is used in this guide.

## Prerequisites

* Entitlement for Openshift code. If you have registered for the Red Hat developer program, you can obtain your entitlement for the free trial [from the portal](https://developers.redhat.com/products/openshift/download) after logging in.

* [kubectl](https://kubernetes.io/docs/tasks/tools/#kubectl)

* [Openshift client (oc)](https://access.redhat.com/documentation/en-us/openshift_container_platform/4.17/html-single/cli_tools/index#cli-getting-started)

* ports 80, 443 and 6443 available on machine. If you have Docker Desktop installed, you must either disable Kubernetes or stop Docker in order for the installation to work.

* **sudo** privileges on your hosting environment

## Configuration and Setup

1. [Install the Red Hat Openshift Local binary](https://console.redhat.com/openshift/create/local) for your platform. When you download the installer, also download the pull secret.

2. With the `crc` utility installed, configure settings. Provide as much RAM and CPU as you can, depending on your system. In this example, 20 GB of RAM, 9 vCPUs, and a disk size of 80GB are set. The consent-telemetry is optional, depending on whether you consent to usage data metrics being sent to Red Hat.

   ```
   # Version information
   crc version

   # Output
   CRC version: 2.49.0+e843be
   OpenShift version: 4.18.2
   MicroShift version: 4.18.2

   # Set configuration
   crc config set memory 20480
   crc config set cpus 9
   crc config set consent-telemetry no
   crc config set disk-size 80
   crc config set pull-secret-file <path>/pull-secret.txt

   # Confirm
   crc config view

   - consent-telemetry                     : no
   - cpus                                  : 9
   - disk-size                             : 80
   - memory                                : 20480
   - pull-secret-file                      : <path>/pull-secret.txt
   ```

3. Set up your local machine for running Red Hat Openshift Local by running **crc setup**:

   ```
   crc setup

   # Output
   INFO Using bundle path /Users/davidross/.crc/cache/crc_vfkit_4.18.2_arm64.crcbundle
   INFO Checking if running macOS version >= 13.x
   INFO Checking if running as non-root
   INFO Checking if crc-admin-helper executable is cached
   INFO Checking if running on a supported CPU architecture
   INFO Checking if crc executable symlink exists
   INFO Checking minimum RAM requirements
   INFO Check if Podman binary exists in: /Users/davidross/.crc/bin/oc
   INFO Checking if running emulated on Apple silicon
   INFO Checking if vfkit is installed
   INFO Checking if CRC bundle is extracted in '$HOME/.crc'
   INFO Checking if /Users/davidross/.crc/cache/crc_vfkit_4.18.2_arm64.crcbundle exists
   INFO Getting bundle for the CRC executable
   INFO Downloading bundle: /Users/davidross/.crc/cache/crc_vfkit_4.18.2_arm64.crcbundle...
   5.35 GiB / 5.35 GiB [---------------------------------------] 100.00% 38.49 MiB/s
   INFO Uncompressing /Users/davidross/.crc/cache/crc_vfkit_4.18.2_arm64.crcbundle
   crc.img:  31.00 GiB / 31.00 GiB [--------------------------------------] 100.00%
   oc:  138.71 MiB / 138.71 MiB [-----------------------------------------] 100.00%
   INFO Checking if old launchd config for tray and/or daemon exists
   INFO Checking if crc daemon plist file is present and loaded
   INFO Adding crc daemon plist file and loading it
   INFO Checking SSH port availability
   Your system is correctly setup for using CRC. Use 'crc start' to start the instance
   ```

4. Start the Red Hat Openshift Local instance:

   ```
   crc start

   # Output
   INFO Using bundle path /Users/davidross/.crc/cache/crc_vfkit_4.18.2_arm64.crcbundle
   INFO Checking if running macOS version >= 13.x
   INFO Checking if running as non-root
   INFO Checking if crc-admin-helper executable is cached
   INFO Checking if running on a supported CPU architecture
   INFO Checking if crc executable symlink exists
   INFO Checking minimum RAM requirements
   INFO Check if Podman binary exists in: /Users/davidross/.crc/bin/oc
   INFO Checking if running emulated on Apple silicon
   INFO Checking if vfkit is installed
   INFO Checking if old launchd config for tray and/or daemon exists
   INFO Checking if crc daemon plist file is present and loaded
   INFO Checking SSH port availability
   INFO Loading bundle: crc_vfkit_4.18.2_arm64...
   INFO Starting CRC VM for openshift 4.18.2...
   INFO CRC instance is running with IP 127.0.0.1
   INFO CRC VM is running
   INFO Updating authorized keys...
   INFO Resizing /dev/vda4 filesystem
   INFO Configuring shared directories
   INFO Check internal and public DNS query...
   INFO Check DNS query from host...
   INFO Verifying validity of the kubelet certificates...
   INFO Starting kubelet service
   INFO Waiting for kube-apiserver availability... [takes around 2min]
   INFO Adding user's pull secret to the cluster...
   INFO Updating SSH key to machine config resource...
   INFO Waiting until the user's pull secret is written to the instance disk...
   INFO Changing the password for the kubeadmin user
   INFO Updating cluster ID...
   INFO Updating root CA cert to admin-kubeconfig-client-ca configmap...
   INFO Starting openshift instance... [waiting for the cluster to stabilize]
   INFO Operator authentication is progressing
   INFO Operator console is progressing
   INFO All operators are available. Ensuring stability...
   INFO Operators are stable (2/3)...
   INFO Operators are stable (3/3)...
   INFO Adding crc-admin and crc-developer contexts to kubeconfig...
   Started the OpenShift cluster.

   The server is accessible via web console at:
     https://console-openshift-console.apps-crc.testing

   Log in as administrator:
     Username: kubeadmin
     Password: <password>

   Log in as user:
     Username: developer
     Password: <password>

   Use the 'oc' command line interface:
     $ eval $(crc oc-env)
     $ oc login -u developer https://api.crc.testing:6443
   ```

   Depending on the speed of your system, this will take 5 to 15 minutes. There is a 10 minute timeout on checking the stability of operators deployed by Openshift. It might be the case that the tool reports these have not reached full stability in that window, particularly if using an Apple MacBook Pro with an Intel chip. In the writing of this guide, no issues were found using Openshift deployed in this manner, even if the error occurs. Each time the steps in this guide were tested, everything eventually reached a healthy status, even if not in the window expected on some occasions.

Setup is complete. This local environment should be ready to deploy our [Helm examples](https://developer.pingidentity.com/helm/examples/index.html).

## Stop the Red Hat Openshift Local instance

When not working with the environment, you can stop the instance by running the following command. All settings, projects and objects created will be retained and available when it is started again.

`crc stop`

Run `crc start` again to launch the instance.

## Delete the Red Hat Openshift Local instance

You can also remove the instance by running the following command. If you take this action, the embedded VM instance, all objects and projects created will be lost. A new instance will be deployed the next time you run `crc start`.

`crc delete`

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Deleting the instance does not delete the configuration settings for Red Hat Openshift Local (RAM, CPU, disk, and so on, created or modified when running the `crc config set` command). If you want to completely remove all configuration, you can delete the $HOME/.crc folder and its contents. Also, you will need to edit `/etc/hosts` and remove the following aliases to the 127.0.0.1 IP: `api.crc.testing canary-openshift-ingress-canary.apps-crc.testing console-openshift-console.apps-crc.testing default-route-openshift-image-registry.apps-crc.testing downloads-openshift-console.apps-crc.testing host.crc.testing oauth-openshift.apps-crc.testing` |

---

---
title: Deploy a PingAccess Cluster with PingIdentity Helm Charts Without a Server Profile
description: Deploy a PingAccess cluster using Ping Identity Helm charts without a custom server profile, for quick testing of the admin console
component: devops
page_id: devops::deployment/deployPACluster
canonical_url: https://developer.pingidentity.com/devops/deployment/deployPACluster.html
llms_txt: https://developer.pingidentity.com/devops/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  devops-purpose: Purpose
  devops-prerequisites: Prerequisites
  devops-steps: Steps
---

# Deploy a PingAccess Cluster with PingIdentity Helm Charts Without a Server Profile

|   |                                                                                                            |
| - | ---------------------------------------------------------------------------------------------------------- |
|   | The instructions in this document are for testing and learning and are not intended for use in production. |

## Purpose

Create and deploy a PingAccess Cluster using PingIdentity Helm Charts, without having to create a custom server profile. This process will allow you to quickly bring up the PingAccess UI and conduct any tests you need.

## Prerequisites

* [kubectl](https://kubernetes.io/docs/tasks/tools/#kubectl)

* Access to a Kubernetes cluster

## Steps

1. Confirm that your kuberenetes context and namespace are set correctly

   ```sh
   # Display kuberenetes context
   kubectx

   # Display namespace
   kubens -c
   ```

   If these values are not set or are incorrect, you can set them with the following commands. If you do not yet have a namespace, or do not have access to a kubernetes cluster, refer to [Deploy an Example Stack](../get-started/getStartedExample.html).

   ```sh
   # Display kuberenetes context
   kubectx <context>

   # Display namespace
   kubens <namespace>
   ```

2. Confirm that there are no conflicting persistent volumes.

   ```sh
   #List any persistent volumes
   kubectl get pvc
   ```

   If you see a persistent volume with a name that resembles `out-dir-demo-pingaccess-admin-0`, then delete it before deploying your cluster.

   ```sh
   #Delete name_of_pvc persistent volume
   kubectl delete pvc out-dir-demo-pingaccess-admin-0
   ```

   |   |                                                                                                                                  |
   | - | -------------------------------------------------------------------------------------------------------------------------------- |
   |   | This functionality has only been implemented for Sprint tags of 2211 or later. Therefore, it will not work for all earlier tags. |

3. Create a YAML file similar to the one shown here. Make sure to replace `insert domain name here` with your domain name.

   ```sh
   global:
   envs:
       PING_IDENTITY_ACCEPT_EULA: "YES"
   ingress:
       enabled: true
       addReleaseNameToHost: prepend
       defaultDomain: "insert domain name here"
       defaultTlsSecret:
       annotations:
           nginx.ingress.kubernetes.io/backend-protocol: "HTTPS"
           kubernetes.io/ingress.class: "nginx-public"

   #############################################################
   # pingaccess-admin values
   #############################################################
   pingaccess-admin:
   enabled: true
   privateCert:
       generate: true
   envs:
       PING_IDENTITY_PASSWORD: "2FederateM0re!"

   #############################################################
   # pingaccess-engine values
   #############################################################
   pingaccess-engine:
   enabled: true
   container:
       replicaCount: 1
   envs:
       PING_IDENTITY_PASSWORD: "2FederateM0re!"
   ```

4. Create the default PingAccess cluster. Make sure that you fill in the "PATH" to your new values.yaml file. This deployment may take a few minutes to become healthy.

   ```sh
   helm upgrade --install demo pingidentity/ping-devops -f <path-to-yaml>/values.yaml
   ```

5. To display the status of the deployed components, you can use [k9s](https://k9scli.io/) or issue the corresponding commands shown here:

   * Display the services (endpoints for connecting) by running `kubectl get service --selector=app.kubernetes.io/instance=demo`

     ```
     NAME                            TYPE        CLUSTER-IP       EXTERNAL-IP   PORT(S)             AGE
     demo-pingaccess-admin           ClusterIP   172.20.221.233   <none>        9090/TCP,9000/TCP   37s
     demo-pingaccess-admin-cluster   ClusterIP   None             <none>        <none>              37s
     demo-pingaccess-engine          ClusterIP   172.20.126.86    <none>        3000/TCP            37s
     ```

   * To view the pods, run `kubectl get pods --selector=app.kubernetes.io/instance=demo` - you will need to run this at intervals until all pods have started (**Running** status):

     ```
     NAME                                      READY   STATUS            RESTARTS   AGE
     demo-pingaccess-admin-0                   1/1     Running   0          28m
     demo-pingaccess-engine-6b977b9498-298jw   1/1     Running   0          28m
     ```

   * To see the ingresses you will use to access the product, run `kubectl get ingress`. If the ingress controller is configured properly, the URL you will see under demo-pingaccess-admin HOST (`demo-pingaccess-admin.<domain-name>`) will be the URL you use to access the PingAccess management console.

     ```
     NAME                     CLASS    HOSTS                                    ADDRESS                                                                         PORTS     AGE
     demo-pingaccess-admin    <none>   demo-pingaccess-admin.<domain-name>      adab69408130011eab1cd028479a4fe3-532fea1b3272797d.elb.us-east-2.amazonaws.com   80, 443   2m1s
     demo-pingaccess-engine   <none>   demo-pingaccess-engine.<domain-name>     adab69408130011eab1cd028479a4fe3-532fea1b3272797d.elb.us-east-2.amazonaws.com   80, 443   2m1s
     ```

   * To see everything tied to the helm release run `kubectl get all --selector=app.kubernetes.io/instance=demo`:

     ```
     NAME                                          READY   STATUS    RESTARTS   AGE
     pod/demo-pingaccess-admin-0                   1/1     Running   0          29m
     pod/demo-pingaccess-engine-6b977b9498-298jw   1/1     Running   0          29m

     NAME                                    TYPE        CLUSTER-IP       EXTERNAL-IP   PORT(S)             AGE
     service/demo-pingaccess-admin           ClusterIP   172.20.221.233   <none>        9090/TCP,9000/TCP   29m
     service/demo-pingaccess-admin-cluster   ClusterIP   None             <none>        <none>              29m
     service/demo-pingaccess-engine          ClusterIP   172.20.126.86    <none>        3000/TCP            29m

     NAME                                     READY   UP-TO-DATE   AVAILABLE   AGE
     deployment.apps/demo-pingaccess-engine   1/1     1            1           29m

     NAME                                                DESIRED   CURRENT   READY   AGE
     replicaset.apps/demo-pingaccess-engine-6b977b9498   1         1         1       29m

     NAME                                     READY   AGE
     statefulset.apps/demo-pingaccess-admin   1/1     29m
     ```

   * To view logs, look at the logs for the deployment of the product in question. For example:

     ```
     #Admin pod logs
     kubectl logs demo-pingaccess-admin-0

     #Engine pod logs
     kubectl logs demo-pingaccess-engine-6b977b9498
     ```

6. Below are the credentials and URL to sign on to the PingAccess management console after the cluster is up and healthy.

   |   |                                                                                                                     |
   | - | ------------------------------------------------------------------------------------------------------------------- |
   |   | This example uses self-signed certificates that will have to be accepted in your browser or added to your keystore. |

   With the ingress in place, you can access the product at the URL seen below, using the domain-name you set in your values.yaml file.

   | Product    | Connection Details                                                                                         |
   | ---------- | ---------------------------------------------------------------------------------------------------------- |
   | PingAccess | * URL: https\://demo-pingaccess-admin.(domain-name)

   * Username: Administrator

   * Password: 2FederateM0re! |

7. When you are finished, you can remove the demonstration components by running the uninstall command for helm:

   `helm uninstall demo`

8. Finally make sure to prune the persistent volume created in the deployment of your PingAccess cluster, by running the delete pvc command for kubectl:

   ```sh
   #Delete name_of_pvc persistent volume
   kubectl delete pvc out-dir-demo-pingaccess-admin-0
   ```

---

---
title: Deploy a robust local Kubernetes Cluster
description: Deploy a multi-node local Kubernetes cluster using Ansible and kubeadm with load balancing, block storage, ingress, and Istio for realistic testing
component: devops
page_id: devops::deployment/deployFullK8s
canonical_url: https://developer.pingidentity.com/devops/deployment/deployFullK8s.html
llms_txt: https://developer.pingidentity.com/devops/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  devops-prerequisites: Prerequisites
  devops-virtual-machines: Virtual machines
  devops-preliminary-operating-system-setup: Preliminary Operating System setup
  devops-install-the-operating-system: Install the Operating System
  devops-create-snapshot-base-os: "Create snapshot 'base-os'"
  devops-prepare-for-using-ansible: Prepare for using Ansible
  configure-ansible-playbooks-for-your-environment: Configure Ansible Playbooks for your environment
  run-the-first-playbook: Run the first playbook
  sample-output: Sample output
  optional-but-recommended-create-snapshot-k8s-installed: "(Optional but recommended) Create snapshot 'k8s-installed'"
  run-the-components-playbook: Run the components playbook
  sample-output-with-everything-enabled-other-than-istio-and-the-istio-addons: Sample output with everything enabled other than Istio and the Istio-addons
  snapshot-k8scomplete: "Snapshot 'k8sComplete'"
  resources-references: Resources & References
---

# Deploy a robust local Kubernetes Cluster

|   |                                                                                                                                                                                                                                                       |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | A video demonstrating the manual process outlined on this page is available [here](https://videos.pingidentity.com/detail/videos/devops/video/6324019967112/robust-test-kubernetes-cluster). An updated video using the ansible playbooks is planned. |

In some cases, a single-node cluster is insufficient for more complex testing scenarios. If you do not have access to a managed Kubernetes cluster and want something more similar to what you would find in a production environment, this guide can help.

This document describes deploying a multi-node cluster using [ansible](https://docs.ansible.com/) and the [kubeadm](https://kubernetes.io/docs/reference/setup-tools/kubeadm//) utility, running under virtual machines. When completed, the cluster will consist of:

* Three nodes, consisting of a master with two worker nodes (to conserve resources, the master will also be configured to run workloads)

* (At the time of writing) Kubernetes 1.35.1 using the `containerd` runtime (no Docker installed)

* (Optional but recommended) Load balancer

* Block storage support for PVC/PV needed by some Ping products

* (Optional) Ingress controller (ingress-nginx)

* (Optional) Istio service mesh

* (Optional) Supplementary tools for tracing and monitoring with Istio

|   |                                                                                                                                                                                                                       |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | While the result is a full Kubernetes installation, the instructions in this document only create an environment sufficient for testing and learning. The cluster is not intended for use in production environments. |

|   |                                                                                                                                                                                                                     |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The ansible playbooks for this guide assume the ARM chip set as found on the Apple M-series chip. If you are running on an Intel-based processor, you will have to adjust some file packages and names accordingly. |

## Prerequisites

In order to complete this guide, you will need:

* 64 GB of RAM (32 GB might be enough if you have an SSD to handle some memory swapping and reduce the RAM on the VMs to 12 GB)

* At least 150 GB of free disk

* Modern processor with multiple cores

* Ansible-playbook CLI tool. You can use brew by running `brew install ansible` or see [the ansible site](https://docs.ansible.com/ansible/latest/installation_guide/intro_installation.html) for instructions on how to install and configure this application.

* Virtualization solution. For this guide, VMware Fusion is used, but other means of creating and running a VM (Virtualbox, KVM) can be adapted.

* Access to [Ubuntu Server 24.04.2 LTS](https://ubuntu.com/download/server) installation media

* **A working knowledge of Kubernetes**, such as knowing how to port-forward, install objects using YAML files, and so on. Details on performing some actions will be omitted, and it is assumed the reader will know what to do.

* Patience

## Virtual machines

First, create 3 VMs as described here, using a default installation of Ubuntu 24.04. For this guide, the user created was `ubuntu`. You can use any name with a password of your choice.

* 4 vCPU

* 16 GB RAM

* 2 disks: 80 GB disk for the primary / 60 GB as secondary

* Attached to a network that allows internet access (bridged or NAT), using a fixed IP address

|   |                                                                                               |
| - | --------------------------------------------------------------------------------------------- |
|   | 192.168.163.0/24 was the IP space used in this guide; adjust to your environment accordingly. |

| VM          | Hostname  | IP address     |
| ----------- | --------- | -------------- |
| Master node | k8smaster | 192.168.163.70 |
| Worker      | k8snode01 | 192.168.163.71 |
| Worker      | k8snode02 | 192.168.163.72 |

## Preliminary Operating System setup

Perform these actions on all three VMs.

### Install the Operating System

Install the operating system as default, using the first disk (80 GB) as the installation target. For this guide, the installation disk was formatted to use the entire disk as the root partition, without LVM support.

## Create snapshot 'base-os'

Halt each VM by running `sudo shutdown -h now`.

Create a snapshot of each VM, naming it **base-os**. This snapshot provides a rollback point in case issues arise later. You will use snapshots at several other key points for the same purpose. After installation is complete, these intermediate snapshots can be removed.

Power up each VM set after taking the snapshots.

### Prepare for using Ansible

|   |                                                 |
| - | ----------------------------------------------- |
|   | This block of commands is executed on the host. |

```shell
# Add the IP addresses to the local hosts file for convenience
sudo tee -a /etc/hosts >/dev/null <\<-EOF
192.168.163.70 k8smaster
192.168.163.71 k8snode01
192.168.163.72 k8snode02
EOF

# Copy the SSH key you will use to access the VMs from your host machine to each VM.
# See https://www.ssh.com/academy/ssh/keygen for instructions on generating an SSH key
# For this guide, the ed25519 algorithm was used
# Adjust the key name accordingly in the ssh-copy-id command

export TARGET_MACHINES=("k8smaster" "k8snode01" "k8snode02")

for machine in "${TARGET_MACHINES[@]}"; do
   echo "Copying key to $machine:"
   ssh-copy-id -i ~/.ssh/localvms ubuntu@"$machine"
   echo "======================"
   echo "Confirming access. You should not be prompted
   for a password and will be shown the hostname:"
   ssh -i ~/.ssh/localvms ubuntu@"$machine" 'hostname'
   echo
done
```

Sample output:

```console
Copying key to k8smaster:
/usr/bin/ssh-copy-id: INFO: Source of key(s) to be installed: "/Users/davidross/.ssh/localvms.pub"
The authenticity of host 'k8smaster (192.168.163.70)' can't be established.
ED25519 key fingerprint is SHA256:qud9m1FRgwzJuwKcEsVVUbZ4bltYmiyKNj5e330ZQCA.
This key is not known by any other names
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
/usr/bin/ssh-copy-id: INFO: attempting to log in with the new key(s), to filter out any that are already installed
/usr/bin/ssh-copy-id: INFO: 1 key(s) remain to be installed -- if you are prompted now it is to install the new keys
ubuntu@k8smaster's password:

Number of key(s) added:        1

Now try logging into the machine, with:   "ssh 'ubuntu@k8smaster'"

======================
Confirming access. You should not be prompted for a password and will be shown the hostname:
k8smaster

<The output above is repeated for each node.>
```

After installation and reboot, perform the basic configuration needed for ansible support on the VMs. The primary change required is to allow `sudo` commands without requiring a password.

|   |                                |
| - | ------------------------------ |
|   | Run these commands on each VM. |

```shell
# Modify /etc/sudoers to allow the ubuntu user to sudo without a password
# This configuration grants the user full root access with no password
# DO NOT DO THIS IN PRODUCTION!

echo "ubuntu ALL=(ALL) NOPASSWD: ALL" | sudo tee -a /etc/sudoers
```

## Configure Ansible Playbooks for your environment

At this point, you are ready to modify the ansible playbooks for creating your cluster.

1. If you have not already done so, clone the `pingidentity-devops-getting-started` repository to your local `${PING_IDENTITY_DEVOPS_HOME}` directory.

   ```sh
   cd "$\{PING_IDENTITY_DEVOPS_HOME}"
   git clone \
   https://github.com/pingidentity/pingidentity-devops-getting-started.git
   ```

2. Navigate to the directory with the ansible scripts:

   ```sh
   cd "$\{PING_IDENTITY_DEVOPS_HOME}"/pingidentity-devops-getting-started/99-helper-scripts/ansible
   ```

3. Modify the `inventory.ini`, `ansible.cfg`, `install_kubernetes.yaml` and `install_list.yaml` files accordingly to suit your environment.

   1. The **inventory.ini** will need modification for your IP addresses, private key file, and user if one other than `ubuntu` was used:

      ```text
      [kubernetes_master]
      k8smaster ansible_host=192.168.163.70

      [kubernetes_nodes]
      k8snode01 ansible_host=192.168.163.71
      k8snode02 ansible_host=192.168.163.72

      [all:vars]
      ansible_user=ubuntu
      ansible_ssh_private_key_file=/Users/davidross/.ssh/localvms
      ansible_python_interpreter=/usr/bin/python3
      ```

   2. The **ansible.cfg** file should not need any modification:

      ```text
      [defaults]
      inventory = inventory.ini
      host_key_checking = False
      ```

   3. The **install\_kubernetes.yaml** file will need the following changes to lines 11-13 if your IP address differs from this example:

      ```text
      k8smaster_ip: "192.168.163.70"
      k8snode01_ip: "192.168.163.71"
      k8snode02_ip: "192.168.163.72"
      ```

   4. Finally, update the **install\_list.yaml** file. By default, no additional components are installed other than block storage, which is needed for some Ping products. To install other optional components, set the value to ***True***. Note that helm is required to install the Ingress controller, and adding K9s, metallb and ingress will provide additional tools for the most production-like implementation:

      ```yaml
      ---
      helm: False
      k9s: False
      metallb: False
      storage: True
      ingress: False
      istio: False
      istioaddons: False
      ...
      ```

## Run the first playbook

With the changes above, you are now ready to run the playbooks. First, run the **install\_kubernetes.yaml** playbook to install Kubernetes.

`ansible-playbook install_kubernetes.yaml -i inventory.ini`

|   |                                                                                                                                                                                               |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The playbook was designed to to be idempotent so you can run it multiple times if needed. An alternative is to reset to the **base-os** snapshot, update the `sudoers` file and run it again. |

### Sample output

> **Collapse: Details**
>
> ```console
> PLAY [Install Kubernetes on all VMs] http://myping-pingdataconsole.pingdemo.example/console/signin
>
> TASK [Gathering Facts] ************************************************************************************************
> ok: [k8snode02]
> ok: [k8smaster]
> ok: [k8snode01]
>
> TASK [Gather architecture info] ***************************************************************************************
> ok: [k8snode01]
> ok: [k8snode02]
> ok: [k8smaster]
>
> TASK [Update package cache] *******************************************************************************************
> ok: [k8smaster]
> ok: [k8snode01]
> ok: [k8snode02]
>
> TASK [Upgrade all packages] *******************************************************************************************
> changed: [k8smaster]
> changed: [k8snode01]
> changed: [k8snode02]
>
> TASK [Add host file entries] ******************************************************************************************
> changed: [k8smaster]
> changed: [k8snode02]
> changed: [k8snode01]
>
> TASK [Add the br_netfilter kernel module and configure for load at boot] *********************************************************************************************************************************
> changed: [k8snode02]
> changed: [k8smaster]
> changed: [k8snode01]
>
> TASK [Add the overlay kernel module and configure for load at boot] **************************************************************************************************************************************
> changed: [k8smaster]
> changed: [k8snode01]
> changed: [k8snode02]
>
> TASK [Creating kernel modules file to load at boot] ******************************************************************************************************************************************************
> changed: [k8snode01]
> changed: [k8snode02]
> changed: [k8smaster]
>
> TASK [Disable swap in fstab by commenting it out] ********************************************************************************************************************************************************
> changed: [k8snode02]
> changed: [k8smaster]
> changed: [k8snode01]
>
> TASK [Disable swap] ***************************************************************************************************
> changed: [k8snode01]
> changed: [k8smaster]
> changed: [k8snode02]
>
> TASK [Enable IP forwarding for iptables] *****************************************************************************************************************************************************************
> changed: [k8smaster]
> changed: [k8snode01]
> changed: [k8snode02]
>
> TASK [Update sysctl parameters without reboot - bridge (ipv4)] *******************************************************************************************************************************************
> [WARNING]: Deprecation warnings can be disabled by setting `deprecation_warnings=False` in ansible.cfg.
> [DEPRECATION WARNING]: Importing 'to_native' from 'ansible.module_utils._text' is deprecated. This feature will be removed from ansible-core version 2.24. Use ansible.module_utils.common.text.converters instead.
> changed: [k8smaster]
> changed: [k8snode02]
> changed: [k8snode01]
>
> TASK [Update sysctl parameters without reboot - bridge (ipv6)] *******************************************************************************************************************************************
> changed: [k8snode01]
> changed: [k8smaster]
> changed: [k8snode02]
>
> TASK [Update sysctl parameters without reboot - IPforward] ***********************************************************************************************************************************************
> changed: [k8smaster]
> changed: [k8snode01]
> changed: [k8snode02]
>
> TASK [Install containerd] *********************************************************************************************
> changed: [k8snode01] => (item=containerd)
> changed: [k8smaster] => (item=containerd)
> changed: [k8snode02] => (item=containerd)
>
> TASK [Add Kubernetes APT key] *****************************************************************************************
> changed: [k8smaster]
> changed: [k8snode02]
> changed: [k8snode01]
>
> TASK [Create directory for containerd configuration file] ************************************************************************************************************************************************
> changed: [k8smaster]
> changed: [k8snode01]
> changed: [k8snode02]
>
> TASK [Check if containerd toml configuration file exists] ************************************************************************************************************************************************
> ok: [k8snode01]
> ok: [k8smaster]
> ok: [k8snode02]
>
> TASK [Create containerd configuration file if it does not exist] *****************************************************************************************************************************************
> changed: [k8snode01]
> changed: [k8smaster]
> changed: [k8snode02]
>
> TASK [Read config.toml file] ******************************************************************************************
> ok: [k8smaster]
> ok: [k8snode01]
> ok: [k8snode02]
>
> TASK [Check if correct containerd.runtimes.runc line exists] *********************************************************************************************************************************************
> ok: [k8snode01]
> ok: [k8smaster]
> ok: [k8snode02]
>
> TASK [Error out if the incorrect or missing containerd.runtimes.runc line does not exist] ****************************************************************************************************************
> skipping: [k8smaster]
> skipping: [k8snode01]
> skipping: [k8snode02]
>
> TASK [Set SystemdCgroup line in file to true if it is currently false] ***********************************************************************************************************************************
> changed: [k8smaster]
> changed: [k8snode01]
> changed: [k8snode02]
>
> TASK [Restart containerd service] *************************************************************************************
> changed: [k8snode01]
> changed: [k8smaster]
> changed: [k8snode02]
>
> TASK [Install prerequisites for Kubernetes] *************************************************************************************
> changed: [k8smaster] => (item=apt-transport-https)
> changed: [k8snode02] => (item=apt-transport-https)
> changed: [k8snode01] => (item=apt-transport-https)
> ok: [k8smaster] => (item=ca-certificates)
> ok: [k8snode02] => (item=ca-certificates)
> ok: [k8snode01] => (item=ca-certificates)
> ok: [k8smaster] => (item=curl)
> ok: [k8snode02] => (item=curl)
> ok: [k8snode01] => (item=curl)
> changed: [k8smaster] => (item=gnupg2)
> changed: [k8snode02] => (item=gnupg2)
> changed: [k8snode01] => (item=gnupg2)
> ok: [k8smaster] => (item=software-properties-common)
> ok: [k8snode02] => (item=software-properties-common)
> ok: [k8snode01] => (item=software-properties-common)
> changed: [k8snode01] => (item=bzip2)
> changed: [k8smaster] => (item=bzip2)
> changed: [k8snode02] => (item=bzip2)
> ok: [k8snode01] => (item=tar)
> ok: [k8smaster] => (item=tar)
> ok: [k8snode02] => (item=tar)
> ok: [k8snode01] => (item=vim)
> ok: [k8smaster] => (item=vim)
> ok: [k8snode02] => (item=vim)
> ok: [k8snode02] => (item=git)
> ok: [k8smaster] => (item=git)
> ok: [k8snode01] => (item=git)
> ok: [k8smaster] => (item=wget)
> ok: [k8snode02] => (item=wget)
> ok: [k8snode01] => (item=wget)
> ok: [k8smaster] => (item=net-tools)
> ok: [k8snode02] => (item=net-tools)
> ok: [k8snode01] => (item=net-tools)
> ok: [k8snode01] => (item=lvm2)
> ok: [k8snode02] => (item=lvm2)
> ok: [k8smaster] => (item=lvm2)
>
> TASK [Get Kubernetes package signing key] ****************************************************************************************************************************************************************
> changed: [k8snode01]
> changed: [k8snode02]
> changed: [k8smaster]
>
> TASK [Add Kubernetes APT repository] **********************************************************************************
> changed: [k8snode01]
> changed: [k8smaster]
> changed: [k8snode02]
>
> TASK [Update package cache] *******************************************************************************************
> ok: [k8snode01]
> ok: [k8smaster]
> ok: [k8snode02]
>
> TASK [Install Kubernetes components] **********************************************************************************
> changed: [k8smaster] => (item=kubelet)
> changed: [k8snode01] => (item=kubelet)
> changed: [k8snode02] => (item=kubelet)
> changed: [k8smaster] => (item=kubeadm)
> changed: [k8snode01] => (item=kubeadm)
> changed: [k8snode02] => (item=kubeadm)
> changed: [k8smaster] => (item=kubectl)
> changed: [k8snode01] => (item=kubectl)
> changed: [k8snode02] => (item=kubectl)
>
> TASK [Hold Kubernetes packages at current version] *******************************************************************************************************************************************************
> changed: [k8snode02]
> changed: [k8snode01]
> changed: [k8smaster]
>
> TASK [Run kubeadm reset to ensure fresh start each time.] ************************************************************************************************************************************************
> changed: [k8snode02]
> changed: [k8snode01]
> changed: [k8smaster]
>
> TASK [Remove any files from a previous installation attempt] *********************************************************************************************************************************************
> skipping: [k8snode01] => (item=/home/ubuntu/.kube)
> skipping: [k8snode01]
> skipping: [k8snode02] => (item=/home/ubuntu/.kube)
> skipping: [k8snode02]
> ok: [k8smaster] => (item=/home/ubuntu/.kube)
>
> TASK [Initialize Kubernetes master] ***********************************************************************************
> skipping: [k8snode01]
> skipping: [k8snode02]
> changed: [k8smaster]
>
> TASK [Check if k8s installation file exists] *************************************************************************************************************************************************************
> skipping: [k8snode01]
> skipping: [k8snode02]
> ok: [k8smaster]
>
> TASK [Fail if K8s installed file does not exist] *********************************************************************************************************************************************************
> skipping: [k8smaster]
> skipping: [k8snode01]
> skipping: [k8snode02]
>
> TASK [Create .kube directory] *****************************************************************************************
> skipping: [k8snode01]
> skipping: [k8snode02]
> changed: [k8smaster]
>
> TASK [Copy kubeconfig to user's home directory] **********************************************************************************************************************************************************
> skipping: [k8snode01]
> skipping: [k8snode02]
> changed: [k8smaster]
>
> TASK [Install Pod network] ********************************************************************************************
> skipping: [k8snode01]
> skipping: [k8snode02]
> changed: [k8smaster]
>
> TASK [Remove taint from master node] **********************************************************************************
> skipping: [k8snode01]
> skipping: [k8snode02]
> changed: [k8smaster]
>
> TASK [Retrieve join command from master and run it on the nodes] *****************************************************************************************************************************************
> skipping: [k8snode01]
> skipping: [k8snode02]
> changed: [k8smaster]
>
> TASK [Join worker nodes to the cluster] ******************************************************************************************************************************************************************
> skipping: [k8snode01] => (item=k8snode01)
> skipping: [k8snode01] => (item=k8snode02)
> skipping: [k8snode01]
> skipping: [k8snode02] => (item=k8snode01)
> skipping: [k8snode02] => (item=k8snode02)
> skipping: [k8snode02]
> changed: [k8smaster -> k8snode01(192.168.163.71)] => (item=k8snode01)
> changed: [k8smaster -> k8snode02(192.168.163.72)] => (item=k8snode02)
>
> TASK [Pause for 5 seconds] ********************************************************************************************
> Pausing for 5 seconds
> (ctrl+C then 'C' = continue early, ctrl+C then 'A' = abort)
> ok: [k8smaster]
>
> TASK [Confirm flannel pods are ready] ********************************************************************************************************************************************************************
> skipping: [k8snode01]
> skipping: [k8snode02]
> changed: [k8smaster]
>
> TASK [Run confirmation command by listing nodes] *********************************************************************************************************************************************************
> changed: [k8smaster]
> changed: [k8snode01 -> k8smaster(192.168.163.70)]
> changed: [k8snode02 -> k8smaster(192.168.163.70)]
>
> TASK [Nodes in the cluster] *******************************************************************************************
> ok: [k8smaster] => {
>     "nodes_command_output.stdout_lines": [
>         "NAME        STATUS   ROLES           AGE   VERSION",
>         "k8smaster   Ready    control-plane   34s   v1.35.1",
>         "k8snode01   Ready    <none>          24s   v1.35.1",
>         "k8snode02   Ready    <none>          23s   v1.35.1"
>     ]
> }
> ok: [k8snode01] => {
>     "nodes_command_output.stdout_lines": [
>         "NAME        STATUS   ROLES           AGE   VERSION",
>         "k8smaster   Ready    control-plane   34s   v1.35.1",
>         "k8snode01   Ready    <none>          24s   v1.35.1",
>         "k8snode02   Ready    <none>          23s   v1.35.1"
>     ]
> }
> ok: [k8snode02] => {
>     "nodes_command_output.stdout_lines": [
>         "NAME        STATUS   ROLES           AGE   VERSION",
>         "k8smaster   Ready    control-plane   34s   v1.35.1",
>         "k8snode01   Ready    <none>          24s   v1.35.1",
>         "k8snode02   Ready    <none>          23s   v1.35.1"
>     ]
> }
>
> TASK [Provide cluster connection information] ************************************************************************************************************************************************************
> skipping: [k8snode01]
> skipping: [k8snode02]
> changed: [k8smaster]
>
> TASK [Cluster information for your .kube/config file] ****************************************************************************************************************************************************
> ok: [k8smaster] => {
>     "msg": [
>         "apiVersion: v1",
>         "clusters:",
>         "- cluster:",
>         "    certificate-authority-data: LS0tLS1CR....",
>         "    server: https://192.168.163.70:6443",
>         "  name: kubernetes",
>         "contexts:",
>         "- context:",
>         "    cluster: kubernetes",
>         "    user: kubernetes-admin",
>         "  name: kubernetes-admin@kubernetes",
>         "current-context: kubernetes-admin@kubernetes",
>         "kind: Config",
>         "users:",
>         "- name: kubernetes-admin",
>         "  user:",
>         "    client-certificate-data: LS0tLS1CR....",
>         "    client-key-data: LS0tLS1CR...."
>     ]
> }
> skipping: [k8snode01]
> skipping: [k8snode02]
>
> PLAY RECAP ************************************************************************************************************
> k8smaster                  : ok=45   changed=33   unreachable=0    failed=0    skipped=2    rescued=0    ignored=0
> k8snode01                  : ok=32   changed=24   unreachable=0    failed=0    skipped=14   rescued=0    ignored=0
> k8snode02                  : ok=32   changed=24   unreachable=0    failed=0    skipped=14   rescued=0    ignored=0
> ```

## (Optional but recommended) Create snapshot 'k8s-installed'

Halt each VM by running `sudo shutdown -h now`.

Create a snapshot of each VM, naming it **k8s-installed**.

Power up each VM set after taking the snapshot.

## Run the components playbook

Now that Kubernetes is installed, modify the `install_list.yaml` file accordingly to enable or disable the components that you want to install. After making changes, run the **install\_others.yaml** playbook.

`ansible-playbook install_others.yaml -i inventory.ini`

|   |                                                                                                                                                                          |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | The playbook was designed to to be idempotent so you can run it multiple times if needed. An alternative is to reset to the **k8s-installed** snapshot and run it again. |

|   |                                                                                                                                                                  |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | After K9s is installed on the master, you can launch it in an SSH session and monitor the progress of the pods being instantiated while the playbook is running. |

### Sample output with everything enabled other than Istio and the Istio-addons

> **Collapse: Details**
>
> ```console
> PLAY [Install Other Components in the Cluster] *********************************
>
> TASK [Gathering Facts] *********************************************************
> ok: [k8smaster]
>
> TASK [Get helm installation file] **********************************************
> changed: [k8smaster]
>
> TASK [Extract helm] ************************************************************
> changed: [k8smaster]
>
> TASK [Remove helm tarball and extracted folder] ********************************
> changed: [k8smaster] => (item=/home/ubuntu/linux-amd64)
> changed: [k8smaster] => (item=/home/ubuntu/helm-v3.12.1-linux-amd64.tar.gz)
>
> TASK [Get K9s installation file] ***********************************************
> changed: [k8smaster]
>
> TASK [Extract k9s] *************************************************************
> changed: [k8smaster]
>
> TASK [Remove k9s tarball] ******************************************************
> changed: [k8smaster]
>
> TASK [Get latest MetalLB version] **********************************************
> changed: [k8smaster]
>
> TASK [Get MetalLB installer] ***************************************************
> changed: [k8smaster]
>
> TASK [Apply MetalLB file] ******************************************************
> changed: [k8smaster]
>
> TASK [Pause for 10 seconds] ****************************************************
> Pausing for 10 seconds
> (ctrl+C then 'C' = continue early, ctrl+C then 'A' = abort)
> ok: [k8smaster]
>
> TASK [Wait for MetalLB controller and speaker pods to be ready] ****************
> changed: [k8smaster] => (item=app=metallb)
> changed: [k8smaster] => (item=component=speaker)
>
> TASK [Creating MetalLB configuration file] *************************************
> changed: [k8smaster]
>
> TASK [Configure MetalLB] *******************************************************
> changed: [k8smaster]
>
> TASK [Remove MetalLB installation yaml files] **********************************
> changed: [k8smaster] => (item=/home/ubuntu/ipaddress_pool_metal.yaml)
> changed: [k8smaster] => (item=/home/ubuntu/metallb-native.yaml)
>
> TASK [Install CertManager prerequisite] ****************************************
> changed: [k8smaster]
>
> TASK [Check if rook directory exists] ******************************************
> ok: [k8smaster]
>
> TASK [Remove directory] ********************************************************
> skipping: [k8smaster]
>
> TASK [Clone Rook repository] ***************************************************
> changed: [k8smaster]
>
> TASK [Install Rook controller] *************************************************
> changed: [k8smaster]
>
> TASK [Wait for Rook controller pod to be ready] ********************************
> changed: [k8smaster]
>
> TASK [Install Rook components] *************************************************
> changed: [k8smaster]
>
> TASK [Pause for 3 1/2 minutes - wait for Rook components to get started] *******
> Pausing for 210 seconds
> (ctrl+C then 'C' = continue early, ctrl+C then 'A' = abort)
> ok: [k8smaster]
>
> TASK [Confirm Rook cluster pods are ready] *************************************
> changed: [k8smaster] => (item=app=csi-cephfsplugin)
> changed: [k8smaster] => (item=app=csi-cephfsplugin-provisioner)
> changed: [k8smaster] => (item=app=csi-rbdplugin)
> changed: [k8smaster] => (item=app=rook-ceph-mgr)
> changed: [k8smaster] => (item=app=rook-ceph-mon)
> changed: [k8smaster] => (item=app=rook-ceph-crashcollector)
> changed: [k8smaster] => (item=app=csi-rbdplugin-provisioner)
> changed: [k8smaster] => (item=app=rook-ceph-osd)
>
> TASK [Creating Block Storage class] ********************************************
> changed: [k8smaster]
>
> TASK [Create block ceph storage class] *****************************************
> changed: [k8smaster]
>
> TASK [Creating script to patch storage class (globbing and substitution hack)] ***
> changed: [k8smaster]
>
> TASK [Set storage class as default] ********************************************
> changed: [k8smaster]
>
> TASK [Remove Rook installation files] ******************************************
> changed: [k8smaster] => (item=/home/ubuntu/rook)
> changed: [k8smaster] => (item=/home/ubuntu/sc-ceph-block.yaml)
> changed: [k8smaster] => (item=/home/ubuntu/patchsc.yaml)
>
> TASK [Install Ingress Nginx] ***************************************************
> changed: [k8smaster]
>
> TASK [Pause for 5 seconds] *****************************************************
> Pausing for 5 seconds
> (ctrl+C then 'C' = continue early, ctrl+C then 'A' = abort)
> ok: [k8smaster]
>
> TASK [Confirm ingress controller pod is ready] *********************************
> changed: [k8smaster]
>
> TASK [Get Ingress service components for confirmation] *************************
> changed: [k8smaster]
>
> TASK [Ingress controller information] ******************************************
> ok: [k8smaster] => {
>     "msg": [
>         "NAME                                 TYPE           CLUSTER-IP       EXTERNAL-IP       PORT(S)                      AGE",
>         "ingress-nginx-controller             LoadBalancer   10.101.36.117    192.168.163.151   80:30865/TCP,443:31410/TCP   31s",
>         "ingress-nginx-controller-admission   ClusterIP      10.103.154.247   <none>            443/TCP                      31s"
>     ]
> }
>
> TASK [Get 'istioctl' installation file] ****************************************
> skipping: [k8smaster]
>
> TASK [Extract istioctl] ********************************************************
> skipping: [k8smaster]
>
> TASK [Install istio] ***********************************************************
> skipping: [k8smaster]
>
> TASK [Pause for 5 seconds] *****************************************************
> skipping: [k8smaster]
>
> TASK [Confirm Istio pods are ready] ********************************************
> skipping: [k8smaster] => (item=app=istiod)
> skipping: [k8smaster] => (item=app=istio-ingressgateway)
> skipping: [k8smaster] => (item=app=istio-egressgateway)
> skipping: [k8smaster]
>
> TASK [Install Istio add-ons] ***************************************************
> skipping: [k8smaster]
>
> TASK [Confirm Istio additional pods are ready] *********************************
> skipping: [k8smaster] => (item=app=grafana)
> skipping: [k8smaster] => (item=app=jaeger)
> skipping: [k8smaster] => (item=app=kiali)
> skipping: [k8smaster] => (item=app=prometheus)
> skipping: [k8smaster] => (item=app.kubernetes.io/name=loki)
> skipping: [k8smaster]
>
> TASK [Creating patch file for services] ****************************************
> skipping: [k8smaster]
>
> TASK [Patch istio add-on services to use load balancer] ************************
> skipping: [k8smaster] => (item=grafana)
> skipping: [k8smaster] => (item=kiali)
> skipping: [k8smaster] => (item=tracing)
> skipping: [k8smaster] => (item=prometheus)
> skipping: [k8smaster]
>
> TASK [Remove istio tarball and extracted folder] *******************************
> skipping: [k8smaster] => (item=/home/ubuntu/istio-1.18.0)
> skipping: [k8smaster] => (item=/home/ubuntu/istio-1.18.0-linux-amd64.tar.gz)
> skipping: [k8smaster] => (item=/home/ubuntu/patch-service.yaml)
> skipping: [k8smaster]
>
> PLAY RECAP *********************************************************************
> k8smaster       : ok=33   changed=27   unreachable=0    failed=0    skipped=11   rescued
> ```

## Snapshot 'k8sComplete'

Shut down the VMs, and snapshot each one. See the helper script in this repository located at `99-helper-scripts/manageCluster.sh` that can be used for automating things under VMware. At this time, your cluster is ready for use.

## Resources & References

This guide was built on the work of others. As with many how-to documents, we have contributed our skills and knowledge to pull everything together and fill in the gaps that were experienced. However, we want to acknowledge at least some of the many sources where we found inspiration, guidance, fixes for errors, and sanity when a step was missed. Not shown here are dozens of places where we went in exploring different options for pieces we did not use or install in the end. **The Ping DevOps Integrations team**

* [How to Deploy MetalLB on Kubernetes - ComputingForGeeks](https://computingforgeeks.com/deploy-metallb-load-balancer-on-kubernetes/)

* [How To: Ubuntu / Debian Linux Regenerate OpenSSH Host Keys - nixCraft](https://www.cyberciti.biz/faq/howto-regenerate-openssh-host-keys)

* [Block Storage Overview - Rook Ceph Documentation](https://www.rook.io/docs/rook/v1.10/Storage-Configuration/Block-Storage-RBD/block-storage/#advanced-example-erasure-coded-block-storage)

* [Toolbox - Rook Ceph Documentation](https://www.rook.io/docs/rook/v1.10/Troubleshooting/ceph-toolbox/#interactive-toolbox)

* [Quickstart - Rook Ceph Documentation](https://www.rook.io/docs/rook/v1.10/Getting-Started/quickstart)

* [How To Install Kubernetes on Ubuntu 24.04 LTS](https://idroot.us/install-kubernetes-ubuntu-24-04/)

* [Containerd Github](https://github.com/containerd/containerd/blob/main/docs/getting-started.md)

* [etcd-io Github issue #13670](https://github.com/etcd-io/etcd/issues/13670)

---

---
title: Deploy Ping DevOps Charts using Helm
description: "Redirect notice pointing to the current Ping Identity Helm chart examples and getting started documentation, which replaced this page's content"
component: devops
page_id: devops::deployment/deployHelm
canonical_url: https://developer.pingidentity.com/devops/deployment/deployHelm.html
llms_txt: https://developer.pingidentity.com/devops/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
---

# Deploy Ping DevOps Charts using Helm

The Helm examples content has moved to the DevOps Helm Charts docs.

Use the current pages here:

* [Helm Chart Examples](https://developer.pingidentity.com/helm/examples/index.html)

* [Helm Getting Started](https://developer.pingidentity.com/helm/getting-started/index.html)

If you bookmarked this page, update your links to the Helm docs section.

---

---
title: Deploy PingDirectory Across Multiple Kubernetes Clusters
description: Deploy a replicated PingDirectory topology across multiple Kubernetes clusters using DNS hostname variables for active/active deployments
component: devops
page_id: devops::deployment/deployPDMultiRegion
canonical_url: https://developer.pingidentity.com/devops/deployment/deployPDMultiRegion.html
llms_txt: https://developer.pingidentity.com/devops/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  devops-overview: Overview
  devops-what-you-will-do: What You Will Do
  devops-pingdirectory-host-naming: PingDirectory Host Naming
  devops-single-cluster-example-with-multiple-namespaces: Single Cluster Example with Multiple Namespaces
  devops-primary-cluster: Primary Cluster
  devops-secondary-cluster: Secondary Cluster
  devops-production-example-with-external-dns-names: Production Example with External DNS Names
  devops-us-west-cluster: us-west cluster
  devops-us-east-cluster: us-east cluster
  devops-variables-to-create-hostnames: Variables to Create Hostnames
  devops-previous-hostname-example-breakdown: Previous Hostname Example Breakdown
  devops-environment-variables: Environment Variables
  primary: Primary
  devops-secondary: Secondary
  devops-cluster-startup-walkthrough: Cluster Startup Walkthrough
  devops-deploying-across-multiple-regions-with-multiple-load-balancers: Deploying Across Multiple Regions with Multiple Load Balancers
  devops-deploy-the-helm-example: Deploy the Helm Example
  devops-cleanup: Cleanup
---

# Deploy PingDirectory Across Multiple Kubernetes Clusters

This example shows how to deploy PingDirectory containers that replicate across multiple Kubernetes clusters.

![K8S Multi-Cluster Overview](../_images/multi-k8s-cluster-pingdirectory-overview.png)

## Overview

Implementing a replicated PingDirectory topology across multiple Kubernetes clusters is desired for highly available active/active deployments as well as active/partial-active scenarios where a hot backup is expected.

PingDirectory Docker images abstract much of the complexity of replication initialization scripts, even across clusters. With this simplification, the focus shifts to providing accessible DNS hostnames across clusters and environment variables to build ordinal hostnames for each PingDirectory instance.

### What You Will Do

1. [PingDirectory Host Naming](#devops-pingdirectory-host-naming) - Set the variables needed to create your hostnames

2. [Cluster Startup Walkthrough](#devops-cluster-startup-walkthrough) - A description of what happens when a PingDirectory cluster starts

3. [Deploy the Helm Example](#devops-deploy-the-helm-example) - Deploy an example set of servers across multiple Kubernetes clusters

Details within each Kubernetes cluster are hidden from outside the cluster, which means that external access to each pod in the cluster is required. The PingDirectory images will set up access to each of the pods using load balancers from an external host to allow each pod to communicate over the LDAP and replication protocols.

## PingDirectory Host Naming

The most important aspect of a successful PingDirectory cross-cluster deployment is assigning accessible and logical DNS hostnames. The rules for this setup include:

1. Each PingDirectory pod needs its own hostname available in DNS

2. Hostnames need to include the ordinal representing the instance in the statefulset

3. All hostnames must be accessible to all directory instances

These rules still leave plenty of room for flexibility, particularly when accounting for the cluster-native DNS names Kubernetes creates.

### Single Cluster Example with Multiple Namespaces

For example, you can simulate a multi-cluster environment in a single Kubernetes cluster by using separate namespaces and creating a separate ClusterIP service for each directory environment. You would end up with something similar to this example:

#### Primary Cluster

| Pod             | Service Name  | Namespace | Hostname                |
| --------------- | ------------- | --------- | ----------------------- |
| pingdirectory-0 | pingdirectory | primary   | pingdirectory-0.primary |
| pingdirectory-1 | pingdirectory | primary   | pingdirectory-1.primary |
| pingdirectory-2 | pingdirectory | primary   | pingdirectory-2.primary |

#### Secondary Cluster

| Pod             | Service Name  | Namespace | Hostname                  |
| --------------- | ------------- | --------- | ------------------------- |
| pingdirectory-0 | pingdirectory | secondary | pingdirectory-0.secondary |
| pingdirectory-1 | pingdirectory | secondary | pingdirectory-1.secondary |
| pingdirectory-2 | pingdirectory | secondary | pingdirectory-2.secondary |

### Production Example with External DNS Names

An example from a production environment with external hostnames might appear more like this example:

#### us-west cluster

| Pod             | Service Name  | DNS/Hostname                            |
| --------------- | ------------- | --------------------------------------- |
| pingdirectory-0 | pingdirectory | pingdirectory-0-us-west.ping-devops.com |
| pingdirectory-1 | pingdirectory | pingdirectory-1-us-west.ping-devops.com |
| pingdirectory-2 | pingdirectory | pingdirectory-2-us-west.ping-devops.com |

#### us-east cluster

| Pod             | Service Name  | DNS/Hostname                            |
| --------------- | ------------- | --------------------------------------- |
| pingdirectory-0 | pingdirectory | pingdirectory-0-us-east.ping-devops.com |
| pingdirectory-1 | pingdirectory | pingdirectory-1-us-east.ping-devops.com |
| pingdirectory-2 | pingdirectory | pingdirectory-2-us-east.ping-devops.com |

## Variables to Create Hostnames

To provide flexibility on how each PingDirectory instance will find other instances, a full DNS hostname is broken into multiple variables.

| Variable                   | Description                                                                                              |
| -------------------------- | -------------------------------------------------------------------------------------------------------- |
| `K8S_POD_HOSTNAME_PREFIX`  | The string used as the prefix for all host names. Defaults to the name of the `StatefulSet`.             |
| `K8S_POD_HOSTNAME_SUFFIX`  | The string used as the suffix for all pod host names. Defaults to `K8S_CLUSTER`.                         |
| `K8S_SEED_HOSTNAME_SUFFIX` | The string used as the suffix for all seed host names. Defaults to `K8S_SEED_CLUSTER` (discussed later). |

With these variables, a full hostname is created in this manner:

```sh
${K8S_POD_HOSTNAME_PREFIX}<instance-ordinal>${K8S_POD_HOSTNAME_SUFFIX}
```

Use `K8S_POD_HOSTNAME_SUFFIX` when constructing the hostname for a pod in the current cluster. Use `K8S_SEED_HOSTNAME_SUFFIX` when a pod needs to refer to the seed cluster.

### Previous Hostname Example Breakdown

| Hostname                                | K8S\_POD\_HOSTNAME\_PREFIX | K8S\_POD\_HOSTNAME\_SUFFIX | K8S\_SEED\_HOSTNAME\_SUFFIX |
| --------------------------------------- | -------------------------- | -------------------------- | --------------------------- |
| pingdirectory-0.primary                 | `pingdirectory-`           | `.primary`                 | `.primary`                  |
| pingdirectory-2-us-west.ping-devops.com | `pingdirectory-`           | `-us-west.ping-devops.com` | `-us-west.ping-devops.com`  |

## Environment Variables

| Variable                   | Required | Description                                                                            |
| -------------------------- | -------- | -------------------------------------------------------------------------------------- |
| `K8S_CLUSTERS`             | \*\*     | The total list of Kubernetes clusters to which the StatefulSet will replicate.         |
| `K8S_CLUSTER`              | \*\*     | The Kubernetes cluster to which the StatefulSet will be deployed.                      |
| `K8S_SEED_CLUSTER`         | \*\*     | The Kubernetes cluster to which the seed server is deployed.                           |
| `K8S_NUM_REPLICAS`         |          | The number of replicas that make up the StatefulSet.                                   |
| `K8S_POD_HOSTNAME_PREFIX`  |          | The string used as the prefix for all host names. Defaults to `StatefulSet`.           |
| `K8S_POD_HOSTNAME_SUFFIX`  |          | The string used as the suffix for all pod host names. Defaults to `K8S_CLUSTER`.       |
| `K8S_SEED_HOSTNAME_SUFFIX` |          | The string used as the suffix for all seed host names. Defaults to `K8S_SEED_CLUSTER`. |
| `K8S_INCREMENT_PORTS`      |          | `true` or `false`. If `true`, the port for each pod will be incremented by 1.          |

If you also deploy PingDirectoryProxy with automatic server discovery across multiple clusters, these variables establish the proxy location model as well. `K8S_CLUSTER` becomes the proxy's local location, and the PingDirectoryProxy automatic-discovery profile uses the non-local cluster order in `K8S_CLUSTERS` as the default local preferred failover order. Set `PREFERRED_FAILOVER_LOCATIONS` on the proxy to use an explicit ordered subset. See [Deploy PingDirectoryProxy and PingDirectory with automatic backend discovery](deployPDProxyBackendDiscovery.html).

An example set of the YAML configuration for these environment variables is as follows:

### Primary

```yaml
K8S_STATEFUL_SET_NAME=pingdirectory
K8S_STATEFUL_SET_SERVICE_NAME=pingdirectory

K8S_CLUSTERS=us-east-2 eu-west-1
K8S_CLUSTER=us-east-2
K8S_SEED_CLUSTER=us-east-2
K8S_NUM_REPLICAS=3

K8S_POD_HOSTNAME_PREFIX=pd-
K8S_POD_HOSTNAME_SUFFIX=.us-cluster.ping-devops.com
K8S_SEED_HOSTNAME_SUFFIX=.us-cluster.ping-devops.com

K8S_INCREMENT_PORTS=true
LDAPS_PORT=8600
REPLICATION_PORT=8700
```

These environment variable settings map out like this:

| Seed | Instance                  | Hostname                        | LDAP | REPL |
| ---- | ------------------------- | ------------------------------- | ---- | ---- |
|      | CLUSTER:us-east-2         |                                 |      |      |
| \*\* | pingdirectory-0.us-east-2 | pd-0.us-cluster.ping-devops.com | 8600 | 8700 |
|      | pingdirectory-1.us-east-2 | pd-1.us-cluster.ping-devops.com | 8601 | 8701 |
|      | pingdirectory-2.us-east-2 | pd-2.us-cluster.ping-devops.com | 8602 | 8702 |

### Secondary

```yaml
K8S_STATEFUL_SET_NAME=pingdirectory
K8S_STATEFUL_SET_SERVICE_NAME=pingdirectory

K8S_CLUSTERS=us-east-2 eu-west-1
K8S_CLUSTER=eu-west-1
K8S_SEED_CLUSTER=us-east-2
K8S_NUM_REPLICAS=3

K8S_POD_HOSTNAME_PREFIX=pd-
K8S_POD_HOSTNAME_SUFFIX=.eu-cluster.ping-devops.com
K8S_SEED_HOSTNAME_SUFFIX=.us-cluster.ping-devops.com

K8S_INCREMENT_PORTS=true
LDAPS_PORT=8600
REPLICATION_PORT=8700
```

| Seed | Instance                  | Hostname                        | LDAP | REPL |
| ---- | ------------------------- | ------------------------------- | ---- | ---- |
|      | CLUSTER:eu-west-1         |                                 |      |      |
|      | pingdirectory-0.eu-west-1 | pd-0.eu-cluster.ping-devops.com | 8600 | 8700 |
|      | pingdirectory-1.eu-west-1 | pd-1.eu-cluster.ping-devops.com | 8601 | 8701 |
|      | pingdirectory-2.eu-west-1 | pd-2.eu-cluster.ping-devops.com | 8602 | 8702 |

## Cluster Startup Walkthrough

By now you can see that there are *many* variables that have been described. These variables exist to provide flexibility to accommodate various infrastructure constraints. For example, in some environments you cannot use the same port for each instance, so we must accommodate incrementing ports.

Continuing, it is helpful to know what happens when a cluster starts in order to understand why the initial creation of a cluster must be very prescriptive.

1. The first pod must start on its own and become healthy. This startup is critical to prevent replication islands. The very first time the very first pod starts, we call it "GENESIS". All other pods are dependent on this `SEED_POD` in the `SEED_CLUSTER` starting correctly by itself. The entire purpose of defining `SEED_POD` and `SEED_CLUSTER` variables is avoid multiple genesis scenarios.

2. After the first pod is healthy, it begins querying DNS for combinations of hostnames at their LDAPS port to find another PingDirectory instance.

In our first cluster, this would be the hostname of pingdirectory-1, but it could also be pingdirectory-0 of another cluster. After the query returns successful, creation of the replication topology automatically begins. From this point onward, the order in which instances start is less important.

## Deploying Across Multiple Regions with Multiple Load Balancers

If infrastructure constraints prevent you from using [Peered Clusters](deployK8s-AWS.html), an alternate option is to deploy with a separate LoadBalancer service for each PingDirectory pod.

The following diagram shows how you can use muliple load balancers.

![Multiple Load Balancers](../_images/multi-k8s-cluster-pingdirectory-multi-lb.png)

Advantages:

* Use the same well-known port, such as 1636/8989

* Separate IP addresses per instance

Disadvantages:

* DNS management

  * Separate hostname required per pod

This method is supported in our Helm charts with the `pingdirectory.services.loadBalancerServicePerPod` field.

## Deploy the Helm Example

Clone this `getting-started` [repository](https://github.com/pingidentity/pingidentity-devops-getting-started) to get the Helm values .yaml files for the exercise. There are two multi-region examples. For peered clusters, the example files are under the folder `30-helm/multi-region/pingdirectory`. For deploying with multiple load balancers, the example files are under the folder `30-helm/multi-region/pingdirectory-loadbalancer-per-pod`. After cloning:

1. Modify any external hostnames in the sample files as necessary - see the lines under `## CHANGEME` comments.

2. Deploy the first set of pods (the example here uses [kubectx](https://github.com/ahmetb/kubectx) to set the kubectl context).

   ```sh
   kubectx west
   helm upgrade --install example pingidentity/ping-devops -f 01-west.yaml
   ```

3. Wait for the example-pingdirectory pods to be running and ready.

4. Deploy the second set of pods.

   ```sh
   kubectx east
   helm upgrade --install example pingidentity/ping-devops -f 02-east.yaml
   ```

5. Wait for all example-pingdirectory pods to be running and ready.

6. Verify that pods are replicating.

   ```sh
   kubectx west
   kubectl exec example-pingdirectory-0 -- dsreplication status --showAll
   ```

## Cleanup

```sh
kubectx west
helm uninstall example
kubectl delete pvc --selector=app.kubernetes.io/instance=example
kubectx east
helm uninstall example
kubectl delete pvc --selector=app.kubernetes.io/instance=example
```

---

---
title: Deploy PingDirectoryProxy and PingDirectory with automatic backend discovery
description: Configure PingDirectoryProxy to automatically discover PingDirectory backend servers instead of manually listing them in the configuration
component: devops
page_id: devops::deployment/deployPDProxyBackendDiscovery
canonical_url: https://developer.pingidentity.com/devops/deployment/deployPDProxyBackendDiscovery.html
llms_txt: https://developer.pingidentity.com/devops/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  devops-configuring-the-proxy-instance-to-join-the-directory-topology: Configuring the proxy instance to join the directory topology
  devops-waiting-for-the-directory-topology-to-be-ready-before-starting: Waiting for the directory topology to be ready before starting
  devops-configuring-automatic-server-discovery-on-proxy-using-a-server-profile: Configuring automatic server discovery on proxy using a server profile
  devops-setting-load-balancing-algorithm-names-on-the-directory-instances: Setting load balancing algorithm names on the directory instances
  devops-removing-the-proxy-server-from-the-topology-on-pod-shutdown: Removing the proxy server from the topology on pod shutdown
  devops-automatic-server-discovery-when-directory-and-proxy-pods-are-split-across-multiple-clusters: Automatic server discovery when directory and proxy pods are split across multiple clusters
---

# Deploy PingDirectoryProxy and PingDirectory with automatic backend discovery

Since version 8.3 of PingDirectoryProxy, proxy servers can use [automatic server discovery](https://docs.pingidentity.com/pingdirectory/11.0/pingdirectoryproxy_server_administration_guide/pd_proxy_auto_backend_server_discovery.html) to determine the backend PingDirectory servers, rather than adding those servers individually to the configuration. This page describes how to use this feature with the PingDirectory and PingDirectoryProxy Docker images and the ping-devops Helm chart.

The directory and proxy Docker images added support for this feature as of the 2310 release, and the ping-devops Helm chart added support in release `0.9.20`.

## Configuring the proxy instance to join the directory topology

The first step of enabling automatic server discovery is to have the proxy server(s) join the topology of replicating directory servers. To enable this, the proxy Docker image supports the following variables:

* `JOIN_PD_TOPOLOGY`: Set to `true` to add the proxy instance to a directory topology

* `PINGDIRECTORY_HOSTNAME`: The hostname of the directory server to connect with when joining the topology

* `PINGDIRECTORY_LDAPS_PORT`: The LDAPS port of the directory server to connect with when joining the topology

If all three of these variables are set, the proxy server will join the designated topology after the server starts up.

### Waiting for the directory topology to be ready before starting

The designated directory server must be running for the proxy server to join the topology. To ensure directory is running before proxy attempts to join, a `wait-for` can be used.

For example, using the ping-devops Helm chart, the following values yaml instructs proxy to wait until the second `pingdirectory` pod is running before starting and attempting to join the topology. "releasename" can be replaced with the Helm release name.

```
initContainers:
  wait-for-pd:
    name: wait-for-pd
    image: pingidentity/pingtoolkit:2309
    command: ['sh', '-c', 'echo "Waiting for PingDirectory..." && wait-for releasename-pingdirectory-1.releasename-pingdirectory-cluster:1636 -t 300 -- echo "PingDirectory running"']

pingdirectory:
  container:
    replicaCount: 2
  enabled: true
  envs:
    SERVER_PROFILE_URL: https://github.com/pingidentity/pingidentity-server-profiles.git
    SERVER_PROFILE_PATH: baseline/pingdirectory
    LOAD_BALANCING_ALGORITHM_NAMES:dc_example_dc_com-fewest-operations;dc_example_dc_com-failover

pingdirectoryproxy:
  includeInitContainers:
  - wait-for-pd
  container:
    replicaCount: 1
  enabled: true
  envs:
    SERVER_PROFILE_URL: https://github.com/pingidentity/pingidentity-server-profiles.git
    SERVER_PROFILE_PATH: pingdirectoryproxy-automatic-server-discovery/pingdirectoryproxy
    JOIN_PD_TOPOLOGY: "true"
    PINGDIRECTORY_HOSTNAME: releasename-pingdirectory-0.releasename-pingdirectory-cluster
    PINGDIRECTORY_LDAPS_PORT: "1636"
```

## Configuring automatic server discovery on proxy using a server profile

The proxy server must also be configured via `dsconfig` to enable automatic server discovery. For an example, see the automatic server discovery [server profile](https://github.com/pingidentity/pingidentity-server-profiles/tree/master/pingdirectoryproxy-automatic-server-discovery).

Use the `pingdirectoryproxy-automatic-server-discovery/pingdirectoryproxy` profile path. The profile contains the static automatic-discovery `dsconfig` plus a startup hook for multi-region deployments.

When `JOIN_PD_TOPOLOGY=true` and both `K8S_CLUSTERS` and `K8S_CLUSTER` are set, the startup hook:

* Treats `K8S_CLUSTER` as the local proxy location

* Ensures each configured failover location exists as a peer location

* Sets the local location's `preferred-failover-location` values in the same order as the non-local cluster names in `K8S_CLUSTERS`

* Uses `PREFERRED_FAILOVER_LOCATIONS`, when set, as an explicit ordered subset of non-local clusters from `K8S_CLUSTERS`

* Re-applies that configuration on restart

## Setting load balancing algorithm names on the directory instances

To associate directory servers with the load balancing algorithms configured on the proxy server, the `load-balancing-algorithm-name` property must be set. This can be done with the `LOAD_BALANCING_ALGORITHM_NAMES` environment variable in the directory Docker image. When using multiple algorithm names, separate them with a `;`. See the above yaml snippet for an example.

## Removing the proxy server from the topology on pod shutdown

By default the proxy server will rejoin the topology automatically on restarts. In the `ping-devops` Helm chart, proxy does not use a persistent volume, so it will fully restart and rejoin the topology during each startup.

Another option, which allows for scaling down the number of proxy servers, is adding a `preStop` hook to remove the proxy server from the topology. In general this can cause slowness because it will run whenever a pod stops, but it ensures that scaling down the number of proxies does not leave outdated servers in the topology registry. For example:

```
pingdirectoryproxy:
  container:
    # Add the preStop hook to run the remove-defunct-server tool
    lifecycle:
      preStop:
        exec:
          command:
          - /opt/staging/hooks/90-shutdown-sequence.sh
```

## Automatic server discovery when directory and proxy pods are split across multiple clusters

When [deploying directory pods across multiple Kubernetes clusters](deployPDMultiRegion.html), some additional configuration needs to be added to allow proxy to join the directory topology and enable automatic server discovery.

Essentially, the proxy workload will need to have similar variables and network access as the directory workload (see the directory multi-cluster doc linked above). In addition, proxy will need the right variables set to join the topology and the right wait-for logic to wait for the other servers to be ready before starting and joining the topology.

For location-aware load balancing algorithms, joining the topology is not sufficient by itself. The proxy must also have peer `Location` objects and `preferred-failover-location` values configured for its local location. The automatic-discovery profile now derives that configuration from `K8S_CLUSTERS`, `K8S_CLUSTER`, and optionally `PREFERRED_FAILOVER_LOCATIONS` during startup.

For example, if `K8S_CLUSTERS="west east north"` and `K8S_CLUSTER="west"`, then the proxy creates peer locations for `east` and `north` and sets the local `west` location to prefer `east` first and `north` second. To override that default order or use only a subset, set `PREFERRED_FAILOVER_LOCATIONS` to the ordered non-local locations to apply.

See [here](https://github.com/pingidentity/pingidentity-devops-getting-started/tree/master/30-helm/multi-region/pingdirectoryproxy-automatic-server-discovery) for a complete Helm example.

---

---
title: Deploying PingFederate Across Multiple Kubernetes Clusters
description: Deploy a single PingFederate cluster spanning multiple peered Kubernetes clusters using DNS_PING and externalDNS for cross-region traffic
component: devops
page_id: devops::deployment/deployPFMultiRegion
canonical_url: https://developer.pingidentity.com/devops/deployment/deployPFMultiRegion.html
llms_txt: https://developer.pingidentity.com/devops/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  devops-prerequisites: Prerequisites
  devops-overview: Overview
  devops-what-you-will-do: What You Will Do
  devops-example-deployment: Example deployment
  devops-cleanup: Cleanup
---

# Deploying PingFederate Across Multiple Kubernetes Clusters

This section will discuss deploying a single PingFederate cluster that spans across multiple Kubernetes clusters.

Deploying PingFederate in multiple regions should not imply that spanning a single PingFederate cluster across multiple Kubernetes clusters is necessary or optimal. This scenario makes sense when you have:

* Traffic that can cross between regions at any time. For example, *west* and *east* and users may be routed to either location.

* Configuration that needs to be the same in multiple regions **and** there is no reliable automation to ensure this is the case

If all configuration changes are delivered via a pipeline, and traffic will not cross regions, having separate PingFederate clusters can work.

|   |                                                                                                                              |
| - | ---------------------------------------------------------------------------------------------------------------------------- |
|   | The set of pre-requisites required for AWS Kubernetes multi-clustering to be successful is found [here](deployK8s-AWS.html). |

Static engine lists, which may be used to extend traditional, on-premise PingFederate clusters is out of scope in this document.

## Prerequisites

* Two Kubernetes clusters created with the following requirements:

  * VPC IPs selected from RFC1918 CIDR blocks

  * The two cluster VPCs peered together

  * All appropriate routing tables modified in both clusters to send cross cluster traffic to the VPC peer connection

  * Security groups on both clusters to allow traffic for ports 7600 and 7700 in both directions

  * Verification that a pod in one cluster can connect to a pod in the second cluster on ports 7600 and 7700 (directly to the back-end IP assigned to the pod, not through an exposed service)

  * externalDNS enabled

    See example "AWS configuration" instructions [here](deployK8s-AWS.html)

* Helm client installed

## Overview

![PingFederate DNS PING MultiRegion Deployment Diagram](../_images/pf_dns_ping_overview_diagram.png)

The PingFederate Docker image default `instance/server/default/conf/tcp.xml` file points to DNS\_PING. After you have two peered Kubernetes clusters, spanning a PingFederate cluster across the two becomes easy. A single PingFederate cluster uses DNS\_PING to query a local headless service. In this example we use [externalDNS](https://github.com/kubernetes-sigs/external-dns) to give an externalName to the headless service. The `externalDNS` feature from the Kubernetes special interest group (SIG) creates a corresponding record on AWS Route53 and constantly updates it with container IP addresses of the backend PF engines.

|   |                                                                                                                                                                                                                                                    |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | If you are unable to use [externalDNS](https://github.com/kubernetes-sigs/external-dns), another way to expose the headless service across clusters is needed. HAProxy may be a viable option to explore and is beyond the scope of this document. |

## What You Will Do

* Clone the example files from the `getting-started` [Repository](https://github.com/pingidentity/pingidentity-devops-getting-started)

* Edit the externalName of the pingfederate-cluster service and the DNS\_QUERY\_LOCATION variable as needed

  Search the files for `# CHANGEME` comments to find where these changes need to be made.

* Deploy the clusters

* Cleanup

## Example deployment

Clone this `getting-started` [repository](https://github.com/pingidentity/pingidentity-devops-getting-started) to get the Helm values yaml for the exercise. The files are located under the folder `30-helm/multi-region/pingfederate`.

After cloning:

1. Update the first uncommented line under any `## CHANGEME` comment in the files. The changes will indicate the Kubernetes namespace and the externalName of the pingfederate-cluster service.

2. Deploy the first cluster (the example here uses [kubectx](https://github.com/ahmetb/kubectx) to set the kubectl context))

   ```sh
   kubectx west
   helm upgrade --install example pingidentity/ping-devops -f base.yaml -f 01-layer-west.yaml
   ```

3. Deploy the second cluster

   ```sh
   kubectx east
   helm upgrade --install example pingidentity/ping-devops -f base.yaml -f 01-layer-east.yaml
   ```

4. Switch back to the first cluster, and simulate a regional failure by removing the PingFederate cluster entirely:

   ```sh
   kubectx west
   helm uninstall example
   ```

5. Switch back to the second cluster and switch failover to active

   ```sh
   kubectx east
   helm upgrade --install example pingidentity/ping-devops -f base.yaml -f 02-layer-east.yaml
   ```

## Cleanup

```sh
kubectx east
helm uninstall example
kubectx west
helm uninstall example
```

---

---
title: Deployment Overview
description: Overview of deployment examples for running Ping products with Docker Compose and Helm/Kubernetes after completing the getting started stack
component: devops
page_id: devops::deployment/introduction
canonical_url: https://developer.pingidentity.com/devops/deployment/introduction.html
llms_txt: https://developer.pingidentity.com/devops/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
---

# Deployment Overview

This section assumes you have already deployed the full-stack server profile in [Get Started](../get-started/introduction.html).

In this section, you will find examples for using **Docker Compose** for running standalone product containers and **Helm/Kubernetes** to deploy Ping products in typical combinations.

---

---
title: Docker Compose
description: Deploy standalone PingAccess, PingCentral, PingDirectory, or PingFederate containers using Docker Compose examples
component: devops
page_id: devops::deployment/deployCompose
canonical_url: https://developer.pingidentity.com/devops/deployment/deployCompose.html
llms_txt: https://developer.pingidentity.com/devops/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  devops-single-product-examples-only: Single product examples only
---

# Docker Compose

## Single product examples only

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | Docker Compose was used by Ping in the past for basic orchestration and examples. We are no longer maintaining multi-product or clustering docker compose examples. All of those files have been removed from this repository. The only examples remaining are for deploying individual products. For orchestration of multiple products, clustering, and other use cases, see [Helm Chart Examples](https://developer.pingidentity.com/helm/examples/index.html). |

Example docker compose files to deploy standalone instances of PingAccess, PingCentral, PingDirectory or PingFederate are in the [Github repository](https://github.com/pingidentity/pingidentity-devops-getting-started/tree/master/11-docker-compose/00-standalone). Refer to the comments in each provided file for instructions on accessing the product after running `docker compose up` from the directory of the product in which you are interested.

---

---
title: Environment considerations
description: Address PingData deployment considerations, including NFS extension installation constraints and PingDirectory inotify watch limits
component: devops
page_id: devops::deployment/pingDataEnvironmentConsiderations
canonical_url: https://developer.pingidentity.com/devops/deployment/pingDataEnvironmentConsiderations.html
llms_txt: https://developer.pingidentity.com/devops/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  devops-network-file-system-nfs-constraints: Network File System (NFS) constraints
  devops-pingdirectory-inotify-watch-limit-requirement: PingDirectory inotify watch limit requirement
---

# Environment considerations

## Network File System (NFS) constraints

All PingData products use the `manage-extension` tool for installing extensions. Due to how the tool operates, it can lead to issues when the deployment involves NFS.

If your deployment uses NFS, rather than using the `manage-extensions` tool, unzip the extension manually and add it to the appropriate directory.

The following example script, called `181-install-extensions.sh.post`, loops through the extensions to unzip and then removes them from the server profile.

```sh
#!/usr/bin/env sh
# Loop through extensions to unzip, then remove them from the server profile
PROFILE_EXTENSIONS_DIR="${PD_PROFILE}/server-sdk-extensions"
if test -d "${PROFILE_EXTENSIONS_DIR}"; then
  find "${PROFILE_EXTENSIONS_DIR}" -type f -name '*.zip' -print > /tmp/_extensionList
  while IFS= read -r _extensionFile; do
      echo "Installing extension: ${_extensionFile}"
      unzip -q "${_extensionFile}" -d /opt/out/instance/extensions/
      rm "${_extensionFile}"
  done < /tmp/_extensionList
  rm -f /tmp/_extensionList
fi
```

## PingDirectory inotify watch limit requirement

When using inotify with PingDirectory, you must set a watch limit on the host system. This value cannot be set from a docker container, and the value read within a docker container is always the host value.

For more information, refer to [Set file system event monitoring (inotify)](https://docs.pingidentity.com/pingdirectory/latest/installing_the_pingdirectory_suite_of_products/pd_ds_set_file_system_event_monitoring.html) in the PingDirectory documentation.

---

---
title: Ingress on Local Kind Cluster
description: Configure an NGINX ingress for a local kind Kubernetes cluster to access Ping product consoles such as PingFederate, PingAccess, and PingDirectory
component: devops
page_id: devops::deployment/deployHelmLocalIngress
canonical_url: https://developer.pingidentity.com/devops/deployment/deployHelmLocalIngress.html
llms_txt: https://developer.pingidentity.com/devops/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  devops-prerequisites: Prerequisites
  devops-assumptions: Assumptions
  instructions: Instructions
  create-ingresses: Create ingresses
  cleaning-up: Cleaning up
---

# Ingress on Local Kind Cluster

If you have deployed the local kind cluster as outlined on the [Deploy a local Kubernetes Cluster](deployLocalK8sCluster.html) page, follow these instructions to use an ingress for accessing your products.

## Prerequisites

* A kind cluster deployed with ingress enabled. For this guide, the cluster name `ping` is assumed

* The hostname aliases have been appended to the `/etc/hosts` file

* You have created the secret for your DevOps user and key for retrieving licenses

## Assumptions

With the `/etc/hosts` file entries created from the page linked above, the release in helm **must** be `myping` for the hostnames to work with the configuration here. Consider the first entry as an example:

```
127.0.0.1 myping-pingaccess-admin.pingdemo.example ...
```

When using our charts, the release name provided to helm is prepended - that is what provides the `myping-` portion of the hostname in the file. The `pingdemo.example` domain suffix is provided through the ingress definitions as shown later on this page. So, the structure is:

```
<helm-release-name>-<ping-product-service>.<domain-name-from-ingress>
```

If you use a release name other than `myping` or a domain other than `pingdemo.example` you will need to update the aliases in `/etc/hosts`/ accordingly.

## Instructions

There is a file under the `30-helm` directory of this repository named `ingress.yaml`. Modify this file for use with a local cluster:

* Replace `insert domain name here` with your domain name (pingdemo.example in this guide)

* Edit line 11, removing the `-public` suffix for the class

The file should look as shown here:

```
global:
  envs:
    PING_IDENTITY_ACCEPT_EULA: "YES"
  ingress:
    enabled: true
    addReleaseNameToHost: prepend
    defaultDomain: "pingdemo.example"
    defaultTlsSecret:
    annotations:
      nginx.ingress.kubernetes.io/backend-protocol: "HTTPS"
      kubernetes.io/ingress.class: "nginx"
```

## Create ingresses

When deploying using helm and one of the example YAML files in the 30-helm directory, also pass in the ingress.yaml file to include the ingress definitions as part of the overall deployment.

For example, to use the `everything.yaml` and include ingresses, you would run the following command from the 30-helm directory (after updating the ingress.yaml file):

```
helm upgrade --install myping pingidentity/ping-devops -f everything.yaml -f ingress.yaml
```

After everything has started, you will see the same pods and services as in the getting started example. In addition, you will see ingress definitions in the same namespace as the products:

```
# List ingress definitions
kubectl get ingress

# Output
NAME                         CLASS    HOSTS                                       ADDRESS     PORTS     AGE
myping-pingaccess-admin      <none>   myping-pingaccess-admin.pingdemo.example      localhost   80, 443   47m
myping-pingaccess-engine     <none>   myping-pingaccess-engine.pingdemo.example     localhost   80, 443   47m
myping-pingauthorize         <none>   myping-pingauthorize.pingdemo.example         localhost   80, 443   47m
myping-pingdataconsole       <none>   myping-pingdataconsole.pingdemo.example       localhost   80, 443   47m
myping-pingdirectory         <none>   myping-pingdirectory.pingdemo.example         localhost   80, 443   47m
myping-pingfederate-admin    <none>   myping-pingfederate-admin.pingdemo.example    localhost   80, 443   47m
myping-pingfederate-engine   <none>   myping-pingfederate-engine.pingdemo.example   localhost   80, 443   47m
```

The HOSTS column reflects the entries added to the `/etc/hosts` file.

To access a given service, enter the HOSTS entry in your browser (you will have to accept the self-signed certificate). For example, to view the Ping Federate console, you would access **<https://myping-pingfederate-admin.pingdemo.example/>**. For the Ping Data console, **<https://myping-pingdataconsole.pingdemo.example>** and so on.

Here are the credentials and URLs. This table is similar to the getting started example but reflects the release name used on this page:

| Product                                                                             | Connection Details                                                                                                                                                           |
| ----------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [PingFederate](https://myping-pingfederate-admin.pingdemo.example/pingfederate/app) | * URL: <https://myping-pingfederate-admin.pingdemo.example/pingfederate/app>

* Username: administrator

* Password: 2FederateM0re                                           |
| [PingDirectory](https:///myping-pingdataconsole.pingdemo.example)                   | - URL: <https://myping-pingdataconsole.pingdemo.example/console>

- Server: ldaps\://myping-pingdirectory-cluster:1636

- Username: administrator

- Password: 2FederateM0re |
| [PingAccess](https://myping-pingaccess-admin.pingdemo.example)                      | * URL: <https://myping-pingaccess-admin.pingdemo.example>

* Username: administrator

* Password: 2FederateM0re                                                              |
| [PingAuthorize](https:///myping-pingdataconsole.pingdemo.example)                   | - URL: <https://myping-pingdataconsole.pingdemo.example/console>

- Server: ldaps\://myping-pingauthorize-cluster:1636

- Username: administrator

- Password: 2FederateM0re |

## Cleaning up

Since the ingresses are deployed as part of the overall release, deleting the release will also remove the ingress definitions (leaving the ingress controller intact).

The ingress controller will be removed when the cluster is deleted. If you only want to remove the ingress controller, you can either:

* Run `kubectl delete -f https://raw.githubusercontent.com/kubernetes/ingress-nginx/main/deploy/static/provider/kind/1.23/deploy.yaml` if you installed the controller from Github

  **OR**

* Run `kubectl delete -f ./20-kubernetes/kind-nginx.yaml` if you used the local copy to install the controller.

---

---
title: Kubernetes deployments for cloud platforms
description: Find links to Kubernetes deployment guides for Ping products on Amazon EKS and Microsoft Azure AKS cloud platforms
component: devops
page_id: devops::deployment/deployK8sCloud
canonical_url: https://developer.pingidentity.com/devops/deployment/deployK8sCloud.html
llms_txt: https://developer.pingidentity.com/devops/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  devops-before-you-begin: Before you begin
  devops-aws-eks: AWS EKS
  devops-aks: AKS
---

# Kubernetes deployments for cloud platforms

We currently have instructions for typical configuration of Kubernetes for use with Ping products on these platforms:

* Amazon Web Services (AWS) Elastic Kubernetes Service (EKS)

* Microsoft Azure Kubernetes Service (AKS)

Each hosting platform supports and manages Kubernetes differently.

## Before you begin

You must:

* Complete [Get Started](../get-started/introduction.html) to set up your DevOps environment and run a test deployment of the products.

* Create a Kubernetes cluster on one of these platforms:

  * Amazon EKS

  * Microsoft AKS

* Create a Kubernetes secret using your DevOps credentials. For more information, see *For Kubernetes* in [Using Your DevOps User and Key](../how-to/devopsUserKey.html).

## AWS EKS

See [Peering VPCs for multi-region EKS deployments](deployK8s-AWS.html).

## AKS

See [Azure Kubernetes Service](deployK8s-AKS.html).

---

---
title: Operating Patterns
description: Compare PingFederate configuration management patterns, including Terraform-based config and persisted admin console data mounts
component: devops
page_id: devops::deployment/deploymentPatterns
canonical_url: https://developer.pingidentity.com/devops/deployment/deploymentPatterns.html
llms_txt: https://developer.pingidentity.com/devops/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  devops-pingfederate-configuration-management: "Pattern: PingFederate Configuration Management"
  devops-1-infrastructure-configuration: 1) Infrastructure Configuration
  devops-examples-of-managed-components: Examples of managed components:
  devops-orchestration: Orchestration
  devops-2-server-configuration: 2) Server Configuration
  examples-of-managed-components: Examples of managed components:
  devops-orchestration-2: Orchestration
  devops-3-application-configuration-app-config: 3) Application Configuration (App Config)
  devops-managed-components: Managed components
  devops-orchestration-3: Orchestration
  devops-using-the-pingfederate-terraform-provider: "Pattern: Using the PingFederate Terraform provider"
  devops-pingfederate-data-mount: "Pattern: Using a Data Mount to Persist Application Configuration for PingFederate Admin Console"
  devops-data-mount-helm-example: Data Mount Helm Example
  devops-values-with-this-approach: Advantages with this approach
  devops-cautions-with-this-approach: Cautions with this approach
---

# Operating Patterns

This page discusses how to have a successful first day and beyond.

After you are comfortable with the deployment examples in the getting-started repository, you can shift your focus to managing ongoing operations of the products that are relevant to you. Since it is not feasible to cover every operating scenario, this section will focus on guidance to identify an operating pattern suitable for your organization.

The PingFederate application is used as an example of performing this assessment with some example patterns.

## Pattern: PingFederate Configuration Management

PingFederate has a variety of operating patterns. These patterns typically involve a trade-off between ease of implementation and mitigation of deployment risks.

To simplify the moving parts, PingFederate configuration can be categorized into three patterns:

### 1) Infrastructure Configuration

#### Examples of managed components:

* Resource allocation (CPU/Memory/Storage)

* Client Ingress (Access and Hostnames)

* Image Version

* Exposed Ports

* Environment Variable Definitions

* Secrets Definitions

#### Orchestration

* These items are defined in the [release values.yaml file](https://helm.sh/docs/chart_template_guide/values_files/) and any changes here triggers an update.

### 2) Server Configuration

This pattern can be oversimplified to *everything outside of* the `/instance/server/default/data` folder or `/instance/bulk-config/data.json`.

#### Examples of managed components:

* `*.properties` files

* Integration Kits

* HTML templates

* log formatting (log4j2.xml)

#### Orchestration

These items are stored in the [Server Profile](../how-to/containerAnatomy.html) and any change *should* trigger an update. It is up to the implementer to ensure that happens. Triggering an update can be done by adding a non-functional variable in `values.yaml` to track the current profile "version". Example: `SERVER_PROFILE_VERSION: v1.1`

### 3) Application Configuration (App Config)

Application configuration can be managed via any combination of the following, according to customer internal configuration management requirements:

* The [PingFederate Terraform provider](https://terraform.pingidentity.com/getting-started/pingfederate/) - a way to declare the "end state" of configuration of a PingFederate server. Terraform can be used to identify and correct configuration drift in an environment ad-hoc or on a schedule. Configuration managed through Terraform uses the PingFederate administration API and requires the server to have successfully started. Configuration changes typically require replication to the engine nodes, but do not require a restart of the PingFederate service to take effect.

* The `/instance/server/default/data` folder in the server profile - a way to declare the initial start-up configuration of PingFederate admin and engine nodes by providing a foundational filesystem structure. The configuration is pulled from Git and applied during container start-up, while changes to this configuration typically requires servers to be restarted to take effect. This configuration method is typically used when deploying new adapter JAR files or deployments to the PingFederate server's built-in Jetty container.

* The `/instance/bulk-config/data.json` file in the server profile - a way to declare the initial start-up configuration of the PingFederate service by providing a foundational configuration package. The configuration is pulled from Git and applied during container start-up, while changes to this configuration typically requires a server restart to take effect.

#### Managed components

This category is the core PingFederate configuration. This pattern incorporates changes that are typically made through the UI or Admin APIs.

#### Orchestration

Depending on your operating pattern, changes here may be delivered through a rolling update or by configuration replication.

## Pattern: Using the PingFederate Terraform provider

Terraform updates should trigger server replication to the engine nodes at the end of the PingFederate configuration pipeline.

The admin server should use a persistent volume so it can recover the same admin configuration as before if the pod is restarted. If the clustered engine pods are restarted, they refresh their configuration from the admin server during startup. See the below section for details on how to configure a persistent volume.

The Terraform configuration should be managed in a repository separate from infrastructure and server profile configuration. Changes made to the PingFederate server via Terraform require replication to PingFederate engine nodes as the final step of configuration and do not require rolling restarts to the PingFederate deployment for changes to take effect.

For more information on using the PingFederate Terraform provider, see the [getting started guide](https://terraform.pingidentity.com/getting-started/pingfederate/).

## Pattern: Using a Data Mount to Persist Application Configuration for PingFederate Admin Console

In the most common pattern, a user would attach a persistent volume (PV) to `/opt/out/instance/server/default/data` *only* on the PingFederate Admin Console.

This model is intended to be used when PingFederate Administrators need to deliver configuration through the UI in *each environment, including production*. Another reason for this use case may be if SP connections are allowed to be created by app developers using the Admin API. In both of these scenarios, the defining factor is that there are mutations in the production Admin console that are not being tracked in any other way, such as through source control, and therefore must be persisted.

**Attributes of this pattern:**

* App Config is persisted in each SDLC environment (e.g. Dev, QA, Prod)

* App Config promotion is done manually or via the Admin API

* App Config is replicated from Admin Console to Engines

* Server Config is maintained and delivered via the server profile

* Server profile *does not* include App Config

* Server profile ***must not*** have `instance/bulk-config/data.json` or `/instance/server/default/data`

* Backups are taken regularly to provide recovery in case of PV loss or corruption

### Data Mount Helm Example

Helm values relevant to this configuration may look like:

```
pingfederate-admin:
  enabled: true
  container:
    replicaCount: 1
  envs:
    SERVER_PROFILE_URL: <insert your server profile URL here>
    SERVER_PROFILE_PATH: <insert your server profile path here>
    SERVER_PROFILE_VERSION: <server profile version>
  workload:
    type: StatefulSet
    statefulSet:
      persistentvolume:
        enabled: true
        volumes:
          out-dir:
             NOTE THIS PVC DEFINITION 
            mountPath: /opt/out/instance/server/default/data
            persistentVolumeClaim:
              accessModes:
              - ReadWriteOnce
              storageClassName:
              resources:
                requests:
                  storage: 8Gi

pingfederate-engine:
  enabled: true
  envs:
    SERVER_PROFILE_URL: <insert your server profile URL here>
    SERVER_PROFILE_PATH: <insert your server profile path here>
    SERVER_PROFILE_VERSION: <server profile version>
  container:
    replicaCount: 3
  workload:
    type: Deployment
    deployment:
      strategy:
        type: RollingUpdate
        rollingUpdate:
          maxSurge: 1
          maxUnavailable: 0
```

The key aspect here is `pingfederate-admin.workload.statefulset.persistentvolume.volumes.out-dir.mountPath=/opt/out/instance/server/default/data`. This location is where all UI configuration (App Config) is stored as files. As this location is the `mountPath`, PingFederate administrators have the freedom to deliver any files *not* used in `/opt/out/instance/server/default/data` via a Server Profile.

For example, adding a new IDP adapter requires a restart of the service in order for the adapter to be identified and available to App Config. The steps in this case would be:

1. Add the adapter at `<server profile URL>/<server profile path>/pingfederate/instance/server/default/deploy/idp-adapter-name-1.jar`

2. Update `SERVER_PROFILE_VERSION: <current version>` -> `SERVER_PROFILE_VERSION: <new version>` on both the admin and engine deployments (for example, v1.1 -> v1.2)

3. Run `helm upgrade --install myping pingidentity/ping-devops -f /path/to/values.yaml`

If the release already exists, the variable change signifies that the definition has mutated, and therefore must be redeployed. The admin pod will be deleted and recreated while the engines will surge and roll one by one.

Reference links:

* [K8s - Performing a Rolling Update](https://kubernetes.io/docs/tutorials/kubernetes-basics/update/update-intro/)

* [K8s - Update a deployment](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/#updating-a-deployment)

#### Advantages with this approach

* Managing App Config is more familiar to PingFederate administrators with traditional experience

* Fewer parts to consider when building a CI/CD pipeline because there is no configuration export and templating needed

* Ability to have configurations different in each environment

#### Cautions with this approach

* There is more room for user configuration error and possible outages because configurations are not promoted with automated testing

---

---
title: Peering VPCs for multi-region EKS deployments
description: Configure VPC peering with AWS transit gateways to connect multi-region Amazon EKS clusters for Ping product deployments
component: devops
page_id: devops::deployment/deployK8s-AWS
canonical_url: https://developer.pingidentity.com/devops/deployment/deployK8s-AWS.html
llms_txt: https://developer.pingidentity.com/devops/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  devops-preparing-aws-eks-for-multi-region-deployments: Preparing AWS EKS for Multi-Region Deployments
  devops-prerequisites: Prerequisites
  devops-create-the-multi-region-clusters: Create the multi-region clusters
---

# Peering VPCs for multi-region EKS deployments

## Preparing AWS EKS for Multi-Region Deployments

In this guide you will deploy two Kubernetes clusters, each in a different Amazon Web Services (AWS) region. An AWS virtual private cloud (VPC) is assigned and dedicated to each cluster. You will also add communication between these clusters, using a transit gateway. Throughout this document, "VPC" is synonymous with "cluster".

### Prerequisites

Before you begin, you must have

* AWS account permissions to create clusters

### Create the multi-region clusters

1. Create VPCs.

   * Sign on to the AWS console and navigate to the **VPC** service.

   * Toggle to the `eu-west-1` region.

   * Select **Your VPCs** (under Virtual Private Cloud) and click **Create VPC**

   * Add a name tag, such as `demo-vpc-eu-west-1`

   * Add a IPv4 CIDR, such as `10.0.0.0/16`

   * Click **Create VPC**.

     > Make note of the `VpcId` and `IPv4 CIDR` values for the `eu-west-1` and `us-east-1` VPCs for use in subsequent steps.

   * Repeat this step in `us-east-1` region.

2. Create the transit gateway for each region on which your deployment is being hosted. Toggle to the `eu-west-1` region.

   * Navigate to the **Transit gateways** section and click **Create transit gateway**.

   * Add a name tag such as `demo-tgw-eu-west-1`.

   * Add a unique Amazon side Autonomous System Number for each region (ex. 64512 or 64513).

   * Disable both the `Default route table association` and `Default route table propagation`.

     |   |                                                                                                                                                                                                                                                                |
     | - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
     |   | If you enable the options above, the default association route table and propagation route table will be created. This action may not suit more complex routing needs; see below for details on how to manually set the associations/propagation route tables. |

   * Click **Create transit gateway**.

   * Repeat this step in `us-east-1` region.

3. Create the transit gateway peering connection attachment. Toggle to the `eu-west-1` region.

   * Navigate to the **Transit gateway attachments** section and click **Create transit gateway attachments**.

   * Add a name tag such as `demo-peering-attachment-us-east-1`.

     |   |                                                                                                     |
     | - | --------------------------------------------------------------------------------------------------- |
     |   | This name refers to the region to which it is peering, not the region in which it is being created. |

   * Select the Transit gateway id that you just made in the `eu-west-1` region.

   * Change **Attachment type** to `Peering Connection`.

   * For **Region** select `us-east-1`.

   * For **Transit gateway (accepter)** add the Transit gateway id that you just made in the `us-east-1` region.

   * Click **Create transit gateway attachment** .

4. Accept transit gateway peering attachment.

   * After the transit gateway peering connection shows `pending acceptance` as its **State**, toggle to the `us-east-1` region and select **Transit gateway attachments**.

   * You should see the attachment you just made. Select **Actions** and click accept.

   * Add a name to this attachment such as `demo-peering-attachment-eu-west-1`.

     |   |                                                                                                     |
     | - | --------------------------------------------------------------------------------------------------- |
     |   | This name refers to the region to which it is peering, not the region in which it is being created. |

5. Attach VPCs to the transit gateways in each region. Toggle to the `eu-west-1` region.

   * Navigate to the **Transit gateway attachments** section and click **Create transit gateway attachments**.

   * Add a name tag such as `demo-vpc-eu-west-1`.

   * Select the Transit gateway id that you just made in the `eu-west-1` region.

   * Select the Vpc Id that you made note of in step 3 for the `eu-west-1` region.

   * Click **Create transit gateway attachment**.

   * Repeat this step in `us-east-1` region.

6. Accept transit gateway VPC attachments. Toggle to the `eu-west-1` region.

   * Navigate to the **Transit gateway attachments** section and click **Create transit gateway attachments**.

   * You should see the vpc attachment you just made. Select **Actions** and click accept.

     |   |                                                                                                                                                                                                                      |
     | - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
     |   | If you are using different accounts to create transit gateways and their attachments, the name tag will not be visible here. In this situation, you should add an attachment name now, such as `demo-vpc-eu-west-1`. |

   * Repeat this step in `us-east-1` region.

7. Add routes to vpc route table. Toggle to the `eu-west-1` region.

   * Navigate to the **Route tables** section and select the route table for the Vpc Id you created.

   * Select **Routes** in the bottom third of the page.

   * Select **Edit routes** then click **Add route**.

   * Add a destination that is more broad than the local one that is present. For example if the local destination is `10.0.0.0/16` add `10.0.0.0/8`.

   * For the **Target** select `Transit Gateway` and add then add the Transit gateway id that you created in this region.

   * Click **Save changes**.

   * Repeat this step in `us-east-1` region.

8. Configure the transit gateway route tables. Toggle to the `eu-west-1` region.

   * Navigate to the **Transit gateway route tables** section and click **Create transit gateway route table**.

   * Add a name tag such as `demo-eu-west-1-route-table`.

   * Select the Transit gateway id that you created in this region.

   * Click **Create transit gateway route table**.

   * Repeat this step in `us-east-1` region.

9. Associate the transit gateway. Toggle to the `eu-west-1` region.

   * After the transit gateway route table has been successfully created, select that route table and click **Associations** then **Create association**.

   * Choose the VPC attachment for this region and click **Create association**.

10. Add static routes to the transit gateway. Toggle to the `eu-west-1` region.

    * Select that route table that you just created an association for and click **Routes** then **Create static route**.

    * Add the`IPv4 CIDR` for the remote VPC that you made note of in step 3 for the `us-east-1` region.

    * Select the transit gateway peering connection attachment.

    * Click **Create static route**.

    * Repeat this step in `us-east-1` region.

11. Create a blackout static route to ensure the transit gateway drops any other network traffic. Toggle to the `eu-west-1` region.

    * Select **Create static route**

    * Add 10.0.0.0/8 as the CIDR

    * Select Blackhole

    * Click **Create static route**.

    * Repeat this step in `us-east-1` region.

At this point you should have a system of connected VPCs on the `us-east-1` `eu-west-1` regions. You can now deploy EC2 instances to these VPCs and communicate between them.

---

---
title: PingDirectoryProxy Automatic Server Discovery Demo
description: Walk through a demo deploying PingDirectoryProxy automatic server discovery across multi-region Kubernetes clusters
component: devops
page_id: devops::deployment/deployPDProxyDiscoveryDemoWalkthrough
canonical_url: https://developer.pingidentity.com/devops/deployment/deployPDProxyDiscoveryDemoWalkthrough.html
llms_txt: https://developer.pingidentity.com/devops/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  devops-purpose: Purpose
  devops-expected-deployment-flow: Expected Deployment Flow
  devops-local-working-directory: Local Working Directory
  devops-helm-repository: Helm Repository
  devops-expected-behavior: Expected Behavior
  devops-common-validation-commands: Common Validation Commands
  devops-demo-1-docker-desktop-namespace-simulation: "Demo 1: Docker Desktop Namespace Simulation"
  devops-docker-prerequisites: Docker Prerequisites
  devops-create-namespaces: Create Namespaces
  devops-create-devops-secret: Create DevOps Secret
  devops-create-docker-desktop-values: Create Docker Desktop Values
  devops-deploy-docker-desktop-demo: Deploy Docker Desktop Demo
  devops-confirm-dns-and-tcp-reachability: Confirm DNS and TCP Reachability
  devops-confirm-default-hook-behavior: Confirm Default Hook Behavior
  devops-restart-validation: Restart Validation
  devops-explicit-preferred-failover-variation: Explicit Preferred Failover Variation
  devops-invalid-override-includes-local-cluster: Invalid Override Includes Local Cluster
  devops-invalid-override-references-unknown-cluster: Invalid Override References Unknown Cluster
  devops-docker-desktop-cleanup: Docker Desktop Cleanup
  devops-demo-2-local-multi-cluster-with-kind: "Demo 2: Local Multi-Cluster with kind"
  devops-kind-prerequisites: kind Prerequisites
  devops-create-kind-clusters: Create kind Clusters
  devops-inspect-docker-network: Inspect Docker Network
  devops-install-metallb: Install MetalLB
  devops-run-dnsmasq: Run dnsmasq
  devops-configure-coredns-forwarding: Configure CoreDNS Forwarding
  devops-create-namespaces-and-secrets: Create Namespaces and Secrets
  devops-create-kind-values: Create kind Values
  devops-deploy-west: Deploy West
  devops-deploy-east: Deploy East
  devops-confirm-cross-cluster-tcp-reachability: Confirm Cross-Cluster TCP Reachability
  devops-wait-for-workloads: Wait for Workloads
  devops-confirm-kind-default-hook-behavior: Confirm kind Default Hook Behavior
  devops-kind-explicit-preferred-failover-variation: kind Explicit Preferred Failover Variation
  devops-kind-invalid-local-override: kind Invalid Local Override
  devops-kind-invalid-unknown-override: kind Invalid Unknown Override
  devops-kind-restart-validation: kind Restart Validation
  devops-kind-cleanup: kind Cleanup
  devops-minikube-variant: minikube Variant
  devops-minikube-prerequisites: minikube Prerequisites
  devops-create-profiles: Create Profiles
  devops-loadbalancer-support: LoadBalancer Support
  devops-minikube-dnsmasq-and-coredns: minikube dnsmasq and CoreDNS
  devops-minikube-namespaces-and-secrets: minikube Namespaces and Secrets
  devops-minikube-deploy-west: minikube Deploy West
  devops-minikube-deploy-east: minikube Deploy East
  devops-minikube-cleanup: minikube Cleanup
  devops-troubleshooting: Troubleshooting
  devops-demo-closeout-evidence: Demo Closeout Evidence
---

# PingDirectoryProxy Automatic Server Discovery Demo

## Purpose

This example demonstrates PingDirectoryProxy automatic server discovery from a typical multi-region environment.

Prequisites:

* Access to the published `pingidentity/ping-devops` Helm chart. Ensure you are at version 0.12.1 or later

* Access to the `pingidentity-server-profiles` GitHub repository

The demonstrations below illustrate one method of deploying PingDirectoryProxy to use location-aware load-balancing algorithms without requiring manual post-deployment `dsconfig` operations. The hook provided in the example server profile automatically configures the proxy's local location and preferred failover locations based on environment variables.

|   |                                                                                                                                                                                                                         |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The server profile hook script and other files provided for this example are for demonstration purposes only. They should be considered only as a starting point for similar functionality in a production environment. |

## Expected Deployment Flow

The west deployment is the seed side of the example and is applied first. The west PingDirectory pods start first, with `west-pingdirectory-0` acting as the seed server for topology operations.

The west PingDirectoryProxy pod is also created by the west Helm release, but its init container waits for the east PingDirectory pods to converge before it starts. This action prevents PingDirectoryProxy from joining the topology while the PingDirectory servers are still converging.

After west PingDirectory pods are running, apply the east deployment. The east PingDirectory pods use the west seed server when they join the topology. The east PingDirectoryProxy pod then waits for the west PingDirectoryProxy pod, so proxy topology operations happen after the directory topology is established.

To summarize, the intended readiness order is:

1. West PingDirectory pods start and establish the seed topology.

2. East PingDirectory pods start and join the west seed topology.

3. West PingDirectoryProxy pod starts, joins the PingDirectory topology, and configures the local `west` location with `east` as failover.

4. East PingDirectoryProxy pod starts, joins the PingDirectory topology, and configures the local `east` location with `west` as failover.

## Local Working Directory

For this walkthrough, run the commands from a local directory. Create a local demo directory for generated values and DNS files:

```shell
mkdir pdproxy-discovery-demo
cd pdproxy-discovery-demo
```

## Helm Repository

Add or refresh the published Ping Identity Helm repository:

```shell
helm repo add pingidentity https://helm.pingidentity.com/
helm repo update pingidentity
helm search repo pingidentity/ping-devops --versions | head
```

## Expected Behavior

Without `PREFERRED_FAILOVER_LOCATIONS`:

* `K8S_CLUSTER` becomes the local proxy location

* All non-local entries from `K8S_CLUSTERS` become preferred failover locations

* Ordering follows `K8S_CLUSTERS`

With `PREFERRED_FAILOVER_LOCATIONS`:

* The hook uses that value as an explicit ordered subset

* Each value must exist in `K8S_CLUSTERS`

* The local `K8S_CLUSTER` must not be included

* Duplicate preferred failover values are ignored

Example:

```shell
K8S_CLUSTERS="west east"
K8S_CLUSTER="west"
PREFERRED_FAILOVER_LOCATIONS="east"
```

Expected local proxy location result:

```shell
west preferred-failover-location: east
```

## Common Validation Commands

Run these in a session established through `kubectl exec` in a proxy pod:

```shell
dsconfig list-locations
dsconfig get-location-prop --location-name <local-location>
dsconfig list-server-instances --property load-balancing-algorithm-name
ldapsearch -b cn=monitor "(objectclass=ds-load-balancing-algorithm-monitor-entry)"
```

Useful filtered monitor command:

```shell
ldapsearch \
  -b cn=monitor \
  "(objectclass=ds-load-balancing-algorithm-monitor-entry)" \
  algorithm-name health-check-state local-servers-health-check-state \
  non-local-servers-health-check-state num-available-servers ldap-external-server
```

Expected success:

* `dsconfig list-locations` includes local and configured failover locations

* `dsconfig get-location-prop --location-name <local>` shows expected `preferred-failover-location` values

* `dsconfig list-server-instances --property load-balancing-algorithm-name` shows PingDirectory instances assigned to the expected LBAs

* LBA monitor entries report `AVAILABLE`, not `No servers configured`

## Demo 1: Docker Desktop Namespace Simulation

This first demonstration validates the server-profile hook with minimal infrastructure. It is not a true multi-cluster networking test, but rather simulates two regions with two namespaces in one Kubernetes cluster and uses Kubernetes DNS names instead of external DNS.

### Docker Prerequisites

Required:

* Docker Desktop with Kubernetes enabled

* `kubectl`

* `helm`

* [Ping Identity DevOps](../how-to/devopsRegistration.html) credentials available as environment variables or in a local `.env` file

Recommended Docker Desktop resources:

* CPUs: 6 or more

* Memory: 12 GB or more

* Disk: 30 GB free

Verify:

```shell
kubectl config current-context
kubectl cluster-info
helm version
```

### Create Namespaces

```shell
kubectl create namespace west
kubectl create namespace east
```

If they already exist:

```shell
kubectl get namespace west east
```

### Create DevOps Secret

Using an existing `.env` file:

```shell
kubectl -n west create secret generic devops-secret \
  --from-env-file=.env \
  --dry-run=client -o yaml | kubectl -n west apply -f -

kubectl -n east create secret generic devops-secret \
  --from-env-file=.env \
  --dry-run=client -o yaml | kubectl -n east apply -f -
```

Using existing environment variables:

```shell
kubectl -n west create secret generic devops-secret \
  --from-literal=PING_IDENTITY_DEVOPS_USER="$PING_IDENTITY_DEVOPS_USER" \
  --from-literal=PING_IDENTITY_DEVOPS_KEY="$PING_IDENTITY_DEVOPS_KEY" \
  --from-literal=PING_IDENTITY_ACCEPT_EULA="YES" \
  --type=Opaque \
  --dry-run=client -o yaml | kubectl -n west apply -f -

kubectl -n east create secret generic devops-secret \
  --from-literal=PING_IDENTITY_DEVOPS_USER="$PING_IDENTITY_DEVOPS_USER" \
  --from-literal=PING_IDENTITY_DEVOPS_KEY="$PING_IDENTITY_DEVOPS_KEY" \
  --from-literal=PING_IDENTITY_ACCEPT_EULA="YES" \
  --type=Opaque \
  --dry-run=client -o yaml | kubectl -n east apply -f -
```

Verify:

```shell
kubectl -n west get secret devops-secret
kubectl -n east get secret devops-secret
```

### Create Docker Desktop Values

Create `./dd-west.yaml`:

```shell
cat > ./dd-west.yaml <<'YAML'
global:
  image:
    tag: "2603"

initContainers:
  wait-for-east-pd:
    name: wait-for-east-pd
    image: pingidentity/pingtoolkit:2603
    command:
    - sh
    - -c
    - |
      echo "Waiting for east PingDirectory..."
      wait-for east-pingdirectory-1.east-pingdirectory-cluster.east.svc.cluster.local:1636 -t 600 -- echo "east PingDirectory running"

pingdirectory:
  container:
    replicaCount: 2
  enabled: true
  envs:
    SERVER_PROFILE_URL: https://github.com/pingidentity/pingidentity-server-profiles.git
    SERVER_PROFILE_PATH: baseline/pingdirectory
    LOAD_BALANCING_ALGORITHM_NAMES: dc_example_dc_com-fewest-operations;dc_example_dc_com-failover
    K8S_CLUSTERS: west east
    K8S_CLUSTER: west
    K8S_SEED_CLUSTER: west
    K8S_NUM_REPLICAS: "2"
    K8S_POD_HOSTNAME_PREFIX: "west-pingdirectory-"
    K8S_POD_HOSTNAME_SUFFIX: ".west-pingdirectory-cluster.west.svc.cluster.local"
    K8S_SEED_HOSTNAME_SUFFIX: ".west-pingdirectory-cluster.west.svc.cluster.local"
    K8S_INCREMENT_PORTS: "false"

pingdirectoryproxy:
  includeInitContainers:
  - wait-for-east-pd
  container:
    replicaCount: 1
  enabled: true
  envs:
    SERVER_PROFILE_URL: https://github.com/pingidentity/pingidentity-server-profiles.git
    SERVER_PROFILE_PATH: pingdirectoryproxy-automatic-server-discovery/pingdirectoryproxy
    K8S_CLUSTERS: west east
    K8S_CLUSTER: west
    K8S_SEED_CLUSTER: west
    K8S_NUM_REPLICAS: "1"
    K8S_POD_HOSTNAME_PREFIX: "west-pingdirectoryproxy-"
    K8S_POD_HOSTNAME_SUFFIX: ".west-pingdirectoryproxy-cluster.west.svc.cluster.local"
    K8S_SEED_HOSTNAME_SUFFIX: ".west-pingdirectoryproxy-cluster.west.svc.cluster.local"
    K8S_INCREMENT_PORTS: "false"
    JOIN_PD_TOPOLOGY: "true"
    PINGDIRECTORY_HOSTNAME: west-pingdirectory-0.west-pingdirectory-cluster.west.svc.cluster.local
    PINGDIRECTORY_LDAPS_PORT: "1636"
YAML
```

Create `./dd-east.yaml`:

```shell
cat > ./dd-east.yaml <<'YAML'
global:
  image:
    tag: "2603"

initContainers:
  wait-for-west-proxy:
    name: wait-for-west-proxy
    image: pingidentity/pingtoolkit:2603
    command:
    - sh
    - -c
    - |
      echo "Waiting for west PingDirectoryProxy..."
      wait-for west-pingdirectoryproxy-0.west-pingdirectoryproxy-cluster.west.svc.cluster.local:1636 -t 600 -- echo "west PingDirectoryProxy running"

pingdirectory:
  container:
    replicaCount: 2
  enabled: true
  envs:
    SERVER_PROFILE_URL: https://github.com/pingidentity/pingidentity-server-profiles.git
    SERVER_PROFILE_PATH: baseline/pingdirectory
    LOAD_BALANCING_ALGORITHM_NAMES: dc_example_dc_com-fewest-operations;dc_example_dc_com-failover
    K8S_CLUSTERS: west east
    K8S_CLUSTER: east
    K8S_SEED_CLUSTER: west
    K8S_NUM_REPLICAS: "2"
    K8S_POD_HOSTNAME_PREFIX: "east-pingdirectory-"
    K8S_SEED_HOSTNAME_PREFIX: "west-pingdirectory-"
    K8S_POD_HOSTNAME_SUFFIX: ".east-pingdirectory-cluster.east.svc.cluster.local"
    K8S_SEED_HOSTNAME_SUFFIX: ".west-pingdirectory-cluster.west.svc.cluster.local"
    K8S_INCREMENT_PORTS: "false"

pingdirectoryproxy:
  includeInitContainers:
  - wait-for-west-proxy
  container:
    replicaCount: 1
  enabled: true
  envs:
    SERVER_PROFILE_URL: https://github.com/pingidentity/pingidentity-server-profiles.git
    SERVER_PROFILE_PATH: pingdirectoryproxy-automatic-server-discovery/pingdirectoryproxy
    K8S_CLUSTERS: west east
    K8S_CLUSTER: east
    K8S_SEED_CLUSTER: west
    K8S_NUM_REPLICAS: "1"
    K8S_POD_HOSTNAME_PREFIX: "east-pingdirectoryproxy-"
    K8S_SEED_HOSTNAME_PREFIX: "west-pingdirectoryproxy-"
    K8S_POD_HOSTNAME_SUFFIX: ".east-pingdirectoryproxy-cluster.east.svc.cluster.local"
    K8S_SEED_HOSTNAME_SUFFIX: ".west-pingdirectoryproxy-cluster.west.svc.cluster.local"
    K8S_INCREMENT_PORTS: "false"
    JOIN_PD_TOPOLOGY: "true"
    PINGDIRECTORY_HOSTNAME: west-pingdirectory-0.west-pingdirectory-cluster.west.svc.cluster.local
    PINGDIRECTORY_LDAPS_PORT: "1636"
YAML
```

### Deploy Docker Desktop Demo

Do not use `--wait` on the west install. The west proxy intentionally waits for east PingDirectory through an init container.

```shell
helm upgrade --install west pingidentity/ping-devops \
  -n west \
  -f ./dd-west.yaml
```

Wait for west PingDirectory pods to start:

```shell
kubectl -n west rollout status statefulset/west-pingdirectory --timeout=15m
```

Install east:

```shell
helm upgrade --install east pingidentity/ping-devops \
  -n east \
  -f ./dd-east.yaml
```

Wait for all workloads:

```shell
kubectl -n west rollout status statefulset/west-pingdirectoryproxy --timeout=15m
kubectl -n east rollout status statefulset/east-pingdirectory --timeout=15m
kubectl -n east rollout status statefulset/east-pingdirectoryproxy --timeout=15m
```

### Confirm DNS and TCP Reachability

```shell
kubectl -n west run dns-test --rm -i --restart=Never --image=pingidentity/pingtoolkit:2603 -- \
  nslookup east-pingdirectory-0.east-pingdirectory-cluster.east.svc.cluster.local

kubectl -n east run dns-test --rm -i --restart=Never --image=pingidentity/pingtoolkit:2603 -- \
  nslookup west-pingdirectory-0.west-pingdirectory-cluster.west.svc.cluster.local

kubectl -n west run net-test --rm -i --restart=Never --image=pingidentity/pingtoolkit:2603 -- \
  wait-for east-pingdirectory-0.east-pingdirectory-cluster.east.svc.cluster.local:1636 -t 30 -- echo ok

kubectl -n east run net-test --rm -i --restart=Never --image=pingidentity/pingtoolkit:2603 -- \
  wait-for west-pingdirectory-0.west-pingdirectory-cluster.west.svc.cluster.local:1636 -t 30 -- echo ok
```

### Confirm Default Hook Behavior

West:

```shell
kubectl -n west exec west-pingdirectoryproxy-0 -- dsconfig list-locations
kubectl -n west exec west-pingdirectoryproxy-0 -- dsconfig get-location-prop --location-name west
kubectl -n west exec west-pingdirectoryproxy-0 -- dsconfig list-server-instances --property load-balancing-algorithm-name
kubectl -n west exec west-pingdirectoryproxy-0 -- ldapsearch -b cn=monitor \
  "(objectclass=ds-load-balancing-algorithm-monitor-entry)" \
  algorithm-name health-check-state local-servers-health-check-state \
  non-local-servers-health-check-state num-available-servers
```

East:

```shell
kubectl -n east exec east-pingdirectoryproxy-0 -- dsconfig list-locations
kubectl -n east exec east-pingdirectoryproxy-0 -- dsconfig get-location-prop --location-name east
kubectl -n east exec east-pingdirectoryproxy-0 -- dsconfig list-server-instances --property load-balancing-algorithm-name
kubectl -n east exec east-pingdirectoryproxy-0 -- ldapsearch -b cn=monitor \
  "(objectclass=ds-load-balancing-algorithm-monitor-entry)" \
  algorithm-name health-check-state local-servers-health-check-state \
  non-local-servers-health-check-state num-available-servers
```

Expected:

```shell
west proxy:
  locations: west, east
  west preferred-failover-location: east

east proxy:
  locations: east, west
  east preferred-failover-location: west

both proxies:
  LBA monitor status: AVAILABLE
  num-available-servers: 4
```

### Restart Validation

```shell
kubectl -n west rollout restart statefulset/west-pingdirectoryproxy
kubectl -n west rollout status statefulset/west-pingdirectoryproxy --timeout=15m
kubectl -n west exec west-pingdirectoryproxy-0 -- dsconfig get-location-prop --location-name west
```

The proxy pod can report Ready before backend health checks converge. Wait for LBA convergence:

```shell
until kubectl -n west exec west-pingdirectoryproxy-0 -- ldapsearch -b cn=monitor \
  "(objectclass=ds-load-balancing-algorithm-monitor-entry)" \
  algorithm-name health-check-state local-servers-health-check-state \
  non-local-servers-health-check-state num-available-servers | \
  grep -q "non-local-servers-health-check-state: AVAILABLE"; do
  sleep 10
done
```

Repeat for east:

```shell
kubectl -n east rollout restart statefulset/east-pingdirectoryproxy
kubectl -n east rollout status statefulset/east-pingdirectoryproxy --timeout=15m
kubectl -n east exec east-pingdirectoryproxy-0 -- dsconfig get-location-prop --location-name east

until kubectl -n east exec east-pingdirectoryproxy-0 -- ldapsearch -b cn=monitor \
  "(objectclass=ds-load-balancing-algorithm-monitor-entry)" \
  algorithm-name health-check-state local-servers-health-check-state \
  non-local-servers-health-check-state num-available-servers | \
  grep -q "non-local-servers-health-check-state: AVAILABLE"; do
  sleep 10
done
```

Expected:

* Hook runs again.

* No duplicate location problem occurs.

* Preferred failover values remain correct.

* LBAs become available.

### Explicit Preferred Failover Variation

```shell
helm upgrade --install west pingidentity/ping-devops \
  -n west \
  -f ./dd-west.yaml \
  --set-string pingdirectoryproxy.envs.PREFERRED_FAILOVER_LOCATIONS="east"

helm upgrade --install east pingidentity/ping-devops \
  -n east \
  -f ./dd-east.yaml \
  --set-string pingdirectoryproxy.envs.PREFERRED_FAILOVER_LOCATIONS="west"

kubectl -n west rollout status statefulset/west-pingdirectoryproxy --timeout=15m
kubectl -n east rollout status statefulset/east-pingdirectoryproxy --timeout=15m

kubectl -n west exec west-pingdirectoryproxy-0 -- dsconfig get-location-prop --location-name west
kubectl -n east exec east-pingdirectoryproxy-0 -- dsconfig get-location-prop --location-name east
```

Expected:

```shell
west preferred-failover-location: east
east preferred-failover-location: west
```

### Invalid Override Includes Local Cluster

```shell
helm upgrade --install west pingidentity/ping-devops \
  -n west \
  -f ./dd-west.yaml \
  --set-string pingdirectoryproxy.envs.PREFERRED_FAILOVER_LOCATIONS="west east"
```

Expected:

* west proxy startup fails

* logs contain `PREFERRED_FAILOVER_LOCATIONS`

* logs contain `must not include the local K8S_CLUSTER`

Check:

```shell
kubectl -n west logs west-pingdirectoryproxy-0
```

Restore:

```shell
helm upgrade --install west pingidentity/ping-devops \
  -n west \
  -f ./dd-west.yaml

kubectl -n west delete pod west-pingdirectoryproxy-0
kubectl -n west rollout status statefulset/west-pingdirectoryproxy --timeout=15m
```

### Invalid Override References Unknown Cluster

```shell
helm upgrade --install west pingidentity/ping-devops \
  -n west \
  -f ./dd-west.yaml \
  --set-string pingdirectoryproxy.envs.PREFERRED_FAILOVER_LOCATIONS="east central"
```

Expected:

* west proxy startup fails

* logs contain `PREFERRED_FAILOVER_LOCATIONS`

* logs contain `must only include clusters listed in K8S_CLUSTERS`

Restore:

```shell
helm upgrade --install west pingidentity/ping-devops \
  -n west \
  -f ./dd-west.yaml

kubectl -n west delete pod west-pingdirectoryproxy-0
kubectl -n west rollout status statefulset/west-pingdirectoryproxy --timeout=15m
```

### Docker Desktop Cleanup

```shell
helm uninstall west -n west
helm uninstall east -n east

kubectl delete namespace west
kubectl delete namespace east
```

## Demo 2: Local Multi-Cluster with kind

Use this demo to validate the real cross-cluster hostname model.

This demo uses two separate `kind` clusters:

* `kind-west`

* `kind-east`

This path exercises separate Kubernetes control planes and requires:

* stable per-pod `LoadBalancer` IPs for PingDirectory

* routable `LoadBalancer` IPs for PingDirectoryProxy

* DNS records for external names

* CoreDNS forwarding in both clusters

* cross-cluster TCP reachability

### kind Prerequisites

Required:

* Docker

* If using Docker Desktop, ensure Kubernetes is disabled so as to not interfere with kind

* `kind`

* `kubectl`

* `helm`

* [Ping Identity DevOps](../how-to/devopsRegistration.html) credentials available as environment variables or in a local `.env` file

Recommended resources:

* CPUs: 8 or more

* Memory: 16 GB or more

### Create kind Clusters

```shell
kind create cluster --name west
kind create cluster --name east
```

Verify contexts:

```shell
kubectl config get-contexts | grep kind-
```

Expected contexts:

```shell
kind-west
kind-east
```

### Inspect Docker Network

Both kind clusters usually use the Docker network named `kind`.

```shell
docker network inspect kind
```

Record the subnet. Example:

```shell
172.19.0.0/16
```

Choose non-overlapping IP ranges from that subnet:

```shell
export DNSMASQ_IP=172.19.0.53
export WEST_LB_RANGE=172.19.10.200-172.19.10.230
export EAST_LB_RANGE=172.19.11.200-172.19.11.230
```

Adjust these values if the Docker `kind` network uses a different subnet.

### Install MetalLB

```shell
kubectl --context kind-west apply -f https://raw.githubusercontent.com/metallb/metallb/v0.14.5/config/manifests/metallb-native.yaml
kubectl --context kind-east apply -f https://raw.githubusercontent.com/metallb/metallb/v0.14.5/config/manifests/metallb-native.yaml

kubectl --context kind-west -n metallb-system wait --for=condition=Available deployment/controller --timeout=180s
kubectl --context kind-east -n metallb-system wait --for=condition=Available deployment/controller --timeout=180s
```

Create MetalLB pools:

```shell
cat > ./kind-west-metallb.yaml <<EOF
apiVersion: metallb.io/v1beta1
kind: IPAddressPool
metadata:
  name: pdproxy-discovery-west
  namespace: metallb-system
spec:
  addresses:
  - ${WEST_LB_RANGE}
---
apiVersion: metallb.io/v1beta1
kind: L2Advertisement
metadata:
  name: pdproxy-discovery-west
  namespace: metallb-system
spec:
  ipAddressPools:
  - pdproxy-discovery-west
EOF

cat > ./kind-east-metallb.yaml <<EOF
apiVersion: metallb.io/v1beta1
kind: IPAddressPool
metadata:
  name: pdproxy-discovery-east
  namespace: metallb-system
spec:
  addresses:
  - ${EAST_LB_RANGE}
---
apiVersion: metallb.io/v1beta1
kind: L2Advertisement
metadata:
  name: pdproxy-discovery-east
  namespace: metallb-system
spec:
  ipAddressPools:
  - pdproxy-discovery-east
EOF

kubectl --context kind-west apply -f ./kind-west-metallb.yaml
kubectl --context kind-east apply -f ./kind-east-metallb.yaml
```

### Run dnsmasq

Create a small dnsmasq image:

```shell
mkdir -p dnsmasq

cat > ./dnsmasq/Dockerfile <<'EOF'
FROM alpine:3.23
RUN apk add --no-cache dnsmasq
ENTRYPOINT ["dnsmasq"]
EOF

docker build -t pdproxy-discovery-dnsmasq:2.91 ./dnsmasq
```

Create DNS files:

```shell
cat > ./dnsmasq/dnsmasq.conf <<'EOF'
no-daemon
log-queries
log-facility=-
listen-address=0.0.0.0
bind-interfaces
addn-hosts=/etc/dnsmasq.d/hosts.lab
EOF

cat > ./dnsmasq/hosts.lab <<'EOF'
# Filled in after LoadBalancer services receive IPs.
EOF
```

Start dnsmasq:

```shell
docker rm -f pdproxy-discovery-dnsmasq 2>/dev/null || true

docker run -d --name pdproxy-discovery-dnsmasq \
  --network kind \
  --ip "${DNSMASQ_IP}" \
  -v "$PWD/./dnsmasq/dnsmasq.conf:/etc/dnsmasq.conf:ro" \
  -v "$PWD/./dnsmasq/hosts.lab:/etc/dnsmasq.d/hosts.lab:ro" \
  pdproxy-discovery-dnsmasq:2.91
```

Verify:

```shell
docker logs pdproxy-discovery-dnsmasq
```

### Configure CoreDNS Forwarding

Patch both clusters so `west.example.com` and `east.example.com` forward to dnsmasq.

```shell
kubectl --context kind-west -n kube-system get configmap coredns -o yaml > ./kind-west-coredns.before.yaml
kubectl --context kind-east -n kube-system get configmap coredns -o yaml > ./kind-east-coredns.before.yaml
```

Patch CoreDNS in west:

If `DNSMASQ_IP` differs from the example, replace `172.19.0.53` in both patch payloads.

```shell
kubectl --context kind-west -n kube-system patch configmap coredns --type merge -p '{
  "data": {
    "Corefile": "west.example.com:53 {\n    forward . 172.19.0.53\n}\n\neast.example.com:53 {\n    forward . 172.19.0.53\n}\n\n.:53 {\n    errors\n    health {\n       lameduck 5s\n    }\n    ready\n    kubernetes cluster.local in-addr.arpa ip6.arpa {\n       pods insecure\n       fallthrough in-addr.arpa ip6.arpa\n       ttl 30\n    }\n    prometheus :9153\n    forward . /etc/resolv.conf {\n       max_concurrent 1000\n    }\n    cache 30 {\n       disable success cluster.local\n       disable denial cluster.local\n    }\n    loop\n    reload\n    loadbalance\n}\n"
  }
}'
```

Patch CoreDNS in east with the same forwarding blocks:

```shell
kubectl --context kind-east -n kube-system patch configmap coredns --type merge -p '{
  "data": {
    "Corefile": "west.example.com:53 {\n    forward . 172.19.0.53\n}\n\neast.example.com:53 {\n    forward . 172.19.0.53\n}\n\n.:53 {\n    errors\n    health {\n       lameduck 5s\n    }\n    ready\n    kubernetes cluster.local in-addr.arpa ip6.arpa {\n       pods insecure\n       fallthrough in-addr.arpa ip6.arpa\n       ttl 30\n    }\n    prometheus :9153\n    forward . /etc/resolv.conf {\n       max_concurrent 1000\n    }\n    cache 30 {\n       disable success cluster.local\n       disable denial cluster.local\n    }\n    loop\n    reload\n    loadbalance\n}\n"
  }
}'
```

Restart CoreDNS:

```shell
kubectl --context kind-west -n kube-system rollout restart deployment coredns
kubectl --context kind-east -n kube-system rollout restart deployment coredns
kubectl --context kind-west -n kube-system rollout status deployment coredns --timeout=120s
kubectl --context kind-east -n kube-system rollout status deployment coredns --timeout=120s
```

### Create Namespaces and Secrets

```shell
kubectl --context kind-west create namespace west
kubectl --context kind-east create namespace east
```

Using an existing `.env` file:

```shell
kubectl --context kind-west -n west create secret generic devops-secret \
  --from-env-file=.env \
  --dry-run=client -o yaml | kubectl --context kind-west -n west apply -f -

kubectl --context kind-east -n east create secret generic devops-secret \
  --from-env-file=.env \
  --dry-run=client -o yaml | kubectl --context kind-east -n east apply -f -
```

Using existing environment variables:

```shell
kubectl --context kind-west -n west create secret generic devops-secret \
  --from-literal=PING_IDENTITY_DEVOPS_USER="$PING_IDENTITY_DEVOPS_USER" \
  --from-literal=PING_IDENTITY_DEVOPS_KEY="$PING_IDENTITY_DEVOPS_KEY" \
  --from-literal=PING_IDENTITY_ACCEPT_EULA="YES" \
  --type=Opaque \
  --dry-run=client -o yaml | kubectl --context kind-west -n west apply -f -

kubectl --context kind-east -n east create secret generic devops-secret \
  --from-literal=PING_IDENTITY_DEVOPS_USER="$PING_IDENTITY_DEVOPS_USER" \
  --from-literal=PING_IDENTITY_DEVOPS_KEY="$PING_IDENTITY_DEVOPS_KEY" \
  --from-literal=PING_IDENTITY_ACCEPT_EULA="YES" \
  --type=Opaque \
  --dry-run=client -o yaml | kubectl --context kind-east -n east apply -f -
```

### Create kind Values

Create `./kind-west.yaml`:

```shell
cat > ./kind-west.yaml <<'YAML'
global:
  image:
    tag: "2603"

initContainers:
  wait-for-east-pd:
    name: wait-for-east-pd
    image: pingidentity/pingtoolkit:2603
    command:
    - sh
    - -c
    - |
      echo "Waiting for east PingDirectory..."
      wait-for east-pingdirectory-1.east.example.com:1636 -t 900 -- echo "east PingDirectory running"

pingdirectory:
  container:
    replicaCount: 2
  enabled: true
  envs:
    SERVER_PROFILE_URL: https://github.com/pingidentity/pingidentity-server-profiles.git
    SERVER_PROFILE_PATH: baseline/pingdirectory
    LOAD_BALANCING_ALGORITHM_NAMES: dc_example_dc_com-fewest-operations;dc_example_dc_com-failover
    MAKELDIF_USERS: "2000"
    K8S_CLUSTERS: west east
    K8S_CLUSTER: west
    K8S_SEED_CLUSTER: west
    K8S_NUM_REPLICAS: "2"
    K8S_POD_HOSTNAME_PREFIX: "west-pingdirectory-"
    K8S_POD_HOSTNAME_SUFFIX: ".west.example.com"
    K8S_SEED_HOSTNAME_SUFFIX: ".west.example.com"
    K8S_INCREMENT_PORTS: "false"
    SKIP_WAIT_FOR_DNS: "true"
  services:
    loadBalancerServicePerPod: true
    loadBalancerExternalDNSHostnameSuffix: .west.example.com

pingdirectoryproxy:
  includeInitContainers:
  - wait-for-east-pd
  container:
    replicaCount: 1
  enabled: true
  envs:
    SERVER_PROFILE_URL: https://github.com/pingidentity/pingidentity-server-profiles.git
    SERVER_PROFILE_PATH: pingdirectoryproxy-automatic-server-discovery/pingdirectoryproxy
    K8S_CLUSTERS: west east
    K8S_CLUSTER: west
    K8S_SEED_CLUSTER: west
    K8S_NUM_REPLICAS: "1"
    K8S_POD_HOSTNAME_PREFIX: "west-pingdirectoryproxy-"
    K8S_POD_HOSTNAME_SUFFIX: ".west.example.com"
    K8S_SEED_HOSTNAME_SUFFIX: ".west.example.com"
    K8S_INCREMENT_PORTS: "false"
    SKIP_WAIT_FOR_DNS: "true"
    JOIN_PD_TOPOLOGY: "true"
    PINGDIRECTORY_HOSTNAME: west-pingdirectory-0.west.example.com
    PINGDIRECTORY_LDAPS_PORT: "1636"
  services:
    useLoadBalancerForDataService: true
    dataExternalDNSHostname: west-pingdirectoryproxy-0.west.example.com
    ldaps:
      servicePort: 1636
      containerPort: 1636
      clusterService: true
      dataService: true
YAML
```

Create `./kind-east.yaml`:

```shell
cat > ./kind-east.yaml <<'YAML'
global:
  image:
    tag: "2603"

initContainers:
  wait-for-west-proxy:
    name: wait-for-west-proxy
    image: pingidentity/pingtoolkit:2603
    command:
    - sh
    - -c
    - |
      echo "Waiting for west PingDirectoryProxy..."
      wait-for west-pingdirectoryproxy-0.west.example.com:1636 -t 900 -- echo "west PingDirectoryProxy running"

pingdirectory:
  container:
    replicaCount: 2
  enabled: true
  envs:
    SERVER_PROFILE_URL: https://github.com/pingidentity/pingidentity-server-profiles.git
    SERVER_PROFILE_PATH: baseline/pingdirectory
    LOAD_BALANCING_ALGORITHM_NAMES: dc_example_dc_com-fewest-operations;dc_example_dc_com-failover
    MAKELDIF_USERS: "2000"
    K8S_CLUSTERS: west east
    K8S_CLUSTER: east
    K8S_SEED_CLUSTER: west
    K8S_NUM_REPLICAS: "2"
    K8S_POD_HOSTNAME_PREFIX: "east-pingdirectory-"
    K8S_SEED_HOSTNAME_PREFIX: "west-pingdirectory-"
    K8S_POD_HOSTNAME_SUFFIX: ".east.example.com"
    K8S_SEED_HOSTNAME_SUFFIX: ".west.example.com"
    K8S_INCREMENT_PORTS: "false"
    SKIP_WAIT_FOR_DNS: "true"
  services:
    loadBalancerServicePerPod: true
    loadBalancerExternalDNSHostnameSuffix: .east.example.com

pingdirectoryproxy:
  includeInitContainers:
  - wait-for-west-proxy
  container:
    replicaCount: 1
  enabled: true
  envs:
    SERVER_PROFILE_URL: https://github.com/pingidentity/pingidentity-server-profiles.git
    SERVER_PROFILE_PATH: pingdirectoryproxy-automatic-server-discovery/pingdirectoryproxy
    K8S_CLUSTERS: west east
    K8S_CLUSTER: east
    K8S_SEED_CLUSTER: west
    K8S_NUM_REPLICAS: "1"
    K8S_POD_HOSTNAME_PREFIX: "east-pingdirectoryproxy-"
    K8S_SEED_HOSTNAME_PREFIX: "west-pingdirectoryproxy-"
    K8S_POD_HOSTNAME_SUFFIX: ".east.example.com"
    K8S_SEED_HOSTNAME_SUFFIX: ".west.example.com"
    K8S_INCREMENT_PORTS: "false"
    SKIP_WAIT_FOR_DNS: "true"
    JOIN_PD_TOPOLOGY: "true"
    PINGDIRECTORY_HOSTNAME: west-pingdirectory-0.west.example.com
    PINGDIRECTORY_LDAPS_PORT: "1636"
  services:
    useLoadBalancerForDataService: true
    dataExternalDNSHostname: east-pingdirectoryproxy-0.east.example.com
    ldaps:
      servicePort: 1636
      containerPort: 1636
      clusterService: true
      dataService: true
YAML
```

### Deploy West

Do not use `--wait`. The west proxy waits for east PingDirectory through an init container.

```shell
helm upgrade --install west pingidentity/ping-devops \
  --kube-context kind-west \
  -n west \
  -f ./kind-west.yaml
```

Patch the west proxy LoadBalancer service so the advertised proxy hostname can route to the starting proxy before the proxy pod is marked Ready:

```shell
kubectl --context kind-west -n west patch service west-pingdirectoryproxy \
  --type merge \
  -p '{"spec":{"publishNotReadyAddresses":true}}'
```

This patch is required when the chart does not expose `publishNotReadyAddresses` for the generated service. The proxy topology join reaches the proxy through its advertised external LoadBalancer hostname before readiness succeeds. This patch is needed for this local example to work.

Wait for west PingDirectory pods to start:

```shell
kubectl --context kind-west -n west rollout status statefulset/west-pingdirectory --timeout=15m
kubectl --context kind-west -n west get svc
```

Record:

* `west-pingdirectory-0` external IP

* `west-pingdirectory-1` external IP

* `west-pingdirectoryproxy` external IP

Update `./dnsmasq/hosts.lab` with west records.

Example:

```shell
172.19.10.202 west-pingdirectory-0.west.example.com
172.19.10.201 west-pingdirectory-1.west.example.com
172.19.10.200 west-pingdirectoryproxy-0.west.example.com
```

Restart dnsmasq:

```shell
docker restart pdproxy-discovery-dnsmasq
```

Verify west DNS from both clusters:

```shell
kubectl --context kind-west run dns-west-from-west --restart=Never --image=pingidentity/pingtoolkit:2603 -- \
  nslookup west-pingdirectory-0.west.example.com
kubectl --context kind-west wait --for=jsonpath='{.status.phase}'=Succeeded pod/dns-west-from-west --timeout=120s
kubectl --context kind-west logs dns-west-from-west
kubectl --context kind-west delete pod dns-west-from-west

kubectl --context kind-east run dns-west-from-east --restart=Never --image=pingidentity/pingtoolkit:2603 -- \
  nslookup west-pingdirectory-0.west.example.com
kubectl --context kind-east wait --for=jsonpath='{.status.phase}'=Succeeded pod/dns-west-from-east --timeout=120s
kubectl --context kind-east logs dns-west-from-east
kubectl --context kind-east delete pod dns-west-from-east
```

### Deploy East

```shell
helm upgrade --install east pingidentity/ping-devops \
  --kube-context kind-east \
  -n east \
  -f ./kind-east.yaml
```

Patch the east proxy LoadBalancer service for the same pre-readiness routing requirement:

```shell
kubectl --context kind-east -n east patch service east-pingdirectoryproxy \
  --type merge \
  -p '{"spec":{"publishNotReadyAddresses":true}}'
```

Get east service IPs:

```shell
kubectl --context kind-east -n east get svc
```

Append east records to `./dnsmasq/hosts.lab`.

Example:

```shell
172.19.11.201 east-pingdirectory-0.east.example.com
172.19.11.202 east-pingdirectory-1.east.example.com
172.19.11.200 east-pingdirectoryproxy-0.east.example.com
```

Restart dnsmasq:

```shell
docker restart pdproxy-discovery-dnsmasq
```

Verify east DNS from both clusters:

```shell
kubectl --context kind-west run dns-east-from-west --restart=Never --image=pingidentity/pingtoolkit:2603 -- \
  nslookup east-pingdirectory-0.east.example.com
kubectl --context kind-west wait --for=jsonpath='{.status.phase}'=Succeeded pod/dns-east-from-west --timeout=120s
kubectl --context kind-west logs dns-east-from-west
kubectl --context kind-west delete pod dns-east-from-west

kubectl --context kind-east run dns-east-from-east --restart=Never --image=pingidentity/pingtoolkit:2603 -- \
  nslookup east-pingdirectory-0.east.example.com
kubectl --context kind-east wait --for=jsonpath='{.status.phase}'=Succeeded pod/dns-east-from-east --timeout=120s
kubectl --context kind-east logs dns-east-from-east
kubectl --context kind-east delete pod dns-east-from-east
```

### Confirm Cross-Cluster TCP Reachability

```shell
kubectl --context kind-west run net-west-to-east-pd --restart=Never --image=pingidentity/pingtoolkit:2603 -- \
  wait-for east-pingdirectory-0.east.example.com:1636 -t 60 -- echo ok
kubectl --context kind-west wait --for=jsonpath='{.status.phase}'=Succeeded pod/net-west-to-east-pd --timeout=120s
kubectl --context kind-west logs net-west-to-east-pd
kubectl --context kind-west delete pod net-west-to-east-pd

kubectl --context kind-east run net-east-to-west-pd --restart=Never --image=pingidentity/pingtoolkit:2603 -- \
  wait-for west-pingdirectory-0.west.example.com:1636 -t 60 -- echo ok
kubectl --context kind-east wait --for=jsonpath='{.status.phase}'=Succeeded pod/net-east-to-west-pd --timeout=120s
kubectl --context kind-east logs net-east-to-west-pd
kubectl --context kind-east delete pod net-east-to-west-pd

kubectl --context kind-east run proxy-east-to-west --restart=Never --image=pingidentity/pingtoolkit:2603 -- \
  wait-for west-pingdirectoryproxy-0.west.example.com:1636 -t 60 -- echo ok
kubectl --context kind-east wait --for=jsonpath='{.status.phase}'=Succeeded pod/proxy-east-to-west --timeout=120s
kubectl --context kind-east logs proxy-east-to-west
kubectl --context kind-east delete pod proxy-east-to-west
```

### Wait for Workloads

```shell
kubectl --context kind-west -n west rollout status statefulset/west-pingdirectory --timeout=15m
kubectl --context kind-east -n east rollout status statefulset/east-pingdirectory --timeout=15m
kubectl --context kind-west -n west rollout status statefulset/west-pingdirectoryproxy --timeout=15m
kubectl --context kind-east -n east rollout status statefulset/east-pingdirectoryproxy --timeout=15m
```

### Confirm kind Default Hook Behavior

West:

```shell
kubectl --context kind-west -n west exec west-pingdirectoryproxy-0 -- dsconfig list-locations
kubectl --context kind-west -n west exec west-pingdirectoryproxy-0 -- dsconfig get-location-prop --location-name west
kubectl --context kind-west -n west exec west-pingdirectoryproxy-0 -- dsconfig list-server-instances --property load-balancing-algorithm-name
kubectl --context kind-west -n west exec west-pingdirectoryproxy-0 -- ldapsearch -b cn=monitor \
  "(objectclass=ds-load-balancing-algorithm-monitor-entry)" \
  algorithm-name health-check-state local-servers-health-check-state \
  non-local-servers-health-check-state num-available-servers
```

East:

```shell
kubectl --context kind-east -n east exec east-pingdirectoryproxy-0 -- dsconfig list-locations
kubectl --context kind-east -n east exec east-pingdirectoryproxy-0 -- dsconfig get-location-prop --location-name east
kubectl --context kind-east -n east exec east-pingdirectoryproxy-0 -- dsconfig list-server-instances --property load-balancing-algorithm-name
kubectl --context kind-east -n east exec east-pingdirectoryproxy-0 -- ldapsearch -b cn=monitor \
  "(objectclass=ds-load-balancing-algorithm-monitor-entry)" \
  algorithm-name health-check-state local-servers-health-check-state \
  non-local-servers-health-check-state num-available-servers
```

Expected:

```shell
west proxy:
  locations: west, east
  west preferred-failover-location: east

east proxy:
  locations: east, west
  east preferred-failover-location: west

both proxies:
  LBA monitor status: AVAILABLE
  num-available-servers: 4
```

### kind Explicit Preferred Failover Variation

```shell
helm upgrade --install west pingidentity/ping-devops \
  --kube-context kind-west \
  -n west \
  -f ./kind-west.yaml \
  --set-string pingdirectoryproxy.envs.PREFERRED_FAILOVER_LOCATIONS="east"

helm upgrade --install east pingidentity/ping-devops \
  --kube-context kind-east \
  -n east \
  -f ./kind-east.yaml \
  --set-string pingdirectoryproxy.envs.PREFERRED_FAILOVER_LOCATIONS="west"

kubectl --context kind-west -n west patch service west-pingdirectoryproxy \
  --type merge \
  -p '{"spec":{"publishNotReadyAddresses":true}}'

kubectl --context kind-east -n east patch service east-pingdirectoryproxy \
  --type merge \
  -p '{"spec":{"publishNotReadyAddresses":true}}'

kubectl --context kind-west -n west rollout status statefulset/west-pingdirectoryproxy --timeout=15m
kubectl --context kind-east -n east rollout status statefulset/east-pingdirectoryproxy --timeout=15m

kubectl --context kind-west -n west exec west-pingdirectoryproxy-0 -- dsconfig get-location-prop --location-name west
kubectl --context kind-east -n east exec east-pingdirectoryproxy-0 -- dsconfig get-location-prop --location-name east
```

Expected:

```shell
west preferred-failover-location: east
east preferred-failover-location: west
```

### kind Invalid Local Override

```shell
helm upgrade --install west pingidentity/ping-devops \
  --kube-context kind-west \
  -n west \
  -f ./kind-west.yaml \
  --set-string pingdirectoryproxy.envs.PREFERRED_FAILOVER_LOCATIONS="west east"
```

Expected:

* west proxy fails during startup

* logs show local cluster is not allowed in `PREFERRED_FAILOVER_LOCATIONS`

Check:

```shell
kubectl --context kind-west -n west logs west-pingdirectoryproxy-0 -f
```

Restore:

```shell
helm upgrade --install west pingidentity/ping-devops \
  --kube-context kind-west \
  -n west \
  -f ./kind-west.yaml

kubectl --context kind-west -n west patch service west-pingdirectoryproxy \
  --type merge \
  -p '{"spec":{"publishNotReadyAddresses":true}}'

kubectl --context kind-west -n west delete pod west-pingdirectoryproxy-0
kubectl --context kind-west -n west rollout status statefulset/west-pingdirectoryproxy --timeout=15m
```

### kind Invalid Unknown Override

```shell
helm upgrade --install west pingidentity/ping-devops \
  --kube-context kind-west \
  -n west \
  -f ./kind-west.yaml \
  --set-string pingdirectoryproxy.envs.PREFERRED_FAILOVER_LOCATIONS="east central"
```

Expected:

* west proxy fails during startup

* logs show every preferred failover location must be listed in `K8S_CLUSTERS`

Restore:

```shell
helm upgrade --install west pingidentity/ping-devops \
  --kube-context kind-west \
  -n west \
  -f ./kind-west.yaml

kubectl --context kind-west -n west patch service west-pingdirectoryproxy \
  --type merge \
  -p '{"spec":{"publishNotReadyAddresses":true}}'

kubectl --context kind-west -n west delete pod west-pingdirectoryproxy-0
kubectl --context kind-west -n west rollout status statefulset/west-pingdirectoryproxy --timeout=15m
```

### kind Restart Validation

```shell
kubectl --context kind-west -n west rollout restart statefulset/west-pingdirectoryproxy
kubectl --context kind-west -n west rollout status statefulset/west-pingdirectoryproxy --timeout=15m
kubectl --context kind-west -n west exec west-pingdirectoryproxy-0 -- dsconfig get-location-prop --location-name west

until kubectl --context kind-west -n west exec west-pingdirectoryproxy-0 -- ldapsearch -b cn=monitor \
  "(objectclass=ds-load-balancing-algorithm-monitor-entry)" \
  algorithm-name health-check-state local-servers-health-check-state \
  non-local-servers-health-check-state num-available-servers | \
  grep -q "non-local-servers-health-check-state: AVAILABLE"; do
  sleep 10
done
```

Expected:

* hook re-runs

* preferred failover remains correct

* LBAs become available

### kind Cleanup

```shell
helm --kube-context kind-west uninstall west -n west
helm --kube-context kind-east uninstall east -n east

kind delete cluster --name west
kind delete cluster --name east

docker rm -f pdproxy-discovery-dnsmasq
```

## minikube Variant

This variant uses two Docker-driver minikube profiles:

* `west`

* `east`

### minikube Prerequisites

Required:

* Docker Desktop with Kubernetes disabled

* `kubectl`

* `helm`

* `minikube`

* [Ping Identity DevOps](../how-to/devopsRegistration.html) credentials available as environment variables or in a local `.env` file

The profile subnets vary by machine. Substitute the ranges from `docker network inspect`.

### Create Profiles

```shell
minikube start --profile west --driver=docker --cpus=4 --memory=8192
minikube start --profile east --driver=docker --cpus=4 --memory=8192
```

Verify contexts:

```shell
kubectl config get-contexts | grep -E 'west|east'
```

### LoadBalancer Support

Enable MetalLB:

```shell
minikube -p west addons enable metallb
minikube -p east addons enable metallb
```

This step requires Docker API access because minikube inspects and updates the profile containers.

Find Docker network subnets:

```shell
docker network inspect west --format '{{json .IPAM.Config}}'
docker network inspect east --format '{{json .IPAM.Config}}'
```

Example subnets:

```shell
west: 192.168.49.0/24
east: 192.168.58.0/24
```

Patch deterministic MetalLB ranges. Adjust IPs for the actual subnets:

```shell
kubectl --context west -n metallb-system patch configmap config --type merge \
  -p '{"data":{"config":"address-pools:\n- name: west\n  protocol: layer2\n  addresses:\n  - 192.168.49.200-192.168.49.209\n"}}'

kubectl --context east -n metallb-system patch configmap config --type merge \
  -p '{"data":{"config":"address-pools:\n- name: east\n  protocol: layer2\n  addresses:\n  - 192.168.58.200-192.168.58.209\n"}}'
```

Attach each minikube node container to the other profile network:

```shell
docker network connect east west || true
docker network connect west east || true
```

### minikube dnsmasq and CoreDNS

Create DNS files:

```shell
mkdir -p ./minikube-dnsmasq

cat > ./minikube-dnsmasq/dnsmasq.conf <<'EOF'
no-daemon
log-queries
log-facility=-
listen-address=0.0.0.0
bind-interfaces
addn-hosts=/etc/dnsmasq.d/hosts.lab
EOF

cat > ./minikube-dnsmasq/hosts.lab <<'EOF'
# Filled in after minikube LoadBalancer services receive IPs.
EOF
```

Build the dnsmasq image if it is not already present:

```shell
docker build -t pdproxy-discovery-dnsmasq:2.91 ./dnsmasq
```

Run dnsmasq on both profile networks. Adjust resolver IPs for the actual subnets:

```shell
docker rm -f pdproxy-discovery-minikube-dnsmasq 2>/dev/null || true

docker run -d --name pdproxy-discovery-minikube-dnsmasq \
  --network west \
  --ip 192.168.49.250 \
  -v "$PWD/./minikube-dnsmasq/dnsmasq.conf:/etc/dnsmasq.conf:ro" \
  -v "$PWD/./minikube-dnsmasq/hosts.lab:/etc/dnsmasq.d/hosts.lab:ro" \
  pdproxy-discovery-dnsmasq:2.91 \
  -C /etc/dnsmasq.conf

docker network connect --ip 192.168.58.250 east pdproxy-discovery-minikube-dnsmasq
```

Patch CoreDNS in each profile. Forward to the dnsmasq IP on that profile's local Docker network.

If your profile subnets differ from the examples, replace `192.168.49.250` and `192.168.58.250` in the patch payloads.

Back up the existing CoreDNS ConfigMaps:

```shell
kubectl --context west -n kube-system get configmap coredns -o yaml > ./minikube-west-coredns.before.yaml
kubectl --context east -n kube-system get configmap coredns -o yaml > ./minikube-east-coredns.before.yaml
```

Patch the west profile, using the west dnsmasq IP:

```shell
kubectl --context west -n kube-system patch configmap coredns --type merge -p '{
  "data": {
    "Corefile": "west.example.com:53 {\n    forward . 192.168.49.250\n}\n\neast.example.com:53 {\n    forward . 192.168.49.250\n}\n\n.:53 {\n    log\n    errors\n    health {\n       lameduck 5s\n    }\n    ready\n    kubernetes cluster.local in-addr.arpa ip6.arpa {\n       pods insecure\n       fallthrough in-addr.arpa ip6.arpa\n       ttl 30\n    }\n    prometheus :9153\n    hosts {\n       192.168.65.254 host.minikube.internal\n       fallthrough\n    }\n    forward . /etc/resolv.conf {\n       max_concurrent 1000\n    }\n    cache 30 {\n       disable success cluster.local\n       disable denial cluster.local\n    }\n    loop\n    reload\n    loadbalance\n}\n"
  }
}'
```

Patch the east profile, using the east dnsmasq IP:

```shell
kubectl --context east -n kube-system patch configmap coredns --type merge -p '{
  "data": {
    "Corefile": "west.example.com:53 {\n    forward . 192.168.58.250\n}\n\neast.example.com:53 {\n    forward . 192.168.58.250\n}\n\n.:53 {\n    log\n    errors\n    health {\n       lameduck 5s\n    }\n    ready\n    kubernetes cluster.local in-addr.arpa ip6.arpa {\n       pods insecure\n       fallthrough in-addr.arpa ip6.arpa\n       ttl 30\n    }\n    prometheus :9153\n    hosts {\n       192.168.65.254 host.minikube.internal\n       fallthrough\n    }\n    forward . /etc/resolv.conf {\n       max_concurrent 1000\n    }\n    cache 30 {\n       disable success cluster.local\n       disable denial cluster.local\n    }\n    loop\n    reload\n    loadbalance\n}\n"
  }
}'
```

Restart CoreDNS:

```shell
kubectl --context west -n kube-system rollout restart deployment coredns
kubectl --context east -n kube-system rollout restart deployment coredns
kubectl --context west -n kube-system rollout status deployment coredns --timeout=120s
kubectl --context east -n kube-system rollout status deployment coredns --timeout=120s
```

### minikube Namespaces and Secrets

```shell
kubectl --context west create namespace west
kubectl --context east create namespace east
```

Using an existing `.env` file:

```shell
kubectl --context west -n west create secret generic devops-secret \
  --from-env-file=.env \
  --dry-run=client -o yaml | kubectl --context west -n west apply -f -

kubectl --context east -n east create secret generic devops-secret \
  --from-env-file=.env \
  --dry-run=client -o yaml | kubectl --context east -n east apply -f -
```

Using existing environment variables:

```shell
kubectl --context west -n west create secret generic devops-secret \
  --from-literal=PING_IDENTITY_DEVOPS_USER="$PING_IDENTITY_DEVOPS_USER" \
  --from-literal=PING_IDENTITY_DEVOPS_KEY="$PING_IDENTITY_DEVOPS_KEY" \
  --from-literal=PING_IDENTITY_ACCEPT_EULA="YES" \
  --type=Opaque \
  --dry-run=client -o yaml | kubectl --context west -n west apply -f -

kubectl --context east -n east create secret generic devops-secret \
  --from-literal=PING_IDENTITY_DEVOPS_USER="$PING_IDENTITY_DEVOPS_USER" \
  --from-literal=PING_IDENTITY_DEVOPS_KEY="$PING_IDENTITY_DEVOPS_KEY" \
  --from-literal=PING_IDENTITY_ACCEPT_EULA="YES" \
  --type=Opaque \
  --dry-run=client -o yaml | kubectl --context east -n east apply -f -
```

### minikube Deploy West

Use the `kind` values files created earlier. They use the same `west.example.com` and `east.example.com` external hostname model.

```shell
helm upgrade --install west pingidentity/ping-devops \
  --kube-context west \
  -n west \
  -f ./kind-west.yaml

kubectl --context west -n west patch service west-pingdirectoryproxy \
  --type merge \
  -p '{"spec":{"publishNotReadyAddresses":true}}'

kubectl --context west -n west rollout status statefulset/west-pingdirectory --timeout=15m
kubectl --context west -n west get svc
```

Add west records to `./minikube-dnsmasq/hosts.lab` using actual LoadBalancer IPs.

Example:

```shell
192.168.49.201 west-pingdirectory-0.west.example.com
192.168.49.202 west-pingdirectory-1.west.example.com
192.168.49.200 west-pingdirectoryproxy-0.west.example.com
```

Restart dnsmasq and verify west DNS from both profiles:

```shell
docker restart pdproxy-discovery-minikube-dnsmasq

kubectl --context west run dns-test --rm -i --restart=Never --image=pingidentity/pingtoolkit:2603 -- \
  nslookup west-pingdirectory-0.west.example.com

kubectl --context east run dns-test --rm -i --restart=Never --image=pingidentity/pingtoolkit:2603 -- \
  nslookup west-pingdirectory-0.west.example.com
```

### minikube Deploy East

```shell
helm upgrade --install east pingidentity/ping-devops \
  --kube-context east \
  -n east \
  -f ./kind-east.yaml

kubectl --context east -n east patch service east-pingdirectoryproxy \
  --type merge \
  -p '{"spec":{"publishNotReadyAddresses":true}}'

kubectl --context east -n east get svc
```

Add east records to `./minikube-dnsmasq/hosts.lab` using actual LoadBalancer IPs.

Example:

```shell
192.168.58.201 east-pingdirectory-0.east.example.com
192.168.58.202 east-pingdirectory-1.east.example.com
192.168.58.200 east-pingdirectoryproxy-0.east.example.com
```

Restart dnsmasq and verify east DNS from both profiles:

```shell
docker restart pdproxy-discovery-minikube-dnsmasq

kubectl --context west run dns-test --rm -i --restart=Never --image=pingidentity/pingtoolkit:2603 -- \
  nslookup east-pingdirectory-0.east.example.com

kubectl --context east run dns-test --rm -i --restart=Never --image=pingidentity/pingtoolkit:2603 -- \
  nslookup east-pingdirectory-0.east.example.com
```

Wait for all workloads:

```shell
kubectl --context west -n west rollout status statefulset/west-pingdirectory --timeout=15m
kubectl --context east -n east rollout status statefulset/east-pingdirectory --timeout=15m
kubectl --context west -n west rollout status statefulset/west-pingdirectoryproxy --timeout=15m
kubectl --context east -n east rollout status statefulset/east-pingdirectoryproxy --timeout=15m
```

Then use the TCP verification, proxy validation, variation, and restart steps from the kind demo, replacing:

```shell
kind-west -> west
kind-east -> east
```

After restoring from an intentional invalid override, delete the failed proxy pod if it remains on the old invalid checksum:

```shell
kubectl --context west -n west delete pod west-pingdirectoryproxy-0
kubectl --context west -n west rollout status statefulset/west-pingdirectoryproxy --timeout=15m
```

### minikube Cleanup

```shell
helm --kube-context west uninstall west -n west
helm --kube-context east uninstall east -n east

minikube delete --profile west
minikube delete --profile east

docker rm -f pdproxy-discovery-minikube-dnsmasq
```

## Troubleshooting

1. Confirm `devops-secret` exists in every namespace.

2. Confirm the Helm command uses `pingidentity/ping-devops`, not a local chart path.

3. Confirm `SERVER_PROFILE_BRANCH` is not set in the values.

4. Confirm `SERVER_PROFILE_PATH` is `pingdirectoryproxy-automatic-server-discovery/pingdirectoryproxy`.

5. Confirm DNS resolves every name used by `PINGDIRECTORY_HOSTNAME`, `K8S_POD_HOSTNAME_PREFIX`, and `K8S_POD_HOSTNAME_SUFFIX`.

6. Confirm TCP port `1636` is reachable cross-region.

7. Confirm proxy logs show the location hook ran.

8. Confirm `dsconfig list-locations`.

9. Confirm `preferred-failover-location`.

10. Confirm LBA monitor availability.

Useful log checks:

```shell
kubectl -n west logs west-pingdirectoryproxy-0 | grep -E "PingDirectoryProxy multi-cluster|preferred failover|PREFERRED_FAILOVER_LOCATIONS|CONTAINER FAILURE"
kubectl -n east logs east-pingdirectoryproxy-0 | grep -E "PingDirectoryProxy multi-cluster|preferred failover|PREFERRED_FAILOVER_LOCATIONS|CONTAINER FAILURE"
```

For kind:

```shell
kubectl --context kind-west -n west logs west-pingdirectoryproxy-0 | grep -E "PingDirectoryProxy multi-cluster|preferred failover|PREFERRED_FAILOVER_LOCATIONS|CONTAINER FAILURE"
kubectl --context kind-east -n east logs east-pingdirectoryproxy-0 | grep -E "PingDirectoryProxy multi-cluster|preferred failover|PREFERRED_FAILOVER_LOCATIONS|CONTAINER FAILURE"
```

## Demo Closeout Evidence

Capture these outputs:

```shell
kubectl -n west exec west-pingdirectoryproxy-0 -- dsconfig list-locations
kubectl -n west exec west-pingdirectoryproxy-0 -- dsconfig get-location-prop --location-name west
kubectl -n west exec west-pingdirectoryproxy-0 -- dsconfig list-server-instances --property load-balancing-algorithm-name
kubectl -n west exec west-pingdirectoryproxy-0 -- ldapsearch -b cn=monitor "(objectclass=ds-load-balancing-algorithm-monitor-entry)"
kubectl -n west logs west-pingdirectoryproxy-0 | grep "PingDirectoryProxy multi-cluster location configuration completed"
```

For kind and minikube, include the appropriate `--context` values.

---

---
title: PingFederate Multi-Region Active/Passive Administrative Consoles
description: Deploy PingFederate admin consoles across two Kubernetes clusters in active/passive mode using Submariner for cross-cluster networking
component: devops
page_id: devops::deployment/deployPFAdminSubmarinerWalkthrough
canonical_url: https://developer.pingidentity.com/devops/deployment/deployPFAdminSubmarinerWalkthrough.html
llms_txt: https://developer.pingidentity.com/devops/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  devops-pf-submariner-purpose: Purpose
  devops-pf-submariner-topology: Cluster Topology Overview
  devops-pf-submariner-discovery: How Discovery Works in This Approach
  devops-pf-submariner-prerequisites: Prerequisites
  devops-pf-submariner-deploy-kind: Deploy Submariner Kind Clusters
  devops-pf-submariner-install-subctl: Install subctl
  devops-pf-submariner-create-clusters: Create kind clusters
  devops-pf-submariner-proxy-settings: Fix proxy settings on kind nodes
  devops-pf-submariner-preload-images: Pre-load Submariner images
  devops-pf-submariner-broker-join: Deploy Submariner broker and join clusters
  devops-pf-submariner-namespaces: Prepare Namespaces and Secrets
  devops-pf-submariner-deployment-files: Deployment Files
  devops-pf-submariner-scripts-yaml: scripts.yaml
  devops-pf-submariner-base-yaml: base.yaml
  devops-pf-submariner-east-yaml: east-pf.yaml
  devops-pf-submariner-kustomize: Kustomize Post-Renderer
  devops-pf-submariner-deploy: Deploy
  devops-pf-submariner-console: Accessing the Admin Console
  devops-pf-submariner-nodeport-rationale: Why NodePort instead of port-forward
  devops-pf-submariner-active-node: Determining which cluster holds the active node
  devops-pf-submariner-browser: Open the console in a browser
  devops-pf-submariner-failover: After failover
  devops-pf-submariner-validation: Validation
  devops-pf-submariner-cluster-status: Cluster Status
  devops-pf-submariner-active-endpoint: Active Service Endpoint
  devops-pf-submariner-scale-test: Scale Test
  devops-pf-submariner-cold-start: Simultaneous Cold Start Validation
  devops-pf-submariner-dns-verify: Cross-Cluster DNS Verification
  devops-pf-submariner-cleanup: Cleanup
---

# PingFederate Multi-Region Active/Passive Administrative Consoles

## Purpose

This walkthrough demonstrates the deployment of multiple PingFederate administrative consoles in an active/passive multi-cluster configuration. Cross-cluster networking for this demonstration is handled by [Submariner](https://multicluster.sigs.k8s.io/implementations/mcs-implementations/). Submariner exports services from one cluster into another via the `svc.clusterset.local` DNS namespace. With this communication in place, all PingFederate administrative pods use standard JGroups `DNS_PING` with a single `DNS_QUERY_LOCATION` pointing at the clusterset headless service.

|   |                                                                                                                            |
| - | -------------------------------------------------------------------------------------------------------------------------- |
|   | The configuration shown here is a starting point for demonstration purposes. It is not intended to be a production design. |

## Cluster Topology Overview

When deployed in a typical scenario, two distinct Kubernetes clusters have their own isolated Kubernetes control plane and DNS domain (`svc.cluster.local`). With this isolation, a pod in one cluster cannot resolve any name in another cluster. In this demonstration, two kind clusters (`kind-west`, `kind-east`) will illustrate how the Multicluster Services (MCS) API overcomes this limitation and can be used by PingFederate.

Submariner, implementing MCS, joins the clusters at the network layer:

* A Submariner gateway pod on each cluster establishes a cross-cluster tunnel over the Docker bridge network (no NAT required in a local kind setup).

* The Submariner operator installs a Lighthouse CoreDNS plugin in each cluster that intercepts `*.svc.clusterset.local` queries.

After joining, any pod in either cluster can reach pods in the other cluster by their pod CIDR addresses (east pods: `10.245.x.x`, west pods: `10.244.x.x`).

A `ServiceExport` resource instructs the Submariner lighthouse agent to advertise that service into the clusterset. A corresponding `ServiceImport` is created in the same namespace on every other cluster. The Lighthouse CoreDNS plugin answers `<service>.<namespace>.svc.clusterset.local` queries by returning all endpoint pod IPs across all clusters. For a headless service (like `pingfederate-cluster`), the DNS response contains one A-record per pod across both `kind-west` and `kind-east`.

```
         kind-west                                               kind-east
-----------------------------                        -----------------------------
      pf-mr/pingfederate-admin-0                           pf-mr/pingfederate-admin-0
        DNS_QUERY_LOCATION ->                              DNS_QUERY_LOCATION ->
  pingfederate-cluster.pf-mr.svc.clusterset.local    pingfederate-cluster.pf-mr.svc.clusterset.local
              |                                                      |
              +---------------- Submariner tunnel -------------------+
                                 (Docker bridge)

Lighthouse CoreDNS returns:
  10.244.x.x  (west admin-0 pod IP)
  10.245.x.x  (east admin-0 pod IP)
```

The `pingfederate-admin-active` Service selects pods with label `pf.admin.active: "true"`. The `pfadmin-check-active.sh` hook, called from `liveness.sh` at each liveness interval, queries the admin heartbeat with `?checkActive=true` and patches the pod's label via the Kubernetes API. Only the active node carries the label; the service endpoint changes automatically on failover. Because `pingfederate-admin-active` is also exported via `ServiceExport`, its clusterset FQDN routes to the active pod regardless in which cluster it is running.

## How Discovery Works in This Approach

JGroups `DNS_PING` resolves `DNS_QUERY_LOCATION` to find cluster members. In a single cluster, `DNS_QUERY_LOCATION` points at the local headless Service (`svc.cluster.local`). In a multi-cluster setup without shared DNS, that resolution fails across cluster boundaries. With Submariner in place, setting `DNS_QUERY_LOCATION` to the clusterset address gives JGroups a single DNS name that always returns the full member list regardless in which cluster the pod is located.

When `PF_ADMIN_SEED` is not set, the image uses `DNS_PING` — this value is the default and resolves as expected.

## Prerequisites

* Docker (Docker Desktop Kubernetes **disabled** to avoid `kind` conflicts)

* `kind` — `brew install kind`

* `kubectl` — `brew install kubectl`

* `kubectx` - a convenience tool for managing contexts (<https://github.com/ahmetb/kubectx#installation>)

* `helm` — `brew install helm`

* `kustomize` — `brew install kustomize`

* `subctl` — `curl -Ls https://get.submariner.io | bash` (installs to `~/.local/bin`)

* [Ping Identity DevOps](../how-to/devopsRegistration.html) credentials

* PingFederate image `2605` or later (required for the multi-cluster hook logic in `scripts.yaml`)

Recommended resources: 8 or more CPUs, 16 GB or more RAM.

## Deploy Submariner Kind Clusters

Install `subctl` and create two kind clusters with non-overlapping CIDRs, then join them via Submariner.

### Install subctl

```shell
curl -Ls https://get.submariner.io | bash
export PATH="$HOME/.local/bin:$PATH"
subctl version
```

### Create kind clusters

The kind cluster configurations used here include `extraPortMappings` that bind host ports directly to a NodePort on each cluster's control-plane node. This configuration enables the user to access the PingFederate admin console from a host browser without a running `kubectl port-forward` session. See [Why NodePort instead of port-forward](#devops-pf-submariner-nodeport-rationale) for details.

Create `kind-west.yaml`:

```yaml
kind: Cluster
apiVersion: kind.x-k8s.io/v1alpha4
networking:
  podSubnet: "10.244.0.0/16"
  serviceSubnet: "10.96.0.0/16"
nodes:
- role: control-plane
  extraPortMappings:
  - containerPort: 30999
    hostPort: 9999
    protocol: TCP
- role: worker
```

Create `kind-east.yaml`:

```yaml
kind: Cluster
apiVersion: kind.x-k8s.io/v1alpha4
networking:
  podSubnet: "10.245.0.0/16"
  serviceSubnet: "10.97.0.0/16"
nodes:
- role: control-plane
  extraPortMappings:
  - containerPort: 30999
    hostPort: 19999
    protocol: TCP
- role: worker
```

Create the clusters:

```shell
kind create cluster --name west --config kind-west.yaml
kind create cluster --name east --config kind-east.yaml
kubectx
# Expected: kind-west, kind-east
```

### Fix proxy settings on kind nodes

If your Docker Desktop has a proxy configured, kind nodes inherit it and `containerd` cannot pull images from `quay.io`. Override `NO_PROXY` to bypass the proxy for registry traffic:

```shell
for node in west-control-plane west-worker east-control-plane east-worker; do
  docker exec $node sh -c '
    mkdir -p /etc/systemd/system/containerd.service.d
    cat > /etc/systemd/system/containerd.service.d/no-proxy.conf << EOF
[Service]
Environment="NO_PROXY=quay.io,registry.access.redhat.com,gcr.io,k8s.gcr.io,registry.k8s.io,docker.io"
EOF
    systemctl daemon-reload && systemctl restart containerd
  '
done
```

### Pre-load Submariner images

Submariner 0.24.0 uses images from `quay.io`. Pull them to the host and load into each node to avoid pull failures:

```shell
IMAGES=(
  quay.io/submariner/submariner-operator:0.24.0
  quay.io/submariner/submariner-gateway:0.24.0
  quay.io/submariner/submariner-route-agent:0.24.0
  quay.io/submariner/lighthouse-agent:0.24.0
  quay.io/submariner/lighthouse-coredns:0.24.0
)

for img in "${IMAGES[@]}"; do docker pull "$img"; done

for cluster in west east; do
  for node in $(kubectl --context kind-${cluster} get nodes -o jsonpath='{.items[*].metadata.name}'); do
    for img in "${IMAGES[@]}"; do
      docker save "$img" | docker exec -i $node ctr -n k8s.io images import -
    done
  done
done
```

### Deploy Submariner broker and join clusters

```shell
# Deploy broker on west (it becomes the broker host)
subctl deploy-broker --context kind-west

# Label gateway nodes
kubectl --context kind-west label node west-worker submariner.io/gateway=true
kubectl --context kind-east label node east-worker submariner.io/gateway=true

# Join both clusters
subctl join broker-info.subm --context kind-west --clusterid west \
  --natt=false --label-gateway=false --check-broker-certificate=false

subctl join broker-info.subm --context kind-east --clusterid east \
  --natt=false --label-gateway=false --check-broker-certificate=false
```

After `subctl join`, the operator on each cluster tries to reach the broker using `127.0.0.1` (the host port-forward address), which is unreachable from inside the pod. Patch the broker URL to use in-cluster addresses:

```shell
# west operator reaches broker via its own in-cluster kubernetes service
# 10.96.0.1 is the ClusterIP of the kubernetes service in the default namespace:
#   kubectl --context kind-west get svc kubernetes -n default
kubectl --context kind-west patch submariner -n submariner-operator submariner \
  --type=json -p='[{"op":"replace","path":"/spec/brokerK8sApiServer","value":"10.96.0.1:443"}]'

# east operator must reach west's API server via the docker bridge network
C1_IP=$(docker inspect west-control-plane \
  --format '{{(index .NetworkSettings.Networks "kind").IPAddress}}')
kubectl --context kind-east patch submariner -n submariner-operator submariner \
  --type=json -p="[{\"op\":\"replace\",\"path\":\"/spec/brokerK8sApiServer\",\"value\":\"${C1_IP}:6443\"}]"
```

Verify connectivity:

```shell
subctl show connections --context kind-west
# GATEWAY           CLUSTER    REMOTE IP   NAT   STATUS
# east-worker       east       172.19.x.x  no    connected
```

## Prepare Namespaces and Secrets

```shell
DEVOPS_USER=<your-devops-user>
DEVOPS_KEY=<your-devops-key>

for ctx in kind-west kind-east; do
  kubectl --context $ctx create namespace pf-mr
  kubectl --context $ctx create secret generic devops-secret -n pf-mr \
    --from-literal=PING_IDENTITY_DEVOPS_USER=$DEVOPS_USER \
    --from-literal=PING_IDENTITY_DEVOPS_KEY=$DEVOPS_KEY
done
```

## Deployment Files

This deployment uses four files. Three are Helm values files consumed directly by `helm upgrade --install`; the fourth is a Kustomize post-renderer that injects additional Kubernetes resources that the `ping-devops` chart does not generate natively.

### scripts.yaml

This file defines two scripts mounted into the admin pods as ConfigMap entries. Starting with the `2605` release of the PingFederate image, there is new hook logic that uses `403 + license_agreement_not_accepted` detection to determine whether a node needs seeding, which works correctly in both single- and multi-cluster deployments with a shared DNS.

The two scripts here:

* `liveness.sh` calls `pfadmin-check-active.sh` on each liveness check to keep the pod label in sync with the current active/passive role.

* `pfadmin-check-active.sh` queries the active heartbeat endpoint and patches the pod's `pf.admin.active` label accordingly. The `pingfederate-admin-active` Service selector uses this label to route traffic only to the currently active node.

```yaml
configMaps:
  custom-hooks:
    data:
      liveness.sh: |-
        #!/usr/bin/env sh
        URL="https://127.0.0.1:${PF_ENGINE_PORT}/pf/heartbeat.ping"
        if test "${OPERATIONAL_MODE}" = "CLUSTERED_CONSOLE" -o "${OPERATIONAL_MODE}" = "STANDALONE"; then
            test -f /tmp/ready || exit 1
            if test "${PF_CLUSTER_ADMIN_NODES_SYNC_ENABLED}" = "true"; then
                . "${HOOKS_DIR}/pfadmin-check-active.sh"
                setPFActive
            fi
            test "${OPERATIONAL_MODE}" = "CLUSTERED_CONSOLE" && URL="https://127.0.0.1:${PF_ADMIN_PORT}/pf/heartbeat.ping"
        fi
        curl -sSk -o /dev/null "${URL}" || exit 1
      pfadmin-check-active.sh: |-
        #!/usr/bin/env sh
        setPFActive() {
            APISERVER="https://kubernetes.default.svc"
            SERVICEACCOUNT="/var/run/secrets/kubernetes.io/serviceaccount"
            NAMESPACE=$(cat ${SERVICEACCOUNT}/namespace)
            TOKEN=$(cat ${SERVICEACCOUNT}/token)
            CACERT=${SERVICEACCOUNT}/ca.crt
            POD_NAME=$(hostname)

            URL="https://127.0.0.1:${PF_ADMIN_PORT}/pf/heartbeat.ping?checkActive=true"
            _activelabel="false"
            _curlres=$(curl -sSk -o /dev/null -w "%{response_code}" "${URL}" 2>/dev/null)
            test "${_curlres}" -eq "200" && _activelabel="true"

            curl -s --cacert ${CACERT} -X PATCH -o /dev/null -w "%{http_code}" \
                -H "Content-Type: application/strategic-merge-patch+json" \
                -H "Authorization: Bearer ${TOKEN}" \
                "${APISERVER}/api/v1/namespaces/${NAMESPACE}/pods/${POD_NAME}" \
                --data "{\"metadata\":{\"labels\":{\"pf.admin.active\":\"${_activelabel}\"}}}"
        }
```

### base.yaml

The west cluster Helm values. `global.image.tag` sets the image version for all products. `PF_NODE_GROUP_ID` labels the cluster in the PingFederate console and is used by the `east-pf.yaml` override to distinguish the east cluster.

```yaml
global:
  addReleaseNameToResource: none
  image:
    tag: "2605"
  envs:
    PING_IDENTITY_ACCEPT_EULA: "YES"
    PING_IDENTITY_PASSWORD: 2FederateM0re

pingfederate-admin:
  enabled: true
  envs:
    OPERATIONAL_MODE: CLUSTERED_CONSOLE
    # clusterset.local resolves across both clusters via Submariner Lighthouse CoreDNS
    DNS_QUERY_LOCATION: "pingfederate-cluster.pf-mr.svc.clusterset.local"
    PF_NODE_GROUP_ID: west
    PF_CLUSTER_ADMIN_NODES_SYNC_ENABLED: "true"
  volumeMounts:
    - mountPath: "/opt/liveness.sh"
      name: custom-vol
      subPath: liveness.sh
    - mountPath: "/opt/in/hooks/pfadmin-check-active.sh"
      name: custom-vol
      subPath: pfadmin-check-active.sh
  volumes:
    - name: custom-vol
      configMap:
        name: custom-hooks
        defaultMode: 0777
  rbac:
    generateServiceAccount: true
    serviceAccountName: pf-mc-admin-sa
    generateRoleAndRoleBinding: true
    applyServiceAccountToWorkload: true
    role:
      rules:
        - apiGroups: [""]
          resources: ["pods"]
          verbs: ["get", "watch", "list", "patch"]
  workload:
    labels:
      active: "false"
    type: StatefulSet
    statefulSet:
      persistentvolume:
        enabled: true

pingfederate-engine:
  enabled: false
```

### east-pf.yaml

Applied on top of `base.yaml` for the east cluster deployment. Overrides the cluster identity.

```yaml
pingfederate-admin:
  enabled: true
  envs:
    PF_NODE_GROUP_ID: east
  container:
    replicaCount: 1
```

### Kustomize Post-Renderer

The `ping-devops` chart does not generate per-instance `ServiceExport` resources or the selector-based active-admin Services. A Kustomize post-renderer injects these after Helm renders its manifests.

Create a `kustomize/` subdirectory with these five files.

`kustomize/kustomize` (executable script):

```bash
#!/bin/bash
cd "$(dirname "$0")"
cat <&0 > all.yaml
kustomize build . && rm all.yaml
```

```shell
chmod +x kustomize/kustomize
```

`kustomize/kustomization.yaml`:

```yaml
resources:
  - all.yaml
  - pf-admin-active-svc.yaml
  - pf-admin-active-nodeport.yaml
  - ServiceExport.yaml
```

`kustomize/pf-admin-active-svc.yaml` — a ClusterIP Service that selects only pods with label `pf.admin.active: "true"`:

```yaml
apiVersion: v1
kind: Service
metadata:
  name: pingfederate-admin-active
  namespace: pf-mr
  labels:
    app.kubernetes.io/instance: pf-mr
    app.kubernetes.io/managed-by: Helm
    app.kubernetes.io/name: pingfederate-admin
spec:
  ports:
    - name: https
      port: 9999
      protocol: TCP
      targetPort: 9999
  selector:
    app.kubernetes.io/instance: pf-mr
    app.kubernetes.io/name: pingfederate-admin
    pf.admin.active: "true"
```

`kustomize/pf-admin-active-nodeport.yaml` — a NodePort Service using the same `pf.admin.active: "true"` selector, bound to `nodePort: 30999` which maps to host ports via `extraPortMappings` in the kind cluster configuration:

```yaml
apiVersion: v1
kind: Service
metadata:
  name: pingfederate-admin-active-nodeport
  namespace: pf-mr
spec:
  type: NodePort
  ports:
    - name: https
      port: 9999
      targetPort: 9999
      nodePort: 30999
      protocol: TCP
  selector:
    app.kubernetes.io/instance: pf-mr
    app.kubernetes.io/name: pingfederate-admin
    pf.admin.active: "true"
```

`kustomize/ServiceExport.yaml` — exports all four PingFederate services into the Submariner clusterset so they are accessible from both clusters via `svc.clusterset.local`:

```yaml
apiVersion: multicluster.x-k8s.io/v1alpha1
kind: ServiceExport
metadata:
  name: pingfederate-admin
  namespace: pf-mr
---
apiVersion: multicluster.x-k8s.io/v1alpha1
kind: ServiceExport
metadata:
  name: pingfederate-admin-active
  namespace: pf-mr
---
apiVersion: multicluster.x-k8s.io/v1alpha1
kind: ServiceExport
metadata:
  name: pingfederate-cluster
  namespace: pf-mr
---
apiVersion: multicluster.x-k8s.io/v1alpha1
kind: ServiceExport
metadata:
  name: pingfederate-engine
  namespace: pf-mr
```

## Deploy

The `kustomize/kustomize` script acts as a Helm post-renderer: it receives the rendered manifests on stdin and emits them plus the additional resources that the `ping-devops` chart does not generate natively.

Helm v4 requires post-renderers to be registered as plugins — passing a script path directly does not work. Create a `plugin.yaml` file in your working directory, replacing `<absolute-path-to>` with the absolute path to your `kustomize/` directory:

```yaml
name: "kustomize-renderer"
apiVersion: "v1"
version: "0.1.0"
type: "postrenderer/v1"
runtime: "subprocess"
runtimeConfig:
  platformCommand:
    - command: "<absolute-path-to>/kustomize/kustomize"
```

Register the plugin (this is a one-time step per machine):

```shell
mkdir -p "$(helm env HELM_PLUGINS)/kustomize-renderer"
cp plugin.yaml "$(helm env HELM_PLUGINS)/kustomize-renderer/"
```

Verify: `helm plugin list` should show `kustomize-renderer` with type `postrenderer/v1`.

|   |                                                                                                                                                                                                        |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | On Helm v3, plugin registration is not required. You can pass the script path directly with `--post-renderer ./kustomize/kustomize`. See [helm/helm#31340](https://github.com/helm/helm/issues/31340). |

Deploy to the west cluster:

```shell
helm upgrade --install pf-mr pingidentity/ping-devops \
  --kube-context kind-west \
  --namespace pf-mr \
  -f scripts.yaml -f base.yaml \
  --post-renderer kustomize-renderer
```

Wait for `pingfederate-admin-0` to come up and verify ServiceExports and ServiceImports:

```shell
kubectl --context kind-west get serviceexport -n pf-mr
# NAME                       AGE
# pingfederate-admin         ...
# pingfederate-admin-active  ...
# pingfederate-cluster       ...

kubectl --context kind-west get serviceimport -n pf-mr
# NAME                       TYPE          IP     AGE
# pingfederate-admin         ClusterSetIP  ...    ...
# pingfederate-admin-active  ClusterSetIP  ...    ...
# pingfederate-cluster       Headless             ...
```

Deploy to the east cluster:

```shell
helm upgrade --install pf-mr pingidentity/ping-devops \
  --kube-context kind-east \
  --namespace pf-mr \
  -f scripts.yaml -f base.yaml -f east-pf.yaml \
  --post-renderer kustomize-renderer
```

## Accessing the Admin Console

The standard `pingfederate-admin` Service includes all admin pods — active and passive. Passive nodes return `403` for most admin operations and give severely limited console access. Always use `pingfederate-admin-active` to reach the admin console or admin API.

With the scripts in place, the `pf.admin.active` label is refreshed on each pod at every liveness interval. When this label is in place, the `pingfederate-admin-active` Service's selector matches only the active pod so its endpoint tracks the currently active node automatically — including across a failover from one cluster to the other.

### Why NodePort instead of port-forward

On macOS, Docker Desktop runs kind nodes inside a Linux VM. MetalLB LoadBalancer IPs live on the Docker bridge inside that VM and are not reachable from the host browser. `kubectl port-forward` works but requires a live terminal session, breaks on pod restart, and can only target one cluster at a time.

kind `extraPortMappings` bind a host port to a container port on the kind control-plane node at cluster creation time. This gives each cluster a stable `localhost` URL with no running process required. The `pingfederate-admin-active-nodeport` Service uses the same `pf.admin.active: "true"` selector as the ClusterIP service — it tracks the active node automatically and follows failover to the other cluster.

In a production environment, this port configuration would likely not be necessary. However, in any case, there would need to be some means of tracking the active pod and dynamically or manually updating DNS or other configurations to get to the active console. In this demonstration, we rely on using the assigned port of the active cluster service as our indicator for which pod we will be accessing.

|   |                                                                                                                                                                                                          |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | If host port `9999` is already in use on your machine, change `hostPort` in the `kind-west.yaml` configuration and update the browser URL accordingly. The same applies to `19999` for the east cluster. |

### Determining which cluster holds the active node

```shell
kubectl --context kind-west -n pf-mr get pods \
  -l pf.admin.active=true -o wide

kubectl --context kind-east -n pf-mr get pods \
  -l pf.admin.active=true -o wide
```

Exactly one pod across both clusters should show `pf.admin.active=true`.

### Open the console in a browser

Open the PingFederate admin console using the host port for the cluster that holds the active node:

* West active: `https://localhost:9999/pingfederate/app`

* East active: `https://localhost:19999/pingfederate/app`

Accept the self-signed certificate warning. Log in with username `administrator` and password `2FederateM0re`.

|   |                                                                                                                                                                                                      |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The NodePort on the cluster that does not hold the active node has no endpoint and returns no response. This is expected — it also serves as a quick indicator of which cluster is currently active. |

### After failover

When the active node changes, liveness checks on the surviving pods update their labels within one liveness period. The `pingfederate-admin-active-nodeport` endpoint shifts accordingly. Re-run the active node check above to confirm which cluster holds the new active pod, then open the corresponding browser URL.

## Validation

### Cluster Status

Query from whichever cluster holds the active node (see [Determining which cluster holds the active node](#devops-pf-submariner-active-node)):

```shell
kubectl --context kind-west -n pf-mr exec pingfederate-admin-0 -- \
  curl --insecure --silent \
    -H 'X-XSRF-Header: PingFederate' \
    --user "administrator:2FederateM0re" \
    'https://localhost:9999/pf-admin-api/v1/cluster/status' | jq .
```

Expected: 1 `ACTIVE` node, all others `PASSIVE`.

### Active Service Endpoint

```shell
kubectl --context kind-west -n pf-mr get endpoints pingfederate-admin-active
# NAME                       ENDPOINTS           AGE
# pingfederate-admin-active  10.130.1.57:9999    ...
# (single endpoint — the active pod only)

kubectl --context kind-west -n pf-mr get endpoints pingfederate-admin
# NAME                  ENDPOINTS                             AGE
# pingfederate-admin    10.130.1.57:9999,10.130.1.59:9999    ...
# (all admin pods)
```

### Scale Test

```shell
kubectl --context kind-west -n pf-mr scale sts pingfederate-admin --replicas=2
```

Expected log from `pingfederate-admin-1`:

```shell
INFO: Node is already seeded (HTTP 200). Skipping initial setup.
INFO: Querying cluster for existing active admin node...
INFO: Active admin already present in cluster. This node will remain passive.
```

The `pingfederate-admin-active` endpoint must still point only at the original active pod.

### Simultaneous Cold Start Validation

Both clusters deployed in the preceding steps without sequencing already proves this feature will work. The 403-detection in hook 81 (built into the image) handles the potential race condition: each node queries `/cluster/status`; whichever sees `403 + license_agreement_not_accepted` first seeds itself and promotes; the other sees `200` (state already replicated via DNS\_PING) and stays passive.

To repeat the test explicitly:

```shell
kubectl --context kind-west -n pf-mr delete pvc --all
kubectl --context kind-east -n pf-mr delete pvc --all
kubectl --context kind-west delete namespace pf-mr
kubectl --context kind-east delete namespace pf-mr

kubectl --context kind-west create namespace pf-mr
kubectl --context kind-east create namespace pf-mr
# (re-create devops-secret in both namespaces)

helm upgrade --install pf-mr pingidentity/ping-devops \
  --kube-context kind-west --namespace pf-mr \
  -f scripts.yaml -f base.yaml \
  --post-renderer kustomize-renderer &

helm upgrade --install pf-mr pingidentity/ping-devops \
  --kube-context kind-east --namespace pf-mr \
  -f scripts.yaml -f base.yaml -f east-pf.yaml \
  --post-renderer kustomize-renderer &
wait

kubectl --context kind-west -n pf-mr rollout status statefulset/pingfederate-admin --timeout=15m &
kubectl --context kind-east -n pf-mr rollout status statefulset/pingfederate-admin --timeout=15m &
wait
```

Expected: 2 nodes in cluster status, exactly 1 `ACTIVE`, 1 `PASSIVE`.

### Cross-Cluster DNS Verification

Confirm the clusterset DNS name resolves from an east pod:

```shell
kubectl --context kind-east -n pf-mr exec pingfederate-admin-0 -- \
  nslookup pingfederate-cluster.pf-mr.svc.clusterset.local
# Returns A-records for all pod IPs across both clusters
```

## Cleanup

Delete the PersistentVolumeClaims before deleting the clusters. kind's local-path provisioner binds PVCs to host directories on the kind nodes; deleting the cluster without first removing the PVCs leaves those directories orphaned on the host.

```shell
kubectl --context kind-west -n pf-mr delete pvc --all
kubectl --context kind-east -n pf-mr delete pvc --all
```

Then delete the kind clusters. All Submariner broker state, gateway state, and `subctl join` artifacts are destroyed with the clusters — no separate Submariner cleanup step is required.

```shell
kind delete cluster --name west
kind delete cluster --name east
```

---

---
title: Restoring a Multi-Region PingDirectory Deployment After Seed Cluster Failure
description: Manually restore a multi-region PingDirectory topology after the seed cluster and its persistent volumes are lost
component: devops
page_id: devops::deployment/restorePDMultiRegionSeedFailure
canonical_url: https://developer.pingidentity.com/devops/deployment/restorePDMultiRegionSeedFailure.html
llms_txt: https://developer.pingidentity.com/devops/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  devops-starting-point: Starting point
  devops-overview: Overview
  devops-force-a-server-to-act-as-master-of-the-topology: Force a server to act as master of the topology
  devops-remove-the-unreachable-servers-from-the-topology: Remove the unreachable servers from the topology
  devops-undo-forcing-a-server-to-act-as-master-of-the-topology: Undo forcing a server to act as master of the topology
  devops-remove-the-seed-servers-from-their-own-topology-after-restart-if-necessary: Remove the seed servers from their own topology after restart if necessary
  devops-add-the-servers-from-the-refreshed-seed-region-to-the-topology-of-the-surviving-region: Add the servers from the refreshed seed region to the topology of the surviving region
  devops-run-dsreplication-initialize-all-from-a-server-of-the-surviving-region: Run dsreplication initialize-all from a server of the surviving region
---

# Restoring a Multi-Region PingDirectory Deployment After Seed Cluster Failure

The PingDirectory hook scripts rely on the seed server of the seed cluster being available when running in a multi-region environment. This dependency leads to the question of what can be done if the seed region's servers, along with their persistent volumes, are lost. This page describes manual steps that can be taken to restore the PingDirectory topology in this case.

|   |                                                                                            |
| - | ------------------------------------------------------------------------------------------ |
|   | These steps are only needed if the seed region is lost *including its persistent volumes*. |

In this document, the non-seed region is referred to as the "surviving" region.

## Starting point

Assume the seed region and all of its persistent volumes have been lost. The surviving region will still replicate among itself, but it will not be able to reach the seed region servers even after they are restarted, due to changes to the server certificates caused by the restart.

In the examples on this page, `east` represents the original seed region that has failed and is being rebuilt, while `west` represents the surviving region that remains online and is used to restore the topology. This matches the seed-versus-secondary relationship shown in the multi-region deployment example, even though this page shortens the regional labels to `east` and `west`.

If you compare this page with the multi-region deployment example, interpret the failed seed region here as the previously configured seed cluster, and interpret the surviving region as the secondary cluster that remained available.

Running the `status` command on one of the surviving pods, you will see in the output that there are configured servers in the topology that are not reachable:

```
          --- Mirrored Subtrees ---
Base DN               : Write Master                   : Configured      : Outbound        : Inbound         : Failed Write
                      :                                : Peers           : Connections     : Connections     : Operations
----------------------:--------------------------------:-----------------:-----------------:-----------------:----------------
cn=Cluster,cn=config  : N/A (single instance topology) : 0               : 0               : 0               : 0
cn=Topology,cn=config : No Master (data read-only)     : 3               : 1               : 1               : 0
```

You will also see administrative alerts in the output indicating that the mirrored subtree manager cannot establish a connection with the servers in the seed region.

## Overview

The key steps to restore the topology in this case are:

1. Force a server in the surviving region to act as master of the topology

2. Remove the unreachable servers from the topology

3. Undo forcing a server to act as master of the topology

4. Ensure any seed region pods are in single-server topologies

5. Use `dsreplication enable` to add the servers from the refreshed seed region to the topology of the surviving region

6. Use `dsreplication initialize-all` from a server of the surviving region to update the data across the regions

## Force a server to act as master of the topology

The PingDirectory topology will see that it cannot connect with half the servers and will switch to read-only mode. To allow the changes we need to make to the topology to fix this, exec into one of the pods in the surviving region.

`kubectl exec -ti example-pingdirectory-0 sh`

Run the following command to force this pod as master:

`dsconfig set-global-configuration-prop --set force-as-master-for-mirrored-data:true --no-prompt`

## Remove the unreachable servers from the topology

Now we must tell the surviving pods that the original seed region pods no longer exist, and that they must be removed from the topology. These commands may take a long time to run, as the `remove-defunct-server` tool will keep trying to connect for up to ten minutes depending on the state of the seed region.

`remove-defunct-server --ignoreOnline --serverInstanceName example-pingdirectory-1.east --bindDN [bind dn] --bindPassword [bind password]`

In the above command, replace the `--serverInstanceName` argument with the instance name of one of the seed region pods. Repeat the command for each seed region pod's instance name.

This step may differ depending on the state of the seed region. If the seed region is wiped out and is still not available, then you may be prompted during the `remove-defunct-server` process whether you want to retry connecting to a server that was from the failed seed region. Enter "no" and continue if prompted.

If the seed region has been restored and the servers are up by the time you are running this command, then you will likely see the ten minute timeout described above. This situation occurs because the servers are available on the same hostnames as before, but their inter-server certificates have changed during the restart. The new certificates mean SSL connections will not be possible, leading to the connection timeout.

## Undo forcing a server to act as master of the topology

At this point the pods in the surviving region should now be the only pods in that region's topology - they should no longer be attempting to contact any pod from the failed seed region.

```
  --- Mirrored Subtrees ---
Base DN               : Write Master                   : Configured      : Outbound        : Inbound         : Failed Write
                      :                                : Peers           : Connections     : Connections     : Operations
----------------------:--------------------------------:-----------------:-----------------:-----------------:----------------
cn=Cluster,cn=config  : N/A (single instance topology) : 0               : 0               : 0               : 0
cn=Topology,cn=config : example-pingdirectory-0.west   : 1               : 1               : 1               : 0
```

Exec into the pod that was forced as master in the first step. Run this command to undo the previous change:

`dsconfig set-global-configuration-prop --set force-as-master-for-mirrored-data:false --no-prompt`

## Remove the seed servers from their own topology after restart if necessary

If the seed region was completely wiped out and unavailable during the earlier `remove-defunct-server` step, this step will be necessary. When the seed region comes up again, it will join its servers together in a new topology containing only the seed pods, as it is unaware of the other region.

It is not possible to merge two existing topologies containing more than one server each. We need to split up the restarted seed region pods into individual single-server topologies so that we can add them to the topology of the surviving region.

Exec into one of the seed region pods:

`kubectl exec -ti example-pingdirectory-0 sh`

Use `remove-defunct-server` to split up each server, starting with the highest pod ordinal and working down until ordinal `1`. After this is done, all seed region pods will be in separate single-server topologies, and we can then add them to the existing topology of the surviving region.

`remove-defunct-server --ignoreOnline --serverInstanceName example-pingdirectory-1.east --bindDN [bind dn] --bindPassword [bind password]`

## Add the servers from the refreshed seed region to the topology of the surviving region

At this point the servers in the seed region should be in their own single-server topologies, and the servers in the surviving region should be in a topology containing only the pods in that region.

Now we can re-enable replication between the regions. Run the following command once for each pod in the seed region, updating the `--host1` or `--host2` argument each time to point to the server being enabled in that run. The command can be run from a shell on any pod.

```
dsreplication enable \
    --trustAll \
    --host1 example-pingdirectory-0.example.west.example.com \
    --port1 "${LDAPS_PORT}" \
    --useSSL1 \
    --replicationPort1 "${REPLICATION_PORT}" \
    --bindDN1 "${ROOT_USER_DN}" \
    --bindPasswordFile1 "${ROOT_USER_PASSWORD_FILE}" \
    --host2 example-pingdirectory-0.example.east.example.com \
    --port2 "${LDAPS_PORT}" \
    --useSSL2 \
    --replicationPort2 "${REPLICATION_PORT}" \
    --bindDN2 "${ROOT_USER_DN}" \
    --bindPasswordFile2 "${ROOT_USER_PASSWORD_FILE}" \
    --adminUID "${ADMIN_USER_NAME}" \
    --adminPasswordFile "${ADMIN_USER_PASSWORD_FILE}" \
    --no-prompt --ignoreWarnings \
    --baseDN dc=example,dc=com \
    --noSchemaReplication
```

## Run dsreplication initialize-all from a server of the surviving region

All of the pods are again in a topology together. Now we need to initialize the seed region with the data from the surviving region. Run the following command, targeting a server in the surviving region with the `--hostname` argument (this indicates which server the data is coming from, so we want to use a server in the surviving region):

```
dsreplication initialize-all \
    --hostname example-pingdirectory-0.example.west.example.com \
    --port 7700 --useSSL \
    --baseDN dc=example,dc=com --adminUID admin \
    --adminPasswordFile /tmp/pw --no-prompt
```

Now we can see from `dsreplication status --showAll` that all the pods are replicating and have matching generation IDs:

```
          --- Replication Status for dc=example,dc=com: Enabled ---
Server                                                                               : Location : Entries : Conflict Entries : Backlog (1) : Rate (2) : A.O.B.C. (3) : Generation ID : Server ID : Replica ID
-------------------------------------------------------------------------------------:----------:---------:------------------:-------------:----------:--------------:---------------:-----------:-----------
example-pingdirectory-0.west (example-pingdirectory-0.example.west.example.com:7700) : west     : 2038    : 0                : 0           : 0        : 0 seconds    : 4105471824    : 19064     : 32073
example-pingdirectory-1.west (example-pingdirectory-1.example.west.example.com:7700) : west     : 2038    : 0                : 0           : 0        : 0 seconds    : 4105471824    : 4444      : 18281
example-pingdirectory-0.east (example-pingdirectory-0.example.east.example.com:7700) : east     : 2038    : 0                : 0           : 0        : 0 seconds    : 4105471824    : 28554     : 13185
example-pingdirectory-1.east (example-pingdirectory-1.example.east.example.com:7700) : east     : 2038    : 0                : 0           : 0        : 0 seconds    : 4105471824    : 2590      : 4761
```

And from `status` we can see all the inbound and outbound connections are functioning as expected:

```
          --- Mirrored Subtrees ---
Base DN               : Write Master                   : Configured      : Outbound        : Inbound         : Failed Write
                      :                                : Peers           : Connections     : Connections     : Operations
----------------------:--------------------------------:-----------------:-----------------:-----------------:----------------
cn=Cluster,cn=config  : N/A (single instance topology) : 0               : 0               : 0               : 0
cn=Topology,cn=config : example-pingdirectory-0.west   : 3               : 3               : 3               : 0
```