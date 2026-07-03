---
title: <code>am</code> and <code>idm</code> images
description: "AM and IDM use two types of configuration: static configuration and dynamic configuration."
component: forgeops
version: 2026.2
page_id: forgeops:customize:fr-data
canonical_url: https://docs.pingidentity.com/forgeops/2026.2/customize/fr-data.html
llms_txt: https://docs.pingidentity.com/forgeops/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["CDK", "Dynamic Configuration", "Static Configuration", "Amster", "Configuration Profile"]
section_ids:
  static-configuration: Static configuration
  dynamic-configuration: Dynamic configuration
  tips_for_managing_am_dynamic_configuration: Tips for managing AM dynamic configuration
  tips_for_managing_idm_dynamic_configuration: Tips for managing IDM dynamic configuration
  configuration-profiles: Configuration profiles
  next_step: Next step
---

# `am` and `idm` images

AM and IDM use two types of configuration: [static configuration](#static-configuration) and [dynamic configuration](#dynamic-configuration).

## Static configuration

Static configuration consists of properties and settings used by the Ping Advanced Identity Software. Examples of static configuration include AM realms, AM authentication trees, IDM social identity provider definitions, and IDM data mapping models for reconciliation.

Static configuration is stored in JSON configuration files. Because of this, static configuration is also referred to as *file-based configuration*.

You build static configuration into the `am` and `idm` Docker images during development using the following general process:

1. Change the AM or IDM configuration in a single-instance ForgeOps deployment using the UIs and APIs.

2. Export the changes to your `forgeops` repository clone.

3. Build a new AM or IDM Docker image that contains the updated configuration.

4. Restart Ping Advanced Identity Software services using the new Docker images.

5. Test your changes. Incorrect changes to static configuration might cause the platform to become inoperable.

6. Promote your changes to your test and production environments as desired.

Refer to [`am` image](am.html) and [`idm` image](idm.html) for more detailed steps.

In Ping Advanced Identity Software deployments, static configuration is *immutable*. Do not change static configuration in testing or production. Instead, if you need to change static configuration, return to the development phase, make your changes, and build new custom Docker images that include the changes. Then, promote the new images to your test and production environments.

## Dynamic configuration

Dynamic configuration consists of access policies, applications, and data objects used by the Ping Advanced Identity Software. Examples of dynamic configuration include AM access policies, AM agents, AM OAuth 2.0 client definitions, IDM identities, and IDM relationships.

Dynamic configuration can change at any time, including when the platform is running in production.

You'll need to devise a strategy for managing AM and IDM dynamic configuration, so that you can:

* Extract sample dynamic configuration for use by developers.

* Back up and restore dynamic configuration.

### Tips for managing AM dynamic configuration

You can use one or both of the following techniques to manage AM dynamic configuration:

* Use the forgeops amster command to manage AM dynamic configuration. For example:

  1. Make modifications to AM dynamic configuration by using the AM admin UI.

  2. Export the AM dynamic configuration to your local file system by using the forgeops amster command. You might manage these files in a Git repository. For example:

     ```
     $ cd /path/to/forgeops/bin
     $ mkdir /tmp/amster
     $ ./forgeops amster export --env-name my-env /tmp/amster
     Cleaning up amster components
     Packing and uploading configs
     configmap/amster-files created
     configmap/amster-export-type created
     Deploying amster
     job.batch/amster created

     Waiting for amster job to complete. This can take several minutes.
     pod/amster-r99l9 condition met
     tar: Removing leading `/' from member names
     Updating amster config.
     Updating amster config complete.
     Cleaning up amster components
     job.batch "amster" deleted
     configmap "amster-files" deleted
     configmap "amster-export-type" deleted
     ```

  3. If desired, import these files into another AM deployment by using the forgeops amster import command.

  Note that the forgeops amster command automatically converts passwords in AM dynamic configuration to configuration expressions. Because of this, passwords in AM configuration files will not appear in cleartext. For details about how to work with dynamic configuration that has passwords and other properties specified as configuration expressions, refer to [Export Utilities and Configuration Expressions](value-substitution.html#export-config-expr).

* Write REST API applications to import and export AM dynamic configuration. For more information, refer to [Rest API](https://docs.pingidentity.com/pingam/8/REST-guide/preface.html) in the AM documentation.

### Tips for managing IDM dynamic configuration

You can use one or both of the following techniques to manage IDM dynamic configuration:

* Migrate dynamic configuration by using IDM's Data Migration Service. For more information, refer to [Migrate Data](https://docs.pingidentity.com/pingidm/8/upgrade-guide/data-migration.html) in the IDM documentation.

* Write REST API applications to import and export IDM dynamic configuration. For more information, refer to the [Rest API Reference](https://docs.pingidentity.com/pingidm/8/rest-api-reference/preface.html) in the IDM documentation.

## Configuration profiles

A Ping Advanced Identity Software *configuration profile* is a named set of configuration that describes the operational characteristics of a running ForgeOps deployment. A configuration profile consists of:

* AM static configuration

* IDM static configuration

Configuration profiles reside in the following paths in the `forgeops` repository:

* docker/am/config-profiles

* docker/idm/config-profiles

User-customized configuration profiles are stored in subdirectories of these paths. For example, a configuration profile named `my-profile` would be stored in the paths docker/am/config-profiles/my-profile and docker/idm/config-profiles/my-profile.

Use Git to manage the directories that contain configuration profiles.

## Next step

* [icon: check-square-o, set=fa][Perform additional setup](setup.html)

* [icon: check-square-o, set=fa][Understand custom images](custom-images.html)

* [icon: check-square-o, set=fa][Customize the DS image](ds.html)

* [icon: check-square-o, set=fa][Understand AM and IDM configuration](fr-data.html)

* [icon: square-o, set=fa]*[Understand property value substitution](value-substitution.html)*

* [icon: square-o, set=fa][Customize the AM image](am.html)

* [icon: square-o, set=fa][Customize the IDM image](idm.html)
