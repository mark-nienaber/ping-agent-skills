---
title: Quick deployment on minikube
description: Perform the steps described in this section to set up a demo or development environment on minikube.
component: forgeops
version: 2026.2
page_id: forgeops:quick:quick-set-mini
canonical_url: https://docs.pingidentity.com/forgeops/2026.2/quick/quick-set-mini.html
llms_txt: https://docs.pingidentity.com/forgeops/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  set_up_a_minikube_cluster: Set up a minikube cluster
  perform_forgeops_deployment: Perform ForgeOps deployment
  access_the_administrator_ui: Access the administrator UI
---

# Quick deployment on minikube

Perform the steps described in this section to set up a demo or development environment on minikube.

|   |                                                                                                                                                                                                                                                                              |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Use the steps described here only to set up in a demo or development environment. More information about setting up clusters is available in [Setup overview](../setup/overview.html), and performing ForgeOps deployment in [Deployment overview](../deploy/overview.html). |

## Set up a minikube cluster

1. Clone the `forgeops` and check out the `2026.2.1`. For example:

   ```
   $ git clone https://github.com/ForgeRock/forgeops.git
   $ cd forgeops
   $ git checkout 2026.2.1
   ```

2. Ensure that you have installed the following:

   1. Required third-party software. Learn more about required third-party software [here](../setup/minikube.html#minikube-third-party-software).

   2. Docker engine. Learn more about Docker requirements [here](../setup/minikube.html#docker-mini).

3. Set up a minikube cluster:

   1. Create minikube cluster:

      ```
      $ minikube start --cpus=3 --memory=9g --disk-size=40g --cni=true \
        --kubernetes-version=stable --addons=ingress,volumesnapshots,metrics-server \
        --driver=docker
      ```

   2. Add an entry to the /etc/hosts file to resolve the deployment FQDN, for example forgeops.example.com:

      ```
      127.0.0.1 forgeops.example.com
      ```

4. Create a `venv` for using the `forgeops` utility:

   1. Initiate a Python virtual environment\[[1](#_footnotedef_1 "View footnote.")].

      ```
      $ python3 -m venv .venv
      ```

   2. Configure Python3 dependencies for `forgeops` utility.

      ```
      $ source .venv/bin/activate
      $ /path/to/forgeops/bin/forgeops configure
      ```

## Perform ForgeOps deployment

This section describes steps to perform ForgeOps deployment on minikube quickly using Helm. Learn more about deployment steps in [Deployment overview](../deploy/overview.html).

**Perform the following steps in the terminal window where you have activated the Python venv.**

1. Set up the default cluster issuer\[[2](#_footnotedef_2 "View footnote.")]. For example:

   ```
   $ kubectl apply -f /path/to/forgeops/etc/resources/selfsigned-issuer.yaml
   ```

2. Set up a ForgeOps deployment configuration environment:

   ```
   $ cd /path/to/forgeops/bin
   $ ./forgeops env --env-name my-env --fqdn forgeops.example.com --cluster-issuer my-cluster-issuer --single-instance
   ```

   In the previous command, replace forgeops.example.com and my-cluster-issuer with appropriate values from your environment.

3. Set up your Kubernetes context:

   1. Create a Kubernetes namespace in the cluster for the Ping Advanced Identity Software pods:

      ```
      $ kubectl create namespace my-namespace
      ```

   2. Set the active namespace in your Kubernetes context to the Kubernetes namespace you just created:

      ```
      $ kubens my-namespace
      ```

4. Install the prerequisites:

   ```
   $ ./forgeops prereqs
   ```

5. In a separate terminal tab or window, run the minikube tunnel command, and enter your system's superuser password when prompted:

   ```
   $ sudo minikube tunnel
   ✅  Tunnel successfully started
   ...
   ```

6. Set up the `fast` storage class using the `minikube-fast-storage-class.yaml` file in the /path/to/forgeops/etc/resources directory:

   ```
   $ kubectl apply -f /path/to/forgeops/etc/resources/minikube-fast-storage-class.yaml
   ```

7. Enable secret generator in your deployment environment:

   ```
   $ cd /path/to/forgeops/bin
   $ ./forgeops env --env-name my-env --namespace my-namespace
   ```

8. Perform a ForgeOps deployment using Helm:

   ```
   $ helm upgrade --install identity-platform identity-platform \
    --repo https://ForgeRock.github.io/forgeops/ \
    --namespace my-namespace \
    --values /path/to/forgeops/helm/my-env/values.yaml
   ```

9. Check the status of the pods in the namespace in which you deployed the platform until all the pods are ready:

   1. Run the kubectl get pods command.

   2. Review the output. Deployment is complete when:

      * All entries in the `STATUS` column indicate `Running` or `Completed`.

      * The `READY` column indicates all running containers are available. The entry in the `READY` column represents \[total number of containers/number of available containers].

   3. If necessary, continue to query your deployment's status until all the pods are ready.

## Access the administrator UI

1. Obtain the `amadmin` user's password:

   ```
   $ cd /path/to/forgeops/bin
   $ ./forgeops info | grep amadmin
   vr58qt11ihoa31zfbjsdxxrqryfw0s31 (amadmin user)
   ```

2. Open a new window or tab in a web browser.

   1. Go to https\://forgeops.example.com/platform.

      The Kubernetes ingress controller handles the request, routing it to the `login-ui` pod.

      The login UI prompts you to log in.

   2. Log in as the `amadmin` user, with the password you obtained in the previous step.

      The Ping Advanced Identity Software UI appears in the browser.

***

[1](#_footnoteref_1). If you have updated Python3, you should delete the existing virtual environment and create a new one using the updated python3 version: rm -rf .venv && python3 -m venv .venv && ./bin/forgeops configure[2](#_footnoteref_2). You can use the self-signed issuer provided by ForgeOps for test purposes. For production environments, ForgeOps recommends using a cluster issuer that uses a certificate from a trusted certificate authority (CA).
