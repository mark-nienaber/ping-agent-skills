---
title: Migrate from a ForgeOps 7.4 or 7.5 release branch to the 2026.2 tag
description: If you've already installed Ping Advanced Identity Software using the previous release branch of the forgeops repository, such as release/7.4-20240126 or release/7.5-20240608, follow the steps provided on this page to upgrade to the latest platform 8.1.0 branch.
component: forgeops
version: 2026.2
page_id: forgeops:upgrade:mig-74-75
canonical_url: https://docs.pingidentity.com/forgeops/2026.2/upgrade/mig-74-75.html
llms_txt: https://docs.pingidentity.com/forgeops/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Upgrade", "ForgeOps"]
section_ids:
  prerequisites_and_assumptions: Prerequisites and assumptions
  subscribe_to_release_note_updates: Subscribe to release note updates
  back_up_critical_data: Back up critical data
  create_the_new_release_in_your_forgeops_branch: Create the new release in your forgeops branch
  export_the_release_7_4_or_7_5_am_and_idm_configurations: Export the release 7.4 or 7.5 AM and IDM configurations
  build_new_images_containing_your_forgeops_configuration: Build new images containing your ForgeOps configuration
  upgrade_the_exported_configuration_profiles_to_release_8_1_0: Upgrade the exported configuration profiles to release 8.1.0
  rebuild_your_new_images: Rebuild your new images
---

# Migrate from a ForgeOps 7.4 or 7.5 release branch to the 2026.2 tag

If you've already installed Ping Advanced Identity Software using the previous release branch of the `forgeops` repository, such as `release/7.4-20240126` or `release/7.5-20240608`, follow the steps provided on this page to upgrade to the latest platform 8.1.0 branch.

This upgrade methodology has been tested against a deployment based on ForgeOps-provided Docker images with basic configuration settings.

|   |                                                                                                                                                                                                                                                                                                                   |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Because the Ping Advanced Identity Software is highly customizable, it is challenging to test all possible upgrade scenarios. It is your responsibility to validate that these upgrade steps work correctly in a test environment with your customized configuration before you upgrade a production environment. |

## Prerequisites and assumptions

If you've deployed the Ping Advanced Identity Software from a previous release of ForgeOps, such as `release/7.4-20240126` or `release/7.5-20240608`:

* If you are using Kustomize to manage your ForgeOps deployment, [Migrate your Kustomize configurations](migrate-forgeops.html) first.

* You would have created your custom branch with the [new ForgeOps release](https://github.com/ForgeRock/forgeops).

* Copy your product configuration profiles from your 7.4 or 7.5 release branch, for example: /path/to/forgeops/docker/am/config-profile/my-profile to the same location in your new custom branch.

To upgrade the platform from release 7.4 or 7.5 to 8.1.0, you'll need:

* A running 7.4 or 7.5 release of ForgeOps deployment. If you need to port your AM custom configurations, then the running ForgeOps deployment should be a single-instance deployment with your AM and IDM configurations.

* A `forgeops` repository clone with a branch that contains 7.4 or 7.5 artifacts.

* A `forgeops` repository clone with a branch that contains 8.1.0 artifacts.

Example commands in the steps on this page assume:

* `7.4 or 7.5-profile` is the name of the 7.4 or 7.5 configuration profile.

* Your 7.4 or 7.5 ForgeOps deployment is a small cluster.

* Your 7.4 or 7.5 small, medium, or large ForgeOps deployment doesn't include PingGateway.

When you perform the upgrade:

* Choose a different name for the configuration profile if you prefer.

* Specify a different cluster size, if applicable.

* Add commands to upgrade PingGateway, if applicable.

## Subscribe to release note updates

Get updates from ForgeOps when there are changes to ForgeOps 2026.2.

For more information about getting notifications or subscribing to the ForgeOps 2026.2 RSS feed, refer to [ForgeOps release notes](../rn/rn.html).

## Back up critical data

Before upgrading, back up all critical data, including:

* Directory data stored in the `ds-idrepo` and `ds-cts` backends

* AM and IDM configuration data

* Customized artifacts in your `forgeops` repository clone

After you've started to upgrade, you might not be able to roll back directory data easily because the data is upgraded in place. If you need to roll back directory data, you'll have to redeploy DS and restore directory data from a backup. For a simpler restore scenario, consider backing up directory data on [volume snapshots](../backup/snapshots.html).

## Create the new release in your `forgeops` branch

You can manage multiple releases in ForgeOps 8.1.0 using the forgeops image command. Learn more about the [forgeops image command](https://github.com/ForgeRock/forgeops/blob/main/how-tos/manage-platform-images.md).

1. If you don't have the 7.4 or 7.5 release file for your 7.4 or 7.5 deployment, create a 7.4 or 7.5 release file in your `forgeops` branch. For example, to create the release file for 7.4.0 release:

   ```
    $ cd /path/to/forgeops
    $ ./bin/forgeops image --release 7.4.0 platform --release-name 7.4.0
   ```

   This is in case you need to roll back AM or IDM or you have configuration changes you wish to export from your single-instance environment.

2. Create a 8.1.0 release in docker/COMPONENT/releases/8.1.0 in your `forgeops` branch:

   ```
    $ cd /path/to/forgeops
    $ ./bin/forgeops image --release 8.1.0 platform --release-name 8.1.0
   ```

3. Set the images in your environment to the new release:

   ```
    $ ./bin/forgeops image --release 8.1.0 --env-name my-custom-env platform
   ```

## Export the release 7.4 or 7.5 AM and IDM configurations

If you have AM or IDM configuration changes, in a single-instance deployment, that you haven't yet exported to a configuration profile:

1. Locate a branch of your `forgeops` repository clone that contains release 7.4 or 7.5 artifacts and check out the branch.

2. (Optional) Check out a new branch based on the branch that contains release 7.4 or 7.5 artifacts.

3. Locate a namespace running release 7.4 or 7.5 of the single-instance deployment that contains your AM and IDM configurations.

4. Export the AM and IDM configurations from the 7.4 or 7.5 single-instance deployment:

   ```
   $ cd /path/to/forgeops
   $ ./bin/config export am 7.4 or 7.5-profile --sort --release-name 7.4 or 7.5
   $ ./bin/config export idm 7.4 or 7.5-profile --sort --release-name 7.4 or 7.5
   ```

   |   |                                                                                                                                                                                                                                                                     |
   | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | The `--release-name` option is required to ensure you use the release of the `am-config-upgrader` that matches your deployment. This only replaces any default config expressions that are lost during config updates in PingAM. It doesn't carry out any upgrades. |

## Build new images containing your ForgeOps configuration

1. Run the `am-config-upgrader` utility to upgrade the AM configuration to 8.1.0:

   ```
   $ cd /path/to/forgeops
   $ ./bin/forgeops upgrade-am-config docker/am/config-profiles/my-config-profile --release-name 8.1.0
   ```

2. Run the git add . and git commit commands.

3. Build Docker images for the newer patch release that contain your configuration profile:

   ```
   $ cd /path/to/forgeops
   $ ./bin/forgeops build am --config-profile my-config-profile \
     --env-name my-custom-env --release-name 8.1.0 --push-to my-repo  \
     --tag custom-am-tag

   $ ./bin/forgeops build idm --config-profile my-config-profile \
     --env-name my-custom-env --release-name 8.1.0 \
     --push-to my-repo --tag custom-idm-tag
   ```

   The newly built Docker images are based on ForgeOps-provided Docker images.

## Upgrade the exported configuration profiles to release 8.1.0

* In Kustomize environment

  1. Set your Kubernetes context to the cluster on which ForgeOps is deployed.

  2. Upgrade the `ds-cts` pods to the new patch release.

     1. Run the `forgeops apply ds-cts` command to update `ds-cts` pods sequentially:

        ```
        $ cd /path/to/forgeops
        $ ./bin/forgeops apply ds-cts --env-name my-custom-env
        ```

     2. Run the `kubectl get pods --watch` command to observe the pod upgrades.

     3. After all the `ds-cts` pods have been upgraded, run the `ds-debug.sh` command to verify that directory replication is working correctly in each ds-cts pod:

        ```
        $ ./bin/ds-debug.sh --pod-name ds-cts-0 rstatus
        ```

  3. Similarly, upgrade the `ds-idrepo` pods to the new patch release and verify that directory replication is working correctly in each `ds-idrepo` pod.

  4. Upgrade all the Ping Advanced Identity Software pods to the new patch release:

     ```
     $ ./bin/forgeops apply ui --env-name my-custom-env
     ```

     Wait for all the pods to be upgraded. Run the `kubectl get pods --watch` command to observe the progress of upgrade.

  5. Start the admin UIs for AM and IDM in the upgraded deployment and verify that:

     * The start page for each admin UI displays the expected component release for the 8.1.0 release.

     * AM and IDM use your custom configuration.

* In Helm environment

  1. Set your Kubernetes context to the cluster on which ForgeOps is deployed.

  2. Upgrade the platform:

     ```
     $ cd /path/to/forgeops
     $ helm upgrade --install identity-platform \
       oci://us-docker.pkg.dev/forgeops-public/charts/identity-platform \
       --version 8.1.0 --namespace my-namespace \
       --values helm/my-custom-env/values.yaml
     ```

  3. After all the `ds-cts` pods have been upgraded, run the `ds-debug.sh` command to verify that directory replication is working correctly in each ds-cts pod:

     ```
     $ ./bin/ds-debug.sh --pod-name ds-cts-0 rstatus
     ```

  4. After the `ds-idrepo` pods have been upgraded, run the ds-debug.sh command to verify that directory replication is working correctly:

     ```
     $ ./bin/ds-debug.sh --pod-name ds-idrepo-0 rstatus
     ```

  5. Start the admin UIs for AM and IDM in the upgraded deployment and verify that:

     * The start page for each admin UI displays the expected component release for the 8.1.0 release.

     * AM and IDM use your custom configuration.

## Rebuild your new images

If you are using ForgeOps deployment in production, you must rebuild base Docker images and custom Docker images for release 8.1.0:

* Learn more about building base docker images in [Your own base Docker images](../reference/base-docker-images.html#base-images).

* Learn more about building your Docker images with custom configurations in [Creating Docker images for use in production](../reference/base-docker-images.html#_create_docker_images_for_use_in_production).

---

---
title: Migrate your Kustomize configurations
description: This section covers steps required to migrate your Kustomize overlays from legacy ForgeOps artifacts, such as 7.4 or 7.5, to the new ForgeOps deployment environment.
component: forgeops
version: 2026.2
page_id: forgeops:upgrade:migrate-forgeops
canonical_url: https://docs.pingidentity.com/forgeops/2026.2/upgrade/migrate-forgeops.html
llms_txt: https://docs.pingidentity.com/forgeops/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Kustomize configuration", "ForgeOps"]
section_ids:
  considerations: Considerations
  migrating_your_kustomize_overlays: Migrating your Kustomize overlays
---

# Migrate your Kustomize configurations

This section covers steps required to migrate your Kustomize overlays from legacy ForgeOps artifacts, such as [7.4](https://github.com/ForgeRock/forgeops/tree/release/7.4-20240805) or [7.5](https://github.com/ForgeRock/forgeops/tree/release/7.5-20240618), to the new ForgeOps deployment environment.

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | 1. If you are using DS Operator in your deployment, then use [step 3 in Upgrade from version 7.3](https://docs.pingidentity.com/forgeops/7.4/how-to/73to74.html#upgrade_the_7_3_pods_to_7_4_and_build_custom_7_4_docker_images) to migrate away from using the DS Operator and then perform the migration.

2. When you migrate Kustomize overlays, **don't copy the files from the old overlay**. Create a new overlay and then copy the content in the old overlay to the new overlay. |

The format and layout of the overlays in the new **main** branch have changed from the previous ForgeOps releases. The main changes are:

* Each overlay contains sub-overlays for each product. This enables users to deploy products individually or collectively just as with the previous version of the forgeops command.

* The `image-defaulter` is included in the overlay, so that it's specific for a deployment environment.

* Each product has a separate dedicated ingress file. This enables users to set up product-specific configurations if required. Therefore, set up the FQDN for your new environment using the forgeops env command. **Don't migrate the old ingress overlay.**

## Considerations

Using the new forgeops command, you can select the version of products you want to deploy from 7.4 onwards. ForgeOps team recommends you migrate your deployment in the following way:

1. Migrate your overlay to the new overlay layout using the steps below.

2. Upgrade your images to a new version once your overlay is updated. Learn more at [Migrate from a ForgeOps 7.4 or 7.5 release branch to the 2026.2 tag](mig-74-75.html).

## Migrating your Kustomize overlays

To migrate your Kustomize overlays from previous versions, you need either of:

* Your custom overlay and the contents of kustomize/deploy/image-defaulter/kustomization.yaml, or

* Your custom deployment environment directory you've used to create a dedicated `image-defaulter` for your environment using the `--deploy-env` option.

Steps:

1. Ensure your custom overlay or custom deployment environment directory is saved locally so it's accessible when you check out the 2026.2.1 tag.

2. Check out the 2026.2.1 tag.

   ```
   $ cd /path/to/forgeops/
   $ git checkout 2026.2.1
   ```

3. Create a new overlay specifying your FQDN and the certificate issuer. Add the --deployment-size flag that most closely represents your old deployment.

   This adds the configuration into the Helm values file for you, so it's easy to edit the Helm values to match your Kustomize environment.

   ```
   $ ./bin/forgeops env --env-name my-env --fqdn my-fqdn \
     --cluster-issuer my-cluster-issuer --deployment-size
   ```

   |   |                                                                                                                                                                                                                                                                                                                |
   | - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | 1. Specify your FQDN when creating a new custom overlay as it will populate the required manifests in the new overlay.

   2. If you want to use a specific issuer for your deployment environment instead of the ClusterIssuer, then replace the `--cluster-issuer` option with `--issuer` option appropriately. |

4. Using the forgeops env command incorporate the modifications you made in your previous ForgeOps deployment. The following example shows how to set up AM replicas to 3:

   ```
   $ ./bin/forgeops env --env-name my-env am-rep 3

   Updating existing overlay.
   Updating existing helm values.
   ...
   ```

   |   |                                                                                                                                                                                 |
   | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | Note the value of `am:replicas` in the `my-env/am/deployment.yml` file:```
   apiVersion: apps/v1
   kind: Deployment
     name: am
       replicas: 3
       template:
         spec:
     \...
   ``` |

5. Run the forgeops image command to update the image in your container repository.

   1. Select the upstream platform image version for your running deployment. For example in a 7.5.0 platform:

      ```
      $ ./bin/forgeops image --env-name my-env --release 7.5.0 platform
      ```

   2. Set your custom images. For example, let's say the am image lines look like this in the `kustomize/overlay/my-env/image-defaulter/kustomization.yaml` file:

      ```
      name: am
        newName: us-docker.pkg.dev/MyProject/images/am
        newTag: 7.5.0
      \...
      ```

      Then use the forgeops image command with `tag` value of the component to build and store the component image in your container repository. For example, to build image for AM:

      ```
      $ ./bin/forgeops image --env-name my-env \
        --image-repo us-docker.pkg.dev/MyProject/images --tag 7.5.0 am
      ```

      * Other things to watch out for

        * Update the `base/base.yaml` file, and ensure to correctly specify the FQDN, `AM_STORES_CTS_SERVERS`, and `AM_STORES_USER_SERVERS`.

        * A separate ingress file exists for each product. The FQDN is populated in these files when you set up the deployment environment using the forgeops env command.

---

---
title: Update Helm Chart
description: In ForgeOps deployments using Helm chart version 2025.1.0 version or later, the customized values.yaml files are independent of the Helm chart versions. Therefore, you can update the version of a Helm chart and continue to work with your customized values.yaml files in your ForgeOps deployment environment.
component: forgeops
version: 2026.2
page_id: forgeops:upgrade:update-helm
canonical_url: https://docs.pingidentity.com/forgeops/2026.2/upgrade/update-helm.html
llms_txt: https://docs.pingidentity.com/forgeops/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Upgrade", "ForgeOps", "Helm chart"]
---

# Update Helm Chart

In ForgeOps deployments using Helm chart version 2025.1.0 version or later, the customized values.yaml files are independent of the Helm chart versions. Therefore, you can update the version of a Helm chart and continue to work with your customized `values.yaml` files in your ForgeOps deployment environment.

|   |                                                                                                                                                                                                                                                                                                                               |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | * The `values.yaml` files in ForgeOps deployments using 7.4 and 7.5 releases are not independent of the Helm chart versions. You cannot upgrade the Helm chart version in your ForgeOps deployment of 7.4 and 7.5 releases.

* Check the ForgeOps release notes to see what changes are in the new version of the Helm chart. |

1. If you used the helm upgrade --install command to perform ForgeOps deployment, you can update the Helm chart version:

   ```
   $ cd /path/to/forgeops
   $ helm upgrade --install identity-platform \
     oci://us-docker.pkg.dev/forgeops-public/charts/identity-platform \
     --version new-version --namespace my-namespace \
     --values helm/my-custom-env/values.yaml
   ```

   In the helm upgrade command, specify the new version of the Helm chart, such as 2025.1.1 for new-version.

---

---
title: Upgrade and Migration Overview
description: This section provides the conceptual and procedural details for upgrading your ForgeOps deployment environment or migrating utilities therein.
component: forgeops
version: 2026.2
page_id: forgeops:upgrade:upgrade-overview
canonical_url: https://docs.pingidentity.com/forgeops/2026.2/upgrade/upgrade-overview.html
llms_txt: https://docs.pingidentity.com/forgeops/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Upgrade", "ForgeOps"]
---

# Upgrade and Migration Overview

This section provides the conceptual and procedural details for upgrading your ForgeOps deployment environment or migrating utilities therein.

|   |                                                                                                                                                                                                                                                                                                                |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Because the Ping Advanced Identity Software is highly customizable, testing all possible upgrade scenarios is challenging. It is your responsibility to validate that these upgrade steps work correctly in a test environment with your customized configuration before you upgrade a production environment. |

Upgrading ForgeOps deployments involves three main sections:

* Upgrade ForgeOps deployment from 2025.1

  * [Upgrade Helm charts](update-helm.html)

* Upgrade Ping Advanced Identity Software Docker images

  * [Upgrade Ping Advanced Identity Software Docker images to new major or minor version](upgrade-product.html).

  * [Upgrade Ping Advanced Identity Software Docker image to new patch release](upgrade-patch.html).

* Upgrade from previous ForgeOps releases

  * [Migrate Kustomize configurations](migrate-forgeops.html).

  * [Migrate from a ForgeOps 7.4 or 7.5 release branch to the 2026.2 tag](mig-74-75.html).

---

---
title: Upgrade Ping Advanced Identity Software Docker image to new patch release
description: Patched images are released for each Ping Advanced Identity Software product separately. So you may need to update each of PingAM, PingIDM, or PingDS images to a newer image patch release separately.
component: forgeops
version: 2026.2
page_id: forgeops:upgrade:upgrade-patch
canonical_url: https://docs.pingidentity.com/forgeops/2026.2/upgrade/upgrade-patch.html
llms_txt: https://docs.pingidentity.com/forgeops/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Upgrade Forgeops", "Patch"]
section_ids:
  prerequisites_and_assumptions: Prerequisites and assumptions
  back_up_critical_directory_data: Back up critical Directory data
  get_ready_for_upgrade: Get ready for upgrade
  upgrade_a_product_to_a_newer_patch_release: Upgrade a product to a newer patch release
  upgrade_the_platform_uis_to_a_newer_patch_version: Upgrade the platform UIs to a newer patch version
---

# Upgrade Ping Advanced Identity Software Docker image to new patch release

Patched images are released for each Ping Advanced Identity Software product separately. So you may need to update each of PingAM, PingIDM, or PingDS images to a newer image patch release separately.

|   |                                                                                                                                                                                                                                                                                                                |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Because the Ping Advanced Identity Software is highly customizable, testing all possible upgrade scenarios is challenging. It is your responsibility to validate that these upgrade steps work correctly in a test environment with your customized configuration before you upgrade a production environment. |

## Prerequisites and assumptions

To upgrade PingAM, PingIDM, or PingDS image to a newer patch release, you'll need:

* A local clone of the ForgeOps repository.

* A running ForgeOps deployment deployed using ForgeOps 2025.1.0 or later.

* A configured ForgeOps deployment environment in your forgeops repository clone using the forgeops env command.

Example commands in this section assume that your ForgeOps deployment:

* Is using the default configuration.

* Doesn't include PingGateway.

## Back up critical Directory data

If upgrading DS, back up all the directory data stored in the `ds-idrepo` and `ds-cts` backends. After you've started to upgrade, you can't roll back directory data changes easily because the data is upgraded in place. To roll back directory data, you must redeploy DS and restore directory data. Consider backing up directory data on volume snapshots for a simpler restore scenario.

|   |                                                                                                                                           |
| - | ----------------------------------------------------------------------------------------------------------------------------------------- |
|   | For upgrading a `dev` environment, ensure that you've exported your AM or IDM configuration changes to your custom configuration profile. |

## Get ready for upgrade

1. Set your Kubernetes context so that you can access the cluster which contains your ForgeOps deployment.

2. Check the current supported product versions available if required:

   ```
   $ cd /path/to/forgeops
   $ ./bin/forgeops info --list-releases
   ```

## Upgrade a product to a newer patch release

This section covers the steps to upgrade AM, Amster, IDM, or DS to a new patch release.

|   |                                                                                                                      |
| - | -------------------------------------------------------------------------------------------------------------------- |
|   | Amster and AM need to be on the same version. So if you're upgrading AM, carry out the same steps to upgrade Amster. |

1. Create a new release in your ForgeOps repository clone that includes your customized configuration of the product to be updated, using one of the following options:

   1. To update to a new patch release use the forgeops image command and specify:

      * The new patch version in the `--release` flag.

      * Your current release in the `--release-name` flag.

        For example, to upgrade your AM image to 7.5.2 release:

        ```
        $ cd /path/to/forgeops
        $ ./bin/forgeops image --release 7.5.2 --release-name my-custom-release am
        ```

   2. To update to the latest secure image in your current release, use the forgeops image command and specify:

      * The product version you've deployed in the `--release` flag.

      * Specify your current release in the `--release-name` flag.

        |   |                                                                                                                                 |
        | - | ------------------------------------------------------------------------------------------------------------------------------- |
        |   | When you specify the current release in the forgeops image command, it selects the latest available secure image automatically. |

        For example, to upgrade your AM image to the latest secure image of 7.5.1 release:

        ```
        $ cd /path/to/forgeops
        $ ./bin/forgeops image --release 7.5.1 --release-name my-custom-release am
        ```

2. If you're upgrading AM, upgrade your custom AM configuration profile to the new version.

   |   |                                                                                                                                        |
   | - | -------------------------------------------------------------------------------------------------------------------------------------- |
   |   | The `--release-name` option is required to ensure you use the version of the `am-config-upgrader` that matches your target AM version. |

   ```
   $ cd /path/to/forgeops
   $ ./bin/forgeops upgrade-am-config --release-name my-custom-release \
    --config-profile docker/am/config-profiles/my-custom-release
   ```

3. Build your new custom image for the product you are upgrading.

   |   |                                                                 |
   | - | --------------------------------------------------------------- |
   |   | The `--config-profile` option isn't required to build DS image. |

   ```
   $ cd /path/to/forgeops
   $ ./bin/forgeops build am --env-name my-custom-env \
     --release-name my-custom-release \
     --config-profile my-config-profile
   ```

4. Deploy your updated version.

   > **Collapse: In a Helm environment**
   >
   > ```
   > $ cd /path/to/forgeops
   > $ helm upgrade --install identity-platform \
   > oci://us-docker.pkg.dev/forgeops-public/charts/identity-platform \
   > --version deployed version --namespace my-namespace \
   > --values helm/my-custom-env/values.yaml
   > ```

   > **Collapse: In a Kustomize environment**
   >
   > ```
   > $ cd /path/to/forgeops
   > $ ./bin/forgeops apply --env-name my-custom-env product
   > ```
   >
   > |   |                                                                                               |
   > | - | --------------------------------------------------------------------------------------------- |
   > |   | In the forgeops apply command, specify the product, such as `am`, `idm`, or `ds` for product. |

### Upgrade the platform UIs to a newer patch version

Use the steps in this section to upgrade platform UIs in a ForgeOps deployment. Usually the new platform UI patch versions are available together, so the steps upgrade all the platform UIs together. **You don't need to build new Docker images when you upgrade Platform UIs**.

1. Upgrade your deployment environment to the new patch version.

   1. To upgrade to the new patch release of platform UIs, specify the new patch number in the `--release` flag of the forgeops image command. For example, to upgrade to the **7.5.2** version UIs:

      ```
      $ cd /path/to/forgeops
      $ ./bin/forgeops image --release 7.5.2 ui --env-name my-custom-env
      ```

   2. To update to the latest platform UI secure image for the currently deployed release, specify the current platform UI version in the `--release` flag:

      ```
      $ cd /path/to/forgeops
      $ ./bin/forgeops image --release 7.5.1 ui --env-name my-custom-env
      ```

2. Deploy your updated patch image:

   > **Collapse: In a Helm environment**
   >
   > ```
   > $ cd /path/to/forgeops
   > $ helm upgrade --install identity-platform \
   > oci://us-docker.pkg.dev/forgeops-public/charts/identity-platform \
   > --version deployed version --namespace my-namespace \
   > --values helm/my-custom-env/values.yaml
   > ```

   > **Collapse: In a Kustomize environment**
   >
   > ```
   > $ cd /path/to/forgeops
   > $ ./bin/forgeops apply --env-name [.var}#my-custom-env# ui
   > ```

---

---
title: Upgrade Ping Advanced Identity Software Docker images to new major or minor version
description: If you've performed ForgeOps deployment using the older AM, IDM, and DS Docker images, you should upgrade your ForgeOps deployment to use the newer version of Ping Advanced Identity Software product Docker images.
component: forgeops
version: 2026.2
page_id: forgeops:upgrade:upgrade-product
canonical_url: https://docs.pingidentity.com/forgeops/2026.2/upgrade/upgrade-product.html
llms_txt: https://docs.pingidentity.com/forgeops/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Upgrade", "ForgeOps"]
section_ids:
  prerequisites_and_assumptions: Prerequisites and assumptions
  back_up_critical_data: Back up critical data
  get_ready_to_upgrade: Get ready to upgrade
  upgrade_the_platform_product_images_to_a_new_major_or_minor_version: Upgrade the platform product images to a new major or minor version
  upgrade_the_platform_uis_to_a_new_version: Upgrade the platform UIs to a new version
---

# Upgrade Ping Advanced Identity Software Docker images to new major or minor version

If you've performed ForgeOps deployment using the older AM, IDM, and DS Docker images, you should upgrade your ForgeOps deployment to use the newer version of Ping Advanced Identity Software product Docker images.

|   |                                                                                                           |
| - | --------------------------------------------------------------------------------------------------------- |
|   | Using this procedure, you can upgrade all the platform product Docker images sequentially, one at a time. |

This upgrade methodology has been tested against a deployment based on ForgeOps-provided Docker images with basic configuration settings.

|   |                                                                                                                                                                                                                                                                                                                |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Because the Ping Advanced Identity Software is highly customizable, testing all possible upgrade scenarios is challenging. It is your responsibility to validate that these upgrade steps work correctly in a test environment with your customized configuration before you upgrade a production environment. |

## Prerequisites and assumptions

To upgrade platform products in a ForgeOps deployment to a newer release, you'll need:

* A `forgeops` repository clone of ForgeOps 2026.1.0 release tag or later.

* A running ForgeOps deployment environment, which has been configured using the forgeops env command.

Example commands in the steps on this page assume that your ForgeOps deployment:

* Is using the default configuration.

* Doesn't include PingGateway.

## Back up critical data

Before upgrading, back up all critical data, including:

* Directory data stored in the `ds-idrepo` and `ds-cts` backends

* AM and IDM configuration data

* Customized artifacts in your `forgeops` repository clone

After you've started upgrading, you might not be able to roll back directory data easily because the data is upgraded in place. To roll back directory data, you must redeploy DS and restore directory data. Consider backing up directory data on [volume snapshots](../backup/snapshots.html) for a simpler restore scenario.

## Get ready to upgrade

1. Set your Kubernetes context to the cluster running your ForgeOps deployment.

2. View the list of supported product versions:

   ```
   $ cd /path/to/forgeops
   $ ./bin/forgeops info --list-releases
   ```

## Upgrade the platform product images to a new major or minor version

|   |                                                                                                                             |
| - | --------------------------------------------------------------------------------------------------------------------------- |
|   | Amster and AM images need to be on the same version. So if you're upgrading AM, carry out the same steps to upgrade Amster. |

1. Set images of the new version of ForgeOps provided platform products. Specify the new version in the `--release` flag:

   * The new product version in the `--release` flag, such as **8.1.0**.

   * The `platform` option to apply the product version to the whole platform.

     ```
     $ cd /path/to/forgeops
     $ ./bin/forgeops image --release 8.1.0 \
       --env-name my-env platform
     ```

2. Create your new release files for all platform products including `am-config-upgrader`.

   ```
   $ cd /path/to/forgeops
   $ *./bin/forgeops image --release 8.1.0 \
     --release-name my-custom-release am-config-upgrader
   ```

3. Upgrade your custom AM configuration profile to the new version:

   |   |                                                                                                                        |
   | - | ---------------------------------------------------------------------------------------------------------------------- |
   |   | Use the `--release-name` option to ensure you use the version of the `upgrade-am-config` that matches your deployment. |

   ```
   $ cd /path/to/forgeops
   $ ./bin/forgeops upgrade-am-config --release-name my-custom-release \
    --config-profile docker/am/config-profiles/my-config-profile
   ```

4. Build new custom images for AM and IDM using your release files and custom configuration profile:

   ```
   $ cd /path/to/forgeops
   $ ./bin/forgeops config build am --env-name my-custom-env \
     --release-name my-custom-release \
     --config-profile my-am-config-profile
   $ ./bin/forgeops config build idm --env-name my-custom-env \
     --release-name my-custom-release \
     --config-profile my-idm-config-profile
   ```

5. (Optional) Build new custom images for Amster and DS using your release files only if you have custom configuration for these products.

6. Deploy your updated images for all platform products:

   > **Collapse: In a Kustomize environment**
   >
   > ```
   > $ cd /path/to/forgeops
   > $ ./bin/forgeops apply --env-name my-custom-env platform
   > ```

   > **Collapse: In a Helm environment**
   >
   > ```
   > $ cd /path/to/forgeops/charts/identity-platform
   > $ helm upgrade --install identity-platform ./ \
   >  --values /path/to/forgeops/helm/my-env/values.yaml
   > ```

## Upgrade the platform UIs to a new version

This section refers to an upgrade to the platform UIs only.

**You don't need to build new Docker images when you upgrade Platform UIs**.

1. Update your environment to the new version. Specify the new version in the `--release` flag:

   ```
   $ cd /path/to/forgeops
   $ ./bin/forgeops image --release 8.0.0 ui --env-name my-custom-env
   ```

2. Deploy your updated version (Kustomize only)

   ```
   $ cd /path/to/forgeops
   $ ./bin/forgeops apply --env-name my-custom-env*
   ```