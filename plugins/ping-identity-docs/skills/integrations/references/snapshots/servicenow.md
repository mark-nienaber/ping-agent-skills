---
title: Adding the Ping Identity provisioning role in ServiceNow
description: To allow PingFederate to manage users in ServiceNow, add the special Ping Identity provisioning role in your ServiceNow instance.
component: servicenow
page_id: servicenow:setup:pf_servicenow_connector_adding_the_ping_identity_provisioning_role_in_servicenow
canonical_url: https://docs.pingidentity.com/integrations/servicenow/setup/pf_servicenow_connector_adding_the_ping_identity_provisioning_role_in_servicenow.html
revdate: July 8, 2024
section_ids:
  steps: Steps
---

# Adding the Ping Identity provisioning role in ServiceNow

To allow PingFederate to manage users in ServiceNow, add the special Ping Identity provisioning role in your ServiceNow instance.

## Steps

1. Sign on to https\://*yourinstance*.servicenow\.com as an administrator.

2. Install the Ping Identity Provisioning Solution app.

   The app contains the provisioning role.

   1. In the ServiceNow admin console, navigate to **All Available Applications**.

   2. Search for and select the **Ping Identity Provisioning Solution** app.

   3. Click **Install**.

3. **Optional:** If you want the ServiceNow connector to be able to remove roles from users, grant additional permissions to the provisioning role.

   |   |                                                                                                                                                                                                                                                                                                                                                                                                                        |
   | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | Due to a limitation in the ServiceNow API, the ServiceNow Provisioner requires additional security permissions to be able to remove roles from users. We recommend that you only grant these permissions if you require the role removal functionality. Otherwise, skip these steps. For more details, see [Known issues and limitations](../release_notes/pf_servicenow_connector_known_issues_and_limitations.html). |

   1. In the upper-right corner, click your administrator account name. Click **Elevate Roles**.

      ![The ServiceNow account name menu.](_images/ndn1574898659542.jpg)

   2. On the **Elevate Roles** dialog, select **security\_admin**. Click **OK**.

   3. Go to **System Security > Access Control (ACL)**. Click **New**.

   4. On the **New record** tab, from the **Operation** list, select **Delete**.

   5. From the **Name** list, select **User Role (sys\_user\_has\_role)**.

   6. In the **Requires role** section, double-click **Insert a new row**.

   7. Enter `ping_identity_provisioning_role`, and then press enter.

      ![The new role field with ping\_identity\_provisioning\_role entered.](_images/gzk1574899230765.jpg)

   8. Click **Submit**.
