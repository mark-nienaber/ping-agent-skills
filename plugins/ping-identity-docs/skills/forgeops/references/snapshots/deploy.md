---
title: Deploy using Helm on GKE, EKS, or AKS
description: In a development or demo environment, you can use the Helm chart available locally in /path/to/forgeops/charts directory for performing ForgeOps deployment. In a production environment, it's highly recommended to use the Helm charts published on the registry.
component: forgeops
version: 2026.2
page_id: forgeops:deploy:deploy-scenario-helm-cloud
canonical_url: https://docs.pingidentity.com/forgeops/2026.2/deploy/deploy-scenario-helm-cloud.html
llms_txt: https://docs.pingidentity.com/forgeops/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Prometheus", "Grafana", "Alertmanager", "Helm"]
section_ids:
  next_step: Next step
---

# Deploy using Helm on GKE, EKS, or AKS

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | * In a development or demo environment, you can use the Helm chart available locally in /path/to/forgeops/charts directory for performing ForgeOps deployment. In a production environment, it's highly recommended to use the Helm charts published on the registry.

* The default ForgeOps deployment provides a self-signed certificate that has a very limited use even in demo environments. You must use a certificate obtained from a certificate authority for use in your environment. You can use the [Add custom certificates](../prepare/security/secrets-rotation.html#add-cust-cert) procedure.

* The current ForgeOps deployments on GKE, AKS, and EKS use Traefik as the default ingress controller. You can continue to use NGINX, but note that Kubernetes has stopped the support for ingress-nginx controller, so we strongly recommend you use Traefik for new deployments.

* On minikube, ForgeOps deployments continues to use the ingress-nginx addon provided by minikube. |

1. Verify you've set up your environment and created a Kubernetes cluster as documented in the [setup section](../setup/overview.html).

2. Use the terminal where you have already activated Python3 virtual environment. If you haven't already done so, activate the virtual environment in a new terminal window:

   ```
   $ source .venv/bin/activate
   ```

3. Verify your ForgeOps version:

   ```
   $ cd /path/to/forgeops
   $ ./bin/forgeops version
   ```

4. The configuration of a ForgeOps deployment is steered through the use of Kustomize overlays or Helm values. Use the forgeops env command to set up the Kustomize overlays and Helm values files to configure your ForgeOps deployment environment:

   * If you want to use the issuer provided with the platform for demo, then you can use default-issuer.

   * For a clusters on a cloud environment specify the --deployment-size as `--small`, `--medium`, or `--large`.

   * For a single-instance deployment, specify --deployment-size as `--single-instance`.

     ```
     $ cd /path/to/forgeops/bin
     $ ./forgeops env --env-name my-env --fqdn my-fqdn.example.com --cluster-issuer my-cluster-issuer --deployment-size
     ```

     In the command above, replace my-fqdn.example.com, my-cluster-issuer, and --deployment-size with appropriate values from your environment.

     Learn more about deployment sizes in [Cluster and deployment sizes](architecture.html#cluster-and-deployment-sizes) and about single instances [here](architecture.html#single-inst).

5. Ensure that the `image.repository` and `image.tag` are correctly specified in the Helm values file (/path/to/forgeops/helm/my-env/values.yaml) in your ForgeOps deployment environment.

   In your production environment, use the forgeops image command to select the latest available platform image corresponding to the major ForgeOps release, and not necessarily the latest image available from ForgeOps. This documentation uses images as latest from ForgeOps as default for demo and learning purposes. Using images tagged as latest from ForgeOps directly in your production environment can result in unintended upgrades.

   Learn more about setting and using ForgeOps platform image version tags [here](https://github.com/ForgeRock/forgeops/blob/main/how-tos/manage-platform-images.md).

   Learn more about customizing ForgeOps platform images [here](../customize/overview.html).

6. Use the forgeops image command to set up the correct component image versions to be deployed:

   ```
   $ cd /path/to/forgeops/bin
   $ ./forgeops image --release my-image --env-name my-env platform
   ```

7. Set up your Kubernetes context:

   1. Set the `KUBECONFIG` environment variable so that your Kubernetes context references the cluster in which you'll perform the ForgeOps deployment.

   2. Create a Kubernetes namespace in the cluster for the Ping Advanced Identity Software pods:

      ```
      $ kubectl create namespace my-namespace
      ```

   3. Set the active namespace in your Kubernetes context to the Kubernetes namespace you just created:

      ```
      $ kubens my-namespace
      ```

8. Set up the certificate and secret management prerequisites:

   |   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
   | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
   |   | 1. The `forgeops` utility uses `cert-manager` as the certificate management utility. If you need to use a different certificate management utility, refer to the corresponding documentation for installing that utility. You can disable `cert-manager` for ingresses in your ForgeOps deployment environment using the --ingress-no-cert-manager option of the forgeops env command:

      ```
      $ forgeops env --env-name my-env --ingress-no-cert-manager
      ```

   2. Currently, `secret-agent` is used as the default secrets management utility in ForgeOps deployments. You can continue to use the secret agent in existing deployments.

   3. ForgeOps artifacts include alternatives for ingress (Traefik or `ha-proxy`).

      The forgeops prereqs command provides a corresponding `--` option to select the component you want to use. The `--` option isn't available for components, such as `cert-manager`, for which an alternative isn't provided.

      A few examples of the forgeops prereqs command are provided in the [`forgeops prereqs` command reference](../reference/forgeops-cmd-ref.html#prereqs-examples).

   4. Versions 1.2.9 and 1.2.10 of `secret-agent` have a flaw that causes the `secret-agent` operator to crash when it tries to access the Kubernetes API. If you are using `secret-agent`, **avoid `secret-agent` versions 1.2.9 and 1.2.10; upgrade to version 1.2.11**. |

   1. To install all prereqs including `secret-agent` for secret management:

      ```
      $ forgeops prereqs
      ```

9. (Optional) If you've set up your Kubernetes cluster using ForgeOps provided Terraform manifest, then you would have already created the required `fast` storage and volume snapshot classes. If you are setting your Kubernetes cluster using your own scripts, then create these classes using corresponding YAML scripts provided in the /path/to/forgeops/etc/resources folder.

   For example, on GKE:

   ```
   $ kubectl apply -f /path/to/forgeops/etc/resources/gke-fast-storage-class.yaml
   $ kubectl apply -f /path/to/forgeops/etc/resources/gke-volume-snapshot-class.yaml
   ```

10. Run the helm upgrade command to perform a ForgeOps deployment:

    ```
    $ helm upgrade --install identity-platform  identity-platform \
     --repo https://ForgeRock.github.io/forgeops/ \
     --version 2026.2 --namespace my-namespace \
     --values /path/to/forgeops/helm/my-env/values.yaml
    ```

    When deploying the platform with Docker images other than the ForgeOps-provided images, you'll also need to set additional Helm values such as `am.image.repository`, `am.image.tag`, `idm.image.repository`, and `idm.image.tag`. For an example, refer to [Redeploy AM: Helm deployments](../customize/am.html#redeploy-am-helm).

    |   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
    | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
    |   | Ping Identity only offers its software or services to legal entities that have entered into a binding license agreement with Ping Identity. When you install Docker images provided by ForgeOps, you agree either that: 1) you are an authorized user of a Ping Advanced Identity Software customer that has entered into a license agreement with Ping Identity governing your use of the Ping Identity software; or 2) your use of the Ping Advanced Identity Software is subject to the [Ping Identity Subscription Agreements](https://www.pingidentity.com/en/legal/subscription-agreement.html). |

11. Check the status of the pods in the namespace in which you deployed the platform until all the pods are ready:

    1. Run the kubectl get pods command.

    2. Review the output. Deployment is complete when:

       * All entries in the `STATUS` column indicate `Running` or `Completed`.

       * The `READY` column indicates all running containers are available. The entry in the `READY` column represents \[total number of containers/number of available containers].

    3. If necessary, continue to query your deployment's status until all the pods are ready.

12. Back up and save the Kubernetes secrets that contain the master and TLS keys:

    1. To avoid accidentally putting the backups under version control, change to a directory that is outside your `forgeops` repository clone.

    2. The `ds-master-keypair` secret contains the DS master key. This key is required to decrypt data from a directory backup. *Failure to save this key could result in data loss.*

       Back up the Kubernetes secret that contains the DS master key:

       ```
       $ kubectl get secret ds-master-keypair -o yaml > master-key-pair.yaml
       ```

    3. The `ds-ssl-keypair` secret contains the DS TLS key. This key is needed for cross-environment replication topologies.

       Back up the Kubernetes secret that contains the DS TLS key pair:

       ```
       $ kubectl get secret ds-ssl-keypair -o yaml > tls-key-pair.yaml
       ```

    4. Save the two backup files.

13. (Optional) Deploy Prometheus, Grafana, and Alertmanager for monitoring and alerting\[[1](#_footnotedef_1 "View footnote.")]:

    1. Deploy Prometheus, Grafana, and Alertmanager pods in your ForgeOps deployment:

       ```
       $ /path/to/forgeops/bin/prometheus-deploy.sh

       **This script requires Helm version 3.04 or later due to changes in the behaviour of 'helm repo add' command.**

       namespace/monitoring created
       "stable" has been added to your repositories
       "prometheus-community" has been added to your repositories
       Hang tight while we grab the latest from your chart repositories...
       ...
       Update Complete. ⎈Happy Helming!⎈
       Release "prometheus-operator" does not exist. Installing it now.
       NAME: prometheus-operator
       LAST DEPLOYED: ...
       NAMESPACE: monitoring
       STATUS: deployed
       REVISION: 1
       NOTES:
       kube-prometheus-stack has been installed. Check its status by running:
         kubectl --namespace monitoring get pods -l "release=prometheus-operator"

       Visit https://github.com/prometheus-operator/kube-prometheus for instructions
       on how to create & configure Alertmanager and Prometheus instances using the Operator.
       ...
       Release "forgerock-metrics" does not exist. Installing it now.
       NAME: forgerock-metrics
       LAST DEPLOYED: ...
       NAMESPACE: monitoring
       STATUS: deployed
       REVISION: 1
       TEST SUITE: None
       ```

    2. Check the status of the pods in the `monitoring` namespace until all the pods are ready:

       ```
       $ kubectl get pods --namespace monitoring
       NAME                                                     READY   STATUS    RESTARTS   AGE
       alertmanager-prometheus-operator-kube-p-alertmanager-0   2/2     Running   0          119s
       prometheus-operator-grafana-95b8f5b7d-nn65h              3/3     Running   0          2m4s
       prometheus-operator-kube-p-operator-7d54989595-pdj44     1/1     Running   0          2m4s
       prometheus-operator-kube-state-metrics-d95996bc4-wcf7s   1/1     Running   0          2m4s
       prometheus-operator-prometheus-node-exporter-67xq4       1/1     Running   0          2m4s
       prometheus-operator-prometheus-node-exporter-b4grn       1/1     Running   0          2m4s
       prometheus-operator-prometheus-node-exporter-cwhcn       1/1     Running   0          2m4s
       prometheus-operator-prometheus-node-exporter-h9brd       1/1     Running   0          2m4s
       prometheus-operator-prometheus-node-exporter-q8zrk       1/1     Running   0          2m4s
       prometheus-operator-prometheus-node-exporter-vqpt5       1/1     Running   0          2m4s
       prometheus-prometheus-operator-kube-p-prometheus-0       2/2     Running   0          119s
       ```

14. (Optional) Install a TLS certificate instead of using the default self-signed certificate in your ForgeOps deployment. Refer to [TLS certificate](../prepare/security/https.html#tls-certificate) for details.

## Next step

* [icon: check-square-o, set=fa][Become familiar with ForgeOps deployments](overview.html)

* [icon: check-square-o, set=fa][Understand ForgeOps architecture](architecture.html)

* [icon: check-square-o, set=fa][Deploy the platform](deploy.html)

* [icon: square-o, set=fa]*[Access platform UIs and APIs](access.html)*

* [icon: square-o, set=fa][Plan for production deployment](next-steps.html)

***

[1](#_footnoteref_1). Installing Prometheus, Grafana, and Alertmanager technology in ForgeOps deployments provides an example of how you might set up monitoring and alerting in a Ping Advanced Identity Software deployment in the cloud. Remember, [ForgeOps deployments are reference implementations.](../start/start-here.html#cdm-sandbox) When you [create a project plan](../start/start-here.html#planning), you'll need to determine how to monitor and send alerts in your production deployment.

---

---
title: Deploy using Helm on minikube
description: In a development or demo environment, you can use the Helm chart available locally in /path/to/forgeops/charts directory for performing ForgeOps deployment. In a production environment, it's highly recommended to use the Helm charts published on the registry.
component: forgeops
version: 2026.2
page_id: forgeops:deploy:deploy-scenario-helm-local
canonical_url: https://docs.pingidentity.com/forgeops/2026.2/deploy/deploy-scenario-helm-local.html
llms_txt: https://docs.pingidentity.com/forgeops/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Helm", "minikube"]
section_ids:
  next_step: Next step
---

# Deploy using Helm on minikube

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | * In a development or demo environment, you can use the Helm chart available locally in /path/to/forgeops/charts directory for performing ForgeOps deployment. In a production environment, it's highly recommended to use the Helm charts published on the registry.

* The default ForgeOps deployment provides a self-signed certificate that has a very limited use even in demo environments. You must use a certificate obtained from a certificate authority for use in your environment. You can use the [Add custom certificates](../prepare/security/secrets-rotation.html#add-cust-cert) procedure.

* The current ForgeOps deployments on GKE, AKS, and EKS use Traefik as the default ingress controller. You can continue to use NGINX, but note that Kubernetes has stopped the support for ingress-nginx controller, so we strongly recommend you use Traefik for new deployments.

* On minikube, ForgeOps deployments continues to use the ingress-nginx addon provided by minikube. |

1. Verify you've set up your environment and created a Kubernetes cluster as documented in the [setup section](../setup/overview.html).

2. Use the terminal where you have already activated Python3 virtual environment. If you haven't already done so, activate the virtual environment in a new terminal window:

   ```
   $ source .venv/bin/activate
   ```

3. Verify your ForgeOps version:

   ```
   $ cd /path/to/forgeops
   $ ./bin/forgeops version
   ```

4. The configuration of a ForgeOps deployment is steered through the use of Kustomize overlays or Helm values. Use the forgeops env command to set up the Kustomize overlays and Helm values files to configure your ForgeOps deployment environment:

5. In a minikube, set up the default cluster issuer\[[1](#_footnotedef_1 "View footnote.")]. For example:

   ```
   $ kubectl apply -f /path/to/forgeops/etc/resources/selfsigned-issuer.yaml
   ```

6. In minikube, set up a single instance deployment environment. For example:

   ```
   $ cd /path/to/forgeops/bin
   $ ./forgeops env --env-name my-env --fqdn my-fqdn.example.com \
     --cluster-issuer my-cluster-issuer --single-instance
   ```

   In the command above, replace my-fqdn.example.com and my-cluster-issuer with appropriate values from your environment.

   Learn more about deployment sizes in [Cluster and deployment sizes](architecture.html#cluster-and-deployment-sizes) and about single instances [here](architecture.html#single-inst).

7. Ensure that the `image.repository` and `image.tag` are correctly specified in the Helm values file (/path/to/forgeops/helm/my-env/values.yaml) in your ForgeOps deployment environment.

   In your production environment, use the forgeops image command to select the latest available platform image corresponding to the major ForgeOps release, and not necessarily the latest image available from ForgeOps. This documentation uses images as latest from ForgeOps as default for demo and learning purposes. Using images tagged as latest from ForgeOps directly in your production environment can result in unintended upgrades.

   Learn more about setting and using ForgeOps platform image version tags [here](https://github.com/ForgeRock/forgeops/blob/main/how-tos/manage-platform-images.md).

   Learn more about customizing ForgeOps platform images [here](../customize/overview.html).

8. Use the forgeops image command to set up the correct component image versions to be deployed:

   ```
   $ cd /path/to/forgeops/bin
   $ ./forgeops image --release my-image --env-name my-env platform
   ```

9. Set up your Kubernetes context:

   1. Create a Kubernetes namespace in the cluster for the Ping Advanced Identity Software pods:

      ```
      $ kubectl create namespace my-namespace
      ```

   2. Set the active namespace in your Kubernetes context to the Kubernetes namespace you just created:

      ```
      $ kubens my-namespace
      ```

10. Set up the certificate management and secret agent.

    |   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
    | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
    |   | 1) Because minikube provides its own ingress controller, there's no need to install another ingress controller.1. The `forgeops` utility uses `cert-manager` as the certificate management utility. If you need to use a different certificate management utility, refer to the corresponding documentation for installing that utility. You can disable `cert-manager` for ingresses in your ForgeOps deployment environment using the --ingress-no-cert-manager option of the forgeops env command:

       ```
       $ forgeops env --env-name my-env --ingress-no-cert-manager
       ```

    2. Currently, `secret-agent` is used as the default secrets management utility in ForgeOps deployments. You can continue to use the secret agent in existing deployments.

    3. ForgeOps artifacts include alternatives for ingress (Traefik or `ha-proxy`).

       The forgeops prereqs command provides a corresponding `--` option to select the component you want to use. The `--` option isn't available for components, such as `cert-manager`, for which an alternative isn't provided.

       A few examples of the forgeops prereqs command are provided in the [`forgeops prereqs` command reference](../reference/forgeops-cmd-ref.html#prereqs-examples).

    4. Versions 1.2.9 and 1.2.10 of `secret-agent` have a flaw that causes the `secret-agent` operator to crash when it tries to access the Kubernetes API. If you are using `secret-agent`, **avoid `secret-agent` versions 1.2.9 and 1.2.10; upgrade to version 1.2.11**. |

    1. To install the secret agent for secret management:

       ```
       $ forgeops prereqs cert-manager secrets
       ```

11. In a separate terminal tab or window, run the minikube tunnel command, and enter your system's superuser password when prompted:

    ```
    $ minikube tunnel
    ✅  Tunnel successfully started

    📌  NOTE: Please do not close this terminal as this process must stay alive for the tunnel to be accessible …​

    ❗  ...
    Password:
    ```

    The tunnel creates networking that lets you access the minikube cluster's ingress on the localhost IP address (127.0.0.1). Leave the tab or window that started the tunnel open for as long as you run the ForgeOps deployment.

    Refer to [this post](https://stackoverflow.com/questions/70961901/ingress-with-minikube-working-differently-on-mac-vs-ubuntu-when-to-set-etc-host) for an explanation about why a minikube tunnel is required to access ingress resources when running minikube on an ARM-based macOS system.

12. Set up the `fast` storage class using the `minikube-fast-storage-class.yaml` file in the /path/to/forgeops/etc/resources directory:

    ```
    $ kubectl apply -f /path/to/forgeops/etc/resources/minikube-fast-storage-class.yaml
    ```

13. Enable secret agent in your deployment environment:

    ```
    $ forgeops env --env-name my-env --namespace my-namespace  --secret-agent
    ```

14. Run the helm upgrade command to perform a ForgeOps deployment:

    ```
    $ helm upgrade --install identity-platform identity-platform \
     --repo https://ForgeRock.github.io/forgeops/ \
     --namespace my-namespace \
     --values /path/to/forgeops/helm/my-env/values.yaml
    ```

    The preceding command creates a single-instance ForgeOps deployment. Only single-instance deployments are supported on minikube.

    Learn more about single-instance deployments in [Cluster and deployment sizes](architecture.html#cluster-and-deployment-sizes).

    |   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
    | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
    |   | Ping Identity only offers its software or services to legal entities that have entered into a binding license agreement with Ping Identity. When you install Docker images provided by ForgeOps, you agree either that: 1) you are an authorized user of a Ping Advanced Identity Software customer that has entered into a license agreement with Ping Identity governing your use of the Ping Identity software; or 2) your use of the Ping Advanced Identity Software is subject to the [Ping Identity Subscription Agreements](https://www.pingidentity.com/en/legal/subscription-agreement.html). |

15. Check the status of the pods in the namespace in which you deployed the platform until all the pods are ready:

    1. Run the kubectl get pods command.

    2. Review the output. Deployment is complete when:

       * All entries in the `STATUS` column indicate `Running` or `Completed`.

       * The `READY` column indicates all running containers are available. The entry in the `READY` column represents \[total number of containers/number of available containers].

    3. If necessary, continue to query your deployment's status until all the pods are ready.

16. (Optional) Install a TLS certificate instead of using the default self-signed certificate in your ForgeOps deployment. Refer to [TLS certificate](../prepare/security/https.html#tls-certificate) for details.

## Next step

* [icon: check-square-o, set=fa][Become familiar with ForgeOps deployments](overview.html)

* [icon: check-square-o, set=fa][Understand ForgeOps architecture](architecture.html)

* [icon: check-square-o, set=fa][Deploy the platform](deploy.html)

* [icon: square-o, set=fa]*[Access platform UIs and APIs](access.html)*

* [icon: square-o, set=fa][Plan for production deployment](next-steps.html)

***

[1](#_footnoteref_1). You can use the self-signed issuer provided by ForgeOps for test purposes. For production environments, ForgeOps recommends using a cluster issuer that uses a certificate from a trusted certificate authority (CA).

---

---
title: Deploy using Kustomize on GKE, EKS, or AKS
description: In a development or demo environment, you can use the Helm chart available locally in /path/to/forgeops/charts directory for performing ForgeOps deployment. In a production environment, it's highly recommended to use the Helm charts published on the registry.
component: forgeops
version: 2026.2
page_id: forgeops:deploy:deploy-scenario-kustomize-cloud
canonical_url: https://docs.pingidentity.com/forgeops/2026.2/deploy/deploy-scenario-kustomize-cloud.html
llms_txt: https://docs.pingidentity.com/forgeops/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["forgeops Command", "Prometheus", "Grafana", "Alertmanager"]
section_ids:
  alt-techniques-kustomize-cloud: Alternative deployment techniques when using Kustomize
  staged_deployments: Staged deployments
  generating_kustomize_manifests_and_using_kubectl_apply_commands: Generating Kustomize manifests and using kubectl apply commands
  next_step: Next step
---

# Deploy using Kustomize on GKE, EKS, or AKS

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | * In a development or demo environment, you can use the Helm chart available locally in /path/to/forgeops/charts directory for performing ForgeOps deployment. In a production environment, it's highly recommended to use the Helm charts published on the registry.

* The default ForgeOps deployment provides a self-signed certificate that has a very limited use even in demo environments. You must use a certificate obtained from a certificate authority for use in your environment. You can use the [Add custom certificates](../prepare/security/secrets-rotation.html#add-cust-cert) procedure.

* The current ForgeOps deployments on GKE, AKS, and EKS use Traefik as the default ingress controller. You can continue to use NGINX, but note that Kubernetes has stopped the support for ingress-nginx controller, so we strongly recommend you use Traefik for new deployments.

* On minikube, ForgeOps deployments continues to use the ingress-nginx addon provided by minikube. |

1. Verify you've set up your environment and created a Kubernetes cluster as documented in the [setup section](../setup/overview.html).

2. Use the terminal where you have already activated Python3 virtual environment. If you haven't already done so, activate the virtual environment in a new terminal window:

   ```
   $ source .venv/bin/activate
   ```

3. Verify your ForgeOps version:

   ```
   $ cd /path/to/forgeops
   $ ./bin/forgeops version
   ```

4. The configuration of a ForgeOps deployment is steered through the use of Kustomize overlays or Helm values. Use the forgeops env command to set up the Kustomize overlays and Helm values files to configure your ForgeOps deployment environment:

   * If you want to use the issuer provided with the platform for demo, then you can use default-issuer.

   * For a clusters on a cloud environment specify the --deployment-size as `--small`, `--medium`, or `--large`.

   * For a single-instance deployment, specify --deployment-size as `--single-instance`.

     ```
     $ cd /path/to/forgeops/bin
     $ ./forgeops env --env-name my-env --fqdn my-fqdn.example.com --cluster-issuer my-cluster-issuer --deployment-size
     ```

     In the command above, replace my-fqdn.example.com, my-cluster-issuer, and --deployment-size with appropriate values from your environment.

     Learn more about deployment sizes in [Cluster and deployment sizes](architecture.html#cluster-and-deployment-sizes) and about single instances [here](architecture.html#single-inst).

5. Ensure that the `image.repository` and `image.tag` are correctly specified in the image defaulter file in your ForgeOps deployment environment. The image defaulter file is located at /path/to/forgeops/kustomize/deploy/image-defaulter/kustomization.yaml.

   In your production environment, use the forgeops image command to select the latest available platform image corresponding to the major ForgeOps release, and not necessarily the latest image available from ForgeOps. This documentation uses images tagged as latest from ForgeOps as default for demo and learning purposes. Using images tagged as latest from ForgeOps directly in your production environment can result in unintended upgrades.

   Learn more about customizing ForgeOps platform images [here](../customize/overview.html).

   If you want to use ForgeOps-provided Docker images for the platform, don't modify the image defaulter file. The following command sets up the latest ForgeOps-provided Docker image for the 8.1.0:

   ```
   $ cd /path/to/forgeops/bin
   $ ./forgeops image --env-name my-env --release 8.1.0 platform
   ```

   |   |                                                                                                                                                                                                                                                                                                                                                                         |
   | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | To set up your deployment environment with your customized image, use the following example command:```
   $ cd /path/to/forgeops/bin
   $ ./forgeops image --release my-image --release-name my-release --env-name my-env platform
   ```You can get the image names and tags from the image defaulter file on the system on which the customized Docker images were developed. |

6. Set up your Kubernetes context:

   1. Set the `KUBECONFIG` environment variable so that your Kubernetes context references the cluster in which you'll perform the ForgeOps deployment.

   2. Create a Kubernetes namespace in the cluster for the Ping Advanced Identity Software pods:

      ```
      $ kubectl create namespace my-namespace
      ```

   3. Set the active namespace in your Kubernetes context to the Kubernetes namespace you just created:

      ```
      $ kubens my-namespace
      ```

7. Set up the certificate management, secret agent, and Traefik:

   |   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
   | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
   |   | 1. The `forgeops` utility uses `cert-manager` as the certificate management utility. If you need to use a different certificate management utility, refer to the corresponding documentation for installing that utility. You can disable `cert-manager` for ingresses in your ForgeOps deployment environment using the --ingress-no-cert-manager option of the forgeops env command:

      ```
      $ forgeops env --env-name my-env --ingress-no-cert-manager
      ```

   2. Currently, `secret-agent` is used as the default secrets management utility in ForgeOps deployments. You can continue to use the secret agent in existing deployments.

   3. ForgeOps artifacts include alternatives for ingress (Traefik or `ha-proxy`).

      The forgeops prereqs command provides a corresponding `--` option to select the component you want to use. The `--` option isn't available for components, such as `cert-manager`, for which an alternative isn't provided.

      A few examples of the forgeops prereqs command are provided in the [`forgeops prereqs` command reference](../reference/forgeops-cmd-ref.html#prereqs-examples).

   4. Versions 1.2.9 and 1.2.10 of `secret-agent` have a flaw that causes the `secret-agent` operator to crash when it tries to access the Kubernetes API. If you are using `secret-agent`, **avoid `secret-agent` versions 1.2.9 and 1.2.10; upgrade to version 1.2.11**. |

   1. To install all prereqs including `secret-agent` for secret management:

      ```
      $ forgeops prereqs
      ```

8. (Optional) If you've set up your Kubernetes cluster using ForgeOps provided Terraform manifest, then you would have already created the required `fast` storage and volume snapshot classes. If you are setting your Kubernetes cluster using your own scripts, then create these classes using corresponding YAML scripts provided in the /path/to/forgeops/etc/resources folder.

   For example, on GKE:

   ```
   $ kubectl apply -f /path/to/forgeops/etc/resources/gke-fast-storage-class.yaml
   $ kubectl apply -f /path/to/forgeops/etc/resources/gke-volume-snapshot-class.yaml
   ```

9. Run the forgeops apply command to perform a ForgeOps deployment. Learn more in [`forgeops apply` command reference](../reference/forgeops-cmd-ref.html#forgeops-apply).

   For example:

   ```
   $ cd /path/to/forgeops/bin
   $ ./forgeops apply --env-name my-env
   ```

   If you prefer not to deploy using a single forgeops apply command, you can find more information in [Alternative deployment techniques when using Kustomize](#alt-techniques-kustomize-cloud).

   |   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
   | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
   |   | Ping Identity only offers its software or services to legal entities that have entered into a binding license agreement with Ping Identity. When you install Docker images provided by ForgeOps, you agree either that: 1) you are an authorized user of a Ping Advanced Identity Software customer that has entered into a license agreement with Ping Identity governing your use of the Ping Identity software; or 2) your use of the Ping Advanced Identity Software is subject to the [Ping Identity Subscription Agreements](https://www.pingidentity.com/en/legal/subscription-agreement.html). |

10. Check the status of the pods in the namespace in which you deployed the platform until all the pods are ready:

    1. Run the kubectl get pods command.

    2. Review the output. Deployment is complete when:

       * All entries in the `STATUS` column indicate `Running` or `Completed`.

       * The `READY` column indicates all running containers are available. The entry in the `READY` column represents \[total number of containers/number of available containers].

    3. If necessary, continue to query your deployment's status until all the pods are ready.

11. Back up and save the Kubernetes secrets that contain the master and TLS keys:

    1. To avoid accidentally putting the backups under version control, change to a directory that is outside your `forgeops` repository clone.

    2. The `ds-master-keypair` secret contains the DS master key. This key is required to decrypt data from a directory backup. *Failure to save this key could result in data loss.*

       Back up the Kubernetes secret that contains the DS master key:

       ```
       $ kubectl get secret ds-master-keypair -o yaml > master-key-pair.yaml
       ```

    3. The `ds-ssl-keypair` secret contains the DS TLS key. This key is needed for cross-environment replication topologies.

       Back up the Kubernetes secret that contains the DS TLS key pair:

       ```
       $ kubectl get secret ds-ssl-keypair -o yaml > tls-key-pair.yaml
       ```

    4. Save the two backup files.

12. (Optional) Deploy Prometheus, Grafana, and Alertmanager for monitoring and alerting\[[1](#_footnotedef_1 "View footnote.")]:

    1. Deploy Prometheus, Grafana, and Alertmanager pods in your ForgeOps deployment:

       ```
       $ /path/to/forgeops/bin/prometheus-deploy.sh

       **This script requires Helm version 3.04 or later due to changes in the behaviour of 'helm repo add' command.**

       namespace/monitoring created
       "stable" has been added to your repositories
       "prometheus-community" has been added to your repositories
       Hang tight while we grab the latest from your chart repositories...
       ...
       Update Complete. ⎈Happy Helming!⎈
       Release "prometheus-operator" does not exist. Installing it now.
       NAME: prometheus-operator
       LAST DEPLOYED: ...
       NAMESPACE: monitoring
       STATUS: deployed
       REVISION: 1
       NOTES:
       kube-prometheus-stack has been installed. Check its status by running:
         kubectl --namespace monitoring get pods -l "release=prometheus-operator"

       Visit https://github.com/prometheus-operator/kube-prometheus for instructions
       on how to create & configure Alertmanager and Prometheus instances using the Operator.
       ...
       Release "forgerock-metrics" does not exist. Installing it now.
       NAME: forgerock-metrics
       LAST DEPLOYED: ...
       NAMESPACE: monitoring
       STATUS: deployed
       REVISION: 1
       TEST SUITE: None
       ```

    2. Check the status of the pods in the `monitoring` namespace until all the pods are ready:

       ```
       $ kubectl get pods --namespace monitoring
       NAME                                                     READY   STATUS    RESTARTS   AGE
       alertmanager-prometheus-operator-kube-p-alertmanager-0   2/2     Running   0          119s
       prometheus-operator-grafana-95b8f5b7d-nn65h              3/3     Running   0          2m4s
       prometheus-operator-kube-p-operator-7d54989595-pdj44     1/1     Running   0          2m4s
       prometheus-operator-kube-state-metrics-d95996bc4-wcf7s   1/1     Running   0          2m4s
       prometheus-operator-prometheus-node-exporter-67xq4       1/1     Running   0          2m4s
       prometheus-operator-prometheus-node-exporter-b4grn       1/1     Running   0          2m4s
       prometheus-operator-prometheus-node-exporter-cwhcn       1/1     Running   0          2m4s
       prometheus-operator-prometheus-node-exporter-h9brd       1/1     Running   0          2m4s
       prometheus-operator-prometheus-node-exporter-q8zrk       1/1     Running   0          2m4s
       prometheus-operator-prometheus-node-exporter-vqpt5       1/1     Running   0          2m4s
       prometheus-prometheus-operator-kube-p-prometheus-0       2/2     Running   0          119s
       ```

13. (Optional) Install a TLS certificate instead of using the default self-signed certificate in your ForgeOps deployment. Refer to [TLS certificate](../prepare/security/https.html#tls-certificate) for details.

## Alternative deployment techniques when using Kustomize

### Staged deployments

If you prefer not to perform a ForgeOps Kustomize deployment using a single forgeops apply command, you can deploy the platform in stages, [component by component](../troubleshoot/staged-deployment.html), instead of deploying with a single command. Staging deployments can be useful if you need to troubleshoot a deployment issue.

### Generating Kustomize manifests and using `kubectl apply` commands

You can generate Kustomize manifests using the forgeops env command, and then deploy the platform using the kubectl apply -k command.

The forgeops env command generates Kustomize manifests for your ForgeOps deployment environment. The manifests are written to the /path/to/forgeops/kustomize/overlay/my-env directory of your `forgeops` repository clone. Advanced users who prefer to work directly with Kustomize manifests that describe their ForgeOps deployment can use the generated content in the kustomize/overlay/my-env directory as an alternative to using the forgeops command:

1. Generate an initial set of Kustomize manifests by running the forgeops env command.

2. Run kubectl apply -k commands to deploy and remove platform components. Specify a manifest in the kustomize/overlay/my-env directory as an argument when you run kubectl apply -k commands.

   1. Use GitOps to manage configuration changes to the kustomize/overlay/my-env directory.

## Next step

* [icon: check-square-o, set=fa][Become familiar with ForgeOps deployments](overview.html)

* [icon: check-square-o, set=fa][Understand ForgeOps architecture](architecture.html)

* [icon: check-square-o, set=fa][Deploy the platform](deploy.html)

* [icon: square-o, set=fa]*[Access platform UIs and APIs](access.html)*

* [icon: square-o, set=fa][Plan for production deployment](next-steps.html)

***

[1](#_footnoteref_1). Installing Prometheus, Grafana, and Alertmanager technology in ForgeOps deployments provides an example of how you might set up monitoring and alerting in a Ping Advanced Identity Software deployment in the cloud. Remember, [ForgeOps deployments are reference implementations.](../start/start-here.html#cdm-sandbox) When you [create a project plan](../start/start-here.html#planning), you'll need to determine how to monitor and send alerts in your production deployment.

---

---
title: Deploy using Kustomize on minikube
description: In a development or demo environment, you can use the Helm chart available locally in /path/to/forgeops/charts directory for performing ForgeOps deployment. In a production environment, it's highly recommended to use the Helm charts published on the registry.
component: forgeops
version: 2026.2
page_id: forgeops:deploy:deploy-scenario-kustomize-local
canonical_url: https://docs.pingidentity.com/forgeops/2026.2/deploy/deploy-scenario-kustomize-local.html
llms_txt: https://docs.pingidentity.com/forgeops/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["forgeops Command"]
section_ids:
  alt-techniques-kustomize-local: Alternative deployment techniques when using Kustomize
  staged_deployments: Staged deployments
  generating_kustomize_manifests_and_using_kubectl_apply_commands: Generating Kustomize manifests and using kubectl apply commands
  next_step: Next step
---

# Deploy using Kustomize on minikube

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | * In a development or demo environment, you can use the Helm chart available locally in /path/to/forgeops/charts directory for performing ForgeOps deployment. In a production environment, it's highly recommended to use the Helm charts published on the registry.

* The default ForgeOps deployment provides a self-signed certificate that has a very limited use even in demo environments. You must use a certificate obtained from a certificate authority for use in your environment. You can use the [Add custom certificates](../prepare/security/secrets-rotation.html#add-cust-cert) procedure.

* The current ForgeOps deployments on GKE, AKS, and EKS use Traefik as the default ingress controller. You can continue to use NGINX, but note that Kubernetes has stopped the support for ingress-nginx controller, so we strongly recommend you use Traefik for new deployments.

* On minikube, ForgeOps deployments continues to use the ingress-nginx addon provided by minikube. |

1. Verify you've set up your environment and created a Kubernetes cluster as documented in the [setup section](../setup/overview.html).

2. Use the terminal where you have already activated Python3 virtual environment. If you haven't already done so, activate the virtual environment in a new terminal window:

   ```
   $ source .venv/bin/activate
   ```

3. Verify your ForgeOps version:

   ```
   $ cd /path/to/forgeops
   $ ./bin/forgeops version
   ```

4. The configuration of a ForgeOps deployment is steered through the use of Kustomize overlays or Helm values. Use the forgeops env command to set up the Kustomize overlays and Helm values files to configure your ForgeOps deployment environment:

5. In a minikube, set up the default cluster issuer\[[1](#_footnotedef_1 "View footnote.")]. For example:

   ```
   $ kubectl apply -f /path/to/forgeops/etc/resources/selfsigned-issuer.yaml
   ```

6. In minikube, set up a single instance deployment environment. For example:

   ```
   $ cd /path/to/forgeops/bin
   $ ./forgeops env --env-name my-env --fqdn my-fqdn.example.com \
     --cluster-issuer my-cluster-issuer --single-instance
   ```

   In the command above, replace my-fqdn.example.com and my-cluster-issuer with appropriate values from your environment.

   Learn more about deployment sizes in [Cluster and deployment sizes](architecture.html#cluster-and-deployment-sizes) and about single instances [here](architecture.html#single-inst).

7. Ensure that the `image.repository` and `image.tag` are correctly specified in the image defaulter file in your ForgeOps deployment environment. The image defaulter file is located at /path/to/forgeops/kustomize/deploy/image-defaulter/kustomization.yaml.

   In your production environment, use the forgeops image command to select the latest available platform image corresponding to the major ForgeOps release, and not necessarily the latest image available from ForgeOps. This documentation uses images tagged as latest from ForgeOps as default for demo and learning purposes. Using images tagged as latest from ForgeOps directly in your production environment can result in unintended upgrades.

   Learn more about customizing ForgeOps platform images [here](../customize/overview.html).

   If you want to use ForgeOps-provided Docker images for the platform, don't modify the image defaulter file. The following command sets up the latest ForgeOps-provided Docker image for the 8.1.0:

   ```
   $ cd /path/to/forgeops/bin
   $ ./forgeops image --env-name my-env --release 8.1.0 platform
   ```

   |   |                                                                                                                                                                                                                                                                                                                                                                         |
   | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | To set up your deployment environment with your customized image, use the following example command:```
   $ cd /path/to/forgeops/bin
   $ ./forgeops image --release my-image --release-name my-release --env-name my-env platform
   ```You can get the image names and tags from the image defaulter file on the system on which the customized Docker images were developed. |

8. Set up your Kubernetes context:

   1. Create a Kubernetes namespace in the cluster for the Ping Advanced Identity Software pods:

      ```
      $ kubectl create namespace my-namespace
      ```

   2. Set the active namespace in your Kubernetes context to the Kubernetes namespace you just created:

      ```
      $ kubens my-namespace
      ```

9. Set up the certificate and secret management prerequisites:

   |   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
   | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | 1. Because minikube provides its own ingress controller, there's no need to install another ingress controller.

   2. The `forgeops` utility uses `cert-manager` as the certificate management utility. If you need to use a different certificate management utility, refer to the corresponding documentation for installing that utility. You can disable `cert-manager` for ingresses in your ForgeOps deployment environment using the --ingress-no-cert-manager option of the forgeops env command:

      ```
      $ forgeops env --env-name my-env --ingress-no-cert-manager
      ```

   3. Currently, `secret-agent` is used as the default secrets management utility in ForgeOps deployments. You can continue to use the secret agent in existing deployments.

   4. ForgeOps artifacts include alternatives for ingress (Traefik or `ha-proxy`).

      The forgeops prereqs command provides a corresponding `--` option to select the component you want to use. The `--` option isn't available for components, such as `cert-manager`, for which an alternative isn't provided.

      A few examples of the forgeops prereqs command are provided in the [`forgeops prereqs` command reference](../reference/forgeops-cmd-ref.html#prereqs-examples).

   5. Versions 1.2.9 and 1.2.10 of `secret-agent` have a flaw that causes the `secret-agent` operator to crash when it tries to access the Kubernetes API. If you are using `secret-agent`, **avoid `secret-agent` versions 1.2.9 and 1.2.10; upgrade to version 1.2.11**. |

   1. To install the secret agent for secret management:

      ```
      $ forgeops prereqs cert-manager secrets
      ```

10. In a separate terminal tab or window, run the minikube tunnel command, and enter your system's superuser password when prompted:

    ```
    $ minikube tunnel
    ✅  Tunnel successfully started

    📌  NOTE: Please do not close this terminal as this process must stay alive for the tunnel to be accessible …​

    ❗  ...
    Password:
    ```

    The tunnel creates networking that lets you access the minikube cluster's ingress on the localhost IP address (127.0.0.1). Leave the tab or window that started the tunnel open for as long as you run the ForgeOps deployment.

    Refer to [this post](https://stackoverflow.com/questions/70961901/ingress-with-minikube-working-differently-on-mac-vs-ubuntu-when-to-set-etc-host) for an explanation about why a minikube tunnel is required to access ingress resources when running minikube on an ARM-based macOS system.

11. Set up the `fast` storage class using the `minikube-fast-storage-class.yaml` file in the /path/to/forgeops/etc/resources directory:

    ```
    $ kubectl apply -f /path/to/forgeops/etc/resources/minikube-fast-storage-class.yaml
    ```

12. Enable secret agent in your deployment environment:

    ```
    $ forgeops env --env-name my-env --namespace my-namespace  --secret-agent
    ```

13. Run the forgeops apply command. Learn more in [`forgeops apply` command reference](../reference/forgeops-cmd-ref.html#forgeops-apply).

    For example:

    ```
    $ cd /path/to/forgeops/bin
    $ ./forgeops apply --env-name my-env
    ```

    The preceding command creates a single-instance ForgeOps deployment. Only single-instance deployments are supported on minikube.

    If you prefer not to deploy using a single forgeops apply command, you can find more information in [Alternative deployment techniques when using Kustomize](#alt-techniques-kustomize-local).

    |   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
    | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
    |   | Ping Identity only offers its software or services to legal entities that have entered into a binding license agreement with Ping Identity. When you install Docker images provided by ForgeOps, you agree either that: 1) you are an authorized user of a Ping Advanced Identity Software customer that has entered into a license agreement with Ping Identity governing your use of the Ping Identity software; or 2) your use of the Ping Advanced Identity Software is subject to the [Ping Identity Subscription Agreements](https://www.pingidentity.com/en/legal/subscription-agreement.html). |

14. Check the status of the pods in the namespace in which you deployed the platform until all the pods are ready:

    1. Run the kubectl get pods command.

    2. Review the output. Deployment is complete when:

       * All entries in the `STATUS` column indicate `Running` or `Completed`.

       * The `READY` column indicates all running containers are available. The entry in the `READY` column represents \[total number of containers/number of available containers].

    3. If necessary, continue to query your deployment's status until all the pods are ready.

15. (Optional) Install a TLS certificate instead of using the default self-signed certificate in your ForgeOps deployment. Refer to [TLS certificate](../prepare/security/https.html#tls-certificate) for details.

## Alternative deployment techniques when using Kustomize

### Staged deployments

If you prefer not to perform a ForgeOps Kustomize deployment using a single forgeops apply command, you can deploy the platform in stages, [component by component](../troubleshoot/staged-deployment.html), instead of deploying with a single command. Staging deployments can be useful if you need to troubleshoot a deployment issue.

### Generating Kustomize manifests and using `kubectl apply` commands

You can generate Kustomize manifests using the forgeops env command, and then deploy the platform using the kubectl apply -k command.

The forgeops env command generates Kustomize manifests for your ForgeOps deployment environment. The manifests are written to the /path/to/forgeops/kustomize/overlay/my-env directory of your `forgeops` repository clone. Advanced users who prefer to work directly with Kustomize manifests that describe their ForgeOps deployment can use the generated content in the kustomize/overlay/my-env directory as an alternative to using the forgeops command:

1. Generate an initial set of Kustomize manifests by running the forgeops env command.

2. Run kubectl apply -k commands to deploy and remove platform components. Specify a manifest in the kustomize/overlay/my-env directory as an argument when you run kubectl apply -k commands.

   1. Use GitOps to manage configuration changes to the kustomize/overlay/my-env directory.

## Next step

* [icon: check-square-o, set=fa][Become familiar with ForgeOps deployments](overview.html)

* [icon: check-square-o, set=fa][Understand ForgeOps architecture](architecture.html)

* [icon: check-square-o, set=fa][Deploy the platform](deploy.html)

* [icon: square-o, set=fa]*[Access platform UIs and APIs](access.html)*

* [icon: square-o, set=fa][Plan for production deployment](next-steps.html)

***

[1](#_footnoteref_1). You can use the self-signed issuer provided by ForgeOps for test purposes. For production environments, ForgeOps recommends using a cluster issuer that uses a certificate from a trusted certificate authority (CA).

---

---
title: Deployment overview
description: A ForgeOps deployment is a deployment of the Ping Advanced Identity Software on Kubernetes based on Docker images, Helm charts, Kustomize bases and overlays, utility programs, and other artifacts you can find in the forgeops repository on GitHub.
component: forgeops
version: 2026.2
page_id: forgeops:deploy:overview
canonical_url: https://docs.pingidentity.com/forgeops/2026.2/deploy/overview.html
llms_txt: https://docs.pingidentity.com/forgeops/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  next_step: Next step
---

# Deployment overview

A *ForgeOps deployment* is a deployment of the Ping Advanced Identity Software on Kubernetes based on Docker images, Helm charts, Kustomize bases and overlays, utility programs, and other artifacts you can find in the `forgeops` repository on GitHub.

You can get a ForgeOps deployment up and running on Kubernetes quickly. After performing a ForgeOps deployment, you can use it to explore how you might configure a Kubernetes cluster before you deploy the platform in production.

A ForgeOps deployment is a robust sample deployment for demonstration and exploration purposes only. *It is not a production deployment*.

This section describes how to perform a ForgeOps deployment in a Kubernetes cluster and then access the platform's GUIs and REST APIs. When you're done, you can use ForgeOps deployment to explore deployment customizations.

![Illustrates the major tasks performed to deploy the platform.](_images/deploy.png)

Performing a ForgeOps deployment is a good learning and exploration exercise that helps prepare you to put together a project plan for deploying the platform in production. To better understand how this activity fits in to the overall deployment process, refer to [Performing a ForgeOps deployment](../start/start-here.html#cdm-sandbox).

Using the ForgeOps artifacts and this documentation, you can quickly get the Ping Advanced Identity Software running in a Kubernetes environment. You begin to familiarize yourself with some of the steps you'll need to perform when deploying the platform in the cloud for production use:

Standardizes the process—The ForgeOps team's mission is to standardize a process for deploying the Ping Advanced Identity Software on Kubernetes. The team is made up of technical consultants and cloud software developers. We've had numerous interactions with our customers and discussed common deployment issues. Based on our interactions, we developed the ForgeOps artifacts to make deployment of the platform easier in the cloud.

Simplifies baseline deployment—We then developed artifacts: Dockerfiles, Kustomize bases and overlays, Helm charts, and utility programs to simplify the deployment process. We deployed small-sized, medium-sized, and large-sized production-quality Kubernetes clusters, and kept them up and running 24x7. We conducted continuous integration and continuous deployment as we added new capabilities and fixed problems in the system. We maintained, benchmarked, and tuned the system for optimized performance. Most importantly, we documented the process so you could replicate it.

Eliminates guesswork—If you use our ForgeOps artifacts and follow the instructions in this documentation without deviation, you can successfully deploy the Ping Advanced Identity Software in the cloud. ForgeOps deployments take the guesswork out of setting up a cloud environment. They bypass the deploy-test-integrate-test-repeat cycle many customers struggle through when spinning up the Ping Advanced Identity Software in the cloud for the first time.

Prepares you to deploy in production—After you've performed a ForgeOps deployment you'll be ready to start working with experts on deploying in production. We strongly recommend that you engage a Ping Identity technical consultant or partner to assist you with deploying the platform in production.

## Next step

* [icon: check-square-o, set=fa][Become familiar with ForgeOps deployments](overview.html)

* [icon: square-o, set=fa]*[Understand ForgeOps architecture](architecture.html)*

* [icon: square-o, set=fa][Deploy the platform](deploy.html)

* [icon: square-o, set=fa][Access platform UIs and APIs](access.html)

* [icon: square-o, set=fa][Plan for production deployment](next-steps.html)

---

---
title: ForgeOps architecture
description: After you perform a ForgeOps deployment, the Ping Advanced Identity Software is fully operational in a Kubernetes cluster. forgeops artifacts provide preconfigured JVM settings, memory, CPU limits, and other configurations.
component: forgeops
version: 2026.2
page_id: forgeops:deploy:architecture
canonical_url: https://docs.pingidentity.com/forgeops/2026.2/deploy/architecture.html
llms_txt: https://docs.pingidentity.com/forgeops/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Kubernetes", "Kubernetes Cluster", "Ingress Controller", "Traefik", "HAProxy", "Prometheus", "Grafana", "Alertmanager", "Secret Agent Operator", "Certificate Manager", "Terraform", "Helm", "High Availability", "TLS/SSL", "Replication", "Backup &amp; Restore"]
section_ids:
  next_step: Next step
---

# ForgeOps architecture

After you perform a ForgeOps deployment, the Ping Advanced Identity Software is fully operational in a Kubernetes cluster. `forgeops` artifacts provide preconfigured JVM settings, memory, CPU limits, and other configurations.

Here are some of the characteristics of ForgeOps deployments:

* Cluster and deployment sizes

  When you use the Terraform artifacts in the `forgeops-extras` repository to create a Kubernetes cluster on [Google Cloud](../setup/google-cloud.html#gcp-cluster-size), [AWS](../setup/aws.html#aws-cluster-size), or [Azure](../setup/azure.html#azure-cluster-size), you specify one of three sizes:

  * A small cluster with capacity to handle 1,000,000 test users

  * A medium cluster with capacity to handle 10,000,000 test users

  * A large cluster with capacity to handle 100,000,000 test users

  When you use the minikube start command to create a Kubernetes cluster on [minikube](../setup/minikube.html#minikube-cluster), you don't specify a cluster size.

  When you [perform a ForgeOps deployment](deploy.html), you specify a deployment size. This deployment size should be the same as your cluster size, except when you perform *single-instance ForgeOps deployments*.

  []()Single-instance deployments are special deployments that you use to [configure AM and IDM and build custom Docker images for the Ping Advanced Identity Software](../customize/overview.html). They are called single-instance deployments because unlike small, medium, and large deployments, they have only single pods that run AM and IDM. They are only suitable for developing the AM and IDM configurations and must not be used for testing performance, monitoring, security, and backup requirements in production environments.

  You can perform one or more single-instance deployments on small, medium, and large GKE, EKS, and AKS clusters. Each single-instance deployment resides in its own namespace.

  You can perform one (and only one) single-instance deployment on a minikube cluster.

* Multi-zone Kubernetes cluster

  In small, medium, and large ForgeOps deployments, Ping Advanced Identity Software pods are distributed across three zones for high availability.

  (In single-instance deployments, Ping Advanced Identity Software pods reside in a single zone.)

  Go [here](#cdm-topology) for a diagram that shows the organization of pods in zones and node pools in small, medium, and large ForgeOps deployments.

* Third-party deployment and monitoring tools

  * [What is Traefik?](https://doc.traefik.io/traefik/)

  * [HAProxy Ingress Controller](https://haproxy-ingress.github.io) for Kubernetes ingress support.'\[[1](#_footnotedef_1 "View footnote.")]'

  * [Prometheus](https://prometheus.io/) for monitoring and notifications.'\[[1](#_footnotedef_1 "View footnote.")]'

  * [Prometheus Alertmanager](https://prometheus.io/docs/alerting/alertmanager/) for setting and managing alerts.'\[[1](#_footnotedef_1 "View footnote.")]'

  * [Grafana](https://grafana.com/) for metrics visualization.'\[[1](#_footnotedef_1 "View footnote.")]'

  * [Certificate Manager](https://docs.cert-manager.io) for obtaining and installing security certificates.

  * [Helm](https://helm.sh) for deploying Helm charts.

  * [Terraform](https://developer.hashicorp.com/terraform) for creating example clusters.'\[[1](#_footnotedef_1 "View footnote.")]'

* Ready-to-use Ping Advanced Identity Software components

  * Multiple DS instances are deployed for higher availability. Separate instances are deployed for Core Token Service (CTS) tokens and identities. The instances for identities also contain AM and IDM run-time data.

  * The AM configuration is file-based, stored at the path `/home/forgerock/openam/config` inside the AM Docker container (and in the AM pods).

  * Multiple AM instances are deployed for higher availability.'\[[2](#_footnotedef_2 "View footnote.")]'

  * AM instances are configured to access DS data stores.

  * Multiple IDM instances are deployed for higher availability.'\[[2](#_footnotedef_2 "View footnote.")]'

  * IDM instances are configured to access DS data stores.

- Highly available, distributed deployment'\[[1](#_footnotedef_1 "View footnote.")]' '\[[2](#_footnotedef_2 "View footnote.")]'

  Deployment across three zones ensures that the ingress controller and all Ping Advanced Identity Software components are highly available.

  Pods that run DS are configured to use [soft anti-affinity](https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/#affinity-and-anti-affinity). Because of this, Kubernetes schedules DS pods to run on nodes that don't have any other DS pods whenever possible.

  The exact placement of all other ForgeOps pods is delegated to Kubernetes.

  Pods are organized across three zones in a single node pool with six nodes. Pod placement among the nodes might vary, but the DS pods should run on nodes without any other DS pods.

  ![Clusters that support ForgeOps deployments have three zones and one node pool. The node pool has six nodes.](_images/m-cluster.svg)

- Ingress controller

  Hitherto ForgeOps used ingress-nginx controller by default. In March 2026, [Kubernetes will retire support for ingress-nginx controller](https://kubernetes.io/blog/2026/01/29/ingress-nginx-statement/). ForgeOps team has decided to use Traefik as the default ingress controller for new deployments. Traefik is a modern HTTP reverse proxy and load balancer that makes deploying microservices easy.

  Optionally, you can [deploy HAProxy Ingress](../reference/ingress.html#haproxy) as the ingress controller instead.'\[[1](#_footnotedef_1 "View footnote.")]'

- Secret generation and management

  [The open source Secret Agent operator](https://github.com/ForgeRock/secret-agent) generates Kubernetes secrets for Ping Advanced Identity Software deployments. It also integrates with Google Cloud Secret Manager, AWS Secrets Manager, and Azure Key Vault, providing cloud backup and retrieval for secrets.

- Secured communication

  The ingress controller is TLS-enabled. TLS is terminated at the ingress controller. Incoming requests and outgoing responses are encrypted.

  Inbound communication to DS instances occurs over secure LDAP (LDAPS).

  For more information, refer to [Secure HTTP](../prepare/security/https.html).

- Stateful sets

  ForgeOps deployments use Kubernetes stateful sets to manage the DS pods. Stateful sets protect against data loss if Kubernetes client containers fail.

  On small-, medium- and large- deployments, CTS data stores are configured for [affinity](../reference/glossary.html#glossary-affinity) load balancing for optimal performance.

  ![AM connections to CTS servers use token affinity in ForgeOps deployments.](_images/m-cluster-cts-flow.svg)

  AM policies, application data, and identities reside in the `idrepo` directory service. Small-, medium- and large- deployments use a single `idrepo` master configured to fail over to one of two secondary directory services.

  ![For all the ${am.abbr} pods](_images/m-cluster-idrepo-flow.svg)

- Authentication

  IDM is configured to use AM for authentication.

- DS replication'\[[2](#_footnotedef_2 "View footnote.")]'

  All DS instances are configured for full replication of identities and session tokens.

- Backup and restore'\[[1](#_footnotedef_1 "View footnote.")]'

  Backup and restore can be performed using several techniques. You can:

  * Use the volume snapshot capability in GKE, EKS, or AKS. The cluster where the ForgeOps deployment resides must be configured with a volume snapshot class before you can take volume snapshots, and persistent volume claims must use a CSI driver that supports volume snapshots.

  * Use the ds-backup utility.

  * Use a "last mile" backup archival solutions, such as Amazon S3, Google Cloud Storage, and Azure Cloud Storage that is specific to the cloud provider.

  * Use a Kubernetes backup and restore product, such as Velero, Kasten K10, TrilioVault, Commvault, or Portworx PX-Backup.

  For more information, refer to [Backup and restore overview](../backup/overview.html).

- Initial data loading

  After the first AM instance in a ForgeOps deployment has started, an `amster` job runs. This job loads application data, such as OAuth 2.0 client definitions, to the `idrepo` DS instance.

## Next step

* [icon: check-square-o, set=fa][Become familiar with ForgeOps deployments](overview.html)

* [icon: check-square-o, set=fa][Understand ForgeOps architecture](architecture.html)

* [icon: square-o, set=fa]*[Deploy the platform](deploy.html)*

* [icon: square-o, set=fa][Access platform UIs and APIs](access.html)

* [icon: square-o, set=fa][Plan for production deployment](next-steps.html)

***

[1](#_footnoteref_1). Not available on ForgeOps deployments on minikube.[2](#_footnoteref_2). Not available on single-instance ForgeOps deployments.

---

---
title: ForgeOps deployment
description: After you set up your deployment environment and your Kubernetes cluster, you're ready to perform a ForgeOps deployment.
component: forgeops
version: 2026.2
page_id: forgeops:deploy:deploy
canonical_url: https://docs.pingidentity.com/forgeops/2026.2/deploy/deploy.html
llms_txt: https://docs.pingidentity.com/forgeops/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["forgeops Command", "Prometheus", "Grafana", "Alertmanager", "Helm"]
section_ids:
  deployment_technologies: Deployment technologies
  deployment_scenarios: Deployment scenarios
---

# ForgeOps deployment

After you set up your deployment environment and your Kubernetes cluster, you're ready to perform a ForgeOps deployment.

First, you'll need to choose a deployment technology.

## Deployment technologies

You can perform ForgeOps deployments using either [Kustomize](https://kustomize.io) or [Helm](https://helm.sh).

The preferred deployment technology for ForgeOps deployments is Helm. If you are not familiar with either of these two technologies, choose Helm.

Choose Kustomize as your deployment technology when:

* You performed ForgeOps deployments before Helm charts were available in the `forgeops` repository, and you want to continue to use Kustomize-based deployments.

* You want to generate Kustomize manifests for the platform, including custom manifests, using the forgeops generate command.

* Kustomize is your organization's preferred deployment technology for Kubernetes.

* Kustomize offers needed features that are not available in Helm.

## Deployment scenarios

Follow the steps in one of these scenarios to perform a ForgeOps deployment:

* [Deploy using Helm on GKE, EKS, or AKS](deploy-scenario-helm-cloud.html)

* [Deploy using Helm on minikube](deploy-scenario-helm-local.html)

* [Deploy using Kustomize on GKE, EKS, or AKS](deploy-scenario-kustomize-cloud.html)

* [Deploy using Kustomize on minikube](deploy-scenario-kustomize-local.html)

---

---
title: Next steps
description: If you've followed the instructions for performing a ForgeOps deployment without modifying configurations, then the following indicates that you've been successful:
component: forgeops
version: 2026.2
page_id: forgeops:deploy:next-steps
canonical_url: https://docs.pingidentity.com/forgeops/2026.2/deploy/next-steps.html
llms_txt: https://docs.pingidentity.com/forgeops/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Load Testing", "Backup &amp; Restore", "Ingress Controller", "Kubernetes Cluster", "Alertmanager"]
---

# Next steps

If you've followed the instructions for performing a ForgeOps deployment *without modifying configurations*, then the following indicates that you've been successful:

* The Kubernetes cluster and pods are up and running.

* DS, AM, and IDM are installed and running. You can access each ForgeOps component.

* DS replication and failover work as expected.'\[[1](#_footnotedef_1 "View footnote.")]'

When you're satisfied that all of these conditions are met, then you've successfully taken the first steps towards deploying the Ping Advanced Identity Software on Kubernetes. Congratulations!

You can use the ForgeOps deployment to test deployment customizations—options that you might want to use in production but are not part of the base deployment. Examples'\[[2](#_footnotedef_2 "View footnote.")]' include, but are not limited to:

* Running lightweight benchmark tests

* Backing up and restoring your data

* Securing TLS with a certificate that's dynamically obtained from Let's Encrypt

* Using an ingress controller other than the default in ForgeOps

* Resizing the cluster to meet your business requirements

* Configuring Alert Manager to issue alerts when usage thresholds have been reached

Now that you're familiar with ForgeOps deployments, you're ready to work with a project team to plan and configure your production deployment. You'll need a team with expertise in the Ping Advanced Identity Software, in your cloud provider, and in Kubernetes on your cloud provider. We strongly recommend that you engage a Ping Identity technical consultant or partner to assist you with deploying the platform in production.

You'll perform these major activities:

Platform configuration—Ping Advanced Identity Software experts configure AM and IDM using single-instance ForgeOps deployments and build custom Docker images for the Ping Advanced Identity Software. The [Customization overview](../customize/overview.html) provides information about platform configuration tasks.

Cluster configuration—Cloud technology experts configure the Kubernetes cluster that will host the Ping Advanced Identity Software for optimal performance and reliability. Tasks include configuring your Kubernetes cluster to suit your business needs, setting up monitoring and alerts to track site health and performance, backing up configuration and user data for disaster preparedness, and securing your deployment. The [Prepare to deploy in production](../prepare/overview.html) and READMEs in the `forgeops` repository provide information about cluster configuration.

Site reliability engineering—Site reliability engineers monitor the Ping Advanced Identity Software deployment and keep the deployment up and running based on your business requirements. These could include use cases, service-level agreements, thresholds, and load test profiles. The [Prepare to deploy in production](../prepare/overview.html), and READMEs in the `forgeops` repository, provide information about site reliability.

***

[1](#_footnoteref_1). Not available on single-instance ForgeOps deployments.[2](#_footnoteref_2). Not available on ForgeOps deployments on minikube.

---

---
title: Remove a ForgeOps deployment
description: This page provides instructions for removing ForgeOps deployments for the following scenarios:
component: forgeops
version: 2026.2
page_id: forgeops:deploy:remove
canonical_url: https://docs.pingidentity.com/forgeops/2026.2/deploy/remove.html
llms_txt: https://docs.pingidentity.com/forgeops/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Terraform"]
section_ids:
  helm-cloud: Remove a Helm deployment from GKE, EKS, or AKS
  helm-local: Remove a Helm deployment from minikube
  kustomize-cloud: Remove a Kustomize deployment from GKE, EKS, or AKS
  kustomize-local: Remove a Kustomize deployment from minikube
---

# Remove a ForgeOps deployment

This page provides instructions for removing ForgeOps deployments for the following scenarios:

* [Remove a Helm deployment on GKE, EKS, or AKS](#helm-cloud)

* [Remove a Helm deployment on minikube](#helm-local)

* [Remove a Kustomize deployment on GKE, EKS, or AKS](#kustomize-cloud)

* [Remove a Kustomize deployment on minikube](#kustomize-local)

## Remove a Helm deployment from GKE, EKS, or AKS

1. Set up your Kubernetes context:

   1. Set the `KUBECONFIG` environment variable so that your Kubernetes context references the cluster in which you deployed the platform.

   2. Set the active namespace in your Kubernetes context to the Kubernetes namespace in which you deployed the platform:

      ```
      $ kubens my-namespace
      ```

2. Remove the ForgeOps deployment:

   ```
   $ cd /path/to/forgeops/charts/identity-platform
   $ helm uninstall identity-platform
   ```

   Running helm uninstall identity-platform doesn't delete PVCs and the `amster` job from your namespace.

3. (Optional) To delete PVCs, use the kubectl command. For example, to delete `data-ds-idrepo-0` and `data-ds-cts-0`:

   ```
   $ kubectl delete pvc data-ds-idrepo-0 data-ds-cts-0
   ```

4. (Optional) To delete the `amster` job, use the kubectl command:

   ```
   $ kubectl delete job amster
   ```

5. (Optional) Delete your cluster:

   1. Change to the directory in your `forgeops-extras` repository clone that contains Terraform artifacts:

      ```
      $ cd /path/to/forgeops-extras/terraform
      ```

   2. Run the tf-destroy script to create your cluster:

      ```
      $ ./tf-destroy
      ```

      Respond `yes` to the `Do you really want to destroy all resources?` prompt.

## Remove a Helm deployment from minikube

1. Set the active namespace in your Kubernetes context to the Kubernetes namespace in which you deployed the platform:

   ```
   $ kubens my-namespace
   ```

2. Remove the ForgeOps deployment:

   ```
   $ cd /path/to/forgeops/charts/identity-platform
   $ helm uninstall identity-platform
   ```

   Running helm uninstall identity-platform doesn't delete PVCs and the `amster` job from your namespace.

3. (Optional) To delete PVCs, use the kubectl command. For example, to delete `data-ds-idrepo-0` and `data-ds-cts-0`:

   ```
   $ kubectl delete pvc data-ds-idrepo-0 data-ds-cts-0
   ```

4. (Optional) To delete the `amster` job, use the kubectl command:

   ```
   $ kubectl delete job amster
   ```

5. (Optional) Delete your cluster:

   ```
   $ minikube stop
   $ minikube delete
   ```

## Remove a Kustomize deployment from GKE, EKS, or AKS

1. Set up your Kubernetes context:

   1. Set the `KUBECONFIG` environment variable so that your Kubernetes context references the cluster in which you deployed the platform.

   2. Set the active namespace in your Kubernetes context to the Kubernetes namespace in which you deployed the platform:

      ```
      $ kubens my-namespace
      ```

2. Remove the ForgeOps deployment:

   ```
   $ cd /path/to/forgeops/bin
   $ ./forgeops delete --env-name my-env
   ```

   Respond `Y` to all the `OK to delete?` prompts.

3. (Optional) Delete your cluster:

   1. Change to the directory in your `forgeops-extras` repository clone that contains Terraform artifacts:

      ```
      $ cd /path/to/forgeops-extras/terraform
      ```

   2. Run the tf-destroy script to create your cluster:

      ```
      $ ./tf-destroy
      ```

      Respond `yes` to the `Do you really want to destroy all resources?` prompt.

## Remove a Kustomize deployment from minikube

1. Set the active namespace in your Kubernetes context to the Kubernetes namespace in which you deployed the platform:

   ```
   $ kubens my-namespace
   ```

2. Remove the ForgeOps deployment:

   ```
   $ cd /path/to/forgeops/bin
   $ ./forgeops delete --env-name my-env
   ```

   Respond `Y` to all the `OK to delete?` prompts.

3. (Optional) Delete your cluster:

   ```
   $ minikube stop
   $ minikube delete
   ```

---

---
title: UI and API access
description: This page shows you how to access and monitor the Ping Advanced Identity Software components in a ForgeOps deployment.
component: forgeops
version: 2026.2
page_id: forgeops:deploy:access
canonical_url: https://docs.pingidentity.com/forgeops/2026.2/deploy/access.html
llms_txt: https://docs.pingidentity.com/forgeops/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["User Interface", "REST API", "Monitoring", "Grafana", "Prometheus"]
section_ids:
  am-services-cdm: AM services
  idm-services-cdm: IDM services
  ds_command_line_access: DS command-line access
  cdm-monitoring: ForgeOps deployment monitoring
  grafana: Grafana
  prometheus: Prometheus
  next_step: Next step
---

# UI and API access

This page shows you how to access and monitor the Ping Advanced Identity Software components in a ForgeOps deployment.

AM and IDM are configured for access through the Kubernetes cluster's ingress controller. You can access these components using their admin UIs and REST APIs.

DS cannot be accessed through the ingress controller, but you can use Kubernetes methods to access the DS pods.

## AM services

To access the AM admin UI:

1. Set the active namespace in your local Kubernetes context to the namespace in which you performed the ForgeOps deployment.

2. Obtain the `amadmin` user's password:

   ```
   $ cd /path/to/forgeops/bin
   $ ./forgeops info | grep amadmin
   vr58qt11ihoa31zfbjsdxxrqryfw0s31 (amadmin user)
   ```

3. Open a new window or tab in a web browser.

4. Go to https\://my-fqdn/platform.

   The Kubernetes ingress controller handles the request, routing it to the `login-ui` pod.

   The login UI prompts you to log in.

5. Log in as the `amadmin` user.

   The Ping Advanced Identity Software UI appears in the browser.

6. Select Native Consoles > Access Management.

   The AM admin UI appears in the browser.

To access the AM REST APIs:

1. Start a terminal window session.

2. Run a curl command to verify that you can access the REST APIs through the ingress controller. For example:

   ```
   $ curl \
    --insecure \
    --request POST \
    --header "Content-Type: application/json" \
    --header "X-OpenAM-Username: amadmin" \
    --header "X-OpenAM-Password: vr58qt11ihoa31zfbjsdxxrqryfw0s31" \
    --header "Accept-API-Version: resource=2.0, protocol=1.0" \
    "https://my-fqdn/am/json/realms/root/authenticate"

   {
       "tokenId":"AQIC5wM2...Q..*",
       "successUrl":"/am/console",
       "realm":"/"
   }
   ```

## IDM services

To access the IDM REST APIs:

1. Start a terminal window session.

2. Set the active namespace in your local Kubernetes context to the namespace in which you performed the ForgeOps deployment.

3. Obtain the `amadmin` user's password:

   ```
   $ cd /path/to/forgeops/bin
   $ ./forgeops info | grep amadmin
   vr58qt11ihoa31zfbjsdxxrqryfw0s31 (amadmin user)
   ```

4. AM authorizes IDM REST API access using the [OAuth 2.0 authorization code flow](https://docs.pingidentity.com/pingam/8/oauth2-guide/oauth2-authz-grant.html). ForgeOps deployments come with the `idm-admin-ui` client, which is configured to let you get a bearer token using this OAuth 2.0 flow. You'll use the bearer token in the next step to access the IDM REST API:

   1. Get a session token for the `amadmin` user:

      ```
      $ curl \
       --request POST \
       --insecure \
       --header "Content-Type: application/json" \
       --header "X-OpenAM-Username: amadmin" \
       --header "X-OpenAM-Password: vr58qt11ihoa31zfbjsdxxrqryfw0s31" \
       --header "Accept-API-Version: resource=2.0, protocol=1.0" \
       'https://my-fqdn/am/json/realms/root/authenticate'
      {
       "tokenId":"AQIC5wM...Q..*",
       "successUrl":"/am/console",
       "realm":"/"}
      ```

   2. Get an authorization code. Specify the ID of the session token that you obtained in the previous step in the `Cookie` parameter:

      ```
      $ curl \
       --dump-header - \
       --insecure \
       --request GET \
       --header "Cookie: iPlanetDirectoryPro=AQIC5wM...Q.." \
       "https://my-fqdn/am/oauth2/realms/root/authorize?redirect_uri=https://my-fqdn/platform/appAuthHelperRedirect.html&client_id=idm-admin-ui&scope=openid%20fr:idm:&response_type=code&state=abc123"

      HTTP/2 302
      ...
      code=3cItL9G52DIiBdfXRngv2_dAaYM...
      ```

   3. Exchange the authorization code for an access token. Specify the access code that you obtained in the previous step in the `code` URL parameter:

      ```
      $ curl --request POST \
       --insecure \
       --data "grant_type=authorization_code" \
       --data "code=3cItL9G52DIiBdfXRngv2_dAaYM" \
       --data "client_id=idm-admin-ui" \
       --data "redirect_uri=https://my-fqdn/platform/appAuthHelperRedirect.html" \
       "https://my-fqdn/am/oauth2/realms/root/access_token" 
      {
       "access_token":"oPzGzGFY1SeP2RkI-ZqaRQC1cDg",
       "scope":"openid fr:idm:*",
       "id_token":"eyJ0eXAiOiJKV
        ...
        sO4HYqlQ",
       "token_type":"Bearer",
       "expires_in":239
      }
      ```

5. Run a curl command to verify that you can access the `openidm/config` REST endpoint through the ingress controller. Use the access token returned in the previous step as the bearer token in the authorization header.

   The following example command provides information about the IDM configuration:

   ```
   $ curl \
    --insecure \
    --request GET \
    --header "Authorization: Bearer oPzGzGFY1SeP2RkI-ZqaRQC1cDg" \
    --data "{}" \
    \https://my-fqdn/openidm/config
   {
    "_id":"",
    "configurations":
     [
      {
       "_id":"ui.context/admin",
       "pid":"ui.context.4f0cb656-0b92-44e9-a48b-76baddda03ea",
       "factoryPid":"ui.context"
       },
       ...
      ]
   }
   ```

## DS command-line access

The DS pods in ForgeOps deployment are not exposed outside of the cluster. If you need to access one of the DS pods, use a standard Kubernetes method:

* Execute shell commands in DS pods using the kubectl exec command.

* Forward a DS pod's LDAPS port (1636) to your local computer. Then, you can run LDAP CLI commands, for example ldapsearch. You can also use an LDAP editor such as Apache Directory Studio to access the directory.

For all ForgeOps deployment directory pods, the directory superuser DN is `uid=admin`. Obtain this user's password by running the forgeops info command.

## ForgeOps deployment monitoring

This section describes how to access Grafana dashboards and Prometheus UI'\[[1](#_footnotedef_1 "View footnote.")]' .

### Grafana

To access Grafana dashboards:

1. Set up port forwarding on your local computer for port 3000:

   ```
   $ /path/to/forgeops/bin/prometheus-connect.sh -G
   Forwarding from 127.0.0.1:3000 → 3000
   Forwarding from [::1]:3000 → 3000
   ```

2. In a web browser, navigate to http\://localhost:3000 to access the Grafana dashboards.

3. Log in as the `admin` user with `password` as the password.

When you're done using the Grafana UI, stop Grafana port forwarding by entering Ctrl+c in the terminal window where you initiated port forwarding.

For information about Grafana, refer to [the Grafana documentation](http://docs.grafana.org).

### Prometheus

To access the Prometheus UI:

1. Set up port forwarding on your local computer for port 9090:

   ```
   $ /path/to/forgeops/bin/prometheus-connect.sh -P
   Forwarding from 127.0.0.1:9090 → 9090
   Forwarding from [::1]:9090 → 9090
   ```

2. In a web browser, navigate to http\://localhost:9090 to access the Prometheus UI.

When you're done using the Prometheus UI, stop Prometheus port forwarding by entering Ctrl+c in the terminal window where you initiated port forwarding.

For information about Prometheus, refer to [the Prometheus documentation](https://prometheus.io/docs/introduction/overview).

For a description of ForgeOps monitoring architecture and information about how to customize ForgeOps monitoring, refer to [ForgeOps deployment monitoring](../prepare/monitoring/overview.html).

## Next step

* [icon: check-square-o, set=fa][Become familiar with ForgeOps deployments](overview.html)

* [icon: check-square-o, set=fa][Understand ForgeOps architecture](architecture.html)

* [icon: check-square-o, set=fa][Deploy the platform](deploy.html)

* [icon: check-square-o, set=fa][Access platform UIs and APIs](access.html)

* [icon: square-o, set=fa]*[Plan for production deployment](next-steps.html)*

***

[1](#_footnoteref_1). Not available on ForgeOps deployments on minikube.