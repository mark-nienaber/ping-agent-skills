---
title: Changelog
description: Fixed an issue that caused the provisioning engine to see email1 and Email 1 as different devices. This could cause an error when the provisioning engine tried to add a new device instead of updating the existing device.
component: pingid-sdk
page_id: pingid-sdk:release_notes:pf_pid_sdk_connector_changelog
canonical_url: https://docs.pingidentity.com/integrations/pingid-sdk/release_notes/pf_pid_sdk_connector_changelog.html
revdate: June 19, 2024
section_ids:
  pingid-sdk-connector-1-2-2-october-2020: PingID SDK Connector 1.2.2 – October 2020
  pingid-sdk-connector-1-2-1-september-2019: PingID SDK Connector 1.2.1 – September 2019
  pingid-sdk-connector-1-2-may-2019: PingID SDK Connector 1.2 – May 2019
  pingid-sdk-connector-1-1-october-2018: PingID SDK Connector 1.1 – October 2018
  pingid-sdk-connector-1-0-1-august-2018: PingID SDK Connector 1.0.1 – August 2018
  pingid-sdk-connector-1-0-april-2018: PingID SDK Connector 1.0 – April 2018
---

# Changelog

## PingID SDK Connector 1.2.2 – October 2020

* Fixed an issue that caused the provisioning engine to see `email1` and `Email 1` as different devices. This could cause an error when the provisioning engine tried to add a new device instead of updating the existing device.

## PingID SDK Connector 1.2.1 – September 2019

* Improved username validation and encoding to support API changes.

## PingID SDK Connector 1.2 – May 2019

* Fixed a library issue that prevented users from being deprovisioned in PingFederate 8.1.4 and earlier.

* Fixed an issue that caused the connector to use the wrong EU hostname.

* Added a PingID SDK configuration file upload option to speed up configuration in PingFederate 9.0 and later.

## PingID SDK Connector 1.1 – October 2018

* Added support for three Voice Number user attributes.

* Added support for **Primary Authentication Method Upon Creation** configuration.

* Improved error handling and reporting when PingID users contain no ID.

## PingID SDK Connector 1.0.1 – August 2018

* Fixed an issue when a device is updated. Any unchanged devices on the user account were being removed and re-added to the user.

## PingID SDK Connector 1.0 – April 2018

* Initial release

* Added support for PingID SDK v1.0

* Added support for user life cycle management (including creates, updates, disabling users, and deleting users)

* Added configuration options for workflow capabilities (for example, the ability to disable updates)
