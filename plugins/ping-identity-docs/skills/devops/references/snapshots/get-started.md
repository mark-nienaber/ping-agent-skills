---
title: Deploy an Example Stack
description: Deploy an example Ping Identity product stack to a Kubernetes cluster with Helm using the Traefik ingress controller
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

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | This example was written using Docker Desktop on the Mac platform using the Apple Silicon chip, with Kubernetes provided by the Docker Desktop `kind` implementation in a multi-node configuration. Results would be similar under Docker Desktop's default Kubernetes implementation. The Docker Desktop version used for this guide was `4.96.3 (244472)`, which includes Docker Engine `v29.9.2` and Kubernetes `v1.35.1`. Helm version `4.3.1` was used to deploy the Ping Identity Helm chart `0.16.0` (product images `2609`). The traefik ingress controller version was `v3.7.16`, deployed from Helm chart version `42.1.3`. |

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | If you are new to Kubernetes-based deployments, there is a distinct difference when running under Kubernetes compared to running applications on servers. In a server model, many applications typically run on the same server, and you can access any of them using the same host. For example, many on-premise deployments of PingFederate also include the PingDataConsole, hosted on the same server.Under Kubernetes, however, each application that requires external access is associated with a `service`. A service is a fixed endpoint in the cluster that routes traffic to a given application. So, in this example, there are distinct service endpoints for PingFederate, PingDataConsole, and the other products.In this demo, these service endpoints are load balanced using the Traefik ingress controller. By adding entries to the `/etc/hosts` file, you can access them using typical URL entries. |

The Ping Identity Helm [Getting Started](https://helm.pingidentity.com/getting-started/) page has instructions on getting your environment configured for using the Ping Helm charts.

For more examples, see [Helm Chart Example Configurations](https://developer.pingidentity.com/helm/examples/index.html).

For more information on Helm with Ping products, see [Ping Identity DevOps Helm Charts](https://helm.pingidentity.com).

## What You Will Do

After using Git to clone the `pingidentity-devops-getting-started` repository, you will use Helm to deploy a sample stack to a Kubernetes cluster.

## Prerequisites

* Register for the Ping DevOps program and set your DevOps User and Key as environment variables

* Install [Git](https://git-scm.com/downloads)

* Follow the instructions on the helm [Getting Started](https://helm.pingidentity.com/getting-started/) page up through updating to the latest charts to ensure you have the latest version of our charts

* Access to a Kubernetes cluster. You can enable Kubernetes in Docker Desktop for a simple cluster (on the Mac platform), which is the cluster used for this guide.

## Clone the `getting-started` repository

1. Clone the `pingidentity-devops-getting-started` repository to your local `${PING_IDENTITY_DEVOPS_HOME}` directory.

   |   |                                                                                                              |
   | - | ------------------------------------------------------------------------------------------------------------ |
   |   | **The `${PING_IDENTITY_DEVOPS_HOME}` environment variable points to your DevOps projects parent directory.** |

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
   LAST DEPLOYED: Fri Oct 23 15:16:57 2026
   NAMESPACE: pinghelm
   STATUS: deployed
   REVISION: 1
   DESCRIPTION: Install complete
   TEST SUITE: None
   NOTES:
   #-------------------------------------------------------------------------------------
   # Ping DevOps
   #
   # Description: Ping Identity helm charts - October 2, 2026
   #-------------------------------------------------------------------------------------
   #
   #           Product          tag   typ  #  cpu R/L   mem R/L  Ing
   #    --------------------- ------- --- -- --------- --------- ---
   #    global                2609              0/0       0/0     √
   #
   #  √ pingaccess-admin      2609    sts  1    0/2     1Gi/4Gi   √
   #  √ pingaccess-engine     2609    dep  1    0/2     1Gi/4Gi   √
   #  √ pingauthorize         2609    dep  1    0/2    1.5G/4Gi   √
   #    pingauthorizepap
   #    pingcentral
   #  √ pingdataconsole       2609    dep  1    0/2    .5Gi/2Gi   √
   #    pingdatasync
   #    pingdelegator
   #  √ pingdirectory         2609    sts  1  50m/2     2Gi/8Gi   √
   #    pingdirectoryproxy
   #  √ pingfederate-admin    2609    dep  1    0/2     1Gi/4Gi   √
   #  √ pingfederate-engine   2609    dep  1    0/2     1Gi/4Gi   √
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
     NAME                            TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)                   AGE
     demo-pingaccess-admin           ClusterIP   10.96.23.229    <none>        9090/TCP,9000/TCP         4m20s
     demo-pingaccess-admin-cluster   ClusterIP   None            <none>        <none>                    4m20s
     demo-pingaccess-engine          ClusterIP   10.96.53.209    <none>        3000/TCP                  4m20s
     demo-pingauthorize              ClusterIP   10.96.109.172   <none>        443/TCP                   4m20s
     demo-pingauthorize-cluster      ClusterIP   None            <none>        1636/TCP                  4m20s
     demo-pingdataconsole            ClusterIP   10.96.158.114   <none>        8443/TCP                  4m20s
     demo-pingdirectory              ClusterIP   10.96.245.124   <none>        443/TCP,389/TCP,636/TCP   4m20s
     demo-pingdirectory-cluster      ClusterIP   None            <none>        1636/TCP                  4m20s
     demo-pingfederate-admin         ClusterIP   10.96.252.14    <none>        9999/TCP                  4m20s
     demo-pingfederate-cluster       ClusterIP   None            <none>        7600/TCP,7700/TCP         4m20s
     demo-pingfederate-engine        ClusterIP   10.96.207.25    <none>        9031/TCP                  4m20s
     ```

   * To view the pods, run `kubectl get pods --selector=app.kubernetes.io/instance=demo` - you will need to run this at intervals until all pods have started (** Running **status):

     ```shell
     NAME                                       READY   STATUS    RESTARTS   AGE
     demo-pingaccess-admin-0                    1/1     Running   0          4m20s
     demo-pingaccess-engine-78f75b56d6-w7k6w    1/1     Running   0          4m20s
     demo-pingauthorize-58f9f76fcb-gsdb6        1/1     Running   0          4m20s
     demo-pingdataconsole-66cc557887-l9b7x      1/1     Running   0          4m20s
     demo-pingdirectory-0                       1/1     Running   0          4m20s
     demo-pingfederate-admin-6c658cf4b7-2f6x6   1/1     Running   0          4m20s
     demo-pingfederate-engine-8d6f8cfd4-7klbf   1/1     Running   0          4m20s
     ```

   * To see the ingresses you will use to access the product, run `kubectl get ingress`. If the ingress controller is configured properly, you should see the ingress address populated as shown here (`localhost` under Docker Desktop's default Kubernetes implementation, or the ingress controller pod IP under the `kind` implementation):

     ```shell
     NAME                       CLASS     HOSTS                                       ADDRESS     PORTS     AGE
     demo-pingaccess-admin      traefik     demo-pingaccess-admin.pingdemo.example      172.19.0.7   80, 443   4m20s
     demo-pingaccess-engine     traefik     demo-pingaccess-engine.pingdemo.example     172.19.0.7   80, 443   4m20s
     demo-pingauthorize         traefik     demo-pingauthorize.pingdemo.example         172.19.0.7   80, 443   4m20s
     demo-pingdataconsole       traefik     demo-pingdataconsole.pingdemo.example       172.19.0.7   80, 443   4m20s
     demo-pingdirectory         traefik     demo-pingdirectory.pingdemo.example         172.19.0.7   80, 443   4m20s
     demo-pingfederate-admin    traefik     demo-pingfederate-admin.pingdemo.example    172.19.0.7   80, 443   4m20s
     demo-pingfederate-engine   traefik     demo-pingfederate-engine.pingdemo.example   172.19.0.7   80, 443   4m20s
     ```

   * To see everything tied to the helm release run `kubectl get all --selector=app.kubernetes.io/instance=demo`:

     ```shell
     NAME                                           READY   STATUS    RESTARTS   AGE
     pod/demo-pingaccess-admin-0                    1/1     Running   0          4m21s
     pod/demo-pingaccess-engine-78f75b56d6-w7k6w    1/1     Running   0          4m21s
     pod/demo-pingauthorize-58f9f76fcb-gsdb6        1/1     Running   0          4m21s
     pod/demo-pingdataconsole-66cc557887-l9b7x      1/1     Running   0          4m21s
     pod/demo-pingdirectory-0                       1/1     Running   0          4m21s
     pod/demo-pingfederate-admin-6c658cf4b7-2f6x6   1/1     Running   0          4m21s
     pod/demo-pingfederate-engine-8d6f8cfd4-7klbf   1/1     Running   0          4m21s
     ```

     ```shell
     NAME                                  TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)                   AGE
     service/demo-pingaccess-admin         ClusterIP   10.96.23.229    <none>        9090/TCP,9000/TCP         4m21s
     service/demo-pingaccess-admin-cluster ClusterIP   None            <none>        <none>                    4m21s
     service/demo-pingaccess-engine        ClusterIP   10.96.53.209    <none>        3000/TCP                  4m21s
     service/demo-pingauthorize            ClusterIP   10.96.109.172   <none>        443/TCP                   4m21s
     service/demo-pingauthorize-cluster    ClusterIP   None            <none>        1636/TCP                  4m21s
     service/demo-pingdataconsole          ClusterIP   10.96.158.114   <none>        8443/TCP                  4m21s
     service/demo-pingdirectory            ClusterIP   10.96.245.124   <none>        443/TCP,389/TCP,636/TCP   4m21s
     service/demo-pingdirectory-cluster    ClusterIP   None            <none>        1636/TCP                  4m21s
     service/demo-pingfederate-admin       ClusterIP   10.96.252.14    <none>        9999/TCP                  4m21s
     service/demo-pingfederate-cluster     ClusterIP   None            <none>        7600/TCP,7700/TCP         4m21s
     service/demo-pingfederate-engine      ClusterIP   10.96.207.25    <none>        9031/TCP                  4m21s
     ```

     ```shell
     NAME                                       READY   UP-TO-DATE   AVAILABLE   AGE
     deployment.apps/demo-pingaccess-engine     1/1     1            1           4m21s
     deployment.apps/demo-pingauthorize         1/1     1            1           4m21s
     deployment.apps/demo-pingdataconsole       1/1     1            1           4m21s
     deployment.apps/demo-pingfederate-admin    1/1     1            1           4m21s
     deployment.apps/demo-pingfederate-engine   1/1     1            1           4m21s
     ```

     ```shell
     NAME                                                 DESIRED   CURRENT   READY   AGE
     replicaset.apps/demo-pingaccess-engine-78f75b56d6    1         1         1       4m21s
     replicaset.apps/demo-pingauthorize-58f9f76fcb        1         1         1       4m21s
     replicaset.apps/demo-pingdataconsole-66cc557887      1         1         1       4m21s
     replicaset.apps/demo-pingfederate-admin-6c658cf4b7   1         1         1       4m21s
     replicaset.apps/demo-pingfederate-engine-8d6f8cfd4   1         1         1       4m21s
     ```

     ```shell
     NAME                                     READY   AGE
     statefulset.apps/demo-pingaccess-admin   1/1     4m21s
     statefulset.apps/demo-pingdirectory      1/1     4m21s
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

---

---
title: Deploy an Example Stack with Gateway API
description: Deploy an example Ping Identity product stack to a Kubernetes cluster with Helm using Gateway API and Traefik as the gateway controller
component: devops
page_id: devops::get-started/getStartedExampleGateway
canonical_url: https://developer.pingidentity.com/devops/get-started/getStartedExampleGateway.html
llms_txt: https://developer.pingidentity.com/devops/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  devops-what-you-will-do: What You Will Do
  devops-prerequisites: Prerequisites
  devops-clone-the-repository: Clone the getting-started repository
  devops-deploy-the-example-stack: Deploy the example stack
  devops-next-steps: Next Steps
  devops-gateway-access-caveats: Gateway Access Caveats for Local Clusters
---

# Deploy an Example Stack with Gateway API

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | This example was written using Docker Desktop on the Mac platform using the Apple Silicon chip, with Kubernetes provided by the Docker Desktop `kind` implementation in a multi-node configuration. Results would be similar under Docker Desktop's default Kubernetes implementation. The Docker Desktop version used for this guide was `4.96.3 (244472)`, which includes Docker Engine `v29.9.2` and Kubernetes `v1.35.1`. The walkthrough uses Gateway API `v1.5.0` (installed separately, as described below), Traefik chart version `39.0.9` (Traefik `v3.6.15`) as the Gateway controller, and the latest ping-devops Helm chart at the time of this writing, `0.16.0` (product images `2609`). Helm version `4.3.1` was used. |

The Ping Identity Helm [Getting Started](https://helm.pingidentity.com/getting-started/) page has instructions on getting your environment configured for using the Ping ping-devops Helm charts.

For more examples, see [Helm Chart Example Configurations](https://developer.pingidentity.com/helm/examples/index.html).

For more information on Helm with Ping products, see [Ping Identity DevOps Helm Charts](https://helm.pingidentity.com).

## What You Will Do

After using Git to clone the `pingidentity-devops-getting-started` repository, you will use Helm to deploy a sample stack to a Kubernetes cluster.

## Prerequisites

* Register for the Ping DevOps program and set your DevOps User and Key as environment variables

* Install [Git](https://git-scm.com/downloads)

* Follow the instructions on the helm [Getting Started](https://helm.pingidentity.com/getting-started/) page up through updating to the latest charts to ensure you have the latest version of our charts

* Access to a Kubernetes cluster. You can enable Kubernetes in Docker Desktop for a simple cluster (on the Mac platform), which is the cluster used for this guide.

## Clone the `getting-started` repository

1. Clone the `pingidentity-devops-getting-started` repository to your local `${PING_IDENTITY_DEVOPS_HOME}` directory.

   |   |                                                                                                          |
   | - | -------------------------------------------------------------------------------------------------------- |
   |   | The `${PING_IDENTITY_DEVOPS_HOME}` environment variable points to your DevOps projects parent directory. |

   ```shell
   cd "${PING_IDENTITY_DEVOPS_HOME}"
   git clone https://github.com/pingidentity/pingidentity-devops-getting-started.git
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

      |   |                                                                                                                                                                                                                                                                                                                                                                                 |
      | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
      |   | Recent Traefik chart versions (including the `39.0.x` series used in this guide) bundle the Gateway API CRDs at version 1.4.0, and newer chart versions no longer bundle them at all. To ensure a predictable, current Gateway API version, this guide installs the CRDs standalone first and then deploys Traefik with `--skip-crds` to avoid conflicts with the bundled CRDs. |

   2. Install the Gateway API CRDs:

      ```shell
      kubectl apply -f https://github.com/kubernetes-sigs/gateway-api/releases/download/v1.5.0/standard-install.yaml
      ```

   3. Deploy Traefik with Gateway API support:

      ```shell
      cd <repository-root>/30-helm/

      # If necessary, add the Traefik Helm repository and update to get the latest charts:
      helm repo add traefik https://traefik.github.io/charts

      helm repo update traefik

      # Install Traefik. Chart 39.0.x (Traefik v3.6.x) is pinned here because
      # Traefik v3.7.x does not correctly forward Gateway API traffic to the
      # backends (requests fail with 5xx errors).
      helm upgrade --install traefik traefik/traefik \
          --version 39.0.9 \
          --namespace traefik --create-namespace \
          -f gateway/traefik-values.yaml \
          --skip-crds
      ```

|   |                                                                                                                                                                                                                                                   |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The values file used to configure Traefik in this deployment example is configured to skip backend TLS verification so the Ping product consoles with self-signed certificates will work with Traefik. **Do not use this setting in production.** |

1. To wait for Traefik to reach a healthy state, run the following command. You can also observe pod status using `k9s`. You should see one controller pod running when Traefik is ready:

   ```shell
   kubectl get pods --namespace traefik
   ```

2. Create a wildcard TLS certificate and Kubernetes secret for the Gateway listener:

   ```shell
   openssl req -x509 -newkey rsa:2048 -sha256 -nodes -days 365 \
     -subj '/CN=*.pingdemo.example' \
     -addext 'subjectAltName=DNS:*.pingdemo.example' \
     -keyout /tmp/pingdemo-example.key \
     -out /tmp/pingdemo-example.crt

   kubectl create secret tls pingdemo-example-tls \
     --namespace pinghelm \
     --cert /tmp/pingdemo-example.crt \
     --key /tmp/pingdemo-example.key \
     --dry-run=client -o yaml | kubectl apply -f -
   ```

3. Create the Gateway object and wait for it to be accepted and programmed:

   ```shell
   kubectl apply -f gateway/gateway.yaml
   kubectl wait --for=condition=Accepted gateway/ping-devops-gateway -n pinghelm --timeout=180s
   kubectl wait --for=condition=Programmed gateway/ping-devops-gateway -n pinghelm --timeout=180s
   kubectl get gateway -n pinghelm
   ```

4. Create a secret in the namespace you will be using to run the example (pinghelm). This secret provides credentials to obtain an evaluation license based on your Ping DevOps username and key:

   ```shell
   kubectl create secret generic devops-secret \
     --from-literal=PING_IDENTITY_DEVOPS_USER="$PING_IDENTITY_DEVOPS_USER" \
     --from-literal=PING_IDENTITY_DEVOPS_KEY="$PING_IDENTITY_DEVOPS_KEY" \
     --from-literal=PING_IDENTITY_ACCEPT_EULA="$PING_IDENTITY_ACCEPT_EULA" \
     --type=Opaque \
     --dry-run=client -o yaml | kubectl apply -f -
   ```

5. This example will use the Helm release name `demo` and DNS domain suffix `*pingdemo.example` for accessing applications. Add all expected hosts to `/etc/hosts`:

   ```shell
   echo '127.0.0.1 demo-pingaccess-admin.pingdemo.example demo-pingaccess-engine.pingdemo.example demo-pingauthorize.pingdemo.example demo-pingauthorizepap.pingdemo.example demo-pingdataconsole.pingdemo.example demo-pingdelegator.pingdemo.example demo-pingdirectory.pingdemo.example demo-pingfederate-admin.pingdemo.example demo-pingfederate-engine.pingdemo.example demo-pingcentral.pingdemo.example' | sudo tee -a /etc/hosts > /dev/null
   ```

6. To install the chart, navigate to your local `"${PING_IDENTITY_DEVOPS_HOME}"/pingidentity-devops-getting-started/30-helm` directory and run the command shown here. In this example, the release (deployment into Kubernetes by Helm) is called `demo`, forming the prefix for all objects created. The `gateway/gateway-demo.yaml` file configures Gateway API `HTTPRoute` resources for the products:

   |   |                                                                                                                                                                                                                                  |
   | - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | This walkthrough requires chart version `0.12.0` or later to ensure the necessary Gateway API resources support is included in the deployment. The output below reflects the latest chart available at the time of this writing. |

   ```shell
   # If necessary, add the Ping Identity Helm repository and update to get the latest charts:
   helm repo add pingidentity https://helm.pingidentity.com/
   helm repo update pingidentity

   helm upgrade --install demo pingidentity/ping-devops \
     --namespace pinghelm \
     -f everything.yaml \
     -f gateway/gateway-demo.yaml
   ```

   The latest product Docker images are automatically downloaded if they have not previously been pulled from [Docker Hub](https://hub.docker.com/u/pingidentity/).

   Sample output:

   ```shell
   NAME: demo
   LAST DEPLOYED: Fri Oct 23 15:41:40 2026
   NAMESPACE: pinghelm
   STATUS: deployed
   REVISION: 1
   DESCRIPTION: Install complete
   TEST SUITE: None
   NOTES:
   #-------------------------------------------------------------------------------------
   # Ping DevOps
   #
   # Description: Ping Identity helm charts - October 2, 2026
   #-------------------------------------------------------------------------------------
   #
   #           Product          tag   typ  #  cpu R/L   mem R/L  Ing
   #    --------------------- ------- --- -- --------- --------- ---
   #    global                2609              0/0       0/0     √
   #
   #  √ pingaccess-admin      2609    sts  1    0/2     1Gi/4Gi   √
   #  √ pingaccess-engine     2609    dep  1    0/2     1Gi/4Gi   √
   #  √ pingauthorize         2609    dep  1    0/2    1.5G/4Gi   √
   #    pingauthorizepap
   #    pingcentral
   #  √ pingdataconsole       2609    dep  1    0/2    .5Gi/2Gi   √
   #    pingdatasync
   #    pingdelegator
   #  √ pingdirectory         2609    sts  1  50m/2     2Gi/8Gi   √
   #    pingdirectoryproxy
   #  √ pingfederate-admin    2609    dep  1    0/2     1Gi/4Gi   √
   #  √ pingfederate-engine   2609    dep  1    0/2     1Gi/4Gi   √
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

7. To see the Gateway and HTTPRoute resources created by the chart, run the following command:

   ```shell
   kubectl get gateway,httproute -n pinghelm
   ```

   Sample output:

   ```shell
   NAME                                                    CLASS     ADDRESS      PROGRAMMED   AGE
   gateway.gateway.networking.k8s.io/ping-devops-gateway   traefik   172.19.0.7   True         5m16s

   NAME                                                           HOSTNAMES                                       AGE
   httproute.gateway.networking.k8s.io/demo-pingaccess-admin      ["demo-pingaccess-admin.pingdemo.example"]      5m12s
   httproute.gateway.networking.k8s.io/demo-pingaccess-engine     ["demo-pingaccess-engine.pingdemo.example"]     5m12s
   httproute.gateway.networking.k8s.io/demo-pingauthorize         ["demo-pingauthorize.pingdemo.example"]         5m12s
   httproute.gateway.networking.k8s.io/demo-pingdataconsole       ["demo-pingdataconsole.pingdemo.example"]       5m12s
   httproute.gateway.networking.k8s.io/demo-pingdirectory         ["demo-pingdirectory.pingdemo.example"]         5m12s
   httproute.gateway.networking.k8s.io/demo-pingfederate-admin    ["demo-pingfederate-admin.pingdemo.example"]    5m12s
   httproute.gateway.networking.k8s.io/demo-pingfederate-engine   ["demo-pingfederate-engine.pingdemo.example"]   5m12s
   ```

8. To see the status conditions for the Gateway and HTTPRoutes, run:

   ```shell
   kubectl get httproute -n pinghelm -o yaml | grep -E 'type: Accepted|type: ResolvedRefs'
   ```

   Sample output:

   ```shell
           type: Accepted
           type: ResolvedRefs
           type: Accepted
           type: ResolvedRefs
           type: Accepted
           type: ResolvedRefs
           type: Accepted
           type: ResolvedRefs
           type: Accepted
           type: ResolvedRefs
           type: Accepted
           type: ResolvedRefs
           type: Accepted
           type: ResolvedRefs
           type: Accepted
           type: ResolvedRefs
           type: Accepted
           type: ResolvedRefs
           type: Accepted
           type: ResolvedRefs
           type: Accepted
           type: ResolvedRefs
           type: Accepted
           type: ResolvedRefs
           type: Accepted
           type: ResolvedRefs
           type: Accepted
           type: ResolvedRefs
   ```

   Each of these are the `Accepted` and `ResolvedRefs` conditions for the HTTPRoutes created for the products. If you see any `status: "False"` conditions, that indicates an issue with the route that needs to be resolved before proceeding.

9. To display the status of the deployed components, you can use [k9s](https://k9scli.io/) or issue the corresponding commands shown here:

   * Display the services (endpoints for connecting) by running `kubectl get service --selector=app.kubernetes.io/instance=demo`

     ```shell
     NAME                            TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)                   AGE
     demo-pingaccess-admin           ClusterIP   10.96.101.206   <none>        9090/TCP,9000/TCP         5m13s
     demo-pingaccess-admin-cluster   ClusterIP   None            <none>        <none>                    5m13s
     demo-pingaccess-engine          ClusterIP   10.96.48.98     <none>        3000/TCP                  5m13s
     demo-pingauthorize              ClusterIP   10.96.219.56    <none>        443/TCP                   5m13s
     demo-pingauthorize-cluster      ClusterIP   None            <none>        1636/TCP                  5m13s
     demo-pingdataconsole            ClusterIP   10.96.205.157   <none>        8443/TCP                  5m13s
     demo-pingdirectory              ClusterIP   10.96.81.43     <none>        443/TCP,389/TCP,636/TCP   5m13s
     demo-pingdirectory-cluster      ClusterIP   None            <none>        1636/TCP                  5m13s
     demo-pingfederate-admin         ClusterIP   10.96.34.105    <none>        9999/TCP                  5m13s
     demo-pingfederate-cluster       ClusterIP   None            <none>        7600/TCP,7700/TCP         5m13s
     demo-pingfederate-engine        ClusterIP   10.96.237.88    <none>        9031/TCP                  5m13s
     ```

   * To view the pods, run `kubectl get pods --selector=app.kubernetes.io/instance=demo` - you will need to run this at intervals until all pods have started (** Running **status):

     ```shell
     NAME                                       READY   STATUS    RESTARTS   AGE
     demo-pingaccess-admin-0                    1/1     Running   0          5m13s
     demo-pingaccess-engine-88cd7bdbc-cvgpx     1/1     Running   0          5m13s
     demo-pingauthorize-596cff7f86-x2w99        1/1     Running   0          5m13s
     demo-pingdataconsole-6bfdcf9c66-vvxg5      1/1     Running   0          5m13s
     demo-pingdirectory-0                       1/1     Running   0          5m13s
     demo-pingfederate-admin-594c8f5d4d-2wswc   1/1     Running   0          5m13s
     demo-pingfederate-engine-55b9d7bb47-pbpmb  1/1     Running   0          5m13s
     ```

   * To see the Gateway and HTTPRoutes you will use to access the products, run `kubectl get gateway,httproute -n pinghelm`:

     ```shell
     NAME                                                    CLASS     ADDRESS      PROGRAMMED   AGE
     gateway.gateway.networking.k8s.io/ping-devops-gateway   traefik   172.19.0.7   True         5m16s

     NAME                                                           HOSTNAMES                                       AGE
     httproute.gateway.networking.k8s.io/demo-pingaccess-admin      ["demo-pingaccess-admin.pingdemo.example"]      5m12s
     httproute.gateway.networking.k8s.io/demo-pingaccess-engine     ["demo-pingaccess-engine.pingdemo.example"]     5m12s
     httproute.gateway.networking.k8s.io/demo-pingauthorize         ["demo-pingauthorize.pingdemo.example"]         5m12s
     httproute.gateway.networking.k8s.io/demo-pingdataconsole       ["demo-pingdataconsole.pingdemo.example"]       5m12s
     httproute.gateway.networking.k8s.io/demo-pingdirectory         ["demo-pingdirectory.pingdemo.example"]         5m12s
     httproute.gateway.networking.k8s.io/demo-pingfederate-admin    ["demo-pingfederate-admin.pingdemo.example"]    5m12s
     httproute.gateway.networking.k8s.io/demo-pingfederate-engine   ["demo-pingfederate-engine.pingdemo.example"]   5m12s
     ```

   * To check route status conditions, run:

     ```shell
     kubectl get gateway,httproute -n pinghelm
     kubectl get httproute -n pinghelm -o yaml | grep -E 'type: Accepted|type: ResolvedRefs|status: "False"'
     ```

     Expected output:

     * `ping-devops-gateway` shows `Programmed=True`

     * HTTPRoutes are created for enabled products

     * Each route shows `Accepted=True` and `ResolvedRefs=True`

   * To validate console endpoint reachability, run the following. If you had to use portforwarding or a tunnel, see the [Gateway Access Caveats for Local Clusters](#devops-gateway-access-caveats) section below and adjust the URLs accordingly:

     ```shell
     for u in \
       https://demo-pingfederate-admin.pingdemo.example/pingfederate/app \
       https://demo-pingaccess-admin.pingdemo.example/ \
       https://demo-pingdataconsole.pingdemo.example/console; do
       curl -k -sS -o /dev/null -w "%{http_code} ${u}\n" -L "$u"
     done
     ```

     Example output:

     ```shell
     200 https://demo-pingfederate-admin.pingdemo.example/pingfederate/app
     200 https://demo-pingaccess-admin.pingdemo.example/
     200 https://demo-pingdataconsole.pingdemo.example/console/index.html
     ```

   * To see everything tied to the helm release run `kubectl get all --selector=app.kubernetes.io/instance=demo`:

     ```shell
     NAME                                            READY   STATUS    RESTARTS   AGE
     pod/demo-pingaccess-admin-0                     1/1     Running   0          5m13s
     pod/demo-pingaccess-engine-88cd7bdbc-cvgpx      1/1     Running   0          5m13s
     pod/demo-pingauthorize-596cff7f86-x2w99         1/1     Running   0          5m13s
     pod/demo-pingdataconsole-6bfdcf9c66-vvxg5       1/1     Running   0          5m13s
     pod/demo-pingdirectory-0                        1/1     Running   0          5m13s
     pod/demo-pingfederate-admin-594c8f5d4d-2wswc    1/1     Running   0          5m13s
     pod/demo-pingfederate-engine-55b9d7bb47-pbpmb   1/1     Running   0          5m13s
     ```

     ```shell
     NAME                                    TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)                   AGE
     service/demo-pingaccess-admin           ClusterIP   10.96.101.206   <none>        9090/TCP,9000/TCP         5m13s
     service/demo-pingaccess-admin-cluster   ClusterIP   None            <none>        <none>                    5m13s
     service/demo-pingaccess-engine          ClusterIP   10.96.48.98     <none>        3000/TCP                  5m13s
     service/demo-pingauthorize              ClusterIP   10.96.219.56    <none>        443/TCP                   5m13s
     service/demo-pingauthorize-cluster      ClusterIP   None            <none>        1636/TCP                  5m13s
     service/demo-pingdataconsole            ClusterIP   10.96.205.157   <none>        8443/TCP                  5m13s
     service/demo-pingdirectory              ClusterIP   10.96.81.43     <none>        443/TCP,389/TCP,636/TCP   5m13s
     service/demo-pingdirectory-cluster      ClusterIP   None            <none>        1636/TCP                  5m13s
     service/demo-pingfederate-admin         ClusterIP   10.96.34.105    <none>        9999/TCP                  5m13s
     service/demo-pingfederate-cluster       ClusterIP   None            <none>        7600/TCP,7700/TCP         5m13s
     service/demo-pingfederate-engine        ClusterIP   10.96.237.88    <none>        9031/TCP                  5m13s
     ```

     ```shell
     NAME                                       READY   UP-TO-DATE   AVAILABLE   AGE
     deployment.apps/demo-pingaccess-engine     1/1     1            1           5m13s
     deployment.apps/demo-pingauthorize         1/1     1            1           5m13s
     deployment.apps/demo-pingdataconsole       1/1     1            1           5m13s
     deployment.apps/demo-pingfederate-admin    1/1     1            1           5m13s
     deployment.apps/demo-pingfederate-engine   1/1     1            1           5m13s
     ```

     ```shell
     NAME                                                  DESIRED   CURRENT   READY   AGE
     replicaset.apps/demo-pingaccess-engine-88cd7bdbc      1         1         1       5m13s
     replicaset.apps/demo-pingauthorize-596cff7f86         1         1         1       5m13s
     replicaset.apps/demo-pingdataconsole-6bfdcf9c66       1         1         1       5m13s
     replicaset.apps/demo-pingfederate-admin-594c8f5d4d    1         1         1       5m13s
     replicaset.apps/demo-pingfederate-engine-55b9d7bb47   1         1         1       5m13s
     ```

     ```shell
     NAME                                     READY   AGE
     statefulset.apps/demo-pingaccess-admin   1/1     5m13s
     statefulset.apps/demo-pingdirectory      1/1     5m13s
     ```

   * To view logs, look at the logs for the deployment of the product in question. For example:

     ```shell
     kubectl logs -f deployment/demo-pingfederate-admin
     ```

     1. This table contains the URLs and credentials to sign on to the management consoles for the products.

        |   |                                                                                                                     |
        | - | ------------------------------------------------------------------------------------------------------------------- |
        |   | This example uses self-signed certificates that will have to be accepted in your browser or added to your keystore. |

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

### Gateway Access Caveats for Local Clusters

If your local cluster does not provide a working `LoadBalancer` external address for the Traefik service, use one of the following alternatives.

* Option 1: NodePort service type for Traefik

  ```shell
  helm upgrade --install traefik traefik/traefik \
    --version 39.0.9 \
    --namespace traefik --create-namespace \
    -f gateway/traefik-values.yaml \
    -f gateway/traefik-values-nodeport.yaml \
    --skip-crds
  ```

  If using this option, provide port `30443` in the URLs (for example, `https://demo-pingfederate-admin.pingdemo.example:30443/pingfederate/app`).

* Option 2: ClusterIP service type with local port-forwarding

  ```shell
  helm upgrade --install traefik traefik/traefik \
    --version 39.0.9 \
    --namespace traefik --create-namespace \
    -f gateway/traefik-values.yaml \
    -f gateway/traefik-values-clusterip.yaml \
    --skip-crds

  # Non-privileged port-forward for local testing
  kubectl -n traefik port-forward svc/traefik 8443:443

  # Or keep standard :443 URLs
  sudo kubectl -n traefik port-forward svc/traefik 443:443
  ```

---

---
title: Introduction
description: Get an overview of deploying Ping products with predefined configurations, plus required DevOps registration and PingOne Worker App setup
component: devops
page_id: devops::get-started/introduction
canonical_url: https://developer.pingidentity.com/devops/get-started/introduction.html
llms_txt: https://developer.pingidentity.com/devops/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
---

# Introduction

This section outlines ways to easily deploy Ping products with pre-defined configurations. After you have successfully deployed using this example, you can try other provided examples or move on to customizing the products to fit your needs and environment.

You will need to [register for the Ping DevOps program](../how-to/devopsRegistration.html) in order to obtain trial licenses for evaluating or testing with our products.

After registering at the link above, you will be provided a username and key. These credentials provide a temporary license for your evaluation. See [using your DevOps User and Key](../how-to/devopsUserKey.html) for instructions on use.

Finally, to manage PingOne resources using credentials other than your own, a PingOne Worker App is required. See [this configuration page](../reference/pingone-config.html) for more details on configuration.

---

---
title: Prerequisites
description: Review the license, local runtime environment, and utility prerequisites needed before deploying Ping product containers
component: devops
page_id: devops::get-started/prereqs
canonical_url: https://developer.pingidentity.com/devops/get-started/prereqs.html
llms_txt: https://developer.pingidentity.com/devops/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  devops-product-license: Product license
  evaluation-license: Evaluation License
  devops-existing-license: Existing License
  devops-local-runtime-environment: Local runtime environment
  devops-applications-utilities: Applications / Utilities
  devops-configure-the-environment: Configure the Environment
---

# Prerequisites

In order to use our resources, you will need the following components, software, or other information.

## Product license

You must have a product license to run our images. You may either use an evaluation license or existing license.

### Evaluation License

Generate an evaluation license obtained with a [valid DevOps user key](../how-to/devopsRegistration.html).

When you register for Ping Identity's DevOps program, you are issued credentials that automate the process of retrieving an evaluation product license.

|   |                                                                                                                                                                                                                                |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | For more information about using your DevOps program user and key in various ways (including Kubernetes and with stand-alone containers) see this how-to guide: [Using Your Devops User and Key](../how-to/devopsUserKey.html) |

|   |                                                                                                   |
| - | ------------------------------------------------------------------------------------------------- |
|   | Evaluation licenses are short-lived (30 days) and **must not** be used in production deployments. |

Evaluation licenses can only be used with images published in the last 90 days. If you want to continue to use an image that was published more than 90 days ago, you must obtain a product license.

### Existing License

If you possess a product license for the product, you can use it with supported versions of the image (including those over 90 days old mentioned above) by following these instructions to [mount the product license](../how-to/existingLicense.html).

|   |                                                                                                                                      |
| - | ------------------------------------------------------------------------------------------------------------------------------------ |
|   | The mount points and name of the license file vary by product. The link above provides the proper location and name for these files. |

## Local runtime environment

The initial example uses Kubernetes under Docker Desktop because it does not require a lot of configuration.

In order to try Ping products in a manner most similar to typical production installations, you should consider using a Kubernetes environment. [Kind](https://kind.sigs.k8s.io/) (**K**ubernetes **in** **D**ocker) provides a platform to get started with local Kubernetes development. Instructions for setting up a Kind cluster are [here](../deployment/deployLocalK8sCluster.html).

Other local Kubernetes environments include [Rancher Desktop](https://rancherdesktop.io), [Docker Desktop](https://www.docker.com/products/docker-desktop/) with Kubernetes enabled, and [minikube](https://minikube.sigs.k8s.io/docs/).

|   |                                                                                                                                                                                                                                                                                                                |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Rancher Desktop is compatible with Linux, MacOS, and Windows (using WSL). It also supports the [docker container runtime](https://docs.rancherdesktop.io/preferences#container-runtime), which provides support for running docker commands without installing individual docker components or Docker Desktop. |

For running Docker Compose deployments of single products, any Docker Desktop installation or Linux system with Docker and `docker compose` installed can be used.

## Applications / Utilities

* [Helm](https://helm.sh/docs/intro/install/) cli

* [kubectl](https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands)

* [Homebrew](https://brew.sh) for package installation and management. Homebrew can be used to install k9s, kubectl, helm, and other programs.

  ```shell
    /bin/bash -c "$(curl -fsSL +https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
  ```

  \== Recommended Additional Utilities

* [k9s](https://k9scli.io/)

  ```shell
    brew install derailed/k9s/k9s
  ```

* [kubectx](https://github.com/ahmetb/kubectx)

  ```shell
    brew install kubectx
  ```

* [docker-compose](https://docs.docker.com/compose/install/)

  ```shell
    brew install docker-compose
  ```

  |   |                                                                                                                                                                      |
  | - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | Installing docker-compose is only necessary to deploy Docker containers when using Docker with Rancher Desktop. It is included with the Docker Desktop installation. |

  See [Rancher preferences](https://docs.rancherdesktop.io/preferences#container-runtime) to switch from containerd to dockerd (moby).

## Configure the Environment

1. Open a terminal and create a local DevOps directory named `${HOME}/projects/devops`.

   |   |                                                                                                   |
   | - | ------------------------------------------------------------------------------------------------- |
   |   | ${HOME}/projects/devops is the parent directory for all examples referenced in our documentation. |

2. Set your DevOps User and Key as environment variables so the containers can retrieve evaluation licenses. For more information, see [DevOps Registration](../how-to/devopsRegistration.html).

   ```shell
   export PING_IDENTITY_DEVOPS_USER=<devops-user>
   export PING_IDENTITY_DEVOPS_KEY=<devops-key>
   export PING_IDENTITY_ACCEPT_EULA=YES
   ```

   ```
   Add these statements to your shell profile (for example, `~/.bash_profile` in a bash shell) so they persist across sessions.
   ```

3. Verify the variables are exported in your environment. Restart your shell or source your shell profile, then run:

   ```shell
     env | grep 'PING'
   ```

4. If you saved your DevOps credentials in the `~/.pingidentity/config` property file (created by earlier Ping Identity DevOps tooling), you can load them into your environment by sourcing the file from your shell profile.