---
title: Apache module configuration
description: "The configuration options for the Apache module are listed in the table below. Update the directives as needed in the module's configuration file: <apache installation>/conf/extra/httpd-pfoam.conf"
component: oam
page_id: oam:setup:pf_oam_ik_apache_module_configuration
canonical_url: https://docs.pingidentity.com/integrations/oam/setup/pf_oam_ik_apache_module_configuration.html
revdate: June 21, 2024
---

# Apache module configuration

The configuration options for the Apache module are listed in the table below. Update the directives as needed in the module's configuration file: `<apache installation>/conf/extra/httpd-pfoam.conf`

**Table 1. Configuration directives**

| Field                     | Description                                                                                         | Default Value  |
| ------------------------- | --------------------------------------------------------------------------------------------------- | -------------- |
| OAMCookieName             | Cookie name containing the OAM 11g Session Token. Example: `OAMAuthnCookie_webgate.mydomain.com:80` | n/a            |
| PFResumePath              | Parameter containing the relative sso url passed from PingFederate                                  | resumePath     |
| SessionTokenParameterName | Parameter Name used to pass OAM session token to PingFederate                                       | OAMAuthnCookie |
| PFBaseUrl                 | Base URL for PingFederate used in conjunction with resumePath. Example: `https://mydomain.com:9031` | n/a            |

|   |                                                               |
| - | ------------------------------------------------------------- |
|   | Restart the Apache server after making configuration changes. |
