---
title: DevOps at Ping Identity
description: Summarize the Ping Identity DevOps program, including Docker images, deployment examples, and configuration management tools for containers
component: devops
page_id: devops::devops-landing-page
canonical_url: https://developer.pingidentity.com/devops/devops-landing-page.html
llms_txt: https://developer.pingidentity.com/devops/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  devops-benefits-from-this-program: Benefits from this program
  devops-resources: Resources
  devops-docker-images: Docker Images
  devops-deployment-examples: Deployment Examples
  devops-configuration-management: Configuration Management
  devops-other-resources: Other Resources
---

# DevOps at Ping Identity

This documentation exists to enable DevOps professionals, administrators, and developers to deploy Ping Identity software using container technologies. Our goal is to provide tools, frameworks, blueprints, and reference architectures in support of running our products in containerized environments.

* First time here? We recommend the [Get Started](get-started/introduction.html) page.

* New to Kubernetes? See [Kubernetes Basics](reference/k8sBasics.html).

* New to Helm? See [Helm Basics](reference/HelmBasics.html).

* Important information about [container logging](reference/containerLogging.html).

## Benefits from this program

* **Streamlined Deployments**

  Deploy and run workloads on our solutions without the need for additional hardware or virtual machines (VMs).

* **Consistent and Flexible**

  Maintain all configurations and dependencies, ensuring consistent environments. Containers are portable and can be used on nearly any machine.

* **Optimized Sizing**

  Orchestration of containers allows organizations to increase fault tolerance and availability and to better manage costs by auto-scaling to application demand.

## Resources

Resources provided include Docker images of Ping Identity products, deployment examples, and configuration management tools.

### Docker Images

|                                                                                                                                        |                                                                                                                                                                                  |
| -------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [![docker](_images/logos/docker.png)](https://hub.docker.com/u/pingidentity)[**Docker Images**](https://hub.docker.com/u/pingidentity) | [![github](_images/logos/github.png)](https://github.com/pingidentity/pingidentity-docker-builds)[**Docker Builds**](https://github.com/pingidentity/pingidentity-docker-builds) |

Ping provides preconfigured Docker images of our products for running as containers. Each of our containers is a complete working product instance that is immediately usable when deployed. Our Docker stacks are integrated collections of Ping products preconfigured to coordinate across all containers in the stack.

|   |                                                                             |
| - | --------------------------------------------------------------------------- |
|   | By default, our Docker images run as an unprivileged user in the container. |

You can find information about our available Docker images in the [pingidentity-docker-builds](https://github.com/pingidentity/pingidentity-docker-builds) repository on Github or on the [Docker Hub](https://hub.docker.com/u/pingidentity/) site. Included in this portal are detailed [image specifications](docker-images/dockerImagesRef.html) on variables, related images and so on.

The Docker images are automatically pulled from our repository the first time you deploy a product container or orchestrated set of containers. Alternatively, you can pull the images manually from our [Docker Hub](https://hub.docker.com/u/pingidentity/) site.

|   |                                                                                                                                                                                               |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Older images based on product versions that are no longer supported under our policy are removed from Docker Hub. See the [support policy page](docker-images/imageSupport.html) for details. |

### Deployment Examples

|                                                                                                                                                                                                    |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [![github](_images/logos/github.png)](https://github.com/pingidentity/pingidentity-devops-getting-started)[**DevOps Getting Started**](https://github.com/pingidentity/pingidentity-docker-builds) |

The Github repository linked here provides examples for deploying our products as standalone containers or as an orchestrated deployment in Kubernetes (using Helm).

Docker Compose is often used for development, demonstrations, and lightweight orchestration. Kubernetes is typically used for enterprise-level orchestration.

### Configuration Management

For configuration management, we use:

* Server profiles, providing initial runtime configuration when containers are started. Server profile configuration is pulled from a provided Git repository and applied to the server during container start up.

* Terraform, to manage runtime server configuration after containers have successfully started and server profiles have been successfully applied. Terraform can manage the ongoing state of configuration in a running service without the need for rolling restart.

* YAML files for runtime configuration of stacks. YAML file configuration settings complement those provided through server profiles.

* Environment variables. These can be included in YAML files or called from external files.

* Shell scripts (hooks) to automate certain operations for a product.

* Release tags to give you a choice between stable builds or the current (potentially unstable) builds.

More information about how server profiles, variables and these other options coordinate to configure the products can be found on the [Configuration Reference](reference/config.html) page.

## Other Resources

|                                                                                                                                                       |                                                                                                                       |                                                                                                                                                                       |
| ----------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [![github](_images/logos/github.png)](https://github.com/topics/ping-devops)[**All Ping DevOps Github Repos**](https://github.com/topics/ping-devops) | [![helm](_images/logos/helm.png)](https://helm.pingidentity.com)[**Ping Helm Charts**](https://helm.pingidentity.com) | [![terraform](_images/logos/terraform.png)](https://developer.pingidentity.com/terraform)[**Ping Terraform Providers**](https://developer.pingidentity.com/terraform) |