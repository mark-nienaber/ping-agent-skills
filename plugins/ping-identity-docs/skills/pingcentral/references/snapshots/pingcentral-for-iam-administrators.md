---
title: Configuring logging
description: Instructions for configuring logging for PingCentral.
component: pingcentral
version: 3.1.1
page_id: pingcentral:pingcentral_for_iam_administrators:pingcentral_installing_configuring/pingcentral_logging
canonical_url: https://docs.pingidentity.com/pingcentral/3.1.1/pingcentral_for_iam_administrators/pingcentral_installing_configuring/pingcentral_logging.html
revdate: October 9, 2025
section_ids:
  steps: Steps
---

# Configuring logging

The log file serves as a record of events that occurred within the system and is often used for troubleshooting purposes. This section explains how to access the log file, interpret the entries within it, and change the level of detail the log file captures.

## Steps

1. Access the PingCentral log file from the following location: `/<pingcentral_install>/log/application.log`.

   The level of detail that the log file contains depends on how the logging level is set. Logging levels are a means of categorizing the entries in your log file by severity, and are described in the following table. Detailed log files require more system resources, so PingCentral only records errors, warnings, and some information events by default.

   | Logging level | Description                                                                                                                                                                |
   | ------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   | ERROR         | Indicates a failure within the application occurred.                                                                                                                       |
   | WARNING       | Indicates the system detected an unusual situation and errors might occur.                                                                                                 |
   | INFO          | Provide basic information about activities that occurred. For example, a service was started and stopped, or a new user was added to the application.                      |
   | DEBUG         | Provides additional detail regarding the events that occurred, and is often used to diagnose and troubleshoot reported issues.                                             |
   | TRACE         | Provides even more detailed information than the Debug level regarding the application's behavior. This logging level is not used often and can affect system performance. |

2. Changing the logging level to have the system record additional details can help with troubleshooting. To change the logging level:

   1. Open the configuration file at `/<pingcentral_install>/conf/log4j2.xml`.

   2. Scroll down, locate the Logger line item shown below, and change the logging level within the quotations. The` DEBUG` logging level provides enough information to troubleshoot most issues.

      ```
      <Logger name="com.pingidentity" level="INFO" additivity="false" includeLocation="false">
      	<!--<AppenderRef ref="console"/>-->
      	<AppenderRef ref="file"/>
      </Logger>
      ```

   3. Save and close the file and repeat the task you performed when the error occurred.

   4. For optimal system performance, open the `log4j2.xml` file again and change the logging level back to `INFO`.

   5. Access the `application.log` file again and review the information that was recorded in `DEBUG` mode. If you are working with a technical support team to troubleshoot an issue, you can send them the log file that recorded your activities.

---

---
title: Configuring MTLS
description: Instructions for importing a client TLS key pair so that you can use MTLS for admin API authentication.
component: pingcentral
version: 3.1.1
page_id: pingcentral:pingcentral_for_iam_administrators:pingcentral_installing_configuring/pingcentral_config_mtls
canonical_url: https://docs.pingidentity.com/pingcentral/3.1.1/pingcentral_for_iam_administrators/pingcentral_installing_configuring/pingcentral_config_mtls.html
revdate: April 10, 2025
section_ids:
  steps: Steps
---

# Configuring MTLS

To use mutual TLS (MTLS) for Admin API authentication, import a client TLS key pair. If you're running PingCentral in FIPS-compliant mode, you'll import a `.pem` file, as `.p12` files are not allowed.

|   |                                                                                                                                   |
| - | --------------------------------------------------------------------------------------------------------------------------------- |
|   | Only RSA keys are supported. If you attempt to import Elliptic Curve (EC) keys, you'll receive a parsing or import error message. |

## Steps

1. Select the **Security** tab, expand the menu, and select **Client TLS Key Pair**.

2. Click **Import Key Pair**.

3. On the **Import Key Pair** page, click **Choose PKCS12 or PEM File** and select the `.p12` or `.pem` file to upload it.

4. In the **File Password** field, enter the password to the key store file.

   |   |                                                                                                                                                      |
   | - | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | If you're running PingCentral in FIPS-compliant mode, your password must be at least 14 characters long, and the RSA key must be at least 2048 bits. |

5. In the **Alias** field, specify the alias of the certificate in the key store file that you want to use, if required.

6. In the **Key Password** field, enter the password for the selected certificate if the PKCS12 file requires a separate password for the key.

7. Click **Import**.

---

---
title: Configuring PingAccess for SSO
description: Instructions for configuring PingCentral to use SSO to access PingAccess.
component: pingcentral
version: 3.1.1
page_id: pingcentral:pingcentral_for_iam_administrators:pingcentral_installing_configuring/pingcentral_pa_sso
canonical_url: https://docs.pingidentity.com/pingcentral/3.1.1/pingcentral_for_iam_administrators/pingcentral_installing_configuring/pingcentral_pa_sso.html
revdate: October 15, 2025
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Configuring PingAccess for SSO

## About this task

To use SSO to access PingAccess from PingCentral:

## Steps

1. Configure a new PingFederate client:

   1. In PingFederate, go to **Applications → OAuth → Clients**.

   2. On the **Manage Client** tab, complete these fields:

      * **Client ID**: Enter a unique identifier for the client.

      * **Name**: Enter a name for the client.

      * **Description**: Enter a description of the client.

        Learn more in [Defining the access token attribute contract](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_defining_access_token_attribute_contract.html) in the PingFederate documentation.

        ![In this example, the Client ID and Name field are completed and the Client Secret option is selected.](../_images/eqf1656367100432.jpg)

   3. In the **Client Authentication** field, select **Client Secret**.

   4. In the **Client Secret** field, you can:

      | Option                       | Description                                                                                                                                        |
      | ---------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- |
      | Create or generate a secret. | Choose from:- To create a strong, random alphanumeric string, click **Generate Secret**.

      - Manually enter a secret.                               |
      | Modify an existing secret.   | 1. Select the **Change Secret** check box.

      2. Click **Generate Secret** to create a strong random alphanumeric string or manually enter a secret. |

   5. In the **Grant Types** field, select the **Client Credentials** and **Access Token Validation (Client is a Resource Server)** options.

   6. In the **Default Access Token Manager** field, select **JSON Web Tokens** . Click **Save**.

   7. Access the PingFederate `<pf_install>/pingfederate/bin/run.properties` file, and ensure that this property is set: `pf.admin.api.authentication=OAuth2`.

   8. Access the PingFederate `<pf_install>/pingfederate/bin/oauth2.properties` file, and ensure that the following properties are set.

      | Property                  | Description                                                                                                                                                                                                                                                                |
      | ------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
      | `client.id`               | The unique client identifier defined in step 2.                                                                                                                                                                                                                            |
      | `client.secret`           | The client secret defined in step 4.                                                                                                                                                                                                                                       |
      | `introspection.endpoint`  | This URL specifies where PingFederate validates the authentication token.For example, `https://<PF_RUNTIME_HOST>:<PF_RUNTIME_PORT>/as/introspect.oauth2`                                                                                                                   |
      | `required.scopes`         | Use any of the scopes defined in PingFederate.Go to **System → OAuth Settings → Scope Management** to see a list of available scopes.For details, see [Scopes](https://docs.pingidentity.com/csh?Product=pf-latest\&context=pf_scopes) in the *PingFederate Server* guide. |
      | `username.attribute.name` | The value mapped to the **Username** attribute defined on the **Contract Fulfillment** tab.                                                                                                                                                                                |
      | `role.attribute.name`     | The value mapped to the **admin\_role** attribute defined on the **Contract Fulfillment** tab.                                                                                                                                                                             |

2. Configure PingAccess:

   1. In PingAccess, go to **System → System Settings → Admin Authentication**.

   2. On the **Admin API OAuth** tab, select **Enable** and complete these fields as shown in the example:

      * **Client ID**: Enter the unique client identifier for the new client.

      * **Client Secret**: Enter the client secret defined for the new client.

      * **Scope**: Enter the scopes set as required scopes for the new client.

      * **Subject Attribute Name**: Enter the name of an access token attribute that you want to use as the **Subject** field in audit log entries for the admin API.

        ![In this example, the Admin API OAuth - Enabled tab is displayed in PingAccess.](../_images/apr1656367152907.jpg)

   3. Click **Save**.

3. Configure PingCentral:

   1. In PingCentral, to connect to the new PingFederate client, go to **Environments → Add Environments**.

   2. On the **Connect to Instances** page, scroll down and select **PingAccess**.

   3. Complete the following fields using the properties you just set in PingAccess.

      ![In this example, the Connect to Instances page in PingCentral is displayed.](../_images/pdd1656368680536.jpg)

      * **PingAccess Admin**: Enter the link to access PingAccess.

      * **Authentication Method**: Select **Native** or**OAuth2**.

      * **Token Endpoint URL**: Enter the token endpoint URL, which is available here in PingFederate:`https://<PF_RUNTIME_HOST>:<PF_RUNTIME_PORT>/.well-known/openid-configuration`.

      * **Client ID**: Enter the unique identifier for the new client.

      * **Client Secret**: Enter the client secret defined for the new client.

      * **Scopes**: Enter the scopes set as required scopes for the new client.

   4. Click **Next**.

---

---
title: Configuring PingCentral to run as a Linux systemd service
description: Instructions for running PingCentral as a Linux systemd service.
component: pingcentral
version: 3.1.1
page_id: pingcentral:pingcentral_for_iam_administrators:pingcentral_installing_configuring/pingcentral_conf_pc_linux_systemd
canonical_url: https://docs.pingidentity.com/pingcentral/3.1.1/pingcentral_for_iam_administrators/pingcentral_installing_configuring/pingcentral_conf_pc_linux_systemd.html
revdate: October 9, 2025
section_ids:
  before-you-begin: Before you begin
  steps: Steps
  removing-the-pingcentral-systemd-service: Removing the PingCentral systemd service
  steps-2: Steps
---

# Configuring PingCentral to run as a Linux systemd service

Run PingCentral as a Linux systemd service that automatically starts when Linux starts.

## Before you begin

Ensure that:

* You are signed on to your system as a root user.

* The *\<JAVA-HOME>* path points to the Java Development Kit (JDK) software on your system. For example, `usr/java/jdk11.0_4`.

* The *\<PINGCENTRAL\_HOME>* path points to the folder extracted from the `.zip` archive in your installation directory. Ensure that this path does not reside within a user's home folder.

## Steps

1. Copy the `pingcentral.service` configuration file from `$PINGCENTRAL_HOME/sbin/linux/pingcentral.service` to `/lib/systemd/system/pingcentral.service`.

   |   |                                                                                   |
   | - | --------------------------------------------------------------------------------- |
   |   | You can also copy this file to the `/etc/systemd/system` location, if appropriate |

2. Open the `pingcentral.service` file and assign appropriate values to the following variables:

   * *\<PINGCENTRAL\_HOME>*: Labeled "WorkingDirectory."

   * *\<PINGCENTRAL\_USER>*: Labeled "User."

   * *\<JAVA\_HOME>*: Labeled "Environment."

3. Enable read and write activity for the service using the `chmod 644 /lib/systemd/system/pingcentral.service` command.

   If you copied this file to the /etc/systemd/system location in step 1, use this command instead: `chmod 644 /etc/systemd/system/pingcentral.service`.

4. Load the systemd service using the `systemctl daemon-reload` command.

5. Enable the service using the `systemctl enable pingcentral.service` command.

6. Start the service using the `systemctl start pingcentral.service` command.

## Removing the PingCentral systemd service

If you have privileges that allow you to install applications, you can remove the PingCentral systemv service.

### Steps

1. Sign on to the system as a root user.

   | Option             | Description                                     |
   | ------------------ | ----------------------------------------------- |
   | Stop the service   | Run the `/etc/init.d/pingcentral stop` command. |
   | Delete the service | Run the `chkconfig --del pingcentral` command.  |

2. Delete the `/etc/init.d/pingcentral` script if it is no longer needed.

---

---
title: Configuring PingCentral to run as a Linux systemv service
description: Instructions for running PingCentral as a Linux systemv service.
component: pingcentral
version: 3.1.1
page_id: pingcentral:pingcentral_for_iam_administrators:pingcentral_installing_configuring/pingcentral_conf_pc_linux_systemv
canonical_url: https://docs.pingidentity.com/pingcentral/3.1.1/pingcentral_for_iam_administrators/pingcentral_installing_configuring/pingcentral_conf_pc_linux_systemv.html
revdate: October 9, 2025
section_ids:
  before-you-begin: Before you begin
  steps: Steps
  removing-the-pingcentral-systemv-service: Removing the PingCentral systemv service
  steps-2: Steps
---

# Configuring PingCentral to run as a Linux systemv service

Run PingCentral as a Linux systemv service that automatically starts when Linux starts.

## Before you begin

Ensure that:

* You are signed on to your system as a root user.

* The *\<JAVA\_HOME>*`JAVA_HOME` path points to the Java Development Kit (JDK) software on your system. For example, `/usr/lib/jvm/java-11-openjdk-11.0.5.10-0.e17_7.x86_64`. To verify this information, run the `echo $JAVA_HOME` command.

* The `PINGCENTRAL_HOME` path points to the folder extracted from the `.zip` archive in your installation directory. Ensure that this path doesn't reside within a user's home folder.

## Steps

1. Copy the `pingcentral` file from `<PINGCENTRAL_HOME>/sbin/linux/pingcentral` to `/etc/init.d`.

2. Create a new user to run PingCentral. You might want to create a new user account for each service you run as a way of keeping your services separate, or associate the account with a running process.

3. Create a new `pingcentral` folder in `/var/run/pingcentral` and ensure that the user who will run the service has read and write permissions to the folder.

4. Access the `pingcentral` file in the `/etc/init.d` folder and set values for the following variables at the beginning of the script:

   * `export <JAVA-HOME>`: Specify the name and location of the Java installation folder.

   * `export <PINGCENTRAL_HOME>`: Specify the name and location of the PingCentral installation folder.

   * (Optional): `export USER`: Specify the name of the user who will run the service, if applicable.

5. Register the service by running the `chkconfig --add pingcentral` command from the `/etc/init.d` folder.

6. Make the service script executable by running the `chmod +x pingcentral` command.

   After registering the service, you can control it by running the `pingcentral` command from the `/etc/init.d` folder with the following options:

   * `start`: Starts the PingCentral service.

   * `stop`: Stops the PingCentral service.

   * `restart`: Restarts the PingCentral service.

   * `status`: Displays the status of the PingCentral service and the service process ID.

## Removing the PingCentral systemv service

If you have privileges that allow you to install applications, you can remove the PingCentral systemd service.

### Steps

1. Sign on to the system as a root user.

   | Option              | Description                                      |
   | ------------------- | ------------------------------------------------ |
   | Stop the service    | Run the `systemctl stop pingcentral` command.    |
   | Disable the service | Run the `systemctl disable pingcentral` command. |

2. Delete the `/etc/systemd/system/pingcentral.service` script if it is no longer needed.

---

---
title: Configuring PingCentral to run as a Windows service
description: Instructions for configuring PingCentral to run as a Windows service.
component: pingcentral
version: 3.1.1
page_id: pingcentral:pingcentral_for_iam_administrators:pingcentral_installing_configuring/pingcentral_conf_pc_windows
canonical_url: https://docs.pingidentity.com/pingcentral/3.1.1/pingcentral_for_iam_administrators/pingcentral_installing_configuring/pingcentral_conf_pc_windows.html
revdate: October 9, 2025
section_ids:
  before-you-begin: Before you begin
  steps: Steps
  removing-the-pingcentral-windows-service: Removing the PingCentral Windows service
  steps-2: Steps
---

# Configuring PingCentral to run as a Windows service

Run PingCentral as a Windows service that automatically starts when Windows starts.

## Before you begin

Manually start the server to ensure that PingCentral is running as expected.

|   |                                                                                       |
| - | ------------------------------------------------------------------------------------- |
|   | You must have administrator privileges to configure PingCentral as a Windows service. |

## Steps

1. In the Windows **Search** field, enter `cmd` to access the command prompt.

2. Right-click **Command Prompt** and select **Run as administrator** in the menu.

3. In the command prompt, change directories to the `$PINGCENTRAL_HOME\sbin\windows` directory and run the `install-service.bat` script.

4. Open the Windows Control Panel. In the search field, enter `view local services`.

5. In the list of available services, right-click **PingCentral Service** , and select **Start**.

   The service starts immediately and restarts automatically when rebooted, by default.

## Removing the PingCentral Windows service

If you have administrator privileges, you can remove the PingCentral Windows service.

### Steps

1. In the Windows **Search** field, enter `cmd` to access the command prompt.

2. Right-click **Command Prompt** and select **Run as administrator** in the menu.

3. In the command prompt, change to the `<PINGCENTRAL_HOME>\sbin\windows` directory and run the `uninstall-service.bat` script.

4. After the script is finished running, remove the *\<PINGCENTRAL\_HOME>* environment variable from the system.

---

---
title: Configuring PingCentral to run in FIPS-compliant mode
description: Instructions on configuring PingCentral to run in FIPS-compliant mode.
component: pingcentral
version: 3.1.1
page_id: pingcentral:pingcentral_for_iam_administrators:pingcentral_installing_configuring/pingcentral_fips_mode
canonical_url: https://docs.pingidentity.com/pingcentral/3.1.1/pingcentral_for_iam_administrators/pingcentral_installing_configuring/pingcentral_fips_mode.html
revdate: October 16, 2025
---

# Configuring PingCentral to run in FIPS-compliant mode

Running PingCentral in FIPS-compliant mode guarantees that all cryptographic algorithms and protocols meet the U.S. federal standard for security compliance. When you're connecting PingCentral to an external database, you must use a FIPS-compliant authentication method.

PingCentral is currently running FIPS 140-3. Learn more about this version in [FIPS 140-3](https://csrc.nist.gov/pubs/fips/140-3/final).

To enable this option, access the `<PingCentral_install>/conf/application.properties` file and set the `pingcentral.fips.enabled` property value to `true`.

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | If on Linux systems, the Bouncy Castle FIPS-approved secure random number generator might drain a large amount of entropy during initial seeding. If available entropy becomes too low, the PingCentral server or bundled command-line tools could stall on startup for an extended period of time. If this occurs, then you will likely need to integrate with a hardware random number generator or install an entropy-supplementing daemon like `rngd`. |

---

---
title: Configuring PingFederate and PingAccess for SSO
description: Instructions for configuring PingCentral, PingFederate, and PingAccess for SSO.
component: pingcentral
version: 3.1.1
page_id: pingcentral:pingcentral_for_iam_administrators:pingcentral_installing_configuring/pingcentral_pf_pa_sso
canonical_url: https://docs.pingidentity.com/pingcentral/3.1.1/pingcentral_for_iam_administrators/pingcentral_installing_configuring/pingcentral_pf_pa_sso.html
revdate: October 9, 2025
section_ids:
  configuring-pingfederate-for-sso: Configuring PingFederate for SSO
  about-this-task: About this task
  steps: Steps
  configuring-pingaccess-for-sso: Configuring PingAccess for SSO
  about-this-task-2: About this task
  steps-2: Steps
---

# Configuring PingFederate and PingAccess for SSO

To access PingFederate or PingAccess from PingCentral using single sign-on (SSO), each application must be correctly configured.

|   |                                                                                                                                                                                       |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | You can configure PingFederate to use OAuth2 or a native sign-on to connect to PingCentral, but not both. You can configure PingAccess to use either native sign-on, OAuth2, or both. |

## Configuring PingFederate for SSO

### About this task

To access PingFederate from PingCentral using SSO:

### Steps

1. Review the PingFederate configurations:

   1. In PingFederate, go to **Applications → OAuth → Access Token Management** and ensure that JSON web tokens are configured, as shown in this example.

      Learn more in [Defining the access token attribute contract](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_defining_access_token_attribute_contract.html) in the PingFederate documentation.

      ![In this example, JSON Web Tokens are configured on the Access Token Management page in PingFederate.](../_images/dwp1656366873662.jpg)

   2. On the **Access Token Attribute Contract** tab, ensure that the access token attribute contract includes the following attributes, as listed here and shown in this example.

      * `admin_role`

      * `Username`

        Learn more in [Defining the access token attribute contract](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_defining_access_token_attribute_contract.html) in the PingFederate documentation.

        ![In this example, admin role and Username are configured on the Access Token Attribute Contract tab in PingFederate.](../_images/ugs1656366986886.jpg)

   3. Go to **Applications → OAuth → Access Token Mappings** and ensure that **Client Credentials** are mapped to use**JSON Web Tokens** as the access token manager, as shown in this example. Click **Add Mapping**.

      ![In this example, Client Credentails is mapped to JSON Web Tokens on the Access Token Mappings page in PingFederate.](../_images/gvp1656367019887.jpg)

   4. On the **Contract Fulfillment** tab, ensure that the access token attributes in the contract are correctly mapped and the following attributes are included in the contract:

      * `Username`: The username of the administrator used to access APIs.

      * `admin_role`: This multivalued attribute must include the `admin` and `cryptoadmin` roles. In this example, an OGNL expression is used to include these values.

        ![In this example, admin\_role is an expression mapped to an OGNL expression and Username is mapped to value.](../_images/ehl1656367060970.jpg)

2. Configure a new PingFederate client:

   1. In PingFederate, go to **Applications → OAuth → Clients**.

   2. On the **Manage Client** tab, complete these fields:

      * **Client ID**: Enter a unique identifier for the client.

      * **Name**: Enter a name for the client.

      * **Description**: Enter a description of the client.

        Learn more in [Configuring OAuth clients](https://docs.pingidentity.com/pingfederate/12.3/administrators_reference_guide/pf_configuring_oauth_clients.html) in the PingFederate documentation. -

        ![In this example, the Client ID and Name field are completed and the Client Secret option is selected.](../_images/eqf1656367100432.jpg)

   3. In the **Client Authentication** field, select **Client Secret**.

   4. In the **Client Secret** field, you can:

      | Option                       | Description                                                                                                                                        |
      | ---------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- |
      | Create or generate a secret. | Choose from:- To create a strong, random alphanumeric string, click **Generate Secret**.

      - Manually enter a secret.                               |
      | Modify an existing secret.   | 1. Select the **Change Secret** check box.

      2. Click **Generate Secret** to create a strong random alphanumeric string or manually enter a secret. |

   5. In the **Grant Types** field, select the **Client Credentials** and **Access Token Validation (Client is a Resource Server)** options.

   6. In the **Default Access Token Manager** field, select **JSON Web Tokens** . Click **Save**.

   7. Access the PingFederate `<pf_install>/pingfederate/bin/run.properties` file, and ensure that this property is set: `pf.admin.api.authentication=OAuth2`.

   8. Access the PingFederate `<pf_install>/pingfederate/bin/oauth2.properties` file, and ensure that the following properties are set.

      | Property                  | Description                                                                                                                                                                                                                                                                |
      | ------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
      | `client.id`               | The unique client identifier defined in step 2.                                                                                                                                                                                                                            |
      | `client.secret`           | The client secret defined in step 4.                                                                                                                                                                                                                                       |
      | `introspection.endpoint`  | This URL specifies where PingFederate validates the authentication token.For example, `https://<PF_RUNTIME_HOST>:<PF_RUNTIME_PORT>/as/introspect.oauth2`                                                                                                                   |
      | `required.scopes`         | Use any of the scopes defined in PingFederate.Go to **System → OAuth Settings → Scope Management** to see a list of available scopes.For details, see [Scopes](https://docs.pingidentity.com/csh?Product=pf-latest\&context=pf_scopes) in the *PingFederate Server* guide. |
      | `username.attribute.name` | The value mapped to the **Username** attribute defined on the **Contract Fulfillment** tab.                                                                                                                                                                                |
      | `role.attribute.name`     | The value mapped to the **admin\_role** attribute defined on the **Contract Fulfillment** tab.                                                                                                                                                                             |

3. Configure PingCentral:

   1. In PingCentral, to connect to the new PingFederate client, go to **Environments → Add Environments**.

   2. On the **Connect to Instances** page, complete the following fields using the properties you just set in the PingFederate `oauth2.properties` file.

      ![In this example, the Connect to Instances page in PingCentral is displayed.](../_images/zrg1656367226738.jpg)

      * **PingFederate Admin**: Enter the URL defined in the `pf.admin.baseurl` property for the new client. For details, see [Configuring PingFederate properties](https://docs.pingidentity.com/csh?Product=pf-latest\&context=pf_config_pf_propert) in the *PingFederate Server* guide.

      * **Authentication Method**: Select **OAuth2**.

      * **Token Endpoint URL**: Enter the token endpoint URL, which is PingFederate: `https://<PF_RUNTIME_HOST>:<PF_RUNTIME_PORT>/as/token.oauth2`.

      * **Client ID**: Enter the unique client identifier set as the `client.id` property.

      * **Client Secret**: Enter the client secret set as the `client.secret` property.

      * **Scopes**: Enter the scopes set as the `required.scopes` property.

4. Click **Next**.

## Configuring PingAccess for SSO

### About this task

To use SSO to access PingAccess from PingCentral:

### Steps

1. Configure a new PingFederate client:

   1. In PingFederate, go to **Applications → OAuth → Clients**.

   2. On the **Manage Client** tab, complete these fields:

      * **Client ID**: Enter a unique identifier for the client.

      * **Name**: Enter a name for the client.

      * **Description**: Enter a description of the client.

        Learn more in [Defining the access token attribute contract](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_defining_access_token_attribute_contract.html) in the PingFederate documentation.

        ![In this example, the Client ID and Name field are completed and the Client Secret option is selected.](../_images/eqf1656367100432.jpg)

   3. In the **Client Authentication** field, select **Client Secret**.

   4. In the **Client Secret** field, you can:

      | Option                       | Description                                                                                                                                        |
      | ---------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- |
      | Create or generate a secret. | Choose from:- To create a strong, random alphanumeric string, click **Generate Secret**.

      - Manually enter a secret.                               |
      | Modify an existing secret.   | 1. Select the **Change Secret** check box.

      2. Click **Generate Secret** to create a strong random alphanumeric string or manually enter a secret. |

   5. In the **Grant Types** field, select the **Client Credentials** and **Access Token Validation (Client is a Resource Server)** options.

   6. In the **Default Access Token Manager** field, select **JSON Web Tokens** . Click **Save**.

   7. Access the PingFederate `<pf_install>/pingfederate/bin/run.properties` file, and ensure that this property is set: `pf.admin.api.authentication=OAuth2`.

   8. Access the PingFederate `<pf_install>/pingfederate/bin/oauth2.properties` file, and ensure that the following properties are set.

      | Property                  | Description                                                                                                                                                                                                                                                                |
      | ------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
      | `client.id`               | The unique client identifier defined in step 2.                                                                                                                                                                                                                            |
      | `client.secret`           | The client secret defined in step 4.                                                                                                                                                                                                                                       |
      | `introspection.endpoint`  | This URL specifies where PingFederate validates the authentication token.For example, `https://<PF_RUNTIME_HOST>:<PF_RUNTIME_PORT>/as/introspect.oauth2`                                                                                                                   |
      | `required.scopes`         | Use any of the scopes defined in PingFederate.Go to **System → OAuth Settings → Scope Management** to see a list of available scopes.For details, see [Scopes](https://docs.pingidentity.com/csh?Product=pf-latest\&context=pf_scopes) in the *PingFederate Server* guide. |
      | `username.attribute.name` | The value mapped to the **Username** attribute defined on the **Contract Fulfillment** tab.                                                                                                                                                                                |
      | `role.attribute.name`     | The value mapped to the **admin\_role** attribute defined on the **Contract Fulfillment** tab.                                                                                                                                                                             |

2. Configure PingAccess:

   1. In PingAccess, go to **System → System Settings → Admin Authentication**.

   2. On the **Admin API OAuth** tab, select **Enable** and complete these fields as shown in the example:

      * **Client ID**: Enter the unique client identifier for the new client.

      * **Client Secret**: Enter the client secret defined for the new client.

      * **Scope**: Enter the scopes set as required scopes for the new client.

      * **Subject Attribute Name**: Enter the name of an access token attribute that you want to use as the **Subject** field in audit log entries for the admin API.

        ![In this example, the Admin API OAuth - Enabled tab is displayed in PingAccess.](../_images/apr1656367152907.jpg)

   3. Click **Save**.

3. Configure PingCentral:

   1. In PingCentral, to connect to the new PingFederate client, go to **Environments → Add Environments**.

   2. On the **Connect to Instances** page, scroll down and select **PingAccess**.

   3. Complete the following fields using the properties you just set in PingAccess.

      ![In this example, the Connect to Instances page in PingCentral is displayed.](../_images/pdd1656368680536.jpg)

      * **PingAccess Admin**: Enter the link to access PingAccess.

      * **Authentication Method**: Select **Native** or**OAuth2**.

      * **Token Endpoint URL**: Enter the token endpoint URL, which is available here in PingFederate:`https://<PF_RUNTIME_HOST>:<PF_RUNTIME_PORT>/.well-known/openid-configuration`.

      * **Client ID**: Enter the unique identifier for the new client.

      * **Client Secret**: Enter the client secret defined for the new client.

      * **Scopes**: Enter the scopes set as required scopes for the new client.

   4. Click **Next**.

---

---
title: Configuring PingFederate as a PingAccess token provider
description: This topic explains how to configure PingFederate as the PingAccess token provider.
component: pingcentral
version: 3.1.1
page_id: pingcentral:pingcentral_for_iam_administrators:pingcentral_pf_as_pa_token/pingcentral_configuring_pf_token_provider
canonical_url: https://docs.pingidentity.com/pingcentral/3.1.1/pingcentral_for_iam_administrators/pingcentral_pf_as_pa_token/pingcentral_configuring_pf_token_provider.html
revdate: October 7, 2025
section_ids:
  about-this-task: About this task
  steps: Steps
  trusted_certs: Adding trusted CA certificates to PingCentral
  steps-2: Steps
---

# Configuring PingFederate as a PingAccess token provider

To add PingAccess environments to PingCentral, PingFederate must be configured as the token provider. If you have PingFederate and PingAccess environments established, this configuration is likely in place.

## About this task

To configure PingFederate as the token provider for PingAccess, the Issuer URL in PingAccess must either match the Base URL in PingFederate, or one of the virtual hosts defined in PingFederate.

## Steps

1. To configure PingFederate as a PingAccess token provider, ensure the PingAccess **Issuer URL** and the PingFederate **Base URL** match.

   If a virtual host is defined in PingFederate, continue to step 3.

2. To locate this information:

   * In PingFederate, to locate the **Base URL** field, go to **System → Protocol Settings → Federation Info**, as shown in the following example.

     ![vea1593387214750](../_images/vea1593387214750.jpg)

   * In PingAccess, to locate the **Issuer URL** field, go to **System → Token Provider**.

     |   |                                                                                                      |
     | - | ---------------------------------------------------------------------------------------------------- |
     |   | In some versions of PingAccess, the Issuer URL might exist as separate **Host** and **Port** fields. |

     ![tlc1593529388921](../_images/tlc1593529388921.jpg)

3. If a virtual host is defined in PingFederate, the PingAccess Issuer URL can reference that instead of Base URL. In PingFederate, to locate the virtual host, go the **System → Virtual Host Names** page and review the information in the **Host Domain Name** field.

   ![oct1593529731877](../_images/oct1593529731877.jpg)

## Adding trusted CA certificates to PingCentral

For application owners to securely promote Security Assertion Markup Language (SAML) *(tooltip: \<div class="paragraph">
\<p>A standard, XML-based, message-exchange framework enabling the secure transmittal of authentication tokens and other user attributes across domains.\</p>
\</div>)* applications to PingFederate and PingAccess environments, trusted certificate authority (CA) *(tooltip: \<div class="paragraph">
\<p>An entity that issues digital certificates.\</p>
\</div>)* certificates must be available in PingCentral.

### Steps

1. To add a trusted certificate to PingCentral, select the **Settings** tab.

2. Expand the **Security** menu and select **Trusted CA Certificates**.

   The **Trusted CA Certificates** page displays a list of the certificates currently available in PingCentral.

3. Click **Add Certificate**.

4. In the **Add Certificate** window, in the **Alias** field, enter a unique name for the certificate.

5. Click **Choose File**, select the certificate, and click **Add** to upload it.

   The certificate displays in the list of trusted CA certificates.

6. Click the **Expand** icon for the certificate to view details.

---

---
title: Configuring PingFederate for SSO
description: To access PingFederate from PingCentral using SSO:
component: pingcentral
version: 3.1.1
page_id: pingcentral:pingcentral_for_iam_administrators:pingcentral_installing_configuring/pingcentral_pf_sso
canonical_url: https://docs.pingidentity.com/pingcentral/3.1.1/pingcentral_for_iam_administrators/pingcentral_installing_configuring/pingcentral_pf_sso.html
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Configuring PingFederate for SSO

## About this task

To access PingFederate from PingCentral using SSO:

## Steps

1. Review the PingFederate configurations:

   1. In PingFederate, go to **Applications → OAuth → Access Token Management** and ensure that JSON web tokens are configured, as shown in this example.

      Learn more in [Defining the access token attribute contract](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_defining_access_token_attribute_contract.html) in the PingFederate documentation.

      ![In this example, JSON Web Tokens are configured on the Access Token Management page in PingFederate.](../_images/dwp1656366873662.jpg)

   2. On the **Access Token Attribute Contract** tab, ensure that the access token attribute contract includes the following attributes, as listed here and shown in this example.

      * `admin_role`

      * `Username`

        Learn more in [Defining the access token attribute contract](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_defining_access_token_attribute_contract.html) in the PingFederate documentation.

        ![In this example, admin role and Username are configured on the Access Token Attribute Contract tab in PingFederate.](../_images/ugs1656366986886.jpg)

   3. Go to **Applications → OAuth → Access Token Mappings** and ensure that **Client Credentials** are mapped to use**JSON Web Tokens** as the access token manager, as shown in this example. Click **Add Mapping**.

      ![In this example, Client Credentails is mapped to JSON Web Tokens on the Access Token Mappings page in PingFederate.](../_images/gvp1656367019887.jpg)

   4. On the **Contract Fulfillment** tab, ensure that the access token attributes in the contract are correctly mapped and the following attributes are included in the contract:

      * `Username`: The username of the administrator used to access APIs.

      * `admin_role`: This multivalued attribute must include the `admin` and `cryptoadmin` roles. In this example, an OGNL expression is used to include these values.

        ![In this example, admin\_role is an expression mapped to an OGNL expression and Username is mapped to value.](../_images/ehl1656367060970.jpg)

2. Configure a new PingFederate client:

   1. In PingFederate, go to **Applications → OAuth → Clients**.

   2. On the **Manage Client** tab, complete these fields:

      * **Client ID**: Enter a unique identifier for the client.

      * **Name**: Enter a name for the client.

      * **Description**: Enter a description of the client.

        Learn more in [Configuring OAuth clients](https://docs.pingidentity.com/pingfederate/12.3/administrators_reference_guide/pf_configuring_oauth_clients.html) in the PingFederate documentation. -

        ![In this example, the Client ID and Name field are completed and the Client Secret option is selected.](../_images/eqf1656367100432.jpg)

   3. In the **Client Authentication** field, select **Client Secret**.

   4. In the **Client Secret** field, you can:

      | Option                       | Description                                                                                                                                        |
      | ---------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- |
      | Create or generate a secret. | Choose from:- To create a strong, random alphanumeric string, click **Generate Secret**.

      - Manually enter a secret.                               |
      | Modify an existing secret.   | 1. Select the **Change Secret** check box.

      2. Click **Generate Secret** to create a strong random alphanumeric string or manually enter a secret. |

   5. In the **Grant Types** field, select the **Client Credentials** and **Access Token Validation (Client is a Resource Server)** options.

   6. In the **Default Access Token Manager** field, select **JSON Web Tokens** . Click **Save**.

   7. Access the PingFederate `<pf_install>/pingfederate/bin/run.properties` file, and ensure that this property is set: `pf.admin.api.authentication=OAuth2`.

   8. Access the PingFederate `<pf_install>/pingfederate/bin/oauth2.properties` file, and ensure that the following properties are set.

      | Property                  | Description                                                                                                                                                                                                                                                                |
      | ------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
      | `client.id`               | The unique client identifier defined in step 2.                                                                                                                                                                                                                            |
      | `client.secret`           | The client secret defined in step 4.                                                                                                                                                                                                                                       |
      | `introspection.endpoint`  | This URL specifies where PingFederate validates the authentication token.For example, `https://<PF_RUNTIME_HOST>:<PF_RUNTIME_PORT>/as/introspect.oauth2`                                                                                                                   |
      | `required.scopes`         | Use any of the scopes defined in PingFederate.Go to **System → OAuth Settings → Scope Management** to see a list of available scopes.For details, see [Scopes](https://docs.pingidentity.com/csh?Product=pf-latest\&context=pf_scopes) in the *PingFederate Server* guide. |
      | `username.attribute.name` | The value mapped to the **Username** attribute defined on the **Contract Fulfillment** tab.                                                                                                                                                                                |
      | `role.attribute.name`     | The value mapped to the **admin\_role** attribute defined on the **Contract Fulfillment** tab.                                                                                                                                                                             |

3. Configure PingCentral:

   1. In PingCentral, to connect to the new PingFederate client, go to **Environments → Add Environments**.

   2. On the **Connect to Instances** page, complete the following fields using the properties you just set in the PingFederate `oauth2.properties` file.

      ![In this example, the Connect to Instances page in PingCentral is displayed.](../_images/zrg1656367226738.jpg)

      * **PingFederate Admin**: Enter the URL defined in the `pf.admin.baseurl` property for the new client. For details, see [Configuring PingFederate properties](https://docs.pingidentity.com/csh?Product=pf-latest\&context=pf_config_pf_propert) in the *PingFederate Server* guide.

      * **Authentication Method**: Select **OAuth2**.

      * **Token Endpoint URL**: Enter the token endpoint URL, which is PingFederate: `https://<PF_RUNTIME_HOST>:<PF_RUNTIME_PORT>/as/token.oauth2`.

      * **Client ID**: Enter the unique client identifier set as the `client.id` property.

      * **Client Secret**: Enter the client secret set as the `client.secret` property.

      * **Scopes**: Enter the scopes set as the `required.scopes` property.

4. Click **Next**.

---

---
title: Creating and testing approval expressions
description: Instructions for creating and testing Spring Expression Language (SpEL) expressions, and provide OAuth and SAML SP approval examples.
component: pingcentral
version: 3.1.1
page_id: pingcentral:pingcentral_for_iam_administrators:pingcentral_approval_expressions/pingcentral_create_test_expressions
canonical_url: https://docs.pingidentity.com/pingcentral/3.1.1/pingcentral_for_iam_administrators/pingcentral_approval_expressions/pingcentral_create_test_expressions.html
revdate: October 7, 2025
section_ids:
  before-you-begin: Before you begin
  about-this-task: About this task
  steps: Steps
  oauth-approval-example: OAuth approval example
  saml-sp-approval-example: SAML SP approval example
---

# Creating and testing approval expressions

Configure a Spring Expression Language (SpEL) expression to manage promotion approval requirements for your environment.

## Before you begin

When you configure an environment on the **Connection** page, select **Require Approval If Any Expression Fails** or **Require Approval If Any Expression Succeeds** from the **Approval Expression** list. Learn more in [Managing environments](../pingcentral_mng_environments/pingcentral_mng_environments.html).

### About this task

You can manage promotion approval requirements for your PingCentral environment by creating custom approval expressions with Spring Expression Language (SpEL). These expressions will evaluate the application based on its JSON payload to determine whether an administrator will be required to approve promotions.

## Steps

1. On the **Connection** page, in the **Approval Expression** field, click **Test** to expand the **Test Spring Expression** window.

   The **Test Spring Expression** window displays.

2. In the **Application Configuration** field, enter the application configuration information as a JSON payload.

   If you have promotion configuration information, enter it as a JSON payload in the **Promotion Configuration** field.

3. In the **Spring Expression** field, use the following function to extract values from the JSON payload using a specified JSON path: `#jsonPath(\{JSON payload}, \{JSON path})`.

   Build your own expressions using the following variables:

   * *\#application*: Represents the type of application (OAuth, OIDC, SAML Service Provider (SP), or PingAccess) and its corresponding API model (**ClientApplicationView**, **ConnectionApplicationView**, or **PingAccessApplicationView**).

   * *\#oAuthApplicationPromotion*: Provides access to the **OAuthApplicationPromotionView** API model and promotion configuration information for OAuth and OIDC applications.

   * *\#samlSpApplicationPromotion*: Provides access to the **SamlApplicationPromotionView** API model and promotion configuration information for SAML SP applications.

   * *\#pingAccessApplicationPromotion*: Provides access to the **PingAccessApplicationPromotionView** API model and promotion configuration information for PingAccess applications.

   Learn more about building expressions in [Spring Expression Language (SpEL)](https://docs.spring.io/spring-framework/docs/3.0.x/reference/expressions.html) in the Spring Framework documentation.

4. Under the **Spring Expression** field, click **Test Expression** to test your expression.

   The **Spring Expression** result displays.

   For information about approval expression handling, see the following:

   * If you selected **Require Approval If Any Expression Fails** from the **Approval Type** list: If any expression results in `false` then approval is required. If all expressions are `true` then approval is not required.

   * If you selected **Require Approval If Any Expression Succeeds** from the **Approval Type** list: If any expression results in `true` then approval is required. If all expressions are `false` then approval is not required.

   * If any of the expressions do not return a Boolean value or if there are any errors in the expressions, the promotions will require approval.

   * Multiple expressions can be added and are evaluated sequentially from top to bottom in an IF/ELSE chain. You can change the order in which these expressions display in the list by dragging and dropping them into different locations within the list.

5. Click the **Update** button to save your configuration or click the **Cancel** button to discard it.

This section contains SpEL approval expression examples for OAuth and SAML applications.

## OAuth approval example

In this example, if the **Require Approval If Any Expression Succeeds** option is selected and the application is an OAuth application with the **Client Credentials** grant type, PingCentral requires that an administrator approve the promotion before the application owner can promote it to the target environment.

```
#jsonPath(#application, 'type').equals('OAuth')
&& #jsonPath(#application,
'grantTypes').contains('CLIENT_CREDENTIALS')
```

## SAML SP approval example

In this example, if the **Require Approval If Any Expression Succeeds** option is selected, the application is a SAML SP application, and one or more of the attribute mappings are OGNL expressions, PingCentral requires that an administrator approve the promotion before the application owner can promote it to the target environment.

```
#jsonPath(#application, 'type').equals('SAML_20_SP')
&& !#jsonPath(#application,
"attributeMappings[?(@.type == 'EXPRESSION')]").isEmpty()
```

---

---
title: Installing and configuring PingCentral
description: This page contains links to instructions for installing and configuring PingCentral.
component: pingcentral
version: 3.1.1
page_id: pingcentral:pingcentral_for_iam_administrators:pingcentral_installing_configuring/pingcentral_install_config
canonical_url: https://docs.pingidentity.com/pingcentral/3.1.1/pingcentral_for_iam_administrators/pingcentral_installing_configuring/pingcentral_install_config.html
revdate: October 9, 2025
section_ids:
  installing-pingcentral: Installing PingCentral
  configuring-pingcentral: Configuring PingCentral
---

# Installing and configuring PingCentral

Installation, upgrade, and configuration instructions are accessible from the links on this page.

## Installing PingCentral

* [Using Docker to deploy PingCentral](pingcentral_docker.html)

* [Installing PingCentral on Microsoft Windows](pingcentral_installing_pc_windows.html)

* [Installing PingCentral on Linux systems](pingcentral_installing_pc_linux.html)

* [PingCentral licensing](pingcentral_licensing.html)

* [Setting up MySQL](pingcentral_mysql.html)

* [Upgrading PingCentral](pingcentral_upgrading/pingcentral_upgrading_pc.html)

## Configuring PingCentral

* [Configuring PingCentral to run as a Windows service](pingcentral_conf_pc_windows.html)

* [Configuring PingCentral to run as a Linux systemv service](pingcentral_conf_pc_linux_systemv.html)

* [Configuring PingCentral to run as a Linux systemd service](pingcentral_conf_pc_linux_systemd.html)

* [Configuring PingCentral to run in FIPS-compliant mode](pingcentral_fips_mode.html)

* [Configuring logging](pingcentral_logging.html)

* [Configuring PingFederate and PingAccess for SSO](pingcentral_pf_pa_sso.html)

To avoid seeing a certificate warning when you access PingCentral, replace the user-facing SSL certificate so it will no longer use the self-signed certificate. Learn more about replacing it in [Replacing the Admin Console SSL Certificate](pingcentral_admin_ssl_cert.html).

The Spring Boot Actuator, enabled by default, collects a wide variety of information to help you monitor and manage PingCentral in production environments. Spring Metrics collects a large amount of data, but it does not present the data in ways that are easy to understand, so you might want to move this data to either a Prometheus or Graphite time series database and use Grafana to view it through interactive dashboards with charts and graphs. Learn more in [Monitoring PingCentral](../pingcentral_monitoring/pingcentral_monitoring_pc.html).

---

---
title: Installing PingCentral on Linux systems
description: Instructions for installing PingCentral on Linux systems.
component: pingcentral
version: 3.1.1
page_id: pingcentral:pingcentral_for_iam_administrators:pingcentral_installing_configuring/pingcentral_installing_pc_linux
canonical_url: https://docs.pingidentity.com/pingcentral/3.1.1/pingcentral_for_iam_administrators/pingcentral_installing_configuring/pingcentral_installing_pc_linux.html
revdate: April 10, 2025
section_ids:
  before-you-begin: Before you begin
  steps: Steps
  example: Example:
---

# Installing PingCentral on Linux systems

To install PingCentral, download the latest version of the software and follow the on-screen instructions.

## Before you begin

Ensure that:

* You are signed on to your system and have privileges that allow you to install applications. Run PingCentral as a non-root user.

* All [System requirements and supported configurations](../pingcentral_system_requirements/pingcentral_system_requirements.html) are met, and the Oracle or OpenJDK Java 11 LTS runtime environment is installed.

* The *\<JAVA\_HOME>* path points to the JDK software on your system. For example, `/usr/lib/jvm/java-11-openjdk-11.0.5.10-0.e17_7.x86_64`. To verify this information, run the `echo $JAVA_HOME` command.

* The JAVA`/bin` directory path is added to the *\<PATH>* variable. To verify this information, run the `echo $PATH` command.

## Steps

1. Download the latest version of PingCentral from the Ping Identity [website](https://www.pingidentity.com/en/resources/downloads/pingcentral.html).

2. Extract the file into the appropriate target installation directory.

3. Start PingCentral by running `/<pingcentral_install>/bin/run.sh`.

4. When the installation is complete, open a browser window and enter the machine and PingCentral admin port in the URL field.

   ### Example:

   https\://*\<yourhost>*:9022.

5. Sign on to the application using the following credentials:

   * **Username**: Administrator

   * **Password**: 2FederateM0re!

     |   |                                                                                                          |
     | - | -------------------------------------------------------------------------------------------------------- |
     |   | If you're running PingCentral in FIPS-compliant mode, your password must contain at least 14 characters. |

6. Configure PingCentral to run as a Linux systemv service or a Linux systemd service, as appropriate.

   Learn more in [Configuring PingCentral to run as a Linux systemv service](pingcentral_conf_pc_linux_systemv.html) or [Configuring PingCentral to run as a Linux systemd service](pingcentral_conf_pc_linux_systemd.html).

   Without modification, PingCentral is secure by default.

---

---
title: Installing PingCentral on Microsoft Windows
description: Instructions for installing PingCentral on Microsoft Windows.
component: pingcentral
version: 3.1.1
page_id: pingcentral:pingcentral_for_iam_administrators:pingcentral_installing_configuring/pingcentral_installing_pc_windows
canonical_url: https://docs.pingidentity.com/pingcentral/3.1.1/pingcentral_for_iam_administrators/pingcentral_installing_configuring/pingcentral_installing_pc_windows.html
revdate: April 10, 2025
section_ids:
  before-you-begin: Before you begin
  steps: Steps
---

# Installing PingCentral on Microsoft Windows

PingCentral can be installed on Microsoft Windows Server 2016 or 2019. An installation script is not yet available, so download and extract the contents of the installation file to a suitable location within the host file system.

## Before you begin

Ensure that:

* You are signed on to your system and have privileges that allow you to install applications.

* All [System requirements and supported configurations](../pingcentral_system_requirements/pingcentral_system_requirements.html) are met, and the Oracle Java 11 LTS runtime environment is installed.

* The *\<JAVA\_HOME>* path points to the JDK software on your system. Similar to `/usr/lib/jvm/[JAVA_VERSION]`. To verify this information, run the `echo $JAVA_HOME` command.

* The JAVA `/bin` directory path is added to the *\<PATH>* variable. To verify this information, run the `$echo $PATH` command.

## Steps

1. Download the distribution `.zip` archive and extract its contents where you want the service run.

2. Go to `/<pingcentral_install>/bin/run.bat` and run `run.bat` from a command-line interface.

3. Open a web browser and go to `https://localhost:9022`.

   |   |                                                                                                                                                 |
   | - | ----------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | While you are running PingCentral locally, your browser might warn you that the application you're accessing doesn't have a signed certificate. |

4. Sign on to PingCentral using the following credentials:

   * **Username**: Administrator

   * **Password**: 2FederateM0re!

     Without modification, PingCentral is secure by default.

     |   |                                                                                                          |
     | - | -------------------------------------------------------------------------------------------------------- |
     |   | If you're running PingCentral in FIPS-compliant mode, your password must contain at least 14 characters. |

   Items worth mentioning:

   * If you add PingAccess environments to PingCentral, ensure that PingFederate is configured as the PingAccess token provider. Learn more about this configuration in [Configuring PingFederate as a PingAccess token](../pingcentral_pf_as_pa_token/pingcentral_configuring_pf_token_provider.html).

   * If your application owners promote SAML applications to PingFederate or PingAccess environments, ensure that the appropriate trusted certificate authority (CA) certificates are available in PingCentral. You can find details in [Adding trusted CA certificates to PingCentral](../pingcentral_pf_as_pa_token/pingcentral_configuring_pf_token_provider.html#trusted_certs).

5. Configure PingCentral to run as a Windows service, if appropriate.

   Learn more in [Configuring PingCentral to run as a Windows service](pingcentral_conf_pc_windows.html).

---

---
title: Introduction to PingCentral
description: An introduction to PingCentral and a high-level explanation of how it works.
component: pingcentral
version: 3.1.1
page_id: pingcentral:pingcentral_for_iam_administrators:pingcentral_intro/pingcentral_intro
canonical_url: https://docs.pingidentity.com/pingcentral/3.1.1/pingcentral_for_iam_administrators/pingcentral_intro/pingcentral_intro.html
revdate: October 9, 2025
page_aliases: ["index.adoc"]
---

# Introduction to PingCentral

PingCentral allows you to delegate common application configuration and deployment tasks to application owners, streamlining processes and saving time.

PingCentral:

* Removes many tasks from your list of responsibilities, which lowers operational costs and reduces bottlenecks.

* Provides a central monitoring location for greater visibility into applications across deployment life cycles.

* Minimizes the risk of promoting applications with vulnerable security policies and makes it easier to standardize policies across the applications within your organization.

Using PingCentral does not require extensive training. However, for the best possible experience, review how the platform works before getting started.

* In PingCentral, you set up users and define PingFederate and PingAccess development, test, and production environments.

* In PingFederate and PingAccess, you locate clients, connections, and application security configurations worthy of replicating.

* In PingCentral, you create PingFederate OAuth *(tooltip: \<div class="paragraph">
  \<p>A standard framework that enables an application (OAuth client) to obtain access tokens from an OAuth authorization server for the purpose of retrieving protected resources on a resource server.\</p>
  \</div>)*, OpenID Connect (OIDC) *(tooltip: \<div class="paragraph">
  \<p>An authentication protocol built on top of OAuth that authenticates users and enables clients (relying parties) of all types to request and receive information about authenticated sessions and users. OIDC is extensible, allowing clients to use optional features such as encryption of identity data, discovery of OpenID Providers (OAuth authorization servers), and session management.\</p>
  \</div>)*, Security Assertion Markup Language (SAML) *(tooltip: \<div class="paragraph">
  \<p>A standard, XML-based, message-exchange framework enabling the secure transmittal of authentication tokens and other user attributes across domains.\</p>
  \</div>)*, and PingAccess application templates based on these clients, connections, and applications by using the template wizard, by saving them as templates, or by adding them directly to PingCentral.

  ![This flowchart illustrates the tasks IAM Administrators perform when using PingCentral.](../_images/yen1616785397887.png)

This flowchart shows the tasks that application owners perform when using PingCentral.

In PingCentral, application owners manage the applications assigned to them and use your templates to apply OAuth, OIDC, SAML SP, and PingAccess security configurations to them. A wizard guides them through the process of providing a name and description for each application they create as well as environment-specific information that makes it possible to run the application on the target environment.

![This flowchart illustrates the tasks application owners perform to add applications to and promote them to development, staging, or production environments.](../../_images/nuq1601349842175.jpg)

For a deeper understanding of how PingAccess applications work, see [Promoting applications](../../pingcentral_for_application_owners/pingcentral_promoting_apps/pingcentral_promoting_apps.html).

---

---
title: Managing applications
description: Instructions for managing PingCentral applications.
component: pingcentral
version: 3.1.1
page_id: pingcentral:pingcentral_for_iam_administrators:pingcentral_mng_applications/pingcentral_manage_apps
canonical_url: https://docs.pingidentity.com/pingcentral/3.1.1/pingcentral_for_iam_administrators/pingcentral_mng_applications/pingcentral_manage_apps.html
revdate: October 7, 2025
section_ids:
  _filtering_applications: Filtering applications
  steps: Steps
  adding-applications: Adding applications
  steps-2: Steps
  pingcentral_iam_updating_apps: Updating applications
  about-this-task: About this task
  steps-3: Steps
  result: Result:
  deleting-applications: Deleting applications
  about-this-task-2: About this task
  steps-4: Steps
  result-2: Result:
  choose-from: Choose from:
---

# Managing applications

All PingCentral applications and applications in verified PingAccess and PingFederate environments display on the **Applications** page, where you can filter the list of applications, add new applications, update existing applications, and delete them from PingCentral when they are no longer needed.

|   |                                                                                                                                                                                                                          |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | If an environment is offline or if a PingCentral administrator has set the environment status to **Disabled**, application owners will be unable to update or delete applications for a disabled or offline environment. |

## Filtering applications

Use the filters at the top of the page to filter your list of applications, or use the search feature to locate specific applications.

### Steps

1. Select your filters. You can filter by:

   * Environment

   * Application owner, or groups of application owners

   * Integration type (OAuth and OIDC or SAML)

   * Templates

   * Outdated templates

   * Type. Applications can be managed (applications created from or promoted to PingCentral environments), unmanaged (applications that reside in verified PingAccess or PingFederate environments), or you can select **All** to view all applications at once. Managed applications initially display by default.

     ![A screen capture of the Applications page that displays several of the filters available to filter the application list.](../_images/lay1718893967737.jpg)

2. Click the filters to remove them.

3. If you know the name of an application, further refine your search by entering the first few letters of application's name.

## Adding applications

There are a variety of ways you can add applications to PingCentral. You can apply templates to them, you can create templates from them, or you can add them directly to PingCentral.

### Steps

1. To apply an OAuth, OIDC, SAML, or PingAccess template to an application:

   1. Click **Add Application**.

   2. On the **Select Template** page, select the appropriate template and follow the wizard prompts.

      Learn more about templates in [Selecting a template](../../pingcentral_for_application_owners/pingentral_adding_apps/pingcentral_adding_apps.html#select_template) in PingCentral for Application Owners.

2. To create a template from an unmanaged application:

   1. Select the expandable icon associated with the application.

   2. Click **Add as Template** and follow the wizard prompts.

      The template displays in the list of available templates.

3. To add a PingFederate or PingAccess application directly to PingCentral:

   1. Use the search and filtering features to locate applications.

      Learn more in [Filtering applications](#_filtering_applications).

   2. Select the expandable icon associated with the application.

   3. Click **Add to PingCentral** as shown in the following example, name the application, assign owners, and save it.

      ![This example shows a selected application that displays the Add to PingCentral button.](../_images/gab1576189835931.png)

## Updating applications

Update your applications at any time.

### About this task

To keep your applications secure, rotate certificates and client secrets on a regular basis and apply updated security configurations to applications built from templates when new configuration templates become available.

You don't need to recreate your applications in PingCentral to apply new templates. Replace the templates associated with your applications and promote them again.

### Steps

1. On the **Applications** page, click the **Expand** icon associated with the application you want to update.

2. **Optional:** On the **Connection** tab, if you modified the application configuration externally, click the **Sync** button to initiate an application synchronization.

   |   |                                                                                                            |
   | - | ---------------------------------------------------------------------------------------------------------- |
   |   | Depending on your application type, the **Connection** tab might be labeled **Client** or **Application**. |

   |   |                                                                                                                                                                          |
   | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
   |   | If you created the application from a template, it cannot be synchronized with PingCentral. Only applications added directly to PingCentral can undergo synchronization. |

   #### Result:

   PingCentral retrieves the latest JSON data from the original environment and updates the application.

   |   |                                                                            |
   | - | -------------------------------------------------------------------------- |
   |   | Syncing an application cancels all pending approvals for that application. |

3. Click the **Pencil** icon.

   All the editable information is on one page.

   | Option                                              | Steps                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
   | --------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   | Update the name, description, or owner information. | To update the application name, description, and owner, change the information in the **Name**, **Description**, or **Owners** fields.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
   | Update or change the template.                      | If an application is based on an outdated template, an **Outdated Template** icon displays next to it. To update the application to the latest version of the template, click the **Pencil** icon, click **Update Template**. Configurations in the new template will override those specified in the previous template.To update or change the template used to create the application, click the **Pencil** icon, click **Change Template**, and select a new template from the **Select Template** page.&#xA;&#xA;You cannot apply different template types to applications. For example, you cannot apply SAML template to an OAuth or OIDC application or apply an OAuth or OIDC template to a PingAccess application.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
   | Update OAuth or OIDC application information.       | To update the application:- In the **Client** section, change the scopes associated with OAuth or OIDC applications. Select or clear the appropriate checkboxes.&#xA;&#xA;You cannot edit scopes for applications created in PingCentral 1.2.0. However, you can change the template associated with an application to a template created in a later version, which allows you to update scope information.- In the **Promote** section, change the information in the **Redirect URI** fields for the appropriate environments.

   - To change client secrets, return to the **Applications** page, promote the application again, and generate a new secret.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
   | Update SAML SP application information.             | To update the application:- In the **Attribute Mappings** section, add or remove attributes and expressions or update attribute and expression values.

   - If attribute sources are defined in the underlying connection, select the **- Data Store -** identity attribute option and the applicable data store values.

   - In the **Promotions** section, upload a new `.xml` file that contains service provider (SP) metadata, such as the entity ID, ACS URL, certificates, and attribute information, from another SAML application. Click **Choose File** or **Or Use URL** to provide the metadata file.&#xA;&#xA;If you're providing a new metadata file, you might also need to update the attribute mapping section to include new attributes from the metadata file.- Change the information in the **Entity ID** or **ACS URL** fields.

   - To change the signing certificate, select the appropriate certificate in the **Signing Certificate** list.

   - To change the SP certificate, click **SP Certificate** to upload a new certificate, or click **Remove** to remove it.

     &#xA;&#xA;If a certificate is added to a SAML application and a SAML metadata file is subsequently provided that contains a certificate, additional changes to the application cannot be saved. If this occurs, exit the edit page and reopen it.Update the signature policy by selecting the appropriate option. Refer to step 8 in [Adding SAML application templates](../pingcentral_mng_templates/pingcentral_mng_templates.html#_adding_saml_application_templates) |
   | Update PingAccess application information.          | To update the application:- On the **Properties** tab, in the **Promote** section, update the **Virtual Hosts**, **Access Validation**, **Identity Mapping**, and **Site** or **Agent** names, as appropriate.

   - On the **Resources** tab, update information regarding each resource.

   - On the **Policy** tab, click the **Pencil** icon associated with the policy you want to update.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |

4. Click **Save**.

## Deleting applications

### About this task

You can delete applications within PingCentral, or choose to delete the application from all environments.

### Steps

1. To delete an application, click the associated **Delete** icon.

   #### Result:

   A message displays asking you if you want to delete the application from PingCentral only or from all environments.

2. Select which environments to delete the application from.

   #### Choose from:

   * To delete an application from PingCentral only, click the **Delete** button.

   * To delete an application from all environments, depending on the application type, select the **Delete from PingFederate in all environments** or **Delete from PingAccess in all environments** check box and click the **Delete** button.

---

---
title: Managing approvals (administrators)
description: Instructions for managing application approvals.
component: pingcentral
version: 3.1.1
page_id: pingcentral:pingcentral_for_iam_administrators:pingcentral_mng_approvals/pingcentral_manage_approvals
canonical_url: https://docs.pingidentity.com/pingcentral/3.1.1/pingcentral_for_iam_administrators/pingcentral_mng_approvals/pingcentral_manage_approvals.html
revdate: October 9, 2025
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Managing approvals (administrators)

When an application owner submits an application for promotion approval, administrators can view the application and its approval status on the **Promotion Approvals** page, located under the **Management** tab.

### About this task

From this page, you can:

* Filter for approved, promoted, pending, rejected, or canceled approvals, or by environments or integration type. Use the **Visible** filter, which is enabled by default, to hide approvals that are in a canceled, promoted, or rejected status.

* **Approve**, **Approve and Promote**, or **Reject** an approval.

|   |                                                                                         |
| - | --------------------------------------------------------------------------------------- |
|   | You see a bell icon in the top navigation bar when there are pending approval requests. |

![Screen capture of console for IAM administrators that displays the Promotion Approvals page with active approval requests. Status is filtering for Approved and Pending approval requests.](../_images/tvm1687890488058.jpg)

### Steps

1. Select your filters.

   You can filter by:

   * **Status**: **Approved** or **Pending**. The page automatically filters for any approved and pending approvals.

   * Environments.

   * Integration types (OAuth and OIDC or SAML).

   * Requested (the user that made the request).

   Click the filters to add or remove them.

2. To approve promotion requests from application owners, click **Approve** in the row for the promotion request that you want to approve.

   |   |                                                                                                                                                                                                                                          |
   | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | If the **Allow JSON editing for application promotions** is enabled for the targeted environment and the promotion request requires approval, you'll be able to compare the submitted application JSON to the original application JSON. |

   **Optional:** To approve the request and promote the application to an environment, after you click **Approve**, select the **Promote Application to Environment** check box in the dialog that opens, and click **Approve** to approve the request and promote the application.

   Learn more in [Promotion processes](../pingcentral_promotion_processes/pingcentral_promotion_processes.html).

   |   |                                                                                                                                                                                                                                                                                     |
   | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | If an environment is offline or if a PingCentral administrator has set the environment status to **Disabled**, you will see a note indicating that the environment is inaccessible, and you will be unable to promote the application while the environment is disabled or offline. |

3. To reject an approval request, click **Reject** in the row for the request that you want to decline.

   **Optional:** Supply a rejection explanation in the dialogue box that displays.

---

---
title: Managing environments
description: Instructions for adding,updating, and deleting environments.
component: pingcentral
version: 3.1.1
page_id: pingcentral:pingcentral_for_iam_administrators:pingcentral_mng_environments/pingcentral_mng_environments
canonical_url: https://docs.pingidentity.com/pingcentral/3.1.1/pingcentral_for_iam_administrators/pingcentral_mng_environments/pingcentral_mng_environments.html
revdate: October 7, 2025
section_ids:
  adding-environments: Adding environments
  before-you-begin: Before you begin
  steps: Steps
  choose-from: Choose from:
  choose-from-2: Choose from:
  result: Result:
  updating-environments: Updating environments
  steps-2: Steps
  choose-from-3: Choose from:
  deleting-environments: Deleting environments
  steps-3: Steps
  result-2: Result:
  result-3: Result:
---

# Managing environments

All environments managed within PingCentral, as well as connected PingFederate and PingAccess environments, display on the **Environments** page, where you can view and update information about each environment and delete them from PingCentral when they are no longer needed.

Items worth mentioning:

* If you add PingAccess environments to PingCentral, ensure that PingFederate is configured as the PingAccess token provider. Learn more about this configuration in [Configuring PingFederate as a PingAccess token provider](../pingcentral_pf_as_pa_token/pingcentral_configuring_pf_token_provider.html).

* To enforce random secret generation and restrict non-administrators from creating their own, select the **Generate Client Secret on Promotion** checkbox when managing your environments. PingCentral will generate random client secrets.

* If your application owners promote Security Assertion Markup Language (SAML) *(tooltip: \<div class="paragraph">
  \<p>A standard, XML-based, message-exchange framework enabling the secure transmittal of authentication tokens and other user attributes across domains.\</p>
  \</div>)* applications to PingFederate or PingAccess environments, ensure that the appropriate trusted certificate authority (CA) *(tooltip: \<div class="paragraph">
  \<p>An entity that issues digital certificates.\</p>
  \</div>)* certificates are available in PingCentral. Learn more about these certificates in [Adding trusted CA certificates to PingCentral](../pingcentral_pf_as_pa_token/pingcentral_configuring_pf_token_provider.html#trusted_certs).

* Starting with version 1.14, PingCentral performs regular health checks on its environments. These checks involve calling either the heartbeat endpoint or the admin API version endpoint, depending on the version of PingFederate being used.

  To configure this process, modify the `orchestrator.heartbeat.polling-interval-ms` and `orchestrator.heartbeat.offset-ms` parameters in the `conf/application.properties` file. These settings determine both the frequency of polling and the initial delay before the health check begins.

* Starting with PingCentral 1.8, trusted CA certificates are stored in the PingCentral database instead of an external trust store. Certificates that exist in this trust store in previous versions are imported to the PingCentral database during the upgrade process.

## Adding environments

Use the wizard to add PingFederate and PingAccess environments to PingCentral.

### Before you begin

Ensure that PingFederate is configured as a token provider for PingAccess. Learn how to configure PingFederate [Configuring PingFederate as a PingAccess token provider](../pingcentral_pf_as_pa_token/pingcentral_configuring_pf_token_provider.html).

### Steps

1. On the **Environments** page, click **Add Environment**.

2. On the **Connect to Instances** page, connect to a PingFederate or PingAccess environment:

   #### Choose from:

   * **Native**: Complete the **Username** and **Password** fields for your PingFederate or PingAccess environments.

   * **OAuth2**: Complete the **Token Endpoint URL**, **Client ID**, **Client Secret**, and **Scopes** fields.

   * **Client Certificate**: Select the certificate you want to use for mTLS. See [Configuring MTLS](../pingcentral_installing_configuring/pingcentral_config_mtls.html) for details on uploading these certificates.

     |   |                                                                                                     |
     | - | --------------------------------------------------------------------------------------------------- |
     |   | If an environment is disabled or offline, you will be unable to add the environment to PingCentral. |

     If this is the first time that you have set up this environment, and the initial validation fails, you see a **Skip Verification** option. If you select this option, it allows you to skip the validation process. However, if you set it up correctly, you won't see this option.

   If the environment is disabled or offline, and you edit the connection configuration, the **Skip Verification** check box is automatically marked.

3. Click **Next**.

4. On the **Name Environment** page, complete the **Name**, **Short Code**, and **Description** fields.

5. **Optional:** To configure whether non-administrators need approval for promoting an application to an environment, select an option from the **Approval Type** list:

   #### Choose from:

   * Select **No Approval** to allow non-administrators to promote applications to the environment freely.

   * Select **Approval Required** to indicate that application promotion requires approval.

   * Select **Require Approval If Any Expression Fails** and proceed to the next step to configure an **Approval Expression**.

   * Select **Require Approval If Any Expression Succeeds** and proceed to the next step to configure an **Approval Expression**.

6. **Optional:** If you selected **Require Approval If Any Expression Fails** or **Require Approval If Any Expression Succeeds**, you must configure a Spring Expression Language (SpEL) expression in the **Approval Expression** field.

   You can use SpEL expressions to determine whether an application requires approval or not. Learn more about these expressions in [Creating and testing approval expressions](../pingcentral_approval_expressions/pingcentral_create_test_expressions.html).

   |   |                                                                                                                                                                                             |
   | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | For more information on SpEL, see [Spring Expression Language (SpEL)](https://docs.spring.io/spring-framework/docs/3.0.x/reference/expressions.html) in the Spring Framework documentation. |

7. **Optional:** If you want application owners to be able to edit the underlying application JSON when they promote their OAuth and SAML applications, select **Allow JSON editing for application promotions**.

   |   |                                                                                                                                                                                                                                                                                   |
   | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | Providing application owners with this ability can be risky, so it's highly recommended that you require promotion requests to be approved. That way, you'll be able to compare the submitted application JSON to the original application JSON before you approve the promotion. |

8. **Optional:** To enforce random secret generation and restrict non-administrators from creating their own, select the **Enforce Random Client Secrets** check box.

   PingCentral will generate random client secrets.

9. **Optional:** Select the **Allow only administrators to delete applications from PingFederate** (and PingAccess, when applicable), option to restrict application owners from deleting applications from environments.

10. **Optional:** To add an identity provider (IdP) *(tooltip: \<div class="paragraph">
    \<p>A service that manages identity information and provides authentication services to relying clients or SPs within a federated or distributed network.\</p>
    \</div>)* certificate, select the appropriate certificate in the **Signing Certificate** list or to upload your own certificate, click **Choose** and enter the certificate password in the appropriate field. Click **Save and Close**.

    #### Result:

    The environment is displayed on the **Environments** page. If you chose to protect the environment, you see a shield icon next to its name. Depending on the type of environment, you also see a **PF** or **PA** icon. The color of this icon represents the status of the environment. A green icon indicates that the environment is verified while a red icon indicates that the environment isn't verified.

    Depending on if an environment is online, offline, or disabled, you see the environment status in a display bar. You also see the toggle switch that you can click to disable the environment and indicate that it is undergoing maintenance.

11. Click **Save and Continue**.

12. Click the expandable icon associated with the environment to view environment details.

    ![A screen capture showing the Environments page, which lists all of the environments and displays details regarding each environment when the associated expandable icon is clicked.](../_images/val1695410125951.png)

    Environment details include:

    * A link to PingFederate.

    * A link to PingAccess.

    * A description of the environment.

    * The total number of applications hosted in this environment and a breakdown of or clients, connections, and applications. Click these links to access filtered lists of these applications on the **Applications** page.

      |   |                                                                                                                |
      | - | -------------------------------------------------------------------------------------------------------------- |
      |   | If an environment is unavailable, applications in that environment don't display on the **Applications** page. |

## Updating environments

Update PingFederate and PingAccess environment information at any time.

### Steps

1. To manage the environment maintenance status, see the following choices:

   #### Choose from:

   * To indicate that an environment is down for maintenance, toggle the switch on the applicable environment status bar from left (green) to right (gray). This action signals to application owners that the environment is undergoing maintenance and is now **Disabled**. This prevents PingCentral from connecting to the environment, avoiding UI errors.

   * To revert maintenance status, toggle the switch on the applicable environment status bar from right (gray) to left (green). This action removes the maintenance **Disabled** status, allowing application owners to resume interactions with the environment. This is the default status.

     |   |                                                                                                                                                                                       |
     | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
     |   | If an environment is offline or **Disabled**, the environment information displays a gray **OFFLINE** status bar. If an environment status is unknown, the status bar is unavailable. |

2. To edit environment information, click the expandable icon associated with it, and then click the **Pencil** icon.

   All the editable information displays on one page.

   | Option                                                           | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
   | ---------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   | Update the name and description                                  | To update the name and description, change the information in the **Name**, **Short Code**, and **Description** fields.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
   | Update the assertion encryption certificate                      | To update the assertion encryption certificate, click **Choose** to upload a new certificate and enter the certificate password in the appropriate field.                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
   | Update connection information                                    | To update the connection, ensure that the authentication method you want to use is selected:- **Native**: Update the **Username** and **Password** fields for your PingFederate or PingAccess environments.

   - **OAuth2**: Update the information in the **Token Endpoint URL**, **Client ID**, **Client Secret**, and **Scopes** fields.

   - **Client Certificate**: Update the certificate used for mTLS.

     &#xA;&#xA;If a PingAccess environment is added to PingCentral and removed through the edit page, the connection information is saved and restored if the PingAccess environment is selected again.                   |
   | Configure promotion approval requirements                        | To configure if non-administrators need approval for promoting an application to an environment, select an option from the **Approval Type**.Choose from:- Select **No Approval** to allow non-administrators to promote applications to the environment freely.

   - Select **Approval Required** to indicate that application promotion requires approval.

   - Select **Require Approval If Any Expression Fails** or **Require Approval If Any Expression Succeeds**. Learn more about these options in [Creating and testing approval expressions](../pingcentral_approval_expressions/pingcentral_create_test_expressions.html). |
   | Update the JSON editing option                                   | If you want application owners to be able to edit the underlying application JSON when they promote their OAuth and SAML applications, select **Allow JSON editing for application promotions**.	Providing application owners with this ability can be risky, so it's highly recommended that you require promotion requests to be approved. That way, you'll be able to compare the submitted application JSON to the original application JSON before you approve the promotion.                                                                                                                                                 |
   | Add or remove the enforcement of random client secret generation | To enforce random secret generation and restrict non-administrators from creating their own, select the **Enforce Random Client Secrets** check box. PingCentral will generate random client secrets. To allow non-administrators to generate their own secret, clear the checkbox.                                                                                                                                                                                                                                                                                                                                                |
   | Configure application owner deletion access                      | To restrict application owners from deleting applications from environments, select the **Allow only administrators to delete applications from PingFederate** (and PingAccess, when applicable), option.                                                                                                                                                                                                                                                                                                                                                                                                                          |
   | Update the signing certificate                                   | To update the signing certificate used to promote SAML applications, select the appropriate certificate in the **Signing Certificate** list or upload your own.                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
   | Update the SP certificate                                        | To update the service provider (SP) *(tooltip: \<div class="paragraph">&#xA;\<p>In SAML, an entity that receives and accepts an authentication assertion issued by an IdP, typically for the purpose of allowing access to a protected resource.\</p>&#xA;\</div>)* certificate, click **Choose** to upload a new certificate and enter the certificate password in the appropriate field.                                                                                                                                                                                                                                         |
   | Update the assertion encryption certificate                      | To update the assertion encryption certificate, click **Choose** to upload a new certificate and enter the certificate password in the appropriate field.                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |

3. Click **Save**.

## Deleting environments

Delete environments from PingCentral when they are no longer needed.

### Steps

1. Click the expandable icon associated with the environment to view environment details.

2. To delete the environment from PingCentral, click its associated **Delete** icon.

   #### Result:

   A message displays asking you if you want to delete the environment.

3. Click **Delete**.

   #### Result:

   A message displays saying that the environment was deleted.

   |   |                                                                                                                                                |
   | - | ---------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | When an environment is deleted, applications that were promoted to that environment retain the promotion details from the deleted environment. |

---

---
title: Managing templates
description: Instructions for managing OAuth, OIDC, and SAML application templates.
component: pingcentral
version: 3.1.1
page_id: pingcentral:pingcentral_for_iam_administrators:pingcentral_mng_templates/pingcentral_mng_templates
canonical_url: https://docs.pingidentity.com/pingcentral/3.1.1/pingcentral_for_iam_administrators/pingcentral_mng_templates/pingcentral_mng_templates.html
revdate: October 7, 2025
section_ids:
  oauth-and-oidc-templates: OAuth and OIDC templates
  adding-oauth-and-oidc-templates: Adding OAuth and OIDC templates
  steps: Steps
  updating-oauth-and-oidc-templates: Updating OAuth and OIDC templates
  steps-2: Steps
  reverting-templates-to-previous-versions: Reverting templates to previous versions
  steps-3: Steps
  deleting-templates: Deleting templates
  steps-4: Steps
  result: Result:
  saml-2-0-and-pingaccess-templates: SAML 2.0 and PingAccess templates
  _adding_saml_application_templates: Adding SAML application templates
  steps-5: Steps
  updating-saml-and-pingaccess-templates: Updating SAML and PingAccess templates
  steps-6: Steps
  reverting-templates-to-previous-versions-2: Reverting templates to previous versions
  steps-7: Steps
  deleting-templates-2: Deleting templates
  steps-8: Steps
  result-2: Result:
---

# Managing templates

Templates created in PingCentral are snapshots of the configurations for existing OAuth, OIDC, SAML, and PingAccess applications. If changes are made to those applications, the configurations on which the templates are based become outdated.

Add, update, and delete templates to meet your needs, or revert them to previous versions, as necessary.

You can create PingCentral templates from existing PingFederate or PingAccess applications or build your own.

## OAuth and OIDC templates

Add, update, or delete OAuth and OpenID Connect (OIDC) templates to meet your needs, or revert them to previous versions, as necessary.

To add an OAuth or OIDC template, select a client configuration to replicate. PingCentral retrieves this configuration and saves it as a template, which serves as a building block for future applications.

### Adding OAuth and OIDC templates

#### Steps

1. All templates are listed on the **Templates** page. To add a new template, click **Add Template**.

2. On the **Integration Type** page, select either an OAuth or OpenID Connect template. Click **Next**.

3. On the **Select OAuth Client** or **OIDC Client** page, select the PingFederate environment that hosts the client application you want to use as a template, and then select the application itself from the **Client** list.

   |   |                                                                                                                                                                                           |
   | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | If an environment is offline or if a PingCentral administrator has set the environment status to **Disabled**, you will be unable to select a disabled environment for template creation. |

   You see details regarding the selected client.

   ![This example shows the information that displays when an OAuth client is selected.](../_images/xkr1585249537055.png)

4. To see the JSON for the application, click **Review Configuration**.

5. On the **Name Template** page, add a name and description for your template.

   This information will help application owners select the appropriate template.

6. Select an icon to represent your template.

   The icon you choose is shown with the template name and description.

7. Click **Save and Close**.

   You see the new template in the list of available application templates. Application owners will see the new template on the **Select Template** page.

   ![This example shows the Select Template screen, which lists the templates available for application owners to use.](../../_images/jwq1600185986194.jpg)

   For OAuth or OIDC application templates, the following items are saved:

   * The client application

   * The ATM, if one exists

   * The parent ATM, if one exists

   * The OIDC policy, if one exists

   * Grant types

   * Definitions of exclusive scopes referenced by the client

### Updating OAuth and OIDC templates

#### Steps

1. To update an OAuth or OIDC template, click the **Expand** icon associated with the template.

2. If the template is based on an outdated configuration, you can click the **Sync** button to sync the template with the latest configuration available.

   |   |                                                                                                                                                                                                                                       |
   | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | When you upgrade to PingCentral 2.0, OAuth and OIDC templates created prior to version 2.0 cannot be synced with the most recent configuration available. Recreate the template in version 2.0 to use the sync feature going forward. |

3. Click the **Pencil** icon to make additional changes.

   All the editable information is on one page.

   | Option                                    | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
   | ----------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   | To update the name, description, or icon: | Update the information in the **Name** and **Description** fields or select a new icon to represent the template.                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
   | To update grant types:                    | To update the grant types used for authorization, select or deselect the grant types that you want to use for this template.Learn more about [Grant types](https://docs.pingidentity.com/pingfederate/latest/introduction_to_pingfederate/pf_grant_types.html) in the PingFederate documentation.&#xA;&#xA;Some grant types might not be available with your version of PingFederate.                                                                                                                                                                                                 |
   | To update scopes:                         | To add or update scopes, search for them and select or deselect the scopes that you want to use for this template.Learn more about [Scopes](https://docs.pingidentity.com/pingfederate/latest/introduction_to_pingfederate/pf_scopes.html) in the PingFederate documentation.                                                                                                                                                                                                                                                                                                         |
   | To update extended properties:            | Add or remove the extended property values that you want to use for this template. If you don't want applications owners to update extended property values in their applications, select the **Read-only** checkbox.Learn more about [Extended properties](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_extended_properti.html) in the PingFederate documentation.                                                                                                                                                                            |
   | To update policy contracts:               | Add, delete, or update the current attribute mappings in the PingFederate policy contract associated with this template.Learn more about [Attribute contracts](https://docs.pingidentity.com/pingfederate/latest/introduction_to_pingfederate/pf_attr_contract.html) in the PingFederate documentation.&#xA;&#xA;If you update a policy contract, a new contract is created in PingFederate, and you will be prompted to name it.&#xA;&#xA;	If a template is associated with an environment that is deleted, you will not be able to update OIDC policy information for the template. |

4. Click **Save**.

   If you update the grant types, scopes, or policy contract information, the **Save Template** window displays and reminds you that you are creating a new version of this template. Applications created from the previous template will not change until you update the application to the latest template version. Briefly describe the updates you made to the template in the **Comments** field for tracking purposes and click **Save**.

### Reverting templates to previous versions

The history of each template is available to review and compare with previous versions. You can see which administrator modified the template configuration or policy contract, when it was modified, and details regarding these modifications. You can revert templates to previous versions if necessary.

#### Steps

1. To review the template history, click the **Expand** icon associated with the template, and then click the **History** tab.

2. Click the **Details** link associated with each template version to see its configuration.

3. Click the **Diff with Current Version** toggle to see the differences between this version and the most recent version.

4. To restore this version as the current version, click **Restore This Version**.

   A new version of the template is created that matches the configuration of the version that you want to restore.

   |   |                                                                                                                                                                                                                                                                                                                                                                                 |
   | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | The template revision numbers increment on a system-wide level, not on a per-template basis. So the first time any template in PingCentral is changed, it will have a revision of 1. A change made to a completely different template results in a revision of 6, and so forth. Reverting a template generates another revision, which again increments on a system-wide basis. |

### Deleting templates

#### Steps

1. Click the expandable icon associated with the template to view template details.

2. To delete the template from PingCentral, click its associated **Delete** icon.

   |   |                                                                          |
   | - | ------------------------------------------------------------------------ |
   |   | You cannot delete templates that are still associated with applications. |

   ##### Result:

   A message opens, asking you if you want to delete the template.

3. Click **Delete**.

   A message opens, saying that the template was deleted.

## SAML 2.0 and PingAccess templates

Add, update, or delete SAML and PingAccess templates to meet your needs, or revert them to previous versions, as necessary.

To add a SAML or PingAccess template, select a configuration to replicate. PingCentral retrieves this configuration and saves it as a template, which serves as a building block for future applications.

### Adding SAML application templates

#### Steps

1. All templates are listed on the **Templates** page. To add a new template, click **Add Template**.

2. On the **Integration Type** page, select **SAML**. Click **Next**.

3. On the **Select SAML Connection** page, select the PingFederate environment that hosts the connection you want to use as a template, and then select the connection from the **Connection** list.

   |   |                                                                                                                                                                                           |
   | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | If an environment is offline or if a PingCentral administrator has set the environment status to **Disabled**, you will be unable to select a disabled environment for template creation. |

   Details regarding the connection display.

   ![This example shows the information that displays when a SAML connection is selected.](../_images/ius1569688182345.png)

4. To see the JSON for the SAML connection, click **Review Configuration**.

5. On the **Name Template** page, add a name and description for your template.

   This information will help application owners select the appropriate template.

6. Select an icon to represent your template.

   The icon you choose is shown with the template name and description.

7. **Optional:** If multiple authentication policy contracts exist in the underlying connection, choose the desired contract from the **Authentication Policy Contracts** list.

8. **Optional:** Specify how you want the signature policy configured.

   Note that signature policy configurations are only visible if the corresponding profiles and artifact binding are enabled in the underlying PingFederate SP connection.

   * **Require AuthN requests to be signed when received via the POST or Redirect bindings**: Ensures that authentication messages are signed when received through an HTTP POST binding, or an HTTP Redirect binding. Redirect bindings are often used for smaller messages, while the POST bindings are used for larger SAML assertions.

   * **Always Sign Assertion**: Ensures that the assertion element of a SAML response is digitally signed by the Identity Provider (IdP).

   * **Sign Response As Required**: Ensures that the entire SAML authentication response is digitally signed, rather than just a portion of it. This option is selected by default, and is automatically selected if the **Always Sign Assertion** option is not selected.

   * **Always Sign Artifact Response**: Ensures that all applications, containers, and configurations are also digitally signed by the IdP.

9. Click **Save and Close**.

   You see the new template in the list of available application templates. Application owners see the new template on the **Select Template** page.

   ![This example shows the Select Template screen, which lists the templates available for application owners to use.](../../_images/jwq1600185986194.jpg)

   For SAML SP connection templates, the following items are saved:

   * Connection information.

   * Attribute names and, if applicable, attribute sources defined in the associated authentication policy contract.

### Updating SAML and PingAccess templates

Applications based on outdated templates have **Outdated Template** icons associated with them, which inform application owners of changes.

#### Steps

1. To update a SAML or PingAccess template, click the **Expand** icon associated with the template.

2. If the template is based on an outdated configuration, you can click the **Sync** button to sync the template with the latest configuration available.

3. Click the **Pencil** icon.

   All the editable information is on one page.

4. Update the information in the **Name** and **Description** fields or select a new icon to represent the template.

5. Add or remove the extended property values that you want to use for this template. If you don't want application owners to be able to modify the extended property values in their applications, select the **Read-only** checkbox.

   Learn more about these properties in [Extended properties](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_extended_properties.adoc) in the PingFederate documentation.

6. Click **Save**.

### Reverting templates to previous versions

The history of each template is available to review and compare with previous versions. You can see which administrator modified the template configuration or policy contract, when it was modified, and details regarding these modifications. You can revert templates to previous versions if necessary.

#### Steps

1. To review the template history, click the **Expand** icon associated with the template, and then click the **History** tab.

2. Click the **Details** link associated with each template version to see its configuration.

3. To restore this version as the current version, click **Restore This Version**.

   A new version of the template is created that matches the configuration of the version that you want to restore.

   |   |                                                                                                                                                                                                                                                                                                                                                                                 |
   | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | The template revision numbers increment on a system-wide level, not on a per-template basis. So the first time any template in PingCentral is changed, it will have a revision of 1. A change made to a completely different template results in a revision of 6, and so forth. Reverting a template generates another revision, which again increments on a system-wide basis. |

### Deleting templates

#### Steps

1. Click the expandable icon associated with the template to view template details.

2. To delete the template from PingCentral, click its associated **Delete** icon.

   |   |                                                                          |
   | - | ------------------------------------------------------------------------ |
   |   | You cannot delete templates that are still associated with applications. |

   ##### Result:

   A message opens, asking you if you want to delete the template.

3. Click **Delete**.

   A message opens, saying that the template was deleted.

---

---
title: Managing user groups
description: This section explains how to add, update, and delete user groups.
component: pingcentral
version: 3.1.1
page_id: pingcentral:pingcentral_for_iam_administrators:pingcentral_mng_user_groups/pingcentral_managing_groups
canonical_url: https://docs.pingidentity.com/pingcentral/3.1.1/pingcentral_for_iam_administrators/pingcentral_mng_user_groups/pingcentral_managing_groups.html
revdate: October 13, 2025
section_ids:
  adding-user-groups: Adding user groups
  steps: Steps
  result: Result:
  result-2: Result:
  updating-user-groups: Updating user groups
  steps-2: Steps
  result-3: Result:
  deleting-user-groups: Deleting user groups
  steps-3: Steps
  result-4: Result:
---

# Managing user groups

Adding individual users to PingCentral applications can be a time-consuming process. If you have user groups defined in your data store, you can add the groups to PingCentral so that application owners can associate them with PingCentral applications and provide application access to multiple users at once.

Start by signing on PingCentral using single sign-on (SSO). Next, add information about each group, such as the group name, display name, and description to PingCentral. Group names should match the group names in your datastore and aren't case-sensitive.

If you have a large number of groups to add, you can upload the information into PingCentral in a `.csv` file. Then, you can add these groups of users to PingCentral applications, which provides application access to each user in the group.

Identities, user groups, and group membership information are managed in your datastore. When a user signs on to PingCentral, the groups to which the user belongs are sent as part of the groups claim. PingCentral not only updates its existing group information with information from the datastore, but if the claim contains new groups, it adds those groups to PingCentral, as shown in this diagram. It also updates the user profile to reflect current group memberships.

![This flowchart illustrates the way group information is updated when users sign on to .](../_images/xhf1616786720509.png)

## Adding user groups

After adding groups to PingCentral, associate them with PingCentral applications and provide application access to many users at once. Add groups one by one or import group information in a `.csv` file.

### Steps

1. Sign on to PingCentral using SSO.

   |   |                                                                 |
   | - | --------------------------------------------------------------- |
   |   | Group functionality is only available if you sign on using SSO. |

2. To add groups of users one by one:

   1. On the **Groups** tab, click **Add Group**.

   2. On the **Add Group** page, complete these fields:

      * **Group Name**: Enter the group name. Group names should match the group names in your datastore and are not case-sensitive.

      * **Display Name (Optional)**: Enter the name to display in PingCentral.

      * **Description (Optional)**: Enter a description of the user group to display in PingCentral.

   3. Click **Save and Close**.

      #### Result:

      The new group displays at the top of the **Groups** list. Click the **Expand** icon to see information about the groups and its members. Use the filter to locate specific groups.

      ![A screen capture showing the Groups page with the new group displayed at the top of the page.](../_images/hrh1617036254344.png)

3. To import information about a group of users:

   1. On the **Groups** tab, click **Import Groups**.

   2. On the **Upload File** page, click **Choose**.

   3. Select the `.csv` files that you want to import and click **Open** and click **Next**.

   4. On the **Preview Groups** page, review the group names, display names, and descriptions, and ensure they are accurate. If not, correct the `.csv` file and import it again.

      The **Name** field is required, but the **Display Name** and **Description** fields are optional.

      ![A screen capture showing the Preview Groups page and the information uploaded in the CSV file.](../_images/jms1617039185073.png)

   5. Click **Save and Close**.

      #### Result:

      The new group displays at the top of the **Groups** list. Click the **Expand** icon to see information about the groups and its members. Use the filter to locate specific members or groups.

      After application owners associate users or groups of users with their applications, the ownership information also displays when you select the application.

      ![A screen capture showing the Applications page and the owners assigned to the new application.](../_images/fhs1617035391927.png)

## Updating user groups

You can update the name, display name, and description for a user group.

### Steps

1. To update user group information, click the **Expand** icon associated with the group that you want to update and then click the **Pencil** icon.

   #### Result:

   All the editable information is displayed on the page.

2. Update the information in the **Name**, **Display Name**, and **Description** fields as needed, and click **Save and Close**.

   |   |                                                                                                                                                                       |
   | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | If the group name is updated in PingCentral but not in your data store, the groups will be out of sync, which might cause users to lose access to their applications. |

## Deleting user groups

Delete user groups when they are no longer needed.

### Steps

1. On the **Groups** tab, select the group you want to delete and click the associated **Delete** icon.

   #### Result:

   A message displays asking you if you want to delete the group.

2. Click **Delete**.