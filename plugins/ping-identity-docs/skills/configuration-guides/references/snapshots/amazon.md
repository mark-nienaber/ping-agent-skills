---
title: Assigning Amazon Managed Grafana administrators
description: During authentication to Amazon Managed Grafana, you can optionally assign the Grafana Admin role to users by defining an admin role attribute and populating a PingOne SAML assertion attribute with the expected agreed-upon value.
component: configuration_guides
page_id: configuration_guides:amazon:config_saml_amazonmanagedgrafana_p1_assigning_administrators
canonical_url: https://docs.pingidentity.com/configuration_guides/amazon/config_saml_amazonmanagedgrafana_p1_assigning_administrators.html
revdate: May 6, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
  result: Result:
---

# Assigning Amazon Managed Grafana administrators

## About this task

During authentication to Amazon Managed Grafana, you can optionally assign the Grafana Admin role to users by defining an admin role attribute and populating a PingOne SAML assertion attribute with the expected agreed-upon value.

For the example configuration, in PingOne, the **memberOf** attribute is mapped to the SAML assertion **groups** attribute. In Amazon Managed Grafana, the SAML assertion **groups** attribute is mapped to the Grafana admin role value, as shown in the following image.

![Screen capture of Grafana Assertion mapping section.](_images/tsh1638830072661.png)

## Steps

1. In your Amazon Managed Grafana workspace, go to **SAML Configuration**.

2. In the **Assertion mapping** section, in the **Assertion attribute role** field, enter `groups`.

3. Set the **Admin role values**to the PingOne group for Grafana admins.

   |   |                                                                                                            |
   | - | ---------------------------------------------------------------------------------------------------------- |
   |   | The example in step 7 uses GrafanaAdmins\@directory. The @directory is appended to any PingOne group name. |

4. **Optional:** Set the **Assertion attribute groups**to the **groups** and **Editor role values**to the PingOne group for Grafana editors.

5. Click **Save SAML configuration**.

6. In PingOne, go to **Amazon Managed Grafana application Attribute Mapping**.

7. Map PingOne's **memberOf** attribute to the SAML assertion **groups** attribute.

   ![Screen capture of SSO Attribute Mapping section.](_images/ytt1638830176983.png)

   ### Result:

   Users in the PingOne **GrafanaAdmins** group are Just-In-Time provisioned during authentication as Grafana admins, and users in the PingOne **GrafanaEditors**group are Just-In-Time provisioned during authentication as Grafana editors.
