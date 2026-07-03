---
title: Deployment configuration locations
description: Understand where to store PingAM configuration and run-time data, including options for directory servers and JSON files, and recommendations for high-availability deployments
component: pingam
version: 8.1
page_id: pingam:deployment-planning:deploy-configuration-types
canonical_url: https://docs.pingidentity.com/pingam/8.1/deployment-planning/deploy-configuration-types.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["deployment", "planning", "configuration store"]
page_aliases: ["deployment-planning-guide:deploy-configuration-types.adoc"]
section_ids:
  store-config-in-pingds: Store configuration in PingDS
  store-config-in-fbc: Store configuration in files
  store-runtime-data: Store run-time data
---

# Deployment configuration locations

Every AM deployment has associated *configuration* data. Configuration data consists of properties and settings used by the AM instance to function.

Configuration data is often referred to as *static*, because after your instance is configured to your requirements, it doesn't need to be changed.

Configuration data includes properties and settings for the following:

* Global services

* Realms

* Authentication trees

Configuration data can be stored in directory servers or in JSON files on the local file system. Each option is tailored to a specific deployment requirement.

## Store configuration in PingDS

Storing configuration data in DS datastores offers deployment flexibility and provides instance high availability.

Configuration data in the DS instances is shared between the AM instances in your deployment. The configuration data can be replicated between multiple DS instances in a cluster, and made available to AM instances in different regions, improving availability, and data integrity.

![Replicate data between multiple DS instances in a cluster.](_images/ds-config-store.png)

You can find information on installing AM instances with configuration datastores in [Prepare a configuration store](../installation/prepare-configuration-store.html).

## Store configuration in files

File-based configuration (FBC) is best-suited to a DevOps-style deployment, with the associated tools and practices of that approach.

Static FBC data is written to configuration files in the file system and checked into a source control system, such as Git.

AM instances are created as Docker images, with the FBC incorporated into the image.

![Kubernetes deployment using file-based configuration.](../_images/docker-deployment.png)

You can insert variables into these configuration files before you check them into source control. The variables are substituted with the appropriate values at runtime when you start the Docker container. Using variables lets you reuse the same base configuration files for multiple instances, and different staging environments. For example, development, QA, or pre-production, which are then promoted to production.

Learn more about FBC in [Store configuration data in JSON files](../installation/fbc.html).

Learn more about installing AM instances with Kubernetes in the [ForgeOps](https://docs.pingidentity.com/forgeops/2025.1) documentation.

## Store run-time data

AM instances also create dynamic, run-time data. This data can change and grow frequently, even in a production instance, as business logic changes.

Dynamic data includes properties, settings, and values for the following:

* Policies, policy sets, and resource types

* OAuth 2.0 client profiles

* Federation entities

* Core Token Service (CTS) tokens

* UMA resources, labels, audit messages, and pending requests

Dynamic data is stored in one or more DS instances. You can choose to store dynamic data alongside the configuration data, or separate it into different datastores.

How you separate dynamic data into datastores depends on the volume of dynamic data you expect to handle. For example, CTS data is often highly volatile and short-lived, so it warrants its own set of tuned DS instances. The other dynamic data types might not be as volatile and could potentially all share a set of differently tuned DS instances.

You can find information on setting up DS stores for use with AM in [Prepare datastores](../installation/prepare-ext-stores.html)
