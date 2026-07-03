---
title: Changelog
description: The following is the change history for the Zscaler Internet Access Provisioner.
component: zscaler
page_id: zscaler:zscaler_internet_access_provisioner:pf_zscaler_zia_connector_changelog
canonical_url: https://docs.pingidentity.com/integrations/zscaler/zscaler_internet_access_provisioner/pf_zscaler_zia_connector_changelog.html
revdate: June 18, 2024
section_ids:
  zscaler-internet-access-provisioner-1-1-1-october-2023: Zscaler Internet Access Provisioner 1.1.1 – October 2023
  zscaler-internet-access-provisioner-1-1-february-2020: Zscaler Internet Access Provisioner 1.1 – February 2020
  zscaler-internet-access-provisioner-1-0-2-august-2019: Zscaler Internet Access Provisioner 1.0.2 – August 2019
  zscaler-internet-access-provisioner-1-0-1-july-2018: Zscaler Internet Access Provisioner 1.0.1 – July 2018
  zscaler-internet-access-provisioner-1-0-june-2018: Zscaler Internet Access Provisioner 1.0 – June 2018
---

# Changelog

The following is the change history for the Zscaler Internet Access Provisioner.

## Zscaler Internet Access Provisioner 1.1.1 – October 2023

* Fixed an issue that caused null values or missing members in `PATCH` operations for group updates.

* Improved efficiency of `PATCH` operations for group updates.

* Improved volume of log entries for group create and update operations to reduce log density.

## Zscaler Internet Access Provisioner 1.1 – February 2020

* Renamed the integration to "Zscaler Internet Access Provisioner" to match official branding.

* Added the ability to update the `username` attribute in Zscaler Internet Access.

* Improved error handling and reporting when encountering a user that does not have an ID.

* Improved provisioner efficiency by adding support for Patch operations for group updates.

* Fixed an issue that prevented synchronization of groups with certain special characters in the name.

* Fixed an issue that caused groups to be serialized incorrectly.

## Zscaler Internet Access Provisioner 1.0.2 – August 2019

* Fixed an issue that prevented synchronization of groups with certain special characters in the name.

## Zscaler Internet Access Provisioner 1.0.1 – July 2018

* Fixed compatibility issue when other System for Cross-domain Identity Management (SCIM)-based connectors exist along side Zscaler provisioning connections

## Zscaler Internet Access Provisioner 1.0 – June 2018

* Initial release.

* Added support for user and group life cycle management (including creates, updates, and deletes).

* Added support for adding users to groups.

* Added configuration options for workflow capabilities (for example, the ability to disable updates).
