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
