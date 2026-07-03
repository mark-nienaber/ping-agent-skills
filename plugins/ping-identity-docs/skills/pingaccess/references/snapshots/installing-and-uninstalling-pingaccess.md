---
title: Accessing the administrative console for the first time
description: After installing and starting PingAccess, access the administrative console and perform configuration and first-time sign on tasks.
component: pingaccess
version: 9.1
page_id: pingaccess:installing_and_uninstalling_pingaccess:pa_accessing_the_admin_console
canonical_url: https://docs.pingidentity.com/pingaccess/9.1/installing_and_uninstalling_pingaccess/pa_accessing_the_admin_console.html
llms_txt: https://docs.pingidentity.com/pingaccess/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: May 6, 2024
section_ids:
  steps: Steps
  result: Result:
  result-2: Result
---

# Accessing the administrative console for the first time

After installing and starting PingAccess, access the administrative console and perform configuration and first-time sign on tasks.

## Steps

1. Launch your browser and go to https\://*\<DNS\_NAME>*:9000

   *\<DNS\_NAME>* is the fully-qualified name of the machine running PingAccess.

   |   |                                                                                                                                                                                                                                                                                             |
   | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | If you haven't yet installed a PingAccess license, the server redirects you to the **License Upload** window outside of the main UI. For more information, see the [PingAccess User Interface Reference Guide](../pingaccess_user_interface_reference_guide/pa_uploading_pa_licenses.html). |

2. Sign on with the default username and password:

   * **Username**: `Administrator`

   * **Password**: `2Access`

3. Read and accept the license agreement.

4. Change the default administrator password on the **First Time Login** page, and then click **Continue**.

   |   |                                                                                                                                                                                                                                                            |
   | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | The new password must conform to the rules specified by the `pa.admin.user.password.regex` property in `run.properties`. For more information about these properties, see the [Configuration file reference](../reference_guides/pa_config_file_ref.html). |

   ### Result:

   The PingAccess administrative console opens.

## Result

After successfully signing on, PingAccess creates a backup of the current configuration to allow the administrator to revert any changes made, stored in `<PA_HOME>/data/archive`. You can control the number of backup files to keep using the `pa.backup.filesToKeep` property in the `run.properties` file. For more information about this property, see the [Configuration file reference](../reference_guides/pa_config_file_ref.html).

|   |                                                                                                                                                    |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Because the backup file contains your complete PingAccess configuration, ensure the file is protected with appropriate security controls in place. |
