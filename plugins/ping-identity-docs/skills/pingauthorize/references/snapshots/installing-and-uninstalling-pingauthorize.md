---
title: Available Docker images
description: PingAuthorize provides official Docker images for its server components and administrative tools.
component: pingauthorize
version: 11.1
page_id: pingauthorize:installing_and_uninstalling_pingauthorize:paz_available_docker_images
canonical_url: https://docs.pingidentity.com/pingauthorize/11.1/installing_and_uninstalling_pingauthorize/paz_available_docker_images.html
llms_txt: https://docs.pingidentity.com/pingauthorize/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: November 21, 2025
page_aliases: ["paz_before_install_using_docker.adoc"]
---

# Available Docker images

PingAuthorize provides official Docker images for its server components and administrative tools. These images are published on Ping Identity's [Docker Hub repository](https://hub.docker.com/u/pingidentity/). You can find deployment guidance, examples, and DevOps automation tools in the Ping Identity [DevOps documentation](https://devops.pingidentity.com/).

The following Docker images are available:

| Image                                                                      | Product                         | Description                                                                                 |
| -------------------------------------------------------------------------- | ------------------------------- | ------------------------------------------------------------------------------------------- |
| [pingdataconsole](https://hub.docker.com/r/pingidentity/pingdataconsole)   | PingData administrative console | Administrative console for managing the PingAuthorize server.                               |
| [pingauthorize](https://hub.docker.com/r/pingidentity/pingauthorize)       | PingAuthorize                   | Runtime server that evaluates authorization policies.                                       |
| [pingauthorizepap](https://hub.docker.com/r/pingidentity/pingauthorizepap) | PingAuthorize Policy Editor     | Policy administration point (PAP) used to create, test, and version authorization policies. |
| [pingdirectory](https://hub.docker.com/r/pingidentity/pingdirectory)       | PingDirectory                   | Directory server for storing user identities. PingAuthorize doesn't require PingDirectory.  |

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Only the PingData administrative console, PingAuthorize server, PingAuthorize Policy Editor, and PingDirectory software are licensed under Ping Identity's end-user license agreement. Any other software components contained in the image are licensed solely under the terms of the applicable open source/third party license.Ping Identity accepts no responsibility for the performance of any specific virtualization software and in no way guarantees the performance or interoperability of any virtualization software with its products. |
