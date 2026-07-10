---
title: PingOne for Enterprise requirements and browser support
description: These requirements apply to all versions of PingOne for Enterprise and PingOne SSO for SaaS Apps.
component: pingoneforenterprise
page_id: pingoneforenterprise::p14e_requirements_browsers
canonical_url: https://docs.pingidentity.com/pingoneforenterprise/p14e_requirements_browsers.html
revdate: May 7, 2026
section_ids:
  access-requirements: Access requirements
  supported-browsers: Supported Browsers
---

# PingOne for Enterprise requirements and browser support

These requirements apply to all versions of PingOne for Enterprise and PingOne SSO for SaaS Apps.

## Access requirements

The following URLs and ports must be accessible:

| URL/Port                                                                                                 | Purpose                                                                                                                                                 |
| -------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Port 443                                                                                                 | The default port for secure HTTP.                                                                                                                       |
| https\://admin.pingone.com                                                                               | Connect to your organization's PingOne for Enterprise account for administration and management purposes.                                               |
| https\://desktop.pingone.comhttps\://desktop.pingone.euhttps\://desktop.pingone.com.au                   | Connect to the PingOne for Enterprise dock page for user SSO to applications. The page is a path following this URL and is unique to your organization. |
| https\://authenticator.pingone.comhttps\://authenticator.pingone.euhttps\://authenticator.pingone.com.au | The PingOne for Enterprise authenticator service.                                                                                                       |
| https\://sso.connect.pingidentity.com                                                                    | The single sign-on (SSO) engine for PingOne for Enterprise. This URL isn't regionalized.                                                                |
| https\://login.pingone.comhttps\://login.pingone.euhttps\://login.pingone.com.au                         | The sign-on engine for PingOne for Enterprise Directory and AD Connect.                                                                                 |

## Supported Browsers

Javascript must be enabled for all browsers.

PingOne for Enterprise dock is supported on both desktop and mobile displays, for all specified browser versions.

| Browser                     | Version                                                                                                                          |
| --------------------------- | -------------------------------------------------------------------------------------------------------------------------------- |
| Google Chrome               | Three most recent major versions                                                                                                 |
| Mozilla Firefox             | Three most recent major versions                                                                                                 |
| Apple Safari for MacOS      | Two most recent major versions&#xA;&#xA;The PingOne for Enterprise browser extension isn't supported on Safari.                  |
| Microsoft Edge              | Two most recent major versions&#xA;&#xA;PingOne for Enterprise doesn't support Microsoft Edge running in Internet Explorer mode. |
| Microsoft Internet Explorer | PingOne for Enterprise support for Internet Explorer 11 ended on September 30, 2022.                                             |