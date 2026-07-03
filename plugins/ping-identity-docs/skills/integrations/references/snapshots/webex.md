---
title: Changelog
description: Users are no longer required to provide the WebEx Site ID or Partner ID to configure outbound provisioning.
component: webex
page_id: webex:release_notes:pf_webex_connector_changelog
canonical_url: https://docs.pingidentity.com/integrations/webex/release_notes/pf_webex_connector_changelog.html
revdate: June 27, 2024
section_ids:
  webex-provisioner-2-3-june-2023-current-release: Webex Provisioner 2.3 – June 2023 (current release)
  webex-provisioner-2-1-july-2019: Webex Provisioner 2.1 – July 2019
  webex-provisioner-2-0-2-march-2017: Webex Provisioner 2.0.2 – March 2017
  webex-provisioner-2-0-1-february-2017: Webex Provisioner 2.0.1 – February 2017
  webex-provisioner-2-0-may-2016: Webex Provisioner 2.0 – May 2016
  webex-provisioner-1-0-1-february-2014: Webex Provisioner 1.0.1 – February 2014
  webex-provisioner-1-0-may-2010: Webex Provisioner 1.0 – May 2010
---

# Changelog

## Webex Provisioner 2.3 – June 2023 (current release)

Users are no longer required to provide the WebEx **Site ID** or **Partner ID** to configure outbound provisioning.

## Webex Provisioner 2.1 – July 2019

* Fixed an issue that prevented users with special characters from being provisioned to Webex.

* Improved error handling and reporting for cases where users in the target application do not have an ID.

* Improved error logging security.

* Added [provisioning options](../setup/pf_webex_connector_provisioning_options.html) to control the "create", "update", and "disable" functions individually.

## Webex Provisioner 2.0.2 – March 2017

* Fixed synchronization on update of users, that were previously created with "User Create Enabled" set to false in configurable options.

## Webex Provisioner 2.0.1 – February 2017

* Fixed handling of timezones not listed in Webex's 'Timezone encoding list' .

## Webex Provisioner 2.0 – May 2016

* Added support for additional user attributes.

* Added configuration options for CRUD capabilities.

* Added support for Webex API 10.0 SP3.

* Improved exception handling and reporting.

## Webex Provisioner 1.0.1 – February 2014

* Updated Webex API to use XMLBeans 2.6.0 to be compatible with PingFederate 7.x.

## Webex Provisioner 1.0 – May 2010

* Initial Release.

* Added Support for User Provisioning.
