---
title: Deploy an Example Stack
description: A video demonstration of this example is available here.
component: devops
page_id: devops::get-started/getStartedExample
canonical_url: https://developer.pingidentity.com/devops/get-started/getStartedExample.html
llms_txt: https://developer.pingidentity.com/devops/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  devops-what-you-will-do: What You Will Do
  devops-prerequisites: Prerequisites
  devops-clone-the-repository: Clone the getting-started repository
  devops-deploy-the-example-stack: Deploy the example stack
  devops-next-steps: Next Steps
---

# Deploy an Example Stack

|   |                                                                                                                                                                  |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | A video demonstration of this example is available [here](https://videos.pingidentity.com/detail/videos/devops/video/6313575361112/getting-started-walkthrough). |

|   |                                                                                                                                                                                                                                                                                                                                                               |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | This example was written using Docker Desktop with Kubernetes enabled on the Mac platform using the Apple Silicon chip. The Docker Desktop version used for this guide was `4.46.0 (204649)`, which includes Docker Engine `v28.4.0` and Kubernetes `v1.32.2`. The traefik ingress controller version was `3.6.7`, deployed from Helm chart version `39.0.0`. |

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | If you are new to Kubernetes-based deployments, there is a distinct difference when running under Kubernetes compared to running applications on servers. In a server model, many applications typically run on the same server, and you can access any of them using the same host. For example, many on-premise deployments of PingFederate also include the PingDataConsole, hosted on the same server.Under Kubernetes, however, each application that requires external access is associated with a `service`. A service is a fixed endpoint in the cluster that routes traffic to a given application. So, in this example, there are distinct service endpoints for PingFederate, PingDataConsole, and the other products.In this demo, these service endpoints are load balanced using the Traefik ingress controller. By adding entries to the `/etc/hosts` file, you can access them using typical URL entries. |

The Ping Identity Helm [Getting Started](https://helm.pingidentity.com/getting-started/) page has instructions on getting your environment configured for using the Ping Helm charts.

For more examples, see [Helm Chart Example Configurations](https://developer.pingidentity.com/helm/examples/index.html).

For more information on Helm with Ping products, see [Ping Identity DevOps Helm Charts](https://helm.pingidentity.com).

## What You Will Do

After using Git to clone the `pingidentity-devops-getting-started` repository, you will use Helm to deploy a sample stack to a Kubernetes cluster.

## Prerequisites

* Register for the Ping DevOps program and install/configure `pingctl` with your User and Key

* Install [Git](https://git-scm.com/downloads)

* Follow the instructions on the helm [Getting Started](https://helm.pingidentity.com/getting-started/) page up through updating to the latest charts to ensure you have the latest version of our charts

* Access to a Kubernetes cluster. You can enable Kubernetes in Docker Desktop for a simple cluster, which was the cluster used for this guide (on the Mac platform).

## Clone the `getting-started` repository

1. Clone the `pingidentity-devops-getting-started` repository to your local `${PING_IDENTITY_DEVOPS_HOME}` directory.

   |   |                                                                                                  |
   | - | ------------------------------------------------------------------------------------------------ |
   |   | **The `${PING_IDENTITY_DEVOPS_HOME}` environment variable was set by running `pingctl config`.** |

   ```shell
   cd "${PING_IDENTITY_DEVOPS_HOME}"
   git clone \
     https://github.com/pingidentity/pingidentity-devops-getting-started.git
   ```

## Deploy the example stack

1. Deploy the example stack of our product containers.

   |   |                                                                                                                  |
   | - | ---------------------------------------------------------------------------------------------------------------- |
   |   | For this guide, avoid making changes to the `everything.yaml` file to ensure a successful first-time deployment. |

   1. Create a namespace for running the stack in your Kubernetes cluster.

      ```shell
      # Create the namespace
      kubectl create ns pinghelm

      # Set the kubectl context to the namespace
      kubectl config set-context --current --namespace=pinghelm

      # Confirm
      kubectl config view --minify | grep namespace:
      ```

   2. Deploy the ingress controller to Docker Desktop:

      ```shell
      cd <repository-root>/30-helm/

      helm repo add traefik https://traefik.github.io/charts

      helm repo update traefik

      helm upgrade --install traefik traefik/traefik \
          --namespace traefik --create-namespace \
          -f ingress-traefik-values.yaml
      ```

|   |                                                                                                                                                                                                                                      |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | The values file used to configure traefik during deployment is configured to skip backend TLS verification so the Ping product consoles with self-signed certificates will work with Traefik. Do not use this setting in production. |

1. To wait for the Traefik ingress to reach a healthy state, run the following command. You can also observe the pod status using k9s. You should see one controller pod running when the ingress controller is ready:

   ```shell
   kubectl get pods --namespace traefik
   ```

2. Create a secret in the namespace you will be using to run the example (pinghelm). This secret provides credentials to obtain an evaluation license based on your Ping DevOps username and key:

   ```shell
   kubectl create secret generic devops-secret \
     --from-literal=PING_IDENTITY_DEVOPS_USER="$PING_IDENTITY_DEVOPS_USER" \
     --from-literal=PING_IDENTITY_DEVOPS_KEY="$PING_IDENTITY_DEVOPS_KEY" \
     --from-literal=PING_IDENTITY_ACCEPT_EULA="$PING_IDENTITY_ACCEPT_EULA" \
     --type=Opaque \
     --dry-run=client -o yaml | kubectl apply -f -
   ```

3. This example will use the Helm release name `demo` and DNS domain suffix `*pingdemo.example` for accessing applications. Add all expected hosts to `/etc/hosts`:

   ```shell
   echo '127.0.0.1 demo-pingaccess-admin.pingdemo.example demo-pingaccess-engine.pingdemo.example demo-pingauthorize.pingdemo.example demo-pingauthorizepap.pingdemo.example demo-pingdataconsole.pingdemo.example demo-pingdelegator.pingdemo.example demo-pingdirectory.pingdemo.example demo-pingfederate-admin.pingdemo.example demo-pingfederate-engine.pingdemo.example demo-pingcentral.pingdemo.example' | sudo tee -a /etc/hosts > /dev/null
   ```

4. To install the chart, go to your local `"${PING_IDENTITY_DEVOPS_HOME}"/pingidentity-devops-getting-started/30-helm` directory and run the command shown here. In this example, the release (deployment into Kubernetes by Helm) is called `demo`, forming the prefix for all objects created. The `ingress-demo.yaml` file configures the ingresses for the products to use the ***ping-local*** domain:

   ```shell
   helm upgrade --install demo pingidentity/ping-devops -f everything.yaml -f ingress-demo.yaml
   ```

   The latest product Docker images are automatically downloaded if they have not previously been pulled from [Docker Hub](https://hub.docker.com/u/pingidentity/).

   Sample output:

   ```shell
   NAME: demo
   LAST DEPLOYED: Wed Feb 11 11:06:09 2026
   NAMESPACE: pinghelm
   STATUS: deployed
   REVISION: 1
   DESCRIPTION: Install complete
   TEST SUITE: None
   NOTES:
   #-------------------------------------------------------------------------------------
   # Ping DevOps
   #
   # Description: Ping Identity helm charts - February 4, 2026
   #-------------------------------------------------------------------------------------
   #
   #           Product          tag   typ  #  cpu R/L   mem R/L  Ing
   #    --------------------- ------- --- -- --------- --------- ---
   #    global                2601              0/0       0/0     √
   #
   #  √ pingaccess-admin      2601    sts  1    0/2     1Gi/4Gi   √
   #  √ pingaccess-engine     2601    dep  1    0/2     1Gi/4Gi   √
   #  √ pingauthorize         2601    dep  1    0/2    1.5G/4Gi   √
   #    pingauthorizepap
   #    pingcentral
   #  √ pingdataconsole       2601    dep  1    0/2    .5Gi/2Gi   √
   #    pingdatasync
   #    pingdelegator
   #  √ pingdirectory         2601    sts  1  50m/2     2Gi/8Gi   √
   #    pingdirectoryproxy
   #  √ pingfederate-admin    2601    dep  1    0/2     1Gi/4Gi   √
   #  √ pingfederate-engine   2601    dep  1    0/2     1Gi/4Gi   √
   #
   #    ldap-sdk-tools
   #    pd-replication-timing
   #    pingtoolkit
   #
   #-------------------------------------------------------------------------------------
   # To see values info, simply set one of the following on your helm install/upgrade
   #
   #    --set help.values=all         # Provides all (i.e. .Values, .Release, .Chart, ...) yaml
   #    --set help.values=global      # Provides global values
   #    --set help.values={ image }   # Provides image values merged with global
   #-------------------------------------------------------------------------------------
   ```

   As you can see, PingAccess Admin and Engine, PingData Console, PingDirectory, PingAuthorize, and the PingFederate Admin and Engine are deployed from the provided `everything.yaml` values file.

   It will take several minutes for all components to become operational.

5. To display the status of the deployed components, you can use [k9s](https://k9scli.io/) or issue the corresponding commands shown here:

   * Display the services (endpoints for connecting) by running `kubectl get service --selector=app.kubernetes.io/instance=demo`

     ```shell
     NAME                            TYPE        CLUSTER-IP       EXTERNAL-IP   PORT(S)                   AGE
     demo-pingaccess-admin           ClusterIP   10.105.30.25     <none>        9090/TCP,9000/TCP         6m33s
     demo-pingaccess-admin-cluster   ClusterIP   None             <none>        <none>                    6m33s
     demo-pingaccess-engine          ClusterIP   10.100.1.136     <none>        3000/TCP                  6m33s
     demo-pingauthorize              ClusterIP   10.101.98.228    <none>        443/TCP                   6m33s
     demo-pingauthorize-cluster      ClusterIP   None             <none>        1636/TCP                  6m33s
     demo-pingdataconsole            ClusterIP   10.103.181.27    <none>        8443/TCP                  6m33s
     demo-pingdirectory              ClusterIP   10.106.174.162   <none>        443/TCP,389/TCP,636/TCP   6m33s
     demo-pingdirectory-cluster      ClusterIP   None             <none>        1636/TCP                  6m33s
     demo-pingfederate-admin         ClusterIP   10.96.52.217     <none>        9999/TCP                  6m33s
     demo-pingfederate-cluster       ClusterIP   None             <none>        7600/TCP,7700/TCP         6m33s
     demo-pingfederate-engine        ClusterIP   10.103.84.196    <none>        9031/TCP                  6m33s
     ```

   * To view the pods, run `kubectl get pods --selector=app.kubernetes.io/instance=demo` - you will need to run this at intervals until all pods have started (** Running **status):

     ```shell
     NAME                                       READY   STATUS    RESTARTS   AGE
     demo-pingaccess-admin-0                    1/1     Running   0          7m7s
     demo-pingaccess-engine-59cfb85b9d-7l6tz    1/1     Running   0          7m7s
     demo-pingauthorize-5696dd6b67-hsxnw        1/1     Running   0          7m7s
     demo-pingdataconsole-56b75f9ffb-wld5k      1/1     Running   0          7m7s
     demo-pingdirectory-0                       1/1     Running   0          7m7s
     demo-pingfederate-admin-67cdb47bb4-h88zr   1/1     Running   0          7m7s
     demo-pingfederate-engine-d9889b494-pdhv8   1/1     Running   0          7m7s
     ```

   * To see the ingresses you will use to access the product, run `kubectl get ingress`. If the ingress controller is configured properly, you should see `localhost` as the address as shown here:

     ```shell
     NAME                       CLASS     HOSTS                                       ADDRESS     PORTS     AGE
     demo-pingaccess-admin      traefik     demo-pingaccess-admin.pingdemo.example      localhost   80, 443   7m28s
     demo-pingaccess-engine     traefik     demo-pingaccess-engine.pingdemo.example     localhost   80, 443   7m28s
     demo-pingauthorize         traefik     demo-pingauthorize.pingdemo.example         localhost   80, 443   7m28s
     demo-pingdataconsole       traefik     demo-pingdataconsole.pingdemo.example       localhost   80, 443   7m28s
     demo-pingdirectory         traefik     demo-pingdirectory.pingdemo.example         localhost   80, 443   7m28s
     demo-pingfederate-admin    traefik     demo-pingfederate-admin.pingdemo.example    localhost   80, 443   7m28s
     demo-pingfederate-engine   traefik     demo-pingfederate-engine.pingdemo.example   localhost   80, 443   7m28s   `
     ```

   * To see everything tied to the helm release run `kubectl get all --selector=app.kubernetes.io/instance=demo`:

     ```shell
     NAME                                           READY   STATUS    RESTARTS   AGE
     pod/demo-pingaccess-admin-0                    1/1     Running   0          8m23s
     pod/demo-pingaccess-engine-59cfb85b9d-7l6tz    1/1     Running   0          8m23s
     pod/demo-pingauthorize-5696dd6b67-hsxnw        1/1     Running   0          8m23s
     pod/demo-pingdataconsole-56b75f9ffb-wld5k      1/1     Running   0          8m23s
     pod/demo-pingdirectory-0                       1/1     Running   0          8m23s
     pod/demo-pingfederate-admin-67cdb47bb4-h88zr   1/1     Running   0          8m23s
     pod/demo-pingfederate-engine-d9889b494-pdhv8   1/1     Running   0          8m23s
     ```

     ```shell
     NAME                                  TYPE        CLUSTER-IP       EXTERNAL-IP   PORT(S)                   AGE
     service/demo-pingaccess-admin         ClusterIP   10.105.30.25     <none>        9090/TCP,9000/TCP         8m23s
     service/demo-pingaccess-admin-cluster ClusterIP   None             <none>        <none>                    8m23s
     service/demo-pingaccess-engine        ClusterIP   10.100.1.136     <none>        3000/TCP                  8m23s
     service/demo-pingauthorize            ClusterIP   10.101.98.228    <none>        443/TCP                   8m23s
     service/demo-pingauthorize-cluster    ClusterIP   None             <none>        1636/TCP                  8m23s
     service/demo-pingdataconsole          ClusterIP   10.103.181.27    <none>        8443/TCP                  8m23s
     service/demo-pingdirectory            ClusterIP   10.106.174.162   <none>        443/TCP,389/TCP,636/TCP   8m23s
     service/demo-pingdirectory-cluster    ClusterIP   None             <none>        1636/TCP                  8m23s
     service/demo-pingfederate-admin       ClusterIP   10.96.52.217     <none>        9999/TCP                  8m23s
     service/demo-pingfederate-cluster     ClusterIP   None             <none>        7600/TCP,7700/TCP         8m23s
     service/demo-pingfederate-engine      ClusterIP   10.103.84.196    <none>        9031/TCP                  8m23s
     ```

     ```shell
     NAME                                       READY   UP-TO-DATE   AVAILABLE   AGE
     deployment.apps/demo-pingaccess-engine     1/1     1            1           8m23s
     deployment.apps/demo-pingauthorize         1/1     1            1           8m23s
     deployment.apps/demo-pingdataconsole       1/1     1            1           8m23s
     deployment.apps/demo-pingfederate-admin    1/1     1            1           8m23s
     deployment.apps/demo-pingfederate-engine   1/1     1            1           8m23s
     ```

     ```shell
     NAME                                                 DESIRED   CURRENT   READY   AGE
     replicaset.apps/demo-pingaccess-engine-59cfb85b9d    1         1         1       8m23s
     replicaset.apps/demo-pingauthorize-5696dd6b67        1         1         1       8m23s
     replicaset.apps/demo-pingdataconsole-56b75f9ffb      1         1         1       8m23s
     replicaset.apps/demo-pingfederate-admin-67cdb47bb4   1         1         1       8m23s
     replicaset.apps/demo-pingfederate-engine-d9889b494   1         1         1       8m23s
     ```

     ```shell
     NAME                                     READY   AGE
     statefulset.apps/demo-pingaccess-admin   1/1     8m23s
     statefulset.apps/demo-pingdirectory      1/1     8m23s
     ```

   * To view logs, look at the logs for the deployment of the product in question. For example:

     ```shell
     kubectl logs -f deployment/demo-pingfederate-admin
     ```

     1. These are the URLs and credentials to sign on to the management consoles for the products.

        |   |                                                                                                                     |
        | - | ------------------------------------------------------------------------------------------------------------------- |
        |   | This example uses self-signed certificates that will have to be accepted in your browser or added to your keystore. |

        With the ingresses in place, you can access the products at these URLs:

        | Product                                                                           | Connection Details                                                                                                                                                       |
        | --------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
        | [PingFederate](https://demo-pingfederate-admin.pingdemo.example/pingfederate/app) | * URL: <https://demo-pingfederate-admin.pingdemo.example/pingfederate/app>

        * Username: administrator

        * Password: 2FederateM0re                                         |
        | [PingDirectory](https://demo-pingdataconsole.pingdemo.example/console)            | - URL: <https://demo-pingdataconsole.pingdemo.example/console>

        - Server: ldaps\://demo-pingdirectory-cluster:1636

        - Username: administrator

        - Password: 2FederateM0re |
        | [PingAccess](https://demo-pingaccess-admin.pingdemo.example/)                     | * URL: <https://demo-pingaccess-admin.pingdemo.example/>

        * Username: administrator

        * Password: 2FederateM0re                                                           |
        | [PingAuthorize](https://demo-pingdataconsole.pingdemo.example/console)            | - URL: <https://demo-pingdataconsole.pingdemo.example/console>

        - Server: ldaps\://demo-pingauthorize-cluster:1636

        - Username: administrator

        - Password: 2FederateM0re |

     2. When you are finished, you can remove the demonstration components by running the uninstall command for helm:

        ```shell
        helm uninstall demo
        ```

### Next Steps

Now that you have deployed a set of our product images using the provided chart, you can move on to deployments using configurations that more closely reflect use cases to be explored. Refer to [Helm Chart Examples](https://developer.pingidentity.com/helm/examples/index.html) for other typical deployments.

|   |                                                                                                                                                                                  |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Maintaining logs in a containerized model is different from the typical server-deployed application. See [this page](../reference/containerLogging.html) for additional details. |
