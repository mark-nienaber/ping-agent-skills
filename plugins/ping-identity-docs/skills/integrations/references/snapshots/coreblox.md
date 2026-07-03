---
title: Changelog
description: The following is the change history for the CoreBlox Integration Kit.
component: coreblox
page_id: coreblox:coreblox_integration_kit:pf_coreblox_ik_changelog
canonical_url: https://docs.pingidentity.com/integrations/coreblox/coreblox_integration_kit/pf_coreblox_ik_changelog.html
revdate: October 17, 2025
section_ids:
  coreblox-integration-kit-2-7-1-october-2021: CoreBlox Integration Kit 2.7.1 – October 2021
  coreblox-integration-kit-2-7-september-2020: CoreBlox Integration Kit 2.7 – September 2020
  coreblox-integration-kit-2-6-2-june-2020: CoreBlox Integration Kit 2.6.2 – June 2020
  coreblox-integration-kit-2-6-1-november-2018: CoreBlox Integration Kit 2.6.1 – November 2018
  coreblox-integration-kit-2-6-october-2018: CoreBlox Integration Kit 2.6 – October 2018
  coreblox-integration-kit-2-5-april-2018: CoreBlox Integration Kit 2.5 – April 2018
  coreblox-integration-kit-2-4-june-2017: CoreBlox Integration Kit 2.4 – June 2017
  coreblox-integration-kit-2-3-september-2016: CoreBlox Integration Kit 2.3 – September 2016
  coreblox-integration-kit-2-2-november-2015: CoreBlox Integration Kit 2.2 – November 2015
  coreblox-integration-kit-2-1-may-2015: CoreBlox Integration Kit 2.1 – May 2015
  coreblox-integration-kit-2-0-april-2014: CoreBlox Integration Kit 2.0 – April 2014
  coreblox-integration-kit-1-0-5-march-2014: CoreBlox Integration Kit 1.0.5 – March 2014
  coreblox-integration-kit-1-0-november-2012: CoreBlox Integration Kit 1.0 – November 2012
---

# Changelog

The following is the change history for the CoreBlox Integration Kit.

|   |                                                                                                                                                                                                      |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The CoreBlox Integration Kit was created before Coreblox became SDG. The adapter configuration fields and documentation will be updated to use the new name during the next integration kit release. |

## CoreBlox Integration Kit 2.7.1 – October 2021

* Verified that the CoreBlox IdP Adapter is compliant with US Federal Information Processing Standards (FIPS). Learn more about usage in [Integrating with Bouncy Castle FIPS provider](https://docs.pingidentity.com/pingfederate/latest/getting_started_with_pingfederate/pf_set_up_java8_java11.html) in the PingFederate documentation.

* Updated internal components to better support certificate revocation checks in PingFederate 11.0 and later.

## CoreBlox Integration Kit 2.7 – September 2020

* Fixed an issue that could cause a query string to be encoded incorrectly.

* Fixed an issue that could sometimes cause a redirect loop.

* Added the **Session Cookie Prefix** and **Remove Session Cookie Prefix** settings to accommodate a change in the way the CoreBlox Token Service provides tokens.

## CoreBlox Integration Kit 2.6.2 – June 2020

* Fixed an issue that occurred when a user left the sign-on page, then tried to open the sign-on page again elsewhere.

## CoreBlox Integration Kit 2.6.1 – November 2018

* Improved PingFederate node reliability when making REST calls to the the CoreBlox Token Service by changing to a bundled HTTP client.

## CoreBlox Integration Kit 2.6 – October 2018

* Added the ability to ignore session cookies from inbound requests to the PingFederate SP server. Refer to the **Ignore Session Cookie** field on the CoreBlox SP Adapter **Instance Configuration** page.

## CoreBlox Integration Kit 2.5 – April 2018

* Added the **Send Session Attributes** field to the SP adapter. Use this field to send attribute contract to the the CoreBlox Token Service (CTS) for inclusion in the created session.

## CoreBlox Integration Kit 2.4 – June 2017

* PingFederate 8.4 compatibility updates.

* Optionally, prevent an update to the session cookie after sign on.

* User is redirected for authentication if the session is invalid.

* Session cookie is retained and set to the logged off value after SLO.

* Session cookie isn't modified on SLO error.

## CoreBlox Integration Kit 2.3 – September 2016

* Made the **Login URL** field optional to support multiple CoreBlox environments.

* Improved error logging in both the IdP and SP adapters.

## CoreBlox Integration Kit 2.2 – November 2015

* Added support for cookie provider functionality

* Added support for authentication context in the SP Adapter.

## CoreBlox Integration Kit 2.1 – May 2015

* Added the ability to download a configuration file for the OpenToken agent in the CoreBlox SP adapter.

* Bug fixes.

## CoreBlox Integration Kit 2.0 – April 2014

* Added additional UI configuration validation, notably for the fields required for authorization and for the **Cookie Domain** field in the SP adapter.

* Fixed an issue that caused the adapter to use `userId-qualifier` as the attribute to link accounts instead of the `usesrId` attribute.

* Added the ability to specify an **Authentication Context** for the IdP adapter. Anything entered into this field is included in the SAML assertion. Learn more in the [CoreBlox IdP Adapter settings reference](pf_coreblox_ik_coreblox_idp_adapter_settings_reference.html).

* You can now configure both the IdP and SP adapters to authorize a user before redirecting them to the target resource.

* You can now use the keyword `token` to add the `token` attribute returned in the JSON object from the CTS to the extended contract.

## CoreBlox Integration Kit 1.0.5 – March 2014

* Added support for authorization functionality, enabling review of users' authorization level before they can access a protected resource.

## CoreBlox Integration Kit 1.0 – November 2012

* Initial release.
