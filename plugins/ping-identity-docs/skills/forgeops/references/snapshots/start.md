---
title: Assess your skill level
description: I can:
component: forgeops
version: 2026.2
page_id: forgeops:start:start-here-skills
canonical_url: https://docs.pingidentity.com/forgeops/2026.2/start/start-here-skills.html
llms_txt: https://docs.pingidentity.com/forgeops/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Kubernetes", "Docker", "CI/CD", "Git", "Google Cloud", "AWS", "Azure", "Certificates", "SSL/TLS", "Load Testing", "Backup &amp; Restore"]
section_ids:
  skills-benchmarking: Benchmarking and load testing
  skills-cicd: CI/CD for cloud deployments
  skills-docker: Docker
  skills-git: Git
  skills-integration: External application and database integration
  skills-platform: Ping Advanced Identity Software
  skills-cdm-cloud-provider: Google Cloud, AWS, or Azure (basic)
  skills-prod-cloud-provider: Google Cloud, AWS, or Azure (expert)
  skills-integration-test: Integration testing
  skills-cdk-kubernetes: Kubernetes (basic)
  skills-prod-kubernetes: Kubernetes (expert)
  skills-kubernetes-backup: Kubernetes backup and restore
  skills-proj-plan: Project planning and management for cloud deployments
  skills-security: Security and hardening for cloud deployments
  skills-sr: Site reliability engineering for cloud deployments
---

# Assess your skill level

## Benchmarking and load testing

I can:

* Write performance tests, using tools such as Gatling and Apache JMeter, to ensure that the system meets required performance thresholds and service level agreements (SLAs).

* Resize a Kubernetes cluster, taking into account performance test results, thresholds, and SLAs.

* Run Linux performance monitoring utilities, such as top.

## CI/CD for cloud deployments

I have experience:

* Designing and implementing a CI/CD process for a cloud-based deployment running in production.

* Using a cloud CI/CD tool, such as Tekton, Google Cloud Build, Codefresh, AWS CloudFormation, or Jenkins, to implement a CI/CD process for a cloud-based deployment running in production.

* Integrating GitOps into a CI/CD process.

## Docker

I know how to:

* Write Dockerfiles.

* Create Docker images, and push them to a private Docker registry.

* Pull and run images from a private Docker registry.

I understand:

* The concepts of Docker layers, and building images based on other Docker images using the FROM instruction.

* The difference between the COPY and ADD instructions in a Dockerfile.

## Git

I know how to:

* Use a Git repository collaboration framework, such as GitHub, GitLab, or Bitbucket Server.

* Perform common Git operations, such as cloning and forking repositories, branching, committing changes, submitting pull requests, merging, viewing logs, and so forth.

## External application and database integration

I have expertise in:

* AM policy agents.

* Configuring AM policies.

* Synchronizing and reconciling identity data using IDM.

* Managing cloud databases.

* Connecting Ping Advanced Identity Software components to cloud databases.

## Ping Advanced Identity Software

I have:

* Attended Ping Identity University training courses.

* Deployed the Ping Advanced Identity Software in production, and kept the deployment highly available.

* Configured DS replication.

* Passed the Certified Access and Identity Management exams from Ping Identity (highly recommended).

## Google Cloud, AWS, or Azure (basic)

I can:

* Use the graphical user interface for Google Cloud, AWS, or Azure to navigate, browse, create, and remove Kubernetes clusters.

* Use the cloud provider's tools to monitor a Kubernetes cluster.

* Use the command user interface for Google Cloud, AWS, or Azure.

* Administer cloud storage.

## Google Cloud, AWS, or Azure (expert)

In addition to the [basic skills for Google Cloud, AWS, or Azure](#skills-cdm-cloud-provider), I can

* Review Terraform artifacts in the `forgeops-extras` repository to see how clusters that support ForgeOps deployments are configured.

* Create and manage a Kubernetes cluster using an infrastructure-as-code tool such as Terraform, AWS CloudFormation, or Pulumi.

* Configure multi-zone and multi-region Kubernetes clusters.

* Configure cloud-provider identity and access management (IAM).

* Configure virtual private clouds (VPCs) and VPC networking.

* Manage keys in the cloud using a service such as Google Key Management Service (KMS), Amazon KMS, or Azure Key Vault.

* Configure and manage DNS domains on Google Cloud, AWS, or Azure.

* Troubleshoot a deployment running in the cloud using the cloud provider's tools, such as Google Stackdriver, Amazon CloudWatch, or Azure Monitor.

* Integrate a deployment with certificate management tools, such as cert-manager and Let's Encrypt.

* Integrate a deployment with monitoring and alerting tools, such as Prometheus and Alertmanager.

I have obtained one of the following certifications (highly recommended):

* Google Certified Associate Cloud Engineer Certification.

* AWS professional-level or associate-level certifications (multiple).

* Azure Administrator.

## Integration testing

I can:

* Automate QA testing using a test automation framework.

* Design a chaos engineering test for a cloud-based deployment running in production.

* Use chaos engineering testing tools, such as Chaos Monkey.

## Kubernetes (basic)

I've gone through the tutorials at kubernetes.io, and am able to:

* Use the kubectl command to determine the status of all the pods in a namespace, and to determine whether pods are operational.

* Use the kubectl describe pod command to perform basic troubleshooting on pods that are not operational.

* Use the kubectl command to obtain information about namespaces, secrets, deployments, and stateful sets.

* Use the kubectl command to manage persistent volumes and persistent volume claims.

## Kubernetes (expert)

In addition to the [basic skills for Kubernetes](#skills-cdk-kubernetes), I have:

* Configured role-based access to cloud resources.

* Configured Kubernetes objects, such as deployments and stateful sets.

* Configured Kubernetes ingresses.

* Configured Kubernetes resources using Kustomize.

* Passed the Cloud Native Certified Kubernetes Administrator exam (highly recommended).

## Kubernetes backup and restore

I know how to:

* Schedule backups of Kubernetes persistent volumes on volume snapshots.

* Restore Kubernetes persistent volumes from volume snapshots.

I have experience with one or more of the following:

* Volume snapshots on Google Kubernetes Engine (GKE), Amazon Elastic Kubernetes Service (EKS), or Azure Kubernetes Service (AKS)

* A third-party Kubernetes backup and restore product, such as Velero, Kasten K10, TrilioVault, Commvault, or Portworx PX-Backup.

## Project planning and management for cloud deployments

I have planned and managed:

* A production deployment in the cloud.

* A production deployment of Ping Advanced Identity Software.

## Security and hardening for cloud deployments

I can:

* Harden a Ping Advanced Identity Software deployment.

* Configure TLS, including mutual TLS, for a multi-tiered cloud deployment.

* Configure cloud identity and access management and role-based access control for a production deployment.

* Configure encryption for a cloud deployment.

* Configure Kubernetes network security policies.

* Configure private Kubernetes networks, deploying bastion servers as needed.

* Undertake threat modeling exercises.

* Scan Docker images to ensure container security.

* Configure and use private Docker container registries.

## Site reliability engineering for cloud deployments

I can:

* Manage multi-zone and multi-region deployments.

* Implement DS backup and restore in order to recover from a database failure.

* Manage cloud disk availability issues.

* Analyze monitoring output and alerts, and respond should a failure occur.

* Obtain logs from all the software components in my deployment.

* Follow the cloud provider's recommendations for patching and upgrading software in my deployment.

* Implement an upgrade scheme, such as blue/green or rolling upgrades, in my deployment.

* Create a Site Reliability Runbook for the deployment, documenting all the procedures to be followed and other relevant information.

* Follow all the procedures in the project's Site Reliability Runbook, and revise the runbook if it becomes out-of-date.

---

---
title: ForgeOps release process
description: ForgeOps release process is aimed at simplifying the management of multiple ForgeOps versions in a single branch. This process:
component: forgeops
version: 2026.2
page_id: forgeops:start:release-process
canonical_url: https://docs.pingidentity.com/forgeops/2026.2/start/release-process.html
llms_txt: https://docs.pingidentity.com/forgeops/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Docker", "forgeops Command"]
section_ids:
  key_features: Key features
---

# ForgeOps release process

ForgeOps release process is aimed at simplifying the management of multiple ForgeOps versions in a single branch. This process:

* Removes the need to create and maintain multiple release branches for every product release.

* Enables easier upgrading and switching between multiple supported versions.

* Supports delivery of regularly promoted secure Docker images.

* Unifies documentation to easily consume product information.

## Key features

* Single `main` branch for all new releases

  * The `main` branch doesn't replace the already released forgeops branches. The currently released branches continue to be supported and updated with new minor and patch releases of the products.

  * Deployments use the latest available image for the current product version by default. Customers can select to use a specific supported image as per their needs.

* Product versions are separated from the `forgeops` repository

  * Product image tags are now maintained in tag files at <http://releases.forgeops.com>.

  * The refactored `forgeops` tool retrieves the requested tags and updates Dockerfiles/Helm/Kustomize as required.

  * All new major releases will be released using the new release process only.

  * The new process also supports 7.5 and 7.4 product image tags. Customers can continue to use the release/7.5-\* and release/7.4-\* branches until they are ready to migrate to the new process.

  * Customers can select the latest early-adapter images of the products to test the latest product features (similar to the dev image tag on the `master` branch previously).

* Supported Docker images

  * The new process is required to handle regular delivery of updated secure product images.

    * Docker images are routinely scanned for OS-level vulnerabilities and addressed by the ForgeOps team where OS patches are available.

    * The Ping Advanced Identity Software teams provide the platform-level patches.

  * The delivery process is automated, and the newly promoted tags will be available at <http://releases.forgeops.com>.

  * New `dev` branch for latest forgeops features. Equivalent to the erstwhile `master` branch which is no longer available.

  * Updated release information on <https://github.com/ForgeRock/forgeops>. Customers can get release updates by setting up their GitHub notifications.

  * Single set of documentation that is updated for ForgeOps releases and updates to the `main` branch.

  * Best efforts to document the dev branch updates similar to the early-adapter documentation.

---

---
title: Repositories 
description: The ForgeOps project provides two public GitHub repositories; the forgeops and forgeops-extras repositories.
component: forgeops
version: 2026.2
page_id: forgeops:start:repositories
canonical_url: https://docs.pingidentity.com/forgeops/2026.2/start/repositories.html
llms_txt: https://docs.pingidentity.com/forgeops/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["forgeops Repository", "forgeops-extras"]
section_ids:
  forgeops_repository: forgeops repository
  forgeops-updates: forgeops repository updates
  forgeops-reference: forgeops repository reference
  directories: Directories
  bin: bin
  charts: charts
  cluster_removed: cluster removed
  docker: docker
  etc: etc
  helm: helm
  how_tos: how-tos
  intezer: intezer
  jenkins_scripts: jenkins-scripts
  kustomize: kustomize
  legacy_docs: legacy-docs
  lib: lib
  releases_removed: releases removed
  upgrade: upgrade
  files_in_the_top_level_directory: Files in the top-level directory
  gcloudignore_gitchangelog_rc_gitignore_forgeops_conf_example: .gcloudignore, .gitchangelog.rc, .gitignore, forgeops.conf.example
  changelog_md: CHANGELOG.md
  license: LICENSE
  makefile: Makefile
  notifications_json: notifications.json
  readme_md: README.md
  forgeops_extras_repository: forgeops-extras repository
  forgeops-extras-reference: forgeops-extras repository reference
  directories_2: Directories
  terraform: terraform
  forgeops-fork: Git clone or Git fork?
---

# Repositories

The ForgeOps project provides two public GitHub repositories; the `forgeops` and `forgeops-extras` repositories.

This page provides a high-level overview of the two repositories.

## `forgeops` repository

The [`forgeops` repository](https://github.com/ForgeRock/forgeops.git) contains files needed for customizing and deploying the Ping Advanced Identity Software on a Kubernetes cluster:

* Files used to build Docker images for the Ping Advanced Identity Software:

  * Dockerfiles

  * Scripts and configuration files incorporated into ForgeOps-provided Docker images

  * Canonical configuration profiles for the platform

* Helm charts

* Kustomize bases and overlays

In addition, the repository contains utility scripts and sample files. The scripts and samples are useful for:

* Performing ForgeOps deployments quickly and easily

* Exploring monitoring, alerts, and security customization

Learn more about the files in the repository, recommendations about how to work with them, and the support status for the files in the [`forgeops` repository reference](#forgeops-reference).

|   |                                                                                                                                                                                                                                                              |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | Learn more about configuring GitHub notifications [here](https://docs.github.com/en/account-and-profile/managing-subscriptions-and-notifications-on-github/setting-up-notifications/configuring-notifications) so you can get notified on ForgeOps releases. |

### `forgeops` repository updates

New `forgeops` repository features become available in the `2026.2.1` tag of the `main` branch from time to time.

When you start working with the `forgeops` repository, clone the repository. Depending on your organization's setup, you'll clone the repository either from the public repository on GitHub, or from a fork. You can find more information in [Git clone or Git fork?](#forgeops-fork).

Then, check out the `2026.2.1` tag and create a working branch. For example:

```
$ git checkout 2026.2.1
$ git checkout -b my-working-branch
```

The ForgeOps team recommends that you regularly incorporate updates to the `2026.2.1` tag into your working branch:

1. [Get emails or subscribe to the ForgeOps RSS feed](../rn/rn.html) to be notified when there have been updates to ForgeOps 2026.2.1.

2. Pull new commits in the `2026.2.1` tag from the repository into your `2026.2.1` clone.

3. Rebase the commits from the new branch into your working branch in your `forgeops` repository clone.

It's important to understand the impact of rebasing changes from the `forgeops` repository into your branches. [`forgeops` repository reference](#forgeops-reference) provides advice about which files in the `forgeops` repository to change, which files not to change, and what to look out for when you rebase. Follow the advice in [`forgeops` repository reference](#forgeops-reference) to reduce merge conflicts, and to better understand how to resolve them when you rebase your working branch with updates that the ForgeOps team has made to the `2026.2.1` tag of the `main` branch.

### `forgeops` repository reference

For more information about support for the `forgeops` repository, see [Support for ForgeOps](support.html).

#### Directories

##### bin

Example scripts you can use or model for a variety of deployment tasks.

Recommendation: Don't modify the files in this directory. If you want to add your own scripts to the `forgeops` repository, create a subdirectory under bin, and store your scripts there.

Support Status: Sample files. [Not supported by Ping Identity.](support.html#commercial-support)

##### charts

Helm charts.

Recommendation: Don't modify the files in this directory. If you want to update a values.yaml file, create your deployment environment using the forgeops env command, and edit values.yaml files in the new environment you created. Learn more in the [`forgeops env` command reference](../reference/forgeops-cmd-ref.html#forgeops-env).

Support Status: [Supported is available from Ping Identity.](support.html#commercial-support)

##### cluster removed

The required ForgeOps contents in this directory have been moved to other directories as relevant and this directory has been removed.

##### docker

Contains three types of files needed to build Docker images for the Ping Advanced Identity Software: Dockerfiles, support files that go into Docker images, and configuration profiles.

**Dockerfile**

Common deployment customizations require modifications to the Dockerfile in the docker directory.

Recommendation: Expect to encounter merge conflicts when you rebase changes from ForgeOps into your branches. Be sure to track changes you've made to Dockerfiles, so that you're prepared to resolve merge conflicts after a rebase.

Support Status: Dockerfiles. [Support is available from Ping Identity.](support.html#commercial-support)

**Support Files Referenced by Dockerfiles**

When customizing the default ForgeOps deployments, you might need to add files to the docker directory. For example, to customize the AM WAR file, you might need to add plugin JAR files, user interface customization files, or image files.

Recommendation: If you only add new files to the docker directory, you should not encounter merge conflicts when you rebase changes from ForgeOps into your branches. However, if you need to modify any files from ForgeOps, you might encounter merge conflicts. Be sure to track changes you've made to any files in the docker directory, so that you're prepared to resolve merge conflicts after a rebase.

Support Status:

Scripts and other files from ForgeOps that are incorporated into Docker images for the Ping Advanced Identity Software: [Support is available from Ping Identity.](support.html#commercial-support)

User customizations that are incorporated into custom Docker images for the Ping Advanced Identity Software: [Support is not available from Ping Identity.](support.html#commercial-support)

**Configuration Profiles**

The starter configuration profiles provided with ForgeOps. To create your own configuration profiles, use the forgeops config command in your ForgeOps deployment environment. Add your own configuration profiles to the docker directory using the export command. Don't modify the internal-use only `idm-only` and `ig-only` configuration profiles provided by ForgeOps.

Recommendation: You should not encounter merge conflicts when you rebase changes from ForgeOps into your branches.

Support Status: Configuration profiles. [Support is available from Ping Identity.](support.html#commercial-support)

##### etc

Files used to support ForgeOps deployments.

Recommendation: Don't modify the files in this directory (or its subdirectories).

Support Status: Sample files. [Not supported by Ping Identity.](support.html#commercial-support)

##### helm

Helm values files for each client environment (env) for use with Helm charts. The Helm values files are created and managed by the forgeops env command.

**Files in each ForgeOps deployment environment**

| File                  | Description                                                            |
| --------------------- | ---------------------------------------------------------------------- |
| `env.log`             | Log of `forgeops env` runs.                                            |
| `values.yaml`         | Configuration of components in ForgeOps deployment using Helm.         |
| `values-images.yaml`  | Docker image used in ForgeOps deployment.                              |
| `values-ingress.yaml` | Ingress configuration, such as FQDN.                                   |
| `values-size.yaml`    | Component size information such as number of replicas, cpu, and memory |

Support Status: Environment specific files. [Support is available from Ping Identity.](support.html#commercial-support)

##### how-tos

Description and usage of various utilities provided with ForgeOps.

Recommendation: Don't change these files.

Support Status: Description files. [Support is available from Ping Identity.](support.html#commercial-support)

##### intezer

For ForgeOps internal use only. Don't modify or use.

##### jenkins-scripts

For ForgeOps internal use only. Don't modify or use.

##### kustomize

Artifacts for orchestrating the Ping Advanced Identity Software using Kustomize.

Recommendation: Common deployment customizations, such as changing the deployment namespace and providing a customized FQDN, require modifications to files in the kustomize/overlay directory. Be sure to track changes you've made to the files in the kustomize directory, so that you're prepared to resolve merge conflicts after a rebase.

Support Status: Kustomize bases and overlays. [Support is available from Ping Identity.](support.html#commercial-support)

##### legacy-docs

Documentation for performing ForgeOps deployments using older versions. Includes documentation for supported and deprecated versions of the `forgeops` repository.

Recommendation: Don't modify the files in this directory.

Support Status:

Documentation for supported versions of the `forgeops` repository: [Support is available from Ping Identity.](support.html#commercial-support)

Documentation for deprecated versions of the `forgeops` repository: [Not supported by Ping Identity.](support.html#commercial-support)

##### lib

Python and shell library files used internally. Don't modify.

##### releases removed

##### upgrade

For ForgeOps internal use only. Don't modify.

#### Files in the top-level directory

##### .gcloudignore, .gitchangelog.rc, .gitignore, forgeops.conf.example

For ForgeOps internal use only. Don't modify.

##### CHANGELOG.md

This file records changes in ForgeOps artifacts, processes, and procedures.

Recommendation: Don't modify this file.

##### LICENSE

Software license for artifacts in the `forgeops` repository. Don't modify.

##### Makefile

For ForgeOps internal use only. Don't modify.

##### notifications.json

For ForgeOps internal use only. Don't modify.

##### README.md

The top-level `forgeops` repository README file. Don't modify.

## `forgeops-extras` repository

Use the [forgeops-extras](https://github.com/ForgeRock/forgeops-extras) repository to create sample Kubernetes clusters in which you can deploy the Ping Advanced Identity Software.

### `forgeops-extras` repository reference

For more information about support for the `forgeops-extras` repository, see [Support for ForgeOps](support.html).

#### Directories

##### terraform

Example Terraform artifacts that automate cluster creation and deletion.

Recommendation: Don't modify the files in this directory. If you want to add your own cluster creation support files to the `forgeops` repository, copy the terraform.tfvars file to a new file and make changes there.

Support Status: Sample files. [Not supported by Ping Identity.](support.html#commercial-support)

## Git clone or Git fork?

For the simplest use cases—a single user performing a proof of concept, or exploration of the platform—cloning the ForgeOps public repositories from GitHub provides a quick and adequate way to access the repositories.

If, however, your use case is more complex, you might want to fork the repositories, and use the forks as your common upstream repositories. For example:

* Multiple users in your organization need to access a common version of the repository and share changes made by other users.

* Your organization plans to incorporate `forgeops` and `forgeops-extras` repository changes from ForgeOps.

* Your organization wants to use pull requests when making repository updates.

If you've forked the `forgeops` and `forgeops-extras` repositories:

* You'll need to synchronize your forks with ForgeOps repositories on GitHub when ForgeOps releases new branches.

* Your users will need to clone your forks before they start working instead of cloning the public repositories from GitHub. Because procedures in the documentation tell users to clone the public repositories, you'll need to make sure your users follow different procedures to clone the forks instead.

* The steps to initially get and update your repository clones will differ from the steps provided in the documentation. You'll need to let users know how to work with the forks as the upstream repositories instead of following the steps in the documentation.

---

---
title: Start here
description: Ping Identity provides several resources to help you get started in the cloud. These resources demonstrate how to deploy the Ping Advanced Identity Software on Kubernetes. Before you proceed, review the following precautions:
component: forgeops
version: 2026.2
page_id: forgeops:start:start-here
canonical_url: https://docs.pingidentity.com/forgeops/2026.2/start/start-here.html
llms_txt: https://docs.pingidentity.com/forgeops/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["CDK", "CDM", "Certificates", "SSL/TLS", "Load Testing", "Backup &amp; Restore", "Docker"]
section_ids:
  cdm-sandbox: Try an out-of-the-box ForgeOps deployment
  build-own-service: Build your own service
  planning: Create a project plan
  configure-platform: Configure the platform
  configure-cluster: Configure your cluster
  stay_up_and_running: Stay up and running
---

# Start here

Ping Identity provides several resources to help you get started in the cloud. These resources demonstrate how to deploy the Ping Advanced Identity Software on Kubernetes. Before you proceed, review the following precautions:

* Deploying Ping Advanced Identity Software in a containerized environment requires advanced proficiency in many technologies. Learn more about the required skills in [Assess Your Skill Level](start-here-skills.html).

* If you don't have experience with complex Kubernetes deployments, then either engage a certified Ping Advanced Identity Software consulting partner or deploy the platform on traditional architecture.

* Don't deploy Ping Advanced Identity Software in Kubernetes in production until you've successfully deployed and tested the software in a non-production Kubernetes environment.

Learn more about getting support for Ping Advanced Identity Software in [Support for ForgeOps](support.html).

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | Ping Identity only offers its software or services to legal entities that have entered into a binding license agreement with Ping Identity. When you install Docker images provided by ForgeOps, you agree either that: 1) you are an authorized user of a Ping Advanced Identity Software customer that has entered into a license agreement with Ping Identity governing your use of the Ping Identity software; or 2) your use of the Ping Advanced Identity Software is subject to the [Ping Identity Subscription Agreements](https://www.pingidentity.com/en/legal/subscription-agreement.html). |

## Try an out-of-the-box ForgeOps deployment

Before you start planning a production deployment, perform a ForgeOps deployment without any customizations. If you're new to Kubernetes, or new to the Ping Advanced Identity Software, it's a great way to learn, and you'll have a sandbox suitable for exploring the Ping Advanced Identity Software in a cloud environment.

![Illustrates major tasks when performing a ForgeOps deployment.](_images/start-cdm.png)

Perform a ForgeOps deployment on Google Cloud, AWS, or Microsoft Azure to quickly spin up the platform for demonstration purposes. You'll get a feel for what it's like to deploy the platform on a Kubernetes cluster in the cloud. When you're done, you'll have a robust starter deployment that you can use to test deployment customizations that you'll need for your production environment. Examples of deployment customizations include, but are not limited to:

* Running lightweight benchmark tests

* Making backups of data and restoring the data

* Securing TLS with a certificate that's dynamically obtained from Let's Encrypt

* Using an ingress controller other than Traefik

* Resizing the cluster to meet your business requirements

* Configuring Alert Manager to issue alerts when usage thresholds have been reached

Prerequisite technologies and skills:

* [Git](start-here-skills.html#skills-git)

* [Google Cloud, AWS, or Azure](start-here-skills.html#skills-cdm-cloud-provider)

* [Kubernetes, running on Google Cloud, AWS, or Azure](start-here-skills.html#skills-cdk-kubernetes)

More information:

* [Setup overview](../setup/overview.html)

## Build your own service

![Illustrates the major tasks performed when building a production deployment of ${platform.name} in the cloud.](_images/dg-start-overview.png)

Perform the following activities to customize, deploy, and maintain a production Ping Advanced Identity Software implementation in the cloud:

### Create a project plan

![Illustrates the major tasks performed when planning a production deployment of ${platform.name} in the cloud.](_images/start-plan.png)

After you've spent some time [exploring a ForgeOps deployment](#cdm-sandbox), you're ready to define requirements for your production deployment. *Remember, an out-of-the-box ForgeOps deployment is not a production deployment*. Use out-of-the-box ForgeOps deployments to explore deployment customizations. Then, incorporate the lessons you've learned as you build your own production service.

Analyze your business requirements and define how the Ping Advanced Identity Software needs to be configured to meet your needs. Identify systems to be integrated with the platform, such as identity databases and applications, and plan to perform those integrations. Assess and specify your deployment infrastructure requirements, such as backup, system monitoring, Git repository management, CI/CD, quality assurance, security, and load testing.

Be sure to do the following when you transition to a production environment:

* Obtain and use certificates from an established certificate authority.

* Create and test your backup plan.

* Use a working production-ready FQDN.

* Implement monitoring and alerting utilities.

Prerequisite technologies and skills:

* [Project planning and management](start-here-skills.html#skills-proj-plan)

* [Git](start-here-skills.html#skills-git)

* [Docker](start-here-skills.html#skills-docker)

* [Google Cloud, AWS, or Azure](start-here-skills.html#skills-prod-cloud-provider)

* [Kubernetes, running on Google Cloud, AWS, or Azure](start-here-skills.html#skills-prod-kubernetes)

* [Ping Advanced Identity Software](start-here-skills.html#skills-platform)

* [Applications and databases that you plan to integrate with Ping Advanced Identity Software](start-here-skills.html#skills-integration)

* [CI/CD for a production deployment in the cloud](start-here-skills.html#skills-cicd)

* [Integration testing](start-here-skills.html#skills-integration-test)

* [Deployment hardening and security](start-here-skills.html#skills-security)

* [Benchmarking and load testing](start-here-skills.html#skills-benchmarking)

* [Site reliability](start-here-skills.html#skills-sr)

More information:

* [All the ForgeOps documentation](../index.html)

### Configure the platform

![Illustrates the major tasks performed to configure the ${platform.name} before deploying in production.](_images/start-config-platform.png)

With your [project plan defined](#planning), you're ready to configure the Ping Advanced Identity Software to meet the plan's requirements. Install single-instance ForgeOps deployments on your developers' computers. Configure AM and IDM. If needed, include integrations with external applications in the configuration. Iteratively unit test your configuration as you modify it. Build customized Docker images that contain the configuration.

Prerequisite technologies and skills:

* [Ping Advanced Identity Software](start-here-skills.html#skills-platform)

* [Git](start-here-skills.html#skills-git)

* [Kubernetes, running on Google Cloud, AWS, or Azure](start-here-skills.html#skills-prod-kubernetes)

* [Docker](start-here-skills.html#skills-docker)

More information:

* [Customization overview](../customize/overview.html)

### Configure your cluster

![Illustrates the major tasks performed to configure the cluster before deploying in production.](_images/start-config-cluster.png)

With your [project plan defined](#planning), you're ready to configure a Kubernetes cluster that meets the requirements defined in the plan. Install the platform using the customized Docker images developed in [Configure the platform](#configure-platform). Provision the identity repository with users, groups, and other identity data. Load test your deployment, and then size your cluster to meet service level agreements. Perform integration tests. Harden your deployment. Set up CI/CD for your deployment. Create monitoring alerts so that your site reliability engineers are notified when the system reaches thresholds that affect your SLAs. Implement database backup and test database restore. Simulate failures while under load to make sure your deployment can handle them.

Prerequisite technologies and skills:

* [Google Cloud, AWS, or Azure](start-here-skills.html#skills-prod-cloud-provider)

* [Git](start-here-skills.html#skills-git)

* [Kubernetes, running on Google Cloud, AWS, or Azure](start-here-skills.html#skills-prod-kubernetes)

* [Ping Advanced Identity Software](start-here-skills.html#skills-platform)

* [CI/CD for a production deployment in the cloud](start-here-skills.html#skills-cicd)

* [Integration testing](start-here-skills.html#skills-integration-test)

* [Deployment hardening and security](start-here-skills.html#skills-security)

* [Kubernetes backup and restore](start-here-skills.html#skills-kubernetes-backup)

* [Benchmarking and load testing](start-here-skills.html#skills-benchmarking)

* [Site reliability](start-here-skills.html#skills-sr)

More information:

* [Prepare to deploy in production](../prepare/overview.html)

* [Setup overview](../setup/overview.html)

### Stay up and running

![Illustrates the major tasks performed to keep a ${platform.name} deployment up and running in production.](_images/start-sr.png)

By now, you've [configured the platform](#configure-platform), [configured a Kubernetes cluster](#configure-cluster), and deployed the platform with your customized configuration. Run your Ping Advanced Identity Software deployment in your cluster, continually monitoring it for performance and reliability. Take backups as needed.

Prerequisite technologies and skills:

* [Git](start-here-skills.html#skills-git)

* [Google Cloud, AWS, or Azure](start-here-skills.html#skills-prod-cloud-provider)

* [Kubernetes, running on Google Cloud, AWS, or Azure](start-here-skills.html#skills-prod-kubernetes)

* [Ping Advanced Identity Software](start-here-skills.html#skills-platform)

* [CI/CD for a production deployment in the cloud](start-here-skills.html#skills-cicd)

* [Kubernetes backup and restore](start-here-skills.html#skills-kubernetes-backup)

* [Site reliability](start-here-skills.html#skills-sr)

More information:

* [Prepare to deploy in production](../prepare/overview.html)

---

---
title: Support for ForgeOps
description: This appendix contains information about support options for ForgeOps deployments and the Ping Advanced Identity Software.
component: forgeops
version: 2026.2
page_id: forgeops:start:support
canonical_url: https://docs.pingidentity.com/forgeops/2026.2/start/support.html
llms_txt: https://docs.pingidentity.com/forgeops/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["ForgeOps Support", "Ping Support", "Kubernetes", "Google Cloud", "AWS", "Azure", "forgeops Repository", "forgeops-extras Repository"]
section_ids:
  forgeops_support: ForgeOps support
  life-cycle: ForgeOps lifecycle policy
  forgeops-life-policy: ForgeOps product support lifecycle policy
  forgeops-image-support: Support for ForgeOps-provided images
  licensing: Licensing
  commercial-support: Support
  support-limitations: Support limitations
  kubernetes-services: Third-party Kubernetes services
  documentation_access: Documentation access
  problem_reports_and_information_requests: Problem reports and information requests
  suggestions_for_fixes_and_enhancements_to_artifacts: Suggestions for fixes and enhancements to artifacts
  contact_information: Contact information
---

# Support for ForgeOps

This appendix contains information about support options for ForgeOps deployments and the Ping Advanced Identity Software.

## ForgeOps support

The Ping Identity ForgeOps team has developed artifacts in the [forgeops](https://github.com/ForgeRock/forgeops/tree/2026.2.1) and [forgeops-extras](https://github.com/ForgeRock/forgeops-extras) Git repositories for deploying the Ping Advanced Identity Software in the cloud. The companion [ForgeOps documentation](../index.html) provides examples to help you get started.

These artifacts and documentation are provided on an as-is basis. Ping Identity doesn't guarantee the individual success developers may have in implementing the code on their development platforms or in production configurations.

### ForgeOps lifecycle policy

When a Ping Advanced Identity Software product has been deployed using ForgeOps, the product support lifecycle policy and timeline that applies to that product continues to apply regardless of the deployment type. These support policies relate to the Ping Advanced Identity Software product only and not the underlying container operating system. Therefore, refer to the support lifecycle policy for the relevant Ping Advanced Identity Software product support lifecycle:

* [Support lifecycle policy for PingAM, PingDS, PingIDM, and IGA](https://support.pingidentity.com/s/article/Ping-Identity-Product-Support-Lifecycle-Policy-PingAM-PingDS-PingIDM-and-IGA).

* [Support lifecycle policy for PingGateway and Agents](https://support.pingidentity.com/s/article/Ping-Identity-Product-Support-Lifecycle-Policy-PingGateway-and-Agents).

The support for the underlying container operating system is covered by the [ForgeOps product support lifecycle policy](#forgeops-life-policy).

#### ForgeOps product support lifecycle policy

ForgeOps product support lifecycle policy refers to the versions of the Ping Advanced Identity Software products that are supported by ForgeOps in ForgeOps version 2025.1 and later. ForgeOps will provide support for the last 3 minor or major versions of the Ping Advanced Identity Software products.

* Supported

  ForgeOps will continue to deliver supported images for the latest available patch version of the platform product. For example, if versions 7.5.0 and 7.5.1 are available, ForgeOps provides scanned and patched images only for 7.5.1. These patched images deal with OS level vulnerabilities only and not the Ping Advanced Identity Software products. With the availability of 8.1 images, ForgeOps supports 8.1, 8.0, and 7.5 versions of the platform images, and **7.4 images are no longer supported**.

* Maintained

  ForgeOps tooling continues to have access to the last three versions of the Ping Advanced Identity Software products whether it's supported or not.

  | Version | Release Date | Lifecycle Stage | Supported?                          | Maintained?                         | EOS Start Date |
  | ------- | ------------ | --------------- | ----------------------------------- | ----------------------------------- | -------------- |
  | 8.1     | Apr 21, 2026 | Active          | [icon: check-circle, set=fa]**Yes** | [icon: check-circle, set=fa]**Yes** |                |
  | 8.0     | Apr 7, 2025  | Active          | [icon: check-circle, set=fa]**Yes** | [icon: check-circle, set=fa]**Yes** |                |
  | 7.5     | Apr 2, 2024  | Active          | [icon: check-circle, set=fa]**Yes** | [icon: check-circle, set=fa]**Yes** |                |
  | 7.4     | Oct 9, 2023  | Active          | [icon: times-circle, set=fa]**No**  | [icon: check-circle, set=fa]**Yes** |                |

#### Support for ForgeOps-provided images

ForgeOps supports the latest ForgeOps-provided image for each major or minor version of the supported Ping Advanced Identity Software component. ForgeOps support is limited to ForgeOps-provided image lines. Customers should therefore plan to use the newest published ForgeOps image in a supported version stream, rather than expect vulnerability fixes to be backported to older patch images.

The ForgeOps team scans daily for critical and high severity vulnerabilities in the latest published image for each supported minor version. The team then publishes a new image when upstream fixes are available that can be applied within the currently supported base operating system version. If a vulnerability fix requires moving to a newer operating system version, the change isn't applied in place on the existing image line. Instead, the fix is applied in the next major or minor version of the image, and is made available in the product team's next release, according to that product's release cycle and support commitments.

If your corporate compliance mandates a zero known Common Vulnerabilities and Exposures (zero-CVE) footprint or immediate remediation SLAs that differ from Ping's product lifecycle, you should consider building and managing your own base images, as documented in [Base Docker images](../reference/base-docker-images.html). This gives you more direct control over base image selection, update timing, and remediation policy.

### Licensing

Ping Identity only offers its software or services to legal entities that have entered into a binding license agreement with Ping Identity. When you install Docker images provided by ForgeOps, you agree either that: 1) you are an authorized user of a Ping Advanced Identity Software customer that has entered into a license agreement with Ping Identity governing your use of the Ping Identity software; or 2) your use of the Ping Advanced Identity Software is subject to the [Ping Identity Subscription Agreements](https://www.pingidentity.com/en/legal/subscription-agreement.html).

### Support

Ping Identity provides support for the following resources:

* Docker images provided by the ForgeOps team.

* Artifacts in the [forgeops](https://github.com/ForgeRock/forgeops/tree/2026.2.1) Git repository:

  * Files used to build Docker images for the Ping Advanced Identity Software:

    * Dockerfiles

    * Scripts and configuration files incorporated into the Docker images provided by ForgeOps

    * Canonical configuration profiles for the platform

  * Helm charts

  * Kustomize bases and overlays

* [ForgeOps Documentation](../index.html)

For more information about support for specific directories and files in the `forgeops` repository, refer to the [`forgeops` repository reference](repositories.html#forgeops-reference).

Ping Identity provides support for the Ping Advanced Identity Software. For supported components, containers, and Java versions, refer to the following:

* [PingAM Release Notes](https://docs.pingidentity.com/pingam//release-notes/preface.html)

* [PingIDM Release Notes](https://docs.pingidentity.com/pingidm/8.1/release-notes/preface.html)

* [PingDS Release Notes](https://docs.pingidentity.com/pingds//release-notes/preface.html)

* [PingGateway Release Notes](https://docs.pingidentity.com/pinggateway//release-notes/preface.html)

### Support limitations

Ping Identity provides no support for the following:

* Artifacts in the [forgeops-extras](https://github.com/ForgeRock/forgeops-extras) repository. For more information about support for specific directories and files in the `forgeops-extras` repository, refer to the [`forgeops-extras` repository reference](repositories.html#forgeops-extras-reference).

* Artifacts other than Dockerfiles, Helm charts, Kustomize bases, and Kustomize overlays in the [forgeops](https://github.com/ForgeRock/forgeops/tree/2026.2.1) Git repository. Examples include scripts, example configurations, and so forth.

* Infrastructure outside Ping Identity. Examples include Docker, Kubernetes, Google Cloud Platform, Amazon Web Services, Microsoft Azure, and so forth.

* Software outside Ping Identity. Examples include Java, Apache Tomcat, Traefik, Apache HTTP Server, Certificate Manager, Prometheus, and so forth.

* Deployments that deviate from the [published ForgeOps architecture](../deploy/architecture.html). Deployments that do not include the following architectural features are not supported:

  * PingAM and PingIDM are integrated and deployed together in a Kubernetes cluster.

  * PingIDM login is integrated with PingAM.

  * PingAM uses PingDS as its data repository.

  * PingIDM uses PingDS as its repository.

* Ping Identity publishes Docker images for testing and development. For production deployments, it is recommended that customers build and run containers using a [supported operating system](https://support.pingidentity.com/s/article/What-operating-systems-are-PingAM-PingDS-PingIDM-and-PingGateway-supported-on), required software dependencies, and their customized platform component configurations.

### Third-party Kubernetes services

The ForgeOps reference tools are provided for use with Google Kubernetes Engine, Amazon Elastic Kubernetes Service, and Microsoft Azure Kubernetes Service.

Ping Identity supports running the platform on other Kubernetes platforms such as IBM RedHat OpenShift. However, ForgeOps reference tools are not provided on these platforms, and customers must build, maintain, and support their own tools and configurations.

Ping Identity doesn't support Kubernetes itself. Customers must have a support contract in place with their Kubernetes vendor to resolve infrastructure issues. To avoid any misunderstandings, it must be clear that Ping Identity cannot troubleshoot underlying Kubernetes issues.

Modifications to ForgeOps deployment assets may be required to adapt the platform to the customer's Kubernetes implementation. For example, ingress routes, storage classes, NAT gateways, etc., might need to be modified. Making the modifications requires competency in Kubernetes and familiarity with their chosen distribution.

## Documentation access

Ping Identity publishes comprehensive documentation online:

* The [Knowledge Base](https://support.pingidentity.com/s/knowledge-base) offers a large and increasing number of up-to-date, practical articles that help you deploy and manage Ping Advanced Identity Software.

  While many articles are visible to community members, Ping Identity customers have access to much more, including advanced information for customers using Ping Advanced Identity Software in a mission-critical capacity.

* The developer documentation, such as this site, aims to be technically accurate with respect to the sample that is documented. It is visible to everyone.

## Problem reports and information requests

If you are a named customer Support Contact, contact Ping Identity using the [Customer Support Portal](https://support.pingidentity.com/s/) to request information or report a problem with Dockerfiles, Helm charts, Kustomize bases, or Kustomize overlays in the `forgeops` repository.

When requesting help with a problem, include the following information:

* Description of the problem, including when the problem occurs and its impact on your operation.

* Steps to reproduce the problem.

  If the problem occurs on a Kubernetes system other than minikube, GKE, EKS, or AKS, we might ask you to reproduce the problem on one of those.

* HTML output from the debug-logs command. For more information, refer to [Kubernetes logs and other diagnostics](../troubleshoot/pods.html).

## Suggestions for fixes and enhancements to artifacts

ForgeOps greatly appreciates suggestions for fixes and enhancements to ForgeOps-provided artifacts in the [forgeops](https://github.com/ForgeRock/forgeops/tree/2026.2.1) and [forgeops-extras](https://github.com/ForgeRock/forgeops-extras) repositories.

If you would like to report a problem with or make an enhancement request for an artifact in either repository, create a GitHub issue in the repository.

## Contact information

Ping Identity provides support services, professional services, training through Ping Identity training, and partner services to assist you in setting up and maintaining your deployments. For a general overview of these services, refer to <https://www.pingidentity.com/en/platform.html>.

Ping Identity has staff members around the globe who support our international customers and partners. Learn more about Ping Identity's support offering, including support plans and service-level agreements (SLAs) in the [Ping Advanced Identity Software support page](https://support.pingidentity.com/s/).

---

---
title: Third-party software
description: Before performing a ForgeOps deployment, install the requisite third-party software on your local computer.
component: forgeops
version: 2026.2
page_id: forgeops:start:3rd-party
canonical_url: https://docs.pingidentity.com/forgeops/2026.2/start/3rd-party.html
llms_txt: https://docs.pingidentity.com/forgeops/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  required_third_party_software: Required third-party software
---

# Third-party software

Before performing a ForgeOps deployment, install the requisite third-party software on your local computer.

The ForgeOps team recommends you install third-party software using [Homebrew](https://brew.sh/) on macOS and Linux'\[[1](#_footnotedef_1 "View footnote.")]' .

## Required third-party software

|                                         |         |                                                             |
| --------------------------------------- | ------- | ----------------------------------------------------------- |
| Software                                | Version | Homebrew package                                            |
| **On all platforms**                    |         |                                                             |
| * Python 3                              | 3.14.5  | `python@3`                                                  |
| - Bash                                  | 5.3.9   | `bash`                                                      |
| * Docker client                         | 28.4.0  | `docker`                                                    |
| - Kubernetes client (kubectl)           | 1.36.1  | `kubernetes-cli`                                            |
| * Kubernetes context switcher (kubectx) | 0.11.0  | `kubectx`                                                   |
| - Kustomize                             | 5.8.1   | `kustomize`                                                 |
| * Helm                                  | 4.2.0   | `helm`                                                      |
| - JSON processor jq                     | 1.8.1   | `jq`                                                        |
| * Setup tools (Python)                  | 82.0.1  | `python-setuptools`                                         |
| - Terraform                             | 1.12.2  | `terraform`                                                 |
| **Additionally on Google GKE**          |         |                                                             |
| * Google Cloud SDK                      | 569.0.0 | `gcloud-cli` (cask)\[[1](#_footnotedef_1 "View footnote.")] |
| **Additionally on Amazon EKS**          |         |                                                             |
| - Amazon AWS Command-line Interface     | 2.34.50 | `awscli`                                                    |
| * AWS IAM Authenticator for Kubernetes  | 0.7.16  | `aws-iam-authenticator`                                     |
| **Additionally on Azure AKS**           |         |                                                             |
| - Azure Command-line Interface          | 2.86.0  | `azure-cli`                                                 |
| **Additionally on minikube**            |         |                                                             |
| * minikube                              | 1.38.1  | `minikube`                                                  |

***

[1](#_footnoteref_1). The Linux version of Homebrew doesn't support installing software it maintains as casks. Because of this, if you're setting up an environment on Linux, you won't be able to use Homebrew to install software in several cases. You'll need to refer to the software's documentation for information about how to install the software on a Linux system.

---

---
title: What&#8217;s new in ForgeOps 2026.2
description: The ForgeOps early adapter artifacts have been moved from the dev branch to the main branch of the ForgeOps repository. The main branch will be the default branch for the ForgeOps repository.
component: forgeops
version: 2026.2
page_id: forgeops:start:whats-new
canonical_url: https://docs.pingidentity.com/forgeops/2026.2/start/whats-new.html
llms_txt: https://docs.pingidentity.com/forgeops/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  release_information: Release information
  highlights_in_2026_2_1_release: Highlights in 2026.2.1 release
---

# What's new in ForgeOps 2026.2

## Release information

### Highlights in 2026.2.1 release

* The `main` branch contains pre-release artifacts

  The ForgeOps early adapter artifacts have been moved from the `dev` branch to the `main` branch of the [ForgeOps repository](https://github.com/ForgeRock/forgeops). The `main` branch will be the default branch for the ForgeOps repository.

  Note that the pre-release artifacts in the `main` branch are not meant for production use and are only meant for testing and providing feedback on the new features and changes.

  The `dev` branch that used to contain the pre-release artifacts is discontinued and will no longer be updated.

* Focus more on using Helm 4

  The `forgeops` utility now uses Helm 4 for deploying ForgeOps on Kubernetes. Helm 4 provides improved performance and security features compared to previous Helm versions. We recommend you use Helm in ForgeOps deployments rather than Kustomize.

* Security enabled by default

  The `forgeops` utility now enables security by default for new ForgeOps deployments. Learn more in [Enable security features](../rn/rn.html#sec-2026-2-features).

* SBOM for ForgeOps images

  Software Bill of Materials (SBOM) is now available for ForgeOps images. SBOM provides a detailed inventory of the components and dependencies used in ForgeOps images, which can help you identify and manage security vulnerabilities and compliance issues.

* Images support update

  ForgeOps supports the latest available major or minor versions of the Ping Advanced Identity Software components. Learn more at [ForgeOps image support](support.html#forgeops-image-support).

* Further release information

  Learn more about this release in the [ForgeOps 2026.2.1 release notes](../rn/rn.html#forgeops-2026-2-1-features).