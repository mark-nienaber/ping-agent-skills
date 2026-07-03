---
title: Changelog
description: The following is the change history for the PingID Provisioner.
component: pingid
page_id: pingid:release_notes:pf_pid_connector_changelog
canonical_url: https://docs.pingidentity.com/integrations/pingid/release_notes/pf_pid_connector_changelog.html
revdate: March 31, 2026
section_ids:
  version-1-1-2: Version 1.1.2
  version-1-1-1: Version 1.1.1
  version-1-1: Version 1.1
  version-1-0-1: Version 1.0.1
  version-1-0: Version 1.0
---

# Changelog

The following is the change history for the PingID Provisioner.

## Version 1.1.2

Released in March 2026.

* Improved security by updating bundled components. Removed outdated third-party files and dependencies to address a potential security vulnerability.

## Version 1.1.1

Released in November 2021.

* Improved security by updating bundled components.

## Version 1.1

Released in March 2021.

* Added support for device management.

* Added support for the **Provision Disabled Users** and **User Create** provisioning settings. Learn more in [PingID Connector settings reference](../setup/pf_pid_connector_pid_connector_settings_reference.html).

* Added the **Manage Devices** and **Primary Devices on Create** settings. Learn more in [PingID Connector settings reference](../setup/pf_pid_connector_pid_connector_settings_reference.html).

* Added the ability to upload the `pingid.properties` file. Learn more in [Get your PingID settings file](../setup/pf_pid_connector_get_your_pid_settings_file.html).

## Version 1.0.1

Released in May 2018.

* Fixed an issue that caused deletion of users when **User Update** was set to `false` in the configuration settings.

## Version 1.0

Released in March 2018.

* Initial release.

* Added support for PingID API 4.9.

* Added support for user lifecycle management. This includes updates, disabling users, and deleting users.

* Added configuration options for workflow capabilities. For example, the ability to disable updates.
