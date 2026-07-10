---
title: Compatible database drivers
description: PingFederate is compatible with the following vendor-specific Java database connectivity (JDBC) drivers.
component: pingfederate
version: 13.1
page_id: pingfederate:installing_and_uninstalling_pingfederate:pf_compatible_database_drivers
canonical_url: https://docs.pingidentity.com/pingfederate/13.1/installing_and_uninstalling_pingfederate/pf_compatible_database_drivers.html
llms_txt: https://docs.pingidentity.com/pingfederate/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: May 4, 2026
---

# Compatible database drivers

PingFederate is compatible with the following vendor-specific Java database connectivity (JDBC) *(tooltip: \<div class="paragraph">
\<p>A Java API that allows Java programs to interact with databases.\</p>
\</div>)* drivers.

| Database server                                                      | Driver information                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| -------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Amazon Aurora MySQL 3.12.0 (compatible with MySQL 8.0.44)            | * Driver version information

  aws-advanced-jdbc-wrapper version 2.6.6 with mysql-connector-j version 9.5.0&#xA;&#xA;If you use the AWS wrapper driver, you must deploy the original driver and the wrapper driver together. Learn more in Using the AWS Advanced Wrapper in the AWS documentation.* Driver class

  `software.amazon.jdbc.Driver`

* JDBC URL

  `jdbc:mysql://databaseservername/databasename`

* Database location

  Regional

* Database features

  One writer and multiple readers	If you're using Aurora's high-availability features, the AWS JDBC Driver for MySQL client driver may be used instead of the MySQL Connector/J driver.                       |
| Amazon Aurora PostgreSQL (compatible with PostgreSQL 16.13 and 17.9) | - Driver version information

  aws-advanced-jdbc-wrapper version 2.6.6 with postresql versions 42.7.5&#xA;&#xA;If you use the AWS wrapper driver, you must deploy the original driver and the wrapper driver together. Learn more in Using the AWS Advanced Wrapper in the AWS documentation.- Driver class

  `software.amazon.jdbc.Driver`

- JDBC URL

  `jdbc:postgresql://databaseservername/databasename`

- Database features

  One writer and multiple readers                                                                                                                                                                                                               |
| Microsoft SQL Server 2016 SP2, 2017, 2019, and 2022                  | * Driver version information

  sqljdbc version 13.4.0

* Driver class

  `com.microsoft.sqlserver.jdbc.SQLServerDriver`

* JDBC URL

  `jdbc:sqlserver://databaseservername;databaseName=databasename`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| Microsoft Azure SQL Managed Instance                                 | - Driver version information

  sqljdbc version 13.5.0

- Driver class

  `com.microsoft.sqlserver.jdbc.SQLServerDriver`

- JDBC URL

  `jdbc:sqlserver://databaseservername;databaseName=databasename`&#xA;&#xA;PingFederate supports additional authentication methods which can be specified in the JDBC URL. For example, jdbc:sqlserver://databaseservername;databaseName=databasenameauthentication=ActiveDirectoryManagedIdentity&#xA;&#xA;You need to add extra dependencies to PingFederate to use these methods. These dependencies vary according to the JDBC driver and the authentication method. Learn more in Client setup requirements in the Microsoft documentation. |
| Oracle Database 12c Release 2 and 19c                                | * Driver version information

  ojdbc11 version 23.26.2.0.0

* Driver class

  `oracle.jdbc.OracleDriver`

* JDBC URL

  `jdbc:oracle:thin:@databaseservername/servicename`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Oracle MySQL 8.0 and 8.4                                             | - Driver version information

  mysql-connector-j version 9.7.0&#xA;&#xA;Don't use MySQL driver version 9.3, as it isn't compatible with PingFederate.- Driver class

  `com.mysql.cj.jdbc.Driver`

- JDBC URL

  `jdbc:mysql://databaseservername/databasename`                                                                                                                                                                                                                                                                                                                                                                                                                       |
| PostgreSQL 13.4, 16.4, 17.0, and 18.0                                | * Driver version information

  postgresql version 42.7.11

* Driver class

  `org.postgresql.Driver`

* JDBC URL

  `jdbc:postgresql://databaseservername/databasename`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |

For additional information about these drivers, contact the respective vendors.

---

---
title: Installing and uninstalling PingFederate
description: PingFederate operates as a standalone server based on Java EE application server technology. This section shows you how to properly install PingFederate.
component: pingfederate
version: 13.1
page_id: pingfederate:installing_and_uninstalling_pingfederate:pf_installing_uninstalling_pf
canonical_url: https://docs.pingidentity.com/pingfederate/13.1/installing_and_uninstalling_pingfederate/pf_installing_uninstalling_pf.html
llms_txt: https://docs.pingidentity.com/pingfederate/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: September 3, 2025
section_ids:
  deployment-options: Deployment options
  related-links: Related links
---

# Installing and uninstalling PingFederate

PingFederate operates as a standalone server based on Java EE application server technology. This section shows you how to properly install PingFederate.

A new installation involves:

* Determining the deployment architecture

* Reviewing [system](pf_system_requirements.html) and [port](pf_port_requirement.html) requirements

* [Installing a Java runtime environment](pf_install_java.html)

* [Installing PingFederate](pf_installing_pf.html)

* Completing the Initial Setup wizard

|   |                                                                                                                                                                                                                                                                                                          |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | To avoid issues with browsers honoring [Private Network Access](https://wicg.github.io/private-network-access/) security practices, you should make PingFederate accessible on a public network address if you intend to use it with applications or partners that would be considered public resources. |

## Deployment options

Depending on your needs and infrastructure capabilities, you can choose a standalone or proxy configuration. For information about configuring proxy settings, see [Configuring incoming proxy settings](../administrators_reference_guide/help_systemoptionstasklet_systemoptionsstate.html) and [Configuring forward proxy server settings](../administrators_reference_guide/pf_configure_forward_proxy_server_settings.html).

The following diagram illustrates a standalone PingFederate deployment in a DMZ.

![A diagram showing installation in a DMZ](_images/pf_standalone_config_dmz.png)

In this configuration, the users access PingFederate through a web application server, an enterprise identity management (EIM) system, or both. PingFederate then retrieves information from a datastore to use in processing the transaction.

You can also deploy PingFederate with a proxy server. The following diagram depicts a proxy-server configuration in which users and web browsers access the proxy. The proxy then communicates with PingFederate to request single sign-on (SSO) *(tooltip: \<div class="paragraph">
\<p>The process of authenticating an identity (signing on) at one website (usually with a user ID and password) and then accessing resources secured by other domains without reauthenticating.\</p>
\</div>)*.

![A diagram showing a proxy-server configuration in which users and web browsers access the proxy](_images/pf_proxy_server_config.png)

## Related links

* [Upgrading PingFederate](../upgrading_pingfederate/pf_upgrade_pf.html)

* [Uninstalling PingFederate](pf_uninstall_pf.html)

---

---
title: Installing Java
description: PingFederate requires a Java Runtime Environment (JRE) to be installed on your server.
component: pingfederate
version: 13.1
page_id: pingfederate:installing_and_uninstalling_pingfederate:pf_install_java
canonical_url: https://docs.pingidentity.com/pingfederate/13.1/installing_and_uninstalling_pingfederate/pf_install_java.html
llms_txt: https://docs.pingidentity.com/pingfederate/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: September 10, 2025
section_ids:
  about-this-task: About this task
  steps: Steps
  example: Example:
---

# Installing Java

PingFederate requires a Java Runtime Environment (JRE) *(tooltip: \<div class="paragraph">
\<p>A software layer that provides the class libraries and resources needed for a Java program to run.\</p>
\</div>)* to be installed on your server.

## About this task

PingFederate has been tested in the following Java environments:

* Amazon Corretto 17, 21, and 25

* OpenJDK 17, 21, and 25

* Oracle Java SE Development Kit 17 LTS, 21 LTS, and 25 LTS

|   |                                                                                                                                                                                                  |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | Ping Identity Java Support Policy applies. Learn more in [Java Support Policy](https://support.pingidentity.com/s/article/PingIdentity-Java-Support-Policy) in the Ping Identity Knowledge Base. |

## Steps

1. Download and install a Java runtime.

2. Set the *JAVA\_HOME* environment variable to the Java installation directory path and add its `bin` directory to the *PATH* environment variable.

   ### Example:

   ```
   JAVA_HOME=C:\Program Files\Java\jdk-17
   PATH=%JAVA_HOME%\bin
   ```

   |   |                                                                                                                                                                                                                                                                                                                                                                      |
   | - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | If you intend to use the PingFederate installer for Windows or run PingFederate as a service, you must set the *JAVA\_HOME* environment variable and modify the *PATH* environment variable at the system level. If you are not using the PingFederate installer or running PingFederate as a service, you can set the variables at either the system or user level. |

   |   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
   | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | When running PingFederate on Windows, switching the Java version from 11 to 17, 21, or 25 prevents the service from running, and you won't be able to start PingFederate. The problem occurs because garbage collection logging configuration arguments that are used by Java 17, 21, and 25 are incompatible with those used by Java 11.To change Java versions:1) Run `<pf_install>\pingfederate\sbin\win-x86-64\uninstall-service.bat` to de-register the PingFederate service.

   2) Install the new Java version and update the *JAVA\_HOME* and *PATH* environment variables.

   3) Run `<pf_install>\pingfederate\sbin\win-x86-64\install-service.bat` to register the PingFederate service. |

---

---
title: Installing PingFederate
description: You can install PingFederate on Windows and Linux operating systems.
component: pingfederate
version: 13.1
page_id: pingfederate:installing_and_uninstalling_pingfederate:pf_installing_pf
canonical_url: https://docs.pingidentity.com/pingfederate/13.1/installing_and_uninstalling_pingfederate/pf_installing_pf.html
llms_txt: https://docs.pingidentity.com/pingfederate/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: March 24, 2025
---

# Installing PingFederate

You can install PingFederate on Windows and Linux operating systems.

Install PingFederate using the following methods:

* Install PingFederate on a Windows system by running the installer for Windows or by extracting the distribution `.zip` archive. Using the installer for Windows is the preferred method.

* Install PingFederate on a Linux system by extracting the distribution `.zip` archive.

|   |                                                                                                                                                                               |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | This documentation refers to the installation directory path where the `pingfederate` directory is located as *\<pf\_install>*. For example, `<pf_install>/pingfederate/bin`. |

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | To avoid future problems with automated upgrades, do not rename the installed `pingfederate` directory.If you are installing multiple instances of PingFederate on the same machine, such as a console node and an engine node in a clustered environment, install each instance using a unique `<pf_install>` directory.If you are upgrading an existing PingFederate environment, see [Upgrading PingFederate](../upgrading_pingfederate/pf_upgrade_pf.html). |

Click the corresponding tabs for your preferred installation method.

---

---
title: Installing PingFederate on Linux systems
description: See System requirements for a list of qualified Linux operating systems.
component: pingfederate
version: 13.1
page_id: pingfederate:installing_and_uninstalling_pingfederate:pf_install_pf_on_linux_systems
canonical_url: https://docs.pingidentity.com/pingfederate/13.1/installing_and_uninstalling_pingfederate/pf_install_pf_on_linux_systems.html
llms_txt: https://docs.pingidentity.com/pingfederate/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: February 2, 2023
section_ids:
  before-you-begin: Before you begin
  about-this-task: About this task
  steps: Steps
  result: Result:
  next-steps: Next steps
  related-links: Related links
---

# Installing PingFederate on Linux systems

## Before you begin

* See [System requirements](pf_system_requirements.html) for a list of qualified Linux operating systems.

* [Generate a license key](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_generate_new_license_key.html).

* Ensure you are signed on to your system with sufficient privileges to install and run an application. You must install and run PingFederate under a local user account.

* Verify that you have installed the Java Runtime Environment (JRE) and that you have set the required environment variables correctly. For more information, see [Installing Java](pf_install_java.html).

## About this task

To install PingFederate on a Linux system using the distribution `.zip` archive:

## Steps

1. Download the latest version of the PingFederate Server distribution `.zip` archive from the [Downloads website](https://www.pingidentity.com/en/resources/downloads/pingfederate.html).

2. Extract the archive into the target installation directory.

3. Start PingFederate manually by running `<pf_install>/pingfederate/bin/run.sh`.

   |   |                                                                                                 |
   | - | ----------------------------------------------------------------------------------------------- |
   |   | To configure PingFederate to run as a service on Linux, install PingFederate on Linux manually. |

   ### Result:

   The startup process is complete when you see the following message.

   ```
   PingFederate running...
   ```

## Next steps

If your organization plans to manage keys and certificates using a hardware security module (HSM), see [Supported hardware security modules](../getting_started_with_pingfederate/pf_supported_hardware_security_modules.html).

## Related links

* [memoryoptions and installation](../performance_tuning_guide/pf_memoryoptions_install.html)

* [Fine-tuning JVM options](../performance_tuning_guide/pf_fine_tuning_jvm_option.html)

---

---
title: Installing PingFederate on Windows
description: Generate a license key.
component: pingfederate
version: 13.1
page_id: pingfederate:installing_and_uninstalling_pingfederate:pf_install_pf_on_windows
canonical_url: https://docs.pingidentity.com/pingfederate/13.1/installing_and_uninstalling_pingfederate/pf_install_pf_on_windows.html
llms_txt: https://docs.pingidentity.com/pingfederate/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: February 2, 2023
section_ids:
  before-you-begin: Before you begin
  about-this-task: About this task
  steps: Steps
  choose-from: Choose from:
  next-steps: Next steps
  related-links: Related links
---

# Installing PingFederate on Windows

## Before you begin

* [Generate a license key](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_generate_new_license_key.html).

* Ensure you are signed on to your Windows system with sufficient privileges to install and run an application. PingFederate needs read, write, and execute permissions to function.

* Verify that you have installed the Java Runtime Environment (JRE) and that you have set the required environment variables correctly. Learn more in [Installing Java](pf_install_java.html).

## About this task

You can install PingFederate on a Windows system using the installer for Windows or the distribution `.zip` archive. Using the installer for Windows is the preferred method.

|   |                                                                                                                                                                                                                              |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | To configure PingFederate to run as a service on Windows, install PingFederate on Windows manually. Learn more in [Installing the PingFederate service on Windows manually](pf_install_pf_service_on_windows_manually.html). |

To install PingFederate:

## Steps

1. Install PingFederate using the installer for Windows or the distribution `.zip` archive:

   ### Choose from:

   * To install using the PingFederate installer for Windows:

     1. Download the PingFederate installer for Windows from the Ping Identity [website](https://www.pingidentity.com/en/resources/downloads/pingfederate.html).

     2. Double-click the `.msi` file to open the PingFederate **Setup Wizard**, and follow the instructions to complete the installation.

        PingFederate is configured to run as a service and starts automatically at the end of the installation process.

        |   |                                                                                                                                                                                                                                                                                                                                                                                             |
        | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
        |   | The PingFederate installer for Windows installs only one instance of PingFederate on a Windows server. If you need additional PingFederate instances on the same Windows server, install them using the distribution `.zip` archive.You must manually configure various port settings in the `<pf_install>/pingfederate/bin/run.properties` file for each instance to avoid port conflicts. |

   * To install PingFederate using the distribution `.zip` archive:

     1. Download the distribution `.zip` archive from the Ping Identity [website](https://www.pingidentity.com/en/resources/downloads/pingfederate.html). The distribution `.zip` archive is identical for both Windows and Linux.

     2. Extract the file into an installation directory.

2. If you have installed PingFederate by extracting the distribution `.zip` archive, start PingFederate manually by running `<pf_install>/pingfederate/bin/run.bat`.

   Wait for the script to finish. The startup process completes when you see the following message.

   ```json
   PingFederate running...
   ```

   |   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
   | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | When running PingFederate for Windows, switching the Java version from 11 to 17, or 11 to 21, prevents the service from running, and you won't be able to start PingFederate. The problem occurs because garbage collection logging configuration arguments that are used by Java 17 and 21 are incompatible with those used by Java 11.To change Java versions:1) Run `<pf_install>\pingfederate\sbin\win-x86-64\uninstall-service.bat` to de-register the PingFederate service.

   2) Install the new Java version and update the *JAVA\_HOME* and *PATH* environment variables.

   3) Run `<pf_install>\pingfederate\sbin\win-x86-64\install-service.bat` to register the PingFederate service. |

## Next steps

If your organization plans to manage keys and certificates using a hardware security module (HSM), see [Supported hardware security modules](../getting_started_with_pingfederate/pf_supported_hardware_security_modules.html).

## Related links

* [memoryoptions and installation](../performance_tuning_guide/pf_memoryoptions_install.html)

* [Fine-tuning JVM options](../performance_tuning_guide/pf_fine_tuning_jvm_option.html)

---

---
title: Installing the PingFederate service on Linux manually
description: Generate a license key.
component: pingfederate
version: 13.1
page_id: pingfederate:installing_and_uninstalling_pingfederate:pf_install_pf_service_on_linux_manually
canonical_url: https://docs.pingidentity.com/pingfederate/13.1/installing_and_uninstalling_pingfederate/pf_install_pf_service_on_linux_manually.html
llms_txt: https://docs.pingidentity.com/pingfederate/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: February 2, 2023
section_ids:
  before-you-begin: Before you begin
  about-this-task: About this task
  steps: Steps
  result: Result:
  example: Example:
  example-2: Example:
  next-steps: Next steps
  related-links: Related links
---

# Installing the PingFederate service on Linux manually

## Before you begin

* [Generate a license key](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_generate_new_license_key.html).

* Ensure you are signed on to your system with sufficient privileges to install and run an application.

* Verify that you have installed the Java Runtime Environment (JRE) and that you have set the required environment variables correctly. For more information, see [Installing Java](pf_install_java.html) in the PingFederate Server documentation.

## About this task

If you have not installed PingFederate on Linux using the distribution `.zip` archive, you can install it manually. To install the PingFederate service on Linux manually:

## Steps

1. Download the distribution `.zip` archive from the Ping Identity [Downloads](https://www.pingidentity.com/en/resources/downloads/pingfederate.html) website.

2. Extract the file into an installation directory, `<pf_install>`.

3. Create a new local user account for the PingFederate service, such as `pingfederate`.

   |   |                                                      |
   | - | ---------------------------------------------------- |
   |   | The service account is referred to as *\<pf\_user>*. |

4. Change the ownership of the PingFederate installation directory `<pf_install>` and update the read-write permissions by running the following commands:

   ```
   chown -R <pf_user>  <pf_install>
   chmod -R 775  <pf_install>
   ```

5. If the operating system supports systemd, install the PingFederate unit file:

   1. Edit the `<pf_install>/pingfederate/sbin/linux/pingfederate.service` systemd unit file.

      Replace the following variables with information from your environment:

      * PF\_VERSION

        The version of PingFederate.

      * PF\_USER

        The local user account for the PingFederate service.

      * PF\_HOME

        The `<pf_install>/pingfederate` directory.For example, if `<pf_install>` is `/opt/identity.fed`, replace `${PF_HOME}` with `/opt/identity.fed/pingfederate`.

      * PF\_JAVA\_HOME

        The *\<JAVA\_HOME>* environment variable value (a directory).

   2. Copy the `pingfederate.service` file to the systemd unit files directory, for example, `/etc/systemd/system`.

      |   |                                                                                                                                                                                                         |
      | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
      |   | Depending on the operating system, the exact location might vary. Consult your system administrators as needed. The rest of the step assumes `/etc/systemd/system` is the systemd unit files directory. |

   3. Run the following command to update the read-write permissions of the `pingfederate.service` systemd unit file:

      ```
      chmod 664 /etc/systemd/system/pingfederate.service
      ```

   4. Run the following commands to load the new system configuration changes and start the PingFederate service:

      ```
      systemctl daemon-reload ;\
      systemctl start pingfederate
      ```

   5. Run the following commands to configure the PingFederate service to start automatically as the server boots:

      ```
      systemctl enable pingfederate ;\
      systemctl daemon-reload ;\
      systemctl restart pingfederate
      ```

      ### Result:

      After setting up the PingFederate systemd unit file, you can run the following `systemctl` command to manage the PingFederate service:

      ```
      systemctl start pingfederate
      systemctl stop pingfederate
      systemctl restart pingfederate
      systemctl status pingfederate
      ```

6. If the operating system supports SysV initialization, follow these steps to install the PingFederate script.

   1. Edit the `<pf_install>/pingfederate/sbin/linux/pingfederate` script.

      Replace the following statements with information from your environment:

      * PF\_HOME=*$PF\_HOME*

        Replace *$PF\_HOME* with the `<pf_install>/pingfederate` directory.For example, if `<pf_install>` is `/opt/identity.fed`, replace *$PF\_HOME* with `/opt/identity.fed/pingfederate`.

      * USER="*pingfederate*"

        If the PingFederate service account is not `pingfederate`, replace *\<pingfederate>* with the local user account for the PingFederate service.For example, if *\<pf\_user>* is `pingfed`, replace *\<pingfederate>* with `pingfed`.

        ### Example:

      * Example (truncated)

        If `<pf_install>` and *\<pf\_user>* are `/opt/identity.fed` and `pingfederate` respectively, the required modifications are:

        ```
        ...
        PF_HOME=/opt/identity.fed/pingfederate
        DIR="$PF_HOME/sbin"
        USER="pingfederate"
        ...
        ```

   2. Copy the `pingfederate` script to the SysV initialization directory, for example, `/etc/rc.d/init.d`.

      The exact location might vary, depending on the operating system. Consult your system administrators, as needed. The rest of the step assumes `/etc/rc.d/init.d` is the SysV initialization directory.

   3. Run the following command to update the read-write permissions of the `pingfederate` SysV initialization script:

      ```
      chmod 755 /etc/rc.d/init.d/pingfederate
      ```

   4. Configure the operating system to start the PingFederate service at various runlevels.

      On an RHEL server, you can use the **Service Configuration** utility to do so.

      Alternatively, the initialization directories associated with various runlevels can accept manual symbolic links of the `pingfederate` script by running the `ln -s <source> <target>` command.

      ### Example:

      You can create the following symbolic links on an RHEL server where runlevels 2 and 4 are not used:

      ```
      ln -s /etc/rc.d/init.d/pingfederate /etc/rc3.d/S84pingfederate
      ln -s /etc/rc.d/init.d/pingfederate /etc/rc5.d/S84pingfederate
      ln -s /etc/rc.d/init.d/pingfederate /etc/rc0.d/K15pingfederate
      ln -s /etc/rc.d/init.d/pingfederate /etc/rc1.d/K15pingfederate
      ln -s /etc/rc.d/init.d/pingfederate /etc/rc6.d/K15pingfederate
      ```

   |   |                                                                                                                                         |
   | - | --------------------------------------------------------------------------------------------------------------------------------------- |
   |   | Some operating systems might require a restart of the system to activate the new scripts. Consult your system administrators as needed. |

## Next steps

After setting up the PingFederate SysV initialization script, you can use the `Service Configuration` utility or run the following `service` commands to manage the PingFederate service:

```
service pingfederate start
service pingfederate stop
service pingfederate restart
service pingfederate status
```

## Related links

* [memoryoptions and installation](../performance_tuning_guide/pf_memoryoptions_install.html)

* [Fine-tuning JVM options](../performance_tuning_guide/pf_fine_tuning_jvm_option.html)

---

---
title: Installing the PingFederate service on Windows manually
description: Generate a license key.
component: pingfederate
version: 13.1
page_id: pingfederate:installing_and_uninstalling_pingfederate:pf_install_pf_service_on_windows_manually
canonical_url: https://docs.pingidentity.com/pingfederate/13.1/installing_and_uninstalling_pingfederate/pf_install_pf_service_on_windows_manually.html
llms_txt: https://docs.pingidentity.com/pingfederate/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: February 6, 2023
section_ids:
  before-you-begin: Before you begin
  about-this-task: About this task
  steps: Steps
  result: Result
  related-links: Related links
---

# Installing the PingFederate service on Windows manually

## Before you begin

* [Generate a license key](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_generate_new_license_key.html).

* Ensure you are signed on to your Windows system with sufficient privileges to install and run an application. PingFederate needs read, write, and execute permissions to function.

* Verify that you have installed the Java Runtime Environment (JRE) and that you have set the required environment variables correctly. Learn more in [Installing Java](pf_install_java.html).

## About this task

|   |                                                                                                                                                                                                                              |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | If you have installed PingFederate using the installer for Windows, skip these steps because PingFederate has already been configured to run as a service and to start automatically at the end of the installation process. |

To install the PingFederate service manually:

## Steps

1. Download the distribution `.zip` archive from the Ping Identity [website](https://www.pingidentity.com/en/resources/downloads/pingfederate.html).

   The distribution `.zip` archive is identical for both Windows and Linux.

2. Extract the archive into an installation directory, `<pf_install>`.

3. Start PowerShell or Command Prompt as an administrator.

4. Run the `<pf_install>\pingfederate\sbin\win-x86-64\install-service.bat` file.

5. Go to **Control Panel > Administrative Tools > Services** to open the management console.

6. Right-click the **PingFederate** service and select **Start**.

## Result

The PingFederate service starts automatically on reboot.

## Related links

* [memoryoptions and installation](../performance_tuning_guide/pf_memoryoptions_install.html)

* [Fine-tuning JVM options](../performance_tuning_guide/pf_fine_tuning_jvm_option.html)

---

---
title: Port requirements
description: The following table summarizes the ports and protocols that PingFederate uses to communicate with external components. This information provides guidance for firewall administrators to ensure the correct ports are available across network segments.
component: pingfederate
version: 13.1
page_id: pingfederate:installing_and_uninstalling_pingfederate:pf_port_requirement
canonical_url: https://docs.pingidentity.com/pingfederate/13.1/installing_and_uninstalling_pingfederate/pf_port_requirement.html
llms_txt: https://docs.pingidentity.com/pingfederate/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: October 5, 2022
---

# Port requirements

The following table summarizes the ports and protocols that PingFederate uses to communicate with external components. This information provides guidance for firewall administrators to ensure the correct ports are available across network segments.

|   |                                                                                                                                                                                                                                       |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Direction refers to the direction of the initial requests relative to PingFederate. Inbound refers to requests PingFederate receives from external components. Outbound refers to requests PingFederate sends to external components. |

**PingFederate required ports and protocols**

| Service                                                   | Protocol, direction, transport, default port       | Source                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | Destination                                                            | Description                                                                                                                                                                                                                                                                                  |
| --------------------------------------------------------- | -------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Administrative console                                    | HTTPS, inbound, TCP, 9999                          | Browsers accessing the administrative console, REST calls to the administrative application programming interface (API) *(tooltip: \<div class="paragraph">&#xA;\<p>A specification of interactions available for building software to access an application or service.\</p>&#xA;\</div>)*, and web service calls to the Connection Management Service.Applicable to the console node in a clustered PingFederate environment.                                                                                                                                                                                                                                                                                                                                                                                  | Administrative node                                                    | Used for incoming requests to the administrative console. Configurable in the `run.properties` file.                                                                                                                                                                                         |
| Administrative console                                    | HTTPS, outbound, TCP, 443                          | Administrator accessing online documentation.Applicable to the console node in a clustered PingFederate environment.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | docs.pingidentity.com                                                  | Used for accessing online documentation from the administrative console.                                                                                                                                                                                                                     |
| Runtime engine                                            | HTTPS, inbound, TCP, 9031 (and 9032 if configured) | Browsers accessing the runtime server for single sign-on (SSO) *(tooltip: \<div class="paragraph">&#xA;\<p>The process of authenticating an identity (signing on) at one website (usually with a user ID and password) and then accessing resources secured by other domains without reauthenticating.\</p>&#xA;\</div>)* or single logout (SLO) *(tooltip: \<div class="paragraph">&#xA;\<p>The process of signing a user out of multiple sites where the user has started a SSO session.\</p>&#xA;\</div>)*. Web service calls to the SSO Directory Service. REST calls to the OAuth Client Management Service, the OAuth Access Grant Management Service, the Persistent Grant Management API, and the Session Revocation API.Applicable to all runtime engine nodes in a clustered PingFederate environment. | Runtime engine nodes                                                   | Used for incoming requests to the runtime engine.Configurable in the `run.properties` file.                                                                                                                                                                                                  |
| Cluster traffic                                           | JGroups, inbound, TCP, 7600                        | PingFederate peer servers in a clustered PingFederate environment.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | Administrative node and runtime engine nodes                           | Used for communications between engine nodes in a cluster when the transport mode for cluster traffic is set to TCP (the default behavior).Configurable in the `run.properties` file.                                                                                                        |
| Cluster traffic                                           | JGroups, inbound, TCP, 7700                        | PingFederate peer servers in a clustered PingFederate environment.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | Administrative node and runtime engine nodes                           | Used by other nodes in the cluster as part of the cluster's failure-detection mechanism when the transport mode for cluster traffic is set to TCP (the default behavior).Configurable in the `run.properties` file.                                                                          |
| PingOne connections (if configured)                       | HTTPS, outbound, TCP, 443                          | All nodes                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | pingone.com                                                            | The administrative node uses PingOne APIs to create connections to PingOne. Engine nodes use PingOne APIs to obtain access tokens and call PingOne services.                                                                                                                                 |
| PingOne for Enterprise integration (if configured)        | HTTPS and secure WebSocket, TCP, 443               | PingFederateApplicable to the console node in a clustered PingFederate environment.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | pingone.com                                                            | Used for communications between PingFederate and PingOne for Enterprise for establishing and maintaining a managed SP connection to PingOne for Enterprise, monitoring of PingFederate from the PingOne admin portal, authenticating end users against the PingOne for Enterprise Directory. |
| Cluster traffic (if configured)                           | JGroups, outbound, TCP, 443                        | PingFederate peer servers in a clustered PingFederate environment.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | Amazon Simple Storage Service (Amazon S3) or an OpenStack Swift server | Used by all nodes when the optional dynamic discovery mechanism is enabled.                                                                                                                                                                                                                  |
| Cluster traffic                                           | JGroups, inbound,UDP, 7601                         | PingFederate peer servers in a clustered PingFederate environment.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | Administrative node and runtime engine nodes                           | Used for communications between engine nodes in a cluster when the transport mode for cluster traffic is set to UDP. By default, the transport mode is TCP.Configurable in the`run.properties` file.                                                                                         |
| Active Directory domains/ Kerberos realms (if configured) | Kerberos, outbound, TCP or UDP, 88                 | PingFederate                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | Windows domain controllers                                             | Used for communications between PingFederate and Windows domain controllers for the purpose of Kerberos authentication.                                                                                                                                                                      |
| reCAPTCHA (if configured)                                 | HTTPS, outbound, TCP, 443                          | PingFederate                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | www\.google.com/recaptcha/api/site verify                              | Used by the HTML Form Adapter when invisible reCAPTCHA from Google is enabled to prevent automated attacks.                                                                                                                                                                                  |
| Administration notification                               | SMTP, outbound, TCP, 25 (465 if SMTPS)             | All nodes                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | SMTP server                                                            | Used to send notification messages for various events. For more information, see [Runtime notifications](../administrators_reference_guide/help_notificationoptionstasklet_notificationoptionsstate.html).                                                                                   |

|   |                                                                                                                                                                                                                                                                                                                                                    |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Learn more about integrating PingID in [PingID required domains, URLs, and ports](https://docs.pingidentity.com/pingid/pingid_service_management/pid_domains_urls_ports.html).Depending on the integration kits deployed and the connecting third-party systems, such as email server or SMS service provider, additional ports might be required. |

---

---
title: Running PingFederate as a service using a gMSA on Windows
description: You can run PingFederate as a service using a group Managed Service Account (gMSA) on Windows. gMSAs automatically rotate passwords on a recurring basis. This improves security and reduces password expiration-related downtime by offloading password management onto Windows. gMSAs provide distinct network identity for services. This enables granular, least-privilege access controls on resources, and simplifies multi-server cluster or farm deployments by allowing authorized hosts to share the single managed account. Compared to traditional user or built-in accounts, gMSAs reduce administrative overhead and strengthen the overall security posture for applications running on a Windows Server.
component: pingfederate
version: 13.1
page_id: pingfederate:installing_and_uninstalling_pingfederate:pf_run_pf_service_gmsa_windows
canonical_url: https://docs.pingidentity.com/pingfederate/13.1/installing_and_uninstalling_pingfederate/pf_run_pf_service_gmsa_windows.html
llms_txt: https://docs.pingidentity.com/pingfederate/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  before-you-begin: Before you begin
  setting-up-the-gmsa: Setting up the gMSA
  steps: Steps
  example: Example:
  example-2: Example:
  example-3: Example:
  installing-pingfederate-as-a-service: Installing PingFederate as a service
  steps-2: Steps
  choose-from: Choose from:
  running-pingfederate-as-a-service-with-gmsa: Running PingFederate as a service with gMSA
---

# Running PingFederate as a service using a gMSA on Windows

You can run PingFederate as a service using a group Managed Service Account (gMSA) on Windows. gMSAs automatically rotate passwords on a recurring basis. This improves security and reduces password expiration-related downtime by offloading password management onto Windows. gMSAs provide distinct network identity for services. This enables granular, least-privilege access controls on resources, and simplifies multi-server cluster or farm deployments by allowing authorized hosts to share the single managed account. Compared to traditional user or built-in accounts, gMSAs reduce administrative overhead and strengthen the overall security posture for applications running on a Windows Server.

Learn more about gMSAs in [Group Managed Service Accounts overview](https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/manage/group-managed-service-accounts/group-managed-service-accounts/group-managed-service-accounts-overview) in the Windows documentation.

## Before you begin

* Java 11, 17, or 21. Check [Java requirements](pf_install_java.html) for the version of PingFederate you want to deploy.

* Find the [prerequisites for managing a gMSA](https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/manage/group-managed-service-accounts/group-managed-service-accounts/manage-group-managed-service-accounts?tabs=aduc#prerequisites) in the Windows documentation.

## Setting up the gMSA

## Steps

1. From a Domain Controller within the Active Directory, use the `New-ADServiceAccount` command to create the gMSA.

   ```powershell
   New-ADServiceAccount <accountName> -DNSHostName <serviceHostName> -PrincipalsAllowedToRetrieveManagedPassword <computerAccountsAbleToAccessAccount>
   ```

   ## Example:

   ```powershell
   New-ADServiceAccount PingFarm -DNSHostName pingfederate02.jones.lab -PrincipalsAllowedToRetrieveManagedPassword PINGFEDERATE02$
   ```

   Find a list of other gMSA properties you can set using the [Set-ADServiceAccount](https://learn.microsoft.com/en-us/powershell/module/activedirectory/set-adserviceaccount) command in the Windows documentation.

2. Use the `Install-ADServiceAccount` command to install the gMSA on the specified host machine.

   ## Example:

   On the `pingfederate02` machine from the previous example, you would run the following:

   ```powershell
   Install-ADServiceAccount -Identity 'PingFarm'
   ```

3. Verify the installation by running the `Test-ADServiceAccount` command.

   ### Example:

   If the connection succeeded, running the following command returns a value of `true`:

   ```powershell
   Test-ADServiceAccount -Identity 'PingFarm'
   ```

## Installing PingFederate as a service

## Steps

1. Install PingFederate as a service.

   ### Choose from:

   * Use the `.msi` installer. Learn more in [Installing PingFederate on Windows](pf_install_pf_on_windows.html).

   * Use the install-service script.

     1. Download and unzip the PingFederate `.zip` archive. Learn more in [Installing the PingFederate service on Windows manually](pf_install_pf_service_on_windows_manually.html)

     2. Run the `<pingfed_install>/pingfederate/sbin/win-x86-64/install-service.bat` file.

2. Install PingFederate to a neutral directory like `C:\Program Files\Ping Identity\`.

3. Right-click **PingFederate folder > Properties > Security**.

4. Under the **Group or user names** section, click **Edit > Add > Advanced > Object Types**.

5. Select the **Service Accounts** checkbox.

6. Click **OK**

7. Click **Find Now**.

8. Click your gMSA.

9. Click **OK > OK**.

10. Grant the gMSA account full control of the `PingFederate` folder.

## Running PingFederate as a service with gMSA

1. In Windows, search for `Services` and launch it.

2. Find PingFederate in the list.

3. Right-click **PingFederate > Properties > Log On**.

4. Under **Log on as > This account > Browse > Advanced > Find Now**, select the gMSA.

5. Clear the **Password** fields and click **OK**.

6. Search for `Local Security Policy` and launch it.

7. Click **Local Policy > User Rights Assignment** and grant the gMSA **Log on as a service** permission.

8. Go to **Services** and launch or relaunch PingFederate.

---

---
title: System requirements
description: PingFederate has the following recommended system versions and requirements.
component: pingfederate
version: 13.1
page_id: pingfederate:installing_and_uninstalling_pingfederate:pf_system_requirements
canonical_url: https://docs.pingidentity.com/pingfederate/13.1/installing_and_uninstalling_pingfederate/pf_system_requirements.html
llms_txt: https://docs.pingidentity.com/pingfederate/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 26, 2026
section_ids:
  operating-systems-and-virtualization: Operating systems and virtualization
  java_environment: Java environment
  browsers: Browsers
  tls-protocol: TLS protocol
  datastore-integration: Datastore integration
  distributed-cache-optional: Distributed cache (optional)
  secret-manager-optional: Secret manager (optional)
  proxy-client-authentication-optional: Proxy client authentication (optional)
  hardware-security-modules-optional: Hardware security modules (optional)
  minimum-hardware-requirements: Minimum hardware requirements
  running-pingfederate-on-amazon-web-services: Running PingFederate on Amazon Web Services
---

# System requirements

PingFederate has the following recommended system versions and requirements.

## Operating systems and virtualization

|   |                                                                                                                                                                                                                              |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | PingFederate is tested with default configurations of operating-system components. If your organization customizes implementations or installs third-party plugins, deployment efforts could affect the PingFederate server. |

| Component         | Supported versions                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| ----------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Operating systems | * Amazon Linux 2023

* Canonical Ubuntu 22.04 LTS, 24.04 LTS, and 26.04 LTS

* Microsoft Windows Server 2016, 2019, 2022, and 2025

* Oracle Linux (Red Hat Compatible Kernel) 8.10, 9.7, and 10.0

* Red Hat Enterprise Linux ES 8.10, 9.7, and 10.0

* SUSE Linux Enterprise 12 SP5 and 15 SP7

* RockyLinux 9.8 and 10.2                                                                                                                                                                                                                                                                                                                                                                                                                              |
| Docker support    | - Docker version: 28.2.2

  View the PingFederate Docker image on [DockerHub](https://hub.docker.com/r/pingidentity/pingfederate). Learn more in the Ping Identity [DevOps documentation](https://developer.pingidentity.com/devops/devops-landing-page.html). Note that only the PingFederate software is licensed under Ping Identity's end user license agreement, and any other software components contained within the image are licensed solely under the terms of the applicable open source or third-party license.&#xA;&#xA;Ping Identity accepts no responsibility for the performance of any specific virtualization software and in no way guarantees the performance or interoperability of any virtualization software with its products. |
| Virtualization    | Although Ping Identity doesn't qualify or recommend any specific virtual machine (VM) or container products other than those already specified, PingFederate has run well on several, including AWS Fargate, Hyper-V, VMWare, and Xen.&#xA;&#xA;The list of products is provided for example purposes only. We view all products in this category equally. Ping Identity accepts no responsibility for the performance of any specific virtualization software and in no way guarantees the performance, interoperability, or both of any VM or container software with its products.                                                                                                                                                                    |

## Java environment

* Amazon Corretto 17, 21, and 25

* OpenJDK 17, 21, and 25

* Oracle Java SE Development Kit 17 LTS, 21 LTS, and 25 LTS

Learn more in [Installing Java](pf_install_java.html).

|   |                                                                                                                                                                                                  |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | Ping Identity Java Support Policy applies. Learn more in [Java Support Policy](https://support.pingidentity.com/s/article/PingIdentity-Java-Support-Policy) in the Ping Identity Knowledge Base. |

## Browsers

| Server                | Supported browsers                                                                                                          |
| --------------------- | --------------------------------------------------------------------------------------------------------------------------- |
| Runtime server        | * Apple Safari

* Google Chrome

* Microsoft Edge

* Mozilla Firefox

* Apple iOS 26 (Safari)

* Google Android 16 (Chrome) |
| Administrative server | - Google Chrome

- Microsoft Edge

- Mozilla Firefox                                                                        |

## TLS protocol

* Runtime server and administrative server

  * TLS 1.2 and 1.3

    |   |                                                                                                                                                                                |
    | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
    |   | If PingFederate is in HSM mode, TLS is only compatible with some Java versions. Learn more in [Known issues and limitations](../release_notes/pf_release_notes_130.html#HSMs). |

## Datastore integration

| Functionality                                           | Supported versions                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| ------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| User-attribute lookup                                   | * PingDirectory 10.2, 10.3, 11, and 11.1

* PingDS (Formerly ForgeRock DS) 7.5, 8.0, and 8.1

* Amazon DynamoDB

* Amazon Aurora MySQL 3.12.0 (compatible with MySQL 8.0.44)

* Amazon Aurora PostgreSQL (compatible with PostgreSQL 16.13 and 17.9)

* Azure SQL Managed Instance

* Microsoft Active Directory 2016 and 2022

* Microsoft SQL Server 2017, 2019, and 2022

* Oracle Database 19c and 23ai

* Oracle MySQL 8.4

* Oracle Unified Directory 14c

* PostgreSQL 16.13, 17.9, and 18.3

* Custom implementation through the PingFederate SDK                                   |
| SaaS or SCIM outbound provisioning                      | - Provisioning channel data source

  * PingDirectory 9.3, 10.1, 10.2, 10.3, and 11

  * PingDS (Formerly ForgeRock DS) 7.5, 8.0, and 8.1

  * Microsoft Active Directory 2016

  * Oracle Unified Directory 14c

- Provisioning internal datastore

  * Amazon Aurora MySQL 3.12.0 (compatible with MySQL 8.0.44)

  * Amazon Aurora PostgreSQL (compatible with PostgreSQL 16.13 and 17.9)

  * Microsoft Azure SQL Managed Instance

  * Microsoft SQL Server 2017, 2019, and 2022

  * Oracle Database 19c and 23ai

  * Oracle MySQL 8.0 and 8.4

  * PostgreSQL 16.13, 17.9, and 18.3 |
| SCIM inbound provisioning                               | * Microsoft Active Directory 2016

* Custom implementation through the PingFederate SDK                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| Just-in-time (JIT) inbound provisioning                 | - PingDirectory 9.3, 10.1, 10.2, 10.3, and 11

- PingDS (Formerly ForgeRock DS) 7.5, 8.0, and 8.1

- Azure SQL Managed Instance

- Microsoft Active Directory 2016

- Microsoft SQL Server 2017, 2019, and 2022

- Oracle Unified Directory 14c                                                                                                                                                                                                                                                                                                                                             |
| Account linking                                         | * PingDirectory 9.3, 10.1, 10.2, 10.3, and 11

* PingDS (Formerly ForgeRock DS) 7.5, 8.0, and 8.1

* Amazon DynamoDB

* Amazon Aurora MySQL 3.12.0 (compatible with MySQL 8.0.44)

* Amazon Aurora PostgreSQL (compatible with PostgreSQL 16.13 and 17.9)

* Azure SQL Managed Instance

* Microsoft Active Directory 2016

* Microsoft SQL Server 2017, 2019, and 2022

* Oracle Database 19c and 23ai

* Oracle MySQL 8.0 and 8.4

* Oracle Unified Directory 14c

* PostgreSQL 16.13, 17.9, and 18.3                                                                                     |
| OAuth client configuration and persistent grants        | - PingDirectory 9.3, 10.1, 10.2, 10.3, and 11

- PingDS (Formerly ForgeRock DS) 7.5, 8.0, and 8.1

- Amazon DynamoDB

- Amazon Aurora MySQL 3.12.0 (compatible with MySQL 8.0.44)

- Amazon Aurora PostgreSQL (compatible with PostgreSQL 16.13 and 17.9)

- Azure SQL Managed Instance

- Microsoft Active Directory 2016

- Microsoft SQL Server 2017, 2019, and 2022

- Oracle Database 19c and 23ai

- Oracle MySQL 8.0 and 8.4

- Oracle Unified Directory 14c

- PostgreSQL 16.13, 17.9, and 18.3

- Custom implementation through the PingFederate SDK                               |
| Registration and profile management of local identities | * PingDirectory 9.3, 10.1, 10.2, 10.3, and 11                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| Persistent authentication sessions                      | - PingDirectory 9.3, 10.1, 10.2, 10.3, and 11

- PingDS 7.5, 8.0, and 8.1

- Amazon DynamoDB

- Amazon Aurora MySQL 3.12.0 (compatible with MySQL 8.0.44)

- Amazon Aurora PostgreSQL (compatible with PostgreSQL 16.13 and 17.9)

- Microsoft Azure SQL Managed Instance

- Microsoft SQL Server 2017, 2019, 2022, 2025

- Oracle Database 19c and 23ai

- Oracle MySQL 8.0 and 8.4

- PostgreSQL 16.13, 17.9, and 18.3

- Custom implementation through the PingFederate SDK                                                                                                              |

|   |                                                                                                                                                                                                                                                                                                               |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | PingFederate was tested with vendor-specific Java database connectivity (JDBC) *(tooltip: \<div class="paragraph">&#xA;\<p>A Java API that allows Java programs to interact with databases.\</p>&#xA;\</div>)* 4.2 drivers. Learn more in [Compatible database drivers](pf_compatible_database_drivers.html). |

## Distributed cache (optional)

Redis

Learn more in [Storing PingFederate data with Redis](../administrators_reference_guide/pf_storing_pf_data_redis.html).

## Secret manager (optional)

CyberArk Credential Provider 12

Windows Group Managed Service Account (gMSA)

Learn more in [Secret managers](../administrators_reference_guide/pf_secret_managers.html).

## Proxy client authentication (optional)

* Apache

* NGINX

Other proxies aren't qualified or guaranteed to work with PingFederate. Learn more in [Using Proxied Authentication for the X.509 IdP Adapter](https://support.pingidentity.com/s/article/Using-Proxied-Authentication-for-the-X-509-IdP-Adapter) in Ping Identity Support.

## Hardware security modules (optional)

| Hardware security module                            | Qualified versions                                                                                                                                                                                                                                                                                                                                                                                                                               |
| --------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| AWS CloudHSM                                        | * Client software version: 5.17.2PingFederate must be deployed on one of the Linux or Windows operating systems supported by both AWS CloudHSM and PingFederate.                                                                                                                                                                                                                                                                                 |
| Entrust nShield Connect HSMs                        | - Host and Firmware version: 13.6.12

- Client driver version: 13.6.12                                                                                                                                                                                                                                                                                                                                                                           |
| Thales Luna Cloud HSM Services and Luna Network HSM | * Luna HSM Client 10.9.0Learn more about the Luna HSM Client, including compatible HSMs, HSM firmware, appliance software, and client software, in the [Luna Cloud HSM Service Client Guide](https://thalesdocs.com/dpod/services/luna_cloud_hsm/extern/client_guides/Content/CRN/Luna/client/10-7-1.htm) and the [Luna Network HSM Documentation Archive](https://thalesdocs.com/gphsm/luna/7/docs/network/Content/CRN/Luna/client/10-7-0.htm). |

## Minimum hardware requirements

* Multi-core Intel Xeon processor or higher

  We recommend a minimum of four processing cores distributed across any number of CPUs.

* 4 GB of RAM

  Ensure that at least 1.5 GB are available to PingFederate.

* 1 GB of available hard drive space

### Running PingFederate on Amazon Web Services

The following hardware considerations apply to PingFederate environments running on Amazon Web Services (AWS) *(tooltip: \<div class="paragraph">
\<p>An Amazon subsidiary providing cloud computing platforms.\</p>
\</div>)*:

* PingFederate is qualified to run on the Graviton 2 processor architecture

* We recommend a minimum 2 processor cores and 4 GB of RAM

|   |                                                                                                                                                                                                                                       |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Although it's possible to run PingFederate on less powerful hardware, the guidelines provided accommodate disk space for default logging, auditing profiles, and CPU resources for a moderate level of concurrent request processing. |

---

---
title: Uninstalling PingFederate
description: Learn how to uninstall PingFederate from a Windows or Linux server.
component: pingfederate
version: 13.1
page_id: pingfederate:installing_and_uninstalling_pingfederate:pf_uninstall_pf
canonical_url: https://docs.pingidentity.com/pingfederate/13.1/installing_and_uninstalling_pingfederate/pf_uninstall_pf.html
llms_txt: https://docs.pingidentity.com/pingfederate/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: September 29, 2025
section_ids:
  uninstalling-pingfederate-from-a-linux-server: Uninstalling PingFederate from a Linux server
  before-you-begin: Before you begin
  about-this-task: About this task
  steps: Steps
  choose-from: Choose from:
  uninstalling-pingfederate-from-a-windows-server: Uninstalling PingFederate from a Windows server
  before-you-begin-2: Before you begin
  about-this-task-2: About this task
  steps-2: Steps
  choose-from-2: Choose from:
---

# Uninstalling PingFederate

Uninstalling PingFederate involves removing the previously-installed PingFederate service and the installation directory, `<pf_install>`.

Depending on your deployment, you can uninstall PingFederate from either a Linux server or Windows server.

## Uninstalling PingFederate from a Linux server

### Before you begin

* Ensure that you're signed on to your system with sufficient privileges to uninstall an application.

### About this task

You can use the systemd service or the SysV initialization script to uninstall PingFederate from a Linux server.

### Steps

1. Uninstall PingFederate using one of the following methods:

   ### Choose from:

   * To uninstall PingFederate using the systemd service, use the following `systemctl` commands to stop and disable PingFederate:

     ```
     systemctl stop pingfederate ;\
     systemctl disable pingfederate ;\
     systemctl daemon-reload
     ```

   You can also remove the PingFederate systemd unit file `pingfederate.service` from the systemd unit files directory `/etc/systemd/system` before running the `systemctl daemon-reload` command.

   * To uninstall PingFederate using the SysV initialization script, do one of the following:

     * Use the `Service Configuration utility` to stop and disable the PingFederate service.

     * Remove any symbolic links from various initialization directories to stop the PingFederate service.

     * Remove the PingFederate SysV initialization script `pingfederate` from the SysV initialization directory `/etc/rc.d/init.d`.

       |   |                                                                                                                            |
       | - | -------------------------------------------------------------------------------------------------------------------------- |
       |   | Depending on the operating system, the exact directory locations might vary. Consult your system administrators as needed. |

2. (Optional) Remove the PingFederate installation directory, `<pf_install>`.

## Uninstalling PingFederate from a Windows server

### Before you begin

* Ensure you're signed on to your system with sufficient privileges to uninstall an application.

### About this task

The method you use to uninstall PingFederate depends on whether you installed it using the installer for Windows or the distribution `.zip` file.

### Steps

1. Verify the installation medium. In Windows, go to **Control Panel > Uninstall a Program**.

   |   |                                                                                                                                                                                                                                    |
   | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | The existence of a PingFederate entry indicates a previous installation of PingFederate using the Windows installer. If there's no existing PingFederate entry, the distribution `.zip` file was used to perform the installation. |

2. Depending on the type of installation, uninstall PingFederate using one of the following methods:

   ### Choose from:

   * To uninstall PingFederate using the PingFederate installer for Windows, go to **Control Panel > Uninstall a Program**.

     This removes the PingFederate service and the installation directory.

   * To uninstall PingFederate using the distribution `.zip` file:

     1. Go to **Control Panel > Administrative Tools > Services** to open the Windows management console.

     2. Right-click the **PingFederate** service and select **Stop**.

     3. Run `uninstall-service.bat` from the `<pf_install>\pingfederate\sbin` subdirectory that corresponds to your platform processor.

     4. (Optional) Delete the PingFederate installation directory `<pf_install>`.