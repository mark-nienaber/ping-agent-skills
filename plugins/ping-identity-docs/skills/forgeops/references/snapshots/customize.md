---
title: <code>am</code> and <code>idm</code> images
description: "AM and IDM use two types of configuration: static configuration and dynamic configuration."
component: forgeops
version: 2026.2
page_id: forgeops:customize:fr-data
canonical_url: https://docs.pingidentity.com/forgeops/2026.2/customize/fr-data.html
llms_txt: https://docs.pingidentity.com/forgeops/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["CDK", "Dynamic Configuration", "Static Configuration", "Amster", "Configuration Profile"]
section_ids:
  static-configuration: Static configuration
  dynamic-configuration: Dynamic configuration
  tips_for_managing_am_dynamic_configuration: Tips for managing AM dynamic configuration
  tips_for_managing_idm_dynamic_configuration: Tips for managing IDM dynamic configuration
  configuration-profiles: Configuration profiles
  next_step: Next step
---

# `am` and `idm` images

AM and IDM use two types of configuration: [static configuration](#static-configuration) and [dynamic configuration](#dynamic-configuration).

## Static configuration

Static configuration consists of properties and settings used by the Ping Advanced Identity Software. Examples of static configuration include AM realms, AM authentication trees, IDM social identity provider definitions, and IDM data mapping models for reconciliation.

Static configuration is stored in JSON configuration files. Because of this, static configuration is also referred to as *file-based configuration*.

You build static configuration into the `am` and `idm` Docker images during development using the following general process:

1. Change the AM or IDM configuration in a single-instance ForgeOps deployment using the UIs and APIs.

2. Export the changes to your `forgeops` repository clone.

3. Build a new AM or IDM Docker image that contains the updated configuration.

4. Restart Ping Advanced Identity Software services using the new Docker images.

5. Test your changes. Incorrect changes to static configuration might cause the platform to become inoperable.

6. Promote your changes to your test and production environments as desired.

Refer to [`am` image](am.html) and [`idm` image](idm.html) for more detailed steps.

In Ping Advanced Identity Software deployments, static configuration is *immutable*. Do not change static configuration in testing or production. Instead, if you need to change static configuration, return to the development phase, make your changes, and build new custom Docker images that include the changes. Then, promote the new images to your test and production environments.

## Dynamic configuration

Dynamic configuration consists of access policies, applications, and data objects used by the Ping Advanced Identity Software. Examples of dynamic configuration include AM access policies, AM agents, AM OAuth 2.0 client definitions, IDM identities, and IDM relationships.

Dynamic configuration can change at any time, including when the platform is running in production.

You'll need to devise a strategy for managing AM and IDM dynamic configuration, so that you can:

* Extract sample dynamic configuration for use by developers.

* Back up and restore dynamic configuration.

### Tips for managing AM dynamic configuration

You can use one or both of the following techniques to manage AM dynamic configuration:

* Use the forgeops amster command to manage AM dynamic configuration. For example:

  1. Make modifications to AM dynamic configuration by using the AM admin UI.

  2. Export the AM dynamic configuration to your local file system by using the forgeops amster command. You might manage these files in a Git repository. For example:

     ```
     $ cd /path/to/forgeops/bin
     $ mkdir /tmp/amster
     $ ./forgeops amster export --env-name my-env /tmp/amster
     Cleaning up amster components
     Packing and uploading configs
     configmap/amster-files created
     configmap/amster-export-type created
     Deploying amster
     job.batch/amster created

     Waiting for amster job to complete. This can take several minutes.
     pod/amster-r99l9 condition met
     tar: Removing leading `/' from member names
     Updating amster config.
     Updating amster config complete.
     Cleaning up amster components
     job.batch "amster" deleted
     configmap "amster-files" deleted
     configmap "amster-export-type" deleted
     ```

  3. If desired, import these files into another AM deployment by using the forgeops amster import command.

  Note that the forgeops amster command automatically converts passwords in AM dynamic configuration to configuration expressions. Because of this, passwords in AM configuration files will not appear in cleartext. For details about how to work with dynamic configuration that has passwords and other properties specified as configuration expressions, refer to [Export Utilities and Configuration Expressions](value-substitution.html#export-config-expr).

* Write REST API applications to import and export AM dynamic configuration. For more information, refer to [Rest API](https://docs.pingidentity.com/pingam/8/REST-guide/preface.html) in the AM documentation.

### Tips for managing IDM dynamic configuration

You can use one or both of the following techniques to manage IDM dynamic configuration:

* Migrate dynamic configuration by using IDM's Data Migration Service. For more information, refer to [Migrate Data](https://docs.pingidentity.com/pingidm/8/upgrade-guide/data-migration.html) in the IDM documentation.

* Write REST API applications to import and export IDM dynamic configuration. For more information, refer to the [Rest API Reference](https://docs.pingidentity.com/pingidm/8/rest-api-reference/preface.html) in the IDM documentation.

## Configuration profiles

A Ping Advanced Identity Software *configuration profile* is a named set of configuration that describes the operational characteristics of a running ForgeOps deployment. A configuration profile consists of:

* AM static configuration

* IDM static configuration

Configuration profiles reside in the following paths in the `forgeops` repository:

* docker/am/config-profiles

* docker/idm/config-profiles

User-customized configuration profiles are stored in subdirectories of these paths. For example, a configuration profile named `my-profile` would be stored in the paths docker/am/config-profiles/my-profile and docker/idm/config-profiles/my-profile.

Use Git to manage the directories that contain configuration profiles.

## Next step

* [icon: check-square-o, set=fa][Perform additional setup](setup.html)

* [icon: check-square-o, set=fa][Understand custom images](custom-images.html)

* [icon: check-square-o, set=fa][Customize the DS image](ds.html)

* [icon: check-square-o, set=fa][Understand AM and IDM configuration](fr-data.html)

* [icon: square-o, set=fa]*[Understand property value substitution](value-substitution.html)*

* [icon: square-o, set=fa][Customize the AM image](am.html)

* [icon: square-o, set=fa][Customize the IDM image](idm.html)

---

---
title: <code>am</code> image
description: Prior to the ForgeOps 2026.1 release, the am Docker image contained the AM configuration. In ForgeOps 2026.1 and later releases, AM configuration has been separated from the AM image into a BusyBox container that contains the configuration profiles. This lets you customize configuration changes and build only the BusyBox images.
component: forgeops
version: 2026.2
page_id: forgeops:customize:am
canonical_url: https://docs.pingidentity.com/forgeops/2026.2/customize/am.html
llms_txt: https://docs.pingidentity.com/forgeops/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["CDK", "Docker", "forgeops Command"]
section_ids:
  customization_overview: Customization overview
  detailed_steps: Detailed steps
  redeploy-am-forgeops-command: "Redeploy AM: Kustomize deployments"
  redeploy-am-helm: "Redeploy AM: Helm deployments"
  next_step: Next step
---

# `am` image

Prior to the ForgeOps 2026.1 release, the `am` Docker image contained the AM configuration. In ForgeOps 2026.1 and later releases, AM configuration has been separated from the AM image into a [BusyBox](# "A BusyBox container is a minimal, lightweight containerized environment that includes a compact implementation of common UNIX utilities.") container that contains the configuration profiles. This lets you customize configuration changes and build only the [BusyBox](# "A BusyBox container is a minimal, lightweight containerized environment that includes a compact implementation of common UNIX utilities.") images.

## Customization overview

* Customize AM's configuration data by using the AM admin UI and REST APIs.

* Capture changes to the AM configuration by exporting them from the AM service running on Kubernetes to the staging area.

* Save the modified AM configuration to a configuration profile in your `forgeops` repository clone.

* Build a [BusyBox](# "A BusyBox container is a minimal, lightweight containerized environment that includes a compact implementation of common UNIX utilities.") container image using the exported configuration profile.

* Redeploy AM.

* Verify that changes you've made to the AM configuration are in the new Docker image.

## Detailed steps

1. Verify that:

   * You have access to a [single-instance ForgeOps deployment](../deploy/architecture.html#cluster-and-deployment-sizes).

   * The namespace where the platform is deployed is set in your Kubernetes context.

   * All required third-party software is installed in your local environment ([minikube](../setup/minikube.html#minikube-third-party-software)|[GKE](../setup/google-cloud.html#gcp-third-party-software)|[EKS](../setup/aws.html#aws-third-party-software)|[AKS](../setup/azure.html#azure-third-party-software)).

   * You've [set up your environment to push to your Docker registry](setup.html#docker-push).

2. Perform version control activities on your `forgeops` repository clone:

   1. Run the git status command.

   2. Review the state of the docker/am/config-profiles/my-profile directory.

   3. (Optional) Run the git commit command to commit changes to files that have been modified.

3. Modify the AM configuration using the AM admin UI or the REST APIs.

   You can find more information about how to access the AM admin UI or REST APIs in [AM Services](../deploy/access.html#am-services-cdm).

   You can find important information about configuring values that vary at run-time, such as passwords and host names in [About property value substitution](value-substitution.html).

4. Export the changes you made to the AM configuration in the running ForgeOps deployment to a configuration profile. To use the version of `am-config-upgrader` for your release, speciy the `--release-name` option:

   ```
   $ cd /path/to/forgeops/bin
   $ ./forgeops config export am --release-name my-release my-profile --sort
   ...
   ```

   If the configuration profile doesn't exist yet, the forgeops config export command creates it.

   The forgeops config export am my-profile command copies AM static configuration from the ForgeOps deployment to the configuration profile:

   ![Exporting the configuration from the single-instance deployment to a configuration profile.](_images/config-export-am.svg)

5. Perform version control activities on your `forgeops` repository clone:

   1. Review the differences in the files you exported to the configuration profile. For example:

      ```
      $ git diff
      diff --git a/docker/am/config-profiles/my-profile/config/services/realm/root/selfservicetrees/1.0/organizationconfig/default.json b/docker/am/config-profiles/my-profile/config/services/realm/root/selfservicetrees/1.0/organizationconfig/default.json
      index 970c5a257..19f4f17f0 100644
      --- a/docker/am/config-profiles/my-profile/config/services/realm/root/selfservicetrees/1.0/organizationconfig/default.json
      + b/docker/am/config-profiles/my-profile/config/services/realm/root/selfservicetrees/1.0/organizationconfig/default.json
      @@ -9,6 +9,7 @@
           "enabled": true,
           "treeMapping": {
             "Test": "Test",
      +      "Test1": "Test1",
             "forgottenUsername": "ForgottenUsername",
             "registration": "Registration",
             "resetPassword": "ResetPassword",
      ```

      The first time you export AM configuration changes to a configuration profile, the git diff command doesn't show any changes.

   2. Run the git status command.

   3. If you have new untracked files in your clone, run the git add command.

   4. Review the state of the docker/am/config-profiles/my-profile directory.

   5. (Optional) Run the git commit command to commit changes to files that have been modified.

6. [Identify the repository](setup.html#push-to) to which you'll push the Docker image. You'll use this location to specify the --push-to argument value in the [build am image](#build-am) step.

7. Decide on the image tag name to tag each build of the image. You'll use this tag name to specify the --tag argument in the [build am image](#build-am) step.

8. []()Build a new `BusyBox` image that includes AM static configuration change:

   |   |                                                                                                                                                                                                                                                                                                                                                                   |
   | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | While the forgeops build command uses the Docker engine by default for ForgeOps deployments, it supports Podman as well. If you are using Podman engine instead of Docker in your environment, then set the `CONTAINER_ENGINE` environment variable to `podman` before running the forgeops build command, for example:```
   $ export CONTAINER_ENGINE="podman"
   ``` |

   ```
   $ ./forgeops config build --env-name my-env am \
     --config-profile my-profile --push-to my-repo --tag my-am-tag
   ...
   ```

9. Redeploy AM using your new AM [BusyBox](# "A BusyBox container is a minimal, lightweight containerized environment that includes a compact implementation of common UNIX utilities.") image:

   * If you installed the platform using the forgeops command, follow the steps in [Redeploy AM: Kustomize deployments](#redeploy-am-forgeops-command).

   * If you installed the platform using Helm, follow the steps in [Redeploy AM: Helm deployments](#redeploy-am-helm).

### Redeploy AM: Kustomize deployments

The forgeops build command calls Docker to build a new `am` Docker image and to push the image to your Docker repository. The new image includes your configuration profile. It also updates the [image defaulter](https://github.com/ForgeRock/forgeops/blob/2026.2.1/kustomize/overlay/default/image-defaulter/kustomization.yaml) file so that the next time you install AM, the forgeops apply command gets AM static configuration from your new custom Docker image.

![Building the new custom Docker image.](_images/cdk-build.svg)

1. Perform version control activities on your `forgeops` repository clone:

   1. Run the git status command.

   2. Review the state of the kustomize/overlay/my-env/image-defaulter/kustomization.yaml file.

   3. (Optional) Run the git commit command to commit changes to the image defaulter file.

2. Remove AM from your ForgeOps deployment:

   ```
   $ ./forgeops delete am --env-name my-env
   ... platform detected in namespace: "my-namespace".
   Uninstalling component(s): ['am'] from namespace: "my-namespace".
   OK to delete components? [Y/N] Y
   service "am" deleted
   deployment.apps "am" deleted
   ```

3. Redeploy AM:

   ```
   $ ./forgeops apply am --env-name my-env
   Checking cert-manager and related CRDs: cert-manager CRD found in cluster.
   Checking secret-agent operator and related CRDs: secret-agent CRD found in cluster

   Installing component(s): ['am'] ... from deployment manifests in ...

   service/am created
   deployment.apps/am created

   Enjoy your deployment!
   ```

4. Validate that AM has the expected configuration:

   * Run the kubectl get pods command to monitor the status of the AM pod. Wait until the pod is ready before proceeding to the next step.

   * Describe the AM pod. Locate the tag of the Docker image that Kubernetes loaded, and verify that it's your new custom Docker image's tag.

   * Start the AM admin UI and verify that your configuration changes are present.

### Redeploy AM: Helm deployments

1. Locate the `Successfully tagged` message in the forgeops build output, which contains the new AM Docker image's repository and tag.

2. Redeploy AM using the new AM Docker image:

   ```
   $ helm upgrade identity-platform ./ \
    --namespace my-namespace \
    --values /path/to/forgeops/helm/my-env/values.yaml
   ```

3. Validate that AM has the expected configuration:

   * Run the kubectl get pods command to monitor the status of the AM pod. Wait until the pod is ready before proceeding to the next step.

   * Describe the AM pod. Locate the tag of the Docker image that Kubernetes loaded, and verify that it's your new custom Docker image's tag.

   * Start the AM admin UI and verify that your configuration changes are present.

## Next step

* [icon: check-square-o, set=fa][Perform additional setup](setup.html)

* [icon: check-square-o, set=fa][Understand custom images](custom-images.html)

* [icon: check-square-o, set=fa][Customize the DS image](ds.html)

* [icon: check-square-o, set=fa][Understand AM and IDM configuration](fr-data.html)

* [icon: check-square-o, set=fa][Understand property value substitution](value-substitution.html)

* [icon: check-square-o, set=fa][Customize the AM image](am.html)

* [icon: square-o, set=fa]*[Customize the IDM image](idm.html)*

---

---
title: <code>ds</code> image
description: The ds Docker image contains the DS configuration. You can customize the DS image before deploying it in your production environment.
component: forgeops
version: 2026.2
page_id: forgeops:customize:ds
canonical_url: https://docs.pingidentity.com/forgeops/2026.2/customize/ds.html
llms_txt: https://docs.pingidentity.com/forgeops/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  detailed_steps: Detailed steps
  next_step: Next step
---

# `ds` image

The `ds` Docker image contains the DS configuration. You can customize the DS image before deploying it in your production environment.

|   |                                                                                                 |
| - | ----------------------------------------------------------------------------------------------- |
|   | The customization described here is for use in new Ping Advanced Identity Software deployments. |

This section covers:

* Customize LDAP configuration by including LDIF format LDAP configuration files in `ldif-ext` directory.

* Customize LDAP schema by including customized schema LDIF files in the `config` directory.

* Customize DS setup behavior by updating the setup and post-init runtime scripts in the `runtime-scripts` directory.

* Build an updated DS Docker image that contains the above-mentioned customizations.

* Redeploy DS.

* Verify the changes you've made to the DS configuration are in the new Docker image.

## Detailed steps

1. Verify that:

   * You have access to a [single-instance ForgeOps deployment](../deploy/architecture.html#cluster-and-deployment-sizes).

   * The namespace where the platform is deployed is set in your Kubernetes context.

   * All required third-party software is installed in your local environment ([minikube](../setup/minikube.html#minikube-third-party-software)|[GKE](../setup/google-cloud.html#gcp-third-party-software)|[EKS](../setup/aws.html#aws-third-party-software)|[AKS](../setup/azure.html#azure-third-party-software)).

   * You've [set up your environment to push to your Docker registry](setup.html#docker-push).

2. Perform version control activities on your `forgeops` repository clone:

   1. Run the git status command.

   2. (Optional) Run the git commit command to commit the changes.

3. Add your DS customizations:

   1. Learn more at [custom LDAP configuration](https://community.forgerock.com/t/forgeops-ds-customization-guide-7-4-7-5/5525#adding-custom-ldap-configuration-3) to add LDAP configuration.

   2. Learn more in [custom LDAP schema](https://community.forgerock.com/t/forgeops-ds-customization-guide-7-4-7-5/5525#adding-custom-ldap-schema-4) to add LDAP schema.

   3. Customize DS's setup behavior in the /path/to/forgeops/docker/ds/ds-new directory:

      1. To set up profiles and indexes, edit the `runtime-scripts/setup` script. Learn more in [`setup` script details](https://community.forgerock.com/t/forgeops-ds-script-guide-7-4-7-5/5522#setup-15).

      2. To add custom configurations after indexes have been rebuilt, edit the `runtime-scripts/post-init` script. Learn more in [`post-init` script details](https://community.forgerock.com/t/forgeops-ds-script-guide-7-4-7-5/5522#post-init-12).

      3. To prepare the DS docker image for setup, edit the `ds-setup.sh` script. Learn more in [`ds-setup.sh` script details](https://community.forgerock.com/t/forgeops-ds-script-guide-7-4-7-5/5522#ds-setupsh-5).

4. [Identify the repository](setup.html#push-to) where you'll push the Docker image. You'll use this location to specify the --push-to argument value in the [build ds image](#build-ds) step.

5. Decide on the DS image tag for each build of the image. You'll use this tag to specify the `--tag` argument value in the [build DS image](#build-ds) step.

6. []()Build a new DS image that includes your customization:

   ```
   $ cd /path/to/forgeops/bin
   $ ./forgeops build ds --env-name my-env --config-profile my-profile --push-to my-repo --tag my-ds-tag
   ```

7. Redeploy DS using your new DS image:

* Deploy using the `forgeops` command

* Deploy using Helm

The `forgeops build` command calls Docker to build a new `ds` Docker image and to push the image to your Docker repository. The new image includes your custom LDAP and schema files. It also updates the image defaulter file so that the next time you install DS, the deployed DS server includes your custom DS image.

Perform version control activities on your `forgeops` repository clone:

1. Run the git status command.

   Review the state of the kustomize/overlay/my-env/image-defaulter/kustomization.yaml file.

2. (Optional) Run the git commit command to commit changes to the image defaulter file.

3. Remove DS from your ForgeOps deployment:

   ```
   $ ./forgeops delete ds --env-name my-env
   ...
   deployment.apps "ds" deleted
   ```

4. Delete the PVCs attached to DS pods using the kubectl delete pvc command.

5. Redeploy DS using the new Docker image:

   ```
   $ ./forgeops apply ds --env-name my-env --single-instance
   Checking cert-manager and related CRDs: cert-manager CRD found in cluster.
   Checking secret-agent operator and related CRDs: secret-agent CRD found in cluster
   ```

1) Locate the repository and tag for the new DS Docker image from the forgeops build command output.

2) Delete the PVCs attached to DS pods using the kubectl delete pvc command.

   If the attached DS pod is running, the PVC is not deleted immediately. So you should stop the running DS pods.

   In another terminal window, stop the DS pods using the kubectl delete pods command. This deletes the pods and its attached PVC.

3) Redeploy DS using the new Docker image:

   ```
   $ cd /path/to/forgeops/charts/identity-platform
   $ helm upgrade identity-platform ./ \
    --namespace my-namespace \
    --set 'ds.image.repository=my-repository' \
    --set 'ds.image.tag=my-ds-tag'
   ```

## Next step

* [icon: check-square-o, set=fa][Perform additional setup](setup.html)

* [icon: check-square-o, set=fa][Understand custom images](custom-images.html)

* [icon: check-square-o, set=fa][Customize the DS image](ds.html)

* [icon: square-o, set=fa]*[Understand AM and IDM configuration](fr-data.html)*

* [icon: square-o, set=fa][Understand property value substitution](value-substitution.html)

* [icon: square-o, set=fa][Customize the AM image](am.html)

* [icon: square-o, set=fa][Customize the IDM image](idm.html)

---

---
title: <code>idm</code> image
description: Prior to the ForgeOps 2026.1 release, the idm Docker image contained the IDM configuration. In ForgeOps 2026.1 and later releases, IDM configuration has been separated from the IDM image into a BusyBox container that contains the configuration profiles. This lets you customize configuration changes and build only the BusyBox images.
component: forgeops
version: 2026.2
page_id: forgeops:customize:idm
canonical_url: https://docs.pingidentity.com/forgeops/2026.2/customize/idm.html
llms_txt: https://docs.pingidentity.com/forgeops/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["CDK", "Docker", "forgeops Command"]
section_ids:
  customization_overview: Customization overview
  detailed_steps: Detailed steps
  redeploy-idm-forgeops-command: "Redeploy IDM: Kustomize deployments"
  redeploy-idm-helm: "Redeploy IDM: Helm deployments"
  next_step: Next step
---

# `idm` image

Prior to the ForgeOps 2026.1 release, the `idm` Docker image contained the IDM configuration. In ForgeOps 2026.1 and later releases, IDM configuration has been separated from the IDM image into a [BusyBox](# "A BusyBox container is a minimal, lightweight containerized environment that includes a compact implementation of common UNIX utilities.") container that contains the configuration profiles. This lets you customize configuration changes and build only the [BusyBox](# "A BusyBox container is a minimal, lightweight containerized environment that includes a compact implementation of common UNIX utilities.") images.

## Customization overview

* Customize IDM's configuration data by using the REST APIs.

* Capture changes to the IDM configuration by exporting them from the IDM service running on Kubernetes to the staging area.

* Save the modified IDM configuration to a configuration profile in your `forgeops` repository clone.

* Build a [BusyBox](# "A BusyBox container is a minimal, lightweight containerized environment that includes a compact implementation of common UNIX utilities.") container image using the exported configuration profile.

* Redeploy IDM.

* Verify that changes you've made to the IDM configuration are in the new Docker image.

## Detailed steps

1. Verify that:

   * You have access to a [single-instance ForgeOps deployment](../deploy/architecture.html#cluster-and-deployment-sizes).

   * The namespace where the platform is deployed is set in your Kubernetes context.

   * All required third-party software is installed in your local environment ([minikube](../setup/minikube.html#minikube-third-party-software)|[GKE](../setup/google-cloud.html#gcp-third-party-software)|[EKS](../setup/aws.html#aws-third-party-software)|[AKS](../setup/azure.html#azure-third-party-software)).

   * You've [set up your environment to push to your Docker registry](setup.html#docker-push).

2. Perform version control activities on your `forgeops` repository clone:

   1. Run the git status command.

   2. Review the state of the docker/idm/config-profiles/my-profile directory.

   3. (Optional) Run the git commit command to commit changes to files that have been modified.

3. Modify the IDM configuration using the REST APIs.

   Learn more about how to access the REST APIs in [IDM Services](../deploy/access.html#idm-services-cdm).

   More information about configuring values that vary at run-time, such as passwords and host names is available in [About property value substitution](value-substitution.html).

4. Export the changes you made to the IDM configuration in the running ForgeOps deployment to a configuration profile:

   ```
   $ cd /path/to/forgeops/bin
   $ ./forgeops config export idm my-profile --sort
   ...
   ```

   If the configuration profile doesn't exist yet, the forgeops config export command creates it.

   The forgeops config export idm my-profile command copies IDM static configuration from the ForgeOps deployment to the configuration profile:

   ![Exporting the configuration from the single-instance deployment to a configuration profile.](_images/config-export-idm.svg)

5. Perform version control activities on your `forgeops` repository clone:

   1. Review the differences in the files you exported to the configuration profile. For example:

      ```
      $ git diff
      diff --git a/docker/idm/config-profiles/my-profile/conf/audit.json b/docker/idm/config-profiles/my-profile/conf/audit.json
      index 0b3dbeed6..1e5419eeb 100644
      --- a/docker/idm/config-profiles/my-profile/conf/audit.json
      + b/docker/idm/config-profiles/my-profile/conf/audit.json
      @@ -135,7 +135,9 @@
         },
         "exceptionFormatter": {
           "file": "bin/defaults/script/audit/stacktraceFormatter.js",
      -    "globals": {},
      +    "globals": {
      +      "Test": "Test value"
      +    },
           "type": "text/javascript"
         }
       }
      ```

      The first time you export IDM configuration changes to a configuration profile, the git diff command doesn't show any changes.

   2. Run the git status command.

   3. If you have new untracked files in your clone, run the git add command.

   4. Review the state of the docker/idm/config-profiles/my-profile directory.

   5. (Optional) Run the git commit command to commit changes to files that have been modified.

6. [Identify the repository](setup.html#push-to) to which you'll push the Docker image. You'll use this location to specify the --push-to argument value in the [build idm image](#build-idm) step.

7. Decide on the image tag name so you can tag each build of the image. You'll use this tag name to specify the --tag argument value in the [build idm image](#build-idm) step.

8. []()Build a new [BusyBox](# "A BusyBox container is a minimal, lightweight containerized environment that includes a compact implementation of common UNIX utilities.") image that includes IDM static configuration changes:

   |   |                                                                                                                                                                                                                                                                                                                                                                   |
   | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | While the forgeops build command uses the Docker engine by default for ForgeOps deployments, it supports Podman as well. If you are using Podman engine instead of Docker in your environment, then set the `CONTAINER_ENGINE` environment variable to `podman` before running the forgeops build command, for example:```
   $ export CONTAINER_ENGINE="podman"
   ``` |

   ```
   $ ./forgeops config build --env-name my-env idm \
     --config-profile my-profile --push-to my-repo --tag my-idm-tag

   ...
   ```

9. Redeploy IDM using your new IDM [BusyBox](# "A BusyBox container is a minimal, lightweight containerized environment that includes a compact implementation of common UNIX utilities.") image:

   * If you installed the platform using the forgeops command, follow the steps in [Redeploy IDM: Kustomize deployments](#redeploy-idm-forgeops-command).

   * If you installed the platform using Helm, follow the steps in [Redeploy IDM: Helm deployments](#redeploy-idm-helm).

### Redeploy IDM: Kustomize deployments

The forgeops build command calls Docker to build a new `idm` Docker image and to push the image to your Docker repository. The new image includes your configuration profile. It also updates the [image defaulter](https://github.com/ForgeRock/forgeops/blob/2026.2.1/kustomize/overlay/default/image-defaulter/kustomization.yaml) file so that the next time you install IDM, the forgeops apply command gets IDM static configuration from your new custom Docker image.

![Building the new custom Docker image.](_images/cdk-build.svg)

1. Perform version control activities on your `forgeops` repository clone:

   1. Run the git status command.

   2. Review the state of the kustomize/overlay/my-env/image-defaulter/kustomization.yaml file.

   3. (Optional) Run the git commit command to commit changes to the image defaulter file.

2. Remove IDM from your ForgeOps deployment:

   ```
   $ ./forgeops delete idm --env-name my-env
   "cdk" platform detected in namespace: "my-namespace".
   Uninstalling component(s): ['idm'] from namespace: "my-namespace".
   OK to delete components? [Y/N] Y
   service "idm" deleted
   deployment.apps "idm" deleted
   ```

3. Redeploy IDM:

   ```
   $ ./forgeops apply idm --env-name my-env

   ...
   ```

4. Validate that IDM has the expected configuration:

   * Run the kubectl get pods command to monitor the status of the IDM pod. Wait until the pod is ready before proceeding to the next step.

   * Describe the IDM pod. Locate the tag of the Docker image that Kubernetes loaded, and verify that it's your new custom Docker image's tag.

### Redeploy IDM: Helm deployments

1. Locate the `Successfully tagged` message in the forgeops build output, which contains the new IDM Docker image's repository and tag.

2. Redeploy IDM using the new IDM Docker image:

   ```
   $ helm upgrade identity-platform ./ \
    --version 2026.2 --namespace my-namespace \
    --values /path/to/forgeops/helm/my-env/values.yaml
   ```

3. Validate that IDM has the expected configuration:

   * Run the kubectl get pods command to monitor the status of the AM pod. Wait until the pod is ready before proceeding to the next step.

   * Describe the IDM pod. Locate the tag of the Docker image that Kubernetes loaded, and verify that it's your new custom Docker image's tag.

## Next step

* [icon: check-square-o, set=fa][Perform additional setup](setup.html)

* [icon: check-square-o, set=fa][Understand custom images](custom-images.html)

* [icon: check-square-o, set=fa][Customize the DS image](ds.html)

* [icon: check-square-o, set=fa][Understand AM and IDM configuration](fr-data.html)

* [icon: check-square-o, set=fa][Understand property value substitution](value-substitution.html)

* [icon: check-square-o, set=fa][Customize the AM image](am.html)

* [icon: check-square-o, set=fa][Customize the IDM image](idm.html)

---

---
title: About custom images
description: To develop customized Docker images, start with ForgeOps-provided images. Then, build your configuration profile iteratively as you customize the platform to meet your needs. Building Docker images from time to time integrates your custom configuration profile into new Docker images.
component: forgeops
version: 2026.2
page_id: forgeops:customize:custom-images
canonical_url: https://docs.pingidentity.com/forgeops/2026.2/customize/custom-images.html
llms_txt: https://docs.pingidentity.com/forgeops/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["CDK", "Docker"]
section_ids:
  in_development: In development
  in_production: In production
  next_step: Next step
---

# About custom images

## In development

To develop customized Docker images, start with ForgeOps-provided images. Then, build your configuration profile iteratively as you customize the platform to meet your needs. Building Docker images from time to time integrates your custom configuration profile into new Docker images.

To develop a customized DS Docker image, refer to [`ds` image](ds.html).

To develop a customized AM Docker image, refer to [`am` image](am.html).

To develop a customized IDM Docker image, refer to [`idm` image](idm.html).

![Brief overview of containers for developers.](_images/containerization-dev.svg)

## In production

You can incorporate your configuration changes into the [BusyBox](# "A BusyBox container is a minimal, lightweight containerized environment that includes a compact implementation of common UNIX utilities.") container. To deploy the platform in production, build your configuration [BusyBox](# "A BusyBox container is a minimal, lightweight containerized environment that includes a compact implementation of common UNIX utilities.") container images and integrate in your ForgeOps deployment. The platform images are designed to work with configuration [BusyBox](# "A BusyBox container is a minimal, lightweight containerized environment that includes a compact implementation of common UNIX utilities.") containers, so you can use the latest platform images in production without building new PingAM and PingIDM base images. You don't need to build PingAM and PingIDM base images for production deployment.

Learn more about how to create Docker images for production deployment of the platform in [Base Docker images](../reference/base-docker-images.html).

![Brief overview of containers used in production.](_images/containerization-prod.svg)

## Next step

* [icon: check-square-o, set=fa][Perform additional setup](setup.html)

* [icon: check-square-o, set=fa][Understand custom images](custom-images.html)

* [icon: square-o, set=fa]*[Customize the DS image](ds.html)*

* [icon: square-o, set=fa][Understand AM and IDM configuration](fr-data.html)

* [icon: square-o, set=fa][Understand property value substitution](value-substitution.html)

* [icon: square-o, set=fa][Customize the AM image](am.html)

* [icon: square-o, set=fa][Customize the IDM image](idm.html)

---

---
title: About property value substitution
description: "Many property values in ForgeOps deployments' canonical configuration profile are specified as configuration expressions instead of as hard-coded values. Fully-qualified domain names (FQDNs), passwords, and several other properties are all specified as configuration expressions."
component: forgeops
version: 2026.2
page_id: forgeops:customize:value-substitution
canonical_url: https://docs.pingidentity.com/forgeops/2026.2/customize/value-substitution.html
llms_txt: https://docs.pingidentity.com/forgeops/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["CDK", "Dynamic Configuration", "Static Configuration", "Amster", "Configuration Profile"]
section_ids:
  how_property_value_substitution_works: How property value substitution works
  export-config-expr: Export utilities and configuration expressions
  in_the_idm_configuration: In the IDM configuration
  idm_static_configuration_export: IDM static configuration export
  in_the_am_configuration: In the AM configuration
  am_static_configuration_export: AM static configuration export
  am_dynamic_configuration_export: AM dynamic configuration export
  limitations_on_property_value_substitution_in_am: Limitations on property value substitution in AM
  next_step: Next step
---

# About property value substitution

Many property values in ForgeOps deployments' canonical configuration profile are specified as *configuration expressions* instead of as hard-coded values. Fully-qualified domain names (FQDNs), passwords, and several other properties are all specified as configuration expressions.

Configuration expressions are property values in the AM and IDM configurations that are set when AM and IDM start up. Instead of being set to fixed, hard-coded values in the AM and IDM configurations, their values vary, depending on conditions in the run-time environment.

Using configuration expressions lets you use a single configuration profile that takes different values at run-time depending on the deployment environment. For example, you can use a single configuration profile for development, test, and production deployments.

In the Ping Advanced Identity Software, configuration expressions are preceded by an ampersand and enclosed in braces. For example, `&{am.encryption.key}`.

The statement, `am.encryption.pwd=&{am.encryption.key}` in the AM configuration indicates that the value of the property, `am.encryption.pwd`, is determined when AM starts up. Contrast this with a statement, `am.encryption.pwd=myPassw0rd`, which sets the property to a hard-coded value, `myPassw0rd`, regardless of the run-time environment.

## How property value substitution works

This example shows how property value substitution works for a value specified as a configuration expression in the AM configuration:

1. Search the /path/to/forgeops/docker directory for the string `&{`.

2. Locate this line in your search results:

   ```
   "am.encryption.pwd=&{am.encryption.key}",
   ```

   Because the property `am.encryption.pwd` is being set to a configuration expression, its value will be determined when AM starts up.

3. Search the `forgeops` repository for the string `AM_ENCRYPTION_KEY`. You'll notice that the secret agent operator sets the environment variable, `AM_ENCRYPTION_KEY`. The property, `am.encryption.pwd`, will be set to the value of the environment variable, `AM_ENCRYPTION_KEY` when AM starts up.

Configuration expressions take their values from environment variables as follows:

* Uppercase characters replace lowercase characters in the configuration expression's name.

* Underscores replace periods in the configuration expression's name.

For more information about configuration expressions, refer to [Property Value Substitution](https://docs.pingidentity.com/pingidm/8/setup-guide/using-property-substitution.html) in the IDM documentation.

## Export utilities and configuration expressions

This section covers differences in how `forgeops` repository utilities export configuration that contains configuration expressions from a running ForgeOps deployment.

### In the IDM configuration

The IDM admin UI is aware of configuration expressions.

Passwords specified as configuration expressions are stored in IDM's JSON-based configuration files as configuration expressions.

#### IDM static configuration export

The `forgeops` repository's bin/config export idm command exports IDM static configuration from running ForgeOps deployments to your `forgeops` repository clone. The config utility makes no changes to IDM static configuration; if properties are specified as configuration expressions, the configuration expressions are preserved in the IDM configuration.

### In the AM configuration

The AM admin UI is *not* aware of configuration expressions.

Properties cannot be specified as configuration expressions in the AM admin UI; they must be specified as string values. The string values are preserved in the AM configuration.

AM supports specifying configuration expressions in both static and dynamic configuration.

#### AM static configuration export

The `forgeops` repository's bin/config export am command exports AM static configuration from running ForgeOps deployments to your `forgeops` repository clone. All AM static configuration properties, including passwords, have string values. However, after the config utility copies the AM static configuration from the `forgeops` repository, it calls the AM configuration upgrader. The upgrader transforms the AM configuration, following rules in the etc/am-upgrader-rules/placeholders.groovy file.

These rules tell the upgrader to convert a number of string values in AM static configuration to configuration expressions. For example, there are rules to convert all the passwords in AM static configuration to configuration expressions.

You'll need to modify the etc/am-upgrader-rules/placeholders.groovy file if:

* You add AM static configuration that contains new passwords.

* You want to change additional properties in AM static configuration to use configuration expressions.

|   |                                                                                                                                                      |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | An alternative to modifying the etc/am-upgrader-rules/placeholders.groovy file is using the jq command to modify the output from the config utility. |

#### AM dynamic configuration export

The `forgeops` repository's forgeops amster export command exports AM dynamic configuration from running ForgeOps deployments to your `forgeops` repository clone. When dynamic configuration is exported, it contains properties with string values. The forgeops amster export command transforms values for several types of properties to configuration expressions:

* Passwords

* Fully-qualified domain names

* The Amster version

The Secret Agent configuration computes and propagates passwords for AM dynamic configuration. You'll need to modify the `kustomize/base/secrets/secret_agent_config.yaml` file if:

* You add new AM dynamic configuration that contains passwords to be generated.

* You want to hard code a specific value for an existing password, instead of using a generated password.

#### Limitations on property value substitution in AM

AM doesn't support property value substitution for several types of configuration properties. Refer to [Property value substitution](https://docs.pingidentity.com/pingam/8/setup-guide/property-value-substitution.html) in the AM documentation for more information.

## Next step

* [icon: check-square-o, set=fa][Perform additional setup](setup.html)

* [icon: check-square-o, set=fa][Understand custom images](custom-images.html)

* [icon: check-square-o, set=fa][Customize the DS image](ds.html)

* [icon: check-square-o, set=fa][Understand AM and IDM configuration](fr-data.html)

* [icon: check-square-o, set=fa][Understand property value substitution](value-substitution.html)

* [icon: square-o, set=fa]*[Customize the AM image](am.html)*

* [icon: square-o, set=fa][Customize the IDM image](idm.html)

---

---
title: Additional setup
description: This page covers setup tasks that you'll need to perform before you can develop custom Docker images for the Ping Advanced Identity Software. Complete all of the tasks on this page before proceeding.
component: forgeops
version: 2026.2
page_id: forgeops:customize:setup
canonical_url: https://docs.pingidentity.com/forgeops/2026.2/customize/setup.html
llms_txt: https://docs.pingidentity.com/forgeops/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["CDK", "Mikikube", "GKE", "EKS", "AKS"]
section_ids:
  use_a_single_instance_forgeops_deployment: Use a single-instance ForgeOps deployment
  docker-push: Set up your environment to push to your Docker registry
  push-to: Identify the Docker repository to push to
  deploy-env-init: Initialize deployment environments
  next_step: Next step
---

# Additional setup

This page covers setup tasks that you'll need to perform before you can develop custom Docker images for the Ping Advanced Identity Software. Complete all of the tasks on this page before proceeding.

## Use a single-instance ForgeOps deployment

You must use a [single-instance ForgeOps deployment](../deploy/architecture.html#cluster-and-deployment-sizes) to develop custom Docker images for the Ping Advanced Identity Software.

Use the following links for information about how to create single-instance ForgeOps deployments:

* [Deploy using Helm on GKE, EKS, or AKS](../deploy/deploy-scenario-helm-cloud.html)

* [Deploy using Helm on minikube](../deploy/deploy-scenario-helm-local.html)

* [Deploy using Kustomize on GKE, EKS, or AKS](../deploy/deploy-scenario-kustomize-cloud.html)

* [Deploy using Kustomize on minikube](../deploy/deploy-scenario-kustomize-local.html)

## Set up your environment to push to your Docker registry

ForgeOps deployments support any container registry that supports Docker containers. You'll need to set up your local environment to support your container registry. Here are setup steps for four commonly-used container registries:

> **Collapse: Docker registry on minikube**
>
> Set up your local environment to execute docker commands on minikube's Docker engine.
>
> The ForgeOps team recommends using the built-in Docker engine when developing custom Docker images using minikube. When you use minikube's Docker engine, you don't have to build Docker images on a local engine and then push the images to a local or cloud-based Docker registry. Instead, you build images using the same Docker engine that minikube uses. This streamlines development.
>
> To set up your local computer to use minikube's Docker engine, run the docker-env command in your shell:
>
> ```
> $ eval $(minikube docker-env)
> ```
>
> For more information about using minikube's built-in Docker engine, refer to [Use local images by re-using the Docker daemon](https://kubernetes.io/docs/setup/learning-environment/minikube/#use-local-images-by-re-using-the-docker-daemon) in the minikube documentation.

> **Collapse: Google Cloud Artifact Registry or Container Registry**
>
> To set up your local computer to build and push Docker images:
>
> 1. If it's not already running, start a virtual machine that runs Docker engine. Refer to [Docker engine](../setup/google-cloud.html#docker-gcp) for more information.
>
> 2. Set up a Docker credential helper:
>
>    ```
>    $ gcloud auth configure-docker
>    ```

> **Collapse: AWS Elastic Container Registry**
>
> To set up your local computer to push Docker images:
>
> 1. If it's not already running, start a virtual machine that runs Docker engine. Refer to [Docker engine](../setup/aws.html#docker-aws) for more information.
>
> 2. Log in to Amazon ECR:
>
>    ```
>    $ aws ecr get-login-password | \
>     docker login --username AWS --password-stdin my-docker-registry
>    Login Succeeded
>    ```
>
>    ECR login sessions expire after 12 hours. Because of this, you'll need to perform these steps again whenever your login session expires.\[[1](#_footnotedef_1 "View footnote.")]

> **Collapse: Azure Container Registry**
>
> To set up your local computer to push Docker images:
>
> 1. If it's not already running, start a virtual machine that runs Docker engine. Refer to [Docker engine](../setup/azure.html#docker-azure) for more information.
>
> 2. Install the [ACR Docker Credential Helper](https://github.com/Azure/acr-docker-credential-helper).

## Identify the Docker repository to push to

When you execute the forgeops build command, you must specify the repository to push your Docker image to with the --push-to argument.

The forgeops build command appends a component name to the destination repository. For example, the command forgeops build am --push-to us-docker.pkg.dev/my-project pushes a Docker image to the `us-docker.pkg.dev/my-project/am` repository.

To determine how to specify the --push-to argument for four commonly-used container registries:

> **Collapse: Docker registry on minikube**
>
> Specify --push-to none with the forgeops build command to push the Docker image to the Docker registry embedded in the minikube cluster.

> **Collapse: Google Cloud Artifact Registry or Container Registry**
>
> Obtain the --push-to location from your cluster administrator. After it builds the Docker image, the forgeops build command pushes the Docker image to this repository.

> **Collapse: AWS Elastic Container Registry**
>
> Obtain the --push-to location from your cluster administrator. After it builds the Docker image, the forgeops build command pushes the Docker image to this repository.

> **Collapse: Azure Container Registry**
>
> Obtain the --push-to location from your cluster administrator. After it builds the Docker image, the forgeops build command pushes the Docker image to this repository.

## Initialize deployment environments

Deployment environments let you manage deployment manifests and image defaulters for multiple environments in a single `forgeops` repository clone.

By default, the forgeops build command updates the image defaulter in the kustomize/deploy directory.

When you specify a deployment environment, the forgeops build command updates the image defaulter in the kustomize/deploy-environment directory. For example, if you ran forgeops build --deploy-env production, the image defaulter in the kustomize/deploy-production/image-defaulter directory would be updated.

Before you can use a new deployment environment, you must initialize a directory based on the /path/to/forgeops/kustomize/deploy directory to support the deployment environment. Perform these steps to initialize a new deployment environment:

```
$ cd /path/to/forgeops/bin
$ ./forgeops clean
$ cd ../kustomize
$ cp -rp deploy deploy-my-environment
```

|   |                                                                                                                         |
| - | ----------------------------------------------------------------------------------------------------------------------- |
|   | If you need multiple deployment environments, you'll need to initialize each environment before you can start using it. |

## Next step

* [icon: check-square-o, set=fa][Perform additional setup](setup.html)

* [icon: square-o, set=fa]*[Understand custom images](custom-images.html)*

* [icon: square-o, set=fa][Customize the DS image](ds.html)

* [icon: square-o, set=fa][Understand AM and IDM configuration](fr-data.html)

* [icon: square-o, set=fa][Understand property value substitution](value-substitution.html)

* [icon: square-o, set=fa][Customize the AM image](am.html)

* [icon: square-o, set=fa][Customize the IDM image](idm.html)

***

[1](#_footnoteref_1). You can automate logging into ECR every 12 hours by using the `cron` utility.

---

---
title: Customization overview
description: This section covers how developers build custom Docker images for the Ping Advanced Identity Software. It also contains important conceptual material that you need to understand before you start creating Docker images.
component: forgeops
version: 2026.2
page_id: forgeops:customize:overview
canonical_url: https://docs.pingidentity.com/forgeops/2026.2/customize/overview.html
llms_txt: https://docs.pingidentity.com/forgeops/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Docker"]
section_ids:
  developer_checklist: Developer checklist
---

# Customization overview

This section covers how developers build custom Docker images for the Ping Advanced Identity Software. It also contains important conceptual material that you need to understand before you start creating Docker images.

* Configuration container

  In ForgeOps release 2026.1, AM and IDM configuration profiles have been moved out of the PingAM and PingIDM images into dedicated [BusyBox](# "A BusyBox container is a minimal, lightweight containerized environment that includes a compact implementation of common UNIX utilities.") containers. You can now customize the configuration profiles and rebuild only the configuration [BusyBox](# "A BusyBox container is a minimal, lightweight containerized environment that includes a compact implementation of common UNIX utilities.") images.

|   |                                                                                                                                     |
| - | ----------------------------------------------------------------------------------------------------------------------------------- |
|   | It is highly recommended to deploy the latest platform images in a production environment only after due customization and testing. |

## Developer checklist

Setup:

* [icon: square-o, set=fa]*[Perform additional setup](setup.html)*

* [icon: square-o, set=fa][Understand custom images](custom-images.html)

DS customization:

* [icon: square-o, set=fa][Customize the DS image](ds.html)

AM and IDM customization:

* [icon: square-o, set=fa][Understand AM and IDM configuration](fr-data.html)

* [icon: square-o, set=fa][Understand property value substitution](value-substitution.html)

* [icon: square-o, set=fa][Customize the AM image](am.html)

* [icon: square-o, set=fa][Customize the IDM image](idm.html)