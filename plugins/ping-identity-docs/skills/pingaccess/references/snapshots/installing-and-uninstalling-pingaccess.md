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

---

---
title: Accessing the interactive administrative API documentation
description: View interactive documentation for the administrative API endpoints.
component: pingaccess
version: 9.1
page_id: pingaccess:installing_and_uninstalling_pingaccess:pa_accessing_the_api_docs
canonical_url: https://docs.pingidentity.com/pingaccess/9.1/installing_and_uninstalling_pingaccess/pa_accessing_the_api_docs.html
llms_txt: https://docs.pingidentity.com/pingaccess/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: February 6, 2023
section_ids:
  steps: Steps
  example: Example:
  example-2: Example:
  result: Result:
---

# Accessing the interactive administrative API documentation

View interactive documentation for the administrative API endpoints.

## Steps

1. Launch your browser and go to `https://<host>:<admin-port>/pa-admin-api/v3/api-docs/`.

   ### Example:

   `https://localhost:9000/pa-admin-api/v3/api-docs/`

   |   |                                                         |
   | - | ------------------------------------------------------- |
   |   | The browser might prompt you to enter your credentials. |

2. Enter the administrator username and password.

3. Use the administrative API to perform a variety of administrative tasks, such as gathering information.

   ### Example:

   To use the interactive administrative API documentation to see all defined applications:

   1. Click to expand the `/applications` endpoint.

   2. Click to expand the `GET` method (`GET /applications`).

   3. Enter values for the parameters or leave them all blank.

   4. Click **Try It Out**.

   ### Result:

   The request Uniform Resource Locator (URL) *(tooltip: \<div class="paragraph">
   \<p>Identifies a resource according to its internet location.\</p>
   \</div>)*, response body, response code, and response headers display.

---

---
title: Accessing the PingAccess administrative API
description: Access the PingAccess admin application programming interface (API).
component: pingaccess
version: 9.1
page_id: pingaccess:installing_and_uninstalling_pingaccess:pa_accessing_the_pa_admin_api
canonical_url: https://docs.pingidentity.com/pingaccess/9.1/installing_and_uninstalling_pingaccess/pa_accessing_the_pa_admin_api.html
llms_txt: https://docs.pingidentity.com/pingaccess/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: January 30, 2026
section_ids:
  steps: Steps
  example: Example:
  accessing-the-interactive-administrative-api-documentation: Accessing the interactive administrative API documentation
  steps-2: Steps
  example-2: Example:
  example-3: Example:
  result: Result:
---

# Accessing the PingAccess administrative API

Access the PingAccess admin application programming interface (API) *(tooltip: \<div class="paragraph">
\<p>A specification of interactions available for building software to access an application or service.\</p>
\</div>)*.

## Steps

* Send an HTTP request *(tooltip: \<div class="paragraph">
  \<p>A client transaction sent over HTTP to the server specifying a request method, such as GET, POST, and DELETE, to execute against a resource or resources on the server.\</p>
  \</div>)* to the following URL: `https://<host>:<admin-port>/pa-admin-api/v3/<api-endpoint>`.

  |   |                                                                        |
  | - | ---------------------------------------------------------------------- |
  |   | You must provide appropriate administrator credentials in the request. |

  ### Example:

  The following cURL command sends a GET request to the `applications` resource to retrieve a list of all defined applications:

  ```shell
  curl -k -u Administrator:Password1 -H "X-Xsrf-Header: PingAccess" https://localhost:9000/pa-admin-api/v3/applications
  ```

  In this example:

  * The **-u Administrator:Password1** parameter sends a basic authentication header, specifying `Administrator` as the username and `Password1` as the password.

  * The **-k** parameter specifies to ignore HTTPS certificate issues.

  * The **-H "X-Xsrf-Header: PingAccess"** parameter sends an `X-XSRF-Header` with the value `PingAccess`.

## Accessing the interactive administrative API documentation

View interactive documentation for the administrative API endpoints.

### Steps

1. Launch your browser and go to `https://<host>:<admin-port>/pa-admin-api/v3/api-docs/`.

   #### Example:

   `https://localhost:9000/pa-admin-api/v3/api-docs/`

   |   |                                                         |
   | - | ------------------------------------------------------- |
   |   | The browser might prompt you to enter your credentials. |

2. Enter the administrator username and password.

3. Use the administrative API to perform a variety of administrative tasks, such as gathering information.

   #### Example:

   To use the interactive administrative API documentation to see all defined applications:

   1. Click to expand the `/applications` endpoint.

   2. Click to expand the `GET` method (`GET /applications`).

   3. Enter values for the parameters or leave them all blank.

   4. Click **Try It Out**.

   #### Result:

   The request Uniform Resource Locator (URL) *(tooltip: \<div class="paragraph">
   \<p>Identifies a resource according to its internet location.\</p>
   \</div>)*, response body, response code, and response headers display.

---

---
title: Changing configuration database passwords
description: Rotate the database passwords for the PingAccess configuration database.
component: pingaccess
version: 9.1
page_id: pingaccess:installing_and_uninstalling_pingaccess:pa_changing_config_database_passwords
canonical_url: https://docs.pingidentity.com/pingaccess/9.1/installing_and_uninstalling_pingaccess/pa_changing_config_database_passwords.html
llms_txt: https://docs.pingidentity.com/pingaccess/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: May 8, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
  choose-from: Choose from:
---

# Changing configuration database passwords

Rotate the database passwords for the PingAccess configuration database.

## About this task

The PingAccess configuration database is protected by randomly-generated passwords on startup. You can rotate these passwords for additional security.

## Steps

1. Open a terminal window and go to the `<PA_HOME>/bin` directory.

2. To ensure the `JAVA_HOME` environment variable is set correctly, run the `echo $JAVA_HOME` command.

3. To ensure the proper Java executable is in your path, run the `java -version` command.

   |   |                                                                                                                                       |
   | - | ------------------------------------------------------------------------------------------------------------------------------------- |
   |   | If this command returns a value indicating that the Java executable is not a supported version, correct this issue before continuing. |

4. Stop PingAccess.

5. Run the relevant rotation script for your environment:

   ### Choose from:

   * For Windows:`db-passwd-rotate.bat`

   * For Linux: `db-passwd-rotate.sh`

6. Restart PingAccess.

---

---
title: Configuring PingAccess to run as a Linux systemd service
description: The service script will only start if <JAVA_HOME> and <PA_HOME> are set and if the script can find the PingAccess license file.
component: pingaccess
version: 9.1
page_id: pingaccess:installing_and_uninstalling_pingaccess:pa_configuring_pa_to_run_as_a_linux_systemd_service
canonical_url: https://docs.pingidentity.com/pingaccess/9.1/installing_and_uninstalling_pingaccess/pa_configuring_pa_to_run_as_a_linux_systemd_service.html
llms_txt: https://docs.pingidentity.com/pingaccess/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: May 8, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Configuring PingAccess to run as a Linux systemd service

## About this task

|   |                                                                                                                                         |
| - | --------------------------------------------------------------------------------------------------------------------------------------- |
|   | The service script will only start if *\<JAVA\_HOME>* and *\<PA\_HOME>* are set and if the script can find the PingAccess license file. |

To configure PingAccess to run as a Linux systemd service:

## Steps

1. Copy the configuration file from the `<PA_HOME>/sbin/linux/pingaccess.service` directory to the `/etc/systemd/system/pingaccess.service` directory.

2. In the `pingaccess.service` file, replace the following variables:

   * Replace *<${PA\_HOME}>* with the path to the PingAccess instance.

   * Replace *<${PA\_USER}>* with the username used to run the service.

   * Replace *<${PA\_JAVA\_HOME}>* with the path to the Java installation folder.

3. To allow read-write activity on the service, run:

   ```
   chmod 644 /etc/systemd/system/pingaccess.service
   ```

4. To load the systemd service, run:

   ```
   systemctl daemon-reload
   ```

5. To enable the service, run:

   ```
   systemctl enable pingaccess.service
   ```

6. To start the service, run:

   ```
   systemctl start pingaccess.service
   ```

---

---
title: Configuring PingAccess to run as a Linux systemv service
description: The service script will only start if <JAVA_HOME> and <PA_HOME> are set and if the script can find the PingAccess license file.
component: pingaccess
version: 9.1
page_id: pingaccess:installing_and_uninstalling_pingaccess:pa_configuring_pa_to_run_as_a_linux_systemv_service
canonical_url: https://docs.pingidentity.com/pingaccess/9.1/installing_and_uninstalling_pingaccess/pa_configuring_pa_to_run_as_a_linux_systemv_service.html
llms_txt: https://docs.pingidentity.com/pingaccess/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: May 8, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
  next-steps: Next steps
---

# Configuring PingAccess to run as a Linux systemv service

## About this task

|   |                                                                                                                                         |
| - | --------------------------------------------------------------------------------------------------------------------------------------- |
|   | The service script will only start if *\<JAVA\_HOME>* and *\<PA\_HOME>* are set and if the script can find the PingAccess license file. |

To configure multiple instances of PingAccess on a single host as Linux services, make the following modifications to the script for each service:

* Use a unique script name for each instance.

* Use a separate directory structure for each instance in the file system.

* Configure the following settings in the script file for each instance:

| Setting         | Description                                              |
| --------------- | -------------------------------------------------------- |
| *\<APPNAME>*    | A unique value for each instance.                        |
| *\<PA\_HOME>*   | The path to the PingAccess instance.                     |
| *\<JAVA\_HOME>* | The path to the Java installation folder.                |
| *\<USER>*       | Optional value for the username used to run the service. |

To configure PingAccess to run as a Linux systemv service:

## Steps

1. Copy the PingAccess script file from the `<PA_HOME>/sbin/linux/pingaccess` directory to the `/etc/init.d` directory.

2. **Optional:** Create a new user to run PingAccess.

3. Create the `/var/run/pingaccess` directory.

   |   |                                                                                             |
   | - | ------------------------------------------------------------------------------------------- |
   |   | Ensure that the user who will run the service has read and write permissions to the folder. |

4. Edit the `/etc/init.d/pingaccess` script file and set the values of the following variables at the beginning of the script:

   | Variable                  | Description                                                           |
   | ------------------------- | --------------------------------------------------------------------- |
   | `export <JAVA_HOME>=`     | Specify the Java install folder.                                      |
   | `export <PA_HOME>=`       | Specify the PingAccess install folder.                                |
   | `export USER=` (Optional) | Specify a username to run the service or leave empty for the default. |

5. To register the service, from the `/etc/init.d` directory, run:

   ```
   chkconfig --add pingaccess
   ```

6. To make the service script executable, run:

   ```
   chmod +x pingaccess
   ```

## Next steps

After registering, you can use the `service` command to control the PingAccess service. The available commands are:

* `start`

  Start the PingAccess service.

* `stop`

  Stop the PingAccess service.

* `restart`

  Restart the PingAccess service.

* `status`

  Show the status of the PingAccess service and the service process identifier (PID).

|   |                                                                                                        |
| - | ------------------------------------------------------------------------------------------------------ |
|   | The `service pingaccess status` command displays the current status of the running PingAccess service. |

---

---
title: Configuring PingAccess to run as a Windows service
description: To configure PingAccess to run as a Windows service:
component: pingaccess
version: 9.1
page_id: pingaccess:installing_and_uninstalling_pingaccess:pa_configuring_pa_to_run_as_a_windows_service
canonical_url: https://docs.pingidentity.com/pingaccess/9.1/installing_and_uninstalling_pingaccess/pa_configuring_pa_to_run_as_a_windows_service.html
llms_txt: https://docs.pingidentity.com/pingaccess/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: May 8, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
  result: Result
---

# Configuring PingAccess to run as a Windows service

## About this task

To configure PingAccess to run as a Windows service:

## Steps

1. Open a command prompt as an administrator.

2. In the command prompt, go to the `<PA_HOME>\sbin\windows` directory and run the `install-service.bat` file.

3. In Windows, go to **Control Panel → Administrative Tools → Services**.

4. From the list of available services, right-click **PingAccess Service** and select **Start**.

   You can change the default **Start type** setting in the **Properties** dialog.

## Result

The service starts immediately and restarts automatically on reboot.

---

---
title: Configuring PingAccess to run as a Windows service from the command line
description: To configure PingAccess to run as a Windows service from the command line:
component: pingaccess
version: 9.1
page_id: pingaccess:installing_and_uninstalling_pingaccess:pa_configuring_pa_to_run_as_a_windows_service_from_the_command_line
canonical_url: https://docs.pingidentity.com/pingaccess/9.1/installing_and_uninstalling_pingaccess/pa_configuring_pa_to_run_as_a_windows_service_from_the_command_line.html
llms_txt: https://docs.pingidentity.com/pingaccess/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: May 8, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
  result: Result
---

# Configuring PingAccess to run as a Windows service from the command line

## About this task

To configure PingAccess to run as a Windows service from the command line:

## Steps

1. Go to the `<PA_HOME>\sbin\windows` directory and run the `install-service.bat` file.

2. To set the PingAccess service to start automatically, run `sc config PingAccess start= auto`.

## Result

The service starts immediately and restarts automatically on reboot.

---

---
title: Installation requirements
description: Before you install PingAccess, review the following system, hardware, and port requirements.
component: pingaccess
version: 9.1
page_id: pingaccess:installing_and_uninstalling_pingaccess:pa_installation_requirements
canonical_url: https://docs.pingidentity.com/pingaccess/9.1/installing_and_uninstalling_pingaccess/pa_installation_requirements.html
llms_txt: https://docs.pingidentity.com/pingaccess/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: February 6, 2023
section_ids:
  system-reqs: System requirements
  operating-systems: Operating systems
  docker-versions: Docker versions
  java-runtime-environments: Java runtime environments
  browsers: Browsers
  virtual-systems: Virtual systems
  audit-event-storage: Audit event storage
  hardware-security-modules: Hardware security modules
  an-authentication-protocol-built-on-top-of-oauth-that-authenticates-users-and-enables-clients-relying-parties-of-all-types-to-request-and-receive-information-about-authenticated-sessions-and-users-oidc-is-extensible-allowing-clients-to-use-optional-features-such-as-encryption-of-identity-data-discovery-of-openid-providers-oauth-authorization-servers-and-session-management-openid-connect-oidc-providers: OpenID Connect (OIDC) providers
  pingfederate-versions: PingFederate versions
  hardware-reqs: Hardware requirements
  port-reqs: Port requirements
  pingaccess-admin-console-port: PingAccess admin console port
  pingaccess-cluster-communications-port: PingAccess cluster communications port
  pingaccess-cluster-temporary-certificate-rotation-port: PingAccess cluster temporary certificate rotation port
  pingaccess-engine-port: PingAccess engine port
  pingaccess-agent-port: PingAccess agent port
  pingaccess-sideband-port-optional: PingAccess sideband port (optional)
  pingfederate-traffic-port: PingFederate traffic port
---

# Installation requirements

Before you install PingAccess, review the following system, hardware, and port requirements.

## System requirements

Make sure that your system meets the following requirements for PingAccess deployment and configuration.

Ping Identity qualifies the following configurations and certifies their compatibility with this PingAccess version. Variations of these platforms, such as differences in operating system version or service pack, are supported until the platform creates potential conflicts.

### Operating systems

PingAccess supports actively maintained versions of the following operating systems:

* Amazon Linux

* Canonical Ubuntu (LTS)

* Oracle Linux

* Red Hat Enterprise Linux ES

* Rocky Linux

* SUSE Linux Enterprise Server

* Microsoft Windows Server 2016, 2019, and 2022 (x64)

|   |                                                                                                                                                                                                                                   |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Ping Identity tests PingAccess with default configurations of operating system components. If your organization has custom implementations or has installed third-party plug-ins, this might affect PingAccess server deployment. |

### Docker versions

To deploy the PingAccess server using Docker, you must use an actively maintained GA version of Docker.

* You can find more information about supported versions in [Branches and tags](https://github.com/moby/moby/blob/master/project/BRANCHES-AND-TAGS.md) in the Docker documentation.

* You can find the PingAccess Docker image on [DockerHub](https://hub.docker.com/r/pingidentity/pingaccess) and more information in Ping Identity's [DevOps documentation](https://devops.pingidentity.com/).

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Only the PingAccess software is licensed under Ping Identity's end user license agreement. Any other software components contained within the image are licensed solely under the terms of the applicable open source or third-party license.Ping Identity accepts no responsibility for the performance of any specific virtualization software and in no way guarantees the performance or interoperability of any virtualization software with its products. |

### Java runtime environments

The [Java Support Policy](https://support.pingidentity.com/s/article/PingIdentity-Java-Support-Policy) applies to your Java Runtime Environment (JRE). You must have one of the following versions of the Java Development Kit (JDK) *(tooltip: \<div class="paragraph">
\<p>A development environment for building applications and components using Java.\</p>
\</div>)* installed before installing the PingAccess server:

* Amazon Corretto 17, 21, or 25 (64-bit)

* OpenJDK 17, 21, or 25 (64-bit)

* Oracle JDK 17, 21, or 25 (64-bit)

### Browsers

The PingAccess admin console supports the following browsers:

* Google Chrome

* Microsoft Edge

* Mozilla Firefox

End users can access content protected by PingAccess with any of the previous browsers or Apple Safari. Support extends to Google Android and Apple iOS.

|   |                                                                   |
| - | ----------------------------------------------------------------- |
|   | Currently, PingAccess supports HTTP 1.1 and IPv4 addressing only. |

### Virtual systems

Although Ping Identity doesn't qualify or recommend any specific virtual machine (VM) products, PingAccess runs well on several, including:

* VMWare

* Xen

* Windows Hyper-V

|   |                                                                                                                                                                                                                                                                                                          |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | This list of products is provided only as an example. We view all products in this category equally. Ping Identity accepts no responsibility for the performance of any specific virtualization software and doesn't guarantee the performance or interoperability of any VM software with its products. |

### Audit event storage

PingAccess supports audit event storage with the following databases:

* Microsoft SQL Server 2019 or 2022

* Oracle Database 19c

* PostgreSQL 13 or 16

### Hardware security modules

PingAccess certifies the following HSMs:

* AWS CloudHSM JCE Provider 5.17.1

  |   |                                                                                                                                                                                                                              |
  | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | PingAccess supports AWS CloudHSM with JDK 17 and 21. If you plan to use AWS CloudHSM, you must also deploy your environment on a Linux or Windows operating system that is compatible with both PingAccess and AWS CloudHSM. |

* Thales Luna Cloud HSM Services and Luna Network HSM (Luna HSM Client 10.x)

  |   |                                                                                                                                                                         |
  | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | Currently, there's a known issue with key pairs stored in Safenet Luna HSMs. Learn more in the [PA-16103 known issue](../release_notes/pa_release_notes.html#pa-16103). |

You can find more information about configuring a hardware security module (HSM) *(tooltip: \<div class="paragraph">
\<p>A dedicated cryptographic processor designed to manage and protect digital keys. HSMs act as trust anchors that protect the cryptographic key lifecycle by securely managing, processing, and storing cryptographic keys inside a hardened, tamper-resistant device.\</p>
\</div>)* in [Hardware security module providers](../pingaccess_user_interface_reference_guide/pa_hardware_security_module_providers.html).

### OpenID Connect (OIDC) *(tooltip: \<div class="paragraph">&#xA;\<p>An authentication protocol built on top of OAuth that authenticates users and enables clients (relying parties) of all types to request and receive information about authenticated sessions and users. OIDC is extensible, allowing clients to use optional features such as encryption of identity data, discovery of OpenID Providers (OAuth authorization servers), and session management.\</p>&#xA;\</div>)* providers

Ping Identity aims to support any third-party OIDC-compliant provider. The following table lists some of the most common providers used with PingAccess:

| Provider                        | Provider Type                   |
| ------------------------------- | ------------------------------- |
| PingFederate                    | PingFederate                    |
| PingOne SSO                     | PingOne                         |
| PingOne Advanced Identity Cloud | PingOne Advanced Identity Cloud |
| PingAM                          | PingAM                          |
| PingOne for Enterprise          | Common                          |
| Azure                           | Common                          |
| Okta                            | Common                          |

#### PingFederate versions

This PingAccess version is fully certified with the last four versions of PingFederate. Other PingFederate versions should be compatible as Ping Identity's [EoL policy](https://www.pingidentity.com/en/legal/end-of-life-policy.html) describes.

|   |                                                                                                                                           |
| - | ----------------------------------------------------------------------------------------------------------------------------------------- |
|   | Some PingAccess features rely on a specific minimum PingFederate version to work. This will always be noted in the feature's description. |

## Hardware requirements

|   |                                                                                                                                                                                                                                        |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Although it's possible to run PingAccess on less powerful hardware, the following guidelines accommodate disk space for default logging and auditing profiles and CPU resources for a moderate level of concurrent request processing. |

Run PingAccess on hardware that meets or exceeds these specifications:

* Multi-CPU/Cores (8 or more)

* 4 GB of RAM

* 2.1 GB of available hard drive space

## Port requirements

PingAccess uses ports and protocols to communicate with external components. Use this guide to ensure the correct ports are available across network segments.

|   |                                                                                                                                                                                                                                                             |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | In the following sections, direction indicates whether requests flow to or from PingAccess:- Inbound requests

  Requests that PingAccess receives from external components.

- Outbound requests

  Requests that PingAccess sends to external components. |

### PingAccess admin console port

Used for incoming requests to the PingAccess administrative console.

Configurable using the `admin.port` property in the `run.properties` file. Learn more in the [Configuration file reference guide](../reference_guides/pa_config_file_ref.html).

|   |                                                                                                                                  |
| - | -------------------------------------------------------------------------------------------------------------------------------- |
|   | This port is also used by clustered engine nodes and the replica admin node to pull configuration data using the admin REST API. |

* Protocol: HTTPS

* Transport: TCP

* Default port: 9000

* Destination: PingAccess admin console

* Direction: Inbound

* Source: PingAccess administrator browser, PingAccess administrative application programming interface (API) *(tooltip: \<div class="paragraph">
  \<p>A specification of interactions available for building software to access an application or service.\</p>
  \</div>)* REST calls, PingAccess replica admin and clustered engine nodes.

### PingAccess cluster communications port

Used for incoming requests where the clustered engines request their configuration data.

Configurable using the `clusterconfig.port` property in the `run.properties` file. Learn more in the [Configuration file reference guide](../reference_guides/pa_config_file_ref.html).

|   |                                                                                                                                  |
| - | -------------------------------------------------------------------------------------------------------------------------------- |
|   | This port is also used by clustered engine nodes and the replica admin node to pull configuration data using the admin REST API. |

* Protocol: HTTPS

* Transport: TCP

* Default port: 9090

* Destination: PingAccess admin console

* Direction: Inbound

* Source: PingAccess administrator browser, PingAccess administrative API REST calls, PingAccess replica admin and clustered engine nodes

### PingAccess cluster temporary certificate rotation port

Used for incoming requests where the clustered engines request their configuration data.

Configurable using the `clusterconfig.temp.rotation.port` property in the `run.properties` file. Learn more in the [Configuration file reference guide](../reference_guides/pa_config_file_ref.html#pa-cluster-config-settings).

|   |                                                                                                                                  |
| - | -------------------------------------------------------------------------------------------------------------------------------- |
|   | This port is also used by clustered engine nodes and the replica admin node to pull configuration data using the admin REST API. |

* Protocol: HTTPS

* Transport: TCP

* Default port: 9095

* Destination: PingAccess admin console

* Direction: Inbound

* Source: PingAccess administrator browser, PingAccess administrative API REST calls, PingAccess replica admin and clustered engine nodes

### PingAccess engine port

Used for incoming requests to the PingAccess runtime engine.

Configurable using the `Listeners` configuration page. Learn more in the [PingAccess user interface reference guide](../pingaccess_user_interface_reference_guide/pa_ui_ref_guide.html).

* Protocol: HTTP or HTTPS

* Transport: TCP

* Default port: 3000\*

  |   |                                                                                         |
  | - | --------------------------------------------------------------------------------------- |
  |   | Any additional engine listener ports defined in the configuration must be open as well. |

* Destination: PingAccess engine

* Direction: Inbound

* Source: Client browser, mobile devices, PingFederate engine

### PingAccess agent port

Used for incoming Agent requests to the PingAccess runtime engine.

Configurable using the `agent.http.port` property of the `run.properties` file. Learn more in the [Configuration file reference guide](../reference_guides/pa_config_file_ref.html).

* Protocol: HTTP or HTTPS

* Transport: TCP

* Default port: 3030

* Destination: PingAccess engine

* Direction: Inbound

* Source: PingAccess agent

### PingAccess sideband port (optional)

Used for incoming sideband requests to the PingAccess runtime engine.

Configurable using the `sideband.http.port` property of the `run.properties` file. Learn more in the [Configuration file reference guide](../reference_guides/pa_config_file_ref.html).

|   |                                                                                                                                           |
| - | ----------------------------------------------------------------------------------------------------------------------------------------- |
|   | The default value of the `sideband.http.enabled property` is `false`. This property must be set to `true` to configure a sideband client. |

* Protocol: HTTP or HTTPS

* Transport: TCP

* Default port: 3020

* Destination: PingAccess engine

* Direction: Inbound

* Source: Sideband client (an API gateway such as Kong Gateway or Apigee)

### PingFederate traffic port

Used to validate OAuth *(tooltip: \<div class="paragraph">
\<p>A standard framework that enables an application (OAuth client) to obtain access tokens from an OAuth authorization server for the purpose of retrieving protected resources on a resource server.\</p>
\</div>)* access token *(tooltip: \<div class="paragraph">
\<p>A data object by which a client authenticates to a resource server and lays claim to authorizations for accessing particular resources.\</p>
\</div>)* and ID tokens, make Security Token Service (STS) *(tooltip: \<div class="paragraph">
\<p>An entity responsible for responding to WS-Trust requests for validation and issuance of security tokens used for SSO authentication to web services.\</p>
\</div>)* calls for identity mediation, and return authorized information about a user.

Configurable using the `PingFederate Settings` page within PingAccess. Learn more in the [PingAccess user interface reference guide](../pingaccess_user_interface_reference_guide/pa_ui_ref_guide.html).

* Protocol: HTTPS

* Transport: TCP

* Default port: 9031

* Destination: PingFederate

* Direction: Outbound

* Source: PingAccess engine

---

---
title: Installing and Uninstalling PingAccess
description: Use this section for instructions on installing, configuring, and starting PingAccess.
component: pingaccess
version: 9.1
page_id: pingaccess:installing_and_uninstalling_pingaccess:pa_installing_and_uninstalling_pa
canonical_url: https://docs.pingidentity.com/pingaccess/9.1/installing_and_uninstalling_pingaccess/pa_installing_and_uninstalling_pa.html
llms_txt: https://docs.pingidentity.com/pingaccess/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: May 8, 2024
---

# Installing and Uninstalling PingAccess

Use this section for instructions on installing, configuring, and starting PingAccess.

* Before installing PingAccess, review:

  * [Installation requirements](pa_installation_requirements.html).

* Install PingAccess:

  * On [Linux](pa_installing_pa_on_your_system.html).

  * On [Windows](pa_installing_pa_on_your_system.html).

* After installing PingAccess, you can:

  * [Start PingAccess](pa_starting_pa.html).

  * [Access the admin console for the first time](pa_accessing_the_admin_console.html).

  * [Access the PingAccess administrative API](pa_accessing_the_pa_admin_api.html).

  * [Change configuration database passwords](pa_changing_config_database_passwords.html).

* To stop, run, or uninstall PingAccess, see:

  * [Stopping PingAccess](pa_stopping_pa.html).

  * [Running PingAccess as a service](pa_running_pa_as_a_service.html).

  * [Uninstalling PingAccess](pa_uninstalling_pa.html).

|   |                                                                                                                                                                                   |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | These features are affected by the settings in the configuration file. For more information, see the [Configuration file reference](../reference_guides/pa_config_file_ref.html). |

---

---
title: Installing PingAccess on Linux
description: To install PingAccess on a Linux system:
component: pingaccess
version: 9.1
page_id: pingaccess:installing_and_uninstalling_pingaccess:pa_installing_pa_on_linux
canonical_url: https://docs.pingidentity.com/pingaccess/9.1/installing_and_uninstalling_pingaccess/pa_installing_pa_on_linux.html
llms_txt: https://docs.pingidentity.com/pingaccess/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: May 8, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
  next-steps: Next steps
---

# Installing PingAccess on Linux

## About this task

To install PingAccess on a Linux system:

## Steps

1. Download the distribution `.zip` archive from the [PingAccess downloads page](https://www.pingidentity.com/en/resources/downloads/pingaccess.html).

2. Extract the distribution `.zip` archive into your installation directory.

3. **Optional:** If you are using an existing configuration file to configure the system, move the `data.json` file to the `<PA_Home>/data/start-up-deployer` directory.

   |   |                                                                                                                                                                                                                                                    |
   | - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | When you start PingAccess for the first time, if this configuration is present it will be imported. After a successful import, the `data.json` file is deleted. If the configuration is present but cannot be imported, PingAccess is not started. |

   |   |                                                                                                                                                         |
   | - | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | If you're deploying PingAccess in a cluster configuration, see the [configuration documentation](../reference_guides/pa_configuring_a_pa_cluster.html). |

## Next steps

[Access the administrative console to complete the configuration](pa_accessing_the_admin_console.html).

---

---
title: Installing PingAccess on Windows from the command line
description: To install PingAccess on a Windows system from the CLI:
component: pingaccess
version: 9.1
page_id: pingaccess:installing_and_uninstalling_pingaccess:pa_installing_pa_on_windows_from_the_cli
canonical_url: https://docs.pingidentity.com/pingaccess/9.1/installing_and_uninstalling_pingaccess/pa_installing_pa_on_windows_from_the_cli.html
llms_txt: https://docs.pingidentity.com/pingaccess/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: May 8, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
  next-steps: Next steps
---

# Installing PingAccess on Windows from the command line

## About this task

To install PingAccess on a Windows system from the CLI:

## Steps

1. Download the distribution `.zip` archive.

2. Extract the distribution `.zip` archive into your installation directory.

3. **Optional:** If you are using an existing configuration file to configure the system, move the `data.json` file to the `<PA_Home>/data/start-up-deployer` directory.

   |   |                                                                                                                                                                                                                                                    |
   | - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | When you start PingAccess for the first time, if this configuration is present it will be imported. After a successful import, the `data.json` file is deleted. If the configuration is present but cannot be imported, PingAccess is not started. |

## Next steps

[Access the administrative console to complete the configuration](pa_accessing_the_admin_console.html).

---

---
title: Installing PingAccess on Windows using the installer
description: To install PingAccess on a Windows system using the installer:
component: pingaccess
version: 9.1
page_id: pingaccess:installing_and_uninstalling_pingaccess:pa_installing_pa_on_windows_using_the_installer
canonical_url: https://docs.pingidentity.com/pingaccess/9.1/installing_and_uninstalling_pingaccess/pa_installing_pa_on_windows_using_the_installer.html
llms_txt: https://docs.pingidentity.com/pingaccess/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: May 8, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
  next-steps: Next steps
---

# Installing PingAccess on Windows using the installer

## About this task

To install PingAccess on a Windows system using the installer:

## Steps

1. Download the PingAccess Windows installer from the [PingAccess downloads page](https://www.pingidentity.com/en/resources/downloads/pingaccess.html).

2. Double-click on the installer icon to launch the PingAccess setup wizard.

3. Click **Next** and follow the prompts to complete the installation using the following information for your selected operational mode.

   | Operational Mode             | Requirements                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
   | ---------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   | Standalone                   | Ports:- PingAccess administrative console: TCP 9000

   - PingAccess agent protocol: TCP 3030                                                                                                                                                                                                                                                                                                                                                                                          |
   | Clustered admin node         | Ports:- PingAccess administrative console: TCP 9000

   - Configuration query port: TCP 9090                                                                                                                                                                                                                                                                                                                                                                                           |
   | Clustered replica admin node | Ports:- PingAccess administrative console: TCP 9000

   - Configuration query port: TCP 9090Prerequisites:- You must install and configure a clustered admin node.

   - You must have a configuration data archive file available for the replica admin node. For more information, see [Clustering in PingAccess](../reference_guides/pa_clustering_ref_guide.html) in *Reference Guides*.&#xA;&#xA;Install the clustered replica admin node on a separate machine in the same network. |
   | Clustered engine node        | Ports:- PingAccess agent protocol: TCP 3030Prerequisites:- You must install a clustered admin node.

   - You must have a configuration data archive file available for the clustered engine node. For more information, see [Clustering in PingAccess](../reference_guides/pa_clustering_ref_guide.html) in *Reference Guides*.                                                                                                                                                       |

4. Copy the Uniform Resource Locator (URL) *(tooltip: \<div class="paragraph">
   \<p>Identifies a resource according to its internet location.\</p>
   \</div>)* of the PingAccess administrative console that is displayed on the final page of the PingAccess setup wizard, then click **Finish**.

5. To customize and finalize the PingAccess setup, paste the URL you copied into your web browser and connect to the administrative console of the instance you have just installed.

## Next steps

[Access the administrative console to complete the configuration](pa_accessing_the_admin_console.html).

---

---
title: Installing PingAccess on your system
description: Install PingAccess on Linux, on Windows through an installation wizard, or on Windows through the command-line interface (CLI).
component: pingaccess
version: 9.1
page_id: pingaccess:installing_and_uninstalling_pingaccess:pa_installing_pa_on_your_system
canonical_url: https://docs.pingidentity.com/pingaccess/9.1/installing_and_uninstalling_pingaccess/pa_installing_pa_on_your_system.html
llms_txt: https://docs.pingidentity.com/pingaccess/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: May 6, 2024
section_ids:
  before-you-begin: Before you begin
  installing-pingaccess-on-linux: Installing PingAccess on Linux
  about-this-task: About this task
  steps: Steps
  next-steps: Next steps
  installing-pingaccess-on-windows-using-the-installer: Installing PingAccess on Windows using the installer
  about-this-task-2: About this task
  steps-2: Steps
  next-steps-2: Next steps
  installing-pingaccess-on-windows-from-the-command-line: Installing PingAccess on Windows from the command line
  about-this-task-3: About this task
  steps-3: Steps
  next-steps-3: Next steps
---

# Installing PingAccess on your system

Install PingAccess on Linux, on Windows through an installation wizard, or on Windows through the command-line interface (CLI).

## Before you begin

* Ensure you've met the [installation requirements](pa_installation_requirements.html).

* Ensure you're signed on to your system with appropriate privileges to install and run an application.

  |   |                                                          |
  | - | -------------------------------------------------------- |
  |   | On Linux, install and run PingAccess as a non-root user. |

* Install a [supported Java runtime](pa_installation_requirements.html).

* The system or user environment variable `JAVA_HOME` must exist and be set to a value that represents the location of your Java installation, such as `usr/java/jdk 1.8.0_74`.

* Add the relevant Java directory path to the `PATH` variable so it's available for scripts that depend on it:

  * On Linux: Add the Java Runtime Environment (JRE) *(tooltip: \<div class="paragraph">
    \<p>A software layer that provides the class libraries and resources needed for a Java program to run.\</p>
    \</div>)* `/bin` directory path (for example, `usr/lib64/jvm/jre/bin`).

  * On Windows installer: Add the `javapath` directory path (for example, `C:\Program Files\Oracle\Java\javapath`).

  * On Windows CLI: Add the `javapath` directory path (for example, `C:\Program Files\Oracle\Java\javapath`).

* You must have a `pingaccess.lic` license file.

  |   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
  | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
  |   | If you do not have a PingAccess license, you can request an evaluation key at <https://support.pingidentity.com/s/>. During the first run of PingAccess, you will be prompted to upload the license file.If you are using an existing configuration file to configure the system, copy the configuration file to the system and rename it `data.json`. For more information about exporting the configuration from an existing system, see [Exporting PingAccess configurations](../pingaccess_user_interface_reference_guide/pa_exporting_pa_configs.html). |

- Linux

- Windows installer

- Windows CLI

## Installing PingAccess on Linux

### About this task

To install PingAccess on a Linux system:

### Steps

1. Download the distribution `.zip` archive from the [PingAccess downloads page](https://www.pingidentity.com/en/resources/downloads/pingaccess.html).

2. Extract the distribution `.zip` archive into your installation directory.

3. **Optional:** If you are using an existing configuration file to configure the system, move the `data.json` file to the `<PA_Home>/data/start-up-deployer` directory.

   |   |                                                                                                                                                                                                                                                    |
   | - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | When you start PingAccess for the first time, if this configuration is present it will be imported. After a successful import, the `data.json` file is deleted. If the configuration is present but cannot be imported, PingAccess is not started. |

   |   |                                                                                                                                                         |
   | - | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | If you're deploying PingAccess in a cluster configuration, see the [configuration documentation](../reference_guides/pa_configuring_a_pa_cluster.html). |

### Next steps

[Access the administrative console to complete the configuration](pa_accessing_the_admin_console.html).

## Installing PingAccess on Windows using the installer

### About this task

To install PingAccess on a Windows system using the installer:

### Steps

1. Download the PingAccess Windows installer from the [PingAccess downloads page](https://www.pingidentity.com/en/resources/downloads/pingaccess.html).

2. Double-click on the installer icon to launch the PingAccess setup wizard.

3. Click **Next** and follow the prompts to complete the installation using the following information for your selected operational mode.

   | Operational Mode             | Requirements                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
   | ---------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   | Standalone                   | Ports:- PingAccess administrative console: TCP 9000

   - PingAccess agent protocol: TCP 3030                                                                                                                                                                                                                                                                                                                                                                                          |
   | Clustered admin node         | Ports:- PingAccess administrative console: TCP 9000

   - Configuration query port: TCP 9090                                                                                                                                                                                                                                                                                                                                                                                           |
   | Clustered replica admin node | Ports:- PingAccess administrative console: TCP 9000

   - Configuration query port: TCP 9090Prerequisites:- You must install and configure a clustered admin node.

   - You must have a configuration data archive file available for the replica admin node. For more information, see [Clustering in PingAccess](../reference_guides/pa_clustering_ref_guide.html) in *Reference Guides*.&#xA;&#xA;Install the clustered replica admin node on a separate machine in the same network. |
   | Clustered engine node        | Ports:- PingAccess agent protocol: TCP 3030Prerequisites:- You must install a clustered admin node.

   - You must have a configuration data archive file available for the clustered engine node. For more information, see [Clustering in PingAccess](../reference_guides/pa_clustering_ref_guide.html) in *Reference Guides*.                                                                                                                                                       |

4. Copy the Uniform Resource Locator (URL) *(tooltip: \<div class="paragraph">
   \<p>Identifies a resource according to its internet location.\</p>
   \</div>)* of the PingAccess administrative console that is displayed on the final page of the PingAccess setup wizard, then click **Finish**.

5. To customize and finalize the PingAccess setup, paste the URL you copied into your web browser and connect to the administrative console of the instance you have just installed.

### Next steps

[Access the administrative console to complete the configuration](pa_accessing_the_admin_console.html).

## Installing PingAccess on Windows from the command line

### About this task

To install PingAccess on a Windows system from the CLI:

### Steps

1. Download the distribution `.zip` archive.

2. Extract the distribution `.zip` archive into your installation directory.

3. **Optional:** If you are using an existing configuration file to configure the system, move the `data.json` file to the `<PA_Home>/data/start-up-deployer` directory.

   |   |                                                                                                                                                                                                                                                    |
   | - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | When you start PingAccess for the first time, if this configuration is present it will be imported. After a successful import, the `data.json` file is deleted. If the configuration is present but cannot be imported, PingAccess is not started. |

### Next steps

[Access the administrative console to complete the configuration](pa_accessing_the_admin_console.html).

---

---
title: Managing the PingAccess Linux service
description: Configure PingAccess to run as a Linux systemv or systemd service, or remove the PingAccess Linux service.
component: pingaccess
version: 9.1
page_id: pingaccess:installing_and_uninstalling_pingaccess:pa_managing_pa_as_a_linux_service
canonical_url: https://docs.pingidentity.com/pingaccess/9.1/installing_and_uninstalling_pingaccess/pa_managing_pa_as_a_linux_service.html
llms_txt: https://docs.pingidentity.com/pingaccess/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 18, 2024
section_ids:
  about-this-task: About this task
  configuring-pingaccess-to-run-as-a-linux-systemv-service: Configuring PingAccess to run as a Linux systemv service
  about-this-task-2: About this task
  steps: Steps
  next-steps: Next steps
  configuring-pingaccess-to-run-as-a-linux-systemd-service: Configuring PingAccess to run as a Linux systemd service
  about-this-task-3: About this task
  steps-2: Steps
  removing-the-pingaccess-linux-service: Removing the PingAccess Linux service
  about-this-task-4: About this task
  steps-3: Steps
---

# Managing the PingAccess Linux service

Configure PingAccess to run as a Linux systemv or systemd service, or remove the PingAccess Linux service.

## About this task

Configuring PingAccess to run as a Linux systemv or systemd service causes it to start automatically when Linux starts.

|   |                                                                                             |
| - | ------------------------------------------------------------------------------------------- |
|   | To configure multiple instances of PingAccess as Linux services, see the Linux systemv tab. |

* Linux systemv

* Linux systemd

## Configuring PingAccess to run as a Linux systemv service

### About this task

|   |                                                                                                                                         |
| - | --------------------------------------------------------------------------------------------------------------------------------------- |
|   | The service script will only start if *\<JAVA\_HOME>* and *\<PA\_HOME>* are set and if the script can find the PingAccess license file. |

To configure multiple instances of PingAccess on a single host as Linux services, make the following modifications to the script for each service:

* Use a unique script name for each instance.

* Use a separate directory structure for each instance in the file system.

* Configure the following settings in the script file for each instance:

| Setting         | Description                                              |
| --------------- | -------------------------------------------------------- |
| *\<APPNAME>*    | A unique value for each instance.                        |
| *\<PA\_HOME>*   | The path to the PingAccess instance.                     |
| *\<JAVA\_HOME>* | The path to the Java installation folder.                |
| *\<USER>*       | Optional value for the username used to run the service. |

To configure PingAccess to run as a Linux systemv service:

### Steps

1. Copy the PingAccess script file from the `<PA_HOME>/sbin/linux/pingaccess` directory to the `/etc/init.d` directory.

2. **Optional:** Create a new user to run PingAccess.

3. Create the `/var/run/pingaccess` directory.

   |   |                                                                                             |
   | - | ------------------------------------------------------------------------------------------- |
   |   | Ensure that the user who will run the service has read and write permissions to the folder. |

4. Edit the `/etc/init.d/pingaccess` script file and set the values of the following variables at the beginning of the script:

   | Variable                  | Description                                                           |
   | ------------------------- | --------------------------------------------------------------------- |
   | `export <JAVA_HOME>=`     | Specify the Java install folder.                                      |
   | `export <PA_HOME>=`       | Specify the PingAccess install folder.                                |
   | `export USER=` (Optional) | Specify a username to run the service or leave empty for the default. |

5. To register the service, from the `/etc/init.d` directory, run:

   ```
   chkconfig --add pingaccess
   ```

6. To make the service script executable, run:

   ```
   chmod +x pingaccess
   ```

### Next steps

After registering, you can use the `service` command to control the PingAccess service. The available commands are:

* `start`

  Start the PingAccess service.

* `stop`

  Stop the PingAccess service.

* `restart`

  Restart the PingAccess service.

* `status`

  Show the status of the PingAccess service and the service process identifier (PID).

|   |                                                                                                        |
| - | ------------------------------------------------------------------------------------------------------ |
|   | The `service pingaccess status` command displays the current status of the running PingAccess service. |

## Configuring PingAccess to run as a Linux systemd service

### About this task

|   |                                                                                                                                         |
| - | --------------------------------------------------------------------------------------------------------------------------------------- |
|   | The service script will only start if *\<JAVA\_HOME>* and *\<PA\_HOME>* are set and if the script can find the PingAccess license file. |

To configure PingAccess to run as a Linux systemd service:

### Steps

1. Copy the configuration file from the `<PA_HOME>/sbin/linux/pingaccess.service` directory to the `/etc/systemd/system/pingaccess.service` directory.

2. In the `pingaccess.service` file, replace the following variables:

   * Replace *<${PA\_HOME}>* with the path to the PingAccess instance.

   * Replace *<${PA\_USER}>* with the username used to run the service.

   * Replace *<${PA\_JAVA\_HOME}>* with the path to the Java installation folder.

3. To allow read-write activity on the service, run:

   ```
   chmod 644 /etc/systemd/system/pingaccess.service
   ```

4. To load the systemd service, run:

   ```
   systemctl daemon-reload
   ```

5. To enable the service, run:

   ```
   systemctl enable pingaccess.service
   ```

6. To start the service, run:

   ```
   systemctl start pingaccess.service
   ```

## Removing the PingAccess Linux service

### About this task

|   |                                                         |
| - | ------------------------------------------------------- |
|   | You must run the following commands as the `root` user. |

To remove the PingAccess service from a Linux system:

### Steps

1. To stop the service, run the `/etc/init.d/pingaccess stop` command.

2. Run the `chkconfig --delete pingaccess` command.

3. **Optional:** Delete the `/etc/init.d/pingaccess` script.

---

---
title: Managing the PingAccess Windows service
description: Configure PingAccess to run as a Windows service through an installer or the command line, or remove the PingAccess Windows service.
component: pingaccess
version: 9.1
page_id: pingaccess:installing_and_uninstalling_pingaccess:pa_managing_pa_as_a_windows_service
canonical_url: https://docs.pingidentity.com/pingaccess/9.1/installing_and_uninstalling_pingaccess/pa_managing_pa_as_a_windows_service.html
llms_txt: https://docs.pingidentity.com/pingaccess/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 18, 2024
section_ids:
  before-you-begin: Before you begin
  about-this-task: About this task
  steps: Steps
  configuring-pingaccess-to-run-as-a-windows-service: Configuring PingAccess to run as a Windows service
  about-this-task-2: About this task
  steps-2: Steps
  result: Result
  configuring-pingaccess-to-run-as-a-windows-service-from-the-command-line: Configuring PingAccess to run as a Windows service from the command line
  about-this-task-3: About this task
  steps-3: Steps
  result-2: Result
  removing-the-pingaccess-windows-service: Removing the PingAccess Windows service
  before-you-begin-2: Before you begin
  about-this-task-4: About this task
  steps-4: Steps
---

# Managing the PingAccess Windows service

Configure PingAccess to run as a Windows service through an installer or the command line, or remove the PingAccess Windows service.

## Before you begin

[Install PingAccess](pa_installing_pa_on_your_system.html) and manually start the server to make sure that it runs normally. For more information, see [Accessing the administrative console for the first time](pa_accessing_the_admin_console.html).

|   |                                                                                                              |
| - | ------------------------------------------------------------------------------------------------------------ |
|   | If you installed PingAccess using the Windows installer, the service is installed and started automatically. |

## About this task

Configuring PingAccess as a Windows service causes it to start automatically when Windows starts. To configure PingAccess as a service on a Windows 64-bit operating system:

## Steps

1. Ensure that you are signed on with full administrator privileges.

2. Select one of the following tabs to proceed.

* Manual Installation

* From the Command Line

## Configuring PingAccess to run as a Windows service

### About this task

To configure PingAccess to run as a Windows service:

### Steps

1. Open a command prompt as an administrator.

2. In the command prompt, go to the `<PA_HOME>\sbin\windows` directory and run the `install-service.bat` file.

3. In Windows, go to **Control Panel → Administrative Tools → Services**.

4. From the list of available services, right-click **PingAccess Service** and select **Start**.

   You can change the default **Start type** setting in the **Properties** dialog.

### Result

The service starts immediately and restarts automatically on reboot.

## Configuring PingAccess to run as a Windows service from the command line

### About this task

To configure PingAccess to run as a Windows service from the command line:

### Steps

1. Go to the `<PA_HOME>\sbin\windows` directory and run the `install-service.bat` file.

2. To set the PingAccess service to start automatically, run `sc config PingAccess start= auto`.

### Result

The service starts immediately and restarts automatically on reboot.

## Removing the PingAccess Windows service

### Before you begin

Make sure you have PingAccess administrator privileges.

### About this task

To remove the PingAccess service from a Windows system:

### Steps

1. Open a command prompt.

2. Stop the PingAccess service.

3. Go to the `<PA_HOME>\sbin\windows` directory.

4. Run the `uninstall-service.bat` file.

5. After the script runs, remove the *\<PA\_HOME>* environment variable from the system.

---

---
title: Removing the PingAccess Linux service
description: You must run the following commands as the root user.
component: pingaccess
version: 9.1
page_id: pingaccess:installing_and_uninstalling_pingaccess:pa_removing_the_pa_linux_service
canonical_url: https://docs.pingidentity.com/pingaccess/9.1/installing_and_uninstalling_pingaccess/pa_removing_the_pa_linux_service.html
llms_txt: https://docs.pingidentity.com/pingaccess/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: May 8, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Removing the PingAccess Linux service

## About this task

|   |                                                         |
| - | ------------------------------------------------------- |
|   | You must run the following commands as the `root` user. |

To remove the PingAccess service from a Linux system:

## Steps

1. To stop the service, run the `/etc/init.d/pingaccess stop` command.

2. Run the `chkconfig --delete pingaccess` command.

3. **Optional:** Delete the `/etc/init.d/pingaccess` script.

---

---
title: Removing the PingAccess Windows service
description: Make sure you have PingAccess administrator privileges.
component: pingaccess
version: 9.1
page_id: pingaccess:installing_and_uninstalling_pingaccess:pa_removing_the_pa_windows_service
canonical_url: https://docs.pingidentity.com/pingaccess/9.1/installing_and_uninstalling_pingaccess/pa_removing_the_pa_windows_service.html
llms_txt: https://docs.pingidentity.com/pingaccess/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: May 8, 2024
section_ids:
  before-you-begin: Before you begin
  about-this-task: About this task
  steps: Steps
---

# Removing the PingAccess Windows service

## Before you begin

Make sure you have PingAccess administrator privileges.

## About this task

To remove the PingAccess service from a Windows system:

## Steps

1. Open a command prompt.

2. Stop the PingAccess service.

3. Go to the `<PA_HOME>\sbin\windows` directory.

4. Run the `uninstall-service.bat` file.

5. After the script runs, remove the *\<PA\_HOME>* environment variable from the system.

---

---
title: Running PingAccess as a service
description: PingAccess can run as a service on Linux and Windows 64-bit operating systems, enabling PingAccess to start automatically when the operating system starts.
component: pingaccess
version: 9.1
page_id: pingaccess:installing_and_uninstalling_pingaccess:pa_running_pa_as_a_service
canonical_url: https://docs.pingidentity.com/pingaccess/9.1/installing_and_uninstalling_pingaccess/pa_running_pa_as_a_service.html
llms_txt: https://docs.pingidentity.com/pingaccess/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: May 8, 2024
---

# Running PingAccess as a service

PingAccess can run as a service on Linux and Windows 64-bit operating systems, enabling PingAccess to start automatically when the operating system starts.

The service runs as the `root` (Linux) or `System` (Windows) user by default.

|   |                                                                                                                                                                                                                                                   |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Before setting PingAccess up to run as a service, manually start the server to make sure that PingAccess runs normally. For more information, see [Accessing the administrative console for the first time](pa_accessing_the_admin_console.html). |

* To manage PingAccess as a service on a Linux operating system, see [Managing the PingAccess Linux service](pa_managing_pa_as_a_linux_service.html).

* To manage PingAccess as a service on a Windows 64-bit operating system, see [Managing the PingAccess Windows service](pa_managing_pa_as_a_windows_service.html).

---

---
title: Starting PingAccess
description: After installing PingAccess, start the PingAccess service.
component: pingaccess
version: 9.1
page_id: pingaccess:installing_and_uninstalling_pingaccess:pa_starting_pa
canonical_url: https://docs.pingidentity.com/pingaccess/9.1/installing_and_uninstalling_pingaccess/pa_starting_pa.html
llms_txt: https://docs.pingidentity.com/pingaccess/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: May 8, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
  choose-from: Choose from:
  choose-from-2: Choose from:
  result: Result:
---

# Starting PingAccess

After installing PingAccess, start the PingAccess service.

## About this task

|   |                                                                                                              |
| - | ------------------------------------------------------------------------------------------------------------ |
|   | If you installed PingAccess using the Windows installer, the service is installed and started automatically. |

## Steps

1. In a command prompt or terminal window, change to the PingAccess `bin` directory:

   ### Choose from:

   * On Linux: `cd <PA_HOME>/bin`

   * On Windows: `cd <PA_HOME>\bin`

2. Start the `run` script for the platform:

   ### Choose from:

   * On Linux: `./run.sh`

   * On Windows: `run.bat`

### Result:

PingAccess starts when you see the message `PingAccess running…​` in the command window.