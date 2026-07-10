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