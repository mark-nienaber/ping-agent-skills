---
title: About custom images
description: Build custom Docker images for Ping Advanced Identity Software products configuration in development and production
component: forgeops
version: 2026.3
page_id: forgeops:customize:custom-images
canonical_url: https://docs.pingidentity.com/forgeops/2026.3/customize/custom-images.html
llms_txt: https://docs.pingidentity.com/forgeops/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-03-04T09:42:15Z
keywords: ["CDK", "Docker"]
section_ids:
  in_development: In development
  in_production: In production
  next_step: Next step
---

# About custom images

## In development

To develop customized Docker images, start with ForgeOps-provided images. Then, build your configuration profile iteratively as you customize the platform to meet your needs. Building Docker images from time to time integrates your custom configuration profile into new Docker images.

* [icon: tools, set=fa]**Steps to customize the DS Docker image are being revised, and will be published soon.**

* To develop a customized AM Docker image, refer to [`am` image](am.html).

* To develop a customized IDM Docker image, refer to [`idm` image](idm.html).

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