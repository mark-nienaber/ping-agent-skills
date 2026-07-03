---
title: Managing platform administrators
description: If you are an administrator with Delegated Admin rights, you can sign on to the PingOne for Government administrator management platform, create other administrators, and manage their permissions for Ping products.
component: pgic
page_id: pgic:products_and_self-service_tasks:p14g_managingpingproductadmins
canonical_url: http://docs.pingidentity.com/pgic/products_and_self-service_tasks/p14g_managingpingproductadmins.html
revdate: February 15, 2022
section_ids:
  steps: Steps
---

# Managing platform administrators

If you are an administrator with Delegated Admin rights, you can sign on to the PingOne for Government administrator management platform, create other administrators, and manage their permissions for Ping products.

## Steps

1. From the PingOne for Government administrator management platform, go to **Manage Users**.

   ![Screen capture of PingOne for Government administrator management platform with Manage Users highlighted in red.](_images/nvq1640125189143.png)

   |   |                                                                                                                     |
   | - | ------------------------------------------------------------------------------------------------------------------- |
   |   | If no user has been created for you yet, reach out to [Ping Identity Support](https://support.pingidentity.com/s/). |

2. Click **[icon: plus, set=fa]New User** at the top right of the page.

   ![Screen capture of PingOne for Government administrator management platform with + New User highlighted in red.](_images/mbq1640109978875.png)

3. On the **New User** page:

   1. In the **Select a Type** list, select **Customer Admins**.

   2. Complete the following fields:

      * **Password**

      * **ID**

      * **Email**

      * **Common Name**

      * **Last Name**

      * **Role**

   3. In the **Role** field, enter any roles you want your user to assume, and click **Save**.

   Your new admin user is added to the **Customer Admins** list.

---

---
title: PingAccess self-service
description: PingAccess is an identity-enabled access management product that protects web applications and APIs by applying security policies to client requests. You can connect to PingAccess directly from the platform and complete a variety of tasks, which are listed and described below.
component: pgic
page_id: pgic:products_and_self-service_tasks:p14g_pa_selfservice
canonical_url: http://docs.pingidentity.com/pgic/products_and_self-service_tasks/p14g_pa_selfservice.html
revdate: December 21, 2021
---

# PingAccess self-service

PingAccess is an identity-enabled access management product that protects web applications and APIs by applying security policies to client requests. You can connect to PingAccess directly from the platform and complete a variety of tasks, which are listed and described below.

To connect to PingAccess through the portal, click the expandable icon associated with the environment and select the appropriate PingAccess link.

In PingAccess, you can:

* [Manage applications](http://docs.pingidentity.com/pingaccess/latest/pingaccess_user_interface_reference_guide/pa_applications.html)

  Applications represent the protected web applications and APIs to which client requests are sent. Applications are composed of one or more resources and have a common virtual host and context root, and correspond to a single target site. Applications can be protected by PingAccess Gateway or PingAccess Agent. In a gateway deployment, the target application is specified as a Site. In an agent deployment, the application destination is an Agent.

* [Manage authentication](http://docs.pingidentity.com/pingaccess/latest/pingaccess_user_interface_reference_guide/pa_authentication.html)

  Authentication requirements are policies that dictate how users must authenticate before access is granted to protected web applications. Authentication methods are string values and ordered in a list by preference. At runtime, the type of authentication attempted is determined by the order of the authentication methods.

* [Manage identity mappings](http://docs.pingidentity.com/pingaccess/latest/pingaccess_user_interface_reference_guide/pa_identity_mappings.html)

  Identity mappings make user attributes available to backend sites that use them for authentication. There are multiple types of identity mappings, each with different behavior and a distinct set of fields to specify the identity mapping behavior.

* [Manage rules](http://docs.pingidentity.com/pingaccess/latest/pingaccess_user_interface_reference_guide/pa_rules.html)

  Rules are the building blocks for access control and request processing. There are many types of rules, each with different behavior and a distinct set of fields to specify the rule behavior. Rule sets allow you to group multiple rules into re-usable sets, which can be applied to applications and resources. Rule set groups can contain rule sets or other rule set groups, allowing the rule hierarchy to any level of depth. Rule sets and rule set groups can be applied to applications and resources, as required.

* [Manage web sessions](http://docs.pingidentity.com/pingaccess/latest/pingaccess_user_interface_reference_guide/pa_web_sessions.html)

  Web sessions define the policy for web application session creation, lifetime, timeouts, and scope. Multiple web sessions can be configured to scope the session to meet the needs of a target set of applications. This strategy improves the security model of the session, as it prevents unrelated applications from impersonating an end user.

---

---
title: PingDirectory self-service
description: PingDirectory is a scalable directory used to store identity and rich profile data. Enterprises use it to securely store and manage sensitive customer, partner and employee data, including credentials, profiles, preferences and privacy choices. You can connect to PingDirectory directly from the platform.
component: pgic
page_id: pgic:products_and_self-service_tasks:p14g_pd_selfservice
canonical_url: http://docs.pingidentity.com/pgic/products_and_self-service_tasks/p14g_pd_selfservice.html
revdate: December 21, 2021
---

# PingDirectory self-service

PingDirectory is a scalable directory used to store identity and rich profile data. Enterprises use it to securely store and manage sensitive customer, partner and employee data, including credentials, profiles, preferences and privacy choices. You can connect to PingDirectory directly from the platform.

To connect to PingDirectory through the portal, click the expandable icon associated with the appropriate environment, select the **Products** tab, and select the **LDAPS** link.

In PingDirectory, you can change user and group objects through your preferred LDAP browser. See [Managing entries](http://docs.pingidentity.com/pingdirectory/latest/pingdirectory_server_administration_guide/pd_ds_manage_entries.html) in the *PingDirectory Server Administration Guide* for instructions.

---

---
title: PingFederate self-service
description: PingFederate is an enterprise federation server that enables user authentication and single sign-on. It serves as a global authentication authority that allows employees, customers and partners to securely access all the applications they need from any device. You can connect to PingFederate directly from the platform and complete a variety of tasks, which are listed and described below.
component: pgic
page_id: pgic:products_and_self-service_tasks:p14g_pf_selfservice
canonical_url: http://docs.pingidentity.com/pgic/products_and_self-service_tasks/p14g_pf_selfservice.html
revdate: December 21, 2021
---

# PingFederate self-service

PingFederate is an enterprise federation server that enables user authentication and single sign-on. It serves as a global authentication authority that allows employees, customers and partners to securely access all the applications they need from any device. You can connect to PingFederate directly from the platform and complete a variety of tasks, which are listed and described below.

To connect to PingFederate through the portal, click the expandable icon associated with the environment and select the appropriate PingFederate link.

In PingFederate, you can:

* [Manage applications](p14g_pf_manage_apps.html)

  Create and Modify SAML connections, OAuth and OIDC clients, and other integrations with resources you are protecting through PingFederate as authentication service.

* [Manage authentication policies](p14g_pf_auth_policies.html)

  Combine adapters, selectors, and policy contracts in a logical tree to define the end user authentication experience when accessing a protected resource.

* [Manage data sources](p14g_pf_manage_data_sources.html)

  Source and map user attribute data from anywhere using LDAP, REST, JDBC, and other data types.

---

---
title: "PingFederate: Manage applications"
description: You can configure a wide variety of applications in PingFederate and set up SSO to other Ping products and applications.
component: pgic
page_id: pgic:products_and_self-service_tasks:p14g_pf_manage_apps
canonical_url: http://docs.pingidentity.com/pgic/products_and_self-service_tasks/p14g_pf_manage_apps.html
revdate: May 6, 2024
---

# PingFederate: Manage applications

You can configure a wide variety of applications in PingFederate and set up SSO to other Ping products and applications.

See the following:

* [Configuring a SAML application in PingFederate](http://docs.pingidentity.com/solution-guides/workforce_use_cases/htg_config_saml_app.html)

* [Configure federation with SharePoint server](http://docs.pingidentity.com/solution-guides/single_sign-on_use_cases/htg_config_fed_sharepoint.html)

* [Configuring Workday SSO with PingOne or PingFederate](http://docs.pingidentity.com/solution-guides/single_sign-on_use_cases/htg_config_workday_sso_p14e_pf.html)

* [Integrating CyberArk with Ping products for SSO and authentication](http://docs.pingidentity.com/solution-guides/single_sign-on_use_cases/htg_integrate_cyberark_ping_prod_sso_authn.html)

* [Using Palo Alto Networks Next-Generation Firewall with Ping products](http://docs.pingidentity.com/solution-guides/single_sign-on_use_cases/htg_using_palo_alto_networks_ngfw_with_ping_prods.html)

---

---
title: "PingFederate: Manage authentication policies"
description: Authentication policies are processes used to verify that those attempting to access services and applications are who they claim to be. Administrators can configure these policies in many ways, using a wide variety of authentication sources, to meet your needs.
component: pgic
page_id: pgic:products_and_self-service_tasks:p14g_pf_auth_policies
canonical_url: http://docs.pingidentity.com/pgic/products_and_self-service_tasks/p14g_pf_auth_policies.html
revdate: May 6, 2024
---

# PingFederate: Manage authentication policies

Authentication policies are processes used to verify that those attempting to access services and applications are who they claim to be. Administrators can configure these policies in many ways, using a wide variety of authentication sources, to meet your needs.

See the following:

* [Authentication policies](http://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_authentication_policies.html)

* [Defining authentication\_policies](http://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_defining_auth_policies.html)

* [Adapter mappings](http://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_adapt_mappings.html)

* [Register Azure AD devices automatically through PingFederate for Windows 10 devices](http://docs.pingidentity.com/solution-guides/single_sign-on_use_cases/htg_reg_azure_ad_devices_pf_windows10.html)

* [Integrating MFA with SSO (PingID with PingFederate)](http://docs.pingidentity.com/solution-guides/multi-factor_authentication_use_cases/htg_integrate_mfa_with_sso_pid_with_pf.html)

* [Configuring medium-grained application access control through Azure AD, PingFederate, and PingAccess](http://docs.pingidentity.com/solution-guides/data_and_application_security_use_cases/htg_config_med_grained_app.html)

* [Connecting PingFederate to PingAccess](http://docs.pingidentity.com/solution-guides/data_and_application_security_use_cases/htg_connect_pf_pa_oidc.html)

* [Protecting PingAccess resources through external IdPs with PingFederate acting as an SP (leveraging FedHub)](http://docs.pingidentity.com//solution-guides/data_and_application_security_use_cases/htg_protect_pa_resources_pf.html)

---

---
title: "PingFederate: Manage data sources"
description: Most customers who use PingFederate as an identity provider (IdP) have at least one connection to an external data source. Active Directory is the most common data source used to connect to PingFederate, but other options are available.
component: pgic
page_id: pgic:products_and_self-service_tasks:p14g_pf_manage_data_sources
canonical_url: http://docs.pingidentity.com/pgic/products_and_self-service_tasks/p14g_pf_manage_data_sources.html
revdate: May 6, 2024
---

# PingFederate: Manage data sources

Most customers who use PingFederate as an identity provider (IdP) have at least one connection to an external data source. Active Directory is the most common data source used to connect to PingFederate, but other options are available.

See the following:

* [Datastores](http://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_managedatasourcestasklet_managedatasourcesstate.html)

* [Configuring the Active Directory environment](http://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_config_activ_dir_environme.html)

* [Configuring offline MFA with PingID](http://docs.pingidentity.com/solution-guides/multi-factor_authentication_use_cases/htg_config_offline_mfa_pid.html)

---

---
title: Self-service tasks
description: There's a number of tasks you can complete yourself with Ping Government Identity Cloud. Learn more in the following product guides:
component: pgic
page_id: pgic:products_and_self-service_tasks:p14g_products_selfservice
canonical_url: http://docs.pingidentity.com/pgic/products_and_self-service_tasks/p14g_products_selfservice.html
revdate: December 16, 2025
section_ids:
  product-self-service-tasks: Product self-service tasks
  platform-self-service-tasks: Platform self-service tasks
---

# Self-service tasks

## Product self-service tasks

There's a number of tasks you can complete yourself with Ping Government Identity Cloud. Learn more in the following product guides:

* [PingAM](https://docs.pingidentity.com/pingam/)

* [PingDS](https://docs.pingidentity.com/pingds/)

* [PingIDM](https://docs.pingidentity.com/pingidm/8/release-notes/preface.html)

* [PingGateway](https://docs.pingidentity.com/pinggateway/2025.11/index.html)

* [PingFederate](https://docs.pingidentity.com/pingfederate/)

* [PingDirectory](https://docs.pingidentity.com/pingdirectory/)

* [PingAccess](https://docs.pingidentity.com/pingaccess/)

* [PingCentral](https://docs.pingidentity.com/pingcentral/)

* [PingAuthorize](https://docs.pingidentity.com/pingauthorize/)

## Platform self-service tasks

With Ping Government Identity Cloud, you have complete control over the containers running inside the environment and the applications within them. Documentation on how to complete self-service tasks within the environment is housed within your Gitlab project. Some examples of these tasks include:

* Managing administrators

* Creating and updating virtual hosts

* Application version upgrades

* Setting up access tokens for GitLab

* Working with repos and branches

* Branching: Creating, pushing, and merging

---

---
title: Viewing the platform activity log
description: The activity log displays information about activity that has occurred within the platform.
component: pgic
page_id: pgic:products_and_self-service_tasks:p14g_platform_activity_log
canonical_url: http://docs.pingidentity.com/pgic/products_and_self-service_tasks/p14g_platform_activity_log.html
revdate: May 6, 2024
---

# Viewing the platform activity log

The activity log displays information about activity that has occurred within the platform.

To view the activity log, click **Activity Log**.

This log provides a timestamp of the date and time the activity occurred, the environment or user affected, the action taken, and the user who performed the action, as shown in this example.

![Example of the platform activity log, which displays the timestamp, the environment affected, the action taken, and the name of the user who performed the action.](_images/coq1580247519167.png)

|   |                                                    |
| - | -------------------------------------------------- |
|   | Use this information for troubleshooting purposes. |