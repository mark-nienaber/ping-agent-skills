---
title: "Deploy using Kustomize on GKE, EKS, or AKS (Deprecated) <span class=\"icon gray\"><i class=\"fa fa-alarm-clock\"></i></span>"
description: Deploy ForgeOps using Kustomize on GKE, EKS, or AKS, including prerequisites, images, secrets, monitoring, TLS, and deployment strategies
component: forgeops
version: 2026.3
page_id: forgeops:deploy:deploy-scenario-kustomize-cloud
canonical_url: https://docs.pingidentity.com/forgeops/2026.3/deploy/deploy-scenario-kustomize-cloud.html
llms_txt: https://docs.pingidentity.com/forgeops/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-08-26T09:39:33Z
keywords: ["forgeops Command", "Prometheus", "Grafana", "Alertmanager"]
section_ids:
  alt-techniques-kustomize-cloud: Alternative deployment techniques when using Kustomize
  staged_deployments: Staged deployments
  generating_kustomize_manifests_and_using_kubectl_apply_commands: Generating Kustomize manifests and using kubectl apply commands
  next_step: Next step
---

# Deploy using Kustomize on GKE, EKS, or AKS (Deprecated)[icon: alarm-clock, set=fa]

|   |                                                                                 |
| - | ------------------------------------------------------------------------------- |
|   | This deployment scenario is deprecated and will be removed in a future release. |

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | * In a development or demo environment, you can use the Helm chart available locally in /path/to/forgeops/charts directory for performing ForgeOps deployment. In a production environment, it's highly recommended to use the Helm charts published on the registry.

* The default ForgeOps deployment provides a self-signed certificate that has a very limited use even in demo environments. You must use a certificate obtained from a certificate authority for use in your environment. You can use the [Add custom certificates](../prepare/security/secrets-rotation.html#add-cust-cert) procedure.

* The current ForgeOps deployments on GKE, AKS, and EKS use Traefik as the default ingress controller. You can continue to use NGINX, but note that Kubernetes has stopped the support for ingress-nginx controller, so we strongly recommend you use Traefik for new deployments.

* In ForgeOps 2026.3.2 or later, new Helm-generated deployments enable `readOnlyRootFilesystem` in DS pods by default. Learn more about [how to recreate the PingDS stateful set](https://github.com/ForgeRock/forgeops/blob/2026.3.2/how-tos/recreating-ds-sts.md) when you need to disable or enable `readOnlyRootFilesystem` or make any changes to existing DS stateful sets. |

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

   |   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
   | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | 1. **The `forgeops prereqs` command installs the latest version of prerequisite components, except secret-agent which doesn't select the `latest`.**

   2. The `forgeops prereqs` command installs `cert-manager` for certificate management. If you need to use a different certificate management utility, refer to the corresponding documentation for installing that utility.

      You can disable `cert-manager` for ingresses in your ForgeOps deployment environment using the --ingress-no-cert-manager option of the forgeops env command:

      ```
      $ forgeops env --env-name my-env --ingress-no-cert-manager
      ```

   3. The forgeops prereqs command provides a corresponding `--` option to select the component you want to use. The `--` option isn't available for components, such as `cert-manager`, for which an alternative isn't provided.

      A few examples of the forgeops prereqs command are provided in the [`forgeops prereqs` command reference](../reference/forgeops-cmd-ref.html#prereqs-examples).

   4. **New Helm-based deployments use the Helm-generated secrets by default.**

   5. In Kustomize-based deployments, `secret-agent` is used as the default secrets management utility.

      The secret-agent versions 1.2.9 and 1.2.10 have a flaw that causes the `secret-agent` operator to crash when it tries to access the Kubernetes API. If you are using `secret-agent`, **avoid `secret-agent` versions 1.2.9 and 1.2.10; upgrade to version 1.2.12 or later**. |

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
title: Deployment overview
description: Explore ForgeOps deployments on Kubernetes, understand the deployment workflow, and prepare to deploy the platform in production
component: forgeops
version: 2026.3
page_id: forgeops:deploy:overview
canonical_url: https://docs.pingidentity.com/forgeops/2026.3/deploy/overview.html
llms_txt: https://docs.pingidentity.com/forgeops/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2024-11-21T10:28:18Z
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