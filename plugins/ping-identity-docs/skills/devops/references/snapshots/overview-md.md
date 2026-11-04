---
title: Overview
description: Provide an overview of Ping Identity DevOps resources, including Docker images, deployment examples, and configuration management tools
component: devops
page_id: devops::overview
canonical_url: https://developer.pingidentity.com/devops/overview.html
llms_txt: https://developer.pingidentity.com/devops/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  devops-overview: Overview
  devops-devops-docker-images: DevOps Docker Images
  devops-deployment-examples: Deployment Examples
  devops-configuration-management: Configuration Management
---

# Overview

## Overview

The DevOps resources include Docker images of Ping Identity products, deployment examples, and configuration management tools.

When you're ready, begin with our [Get Started](get-started/introduction.html) guide. Our documentation will help set you up and familiarize you with the use of the resources.

### DevOps Docker Images

|                                                                              |                                                                              |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| [![docker](_images/logos/docker.png)](https://hub.docker.com/u/pingidentity) | [![github](_images/logos/github.png)](https://hub.docker.com/u/pingidentity) |

We make available preconfigured Docker images of our products in Docker containers. Each of our containers is a complete working product instance, immediately usable when deployed. Our Docker stacks are integrated collections of these containers, preconfigured to interoperate with the containers in the stack.

You can find information about our available Docker images in the [pingidentity-docker-builds](https://github.com/pingidentity/pingidentity-docker-builds) repository or on our [Docker Hub](https://hub.docker.com/u/pingidentity/) site.

The Docker images are automatically pulled from our repository the first time you deploy a product container or orchestrated set of containers. Alternatively, you can pull the images from our [Docker Hub](https://hub.docker.com/u/pingidentity/) site.

### Deployment Examples

|                                                                                                                            |
| -------------------------------------------------------------------------------------------------------------------------- |
| [![DevOps Getting Started](_images/logos/github.png)](https://github.com/pingidentity/pingidentity-devops-getting-started) |

We supply examples for deploying our products as standalone containers, as a Docker Compose stack, or as an orchestrated set using Kubernetes.

Use Docker Compose for development, demonstrations, and lightweight orchestration. Use Kubernetes for enterprise-level orchestration.

### Configuration Management

For configuration management, we use:

* Server profiles, for runtime configuration of containers.

* YAML files for runtime configuration of stacks. YAML file configuration settings complement that used for server profiles.

* Environment variables. These can be included in YAML files or called from external files.

* Shell scripts (hooks) to automate certain operations for a product.

* Release tags to give you a choice between stable builds or the current (potentially unstable) builds.

By default, our Docker images run as unprivileged within the container.