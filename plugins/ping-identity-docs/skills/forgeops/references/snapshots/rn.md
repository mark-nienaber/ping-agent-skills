---
title: <code>forgeops</code> repository feature evolution
description: All the features demonstrated in the forgeops repository evolve continuously, and should be expected to change, potentially in backwards-incompatible ways. Specific changes are documented in the ForgeOps release notes, and might go through the following stages:
component: forgeops
version: 2026.2
page_id: forgeops:rn:evolution
canonical_url: https://docs.pingidentity.com/forgeops/2026.2/rn/evolution.html
llms_txt: https://docs.pingidentity.com/forgeops/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
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
description: Subscribe to the ForgeOps 2026.2.1 RSS feed to get notification when there's an update to the latest ForgeOps documentation.
component: forgeops
version: 2026.2
page_id: forgeops:rn:rn
canonical_url: https://docs.pingidentity.com/forgeops/2026.2/rn/rn.html
llms_txt: https://docs.pingidentity.com/forgeops/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  2026: 2026
  june_29_2026: June 29, 2026
  forgeops-2026-2-1-features: ForgeOps 2026.2.1 release features
  forgeops_2026_2_0_release_features: ForgeOps 2026.2.0 release features
---

# ForgeOps release notes

Subscribe to the [icon: rss-square, set=fa][ForgeOps 2026.2.1 RSS feed](https://docs.pingidentity.com/forgeops/latest/rn/rn.xml) to get notification when there's an update to the latest ForgeOps documentation.

|   |                                                                                                                                                                                                                                                              |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | Learn more about configuring GitHub notifications [here](https://docs.github.com/en/account-and-profile/managing-subscriptions-and-notifications-on-github/setting-up-notifications/configuring-notifications) so you can get notified on ForgeOps releases. |

|                                                                                                                                                              |                                                                    |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------ |
| Validated Kubernetes, Ingress-NGINX Controller, HAProxy Ingress, cert-manager, and operator versions for deploying Ping Advanced Identity Software 2026.2    | [Link](versions.html)                                              |
| Limitations when deploying Ping Advanced Identity Software `2026.2` on Kubernetes                                                                            | [Link](limitations.html)                                           |
| More information about the evolving nature of the `forgeops` repository, including technology previews, legacy features, and feature deprecation and removal | [Link](evolution.html)                                             |
| Legal notices                                                                                                                                                | [Link](legal.html)                                                 |
| Archive of release notes in ForgeOps 2026.1 are available from ForgeOps release 2026.1 documentation.                                                        | [Link](https://docs.pingidentity.com/forgeops/2026.1/rn/rn.html)   |
| Archive of release notes in ForgeOps 2025.1 and 2025.2 are available from ForgeOps release 2025.2 documentation.                                             | [Link](https://docs.pingidentity.com/forgeops/2025.2/rn/rn.html)   |
| Archive of release notes in 2024 and before are available from ForgeOps release 7.5 documentation.                                                           | [Link](https://docs.pingidentity.com/forgeops/7.5/rn/rn.html#2024) |
| Archive of release notes in 2023 and before are available from ForgeOps release 7.4 documentation                                                            | [Link](https://docs.pingidentity.com/forgeops/7.4/rn/rn.html#2023) |

## 2026

### June 29, 2026

* Support policy for ForgeOps-provided Ping Advanced Identity Software images

  Support for ForgeOps-provided Ping Advanced Identity Software images has been clarified. Learn more in the [Support for ForgeOps-provided images](../start/support.html#forgeops-image-support) section.

### ForgeOps 2026.2.1 release features

* Updated the list of how-tos available in \`forgeops\`repository

  The list of [how-to articles](../reference/how-tos.html) available in the `forgeops` repository has been updated in the documentation.

* SBOM for ForgeOps images

  Software Bill of Materials (SBOM) is now available for ForgeOps images. SBOM provides a detailed inventory of the components and dependencies used in ForgeOps images, which can help you identify and manage security vulnerabilities and compliance issues. Learn more in the [SBOM article](https://github.com/ForgeRock/forgeops/blob//2026.2.1/how-tos/retrieve-SBOMs-based-on-original-image-URL.md).

* Added self-signed certificate

  A self-signed certificate is now included for testing purposes in minikube environments.This certificate isn't intended for production use and should be used only in test environments.

* Avoid using secret generator

  There has been a lack of response from the secret generator project for questions and issues on using secret generator, we don't recommend or use it in ForgeOps environments. We'll be removing it from our artifacts in a future ForgeOps release. We've removed use of secret generator from ForgeOps documentation. Existing environments aren't affected by this change.

* IDM admin UI is deprecated in 8.1

  The IDM administration endpoint is deprecated in Ping Advanced Identity Software 8.1 and will be removed in a future release. You should use the identity Ping Advanced Identity Software admin UI or IDM REST API to administer user identities instead of the IDM admin UI. Learn more about this change in [Platform admin UI for standalone IDM](https://docs.pingidentity.com/pingidm/8.1/release-notes/whats-new.html#wn-platform-admin-ui-810).

### ForgeOps 2026.2.0 release features

* Removed `ds-util` container

  The `ds-util` container has been removed because the same tasks can be performed directly on DS pods.

- Read-only root filesystem for init containers (Helm only)

  The init containers of all pods have been reconfigured to enable `readOnlyRootFilesystem` security context. This has no impact on deployments, but requires that DS stateful sets be recreated. To enable the `readOnlyRootFilesystem` security context, follow [these steps](#enable-sec-features).

- Flags to enable or disable security features (Helm only)

  You can enable or disable the new security features in your ForgeOps environment using the `--secure` or `--insecure` flags. By default, new environments are created with the `--secure` flag, so the new security features are enabled.

  The `temp` directory of Tomcat is writeable, so users can continue to edit scripts in AM admin UI even when security is enabled.

|   |                                                                                           |
| - | ----------------------------------------------------------------------------------------- |
|   | These flags can be enabled or disabled only in ForgeOps environments deployed using Helm. |

To enable the security features in an existing environment:

1. Run the `forgeops` command:

   ```
   $ cd /path/to/forgeops
   $ ./bin/forgeops env --env-name my-env --secure
   ```

2. Recreate the DS stateful set using the instructions in the [how to recreate an STS article](https://github.com/ForgeRock/forgeops/blob//2026.2.1/how-tos/recreating-ds-sts.md).

   * The platform pods deployed as non-root user using user ID

     The AM, DS, and IDM pods are now deployed as the standard non-root user ID `11111` and the username is no longer referred to. The user ID `11111` is a security standard across the platform. This user ID is set in the pod security context as the `runAsUser` property.

   * `PodDisruptionBudgets` for product components

     You can enable `PodDisruptionBudgets` for platform product components in the Helm charts for Ping Advanced Identity Software including PingGateway. This feature is disabled by default. You can enable it for each component by setting component.pdb.enabled: true in your values file.

     The default policy keeps at least one pod available by setting minAvailable: 1. You can change this value by appropriately changing the value of component.pdb.minAvailable or component.pdb.maxUnavailable.

     The affected components are: `am`, `idm`, `admin-ui`, `end-user-ui`, `login-ui`, `ds-idrepo`, `ds-cts` and `ig` (ping-gateway).

   * Supported Ping Advanced Identity Software images

     ForgeOps supports the last three major or minor versions of the Ping Advanced Identity Software images. With the availability of 8.1 images, ForgeOps supports 8.1, 8.0, and 7.5 versions of the platform images, and **7.4 images are no longer supported**.

     We recommend customers that upgrade to a newer version of the platform images. Use the [upgrade guide](https://docs.pingidentity.com/forgeops/2026.2/upgrade/upgrade-product.html) to upgrade to the latest image. The older tags remain available on <http://releases.forgeops.com> until the next major/minor release.

   * The `config export no-upgrade` topic is removed from documentation

     The `config export` functionality has been included in the forgeops config export command. Because the forgeops config export command already separates out the upgrade function, this topic is not required in the Troubleshooting section of the documentation. The `no-upgrade` option of `config export` topic is removed from the documentation.

   * New `ttl` options for use with `amster` and `ds-set-passwords` jobs

     The `amster` and `ds-set-passwords` jobs now have a time-to-live (TTL) option that you can set to retain these jobs for a specified time. This is useful for jobs that are run manually need and to be retained to run to completion. To use this feature, set the `ttlSecondsAfterFinished` option. The default is 7200 seconds.

     |   |                                                     |
     | - | --------------------------------------------------- |
     |   | This feature is available in new environments only. |

   * Ability to define `apiVersion`, `kind`, and `spec` for a secret

     You can now define the `apiVersion`, `kind`, and `spec` for secrets defined in the `platform.secrets`. This allows you to define secrets using `external-secrets`.

---

---
title: Legal notices
description: Click here for legal information about product documentation published by Ping Identity.
component: forgeops
version: 2026.2
page_id: forgeops:rn:legal
canonical_url: https://docs.pingidentity.com/forgeops/2026.2/rn/legal.html
llms_txt: https://docs.pingidentity.com/forgeops/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
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
description: This page documents limitations on the Ping Advanced Identity Software when deployed on a Kubernetes cluster in the cloud.
component: forgeops
version: 2026.2
page_id: forgeops:rn:limitations
canonical_url: https://docs.pingidentity.com/forgeops/2026.2/rn/limitations.html
llms_txt: https://docs.pingidentity.com/forgeops/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
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

  AM doesn't support [property value substitution](../customize/value-substitution.html) for several types of configuration properties. Refer to [Property value substitution](https://docs.pingidentity.com/pingam/8/setup-guide/property-value-substitution.html) in the AM documentation for more information.

* The SOAP binding isn't supported for SAML v2.0 single logout.

  When deploying SAML v2.0 single logout, use the HTTP-POST or HTTP-Redirect bindings. The SOAP binding isn't supported when AM runs in a container.

* The shared identity repository isn't preconfigured for UMA deployments.

  The shared identity repository deployed with the CDK and the CDM isn't preconfigured to store UMA objects, such as resources, labels, audit messages, and pending requests.

  In order to use UMA in the CDK or the CDM, you'll need to customize your deployment. For more information, refer to the [*User-Managed Access (UMA) 2.0 Guide*](https://docs.pingidentity.com/pingam/8/uma-guide).

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
description: The following Kubernetes versions have been validated for use with Ping Advanced Identity Software 2026.2:
component: forgeops
version: 2026.2
page_id: forgeops:rn:versions
canonical_url: https://docs.pingidentity.com/forgeops/2026.2/rn/versions.html
llms_txt: https://docs.pingidentity.com/forgeops/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  kubernetes: Kubernetes
  forgeops_operators: ForgeOps operators
---

# Validated software versions

## Kubernetes

The following Kubernetes versions have been validated for use with Ping Advanced Identity Software 2026.2:

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

If you install the prerequisites using a technique other than using the forgeops prereqs command, install prerequisites of this version. Newer versions might work, but they haven't been tested with Ping Advanced Identity Software 2026.2.

## ForgeOps operators

ForgeOps has validated the following operator versions for use with Ping Advanced Identity Software 2026.2:

* [Secret Agent operator](https://github.com/ForgeRock/secret-agent) — version 1.2.10

* [DS operator](https://github.com/ForgeRock/ds-operator) — version 0.3.0