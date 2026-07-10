---
title: Ingress issues
description: If the pods in a ForgeOps deployment are starting successfully, but you can't reach the services in those pods, you probably have ingress issues.
component: forgeops
version: 2026.2
page_id: forgeops:troubleshoot:ingress
canonical_url: https://docs.pingidentity.com/forgeops/2026.2/troubleshoot/ingress.html
llms_txt: https://docs.pingidentity.com/forgeops/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Troubleshooting", "Kubernetes", "Ingress Controller"]
---

# Ingress issues

If the pods in a ForgeOps deployment are starting successfully, but you can't reach the services in those pods, you probably have ingress issues.

To diagnose ingress issues:

1. Use the `kubectl describe ing` and `kubectl get ing ingress-name -o yaml` commands to view the ingress object.

2. Describe the service using the `kubectl get svc; kubectl describe svc xxx` command. Does the service have an `Endpoint:` binding? If the service endpoint binding is not present, the service did not match any running pods.

---

---
title: Kubernetes logs and other diagnostics
description: Look at pod descriptions and container log files for irregularities that indicate problems.
component: forgeops
version: 2026.2
page_id: forgeops:troubleshoot:pods
canonical_url: https://docs.pingidentity.com/forgeops/2026.2/troubleshoot/pods.html
llms_txt: https://docs.pingidentity.com/forgeops/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Troubleshooting", "Kubernetes", "Logs"]
section_ids:
  debug_logs_utility: debug-logs utility
  example_troubleshooting_steps: Example troubleshooting steps
---

# Kubernetes logs and other diagnostics

Look at pod descriptions and container log files for irregularities that indicate problems.

*Pods Information* contains details about active Kubernetes pods, including their configuration, status, containers (including containers that have finished running), volume mounts, and pod-related events.

*Container logs* contain startup and run-time messages that might indicate problem areas. Each Kubernetes container has its own log that contains all output written to `stdout` by the application running in the container. The `am` container logs are especially important for troubleshooting AM issues in Kubernetes deployments. AM writes its debug logs to `stdout`. Therefore, the `am` container logs include all the AM debug logs.

## debug-logs utility

The debug-logs utility generates the following HTML-formatted output, which you can view in a browser:

* Descriptions of all the Kubernetes pods running in your namespace

* Logs for all the containers running in these pods

* Descriptions of the PVCs running in your cluster

* Operator logs

* Information about your local environment, including:

  * ForgeOps release version

  * Deployment method (Helm or Kustomize)

  * Third-party software versions

  * The custom resource definitions (CRDs) installed in your cluster

  * Kubernetes storage classes

  * The most recent commits in your forgeops repository clone's commit log

  * Deployment environment in the `env.log` file

  * Details about a variety of Kubernetes objects on your cluster

## Example troubleshooting steps

Suppose you performed a ForgeOps deployment but noticed that one of the pods had an `ImagePullBackOff` error at startup. Here's an example of how you can use pod descriptions and container logs to troubleshoot the problem:

1. Make sure the active namespace in your local Kubernetes context is the one that contains the component you are debugging.

2. Make sure you've checked out the 2026.2.1 branch of the `forgeops` repository.

3. Change to the /path/to/forgeops/bin directory in your `forgeops` repository clone.

4. Run the debug-logs command appropriate to the method you used for deployment:

   1. For Helm-based deployments:

      ```
      $ ./debug-logs --helm --env-name my-env
      Writing environment information
      Writing pod descriptions and container logs
       ...
      Writing information about various Kubernetes objects
      Open /tmp/forgeops/log.html in your browser.
      ```

   2. For Kustomize-based deployments:

      ```
      $ ./debug-logs --kustomize --env-name my-env
      Writing environment information
      Writing pod descriptions and container logs
       ...
      Writing information about various Kubernetes objects
      Open /tmp/forgeops/log.html in your browser.
      ```

5. In a browser, go to the URL shown in the debug-logs output. In this example, the URL is file:///tmp/forgeops/log.html. The browser displays a screen with a link for each Ping Advanced Identity Software pod in your namespace:

   ![Screen shot of debug-logs output.](_images/debug-logs.png)

6. Access the information for the pod that didn't start correctly by selecting its link from the Pod Descriptions and Container Logs section of the debug-logs output.

   Selecting the link takes you to the pod's description. Logs for each of the pod's containers follow the pod's description.

After you've obtained the pod descriptions and container logs, here are some actions you might take:

* Examine each pod's event log for failures.

* If a Docker image could not be pulled, verify that the Docker image name and tag are correct. If you are using a private registry, verify that your image pull secret is correct.

* Examine the init containers. Did each init container complete with a zero (success) exit code? If not, examine the logs from that failed init container using the `kubectl logs pod-xxx -c init-container-name` command.

* Look at the logs from pods to check if the main container entered a crash loop.

---

---
title: minikube hardware resources
description: The minikube start command example in minikube provides a good default virtual hardware configuration for a minikube cluster running a single-instance ForgeOps deployment.
component: forgeops
version: 2026.2
page_id: forgeops:troubleshoot:minikube
canonical_url: https://docs.pingidentity.com/forgeops/2026.2/troubleshoot/minikube.html
llms_txt: https://docs.pingidentity.com/forgeops/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Troubleshooting", "minikube"]
section_ids:
  cluster_configuration: Cluster configuration
  disk_space: Disk space
---

# minikube hardware resources

## Cluster configuration

The minikube start command example in [minikube](../setup/minikube.html) provides a good default virtual hardware configuration for a minikube cluster running a single-instance ForgeOps deployment.

## Disk space

When the minikube cluster runs low on disk space, it acts unpredictably. Unexpected application errors can appear.

Verify that adequate disk space is available by logging in to the minikube cluster and running a command to display free disk space:

```
$ minikube ssh
$ df -h
Filesystem      Size  Used Avail Use% Mounted on
devtmpfs        3.9G     0  3.9G   0% /dev
tmpfs           3.9G     0  3.9G   0% /dev/shm
tmpfs           3.9G  383M  3.6G  10% /run
tmpfs           3.9G     0  3.9G   0% /sys/fs/cgroup
tmpfs           3.9G   64K  3.9G   1% /tmp
/dev/sda1        25G  7.7G   16G  33% /mnt/sda1
/Users          465G  219G  247G  48% /Users
$ exit
logout
```

In the preceding example, 16 GB of disk space is available on the minikube cluster.

---

---
title: Staged installation
description: By default, the forgeops apply command installs the entire Ping Advanced Identity Software.
component: forgeops
version: 2026.2
page_id: forgeops:troubleshoot:staged-deployment
canonical_url: https://docs.pingidentity.com/forgeops/2026.2/troubleshoot/staged-deployment.html
llms_txt: https://docs.pingidentity.com/forgeops/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Troubleshooting", "forgeops Command"]
section_ids:
  multiple_component_installation: Multiple component installation
---

# Staged installation

By default, the forgeops apply command installs the entire Ping Advanced Identity Software.

You can also install the platform in stages to help troubleshoot deployment issues.

To install the platform in stages:

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

     Learn more about deployment sizes in [Cluster and deployment sizes](../deploy/architecture.html#cluster-and-deployment-sizes) and about single instances [here](../deploy/architecture.html#single-inst).

5. Install the `base` and `ds` components first. Other components have dependencies on these two components:

   1. Install the platform `base` component:

      ```
      $ cd /path/to/forgeops/bin
      $ ./forgeops apply base --env-name my-env
      ...
      configmap/platform-config created
      Warning: spec.privateKey.rotationPolicy: In cert-manager >= v1.18.0, the default value changed from Never to Always.
      certificate.cert-manager.io/ds-master-cert created
      certificate.cert-manager.io/ds-ssl-cert created
      issuer.cert-manager.io/selfsigned-issuer created
      secretagentconfiguration.secret-agent.secrets.forgerock.io/forgerock-sac created
      Waiting for secrets to be ready.
      ...
      Relevant passwords:
      ...

      Relevant URLs:
      ...
      ```

   2. After you've installed the `base` component, install the `ds` component:

      ```
      $ ./forgeops apply ds --env-name my-env
      service/ds-cts created
      statefulset.apps/ds-cts created
      service/ds-idrepo created
      statefulset.apps/ds-idrepo created
      configmap/ds-set-passwords-scripts created
      job.batch/ds-set-passwords created
      ```

6. Install the other Ping Advanced Identity Software components. You can either install all the other components by using the forgeops apply apps command, or install them separately:

   1. Install AM:

      ```
      $ ./forgeops apply am --env-name my-env

      configmap/am-entrypoint created
      configmap/am-import-pem-certs created
      configmap/am-logback created
      service/am created
      deployment.apps/am created
      ingress.networking.k8s.io/am created
      Targeting namespace: my-ns
      ```

   2. Install Amster:

      ```
      $ ./forgeops apply amster --env-name my-env
      job.batch/amster created
      ```

   3. Install IDM:

      ```
      $ ./forgeops apply idm --env-name my-env
      configmap/idm created
      configmap/idm-import-pem-certs created
      configmap/idm-logback-xml created
      configmap/idm-logging-properties created
      service/idm created
      deployment.apps/idm created
      ingress.networking.k8s.io/idm created
      ```

7. Install the user interface components. You can either install all the applications by using the forgeops apply ui command, or install them separately:

   1. Install the administration UI:

      ```
      $ ./forgeops apply admin-ui --env-name my-env
      name my-env
      service/admin-ui created
      deployment.apps/admin-ui created
      ingress.networking.k8s.io/admin-ui created
      ```

   2. Install the login UI:

      ```
      $ ./forgeops apply login-ui --env-name my-env
      service/login-ui created
      deployment.apps/login-ui created
      ingress.networking.k8s.io/login-ui created
      ```

   3. Install the end user UI:

      ```
      $ ./forgeops apply end-user-ui --env-name my-env
      name my-env
      service/end-user-ui created
      deployment.apps/end-user-ui created
      ingress.networking.k8s.io/end-user-ui created
      ```

8. In a separate terminal tab or window, run the kubectl get pods command to monitor status of the deployment. Wait until all the pods are ready.

## Multiple component installation

You can specify multiple components with a single forgeops apply command. For example, to install the `base`, `ds`, `am`, and `amster` components in a ForgeOps deployment:

```
$ ./forgeops apply base ds am amster --env-name my-env
```

---

---
title: Third-party software versions
description: The ForgeOps team recommends installing tested versions of third-party software in environments where you'll run ForgeOps deployments.
component: forgeops
version: 2026.2
page_id: forgeops:troubleshoot:sw-versions
canonical_url: https://docs.pingidentity.com/forgeops/2026.2/troubleshoot/sw-versions.html
llms_txt: https://docs.pingidentity.com/forgeops/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
---

# Third-party software versions

The ForgeOps team recommends installing tested versions of third-party software in environments where you'll run ForgeOps deployments.

Refer to the tables that list the tested versions of third-party software for your deployment:

* [On minikube](../setup/minikube.html#minikube-third-party-software)

* [On GKE](../setup/google-cloud.html#gcp-third-party-software)

* [On EKS](../setup/aws.html#aws-third-party-software)

* [On AKS](../setup/azure.html#azure-third-party-software)

You can use the debug-logs utility to get the versions of third-party software installed in your local environment. After you've performed a ForgeOps deployment:

1. Run the /path/to/forgeops/bin/debug-logs utility.

2. Open the log file in your browser.

3. Select Environment Information > Third-party software versions.

---

---
title: Troubleshooting
description: Kubernetes deployments are multi-layered and often complex.
component: forgeops
version: 2026.2
page_id: forgeops:troubleshoot:overview
canonical_url: https://docs.pingidentity.com/forgeops/2026.2/troubleshoot/overview.html
llms_txt: https://docs.pingidentity.com/forgeops/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
---

# Troubleshooting

Kubernetes deployments are multi-layered and often complex.

Errors and misconfigurations can crop up in a variety of places. Performing a logical, systematic search for the source of a problem can be daunting.

Before you troubleshoot, verify your ForgeOps version:

```
$ cd /path/to/forgeops
$ ./bin/forgeops version
```

Here are some techniques you can use to troubleshoot problems with ForgeOps deployments:

| Problem                                                                                 | Troubleshooting Technique                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| --------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Some pods don't start.                                                                  | Review [Kubernetes logs and other diagnostics](pods.html). Verify if your cluster is resource-constrained. Check for under-configured clusters by using the `kubectl describe nodes` and `kubectl get events -w` commands. Pods terminated with out of memory (OOM) errors indicate that your cluster is under-configured. Make sure that you're using [tested versions of third-party software](sw-versions.html). [Stage your installation](staged-deployment.html). Install Ping Advanced Identity Software components separately, instead of installing all the components with a single command. Staging your installation lets you make sure each component works correctly before installing the next component. |
| All the pods have started, but you can't reach the services running in them.            | Make sure you don't have any [ingress issues](ingress.html).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| AM doesn't work as expected.                                                            | [Set the AM logging level](https://community.forgerock.com/t/how-to-enable-and-modify-logging-level-in-forgeops-for-am.html), recreate the issue, and analyze the AM log files. [Turn on audit logging in AM.](https://community.forgerock.com/t/how-to-enable-and-modify-audit-logging-in-am-and-idm-for-forgeops.html)                                                                                                                                                                                                                                                                                                                                                                                                |
| IDM doesn't work as expected.                                                           | [Set the IDM logging level](https://community.forgerock.com/t/how-to-enable-and-modify-logging-level-in-forgeops-for-idm.html), recreate the issue, and analyze the IDM log files. [Turn on audit logging in IDM.](https://community.forgerock.com/t/how-to-enable-and-modify-audit-logging-in-am-and-idm-for-forgeops.html)                                                                                                                                                                                                                                                                                                                                                                                            |
| Your JVM crashed with an out of memory error, or you suspect that you've a memory leak. | [Collect and analyze Java thread dumps and heap dumps](https://support.pingidentity.com/s/article/How-do-I-collect-Java-thread-dumps-and-heap-dumps-for-troubleshooting-a-ForgeOps-deployment).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Changes you've made to ForgeOps's Kustomize files don't work as expected.               | [Fully expand the Kustomize output](kustomize.html), and then examine the output for unintended effects.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| Your minikube deployment doesn't work.                                                  | Make sure that you don't have a problem with [virtual hardware requirements](minikube.html).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| You're having name resolution or other DNS issues.                                      | Use diagnostic tools in the [debug tools container](debug-tools.html#debug-tools-container).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| You want to run DS utilities without disturbing a DS pod.                               | Use the [bin/ds-debug.sh script](debug-tools.html#ds-debug) or DS tools in the [debug tools container](debug-tools.html#debug-tools-container).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| You want to keep the `amster` pod running to diagnose AM configuration issues.          | Use the [forgeops amster command](amster.html).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| The `kubectl` command requires too much typing.                                         | Enable [kubectl tab autocompletion](tab-completion.html).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |

---

---
title: Troubleshooting the <code>amster</code> pod
description: When ForgeOps deployments start, the amster pod starts and imports AM dynamic configuration. Once dynamic configuration is imported, the amster pod is stopped and remains in Completed status.
component: forgeops
version: 2026.2
page_id: forgeops:troubleshoot:amster
canonical_url: https://docs.pingidentity.com/forgeops/2026.2/troubleshoot/amster.html
llms_txt: https://docs.pingidentity.com/forgeops/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Troubleshooting", "Kubernetes", "Amster"]
section_ids:
  start_the_amster_pod: Start the amster pod
  amster-retain: Export and import AM configuration
---

# Troubleshooting the `amster` pod

When ForgeOps deployments start, the `amster` pod starts and imports AM dynamic configuration. Once dynamic configuration is imported, the `amster` pod is stopped and remains in `Completed` status.

```
$ kubectl get pods
NAME                          READY   STATUS      RESTARTS   AGE
admin-ui-b977c857c-2m9pq      1/1     Running     0          10m
am-666687d69c-94thr           1/1     Running     0          12m
amster-4prdg                  0/1     Completed   0          12m
ds-idrepo-0                   1/1     Running     0          13m
end-user-ui-674c4f79c-h4wgb   1/1     Running     0          10m
idm-869679958c-brb2k          1/1     Running     0          12m
login-ui-56dd46c579-gxrtx     1/1     Running     0          10m
```

## Start the `amster` pod

After you install AM, use the forgeops amster run command to start the `amster` pod for manually interacting with AM using the forgeops amster run command-line interface and perform tasks such as exporting and importing AM configuration and troubleshooting:

```
$ ./bin/forgeops amster run --env-name my-env
starting...
...

$ kubectl get pods
NAME                          READY   STATUS    RESTARTS   AGE
admin-ui-b977c857c-2m9pq      1/1     Running   0          22m
am-666687d69c-94thr           1/1     Running   0          24m
amster-852fj                  1/1     Running   0          12s
ds-idrepo-0                   1/1     Running   0          25m
end-user-ui-674c4f79c-h4wgb   1/1     Running   0          22m
idm-869679958c-brb2k          1/1     Running   0          24m
login-ui-56dd46c579-gxrtx     1/1     Running   0          22m
```

The amster jobs have a default time-to-live (TTL) value set to 600 seconds. The amster jobs are removed from the namespace after 10 minutes to allow later runs of amster jobs if the spec is updated in the user's environment and redeployed.

A Kubernetes job cannot be updated after it has started running. If the amster job is running when you apply an update, then an error is thrown. The beginning of the error appears similar to the following:

```
The Job "amster" is invalid: spec.template: Invalid value: ...
...
"batch.kubernetes.io/job-name":"amster", ...
"job-name":"amster"}
```

If an `amster` job fails due to low TTL, then delete `amster` jobs using the kubectl delete jobs command and redeploy.

## Export and import AM configuration

To export AM configuration, use the forgeops amster export command. Similarly, use the forgeops amster import command to import AM configuration. At the end of the export or import session, the `amster` pod is stopped by default. To keep the `amster` pod running, use the --retain option. You can specify the time (in seconds) to keep the `amster` running.

In the following example, the `amster` pod is kept running for 900 seconds after completing export:

```
$ ./bin/forgeops amster export --env-name my-env --retain 900 /tmp/myexports
Cleaning up amster components
job.batch "amster" deleted
configmap "amster-files" deleted
Packing and uploading configs
configmap/amster-files created
configmap/amster-export-type created
Deploying amster
job.batch/amster created

Waiting for amster job to complete. This can take several minutes.
pod/amster-d6vsv condition met
tar: Removing leading `/' from member names
Updating amster config.
Updating amster config complete.
```

```
$ kubectl get pods
NAME                          READY   STATUS    RESTARTS   AGE
admin-ui-b977c857c-2m9pq      1/1     Running   0          27m
am-666687d69c-94thr           1/1     Running   0          29m
amster-d6vsv                  1/1     Running   0          53s
ds-idrepo-0                   1/1     Running   0          30m
end-user-ui-674c4f79c-h4wgb   1/1     Running   0          27m
idm-869679958c-brb2k          1/1     Running   0          29m
login-ui-56dd46c579-gxrtx     1/1     Running   0          27m
```

After 900 seconds notice that the `amster` pod is in `Completed` status:

```
$ kubectl get pods
NAME                          READY   STATUS      RESTARTS   AGE
admin-ui-b977c857c-2m9pq      1/1     Running     0          78m
am-666687d69c-94thr           1/1     Running     0          80m
amster-d6vsv                  0/1     Completed   0          51m
ds-idrepo-0                   1/1     Running     0          81m
end-user-ui-674c4f79c-h4wgb   1/1     Running     0          78m
idm-869679958c-brb2k          1/1     Running     0          80m
login-ui-56dd46c579-gxrtx     1/1     Running     0          78m
```

Similarly, use the `--retain` option with the forgeops amster import command to keep the `amster` job running to completion.