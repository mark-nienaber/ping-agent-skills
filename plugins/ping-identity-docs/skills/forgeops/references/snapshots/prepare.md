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

---

---
title: Access restriction by IP address
description: When installing the ingress controller in production environments, you should consider configuring a CIDR block in the Helm chart for the ingress controller so that you restrict access to worker nodes from a specific IP address or a range of IP addresses.
component: forgeops
version: 2026.2
page_id: forgeops:prepare:security/restrict-access-ip-address
canonical_url: https://docs.pingidentity.com/forgeops/2026.2/prepare/security/restrict-access-ip-address.html
llms_txt: https://docs.pingidentity.com/forgeops/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Security", "Ingress Controller"]
---

# Access restriction by IP address

When installing the ingress controller in production environments, you should consider configuring a CIDR block in the Helm chart for the ingress controller so that you restrict access to worker nodes from a specific IP address or a range of IP addresses.

---

---
title: Alerts
description: Alerts for ForgeOps deployments are defined in the fr-alerts.yaml file in the forgeops repository.
component: forgeops
version: 2026.2
page_id: forgeops:prepare:monitoring/alerts
canonical_url: https://docs.pingidentity.com/forgeops/2026.2/prepare/monitoring/alerts.html
llms_txt: https://docs.pingidentity.com/forgeops/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Monitoring", "Alertmanager", "Prometheus"]
---

# Alerts

Alerts for ForgeOps deployments are defined in the [fr-alerts.yaml](https://github.com/ForgeRock/forgeops/blob/2026.2.1/cluster/addons/prometheus/forgerock-metrics/templates/fr-alerts.yaml) file in the `forgeops` repository.

To configure additional alerts, refer to the [Configure Alerting Rules](https://github.com/ForgeRock/forgeops/blob/2026.2.1/cluster/addons/prometheus/README.md#Configure-alerting-rules) section of the Prometheus and Grafana Deployment README file in the `forgeops` repository.

---

---
title: Cluster access for multiple AWS users
description: It's common for team members to share the use of a cluster. For team members to share a cluster, the cluster owner must grant access to each user:
component: forgeops
version: 2026.2
page_id: forgeops:prepare:security/multi-user-access-aws
canonical_url: https://docs.pingidentity.com/forgeops/2026.2/prepare/security/multi-user-access-aws.html
llms_txt: https://docs.pingidentity.com/forgeops/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Security", "AWS"]
---

# Cluster access for multiple AWS users

It's common for team members to share the use of a cluster. For team members to share a cluster, the cluster owner must grant access to each user:

1. Get the ARNs and names of users who need access to your cluster.

2. Set the Kubernetes context to your Amazon EKS cluster.

3. Edit the authorization configuration map for the cluster using the kubectl edit command:

   ```
   $ kubectl edit -n kube-system configmap/aws-auth
   ```

4. Under the `mapRoles` section, insert the `mapUser` section. An example is shown here with the following parameters:

   * The user ARN is `arn:aws:iam::012345678901:user/new.user`.

   * The user name registered in AWS is new\.user.

     ```
     ... mapUsers: |
         - userarn: arn:aws:iam::012345678901:user/new.user
           username: new.user
           groups:
             - system:masters
     ...
     ```

5. For each additional user, insert the `- userarn:` entry in the `mapUsers:` section:

   ```
   ... mapUsers: |
       - userarn: arn:aws:iam::012345678901:user/new.user
         username: new.user
         groups:
           - system:masters
       - userarn: arn:aws:iam::901234567890:user/second.user
         username: second.user
         groups:
           - system:masters
   ...
   ```

6. Save the configuration map.

---

---
title: Custom Grafana dashboards
description: In addition to the pods from the prometheus-operator project, ForgeOps deployments include a set of Grafana dashboards. The import-dashboards-... pod from the forgeops repository runs after Grafana starts up. This pod imports Grafana dashboards for the Ping Advanced Identity Software and terminates after importing has completed.
component: forgeops
version: 2026.2
page_id: forgeops:prepare:monitoring/dashboards
canonical_url: https://docs.pingidentity.com/forgeops/2026.2/prepare/monitoring/dashboards.html
llms_txt: https://docs.pingidentity.com/forgeops/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Monitoring", "Grafana"]
---

# Custom Grafana dashboards

In addition to the pods from the `prometheus-operator` project, ForgeOps deployments include a set of Grafana dashboards. The `import-dashboards-...` pod from the `forgeops` repository runs after Grafana starts up. This pod imports Grafana dashboards for the Ping Advanced Identity Software and terminates after importing has completed.

You can customize, export and import Grafana dashboards using the Grafana UI or HTTP API.

For information about importing custom Grafana dashboards, refer to the [Import Custom Grafana Dashboards](https://github.com/ForgeRock/forgeops/blob/2026.2.1/cluster/addons/prometheus/README.md#import-custom-grafana-dashboards) section of the Prometheus and Grafana Deployment README file in the `forgeops` repository.

---

---
title: Custom PingGateway image
description: The default PingGateway configuration provided for use with ForgeOps deployments is an example. Replace this configuration with your own routes before using PingGateway in your environment.
component: forgeops
version: 2026.2
page_id: forgeops:prepare:ig/deploy-custom-ig
canonical_url: https://docs.pingidentity.com/forgeops/2026.2/prepare/ig/deploy-custom-ig.html
llms_txt: https://docs.pingidentity.com/forgeops/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["PingGateway", "forgeops Command"]
section_ids:
  deploy_custom_pinggateway_image: Deploy custom PingGateway image
  customize_the_am_url_in_pinggateway: Customize the AM URL in PingGateway
---

# Custom PingGateway image

The default PingGateway configuration provided for use with ForgeOps deployments is an example. Replace this configuration with your own routes before using PingGateway in your environment.

Refer to the [PingGateway Deployment Guide](https://docs.pingidentity.com/pinggateway/2026.3/devops-guide/preface.html) for configuring routes.

## Deploy custom PingGateway image

To build a custom PingGateway image and deploy PingGateway:

1. Verify you've already set up ForgeOps deployment environment using the forgeops env command.

2. Verify that your ForgeOps deployment is up and running.

3. [Set up your environment to push to your Docker registry](../../customize/setup.html#docker-push).

4. Configure PingGateway by creating, modifying, or deleting rules in the /path/to/forgeops/docker/ig/config-profiles/my-profile/config/routes-service directory.

5. [Identify the repository](../../customize/setup.html#push-to) to which you'll push the Docker image. You'll use this location in the next step to specify the --push-to argument's value.

6. Build a new `ig` image that includes your changes to PingGateway static configuration:

   ```
   $ cd /path/to/forgeops/bin
   ...
   $ forgeops image --release 2026.3.0 --release-name my-ig-release ig
   ...
   $ ./forgeops build ig --env-name my-env \
     --config-profile my-profile --push-to my-repo
   ```

7. If PingGateway hadn't already been deployed in the existing ForgeOps deployment, add the - ./ig line in the default overlay file, kustomize/overlay/my-env/kustomization.yaml:

   ```
   kind: Kustomization
   apiVersion: kustomize.config.k8s.io/v1beta1
   resources:
   - ./base
   - ./secrets
   - ./ds-cts
   - ./ds-idrepo
   - ./am
   - ./amster
   - ./idm
   - ./ig
   - ./ds-set-passwords
   - ./admin-ui
   - ./end-user-ui
   - ./login-ui
   ```

8. Uninstall previously deployed PingGateway from your ForgeOps deployment:

   1. Set the active namespace in your local Kubernetes context to the namespace in which you've deployed the PingGateway.

   2. Delete PingGateway:

      ```
      $ ./forgeops delete --env-name my-env ig
      ...
      secret "openig-secrets-env" deleted
      service "ig" deleted
      deployment.apps "ig" deleted
      ```

9. Deploy PingGateway using your customized PingGateway image:

   1. In a Kustomize-based deployment:

      ```
      $ /path/to/forgeops/bin/forgeops apply --env-name my-env ig
      ```

   2. In a Helm-based deployment:

      ```
      $ cd /path/to/forgeops
      $  helm upgrade --install ping-gateway charts/ping-gateway/ \
        --values helm/my-env/values.yaml --namespace my-namespace
      ```

10. Run the kubectl get pods command to check the status of the PingGateway pod. Wait until the PingGateway pod is ready before proceeding to the next step.

11. Verify that your PingGateway routes work.

## Customize the AM URL in PingGateway

To customize the AM URL in PingGateway and deploy using Helm:

1. Edit the configuration file in your ForgeOps deployment environment (`helm/my-env/values.yaml`) and add PingGateway configuration lines. For example:

   ```
   ig:
     env:
       - name: AM_URL
         value: "\http://am/my-am"
   ```

2. Redeploy PingGateway:

   ```
   $ helm upgrade --install ping-gateway charts/ping-gateway/ \
     --values helm/my-env/values.yaml --namespace my-namespace
   ```

3. Verify that the new AM URL has been set up:

   ```
   $ kubectl get pod ig-75f8f95bbf-hk9b7 -o json |grep  -A1 -i AM_URL

        "name": "AM_URL",
        "value": "\http://am/my-am"
   ```

---

---
title: Deploy PingGateway
description: ForgeOps deployments don't include PingGateway by default.
component: forgeops
version: 2026.2
page_id: forgeops:prepare:ig/deploy-default-ig
canonical_url: https://docs.pingidentity.com/forgeops/2026.2/prepare/ig/deploy-default-ig.html
llms_txt: https://docs.pingidentity.com/forgeops/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Internet Gateway", "forgeops Command"]
---

# Deploy PingGateway

ForgeOps deployments don't include PingGateway by default.

To deploy PingGateway after you've performed a ForgeOps deployment:

1. Verify that the ForgeOps deployment is up and running.

2. Set the active namespace in your local Kubernetes context to the namespace in which you've deployed the platform components.

3. Add the - ./ig line in the default overlay file, kustomize/overlay/my-env/kustomization.yaml:

   ```
   kind: Kustomization
   apiVersion: kustomize.config.k8s.io/v1beta1
   resources:
   - ./base
   - ./secrets
   - ./ds-cts
   - ./ds-idrepo
   - ./am
   - ./amster
   - ./idm
   - ./ig
   - ./ds-set-passwords
   - ./admin-ui
   - ./end-user-ui
   - ./login-ui
   ```

4. Add PingGateway Docker image to your ForgeOps deployment configuration:

   ```
   $ cd /path/to/forgeops/bin/
   $ ./forgeops image --release 2026.3.0 ig --env-name my-env
   ```

5. Deploy PingGateway:

   1. In a Kustomize-based deployment:

      ```
      $ /path/to/forgeops/bin/forgeops apply --env-name my-env ig
      ```

   2. In a Helm-based deployment:

      ```
      $ cd /path/to/forgeops
      $ helm upgrade --install ping-gateway charts/ping-gateway/ \
        --values helm/my-env/values.yaml --namespace my-namespace
      ```

6. Run the kubectl get pods command to check the status of the PingGateway pod. Wait until the pod is ready before proceeding to the next step.

7. Verify that PingGateway is running:

   ```
   $ curl --insecure -L -X GET https://my-fqdn/ig/openig/ping -v

   ...
   > GET /ig/openig/ping HTTP/2
   > Host: my-fqdn
   > User-Agent: curl/7.64.1
   > Accept: /
   * Connection state changed (MAX_CONCURRENT_STREAMS == 128)!
   < HTTP/2 200
   < date: Thu, 29 Jul 2021 21:07:44 GMT
   <
   * Connection #0 to host my-fqdn left intact
   * Closing connection 0
   ```

8. Verify that the reverse proxy to the IDM pod is running:

   ```
   $ curl --insecure -L -X GET https://my-fqdn/ig/openidm/info/ping -v
   ...
   * Using HTTP2, server supports multi-use
   * Connection state changed (HTTP/2 confirmed)
   * Copying HTTP/2 data in stream buffer to connection buffer after upgrade: len=0
   ...
   * Connection state changed (MAX_CONCURRENT_STREAMS == 128)!
   < HTTP/2 200
   ...
   ```

---

---
title: ForgeOps deployment monitoring
description: ForgeOps deployments optionally use Prometheus to monitor Ping Advanced Identity Software components and Kubernetes objects, Prometheus Alertmanager to send alert notifications, and Grafana to analyze metrics using dashboards.
component: forgeops
version: 2026.2
page_id: forgeops:prepare:monitoring/overview
canonical_url: https://docs.pingidentity.com/forgeops/2026.2/prepare/monitoring/overview.html
llms_txt: https://docs.pingidentity.com/forgeops/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Monitoring", "Prometheus", "Grafana", "Alertmanager"]
---

# ForgeOps deployment monitoring

ForgeOps deployments optionally use Prometheus to monitor Ping Advanced Identity Software components and Kubernetes objects, Prometheus Alertmanager to send alert notifications, and Grafana to analyze metrics using dashboards.

This topic describes the use of monitoring tools in ForgeOps deployments:

[icon: eye, set=fas, size=3x]

#### [Overview](https://docs.pingidentity.com/forgeops/2026.2/prepare/monitoring/monitoring-intro.html)

Monitoring installation and architecture.

[icon: fedora, set=fab, size=3x]

#### [Monitoring Pods](https://docs.pingidentity.com/forgeops/2026.2/prepare/monitoring/pods.html)

Prometheus and Grafana pods that monitor ForgeOps deployments and provide reporting services.

[icon: tachometer-alt, set=fas, size=3x]

#### [Grafana Dashboards](https://docs.pingidentity.com/forgeops/2026.2/prepare/monitoring/dashboards.html)

Grafana dashboards for the platform that are available in ForgeOps deployments.

[icon: exclamation, set=fas, size=3x]

#### [Prometheus Alerts](https://docs.pingidentity.com/forgeops/2026.2/prepare/monitoring/alerts.html)

Prometheus alerts for the platform that are available in ForgeOps deployments.

---

---
title: Monitoring pods
description: The following Prometheus and Grafana pods from the prometheus-operator project run in the monitoring namespace:
component: forgeops
version: 2026.2
page_id: forgeops:prepare:monitoring/pods
canonical_url: https://docs.pingidentity.com/forgeops/2026.2/prepare/monitoring/pods.html
llms_txt: https://docs.pingidentity.com/forgeops/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Monitoring", "Prometheus", "Alertmanager"]
---

# Monitoring pods

The following Prometheus and Grafana pods from the `prometheus-operator` project run in the `monitoring` namespace:

| Pod                                                      | Description                                                                                                                                               |
| -------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `alertmanager-prometheus-operator-kube-p-alertmanager-0` | Handles Prometheus alerts by grouping them together, filtering them, and then routing them to a receiver, such as a Slack channel.                        |
| `prometheus-operator-kube-state-metrics-...`             | Generates Prometheus metrics for cluster node resources, such as CPU, memory, and disk usage. One pod is deployed for each node in a ForgeOps deployment. |
| `prometheus-operator-prometheus-node-exporter-...`       | Generates Prometheus metrics for Kubernetes objects, such as deployments and nodes.                                                                       |
| `prometheus-operator-grafana-...`                        | Provides the Grafana service.                                                                                                                             |
| `prometheus-prometheus-operator-kube-p-prometheus-0`     | Provides the Prometheus service.                                                                                                                          |
| `prometheus-operator-kube-p-operator-...`                | Runs the Prometheus operator.                                                                                                                             |

See the [prometheus-operator Helm chart README file](https://github.com/helm/charts/blob/master/stable/prometheus-operator/README.md) for more information about the pods in the preceding table.

---

---
title: Network policies
description: Kubernetes network policies let you specify specify how pods are allowed to communicate with other pods, namespaces, and IP addresses.
component: forgeops
version: 2026.2
page_id: forgeops:prepare:security/network-policies
canonical_url: https://docs.pingidentity.com/forgeops/2026.2/prepare/security/network-policies.html
llms_txt: https://docs.pingidentity.com/forgeops/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Security", "Kubernetes", "Network"]
section_ids:
  deny_all_policy: deny-all policy
  ds_idrepo_ldap_policy: ds-idrepo-ldap policy
  ds_cts_ldap_policy: ds-cts-ldap policy
  ds_replication_policy: ds-replication policy
  backend_http_access_policy: backend-http-access policy
  front_end_http_access_policy: front-end-http-access policy
---

# Network policies

Kubernetes [network policies](https://kubernetes.io/docs/concepts/services-networking/network-policies) let you specify specify how pods are allowed to communicate with other pods, namespaces, and IP addresses.

The `forgeops` repository contains two sets of example network policies for the Ping Advanced Identity Software:

1. [Network policies for DS](https://github.com/ForgeRock/forgeops/blob/2026.2.1/kustomize/base/security/ds-netpolicy.yaml).

2. [Network policies for AM and IDM](https://github.com/ForgeRock/forgeops/blob/2026.2.1/kustomize/base/security/app-netpolicy.yaml).

Customize the example policies to meet your security needs, or use them to help you better understand how network policies can make Kubernetes deployments more secure.

All the example policies have the value `Ingress` in the `spec.policyTypes` key:

```
spec:
  policyTypes:
  - Ingress
```

Network policies with this policy type are called *ingress policies*, because they limit ingress traffic in a deployment.

## `deny-all` policy

By default, if no network policies exist in a namespace, then all ingress and egress traffic is allowed to and from pods in that namespace.

The `deny-all` policy modifies the default network policy for ingress. If a pod isn't selected by another network policy in the namespace, ingress is *not* allowed.

For information about how Kubernetes controls pod ingress when pods are selected by multiple network policies in a namespace, refer to [the Kubernetes documentation](https://kubernetes.io/docs/concepts/services-networking/network-policies/#isolated-and-non-isolated-pods).

## `ds-idrepo-ldap` policy

The `ds-idrepo-ldap` policy limits access to `ds-idrepo` pods. Access can only be requested over port 1389, 1636, or 8080, and must come from an `am`, `idm`, or `amster` pod.

This part of the network policy specifies that access must be requested over port *1389*, *1636*, or *8080*:

```
ingress:
- from:
  ...
  ports:
  - protocol: TCP
    port: 1389
  - protocol: TCP
    port: 1636
  - protocol: TCP
    port: 8080
```

This part of the network policy specifies that access must be from an `am`, `idm`, or `amster` pod:

```
ingress:
- from:
  - podSelector:
      matchExpressions:
      - key: app
        operator: In
        values:
        - am
        - idm
        - amster
```

Understanding the example network policies and how to customize them requires some knowledge about labels defined in ForgeOps deployments. For example, `am` pods are defined with a label, `app`, that has the value `am`. You'll find this label in /path/to/forgeops/kustomize/base/am/kustomization.yaml file:

```
commonLabels:
  app.kubernetes.io/name: am
  app.kubernetes.io/instance: am
  app.kubernetes.io/component: am
  app.kubernetes.io/part-of: forgerock
  tier: middle
  app: am
```

## `ds-cts-ldap` policy

The `ds-cts-ldap` policy limits access to `ds-cts` pods. Access can only be requested over port 1389, 1636, or 8080, and must come from an `am` or `amster` pod.

## `ds-replication` policy

`ds` pods in ForgeOps deployments are labeled with `tier: ds`; they're said to reside in the `ds` tier of the deployment.

The `ds-replication` policy limits access to the pods on the `ds` tier. This policy specifies that access to `ds` tier pods over port 8989 can only come from other pods in the same tier.

Note that port 8989 is the default DS replication port. This network policy ensures that only DS pods can access the replication port.

## `backend-http-access` policy

The `backend-http-access` policy limits access to the pods in the `middle` tier, which contains the `am`, `idm`, and `ig` pods. Access can only be requested over port 8080.

## `front-end-http-access` policy

The `front-end-http-access` policy limits access to the pods in the `ui` tier: the `login-ui`, `admin-ui`, and `end-user-ui` pods. Access can only be requested over port 8080.

Note that users send HTTPS requests for the Ping Advanced Identity Software UIs to the ingress controller over port 443. The ingress controller terminates TLS, and then forwards requests to the UI pods over port 8080.

---

---
title: New security features
description: New security features in ForgeOps 2026.2.
component: forgeops
version: 2026.2
page_id: forgeops:prepare:security/sec-features
canonical_url: https://docs.pingidentity.com/forgeops/2026.2/prepare/security/sec-features.html
llms_txt: https://docs.pingidentity.com/forgeops/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Security", "Secret Agent Operator"]
---

# New security features

New security features in ForgeOps 2026.2.

---

---
title: PingGateway deployment
description: Add PingGateway to a ForgeOps deployment.
component: forgeops
version: 2026.2
page_id: forgeops:prepare:ig/overview
canonical_url: https://docs.pingidentity.com/forgeops/2026.2/prepare/ig/overview.html
llms_txt: https://docs.pingidentity.com/forgeops/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
---

# PingGateway deployment

[icon: user-lock, set=fas, size=3x]

#### [Default PingGateway](https://docs.pingidentity.com/forgeops/2026.2/prepare/ig/deploy-default-ig.html)

Add PingGateway to a ForgeOps deployment.

[icon: user-shield, set=fas, size=3x]

#### [Custom PingGateway](https://docs.pingidentity.com/forgeops/2026.2/prepare/ig/deploy-custom-ig.html)

Build a custom PingGateway image and add it to a single-instance ForgeOps deployment.

---

---
title: Prepare to deploy in production
description: After you get your ForgeOps deployment up and running, you can add deployment customizations—options that are not part of an out-of-the-box ForgeOps deployment, but which you may need when you deploy in production.
component: forgeops
version: 2026.2
page_id: forgeops:prepare:overview
canonical_url: https://docs.pingidentity.com/forgeops/2026.2/prepare/overview.html
llms_txt: https://docs.pingidentity.com/forgeops/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
---

# Prepare to deploy in production

After you get your ForgeOps deployment up and running, you can add deployment customizations—options that are not part of an out-of-the-box ForgeOps deployment, but which you may need when you deploy in production.

[icon: play-circle, set=fas, size=3x]

#### [Production Deployment Overview](https://docs.pingidentity.com/forgeops/2026.2/start/start-here.html#build-own-service)

Customize, deploy, and maintain a production ForgeOps deployment.

[icon: door-open, set=fas, size=3x]

#### [Identity Gateway](https://docs.pingidentity.com/forgeops/2026.2/prepare/ig/overview.html)

Add PingGateway to your deployment.

[icon: stethoscope, set=fas, size=3x]

#### [Monitoring](https://docs.pingidentity.com/forgeops/2026.2/prepare/monitoring/overview.html)

Customize Prometheus monitoring and alerts.

[icon: user-lock, set=fas, size=3x]

#### [Security](https://docs.pingidentity.com/forgeops/2026.2/prepare/security/overview.html)

Customize the security features built into ForgeOps deployments.

[icon: floppy-disk-circle-arrow-right, set=fas, size=3x]

#### [Backup](https://docs.pingidentity.com/forgeops/2026.2/backup/overview.html)

Back up and restore data, such as identities and tokens.

---

---
title: Secret Agent operator
description: The open source Secret Agent operator generates all the secrets needed for ForgeOps deployments except for the DS master key and TLS key. When directory instances are created, certificate manager is called to generate these two keys.
component: forgeops
version: 2026.2
page_id: forgeops:prepare:security/secret-agent
canonical_url: https://docs.pingidentity.com/forgeops/2026.2/prepare/security/secret-agent.html
llms_txt: https://docs.pingidentity.com/forgeops/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Security", "Secret Agent Operator"]
page_aliases: ["preview:secret-agent.adoc"]
section_ids:
  secret_generation: Secret generation
  cloud-secret-management: Cloud secret management
  password-changes: Administration password changes
---

# Secret Agent operator

The open source Secret Agent operator generates all the secrets needed for ForgeOps deployments except for the DS master key and TLS key. When directory instances are created, certificate manager is called to generate these two keys.

In addition to generating secrets, the operator also integrates with Google Cloud Secret Manager, AWS Secrets Manager, and Azure Key Vault to manage secrets, providing cloud backup and retrieval for secrets.

The Secret Agent operator runs as a Kubernetes deployment that must be available before you can install AM, IDM, and DS.

## Secret generation

By default, the operator examines your namespace to determine whether it contains all the secrets that it manages for Ping Advanced Identity Software deployments. If any of the secrets it manages are not present, the operator generates them.

Refer to the Secret Agent project README for information about:

* [Importing your own secrets](https://github.com/ForgeRock/secret-agent#importing-your-own-secrets)

* [Secret Agent naming conventions](https://github.com/ForgeRock/secret-agent#naming-convention-for-cloud-backups)

* [Modifying the Secret Agent configuration](https://github.com/ForgeRock/secret-agent#secret-agent-configuration-schema)

## Cloud secret management

Configuring the Secret Agent operator to integrate with a cloud secret manager, such as Google Cloud Secret Manager, AWS Secret Manager, or Azure Key Vault, changes the operator's behavior:

* First, the operator examines your namespace to determine whether it contains all the secrets it manages for Ping Advanced Identity Software deployments.

* If any of the secrets it manages are not in your namespace, the operator checks to refer to if the missing secrets are available in the cloud secret manager:

  * If any of the secrets missing from your namespace are available in the cloud secret manager, the operator gets them from the cloud secret manager and adds them to your namespace.

  * If missing secrets are not available in the cloud secret manager, the Secret Agent operator generates them.

Configure cloud secret management when you have multiple Ping Advanced Identity Software deployments that need to use the same secrets.

Refer to the Secret Agent project README for information about how to configure the Secret Agent operator for cloud secret management using these cloud secret managers:

* [Google Cloud Secret Manager](https://github.com/ForgeRock/secret-agent#set-up-cloud-backup-with-gcp-secret-manager)

* [AWS Secret Manager](https://github.com/ForgeRock/secret-agent#set-up-cloud-backup-with-aws-secret-manager)

* [Azure Key Vault](https://github.com/ForgeRock/secret-agent#set-up-cloud-backup-with-azure-key-vault)

## Administration password changes

ForgeOps deployments use these administration passwords:

* The AM and IDM administration user, `amadmin`

* The AM application store service account, `uid=am-config,ou=admins,ou=am-config`

* The AM CTS service account, `uid=openam_cts,ou=admins,ou=famrecords,ou=openam-session,ou=tokens`

* The shared identity repository service account, `uid=am-identity-bind-account,ou=admins,ou=identities`

* The DS root user, `uid=admin`

Some organizations have a requirement to change administration passwords from time to time. Follow these steps if you need to change the administration passwords:

1. Set the value of the `secretsManagerPrefix` key to `prod` in your [Secret Agent configuration](https://github.com/ForgeRock/secret-agent#naming-convention-for-cloud-backups).

   You can set the value of the `secretsManagerPrefix` key to any prefix you like. These steps use `prod` as an example prefix.

2. Change the `amadmin` user's password:

   1. Change to the bin directory in your `forgeops` repository clone.

   2. Run the forgeops info command. Note the current password for the `amadmin` user.

   3. If you've enabled [cloud secret management](#cloud-secret-management), delete the entry that contains the `amadmin` user's password from the cloud secret manager:

      > **Collapse: Google Cloud**
      >
      > List the secrets managed by the cloud secret manager, locate the URI for the secret that contains the `AM-PASSWORDS-AMADMIN-CLEAR` password, and delete it. For example:
      >
      > ```
      > $ gcloud secrets list --uri
      > $ gcloud secrets delete \
      >  https://secretmanager.googleapis.com/.../prod-am-env-secrets-AM-PASSWORDS-AMADMIN-CLEAR
      > ```

      > **Collapse: AWS**
      >
      > List the secrets managed by the cloud secret manager, locate the ARN for the secret that contains the `AM-PASSWORDS-AMADMIN-CLEAR` password, and delete it. For example:
      >
      > ```
      > $ aws secretsmanager list-secrets --region=my-region
      > $ aws secretsmanager delete-secret --region=my-region \
      >  --force-delete-without-recovery \
      >  --secret-id arn:aws:secretsmanager:...:prod-am-env-secrets-AM-PASSWORDS-AMADMIN-CLEAR-c3KfsL
      > ```

      > **Collapse: Azure**
      >
      > Soft delete the secret that contains the `AM-PASSWORDS-AMADMIN-CLEAR` password from Azure Key Vault. For example:
      >
      > ```
      > $ az keyvault secret delete --vault-name my-key-vault --name prod-am-env-secrets-AM-PASSWORDS-AMADMIN-CLEAR
      > ```
      >
      > Purge the soft deleted secret from Azure Key Vault. For example:
      >
      > ```
      > $ az keyvault secret purge --vault-name my-key-vault --name prod-am-env-secrets-AM-PASSWORDS-AMADMIN-CLEAR
      > ```

   4. Make the namespace where the platform is deployed the active namespace in your local Kubernetes context.

   5. Delete the Kubernetes secret that contains the `amadmin` user's password from the namespace in which the platform is deployed:

      ```
      $ kubectl patch secrets am-env-secrets --type=json \
       --patch='[{"op":"remove", "path": "/data/AM_PASSWORDS_AMADMIN_CLEAR"}]'
      ```

   6. Restart AM by deleting all active AM pods: list all the pods in the namespace where you deployed the platform and then delete all the pods running AM.

   7. After AM comes up, run the forgeops info command again to get the current administration passwords.

      Verify that the `amadmin` user's password has changed by comparing its previous value to its current value.

   8. Verify that you can log in to the platform UI using the new password.

3. Change the AM application store service account's password:

   1. Change to the bin directory in your `forgeops` repository clone.

   2. Run the forgeops info command. Note the current password for the AM application store service account.

   3. If you've enabled [cloud secret management](#cloud-secret-management), delete the entry that contains this account's password from the cloud secret manager:

      > **Collapse: Google Cloud**
      >
      > List the secrets managed by the cloud secret manager, locate the URI for the secret that contains the `AM_STORES_APPLICATION_PASSWORD` password, and delete it. For example:
      >
      > ```
      > $ gcloud secrets list --uri
      > $ gcloud secrets delete \
      >  https://secretmanager.googleapis.com/.../prod-ds-env-secrets-AM_STORES_APPLICATION_PASSWORD
      > ```

      > **Collapse: AWS**
      >
      > List the secrets managed by the cloud secret manager, locate the ARN for the secret that contains the `AM_STORES_APPLICATION_PASSWORD` password, and delete it. For example:
      >
      > ```
      > $ aws secretsmanager list-secrets --region=my-region
      > $ aws secretsmanager delete-secret --region=my-region \
      >  --force-delete-without-recovery \
      >  --secret-id arn:aws:secretsmanager:...:prod-ds-env-secrets-AM_STORES_APPLICATION_PASSWORD-1d4432
      > ```

      > **Collapse: Azure**
      >
      > Soft delete the secret that contains the `AM_STORES_APPLICATION_PASSWORD` password from Azure Key Vault. For example:
      >
      > ```
      > $ az keyvault secret delete --vault-name my-key-vault --name prod-ds-env-secrets-AM_STORES_APPLICATION_PASSWORD
      > ```
      >
      > Purge the deleted secret from Azure Key Vault. For example:
      >
      > ```
      > $ az keyvault secret purge --vault-name my-key-vault --name prod-ds-env-secrets-AM_STORES_APPLICATION_PASSWORD
      > ```

   4. Make the namespace where the platform is deployed the active namespace in your local Kubernetes context.

   5. Delete the Kubernetes secret that contains the service account's password from the namespace where the platform is deployed:

      ```
      $ kubectl patch secrets ds-env-secrets --type=json \
       --patch='[{"op":"remove", "path": "/data/AM_STORES_APPLICATION_PASSWORD"}]'
      ```

   6. Remove your ForgeOps deployment. Be sure to reply `N` when you're prompted to delete PVCs, volume snapshots, and secrets:

      ```
      $ cd /path/to/forgeops/bin
      $ ./forgeops delete
      "small" platform detected in namespace: "my-namespace".
      Uninstalling component(s): ['all'] from namespace: "my-namespace".
      OK to delete components? [Y/N] Y
      OK to delete PVCs? [Y/N] N
      OK to delete volume snapshots? [Y/N] N
      OK to delete secrets? [Y/N] N
      service "admin-ui" deleted
      ...
      ```

   7. Redeploy the platform:

      ```
      $ forgeops apply --small --fqdn my-fqdn
      ```

   8. Review the administration passwords listed in the forgeops install command's' output.

      Verify that the AM application store service account's password has changed by comparing its previous value to its current value.

4. Change the CTS service account's password:

   1. Change to the bin directory in your `forgeops` repository clone.

   2. Run the forgeops info command. Note the current password for the identity repository service account.

   3. If you've enabled [cloud secret management](#cloud-secret-management), delete the entry that contains this account's password from the cloud secret manager:

      > **Collapse: Google Cloud**
      >
      > List the secrets managed by the cloud secret manager, locate the URI for the secret that contains the `AM_STORES_CTS_PASSWORD` password, and delete it. For example:
      >
      > ```
      > $ gcloud secrets list --uri
      > $ gcloud secrets delete \
      >  https://secretmanager.googleapis.com/.../prod-ds-env-secrets-AM_STORES_CTS_PASSWORD
      > ```

      > **Collapse: AWS**
      >
      > List the secrets managed by the cloud secret manager, locate the ARN for the secret that contains the `AM_STORES_CTS_PASSWORD` password, and delete it. For example:
      >
      > ```
      > $ aws secretsmanager list-secrets --region=my-region
      > $ aws secretsmanager delete-secret --region=my-region \
      >  --force-delete-without-recovery \
      >  --secret-id arn:aws:secretsmanager:...:prod-ds-env-secrets-AM_STORES_CTS_PASSWORD-1d4432
      > ```

      > **Collapse: Azure**
      >
      > Delete the secret that contains the `AM_STORES_CTS_PASSWORD` password from Azure Key Vault. For example:
      >
      > ```
      > $ az keyvault secret delete --vault-name my-key-vault --name prod-ds-env-secrets-AM_STORES_CTS_PASSWORD
      > ```
      >
      > Purge the deleted secret from Azure Key Vault. For example:
      >
      > ```
      > $ az keyvault secret purge --vault-name my-key-vault --name prod-ds-env-secrets-AM_STORES_CTS_PASSWORD
      > ```

   4. Make the namespace where the platform is deployed the active namespace in your local Kubernetes context.

   5. Delete the Kubernetes secret that contains the service account's password from the namespace where the platform is deployed:

      ```
      $ kubectl patch secrets ds-env-secrets --type=json \
       --patch='[{"op":"remove", "path": "/data/AM_STORES_CTS_PASSWORD"}]'
      ```

   6. Remove your ForgeOps deployment. Be sure to reply `N` when you're prompted to delete PVCs, volume snapshots, and secrets:

      ```
      $ cd /path/to/forgeops/bin
      $ ./forgeops delete
      "small" platform detected in namespace: "my-namespace".
      Uninstalling component(s): ['all'] from namespace: "my-namespace".
      OK to delete components? [Y/N] Y
      OK to delete PVCs? [Y/N] N
      OK to delete volume snapshots? [Y/N] N
      OK to delete secrets? [Y/N] N
      service "admin-ui" deleted
      ...
      ```

   7. Redeploy the platform:

      ```
      $ forgeops apply --small --fqdn my-fqdn
      ```

   8. Review the administration passwords listed in the forgeops install command's' output.

      Verify that the CTS service account's password has changed by comparing its previous value to its current value.

5. Change the identity repository service account's password:

   1. Change to the bin directory in your `forgeops` repository clone.

   2. Run the forgeops info command. Note the current password for the identity repository service account.

   3. If you've enabled [cloud secret management](#cloud-secret-management), delete the entry that contains this account's password from the cloud secret manager:

      > **Collapse: Google Cloud**
      >
      > List the secrets managed by the cloud secret manager, locate the URI for the secret that contains the `AM_STORES_USER_PASSWORD` password, and delete it. For example:
      >
      > ```
      > $ gcloud secrets list --uri
      > $ gcloud secrets delete \
      >  https://secretmanager.googleapis.com/.../prod-ds-env-secrets-AM_STORES_USER_PASSWORD
      > ```

      > **Collapse: AWS**
      >
      > List the secrets managed by the cloud secret manager, locate the ARN for the secret that contains the `AM_STORES_USER_PASSWORD` password, and delete it. For example:
      >
      > ```
      > $ aws secretsmanager list-secrets --region=my-region
      > $ aws secretsmanager delete-secret --region=my-region \
      >  --force-delete-without-recovery \
      >  --secret-id arn:aws:secretsmanager:...:prod-ds-env-secrets-AM_STORES_USER_PASSWORD-1d4432
      > ```

      > **Collapse: Azure**
      >
      > Soft delete the secret that contains the `AM_STORES_USER_PASSWORD` password from Azure Key Vault. For example:
      >
      > ```
      > $ az keyvault secret delete --vault-name my-key-vault --name prod-ds-env-secrets-AM_STORES_USER_PASSWORD
      > ```
      >
      > Purge the deleted secret from Azure Key Vault. For example:
      >
      > ```
      > $ az keyvault secret purge --vault-name my-key-vault --name prod-ds-env-secrets-AM_STORES_USER_PASSWORD
      > ```

   4. Make the namespace where the platform is deployed the active namespace in your local Kubernetes context.

   5. Delete the Kubernetes secret that contains the service account's password from the namespace where the platform is deployed:

      ```
      $ kubectl patch secrets ds-env-secrets --type=json \
       --patch='[{"op":"remove", "path": "/data/AM_STORES_USER_PASSWORD"}]'
      ```

   6. Remove your ForgeOps deployment. Be sure to reply `N` when you're prompted to delete PVCs, volume snapshots, and secrets:

      ```
      $ cd /path/to/forgeops/bin
      $ ./forgeops delete
      "small" platform detected in namespace: "my-namespace".
      Uninstalling component(s): ['all'] from namespace: "my-namespace".
      OK to delete components? [Y/N] Y
      OK to delete PVCs? [Y/N] N
      OK to delete volume snapshots? [Y/N] N
      OK to delete secrets? [Y/N] N
      service "admin-ui" deleted
      ...
      ```

   7. Redeploy the platform:

      ```
      $ forgeops apply --small --fqdn my-fqdn
      ```

   8. Review the administration passwords listed in the forgeops install command's' output.

      Verify that the identity repository service account's password has changed by comparing its previous value to its current value.

6. Change the DS root user's password:

   1. Change to the bin directory in your `forgeops` repository clone.

   2. Run the forgeops info command. Note the current password for the `uid=admin` account.

   3. If you've enabled [cloud secret management](#cloud-secret-management), delete the entry that contains this account's password from the cloud secret manager:

      > **Collapse: Google Cloud**
      >
      > List the secrets managed by the cloud secret manager, locate the URI for the secret that contains the `dirmanager-pw` password, and delete it. For example:
      >
      > ```
      > $ gcloud secrets list --uri
      > $ gcloud secrets delete \
      >  https://secretmanager.googleapis.com/.../prod-ds-passwords-dirmanager-pw
      > ```

      > **Collapse: AWS**
      >
      > List the secrets managed by the cloud secret manager, locate the ARN for the secret that contains the `dirmanager-pw` password, and delete it. For example:
      >
      > ```
      > $ aws secretsmanager list-secrets --region=my-region
      > $ aws secretsmanager delete-secret --region=my-region \
      >  --force-delete-without-recovery \
      >  --secret-id arn:aws:secretsmanager:...:prod-ds-passwords-dirmanager-pw-2eeaa0
      > ```

      > **Collapse: Azure**
      >
      > Soft delete the secret that contains the `dirmanager-pw` password from Azure Key Vault. For example:
      >
      > ```
      > $ az keyvault secret delete --vault-name my-key-vault --name prod-ds-passwords-dirmanager-pw
      > ```
      >
      > Purge the deleted secret from Azure Key Vault. For example:
      >
      > ```
      > $ az keyvault secret purge --vault-name my-key-vault --name prod-ds-passwords-dirmanager-pw
      > ```

   4. Make the namespace where the platform is deployed the active namespace in your local Kubernetes context.

   5. Delete the Kubernetes secret that contains the service account's password from the namespace where the platform is deployed:

      ```
      $ kubectl patch secrets ds-passwords --type=json \
       --patch='[{"op":"remove", "path": "/data/dirmanager.pw"}]'
      ```

   6. Remove your ForgeOps deployment. Be sure to reply `N` when you're prompted to delete PVCs, volume snapshots, and secrets:

      ```
      $ cd /path/to/forgeops/bin
      $ ./forgeops delete
      "small" platform detected in namespace: "my-namespace".
      Uninstalling component(s): ['all'] from namespace: "my-namespace".
      OK to delete components? [Y/N] Y
      OK to delete PVCs? [Y/N] N
      OK to delete volume snapshots? [Y/N] N
      OK to delete secrets? [Y/N] N
      service "admin-ui" deleted
      ...
      ```

   7. Redeploy the platform:

      ```
      $ forgeops apply --small --fqdn my-fqdn
      ```

   8. Review the administration passwords listed in the forgeops install command's' output.

      Verify that the password for the `uid=admin` account has changed by comparing its previous value to its current value.

---

---
title: Secrets Rotation
description: Secrets rotation is the process of updating or replacing sensitive information stored as Kubernetes secrets. Secrets rotation is crucial for maintaining strong security and mitigating risks of unauthorized access or data breaches.
component: forgeops
version: 2026.2
page_id: forgeops:prepare:security/secrets-rotation
canonical_url: https://docs.pingidentity.com/forgeops/2026.2/prepare/security/secrets-rotation.html
llms_txt: https://docs.pingidentity.com/forgeops/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Security", "Secret Generator", "Secrets Rotation"]
section_ids:
  introduction: Introduction
  performing_secrets_and_passwords_rotation: Performing secrets and passwords rotation
  rotating_ds_env_secrets: Rotating ds-env-secrets
  rotating_ds_passwords: Rotating ds-passwords
  rotating_amster_secret: Rotating amster secret
  rotating_am_env_secrets: Rotating am-env-secrets
  rotating_amster_env_secrets: Rotating amster-env-secrets
  rotating_idm_env_secrets: Rotating idm-env-secrets
  rotating_ds_ssl_keypair: Rotating ds-ssl-keypair
  rotating_am_passwords: Rotating am-passwords
  rotating_ds_master_keypair: Rotating ds-master-keypair
  add-cust-cert: Adding custom certificate to the truststore
---

# Secrets Rotation

## Introduction

Secrets rotation is the process of updating or replacing sensitive information stored as Kubernetes secrets. Secrets rotation is crucial for maintaining strong security and mitigating risks of unauthorized access or data breaches.

In a multi-component system, such as a ForgeOps deployment, each component interacts with others using secrets. Therefore, it's important to consider dependencies among components and perform secrets rotation while maintaining consistent interaction among dependent components.

The forgeops command includes the rotate sub-command to enable `ds-env-secrets` and `ds-passwords` rotation consistently. You can rotate other ForgeOps required secrets also with due consideration to the impact on dependent components and downtime.

## Performing secrets and passwords rotation

This section describes how to rotate secrets and password in ForgeOps deployments. The steps for rotating each secret are mentioned separately for easier understanding and usage.

### Rotating `ds-env-secrets`

The `ds-env-secrets` controls access to DS from AM and IDM, and would normally cause a downtime when rotated. To avoid such a downtime, the forgeops rotate command creates old-ds-env-secrets temporarily to contain old secrets.

In ForgeOps release 2025.2.1, the DS image was built to accommodate multiple passwords. This enables secrets rotation with no downtime.

* For deployments using DS images from 2025.1 or earlier

  If you are using the DS image from the 2025.1 release or earlier, then perform these steps to enable multiple passwords in DS.

  1. In your terminal window, set up environment variables to get the password and connection string (DSPASS and CONN\_STR):

     ```
     $ export DSPASS=$(kubectl get secret ds-passwords -n my_ns -o yaml | yq '.data["dirmanager.pw"]' | tr -d '"' | base64 -d -i -)

     $ export CONN_STR="--hostname localhost --port 4444 --bindDn uid=admin --trustAll --no-prompt --bindPassword $DSPASS"
     ```

  2. Set up DS pods to enable multiple passwords:

     ```
     $ kubectl exec -it ds-cts-0 — bin/dsconfig set-password-policy-prop \
       set-password-policy-prop --policy-name "Default Password Policy" \
       --set allow-multiple-password-values:true $CONN_STR

     $ kubectl exec -it ds-cts-0 — bin/dsconfig set-password-policy-prop \
       set-password-policy-prop --policy-name "Root Password Policy" \
       --set allow-multiple-password-values:true $CONN_STR

     $ kubectl exec -it ds-idrepo-0 — bin/dsconfig set-password-policy-prop \
       set-password-policy-prop --policy-name "Default Password Policy" \
       --set allow-multiple-password-values:true $CONN_STR

     $ kubectl exec -it ds-idrepo-0 — bin/dsconfig set-password-policy-prop \
       set-password-policy-prop --policy-name "Root Password Policy" \
       --set allow-multiple-password-values:true $CONN_STR
     ```

To rotate `ds-env-secrets`, run the forgeops rotate --namespace my\_ns ds-env-secrets command.

The command prompts you to perform steps to complete rotation of `ds-env-secrets`.

### Rotating `ds-passwords`

To rotate `ds-passwords`, run the forgeops rotate --namespace my\_ns ds-passwords command. The command prompts you to perform steps to complete rotation of `ds-passwords`.

You must restart the DS pods to update the `admin` user password because that password is set on DS pod startup. This could also require restarting some services instead of redeploying components.

At the end of its successful run, the forgeops rotate command prompts the user to:

* Delete the temporary secrets.

* Remove the old passwords.

### Rotating `amster` secret

* Impact

  This secret is specific to Amster and doesn't cause a downtime.

* Procedure

  1. Trigger renewal of Kubernetes secret:

     ```
     $ kubectl delete secret amster
     ```

  2. Rolling restart AM pods to pick up new `amster` secret:

     ```
     $ kubectl rollout restart deployment am -n my-ns
     ```

  3. Refresh amster job to verify `amster` can access AM:

     1. Delete amster job to allow redeployment:

        ```
        $ kubectl delete job amster -n my-ns
        ```

     2. Deploy platform changes (`amster`)

        1. For Helm:

           ```
           $ helm upgrade -i identity-platform --repo https://ForgeRock.github.io/forgeops/ \
            --version my-prod-version \
            --values /path/to/forgeops/helm/my-env/values.yaml
           ```

        2. For Kustomize:

           ```
           $ forgeops apply amster --env-name my-env
           ```

  4. Ensure that the `amster import` process has completed successfully:

     ```
     $ kubectl logs -f amster-pod -n my-ns
     ```

### Rotating `am-env-secrets`

* Impact

  AM depends on this secret for authentication. Therefore, during the short time between restarting AM and rerunning Amster, requests that need authentication could fail.

* Procedure

  1. Trigger renewal of Kubernetes secret:

     ```
     $ kubectl delete secret am-env-secrets
     ```

  2. Rolling restart AM pods to pick up new amster secret:

     ```
     $ kubectl rollout restart deployment am -n my-ns
     ```

  3. Reinitiate the amster job:

     1. Delete the amster job to allow redeployment:

        ```
        $ kubectl delete job amster -n my-ns
        ```

     2. Redeploy `amster`:

        1. For Helm:

           ```
           $ helm upgrade -i identity-platform --repo https://ForgeRock.github.io/forgeops/ \
             --values /path/to/forgeops/helm/my-env/values.yaml
           ```

        2. For Kustomize:

           ```
           $ forgeops apply amster --env-name my-env
           ```

  4. Ensure that the amster import process has completed successfully:

     ```
     $ kubectl logs -f amster-pod -n my-ns
     ```

  5. Retrieve the new password for `amadmin` user to log in to the platform:

     ```
     $ forgeops info | grep amadmin
     ```

  6. Log in to the platform with new `amadmin` password to verify the platform is up and running.

### Rotating `amster-env-secrets`

* Impact

  In the very short time between restarting IDM and Amster importing necessary data, the platform isn't accessible. Amster takes a few seconds to import data.

* Procedure

  1. Trigger renewal of Kubernetes secret:

     ```
     $ kubectl delete secret amster-env-secrets
     ```

  2. Rolling restart IDM pods to get the new amster secret:

     ```
     $ kubectl rollout restart deployment idm -n my-ns
     ```

  3. Rerun the `amster` job to import the new secrets:

     1. Delete the `amster` job to allow redeployment:

        ```
        $ kubectl delete job amster -n my-ns
        ```

     2. Redeploy Amster:

        1. When using Helm to deploy:

           ```
           $ helm upgrade -i identity-platform --repo https://ForgeRock.github.io/forgeops/ --values /path/to/custom/values.yaml
           ```

        2. When using Kustomize deploy:

           ```
           $ forgeops apply --env-name my-env amster
           ```

### Rotating idm-env-secrets

* Procedure

  1. Trigger renewal of Kubernetes secret:

     ```
     $ kubectl delete secret idm-env-secrets
     ```

  2. Rolling restart IDM pods:

     ```
     $ kubectl rollout restart deployment idm
     ```

  3. Check pods have come up:

     ```
     $ kubectl get pods -l app.kubernetes.io/component=idm -n my-ns
     ```

### Rotating `ds-ssl-keypair`

|   |                                                                                                                                        |
| - | -------------------------------------------------------------------------------------------------------------------------------------- |
|   | It's not advisable to rotate this secret. If you rotate this secret DS data replication will fail until all the DS pods are restarted. |

* Procedure

  1. Delete the `ds-ssl-keypair` secret:

     ```
     $ kubectl delete secret ds-ssl-keypair -n my-ns
     ```

  2. Check that the secret is recreated:

     ```
     $ kubectl get secret ds-ssl-keypair -n my-ns
     ```

  3. Rolling restart `ds-cts` pods to pick up new secret:

     ```
     $ kubectl rollout restart sts ds-cts -n my-ns
     ```

  4. Rolling restart `ds-idrepo` pods to pick up new secret:

     ```
     $ kubectl rollout restart sts ds-idrepo -n my-ns
     ```

  5. Rolling restart AM pods to pick up new secret:

     ```
     $ kubectl rollout restart deployment am -n my-ns
     ```

  6. Rolling restart IDM pods to pick up new secret:

     ```
     $ kubectl rollout restart deployment idm -n my-ns
     ```

  7. Check pods to ensure they have come back up:

     ```
     $ kubectl get pods -l app.kubernetes.io/component=ds-cts -n my-ns
     $ kubectl get pods -l app.kubernetes.io/component=ds-idrepo -n my-ns
     $ kubectl get pods -l app.kubernetes.io/component=am -n my-ns
     $ kubectl get pods -l app.kubernetes.io/component=idm -n my-ns
     ```

### Rotating `am-passwords`

* Impact

  Rotating `am-passwords` doesn't necessitate a down-time. `am-passwords` is used only in ForgeOps deployments that use `secret agent` for secrets management. It's not relevant for deployments that use `secrets generator`.

* Procedure

  1. Trigger renewal of Kubernetes secret:

     ```
     $ kubectl delete secret am-passwords
     $ kubectl delete secret am-keystore
     ```

  2. Delete the AM pod:

     ```
     $ kubectl delete pod am-wxyz-abcd
     ```

  3. Recreate keystore to use the new secret.

### Rotating `ds-master-keypair`

|   |                                                                                                                                                                                                                                                                                                                 |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | **Do not rotate `ds-master-keypair` because it's used in DS data backups**. The same secret is required to decrypt data when you need to restore from backups. If you must rotate these secrets, then restart backups and discard the previous backups because they can't be used for restoring directory data. |

### Adding custom certificate to the truststore

The following environment variables are used to point to the paths for certificates. You don't need to update any of it.

* **AM\_DEFAULT\_TRUSTSTORE**: PingAM and PingIDM now use the default Java ca certificate as the default truststore.

* **AM\_PEM\_TRUSTSTORE**: Custom user-supplied certificates to append to the truststore.

* **AM\_PEM\_TRUSTSTORE\_DS**: The DS SSL key pair used for LDAPS connectivity between PingAM and PingDS.

The following procedure helps in adding user supplied certificates to the truststore for PingAM and PingIDM. **Certificates should be in pem format.**

* In a Helm based deployment

  * (Option 1) Provide the certificate using a manually created secret. This is the preferred option.

    1. Set `platform.truststore.secret.enabled` to "true".

    2. Ensure `truststore.secret.create` is set to "false".

    3. Create a Kubernetes secret containing certificate:

       ```
       $ kubectl --namespace my-namespace create secret generic \
        platform-truststore-certificates --from-file=/path/to/my-certificates
       ```

  * (Option 2) Provide certificate content in `values.yaml`. This option is useful for testing purposes or if you only have a single certificate.

    1. Set `platform.truststore.secret.enabled` to "true".

    2. Set `platform.truststore.secret.create` to "true".

    3. Add the content of the certificate to `platform.truststore.secret.certificates`.

* In a Kustomize based deployment

  1. Create a Kubernetes secret containing the certificate:

     ```
     $ kubectl --namespace my-namespace create secret generic \
       platform-truststore-certificates --from-file=/path/to/my-certificates
     ```

* Add an existing secret containing custom certificates to the truststore

  1. (Option 1) Recreate your current secret with the name `platform-truststore-certificates` to match the previous steps.

  2. (Option 2) In the overlay file of your environment, update the mount points where `platform-truststore-certificates` is configured with the name of your custom secret.

---

---
title: Secure HTTP
description: ForgeOps deployments use a TLS-enabled ingress controller to enable secure communication to the cluster[1]. Incoming requests and outgoing responses are encrypted. TLS is terminated at the ingress controller.
component: forgeops
version: 2026.2
page_id: forgeops:prepare:security/https
canonical_url: https://docs.pingidentity.com/forgeops/2026.2/prepare/security/https.html
llms_txt: https://docs.pingidentity.com/forgeops/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Security", "SSL/TLS"]
section_ids:
  tls-certificate: TLS certificate
  mkcert: Certificate generated by the mkcert utility
---

# Secure HTTP

ForgeOps deployments use a TLS-enabled ingress controller to enable secure communication to the cluster\[[1](#_footnotedef_1 "View footnote.")]. Incoming requests and outgoing responses are encrypted. TLS is terminated at the ingress controller.

By default, ForgeOps installs Traefik on AKS, EKS, and GKE clusters, and ingress-nginx on minikube\[[2](#_footnotedef_2 "View footnote.")]. The /path/to/forgeops/kustomize/base/ingress/ingress.yaml file contains an annotation—`cert-manager.io/cluster-issuer`—that configures the Traefik to use [cert-manager](https://github.com/jetstack/cert-manager) software for certificate management\[[3](#_footnotedef_3 "View footnote.")].

The forgeops apply command installs the `cert-manager` utility in the `cert-manager` namespace and configures `cert-manager` to generate self-signed certificates for securing communication into the ingress.

When self-signed certificates are used, communication is encrypted, but users receive warnings about insecure communication from some browsers. Because of this, self-signed certificates are suitable for test environments only.

For all other environments, reconfigure certificate management. Two common configurations are:

* Using a certificate with a trust chain that starts at a trusted root certificate—Communication is encrypted, and users do not receive warnings from their browsers.

  [TLS certificate](#tls-certificate) contains a simple example of how to deploy a certificate from a trusted authority in a ForgeOps deployment. The steps in the example:

  * Remove the cert-manager annotation from the ingress.

  * Create a secret named `tls-myfqdn` (for example:tls-forgeops.example.com) that contains the certificate you want to use in your deployment.

* Using a dynamically obtained certificate from [Let's Encrypt](https://letsencrypt.org/)—Communication is encrypted and users do not receive warnings from their browsers.

  You reconfigure cert-manager to use a ClusterIssuer that calls Let's Encrypt to obtain a certificate and installs the certificate as a Kubernetes secret.

There are many options for certificate management in a Ping Advanced Identity Software deployment. For more information about configuring certificate manager, refer to the [cert-manager documentation](https://cert-manager.io/docs).

## TLS certificate

The forgeops apply command installs [cert-manager software](https://cert-manager.io/docs). Similarly, when using Helm, the default ForgeOps deployment requires `cert-manager` annotations.

When the `default-issuer` is used, the ingress controller in ForgeOps deployments is configured to use the self-signed certificate\[[4](#_footnotedef_4 "View footnote.")]. This is the simplest encryption option—you don't have to make any changes to your deployment to get encryption.

However, when you access one of the Ping Identity web applications from your browser, you'll get a "Not Secure" message from your browser. Users will need to bypass the message.

If you have a certificate from a CA, or a [certificate generated by the mkcert utility](#mkcert), you can use your certificate for TLS encryption instead of the default self-signed certificate:

1. Obtain the certificate:

   * Make sure that the certificate is PEM-encoded.

   * A best practice is to include the entire chain of trust with your certificate.

2. Make sure that the deployment FQDN (that you specified in your /etc/hosts file) works with your certificate. Refer to the hostname resolution page for your cluster provider: [Google Cloud](../../setup/google-cloud.html#gcp-ingress) | [AWS](../../setup/aws.html#aws-ingress) | [Azure](../../setup/azure.html#azure-ingress) | [minikube](../../setup/minikube.html#minikube-ingress).

3. Remove cert-manager's annotation from the ingress definition:

   1. If you are using Kustomize, run the kubectl annotate command:

      ```
      $ kubectl annotate ingress forgerock cert-manager.io/cluster-issuer-
      ```

   2. If you are using Helm, edit the charts/identity-platform/values.yaml file and set `cert_manager.enabled` to false:

      ```
      ...
      cert_manager:

          enabled: false
      ```

4. Delete the certificate resource originally created by cert-manager:

   ```
   $ kubectl delete certificate tls-myfqdn
   ```

5. Update your tls-myfqdn secret with your certificate. For example:

   ```
   $ kubectl create secret tls tls-myfqdn --cert=/path/to/my-cert.crt --key=/path/to/my-key.key \
     --dry-run=client -o yaml | kubectl replace -f -
   ```

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | 1) If you have SSL certificate and do not want to use TLS certificates, then you can use your custom SSL certificate in your ForgeOps deployment environment:

   ```
   forgeops env --env-name my-env --ssl-secretname my-ssl-secret
   ```

2) If you disable `cert-manager` in the Helm chart, `cert-manager` is disabled for all certificates including the `ds-ssl-keypair` secret. You must create a custom version of that secret as well. |

## Certificate generated by the mkcert utility

If you don't have a certificate from a CA, you can use the mkcert utility to generate a locally trusted certificate. In many cases, it's acceptable to use mkcert certificates for development purposes.

To use a certificate generated by the mkcert utility in a ForgeOps deployment that uses `my-fqdn` as the deployment FQDN:

1. If you don't have mkcert software installed locally, [install it](https://github.com/FiloSottile/mkcert#installation). Firefox users must install certutil software. Refer to the mkcert installation instructions for more information.

2. If you haven't ever done so, run the mkcert -install command to create a local certificate authority (CA) and install it in your system root store. Restart your browser after creating the local CA.

3. Create a wildcard certificate for the `example.com` domain:

   ```
   $ cd
   $ mkcert "*.example.com"
   ```

   The mkcert utility generates the certificate file as \_wildcard.example.com.pem and the private key file as \_wildcard.example.com-key.pem. Use these two file names when you create the Kubernetes TLS secret.

***

[1](#_footnoteref_1). To access DS, refer to [DS command-line access.](../../deploy/access.html#ds_command_line_access)[2](#_footnoteref_2). If you prefer to use a different ingress controller, deploy infrastructure in Kubernetes to support it.[3](#_footnoteref_3). Traefik and cert-manager are evolving technologies. Descriptions of these technologies were accurate at the time of this writing, but might differ when you deploy them.[4](#_footnoteref_4). For more information on howto change the default behavior, refer to [the steps for creatingTLS certificate](#mkcert-use).

---

---
title: Security
description: This topic describes some security options in a ForgeOps deployment:
component: forgeops
version: 2026.2
page_id: forgeops:prepare:security/overview
canonical_url: https://docs.pingidentity.com/forgeops/2026.2/prepare/security/overview.html
llms_txt: https://docs.pingidentity.com/forgeops/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
---

# Security

This topic describes some security options in a ForgeOps deployment:

[icon: lock, set=fas, size=3x]

#### [Secure Communications](https://docs.pingidentity.com/forgeops/2026.2/prepare/security/https.html)

Secure HTTP and certificate management.

[icon: id-card, set=fas, size=3x]

#### [IP Address Restriction](https://docs.pingidentity.com/forgeops/2026.2/prepare/security/restrict-access-ip-address.html)

Access restriction by incoming IP address, enforced by the ingress controller.

[icon: network-wired, set=fas, size=3x]

#### [Network Policies](https://docs.pingidentity.com/forgeops/2026.2/prepare/security/network-policies.html)

Secure cross-pod communications, enforced by Kubernetes network policies.

[icon: user-friends, set=fas, size=3x]

#### [Cluster Access on AWS](https://docs.pingidentity.com/forgeops/2026.2/prepare/security/multi-user-access-aws.html)

User entries in the Amazon EKS authorization configuration map.

[icon: user-secret, set=fas, size=3x]

#### [Secret Agent](https://docs.pingidentity.com/forgeops/2026.2/prepare/security/secret-agent.html)

Kubernetes operator that generates secrets and provides cloud secret management.

[icon: arrows-spin, set=fas, size=3x]

#### [Rotate Secrets](https://docs.pingidentity.com/forgeops/2026.2/prepare/security/secrets-rotation.html)

Rotate secrets in a ForgeOps deployment.

[icon: shield-check, set=fas, size=3x]

#### [New security features](https://docs.pingidentity.com/forgeops/2026.2/prepare/security/sec-features.html)

New ForgeOps security features