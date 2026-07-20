---
title: Enhanced Utility Sidecar Examples
description: Walk through enhanced utilitySidecar examples for custom commands, envFrom, and fallback volumes in Ping Identity Helm charts
component: helm
page_id: helm::examples/enhanced-sidecar
canonical_url: https://developer.pingidentity.com/helm/examples/enhanced-sidecar.html
llms_txt: https://developer.pingidentity.com/helm/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
page_aliases: ["devops:how-to:enhanced-sidecar.adoc"]
section_ids:
  devops-enhanced-sidecar-what-changed: What Changed
  devops-enhanced-sidecar-prerequisites: Prerequisites
  devops-enhanced-sidecar-example-files: Example Files
  devops-enhanced-sidecar-render-examples: Render the examples without installing them:
  devops-enhanced-sidecar-example-1: "Example 1: Backward-Compatible PingDirectory Backup Pattern"
  deploy-the-example: Deploy the Example
  devops-enhanced-sidecar-example-2: "Example 2: Custom Command, Args, and envFrom"
  devops-enhanced-sidecar-example-3: "Example 3: Deployment-Based Sidecar with Fallback Volumes"
  devops-enhanced-sidecar-diagnostics: Common Diagnostics
---

# Enhanced Utility Sidecar Examples

This page demonstrates the `utilitySidecar` enhancements added to the Ping Identity Helm charts starting in version `0.12.1`. Use these examples as a starting point when you want to keep sidecar-based operational tasks, such as backup, restore, support collection, or lightweight tooling, separate from the main product container.

For baseline sidecar pattern, see [Using a Utility Sidecar](https://developer.pingidentity.com/devops/deployment/deployK8sUtilitySidecar.html).

For more general Helm examples, see [Helm Chart Example Configurations](../helm-charts-landing-page.html).

## What Changed

Previous `utilitySidecar` behavior in `_workload.tpl` had several fixed assumptions:

* `utilitySidecar` always rendered `command: ["tail"]` and `args: ["-f", "/dev/null"]`

* The sidecar always mounted `/opt/out` from a hardcoded `out-dir` volume name

* The sidecar always mounted `/tmp` from a hardcoded `temp` volume name

* `envFrom` was not supported

* No fallback logic ensured that `temp` and `out-dir` pod volumes actually existed

* The schema documented only `enabled` and `resources`, even though the template also accepted `image`, `env`, `securityContext`, and extra sidecar volume mounts

The current behavior expands and aligns the contract:

* `utilitySidecar.command` is optional and defaults to `tail` only when unset

* `utilitySidecar.args` is optional and defaults to `-f /dev/null` only when unset

* `utilitySidecar.envFrom` renders when provided

* `/opt/out` mounts the resolved rendered volume name instead of always using the literal `out-dir`

* For StatefulSets, if naming rules render `out-dir-<release>`, the sidecar mounts that exact resolved name

* If `utilitySidecar.enabled=true` and `temp` or `out-dir` are missing, fallback `emptyDir` volumes are created

* Fallback volume creation is skipped when those volumes already come from product volumes, `includeVolumes`, StatefulSet PVC volumes, or workload secret/configMap volume helpers

* `utilitySidecar.volumes` still adds only sidecar `volumeMounts`; it does not create pod volumes

* `values.schema.json` and `values.yaml` now align with the fields the template accepts, including `image`, `command`, `args`, `resources`, `env`, `envFrom`, `securityContext`, and extra sidecar volume mounts

## Prerequisites

* Helm chart version `0.12.1` or later

* `kubectl` and `helm`

* A reachable Kubernetes cluster with a working `kubectl` context

* A valid `devops-secret` in the namespace you use if you want the Ping product containers to start successfully

* See [Deploy an Example Stack](https://developer.pingidentity.com/devops/get-started/getStartedExample.html) for more details on these prerequisites.

If you only want to inspect rendered manifests, a running cluster is not required.

## Example Files

The example values files are stored in the `pingidentity-devops-getting-started` repository under `30-helm/enhanced-sidecar/`:

* [01-pingdirectory-periodic-backup-compatible.yaml](https://raw.githubusercontent.com/pingidentity/pingidentity-devops-getting-started/master/30-helm/enhanced-sidecar/01-pingdirectory-periodic-backup-compatible.yaml)

* [02-pingdirectory-custom-command-envfrom.yaml](https://raw.githubusercontent.com/pingidentity/pingidentity-devops-getting-started/master/30-helm/enhanced-sidecar/02-pingdirectory-custom-command-envfrom.yaml)

* [03-pingdataconsole-deployment-sidecar.yaml](https://raw.githubusercontent.com/pingidentity/pingidentity-devops-getting-started/master/30-helm/enhanced-sidecar/03-pingdataconsole-deployment-sidecar.yaml)

## Render the examples without installing them:

If you want to inspect the rendered manifests without installing the examples into a cluster, use `helm template` with the example values files:

```shell
helm template demo-01 pingidentity/ping-devops \
  -f 30-helm/enhanced-sidecar/01-pingdirectory-periodic-backup-compatible.yaml

helm template demo-02 pingidentity/ping-devops \
  -f 30-helm/enhanced-sidecar/02-pingdirectory-custom-command-envfrom.yaml

helm template demo-03 pingidentity/ping-devops \
  -f 30-helm/enhanced-sidecar/03-pingdataconsole-deployment-sidecar.yaml
```

## Example 1: Backward-Compatible PingDirectory Backup Pattern

Use [01-pingdirectory-periodic-backup-compatible.yaml](https://raw.githubusercontent.com/pingidentity/pingidentity-devops-getting-started/master/30-helm/enhanced-sidecar/01-pingdirectory-periodic-backup-compatible.yaml) when you want the familiar PingDirectory backup pattern while staying compatible with the enhanced template behavior. This example is primarily to demonstrate that the enhancements do not break existing patterns, but it also serves as a starting point for users who want to keep using backup and restore scripts delivered via ConfigMaps without needing to adopt the new `command`, `args`, or `envFrom` features.

This example:

* Preserves the historical `utilitySidecar` backup style

* Uses an explicit `temp` volume

* Mounts backup and restore scripts into the sidecar

* Keeps the sidecar idle using the default `tail -f /dev/null` behavior

### Deploy the Example

These steps will walk through the process: Create a namespace, create the required secret, create the backup and restore ConfigMaps, and install the example:

```shell
# Namespace
kubectl create namespace sidecar-demo-01

# DevOps Secret
kubectl -n sidecar-demo-01 create secret generic devops-secret \
  --from-literal=PING_IDENTITY_DEVOPS_USER='<your devops user>' \
  --from-literal=PING_IDENTITY_DEVOPS_KEY='<your devops key>'
  --from-literal=PING_IDENTITY_ACCEPT_EULA='yes'

# Backup and Restore ConfigMaps (sample scripts that just print a message and exit successfully)
# Sleep provides time to access the logs of the container and see the message
# before the script finishes and the container exits.
printf '%s\n' '#!/bin/sh' 'sleep 30 && echo backup-ran' > /tmp/backup.sh
printf '%s\n' '#!/bin/sh' 'sleep 30 && echo restore-ran' > /tmp/restore.sh
chmod +x /tmp/backup.sh /tmp/restore.sh

kubectl -n sidecar-demo-01 create configmap pingdirectory-backup \
  --from-file=backup.sh=/tmp/backup.sh
kubectl -n sidecar-demo-01 create configmap pingdirectory-restore \
  --from-file=restore.sh=/tmp/restore.sh

# Install the example
helm upgrade --install sidecar-demo-01 pingidentity/ping-devops \
  -n sidecar-demo-01 \
  -f 30-helm/enhanced-sidecar/01-pingdirectory-periodic-backup-compatible.yaml
```

Verify that the sidecar and backup mounts render as expected:

```shell
kubectl -n sidecar-demo-01 get pod -o yaml | \
  rg -n "name: utility-sidecar|mountPath: /opt/in/backup.sh|mountPath: /opt/in/restore.sh|mountPath: /tmp"

# Sample output:
107:      - mountPath: /tmp
121:      name: utility-sidecar
139:      - mountPath: /tmp
141:      - mountPath: /opt/in/backup.sh
144:      - mountPath: /opt/in/restore.sh
271:      - mountPath: /tmp
286:      name: utility-sidecar
309:      - mountPath: /tmp
311:      - mountPath: /opt/in/backup.sh
313:      - mountPath: /opt/in/restore.sh

kubectl -n sidecar-demo-01 get cronjob sidecar-demo-01-pingdirectory-cronjob -o yaml | \
  rg -n "utility-sidecar|/opt/in/backup.sh"

# Sample output:
30:            - kubectl exec -ti sidecar-demo-01-pingdirectory-0 --container utility-sidecar
31:              -- /opt/in/backup.sh
```

## Example 2: Custom Command, Args, and `envFrom`

Use [02-pingdirectory-custom-command-envfrom.yaml](https://raw.githubusercontent.com/pingidentity/pingidentity-devops-getting-started/master/30-helm/enhanced-sidecar/02-pingdirectory-custom-command-envfrom.yaml) is an example of using the newly supported `command`, `args`, and `envFrom` fields.

This example:

* Overrides the sidecar command with `/bin/sh -c`

* Uses custom startup logic in `args`

* Adds `envFrom` references to both a ConfigMap and a Secret

* Keeps script delivery in a ConfigMap mounted into the sidecar

As above, these steps will walk through the process: Create the namespace and referenced runtime objects, then install the example:

```shell
# Namespace
kubectl create namespace sidecar-demo-02

# DevOps Secret
kubectl -n sidecar-demo-02 create secret generic devops-secret \
  --from-literal=PING_IDENTITY_DEVOPS_USER='<your devops user>' \
  --from-literal=PING_IDENTITY_DEVOPS_KEY='<your devops key>'
  --from-literal=PING_IDENTITY_ACCEPT_EULA='yes'

# Runtime Objects
kubectl -n sidecar-demo-02 create configmap sidecar-runtime-env \
  --from-literal=EXAMPLE_FLAG=true

kubectl -n sidecar-demo-02 create secret generic sidecar-runtime-secret \
  --from-literal=EXAMPLE_SECRET=value

# Install the example
helm upgrade --install sidecar-demo-02 pingidentity/ping-devops \
  -n sidecar-demo-02 \
  -f 30-helm/enhanced-sidecar/02-pingdirectory-custom-command-envfrom.yaml
```

Verify that the custom command, args, and environment sources render:

```shell
kubectl -n sidecar-demo-02 get statefulset sidecar-demo-02-pingdirectory -o yaml | \
  rg -n "utility-sidecar|/bin/sh|-c|chmod \\+x /opt/in/collect-support.sh|tail -f /dev/null"

# Sample output:
# The chmod and tail commands are arguments passed by the
# sample values file.
17:  uid: ff44ff10-6901-4ee3-b04e-c5509c49e6ee
29:  serviceName: sidecar-demo-02-pingdirectory-cluster
122:          chmod +x /opt/in/collect-support.sh
123:          tail -f /dev/null
125:        - /bin/sh
126:        - -c
137:        name: utility-sidecar

kubectl -n sidecar-demo-02 get statefulset sidecar-demo-02-pingdirectory -o yaml

# Sample output from approximately line 128:
        env:
        - name: SIDECAREXAMPLE_MODE
          value: collect-support
        envFrom:
        - configMapRef:
            name: sidecar-runtime-env
        - secretRef:
            name: sidecar-runtime-secret
```

## Example 3: Deployment-Based Sidecar with Fallback Volumes

Use [03-pingdataconsole-deployment-sidecar.yaml](https://raw.githubusercontent.com/pingidentity/pingidentity-devops-getting-started/master/30-helm/enhanced-sidecar/03-pingdataconsole-deployment-sidecar.yaml) as the example of using the minimal sidecar pattern on a Deployment-based workload.

This example highlights the new fallback logic:

* `utilitySidecar.enabled: true` is enough to trigger fallback `temp` and `out-dir` creation when those pod volumes are otherwise missing

* `includeVolumes` still defines extra pod volumes

* `utilitySidecar.volumes` still adds only sidecar volume mounts

Create the namespace and referenced objects, then install the example:

```shell
kubectl create namespace sidecar-demo-03

kubectl -n sidecar-demo-03 create secret generic devops-secret \
  --from-literal=PING_IDENTITY_DEVOPS_USER='<your devops user>' \
  --from-literal=PING_IDENTITY_DEVOPS_KEY='<your devops key>'
  --from-literal=PING_IDENTITY_ACCEPT_EULA='yes'

kubectl -n sidecar-demo-03 create configmap pingdataconsole-sidecar-env \
  --from-literal=FEATURE_FLAG=enabled

printf '%s\n' '#!/bin/sh' 'sleep 30 && echo tool-ran' > /tmp/tool.sh
kubectl -n sidecar-demo-03 create configmap pingdataconsole-sidecar-tools \
  --from-file=tool.sh=/tmp/tool.sh

helm upgrade --install sidecar-demo-03 pingidentity/ping-devops \
  -n sidecar-demo-03 \
  -f 30-helm/enhanced-sidecar/03-pingdataconsole-deployment-sidecar.yaml
```

Verify that the fallback volumes and included sidecar mount render:

```shell
kubectl -n sidecar-demo-03 get deployment sidecar-demo-03-pingdataconsole -o yaml | \
  rg -n "name: utility-sidecar|mountPath: /opt/out|mountPath: /tmp|mountPath: /opt/in/tools"

# Sample output from approximately line 122
        name: utility-sidecar
        resources:
          limits:
            cpu: "1"
            memory: 2Gi
          requests:
            cpu: "0"
            memory: 128Mi
        securityContext:
          allowPrivilegeEscalation: false
          capabilities:
            drop:
            - ALL
        terminationMessagePath: /dev/termination-log
        terminationMessagePolicy: File
        volumeMounts:
        - mountPath: /opt/out
          name: out-dir
        - mountPath: /tmp
          name: temp
        - mountPath: /opt/in/tools
          name: tools-config

kubectl -n sidecar-demo-03 get deployment sidecar-demo-03-pingdataconsole -o yaml | \
  rg -n "name: temp|name: out-dir|emptyDir|tools-config"

# Sample output:
139:          name: out-dir
141:          name: temp
143:          name: tools-config
161:        name: tools-config
162:      - emptyDir: {}
163:        name: temp
164:      - emptyDir: {}
165:        name: out-dir
```

## Common Diagnostics

Use these commands when a sidecar example does not behave as expected:

```shell
helm list -A | rg sidecar-demo
kubectl get pods -A | rg sidecar-demo

helm -n sidecar-demo-01 get manifest sidecar-demo-01 | rg -n "utility-sidecar|out-dir|temp|cronjob"
helm -n sidecar-demo-02 get manifest sidecar-demo-02 | rg -n "utility-sidecar|envFrom|collect-support"
helm -n sidecar-demo-03 get manifest sidecar-demo-03 | rg -n "utility-sidecar|out-dir|temp|tools-config"
```

If the workload does not start, confirm that the `devops-secret` values are valid for the namespace you used and that your environment can pull the required Ping images.

---

---
title: Gateway API LDAPS Example
description: Walk through exposing PingDirectory over HTTPS and LDAPS using Gateway API and Traefik with the Ping Identity Helm chart
component: helm
page_id: helm::examples/gatewayLDAPSWithTCPRroute
canonical_url: https://developer.pingidentity.com/helm/examples/gatewayLDAPSWithTCPRroute.html
llms_txt: https://developer.pingidentity.com/helm/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  devops-what-you-will-deploy: What You Will Deploy
  devops-files-used: Files Used
  devops-install-gateway-api-crds: Install Gateway API CRDs
  devops-install-traefik: Install or Update Traefik
  devops-create-namespace-and-secret: Create the Namespace and TLS Secret
  devops-apply-the-gateway: Apply the Gateway and Create a Secret for DevOps License
  devops-deploy-the-chart: Deploy the Ping Identity Chart
  devops-add-host-mappings: Add Local Host Mappings
  devops-validate-rendered-routes: Validate the Rendered Routes
  devops-validate-browser-access: Validate Browser Access and Console Login
  devops-validate-cli-access: Validate HTTPS and LDAPS Access with CLI
  devops-troubleshooting: Troubleshooting
  devops-cleanup: Cleanup
---

# Gateway API LDAPS Example

This walkthrough shows how to expose PingDirectory over both HTTPS and LDAPS through Gateway API with Traefik.

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | This example was written using Docker Desktop with Kubernetes enabled on the Mac platform using the Apple Silicon chip. The Docker Desktop version used for this guide was `4.67.0 (222858)`, which includes Docker Engine `29.3.1` and Kubernetes `v1.34.1`. The walkthrough uses Gateway API `v1.4.1`, Traefik `3.6.12` as the Gateway controller, and the ping-devops Helm chart `0.12.2` (the release version at which TCPRoute support was added). The Docker Desktop Kubernetes environment was reset before starting. |

|   |                                                                                                                                                                                                                                                                                                                                                                             |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Traefik 3.6.12 is the latest version installed by default using their Helm charts `v39.0.7` as of the time of this writing. However, currently Traefik at any version is not compatible with the most recent version of the Gateway API (1.5.1). Until support for the latest Gateway API version is added to Traefik, you must use Gateway API v1.4.1 to run this example. |

The [Getting Started](../getting-started/getting-started.html) page has instructions on getting your environment configured for using Ping ping-devops Helm charts.

For more examples, see [Helm Chart Example Configurations](../helm-charts-landing-page.html).

For more information on Helm with Ping products, see [Ping Identity DevOps Helm Charts](../helm-charts-landing-page.html).

## What You Will Deploy

When finished with this example, you will have deployed the following:

* Release name: `gateway-ldaps-demo`

* Namespace: `ping-gateway`

* Gateway API CRDs if not already installed in Docker Desktop Kubernetes

* The experimental Gateway API channel is installed because `TCPRoute` is still `gateway.networking.k8s.io/v1alpha2`

* Traefik running in namespace `traefik`

## Files Used

The example values files are stored in the `pingidentity-devops-getting-started` repository under `30-helm/gateway/tcproute/`. You will need to clone the repository or copy the files locally to run the example. The files are:

* [gateway\_ldaps\_demo\_values.yaml](https://raw.githubusercontent.com/pingidentity/pingidentity-devops-getting-started/master/30-helm/gateway/tcproute/gateway_ldaps_demo_values.yaml)

* [gateway\_ldaps\_demo\_gateway.yaml](https://raw.githubusercontent.com/pingidentity/pingidentity-devops-getting-started/master/30-helm/gateway/tcproute/gateway_ldaps_demo_gateway.yaml)

* [gateway\_ldaps\_demo\_traefik\_values.yaml](https://raw.githubusercontent.com/pingidentity/pingidentity-devops-getting-started/master/30-helm/gateway/tcproute/gateway_ldaps_demo_traefik_values.yaml)

An expected route render file is also included for reference:

* [gateway\_ldaps\_demo\_expected\_routes.yaml](https://raw.githubusercontent.com/pingidentity/pingidentity-devops-getting-started/master/30-helm/gateway/tcproute/gateway_ldaps_demo_expected_routes.yaml)

|   |                                                                                                                            |
| - | -------------------------------------------------------------------------------------------------------------------------- |
|   | The YAML files noted above are annotated to inform the reader what each entry accomplishes in the context of this example. |

## Install Gateway API CRDs

1. Install the standard and experimental Gateway API CRDs before rendering `TCPRoute`.

   ```shell
    kubectl apply --server-side=true -f https://github.com/kubernetes-sigs/gateway-api/releases/download/v1.4.1/standard-install.yaml

    kubectl apply --server-side=true -f https://github.com/kubernetes-sigs/gateway-api/releases/download/v1.4.1/experimental-install.yaml

   # Confirm the CRDs are installed
   kubectl get crd | grep gateway.networking.k8s.

   backendtlspolicies.gateway.networking.k8s.io          2026-04-08T20:49:22Z
   gatewayclasses.gateway.networking.k8s.io              2026-04-08T20:49:22Z
   gateways.gateway.networking.k8s.io                    2026-04-08T20:49:22Z
   grpcroutes.gateway.networking.k8s.io                  2026-04-08T20:49:22Z
   httproutes.gateway.networking.k8s.io                  2026-04-08T20:49:22Z
   referencegrants.gateway.networking.k8s.io             2026-04-08T20:49:22Z
   tcproutes.gateway.networking.k8s.io                   2026-04-08T20:49:22Z
   tlsroutes.gateway.networking.k8s.io                   2026-04-08T20:49:22Z
   udproutes.gateway.networking.k8s.io                   2026-04-08T20:49:22Z
   ```

|   |                                                                                                                                                                                                                                                              |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | The `kubectl apply` commands used above use the `--server-side=true` flag due to the size of the Gateway API CRD manifests. See [Gateway API v1.4.1 Release Notes](https://github.com/kubernetes-sigs/gateway-api/releases/tag/v1.4.1) for more information. |

## Install or Update Traefik

1. Use the Traefik values file to enable Gateway API and the LDAPS TCP entrypoint.

   ```shell
   helm repo add traefik https://traefik.github.io/charts
   helm repo update

   helm upgrade --install traefik traefik/traefik \
     --namespace traefik \
     --create-namespace \
     -f 30-helm/gateway/tcproute/gateway_ldaps_demo_traefik_values.yaml \
     --skip-crds
   ```

## Create the Namespace and TLS Secret

1. Create the application namespace and a TLS secret for the HTTPS listener.

   ```shell
   kubectl create namespace ping-gateway

   # Set the kubectl context to the namespace
   kubectl config set-context --current --namespace=ping-gateway

   # Confirm
   kubectl config view --minify | grep namespace:

   # Create a self-signed certificate for the HTTPS listener.
   # The common name should match the hostnames used in the `HTTPRoute` resources.
   openssl req -x509 -nodes -days 365 \
     -newkey rsa:2048 \
     -keyout gateway-demo.key \
     -out gateway-demo.crt \
     -subj "/CN=*.pingdemo.example"

   kubectl -n ping-gateway create secret tls gateway-demo-tls \
     --cert=gateway-demo.crt \
     --key=gateway-demo.key
   ```

## Apply the Gateway and Create a Secret for DevOps License

1. Apply the Gateway manifest.

   ```shell
   kubectl apply -f 30-helm/gateway/tcproute/gateway_ldaps_demo_gateway.yaml
   ```

   The Gateway creates:

   * An HTTPS listener on port `8443`

   * An LDAPS TCP listener on port `1636`

     The TCP listener name is `ldaps-1636`. The chart values bind the `TCPRoute` to that listener with `sectionName`.

2. Create a secret in the namespace you will be using to run the example. This secret provides credentials to obtain an evaluation license based on your Ping DevOps username and key:

   ```shell
   kubectl create secret generic devops-secret \
     --from-literal=PING_IDENTITY_DEVOPS_USER="$PING_IDENTITY_DEVOPS_USER" \
     --from-literal=PING_IDENTITY_DEVOPS_KEY="$PING_IDENTITY_DEVOPS_KEY" \
     --from-literal=PING_IDENTITY_ACCEPT_EULA="$PING_IDENTITY_ACCEPT_EULA" \
     --type=Opaque \
     --dry-run=client -o yaml | kubectl apply -f -
   ```

## Deploy the Ping Identity Chart

1. Deploy the chart with the LDAPS example values.

   ```shell
   helm upgrade --install gateway-ldaps-demo pingidentity/ping-devops \
     --namespace ping-gateway \
     -f 30-helm/gateway/tcproute/gateway_ldaps_demo_values.yaml
   ```

   The example deploys:

   * `pingdirectory`

   * `pingdataconsole`

     The chart renders:

   * An `HTTPRoute` for PingDirectory admin HTTPS

   * An `HTTPRoute` for PingDataConsole

   * A `TCPRoute` for PingDirectory LDAPS

## Add Local Host Mappings

1. Docker Desktop exposes the Traefik `LoadBalancer` on the local host. Add the example hostnames to `/etc/hosts`.

   ```text
   127.0.0.1 gateway-ldaps-demo-pingdataconsole.pingdemo.example gateway-ldaps-demo-pingdirectory.pingdemo.example
   ```

## Validate the Rendered Routes

1. Confirm that the Gateway, `HTTPRoute`, and `TCPRoute` resources were created.

   ```shell
   kubectl -n ping-gateway get gateway,httproute,tcproute

   # Expected output includes:
   NAME                                                    CLASS     ADDRESS      PROGRAMMED   AGE
   gateway.gateway.networking.k8s.io/ping-devops-gateway   traefik   172.19.0.5   True         112s

   NAME                                                                     HOSTNAMES                                                 AGE
   httproute.gateway.networking.k8s.io/gateway-ldaps-demo-pingdataconsole   ["gateway-ldaps-demo-pingdataconsole.pingdemo.example"]   65s
   httproute.gateway.networking.k8s.io/gateway-ldaps-demo-pingdirectory     ["gateway-ldaps-demo-pingdirectory.pingdemo.example"]     65s

   NAME                                                                        AGE
   tcproute.gateway.networking.k8s.io/gateway-ldaps-demo-pingdirectory-ldaps   65s
   ```

## Validate Browser Access and Console Login

1. Open PingDataConsole in a browser:

   `https://gateway-ldaps-demo-pingdataconsole.pingdemo.example/console/signin`

   Accept the browser certificate warning.

2. Use these login values in the PingDataConsole sign-in form:

   * Server: `ldaps://gateway-ldaps-demo-pingdirectory-cluster:1636`

   * Username: `administrator`

   * Password: `2FederateM0re`

     Operational success for the browser path is:

   * The console login page loads through the `HTTPRoute`

   * The console successfully authenticates to PingDirectory over LDAPS using the in-cluster cluster service

   * The console displays the connected PingDirectory server after login

## Validate HTTPS and LDAPS Access with CLI

1. Validate PingDataConsole.

   ```shell
   curl -skI --resolve gateway-ldaps-demo-pingdataconsole.pingdemo.example:443:127.0.0.1 \
     https://gateway-ldaps-demo-pingdataconsole.pingdemo.example/
   ```

   Expected result: `HTTP/2 200`

2. Validate PingDirectory admin HTTPS.

   ```shell
   curl -skI --resolve gateway-ldaps-demo-pingdirectory.pingdemo.example:443:127.0.0.1 \
     https://gateway-ldaps-demo-pingdirectory.pingdemo.example/
   ```

   Expected result: a valid HTTP response from PingDirectory, which may be `404` at `/`

3. Validate PingDirectory LDAPS.

   ```shell
   openssl s_client -connect 127.0.0.1:1636 \
     -servername gateway-ldaps-demo-pingdirectory.pingdemo.example </dev/null
   ```

   Expected result: successful TLS handshake and a PingDirectory self-signed certificate

## Troubleshooting

* If `TCPRoute` does not render, verify the cluster has the experimental Gateway API CRDs installed.

* If the `TCPRoute` renders but does not attach, verify the Gateway listener name matches `sectionName: ldaps-1636`.

* If Traefik does not expose `1636`, verify the LDAPS port is enabled in the Traefik values and the Service publishes it.

* If the browser console loads but the server login fails, verify the server field is `ldaps://gateway-ldaps-demo-pingdirectory-cluster:1636`.

* If PingDataConsole cannot bind to PingDirectory, verify `defaultLogin.server.host` is `pingdirectory-cluster`, which the chart expands to `gateway-ldaps-demo-pingdirectory-cluster`.

## Cleanup

1. Remove the example resources.

   ```shell
   helm uninstall gateway-ldaps-demo -n ping-gateway
   kubectl delete -f 30-helm/gateway/tcproute/gateway_ldaps_demo_gateway.yaml
   kubectl delete namespace ping-gateway

   # Optionally, remove Traefik and the Gateway API CRDs if no longer needed:
   kubectl delete namespace traefik
   kubectl delete -f https://github.com/kubernetes-sigs/gateway-api/releases/download/v1.4.1/experimental-install.yaml
   kubectl delete -f https://github.com/kubernetes-sigs/gateway-api/releases/download/v1.4.1/standard-install.yaml
   ```

---

---
title: Helm Chart Examples
description: List example Helm values files for deploying Ping Identity products, including ingress, vault, and Gateway API configurations
component: helm
page_id: helm::examples/index
canonical_url: https://developer.pingidentity.com/helm/examples/index.html
llms_txt: https://developer.pingidentity.com/helm/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
page_aliases: ["devops:deployment:deployHelm.adoc"]
section_ids:
  devops-helm-chart-example-configurations: Helm Chart Example Configurations
  devops-to-deploy: To Deploy
  devops-uninstall: Uninstall
---

# Helm Chart Examples

Install and configure Helm according to [Getting Started](../getting-started/getting-started.html) before trying these examples.

|   |                                                                                                                                                                                                                                           |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | If you want to be notified when new chart version is released, see **Orchestration/Helm/Kubernetes** section of [FAQ page](https://developer.pingidentity.com/devops/reference/faqs.html) for instructions on following chart repository. |

|   |                                                                                                                                                                                                                                                                 |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | If you want to run ingress-based examples on local kind cluster, see [this page](https://developer.pingidentity.com/devops/deployment/deployHelmLocalIngress.html) for ingress configuration instructions. Otherwise, you can port-forward to product services. |

## Helm Chart Example Configurations

Following table contains example configurations and instructions to run and configure Ping products using Ping Devops Helm Chart.

|                                                |                                                                                                          |                                                                                                                                                                                                                         |                                                                                                  |
| ---------------------------------------------- | -------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------ |
| Config                                         | Description                                                                                              | `.yaml`                                                                                                                                                                                                                 | Notes                                                                                            |
| Everything                                     | Example with most products integrated together                                                           | [everything.yaml](https://raw.githubusercontent.com/pingidentity/pingidentity-devops-getting-started/master/30-helm/everything.yaml)                                                                                    |                                                                                                  |
| Ingress                                        | Expose application outside cluster                                                                       | [ingress.yaml](https://raw.githubusercontent.com/pingidentity/pingidentity-devops-getting-started/master/30-helm/ingress.yaml)                                                                                          | Update line 7 with your domain                                                                   |
| RBAC                                           | Enable RBAC for workloads                                                                                | [rbac.yaml](https://raw.githubusercontent.com/pingidentity/pingidentity-devops-getting-started/master/30-helm/rbac.yaml)                                                                                                |                                                                                                  |
| Vault                                          | Example vault values section                                                                             | [vault.yaml](https://raw.githubusercontent.com/pingidentity/pingidentity-devops-getting-started/master/30-helm/vault.yaml)                                                                                              |                                                                                                  |
| Vault Keystores                                | Example vault values for keystores                                                                       | [vault-keystores.yaml](https://raw.githubusercontent.com/pingidentity/pingidentity-devops-getting-started/master/30-helm/vault-keystores.yaml)                                                                          |                                                                                                  |
| PingAccess                                     | PingAccess Admin Console & Engine                                                                        | [pingaccess-cluster.yaml](https://raw.githubusercontent.com/pingidentity/pingidentity-devops-getting-started/master/30-helm/pingaccess-cluster.yaml)                                                                    |                                                                                                  |
| PingAccess & PingFederate Integration          | PA & PF Admin Console & Engine                                                                           | [pingaccess-pingfederate-integration.yaml](https://raw.githubusercontent.com/pingidentity/pingidentity-devops-getting-started/master/30-helm/pingaccess-pingfederate-integration.yaml)                                  |                                                                                                  |
| PingFederate                                   | PingFederate Admin Console & Engine                                                                      | [pingfederate-cluster.yaml](https://raw.githubusercontent.com/pingidentity/pingidentity-devops-getting-started/master/30-helm/pingfederate-cluster.yaml)                                                                |                                                                                                  |
| PingFederate                                   | Upgrade PingFederate                                                                                     | See .yaml files in [pingfederate-upgrade](https://github.com/pingidentity/pingidentity-devops-getting-started/tree/master/30-helm/pingfederate-upgrade)                                                                 |                                                                                                  |
| PingDirectory                                  | PingDirectory Instance                                                                                   | [pingdirectory.yaml](https://raw.githubusercontent.com/pingidentity/pingidentity-devops-getting-started/master/30-helm/pingdirectory.yaml)                                                                              |                                                                                                  |
| PingDirectory Upgrade                          | PingDirectory Upgrade with partition                                                                     | See .yaml files in [pingdirectory-upgrade-partition](https://github.com/pingidentity/pingidentity-devops-getting-started/tree/master/30-helm/pingdirectory-upgrade-partition)                                           |                                                                                                  |
| PingDirectory Backup and Sidecar               | PingDirectory with periodic backup and sidecar                                                           | [pingdirectory-periodic-backup.yaml](https://raw.githubusercontent.com/pingidentity/pingidentity-devops-getting-started/master/30-helm/pingdirectory-backup/pingdirectory-periodic-backup.yaml)                         |                                                                                                  |
| Enhanced Utility Sidecar                       | Backward-compatible PingDirectory backup pattern                                                         | [01-pingdirectory-periodic-backup-compatible.yaml](https://raw.githubusercontent.com/pingidentity/pingidentity-devops-getting-started/master/30-helm/enhanced-sidecar/01-pingdirectory-periodic-backup-compatible.yaml) | Walkthrough: [Enhanced Utility Sidecar Examples](enhanced-sidecar.html)                          |
| Enhanced Utility Sidecar                       | PingDirectory sidecar with custom command, args, and envFrom                                             | [02-pingdirectory-custom-command-envfrom.yaml](https://raw.githubusercontent.com/pingidentity/pingidentity-devops-getting-started/master/30-helm/enhanced-sidecar/02-pingdirectory-custom-command-envfrom.yaml)         | Walkthrough: [Enhanced Utility Sidecar Examples](enhanced-sidecar.html)                          |
| Enhanced Utility Sidecar                       | PingDataConsole deployment with fallback sidecar volumes                                                 | [03-pingdataconsole-deployment-sidecar.yaml](https://raw.githubusercontent.com/pingidentity/pingidentity-devops-getting-started/master/30-helm/enhanced-sidecar/03-pingdataconsole-deployment-sidecar.yaml)             | Walkthrough: [Enhanced Utility Sidecar Examples](enhanced-sidecar.html)                          |
| Gateway API LDAPS                              | Expose PingDirectory over HTTPS and LDAPS through Gateway API with Traefik                               | [gateway\_ldaps\_demo\_values.yaml](https://raw.githubusercontent.com/pingidentity/pingidentity-devops-getting-started/master/30-helm/gateway/tcproute/gateway_ldaps_demo_values.yaml)                                  | Walkthrough: [Expose PingDirectory with Gateway API and Traefik](gatewayLDAPSWithTCPRroute.html) |
| PingDirectory Archive Backup to S3 (Demo Only) | Archive PingDirectory backup to S3                                                                       | Sample files in [s3-sidecar](https://github.com/pingidentity/pingidentity-devops-getting-started/tree/master/30-helm/s3-sidecar)                                                                                        |                                                                                                  |
| PingDirectory Scale Down                       | Scale down PingDirectory StatefulSet                                                                     | See .yaml files in [pingdirectory-scale-down](https://github.com/pingidentity/pingidentity-devops-getting-started/tree/master/30-helm/pingdirectory-scale-down)                                                         |                                                                                                  |
| PingAuthorize and PingDirectory                | PingAuthorize with PAP and PingDirectory                                                                 | [pingauthorize-pingdirectory.yaml](https://raw.githubusercontent.com/pingidentity/pingidentity-devops-getting-started/master/30-helm/pingauthorize-pingdirectory.yaml)                                                  |                                                                                                  |
| Entry Balancing                                | PingDirectory and PingDirectoryProxy entry balancing                                                     | See .yaml files in [entry-balancing](https://github.com/pingidentity/pingidentity-devops-getting-started/tree/master/30-helm/entry-balancing)                                                                           |                                                                                                  |
| PingCentral                                    | PingCentral                                                                                              | [pingcentral.yaml](https://raw.githubusercontent.com/pingidentity/pingidentity-devops-getting-started/master/30-helm/pingcentral.yaml)                                                                                  |                                                                                                  |
| PingCentral with MySQL                         | PingCentral with external MySQL deployment                                                               | [pingcentral-external-mysql-db.yaml](https://raw.githubusercontent.com/pingidentity/pingidentity-devops-getting-started/master/30-helm/pingcentral-external-mysql-db/pingcentral-external-mysql-db.yaml)                |                                                                                                  |
| Simple Sync                                    | PingDataSync and PingDirectory                                                                           | [simple-sync.yaml](https://raw.githubusercontent.com/pingidentity/pingidentity-devops-getting-started/master/30-helm/simple-sync.yaml)                                                                                  |                                                                                                  |
| PingDataSync Failover                          | PingDataSync and PingDirectory with failover                                                             | [pingdatasync-failover.yaml](https://raw.githubusercontent.com/pingidentity/pingidentity-devops-getting-started/master/30-helm/pingdatasync-failover.yaml)                                                              |                                                                                                  |
| Cluster Metrics                                | Example values using various open source tools                                                           | See .yaml files in [cluster-metrics](https://github.com/pingidentity/pingidentity-devops-getting-started/tree/master/30-helm/cluster-metrics)                                                                           |                                                                                                  |
| PingDataConsole SSO with PingOne               | Sign in to PingDataConsole with PingOne                                                                  | [pingdataconsole-pingone-sso.yaml](https://raw.githubusercontent.com/pingidentity/pingidentity-devops-getting-started/master/30-helm/pingdataconsole-pingone-sso.yaml)                                                  |                                                                                                  |
| Using CSI Volumes                              | Mount secrets with CSI volumes                                                                           | [csi-secrets-volume.yaml](https://raw.githubusercontent.com/pingidentity/pingidentity-devops-getting-started/master/30-helm/csi-secrets-volume.yaml)                                                                    |                                                                                                  |
| Secrets Store CSI Driver with Vault            | Deploy PingDirectory and PingFederate using Vault as a secrets provider via the Secrets Store CSI Driver | [ping-values.yaml](https://raw.githubusercontent.com/pingidentity/pingidentity-devops-getting-started/master/30-helm/vault-spc/ping-values.yaml)                                                                        | Walkthrough: [Using Secrets Store CSI Driver with HashiCorp Vault](vault-spc-walkthrough.html)   |
| Splunk logging sidecar                         | Forward product logs to Splunk                                                                           | See files in [splunk folder](https://github.com/pingidentity/pingidentity-devops-getting-started/tree/master/20-kubernetes/splunk)                                                                                      |                                                                                                  |
| ImagePullSecrets (individual)                  | Provide secret for private registry authentication                                                       | [image-pull-secrets-individual.yaml](https://raw.githubusercontent.com/pingidentity/pingidentity-devops-getting-started/master/30-helm/image-pull-secrets-individual.yaml)                                              | Replace stubs with your values                                                                   |
| ImagePullSecrets (global)                      | Provide global secret for private registry authentication                                                | [image-pull-secrets-global.yaml](https://raw.githubusercontent.com/pingidentity/pingidentity-devops-getting-started/master/30-helm/image-pull-secrets-global.yaml)                                                      | Replace stubs with your values                                                                   |

### To Deploy

```
helm upgrade --install myping pingidentity/ping-devops \
    -f <HTTP link to yaml>
```

### Uninstall

```
helm uninstall myping
```

---

---
title: Using Secrets Store CSI Driver with HashiCorp Vault
description: Walk through deploying PingDirectory and PingFederate with secrets sourced from HashiCorp Vault via the Secrets Store CSI Driver
component: helm
page_id: helm::examples/vault-spc-walkthrough
canonical_url: https://developer.pingidentity.com/helm/examples/vault-spc-walkthrough.html
llms_txt: https://developer.pingidentity.com/helm/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  devops-vault-spc-overview: Overview
  devops-vault-spc-prerequisites: Prerequisites
  devops-vault-spc-infra-setup: Infrastructure Setup (Steps 1–4)
  devops-vault-spc-step1: "Step 1: Install the Secrets Store CSI Driver"
  devops-vault-spc-step2: "Step 2: Install Vault with the CSI Provider"
  devops-vault-spc-step3: "Step 3: Seed Vault with Secrets"
  3-1-authenticate-and-enable-the-kv-engine: 3.1 Authenticate and enable the KV engine
  3-2-pingdirectory-devops-credentials: 3.2 PingDirectory DevOps credentials
  3-3-pingdirectory-password-and-license-secrets: 3.3 PingDirectory password and license secrets
  3-4-pingfederate-secrets-not-for-production-use: 3.4 PingFederate secrets (not for production use!)
  devops-vault-spc-step4: "Step 4: Configure Kubernetes Auth in Vault"
  4-1-create-the-namespace-and-serviceaccount: 4.1 Create the namespace and ServiceAccount
  4-2-enable-kubernetes-auth: 4.2 Enable Kubernetes auth
  4-3-write-a-policy-granting-read-access-to-the-ping-secrets: 4.3 Write a policy granting read access to the ping secrets
  4-4-bind-the-policy-to-the-serviceaccount: 4.4 Bind the policy to the ServiceAccount
  devops-vault-spc-step5: "Step 5: PingDirectory Values"
  devops-vault-spc-step6: "Step 6: PingFederate Values"
  devops-vault-spc-step7: "Step 7: Deploy"
  devops-vault-spc-verify: Verify
  verify-the-env-file-is-mounted: Verify the .env file is mounted
  verify-environment-variables-were-sourced: Verify environment variables were sourced
  verify-pingfederate: Verify PingFederate
  devops-vault-spc-alternative: "Alternative: Kubernetes Secret Sync"
  devops-vault-spc-preexisting: "Optional: Using a Pre-Existing SecretProviderClass"
  devops-vault-spc-rotation: Secret Rotation
  before-you-rotate-add-pd_rebuild_on_restart: "Before you rotate: add PD_REBUILD_ON_RESTART"
  step-1-update-the-secret-in-vault: "Step 1: Update the secret in Vault"
  step-2-confirm-the-csi-driver-has-propagated-the-new-value: "Step 2: Confirm the CSI driver has propagated the new value"
  step-3-restart-the-pod: "Step 3: Restart the pod"
  step-4-verify-the-new-password-is-active: "Step 4: Verify the new password is active"
  devops-vault-spc-troubleshooting: Troubleshooting
  pod-stuck-in-containercreating: Pod stuck in ContainerCreating
  vault-authentication-errors: Vault authentication errors
  environment-variables-not-set-after-pod-starts: Environment variables not set after pod starts
  kubernetes-secret-not-created-alternative-path-only: Kubernetes Secret not created (Alternative path only)
  verifying-the-csi-driver-and-vault-provider-daemonsets: Verifying the CSI driver and Vault provider DaemonSets
  devops-vault-spc-cleanup: Clean Up
---

# Using Secrets Store CSI Driver with HashiCorp Vault

This walkthrough deploys PingDirectory and PingFederate using the `ping-devops` Helm chart with all secrets sourced from HashiCorp Vault via the Secrets Store CSI Driver.

|   |                                                                                                                                  |
| - | -------------------------------------------------------------------------------------------------------------------------------- |
|   | In order for this example to work, you must be on the `ping-devops` Helm chart version `0.12.3` or later, released in June 2026. |

|   |                                                                                                                                                                                                                                                                                                                        |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | This walkthrough uses Vault in development mode — in-memory storage, auto-unsealed, single node. Do not use this configuration in production. Production deployments should use Vault HA with TLS and a dedicated namespace. In addition, the credentials shown here are samples and should not be used in production. |

The [Getting Started](../getting-started/getting-started.html) page has instructions on configuring your environment for using Ping `ping-devops` Helm charts.

For more examples, see [Helm Chart Example Configurations](../helm-charts-landing-page.html).

## Overview

The Secrets Store CSI Driver fetches secrets from Vault and makes them available inside pods as mounted files. Ping product containers already know how to consume secrets this way: the `source_secret_envs` hook function sources every `*.env` file found in `SECRETS_DIR` and exports its `KEY=VALUE` pairs as environment variables.

This walkthrough uses that native mechanism as the primary delivery path:

1. Each product's secrets are stored in Vault as a single `content` key containing `KEY=VALUE` pairs.

2. The CSI driver mounts that content as a `product.env` file at a configurable path.

3. Setting `SECRETS_DIR` to the mount path tells the Ping startup hooks where to find the file.

4. No Kubernetes `Secret` objects are created — secret values exist only as files inside the pod.

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The Secrets Store CSI Driver fetches one Vault key per `objectName` entry and writes its value directly to a file. If you store secrets as individual keys in Vault (e.g. `ROOT_USER_PASSWORD`, `PING_IDENTITY_DEVOPS_USER`), the CSI driver fetches each value as a plain string — which is what you want.However, if you attempt to fetch the **entire secret** in one shot without specifying a `secretKey`, the CSI driver writes the raw KV v2 API envelope JSON (`{"data":{"ROOT_USER_PASSWORD":"…​"},"metadata":{…​}}`) to the file. The Ping startup hooks source that file expecting `KEY=VALUE` lines — the JSON envelope is unparseable and credentials are silently ignored.The fix is a storage convention: put all of a product's credentials into a single Vault key named `content` whose value is a `KEY=VALUE` block. The CSI driver then writes that block verbatim to the mounted file, and `source_secret_envs` picks it up natively. |

The `ping-devops` chart integrates with the CSI driver through the `secretProviderClass` values block: set `enabled: true` and the chart auto-wires a CSI volume and mount into every pod spec, and optionally creates the `SecretProviderClass` resource itself.

|   |                                                                                                                                                                                                                                                                                                                                                                                |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | Ping container images default `SECRETS_DIR` to `/run/secrets`, and `/var/run` is a symlink to `/run` inside those images. Mounting a read-only CSI volume at `/run/secrets` conflicts with the Kubernetes ServiceAccount token mount at `/var/run/secrets/kubernetes.io/serviceaccount`. This walkthrough mounts at `/run/vault-secrets` and overrides `SECRETS_DIR` to match. |

## Prerequisites

* `kubectl` configured to a running cluster (Docker Desktop or kind works for this walkthrough)

* `helm` v3

* A `PING_IDENTITY_DEVOPS_USER` and `PING_IDENTITY_DEVOPS_KEY`

## Infrastructure Setup (Steps 1–4)

|   |                                                                                                                                                                                                                                                                                                                                                     |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Steps 1–4 install and configure the Secrets Store CSI Driver, HashiCorp Vault, and the Kubernetes auth plumbing those components require. In a real environment these would already be managed by your platform team. If you have them in place, skip to [Step 5](#devops-vault-spc-step5) where the `ping-devops` Helm chart configuration begins. |

## Step 1: Install the Secrets Store CSI Driver

The CSI driver runs as a DaemonSet on every node.

```shell
helm repo add secrets-store-csi-driver \
  https://kubernetes-sigs.github.io/secrets-store-csi-driver/charts
helm repo update

helm install csi-secrets-store \
  secrets-store-csi-driver/secrets-store-csi-driver \
  --namespace kube-system \
  --set syncSecret.enabled=true \
  --set enableSecretRotation=true
```

Verify the DaemonSet is running:

```shell
kubectl get daemonset -n kube-system \
  -l app.kubernetes.io/instance=csi-secrets-store
```

`DESIRED` and `READY` should match (one pod per schedulable node).

## Step 2: Install Vault with the CSI Provider

The HashiCorp Helm chart installs both the Vault server and the Vault CSI provider DaemonSet in a single release. The injector (sidecar-based secret delivery) is disabled because we are using the CSI path instead.

```shell
helm repo add hashicorp https://helm.releases.hashicorp.com
helm repo update

helm install vault hashicorp/vault \
  --namespace vault \
  --create-namespace \
  --set "server.dev.enabled=true" \
  --set "server.dev.devRootToken=root" \
  --set "csi.enabled=true" \
  --set "injector.enabled=false"
```

Wait for Vault to be ready:

```shell
kubectl wait pod vault-0 \
  -n vault \
  --for=condition=Ready \
  --timeout=120s
```

## Step 3: Seed Vault with Secrets

Open a shell into the Vault pod:

```shell
kubectl exec -it vault-0 -n vault -- /bin/sh
```

The following commands are run **inside** that shell.

### 3.1 Authenticate and enable the KV engine

```shell
export VAULT_TOKEN=root
export VAULT_ADDR=http://127.0.0.1:8200

vault secrets enable -path=ping kv-v2
```

### 3.2 PingDirectory DevOps credentials

DevOps credentials and EULA acceptance are stored as a `content` key sourced by the Ping startup hooks. Replace the placeholder values with your credentials.

```shell
vault kv put ping/pd-env content="PING_IDENTITY_DEVOPS_USER=<username>
PING_IDENTITY_DEVOPS_KEY=<devops_key>
PING_IDENTITY_ACCEPT_EULA=YES"
```

### 3.3 PingDirectory password and license secrets

PingDirectory resolves credentials from files at startup via `*_FILE` environment variables. Store the passwords — and optionally the license file — as individual keys in a separate Vault secret so each can be mounted as its own file.

```shell
vault kv put ping/pdpwd - <<EOF
{
  "admin-user-password": "SecretAdm1nPa55word",
  "encryption-password": "SuperLongEncryptionPassword",
  "root-user-password": "3FederateMuchMore",
  "pd-license": "<base64-encoded-PingDirectory.lic-content>"
}
EOF
```

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | This walkthrough uses `PING_IDENTITY_DEVOPS_USER` and `PING_IDENTITY_DEVOPS_KEY` to obtain a development license from the Ping DevOps license server at startup, so no static license file is required. The `pd-license` key and `PingDirectory.lic` object entry in Step 5 illustrate the pattern for production deployments where a static license file is managed centrally in Vault — replace the placeholder with the base64-encoded content of your `PingDirectory.lic` file. |

### 3.4 PingFederate secrets (not for production use!)

```shell
vault kv put ping/pf-env content="PING_IDENTITY_DEVOPS_USER=<username>
PING_IDENTITY_DEVOPS_KEY=<devops_key>
PING_IDENTITY_ACCEPT_EULA=YES
PING_IDENTITY_PASSWORD=<admin-password>
PF_RUN_PF_CLUSTER_AUTH_PWD=<cluster-auth-password>"
```

|   |                                                                                                                                                                                                                                                                                                                              |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | `PF_RUN_PF_CLUSTER_AUTH_PWD` sets the cluster authentication password shared between the admin and engine nodes. If you rotate this value in Vault, you must restart **both** the admin and engine pods — restarting only the admin leaves the engine using the old cluster password and it will fail to rejoin the cluster. |

Exit the shell:

```shell
exit
```

## Step 4: Configure Kubernetes Auth in Vault

The Vault Kubernetes auth method lets pods authenticate to Vault using the ServiceAccount token Kubernetes automatically mounts into every pod. When a pod requests a secret via the CSI driver, the Vault provider presents that token; Vault validates it against the cluster and, if the token's ServiceAccount matches a configured role, issues a short-lived Vault token scoped to the policy you define.

### 4.1 Create the namespace and ServiceAccount

```shell
kubectl create namespace ping

kubectl create serviceaccount ping-vault-auth -n ping \
  --dry-run=client -o json \
  | jq '.automountServiceAccountToken = false' \
  | kubectl apply -f -
```

Setting `automountServiceAccountToken: false` prevents Kubernetes from mounting the SA token at the default `/var/run/secrets/kubernetes.io/serviceaccount` path. The Vault CSI provider does not use that auto-mounted token — it mounts its own projected token — so disabling automounting removes an unnecessary credential from every pod.

### 4.2 Enable Kubernetes auth

```shell
kubectl exec -it vault-0 -n vault -- vault auth enable kubernetes
```

Configure the auth method using the Vault pod's own cluster credentials:

```shell
kubectl exec -it vault-0 -n vault -- /bin/sh -c '
  vault write auth/kubernetes/config \
    kubernetes_host="https://$KUBERNETES_PORT_443_TCP_ADDR:443" \
    token_reviewer_jwt="$(cat /var/run/secrets/kubernetes.io/serviceaccount/token)" \
    kubernetes_ca_cert=@/var/run/secrets/kubernetes.io/serviceaccount/ca.crt
'
```

### 4.3 Write a policy granting read access to the ping secrets

```shell
kubectl exec -it vault-0 -n vault -- vault policy write ping-policy - <<'EOF'
path "ping/data/pd-env" {
  capabilities = ["read"]
}
path "ping/data/pdpwd" {
  capabilities = ["read"]
}
path "ping/data/pf-env" {
  capabilities = ["read"]
}
EOF
```

### 4.4 Bind the policy to the ServiceAccount

```shell
kubectl exec -it vault-0 -n vault -- vault write auth/kubernetes/role/ping-role \
  bound_service_account_names=ping-vault-auth \
  bound_service_account_namespaces=ping \
  policies=ping-policy \
  ttl=1h
```

Any pod in the `ping` namespace using the `ping-vault-auth` ServiceAccount can now request secrets.

## Step 5: PingDirectory Values

|   |                                                                                                                                                                     |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The next two sections provide snippets from a values file for exploration and discussion. Refer to [Step 7](#devops-vault-spc-step7) for the location of this file. |

The `objects` block requests three files from Vault: the `content` key of `ping/pd-env` (mounted as `pingdirectory.env` and sourced by the Ping startup hooks), the `root-user-password` key from `ping/pdpwd` (mounted as a standalone file), and optionally `PingDirectory.lic` for static-license deployments (see the note in Step 3.3). Setting `SECRETS_DIR` injects the `.env` file's key-value pairs as environment variables; `ROOT_USER_PASSWORD_FILE` tells PingDirectory to read its root password from the mounted file.

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | `ROOT_USER_PASSWORD_FILE` delivers the root password via a mounted file rather than a static environment variable, which is what enables Vault secret rotation to work. However, PingData products (PingDirectory, PingDirectoryProxy, PingDataSync) write credentials into an internal configuration database at first startup and do not re-read them on subsequent restarts unless explicitly told to do so. If you intend to rotate the `root-user-password` secret in Vault, you must also set `PD_REBUILD_ON_RESTART: "true"` in the `envs` block — without it, `manage-profile replace-profile` detects no profile changes and exits without re-applying the rotated password. See the [Secret Rotation](#devops-vault-spc-rotation) section for full details. |

pingdirectory portion of ping-values.yaml

```yaml
pingdirectory:
  enabled: true
  envs:
    SERVER_PROFILE_URL: https://github.com/pingidentity/pingidentity-server-profiles.git
    SERVER_PROFILE_PATH: getting-started/pingdirectory
    SECRETS_DIR: /run/vault-secrets
    ROOT_USER_PASSWORD_FILE: "/run/vault-secrets/root-user-password"
  secretProviderClass:
    enabled: true
    create: true
    provider: vault
    mountPath: /run/vault-secrets
    parameters:
      vaultAddress: http://vault.vault:8200
      roleName: ping-role
      objects: |
        - objectName: "pingdirectory.env"
          secretPath: "ping/data/pd-env"
          secretKey: "content"
        - objectName: "root-user-password"
          secretPath: "ping/data/pdpwd"
          secretKey: "root-user-password"
        - objectName: "PingDirectory.lic"
          secretPath: "ping/data/pdpwd"
          secretKey: "pd-license"
```

## Step 6: PingFederate Values

PingFederate follows the same pattern — one `*.env` file per pod type.

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | The CSI driver propagates updated Vault secrets to the mounted file automatically, but PingFederate does not re-read environment variables from that file while running. A pod restart is required to pick up rotated secrets. Depending on your [operating pattern](https://devops.pingidentity.com/how-to/operatingPatterns/) (Deployment vs. StatefulSet, single node vs. clustered), a rolling restart of the affected pods is typically sufficient. If you rotate `PF_RUN_PF_CLUSTER_AUTH_PWD`, restart **both** admin and engine pods — the cluster auth password must match across all members. |

pingfederate-admin portion of ping-values.yaml

```yaml
pingfederate-admin:
  enabled: true
  envs:
    SERVER_PROFILE_URL: https://github.com/pingidentity/pingidentity-server-profiles.git
    SERVER_PROFILE_PATH: getting-started/pingfederate
    SECRETS_DIR: /run/vault-secrets
  secretProviderClass:
    enabled: true
    create: true
    provider: vault
    mountPath: /run/vault-secrets
    parameters:
      vaultAddress: http://vault.vault:8200
      roleName: ping-role
      objects: |
        - objectName: "pingfederate.env"
          secretPath: "ping/data/pf-env"
          secretKey: "content"
```

pingfederate-engine portion of ping-values.yaml

```yaml
pingfederate-engine:
  enabled: true
  envs:
    SERVER_PROFILE_URL: https://github.com/pingidentity/pingidentity-server-profiles.git
    SERVER_PROFILE_PATH: getting-started/pingfederate
    SECRETS_DIR: /run/vault-secrets
  secretProviderClass:
    enabled: true
    create: true
    provider: vault
    mountPath: /run/vault-secrets
    parameters:
      vaultAddress: http://vault.vault:8200
      roleName: ping-role
      objects: |
        - objectName: "pingfederate.env"
          secretPath: "ping/data/pf-env"
          secretKey: "content"
```

## Step 7: Deploy

The complete values file combining Steps 5 and 6 is in the [getting-started repository](https://github.com/pingidentity/pingidentity-devops-getting-started) at `30-helm/vault-spc/ping-values.yaml`. Clone it if you haven't already, then deploy.

The `global.rbac` block tells the chart to assign the `ping-vault-auth` ServiceAccount — which is bound to the Vault role — to every workload pod. Without this, pods authenticate with the `default` ServiceAccount, which is not authorized in Vault.

```shell
git clone https://github.com/pingidentity/pingidentity-devops-getting-started.git
cd pingidentity-devops-getting-started

helm install ping pingidentity/ping-devops \
  -n ping \
  --set global.rbac.serviceAccountName=ping-vault-auth \
  --set global.rbac.applyServiceAccountToWorkload=true \
  -f 30-helm/vault-spc/ping-values.yaml
```

Watch the pods reach `Running`:

```shell
kubectl get pods -n ping -w
```

## Verify

### Verify the .env file is mounted

Confirm the CSI driver wrote the secret file into the pod:

```shell
kubectl exec -n ping \
  $(kubectl get pod -n ping -l app.kubernetes.io/name=pingdirectory -o name | head -1) \
  -- ls /run/vault-secrets
```

Expected:

```
PingDirectory.lic
pingdirectory.env
root-user-password
```

### Verify environment variables were sourced

Confirm `ROOT_USER_PASSWORD_FILE` is set and the `.env` file was consumed at startup:

```shell
kubectl exec -n ping \
  $(kubectl get pod -n ping -l app.kubernetes.io/name=pingdirectory -o name | head -1) \
  -- env | grep ROOT_USER_PASSWORD_FILE
```

Expected:

```
ROOT_USER_PASSWORD_FILE=/run/vault-secrets/root-user-password
```

|   |                                                                                                                                                                                                                                                                                    |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | `PING_IDENTITY_DEVOPS_USER` and `PING_IDENTITY_DEVOPS_KEY` are read from the mounted `.env` file at startup to obtain the development license, but are not exported into the container's environment. If the server started successfully, the credentials were consumed correctly. |

Confirm the password file itself is present:

```shell
kubectl exec -n ping \
  $(kubectl get pod -n ping -l app.kubernetes.io/name=pingdirectory -o name | head -1) \
  -- cat /run/vault-secrets/root-user-password
```

### Verify PingFederate

```shell
kubectl exec -n ping \
  $(kubectl get pod -n ping -l app.kubernetes.io/name=pingfederate-admin -o name | head -1) \
  -- env | grep -E 'PING_IDENTITY_PASSWORD|PING_IDENTITY_DEVOPS_USER'
```

## Alternative: Kubernetes Secret Sync

If you cannot set `SECRETS_DIR` on the container — for example when a platform team manages the deployment spec — you can use the Kubernetes Secret sync mechanism instead. The `secretObjects` block instructs the CSI driver to create a Kubernetes `Secret` from the mounted files; `container.envFrom` then injects that Secret's keys as environment variables.

This approach requires one `objectName` entry per secret key (rather than one per product) and creates Kubernetes `Secret` objects in the cluster.

|   |                                                                                                                                                                           |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The Kubernetes `Secret` created by `secretObjects` is only created after the first pod successfully mounts the CSI volume. It does not exist before the first pod starts. |

For this path, seed Vault with individual per-key secrets instead of the `content` key format used in Step 3. You will also need to update the Vault policy in Step 4.3 to cover these paths:

```shell
vault kv put ping/devops \
  PING_IDENTITY_DEVOPS_USER="<username>" \
  PING_IDENTITY_DEVOPS_KEY="<devops_key>" \
  PING_IDENTITY_ACCEPT_EULA="YES"

vault kv put ping/pingdirectory \
  ROOT_USER_PASSWORD="3FederateMuchMore" \
  ROOT_USER_DN="cn=administrator"

vault kv put ping/pingfederate \
  PING_IDENTITY_PASSWORD="<admin-password>"
```

The values configuration for PingDirectory then becomes:

pingdirectory with secretObjects/envFrom

```yaml
pingdirectory:
  enabled: true
  envs:
    SERVER_PROFILE_URL: https://github.com/pingidentity/pingidentity-server-profiles.git
    SERVER_PROFILE_PATH: getting-started/pingdirectory
  secretProviderClass:
    enabled: true
    create: true
    provider: vault
    mountPath: /run/vault-secrets
    parameters:
      vaultAddress: http://vault.vault:8200
      roleName: ping-role
      objects: |
        - objectName: "PING_IDENTITY_DEVOPS_USER"
          secretPath: "ping/data/devops"
          secretKey: "PING_IDENTITY_DEVOPS_USER"
        - objectName: "PING_IDENTITY_DEVOPS_KEY"
          secretPath: "ping/data/devops"
          secretKey: "PING_IDENTITY_DEVOPS_KEY"
        - objectName: "PING_IDENTITY_ACCEPT_EULA"
          secretPath: "ping/data/devops"
          secretKey: "PING_IDENTITY_ACCEPT_EULA"
        - objectName: "ROOT_USER_PASSWORD"
          secretPath: "ping/data/pingdirectory"
          secretKey: "ROOT_USER_PASSWORD"
        - objectName: "ROOT_USER_DN"
          secretPath: "ping/data/pingdirectory"
          secretKey: "ROOT_USER_DN"
    secretObjects:
      - secretName: ping-pd-env
        type: Opaque
        data:
          - objectName: PING_IDENTITY_DEVOPS_USER
            key: PING_IDENTITY_DEVOPS_USER
          - objectName: PING_IDENTITY_DEVOPS_KEY
            key: PING_IDENTITY_DEVOPS_KEY
          - objectName: PING_IDENTITY_ACCEPT_EULA
            key: PING_IDENTITY_ACCEPT_EULA
          - objectName: ROOT_USER_PASSWORD
            key: ROOT_USER_PASSWORD
          - objectName: ROOT_USER_DN
            key: ROOT_USER_DN
  container:
    envFrom:
      - secretRef:
          name: ping-pd-env
```

## Optional: Using a Pre-Existing SecretProviderClass

If your platform team manages `SecretProviderClass` resources centrally, set `create: false` and provide the name. The chart will wire up the CSI volume pointing at that resource without attempting to create or own it. For example:

```yaml
pingdirectory:
  secretProviderClass:
    enabled: true
    create: false
    name: platform-team-pd-spc
```

## Secret Rotation

This section walks through rotating the PingDirectory root user password end-to-end: updating it in Vault, confirming the CSI driver propagates it to the pod, and restarting the pod so the product picks it up.

### Before you rotate: add `PD_REBUILD_ON_RESTART`

PingData products (PingDirectory, PingDirectoryProxy, PingDataSync) write credentials into an internal configuration database at first startup. On subsequent restarts, `manage-profile replace-profile` checks whether the server profile has changed. Secret files delivered via `*_FILE` environment variables are not tracked in the profile manifest, so `replace-profile` detects "no changes" and exits without re-applying credentials — even though the mounted file now contains the rotated value. The pod starts successfully using the old internally-stored password; the rotation silently fails.

Setting `PD_REBUILD_ON_RESTART: "true"` forces `replace-profile` to run in full replace mode, re-applying all credentials from the mounted files on every restart.

Add this to the `pingdirectory` `envs` block before rotating any credential:

```yaml
pingdirectory:
  envs:
    PD_REBUILD_ON_RESTART: "true"
```

Then apply it:

```shell
helm upgrade ping pingidentity/ping-devops \
  -n ping \
  --reuse-values \
  --set-string pingdirectory.envs.PD_REBUILD_ON_RESTART=true
```

|   |                                                                                                                                                                                                                                                                                                                                                                                              |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Use `--set-string` rather than `--set` for this value. `--set` without a type hint sends `true` as a boolean, which Kubernetes rejects when writing it to a ConfigMap string field. `--set-string` forces the value to a string. If you prefer to manage this in your values file, `PD_REBUILD_ON_RESTART: "true"` in YAML is equivalent — the YAML quotes are syntax, not value characters. |

### Step 1: Update the secret in Vault

```shell
kubectl exec -it vault-0 -n vault -- /bin/sh -c '
  export VAULT_TOKEN=root
  export VAULT_ADDR=http://127.0.0.1:8200
  vault kv patch ping/pdpwd root-user-password="R0tatedNewPa55word!"
'
```

### Step 2: Confirm the CSI driver has propagated the new value

The CSI driver polls Vault on a rotation interval (default: two minutes). Wait for the mounted file to update before restarting the pod:

```shell
kubectl exec -n ping \
  $(kubectl get pod -n ping -l app.kubernetes.io/name=pingdirectory -o name | head -1) \
  -- cat /run/vault-secrets/root-user-password
```

Repeat until the output shows the new password.

### Step 3: Restart the pod

Delete the pod so the StatefulSet recreates it, picking up the rotated secret and running `replace-profile` with `--replaceFullProfile`:

```shell
kubectl delete pod \
  $(kubectl get pod -n ping -l app.kubernetes.io/name=pingdirectory -o name | head -1 | sed 's|pod/||') \
  -n ping
```

|   |                                                                                                                                                                                                                                                                                                                |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | In this single-pod walkthrough, deleting the pod is safe — the StatefulSet recreates it immediately. In a production deployment with multiple replicas, rotate one pod at a time: delete it, wait for `1/1 Running`, then proceed to the next. Deleting all pods simultaneously risks replication quorum loss. |

Watch it return to `Running`:

```shell
kubectl get pods -n ping -w
```

### Step 4: Verify the new password is active

```shell
kubectl exec -n ping \
  $(kubectl get pod -n ping -l app.kubernetes.io/name=pingdirectory -o name | head -1) \
  -- ldapsearch --useSSL --trustAll -h localhost -p 1636 \
  -D "cn=administrator" -w "R0tatedNewPa55word!" \
  -b "" -s base "(objectClass=*)" namingContexts
```

A `Result Code: 0 (success)` response confirms the rotated password is active.

|   |                                                                                                                                                                                                   |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | A rotated `PingDirectory.lic` written to the mount point has no effect until the pod restarts and re-runs the Profile stage. The same `PD_REBUILD_ON_RESTART` flag and restart procedure applies. |

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Environment variables injected via `envFrom` are set at container startup from the synced Kubernetes `Secret` and are not re-read at runtime. A Vault secret rotation updates the mounted file and the Kubernetes `Secret`, but the running container's environment does not change until the pod is restarted. Unlike the primary path, there is no `PD_REBUILD_ON_RESTART` equivalent — a restart is always required and is sufficient. |

## Troubleshooting

### Pod stuck in `ContainerCreating`

```shell
kubectl describe pod <pod-name> -n ping
```

Common events and their causes:

* `failed to get secretproviderclass ping/…​-spc` — the `SecretProviderClass` resource does not exist or is in the wrong namespace. Check `kubectl get secretproviderclass -n ping`.

* `failed to mount secrets store objects` — the Vault provider could not authenticate. The most common cause is a mismatch between the pod's ServiceAccount name or namespace and the Vault role's `bound_service_account_names` / `bound_service_account_namespaces`. Verify the pod is using the correct ServiceAccount with `kubectl get pod <pod-name> -n ping -o jsonpath='{.spec.serviceAccountName}'` and confirm the Vault role with `kubectl exec -it vault-0 -n vault — vault read auth/kubernetes/role/ping-role`.

* `secrets-store.csi.x-k8s.io/v1 is not available in Capabilities.APIVersions` — the CSI driver CRDs are not installed. Re-run [Step 1](#devops-vault-spc-step1).

* `make mountpoint …​ read-only file system` on the SA token path — the CSI mountPath conflicts with the Kubernetes ServiceAccount token path. Set `mountPath: /run/vault-secrets` in the `secretProviderClass` block.

### Vault authentication errors

```shell
kubectl logs -n vault -l app.kubernetes.io/name=vault-csi-provider
```

Verify the role binding matches the pod's ServiceAccount:

```shell
kubectl exec -it vault-0 -n vault -- vault read auth/kubernetes/role/ping-role
```

### Environment variables not set after pod starts

If the pod reaches `Running` but expected env vars are missing, confirm the startup hooks found the `.env` file:

```shell
kubectl logs <pod-name> -n ping | grep -E "SECRETS_DIR|\.env"
```

The log should show `SECRETS_DIR : /run/vault-secrets`. If it shows the default `/run/secrets` instead, the `envs.SECRETS_DIR` override was not applied — check the values file.

### Kubernetes Secret not created (Alternative path only)

The synced Secret (`secretObjects`) is only created after the first pod successfully mounts the CSI volume. If the pod never reaches `Running`, the Secret will not exist. Fix the pod startup issue first, then check:

```shell
kubectl get secret -n ping
```

### Verifying the CSI driver and Vault provider DaemonSets

```shell
kubectl get daemonset -n kube-system -l app.kubernetes.io/instance=csi-secrets-store
kubectl get daemonset -n vault -l app.kubernetes.io/instance=vault
```

Both should show one pod per schedulable node.

## Clean Up

```shell
helm uninstall ping -n ping
kubectl delete namespace ping

helm uninstall vault -n vault
kubectl delete namespace vault

helm uninstall csi-secrets-store -n kube-system
```