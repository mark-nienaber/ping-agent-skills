---
title: <code>forgeops</code> repository feature evolution
description: Track ForgeOps releases including new features, deprecation, and removals
component: forgeops
version: 2026.3
page_id: forgeops:rn:evolution
canonical_url: https://docs.pingidentity.com/forgeops/2026.3/rn/evolution.html
llms_txt: https://docs.pingidentity.com/forgeops/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2024-11-21T10:28:18Z
---

# `forgeops` repository feature evolution

All the features demonstrated in the `forgeops` repository evolve continuously, and should be expected to change, potentially in backwards-incompatible ways. Specific changes are documented in the [ForgeOps release notes](rn.html), and might go through the following stages:

| Stage              | Definition                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| ------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Technology Preview | *Technology previews* provide access to new technology that is not yet supported. Technology preview features may be functionally incomplete, and the function as implemented is subject to change without notice. *DO NOT DEPLOY FEATURES MARKED AS BEING IN TECHNOLOGY PREVIEW INTO A PRODUCTION ENVIRONMENT.* You are encouraged to test drive technology preview features in a non-production environment, and are welcome to make comments and suggestions about the features. ForgeOps doesn't guarantee that a technology preview feature will be present at a future time. The final complete version of the feature is liable to change between preview and the final version. Technology previews are provided on an "as is" basis for evaluation purposes only, and Ping Identity accepts no liability or obligations for the use thereof. |
| Evolving           | All features that are not in technology preview, legacy, deprecated, or removed status are considered to be *evolving*. Evolving features might change at any time, even in backwards-incompatible ways. Evolving features in the `forgeops` repository might or might not be supported. Learn more in [Support for ForgeOps](../start/support.html).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| Legacy             | Features in *legacy* status have been replaced with improved versions, and are no longer being developed by ForgeOps. You should migrate to the newer version; however the existing functionality will remain. Legacy features or interfaces are marked as *Deprecated* if they are scheduled to be removed. Legacy features in the `forgeops` repository might or might not be supported. Learn more in [Support for ForgeOps](../start/support.html).                                                                                                                                                                                                                                                                                                                                                                                               |
| Deprecated         | *Deprecated* features are likely to be removed in future versions of the repository. Deprecated features in the `forgeops` repository might or might not be supported. Learn more in [Support for ForgeOps](../start/support.html).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| Removed            | Removed features were previously deprecated, and have now been removed. Features that have been removed from the `forgeops` repository are not supported.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |

---

---
title: ForgeOps release notes
description: Review ForgeOps release notes for new features, bug fixes, documentation updates, limitations, and supported platform changes
component: forgeops
version: 2026.3
page_id: forgeops:rn:rn
canonical_url: https://docs.pingidentity.com/forgeops/2026.3/rn/rn.html
llms_txt: https://docs.pingidentity.com/forgeops/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-08-28T11:57:11Z
section_ids:
  2026: 2026
  october_26_2026: October 26, 2026
  october_14_2026: October 14, 2026
  forgeops_2026_3_2_release_features: ForgeOps 2026.3.2 release features
  deprecated_features: Deprecated features
  new_features_and_updated_functionality: New features and updated functionality
  bug_fixes: Bug fixes
  documentation_updates: Documentation updates
  forgeops_2026_3_1_release_features: ForgeOps 2026.3.1 release features
  new_features_and_updated_functionality_2: New features and updated functionality
  bugfixes: Bugfixes
  august_28_2026: August 28, 2026
  august_24_2026: August 24, 2026
  august_17_2026: August 17, 2026
  august_14_2026: August 14, 2026
  forgeops_2026_3_0_release_features: ForgeOps 2026.3.0 release features
  new_features_and_updated_functionality_3: New features and updated functionality
  bug_fixes_2: Bug fixes
  documentation_updates_2: Documentation updates
---

# ForgeOps release notes

Subscribe to the [icon: rss-square, set=fa][ForgeOps 2026.3 RSS feed](https://docs.pingidentity.com/forgeops/latest/rn/rn.xml) to get notified when the latest ForgeOps documentation is updated.

|   |                                                                                                                                                                                                                                                              |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | Learn more about configuring GitHub notifications [here](https://docs.github.com/en/account-and-profile/managing-subscriptions-and-notifications-on-github/setting-up-notifications/configuring-notifications) so you can get notified on ForgeOps releases. |

|                                                                                                                                                              |                                                                    |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------ |
| Validated Kubernetes, Ingress-NGINX Controller, HAProxy Ingress, cert-manager, and operator versions for deploying Ping Advanced Identity Software 2026.3    | [Link](versions.html)                                              |
| Limitations when deploying Ping Advanced Identity Software `2026.3` on Kubernetes                                                                            | [Link](limitations.html)                                           |
| More information about the evolving nature of the `forgeops` repository, including technology previews, legacy features, and feature deprecation and removal | [Link](evolution.html)                                             |
| Legal notices                                                                                                                                                | [Link](legal.html)                                                 |
| Release notes for ForgeOps 2026.2                                                                                                                            | [Link](https://docs.pingidentity.com/forgeops/2026.2/rn/rn.html)   |
| Release notes for ForgeOps 2026.1                                                                                                                            | [Link](https://docs.pingidentity.com/forgeops/2026.1/rn/rn.html)   |
| Release notes for ForgeOps 2025.1 and 2025.2                                                                                                                 | [Link](https://docs.pingidentity.com/forgeops/2025.2/rn/rn.html)   |
| Release notes for 2024 and earlier                                                                                                                           | [Link](https://docs.pingidentity.com/forgeops/7.5/rn/rn.html#2024) |
| Release notes for 2023 and earlier                                                                                                                           | [Link](https://docs.pingidentity.com/forgeops/7.4/rn/rn.html#2023) |

## 2026

### October 26, 2026

* Added a procedure to set up custom release site

  A new procedure to create a custom release site has been added to the documentation. Learn more in the [Custom release site](../reference/releases.html) section.

### October 14, 2026

* New RCS Helm chart

  You can now use a new Helm chart called `charts/rcs` to deploy the Ping Remote Connector Server. Learn more in the [Ping RCS Connector](../integration/rcs-helm-chart.html) section.

* Update namespace for role-binding

  The forgeops env command now updates the namespace in the `role-binding.yaml` when `--namespace` option is used. This ensures that the role binding is created in the correct namespace.

* Fixed a bug in `forgeops config build` command

  When running the forgeops config build command, it throws errors because of a change to use the common args. The `args.profile` parameter needs to be `args.config_profile`. It has been fixed now.

* Fixed a syntax error in `docker/am/import-pem-certs.sh`

  In the `docker/am/import-pem-certs.sh` file, an invalid syntax (missing ']') was found. The syntax error has been fixed.

* Fixed the issue of multiple `monitor` users

  When using Prometheus for scraping, it caused errors because there are two `monitor` user entries present in the DS: one each for DS and IDM. This issue has been fixed now by appropriately addressing the scraping algorithm. If you are using older versions of ForgeOps tools, and have upgraded DS to 8.1.1 version, then you can fix the issue by removing the `monitor` user created by IDM. Learn more in the [Troubleshoot monitor user issue](../troubleshoot/monitor.html) section.

### ForgeOps 2026.3.2 release features

#### Deprecated features[icon: alarm-clock, set=fa]

The following tools are deprecated and will be removed after the deprecation period:

* Kustomize

  Support for Kustomize-based deployments is deprecated. Users should migrate to Helm chart-based deployments. You can use the [Migrate to Helm](https://github.com/ForgeRock/forgeops/blob//2026.3.2/how-tos/migrate-kustomize-to-helm.md) guide in the ForgeOps repository.

  * **Deprecated in:** 2026.3.2

  * **Expected removal:** 12 months after 2026.3.2 release

  * **Migration path:** Migrate to Helm chart-based deployments

* Secret agent

  The secret agent operator is deprecated. Users should migrate to the built-in Helm-generated secrets or an alternative secrets management solution such as External Secrets Operator or HashiCorp Vault. Use [Migrate to Helm-generated secrets](../prepare/security/migrate-helmsec.html) for guidance on migrating to Helm-generated secrets.

  * **Deprecated in:** 2026.3.2

  * **Expected removal:** 12 months after 2026.3.2 release

  * **Migration path:** Migrate to Helm-generated secrets or a supported external secrets management solution

#### New features and updated functionality

* Restored IDM admin UI for PingIDM 8.1.0

  In PingIDM 8.1.0, the legacy IDM admin UI was removed. It was also removed from the ForgeOps 2026.3.1 release. To support use cases that still require it, you can optionally enable IDM admin UI as a separate nginx pod in a Helm deployment in IDM 8.1.0 or later.

  |   |                                                                                                                                                                                                                                         |
  | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | 1. **This feature is available only in Helm deployments** and not in Kustomize deployments.

  2. This feature is available in ForgeOps 2026.3.1 release and later.

  3. The new URL path for the IDM is `/api` instead of `/openidm/api`. |

* Updated the process of customizing DS deployments

  The revised process of deploying customized DS is now available in the documentation. Learn more in the [Customize the DS Docker image](../customize/ds.html) section.

  A new [DS image description](https://github.com/ForgeRock/forgeops/blob//2026.3.2/docker/ds/README.md) file has been added in the `forgeops` repository.

* Enabled HTTPS access to the releases site

  The [releases site](https://releases.forgeops.com) could be accessed using HTTP protocol only. Now the releases site can be accessed using HTTPS protocol.

#### Bug fixes

* Refined `forgeops info --json` output

  The `forgeops info --json` command generated extra content that wasn't in JSON format. This caused JSON parsing errors when the output is used directly. Now, the `forgeops info --json` command has been refined so that only valid JSON format is produced.

* Update `ds-set-passwords` image when DS is updated

  Previously, the `ds-set-passwords` wasn't updated in the `values.yaml` file when DS image was updated, causing them to be out of sync. Now, the `ds-idrepo-0` image section is used directly instead of a separate `ds-set-passwords` image section to avoid any out-of-sync issue.

* Prevent logging sensitive information in Kubernetes logs

  The forgeops dsconfig command previously leaked the directory manager user's password into Kubernetes logs. Now, the forgeops dsconfig command copies a file containing the credentials to a temporary file in the pod. The dsconfig command running in the pod reads the credentials from the temporary file within the pod and is cleaned up after the command completes. This prevents the credentials from appearing in the logs.

* Fixed `forgeops config build` command

  The `forgeops config build` command had a bug preventing it from executing. This bug has been fixed.

* The `topologySpreadConstraint` configuration is corrected

  The `topologySpreadConstraint` blocks for ds-cts and ds-idrepo were improperly configured. The `matchLabels` is changed to `app.kubernetes.io/component`. The `topologyKey` is changed to `kubernetes.io/hostname`. This ensures that DS pods are upgraded using the rolling update strategy.

#### Documentation updates

* Procedure to customize DS Docker images

  The procedure to customize DS Docker images has been updated to reflect the revised DS base image creation process. Learn more in the [Customize the DS Docker image](../customize/ds.html) section.

* Procedure to migrate to Helm-based deployment

  The procedure to [migrate from Kustomize-based deployment to Helm-based](https://github.com/ForgeRock/forgeops/blob//2026.3.2/how-tos/migrate-kustomize-to-helm.md) deployment has been documented.

* Updated How-to procedures

  In the `forgeops` repository, the following procedures have been updated:

  * [Adding custom certificates to the truststore](https://github.com/ForgeRock/forgeops/blob//2026.3.2/how-tos/adding-user-supplied-certs-to-truststore.md).

  * [Retrieve SBOMs for ForgeOps images](https://github.com/ForgeRock/forgeops/blob//2026.3.2/how-tos/retrieve-SBOMs-based-on-original-image-URL.md).

* Renamed How-to procedures

  In the `forgeops` repository, the file name for the following procedures have been renamed:

  * [Enabling REST APIs in PingAccess](https://github.com/ForgeRock/forgeops/blob//2026.3.2/how-tos/pingam-enabling-rest-apis.md)

  * [Recreating DS STS](https://github.com/ForgeRock/forgeops/blob//2026.3.2/how-tos/pingds-recreating-sts.md)

  * [Using an externally deployed DS with a ForgeOps deployment](https://github.com/ForgeRock/forgeops/blob//2026.3.2/how-tos/pingds-use-an-externally-deployed-ds-with-a-forgeops-deployment.md)

### ForgeOps 2026.3.1 release features

#### New features and updated functionality

* New `forgeops dsconfig` subcommand

  A new `forgeops dsconfig` subcommand has been added to allow users to make changes to DS configuration in DS pods.

  The `forgeops dsconfig` command uses the secrets in the namespace where you deployed ForgeOps to determine the connection options needed and automatically passes them to the `dsconfig` command on the DS pod of your choosing.

  Enclose strings with spaces in double quotes and escape special characters as needed. Learn more using the `forgeops dsconfig --help` command.

* Removed the dry run (`-r`) short flag

  The dry run short flag (`-r`) conflicted with the repository option and has been removed. Use `--dryrun` instead.

#### Bugfixes

* Incorrect image tag for ssh-keygen job's init container

  The new job added in the 2026.3.0 release for Helm-generated secrets had a bug that mixed up the latest tag during the release process. Accordingly, the init container for the ssh-keygen job was using the wrong image tag. Now this issue has been fixed by pinning the tag for ssh-keygen's init container to a digest.

* AM port in `forgerock-metrics`

  The AM port in `forgerock-metrics` Helm chart has been changed to `http`.

* `forgeops env --upgrade` with `--no-helm` or `--no-kustomize`

  The `forgeops env --upgrade` command caused errors when `--no-helm` and `--no-kustomize` flags are used. Now the `forgeops env --upgrade` command has been updated to properly honor those flags.

* DS base image creation is under revision

  The DS base image creation process is being revised to incorporate the new changes to the DS product and the `forgeops` tool. The revised process will be available in the documentation soon.

### August 28, 2026

* `initImage` of `ssh-keygen` tag corrected

  The `initImage` tag of the `ssh-keygen` job was incorrectly set, which affected the use of Helm-generated secrets. Now the `initImage` tag setting has been corrected.

### August 24, 2026

* Deploying on WSL2 minikube cluster

  According to [this pull request](https://github.com/kubernetes/minikube/pull/23409), the network issues have been resolved. If you want to try deploying ForgeOps on a WSL2 minikube cluster, you can [set up minikube on WSL2](https://minikube.sigs.k8s.io/docs/tutorials/wsl_docker_driver) and deploy ForgeOps. However, the ForgeOps team hasn't tested the deployment on a WSL2 minikube cluster and might not be able to vouch for the correctness or completeness of the procedure.

### August 17, 2026

* Latest version of prereqs are installed by `forgeops prereqs` command

  The `forgeops prereqs` command now installs the latest versions of prerequisite components, except secret-agent. This avoids issues with older versions of prerequisite components that might not be compatible with the latest ForgeOps release.

### August 14, 2026

* Updated platform UI images are available

  Updated platform UI images are now available in ForgeOps deployments:

  * Ping Advanced Identity Software admin UI : **8.1.2**

  * Login UI : **8.1.2**

  * End-user UI : **8.1.2**

* Fix `forgeops env --upgrade` command

  The `forgeops env --upgrade` command now correctly honors `--no-helm` and `--no-kustomize` flags instead of erroring out. This allows you to upgrade only Helm charts or only Kustomize configurations in your ForgeOps deployment.

* Enable or disable security features

  In ForgeOps 2026.3.0 release and later, the security features are enabled by default when you create a ForgeOps deployment environment. You can also disable the security features when you create a ForgeOps deployment environment by using the `--insecure` option of the `forgeops env` command. Learn more in the [`forgeops env` command reference](../reference/forgeops-cmd-ref.html#forgeops-env) section.

### ForgeOps 2026.3.0 release features

#### New features and updated functionality

* Helm-generated secrets

  * Secrets generation (Helm only)

    You can now generate secrets with Helm in ForgeOps deployments. When you create a new ForgeOps environment with release 2026.2.0 or later, Helm-generated secret generation is enabled by default. Learn more in [Helm-generated secrets](../prepare/security/helm-gen-sec.html).

  * ssh-keygen job

    Helm cannot generate ssh keys, so a Kubernetes job is used to generate an ssh key and store it in a secret. This is used by `amster` to connect to am.

  * New migration command

    A new subcommand, **forgeops migrate sa2hs**, has been added. This subcommand can be used to migrate secrets from secret agent to Helm-generated secrets.

* Integration with the PingOne Worker service

  ForgeOps 2026.3 adds integration with the PingOne Worker service so you can use real-time risk scores to make authentication decisions. Learn more in [Integrate ForgeOps with the PingOne Worker service](../integration/int-p1-worker.html).

* Helm chart for RCS

  A new Helm chart has been created for RCS Server. This allows users to synchronize data with a ForgeOps deployment. Learn more in the [ForgeOps RCS Helm chart README.md file](https://github.com/ForgeRock/forgeops/tree/2026.3.2/charts/rcs/README.md).

* Dynamic job naming (Helm only)

  The Helm release revision number is now appended to the names of `amster`, `ds-set-passwords`, and `keystore-create` Kubernetes jobs in the `identity-platform` Helm chart. For example `amster-3`, `ds-set-passwords-3`, and `keystore-create-3`. This ensures that when the `helm upgrade` command is run, it generates a distinct job name, and prevents failures caused by Kubernetes' immutability constraint on existing jobs.

* Increased TTL for Helm jobs (Helm only)

  The default `ttlSecondsAfterFinished` value for all three Kubernetes jobs has been increased from 7200 seconds (2 hours) to 43200 seconds (12 hours), to afford more time to inspect completed or failed jobs before they are automatically cleaned up.

* Adding PingOne secret

  It is now possible to create and use a secret with ForgeOps to connect to the PingOne Worker Service. This secret gets mounted on the AM filesystem so that it can be used by AM. A new flag has been added to `forgeops env` to set the secret name. Learn more in the [PingOne Worker Service integration](../integration/int-p1-worker.html) section.

* Applying schema updates to existing deployments

  When you upgrade a ForgeOps deployment, DS schema updates now run automatically. A new `add schema` script in the `ds-idrepo` StatefulSet startup process applies schema changes when the deployed DS version requires them or when the schema is missing.

* Moving DS runtime scripts into the Helm chart

  Because the DS runtime scripts now apply changes over time, they are now part of the Helm chart. This lets schema changes apply without rebuilding DS images. For compatibility, the scripts remain hard-linked in `docker/DS` until older ForgeOps versions are no longer supported.

#### Bug fixes

* Dynamic Kubernetes job naming (Helm only)

  The `amster`, `ds-set-passwords`, and `keystore-create` Kubernetes job names in the `identity-platform` Helm chart now include the Helm release revision as a suffix, such as `amster-3`, `ds-set-passwords-3`, and `keystore-create-3`. This ensures that each `helm upgrade` creates a distinct job name and avoids failures caused by the Kubernetes job immutability constraint.

* Adding annotations for Traefik sticky sessions

  The `forgeops prereqs` command installs Traefik in NGINX compatibility mode to ease migration from the old, unmaintained NGINX ingress. If you install Traefik manually, sticky sessions can fail. ForgeOps now adds Traefik-specific annotations for sticky sessions to prevent that issue.

* `forgeops wait` reports success prematurely

  After `kubectl rollout restart` on a DS StatefulSet, `forgeops wait` could report success before the rollout completed. ForgeOps now uses `kubectl rollout status` to check readiness.

* Set the AM service port to HTTP

  The AM service port name now uses `http` instead of `https`. The previous name worked with NGINX and with Traefik in NGINX compatibility mode, but it caused failures when Traefik ran normally because the AM pod port is not an SSL port.

#### Documentation updates

* Connecting to the PingOne Worker service

  The documentation now includes a detailed procedure for connecting to the PingOne Worker service. Learn more in the [PingOne Worker service integration](../integration/int-p1-worker.html).

* Migrating to Helm-generated secrets

  The documentation now includes steps for migrating from secret-agent to Helm-generated secrets. Learn more in the [Helm-generated secrets](../prepare/security/helm-gen-sec.html) and [Migrate to Helm-generated secrets](../prepare/security/migrate-helmsec.html) sections.

* `forgeops upgrade-am-config` command

  The `forgeops upgrade-am-config` command lets you upgrade PingAM configuration profiles separately in your ForgeOps deployment environments. Learn more in the [`forgeops upgrade-am-config` command reference](../reference/forgeops-cmd-ref.html#upgrade-am-config).

* Archived ForgeOps documentation for releases 7.2, 7.3, and 7.4

  The documentation for ForgeOps releases 7.2, 7.3, and 7.4 is now [archived](https://docs.pingidentity.com/archive/#family-forgeops). This documentation is for reference only and is no longer actively maintained. PDFs are available at:

  * [ForgeOps 7.2 PDF](https://cdn-docs.pingidentity.com/archive/pdf/forgeops/7.2/forgeops-7.2.pdf)

  * [ForgeOps 7.3 PDF](https://cdn-docs.pingidentity.com/archive/pdf/forgeops/7.3/forgeops-7.3.pdf)

  * [ForgeOps 7.4 PDF](https://cdn-docs.pingidentity.com/archive/pdf/forgeops/7.4/forgeops-7.4.pdf)

* Support policy for ForgeOps-provided Ping Advanced Identity Software images

  The documentation now clarifies support for ForgeOps-provided Ping Advanced Identity Software images. Learn more in the [Support for ForgeOps-provided images](../start/support.html#forgeops-image-support) section.

* Replaced card blocks with table blocks in the documentation

  Documentation pages now use table blocks instead of card blocks to improve readability and make information easier to scan.

---

---
title: Legal notices
description: Review ForgeOps legal notices
component: forgeops
version: 2026.3
page_id: forgeops:rn:legal
canonical_url: https://docs.pingidentity.com/forgeops/2026.3/rn/legal.html
llms_txt: https://docs.pingidentity.com/forgeops/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-06-18T11:55:56Z
section_ids:
  about_ping_advanced_identity_software: About Ping Advanced Identity Software
  fontawesome_copyright: FontAwesome copyright
---

# Legal notices

Click [here](https://backstage.forgerock.com/knowledge/backstagehelp/article/a81642400) for legal information about product documentation published by Ping Identity.

## About Ping Advanced Identity Software

The Ping Advanced Identity Software serves as the basis for our simple and comprehensive identity and access management solution. We help our customers deepen their relationships with their customers, and improve the productivity and connectivity of their employees and partners. Learn more about ForgeOps and about the platform in <https://www.pingidentity.com/en/platform.html>.

The platform includes the following components:

* PingAM, previously ForgeRock® Access Management (AM)

* PingIDM, previously ForgeRock® Identity Management (IDM)

* PingDS, previously ForgeRock® Directory Services (DS)

* PingGateway, previously ForgeRock® Identity Gateway (IG)

## FontAwesome copyright

Copyright © 2017 by Dave Gandy, <https://fontawesome.com/>. This Font Software is licensed under the SIL Open Font License, Version 1.1. Refer to <https://opensource.org/license/openfont-html/>.

---

---
title: Limitations
description: Review ForgeOps limitations
component: forgeops
version: 2026.3
page_id: forgeops:rn:limitations
canonical_url: https://docs.pingidentity.com/forgeops/2026.3/rn/limitations.html
llms_txt: https://docs.pingidentity.com/forgeops/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-02-18T16:22:00Z
section_ids:
  platform-limitations: On all Ping Advanced Identity Software components
  ds-limitations: On PingDS
  am-limitations: On AM
  idm-limitations: On IDM
  ig-limitations: On PingGateway
---

# Limitations

This page documents limitations on the Ping Advanced Identity Software when deployed on a Kubernetes cluster in the cloud.

## On all Ping Advanced Identity Software components

* The forgeops config export command doesn't handle object deletion correctly.

  Configuration objects, such as AM authentication trees and service definitions, aren't deleted correctly by the forgeops config export command. If you've deleted one or more objects from your Ping Advanced Identity Software configuration in a single-instance deployment, and then you export the configuration, the deleted objects continue to exist in your configuration profile.

  To work around this problem, locate the deleted objects in your configuration profile after you've run the forgeops config export command. Then, delete the objects that should've been deleted from the JSON configuration files. After deleting the objects, if you build a new Docker image based on your configuration profile, the new image won't contain the deleted objects.

## On PingDS

* PingDS live data and logs should reside on fast disks.

  PingDS data requires high performant, low latency disks. Use external volumes on solid-state drives (SSDs) for directory data when running in production. Don't use network file systems such as NFS.

* Adding DS pods to a cluster should be done in advance of anticipated additional load.

  When you increase the number of DS pods in a cluster, they're automatically provisioned with the same directory data in existing pods. You must allow time for the data provisioning to complete and new pods to become available.

* Database encryption isn't supported.

  The `ds` Docker image doesn't support database encryption. DS fails to start if it detects that any data was encrypted during the Docker build process.

* DS starts successfully even when it can't decrypt a backend.

  When the DS master key isn't available, DS starts up successfully even though it's unable to decrypt a backend.

* Root file system write access is required to run the DS Docker image.

  The DS Docker image won't run without root file system write access.

## On AM

* AM must be reconfigured and restarted if the number of DS pods changes.

  In DS 8.1.0, you can elastically scale the number of DS pods in Kubernetes. However, the AM configuration doesn't automatically respond to changes in the number of DS pods.

  Because of this, you must modify the AM configuration after you scale the number of `idrepo` or `cts` pods in a running AM deployment.

* Using subrealms in ForgeOps deployments requires additional considerations.

  If you decide to deploy AM with subrealms, you'll need to configure the subrealms in the DS repository before starting AM. Make the LDAP configurations for the AM backend in [the relevant backend ldap configuration files](https://github.com/ForgeRock/forgeops/blob/main/docker/ds/ldif-ext/am-config/external-am-datastore.ldif).

* Session stickiness is required for some deployments.

  Two AM features are stateful, and require you to configure your load balancer to use sticky sessions:

  * SAML v2.0 single logout.

  * Browser-based authentication using authentication chains, which is deprecated in AM 8.1.0. Note that AM authentication trees are not stateful, and don't have this limitation.

  ForgeOps recommends that you configure your load balancer to use sticky sessions to achieve better performance. In the default ForgeOps deployment, Traefik is already configured with session stickiness.

* Value substitution is supported only for some configuration properties.

  AM doesn't support [property value substitution](../customize/value-substitution.html) for several types of configuration properties. Refer to [Property value substitution](https://docs.pingidentity.com/pingam/8.1/setup-guide/property-value-substitution.html) in the AM documentation for more information.

* The SOAP binding isn't supported for SAML v2.0 single logout.

  When deploying SAML v2.0 single logout, use the HTTP-POST or HTTP-Redirect bindings. The SOAP binding isn't supported when AM runs in a container.

* The shared identity repository isn't preconfigured for UMA deployments.

  The shared identity repository deployed with the CDK and the CDM isn't preconfigured to store UMA objects, such as resources, labels, audit messages, and pending requests.

  In order to use UMA in the CDK or the CDM, you'll need to customize your deployment. For more information, refer to the [*User-Managed Access (UMA) 2.0 Guide*](https://docs.pingidentity.com/pingam/8.1/uma-guide).

## On IDM

* The IDM repository is deployed in a single master topology.

  IDM can actively use only a single instance of DS as its repository. Should the DS instance fail, IDM can fail over to another DS instance; the limitation that only a single instance can be active applies. Using multiple DS replicas at the same time isn't supported.

* ForgeOps deployments aren't preconfigured to support IDM's workflow engine.

  ForgeOps deployments use DS as the IDM repository. Because of this, these deployments don't support IDM's workflow engine, and workflow features are disabled.

  Adding workflow support to ForgeOps deployments requires substantial, complex configuration changes, including:

  * Adding a JDBC repository to the ForgeOps deployment.

  * Enabling workflow features in IDM.

## On PingGateway

There are no limitations for this release.

---

---
title: Validated software versions
description: Check validated Kubernetes, ingress controller, cert-manager, and ForgeOps operator versions for ForgeOps deployments
component: forgeops
version: 2026.3
page_id: forgeops:rn:versions
canonical_url: https://docs.pingidentity.com/forgeops/2026.3/rn/versions.html
llms_txt: https://docs.pingidentity.com/forgeops/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-06-23T12:17:10Z
section_ids:
  kubernetes: Kubernetes
  forgeops_operators: ForgeOps operators
---

# Validated software versions

## Kubernetes

The following Kubernetes versions have been validated for use with Ping Advanced Identity Software 2026.3:

| Cloud provider                          | Kubernetes version                                                                              |
| --------------------------------------- | ----------------------------------------------------------------------------------------------- |
| Google Kubernetes Engine (GKE)          | 1.34                                                                                            |
| Amazon Elastic Kubernetes Service (EKS) | 1.34                                                                                            |
| Azure Kubernetes Service (AKS)          | 1.34                                                                                            |
| minikube                                | [The stable Kubernetes version for minikube](https://minikube.sigs.k8s.io/docs/commands/start). |

Earlier and later Kubernetes versions might also work. If you want to try using other Kubernetes versions, it's your responsibility to validate them.

The forgeops prereqs commmand is used to install the following prerequisites:

* Traefik version 3.6

* HAProxy Ingress controller version 0.14.5

* `cert-manager` version 1.13.0

If you install the prerequisites using a technique other than using the forgeops prereqs command, install prerequisites of this version. Newer versions might work, but they haven't been tested with Ping Advanced Identity Software 2026.3.

## ForgeOps operators

ForgeOps has validated the following operator versions for use with Ping Advanced Identity Software 2026.3:

* [Secret Agent operator](https://github.com/ForgeRock/secret-agent) — version 1.2.12

* [DS operator](https://github.com/ForgeRock/ds-operator) — version 0.3.0