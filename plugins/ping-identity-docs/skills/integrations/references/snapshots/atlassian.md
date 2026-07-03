---
title: Atlassian Cloud Provisioner
description: The Atlassian Cloud Provisioner allows PingFederate to integrate with Atlassian Cloud for user and group provisioning and single sign-on (SSO).
component: atlassian
page_id: atlassian:atlassian_cloud_provisioner:pf_atlassian_cloud_connector
canonical_url: https://docs.pingidentity.com/integrations/atlassian/atlassian_cloud_provisioner/pf_atlassian_cloud_connector.html
revdate: July 3, 2024
section_ids:
  features: Features
  intended-audience: Intended audience
  system-requirements: System requirements
---

# Atlassian Cloud Provisioner

The Atlassian Cloud Provisioner allows PingFederate to integrate with Atlassian Cloud for user and group provisioning and single sign-on (SSO).

## Features

* Manages users in Atlassian Cloud based on changes in an external data store that is attached to PingFederate.

  * Creates, updates, disable, and delete users.

  * Allows you to enable the create, update, disable, and delete capabilities independently.

  * Allows you to choose to disable or delete users when deprovisioning.

  * Allows you to provision disabled users.

  * Creates and deletes groups.

  * Updates group memberships.

* Browser-based single sign-on (SSO) initiated by the service provider (SP) or identity provider (IdP).

* Pre-populates some connection settings with the included quick connection template and SAML metadata file.

## Intended audience

This document is intended for PingFederate administrators. Before you start, familiarize yourself with:

* The following sections of the Atlassian Cloud documentation:

  * [Atlassian organizations](https://confluence.atlassian.com/cloud/atlassian-organizations-964957873.html)

  * [User provisioning](https://confluence.atlassian.com/cloud/user-provisioning-959305316.html)

  * [SAML single sign-on](https://confluence.atlassian.com/cloud/saml-single-sign-on-943953302.html)

* The following sections of the PingFederate documentation:

  * [Identity provider SSO configuration](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_ident_provid_sso_config.html)

  * [Datastores](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_managedatasourcestasklet_managedatasourcesstate.html)

  * [Managing IdP adapters](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_managing_idp_adapters.html)

  * [Managing digital signing certificates and decryption keys](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_certmanagementtasklet_dsigsigningcert_certmanagementstate.html)

  * [SP connection management](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_sp_connect_management.html)

  * [Configuring outbound provisioning](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_spconnectionconfigtasklet_saasprovisioningstate.html)

  * [Configuring outbound provisioning settings](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_protocolsettingstasklet_saasglobalprovisioningsettingsstate.html)

## System requirements

* PingFederate 11.3 or later.

  |   |                                                                                                                                                                                           |
  | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | To allow PingFederate to make outbound connections to the Atlassian Cloud API, you might need to add the following domains to the allow list for your firewall:https\://api.atlassian.com |

* An Atlassian Cloud administrator account.

* An [Atlassian Access](https://www.atlassian.com/software/access) subscription.
