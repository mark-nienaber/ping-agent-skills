---
title: Docker Builds - Hooks
description: List the ordered lifecycle hook scripts called during a Ping Identity Docker image entrypoint for customizing server profiles
component: devops
page_id: devops::docker-builds/DOCKER_BUILDS_HOOKS
canonical_url: https://developer.pingidentity.com/devops/docker-builds/DOCKER_BUILDS_HOOKS.html
llms_txt: https://developer.pingidentity.com/devops/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  devops-hooks-details: Hooks Details
---

# Docker Builds - Hooks

**Audience** - Operators of DevOps Cloud environments. Not intended for Developers and admins of the Ping Identity products.

**Description** - This document describes the many number of scripts that are called in during the lifecycle of a Ping Identity docker image from the initial `entrypoint.sh` script.

Included with the base docker images, there is an example/stub provided for all possible hooks. It is **very important** that these names be used if a developer wishes to make subtle changes to their server-profile.

The full ordered list of scripts that are called depending on what type of image (i.e. pingdirectory or pingdatasync) are:

![DOCKER BUILDS HOOKS 1](../_images/DOCKER_BUILDS_HOOKS_1.png)

## Hooks Details

Details on hooks can be found within the code of each hook in the [Docker-Builds Repo](https://github.com/pingidentity/pingidentity-docker-builds) as well in `pingidentity-devops-getting-started/docs/docker-images/<image_name>/hooks` for each of the products images.

---

---
title: Docker Builds Repository Summary
description: Summarize the filesystem layout of the pingidentity-docker-builds GitHub repository, including directories for each product image
component: devops
page_id: devops::docker-builds/README
canonical_url: https://developer.pingidentity.com/devops/docker-builds/README.html
llms_txt: https://developer.pingidentity.com/devops/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  devops-filesystem-layout: Filesystem layout
  devops-non-image-related: Non-image related
  devops-image-directories: Image directories
---

# Docker Builds Repository Summary

|   |                                                                                                                                                                                            |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | This page only describes the repository structure for context and understanding. For instructions on using the repository to build an image, visit [this page](../how-to/buildLocal.html). |

In the [docker-builds](https://github.com/pingidentity/pingidentity-docker-builds) Github repository, we share our Dockerfiles and automation scripts used for building Ping product container images. You can use these scripts and supporting pieces found in the repository to build an image of your own locally. For example, you can use this process to build an image for an older version we no longer provide on Docker Hub.

The image build process at Ping uses the [Docker multi-stage build](https://docs.docker.com/build/building/multi-stage/) process. Every product image is a thin product layer added on top of a prebuilt parent image that Ping provides — `pingbase` or `pingbase-java` (see [Parent Images](../docker-images/pingbase/README.html)). The parent images bundle the base operating system and, for Java products, the JVM (BellSoft Liberica, JDK 17, 21, or 25 — 25 is the default). They are published to [Docker Hub](https://hub.docker.com/u/pingidentity/) with floating OS-major tags and are [signed with Cosign](https://devops.pingidentity.com/docker-images/imageSignatureVerification.html). Common scripts shared by all products live in the repository as plain build inputs and are copied into each image; there are no foundation or intermediate images to build.

As you explore the repository, you will find a directory for each product, each with a Dockerfile and supporting scripts that add the product layer on top of the parent image. The result is a complete product image for use in Kubernetes or another container orchestration environment, with a consistent structure across all products.

## Filesystem layout

The repository includes the following directories. This list is not comprehensive; it is focused on those folders of relevance to users:

### Non-image related

| Repository Directory | Description                                                                                             |
| -------------------- | ------------------------------------------------------------------------------------------------------- |
| ci_scripts           | Files and scripts used for building container images, both in an automated build pipeline and local use |

#### Image directories

| Repository Directory | Description                                                                                                                                              |
| -------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ldap-sdk-tools       | Files and scripts for an image with LDAP SDK tools available for use with Ping Directory                                                                 |
| runtime              | Plain build inputs (not an image): common runtime scaffold — entrypoint chain, hook framework, dependency installation — copied into every product image |
| legal                | Shared license text copied into every product image                                                                                                      |
| pingaccess           | Product-specific files and scripts for PingAccess container image                                                                                        |
| pingauthorize        | Product-specific files and scripts for PingAuthorize container image                                                                                     |
| pingauthorizepap     | Product-specific files and scripts for PingAuthorize Policy Editor container image                                                                       |
| pingcentral          | Product-specific files and scripts for PingCentral container image                                                                                       |
| pingdataconsole      | Product-specific files and scripts for Ping Data Console container image                                                                                 |
| pingdatasync         | Product-specific files and scripts for PingDataSync container image                                                                                      |
| pingdelegator        | Product-specific files and scripts for PingDelegator container image                                                                                     |
| pingdirectory        | Product-specific files and scripts for PingDirectory container image                                                                                     |
| pingdirectoryproxy   | Product-specific files and scripts for PingDirectory Proxy container image                                                                               |
| pingfederate         | Product-specific files and scripts for PingFederate container image                                                                                      |
| pingtoolkit          | Files and scripts for a utility image, typically used for an init or task-related container                                                              |