---
title: Portal Updates
description: List recent updates and changes to the Ping Identity DevOps documentation portal, including storage guidance and removed content
component: devops
page_id: devops::home/portalUpdates
canonical_url: https://developer.pingidentity.com/devops/home/portalUpdates.html
llms_txt: https://developer.pingidentity.com/devops/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  devops-september-2023: September 2023
  devops-a-statement-on-aws-efsebs: A statement on AWS EFS/EBS
  devops-july-2023: July 2023
  devops-read-only-filesystem-example-and-explanation: Read-only filesystem example and explanation
  devops-november-2022: November 2022
  devops-video-content-is-arriving: Video content is arriving
  devops-july-2022: July 2022
  devops-removal-of-docker-compose-examples: Removal of Docker Compose examples
  devops-removal-of-kubernetes-kustomize-examples: Removal of Kubernetes Kustomize examples
  devops-confirmation-of-documentation: Confirmation of Documentation
---

# Portal Updates

This page provides details on significant changes to this portal.

## September 2023

### A statement on AWS EFS/EBS

Some of the product documentation does not explicitly explain the recommended storage solution to use when running on AWS. Clarification was added, particularly when running Ping products in containerized environments [here](../reference/awsStorage.html).

## July 2023

### Read-only filesystem example and explanation

Some environments require the use of a read-only filesystem on containers in runtime. As our product images mature to better align with this practice, a way to work around the situation with our images as they stand today can be found [here](../reference/readOnlyFilesystem.html).

## November 2022

### Video content is arriving

In recent weeks, videos on topics relevant to the DevOps program at Ping have started to be released. Look for links on some pages where the videos are relevant, or you can browse all videos [here](../videos/videos.html).

## July 2022

### Removal of Docker Compose examples

With focus of using Helm to provision to Kubernetes as recommended practice, multi-product Docker Compose examples were no longer maintained or supported and have been removed. The only examples that remain are for single-product deployments. For orchestrating multiple products, see [Helm examples](https://developer.pingidentity.com/helm/examples/index.html).

### Removal of Kubernetes Kustomize examples

Kustomize was the former method for for Kubernetes orchestration. As most of those examples were replaced by Helm, the Kustomize guides and files were also removed from this portal.

### Confirmation of Documentation

We received reports in recent weeks that some of examples were not working due to changes in Kubernetes version support, files that had been removed from this repository, and other reasons. All examples and guides on this portal have been reviewed and should work as written.