---
title: Container Configuration
description: Configure replica count, resource limits, node placement, and liveness, readiness, and startup probes for Ping Identity Helm chart workloads
component: helm
page_id: helm::configs/container
canonical_url: https://developer.pingidentity.com/helm/configs/container.html
llms_txt: https://developer.pingidentity.com/helm/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  global-section: Global Section
  probes-configuration: Probes Configuration
---

# Container Configuration

[Kubernetes Workload Controller](https://kubernetes.io/docs/concepts/workloads/controllers/) resources are created depending on configuration values:

* [Deployments](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/)

* [StatefulSets](https://kubernetes.io/docs/concepts/workloads/controllers/statefulset/)

## Global Section

Default yaml defined in the global `container` section:

```yaml
global:
  container:
    replicaCount: 1
    resources:
      requests:
        cpu: 0
        memory: 0
      limits:
        cpu: 0
        memory: 0
    nodeSelector: {}
    tolerations: []
    affinity: {}
    terminationGracePeriodSeconds: 30
    envFrom: []
    lifecyle: {}
    probes:
      livenessProbe:
        exec:
          command:
            - /opt/liveness.sh
        initialDelaySeconds: 30
        periodSeconds: 30
        timeoutSeconds: 5
        successThreshold: 1
        failureThreshold: 4
      readinessProbe:
        exec:
          command:
            - /opt/readiness.sh
        initialDelaySeconds: 30
        periodSeconds: 5
        timeoutSeconds: 5
        successThreshold: 1
        failureThreshold: 4
      startupProbe:
         exec:
           command:
             - /opt/liveness.sh
         periodSeconds: 10
         timeoutSeconds: 5
         failureThreshold: 90
```

## Probes Configuration

[Kubernetes Probes](https://kubernetes.io/docs/tasks/configure-pod-container/configure-liveness-readiness-startup-probes/) defined in the `container:` section will be added to workloads (that is, Deployments/StatefulSets).

Fields used to configure probes can be found in the [Kubernetes documentation](https://kubernetes.io/docs/tasks/configure-pod-container/configure-liveness-readiness-startup-probes/#configure-probes).

---

---
title: External Image Configuration
description: Configure the external pingtoolkit image used by init containers in Ping Identity Helm chart deployments
component: helm
page_id: helm::configs/external-image
canonical_url: https://developer.pingidentity.com/helm/configs/external-image.html
llms_txt: https://developer.pingidentity.com/helm/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  global-section: Global Section
---

# External Image Configuration

Defines an external image for initContainer utilities.

## Global Section

Default yaml defined in the global `externalImage` section:

```yaml
global:
  externalImage:
    pingtoolkit: pingidentity/pingtoolkit:latest
```

| External Image Parameters | Description                                                                                  |
| ------------------------- | -------------------------------------------------------------------------------------------- |
| pingtoolkit               | Registry, image and tag location for pingtoolkit. Used for primarily during init containers. |

|   |                                                                                                                                                                                                                                 |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | If your Kubernetes cluster doesn't have access to an external Docker repository, you can download and save the `pingtoolkit` image to your local repo. Setting this to your local repo will cause the charts to use that image. |

---

---
title: "global: Values"
description: Configure how the Helm addReleaseNameToResource value prepends, appends, or omits the release name on Kubernetes resource names
component: helm
page_id: helm::configs/global
canonical_url: https://developer.pingidentity.com/helm/configs/global.html
llms_txt: https://developer.pingidentity.com/helm/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  addreleasenametoresource: addReleaseNameToResource
---

# global: Values

There is a top-level `global` value providing instructions on how to name all Kubernetes resources, so a deployer might deploy several releases under the same namespace.

## addReleaseNameToResource

Provides global ability to add the Helm `.Release.Name` to Kubernetes resources.

| Value   | Description                      | Example: (Release.Name=acme, resource=pingdirectory) |
| ------- | -------------------------------- | ---------------------------------------------------- |
| prepend | Prepends Release.Name \[DEFAULT] | acme-pingdirectory                                   |
| append  | Appends Release.Name             | pingdirectory-acme                                   |
| none    | No use of Release.Name           | pingdirectory                                        |

---

---
title: Image Configuration
description: Configure the container image repository, name, tag, and pull policy for Ping Identity Helm chart deployments
component: helm
page_id: helm::configs/image
canonical_url: https://developer.pingidentity.com/helm/configs/image.html
llms_txt: https://developer.pingidentity.com/helm/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  global-section: Global Section
  product-section: Product Section
---

# Image Configuration

Provides values to define kubernetes image information to deployments and statefulsets.

## Global Section

Default image yaml defined in the global section:

```yaml
global:
  image:
    repository: pingidentity
    name:        # Set in product section
    tag: 2307
    pullPolicy: Always
  imagePullSecrets: []  # As needed for authentication to private repositories
  # - name: myregkeysecretname
```

## Product Section

Each product section specifies the name by default.

```yaml
pingaccess-admin:
  image:
    name: pingaccess
```

To have images use a different repository and tag, use the following:

```yaml
global:
  image:
    tag: edge
    repository: my.company.docker-repo.com
```

This snippet would result in pulling a PingAccess image from `my.company.docker-repo.com/pingaccess:edge`.

---

---
title: Ingress Configuration
description: Configure Kubernetes Ingress resources, hostnames, annotations, and TLS settings for Ping Identity Helm chart deployments
component: helm
page_id: helm::configs/ingress
canonical_url: https://developer.pingidentity.com/helm/configs/ingress.html
llms_txt: https://developer.pingidentity.com/helm/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  global-section: Global Section
  product-section: Product Section
  example-ingress-manifest: Example Ingress Manifest
---

# Ingress Configuration

[Kubernetes Ingress resources](https://kubernetes.io/docs/concepts/services-networking/ingress/) are created depending on configuration values.

## Global Section

Default yaml defined in the global `ingress` section, followed by definitions for each parameter:

```yaml
global:
  ingress:
    enabled: false
    addReleaseNameToHost: subdomain
    defaultDomain: example.com
    defaultTlsSecret:
    annotations: {}
    spec: {}
```

| Ingress Parameters    | Description                                                                                                                                                                                                               | Options                           | Default Value |
| --------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------- | ------------- |
| enabled               | Enables ingress definition.                                                                                                                                                                                               |                                   | false         |
| addReleaseNameToHost  | How `helm release-name` should be added to host.                                                                                                                                                                          | prependappendsubdomainnone        | subdomain     |
| defaultDomain         | Default DNS domain to use. Replaces the string "\_defaultDomain\_".                                                                                                                                                       |                                   |               |
| defaultTlsSecret      | Default TLS Secret to use. Replaces the string "\_defaultTlsSecret\_".                                                                                                                                                    |                                   | example.com   |
| annotations           | Annotations are used to provide configuration details to specific ingress controller types.                                                                                                                               | \* see option for nginx ingress   | {}            |
| spec.ingressClassName | This value is replacing the `kubernetes.io/ingress.class` annotation. See [this page](https://kubernetes.github.io/ingress-nginx/user-guide/k8s-122-migration/#what-is-the-flag-watch-ingress-without-class) for details. | name of the IngressClass resource | {}            |

**Annotations example for nginx ingress:**

```yaml
annotations:
  nginx.ingress.kubernetes.io/backend-protocol: "HTTPS"
```

**ingressClassName specification example for nginx ingress:**

```yaml
 spec:
   # Must match the name of the IngressClass resource
   ingressClassName: nginx-public
```

## Product Section

Default yaml defined in the product `ingress` section, followed by definitions for each parameter:

```yaml
ingress:
  hosts:
    - host: pingfederate-admin._defaultDomain_
      paths:
      - path: /
        backend:
          serviceName: admin
  tls:
    - secretName: _defaultTlsSecret_
      hosts:
```

| Ingress Parameters                    | Description                                                                                              | Default Value                    |
| ------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------- |
| hosts                                 | Array of hosts definitions                                                                               |                                  |
| hosts\[].host                         | Full DNS name of host to use for external name. "\_defaultDomain\_" will be replaced with .defaultDomain | {product-name}.\_defaultDomain\_ |
| hosts\[].paths                        | Array of paths to define for host                                                                        |                                  |
| hosts\[].paths\[].path                | Path on external ingress                                                                                 |                                  |
| hosts\[].paths\[].backend.serviceName | Name of the service to map to. This will result in the ingressPort on the server to be used.             |                                  |
| tls                                   | Array of tls definitions                                                                                 |                                  |
| tls\[].secretName                     | Certificate secret to use                                                                                | \_defaultTlsSecret\_             |
| tls\[].hosts                          | Array of specific hosts                                                                                  |                                  |

**Example use of \_defaultDomain\_ and addReleaseNameToHost:**

```none
     helm ReleaseName = acme
        defaultDomain = example.com
 addReleaseNameToHost = subdomain
ingress.hosts[0].host = pingfed-admin._defaultDomain_

Resulting host will be: pingfed-admin.acme.example.com
                                        ^    ^^^^^^^
                                        |       |
                              ReleaseName    defaultDomain
```

## Example Ingress Manifest

Below is an example product ingress for `pingfederate-admin` when deployed by Helm with a release-name of `acme`. It includes an ingress for the admin service (9999) using the default domain and tls secret, defined in the global section (if set).

```yaml
kind: Ingress
metadata:
  annotations:
    ....
  spec:
    rules:
      - host: pingfederate-admin.acme.example.com
        http:
          paths:
          - backend:
              serviceName: acme-pingfederate-admin
              serviceName: admin
            path: /
      tls:
      - hosts:
      - pingfederate-admin.acme.example.com
      secretName: ""
```

---

---
title: Introduction
description: Explains how Helm values files, override files, and --set parameters merge to configure Ping Identity Helm chart deployments
component: helm
page_id: helm::configs/index
canonical_url: https://developer.pingidentity.com/helm/configs/index.html
llms_txt: https://developer.pingidentity.com/helm/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
page_aliases: ["configs:index.adoc"]
section_ids:
  chart-values: Chart Values
  global-section: Global Section
  product-sections: Product Sections
---

# Introduction

The charts make heavy use of `Values` yaml files to pass configuration details to the Helm Charts. As defined by [Helm Values Files](https://helm.sh/docs/chart_template_guide/values_files/), values are provided to the chart using the following mechanisms:

* `values.yaml` file in the chart

* Value files passed to Helm during install/upgrade with the `-f` flag

* Individual parameters passed with the `--set` flag

The list above is in order of specificity: `values.yaml` in the chart can be overridden with `-f` supplied files, which can in turn be overridden with the `--set` parameter.

The example below shows how values from the chart, a user-supplied `myconfig.yaml` file, and `--set` parameters are merged with each other to form merged values.

![values configs](../_images/values-configs.png)

## Chart Values

To see the values supplied by the chart, simply use the `helm show values` command to print them. This provides both the data as ell as context-sensitive comments to each section.

```none
helm show values pingidentity/ping-devops
############################################################
# Ping Identity DevOps values.yaml
############################################################
# ...
```

You can also see all the available values in the [helm-charts](https://github.com/pingidentity/helm-charts/blob/master/charts/ping-devops/values.yaml) repository on GitHub.

The default values are broken up into two major sections:

* **global** — Represents the base set of values that will be provided to each product section unless it's overridden in that section.

* **product** — For every image/product, the values will be merged with the global settings and take precedence.

|   |                                                                                                                                                                           |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Values can only be modified when merged. They cannot be deleted. Also, if a value is set to the boolean true, and merged with a boolean of false, it will always be true. |

## Global Section

The `global:` section of the values contains configuration that is available to each product section. If a value is set in globals, that will be available to every product. This is very powerful, as you can turn on the ingress for every product by simply setting:

```yaml
global:
  ingress:
    enabled: true
```

This would in essence set `ingress.enabled=true` for every product:

```yaml
pingaccess:
  ingress:
    enabled: true

pingdirectory:
  ingress:
    enable: true
```

and so on.

It is much easier to set something in the `global:` section rather than repeat it for each product. To enable the ingress for only a few specific products, leave the default of `global.ingress.enabled=false` and set that value for those product sections.

## Product Sections

Just like the `global:` values, each product can have the same values as well as many more that are specific to that product/image. In the following example, persistent volume configuration is provided for PingDirectory:

```yaml
pingdirectory:
  persistentvolume:
    enabled: true
    volumes:
      - name: out-dir
        mountPath: /opt/out
        storage: 8Gi
        storageClassName:
```

---

---
title: License Configuration
description: Configure the devops-secret used to obtain evaluation licenses for Ping Identity product containers
component: helm
page_id: helm::configs/license
canonical_url: https://developer.pingidentity.com/helm/configs/license.html
llms_txt: https://developer.pingidentity.com/helm/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  global-section: Global Section
---

# License Configuration

Provides a secret used for obtaining evaluation licenses for Ping Identity products.

## Global Section

Default yaml defined in the global `license` section, followed by definitions for each parameter:

```yaml
global:
  license:
    secret:
      devOps: devops-secret
```

| License Parameters | Description                                                | Default Value |
| ------------------ | ---------------------------------------------------------- | ------------- |
| secret.devops      | Secret containing PING\_IDENTITY\_DEVOPS\_USER/KEY values. | devops-secret |

|   |                                                                                                                                                                             |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Use the `pingctl` command-line tool to create the devops-secret with your Ping Identity DevOps user and key.`pingctl kubernetes generate devops-secret \| kubectl apply -f` |

---

---
title: List of Supported Values
description: Reference list of all global and product-level values supported by the Ping Identity ping-devops Helm chart
component: helm
page_id: helm::configs/supported-values
canonical_url: https://developer.pingidentity.com/helm/configs/supported-values.html
llms_txt: https://developer.pingidentity.com/helm/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  global-values: Global Values
  workload-values-deployment-and-statefulset: Workload Values – Deployment and StatefulSet
  other-global-defaults: Other Global Defaults
  shared-utilities: Shared Utilities
  imageproduct-values: Image/Product Values
---

# List of Supported Values

These are the values supported in the ping-devops chart. In general, values specified in the global section can be overridden for individual products. The product sections have many global fields overridden by default (workloads, services, etc.).

## Global Values

| Name                                            | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | Default                                            |
| ----------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------- |
| `global.annotations`                            | Annotations listed, will be added to all Kubernetes resources.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | `{}`                                               |
| `global.labels`                                 | Labels listed, will be added to all Kubernetes resources.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | `{}`                                               |
| `global.envs`                                   | Environment variables listed will be added to the global-env-vars configmap                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | `{}`                                               |
| `global.addReleaseNameToResource`               | Provides global ability to add names to kubernetes resources. One of `{none, append, prepend}`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | `prepend`                                          |
| `global.ingress.enabled`                        | If true, deploy Ingress resources.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | `false`                                            |
| `global.ingress.addReleaseToHost`               | Add release to host. One of `{prepend, append, subdomain, none}`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | `subdomain`                                        |
| `global.ingress.defaultDomain`                  | Replaces with "*defaultDomain*" in host fields                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | `example.com`                                      |
| `global.ingress.defaultTlsSecret`               | Replaces with "*defaultTlsSecret*" in tls.secretName                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |                                                    |
| `global.ingress.annotations`                    | Annotations to apply to Ingress resources.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | `{}`                                               |
| `global.ingress.spec.ingressClassName`          | IngressClassName used by the generated Ingress resources.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |                                                    |
| `global.gateway.enabled`                        | If true, deploy Gateway API route resources.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | `false`                                            |
| `global.gateway.apiVersion`                     | Deprecated HTTPRoute API version fallback. Use global.gateway.httpRouteApiVersion.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | `gateway.networking.k8s.io/v1`                     |
| `global.gateway.httpRouteApiVersion`            | Gateway API version used for HTTPRoute resources.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | `gateway.networking.k8s.io/v1`                     |
| `global.gateway.tcpRouteApiVersion`             | Gateway API version used for TCPRoute resources.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | `gateway.networking.k8s.io/v1alpha2`               |
| `global.gateway.parentRefs`                     | Parent Gateway references                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | `[]`                                               |
| `global.gateway.addReleaseNameToHost`           | Add release to host. One of `{prepend, append, subdomain, none}`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | `subdomain`                                        |
| `global.gateway.defaultDomain`                  | Replaces with "*defaultDomain*" in host fields                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | `example.com`                                      |
| `global.gateway.hosts`                          | Gateway route hosts/paths for HTTPRoute. pathType must be one of `{Exact, PathPrefix, RegularExpression}` and this can also be set per-product at {product}.gateway.hosts.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | `[]`                                               |
| `global.gateway.annotations`                    | Annotations to apply to Gateway API route resources.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | `{}`                                               |
| `global.gateway.tcpRoutes`                      | Gateway listener bindings for TCPRoute. Each entry requires name, sectionName, and backend.serviceName. This can also be set per-product at {product}.gateway.tcpRoutes.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | `[]`                                               |
| `global.privateCert.generate`                   | If true, then an internal certificate secret will be created along with mount of the certificate in /run/secrets/internal-cert (creates a tls.crt and tls.key). By default the Issuer of the cert will be the service name created by the Helm Chart. Additionally, the ingress and gateway hosts, if enabled, will be added to the list of X509v3 Subject Alternative Name                                                                                                                                                                                                                                                                                                                                                                                                                                 | `false`                                            |
| `global.privateCert.format`                     | The format of the certificate to be generated. Used "pingaccess-fips-pem" to generate a valid certificate for running PingAccess in FIPS mode. Any other value will generate a PKCS12 keystore with the generated certificate.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | `PKCS12`                                           |
| `global.privateCert.additionalHosts`            | Additional hosts for the cert                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | `[]`                                               |
| `global.privateCert.additionalIPs`              | Additional IP addresses for the cert                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | `[]`                                               |
| `global.masterPassword`                         | Uses Helm function derivePassword, which uses the master password specification: <https://masterpassword.app/masterpassword-algorithm.pdf>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |                                                    |
| `global.masterPassword.enabled`                 | Enable master password                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | `false`                                            |
| `global.masterPassword.strength`                | Master password template. One of `{long, maximum}`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |                                                    |
| `global.masterPassword.name`                    | Defaults to release name                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |                                                    |
| `global.masterPassword.site`                    | Defaults to chart name                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |                                                    |
| `global.masterPassword.secret`                  | Defaults to release namespace                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |                                                    |
| `global.vault`                                  | Hashicorp Vault configuration                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |                                                    |
| `global.vault.enabled`                          | Enable Vault                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | `false`                                            |
| `global.vault.hashicorp.annotations`            | Annotation names, which will be appended to 'vault.hashicorp.com/' in the annotation. The vault.hashicorp.annotations.serviceAccountName value will be overwritten by the service account generated for the workload if there is one.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |                                                    |
| `global.vault.secretPrefix`                     | Prefix that will be prepended to any secrets being injected.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | `""`                                               |
| `global.vault.secrets`                          | Vault secrets to pull in                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | `{}`                                               |
| `global.secretProviderClass.enabled`            | Enable Secrets Store CSI Driver integration. When true, a CSI volume and volumeMount are auto-wired into the pod spec and utility sidecar.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | `false`                                            |
| `global.secretProviderClass.create`             | When true, a SecretProviderClass resource is rendered for each enabled product (requires the secrets-store.csi.x-k8s.io/v1 CRD to be pre-installed).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | `false`                                            |
| `global.secretProviderClass.name`               | Override the generated SecretProviderClass resource name. Defaults to \<release>-\<product>-spc when empty.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | `""`                                               |
| `global.secretProviderClass.provider`           | CSI driver provider. One of: aws, azure, gcp, vault, akeyless, conjur, openbao                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | `""`                                               |
| `global.secretProviderClass.parameters`         | Provider-specific parameters passed through as raw YAML to spec.parameters.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | `{}`                                               |
| `global.secretProviderClass.secretObjects`      | Kubernetes Secret objects to sync from the CSI volume (opaque passthrough).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | `[]`                                               |
| `global.secretProviderClass.mountPath`          | Mount path for the CSI volume inside containers.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | `/run/secrets`                                     |
| `global.secretProviderClass.readOnly`           | Whether the CSI volume mount is read-only.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | `true`                                             |
| `global.imagePullSecrets`                       | Repository authentication using secret defined as a docker-registry secret in Kubernetes.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | `[]`                                               |
| `global.image.repository`                       | Default image registry is not the fully-qualified name of the image Example: image.repository: pingidentity, docker.io, 123.dkr.ecr.us-west-1.amazonaws.com                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | `pingidentity`                                     |
| `global.image.repositoryFqn`                    | Docker image repository fully-qualified name. Overrides image.repository and image.name on the pod image spec Example: image.repositoryFqn: pingidentity/pingfederate, docker.io/my-pingfederate                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |                                                    |
| `global.image.name`                             | Default image name MUST be set in child chart Example: image.name: pingfederate                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |                                                    |
| `global.image.tag`                              | Default image tag                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | `2606`                                             |
| `global.image.pullPolicy`                       | Default image pull policy                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | `IfNotPresent`                                     |
| `global.rbac.generateServiceAccount`            | Set to true to generate a service account for the workload.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | `false`                                            |
| `global.rbac.serviceAccountName`                | Name of the service account that will be generated. The default value of "*defaultServiceAccountName*" will result in a service account named based on the Helm installation and the specific workload being deployed. If generateServiceAccount and generateGlobalServiceAccount are false, this value can also refer to a service account created outside of Helm.                                                                                                                                                                                                                                                                                                                                                                                                                                        | `defaultServiceAccountName`                        |
| `global.rbac.generateRoleAndRoleBinding`        | Set to true to generate a Role and RoleBinding corresponding to the workload service account.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | `false`                                            |
| `global.rbac.generateGlobalServiceAccount`      | Set to true to generate a service account for the entire installation. This global service account will be used for workloads that do not generate their own service account.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | `false`                                            |
| `global.rbac.generateGlobalRoleAndRoleBinding`  | Set to true to generate a Role and RoleBinding corresponding to the global service account for the entire installation.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | `false`                                            |
| `global.rbac.applyServiceAccountToWorkload`     | Set to true (the default) to apply to service account to the workload.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | `true`                                             |
| `global.rbac.role`                              | This yaml will be directly inserted into the generated Role when generateRoleAndRoleBinding and/or generateGlobalRoleAndRoleBinding are true. The rules for the Role can be set here.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | `get, watch, and list verbs for the pods resource` |
| `global.rbac.serviceAccountAnnotations`         | Any custom annotations to add to the service account.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |                                                    |
| `global.rbac.roleAnnotations`                   | Any custom annotations to add to the role.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |                                                    |
| `global.rbac.roleBindingAnnotations`            | Any custom annotations to add to the role binding.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |                                                    |
| `global.rbac.serviceAccountLabels`              | Any custom labels to add to the service account.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |                                                    |
| `global.rbac.roleLabels`                        | Any custom labels to add to the role.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |                                                    |
| `global.rbac.roleBindingLabels`                 | Any custom labels to add to the role binding.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |                                                    |
| `global.externalImage`                          | Provides ability to use external images for various purposes such as using curl, waitfor, etc. A pingtoolkit image is included by default for running waitFor and generating private cert initContainers. A pingaccess image is also included by default to allow generating an encrypted PEM-formatted cert that is compatible with FIPS mode. Any values specified on the image will be copied directly to the k8s spec for the container, except for the externalImage.{name}.image section, which follows the format of the global.image section. If no image section is specified (the default), the corresponding value from the product values section will be used. For example, if externalImage.pingtoolkit.image is empty, the values from the top-level pingtoolkit.image section will be used. | `{pingtoolkit, pingaccess}`                        |
| `global.services`                               | Services mapping a port to a targetPort on the corresponding container                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | `{}`                                               |
| `global.services.clusterExternalDNSHostname`    | Value for the external-dns.alpha.kubernetes.io/hostname annotation for the cluster service.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |                                                    |
| `global.services.clusterServiceName`            | If set, then this name will be used as the cluster service name (i.e clusterService == true).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |                                                    |
| `global.services.useLoadBalancerForDataService` | If true, the data service will be created with type: LoadBalancer.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | `false`                                            |
| `global.services.serviceName.dataService`       | If true, a ClusterIP service is created reachable within the cluster. A single IP is provided and the service will round-robin across the backend containers                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |                                                    |
| `global.services.serviceName.clusterService`    | If true, a headless service is created, explicitly specifying "None" for the clusterIP. DNS requests to this service will provide one of the IPs of the backend containers                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |                                                    |
| `global.services.serviceName.containerPort`     | Port on the kubernetes container                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |                                                    |
| `global.services.serviceName.servicePort`       | Port available from the kubernetes service. If clusterService=true this port on the cluster service is not really used, as the headless service always maps through to the container port                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |                                                    |
| `global.services.serviceName.ingressPort`       | Port available from the kubernetes ingress                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |                                                    |
| `global.services.serviceName.gatewayPort`       | Port available from the kubernetes gateway                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |                                                    |
| `global.services.annotations`                   | Any custom annotations to add to the service.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |                                                    |
| `global.services.clusterServiceAnnotations`     | Any custom annotations to add to the ClusterIP service.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |                                                    |
| `global.services.labels`                        | Any custom labels to add to the service.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |                                                    |
| `global.services.clusterServiceLabels`          | Any custom labels to add to the ClusterIP service.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |                                                    |

## Workload Values – Deployment and StatefulSet

| Name                                                                                    | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | Default                                                    |
| --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------- |
| `global.workload`                                                                       | Can be Deployment or StatefulSet                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | `Deployment`                                               |
| `global.workload.annotations`                                                           | Annotations to apply to the template in the workload. To apply top-level annotations to the Deployment or StatefulSet itself, use global.workload.deployment.annotations or global.workload.statefulSet.annotations.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |                                                            |
| `global.workload.labels`                                                                | Labels to apply to the template in the workload. To apply top-level labels to the Deployment or StatefulSet itself, use global.workload.deployment.labels or global.workload.statefulSet.labels.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |                                                            |
| `global.workload.schedulerName`                                                         | K8s scheduler                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | `default-scheduler`                                        |
| `global.workload.shareProcessNamespace`                                                 | Set shareProcessNamespace in the pod spec                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | `false`                                                    |
| `global.workload.enableServiceLinks`                                                    | indicates whether info about services can be added as env variables                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | `true`                                                     |
| `global.workload.topologySpreadConstraints`                                             | Configuration of pod spread across cluster zones                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | `[]`                                                       |
| `global.workload.podDisruptionBudget`                                                   | PodDisruptionBudget configuration                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |                                                            |
| `global.workload.podDisruptionBudget.enabled`                                           | Enable PodDisruptionBudget generation                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | `false`                                                    |
| `global.workload.podDisruptionBudget.minAvailable`                                      | Minimum available pods Set exactly one of minAvailable or maxUnavailable. Accepts integer or percentage string.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |                                                            |
| `global.workload.podDisruptionBudget.maxUnavailable`                                    | Maximum unavailable pods Set exactly one of minAvailable or maxUnavailable. Accepts integer or percentage string.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |                                                            |
| `global.workload.podDisruptionBudget.unhealthyPodEvictionPolicy`                        | Optional unhealthy pod eviction policy for the generated PodDisruptionBudget. Requires Kubernetes v1.31+. If set on Kubernetes versions older than v1.31, template rendering fails.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |                                                            |
| `global.workload.podDisruptionBudget.annotations`                                       | Annotations for the PodDisruptionBudget                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |                                                            |
| `global.workload.podDisruptionBudget.labels`                                            | Labels for the PodDisruptionBudget PodDisruptionBudgets only affect voluntary disruptions that use the Eviction API. They do not prevent involuntary disruptions, direct pod deletion, workload deletion, or workload rolling updates. Percentage values round up, which can allow full disruption of single-replica workloads. Strict budgets such as maxUnavailable: 0 or minAvailable: 100% can block kubectl drain.                                                                                                                                                                                                                                                                             |                                                            |
| `global.workload.deployment`                                                            | Deployment workload configuration                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |                                                            |
| `global.workload.deployment.strategy`                                                   | Deployment pod replacement strategy                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |                                                            |
| `global.workload.deployment.strategy.type`                                              | Strategy type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | `RollingUpdate`                                            |
| `global.workload.deployment.strategy.rollingUpdate.maxSurge`                            | Max surge, only applicable for RollingUpdate type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | `1`                                                        |
| `global.workload.deployment.strategy.rollingUpdate.maxUnavailable`                      | Max unavailable, only applicable for RollingUpdate type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | `0`                                                        |
| `global.workload.deployment.annotations`                                                | Annotations to apply to the top-level Deployment. To apply annotations to the template within the Deployment, use global.workload.annotations.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |                                                            |
| `global.workload.deployment.labels`                                                     | Labels to apply to the top-level Deployment. To apply labels to the template within the Deployment, use global.workload.labels.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |                                                            |
| `global.workload.statefulSet`                                                           | StatefulSet workload configuration                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |                                                            |
| `global.workload.statefulSet.partition`                                                 | Used for canary testing if n>0                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | `0`                                                        |
| `global.workload.statefulSet.persistentvolume.enabled`                                  | Enable persistent volumes                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | `true`                                                     |
| `global.workload.statefulSet.persistentvolume.volumes`                                  | For every volume defined in the volumes list, 3 items will be created in the StatefulSet: 1. container.volumeMounts - name and mountPath. 2. template.spec.volume - name and persistentVolumeClaim.claimName. 3. spec.volumeClaimTemplates - persistentVolumeClaim.                                                                                                                                                                                                                                                                                                                                                                                                                                 | `{out-dir}`                                                |
| `global.workload.statefulSet.persistentvolume.volumes.volumeName.mountPath`             | Mount path for the volume                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |                                                            |
| `global.workload.statefulSet.persistentvolume.volumes.volumeName.persistentVolumeClaim` | volumeClaimTemplate                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |                                                            |
| `global.workload.statefulSet.podManagementPolicy`                                       | Controls how pods are created during initial scale up, when replacing pods on nodes, or when scaling down. The default behavior is OrderedReady. The Parallel podManagementPolicy allows for starting up and scaling down multiple Pods simultaneously. Updates are not affected. The only products that support Parallel are PingDirectory and PingDataSync, on versions 2209 and later. When using the Parallel policy, consider setting the RETRY\_TIMEOUT\_SECONDS environment variable to a higher value (it defaults to 180) for the Pods. If the value is too low with many servers starting at once, it may lead to some Pods restarting unnecessarily during the initial workload startup. | `OrderedReady`                                             |
| `global.workload.statefulSet.annotations`                                               | Annotations to apply to the top-level StatefulSet. To apply annotations to the template within the StatefulSet, use global.workload.annotations.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |                                                            |
| `global.workload.statefulSet.labels`                                                    | Labels to apply to the top-level StatefulSet. To apply labels to the template within the StatefulSet, use global.workload.labels.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |                                                            |
| `global.workload.securityContext`                                                       | securityContext for the workload Pod spec. The securityContext defined will be inserted directly into the Pod spec. The user (9031) and group (0) represent the current user and group used with PingIdentity images (except PingDelegator). The fsGroup is required for any workloads that volumeMount a pvc (i.e. StatefulSets). Set as securityContext: null when no generated securityContext is desired.                                                                                                                                                                                                                                                                                       | `fsGroup 0, runAsUser 9031, runAsGroup 0`                  |
| `global.clustering.autoscaling`                                                         | Configure Horizontal Pod Autoscaling                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |                                                            |
| `global.clustering.autoscaling.enabled`                                                 | Enable Horizontal Pod Autoscaling. If enabled, ensure that proper container.resources values are set and coordinated with the targetCPUUtilizationPercentage or targetMemoryUtilizationPercentage                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | `false`                                                    |
| `global.clustering.autoscaling.minReplicas`                                             | Autoscaler minimum replicas                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | `1`                                                        |
| `global.clustering.autoscaling.maxReplicas`                                             | Autoscaler maximum replicas                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | `4`                                                        |
| `global.clustering.autoscaling.targetCPUUtilizationPercentage`                          | Target CPU utilization                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | `75`                                                       |
| `global.clustering.autoscaling.targetMemoryUtilizationPercentage`                       | Target memory utilization                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |                                                            |
| `global.clustering.autoscaling.annotations`                                             | Custom annotations for the HPA.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |                                                            |
| `global.clustering.autoscaling.labels`                                                  | Custom labels for the HPA.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |                                                            |
| `global.clustering.autoscaling.behavior`                                                | Custom HPA behavior yaml                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | `{}`                                                       |
| `global.clustering.autoscalingMetricsTemplate`                                          | Custom HPA metrics yaml                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | `[]`                                                       |
| `global.container`                                                                      | Configure the container in the workload Pod spec                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |                                                            |
| `global.workload.container.securityContext`                                             | securityContext at the container level for the workload. The securityContext defined will be inserted directly into the spec for the main container of the Pod. Container-level securityContext values will overwrite any corresponding values from the Pod-level securityContext.                                                                                                                                                                                                                                                                                                                                                                                                                  | `allowPrivilegeEscalation: false, capabilities: drop: ALL` |
| `global.container.replicaCount`                                                         | Number of replicas for workload                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | `1`                                                        |
| `global.container.resources`                                                            | container resources yaml to insert into Pod spec                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |                                                            |
| `global.container.nodeSelector`                                                         | nodeSelector yaml to insert into Pod spec                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | `{}`                                                       |
| `global.container.tolerations`                                                          | tolerations yaml to insert into Pod spec                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | `[]`                                                       |
| `global.container.affinity`                                                             | affinity yaml to insert into Pod spec                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | `{}`                                                       |
| `global.container.terminationGracePeriodSeconds`                                        | termination grace period                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | `30`                                                       |
| `global.container.envFrom`                                                              | envFrom yaml to insert into Pod spec                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | `[]`                                                       |
| `global.container.env`                                                                  | Additional environment variables to insert into the Pod spec. Unlike the global.envs values, these will be set directly on the Pod. global.envs values are set in ConfigMaps rather than on the Pod directly. This value allows for setting the valueFrom field for an environment variable when necessary.                                                                                                                                                                                                                                                                                                                                                                                         | `[]`                                                       |
| `global.container.lifecycle`                                                            | lifecycle yaml to insert into Pod spec                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |                                                            |
| `global.container.probes`                                                               | probes yaml to insert into Pod spec                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | `liveness, readiness, and startup probes defined`          |

## Other Global Defaults

| Name                                    | Description                                                                                                                                                                                                                                                                                                                                                                                                           | Default                                                     |
| --------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------- |
| `global.license.secret.devOps`          | Identify the k8s secret containing the DevOps USER/KEY if used during deployment. pingctl can be used to generate the devops-secret                                                                                                                                                                                                                                                                                   | `devops-secret`                                             |
| `global.utilitySidecar`                 | Deploy a utility sidecar for running command-line tools. This sidecar is useful for command line utilities like collect-support-data. The sidecar will remain running alongside the workload, even when the sidecar isn't being used. It does not need to be listed in the includeSidecars value.                                                                                                                     |                                                             |
| `global.utilitySidecar.enabled`         | Enable the utility sidecar                                                                                                                                                                                                                                                                                                                                                                                            | `false`                                                     |
| `global.utilitySidecar.image`           | Override image fields for the sidecar. Any image fields not set here inherit from the product image.                                                                                                                                                                                                                                                                                                                  |                                                             |
| `global.utilitySidecar.command`         | Override the sidecar container command                                                                                                                                                                                                                                                                                                                                                                                | `["tail"]`                                                  |
| `global.utilitySidecar.args`            | Override the sidecar container args                                                                                                                                                                                                                                                                                                                                                                                   | `["-f", "/dev/null"] when command is not overridden`        |
| `global.utilitySidecar.resources`       | Set k8s resources yaml for the sidecar spec                                                                                                                                                                                                                                                                                                                                                                           | `1 CPU and 2g memory limit, 0 CPU and 128Mi memory request` |
| `global.utilitySidecar.envFrom`         | Optional envFrom sources for the sidecar                                                                                                                                                                                                                                                                                                                                                                              | `[]`                                                        |
| `global.utilitySidecar.env`             | Environment variables for the sidecar                                                                                                                                                                                                                                                                                                                                                                                 | `[]`                                                        |
| `global.utilitySidecar.volumes`         | Additional sidecar volumeMounts This existing field only adds container-level volumeMounts to the utility sidecar. It does not create pod-level volumes implicitly. The chart automatically creates emptyDir backing volumes for temp and out-dir only when the utility sidecar is enabled and the workload does not already define them. StatefulSet out-dir PVC behavior remains unchanged when already configured. | `[]`                                                        |
| `global.utilitySidecar.securityContext` | securityContext at the container level for the sidecar. The securityContext defined will be inserted directly into the spec for the sidecar. By default no container securityContext is defined. In Kubernetes when a container-level securityContext is set, it will overwrite any corresponding values from the Pod-level securityContext.                                                                          | `allowPrivilegeEscalation: false, capabilities: drop: ALL`  |
| `global.includeSidecars`                | names of sidecars to include, from the top-level `sidecars` value                                                                                                                                                                                                                                                                                                                                                     | `[]`                                                        |
| `global.includeInitContainers`          | names of sidecars to include, from the top-level `initContainers` value                                                                                                                                                                                                                                                                                                                                               | `[]`                                                        |
| `global.includeVolumes`                 | names of sidecars to include, from the top-level `volumes` value                                                                                                                                                                                                                                                                                                                                                      | `[]`                                                        |

## Shared Utilities

| Name             | Description                                                                                                         | Default |
| ---------------- | ------------------------------------------------------------------------------------------------------------------- | ------- |
| `sidecars`       | Sidecar yaml definitions available to product workload spec                                                         | `{}`    |
| `initContainers` | initContainer yaml definitions available to product workload spec                                                   | `{}`    |
| `volumes`        | volume yaml definitions available to product workload spec for sidecars, initContainers, or main product containers | `{}`    |
| `configMaps`     | configMap yaml definitions available to product workload spec for sidecars or main product containers               | `{}`    |

## Image/Product Values

| Name                                                           | Description                                                                                                                                                                                                                                               | Default                                                    |
| -------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------- |
| `ldap-sdk-tools`                                               | LDAP SDK tools values                                                                                                                                                                                                                                     |                                                            |
| `ldap-sdk-tools.enabled`                                       | Enable LDAP SDK tools deployment                                                                                                                                                                                                                          | `false`                                                    |
| `pingfederate-admin`                                           | PingFederate admin values                                                                                                                                                                                                                                 |                                                            |
| `pingfederate-admin.enabled`                                   | Enable PingFederate admin deployment                                                                                                                                                                                                                      | `false`                                                    |
| `pingfederate-admin.cronjob`                                   | CronJobs run a kubectl exec command to run commands on a utility sidecar container. They will also create the necessary ServiceAccount, Role, and RoleBinding to run the jobs                                                                             |                                                            |
| `pingfederate-admin.cronjob.enabled`                           | Enable the PingFederate Admin CronJob                                                                                                                                                                                                                     | `false`                                                    |
| `pingfederate-admin.cronjob.spec`                              | yaml to insert into the created CronJob spec. If specified, this will override any other specified values for the CronJob.                                                                                                                                |                                                            |
| `pingfederate-admin.cronjob.spec.jobTemplate`                  | yaml to override default jobTemplate. If a jobTemplate is not overridden, a default template will be inserted.                                                                                                                                            |                                                            |
| `pingfederate-admin.cronjob.image`                             | Image to run the jobs. The image must include kubectl and sh.                                                                                                                                                                                             | `pingidentity/pingtoolkit:latest`                          |
| `pingfederate-admin.cronjob.args`                              | Job arguments                                                                                                                                                                                                                                             | `[]`                                                       |
| `pingfederate-admin.cronjob.podSecurityContext`                | securityContext for the pod in the jobTemplate. This will be used if a jobTemplate is not specified.                                                                                                                                                      | `null`                                                     |
| `pingfederate-admin.cronjob.podSecurityContext`                | securityContext for the container in the jobTemplate. This will be used if a jobTemplate is not specified.                                                                                                                                                | `allowPrivilegeEscalation: false, capabilities: drop: ALL` |
| `pingfederate-engine`                                          | PingFederate engine values                                                                                                                                                                                                                                |                                                            |
| `pingfederate-engine.enabled`                                  | Enable PingFederate engine deployment                                                                                                                                                                                                                     | `false`                                                    |
| `pingfederate-engine.cronjob`                                  | CronJobs run a kubectl exec command to run commands on a utility sidecar container. They will also create the necessary ServiceAccount, Role, and RoleBinding to run the jobs                                                                             |                                                            |
| `pingfederate-engine.cronjob.enabled`                          | Enable the PingFederate engine CronJob                                                                                                                                                                                                                    | `false`                                                    |
| `pingfederate-engine.cronjob.spec`                             | yaml to insert into the created CronJob spec. If specified, this will override any other specified values for the CronJob.                                                                                                                                |                                                            |
| `pingfederate-engine.cronjob.spec.jobTemplate`                 | yaml to override default jobTemplate. If a jobTemplate is not overridden, a default template will be inserted.                                                                                                                                            |                                                            |
| `pingfederate-engine.cronjob.image`                            | Image to run the Jobs. The image must include kubectl and sh.                                                                                                                                                                                             | `pingidentity/pingtoolkit:latest`                          |
| `pingfederate-engine.cronjob.args`                             | Job arguments                                                                                                                                                                                                                                             | `[]`                                                       |
| `pingfederate-engine.cronjob.podSecurityContext`               | securityContext for the pod in the jobTemplate. This will be used if a jobTemplate is not specified.                                                                                                                                                      | `null`                                                     |
| `pingfederate-engine.cronjob.podSecurityContext`               | securityContext for the container in the jobTemplate. This will be used if a jobTemplate is not specified.                                                                                                                                                | `allowPrivilegeEscalation: false, capabilities: drop: ALL` |
| `pingdirectory`                                                | PingDirectory values                                                                                                                                                                                                                                      |                                                            |
| `pingdirectory.enabled`                                        | Enable PingDirectory deployment                                                                                                                                                                                                                           | `false`                                                    |
| `pingdirectory.cronjob`                                        | CronJobs run a kubectl exec command to run commands on a utility sidecar container. They will also create the necessary ServiceAccount, Role, and RoleBinding to run the jobs                                                                             |                                                            |
| `pingdirectory.cronjob.enabled`                                | Enable the PingDirectory CronJob                                                                                                                                                                                                                          | `false`                                                    |
| `pingdirectory.cronjob.spec`                                   | yaml to insert into the created CronJob spec. If specified, this will override any other specified values for the CronJob.                                                                                                                                |                                                            |
| `pingdirectory.cronjob.spec.jobTemplate`                       | yaml to override default jobTemplate. If a jobTemplate is not overridden, a default template will be inserted.                                                                                                                                            |                                                            |
| `pingdirectory.cronjob.image`                                  | Image to run the Jobs. The image must include kubectl and sh.                                                                                                                                                                                             | `pingidentity/pingtoolkit:latest`                          |
| `pingdirectory.cronjob.args`                                   | Job arguments                                                                                                                                                                                                                                             | `[]`                                                       |
| `pingdirectory.cronjob.podSecurityContext`                     | securityContext for the pod in the jobTemplate. This will be used if a jobTemplate is not specified.                                                                                                                                                      | `null`                                                     |
| `pingdirectory.cronjob.podSecurityContext`                     | securityContext for the container in the jobTemplate. This will be used if a jobTemplate is not specified.                                                                                                                                                | `allowPrivilegeEscalation: false, capabilities: drop: ALL` |
| `pingdirectory.services.serviceName.loadBalancerService`       | If true, the per-Pod LoadBalancer services enabled with pingdirectory.services.loadBalancerServicePerPod will include this port.                                                                                                                          | `false`                                                    |
| `pingdirectory.services.loadBalancerServicePerPod`             | Set to true to create a separate LoadBalancer service for each individual Pod in the PingDirectory StatefulSet.                                                                                                                                           | `false`                                                    |
| `pingdirectory.services.loadBalancerExternalDNSHostnameSuffix` | Value used for the external-dns.alpha.kubernetes.io/hostname annotation for the LoadBalancer services. This value will be used as a suffix for the hostname for each individual pod when pingdirectory.services.loadBalancerServicePerPod is set to true. |                                                            |
| `pingdirectoryproxy`                                           | PingDirectoryProxy values                                                                                                                                                                                                                                 |                                                            |
| `pingdirectoryproxy.enabled`                                   | Enable PingDirectoryProxy deployment                                                                                                                                                                                                                      | `false`                                                    |
| `pingdelegator`                                                | PingDelegator values                                                                                                                                                                                                                                      |                                                            |
| `pingdelegator.enabled`                                        | Enable PingDelegator deployment                                                                                                                                                                                                                           | `false`                                                    |
| `pingdatasync`                                                 | PingDataSync values                                                                                                                                                                                                                                       |                                                            |
| `pingdatasync.enabled`                                         | Enable PingDataSync deployment                                                                                                                                                                                                                            | `false`                                                    |
| `pingauthorize`                                                | PingAuthorize values                                                                                                                                                                                                                                      |                                                            |
| `pingauthorize.enabled`                                        | Enable PingAuthorize deployment                                                                                                                                                                                                                           | `false`                                                    |
| `pingauthorizepap`                                             | PingAuthorizePAP values                                                                                                                                                                                                                                   |                                                            |
| `pingauthorizepap.enabled`                                     | Enable PingAuthorizePAP deployment                                                                                                                                                                                                                        | `false`                                                    |
| `pingaccess-admin`                                             | PingAccess admin values                                                                                                                                                                                                                                   |                                                            |
| `pingaccess-admin.enabled`                                     | Enable PingAccess admin deployment                                                                                                                                                                                                                        | `false`                                                    |
| `pingaccess-engine`                                            | PingAccess engine values                                                                                                                                                                                                                                  |                                                            |
| `pingaccess-engine.enabled`                                    | Enable PingAccess engine deployment                                                                                                                                                                                                                       | `false`                                                    |
| `pingcentral`                                                  | PingCentral values                                                                                                                                                                                                                                        |                                                            |
| `pingcentral.enabled`                                          | Enable PingCentral deployment                                                                                                                                                                                                                             | `false`                                                    |
| `pingdataconsole`                                              | PingDataConsole values                                                                                                                                                                                                                                    |                                                            |
| `pingdataconsole.enabled`                                      | Enable PingDataConsole deployment                                                                                                                                                                                                                         | `false`                                                    |
| `pingdataconsole.defaultLogin`                                 | Default login details for the console                                                                                                                                                                                                                     |                                                            |
| `pingdataconsole.defaultLogin.server.host`                     | Default hostname                                                                                                                                                                                                                                          | `pingdirectory-cluster`                                    |
| `pingdataconsole.defaultLogin.server.port`                     | Default port                                                                                                                                                                                                                                              | `636`                                                      |
| `pingdataconsole.defaultLogin.username`                        | Default username                                                                                                                                                                                                                                          | `administrator`                                            |
| `pd-replication-timing`                                        | PingDirectory replication timing values                                                                                                                                                                                                                   |                                                            |
| `pd-replication-timing.enabled`                                | Enable PingDirectory replication timing deployment                                                                                                                                                                                                        | `false`                                                    |
| `pingtoolkit`                                                  | PingToolkit values                                                                                                                                                                                                                                        |                                                            |
| `pingtoolkit.enabled`                                          | Enable PingToolkit deployment                                                                                                                                                                                                                             | `false`                                                    |
| `testFramework.rbac.serviceAccountImagePullSecrets`            | Repository authentication using secrets defined as a docker-registry secrets in Kubernetes.                                                                                                                                                               | `[]`                                                       |

---

---
title: OpenShift Configuration
description: Configure OpenShift-compatible security context settings by unsetting fsGroup and runAsUser in Ping Identity Helm chart values
component: helm
page_id: helm::configs/openshift-config
canonical_url: https://developer.pingidentity.com/helm/configs/openshift-config.html
llms_txt: https://developer.pingidentity.com/helm/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  unset-fsgroup-and-runasuser-at-the-pod-level: Unset fsGroup and runAsUser at the Pod Level
  initcontainers-unset-runasuser-at-the-container-level: "initContainers: Unset runAsUser at the Container Level"
---

# OpenShift Configuration

Openshift is designed to use a randomly generated user ID and group ID (UID/GID) for the `runAsUser` and `fsGroup` fields of the pod- and container-level security contexts.

By default, the security contexts in the chart use values corresponding to the user and group IDs under which the product runs. You can unset the `fsGroup` and `runAsUser` securityContext fields in your custom values, allowing OpenShift to set them as expected.

## Unset `fsGroup` and `runAsUser` at the Pod Level

In the global section of the values.yaml file, add the following stanza:

```yaml
global:
  workload:
    securityContext:
      fsGroup: null
      runAsUser: null
```

This will unset `fsGroup` and `runAsUser` in the pod-level security context. Pods that require initContainers will have to also unset `runAsUser` in the container-level security context.

## initContainers: Unset `runAsUser` at the Container Level

Some of the product deployments use initContainers for various operations, such as waiting for other services to be available or configuration actions. These containers, while part of the workload, have the security context set at the container level, not the pod level. The values listed above apply only to the pod-level security context. To unset `runAsUser` for any pingtoolkit initContainers so Openshift can take over, also add the following stanza:

```yaml
global:
  externalImage:
    pingtoolkit:
      securityContext:
        runAsUser: null
```

For example, here is a complete block for configuring pingaccess-admin with a `waitFor` initContainer:

```yaml
global:
  workload:
    securityContext:
      fsGroup: null
      runAsUser: null
  externalImage:
    pingtoolkit:
      securityContext:
        runAsUser: null

  pingaccess-admin:
    enabled: true
    privateCert:
    generate: true
    envs:
      SERVER_PROFILE_URL: https://github.com/pingidentity/pingidentity-server-profiles.git
      SERVER_PROFILE_PATH: baseline/pingaccess
    container:
      waitFor:
        pingfederate-engine:
          service: https
          timeoutSeconds: 300
```

---

---
title: PrivateCert Configuration
description: Generate an internal TLS certificate and keystore for a Ping Identity product using the Helm chart privateCert settings
component: helm
page_id: helm::configs/privatecerts
canonical_url: https://developer.pingidentity.com/helm/configs/privatecerts.html
llms_txt: https://developer.pingidentity.com/helm/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  global-section: Global Section
  product-section: Product Section
---

# PrivateCert Configuration

Generates a private certificate (.crt and .key) based on the internal hostname of the service.

## Global Section

|   |                                                        |
| - | ------------------------------------------------------ |
|   | privateCert is currently only supported by PingAccess. |

Default yaml defined in the global `privateCert` section. By default, certificates will not be generated. It is advised to NOT generate internal certs at the global level, as many services don't need a private cert on the internal service.

```yaml
global:
############################################################
# Internal Certificates
#
# If set to true, then an internal certificate secret will
# be created along with mount of the certificate in
# /run/secrets/internal-cert (creates a tls.crt and tls.key)
#
# By default the Issuer of the cert will be the service name
# created by the Helm Chart.  Additionally, the ingress hosts,
# if enabled, will be added to the list of X509v3 Subject Alternative Name
#
# Use the additionalHosts and additionalIPs if additional custom
# names and ips are needed.
#
#      privateCert.generate: {true | false}
#      privateCert.additionalHosts: {optional array of hosts}
#      privateCert.additionalIPs: {optional array of IP Addresses}
############################################################
privateCert:
  generate: false
  additionalHosts: []
  additioanlIPs: []
```

## Product Section

Generating an internal certificate is as simple as setting `privateCert.generate` to true.

Here's an example of generating an internal certificate for `pingaccess-engine`:

```yaml
pingaccess-admin:
  privateCert:
    generate:true
```

This will ultimately create a secret named `{release-productname}-private-cert` containing a valid `tls.crt` and `tls.key`.

By default, the issuer of the cert will be the service name created by the Helm Chart. Additionally, the ingress hosts, if enabled, will be added to the list of `X509v3 Subject Alternative Name`.

The product image will then create an init container to generate a pkcs12 file that will be placed in `/run/secrets/private-keystore/keystore.env`, which will be mounted into the running container.

When the container's hooks are running, it will source the environment variables in this keystore.env. The default variables set are:

* `PRIVATE_KEYSTORE_PIN={base64 random pin}`

* `PRIVATE_KEYSTORE_TYPE=pkcs12`

* `PRIVATE_KEYSTORE={pkcs12 keystore}`

These environment variables are required in the `data.json.subst` file in order to use the generated privateCert. They can be used in any server-profile artifacts to be replaced when the images are started.

---

---
title: Service Configuration
description: Configure Kubernetes Service resources, including ports and cluster or data service types, for Ping Identity Helm chart products
component: helm
page_id: helm::configs/service
canonical_url: https://developer.pingidentity.com/helm/configs/service.html
llms_txt: https://developer.pingidentity.com/helm/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  product-section: Product Section
---

# Service Configuration

[Kubernetes Service resources](https://kubernetes.io/docs/concepts/services-networking/service/) are created depending on configuration values.

## Product Section

Default yaml defined in the product `services` section. The example found in the `pingfederate-admin` section is:

```yaml
services:
  admin:
    servicePort: 9999
    containerPort: 9999
    ingressPort: 443
    dataService: true
  clusterbind:
    servicePort: 7600
    containerPort: 7600
    clusterService: true
  clusterfail:
    servicePort: 7700
    containerPort: 7700
    clusterService: true
  clusterExternalDNSHostname:
```

| Service Parameters                  | Description                                                   |
| ----------------------------------- | ------------------------------------------------------------- |
| services                            | Array of services                                             |
| services\[].{name}                  | Service Name. (i.e. https, ldap, admin, api)                  |
| services\[].{name}.servicePort      | External port of service                                      |
| services\[].{name}.containerPort    | Port on target container                                      |
| services\[].{name}.ingressPort      | Port on ingress container (if ingress is used)                |
| services\[].{name}.dataService      | Adds to a ClusterIP service with single DNS/IP                |
| services\[].{name}.clusterService   | Adds to a headless service with DNS request returning all IPs |
| services.clusterExternalDNSHostname |                                                               |

The example above will create a container/service/ingress that looks like this:

```none
  +-------------+               +-----------+              +-----------+
  |  Container  |--(9999)-------|  Service  |-(9999)-------|  Ingress  |-(443)---
  +-------------+               +-----------+              +-----------+


  +-------------+  (7600)       +-----------+ (7600)
  |  Container  |--(7700)-------|  Service  |-(7700)
  +-------------+               +-----------+
```

---

---
title: Vault Configuration
description: Configure HashiCorp Vault annotations and secret injection for Ping Identity Helm chart deployments
component: helm
page_id: helm::configs/vault
canonical_url: https://developer.pingidentity.com/helm/configs/vault.html
llms_txt: https://developer.pingidentity.com/helm/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  vault-secret-values: Vault Secret Values
  special-key-name-to-json: Special Key Name (to-json)
  vault-annotations: Vault Annotations
  example: Example
  using-vault-secrets-to-mount-base64-encoded-keystore-files: Using Vault Secrets to Mount base64-Encoded Keystore Files
---

# Vault Configuration

The current Helm chart support is provided for Hashicorp Vault annotations and use of the Hashicorp injector. More information on Hashicorp Vault annotations can be found [here](https://www.vaultproject.io/docs/platform/k8s/injector/annotations).

|   |                                                                                                                                                                                                                                                                                                                                   |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The PingIdentity DevOps images and Helm chart only support version 2 of the KV secrets engine API for Vault secrets. PingDirectory itself currently only supports KV version 1 for password storage schemes. Learn more in the [Vault KV secrets engine documentation](https://developer.hashicorp.com/vault/api-docs/secret/kv). |

## Vault Secret Values

An example vault values section looks like:

```yaml
vault:
  enabled: true
  hashicorp:
    annotations:
      role: {hashicorp-vault-role}
    secretPrefix: {path to secret}
    secrets:
      {secret-name}:
        {secret-key | to-json}:
          path: /opt/in/some/location/secrets
          file: devops-secret.env
```

The `vault.hashicorp.secrets` is a map that specifies each `secret` to pull from the vault. And for each secret, a map specifies the `key` to pull with instructions of where to place the secret based on `path` and `file`.

| License Parameters          | Description                                                                   | Default Value     |
| --------------------------- | ----------------------------------------------------------------------------- | ----------------- |
| secrets.{secret}            | map of secret                                                                 | devops-secret     |
| secrets.{secret}.{key}      | map of key                                                                    | pingaccess.lic    |
| secrets.{secret}.{key}.path | optional: location of secret. Defaults to vault.annotation.secret-volume-path | /opt/in/some/path |
| secrets.{secret}.{key}.file | required: file name secrets placed into                                       | pingaccess.lic    |

## Special Key Name (to-json)

There is a special key name that can be provided that will drop the raw secret into the container as its json representation with all the secret key names/values.

If dropped into the `SECRETS_DIR` (defaults to `/run/secrets`) directory, these files will be processed as:

* PROPERTY\_FILE if the file ends in `.env`, or

* Separate files will be created for each key=value pair.

See the example below in this document for the transformation that occurs with the `devops-secret.env`.

## Vault Annotations

Default yaml defined in the global `vault` section. The options of annotation names/values can be found at [vault definitions](https://www.vaultproject.io/docs/platform/k8s/injector/annotations).

For each of the annotations, the helm chart will automatically pre-pend the annotation with the hashicorp annotation prefix of `vault.hashicorp.com`. See example below.

```yaml
global:
  vault:
    enabled: false
    hashicorp:
      annotations:
        agent-inject: true
        agent-init-first: true
        agent-pre-populate-only: true
        log-level: info
        preserve-secret-case: true
        role: k8s-default
        secret-volume-path: /run/secrets
```

The serviceAccount used by Vault will match the default serviceAccount for the workload.

## Example

The following includes an example Hashicorp Vault secrets as well as a value values.yaml that make use of the secrets and an example of where secrets will be placed into the container.

**Example: Hashicorp Vault secrets**

```none
SECRET:secrets/jsmith@example.com/jsmith-namespace/licenses

{
"pingaccess-6.2": "Product=PingAccess\nVersion=6.2...",
"pingdirectory-8.2": "Product=PingDirectory\nVersion=8.2...",
"pingfederate-10.2": "Product=PingFederate\nVersion=10.2..."
}

SECRET: secrets/jsmith@example.com/jsmith-namespace/devops-secrets.env

{
"PING_IDENTITY_ACCEPT_EULA": "YES",
"PING_IDENTITY_DEVOPS_KEY": "d254....-....-...-...-............",
"PING_IDENTITY_DEVOPS_USER": "jsmith@example.com"
}

SECRET: secrets/jsmith@example.com/jsmith-namespace/certs

{
"tls.crt": "LS0tLS1CRUdJ...a9dk",
"tls.key": "LS0tLS1CRUdJ...38sj"
}
```

**Example: Vault secrets .yaml**

```yaml
pingfederate-admin:
  vault:
    hashicorp:
      secrets:
        devops-secret.env:
          to-json:
            file: devops-secret.env
        licenses:
          pingaccess-6.2:
            file: pingaccess.lic
            path: /opt/in/some/location/licenses
        test-certs:
          to-json:
            file: test-certs
```

Places the following files into the container.

**Example: Container files**

FILE: /run/secrets/devops-secret.env

```none
PING_IDENTITY_ACCEPT_EULA="YES"
PING_IDENTITY_DEVOPS_KEY="d254....-....-...-...-............"
PING_IDENTITY_DEVOPS_USER="jsmith@example.com"
```

FILE: /opt/in/some/location/licenses/pingaccess.lic

```none
Product=PingAccess
Version=6.2
...
```

FILE: /run/secrets/tls.crt

```none
LS0tLS1CRUdJ...a9dk
```

FILE: /run/secrets/tls.key

```none
LS0tLS1CRUdJ...38sj
```

## Using Vault Secrets to Mount base64-Encoded Keystore Files

To pull keystore files from a Vault cluster, create a secret with separate keys for each individual keystore file. The value of each key should be the base64 representation of the file that needs to be mounted. The names of the keys as well as the name of the secret will be used in the Helm values yaml when mounting the keystore files.

Environment variables or other configuration for the product being deployed will need to be set to point to the location where the keystores are being mounted. For example, for PingDirectory:

```none
KEYSTORE_FILE=/run/secrets/mykeystore.jks
KEYSTORE_PIN_FILE=/run/secrets/mykeystore.pin
```

Ensure the Vault cluster is accessible to the Kubernetes cluster where your Helm release is being deployed. You can then use the Vault annotations to mount the keystore files in the desired location. For an example, see the "Vault Keystores" example on the [Helm examples page](https://developer.pingidentity.com/helm/examples/index.html).

---

---
title: VolumeMounts Configuration
description: Mount secret and configMap data into a Ping Identity Helm chart workload container using volumes and volumeMounts
component: helm
page_id: helm::configs/volumemounts
canonical_url: https://developer.pingidentity.com/helm/configs/volumemounts.html
llms_txt: https://developer.pingidentity.com/helm/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  globalproduct-section: Global/Product Section
---

# VolumeMounts Configuration

Provides support for mounting secret or configMap volumes on a workload container.

## Global/Product Section

Adds ability to use **secret** and **configMap** data in a container via a VolumeMount. A common use for this configuration is bringing product licenses or scripts into the container.

**Example of creating two volume mounts in container from secret and configMap:**

```yaml
pingfederate-admin:
   enabled: true
   volumes:
     - name: pf-props
       configMap:
         name: pingfederate-props
     - name: pf-license
       secret:
         secretName: pingfederate-license
   volumeMounts:
     - mountPath: /opt/in/etc/pingfederate.properties
       name: pf-props
     - mountPath: /opt/in/instance/server/default/conf/pingfederate.lic
       name: pf-license
```

|   |                                                                                                                                                                                                                                             |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | [Secrets](https://kubernetes.io/docs/tasks/configmap-secret/managing-secret-using-kubectl) and [ConfigMaps](https://kubernetes.io/docs/concepts/configuration/configmap/) must be created in the cluster prior to deploying the helm chart. |

In this case, a secret (called `pingfederate-license`) and configMap (called `pingfederate-props`) will bring in a couple of key values (license, hello) and (pf-props) into the container as specific files. The resulting object will look like this:

**Example of kubectl describe of pingfederate-admin container**

```yaml
Containers:
  pingfederate-admin:
    Mounts:
      /opt/in/etc/pingfederate.properties from pingfederate-props (ro,path="pingfederate.properties")
      /opt/in/instance/server/default/conf/pingfederate.lic from pingfederate-license (ro,path="pingfederate.lic")
Volumes:
  pingfederate-license:
    Type:        Secret (a volume populated by a Secret)
    SecretName:  pingfederate-license
    Optional:    false
  pingfederate-props:
    Type:      ConfigMap (a volume populated by a ConfigMap)
    Name:      pingfederate-props
    Optional:  false
```

---

---
title: Workload Configuration
description: Configure Deployment and StatefulSet workload settings, including security context and waitFor, in Ping Identity Helm charts
component: helm
page_id: helm::configs/workload
canonical_url: https://developer.pingidentity.com/helm/configs/workload.html
llms_txt: https://developer.pingidentity.com/helm/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  global-section: Global Section
  persistent-volumes: Persistent Volumes
  security-context: Security Context
  waitfor: WaitFor
---

# Workload Configuration

Kubernetes Workload resources are created depending on configuration values:

* [Deployments](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/)

* [StatefulSets](https://kubernetes.io/docs/concepts/workloads/controllers/statefulset/)

## Global Section

Default yaml is defined in the global `workload` section. Individual products override these defaults based on the required workload.

```yaml
global:
  workload:
    type: Deployment

    deployment:
      strategy:
        type: RollingUpdate
        rollingUpdate:
          maxSurge: 1
          maxUnavailable: 0

    statefulSet:
      partition: 0

      persistentvolume:
        enabled: true
        volumes:
          out-dir:
            mountPath: /opt/out
            persistentVolumeClaim:
              accessModes:
              - ReadWriteOnce
              storageClassName:
              resources:
                requests:
                  storage: 4Gi

    securityContext:
      fsGroup: 9999
    securityContext: {}
```

| Workload Parameters               | Description                                                                                  |
| --------------------------------- | -------------------------------------------------------------------------------------------- |
| type                              | One of Deployment or StatefulSet                                                             |
| deployment.strategy.type          | One of RollingUpdate or ReCreate                                                             |
| deployment.strategy.rollingUpdate | If type=RollingUpdate                                                                        |
| statefulSet.partition             | Used for canary testing if n>0                                                               |
| statefulSet.persistentVolume      | Provides details around creation of PVC/Volumes (see below)                                  |
| securityContext                   | Provides security context details for starting container as different user/group (see below) |
| securityContext.fsGroup           | Sets the group id on fileSystem writes. This is needed especially for mounted volumes (pvs)  |

### Persistent Volumes

For every volume defined in the volumes list, three items will be created in the StatefulSet:

* container.volumeMounts — name and mountPath

* template.spec.volume — name and persistentVolumeClaim.claimName

* spec.volumeClaimTemplates — persistentVolumeClaim

For further details, see the [Kubernetes documentation](https://kubernetes.io/docs/concepts/storage/persistent-volumes/).

### Security Context

To run the containers with a different user/group/fsgroup, use the following example to set those details on the deployment/statefulset:

```yaml
global:
  workload:
    container:
      securityContext:
        runAsGroup: 9999
        runAsUser: 9031
        fsGroup: 9999
```

### WaitFor

For each product, you can provide a `waitFor` structure indicating the name, service, and timeout (in seconds) for which the container should wait before continuing (default: 300). This setting will inject an initContainer using the PingToolkit wait-for utility that relies on `nc host:port` before continuing.

Example: PingFederate Admin waiting on pingdirectory ldaps service to be available

```yaml
pingfederate-admin:
  container:
    waitFor:
      pingdirectory:
        service: ldaps
        timeoutSeconds: 600
      pingauthorize:
        service: https
        timeoutSeconds: 300
```

* By default, the pingfederate-engine will waitFor pingfederate-admin before it starts.

* By default, the pingaccess-engine will waitFor pingaccess-admin before it starts.