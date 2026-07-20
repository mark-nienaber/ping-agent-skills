---
title: Automatically update and remove PingID users
description: The PingID Connector synchronizes user identities and their profile attributes from a configured datastore within PingFederate to PingID.
component: pingid
page_id: pingid:pingid_user_life_cycle_management:pid_automatically_update_remove_pid_users
canonical_url: http://docs.pingidentity.com/pingid/pingid_user_life_cycle_management/pid_automatically_update_remove_pid_users.html
llms_txt: http://docs.pingidentity.com/pingid/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: April 15, 2026
section_ids:
  processing-steps: Processing steps
---

# Automatically update and remove PingID users

The PingID Connector synchronizes user identities and their profile attributes from a configured datastore within PingFederate to PingID.

Ping Identity offers a catalog of connectors that provide provisioning capabilities to software as a service (SaaS) providers. The connectors act as mediators to handle transactions safely and securely. The PingID Connector offers profile management solutions to multiple directory types, such as LDAP, Active Directory (AD), and PingDirectory.

![Diagram showing how the PingID Connector interacts with PingFederate, PingOne, and Active Directory.](_images/ccr1564020537891.png)

## Processing steps

1. PingFederate polls the user directory for any changes to user records at regular intervals, configurable in PingFederate.

2. Records requiring action found during step one are stored within PingFederate's intermediary database and marked as a requiring an update in PingID (PingOne).

3. The connector pulls the marked record from the intermediary database and performs the necessary Read (Get), Update, or Delete operation against the PingID record. These changes are reflected in the PingOne admin portal.

   The PingID Connector:

   * Provides support for PingID API 4.9

   * Includes support for user lifecycle management including updates, disabling users, and deleting users

   * Includes configuration options for workflow capabilities, such as the ability to disable updates.

Download the PingID for PingFederate connector in [PingFederate Server SaaS Connectors](https://www.pingidentity.com/en/resources/downloads/pingfederate.html).

Learn more about how to configure the PingID for PingFederate connector in [PingID Provisioner](http://docs.pingidentity.com/integrations/pingid/pf_pid_connector.html) in the PingFederate documentation.

---

---
title: Bypassing a user&#8217;s service
description: Bypass the need for a user to authenticate using their secondary authentication method.
component: pingid
page_id: pingid:pingid_user_life_cycle_management:pid_bypassing_users_service
canonical_url: http://docs.pingidentity.com/pingid/pingid_user_life_cycle_management/pid_bypassing_users_service.html
llms_txt: http://docs.pingidentity.com/pingid/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: April 14, 2026
section_ids:
  steps: Steps
  result: Result:
---

# Bypassing a user's service

Bypass the need for a user to authenticate using their secondary authentication method.

If a user of the PingID service doesn't have access to the mobile device that is paired with PingID, you can bypass a user's secondary authentication for a selected duration. At the end of a limited duration, secondary authentication for the user resumes automatically.

## Steps

1. In the PingOne admin portal, go to **Users > Users by Service**.

2. Click the service you want.

   The filtered list displays only the selected service users.

3. For a selected user, click the **Expand** icon to expand the user information for the service.

4. Click the **Edit** icon, then click the **Bypass** toggle.

5. From the list, select the duration to bypass the service.

   Only global administrators can select **Unlimited Time** to bypass the service indefinitely. All other administrators that have bypass permissions are restricted to a maximum period of 3 days.

   |   |                                                                                                                                                                                                         |
   | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | Learn more about the types of administrative roles available in [Assigning administrator roles](http://docs.pingidentity.com/pingone/directory/p1_manage_user_roles.html) in the PingOne documentation. |

6. To enable your bypass setting, click the **Bypass** toggle again.

   When the selected length of time has passed, authentication automatically resumes for the user.

   If you select **Unlimited Time**, the user will never be authenticated using this authentication provider.

   ### Result:

   The bypass becomes active immediately.

---

---
title: Changing a user&#8217;s primary device
description: If you have enabled multiple devices, and a user has more than one device, change the user's primary device from the PingID service.
component: pingid
page_id: pingid:pingid_user_life_cycle_management:pid_changing_users_primary_device
canonical_url: http://docs.pingidentity.com/pingid/pingid_user_life_cycle_management/pid_changing_users_primary_device.html
llms_txt: http://docs.pingidentity.com/pingid/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: January 30, 2024
section_ids:
  steps: Steps
  result: Result:
---

# Changing a user's primary device

If you have enabled multiple devices, and a user has more than one device, change the user's primary device from the PingID service.

## Steps

1. In the PingOne admin portal, go to **Users → Users by Service**.

2. From the list of services, click **PingID**.

3. Click the **Expand** icon to expand the user activity panel for the relevant user. ![Screen capture showing the expanded user activity panel for a user in PingOne. The screen capture shows three expandable sections: Single Sign-On, Provisioning, and PingID.](_images/imr1564020532881.png)

4. Click **PingID** to expand the entry.

5. Click the **Pencil** icon next to the relevant secondary device, and then click **Make Primary**.

6. When prompted, verify that you want to make that specific device the primary device for that user . ![Screen capture of the PingOne admin portal, PingID Devices section, showing the Pencil icon for a Desktop Mac device and the popup menu for the Make Primary, Unpair and Multi-select options when editing a user,](_images/rpk1564020534811.png)

   ### Result:

   The device is promoted to Primary. If Default to Primary is configured for your organization, the user is prompted to authenticate using the selected device by default.

   |   |                                                                           |
   | - | ------------------------------------------------------------------------- |
   |   | The user can still change their device during the authentication process. |

---

---
title: Disabling a user&#8217;s service
description: Disable a user's service if you want to block the user's access to a service for an unspecified length of time, such as due to security issues or user absence.
component: pingid
page_id: pingid:pingid_user_life_cycle_management:pid_disabling_a_users_service
canonical_url: http://docs.pingidentity.com/pingid/pingid_user_life_cycle_management/pid_disabling_a_users_service.html
llms_txt: http://docs.pingidentity.com/pingid/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: January 28, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Disabling a user's service

Disable a user's service if you want to block the user's access to a service for an unspecified length of time, such as due to security issues or user absence.

## About this task

You can subsequently re-enable the user's access if you choose.

## Steps

1. In the PingOne admin portal, go to **Users → Users by Service**.

2. From the list of services, click the desired service.

3. For the selected user, click the **Expand** icon to expand the user activity panel for the service.

4. Click **Disable** to disable the user's access to the service.

   You can choose to re-enable the user's service access from this panel later.

---

---
title: Monitoring service activity
description: Several options are available for filtering and monitoring service activity.
component: pingid
page_id: pingid:pingid_user_life_cycle_management:pid_monitoring_service_activity
canonical_url: http://docs.pingidentity.com/pingid/pingid_user_life_cycle_management/pid_monitoring_service_activity.html
llms_txt: http://docs.pingidentity.com/pingid/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: January 27, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
  result: Result:
---

# Monitoring service activity

Several options are available for filtering and monitoring service activity.

## About this task

View a list of users by service, filter the list by a specific service, or search for a specific user.

## Steps

1. In the PingOne admin portal, go to **Users → Users by Service**.

   ### Result:

   The **Users by Service** window displays users for all services. By default, each user entry lists all services associated with that user. Hover over a service to view its full name.

2. Choose from the following options to filter the list.

   | Choice                                                         | Description                                                                                                                                                                  |
   | -------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   | View users by a specific service                               | Select the service to filter. A list of all users associated with the selected service is displayed                                                                          |
   | View the services for a specific user                          | In the search bar, enter any part of the user name or email address. If you filter the list by a specific service the search returns results only for users of that service. |
   | View the service details of a specific user                    | Click the **Expand** icon. If more than one service is shown for the user, you can expand each service to see the last activity details.                                     |
   | View a report showing all user activity for a specific service | Click the relevant link in the user entry, such as **View SSO Activity**.                                                                                                    |

---

---
title: PingID User Life Cycle Management
description: Managing the PingID User Life Cycle involves multiple tasks.
component: pingid
page_id: pingid:pingid_user_life_cycle_management:pid_user_life_cycle_management
canonical_url: http://docs.pingidentity.com/pingid/pingid_user_life_cycle_management/pid_user_life_cycle_management.html
llms_txt: http://docs.pingidentity.com/pingid/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: January 27, 2024
---

# PingID User Life Cycle Management

Managing the PingID User Life Cycle involves multiple tasks.

The life cycle tasks include:

* [Monitoring service activity](pid_monitoring_service_activity.html)

* [Disabling a user's service](pid_disabling_a_users_service.html)

* [Bypassing a user's service](pid_bypassing_users_service.html)

* [Unpairing a user's device from the PingID service](pid_unpairing_users_device_from_pid_service.html)

* [Changing a user's primary device](pid_changing_users_primary_device.html)

* [Removing a PingID user](pid_removing_a_pid_user.html)

* [Automatically update and remove PingID users](pid_automatically_update_remove_pid_users.html)

* User management reports

|   |                                                                                                                                                                                                                                                |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | If you have already connected your existing PingID account to PingOne SSO, you must use the PingOne SSO portal to manage users and their devices. For details, see [Users](http://docs.pingidentity.com/pingone/directory/p1_aboutusers.html). |

---

---
title: Removing a PingID user
description: Permanently remove a PingID service user.
component: pingid
page_id: pingid:pingid_user_life_cycle_management:pid_removing_a_pid_user
canonical_url: http://docs.pingidentity.com/pingid/pingid_user_life_cycle_management/pid_removing_a_pid_user.html
llms_txt: http://docs.pingidentity.com/pingid/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: January 23, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
  result: Result:
---

# Removing a PingID user

Permanently remove a PingID service user.

## About this task

This might be necessary if a user has left your organization. For more information, see [Disabling a user's service](pid_disabling_a_users_service.html).

## Steps

1. In the PingOne admin portal, go to **Users → Users by Service**.

2. From the list of services, click **PingID**.

3. Click the **Expand** icon, to expand the user activity panel for the relevant user. ![Screen capture showing the expanded user activity panel for a user in PingOne. The screen capture shows three expandable sections: Single Sign-On, Provisioning, and PingID.](_images/imr1564020532881.png)

4. Click **PingID** to expand the entry.

5. To remove a user from a specific service, click the **Pencil** icon next to the relevant service, and then click **Remove**.

6. When prompted, confirm that you want to remove the service. ![Screen capture of the PingOne admin portal, PingID Services section, showing the Pencil icon for SSO service and the popup menu for the Disable, Bypass, Remove and Multi-select options when editing a user,](_images/ick1564020536365.png)

   ### Result:

   The user is removed from the selected service.

7. To remove the user from all services, click **Remove from PingID**. ![Screen capture of PingOne admin portal, in the PingID section, showing Pencil icon for PingID service for a user and the popup menu for the Disable and Remove from PingID options when editing a user,](_images/qbh1564020536950.png)

---

---
title: Unpairing a user&#8217;s device from the PingID service
description: Unpair a user's device from the PingID service.
component: pingid
page_id: pingid:pingid_user_life_cycle_management:pid_unpairing_users_device_from_pid_service
canonical_url: http://docs.pingidentity.com/pingid/pingid_user_life_cycle_management/pid_unpairing_users_device_from_pid_service.html
llms_txt: http://docs.pingidentity.com/pingid/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: January 30, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
  result: Result:
---

# Unpairing a user's device from the PingID service

Unpair a user's device from the PingID service.

## About this task

If a user unpairs a device while offline, they can only unpair a device locally, and the PingID service remains paired, blocking the user from pairing that device again until the device is unpaired from the PingID service.

|   |                                                                                                                                                                                                                                                                                                                                                                                         |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | When the user next attempts to single sign on (SSO) to PingOne, they'll be prompted to pair a new device to complete the SSO process. If the new device isn't yet available to the user, you can set the PingID service to bypass PingID authentication for the user for a selected duration. For more information, see [Bypassing a user's service](pid_bypassing_users_service.html). |

## Steps

1. In the PingOne admin portal, go to **Users → Users by Service**.

2. From the services list, click **PingID**.

3. Click the **Expand** icon to expand the user activity panel for the relevant user. ![Screen capture showing the expanded user activity panel for a user in PingOne. The screen capture shows three expandable sections: Single Sign-On, Provisioning, and PingID.](_images/imr1564020532881.png)

4. Click **PingID** to expand the entry.

5. Click the **Pencil** icon next to the relevant desktop app entry, and then click **Unpair**.

6. When prompted, verify that you want to unpair the device. ![Screen capture of the PingOne admin portal, PingID Devices section, showing the Pencil icon for a Desktop Mac device and the popup menu for the Make Primary, Unpair and Multi-select options when editing a user,](_images/rpk1564020534811.png)

   ### Result:

   The device is unpaired from the PingID service. The user will be prompted to pair a new device the next time they SSO to PingOne, unless you've set the PingID service bypass option.

   |   |                                                                                                               |
   | - | ------------------------------------------------------------------------------------------------------------- |
   |   | It might be necessary for the user to unpair the device locally in order to be able to pair the device again. |