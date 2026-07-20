---
title: Before you start
description: Ping® Identity Reporting requires the following hardware and software requirements to run in your production environment.
component: identity-reporting
page_id: identity-reporting:release-notes:chap-before-you-install
canonical_url: https://docs.pingidentity.com/identity-reporting/release-notes/chap-before-you-install.html
section_ids:
  sec-idm-version: Ping Identity Management
---

# Before you start

Ping® Identity Reporting requires the following hardware and software requirements to run in your production environment.

## Ping Identity Management

Ping Identity Reporting is designed to work with Ping® Identity Management. Identity Reporting supports the following PingIDM version:

**Table 1: PingIDM requirements**

|         |                           |
| ------- | ------------------------- |
| PingIDM | 7.0, 7.1, 7.2, 7.3, 8.0.x |

|   |                                                                                                                                                                                                                                                                                       |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | For system requirements, operating system requirements, and Java requirements, Identity Reporting requires the same setup as PingIDM. Learn more about PingIDM requirements in [Before You Install](https://docs.pingidentity.com/pingidm/7.3/release-notes/before-you-install.html). |

---

---
title: Changelog
description: This section covers key issues in Ping Identity Reporting software.
component: identity-reporting
page_id: identity-reporting:release-notes:chap-changelog
canonical_url: https://docs.pingidentity.com/identity-reporting/release-notes/chap-changelog.html
section_ids:
  latest: Latest
  september_2025: September 2025
  fixes: Fixes
  2023_may: 2023 May
  fixes_2: Fixes
  limitations: Limitations
  known_issues: Known issues
---

# Changelog

This section covers key issues in Ping Identity Reporting software.

Subscribe to get automatic updates: [icon: rss-square, set=fa][Ping Identity Reporting changelog RSS feed](../release-notes/chap-changelog.xml)

## Latest

### September 2025

* Initial release of Ping Identity Reporting 7.1.2.

#### Fixes

* IGA-2289 - Issue with API definitions pagination

* IGA-2301 - Fixed GET method including a body key in params

* IGA-1876 - Fixed appAuthHelperBundle logout issues

* IGA-2614 - Fix errors with report emails with project directory

* IGA-2669 - Allow decoded/encoded \_queryFilter values in query params

* IGA-2597 - Set XHR as identity proxy preference

* IGA-3576 - Fix issue with port number validation

* IGA-3588 - Change installer reference to jetty.xml

* IGA-3589 - Removed extra whitespace in authentication body

### 2023 May

* Initial release of 7.1.1.

#### Fixes

* IGA-114 - IDR bundle install location

* IGA-1285 - Fix SQL report download from report screen

* IGA-1288 - Uniform pagination across data source types

* IGA-1314 - UI - Display of managed/user objects on form edits showing invalid data

* IGA-1315 - UI - Fix visibility of create definition button

* IGA-1396 - UI - Fix async select of definitions on report schedules search parameters

* IGA-1429 - UI - Definition columns not showing overflow text

* IGA-1536 - Set proper commit and version info in conf

* IGA-1700 - Restrict data source information returned

* IGA-1701 - IGA installer front end directory reference

* IGA-1706 - Add bearer token path and content type for API authentication call

#### Limitations

Identity Reporting does not support internationalization or multi-language support of any kind.

#### Known issues

There are no known issues at this time.

---

---
title: Documentation updates
description: The following table tracks changes to the documentation set following the release of Identity Reporting 7.1.x:
component: identity-reporting
page_id: identity-reporting:release-notes:chap-doc-updates
canonical_url: https://docs.pingidentity.com/identity-reporting/release-notes/chap-doc-updates.html
---

# Documentation updates

The following table tracks changes to the documentation set following the release of Identity Reporting 7.1.x:

**Documentation Change Log**

| Date       | Description                                   |
| ---------- | --------------------------------------------- |
| 2026-01-08 | Updated the PingIDM supported version to 8.0. |
| 2025-09-29 | Added an RSS feed link to the changelog.      |
| 2025-09-05 | Release of Ping Identity Reporting 7.1.2      |
| 2023-05    | Release of Ping Identity Reporting 7.1.1.     |
| 2022-05    | Release of Ping Identity Reporting 7.1.       |
| 2020-09    | Initial release of Ping Identity Reporting 1. |

---

---
title: Getting support
description: Ping Identity provides support services, professional services, training through Ping Identity University, and partner services to assist you in setting up and maintaining your deployments. For a general overview of these services, learn more in https://support.pingidentity.com.
component: identity-reporting
page_id: identity-reporting:release-notes:appendix-getting-support
canonical_url: https://docs.pingidentity.com/identity-reporting/release-notes/appendix-getting-support.html
---

# Getting support

Ping Identity provides support services, professional services, training through Ping Identity University, and partner services to assist you in setting up and maintaining your deployments. For a general overview of these services, learn more in <https://support.pingidentity.com>.

Ping Identity has staff members around the globe who support our international customers and partners. For details on Ping Identity's support offering, including support plans and service level agreements (SLAs), visit [support](https://support.pingidentity.com).

Ping Identity publishes comprehensive documentation online:

* The Ping Identity [Knowledge Base](https://support.pingidentity.com/s/knowledge-base) offers a large and increasing number of up-to-date, practical articles that help you deploy and manage Ping Identity software.

  While many articles are visible to community members, Ping Identity customers have access to much more, including advanced information for customers using Ping Identity software in a mission-critical capacity.

* Ping Identity product documentation, such as this document, aims to be technically accurate and complete with respect to the software documented. It is visible to everyone and covers all product features and examples of how to use them.

---

---
title: Release notes
description: These release notes are intended to provide information to administrators and evaluators of the Ping Identity Reporting. All information is accurate at the time of publication and updates are be provided by Ping Identity with subsequent software releases.
component: identity-reporting
page_id: identity-reporting:release-notes:preface
canonical_url: https://docs.pingidentity.com/identity-reporting/release-notes/preface.html
page_aliases: ["index.adoc"]
---

# Release notes

These release notes are intended to provide information to administrators and evaluators of the Ping Identity Reporting. All information is accurate at the time of publication and updates are be provided by Ping Identity with subsequent software releases.

[icon: newspaper, set=fas, size=3x]

#### [What's New](chap-whats-new.html)

Discover new features.

[icon: shield-alt, set=fas, size=3x]

#### [Check security advisories](chap-security-advisories.html)

Gain insight into security advisories in the community and at Ping Identity.

[icon: cogs, set=fas, size=3x]

#### [Before you start](chap-before-you-install.html)

Learn about the requirements for running Identity Reporting software in production.

[icon: star-of-life, set=fas, size=3x]

#### [Fixes, limitations, and known issues](chap-key-fixes.html)

Learn about the fixes, limitations, and known issues in this release.

[icon: book, set=fas, size=3x]

#### [Check doc updates](chap-doc-updates.html)

Track important changes to the documentation.

[icon: life-ring, set=fas, size=3x]

#### [Get support](appendix-getting-support.html)

Find out where to get professional support and training.

---

---
title: Security advisories
description: Ping Identity issues security advisories in collaboration with our customers and the open source community to address any security vulnerabilities transparently and rapidly. Ping Identity's security advisory policy governs the process by which security issues are submitted, received, and evaluated, as well as the timeline for issuing security advisories and patches.
component: identity-reporting
page_id: identity-reporting:release-notes:chap-security-advisories
canonical_url: https://docs.pingidentity.com/identity-reporting/release-notes/chap-security-advisories.html
---

# Security advisories

Ping Identity issues security advisories in collaboration with our customers and the open source community to address any security vulnerabilities transparently and rapidly. Ping Identity's security advisory policy governs the process by which security issues are submitted, received, and evaluated, as well as the timeline for issuing security advisories and patches.

For details of all the security advisories across Ping Identity products, learn more in [Security Advisories](https://support.pingidentity.com/s/global-search/%40uri#q=security%20advisory\&t=All\&sort=relevancy\&numberOfResults=25).

---

---
title: What&#8217;s new
description: Ping Identity Reporting 7.1.2 contains no new key features or functionality changes.
component: identity-reporting
page_id: identity-reporting:release-notes:chap-whats-new
canonical_url: https://docs.pingidentity.com/identity-reporting/release-notes/chap-whats-new.html
section_ids:
  pingidr_7_1_2: PingIDR 7.1.2
  pingidr_7_1_1: PingIDR 7.1.1
  whats-new-7.1.0: PingIDR 7.1
  improvements-changes: Improvements/changes in configuration
---

# What's new

## PingIDR 7.1.2

Ping Identity Reporting 7.1.2 contains no new key features or functionality changes.

## PingIDR 7.1.1

Ping Identity Reporting 7.1.1 contains no new key features or functionality changes.

## PingIDR 7.1

Ping Identity Reporting 7.1 introduces the following new features and functionality:

### Improvements/changes in configuration

* **API as a Data Source and Report Definition**. You can now utilize REST API endpoints as a data source, as well as create report definitions.

* **Dynamic Report Parameters**. Dynamic report parameters can be used for any SQL or API report definitions.

* **User Interface Enhancements**. Changes to the user interface to coincide with the current platform user interface.