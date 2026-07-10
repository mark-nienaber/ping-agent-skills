---
title: Admin console best practices
description: The admin console is a convenient way to configure and manage your PingFederate environment. However, you should keep the following best practices in mind while using the admin console so that you don't inadvertently create errors or corrupt your PingFederate configuration.
component: pingfederate
version: 13.1
page_id: pingfederate:getting_started_with_pingfederate:pf_admin_console_best_practices
canonical_url: https://docs.pingidentity.com/pingfederate/13.1/getting_started_with_pingfederate/pf_admin_console_best_practices.html
llms_txt: https://docs.pingidentity.com/pingfederate/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
---

# Admin console best practices

The admin console is a convenient way to configure and manage your PingFederate environment. However, you should keep the following best practices in mind while using the admin console so that you don't inadvertently create errors or corrupt your PingFederate configuration.

* Don't use your browser's **Back** button

  Using your browser's navigation buttons such as **Back** or **Reload**, can cause PingFederate to behave inconsistently.

  If you need to go back to a previous menu, use the navigation buttons at the top or right side of the PingFederate menu.

  To go back a step in a configuration workflow with multiple tabs, click the tab you want to visit, or click **Previous** at the bottom of the screen.

  ![a screencapture of the Protocol Settings menu with arrows pointing to the previous tab and Previous button.](../administrators_reference_guide/_images/pf_img_backnav.png)

* Don't use multiple browser tabs

  Using PingFederate in multiple browser tabs could cause errors or inconsistencies.

* Wait for a page to finish loading before going to another page

  Going to another page before the current page finishes loading can cause inconsistent behavior. Even if you go to a page by mistake, allow it to load fully before going elsewhere.

* One administrator at a time

  You should allow only one administrative user to sign on to PingFederate at any one time. Because admins can create or change configurations, having multiple admins working in PingFederate at the same time risks causing conflicts.

  |   |                                                                                                                                                 |
  | - | ----------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | To configure PingFederate to allow only one administrator at a time, set the `pf.console.login.mode` parameter in `run.properties` to `single`. |

  You can have one or more auditors in PingFederate at the same time as an admin. Auditors can see settings in the admin console, but they can't change them.

* Don't replicate while an admin is working

  If you're running PingFederate in a clustered environment, you should only replicate configurations to other nodes while no admins are working in the admin console. If an admin is creating or changing a configuration while replication is in progress, the replication might only carry over a portion of the configuration.

* Clear your cache and cookies

  If pages in PingFederate aren't loading at all, or it returns the **Something's not right** error page, trying clearing the cache and cookies in your browser. This can be particularly effective after an upgrade.

---

---
title: AWS CloudHSM operational notes
description: When using a hardware security module (HSM), some restrictions apply to PingFederate.
component: pingfederate
version: 13.1
page_id: pingfederate:getting_started_with_pingfederate:pf_aws_cloudhsm_operat_notes
canonical_url: https://docs.pingidentity.com/pingfederate/13.1/getting_started_with_pingfederate/pf_aws_cloudhsm_operat_notes.html
llms_txt: https://docs.pingidentity.com/pingfederate/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: December 13, 2023
---

# AWS CloudHSM operational notes

When using a hardware security module (HSM), some restrictions apply to PingFederate.

* PingFederate requires Java 17 or 21 for deployment.

* As an OpenID Provider, PingFederate can use static or dynamically-rotating keys to sign ID tokens, JSON web tokens (JWTs) for client authentication, and OpenID Connect request objects. When using dynamically rotating keys as part of the default configuration, the memory, not the HSM, stores short-term keys. The HSM can store static keys.

* Private keys aren't exportable. When configured for use with the HSM, PingFederate disables administrative-console options for this feature. Only the public portion of generated keys is exportable.

* When using the Configuration Archive feature, any keys, certificates, or objects generated and stored on the HSM prior to saving a configuration archive must continue to exist unaltered when the archive is restored. In other words, the PingFederate user interface must execute any deletion or creation of objects on the HSM for proper operation.

  For example, you create and save objects A, B, and C to the HSM and create a data archive that contains references to those objects. If you delete object C and attempt to recover it through the data archive, PingFederate fails. Because the data archive contains a reference to the object and the object has been deleted from the HSM, you cannot use that data archive again.

* PingFederate limits cipher suites to those listed in the `<pf_install>/pingfederate/server/default/data/config-store/com.pingidentity.crypto.AWSCloudHSMJCEManager.xml` file.

|   |                                                                                                                           |
| - | ------------------------------------------------------------------------------------------------------------------------- |
|   | If the CloudHSM client daemon disconnects during runtime, PingFederate automatically attempts to reconnect to the daemon. |

---

---
title: Bouncy Castle FIPS provider
description: In Bouncy Castle Federal Information Processing Standards (FIPS) mode, all security-related cryptographic operations in PingFederate are handled by the Bouncy Castle FIPS security provider. Bouncy Castle FIPS is a FIPS 140-2 validated software cryptographic module. Operating in Bouncy Castle FIPS mode might be required if PingFederate is running as part of a FedRAMP-certified cloud service.
component: pingfederate
version: 13.1
page_id: pingfederate:getting_started_with_pingfederate:pf_bouncy_castle_fips_provider
canonical_url: https://docs.pingidentity.com/pingfederate/13.1/getting_started_with_pingfederate/pf_bouncy_castle_fips_provider.html
llms_txt: https://docs.pingidentity.com/pingfederate/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: October 24, 2025
section_ids:
  bouncy-castle-operational-notes: Bouncy Castle operational notes
  bouncy-castle-upgrade-considerations: Bouncy Castle upgrade considerations
---

# Bouncy Castle FIPS provider

In Bouncy Castle Federal Information Processing Standards (FIPS) mode, all security-related cryptographic operations in PingFederate are handled by the Bouncy Castle FIPS security provider. Bouncy Castle FIPS is a FIPS 140-2 validated software cryptographic module. Operating in Bouncy Castle FIPS mode might be required if PingFederate is running as part of a FedRAMP-certified cloud service.

Third-party libraries deployed in PingFederate, such as JDBC drivers, aren't guaranteed to operate in a FIPS-compliant fashion. When FIPS 140-3 compliance is a goal, you should confirm with the vendor before using any third-party libraries.

Plugins such as adapters and password credential validators need to be individually assessed for FIPS compliance. The FIPS status of a plugin is displayed in the Summary page inside its configuration. A warning is also logged on start-up for any configured plugins that are not FIPS-compliant or have not yet been assessed.

The integration of Bouncy Castle FIPS provider supports two phases:

* **Hybrid** to transition private keys from default keystore to the Bouncy Castle keystore.

* **Non-Hybrid** to start storing private keys only in the Bouncy Castle keystore.

Several properties in the `<pf_install>/pingfederate/bin/run.properties` file allow you to configure these phases as shown in the following table.

| Phase      | Properties                                |
| ---------- | ----------------------------------------- |
| Hybrid     | `pf.hsm.mode=BCFIPS``pf.hsm.hybrid=true`  |
| Non-Hybrid | `pf.hsm.mode=BCFIPS``pf.hsm.hybrid=false` |

|   |                                                                                                               |
| - | ------------------------------------------------------------------------------------------------------------- |
|   | The only way to switch from BCFIPS mode back to non-BCFIPS mode is to roll back PingFederate with an archive. |

## Bouncy Castle operational notes

When using the Bouncy Castle FIPS provider, some restrictions apply to PingFederate.

* As an OpenID Provider, PingFederate can use static or dynamically rotating keys to sign ID tokens, JSON web tokens (JWTs) for client authentication, and OpenID Connect request objects. When using dynamically rotating keys as part of the default configuration, the memory, not the BCFIPS key stores, stores short-term keys. The HSM can store static keys.

* PingFederate limits cipher suites to those listed in the `<pf_install>/pingfederate/server/default/data/config-store/com.pingidentity.crypto.BCFIPSJCEManager.xml` file.

## Bouncy Castle upgrade considerations

If you're upgrading to FIPS 140-3, you might notice specific behavior changes due to the stricter requirements of the new standard.

By default, PingFederate runs in approved mode. This is controlled by the setting `pf.fips.allow.unapproved.algorithms` in `run.properties`, which is set to `false` by default.

When running in this approved mode, the following algorithms are no longer available for use:

* DES decryption

* RSA PKCS#1.5 encryption

* SHA-1 for signature generation

Learn more detailed information on these and other potential changes in the [Bouncy Castle BC-FJA 2.0.0 Porting Guide](https://downloads.bouncycastle.org/fips-java/docs/BC-FJA%202.0.0%20Porting%20Guide.pdf).

---

---
title: Console buttons
description: The buttons at the bottom of the administrative console change depending on where you are in the configuration process.
component: pingfederate
version: 13.1
page_id: pingfederate:getting_started_with_pingfederate:pf_console_buttons
canonical_url: https://docs.pingidentity.com/pingfederate/13.1/getting_started_with_pingfederate/pf_console_buttons.html
llms_txt: https://docs.pingidentity.com/pingfederate/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 5, 2022
---

# Console buttons

The buttons at the bottom of the administrative console change depending on where you are in the configuration process.

The following table describes these buttons.

| Button         | Description                                                                                                                                                                                                                                                                                                                                   |
| -------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Save**       | Saves changes for all tabs in the current task and returns to thewindow from which the task or tab was accessed. This button is available only when the **Save** operation is valid.                                                                                                                                                          |
| **Done**       | Marks all steps as complete for a current task, but does not save the configuration because further tasks or steps are necessary. To save your changes, click **Save**, or continue the configuration until you see a **Save** button. When creating a new service provider (SP) or identity provider (IdP) connection, click **Save Draft**. |
| **Save Draft** | Saves a connection's draft configuration.                                                                                                                                                                                                                                                                                                     |
| **Cancel**     | Discards all changes and returns to the window from which the current task was accessed.                                                                                                                                                                                                                                                      |
| **Previous**   | Returns to the previous tab.                                                                                                                                                                                                                                                                                                                  |
| **Next**       | Proceeds to the next tab if all required steps are complete in the current tab.                                                                                                                                                                                                                                                               |

|   |                                                                                                                                                                                   |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Do not use the browser's **Back**, **Forward**, or**Refresh** buttons. Always use the navigation buttons in the PingFederate user interface, **Previous**, **Next**, or **Done**. |

---

---
title: Customizing shortcuts
description: Shortcuts allow you to access specific locations within the PingFederate administrative console immediately. You can customize which shortcuts you want to use by opening the Shortcuts customization menu available on the PingFederate main window.
component: pingfederate
version: 13.1
page_id: pingfederate:getting_started_with_pingfederate:pf_custom_shortcuts
canonical_url: https://docs.pingidentity.com/pingfederate/13.1/getting_started_with_pingfederate/pf_custom_shortcuts.html
llms_txt: https://docs.pingidentity.com/pingfederate/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 5, 2022
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Customizing shortcuts

Shortcuts allow you to access specific locations within the PingFederate administrative console immediately. You can customize which shortcuts you want to use by opening the **Shortcuts** customization menu available on the PingFederate main window.

## About this task

Shortcuts are available for all PingFederate roles. You can customize up to ten shortcuts.

## Steps

1. Click the **Pencil** icon beside **Shortcuts** to open the Shortcuts customization menu.

   The currently configured shortcuts are shown in the upper pane.

2. You can perform the following tasks.

   * To remove a current shortcut, click its icon in the upper pane. When you do this, the icon is displayed underneath **Recently Used**. Click the icon if you want to move it back to the list of current shortcuts.

   * To rearrange the current shortcuts, click and drag them to different positions in the upper pane.

   * To view the shortcuts that are available in every navigation section of the administrative console, click **Authentication**, **Applications**, **Security**, and **System**. Click a shortcut's icon or drag it into the upper pane to add it to the list of current shortcuts.

   * To restore the default shortcut settings, click **Restore Default**.

3. When you have finished customizing your shortcuts, click **Save**.

---

---
title: Getting Started with PingFederate
description: This guide provides information about configuring PingFederate to deploy a secure Internet-identity platform, including single sign-on (SSO), based on the latest security and business standards.
component: pingfederate
version: 13.1
page_id: pingfederate:getting_started_with_pingfederate:pf_get_started_w_pf
canonical_url: https://docs.pingidentity.com/pingfederate/13.1/getting_started_with_pingfederate/pf_get_started_w_pf.html
llms_txt: https://docs.pingidentity.com/pingfederate/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: October 6, 2022
---

# Getting Started with PingFederate

This guide provides information about configuring PingFederate to deploy a secure Internet-identity platform, including single sign-on (SSO) *(tooltip: \<div class="paragraph">
\<p>The process of authenticating an identity (signing on) at one website (usually with a user ID and password) and then accessing resources secured by other domains without reauthenticating.\</p>
\</div>)*, based on the latest security and business standards.

---

---
title: Integrating Bouncy Castle FIPS providers
description: This procedure describes how to integrate PingFederate with Bouncy Castle Federal Information Processing Standards (FIPS) provider.
component: pingfederate
version: 13.1
page_id: pingfederate:getting_started_with_pingfederate:pf_integrating_bouncy_castle_fips
canonical_url: https://docs.pingidentity.com/pingfederate/13.1/getting_started_with_pingfederate/pf_integrating_bouncy_castle_fips.html
llms_txt: https://docs.pingidentity.com/pingfederate/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: November 18, 2025
section_ids:
  steps: Steps
---

# Integrating Bouncy Castle FIPS providers

This procedure describes how to integrate PingFederate with Bouncy Castle Federal Information Processing Standards (FIPS) provider.

## Steps

1. Edit the `<pf_install>/pingfederate/server/default/conf/service-points.conf` file.

   1. Go to the `# Crypto provider services` section.

   2. Set `jce.manager` to `com.pingidentity.crypto.BCFIPSJCEManager`.

   3. Set `certificate.service` to `com.pingidentity.crypto.BCFIPSCertificateServiceImpl`.

   |   |                                                                                                                                                                                    |
   | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | In clustered PingFederate environments, you must manually edit the `service-points.conf` file on each node because cluster replication can't replicate this change to other nodes. |

2. Edit the `<pf_install>/pingfederate/bin/run.properties` file.

   1. Change the `pf.hsm.mode` property to `BCFIPS`.

   2. If you are setting up a new PingFederate installation, set the value of the `pf.hsm.hybrid` property to `false` to store newly created or imported certificates on your HSM.

   3. If you are configuring an existing PingFederate installation, set the `pf.hsm.hybrid` value to `true` for the flexibility to store each relevant key and certificate on the HSM or the local trust store.

   This allows you to transition the storage of keys and certificates to your HSM without deploying a new PingFederate environment. For more information, see [Transitioning to an HSM](../administrators_reference_guide/pf_transition_to_hsm.html).

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | On Linux systems, the Bouncy Castle FIPS-approved secure random number generator can drain a large amount of entropy during initial seeding. If available entropy becomes too low, the PingFederate server or bundled command-line tools can stall on startup for long periods of time. If this occurs, then you will likely need to integrate with a hardware random number generator or install an entropy-supplementing daemon like `rngd`. |

---

---
title: Integrating with AWS CloudHSM
description: PingFederate supports multiple hardware security modules (HSMs), including Amazon Web Services (AWS) CloudHSM.
component: pingfederate
version: 13.1
page_id: pingfederate:getting_started_with_pingfederate:pf_integra_aws_cloudhsm
canonical_url: https://docs.pingidentity.com/pingfederate/13.1/getting_started_with_pingfederate/pf_integra_aws_cloudhsm.html
llms_txt: https://docs.pingidentity.com/pingfederate/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: November 10, 2025
section_ids:
  before-you-begin: Before you begin
  steps: Steps
  choose-from: Choose from:
  choose-from-2: Choose from:
  choose-from-3: Choose from:
  example: Example:
---

# Integrating with AWS CloudHSM

PingFederate supports multiple hardware security modules (HSMs), including Amazon Web Services (AWS) *(tooltip: \<div class="paragraph">
\<p>An Amazon subsidiary providing cloud computing platforms.\</p>
\</div>)* CloudHSM.

## Before you begin

* Ensure that Java 17 or 21 is installed on the PingFederate server. Learn more in [Installing Java](../installing_and_uninstalling_pingfederate/pf_install_java.html).

* PingFederate must be deployed on one of the operating systems supported by both AWS CloudHSM and PingFederate. See [System requirements](../installing_and_uninstalling_pingfederate/pf_system_requirements.html) and [Supported platforms for the client SDKs](https://docs.aws.amazon.com/cloudhsm/latest/userguide/client-supported-platforms.html) in the AWS CloudHSM documentation for a list of mutually supported operating systems.

|   |                                                                                        |
| - | -------------------------------------------------------------------------------------- |
|   | As of version 11.2, PingFederate will no longer support the AWS CloudHSM Client SDK 3. |

## Steps

1. Request a crypto user (CU) account from your AWS CloudHSM administrator.

   You need this account's username and password for your PingFederate installation.

2. Install and configure the AWS CloudHSM Java Cryptography Extension (JCE) provider for Client SDK 5. Learn more in [Install and use the AWS CloudHSM JCE provider for Client SDK 5](https://docs.aws.amazon.com/cloudhsm/latest/userguide/java-library-install_5.html) in the AWS CloudHSM documentation.

   |   |                                                                                                                                                                                                      |
   | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | To ensure successful installation of the JCE provider, do not install the AWS CloudHSM client. If you are upgrading from PingFederate 11.1 or earlier, remove any existing CloudHSM client software. |

3. Connect the Client SDK to the AWS CloudHSM cluster. For instructions, see [Bootstrap the Client SDK](https://docs.aws.amazon.com/cloudhsm/latest/userguide/cluster-connect.html#connect-how-to) in the AWS CloudHSM documentation.

4. Run the appropriate command for your operating system to ensure that keys are available to use even if a cluster not containing multiple HSMs is used:

   ### Choose from:

   * On Linux operating systems, run the `sudo /opt/cloudhsm/bin/configure-jce --disable-key-availability-check` command.

   * On Windows operating systems, run the `C:\Program Files\Amazon\CloudHSM\bin\configure-jce.exe --disable-key-availability-check` command.

5. If you plan to use elliptic curve (EC) keys for decryption, run the appropriate command for your operating system.

   ### Choose from:

   * On Linux operating systems, run the `sudo /opt/cloudhsm/bin/configure-jce --enable-ecdh-without-kdf` command.

   * On Windows operating systems, run the `C:\Program Files\Amazon\CloudHSM\bin\configure-jce.exe --enable-ecdh-without-kdf` command.

6. Configure a new PingFederate installation on the network interconnected to the HSM.

   |   |                                                                                       |
   | - | ------------------------------------------------------------------------------------- |
   |   | Go to the next step to integrate an existing PingFederate installation with your HSM. |

7. To enable the Java interface and PingFederate integration, copy the `cloudhsm-jce-5.6.0.jar` file to the `pingfederate/startup` directory:

   |   |                                                                                                                                                                                                                      |
   | - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | * On Linux operating systems, the file location is`/opt/cloudhsm/java/cloudhsm-jce-5.6.0.jar`.

   * On Windows operating systems, the file location is `C:\Program Files\Amazon\CloudHSM\java\cloudhsm-jce-5.6.0.jar`. |

8. If you are upgrading from PingFederate 11.1 or earlier, revert any previous changes to the `JAVA_HOME/jre/lib/security/java.security` file and remove the `pf-aws-cloud-hsm-wrapper.jar` and other files previously copied to `JAVA_HOME/jre/lib/ext`.

9. Edit the `<pf_install>/pingfederate/server/default/conf/service-points.conf` file.

   1. Go to the `# Crypto provider services` section.

   2. Change the `jce.manager` and `certificate.service` service endpoints to the following:

      ```
      ...
      jce.manager=com.pingidentity.crypto.AWSCloudHSMJCEManager
      ...
      certificate.service=com.pingidentity.crypto.AWSCloudHSMCertificateServiceImpl
      ...
      ```

      |   |                                                                                                                                                                                    |
      | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
      |   | In clustered PingFederate environments, you must manually edit the `service-points.conf` file on each node because cluster replication can't replicate this change to other nodes. |

10. Update the `<pf_install>/pingfederate/bin/run.properties` file:

    1. Change the value of the `pf.hsm.mode` property from `OFF` to `AWSCLOUDHSM`.

    2. If you are setting up a new PingFederate installation, set the value of the `pf.hsm.hybrid` property to `false` to store newly-created or imported certificates on your HSM.

    3. If you are configuring an existing PingFederate installation, set the value to `true` for the flexibility to store each relevant key and certificate on the HSM or the local trust store.

    This allows you to transition the storage of keys and certificates to your HSM without deploying a new PingFederate environment. For more information, see [Transitioning to an HSM](../administrators_reference_guide/pf_transition_to_hsm.html).

11. Run:

    ### Choose from:

    * The `<pf_install>/pingfederate/bin/hsmpass.sh` script on Linux operating systems.

    * The `<pf_install>/pingfederate/bin/hsmpass.bat` command on Windows operating systems.

12. Enter the password for the CU account that you requested in step 1 when prompted.

    This procedure securely stores the password for communication to the HSM from PingFederate.

13. If the username of the CU account is not `crypto_user`, update the `com.pingidentity.crypto.AWSCloudHSM.xml` file:

    1. Edit the `<pf_install>/pingfederate/server/default/data/config-store/com.pingidentity.crypto.AWSCloudHSM.xml` file.

       The unmodified version of the `com.pingidentity.crypto.AWSCloudHSM.xml` file is shown in the following:

       ```xml
       <?xml version="1.0" encoding="UTF-8"?>
       <con:config xmlns:con="http://www.sourceid.org/2004/05/config">
           <con:item name="Partition">PARTITION_1</con:item>
           <con:item name="CryptoUser">crypto_user</con:item>
       </con:config>
       ```

    2. Replace `crypto_user` with the username of the CU account.

       ### Example:

       In the following example, the username of the CU account is `example_user`.

    ```xml
    <?xml version="1.0" encoding="UTF-8"?>
    <con:config xmlns:con="http://www.sourceid.org/2004/05/config">
        <con:item name="Partition">PARTITION_1</con:item>
        <con:item name="CryptoUser">example_user</con:item>
    </con:config>
    ```

14. Repeat these steps on each node.

15. Start the new PingFederate server or restart the existing PingFederate server.

---

---
title: Integrating with Entrust nShield Connect HSM
description: PingFederate supports multiple hardware security modules (HSMs), including Entrust nShield Connect HSM.
component: pingfederate
version: 13.1
page_id: pingfederate:getting_started_with_pingfederate:pf_integra_entrus_nshield_connec_hsm
canonical_url: https://docs.pingidentity.com/pingfederate/13.1/getting_started_with_pingfederate/pf_integra_entrus_nshield_connec_hsm.html
llms_txt: https://docs.pingidentity.com/pingfederate/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: January 12, 2024
section_ids:
  steps: Steps
---

# Integrating with Entrust nShield Connect HSM

PingFederate supports multiple hardware security modules (HSMs), including Entrust nShield Connect HSM.

## Steps

1. Ensure the PingFederate server has a supported Java virtual machine (JVM) installed.

   For more information, see [Installing Java](../installing_and_uninstalling_pingfederate/pf_install_java.html).

2. Install and configure your Entrust nShield Connect HSM client software.

   As part of the installation, install the optional Java Support (including KeySafe) and nCipherKM JCA/JCE provider classes components.

3. After installation, see the HSM documentation from Entrust to make your PingFederate server a client of an HSM server.

   |   |                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
   | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | PingFederate supports both Operator Card Set (OCS) protected keys and module-protected keys.For OCS, note the password. You need the password for your installation of PingFederate.For module-protected keys, edit the `pingfederate/server/default/data/config-store/com.pingidentity.crypto.NCipherSettings.xml` file to add the following entries:```
   <con:item name="protect">module</con:item>
   <con:item name="ignorePassphrase">true</con:item>
   ``` |

4. To enable the Java interface, copy the `NFAST_HOME/java/classes/nCipherKM.jar` file to the `<pf_install>/pingfederate/startup` directory.

5. If you're upgrading from PingFederate 11.1 or earlier, revert any previous changes to the `JAVA_HOME/jre/lib/security/java.security` file and remove the `nCipherKM.jar` file previously copied to `JAVA_HOME/jre/lib/ext`.

6. Set up a new PingFederate installation on the network interconnected to the HSM.

   |   |                                                                                         |
   | - | --------------------------------------------------------------------------------------- |
   |   | Skip to the next step to integrate an existing PingFederate installation with your HSM. |

7. Edit the `<pf_install>/pingfederate/server/default/conf/service-points.conf` file.

   1. Go to the `# Crypto provider services` section.

   2. Change the `jce.manager` and `certificate.service` service endpoints to the following:

      ```
      ...
      jce.manager=com.pingidentity.crypto.NcipherJCEManager
      ...
      certificate.service=com.pingidentity.crypto.NcipherCertificateServiceImpl
      ...
      ```

      |   |                                                                                                                                                                                    |
      | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
      |   | In clustered PingFederate environments, you must manually edit the `service-points.conf` file on each node because cluster replication can't replicate this change to other nodes. |

8. Update the `<pf_install>/pingfederate/bin/run.properties` file.

   1. Change the value of `pf.hsm.mode` from `OFF` to `NCIPHER`.

   2. If you are configuring a new PingFederate installation, set the value of `pf.hsm.hybrid` to `false` to store newly created or imported certificates on your HSM.

   3. If you are configuring an existing PingFederate installation, set the value to `true`, which provides the flexibility to store each relevant key and certificate on the HSM or the local trust store. This capability allows you to transition the storage of keys and certificates to your HSM without the need to deploy a new PingFederate environment and to mirror the setup. For more information, see [Transitioning to an HSM](../administrators_reference_guide/pf_transition_to_hsm.html).

9. From the `<pf_install>/pingfederate/bin` directory, run the `hsmpass.bat` batch file for Windows or the `hsmpass.sh` script for Linux.

   Enter the Operator Card Set password when prompted. See [\[step2\]](#step2).

   This procedure securely stores the password for communication to the HSM from PingFederate.

10. If you're not using the default slot for OCS protection, specify the slot in `<pf_install>/pingfederate/server/default/data/config-store/com.pingidentity.crypto.NCipherSettings.xml`.

11. If you are setting up a new or configuring an existing PingFederate cluster, repeat these steps on each node.

    When finished, use the following steps to replicate nShield data to the connected nodes in the cluster.

    1. On the console node, go to the `<pf_install>/pingfederate/server/default/data` directory and create a sub directory named `ncipher-kmdata-local`.

    2. Copy to the `ncipher-kmdata-local` directory all files from the `NFAST_KMDATA\local` directory, where `NFAST_KMDATA` is an environment variable created during the nShield Connect installation.

    For example, `NFAST_KMDATA` could be set to `C:\ProgramData\nCipher\Key Management Data`.

    1. Create a new environment variable named `NFAST_KMLOCAL` and set it to `<pf_install>/pingfederate/server/default/data/ncipher-kmdata-local`.

       |   |                                                                              |
       | - | ---------------------------------------------------------------------------- |
       |   | You must define this environment variable on all servers within the cluster. |

    2. Restart the nShield Connect hardserver on all PingFederate servers in the cluster. For instructions on restarting the hardserver, see the HSM documentation from Entrust.

    3. Sign on to the PingFederate administrative console and go to **System > Server > Cluster Management**.

    4. To push the configuration changes, including the nShield data, to the engine nodes, click **Replicate Configuration**.

12. Start the new PingFederate server or restart the existing PingFederate server.

---

---
title: Integrating with Thales Luna Network HSM
description: PingFederate supports multiple hardware security modules (HSMs), including Thales Luna Network HSMs.
component: pingfederate
version: 13.1
page_id: pingfederate:getting_started_with_pingfederate:pf_integrating_thales_luna_network_hsm
canonical_url: https://docs.pingidentity.com/pingfederate/13.1/getting_started_with_pingfederate/pf_integrating_thales_luna_network_hsm.html
llms_txt: https://docs.pingidentity.com/pingfederate/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: December 30, 2025
section_ids:
  steps: Steps
---

# Integrating with Thales Luna Network HSM

PingFederate supports multiple hardware security modules (HSMs), including Thales Luna Network HSMs.

## Steps

1. Ensure that the PingFederate server has a supported Java virtual machine (JVM) installed.

   Learn more in [Installing Java](../installing_and_uninstalling_pingfederate/pf_install_java.html).

2. Install and configure your Thales Luna Network HSM, including the optional JSP package for Java, according to Thales's instructions.

   This includes creating a partition, creating a Network Trust Link (NTL), and assigning a client to a partition.

   1. Ensure the operation of the `vtl verify` command to indicate secure and proper communication with the HSM.

   2. Delete any unnecessary keys or objects created while testing communication to the HSM from the host running PingFederate.

   3. For your PingFederate installation, record the password used to open communication to the HSM through the NTL.

3. Update the `java.security` file in your Java environment by inserting `LunaProvider` after `SunJCE`, and then moving `SunRsaSign` and `SunEC` below `LunaProvider`. Ensure that the providers are numbered sequentially after your changes.

   * If the node uses Java 17 or 21, the `java.security` file is in the `JAVA_HOME/conf/security` directory. Here's an example of an updated file for Java 17:

     ```
     # List of providers and their preference orders (see above):
     security.provider.1=SUN
     security.provider.2=SunJSSE
     security.provider.3=SunJCE
     security.provider.4=com.safenetinc.luna.provider.LunaProvider
     security.provider.5=SunRsaSign
     security.provider.6=SunEC
     security.provider.7=SunJGSS
     security.provider.8=SunSASL
     security.provider.9=XMLDSig
     security.provider.10=SunPCSC
     security.provider.11=JdkLDAP
     security.provider.12=JdkSASL
     security.provider.13=SunMSCAPI
     security.provider.14=SunPKCS11
     ```

4. On the network interconnected to the HSM, set up a new PingFederate installation.

   |   |                                                                                          |
   | - | ---------------------------------------------------------------------------------------- |
   |   | To integrate an existing PingFederate installation with your HSM, skip to the next step. |

5. To enable the Java interface, copy the Luna library and program files to the Java installation as follows.

   | Operating system | Steps                                                                                                                                              |
   | ---------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- |
   | Windows          | Copy the `LunaAPI.dll` and `LunaProvider.jar` files from the `LUNA_HOME/jsp/lib` directory to the `<pf_install>/pingfederate/startup` directory.   |
   | Linux            | Copy the `libLunaAPI.so` and `LunaProvider.jar` files from the `LUNA_HOME/jsp/lib` directory to the `<pf_install>/pingfederate/startup` directory. |

   Prior to installing PingFederate, Thales provides sample Java applications to test that the Java HSM interface works. For more information, see the HSM documentation from Thales.

6. Edit the `<pf_install>/pingfederate/server/default/conf/service-points.conf` file.

   1. Go to the `# Crypto provider services` section.

   2. Change the `jce.manager` and `certificate.service` service endpoints to the following:

      ```
      ...
      jce.manager=com.pingidentity.crypto.LunaJCEManager
      ...
      certificate.service=com.pingidentity.crypto.LunaCertificateServiceImpl
      ...
      ```

      |   |                                                                                                                                                                                    |
      | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
      |   | In clustered PingFederate environments, you must manually edit the `service-points.conf` file on each node because cluster replication can't replicate this change to other nodes. |

7. In `com.pingidentity.crypto.LunaPartitions.xml`, configure `DefaultPartitionSlotOrLabel` with the slot number or label associated with the HSM partition you created in [\[step1\]](#step1).

8. Update the `<pf_install>/pingfederate/bin/run.properties` file.

   1. Change the value of `pf.hsm.mode` from `OFF` to `LUNA`.

   2. To configure a new PingFederate installation, set the value of `pf.hsm.hybrid` to `false`. When set to `false`, the HSM stores newly created or imported certificates.

      To configure an existing PingFederate installation, set the value to `true` for the flexibility to store each relevant key and certificate on the HSM or the local trust store. This allows you to transition the storage of keys and certificates to your HSM without deploying a new PingFederate environment. For more information, see [Transitioning to an HSM](../administrators_reference_guide/pf_transition_to_hsm.html).

9. From the `<pf_install>/pingfederate/bin` directory, run the `hsmpass.bat` batch file for Windows or the `hsmpass.sh` script for Linux.

   1. Enter the NTL password when prompted. For more information, see [\[step1\]](#step1).

      This procedure securely stores the password for NTL communication to the HSM from PingFederate.

      |   |                                                                                                                                                                                                                                                                                          |
      | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
      |   | The Thales Luna Network HSM supports configuration in a high-availability group. For more information, see the Thales distributed-installation instructions. To properly synchronize data, ensure that the `HAOnly` property is enabled using the `vtl haAdmin –HAOnly –enable` command. |

10. Repeat these steps on each node.

11. Start the new PingFederate server or restart the existing PingFederate server.

    |   |                                                                                                                                                   |
    | - | ------------------------------------------------------------------------------------------------------------------------------------------------- |
    |   | Whenever you restart the Luna HSM, Thales recommends you also restart dependent processes such as PingFederate and all server nodes in a cluster. |

---

---
title: Link and store CloudHSM keys
description: You can link private keys stored in Amazon Web Services (AWS) CloudHSM with their certificates in PingFederate's Java keystore.
component: pingfederate
version: 13.1
page_id: pingfederate:getting_started_with_pingfederate:pf_link_store_cloudhsm_keys
canonical_url: https://docs.pingidentity.com/pingfederate/13.1/getting_started_with_pingfederate/pf_link_store_cloudhsm_keys.html
llms_txt: https://docs.pingidentity.com/pingfederate/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  steps: Steps
  result: Result
---

# Link and store CloudHSM keys

You can link private keys stored in Amazon Web Services (AWS) *(tooltip: \<div class="paragraph">
\<p>An Amazon subsidiary providing cloud computing platforms.\</p>
\</div>)* CloudHSM with their certificates in PingFederate's Java keystore.

This allows you to use existing private key and certificate pairs associated with your CloudHSM instance in PingFederate.

You can use this feature to store:

* Signing key pairs

* Server key pairs

* Client key pairs

## Steps

1. Go to **Security > Certificate & Key Management > Signing & Decryption Keys & Certificates**.

2. Click **Link**. This opens the **Link Certificate** tab.

   |   |                                                                               |
   | - | ----------------------------------------------------------------------------- |
   |   | The **Link** button only displays when you run PingFederate in CloudHSM mode. |

3. In the **Private Key ID** field, paste the private key ID.

   To get this value, use the [CloudHSM CLI](https://docs.aws.amazon.com/cloudhsm/latest/userguide/cloudhsm_cli-getting-started-use.html) and run the `key list` command. The **Private Key ID** is the `label` value for the key you want to use.

4. Click **Choose File** to upload the certificate file.

5. Click **Next**.

6. On the **Summary** tab, click **Save**.

## Result

The new key and certificate pair displays in the **Signing & Decryption Keys & Certificates** list.

---

---
title: Navigation tabs and menus
description: The PingFederate administrative console provides navigation tabs and menus. When you select a tab at the top of the console, the relevant menus appear on the left menu pane. When you select a menu, the menu items appear. When you select a menu item, the window with the same name appears. The menus and menu items depend on your permissions in PingFederate. For more information about permissions, see Administrative accounts.
component: pingfederate
version: 13.1
page_id: pingfederate:getting_started_with_pingfederate:pf_nav_tabs_menus
canonical_url: https://docs.pingidentity.com/pingfederate/13.1/getting_started_with_pingfederate/pf_nav_tabs_menus.html
llms_txt: https://docs.pingidentity.com/pingfederate/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: December 1, 2022
---

# Navigation tabs and menus

The PingFederate administrative console provides navigation tabs and menus. When you select a tab at the top of the console, the relevant menus appear on the left menu pane. When you select a menu, the menu items appear. When you select a menu item, the window with the same name appears. The menus and menu items depend on your permissions in PingFederate. For more information about permissions, see [Administrative accounts](../administrators_reference_guide/help_administrativeaccountstasklet_administrativeaccountsstate.html).

**Each navigation tab provides access to multiple menus on the left menu pane**

| Menus on the Authentication tab                      | Menus on the Applications tab            | Menus on the Security tab                            | Menus on the System tab                                                                                                       |
| ---------------------------------------------------- | ---------------------------------------- | ---------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------- |
| * Integration

* Policies

* OAuth

* Token Exchange | - Integration

- OAuth

- Token Exchange | * Certificate & Key Management

* System Integration | - Data & Credential Stores

- Server

- OAuth Settings

- External Systems

- Monitoring & Notifications

- Protocol Metadata |

**Navigation tabs, menus, and menu items in alphabetical order**

| Tabs           | Menus                        | Menu items and window names              |
| -------------- | ---------------------------- | ---------------------------------------- |
| Applications   | Integration                  | Adapter-to-Adapter Mappings              |
|                |                              | Policy Contract Adapter Mappings         |
|                |                              | SP Adapters                              |
|                |                              | SP Connections                           |
|                |                              | SP Default URLs                          |
|                |                              | Target URL Mapping                       |
|                | OAuth                        | Access Token Management                  |
|                |                              | Access Token Mappings                    |
|                |                              | CIBA Request Policies                    |
|                |                              | Clients                                  |
|                |                              | OpenID Connect Policy Management         |
|                | Token Exchange               | Generator Groups                         |
|                |                              | Processor Policies                       |
|                |                              | Token Generator Mappings                 |
|                |                              | Token Generators                         |
|                |                              | Token Translator Mappings                |
| Authentication | Integration                  | Authentication API Applications          |
|                |                              | IdP Adapters                             |
|                |                              | IdP Connections                          |
|                |                              | IdP Default URL                          |
|                | OAuth                        | CIBA Authenticators                      |
|                |                              | IdP Adapter Grant Mapping                |
|                |                              | Policy Contract Grant Mapping            |
|                |                              | Resource Owner Credentials Grant Mapping |
|                | Policies                     | Fragments                                |
|                |                              | Local Identity Profiles                  |
|                |                              | Policies                                 |
|                |                              | Policy Contracts                         |
|                |                              | Selectors                                |
|                |                              | Sessions                                 |
|                | Token Exchange               | STS Request Parameters                   |
|                |                              | Token Processors                         |
| Security       | Certificate & Key Management | Certificate Revocation Checking          |
|                |                              | OAuth & OpenID Connect Keys              |
|                |                              | Partner Metadata URLs                    |
|                |                              | Signing & Decryption Keys & Certificates |
|                |                              | SSL Client Keys & Certificates           |
|                |                              | SSL Server Certificates                  |
|                |                              | System Keys                              |
|                |                              | Trusted CAs                              |
|                | System Integration           | Incoming Proxy Settings                  |
|                |                              | Redirect Validation                      |
|                |                              | Service Authentication                   |
| System         | Data & Credential Stores     | Active Directory Domains/Kerberos Realms |
|                |                              | Data Stores                              |
|                |                              | Identity Store Provisioners              |
|                |                              | Password Credential Validators           |
|                | External Systems             | CAPTCHA and Risk Providers               |
|                |                              | Connect to PingOne for Enterprise        |
|                |                              | Notification Publishers                  |
|                |                              | PingOne Connections                      |
|                |                              | SMS Provider Settings                    |
|                | Monitoring & Notifications   | Runtime Notifications                    |
|                |                              | Runtime Reporting                        |
|                | OAuth Settings               | Authorization Server Settings            |
|                |                              | Client Registration Policies             |
|                |                              | Client Settings                          |
|                |                              | Scope Management                         |
|                | Protocol Metadata            | Attribute Requester Mapping              |
|                |                              | File Signing                             |
|                |                              | Metadata Export                          |
|                |                              | Metadata Settings                        |
|                |                              | SP Affiliations                          |
|                | Server                       | Administrative Accounts                  |
|                |                              | Cluster Management                       |
|                |                              | Configuration Archive                    |
|                |                              | Extended Properties                      |
|                |                              | General Settings                         |
|                |                              | License                                  |
|                |                              | Virtual Host Names                       |

---

---
title: nShield Connect HSM operational notes
description: Some restrictions apply to PingFederate when using a hardware security module (HSM).
component: pingfederate
version: 13.1
page_id: pingfederate:getting_started_with_pingfederate:pf_nshield_connec_hsm_operat_notes
canonical_url: https://docs.pingidentity.com/pingfederate/13.1/getting_started_with_pingfederate/pf_nshield_connec_hsm_operat_notes.html
llms_txt: https://docs.pingidentity.com/pingfederate/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: February 23, 2023
---

# nShield Connect HSM operational notes

Some restrictions apply to PingFederate when using a hardware security module (HSM).

* PingFederate only supports Operator Card Set (OCS) protected keys. If you use a standard, non-persistent OCS, removing the card from the smart card reader causes the HSM to remove the protected keys from its memory. Requests will likely fail because almost all requests require cryptographic processing. To resume operations, insert the card into the smart card reader and then restart PingFederate.

  Alternatively, use a persistent OCS so that protected keys remain in memory even after the card is removed from the smart card reader. PingFederate will continue to process requests and to load keys and certificates from the HSM as needed. Until the card is inserted back into the HSM, the HSM will not support new key and certificate creation and storage. However, using a persistent OCS does not require a restart of PingFederate in this situation. For more information about persistent OCS, consult your HSM vendor.

* As an OpenID Provider, PingFederate can use static or dynamically-rotating keys to sign ID tokens, JSON web tokens (JWTs) for client authentication, and OpenID Connect request objects. When using dynamically-rotating keys as part of the default configuration, the memory, not the HSM, stores short-term keys. The HSM can store static keys.

* Private keys are not exportable. When configured for use with the HSM, PingFederate disables administrative-console options for this feature. Only the public portion of generated keys is exportable.

* When running in FIPS 140-2 level 3 compliance, also called strict FIPS mode, private keys cannot be imported. In this mode, administrative-console options for this feature are disabled.

* When using the Configuration Archive feature, any keys, certificates, or objects generated and stored on the HSM prior to saving a configuration archive must continue to exist unaltered when the archive is restored. In other words, the PingFederate user interface must execute any deletion or creation of objects on the HSM for proper operation.

  For example, you create and save objects A, B, and C to the HSM and create a data archive that contains references to those objects. If you delete object C and attempt to recover it through the data archive, PingFederate fails. Because the data archive contains a reference to the object and the object has been deleted from the HSM, you cannot use that data archive again.Q

* PingFederate limits cipher suites to those listed in the `<pf_install>/pingfederate/server/default/data/config-store/com.pingidentity.crypto.NcipherJCEManager.xml` file.

---

---
title: Opening the PingFederate administrative console
description: The PingFederate administrative console provides a wizard-like interface in which you configure your federation use cases.
component: pingfederate
version: 13.1
page_id: pingfederate:getting_started_with_pingfederate:pf_open_pf_admin_console
canonical_url: https://docs.pingidentity.com/pingfederate/13.1/getting_started_with_pingfederate/pf_open_pf_admin_console.html
llms_txt: https://docs.pingidentity.com/pingfederate/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 5, 2022
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Opening the PingFederate administrative console

The PingFederate administrative console provides a wizard-like interface in which you configure your federation use cases.

## About this task

To open the administrative console:

## Steps

1. Start PingFederate. See [Starting and stopping PingFederate](pf_start_stop_pf.html).

   In a clustered PingFederate environment, start PingFederate on the console node.

2. Start a web browser.

3. Go to https\://*\<pf\_host>*:9999/.

   |   |                                                                                                                                                                                                                                                                                                                                                                                                             |
   | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | For PingFederate 10.1 and earlier, the administrative console is accessed at https\://*\<pf\_host>*:9999/pingfederate/app.*\<pf\_host>* is the network address of your PingFederate server. It can be an IP address, a host name, or a fully qualified domain name. It must be reachable from your computer.`9999` is the default value of the `pf.admin.https.port` property in the `run.properties` file. |

---

---
title: PingFederate administrative console
description: The PingFederate administrative console provides pages and a wizard-like interface in which you configure your federation use cases.
component: pingfederate
version: 13.1
page_id: pingfederate:getting_started_with_pingfederate:pf_admin_console
canonical_url: https://docs.pingidentity.com/pingfederate/13.1/getting_started_with_pingfederate/pf_admin_console.html
llms_txt: https://docs.pingidentity.com/pingfederate/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 5, 2022
---

# PingFederate administrative console

The PingFederate administrative console provides pages and a wizard-like interface in which you configure your federation use cases.

The toolbar at the top of the administrative console provides controls mainly for navigating PingFederate. Learn more about navigating PingFederate in [Navigation tabs and menus](pf_nav_tabs_menus.html).

![The toolbar provides controls for navigating PingFederate](../_images/xug1654555395817.png)

` `

| Toolbar control                                                             | Description                                                                                                                                                                                                                                                         |
| --------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| PingOne home button ![PingOne home button](../_images/sfk1654624859806.png) | If PingFederate is integrated with PingOne, this button opens the PingOne unified admin console.&#xA;&#xA;Configure the region and environment ID for your PingOne unified admin URL in the run.properties file. Learn more in Configuring PingFederate properties. |
| **PingFederate** home link                                                  | Opens the PingFederate administrative console's home page                                                                                                                                                                                                           |
| **Authentication** tab                                                      | Opens the **Authentication** navigation page, which offers a menu pane and a shortcut pane                                                                                                                                                                          |
| **Applications** tab                                                        | Opens the **Applications** navigation page, which offers a menu pane and a shortcut pane                                                                                                                                                                            |
| **Security** tab                                                            | Opens the **Security** navigation page, which offers a menu pane and a shortcut pane                                                                                                                                                                                |
| **System** tab                                                              | Opens the **System** navigation page, which offers a menu pane and a shortcut pane                                                                                                                                                                                  |
| **Search** icon ![Search icon](../_images/dom1654625950097.png)             | Opens a dialog box that lets you search for and open PingFederate pages                                                                                                                                                                                             |
| **Bell** icon ![Bell icon](../_images/eux1654635558642.png)                 | When a dot appears on the icon, clicking the icon opens a message about an important administrative issue. The messages also provide a link to the page where you can resolve the issue.&#xA;&#xA;Some critical notifications appear on a banner above the toolbar. |
| **Help** icon ![Help icon](../_images/bwj1654625472529.png)                 | Opens the **Help** menu, which provides access to context-sensitive online help, a tour of the console, endpoint information, and information about your version and license                                                                                        |
| **Account** icon ![Account icon](../_images/wcu1654625718397.png)           | Lets you sign on to and off from your PingFederate account                                                                                                                                                                                                          |

---

---
title: Setting up PingFederate
description: After installing PingFederate, use the PingFederate setup wizard to configure the necessary initial settings.
component: pingfederate
version: 13.1
page_id: pingfederate:getting_started_with_pingfederate:pf_setting_up_pf
canonical_url: https://docs.pingidentity.com/pingfederate/13.1/getting_started_with_pingfederate/pf_setting_up_pf.html
llms_txt: https://docs.pingidentity.com/pingfederate/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 10, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
  result: Result:
---

# Setting up PingFederate

After [installing PingFederate](../installing_and_uninstalling_pingfederate/pf_installing_uninstalling_pf.html), use the PingFederate setup wizard to configure the necessary initial settings.

## About this task

The setup wizard guides you through the following steps:

1. Agree to the Terms and Conditions.

2. Enter the base URL used for communicating with your PingFederate environment.

3. Connect to PingOne. You can do this step later. For more information, see [Creating connections to PingOne](../administrators_reference_guide/help_p1connections_p1connectioncreate.html).

4. Upload your PingFederate license.

5. Create an administrator account.

6. Review and finish.

|   |                                                                                                                                                                                                             |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The wizard appears every time you open the PingFederate administrative console until you complete your initial setup.If you exit the wizard before completing the setup, none of your information is saved. |

## Steps

1. Start the PingFederate server. For more information, see [Starting and stopping PingFederate](pf_start_stop_pf.html)

2. In your browser, go to https\://*\<pf\_host>*:9999/pingfederate/app. The setup wizard opens.

   |   |                                                                                                                                                                                                                                                                                   |
   | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | *\<pf\_host>* is the network address of your PingFederate server. It can be an IP address, a host name, or a fully qualified domain name. It must be reachable from your computer.`9999` is the default value of the `pf.admin.https.port` property in the `run.properties` file. |

3. Follow the instructions in the wizard.

   |   |                                                                                                                                                                     |
   | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | Click **Back** to return to a previous step.Click **X** and close the browser tab to cancel your setup process.Click **Restart** to start again from the beginning. |

   ### Result:

   After you complete the setup wizard's steps, the PingFederate administrative console opens. You can continue configuring PingFederate.

---

---
title: Starting and stopping PingFederate
description: Depending on the application mode and the operating system, the steps to start, stop, or restart PingFederate vary.
component: pingfederate
version: 13.1
page_id: pingfederate:getting_started_with_pingfederate:pf_start_stop_pf
canonical_url: https://docs.pingidentity.com/pingfederate/13.1/getting_started_with_pingfederate/pf_start_stop_pf.html
llms_txt: https://docs.pingidentity.com/pingfederate/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 8, 2026
section_ids:
  starting-and-stopping-pingfederate-on-windows: Starting and stopping PingFederate on Windows
  starting-and-stopping-pingfederate-as-an-application: Starting and stopping PingFederate as an application
  starting-and-stopping-pingfederate-as-a-windows-service: Starting and stopping PingFederate as a Windows service
  starting-and-stopping-pingfederate-on-linux: Starting and stopping PingFederate on Linux
  starting-and-stopping-pingfederate-as-an-application-2: Starting and stopping PingFederate as an application
  starting-and-stopping-pingfederate-as-a-linux-service: Starting and stopping PingFederate as a Linux service
---

# Starting and stopping PingFederate

Depending on the application mode and the operating system, the steps to start, stop, or restart PingFederate vary.

If you install or upgrade PingFederate using its platform-specific installer, PingFederate configures to run as a service. You can stop and disable the service and run PingFederate as a console application.

If you install or upgrade PingFederate manually by using the PingFederate product distribution file or the Upgrade Utility in command line, you can run PingFederate as a console application or install the PingFederate service manually and run it as a service.

## Starting and stopping PingFederate on Windows

### Starting and stopping PingFederate as an application

To start PingFederate:

1. In Windows, open a command prompt.

2. Go to `<pf_install>/pingfederate/bin`.

3. Run `run.bat`.

4. Keep the command prompt open.

To stop PingFederate:

1. Locate the command prompt running PingFederate.

2. Press CTRL+C to terminate PingFederate.

To stop and restart PingFederate:

1. Locate the command prompt running PingFederate.

2. Press CTRL+C to terminate PingFederate.

3. When PingFederate stops, run `run.bat`.

4. Keep the command prompt open.

### Starting and stopping PingFederate as a Windows service

To start PingFederate:

1. In Windows, go to **Control Panel > System and Security > Administrative Tools > Services**.

2. Right-click on the PingFederate service and click **Start**.

To stop PingFederate:

1. Go to **Control Panel > Administrative Tools > Services**.

2. Right-click on the PingFederate service and click **Stop**.

To restart PingFederate:

1. Go to **Control Panel > Administrative Tools > Services**.

2. Right-click on the PingFederate service and select **Restart**.

## Starting and stopping PingFederate on Linux

### Starting and stopping PingFederate as an application

To start PingFederate:

1. Open a terminal window.

2. Go to `<pf_install>/pingfederate/bin`.

3. Run `run.sh`.

4. Keep the terminal window open.

To stop PingFederate:

1. Locate the terminal window running PingFederate.

2. Press CTRL+C to terminate PingFederate.

To restart PingFederate:

1. Locate the terminal window running PingFederate.

2. Press CTRL+C to terminate PingFederate.

3. When PingFederate stops, run `run.sh`.

4. Keep the terminal window open.

### Starting and stopping PingFederate as a Linux service

To start PingFederate:

1. Open a terminal window.

2. Enter the system-dependent service command to start PingFederate.

To stop PingFederate:

1. Open a terminal window.

2. Enter the system-dependent service command to stop PingFederate.

To restart PingFederate:

1. Open a terminal window.

2. Enter the system-dependent service command to restart PingFederate.

---

---
title: Supported hardware security modules
description: PingFederate supports multiple hardware security module (HSM) configurations for secure material storage and processing.
component: pingfederate
version: 13.1
page_id: pingfederate:getting_started_with_pingfederate:pf_supported_hardware_security_modules
canonical_url: https://docs.pingidentity.com/pingfederate/13.1/getting_started_with_pingfederate/pf_supported_hardware_security_modules.html
llms_txt: https://docs.pingidentity.com/pingfederate/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: August 6, 2025
---

# Supported hardware security modules

PingFederate supports multiple hardware security module (HSM) *(tooltip: \<div class="paragraph">
\<p>A dedicated cryptographic processor designed to manage and protect digital keys. HSMs act as trust anchors that protect the cryptographic key lifecycle by securely managing, processing, and storing cryptographic keys inside a hardened, tamper-resistant device.\</p>
\</div>)* configurations for secure material storage and processing.

When configuring a fresh setup of a PingFederate cluster with active and passive admin nodes and hardware security modules (HSM), you must designate one of the console nodes as the default active console. You can do this in the `cluster-admin-nodes-sync.conf` file of the node you want to make the default active by setting `default.admin.console.role=active`.

Configure the default active console first, and start it up before starting any passive consoles. This allows the passive consoles to synchronize their configurations with the default active console, which contains the necessary default SSL server certificate generated by the active console at its start-up.

If you fail to configure a default active console, the passive console's `server.log` will return the following error:

`Default active server cert is not present on node. This is a passive console node and HSM is configured so the cert will not be generated as that will strand an unused key on the HSM. Instead the configuration data needs to be retrieved from the active console. Ensure the active console is started before starting this passive console.`

Learn more in [Active and passive administrative nodes](../server_clustering_guide/pf_active_passive_admin_nodes.html).

PingFederate supports the following HSMs:

* AWS CloudHSM

* Thales Luna Network HSM

* Entrust nShield Connect HSM

---

---
title: Supported software security package
description: PingFederate supports the Bouncy Castle FIPS provider software security package.
component: pingfederate
version: 13.1
page_id: pingfederate:getting_started_with_pingfederate:pf_supp_softwa_securi_packag
canonical_url: https://docs.pingidentity.com/pingfederate/13.1/getting_started_with_pingfederate/pf_supp_softwa_securi_packag.html
llms_txt: https://docs.pingidentity.com/pingfederate/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 5, 2022
---

# Supported software security package

PingFederate supports the Bouncy Castle FIPS provider software security package.

---

---
title: Tasks and steps
description: Each task consists of a series of tabs. Each tab consists of a sequence of steps. The tasks and tabs appear in the top portion of the page.
component: pingfederate
version: 13.1
page_id: pingfederate:getting_started_with_pingfederate:pf_tasks_and_steps
canonical_url: https://docs.pingidentity.com/pingfederate/13.1/getting_started_with_pingfederate/pf_tasks_and_steps.html
llms_txt: https://docs.pingidentity.com/pingfederate/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 5, 2022
section_ids:
  example: Example
---

# Tasks and steps

Each task consists of a series of tabs. Each tab consists of a sequence of steps. The tasks and tabs appear in the top portion of the page.

![Screen capture of sample tasks and steps in the administrative console](../_images/ace1588872105916.png)Sample tasks and steps

In this example, the primary task is managing one or more IdP adapter instances (**IdP Adapters**). The secondary task is creating an adapter instance (**Create Adapter Instance**). The current tab selects the type of adapter (**Type**). The subsequent tabs, which the administrator has not yet reached, are grayed out.

The administrator console displays a summary page at the end of every task, which offers the opportunity to review and make changes as needed.

Some steps provide buttons that branch to secondary tasks with multiple tabs. When the secondary tasks are complete, the administrative console returns to the primary task for the administrators to continue with the configuration.

|   |                                                                                                                                                                   |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Clicking **Cancel** or **Done** discards all unsaved changes for the tabs shown in the current task and returns you to the page from which you accessed the task. |

## Example

When creating a connection to a partner, the administrator might need to create a new digital signing certificate. The administrative console provides a button to begin creating a new signing certificate. When the administrator completes the task, the administrative console returns to the primary task of creating a connection to a partner.