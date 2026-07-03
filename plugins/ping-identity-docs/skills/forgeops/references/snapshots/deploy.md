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
