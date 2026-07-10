---
title: Adjusting system memory allocation
description: You can adjust system memory allocation to improve overall performance by setting the /proc/sys/vm/max_map_count kernel tuning parameter. Doing this can prevent problems such as the slowing down of batch execution and a continuous increase of memory used by the JVM.
component: pingdirectory
version: 11.1
page_id: pingdirectory:installing_the_pingdirectory_suite_of_products:pd_ds_adjust_system_memory_alloc
canonical_url: https://docs.pingidentity.com/pingdirectory/11.1/installing_the_pingdirectory_suite_of_products/pd_ds_adjust_system_memory_alloc.html
llms_txt: https://docs.pingidentity.com/pingdirectory/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: August 12, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Adjusting system memory allocation

You can adjust system memory allocation to improve overall performance by setting the `/proc/sys/vm/max_map_count` kernel tuning parameter. Doing this can prevent problems such as the slowing down of batch execution and a continuous increase of memory used by the JVM.

## About this task

A good setting to use is four times the number of megabytes of system memory. For example, if you're running on a system with 128 gigabytes of memory, then calculate (128\*1024=131072 megabytes) times 4, which is 524288.

## Steps

1. Sign on as root user.

2. Add the line `vm.max_map_count = <megabytes>` to the file `/etc/sysctl.conf`. For example:

   ```
   vm.max_map_count = 524288
   ```

3. Restart the system to apply the change.

4. (Optional) If you need to tune performance further after setting the `max_map_count` parameter, do the following:

   1. Clone the existing performance profile.

   2. Run the `tuned` command.

   3. Add the line `vm.max_map_count = <megabytes>` to the file `/usr/lib/tuned/profile-name/tuned.conf`.

   4. To select the updated profile, run `tuned-adm profile customized_profile`.

   5. Restart the system to apply the changes.

---

---
title: Completing the installation
description: Regardless of whether you are installing Delegated Admin in a Unix, Linux, or Windows environment, perform the relevant steps in this section after you complete the previous OS-specific tasks.
component: pingdirectory
version: 11.1
page_id: pingdirectory:installing_the_pingdirectory_suite_of_products:pd_da_completing_install
canonical_url: https://docs.pingidentity.com/pingdirectory/11.1/installing_the_pingdirectory_suite_of_products/pd_da_completing_install.html
llms_txt: https://docs.pingidentity.com/pingdirectory/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: September 13, 2023
page_aliases: ["pd_da_pdproxy.adoc", "pd_da_replicated_ds.adoc", "pd_da_external_web_server.adoc", "pd_da_all_locations_except_pdproxy.adoc", "pd_da_next_steps.adoc"]
section_ids:
  pingdirectoryproxy-server: PingDirectoryProxy server
  before-you-begin: Before you begin
  steps: Steps
  example: Example:
  next-steps: Next steps
  external-web-server: External web server
  before-you-begin-2: Before you begin
  steps-2: Steps
  example-2: Example:
  example-3: Example:
  next-steps-2: Next steps
  da_all_except_proxy: PingDirectory server
  steps-3: Steps
  choose-from: Choose from:
  da_next_steps: Next steps
---

# Completing the installation

Regardless of whether you are installing Delegated Admin in a Unix, Linux, or Windows environment, perform the relevant steps in this section after you complete the previous OS-specific tasks.

Navigate to the type of installation you want to complete for the relevant steps.

|   |                                                                                                                                                                                                                                                                                                                                                                                                              |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | If you host Delegated Admin externally or use a custom HTTP connection handler, you must configure the host to include the following response header in all responses sent back from the Delegated Admin application: `X-Frame-Options: SAMEORIGIN`. This header protects your server and the Delegated Admin application from [clickjacking](https://owasp.org/www-community/attacks/Clickjacking) attacks. |

## PingDirectoryProxy server

### Before you begin

The following task assumes that when you ran the `setup` command, you answered `y` to the question `Is Delegated Admin being installed in a topology containing PingDirectoryProxy?`

To configure the PingDirectoryProxy server:

### Steps

* Apply the commands from the `delegated-admin-for-proxy.dsconfig` batch file to the PingDirectoryProxy server where you're installing Delegated Admin.

  #### Example:

  ```shell
  $ ./bin/dsconfig \
    --bindDN "cn=Directory Manager" \
    --bindPassword <password> \
    --no-prompt \
    --batch-file webapps/delegator/delegated-admin-for-proxy.dsconfig
  ```

### Next steps

You must also configure all PingDirectory instances using the `delegated-admin.dsconfig` script as described in [PingDirectory server](#da_all_except_proxy).

## External web server

### Before you begin

The following steps assume that when you ran the `setup` command, you answered `n` to the question `Will the web app be hosted in PingDirectory?`

### Steps

1. Open `config.js` in a text editor.

2. Change the variable values to specify the location of the PingDirectory server.

   | config.jsVariable | Value                                  |
   | ----------------- | -------------------------------------- |
   | `window.DS_HOST`  | Host name of the PingDirectory server  |
   | `window.DS_PORT`  | HTTPS port of the PingDirectory server |

   To view an example outline that features these settings, see `example.config.js`.

3. Save your changes to `config.js`.

4. Create a CORS policy for the Delegated Admin HTTP servlet extension, where *\<origin>* represents the public name of the host, proxy, or load balancer that presents the Delegated Admin web application.

   #### Example:

   ```
   dsconfig create-http-servlet-cross-origin-policy
     --policy-name "Delegated Admin Cross-Origin Policy"
     --set "cors-allowed-methods: GET"
     --set "cors-allowed-methods: OPTIONS"
     --set "cors-allowed-methods: POST"
     --set "cors-allowed-methods: DELETE"
     --set "cors-allowed-methods: PATCH"
     --set "cors-allowed-origins: <origin>"

   dsconfig set-http-servlet-extension-prop
     --extension-name "Delegated Admin"
     --set "cross-origin-policy:Delegated Admin Cross-Origin Policy"
   ```

5. (Optional) If you will be enabling administrators to run Delegated Admin reports in your configuration, run `dsconfig` with the `set-http-servlet-cross-origin-policy-prop` option.

   #### Example:

   ```
   dsconfig set-http-servlet-cross-origin-policy-prop \
     --policy-name "Delegated Admin Cross-Origin Policy" \
     --set cors-exposed-headers:Content-Disposition
   ```

### Next steps

You must also configure any PingDirectory servers in the topology using the `delegated-admin.dsconfig` script as described in [PingDirectory server](#da_all_except_proxy).

## PingDirectory server

To continue installing Delegated Admin on a PingDirectory server, or to complete the installation for an external web server or PingDirectoryProxy:

### Steps

* Select the appropriate PingDirectory installation type:

  #### Choose from:

  * For single instances of PingDirectory, run the following command on the PingDirectory server:

    ```shell
    $ ./bin/dsconfig \
      --bindDN "cn=Directory Manager" \
      --bindPassword <password> \
      --no-prompt \
      --batch-file webapps/delegator/delegated-admin.dsconfig
    ```

  * For replicated instances of the PingDirectory server, run the following command on each PingDirectory server instance in the replication topology:

    ```shell
    $ ./bin/dsconfig \
      --bindDN "cn=Directory Manager" \
      --bindPassword <password> \
      --no-prompt \
      --batch-file webapps/delegator/delegated-admin.dsconfig \
      --applyChangeTo server-group
    ```

## Next steps

|   |                                                                                                                                                                                                                                                                                                                                         |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | You can't sign on to Delegated Admin until you configure the rights of the delegated administrators. Learn more about configuring administrative rights, the REST resource type, session timeout values, and other properties in [Configuring Delegated Admin](../delegated_admin_application_guide/pd_da_config_delegated_admin.html). |

After you configure Delegated Admin, [verify that the application is installed](pd_da_verify_installation.html) and working successfully.

---

---
title: Configuring the file descriptor limits
description: The operating system default file descriptor limits restrict the number of PingDirectory server connections. You can change the descriptor limits to allow more connections.
component: pingdirectory
version: 11.1
page_id: pingdirectory:installing_the_pingdirectory_suite_of_products:pd_ds_config_file_descriptor_limits
canonical_url: https://docs.pingidentity.com/pingdirectory/11.1/installing_the_pingdirectory_suite_of_products/pd_ds_config_file_descriptor_limits.html
llms_txt: https://docs.pingidentity.com/pingdirectory/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: August 12, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
  result: Result
---

# Configuring the file descriptor limits

The operating system default file descriptor limits restrict the number of PingDirectory server connections. You can change the descriptor limits to allow more connections.

## About this task

The PingDirectory server allows for an unlimited number of connections by default, but the file descriptor limit on the operating system restricts the number of connections. Many Linux distributions have a default file descriptor limit of 1024 per process, which might be too low for the server if it needs to handle a large number of concurrent connections.

If the operating system relies on `systemd`, see the Linux operating system documentation for instructions on setting the file descriptor limit.

After you set the operating system limit, you can configure the number of file descriptors that the server will use either by using a `NUM_FILE_DESCRIPTORS` environment variable, or by creating a `config/num-file-descriptors` file with a single line such as `NUM_FILE_DESCRIPTORS=12345`. If these are not set, the operating system uses the default of 65535 descriptors. This is an optional change that you can make if you want to make sure the server shuts down safely before reaching the file descriptor limit.

## Steps

1. Display the current `fs.file-max` limit of the system.

   ```
   sysctl fs.file-max
   ```

   The `fs.file-max` limit is the maximum server-wide file limit that you can set without tuning the kernel parameters in the `proc` file system.

2. Edit the `/etc/sysctl.conf` file.

   If there is a line that sets the value of the `fs.file-max` property, make sure that its value is set to at least 1.5 times the per-process limit.

   If there is no line that sets a value for this property, add the following to the end of the file:

   ```
   fs.file-max = 100000
   ```

   |   |                                                                                              |
   | - | -------------------------------------------------------------------------------------------- |
   |   | 100000 is just an example here. Specify a value of at least 1.5 times the per-process limit. |

3. Display the current hard limit of the system.

   ```
   ulimit -aH
   ```

   The `open files (-n)` value is the maximum number of open files per process limit.

   The value should be set to at least 65535.

4. Edit the `/etc/security/limits.conf` file.

   If the file has lines that set the soft and hard limits for the number of file descriptors, make sure the values are set to 65535. If the lines are not present, add the following lines before `#End of file`, making certain to insert a tab between the columns.

   ```
   *   soft   nofile   65535
   *   hard   nofile   65535
   ```

   |   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
   | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | The number of open file descriptors is limited by the physical memory available to the host. You can determine this limit with the following command.```
   cat /proc/sys/fs/file-max
   ```If the `file-max` value is significantly higher than the 65535 limit, consider increasing the file descriptor limit to between 10% and 15% of the system-wide file descriptor limit. For example, if the `file-max` value is 810752, you could set the file descriptor limit to 100000. If the `file-max` value is lower than 65535, the host is likely not sized appropriately. |

5. Reboot your system, and then use the `ulimit` command to verify that the file descriptor limit is set to 65535.

   ```
   # ulimit -n
   ```

## Result

|   |                                                                                                                                                                                                                                                                                                                                                                                                                       |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | For RedHat 7 or later, modify the `20-nproc.conf` file to set both the open files and max user processes limits.```
/etc/security/limits.d/20-nproc.conf

 Add or edit the following lines if they do not already exist:

 *          soft    nproc     65536
 *          soft    nofile    65536
 *          hard    nproc     65536
 *          hard    nofile    65536
 root       soft    nproc     unlimited
``` |

---

---
title: Delegated Admin
description: Consider the following points when upgrading your version of Delegated Admin.
component: pingdirectory
version: 11.1
page_id: pingdirectory:installing_the_pingdirectory_suite_of_products:pd_da_upgrade_considerations
canonical_url: https://docs.pingidentity.com/pingdirectory/11.1/installing_the_pingdirectory_suite_of_products/pd_da_upgrade_considerations.html
llms_txt: https://docs.pingidentity.com/pingdirectory/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: September 13, 2023
section_ids:
  considerations: Considerations
  upgrade-considerations-introduced-in-delegated-admin-4-9: Upgrade considerations introduced in Delegated Admin 4.9
  upgrade-considerations-introduced-in-delegated-admin-4-8: Upgrade considerations introduced in Delegated Admin 4.8
  upgrade-considerations-introduced-in-delegated-admin-4-6: Upgrade considerations introduced in Delegated Admin 4.6
---

# Delegated Admin

Consider the following points when upgrading your version of Delegated Admin.

## Considerations

If you're running Delegated Admin 3.5 or earlier, upgrade it to the latest version to use PingDirectory 8.0 or later.

Learn more about the compatibility between Delegated Admin and PingDirectory server versions in the [Compatibility matrix](../delegated_admin_application_guide/pd_da_compatibility_matrix.html).

|   |                                                                                                                                                                                                                                                                                  |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | We deprecated support for the Implicit grant type and will remove it in a future release. Use the Authorization Code with PKCE grant type instead. Learn more in [Changing the default OIDC grant type](../delegated_admin_application_guide/pd_da_change_oidc_grant_type.html). |

## Upgrade considerations introduced in Delegated Admin 4.9

The default OpenID Connect (OIDC) grant type used by the `dadmin` client has been updated to Authorization Code with PKCE. The Delegated Admin application will continue to function normally with the Implicit grant type.

## Upgrade considerations introduced in Delegated Admin 4.8

Two new permissions that affect user resource types have been added in Delegated Admin 4.8:

* `Update-profile` grants the ability to update user profiles without allowing password-related privileges.

* `Reset-password` grants the permission to reset passwords without the ability to change other user attributes.

To preserve current admin rights, no action is required after you upgrade. Learn more in [Configuring delegated administrator rights on the PingDirectory server](../delegated_admin_application_guide/pd_da_config_delegated_admin_rights_pd_server.html).

## Upgrade considerations introduced in Delegated Admin 4.6

To use the functionality that allows a help desk agent to trigger a password reset for a user, you must enable the Modifiable Password Policy State plugin on the PingDirectory server that serves as a resource backend.

To enable the **Initiate Password Reset** menu option on user entries, perform the following steps:

1. Run the following command to enable the plugin needed for triggering **Initiate Password Reset**:

   ```
   dsconfig set-plugin-prop \
   --plugin-name "Modifiable Password Policy State Plugin" \
   --set enabled:true --set "base-dn:${searchbasedn}" \
   --set "filter:(|(objectClass=person)(objectClass=ds-cfg-user))"
   ```

2. Run the following command to add a Delegated Admin attribute to the users rest type for `ds-pwp-modifiable-state-json`:

   ```
   dsconfig create-delegated-admin-attribute \
   --type-name users  \
   --attribute-type ds-pwp-modifiable-state-json  \
   --set "display-name:Modifiable Password Policy State"  \
   --set display-order-index:9999
   ```

|   |                                                                                                                                                                                                                                                                                                                                    |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | When you install Delegated Admin 4.6 using the `delegated-admin.dsconfig` script, the Modifiable Password Policy State plugin is enabled. If you're upgrading from a previous version of Delegated Admin, you must manually enable the plugin and add the `ds-pwp-modifiable-state-json` attribute as a Delegated Admin attribute. |

---

---
title: Disabling file system swapping
description: Because file system swapping can interfere with PingDirectory, disable performance tuning tools like tuned.
component: pingdirectory
version: 11.1
page_id: pingdirectory:installing_the_pingdirectory_suite_of_products:pd_proxy_disable_file_system_swapping
canonical_url: https://docs.pingidentity.com/pingdirectory/11.1/installing_the_pingdirectory_suite_of_products/pd_proxy_disable_file_system_swapping.html
llms_txt: https://docs.pingidentity.com/pingdirectory/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 2, 2024
section_ids:
  steps: Steps
---

# Disabling file system swapping

Because file system swapping can interfere with PingDirectory, disable performance tuning tools like `tuned`.

## Steps

1. Sign on as the root user.

2. Add the line `vm.swappiness = 0` to the file `/etc/sysctl.conf`.

3. Restart the system to apply the change.

4. (Optional) If you need to tune performance after disabling file system swapping, do the following:

   1. Clone the existing performance profile.

   2. Run `tuned`.

   3. Add the line `vm.swappiness = 0` to the file `/usr/lib/tuned/profile-name/tuned.conf`.

   4. To select the updated profile, run `tuned-adm profile customized_profile`.

   5. Restart the system to apply the changes.

---

---
title: Downloading the installation packages
description: Download the latest PingDirectory installation packages from the downloads page on the Ping Identity website.
component: pingdirectory
version: 11.1
page_id: pingdirectory:installing_the_pingdirectory_suite_of_products:pd_ds_download_install_packages
canonical_url: https://docs.pingidentity.com/pingdirectory/11.1/installing_the_pingdirectory_suite_of_products/pd_ds_download_install_packages.html
llms_txt: https://docs.pingidentity.com/pingdirectory/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: March 27, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
  choose-from: Choose from:
  choose-from-2: Choose from:
---

# Downloading the installation packages

Download the latest PingDirectory installation packages from the [downloads](https://www.pingidentity.com/en/resources/downloads/pingdirectory-downloads.html) page on the Ping Identity website.

## About this task

To download PingDirectory and its add-ons, you must have an active license and be signed on to the Ping Identity website with the email address used to obtain the license. Add-ons include PingDirectoryProxy, PingDataSync, the PingData Server SDK, and Delegated Admin.

## Steps

1. Sign in to the Ping Identity website.

2. Go to the relevant PingDirectory page.

   ### Choose from:

   * For the latest version, go to the [downloads](https://www.pingidentity.com/en/resources/downloads/pingdirectory-downloads.html) page.

   * For previous versions, go to the [previous releases](https://www.pingidentity.com/en/resources/downloads/pingdirectory-downloads/previous-releases.html) page.

3. Click **PingDirectory** to download the server's `.zip` distribution file.

4. If you want to install one or more add-ons:

   ### Choose from:

   * For the latest versions, click the **Add-ons** tab on the [downloads](https://www.pingidentity.com/en/resources/downloads/pingdirectory-downloads.html) page.

   * For previous versions, locate the add-ons grouped with the version of PingDirectory on the [previous releases](https://www.pingidentity.com/en/resources/downloads/pingdirectory-downloads/previous-releases.html) page.

5. Click the add-ons that you want to download.

6. Extract the compressed PingDirectory `.zip` file to a directory of your choice. For example:

   ```shell
   $ unzip  {pingdir}-<version>.zip
   ```

7. Extract the compressed `.zip` files for any add-ons that you downloaded.

8. For Delegated Admin, copy the folder named `/delegator` and its contents to the appropriate directory as shown in the following table.

   |   |                                                           |
   | - | --------------------------------------------------------- |
   |   | Don't perform this step if you intend to use sample data. |

   | Server                                      | Directory                    |
   | ------------------------------------------- | ---------------------------- |
   | PingDirectory server                        | `/webapps`                   |
   | Replicated instance of PingDirectory server | `/webapps`                   |
   | PingDirectoryProxy server                   | `/webapps`                   |
   | External web server                         | Directory for web-based apps |

---

---
title: Editing OS-level environment variables
description: Certain environment variables might affect the PingDirectory server in unexpected ways. This is particularly true for environment variables that are used by the underlying operating system to control how it uses non-default libraries.
component: pingdirectory
version: 11.1
page_id: pingdirectory:installing_the_pingdirectory_suite_of_products:pd_ds_edit_os_env_variables
canonical_url: https://docs.pingidentity.com/pingdirectory/11.1/installing_the_pingdirectory_suite_of_products/pd_ds_edit_os_env_variables.html
llms_txt: https://docs.pingidentity.com/pingdirectory/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: August 13, 2024
---

# Editing OS-level environment variables

Certain environment variables might affect the PingDirectory server in unexpected ways. This is particularly true for environment variables that are used by the underlying operating system to control how it uses non-default libraries.

For this reason, the PingDirectory server explicitly overrides the values of key environment variables like *\<PATH>*, *\<LD\_LIBRARY\_PATH>*, and *\<LD\_PRELOAD>* to ensure that environment settings used to start the server do not inadvertently impact its behavior.

If you need to edit any of these environment variables, set the values of those variables by manually editing the *\<set\_environment\_vars>* function of the `lib/_script-util.sh` script.

You must stop (`bin/stop-server`) and re-start (`bin/start-server`) the server for the change to take effect.

---

---
title: Installation requirements
description: Before installing Delegated Admin, you must install and configure the following components:
component: pingdirectory
version: 11.1
page_id: pingdirectory:installing_the_pingdirectory_suite_of_products:pd_da_install_requirements
canonical_url: https://docs.pingidentity.com/pingdirectory/11.1/installing_the_pingdirectory_suite_of_products/pd_da_install_requirements.html
llms_txt: https://docs.pingidentity.com/pingdirectory/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: September 13, 2023
page_aliases: ["pd_da_before_you_begin.adoc", "pd_da_install_locations.adoc"]
section_ids:
  application-hosting-options: Application hosting options
---

# Installation requirements

Before installing Delegated Admin, you must install and configure the following components:

* The PingDirectory server

* Your chosen identity provider (IdP) *(tooltip: \<div class="paragraph">
  \<p>A service that manages identity information and provides authentication services to relying clients or SPs within a federated or distributed network.\</p>
  \</div>)*

Learn more about PingDirectory and the supported IdPs in the following table.

| Product              | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | Supported versions                                                                                         |
| -------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| PingDirectory server | Stores user-identity data. The HTTPS port that was configured during PingDirectory server setup is required to install Delegated Admin.Learn more about upgrading a PingDirectory server in [Upgrading the PingDirectory, PingDirectoryProxy, and PingDataSync servers](pd_ds_upgrade_server.html).Learn more about installing and configuring a PingDirectory server in [Installing the PingDirectory server](pd_ds_install_server.html) and [PingDirectory server administration guide](../pingdirectory_server_administration_guide/pd_ds_amin_guide.html).                                                                                                                                                                                                                                            | Refer to the [Compatibility matrix](../delegated_admin_application_guide/pd_da_compatibility_matrix.html). |
| PingFederate server  | &#xA;&#xA;You must configure the following OAuth clients within PingFederate:&#xA;&#xA;Delegated Admin, which obtains an OpenID Connect (OIDC) token that describes the authenticated user. Learn more in Creating an OAuth client for Delegated Admin.&#xA;&#xA;The PingDirectory server itself, which calls PingFederate to validate the OIDC token that Delegated Admin passes to it. Learn more in Creating an OAuth client for PingDirectory.Provides identities for authentication and authorization.Learn more about installing and configuring the PingFederate server in [Configuring the PingFederate server](../delegated_admin_application_guide/pd_da_config_pf_server.html) or the [PingFederate documentation](https://docs.pingidentity.com/pingfederate/latest/pf_pf_landing_page.html). | PingFederate 9.0.0 or later                                                                                |
| Other OIDC providers | &#xA;&#xA;You must configure an OIDC client for Delegated Admin on the OIDC provider. Learn more in Configuring other OIDC identity providers.Provides identities for authentication and authorization.Learn more in [Configuring PingDirectory to use an OIDC identity provider](../delegated_admin_application_guide/pd_da_config_oidc_pd.html).                                                                                                                                                                                                                                                                                                                                                                                                                                                        | N/A                                                                                                        |

## Application hosting options

The location where you choose to install Delegated Admin affects some of the installation steps. Learn more in [Completing the installation](pd_da_completing_install.html).

You can install Delegated Admin in any of the following locations:

* A PingDirectory server, including replicated instances

* A PingDirectoryProxy server

* An external web server

---

---
title: Installing Delegated Admin
description: Different options and procedures are available when you install Delegated Admin depending on your environment and the location of your installation.
component: pingdirectory
version: 11.1
page_id: pingdirectory:installing_the_pingdirectory_suite_of_products:pd_da_install_delegated_admin
canonical_url: https://docs.pingidentity.com/pingdirectory/11.1/installing_the_pingdirectory_suite_of_products/pd_da_install_delegated_admin.html
llms_txt: https://docs.pingidentity.com/pingdirectory/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: September 13, 2023
---

# Installing Delegated Admin

Different options and procedures are available when you install Delegated Admin depending on your environment and the location of your installation.

To install Delegated Admin, read the following sections:

* [Installation requirements](pd_da_install_requirements.html)

* [Preparing to install the application](pd_da_preparing_install.html)

* [Installing the application](pd_da_install_application.html)

* [Completing the installation](pd_da_completing_install.html)

---

---
title: Installing dstat (SUSE Linux)
description: The system monitoring tool dstat can help you troubleshoot PingDirectory servers on SUSE distributions.
component: pingdirectory
version: 11.1
page_id: pingdirectory:installing_the_pingdirectory_suite_of_products:pd_ds_install_dstat_suse
canonical_url: https://docs.pingidentity.com/pingdirectory/11.1/installing_the_pingdirectory_suite_of_products/pd_ds_install_dstat_suse.html
llms_txt: https://docs.pingidentity.com/pingdirectory/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: August 12, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Installing dstat (SUSE Linux)

The system monitoring tool `dstat` can help you troubleshoot PingDirectory servers on SUSE distributions.

## About this task

The `collect-support-data` tool uses the `dstat` utility for system monitoring. You can obtain `dstat` from the [OpenSUSE project website](https://software.opensuse.org/download/package?package=dstat\&project=server%3Amonitoring). The following process shows how to install the `dstat` utility.

## Steps

1. Sign on as the root user.

2. Add the appropriate repository using the `zypper` tool.

3. Install the `dstat` utility.

   ```shell
   $ zypper install dstat
   ```

---

---
title: Installing Java
description: The PingDirectory server requires Java. For optimized performance, use Java for 64-bit architectures. See System requirements for the list of supported Java versions.
component: pingdirectory
version: 11.1
page_id: pingdirectory:installing_the_pingdirectory_suite_of_products:pd_ds_install_java
canonical_url: https://docs.pingidentity.com/pingdirectory/11.1/installing_the_pingdirectory_suite_of_products/pd_ds_install_java.html
llms_txt: https://docs.pingidentity.com/pingdirectory/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: December 18, 2023
section_ids:
  about-this-task: About this task
---

# Installing Java

The PingDirectory server requires Java. For optimized performance, use Java for 64-bit architectures. See [System requirements](pd_ds_system_requirements.html) for the list of supported Java versions.

|   |                                                                                  |
| - | -------------------------------------------------------------------------------- |
|   | Support for Java 11 has been deprecated and will be removed in a future release. |

## About this task

Even if your system already has Java installed, you might want to create a separate Java installation for use by the PingDirectory server so that updates to the system-wide Java installation do not impact the server.

|   |                                                                                                                                                              |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | A separate Java installation requires that you download the Java Development Kit (JDK) instead of the Java Runtime Environment (JRE) for the 64-bit version. |

To install Java, go to the website for the type of Java you want to install, locate the preferred version, and follow the instructions.

---

---
title: Installing sysstat and pstack (Red Hat)
description: If you plan to run PingDirectory on a Red Hat Linux system, install the sysstat and pstack packages. These packages are disabled by default, but are useful for troubleshooting.
component: pingdirectory
version: 11.1
page_id: pingdirectory:installing_the_pingdirectory_suite_of_products:pd_ds_install_sysstat_pstack_red_hat
canonical_url: https://docs.pingidentity.com/pingdirectory/11.1/installing_the_pingdirectory_suite_of_products/pd_ds_install_sysstat_pstack_red_hat.html
llms_txt: https://docs.pingidentity.com/pingdirectory/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: August 14, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Installing sysstat and pstack (Red Hat)

If you plan to run PingDirectory on a Red Hat Linux system, install the `sysstat` and `pstack` packages. These packages are disabled by default, but are useful for troubleshooting.

## About this task

The troubleshooting tool `collect-support-data` uses the `iostat`, `mpstat`, and `pstack` utilities to collect monitoring, performance, and stack trace information on the server's processes.

## Steps

* To install `systat` on your Red Hat system, run the following command.

  ```shell
  $ sudo yum install sysstat gdb dstat -y
  ```

---

---
title: Installing the application
description: The steps for installing the Delegated Admin application depend on:
component: pingdirectory
version: 11.1
page_id: pingdirectory:installing_the_pingdirectory_suite_of_products:pd_da_install_application
canonical_url: https://docs.pingidentity.com/pingdirectory/11.1/installing_the_pingdirectory_suite_of_products/pd_da_install_application.html
llms_txt: https://docs.pingidentity.com/pingdirectory/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: September 13, 2023
page_aliases: ["pd_da_install_unix_linux.adoc", "pd_da_install_windows.adoc"]
section_ids:
  unix-or-linux: Unix or Linux
  steps: Steps
  choose-from: Choose from:
  result: Result
  next-steps: Next steps
  windows: Windows
  steps-2: Steps
  next-steps-2: Next steps
---

# Installing the application

The steps for installing the Delegated Admin application depend on:

* The application host's operating system (OS): Unix, Linux, or Windows

* The identity provider (IdP) *(tooltip: \<div class="paragraph">
  \<p>A service that manages identity information and provides authentication services to relying clients or SPs within a federated or distributed network.\</p>
  \</div>)*: PingFederate or generic OpenID Connect (OIDC) *(tooltip: \<div class="paragraph">
  \<p>An authentication protocol built on top of OAuth that authenticates users and enables clients (relying parties) of all types to request and receive information about authenticated sessions and users. OIDC is extensible, allowing clients to use optional features such as encryption of identity data, discovery of OpenID Providers (OAuth authorization servers), and session management.\</p>
  \</div>)*

To install Delegated Admin, select your OS and IdP and follow the instructions in the corresponding section.

|   |                                                                                                                                                                                  |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Don't assign a value to `window.PF_PORT` in the `config.js` file if PingFederate uses port 443 but doesn't specify that port in the PingFederate base URL, regardless of the OS. |

## Unix or Linux

### Steps

1. Run the following script in the `/delegator` directory.

   ```shell
   $ ./set-up-delegator.sh
   ```

2. Enter the PingDirectory base DN for Delegated Admin resource data when prompted.

3. Respond to the `Use PingFederate as OAuth provider?` prompt:

   #### Choose from:

   * To use PingFederate as your IdP, enter `y`.

     * The script generates several requests for information about your PingFederate server. Enter your own values where applicable, or press Enter to accept the default values.

   * To use a generic OIDC provider as your IdP, enter `n`.

     * Enter the OIDC authority URL and OIDC client ID when prompted. You copied these values from your OIDC provider when you configured the OIDC client for Delegated Admin. Learn more in [Configuring other OIDC identity providers](../delegated_admin_application_guide/pd_da_config_oidc_idp.html).

4. Respond to the remaining command-line prompts.

### Result

For either of the IdPs, the system generates:

* A configuration file, `config.js`, located in the `/webapps/delegator/app` directory.

* A batch file, `delegated-admin.dsconfig`, in the `/webapps/delegator` directory.

  |   |                                                                                                                                                                                                                                                         |
  | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | If you answer `y` to the `setup` script question `Is Delegated Admin being installed in a topology containing PingDirectoryProxy?`, the system also generates a batch file, `delegated-admin-for-proxy.dsconfig` in the `/webapps/delegator` directory. |

### Next steps

Proceed to [Completing the installation](pd_da_completing_install.html) to complete the installation of Delegated Admin.

## Windows

### Steps

1. In the Delegated Admin application directory, copy or rename the file `example.config.js` to `config.js`.

   The `config.js` file contains comments and placeholders for necessary information.

2. Open `config.js` in a text editor.

3. Change the variable values to match your setup configuration.

   | config.js variable              | IdP                                  | Value                                                                                                                                                                    |
   | ------------------------------- | ------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
   | `window.AUTHENTICATE_WITH_PKCE` | PingFederate or other OIDC providers | Specifies whether Delegated Admin should authenticate using the Authorization Code with PKCE grant.&#xA;&#xA;This value must be set to true for a generic OIDC provider. |
   | `window.DADMIN_CLIENT_ID`       | PingFederate or other OIDC providers | Client ID for the PingFederate or OIDC client.                                                                                                                           |
   | `window.OIDC_AUTHORITY`         | Other OIDC providers                 | OIDC authority URL for the OIDC client.                                                                                                                                  |
   | `window.PF_HOST`                | PingFederate                         | Public address of the PingFederate server to which the application redirects the user's browser when signing on.                                                         |
   | `window.PF_PORT`                | PingFederate                         | PingFederate port number.                                                                                                                                                |

4. Save your changes to `config.js`.

5. Concatenate the following files into a single file named `delegated-admin.dsconfig`:

   * `delegated-admin-template-common.dsconfig`

   * `delegated-admin-template-ds.dsconfig`

   * `delegated-admin-template-webapp.dsconfig`

   * `delegated-admin-template-ds-or-proxy.dsconfig`

     |   |                                                                                                                                                                                     |
     | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
     |   | If you are not using PingFederate as your OIDC provider:Include:- `delegated-admin-template-ds-or-proxy-no-pf.dsconfig`Instead of:- `delegated-admin-template-ds-or-proxy.dsconfig` |

6. Open `delegated-admin.dsconfig` in a text editor and replace the variables, `${variable}`, with actual values.

7. Save your changes to `delegated-admin.dsconfig`.

### Next steps

Proceed to [Completing the installation](pd_da_completing_install.html) to complete the installation of Delegated Admin.

---

---
title: Installing the PingDataSync server
description: This section describes how to install and run PingDataSync.
component: pingdirectory
version: 11.1
page_id: pingdirectory:installing_the_pingdirectory_suite_of_products:pd_sync_installing_pds
canonical_url: https://docs.pingidentity.com/pingdirectory/11.1/installing_the_pingdirectory_suite_of_products/pd_sync_installing_pds.html
llms_txt: https://docs.pingidentity.com/pingdirectory/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: September 13, 2023
page_aliases: ["pd_sync_install_pds.adoc", "pd_sync_install_failover_server.adoc"]
section_ids:
  installing-the-main-server: Installing the main server
  about-this-task: About this task
  steps: Steps
  next-steps: Next steps
  installing-a-failover-server: Installing a failover server
  about-this-task-2: About this task
  steps-2: Steps
---

# Installing the PingDataSync server

This section describes how to install and run PingDataSync.

## Installing the main server

### About this task

Use the `setup` tool to install the server. The server needs to be started and stopped by the user who installed it.

### Steps

1. Sign on as a user other than root.

2. Obtain the latest `.zip` release bundle, as described in [Downloading the installation packages](pd_ds_download_install_packages.html), and unpack it in a directory owned by this user.

   ```shell
   $ unzip  {pingdatasync}-<version>.zip
   ```

3. Change to the server root directory.

   ```shell
   $ cd  {pingdatasync}
   ```

4. Run the `setup` command.

   ```shell
   $ ./setup
   ```

5. Type `yes` to accept the End-User License Agreement and press Enter to continue.

6. If adding this server to an existing PingDataSync topology, type `yes`, or press Enter to accept the default (no).

7. Enter the fully qualified host name or IP address of the local host.

8. Create the initial root user DN for PingDataSync, or press Enter to accept the default (cn=Directory Manager).

9. Enter and confirm a password for this account.

10. Press Enter to enable server services and the admin console.

11. Enter the port on which PingDataSync will accept connections from HTTPS clients, or press Enter to accept the default.

12. Enter the port on which PingDataSync will accept connections from LDAP clients, or press Enter to accept the default.

13. Press Enter to enable LDAPS, or enter no.

14. Press Enter to enable StartTLS, or enter no.

15. Select the certificate option for this server.

16. Choose the desired encryption for the directory data, backups, and log files from the choices provided:

    * `Encrypt data with a key generated from an interactively provided passphrase. Using a passphrase (obtained interactively or read from a file) is the recommended approach for new deployments, and you should use the same encryption passphrase when setting up each server in the topology`

    * `Encrypt data with a key generated from a passphrase read from a file`

    * `Encrypt data with a randomly generated key. This option is primarily intended for testing purposes, especially when only testing with a single instance, or if you intend to import the resulting encryption settings definition into other instances in the topology`

    * `Encrypt data with an imported encryption settings definition. This option is recommended if you are adding a new instance to an existing topology that has older server instances with data encryption enabled`

    * `Do not encrypt server data`

17. Choose the option for the amount of memory that should be allocated to the server.

18. To start the server when the configuration is complete, press Enter for (yes).

19. A Setup Summary is displayed. Choose the option to set up the server with the listed parameters, change the parameters, or cancel the setup.

### Next steps

After the server configuration is complete, you can run the `create-sync-pipe-config` tool configure the synchronization environment.

The admin console enables browser-based server management, the `dsconfig` tool enables command-line management, and the Configuration API enables management by third-party interfaces.

## Installing a failover server

### About this task

PingDataSync supports redundant failover servers that automatically become active when the primary server is not available. Multiple servers can be present in the topology in a configurable prioritized order.

Before installing a failover server, have a primary server already installed and configured. When installing the redundant server, the installer will copy the first server's configuration.

The primary and secondary server configuration remain identical. Both servers should be registered to the `allservers` group and all `dsconfig` changes need to be applied to the server group `allservers`.

|   |                                                                                                                                                                                                                                                                                                                                                                                                            |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | If the primary server has extensions defined, they should also be installed on any cloned or redundant servers. If extensions are missing from a secondary server, the following message is displayed during the installation:```
Extension class <com.server.directory.sync.MissingSyncExtension> was not
found. Run manage-extension --install to install your extensions. Re-run setup to continue.
``` |

To remove a failover server, use the `uninstall` command.

### Steps

1. Unpack the PingDataSync `.zip` build. Name the unpacked directory something other than the first server instance directory.

   ```shell
   $ unzip PingData<server_version>.zip -d  <server2>
   ```

2. Go to the server root directory.

3. Run the `setup` command without any options to install the failover server in interactive mode, or run the following command to install it in non-interactive mode:

   ```shell
   $ ./setup --localHostName <server2>.example.com --ldapPort 7389 \
     --masterHostName <server1>.example.com --masterPort 8389 \
     --masterUseNoSecurity \
     --acceptLicense \
     --rootUserPassword password \
     --no-prompt
   ```

   The secondary server is now ready to take over as a primary server in the event of a failover. No `realtime-sync` invocations are needed for this server.

4. Verify the configuration by using the `bin/status` command. Each server instance is given a priority index. The server with the lowest priority index number has the highest priority.

   ```shell
   $ bin/status --bindPassword secret

   ...(status output)...
                                 --- Sync Topology ---
   Host:Port	                       :Status	:Priority
   ---------------------------------------:-------------:---------------
   <server>.example.com:389 (this server) : Active      : 1
   <server>.example.com:389	           : Unavailable : 2
   ```

5. To obtain the name of a particular server, run the `dsconfig` command with the `list-external-servers` option.

   ```shell
   $ bin/dsconfig list-external-servers
   ```

6. To change the priority index of the server, run the `bin/dsconfig` command as follows:

   ```shell
   $ bin/dsconfig set-external-server-prop \
     --server-name  <server2>.example.com:389 \
     --set <server>-priority-index:1
   ```

---

---
title: Installing the PingDirectory server
description: After you prepare your hardware and software systems, you can set up the PingDirectory server.
component: pingdirectory
version: 11.1
page_id: pingdirectory:installing_the_pingdirectory_suite_of_products:pd_ds_install_server
canonical_url: https://docs.pingidentity.com/pingdirectory/11.1/installing_the_pingdirectory_suite_of_products/pd_ds_install_server.html
llms_txt: https://docs.pingidentity.com/pingdirectory/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: September 13, 2023
page_aliases: ["pd_ds_set_up_in_interactive_mode.adoc", "pd_ds_install_in_non_interactive_mode.adoc", "pd_server_enable_encryption_setup.adoc", "pd_server_setting_up_server_with_database.adoc", "pd_ds_install_server_with_no_security.adoc", "pd_ds_install_with_truststore.adoc", "pd_ds_install_lightweight_server.adoc", "pd_ds_install_server_on_windows.adoc"]
section_ids:
  install_pd_ds_interactive: Installing the PingDirectory server in interactive mode
  before-you-begin: Before you begin
  steps: Steps
  example: Example:
  example-2: Example:
  choose-from: Choose from:
  choose-from-2: Choose from:
  choose-from-3: Choose from:
  choose-from-4: Choose from:
  choose-from-5: Choose from:
  result: Result
  installing-the-pingdirectory-server-in-non-interactive-mode: Installing the PingDirectory server in non-interactive mode
  enable_encrypt_setup: Enabling data encryption during non-interactive setup
  about-this-task: About this task
  steps-2: Steps
  set_up_server_db: Setting up the server with an existing encryption settings database
  about-this-task-2: About this task
  steps-3: Steps
  install_no_sec: Installing the PingDirectory server with no security enabled
  steps-4: Steps
  example-3: Example:
  install_with_truststore: Installing the PingDirectory server with a truststore
  steps-5: Steps
  example-4: Example:
  installing-a-lightweight-server: Installing a lightweight server
  installing-the-server-on-windows: Installing the server on Windows
  before-you-begin-2: Before you begin
  about-this-task-3: About this task
  steps-6: Steps
  result-2: Result:
---

# Installing the PingDirectory server

After you prepare your hardware and software systems, you can set up the PingDirectory server.

You can perform the following types of installations:

* An interactive installation guides you through the setup.

* A non-interactive installation doesn't guide you through setup and requires knowledge of the appropriate CLI commands.

* A lightweight installation is appropriate for testing or demonstration purposes.

* A Windows installation includes steps for installing on the Windows operating system.

Navigate to the appropriate section to find instructions for the type of installation you want to perform.

## Installing the PingDirectory server in interactive mode

The `setup` command provides an interactive text-based command-line interface to set up a PingDirectory server instance.

### Before you begin

Review [Pre-installation considerations](pd_ds_before_you_begin_install.html).

### Steps

1. Extract the distribution `.zip` archive, then go to the server root directory.

2. Run the `setup` command.

   #### Example:

   ```shell
   $ ./setup
   ```

   If the *JAVA\_HOME* environment variable is set to an older version of Java, explicitly specify the path to the Java Development Kit (JDK) installation during the setup process. Either set the *JAVA\_HOME* environment variable with the JDK path or execute the `setup` command in a modified Java environment using the `env` command.

   #### Example:

   ```shell
   $ env JAVA_HOME=/ds/java ./setup
   ```

3. Read the Ping Identity End-User License Agreement, and type `yes` to continue.

4. Enter the fully qualified host name or IP address of the local host, or press Enter to accept the default.

5. Enter the distinguished name (DN) for the initial root user, or press Enter to accept the default (`cn=Directory Manager`).

6. Enter and confirm the root user password.

7. Press Enter to enable the Ping Identity services (Configuration, Consent, Delegated Admin, Documentation, and Directory REST API) and the admin console over HTTPS.

   After setup, you can enable or disable individual services and applications by configuring the HTTPS Connection Handler.

8. Enter the port on which the PingDirectory server will accept connections from HTTPS clients, or press Enter to accept the default.

9. Select the unencrypted LDAP connection setting option for this server or press Enter to accept the default (option 3).

   #### Choose from:

   * `Do not accept unencrypted LDAP connections`

     |   |                                             |
     | - | ------------------------------------------- |
     |   | If you select this option, skip to step 12. |

   * `Accept unencrypted LDAP connections, but require StartTLS to secure all communication on those connections`

   * `Accept unencrypted LDAP connections, but optionally allow StartTLS to secure communication on those connections`

   * `Accept unencrypted LDAP connections and do not enable support for StartTLS`

10. Enter the port on which the PingDirectory server will accept connections from LDAP clients, or press Enter to accept the default.

11. Select the desired setting for enabling LDAPS, or press Enter to accept the default.

    |   |                                              |
    | - | -------------------------------------------- |
    |   | If you do not enable LDAPS, skip to step 12. |

12. Enter the port on which the PingDirectory server will accept connections from LDAPS clients, or press Enter to accept the default.

13. Select the certificate option for this server:

    #### Choose from:

    * `Generate self-signed certificate (recommended for testing purposes only)`

    * `Use an existing certificate located on a Java Keystore (JKS). Enter the keystore path and keystore PIN to use an existing certificate using a Java Keystore`

    * `Use an existing certificate located on a PKCS12 keystore. Enter the keystore path and the keystore PIN to use an existing certificate using use a PKCS#12 keystore`

    * `Use an existing certificate on a PKCS11 token. Enter only the keystore PIN to use the PKCS#11 token`

14. Choose the desired encryption for the directory data, backups, and log files from the choices provided:

    #### Choose from:

    * `Encrypt data with a key generated from an interactively provided passphrase. Using a passphrase (obtained interactively or read from a file) is the recommended approach for new deployments. Use the same encryption passphrase when setting up each server in the topology`

    * `Encrypt data with a key generated from a passphrase read from a file`

    * `Encrypt data with a randomly generated key. This option is primarily intended for testing purposes, especially when only testing with a single instance, or if you intend to import the resulting encryption settings definition into other instances in the topology`

    * `Encrypt data with an imported encryption settings definition. This option is recommended if you are adding a new instance to an existing topology that has older server instances with data encryption enabled`

    * `Do not encrypt server data`

15. Type the base DN for the data, or accept the default base DN of `dc=example,dc=com`.

16. To choose an option to generate and import sample data, type the desired number of entries, or press Enter to accept the default number (10000).

    This option is used for quick evaluation of the PingDirectory server. Refer to [Importing data](../pingdirectory_server_administration_guide/pd_ds_importing_data.html) if you want to use other options to initialize the server.

17. Choose the option to tune the amount of memory that will be consumed by the PingDirectory server and its tools.

18. Press Enter to prime or preload the database cache at startup before accepting client connections.

    Priming the cache can increase the startup time for the PingDirectory server but provides optimum performance after startup completes. This option is best used for strict throughput or response time performance requirements, or if other replicas in a replication topology can accept traffic while this PingDirectory server instance is starting.

19. Enter a location name for this server.

20. Enter a unique instance name for this server.

    You cannot change the name after you set it.

21. Press Enter to accept the default (yes) to start the PingDirectory server after the configuration has completed.

    Enter `no` if you want to configure additional settings or import data. Doing this keeps the server in shutdown mode.

22. Select the desired option for populating the `config/tools.properties` file during setup, or press Enter to select the default (option 1).

    #### Choose from:

    * `Do not populate the tools.properties file`

    * `Populate the tools.properties file with properties needed to connect to the server`

    * `Populate the tools.properties file with properties needed to connect to the server, and also include the initial root user DN as the default bind DN`

    * `Populate the tools.properties file with properties needed to connect to the server, and also include the DN and password for the initial root user DN as the default bind DN and password`

      |   |                                                                                                                                                                                                                                                                                                                                      |
      | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
      |   | This fourth option, which is not recommended for production environments, populates the `tools.properties` file with properties needed to connect to the server, includes the DN for the initial root user as the default bind DN, and writes the password for that user to a `tools.pin` file for use as the default bind password. |

23. In the **Setup Summary** window, review your configuration details, and then select your setup option, or press Enter to select the default (option 1):

    #### Choose from:

    * `Set up the server with the parameters you have given`

    * `Provide the setup parameters again`

    * `Cancel the setup`

### Result

If you select option 1, your PingDirectory server is configured and initialized.

## Installing the PingDirectory server in non-interactive mode

Run the `setup` command in non-interactive mode to automate the installation process using a script or to run the command directly from the command line.

Non-interactive mode is useful when setting up production or QA servers with specific configuration requirements. There are two ways to set up a server in non-interactive mode:

* Use the `setup` command with the required arguments.

* Use the `manage-profile setup` command to set up the server with a configured server profile. Learn more in [Setting up the server with an existing encryption settings database](#set_up_server_db) and [Server profiles](../pingdirectory_server_administration_guide/pd_ds_server_profiles.html).

Using the `setup` command in non-interactive mode requires that all mandatory arguments be present for each command call. If there are missing or incorrect arguments, the `setup` command fails and aborts the process. You must use a `--no-prompt` option to suppress interactive output, except for errors, when running in non-interactive mode. You must also specify the port on which the server listens for connections:

* `--ldapPort` for connections from unencrypted LDAP clients

* `--ldapsPort` for connections from TLS-encrypted LDAPs clients

Lastly, you must use the `--acceptLicense` option. To view the license, run the `bin/review-license` command.

To tune the Java Virtual Machine (JVM) *(tooltip: \<div class="paragraph">
\<p>A virtual machine that allows a computer to run Java programs and programs that are compiled to Java bytecode.\</p>
\</div>)* to use maximum memory automatically, use the `--maxHeapSize` option. To preload the database at startup, use the `--primeDB` option.

Learn more about configuring a deployment using a truststore in [Installing the PingDirectory server with a truststore](#install_with_truststore).

To see a description of the available command-line options for the `setup` command, use `setup --help`.

Instructions for additional tasks you can perform while installing the server in non-interactive mode are provided in the following sections.

### Enabling data encryption during non-interactive setup

Enabling data encryption during setup provides the strongest protection for your PingDirectory server.

#### About this task

Enabling encryption during setup ensures that all data written to the local DB backends, the changelog, and the replication database will be encrypted. Enabling encryption during setup also ensures that directory backups and LDIF exports are encrypted by default.

If you enable encryption after setup, then only entries created or updated after enablement will be encrypted, along with their corresponding records in the LDAP changelog and replication database. Any data and indexes that existed before enabling encryption remain unencrypted. To encrypt pre-existing local DB backends, export the data to LDIF and then re-import the LDIF file. To ensure future encryption of backups and LDIF exports, set the `encrypt-backups-by-default` and `encrypt-ldif-exports-by-default` system configuration properties to `true`.

You can enable encryption in either interactive or non-interactive setup. Learn more about enabling encryption in an interactive setup in [Installing the PingDirectory server in interactive mode](#install_pd_ds_interactive).

To enable encryption non-interactively:

#### Steps

* Run the `setup` command with one of the following arguments:

  | Arguments                                                | Description                                                                                                                                                                                                                                                                                                                                     |
  | -------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  | `--encryptDataWithRandomPassphrase`                      | Creates an encryption settings definition for you with a strong, randomly generated key.&#xA;&#xA;Because all instances in a topology should have the same encryption settings definitions, you should only use this argument for standalone instances or the first instance in a topology that will export its definitions to other instances. |
  | `--encryptDataWithPassphraseFromFile`                    | Creates an encryption settings definition from a passphrase you specify. When using this argument, you must specify the path for the file containing the desired passphrase. If you are setting up multiple server instances, you should supply the same passphrase to ensure that definitions are consistent.                                  |
  | `--encryptDataWithSettingsImportedFromFile`              | Imports one or more definitions from a file generated by the `encryption-settings export` command. When using this argument, you must specify the path for the file containing the passphrase that protects the encryption settings export.                                                                                                     |
  | `--encryptDataWithPreExistingEncryptionSettingsDatabase` | Uses the encryption settings definitions from an encryption settings database that was created by another server instance.                                                                                                                                                                                                                      |

### Setting up the server with an existing encryption settings database

For added convenience, you can use an existing encryption settings database when setting up the server.

#### About this task

Setting up the server with an existing encryption settings database offers several advantages. You can:

* Use an encryption settings database protected by an alternative cipher stream provider. Other methods for enabling data encryption during setup will create an encryption settings database that is protected by an unencrypted password stored in a local file, and anyone with access to the system during setup can decrypt that database's contents. Alternative cipher stream providers offer stronger protection.

* Enable data encryption restrictions during setup without the need to configure them later.

* Use an encryption settings database that is frozen at the time of setup without needing to freeze it later.

  |   |                                                                                                                                                                             |
  | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | If you provide a frozen encryption settings database with data encryption restrictions enabled, the definitions it contains are not exposed, even to server administrators. |

To set up the server with an existing encryption settings database:

#### Steps

* Run the `manage-profile setup` command on a [server profile](../pingdirectory_server_administration_guide/pd_ds_server_profiles.html) with the following properties:

  * A `setup-arguments.txt` file including the `--encryptDataWithPreExistingEncryptionSettingsDatabase` argument

  * A `<server-root>/pre-setup/config/encryption-settings/encryption-settings-db` file representing the desired encryption settings database

  * The `pre-setup-dsconfig` directory including one or more `dsconfig` batch files containing changes needed to enable the cipher stream provider

  * Any metadata files contained in the `<server-root>/pre-setup` directory that the cipher stream provider needs to access the encryption settings database.

    The metadata files needed depend on the enabled cipher stream provider:

    * For the file-based cipher stream provider, use the file specified by the cipher stream provider's `password-file` configuration property. If `encryption-metadata-file` has a value, you must also include the file specified by that property.

    * For the Amazon Key Management Service cipher stream provider, use the file specified by the cipher stream provider's `encrypted-metadata-file` configuration property.

    * For the Amazon Secrets Manager cipher stream provider, use the file specified by the cipher stream provider's `encryption-metadata-file` configuration property.

    * For the Azure Key Vault cipher stream provider, use the file specified by the cipher stream provider's `encryption-metadata-file` configuration property.

    * For the Conjur cipher stream provider, use the file specified by the cipher stream provider's `encryption-metadata-file` configuration property.

    * For the PKCS #11 cipher stream provider, use the file specified by the cipher stream provider's `encryption-metadata-file` configuration property.

    * For the Vault cipher stream provider, use the file specified by the cipher stream provider's `vault-encrpytion-metadata-file` configuration property.

### Installing the PingDirectory server with no security enabled

You can install a PingDirectory server in non-interactive mode in a production or QA environment with no security enabled.

#### Steps

* Extract the distribution `.zip` file and, from the server root directory, run the `setup` command with the `--no-prompt` option for non-interactive mode.

  The following example command uses the default root user distinguished name (`cn=Directory Manager`) with the specified `--rootUserPassword` option. You must include the `--acceptLicense` option or the setup generates an error message. The `--instancename` option specifies the name for the server instance and should be unique across all instances in the topology. The `--location` option specifies the name of the location in which the instance will be installed. You should generally configure your topology with a separate location for each data center to allow inter-server communication to prioritize servers in the same location over those in remote locations.

  ##### Example:

  ```shell
  $ ./setup --no-prompt --rootUserPassword "password" \
    --baseDN "dc=example,dc=com" --acceptLicense --ldapPort 389 \
    --instancename Instance1 --location Location1
  ```

### Installing the PingDirectory server with a truststore

You can set up the PingDirectory server in non-interactive mode using an existing truststore for secure communication. This section assumes that you have an existing keystore and truststore with trusted certificates.

#### Steps

* Unzip the distribution `.zip` file and, from the server root directory, run the `setup` command with the `--no-prompt` option for non-interactive mode. The following example enables security using both SSL and StartTLS. It also specifies a JKS keystore and truststore that define the server certificate and trusted CA. The `userRoot` database contents will remain empty and the base DN entry will not be created.

  ##### Example:

  ```shell
  $ ./setup --no-prompt --rootUserPassword "password" \
    --baseDN "dc=example,dc=com" --ldapPort 389 --enableStartTLS \
    --ldapsPort 636 --useJavaKeystore config/keystore.jks \
    --keyStorePasswordFile config/keystore.pin \
    --certNickName server-cert --useJavaTrustStore config/truststore.jks \
    --acceptLicense --instancename Instance1 --location Location1
  ```

  The password to the private key with the keystore is expected to be the same as the password to the keystore. If this is not the case, the private key password can be defined with the admin console or the `dsconfig` command by editing the Trust Manager Provider standard configuration object.

## Installing a lightweight server

Users who want to demo or test a lightweight version of the PingDirectory server on a memory-restricted machine can do so by removing all unused or unneeded configuration objects.

All configuration entries, whether enabled or not, take up some amount of memory to hold the definition and listeners that are notified of changes to those objects.

The configuration framework does not allow you to remove objects that are referenced, and in some cases if you have one configuration object referencing another but really do not need it, then you must first remove the reference to it. If you try to remove a configuration object that is referenced, both `dsconfig` and the admin console should prevent you from removing it and tell you what still references it.

Depending on your test configuration, some example configuration changes that you can make are as follows:

* Reduce the number of worker threads

  Each thread has a stack associated with it, and that consumes memory. If you're running a bare-bones server, then you probably do not have enough load to require a lot of worker threads.

  ```shell
  $ bin/dsconfig set-work-queue-prop \
    --set num-worker-threads:8 \
    --set num-administrative-session-worker-threads:4 \
    --set max-work-queue-capacity:100
  ```

* Reduce the percentage of JVM memory used for the JE database cache

  When you have a memory-constrained environment, you want to ensure that as much memory as possible is available for use during processing and not tied up caching database contents.

  ```shell
  $ bin/dsconfig set-backend-prop --backend-name userRoot --set db-cache-percent:5
  ```

* Disable the Dictionary Password Validator

  The Dictionary Password Validator takes a lot of memory to hold its dictionary. Disabling it frees up some memory. You can delete the other password validators if not needed, such as Attribute Value, Character Set, Length-based, Repeated Characters, Similarity-based, or Unique Characters Password Validator.By default, the Dictionary Password Validator is referenced by the Secure Password Policy and the Root Password Policy. Therefore, you must first enter the following commands to update the password policies so that they no longer reference the validator.

  ```shell
  $ bin/dsconfig set-password-policy-prop --policy-name "Secure Password Policy" --remove password-validator:Dictionary
  $ bin/dsconfig set-password-policy-prop --policy-name "Root Password Policy" --remove password-validator:Dictionary
  ```

  Then, you can disable the Dictionary Password Validator by using the following command:

  ```shell
  $ bin/dsconfig delete-password-validator --validator-name Dictionary
  ```

* Disable the Commonly-Used Passwords Validator

  The Commonly-Used Passwords Validator loads a relatively large dictionary of banned passwords into memory. By default, this validator is referenced by the Secure Password Policy and the Root Password Policy. Therefore, you must first enter the following commands to update the password policies so that they no longer reference the validator.

  ```shell
  $ bin/dsconfig set-password-policy-prop --policy-name "Secure Password Policy" --remove password-validator:Commonly-Used Passwords
  $ bin/dsconfig set-password-policy-prop --policy-name "Root Password Policy" --remove password-validator:Commonly-Used Passwords
  ```

  Then, you can disable the Commonly-Used Passwords Validator by using the following command.

  ```shell
  $ bin/dsconfig delete-password-validator --validator-name Commonly-Used Passwords
  ```

|   |                                                                                                                                              |
| - | -------------------------------------------------------------------------------------------------------------------------------------------- |
|   | There are other items that can be removed, depending on your desired configuration. Contact your authorized support provider for assistance. |

## Installing the server on Windows

Use the `setup.bat` script to install the server on Windows.

### Before you begin

* Make sure that you have set the *JAVA\_HOME* environment variable to the location of your Java installation directory. For more information, see the "Java Runtime Environment" section in [System requirements](pd_ds_system_requirements.html) and [Installing Java](pd_ds_install_java.html).

* Review [Pre-installation considerations](pd_ds_before_you_begin_install.html).

### About this task

Complete the following steps to install the PingDirectory server.

### Steps

1. Extract the distribution `.zip` file.

2. In the Windows Command Prompt or PowerShell, go to the server's root directory, and enter **setup.bat**.

3. Read the Ping Identity End-User License Agreement, and type `yes` to continue.

4. Respond to the prompts. You can enter your own values or press Enter to accept the defaults.

   If you want to see a detailed step-by-step description of the installation, see [Installing the PingDirectory server in interactive mode](#install_pd_ds_interactive) starting with step 3.

5. In the setup summary, review your configuration details, and then select your setup option, or press Enter to select the default (option 1): Set up the server with the parameters you have given.

   #### Result:

   If you select option 1, your PingDirectory server is configured and initialized.

6. If you want to run the server as a Windows service, follow the instructions in [Running the server as a Microsoft Windows service](../pingdirectory_server_administration_guide/pd_ds_run_server_as_ms_windows_service.html).

---

---
title: Installing the PingDirectory Suite of Products
description: PingDirectory offers a highly portable and scalable architecture that runs on multiple platforms and operating systems. The server is specifically optimized for operating systems used in environments that process a large number of entries.
component: pingdirectory
version: 11.1
page_id: pingdirectory:installing_the_pingdirectory_suite_of_products:pd_suite_install_guide
canonical_url: https://docs.pingidentity.com/pingdirectory/11.1/installing_the_pingdirectory_suite_of_products/pd_suite_install_guide.html
llms_txt: https://docs.pingidentity.com/pingdirectory/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: March 21, 2024
---

# Installing the PingDirectory Suite of Products

PingDirectory offers a highly portable and scalable architecture that runs on multiple platforms and operating systems. The server is specifically optimized for operating systems used in environments that process a large number of entries.

This guide describes how to install the PingDirectory server and its add-ons, PingDirectoryProxy, Delegated Admin, and PingDataSync.

It contains instructions for preparing your environment for installation, obtaining or upgrading a Ping Identity license key, downloading the installation packages, and installing the servers. It also describes how to uninstall and upgrade the servers, and how to start, stop, and restart the servers.

---

---
title: Installing the PingDirectoryProxy server
description: After you install the PingDirectory server, you can install and set up the PingDirectoryProxy server.
component: pingdirectory
version: 11.1
page_id: pingdirectory:installing_the_pingdirectory_suite_of_products:pd_proxy_install_dir_proxy_server
canonical_url: https://docs.pingidentity.com/pingdirectory/11.1/installing_the_pingdirectory_suite_of_products/pd_proxy_install_dir_proxy_server.html
llms_txt: https://docs.pingidentity.com/pingdirectory/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: September 13, 2023
page_aliases: ["pd_proxy_install_dps_interactive.adoc", "pd_proxy_install_in_non_interactive_mode.adoc", "pd_proxy_install_first_server_interactive.adoc", "pd_proxy_install_additional_servers.adoc", "pd_proxy_install_first_dps_non_interactive.adoc", "pd_proxy_install_additional_dps_non_interactive.adoc", "pd_proxy_install_dps_truststore_non_interactive.adoc"]
section_ids:
  installing-the-server-in-interactive-mode: Installing the server in interactive mode
  installing-the-first-server: Installing the first server
  steps: Steps
  example: Example:
  choose-from: Choose from:
  choose-from-2: Choose from:
  installing-additional-servers: Installing additional servers
  about-this-task: About this task
  steps-2: Steps
  example-2: Example:
  installing-the-server-in-non-interactive-mode: Installing the server in non-interactive mode
  installing-the-first-server-2: Installing the first server
  about-this-task-2: About this task
  steps-3: Steps
  installing-additional-servers-2: Installing additional servers
  steps-4: Steps
  installing-the-server-with-a-trust-store: Installing the server with a trust store
  about-this-task-3: About this task
  preparing-key-stores-trust-stores-and-pin-files-before-setup: Preparing key stores, trust stores, and .pin files before setup
  steps-5: Steps
---

# Installing the PingDirectoryProxy server

After you install the PingDirectory server, you can install and set up the PingDirectoryProxy server.

You can install using interactive mode, which guides you through the setup, or non-interactive mode, which requires that you enter the appropriate CLI commands for server setup.

## Installing the server in interactive mode

The `setup` command provides an interactive text-based interface to install a PingDirectoryProxy server instance.

### Installing the first server

#### Steps

1. Change to the server root directory.

   ##### Example:

   ```
   cd PingDirectoryProxy
   ```

2. Run the `setup` command.

   ```shell
   $ ./setup
   ```

3. Read the Ping Identity End-User License Agreement, and type `yes` to continue.

4. Press **Enter** to accept the default of `no` in response to adding this new server to an existing topology.

   ```
   Would you like to add this server to an existing Directory Proxy Server topology? (yes / no) [no]:
   ```

5. Enter the fully qualified host name for this server, or press **Enter** to accept the default.

6. Create the initial root user DN for this server, or press **Enter** to accept the default.

7. Enter and confirm a password for this account.

8. To enable the PingDirectoryProxy server services (Configuration, Documentation, and Directory REST API) and admin console over HTTPS, press **Enter** to accept the default. After setup, individual services can be enabled or disabled by configuring the HTTPS Connection Handler.

9. Enter the port where the PingDirectoryProxy server should accept connections from HTTPS clients, or press **Enter** to accept the default.

10. Enter the port where the PingDirectoryProxy server should accept connections from LDAP clients, or press **Enter** to accept the default.

11. The next two options enable LDAPS and StartTLS. Press **Enter** to accept the default (yes), or type **no**. If either are enabled, certificate options are required. To use the Java KeyStore (JKS) or the PKCS#12 key store, the key store path and the key PIN are required. To use the PKCS#11 token, only the key PIN is required.

12. Choose a certificate server option:

    ##### Choose from:

    * `1) Generate self-signed certificate (recommended for testing purposes only)`

    * `2) Use an existing certificate located on a Java Keystore (JKS)`

    * `3) Use an existing certificate located on a PKCS#12 keystore`

    * `4) Use an existing certificate on a PKCS#11 token`

13. Choose the desired encryption for backups and log files from the choices provided:

    ##### Choose from:

    * `Encrypt data with a key generated from an interactively provided passphrase. Using a passphrase (obtained interactively or read from a file) is the recommended approach for new deployments, and you should use the same encryption passphrase when setting up each server in the topology`

    * `Encrypt data with a key generated from a passphrase read from a file`

    * `Encrypt data with a randomly generated key. This option is primarily intended for testing purposes, especially when only testing with a single instance, or if you intend to import the resulting encryption settings definition into other instances in the topology`

    * `Encrypt data with an imported encryption settings definition. This option is recommended if you are adding a new instance to an existing topology that has older server instances with data encryption enabled`

    * `Do not encrypt server data`

14. To configure your PingDirectoryProxy server to use entry balancing, type `yes`, or accept the default `no`. In an entry balancing environment, entries immediately beneath the balancing base DN are divided into disjoint subsets. Each subset of data is handled by a separate set of one or more directory server instances, which replicate this subset of data between themselves. Choosing `yes` will enable more memory be allocated to the server and tools.

15. Choose the option for the amount of memory to assign to this server.

16. Enter an option to set up the server with the current configuration, provide new parameters, or cancel.

17. After setup is complete, choose the next configuration option.

    ```
    This server is now ready for configuration What would you like to do?

       1) Start 'create-initial-proxy-config' to create a basic
          initial configuration (recommended for new users)
       2) Start 'dsconfig' to create a configuration from scratch
       3) Quit

    Enter choice [1]:
    ```

### Installing additional servers

#### About this task

The `setup` command provides an interactive text-based interface to install a PingDirectoryProxy server instance that clones a previously installed PingDirectoryProxy server instance.

#### Steps

1. Change to the server root directory.

   ##### Example:

   ```
   cd PingDirectoryProxy
   ```

2. Use the `setup` command.

   ```shell
   $ ./setup
   ```

3. Read the Ping Identity End-User License Agreement, and type `yes` to continue.

4. Enter `yes` in response to add this new server to an existing topology.

   ```
   Would you like to add this server to an existing Directory Proxy Server topology? (yes / no) [no]: yes
   ```

5. Enter the host name of the PingDirectoryProxy server from which configuration settings are copied during setup.

   ```
   Enter the host name of the peer Directory Proxy Server from which you would like
   to copy configuration settings. [proxy.example.com]:
   ```

6. Type the port number of the peer PingDirectoryProxy server from which configuration settings are copied during setup. You can press **Enter** to accept the default port, which is 389.

   ```
   Enter the port of the peer Directory Proxy Server [389]:
   ```

7. Enter the option corresponding to the type of connection you want to use to connect to the peer PingDirectoryProxy server.

   ```
   How would you like to connect to the peer Directory Proxy Server?
     1) None
     2) SSL
     3) StartTLS

   Enter choice [1]:
   ```

8. Type the root user DN of the peer PingDirectoryProxy server, or press **Enter** to accept the default (`cn=Directory Manager`), and then type and confirm the root user password.

   ```
   Enter the manager account DN for the peer Directory Proxy Server [cn=Directory Manager]:
   Enter the password for cn=Directory Manager:
   ```

9. Enter the host name of the new local PingDirectoryProxy server.

   ```
   Enter the fully qualified host name or IP address of the local host [proxy.example.com]:
   ```

10. Choose the location of your new PingDirectoryProxy server instance or enter a new one.

11. Enter an option to set up the server with the current configuration, provide new parameters, or cancel.

12. After setup is complete, choose the next configuration option.

## Installing the server in non-interactive mode

You can run the `setup` command in non-interactive mode to automate the installation process using a script or to run the command directly from the command line.

The following sections describe how to install the first PingDirectoryProxy server, how to install additional servers, and how to install the server with a trust store.

### Installing the first server

#### About this task

The `setup` command automatically chooses the maximum heap size. You can manually tune the maximum amount of memory devoted to the server's process heap using the `--maxHeapSize` option. The `--maxHeapSize` option is only valid if the `--entryBalancing` option is also present.

If you're using entry balancing, tune the amount of memory devoted to the PingDirectoryProxy server using the `--entryBalancing` option as follows:

```
--entryBalancing --maxHeapSize 1g
```

The amount of memory allowed when using the `--entryBalancing` option is calculated and depends on the amount of system memory available.

#### Steps

1. Run the `setup` command with the `--no-prompt` option.

   The command uses the default root user distinguished name (DN) (`cn=Directory Manager`) with the specified `--rootUserPassword` option. You must include the `--acceptLicense`, `--instanceName`, and `--location` options or the `setup` command will generate an error message.

   ```shell
   $ env JAVA_HOME=/ds/java ./setup --no-prompt \
   --rootUserDN "cn=Directory Manager" \
   --rootUserPassword "password" --ldapPort 389 \
   --acceptLicense \
   --instanceName ds1 --location Denver
   ```

### Installing additional servers

#### Steps

1. Run the `setup` tool with the `--no-prompt` option.

   ```shell
   $ env JAVA_HOME=/ds/java ./setup --no-prompt \
   --rootUserDN "cn=Directory Manager" \
   --rootUserPassword "password" --ldapPort 1389 \
   --localHostName proxy2.example.com \
   --peerHostName proxy1.example.com --peerPort 389 \
   --peerUseNoSecurity --acceptLicense --instanceName ds1 \
   --location austin1
   ```

### Installing the server with a trust store

#### About this task

If you've already configured a trust store, you can run the `setup` command to enable security. The following example enables both SSL and StartTLS security. It also specifies a JKS and trust store that define the server certificate and trusted CA. The passwords for the key store files are defined in the corresponding `.pin` files, where the password is written on the first line of the file.

|   |                                                                                                                                                                                                                                                                                                                    |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | The server expects the password to the private key within the key store to be the same as the password to the key store. If it isn't the same, you can define the private key password within the admin console or using the `dsconfig` command by editing the Key Manager Provider standard configuration object. |

#### Preparing key stores, trust stores, and `.pin` files before `setup`

Running `setup` doesn't copy your key and trust store files or their associated `.pin` files to the server root. You should manually copy those files into the `config` directory of the server root, as follows:

* `config/keystore`

* `config/keystore.pin`

* `config/truststore`

* `config/truststore.pin`

|   |                                                                                                                                                                                                                              |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | If you choose to leave these files in their original locations and supply the original reference paths when running `setup`, don't delete them afterwards. The server uses the files directly from those original locations. |

#### Steps

1. To install a PingDirectoryProxy server with a trust store, run the `setup` command.

   ```shell
   $ env JAVA_HOME=/ds/java ./setup \
     --no-prompt --rootUserDN "cn=Directory Manager" \
     --rootUserPassword "password" --ldapPort 389 \
     --enableStartTLS --ldapsPort 636 \
     --useJavaKeystore /path/to/devkeystore.jks \
     --keyStorePasswordFile /path/to/devkeystore.pin \
     --certNickName server-cert \
     --useJavaTrustStore /path/to/devtruststore.jks \
     --trustStorePasswordFile /path/to/devtruststore.pin \
     --acceptLicense \
     --instanceName ds1 --location Denver

   In order to update the trust store, the password must be provided

   See 'prepare-external-server --help' for general overview

   Testing connection to ds-east-01.example.com:1636 ..... Done
   Testing 'cn=Proxy User,cn=Root DNs,cn=config' access .....
   Created 'cn=Proxy User,cn=Root DNs,cn=config'

   Testing 'cn=Proxy User,cn=Root DNs,cn=config' access ..... Done
   Testing 'cn=Proxy User,cn=Root DNs,cn=config' privileges ..... Done
   Verifying backend 'dc=example,dc=com' ..... Done
   ```

---

---
title: Installing the servers
description: The setup tool allows you to quickly install and configure a stand-alone server instance.
component: pingdirectory
version: 11.1
page_id: pingdirectory:installing_the_pingdirectory_suite_of_products:pd_suite_installing_the_servers
canonical_url: https://docs.pingidentity.com/pingdirectory/11.1/installing_the_pingdirectory_suite_of_products/pd_suite_installing_the_servers.html
llms_txt: https://docs.pingidentity.com/pingdirectory/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: December 18, 2023
section_ids:
  server-installation-modes: Server installation modes
  installation-instructions: Installation instructions
---

# Installing the servers

The `setup` tool allows you to quickly install and configure a stand-alone server instance.

## Server installation modes

You can run the tool in either of the following modes:

* Interactive command-line mode

  This mode prompts for information during the installation process. To start the installation in this mode, run the `setup` command without any options.

* Non-interactive command-line mode

  This mode is designed for setup scripts to automate installations or for command-line usage. To start the installation in this mode, run the `setup` command with the `--no-prompt` option as well as the other arguments required to define the appropriate initial configuration.

|   |                                                                                                                                 |
| - | ------------------------------------------------------------------------------------------------------------------------------- |
|   | Make sure you perform all installation steps while logged on to the system as the user or role under which the server will run. |

|   |                                                                                  |
| - | -------------------------------------------------------------------------------- |
|   | Support for Java 11 has been deprecated and will be removed in a future release. |

## Installation instructions

See the instructions in the following topics to install the PingDirectory suite of products:

* [Installing the PingDirectory server](pd_ds_install_server.html)

* [Installing the PingDirectoryProxy server](pd_proxy_install_dir_proxy_server.html)

* [Installing Delegated Admin](pd_da_install_delegated_admin.html)

* [Installing the PingDataSync server](pd_sync_installing_pds.html)

---

---
title: Managing system entropy
description: Linux uses entropy to calculate random data that is used by the system in cryptographic operations.
component: pingdirectory
version: 11.1
page_id: pingdirectory:installing_the_pingdirectory_suite_of_products:pd_ds_manage_system_entropy
canonical_url: https://docs.pingidentity.com/pingdirectory/11.1/installing_the_pingdirectory_suite_of_products/pd_ds_manage_system_entropy.html
llms_txt: https://docs.pingidentity.com/pingdirectory/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: August 12, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Managing system entropy

Linux uses entropy to calculate random data that is used by the system in cryptographic operations.

## About this task

Some environments with low entropy might have intermittent performance issues with SSL-based communication. This is more typical on virtual machines but can occur in physical instances as well.

## Steps

* For best results, monitor the `kernel.random.entropy_avail` in `sysctl` value.

---

---
title: Obtaining a Ping Identity license key
description: License keys are required to install, update, and renew all Ping Identity products.
component: pingdirectory
version: 11.1
page_id: pingdirectory:installing_the_pingdirectory_suite_of_products:pd_ds_ping_license_keys
canonical_url: https://docs.pingidentity.com/pingdirectory/11.1/installing_the_pingdirectory_suite_of_products/pd_ds_ping_license_keys.html
llms_txt: https://docs.pingidentity.com/pingdirectory/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: August 12, 2024
section_ids:
  how-to-obtain-a-license: How to obtain a license
  when-you-need-a-license: When you need a license
  how-to-specify-a-license: How to specify a license
  how-to-view-the-license-status: How to view the license status
  license-expiration: License expiration
---

# Obtaining a Ping Identity license key

License keys are required to install, update, and renew all Ping Identity products.

## How to obtain a license

To obtain a license key, contact your account representative or use the [Ping Identity licensing portal](https://www.pingidentity.com/en/account/request-license-key.html).

## When you need a license

A license is required for setting up a new single server instance and can be used site-wide for all servers in an environment. Additionally, you must obtain a new license when updating a server to a new major version, such as when upgrading from 8.3 to 9.0. When cloning a server instance with a valid license, you do not need a new license.

|   |                                                          |
| - | -------------------------------------------------------- |
|   | The upgrade process displays a prompt for a new license. |

## How to specify a license

* Specify a license at setup.

  You have these options:

  * Use the `--licenseKeyFile` *\<path-to-license>* option with `setup`.

  * Copy the license file to the server root directory and then run the `setup` tool. The tool discovers the license file.

* Specify a license after setup

  Use the admin console or `dsconfig` (in the **Topology** section, select **License**).

  |   |                                                                                       |
  | - | ------------------------------------------------------------------------------------- |
  |   | Placing the new license file in the server root directory does not work in this case. |

## How to view the license status

To view the details of a license, including its expiration, you have these options:

* Use the server's `status` tool.

* In the admin console, go to the **Status** page and search for **License** on the **Monitors** tab.

## License expiration

The server provides a notification as the expiration date approaches.

Before a license expires, obtain a new one and install it by using `dsconfig` or the admin console. Learn more in [Upgrading a PingDirectory license](pd_ds_upgrade_license.html).

|   |                                                                                                    |
| - | -------------------------------------------------------------------------------------------------- |
|   | An expiring license causes alerts and alarms but does not affect the functionality of the product. |