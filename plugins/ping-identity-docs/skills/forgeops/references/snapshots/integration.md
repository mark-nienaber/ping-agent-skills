---
title: Integrate ForgeOps with the PingOne Worker service
description: Integrate ForgeOps with the PingOne Worker service to use PingOne Protect in authentication journeys on a ForgeOps deployment
component: forgeops
version: 2026.3
page_id: forgeops:integration:int-p1-worker
canonical_url: https://docs.pingidentity.com/forgeops/2026.3/integration/int-p1-worker.html
llms_txt: https://docs.pingidentity.com/forgeops/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-08-12T20:30:59Z
section_ids:
  why_integrate_with_the_pingone_worker_service: Why integrate with the PingOne Worker service?
  set_up_a_pingone_environment: Set up a PingOne environment
  set_up_forgeops_on_minikube: Set up ForgeOps on minikube
  export_am_runtime_config_into_a_profile_and_redeploy: Export AM runtime config into a profile and redeploy
  test_the_integration: Test the integration
---

# Integrate ForgeOps with the PingOne Worker service

## Why integrate with the PingOne Worker service?

Integrating ForgeOps with the PingOne Worker Service allows a ForgeOps deployment to extend platform capabilities through PingOne Universal Services such as PingOne Protect, PingOne Verify, and others. The PingOne Worker service provides the integration point between ForgeOps and these PingOne services using secrets and configuration.

For example, when integrated with PingOne Protect through the PingOne Worker Service, journeys can use real-time risk scores to make smarter authentication decisions. PingOne Protect evaluates signals such as device, network, and user behavior to produce a risk score for each sign-on event. Journeys can then use that score to adapt authentication journeys dynamically, such as allowing access for low-risk events, prompting step-up authentication for medium-risk events, or denying access for high-risk events.

This guide provides sample instructions for setting up the integration in a ForgeOps deployment running on minikube. You can adapt the instructions for your environment and the PingOne services you want to use.

## Set up a PingOne environment

Use the steps in the PingOne documentation to set up a PingOne environment and a PingOne Worker application.

1. Create a PingOne Workforce solution environment as described in [Create a PingOne environment](https://docs.pingidentity.com/pingone/getting_started_with_pingone/p1_getting_started_adding_environment.html).

2. Create a PingOne Worker application as described in [Create a PingOne Worker application](https://docs.pingidentity.com/pingam/8.1/integrations/connect-am-to-PingOne.html#create-worker-application).

3. Enable the PingOne Worker application by using the `Enable` switch in the upper-right corner of the application overview tab.

4. Note the following data from the PingOne Worker application overview tab:

   * Environment ID:

   * Client ID:

   * Client Secret:

## Set up ForgeOps on minikube

|   |                                                                                                                                                                                         |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | 1. Ensure that the window running the minikube tunnel remains open as long as you run the ForgeOps deployment.

2. All forgeops commands must be run in the Python virtual environment. |

1. Use the steps in the [Quick deployment on minikube](../quick/quick-set-mini.html) to set up a ForgeOps deployment on minikube. Use the local Helm chart to deploy ForgeOps in step 7 of the [Perform ForgeOps deployment](../quick/quick-set-mini.html#perform-forgeops-deployment) section:

   ```
   helm upgrade --install identity-platform ./charts/identity-platform  \
   --namespace my-namespace --values helm/my-env/values.yaml
   ```

2. Create a filesystem secret:

   In the following command, replace `my-client-secret` with the client secret you obtained in the PingOne Application overview.

   ```
   $ kubectl create secret generic pingone-secrets \
     --namespace my-namespace \
     --from-literal=am.services.pingone.worker.pingprotect.clientsecret='my-client-secret'
   ```

3. Modify your ForgeOps deployment environment to set the secret name:

   ```
   $ cd /path/to/forgeops/bin
   $ ./forgeops env --env-name my-env --pingone-secret pingone-secrets
   ```

4. Redeploy ForgeOps to pick up the new secret:

   ```
   helm upgrade --install identity-platform ./charts/identity-platform  \
   --namespace my-namespace --values helm/my-env/values.yaml
   ```

5. Check if AM pods have started:

   ```
   $ kubectl get pods --namespace my-namespace
   $ kubectl rollout status deploy/am --namespace my-namespace
   ```

   |   |                                                                                                                                                      |
   | - | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | If any pod is in the `Error` or `CrashLoopBackOff` state, delete the pod with the kubectl delete pod pod-name command and let Kubernetes restart it. |

6. Verify that the secret is present and accessible to the AM pod:

   ```
   $ kubectl exec --namespace my-namespace deploy/am -- ls  /var/run/secrets/pingone
   Defaulted container "openam" out of: openam, ...
   am.services.pingone.worker.pingprotect.clientsecret
   ```

7. Configure a secret store in the AM native console:

   1. In the AM native console, navigate to **Secret Stores > Add Secret Store** and create a new secret store with the following values:

      | Field               | Value                      |
      | ------------------- | -------------------------- |
      | **Secret Store ID** | p1-worker-service          |
      | **Store Type**      | File System Secret Volumes |
      | **Directory**       | /var/run/secrets/pingone   |
      | **File Suffix**     | (leave empty)              |
      | **Value Format**    | Plain Text                 |

8. Configure a Worker Service in AM:

   1. In the AM native console, navigate to **Services > Add Service > PingOne Worker Server** and click **Create**.

   2. In the **Secondary Configuration** tab, click **Add a Secondary Configuration** and enter the following values in the **New workers configuration** form. Then click **Save**:

      | Field                              | Value                                                        |
      | ---------------------------------- | ------------------------------------------------------------ |
      | **Name**                           | Ping_SDK_Worker (note no spaces!)                            |
      | **Client ID**                      | 11a2…..(obtained from PingOne Worker application overview)   |
      | **Client Secret Label Identifier** | pingprotect                                                  |
      | **Environment ID**                 | b2d….(obtained from the PingOne Worker application overview) |

   3. In the ensuing **WORKERS CONFIGURATION** form for `Ping_SDK_Worker`, enter the following values and click **Save and Test Connection**: |**PingOne API Server URL and Authorization URL** |Select from these options, depending on where the PingOne tenant is hosted:

      | Region                           | API URL                      | Authorization URL          |
      | -------------------------------- | ---------------------------- | -------------------------- |
      | North America (Excluding Canada) | https\://api.pingone.com/v1  | https\://auth.pingone.com  |
      | Canada                           | https\://api.pingone.ca/v1   | https\://auth.pingone.ca   |
      | Europe                           | https\://api.pingone.eu/v1   | https\://auth.pingone.eu   |
      | Asia-Pacific                     | https\://api.pingone.asia/v1 | https\://auth.pingone.asia |

|   |                                                                                                                                                                                                                                                                                                    |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The configuration changes made in this section are file-based configuration changes. Therefore, you must export the configuration changes, build a new configuration image, and redeploy as explained in the next steps. Otherwise, you might lose the configuration changes when you redeploy AM. |

## Export AM runtime config into a profile and redeploy

To ensure that the new configuration, such as the file system secret store and worker service connection, isn't lost, the changes must be built into a new image. The following steps show how to export the configuration changes into a new profile, build a new configuration image, and redeploy AM.

1. Create a new profile by exporting the configuration:

   ```
   $ cd /path/to/forgeops/bin
   $ ./forgeops config export --baseline-profile default am workerService \
     --env-name my-env
   ```

2. Build the new config image:

   ```
   $ cd /path/to/forgeops/bin
   $ ./forgeops config build --env-name my-env \
     --config-profile workerService --tag workerService am
   ```

3. If needed, load the configuration image into minikube:

   ```
   $ minikube image load am-custom:workerService
   $ forgeops image --env-name my-env --custom am
   ```

4. Redeploy ForgeOps to pick up the new config image:

   ```
   helm upgrade --install identity-platform ./charts/identity-platform  \
   --namespace my-namespace --values helm/my-env/values.yaml
   ```

5. Check status and wait until the rollout is complete:

   ```
   $ kubectl rollout status deploy/am --namespace my-namespace
   ```

## Test the integration

1. In the AM native console, navigate to **Services** > **PingOne Worker Service** > **Secondary Configuration tab** > **Ping_SDK_Worker** > **Save and Test Connection**.

   You should see the **Connection was successful** message.

2. \[Optionally] Configure a test journey by using these links to test the integration:

   * [PingOne Protect integration](https://docs.pingidentity.com/pingam/8.1/integrations/pingone-protect.html)

   * [PingOne Protect Initialize node](https://docs.pingidentity.com/auth-node-ref/8.1/pingone/pingone-protect-initialize.html#example)

   * [PingOne Protect Result node](https://docs.pingidentity.com/auth-node-ref/8.1/pingone/pingone-protect-result.html)

---

---
title: Integration use cases
description: Integrate ForgeOps with PingOne services such as PingOne Protect and evaluate sample deployment use cases
component: forgeops
version: 2026.3
page_id: forgeops:integration:overview
canonical_url: https://docs.pingidentity.com/forgeops/2026.3/integration/overview.html
llms_txt: https://docs.pingidentity.com/forgeops/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-07-28T09:52:15Z
---

# Integration use cases

After you get your ForgeOps deployment up and running, you can test and evaluate integration with other Ping services. Some sample integration use cases are provided in this section:

| Topic                                                                    | Description                             |
| ------------------------------------------------------------------------ | --------------------------------------- |
| [icon: shield-check, set=fa][PingOne Worker service](int-p1-worker.html) | Integrate with PingOne Protect service. |

---

---
title: Ping RCS Connector
description: Deploy the Ping Remote Connector Server with ForgeOps
component: forgeops
version: 2026.3
page_id: forgeops:integration:rcs-helm-chart
canonical_url: https://docs.pingidentity.com/forgeops/2026.3/integration/rcs-helm-chart.html
llms_txt: https://docs.pingidentity.com/forgeops/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-08-12T20:30:59Z
---

# Ping RCS Connector

* Why RCS?

  The Ping Remote Connector Server (RCS) is a lightweight server that allows your ForgeOps deployment to connect to external systems that aren't directly accessible from the deployment. You can deploy RCS in the same Kubernetes cluster as your ForgeOps deployment or in a separate cluster. You can also deploy RCS on-premises or in the cloud, depending on your needs.

This use case focuses on using RCS to sync identities from Advanced Identity Cloud to ForgeOps so you can use ForgeOps as a disaster recovery environment.

* New RCS Helm chart

  You can now use the new `charts/rcs` Helm chart to deploy RCS in a ForgeOps deployment. The Helm chart sets up the following components:

  * **Communication**: The server listens on port 8759

  * **Security and access control**: You can optionally restrict which systems are allowed to connect (using `remoteIps`)

  * **Configuration**: The Helm chart manages the server's configuration files and logging settings

  * **Extensions**: You can add custom plugins or libraries to expand the server's capabilities

  * **Security certificates**: You can optionally add security certificates to protect connections

    When you deploy the server, it automatically creates a shared security key that all instances use. You can either let the system generate this key automatically by using a password (`RCS_KEY_PASSWORD`) or provide your own existing key.

* RCS registers with IDM automatically

  When you deploy the ForgeOps and RCS charts to the same namespace, IDM registers the RCS automatically. An optional sample LDAP provisioner (`platform.rcs.provisioner.enabled`) exposes the DS idrepo user store through the RCS, which gives the admin UI a working Connectors entry and a base for synchronization setup. Stale registration files are cleaned when IDM restarts. The deployer-supplied connector configurations remain unchanged.

* RCS chart hardening

  * The StatefulSet sets `serviceName`, which is required in Kubernetes versions earlier than 1.34 and provides DNS for each pod.

  * Secret volumes are readable by the non-root runtime UID (mode 0444).

  * The network policy uses the chart's own selector, admits same-namespace consumers alongside `remoteIps`, and allows DNS over TCP.

  * A `checksum/config` annotation rolls the pods when the rendered configuration changes.

  * `RCS_KEY` is JSON-escaped before being written into IDM's registration configuration.

  * `capabilities.drop` uses Kubernetes' `ALL` token instead of the invalid `All`.

  * The chart-publish workflow can no longer publish the placeholder-versioned platform charts or a chart with an unreadable version header.

Learn more about installing and configuring RCS with ForgeOps, in [Helm chart for RCS](https://github.com/ForgeRock/forgeops/tree/2026.3.2/charts/rcs/README.md).