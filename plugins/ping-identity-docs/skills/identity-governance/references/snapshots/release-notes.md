---
title: Changelog
description: Review the release notes in Identity Governance software.
component: identity-governance
version: 7.1.2
page_id: identity-governance:release-notes:chap-changelog
canonical_url: https://docs.pingidentity.com/identity-governance/7.1.2/release-notes/chap-changelog.html
section_ids:
  september_2025: September 2025
  september_25_2025: September 25, 2025
  fixes: Fixes
  limitations: Limitations
  known_issues: Known Issues
  march_2023: March 2023
  march_18_2023: March 18, 2023
  fixes_2: Fixes
  march_2021: March 2021
  march_18_2021: March 18, 2021
  fixes_3: Fixes
---

# Changelog

Review the release notes in Identity Governance software.

Subscribe to get automatic updates: [icon: rss-square, set=fa][Ping Identity Governance changelog RSS feed](../release-notes/chap-changelog.xml)

## September 2025

### September 25, 2025

#### Fixes

* IGA-1764 - Issue with request for self in AM integrated environments

* IGA-1876 - Fixed appAuthHelperBundle logout issues

* IGA-2468 - Allow multiple word searches in addition to split words

* IGA-1455 - Fix for FILTER keyword

* IGA-2500 - Fixed intermittent end user comment modal error

* IGA-2511 - Fixed repo/link reference

* IGA-2563 - Editing scheduled certifications

* IGA-2553 - Update linkedSystems endpoint wrapper

* IGA-2597 - Set XHR as identity proxy preference

* IGA-2563 - Editing certs with only external applications certifiable

* IGA-2644 - File validation in request creation

* IGA-3110 - Searchable array fix

* IGA-3315 - Allow upload of RAR files

* IGA-3365 - Fixed hardcoding of IDM endpoint in httpservice

* IGA-3375 - Additional file validation in request creation

* IGA-3481 - Fixed object certification escalation notifications

##### Limitations

PingIGA doesn't officially support internationalization or multi-language support of any kind.

##### Known Issues

There are no known issues in this release.

## March 2023

### March 18, 2023

#### Fixes

* IGA-276 - Group (role) drop-down list not functioning if AM OAuth is used

* IGA-501 - False error message 'Access Denied' is shown on logon with Access Review

* IGA-518 - Reviewer unable to sign-off on the access review task

* IGA-882 - Clicking the Submit button twice in 'Approve Access-Request' causes failure

* IGA-887 - Removal approvers list incorrectly referenced when defined without approvers

* IGA-888 - AR Admin check will reference both role types if configured that way

* IGA-891 - User with only AR Admin role blocked from certain access

* IGA-1221 - Notifications not sending on certain second stage certification tasks

* IGA-1223 - Scheduled object cert failing validation

* IGA-1306 - Internal role filters returning only 1 entry

* IGA-1349 - Event Details modal stage stepper not loading in other stage's information

* IGA-1355 - Nested attribute specific filters only matching first condition

* IGA-1430 - Access denied error when logging out from certain screens

* IGA-1455 - Campaigns auto sign-off when using DS as IDM repository

* IGA-1628 - Cert generation calls outdated config endpoint

* IGA-1837 - Policy scan query for active eq true

## March 2021

### March 18, 2021

#### Fixes

* FOR-1967 - Multi Stage certification with completely empty first stage not advancing

* FOR-1969 - Events view off when one of the other stage's events is empty

* FOR-1975 - Expiration certification failing to fully close certification

* FOR-1977 - Add displayName to defaults for glossary

* FOR-1980 - Reassigning events in bulk sends a notification for every single event

* IGA-258 - New glossary item creation is slow

* IGA-155 - Access Review not allowing us to delete scheduled script

* IGA-85 - OOTB example remediate does not remove assignments