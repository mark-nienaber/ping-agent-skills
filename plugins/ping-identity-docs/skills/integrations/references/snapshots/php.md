---
title: Changelog
description: The following is the change history for the PHP Integration Kit.
component: php
page_id: php:release_notes:pf_php_ik_changelog
canonical_url: https://docs.pingidentity.com/integrations/php/release_notes/pf_php_ik_changelog.html
revdate: June 21, 2024
---

# Changelog

The following is the change history for the PHP Integration Kit.

**PHP Integration Kit 2.5.2 – January 2016**

* Updated sample application data archive.

**PHP Integration Kit 2.5.1 – December 2012**

* Updated to address security issue found since the previous release.

* Added support for the 2.5.1 version of the OpenToken Adapter and OpenToken Agent.

* Added Support for PHP 5.4.8.

* Added Namespaces to the PHP OpenToken Agent.

**PHP Integration Kit 2.4 – March 2010**

* Added token Reply Prevention to the OpenToken IdP Adapter Advanced Settings.

**PHP Integration Kit 2.3 – November 2008**

* Added POST Transport Method for OpenToken when used by a service Provider.

* Added configuration to specify session cookie vs. persistent cookie.

* Added option to set the "`Secure`" attribute on an OpenToken when cookie is used.

* Correctly handles `null` parameters for SOAP SLO.

* Empty query string (`?`) is not automatically appended to the URL when redirecting to `TargetResource`.

* `TargetResource URL` is URL encoded.

**PHP Integration Kit 2.2 – June 2008**

* Added support for SAML 2.0 `isPassive` and `ForceAuthn`.

* Enforced UTF-8 encoding within the OpenToken adapter.

* Combined the OpenToken adapter and OpenToken Java library jar files into a single adapter file for easier deployment to PingFederate.

**PHP Integration Kit 1.2 – December 2007**

* Repaired OpenToken decoding to correct bit unpacking issue.

* Added Agent Toolkit API HTML documentation.

**PHP Integration Kit 1.1 – December 2007**

* Added support for sending and receiving multi-value attributes in the SAML assertion.

**PHP Integration Kit 1.0 – November 2007**

* Initial release.
