---
title: Developer API Use Cases
description: Integrating PingID with PingFederate through APIs
component: solution-guides
page_id: solution-guides:developer_api_use_cases:htg_developer_api_user_cases
canonical_url: https://docs.pingidentity.com/solution-guides/developer_api_use_cases/htg_developer_api_user_cases.html
llms_txt: https://docs.pingidentity.com/solution-guides/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: April 26, 2025
---

# Developer API Use Cases

| Use Case                                                                                                                               | Description                                                                                    |
| -------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| [Integrating PingID with PingFederate through APIs](htg_integrate_pid_pf_thru_apis.html)                                               | Integrate PingID with PingFederate through APIs.                                               |
| [Performing common administrative tasks using the PingID API with Windows PowerShell](htg_admin_tasks_pid_api_windows_powershell.html) | Many PingID management features are available through the PingID API using Windows PowerShell. |

---

---
title: Integrating PingID with PingFederate through APIs
description: Components
component: solution-guides
page_id: solution-guides:developer_api_use_cases:htg_integrate_pid_pf_thru_apis
canonical_url: https://docs.pingidentity.com/solution-guides/developer_api_use_cases/htg_integrate_pid_pf_thru_apis.html
llms_txt: https://docs.pingidentity.com/solution-guides/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: April 26, 2025
section_ids:
  before-you-begin: Before you begin
  about-this-task: About this task
  steps: Steps
  related-links: Related links
---

# Integrating PingID with PingFederate through APIs

## Before you begin

**Components**

* PingFederate 9.1

* PingID

* PingOne for Enterprise

Do the following:

* Ensure that you have a valid Java development environment.

* Be familiar with the [PingFederate 9.1 SDK Developer's Guide](https://cdn-docs.pingidentity.com/archive/pdf/pingfederate/pingfederate-91.pdf#page=663).

## About this task

Follow these steps to establish a quick connection between your application, PingFederate, and PingID.

## Steps

1. Use the /registrations post method to create a PingOne for Enterprise account.

   See [/registrations](https://admin-api.pingone.com/v3-beta/api-docs/#%21/registrations/postRegistration).

2. Use the /identitybridges methods to identify a placeholder PingOne for Enterprise directory as the backend store and to complete PingOne for Enterprise setup.

   See [/identitybridges](https://admin-api.pingone.com/v3-beta/api-docs/#%21/identity_bridges/setupPingFederate).

3. Use the /pingid methods to minimally configure PingID and download the `pingid.properties` file.

   See [/pingid](https://admin-api.pingone.com/v3-beta/api-docs/#%21/pingid).

4. Use the PingFederate administration API to create the PingID adapter in PingFederate.

   See [Implement an IdP adapter](https://cdn-docs.pingidentity.com/archive/pdf/pingfederate/pingfederate-91.pdf#page=667).

## Related links

* [PingFederate 9.1 Administrator's Manual](https://cdn-docs.pingidentity.com/archive/pdf/pingfederate/pingfederate-91.pdf#page=61)

* [PingFederate 9.1 SDK Developer's Guide](https://cdn-docs.pingidentity.com/archive/pdf/pingfederate/pingfederate-91.pdf#page=663)

* [PingID Administration Guide](https://docs.pingidentity.com/pingid/pid_landing_page.html)

* [PingOne API Reference](https://admin-api.pingone.com/v3-beta/api-docs/)

---

---
title: Performing common administrative tasks using the PingID API with Windows PowerShell
description: Many PingID management features are available through the PingID API using Windows PowerShell.
component: solution-guides
page_id: solution-guides:developer_api_use_cases:htg_admin_tasks_pid_api_windows_powershell
canonical_url: https://docs.pingidentity.com/solution-guides/developer_api_use_cases/htg_admin_tasks_pid_api_windows_powershell.html
llms_txt: https://docs.pingidentity.com/solution-guides/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: April 25, 2025
section_ids:
  before-you-begin: Before you begin
  about-this-task: About this task
  steps: Steps
---

# Performing common administrative tasks using the PingID API with Windows PowerShell

Many PingID management features are available through the PingID API using Windows PowerShell.

## Before you begin

* Have a [PingOne admin account](https://docs.pingidentity.com/pingoneforenterprise/pingone_for_enterprise/p14e_register_p14e_account.html).

* Have [Windows PowerShell](https://learn.microsoft.com/en-us/powershell/scripting/what-is-windows-powershell) installed on your server.

## About this task

While it may not be necessary to build a custom application, the PingID API can be helpful in performing common tasks through Windows Powershell. The linked `.zip` file contains scripts to run several common tasks.

## Steps

1. Download the `pingid.properties` file from PingOne for Enterprise.

   1. Log in to <https://admin.pingone.com>.

   2. Go to **Setup → PingID → Client Integration**.

   3. In the **Integrate with PingFederate and other clients** section, click **Download**.

2. Download and configure the PowerShell scripts.

   1. Go to <https://github.com/pingidentity/pingid-powershell-scripts>.

   2. Click **Clone or download → Download ZIP**.

   3. Extract the `.zip` file on a server with PowerShell installed.

   4. Edit the `pingid-api-helper.psl` file to include the `$org_alias`, `$use_benefit`, and `$token` values from your `pingid.properties` file.

3. Run administrative task PowerShell scripts.

   The `.zip` file contains several scripts that you can use to perform tasks similar to the following examples.

   | Task                                   | Script                                                                                                       |
   | -------------------------------------- | ------------------------------------------------------------------------------------------------------------ |
   | Obtain user details                    | `PS C:\Scripts\pingid-powershell-scripts-master\scripts>./Get-User-Details -UserName <user name>`            |
   | Put user in temporary bypass mode      | `PS C:\Scripts\pingid-powershell-scripts-master\scripts>./Toggle-User-Bypass -UserName <user name> -Hours 8` |
   | Remove user from temporary bypass mode | `PS C:\Scripts\pingid-powershell-scripts-master\scripts>./Toggle-User-Bypass -UserName <user name>`          |
   | Remove a user from PingID              | `PS C:\Scripts\pingid-powershell-scripts-master\scripts>./Delete-User -UserName <user name>`                 |

   |   |                                                                                                                                                                                                                                                               |
   | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | If you need to change your PowerShell execution policy, refer to [About Execution Policies](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_execution_policies?view=powershell-7.5\&viewFallbackFrom=powershell-6). |