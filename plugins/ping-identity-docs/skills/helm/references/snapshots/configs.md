---
title: Container Configuration
description: Kubernetes Workload Controller resources are created depending on configuration values:
component: helm
page_id: helm::configs/container
canonical_url: https://developer.pingidentity.com/helm/configs/container.html
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
