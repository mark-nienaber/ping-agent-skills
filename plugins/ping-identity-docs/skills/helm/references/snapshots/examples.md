---
title: Enhanced Utility Sidecar Examples
description: This page demonstrates the utilitySidecar enhancements added to the Ping Identity Helm charts starting in version 0.12.1. Use these examples as a starting point when you want to keep sidecar-based operational tasks, such as backup, restore, support collection, or lightweight tooling, separate from the main product container.
component: helm
page_id: helm::examples/enhanced-sidecar
canonical_url: https://developer.pingidentity.com/helm/examples/enhanced-sidecar.html
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
