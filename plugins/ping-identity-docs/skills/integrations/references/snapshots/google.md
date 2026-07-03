---
title: Access the Password Manager
description: After configuring PingFederate and deploying the application, users can access the Google Apps Password Manager using the URL below. You can find additional parameters in System-service endpoints in the PingFederate Administrator's Manual.
component: google
page_id: google:google_workspace_provisioner:pf_google_workforce_connector_access_the_password_manager
canonical_url: https://docs.pingidentity.com/integrations/google/google_workspace_provisioner/pf_google_workforce_connector_access_the_password_manager.html
revdate: June 24, 2024
---

# Access the Password Manager

After configuring PingFederate and deploying the application, users can access the Google Apps Password Manager using the URL below. You can find additional parameters in [System-service endpoints](https://docs.pingidentity.com/pingfederate/latest/developers_reference_guide/pf_sys_services_endpoints.html) in the PingFederate Administrator's Manual.

|   |                                                                                                                                                                             |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | If you have configured more than one IdP-to-SP adapter mapping, you must specify the SP-adapter instance ID as the value for the query parameter `SpSessionAuthnAdapterId`. |

`http[s]://<pf_host>:<port>/pf/adapter2adapter.ping?TargetResource=http[s]://<g_apps_pm_host>:<port>/gapps-password-manager/ResetPassword`

where:

* `<pf_host>:<port>` is the PingFederate host server name or IP address and port number.

* `<g_apps_pm_host>:<port>` is the host server name or IP address and port number where the Password Manager is deployed (may be the same as for PingFederate).
