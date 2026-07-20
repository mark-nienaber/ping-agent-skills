---
title: Apache Tomcat
description: Configure Apache Tomcat as a deployment container for PingAM, including JVM settings, cookie domains, request logging, and security parameters
component: pingam
version: 8.1
page_id: pingam:installation:prepare-apache-tomcat
canonical_url: https://docs.pingidentity.com/pingam/8.1/installation/prepare-apache-tomcat.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Install", "Web Container"]
page_aliases: ["install-guide:prepare-apache-tomcat.adoc"]
section_ids:
  jvm_startup: JVM startup
  slashes_in_resource_names: Slashes in resource names
  cookie_domains: Cookie domains
  log_request_times: Log request times
  encoding_and_security: Encoding and security
---

# Apache Tomcat

AM examples often use Apache Tomcat (Tomcat) as the deployment container. In these examples, Tomcat is installed on `am.example.com` and listens on the default ports without a Java Security Manager enabled.

## JVM startup

AM core services require a minimum JVM heap size of 1 GB, and a metadata space size of up to 256 MB.

|   |                                                                                                                                                                                                                                                                                                                                                              |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | Metadata space (Metaspace) is a dedicated region within Native Memory. It can grow automatically if you don't set a maximum size. The ideal Metaspace size depends on your deployment and the number of scripts you're running. 256 MB is considered a safe value for production deployments, but you might need to tweak this for your specific deployment. |

Set a `CATALINA_OPTS` environment variable with the appropriate tuning for your environment. For example, add the following in your `setenv` file:

* Linux

* Windows

In `$CATALINA_BASE/bin/setenv.sh`:

```bash
export CATALINA_OPTS="$CATALINA_OPTS -server -Xmx2g -XX:MetaspaceSize=256m -XX:MaxMetaspaceSize=256m"
```

In `$CATALINA_BASE/bin/setenv.bat`:

```powershell
set "CATALINA_OPTS=%CATALINA_OPTS% -server -Xmx2g -XX:MetaspaceSize=256m -XX:MaxMetaspaceSize=256m"
```

Some versions of Microsoft Edge support the `Expires` header attribute instead of the `Max-Age` header attribute, which may cause SAML 2.0 and agent logout sequences to fail.

If you have set the `org.apache.catalina.STRICT_SERVLET_COMPLIANCE` Tomcat property to `true`, add the `org.apache.tomcat.util.http.ServerCookie.ALWAYS_ADD_EXPIRE` property in the `setenv` file, to add the `Expires` attribute to the headers:

* Linux

* Windows

In `$CATALINA_BASE/bin/setenv.sh`:

```bash
export CATALINA_OPTS="$CATALINA_OPTS -server -Xmx2g -XX:MetaspaceSize=256m -XX:MaxMetaspaceSize=256m \
-Dorg.apache.tomcat.util.http.ServerCookie.ALWAYS_ADD_EXPIRES=true"
```

In `$CATALINA_BASE/bin/setenv.bat`:

```powershell
set "CATALINA_OPTS=%CATALINA_OPTS% -server -Xmx2g -XX:MetaspaceSize=256m -XX:MaxMetaspaceSize=256m -
-Dorg.apache.tomcat.util.http.ServerCookie.ALWAYS_ADD_EXPIRES=true"
```

## Slashes in resource names

Some AM resources have names that can contain slash characters (`/`), for example, in policy names, application names, and SAML 2.0 entities. These slash characters can cause unexpected behavior when running AM on Tomcat.

Avoid resource names that contain forward slashes.

## Cookie domains

Set the cookie domain name value to an empty string (for *host-only* cookies) or to any non-top level domain (for *domain* cookies).

For example, if you install AM on `am.example.com`, you can set the cookie domain name to `example.com`.

|   |                                                                                                                                                                  |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Because host-only cookies are more secure than domain cookies, you *should* use host-only cookies unless you have a good business case for using domain cookies. |

You can find information on configuring the cookie domain during installation in [Install an instance](interactive-install.html#configure-openam-custom).

## Log request times

Tomcat provides components called valves that can be configured to track access to resources. The Access Log Valve outputs information about request activity to log files for you to analyze or use when troubleshooting.

To record request times in the Access Log Valve log, configure the `pattern` attribute to include the following values:

* `%D`: The time taken to send an entire request in milliseconds. This is the total processing time and may be affected by network conditions.

* `%F`: The time taken to commit the response in milliseconds.

Example `Valve` element in `server.xml`:

```bash
<Valve className="org.apache.catalina.valves.AccessLogValve" directory="logs"
       prefix="localhost_access_log" suffix=".txt"
       pattern="%h %l %u %t "%r" %s %b %D %F" />
```

You can find information about the Access Log Valve configuration in the [Tomcat documentation](https://tomcat.apache.org/tomcat-10.0-doc/config/valve.html#Access_Log_Valve), including the `%F` value.

## Encoding and security

You should edit the Tomcat `<Connector>` configuration to set `URIEncoding="UTF-8"`. UTF-8 URI encoding means the container can correctly decode URL-encoded characters in URI paths. This is particularly useful if your applications use the AM REST APIs and some identifiers, such as usernames, contain special characters.

You should also set the `protocols` property appropriately to define which protocols are supported. Make sure you don't support any unsafe protocols such as the SSL v3.0 protocol (`SSLv3`).

`<Connector>` configuration elements are found in the configuration file, `/path/to/tomcat/conf/server.xml`. The following excerpt shows an example `<Connector>` with the `URIEncoding` and `protocols` attributes set appropriately:

```xml
<Connector port="8443" protocol="HTTP/1.1"
                  SSLEnabled="true"
                  protocols="TLSv1.2,TLSv1.3"
                  maxThreads="150"
                  scheme="https"
                  secure="true"
                  clientAuth="false"
                  URIEncoding="UTF-8" />
```

When you have finished setting up Apache Tomcat, you *should* enforce HTTPS connections to AM. Learn more in [Secure connections to the AM container](configure-container-HTTPS.html).

---

---
title: Configure sites and add servers
description: Configure PingAM sites to group multiple servers together and add servers to sites for high availability behind a load balancer
component: pingam
version: 8.1
page_id: pingam:installation:configure-sites
canonical_url: https://docs.pingidentity.com/pingam/8.1/installation/configure-sites.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Install", "Deployment"]
page_aliases: ["install-guide:configure-sites.adoc"]
section_ids:
  configure-site-after-installation: Configure a site with the first server
  add-servers-to-site: Add a server to a site
---

# Configure sites and add servers

Sites group multiple AM servers together to provide services.

To configure a site, follow these high-level steps:

1. Install the first server in the site. This creates the configuration that the site will share.

   Learn more in [Interactive install](interactive-install.html).

2. Add the first server to a site if you didn't do this already during the installation.

   Learn more in [Configure a site with the first server](#configure-site-after-installation).

3. Add more servers to the site.

   Learn more in [Add a server to a site](#add-servers-to-site).

## Configure a site with the first server

The following steps show how to set up a site when AM is running:

1. Review AM's load balancing requirements in [Load balancing](../setup/configure-lb.html).

2. In the AM admin UI, go to Deployment > Sites.

3. Click Add a Site to start configuring the new site.

4. On the New Site page, enter the site name without any spaces. For example, the site name must be in the format `ExampleSite`, rather than `Example Site`.

   Set the Primary URL to the load balancer URL that's the entry point for the site, such as `https://lb.example.com/am`.

   The site URL is the URL to the load balancer in front of the AM servers in the site. For example, if your load balancer listens for HTTPS on host `lb.example.com` and port `443` with AM under `/am`, then your site URL is `https://lb.example.com/am`.

   Client applications and web or Java agents access the servers in the site through the site URL.

5. Click Save to keep the site configuration.

6. Configure the cookie domain of your site as required. Learn more in [Change the cookie domain](../security/changing-cookie-domain.html).

7. Go to Deployment > Servers > server name > General.

8. Set the Parent Site drop-down menu to the name of the site you just created, and save your changes.

   At this point, the first server is part of the new site you have configured.

   For all additional servers in the AM site, add them to the site at configuration time as described in [Add a server to a site](#add-servers-to-site).

## Add a server to a site

High availability requires redundant servers in case of failure. With AM, you configure an AM site with multiple servers in a pool behind a load balancing service that exposes a single URL as an entry point to the site.

Follow these steps to configure a server to an existing site:

1. Go to the deployment URL of the new instance to display the AM configurator page.

2. On the initial configuration page, click Create New Configuration.

3. Read the license agreement. Agree to the license agreement and click Continue.

4. On the Default User Password page, enter the same password you entered for the `amAdmin` administrator when you configured the first server in the site.

5. Configure server settings as required.

   The cookie domain must be identical to that of the first server in the site.

   |   |                                                                                                                                                                                |
   | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
   |   | You'll get a warning if the Configuration Directory isn't empty. If this happens, check that the directory you're trying to use doesn't contain any data you need to preserve. |

6. On the Configuration Data Store page, configure the same DS instance that is already used as the configuration store for the rest of the instances in the site, including the same encryption key.

   |   |                                                                                                                |
   | - | -------------------------------------------------------------------------------------------------------------- |
   |   | You can find the encryption key under Deployment > Servers > server name > Security > Password Encryption Key. |

   Make sure you also select the Additional server for existing deployment option.

7. On the Site Configuration page, select Yes, and enter the same Site Name and Load Balancer URL values as the existing servers in the site.

   |   |                                         |
   | - | --------------------------------------- |
   |   | Spaces aren't allowed in the site name. |

8. Check the details on the Configurator Summary page.

   * If anything needs changing, click Previous to return to earlier pages and update as needed.

   * If everything is correct, click Create Configuration to proceed.

9. When the configuration process completes, **stop** the newly-installed AM instance or the container where it runs, and don't try to access it.

10. Compare the `/path/to/am/config/boot.json` bootstrap file with that of a running instance. Make sure the newly installed instance's bootstrap file is appropriate for your environment.

    > **Collapse: The  file doesn't exist in the new instance**
    >
    > Depending on the configuration of the AM keystore in the site, the installation process might not create the bootstrap file.
    >
    > If not, copy the bootstrap file from another instance and continue with the procedure.

    Unless your environment has a requirement to configure the AM keystore in a different location on each instance, it's likely the bootstrap file will be the same across the site.

    If you are [overriding the start up settings](startup-openam.html#startup-openam-dynamic):

    * Make sure you have copied the customized bootstrap file from another instance in the site.

    * Make sure you are overwriting the existing bootstrap file with your modified file prior to every AM restart.

11. Make the existing AM keystore infrastructure available to the new instance:

    * Back up the new instance's default keystore and password files in the following locations:

      * `/path/to/am/security/keystores/`

      * `/path/to/am/security/secrets/default/`

    * Make sure the existing keystores in the site are available in the same location to the new instance. You might need to make changes, such as copying the keystores and their password files or mounting a volume.

    * Make sure the keystore files configured in the `/path/to/am/config/boot.json` file are available to the instance.

12. Make the existing secret store infrastructure in the site available to the new instance:

    * In the AM admin UI of an existing instance in the site, go to Configure > Secret Stores.

    * Review the list of secret stores configured globally and provide the relevant stores to the new instance. For example:

      * For keystore-type secret stores, copy the keystores to the same path on the new instance.

      * For filesystem-type secret stores, copy the contents of the directories to the same path or make the filesystem available on the same mount point on the new instance.

      * For HSM-type stores, make sure the new instance can access it.

      * For secrets configured as environment variables accessible by the container where AM runs, make sure they're also accessible by the container of the new instance.

    * Go to Realms > *realm name* > Secret Stores.

    * Review the list of secret stores configured per realm and make sure to provide the relevant stores to the new instance.

13. Restart the new instance.

    The instance is now configured for the site.

14. Review AM's load balancing requirements in [Load balancing](../setup/configure-lb.html).

15. Make sure the cookie domain configuration is appropriate for your site. Learn more in [Change the cookie domain](../security/changing-cookie-domain.html).

---

---
title: Customize the AM <code>.war</code> file
description: Customize PingAM extension points and user pages by adding classes and resources to the `.war` file before deployment
component: pingam
version: 8.1
page_id: pingam:installation:customize-openam
canonical_url: https://docs.pingidentity.com/pingam/8.1/installation/customize-openam.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Customization", "Install", "Deployment"]
page_aliases: ["install-guide:customize-openam.adoc"]
---

# Customize the AM `.war` file

For basic AM installations you don't need to customize the AM `.war` file before deploying it. If you need to customize any AM extension points, add the new classes to the `.war` file before deploying it.

|   |                                                                                                                               |
| - | ----------------------------------------------------------------------------------------------------------------------------- |
|   | Find information about customizing the secure cookie filter in [Secure cookie filter](../security/secure-cookie-filter.html). |

You can also [customize the AM user pages](../ui-customization/preface.html) and package them into the `.war` file.

Learn more about customizing the `.war` file in [Customize before upgrading](../upgrade/upgrade-planning.html#pre-upgrade-customization).

---

---
title: Delete and redeploy AM
description: Delete PingAM configuration files and redeploy the application to start the installation process from the beginning
component: pingam
version: 8.1
page_id: pingam:installation:start-over-install
canonical_url: https://docs.pingidentity.com/pingam/8.1/installation/start-over-install.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Install", "Backup &amp; Restore"]
page_aliases: ["install-guide:start-over-install.adoc"]
---

# Delete and redeploy AM

If you need to delete your configuration and start the process from the beginning, follow these steps:

1. Stop the AM web application to clear the configuration held in memory.

   The following example shuts down Apache Tomcat:

   ```bash
   $ /path/to/tomcat/bin/shutdown.sh
   Password:
   Using CATALINA_BASE:   /path/to/tomcat
   Using CATALINA_HOME:   /path/to/tomcat
   Using CATALINA_TMPDIR: /path/to/tomcat/temp
   Using JRE_HOME:        /path/to/jdk/jre
   Using CLASSPATH:
   /path/to/tomcat/bin/bootstrap.jar:/path/to/tomcat/bin/tomcat-juli.jar
   ```

2. Delete the AM configuration files, by default under the `$HOME` of the user running the web application container:

   ```bash
   $ rm -rf $HOME/am $HOME/.openamcfg
   ```

3. When installing or reinstalling a standalone AM instance, you must ensure the configuration store used does not contain previous configuration data.

   You should either install a new, clean instance of DS, or delete the entries under the configured AM suffix (by default `ou=am-config`) of an existing instance.

   Note that when adding a server to an existing deployment, you must not delete the configuration from DS, as it is shared by all servers in the deployment. See [Add a server to a site](configure-sites.html#add-servers-to-site).

4. Delete any cached files from the container.

   For example, on Tomcat, files are cached in a folder named after the deployment path, such as `/path/to/tomcat/work/Catalina/localhost/deployment path`. Use a command such as the following to delete these cached files:

   ```bash
   $ rm -rf /path/to/tomcat/work/Catalina/localhost/am
   ```

5. Restart the AM web application.

   The following example starts the Tomcat container:

   ```bash
   $ /path/to/tomcat/bin/startup.sh
   Password:
   Using CATALINA_BASE:   /path/to/tomcat
   Using CATALINA_HOME:   /path/to/tomcat
   Using CATALINA_TMPDIR: /path/to/tomcat/temp
   Using JRE_HOME:        /path/to/jdk/jre
   Using CLASSPATH:
   /path/to/tomcat/bin/bootstrap.jar:/path/to/tomcat/bin/tomcat-juli.jar
   ```

---

---
title: Deploy AM
description: Extract the WAR file into your application container to deploy PingAM before installation and configuration
component: pingam
version: 8.1
page_id: pingam:installation:deploy-openam
canonical_url: https://docs.pingidentity.com/pingam/8.1/installation/deploy-openam.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Install", "Deployment", "Topology"]
page_aliases: ["install-guide:deploy-openam.adoc"]
---

# Deploy AM

After you have downloaded AM software, deploy it to your installed application container.

Deploying AM only extracts the files into the application container, prior to installation and configuration. Deploying AM also makes LDIF files available, which can be used to prepare datastores for use with AM.

|   |                                                                                                                                                                                                                                                                                                                                                                      |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | After deploying AM, but before installation, your application container serves AM's installer (or upgrader, if performing an upgrade) user interfaces.We recommend that any external network access to the application container is suspended until the install, or upgrade, is complete. When complete, AM prevents access to the installer, or upgrader UI itself. |

The `AM-8.1.1.war` file contains the AM server. How you deploy the `.war` file depends on your web application container.

1. Deploy the `.war` file on your container.

   For example, copy the file to deploy on Apache Tomcat.

   ```
   $ cp AM-8.1.1.war /path/to/tomcat/webapps/am.war
   ```

   In development or demonstration deployments, change the `.war` file name to `am.war` when deploying in Tomcat, so that the deployment URI is `/am`.

   |   |                                                                                                                                                                                                                                                                                                                                                                                                                            |
   | - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | * Change the file name to something other than `am.war` when deploying to a production environment so the deployment URI isn't `/am`. Your deployment URI in production shouldn't disclose the kind of software it is hosting.

   * AM requires a deployment URI with a non-empty string after `/`. Don't deploy AM in the root context. For example, don't rename the `.war` file to `ROOT.war` before deploying on Tomcat. |

   It can take several seconds for AM to be deployed in your container.

2. Go to the initial configuration page. For example, `https://am.example.com:8443/am`.

   ![The initial configuration page lets you start configuring AM.](_images/openam-start.png)

   AM is now ready for installation.

3. You can now configure datastores using the files created during deployment. Learn more in [Prepare datastores](prepare-ext-stores.html).

---

---
title: Download AM
description: Download PingAM software packages including the complete distribution, WAR file, administrative tools, agents, and documentation
component: pingam
version: 8.1
page_id: pingam:installation:download-openam-software
canonical_url: https://docs.pingidentity.com/pingam/8.1/installation/download-openam-software.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Install"]
page_aliases: ["install-guide:download-openam-software.adoc"]
---

# Download AM

The [Ping Identity Download Center](https://backstage.pingidentity.com/downloads) hosts downloads, including a `.zip` file with all of the AM components, the `.war` file, AM tools, the configurator, web and Java agents, PingGateway, and documentation. Review the Software License and Subscription Agreement presented before you download AM files.

For each release of AM, you can download the entire package as a `.zip` file, only the AM `.war` file, or only the administrative tools as a `.zip` archive.

After you download the `.zip` file, create a new directory for AM, and unzip the `.zip` file to access the content.

```
$ cd ~/Downloads
$ mkdir am && cd am
$ unzip ~/Downloads/AM-8.1.1.zip
```

When you unzip the archive of the entire package, you get samples, snmp and legal-notices directories in addition to the following files:

**Distribution Files**

| File                           | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| ------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `AM-8.1.1.war`                 | The distribution `.war` file includes the core server code and an administrative graphical user interface (GUI) Web console.During installation, the `.war` file accesses properties to get the fully qualified domain name, port, context path, and the location of the configuration folder. These properties can be retrieved from the `boot.json` file in the AM installation directory, from environment variables, or from a combination of the two.This file is also available to download individually. |
| `AM-crypto-tool-8.1.1.war`     | A utility with some cryptographic functionality used for creating Docker images.	Strictly for future use, not currently supported.                                                                                                                                                                                                                                                                                                                                                                              |
| `Config-Upgrader-8.1.1.zip`    | Configuration file upgrade tool.Find more information on converting configuration files for import into AM in the `README.md` file in the `Config-Upgrader-8.1.1.zip` file.                                                                                                                                                                                                                                                                                                                                     |
| `Fedlet-8.1.1.zip`             | An AM Fedlet, a light-weight SAML 2.0 service provider.The Fedlet lets you set up a federated deployment without the need of a fully-featured service provider.                                                                                                                                                                                                                                                                                                                                                 |
| `IDPDiscovery-8.1.1.war`       | An IdP Discovery Profile (SAMLv2 binding profile) for its IdP Discovery service. The profile keeps track of the identity providers for each user.                                                                                                                                                                                                                                                                                                                                                               |
| `sample-trees-8.1.1.zip`       | Sample authentication trees for demonstration purposes. The trees are provided as JSON files and can be imported into an AM deployment using *Amster*. Find information on importing files using Amster in [Import configuration data](../amster/import-config.html).                                                                                                                                                                                                                                           |
| `Truststore-Utility-8.1.1.zip` | A utility to help with creating a trust store for use with web authentication.Find more information in the `readme.md` in the `.zip` archive and [MFA: Web authentication (WebAuthn) and passkeys](../am-authentication/authn-mfa-webauthn.html).                                                                                                                                                                                                                                                               |

---

---
title: IBM WebSphere Liberty
description: Deploy PingAM in IBM WebSphere Liberty by preparing the JVM, customizing the WAR file, and configuring WebSphere classloader and SOAP settings
component: pingam
version: 8.1
page_id: pingam:installation:prepare-ibm-websphere
canonical_url: https://docs.pingidentity.com/pingam/8.1/installation/prepare-ibm-websphere.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Install", "Web Container"]
page_aliases: ["install-guide:prepare-ibm-websphere.adoc"]
section_ids:
  prep-openam-for-websphere: Prepare AM for WebSphere
  prep-websphere-for-am: Prepare WebSphere
---

# IBM WebSphere Liberty

To deploy AM in IBM WebSphere Liberty, perform the following steps:

1. Update the JVM options as described in [Prepare the Java environment](prepare-java.html).

2. Customize the `AM-8.1.1.war` file as described in [Prepare AM for WebSphere](#prep-openam-for-websphere).

3. After deploying AM, configure WebSphere as described in [Prepare WebSphere](#prep-websphere-for-am).

## Prepare AM for WebSphere

To prepare AM to run in WebSphere, change the AM `.war` file to ensure that the AM upgrade process is able to find the AM configuration files. You must make this change whenever you deploy a new `.war` file as part of an AM upgrade.

|   |                                                                                                          |
| - | -------------------------------------------------------------------------------------------------------- |
|   | If you are installing on Windows, use slashes (`/`) in the paths listed here, and not backslashes (`\`). |

1. Create a temporary directory and expand the `AM-8.1.1.war` file. For example:

   ```bash
   $ cd /tmp
   $ mkdir /tmp/am && cd /tmp/am
   $ jar xvf ~/Downloads/AM-8.1.1.war
   ```

2. Locate the `bootstrap.properties` file in the `WEB-INF/classes` directory of the expanded `war` file.

   Update the `# configuration.dir=` line in the `bootstrap.properties` file to specify a path with read and write permissions. For example:

   ```properties
   # This property should also be used when the system user that
   # is running the web/application server process does not have
   # a home directory. i.e. System.getProperty("user.home") returns
   # null.

   configuration.dir=/my/readwrite/config/dir
   ```

3. Rebuild the `AM-8.1.1.war` file:

   ```bash
   $ jar cvf ../AM-8.1.1.war *
   ```

## Prepare WebSphere

In addition to preparing the AM `.war` file, follow these steps to configure WebSphere for AM *after you deploy AM into WebSphere*:

1. Load classes from AM bundled libraries before loading classes from libraries delivered with Liberty:

   * In the WebSphere Liberty administration console, go to Explore > Configure > server.xml.

   * Select the `am` web application, click Add Child, and select Classloader from the list.

   * In the Delegation field, select parentLast.

   * Save your work.

2. If your environment uses SOAP, add the SOAP-related properties to the JVM.

   In the `AM-config-dir`, create a file named `jvm.options`, and add the following properties:

   ```none
   -Djavax.xml.soap.MessageFactory=com.sun.xml.internal.messaging.saaj.soap.ver1_1.SOAPMessageFactory1_1Impl
   -Djavax.xml.soap.SOAPFactory=com.sun.xml.internal.messaging.saaj.soap.ver1_1.SOAPFactory1_1Impl
   -Djavax.xml.soap.SOAPConnectionFactory=com.sun.xml.internal.messaging.saaj.client.p2p.HttpSOAPConnectionFactory
   -Djavax.xml.soap.MetaFactory=com.sun.xml.internal.messaging.saaj.soap.SAAJMetaFactoryImpl
   -Dcom.ibm.websphere.webservices.DisableIBMJAXWSEngine=true
   ```

---

---
title: Install AM
description: Install PingAM instances in production or high-availability environments using interactive, passive, or site-based deployment methods
component: pingam
version: 8.1
page_id: pingam:installation:installing-instances
canonical_url: https://docs.pingidentity.com/pingam/8.1/installation/installing-instances.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Install", "Availability"]
page_aliases: ["install-guide:installing-instances.adoc"]
section_ids:
  install-high-availability: Install multiple instances for high availability
---

# Install AM

Production or production-like environments require a separate configuration store and CTS token store.

You can store the configuration in a DS server or in JSON files. File-based configuration (FBC) is best-suited to a DevOps-style deployment, with the associated tools and practices of that approach.

The CTS token store must be a DS server. If you store configuration in a DS server, AM stores CTS tokens there until you configure a separate LDAP store for them.

Learn more in [Prepare datastores](prepare-ext-stores.html).

The following table provides information to help you install AM instances:

| Task or requirement                                                                                                                                                                              | Resources                                                                                                                             |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------- |
| Configure an instance interactively in a production or pre-production environmentThis can be the first instance of a site deployment. Interactive installation assumes a DS configuration store. | [Interactive install](interactive-install.html)                                                                                       |
| Configure an instance without user interactionYou can install an instance passively with either a DS configuration or file-based configuration.                                                  | [Passive install](passive-install.html)                                                                                               |
| Configure an AM site and add an instance to the siteA *site* lets you group multiple AM servers.                                                                                                 | [Install multiple instances for high availability](#install-high-availability)[Configure sites and add servers](configure-sites.html) |

## Install multiple instances for high availability

Install multiple instances to maintain service availability. If one instance is down for any reason, another instance can respond instead. This means you need some type of component, such as a load balancer or a proxy server, between incoming traffic and AM to route around instances that are down.

AM uses a *site* for this purpose. In an AM site, multiple AM instances are configured in the same way, and accessed through a load balancer layer.

The load balancer can be implemented in hardware or software, but it is separate and independent from AM. When installed properly, a site configuration improves service availability, because the load balancer routes around AM instances that are down, sending traffic to other servers in the site.

You can find high-level deployment information in [Deployment planning](../deployment-planning/preface.html).

|   |                                                                                                                                                      |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | If you need to delete your AM configuration entirely and start again, you can find information in [Delete and redeploy AM](start-over-install.html). |

---

---
title: Installation
description: Install PingAM for access and federation management
component: pingam
version: 8.1
page_id: pingam:installation:preface
canonical_url: https://docs.pingidentity.com/pingam/8.1/installation/preface.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Install"]
page_aliases: ["index.adoc", "release-notes:preface.adoc", "install-guide:preface.adoc"]
---

# Installation

This guide shows you how to install PingAM for access and federation management.

Unless you are planning a demo or test installation, read the [Release notes](https://docs.pingidentity.com/pingam/release-notes) before you get started.

[icon: th-list, set=fad, size=3x]

#### [Prepare the environment for deployment](prepare-env-install.html)

Prerequisites for deploying PingAM software.

[icon: copy, set=fad, size=3x]

#### [Prepare the Java container](prepare-containers.html)

Prepare the application server of your choice.

[icon: cogs, set=fad, size=3x]

#### [Install AM](installing-instances.html)

Install AM servers for high availability.

[icon: cubes, set=fad, size=3x]

#### [Prepare datastores](prepare-ext-stores.html)

Store identities, configuration, CTS, policies and applications, and UMA-related data in LDAP directories.

[icon: files, set=fad, size=3x]

#### [Store configuration in files](fbc.html)

Store configuration data in JSON files.

[icon: times, set=fad, size=3x]

#### [Remove installations](removing-instances.html)

Uninstall AM and start over.

[icon: ambulance, set=fad, size=3x]

#### [Troubleshoot installations](install-troubleshooting.html)

Troubleshoot or repair an AM installation.

---

---
title: Interactive install
description: Customize PingAM deployment parameters during interactive installation, including cookie domain, configuration datastore, and user datastore settings
component: pingam
version: 8.1
page_id: pingam:installation:interactive-install
canonical_url: https://docs.pingidentity.com/pingam/8.1/installation/interactive-install.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Install"]
page_aliases: ["install-custom.adoc", "install-guide:interactive-install.adoc"]
---

# Interactive install

During interactive installation, you customize the parameters of the AM deployment, such as the cookie domain and the settings of the configuration and datastores.

* Installing the first instance creates the required configuration that the site will share.

  You can specify the site configuration when you install the first instance or configure the site when the first instance is running.

* By default, the cookie domain is set to the full URL of the first instance; for example, `server.west.example.com`.

  You can change the cookie domain when you're installing the first instance or later.

* You can use a load balancer layer to protect AM services. The load balancer can restrict access to AM services, throttle traffic, offload HTTPS encryption, and so forth.

  As an alternative, or in addition, you can use a separate reverse proxy.

* When you are protecting AM with a load balancer or proxy service, configure your container so that AM can trust the load balancer or proxy service.

* The container for each instance in the site must trust any certificate authorities (CA) used to sign certificates used by other instances in the site to communicate using SSL.

* Successful authentication can depend on information about the authenticating user, such as the IP address where the request originated. When AM is accessed through a load balancer or proxy layer, pass this information along using request headers. Also, configure AM to consume and to forward the headers as necessary. Learn more in [Handle HTTP request headers](../setup/configure-lb.html#handle-request-headers).

Follow these steps to install a single AM instance, or to install the first instance on a site.

1. Go to your deployment URL. For example, `https://am.example.com:8443/am`.

2. On the initial configuration page, click Create New Configuration.

3. Read the license agreement. Agree to the license agreement and click Continue.

4. On the Default User Password page, provide a password with at least eight characters for the AM Administrator, `amAdmin`.

5. Verify that the server settings are valid for your configuration.

   * Server URL

     Provide a valid URL to the base of your AM web container, including an FQDN.

     In a test or QA environment, you can simulate the FQDN by adding it to your `/etc/hosts` as an alias. The following example shows lines from the `/etc/hosts` file on a Linux system where AM is installed:

     ```none
     127.0.0.1 localhost.localdomain localhost
     ::1 localhost6.localdomain6 localhost6
     127.0.1.1 am am.example.com
     ```

   * Cookie Domain

     The domain for which created cookies will be valid. For example `example.com`.

   * Platform Locale

     The platform locale of your server. Supported locales include en\_US (English), de (German), es (Spanish), fr (French), ja (Japanese), ko (Korean), zh\_CN (Simplified Chinese), and zh\_TW (Traditional Chinese).

   * Configuration Directory

     The directory to use for configuration files. AM must be able to write to this directory.

     By default, the configuration directory is located in `$HOME/am`, where $HOME corresponds to the user who runs the web container.

6. On the Configuration Data Store page, you can configure options related to AM configuration data.

   The installation process stores AM configuration data in an existing DS server. You must have prepared the server as explained in [Prepare a configuration store](prepare-configuration-store.html).

   * SSL/TLS Enabled

     Select this option to use LDAPS to communicate with the configuration store. DS is configured for LDAPS by default.

     Before proceeding, make sure you have shared the DS certificate with the container where AM is running. Learn more in [Prepare the truststore](prepare-trust-store.html).

   * Host Name

     The FQDN of the DS server.

   * Port

     The LDAPS port of the DS server.

   * Encryption Key

     A randomly generated key that AM uses for different purposes. All the servers in the site must have the same encryption key.

     The installer creates a random key automatically, which you can use.

   * Root Suffix

     The root suffix of the DS store.

     The default base DN of a DS store when you configure it with the `am_config` profile is `ou=am-config`.

   * Login ID

     The bind DN to use to connect to the DS store.

     The default bind DN of a DS store when you configure it with the `am_config` profile is `uid=am-config,ou=admins,ou=am-config`.

     Don't use `cn=admin` as the bind account.

   * Password

     The password for the bind DN.

   * Server configuration

     * New deployment

       The installation is a new deployment, with its own configuration and identity stores.

       If you choose this option, the next step is to configure the identity store.

     * Additional server for existing deployment

       The installation is an additional server for an existing deployment, which uses the existing configuration and identity stores.

       If you choose this option, you don't need to configure the identity store. The installation uses the same stores as those of the existing deployment.

       Learn more in [Add a server to a site](configure-sites.html#add-servers-to-site).

7. If you specified New deployment in the previous step, the User Data Store page appears as the next step. Use this page to configure where AM looks for identities.

   AM must have write access to the directory service you choose, because it adds to the directory schema needed to allow AM to manage identity profiles in the identity store.

   * User Data Store Type

     If you have already provisioned a directory service with identities in a supported identity store, then select that type of directory from the options available.

   * SSL/TLS Enabled

     Select this option to use a secure connection. When using this option, make sure the trust store used by the JVM running AM has the necessary certificates installed. Learn more in [Prepare the truststore](prepare-trust-store.html).

   * Directory Name

     The FQDN of the identity store.

   * Port

     The LDAPS port of the identity store. Make sure the port you define corresponds to the port the directory server listens to for StartTLS or SSL connections.

   * Root Suffix

     The base DN of the identity store.

     If you installed PingDS with the `am-identity-store` profile, the base DN is `ou=identities`.

   * Login ID

     The directory administrator user DN. The administrator must be able to update the schema and identity profiles.

     If you installed PingDS with the `am-identity-store` profile, the bind DN to use here is `uid=am-identity-bind-account,ou=admins,ou=identities`.

   * Password

     The password for the directory administrator user.

     If you installed PingDS with the `am-identity-store` profile, this password is the one you set with `am-identity-store/amIdentityStoreAdminPassword`.

8. On the Site Configuration page, you can set up AM as part of a site where the load is balanced across multiple AM servers.

   When you deploy multiple servers, AM automatically enables session high availability.(1) AM stores session data in a directory service that is shared by multiple AM servers. The shared storage means that if an AM server fails, other AM servers in the deployment have access to the user's session data and can serve requests about that user. As a result, the user doesn't have to log in again.

   You can also set up a site after initial installation and configuration. Learn more in [Configure a site with the first server](configure-sites.html#configure-site-after-installation).

9. Check the details on the Configurator Summary page.

   * If anything needs changing, click Previous to return to earlier pages and update as needed.

   * If everything is correct, click Create Configuration to proceed. The configuration progress is shown in the browser and also output to the installation log.

10. When the configuration process completes, click Proceed to Login, and log in as the `amAdmin` administrator.

    After logging in, the Realms page is displayed.

11. Restrict permissions to the configuration directory to prevent other users accessing configuration files.

12. The AM install wizard uses four libraries that should be removed after installation for security reasons.

    When your installation is complete, remove the following .jar files from the `WEB-INF/lib` directory:

    * `click-extras-2.3.0.jar`

    * `click-nodeps-2.3.0.jar`

    * `ognl-3.2.10.jar`

    * `velocity-1.7.jar`

    |   |                                                                                                                               |
    | - | ----------------------------------------------------------------------------------------------------------------------------- |
    |   | These files are used *only* by the install and upgrade wizards. Removing them will have no effect on your installed instance. |

    You must also remove the references to `click-servlet` from the deployment descriptor file. Edit `/path/to/tomcat/webapps/am/WEB-INF/web.xml` to remove the following mappings:

    ```xml
    <servlet>
        <servlet-name>click-servlet</servlet-name>
        <servlet-class>org.apache.click.ClickServlet</servlet-class>
    </servlet>

    ...

    <servlet-mapping>
        <servlet-name>click-servlet</servlet-name>
        <url-pattern>*.htm</url-pattern>
    </servlet-mapping>
    ```

13. Review the suggested [next steps](post-install.html) after installing AM.

(1) You can configure AM to store sessions in the [Core Token Service (CTS) token store](../cts/preface.html) or on the client. Because [client-side](../am-sessions/client-based-sessions.html) sessions reside in HTTP cookies, they don't need to be retrieved from a persistent datastore. In the event of a server failure, they can be retrieved from the cookies. AM doesn't store client-side sessions in the CTS token store. You can find details about sessions in [Introduction to sessions](../am-sessions/about-sessions.html).

---

---
title: JBoss and WildFly
description: Prepare JBoss, JBoss EAP, and WildFly application servers to deploy PingAM, and configure the PingAM WAR archive for these environments
component: pingam
version: 8.1
page_id: pingam:installation:prepare-jboss
canonical_url: https://docs.pingidentity.com/pingam/8.1/installation/prepare-jboss.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Install", "Web Container"]
page_aliases: ["install-guide:prepare-jboss.adoc"]
section_ids:
  prep-jboss-for-openam: Prepare JBoss or WildFly
  prep-openam-for-jboss: Prepare AM for JBoss and WildFly
---

# JBoss and WildFly

You can deploy AM on JBoss AS, JBoss EAP, and WildFly. The procedures listed here provide steps for configuring JBoss AS, JBoss EAP, and WildFly for AM.

After configuring JBoss or WildFly, you then prepare AM for deployment by making changes to the contents of the AM `.war` archive.

## Prepare JBoss or WildFly

1. Stop JBoss or WildFly.

2. The default JVM settings don't allocate enough memory to AM. This step shows one method you can use to modify the JVM settings. You can find other methods in JBoss [Configuring JVM Settings](https://docs.redhat.com/en/documentation/red_hat_jboss_enterprise_application_platform/8.1/html/configuration_guide/configuring-jvm-settings_default) or WildFly [JVM Settings](https://docs.jboss.org/author/display/WFLY/JVM%20settings.html).

   * Open the `standalone.conf` file in the `/path/to/jboss/bin` directory for JBoss or WildFly in standalone mode.

   * Check the JVM settings associated with `JAVA_OPTS`.

     Change the JVM heap size to `-Xmx2g`. The default JVM heap size for some versions of JBoss might already exceed the recommended value.

     Change the metaspace size to `-XX:MaxMetaspaceSize=256m` if the default size doesn't exceed this amount.

   * Set one of the following JVM `JAVA_OPTS` settings in the same file depending on which web application container you're preparing:

     * JBoss:

       ```none
       -Dorg.apache.tomcat.util.http.ServerCookie.ALWAYS_ADD_EXPIRES=true
       ```

       Make sure the headers include the `Expires` attribute in addition to `Max-Age` because some versions of Microsoft Edge don't support `Max-Age`.

     * WildFly:

       ```none
       -Dio.undertow.legacy.cookie.ALLOW_HTTP_SEPARATORS_IN_V0=true
       ```

3. Edit the WildFly configuration to allow HTTP connections from any IP address.

   In the `/path/to/wildfly/standalone/configuration/standalone.xml` file, locate the `<interface name="public">` interface (around line 512 of the file) and change the value to `<any-address/>`:

   ```xml
   <interface name="public">
      <any-address/>
   </interface>
   ```

4. Set up WildFly for Social Authentication by performing the following steps:

   * Ensure the WildFly server is running.

   * Go to the WildFly Path.

   * In the `$JBOSS_HOME/bin` directory, run the `jboss-cli.sh` script file:

     ```bash
     $ ./bin/jboss-cli.sh
     ```

   * Type "connect" to connect to the server.

   * Enable use of the equals (`=`) symbol in cookies by running the following command:

     For example:

     ```none
     [standalone@localhost:9990 /] /subsystem=undertow/server=default-server/
     http-listener=default:write-attribute(name=allow-equals-in-cookie-value,
     value=true)
     {
        "outcome" => "success",
        "response-headers" => {
           "operation-requires-reload" => true,
           "process-state" => "reload-required"
         }
     }
     ```

   * Restart WildFly.

5. Deploy the `am.war` file into the appropriate deployment directory. The directory varies depending on whether you're running in standalone or domain mode.

## Prepare AM for JBoss and WildFly

To prepare AM to run with JBoss or WildFly, you must change the default AM `war` file. JBoss and WildFly deploy applications from different temporary directories every time you restart the container, which would require reconfiguring AM. To avoid problems, change the AM `war` file as follows:

1. If you haven't already done so, create a temporary directory and expand the `AM-8.1.1.war` file. For example:

   ```bash
   $ cd /tmp
   $ mkdir /tmp/am && cd /tmp/am
   $ jar xvf ~/Downloads/AM-8.1.1.war
   ```

2. Locate the `bootstrap.properties` file in the `WEB-INF/classes` directory of the expanded `war` archive. Update the `# configuration.dir=` line in this file to specify a path with read and write permissions, then save the change.

   ```properties
   # This property should also be used when the system user that
   # is running the web/application server process does not have
   # a home directory. i.e. System.getProperty("user.home") returns
   # null.

   configuration.dir=/my/readwrite/config/dir
   ```

3. If you are deploying AM on JBoss AS or JBoss EAP, remove the `jboss-all.xml` file from the `WEB-INF` directory of the expanded `war` archive.

   Don't remove this file if you are deploying AM on WildFly.

4. Rebuild the `am.war` file.

   ```bash
   $ jar cvf ../am.war *
   ```

---

---
title: Next steps
description: Complete essential PingAM configuration tasks after installation, including realm setup, authentication trees, security hardening, and federation features
component: pingam
version: 8.1
page_id: pingam:installation:post-install
canonical_url: https://docs.pingidentity.com/pingam/8.1/installation/post-install.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Install"]
page_aliases: ["install-guide:post-install.adoc"]
---

# Next steps

Congratulations on installing AM!

The following list shows you different tasks to consider after installing AM:

* Core administrative tasks

  * Log in to the AM admin UI.

  * Learn about the administration command-line tools.

  * Learn about realms, configure them, and connect them to identity stores.

  * Configure AM's cookie domain.

  * Learn about other types of configuration stores and decide if your environment would benefit from having dedicated application stores.

    Find more information in [Setup and configuration](../setup/preface.html).

* Core Token Service tasks

  * Learn about the Core Token Service and decide if your environment would benefit from having dedicated CTS token stores.

    Find more information in [Core Token Service (CTS)](../cts/preface.html).

* Access Management-related tasks

  * Learn about authentication trees and nodes and configure them to let your users log in to AM.

  * Learn about sessions in AM and configure them for your environment.

    Find more information in [Authentication and SSO](../am-authentication/preface.html).

* Security-related tasks

  * Secure your core AM environment against different threats.

  * Configure keys and keystores used for different AM features.

  * Change the `amAdmin` user password.

  * Learn about delegated privileges and configure delegated realm administrators.

  * Configure audit logging services.

    Find more information in [Security](../security/preface.html).

* Maintenance-related tasks

  * Learn how to back up and restore your environment.

  * Learn how to monitor your AM instances.

  * Learn how to enable debug logging and how to record troubleshooting information.

  * Tune AM.

    Find more information in [Maintenance](../maintenance/preface.html).

* Federation

  AM offers authentication and authorization functionality which you can expand with Internet specifications and drafts, such as OAuth 2.0, and SAML 2.0.

  When you're confident about your base AM configuration, move on to more advanced features such as protecting web applications, configuring single sign-on (SSO), federating access across applications, and others.

  Find more information in [OAuth 2.0](../am-oauth2/preface.html), [OpenID Connect 1.0](../am-oidc1/preface.html), and [SAML 2.0](../am-saml2/preface.html).

---

---
title: Passive install
description: Set up PingAM with minimal user intervention using JSON files, REST API, or Amster
component: pingam
version: 8.1
page_id: pingam:installation:passive-install
canonical_url: https://docs.pingidentity.com/pingam/8.1/installation/passive-install.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Install", "Silent install", "Non-interactive install"]
page_aliases: ["install-guide:passive-install.adoc"]
---

# Passive install

Passive installation, also called non-interactive or silent installation, lets you set up AM with minimal user intervention.

There are three methods of installing AM passively:

[icon: files, set=fad, size=3x]

#### [Passive install with FBC](passive-install-fbc.html)

Set up AM to read its configuration from JSON files.

[icon: gears, set=fad, size=3x]

#### [Passive install over REST](passive-install-rest.html)

Configure AM using the REST API.

[icon: wrench, set=fad, size=3x]

#### [Passive install using Amster](passive-install-amster.html)

Configure AM with Amster.

File-based configuration (FBC) is best-suited to a DevOps-style deployment, with the associated tools and practices of that approach.

Learn more in [Deployment configuration locations](../deployment-planning/deploy-configuration-types.html).

---

---
title: Passive install over REST
description: Use the REST API to install PingAM with minimal user interaction by sending a POST request to the /config/configurator endpoint
component: pingam
version: 8.1
page_id: pingam:installation:passive-install-rest
canonical_url: https://docs.pingidentity.com/pingam/8.1/installation/passive-install-rest.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
page_aliases: ["silent-install.adoc", "install-guide:passive-install-configurator.adoc", "passive-install-configurator.adoc"]
section_ids:
  examples: Examples
  install_a_standalone_server: Install a standalone server
  install_two_servers_in_a_site_configuration: Install two servers in a site configuration
  config-properties: Configuration properties
---

# Passive install over REST

Use the REST API to install AM with minimal user interaction. The AM server must be deployed and running *but not yet configured*.

Send a `POST` request to the `/config/configurator` endpoint with the configuration properties. You can find a list of valid properties in [Configuration properties](#config-properties).

## Examples

These examples assume you have a DS instance up and running, and that the instance has been installed as a [configuration store](https://docs.pingidentity.com/pingds/8.1/install-guide/profile-am-config.html), [identity store](https://docs.pingidentity.com/pingds/8.1/install-guide/profile-am-idrepo.html), and [CTS store](https://docs.pingidentity.com/pingds/8.1/install-guide/profile-am-cts.html).

|   |                                                                                                                                                                                    |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | You can find information on setting up an evaluation DS server that stores all three data types in [Step 2. Prepare your datastore](../evaluation/step-2-prepare-data-store.html). |

### Install a standalone server

```bash
$ curl \
--request POST \
--header "Content-Type: application/x-www-form-urlencoded" \
--data-urlencode "SERVER_URL=https://am.example.com:8443" \
--data-urlencode "DEPLOYMENT_URI=/am" \
--data-urlencode "BASE_DIR=$HOME/am" \
--data-urlencode "locale=en_US" \
--data-urlencode "PLATFORM_LOCALE=en_US" \
--data-urlencode "ADMIN_PWD=Ch4ng31t" \
--data-urlencode "ADMIN_CONFIRM_PWD=Ch4ng31t" \
--data-urlencode "COOKIE_DOMAIN=am.example.com" \
--data-urlencode "acceptLicense=true" \
--data-urlencode "DATA_STORE=dirServer" \
--data-urlencode "DIRECTORY_SSL=SSL" \
--data-urlencode "DIRECTORY_SERVER=ds.example.com" \
--data-urlencode "DIRECTORY_PORT=1636" \
--data-urlencode "DIRECTORY_ADMIN_PORT=4444" \
--data-urlencode "ROOT_SUFFIX=ou=am-config" \
--data-urlencode "DS_DIRMGRDN=uid=am-config,ou=admins,ou=am-config" \
--data-urlencode "DS_DIRMGRPASSWD=Ch4ng31t" \
--data-urlencode "USERSTORE_TYPE=LDAPv3ForOpenDS" \
--data-urlencode "USERSTORE_SSL=SSL" \
--data-urlencode "USERSTORE_HOST=ds.example.com" \
--data-urlencode "USERSTORE_PORT=1636" \
--data-urlencode "USERSTORE_SUFFIX=ou=identities" \
--data-urlencode "USERSTORE_MGRDN=uid=am-identity-bind-account,ou=admins,ou=identities" \
--data-urlencode "USERSTORE_PASSWD=Ch4ng31t" \
"https://am.example.com:8443/am/config/configurator"

Configuration complete!
```

### Install two servers in a site configuration

Install the first server. The REST call is the same as for a standalone server install, with the addition of the `AM_ENC_KEY` property and the site properties (`LB_SITE_NAME` and `LB_PRIMARY_URL`):

```bash
$ curl \
--request POST \
--header "Content-Type: application/x-www-form-urlencoded" \
--data-urlencode "SERVER_URL=https://am.example.com:8443" \
--data-urlencode "DEPLOYMENT_URI=/am" \
--data-urlencode "BASE_DIR=$HOME/am" \
--data-urlencode "locale=en_US" \
--data-urlencode "PLATFORM_LOCALE=en_US" \
--data-urlencode "AM_ENC_KEY=O6QWwHPO4os+zEz3Nqn/2daAYWyiFE32" \
--data-urlencode "ADMIN_PWD=Ch4ng31t" \
--data-urlencode "ADMIN_CONFIRM_PWD=Ch4ng31t" \
--data-urlencode "COOKIE_DOMAIN=am.example.com" \
--data-urlencode "acceptLicense=true" \
--data-urlencode "DATA_STORE=dirServer" \
--data-urlencode "DIRECTORY_SSL=SSL" \
--data-urlencode "DIRECTORY_SERVER=ds.example.com" \
--data-urlencode "DIRECTORY_PORT=1636" \
--data-urlencode "DIRECTORY_ADMIN_PORT=4444" \
--data-urlencode "ROOT_SUFFIX=ou=am-config" \
--data-urlencode "DS_DIRMGRDN=uid=am-config,ou=admins,ou=am-config" \
--data-urlencode "DS_DIRMGRPASSWD=Ch4ng31t" \
--data-urlencode "USERSTORE_TYPE=LDAPv3ForOpenDS" \
--data-urlencode "USERSTORE_SSL=SSL" \
--data-urlencode "USERSTORE_HOST=ds.example.com" \
--data-urlencode "USERSTORE_PORT=1636" \
--data-urlencode "USERSTORE_SUFFIX=ou=identities" \
--data-urlencode "USERSTORE_MGRDN=uid=am-identity-bind-account,ou=admins,ou=identities" \
--data-urlencode "USERSTORE_PASSWD=Ch4ng31t" \
--data-urlencode "LB_SITE_NAME=lb" \
--data-urlencode "LB_PRIMARY_URL=https://lb.example.com:8443/am" \
"https://am.example.com:8443/am/config/configurator"

Configuration complete!
```

Install the second server. Make sure the `AM_ENC_KEY` and site properties match those used for the first server:

```bash
$ curl \
--request POST \
--header "Content-Type: application/x-www-form-urlencoded" \
--data-urlencode "SERVER_URL=https://am2.example.com:8443" \
--data-urlencode "DEPLOYMENT_URI=/am" \
--data-urlencode "BASE_DIR=$HOME/am" \
--data-urlencode "locale=en_US" \
--data-urlencode "PLATFORM_LOCALE=en_US" \
--data-urlencode "AM_ENC_KEY=O6QWwHPO4os+zEz3Nqn/2daAYWyiFE32" \
--data-urlencode "ADMIN_PWD=Ch4ng31t" \
--data-urlencode "ADMIN_CONFIRM_PWD=Ch4ng31t" \
--data-urlencode "COOKIE_DOMAIN=am.example.com" \
--data-urlencode "acceptLicense=true" \
--data-urlencode "DATA_STORE=dirServer" \
--data-urlencode "DIRECTORY_SSL=SSL" \
--data-urlencode "DIRECTORY_SERVER=ds.example.com" \
--data-urlencode "DIRECTORY_PORT=1636" \
--data-urlencode "DIRECTORY_ADMIN_PORT=4444" \
--data-urlencode "ROOT_SUFFIX=ou=am-config" \
--data-urlencode "DS_DIRMGRDN=uid=am-config,ou=admins,ou=am-config" \
--data-urlencode "DS_DIRMGRPASSWD=Ch4ng31t" \
--data-urlencode "USERSTORE_TYPE=LDAPv3ForOpenDS" \
--data-urlencode "USERSTORE_SSL=SSL" \
--data-urlencode "USERSTORE_HOST=ds.example.com" \
--data-urlencode "USERSTORE_PORT=1636" \
--data-urlencode "USERSTORE_SUFFIX=ou=identities" \
--data-urlencode "USERSTORE_MGRDN=uid=am-identity-bind-account,ou=admins,ou=identities" \
--data-urlencode "USERSTORE_PASSWD=Ch4ng31t" \
--data-urlencode "LB_SITE_NAME=lb" \
--data-urlencode "LB_PRIMARY_URL=https://lb.example.com:8443/am" \
"https://am2.example.com:8443/am/config/configurator"

Configuration complete!
```

## Configuration properties

The following table lists the configuration properties that you can set when installing AM over REST.

| Property name          | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | Example values                                         |
| ---------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------ |
| SERVER\_URL            | The protocol, fully qualified domain name, and port to use for the AM server instance.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | `https://am.example.com:8443`                          |
| DEPLOYMENT\_URI        | The deployment URI to use for the AM server instance.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | `/am`                                                  |
| BASE\_DIR              | The configuration directory where AM stores files.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | `$HOME/am`                                             |
| locale                 | The user locale.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | `en_GB`                                                |
| PLATFORM\_LOCALE       | The locale of the AM server instance.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | `en_US`                                                |
| AM\_ENC\_KEY           | The password encryption key, which must be the same on all servers in a site configuration.If this property is excluded, AM generates a random password encryption key on install that you can view in the AM admin UI, under Deployment > Servers > *server name* > Security.                                                                                                                                                                                                                                                                                                                                        | `O6QWwHPO4os+zEz3Nqn/2daAYWyiFE32`                     |
| ADMIN\_PWD             | The password of the AM administrator user `amAdmin`, which must be at least 8 characters in length and must be the same on all servers in a site configuration.                                                                                                                                                                                                                                                                                                                                                                                                                                                       | `Ch4ng31t`                                             |
| ADMIN\_CONFIRM\_PWD    | Confirmation of the `amAdmin` password.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | `Ch4ng31t`                                             |
| COOKIE\_DOMAIN         | The name of the trusted DNS domain AM returns to a browser when it grants a session ID to a user.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | `am.example.com`                                       |
| acceptLicense          | Set this to `true` to auto-accept the software license agreement, which suppresses the display of the license acceptance page during the install.                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | `true`                                                 |
| DATA\_STORE            | Set this to `dirServer` to indicate an external PingDS directory server for the configuration store.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | `dirServer`                                            |
| DIRECTORY\_SSL         | Set this to `SSL` to use LDAP with SSL. DS is configured for LDAPS by default. To use LDAP without SSL, set this to `SIMPLE`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | `SSL`                                                  |
| DIRECTORY\_SERVER      | The fully qualified domain name of the configuration store directory server host.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | `ds.example.com`                                       |
| DIRECTORY\_PORT        | The LDAPS or LDAP port number for the configuration store directory server.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | `1636`                                                 |
| DIRECTORY\_ADMIN\_PORT | The administration port number for the configuration store directory server.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | `4444`                                                 |
| ROOT\_SUFFIX           | The root suffix distinguished name (DN) for the configuration store.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | `ou=am-config`                                         |
| DS\_DIRMGRDN           | The bind DN of the configuration store user account.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | `uid=am-config,ou=admins,ou=am-config`                 |
| DS\_DIRMGRPASSWD       | The password for the bind DN.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | `Ch4ng31t`                                             |
| USERSTORE\_TYPE        | The type of directory server to use for the identity store.Possible values are:- `LDAPv3ForAD`: Active Directory with host and port settings

- `LDAPv3ForADDC`: Active Directory with domain name setting

  If you use this type, you must also set the `USERSTORE_DOMAINNAME` property.

- `LDAPv3ForADAM`: Active Directory Lightweight Directory Services (AD LDS)

- `LDAPv3ForForgeRockIAM`: PingDS

  Only use this type if DS is the shared identity store in a Ping Identity Platform deployment. Otherwise, use `LDAPv3ForOpenDS`.

- `LDAPv3ForOpenDS`: PingDS

- `LDAPv3ForPingDirectory`: PingDirectory | `LDAPv3ForOpenDS`                                      |
| USERSTORE\_DOMAINNAME  | If `USERSTORE_TYPE` is `LDAPv3ForADDC`, set this to the Active Directory Domain Name. Then only set the `USERSTORE_SSL`, `USERSTORE_MGRDN`, and `USERSTORE_PASSWD` properties to let Active Directory use DNS to retrieve service locations. Otherwise, don't set this property.                                                                                                                                                                                                                                                                                                                                      | `ad.example.com`                                       |
| USERSTORE\_SSL         | Set this to `SSL` to use LDAP with SSL. DS is configured for LDAPS by default. To use LDAP without SSL, set this to `SIMPLE`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | `SSL`                                                  |
| USERSTORE\_HOST        | The fully qualified domain name of the identity store directory server.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | `ds.example.com`                                       |
| USERSTORE\_PORT        | The LDAPS or LDAP port number for the identity store directory server.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | `1636`                                                 |
| USERSTORE\_SUFFIX      | The root suffix DN for the identity store.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | `ou=identities`                                        |
| USERSTORE\_MGRDN       | The bind DN of the identity store user account.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | `uid=am-identity-bind-account,ou=admins,ou=identities` |
| USERSTORE\_PASSWD      | The password for the bind DN.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | `Ch4ng31t`                                             |
| LB\_SITE\_NAME         | The name of the AM site. Required when installing a server as part of a site configuration.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | `lb`                                                   |
| LB\_PRIMARY\_URL       | The load balancer URL for the site. Required when installing a server as part of a site configuration.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | `https://lb.example.com:8443/am`                       |

---

---
title: Passive install using Amster
description: Use Amster to configure a deployed PingAM instance as a standalone server or within a site with external configuration and identity stores
component: pingam
version: 8.1
page_id: pingam:installation:passive-install-amster
canonical_url: https://docs.pingidentity.com/pingam/8.1/installation/passive-install-amster.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
page_aliases: ["user-guide:amster-install-am.adoc", "amster:configure-am-with-amster.adoc"]
section_ids:
  install-am-examples: Examples
  example_1_standalone_server: "Example 1: Standalone server"
  example_2_two_servers_in_a_site: "Example 2: Two servers in a site"
  install-am-options: Configuration options
  am-post-install-steps-sites: Post-installation steps for site deployments
  amster-troubleshooting-am-install: Troubleshoot AM installations
---

# Passive install using Amster

Use Amster to configure a deployed AM instance as either a single, standalone server or as a server within a site.

Amster configures AM to use an external configuration store and identity store.

|   |                                                                                                                                                                          |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | You can't use Amster to install PingAM in file-based configuration (FBC) mode. Instead, follow the instructions in [Passive install with FBC](passive-install-fbc.html). |

To configure AM with Amster, run the `install-openam` command:

**Usage:**

```
am> install-openam \
 --serverUrl protocol://FQDN:port/URI \
 --adminPwd amAdmin_password \
   [options]
```

* `--serverUrl protocol://FQDN:port/URI`

  The protocol, URL, port, and deployment URI of the AM instance. For example, `https://am.example.com:8443/am`.

* `--adminPwd amAdmin-password`

  The password of the `amAdmin` user. If the `--cfgStoreDirMgrPwd` option is not specified, this value is also the password of the configuration store's directory manager user.

  The password must be at least 8 characters in length.

**Options:**

* `[options]`

  Use these optional parameters to configure properties like the cookie domain, ports, and passwords for the configuration store.

  To see all available options, run the `:help install-openam` command or read [Configuration options](#install-am-options).

## Examples

Before you start, make sure your AM instance is deployed and running, but not yet configured. Learn more in [Deploy AM](deploy-openam.html).

Before you run the `amster` command, you must create a truststore for AM, and prepare the external configuration and identity stores. Learn more in [Prepare datastores](prepare-ext-stores.html).

You can't install AM with an external configuration store that already contains configuration data, unless you're adding a server to an existing site.

|   |                                                                                                           |
| - | --------------------------------------------------------------------------------------------------------- |
|   | Amster also supports scripting the installation process. Learn more in [Scripts](../amster/scripts.html). |

### Example 1: Standalone server

This example installs AM with external configuration and identity stores.

```
am> install-openam \
 --serverUrl https://am.example.com:8443/am \
 --adminPwd Ch4ng31t \
 --acceptLicense \
 --cfgStoreDirMgrPwd Ch4ng31t \
 --cfgStore dirServer \
 --cfgStoreHost ds.example.com \
 --cfgStoreAdminPort 4444 \
 --cfgStorePort 1636 \
 --cfgStoreSsl SSL \
 --cfgStoreRootSuffix ou=am-config \
 --userStoreDirMgrPwd Ch4ng31t \
 --userStoreHost ds.example.com \
 --userStoreType LDAPv3ForOpenDS \
 --userStorePort 1636 \
 --userStoreSsl SSL \
 --userStoreRootSuffix ou=identities
timestamp: Checking license acceptance…​
timestamp: License terms accepted.
timestamp: Checking configuration directory /Users/Ping/am.
timestamp: …​Success.
timestamp: Tag swapping schema files.
timestamp: …​Success.
…​
timestamp: Loading Schema /Users/Ping/am/opendj_pushdevices.ldif
timestamp: …​Success.
timestamp: Installing new plugins…​
timestamp: Plugin installation complete.
timestamp: Setting up monitoring authentication file.
Configuration complete!
```

* When you install AM locally, Amster stores the AM configuration in the home directory of the user running the `amster` command. For example, for the `tomcat` user, the configuration is stored in `/path/to/tomcat_home/am` . To change this location, use the `--cfgDir` option.

* The DS instances in this example require secure connections, so the `amster` command specifies port `1636` and `SSL` for both stores.

  Find information about other options in [Configuration options](#install-am-options).

  You must create a truststore and configure it in the AM container. If you don't, the installation will fail.

* If a problem occurs while setting up the configuration store, the installation process exits with an error. When this happens, going to the AM URL opens the configuration page.

### Example 2: Two servers in a site

This example shows how to install two AM servers in a site with external configuration and identity stores.

Before you start, create a truststore for each AM server and prepare the external stores. Because both servers share the configuration and identity store, their truststores must contain the same certificates.

First instance:

```
am> install-openam \
 --serverUrl https://am1.example.com:8443/am \
 --adminPwd Ch4ng31t \
 --acceptLicense \
 --cookieDomain example.com \
 --lbSiteName TestSite01 \
 --cfgDir /tomcat/am1 \
 --lbPrimaryUrl https://site.example.com:8443/am \
 --cfgStoreDirMgr uid=am-config,ou=admins,ou=am-config \
 --cfgStoreDirMgrPwd Ch4ng31t
 --cfgStore dirServer \
 --cfgStoreHost ds.example.com \
 --cfgStoreAdminPort 3444 \
 --cfgStorePort 1636 \
 --cfgStoreSsl SSL \
 --cfgStoreRootSuffix ou=am-config \
 --userStoreDirMgrPwd Ch4ng31t \
 --userStoreHost ds.example.com \
 --userStoreType LDAPv3ForOpenDS \
 --userStorePort 1636 \
 --userStoreSsl SSL \
 --userStoreRootSuffix ou=identities
timestamp: Checking license acceptance…​
timestamp: License terms accepted.
timestamp: Checking configuration directory /tomcat/am1.
timestamp: …​Success.
…​
timestamp: …​Success.
…​
timestamp: …​Success.
timestamp: Installing new plugins…​
timestamp: Plugin installation complete.
timestamp: Setting up monitoring authentication file.
Configuration complete!
```

* Amster creates the directory specified with the `--cfgDir` option.

* The `--lbSiteName` option creates a site with that name, accessible at the URL specified with `--lbPrimaryUrl`.

* Use the `--cookieDomain` option to set the cookie domain. If you don't specify it, Amster uses the server's URL, which isn't optimal for a site with multiple servers.

Second instance:

```
am> install-openam \
 --serverUrl https://am2.example.com:8443/am \
 --adminPwd Ch4ng31t \
 --acceptLicense \
 --cookieDomain example.com \
 --lbSiteName TestSite01 \
 --cfgDir /tomcat/am2 \
 --lbPrimaryUrl https://site.example.com:8443/am \
 --cfgStoreDirMgr uid=am-config,ou=admins,ou=am-config \
 --cfgStoreDirMgrPwd Ch4ng31t \
 --cfgStore dirServer\
 --cfgStoreHost ds.example.com \
 --cfgStoreAdminPort 3444 \
 --cfgStorePort 1636 \
 --cfgStoreSsl SSL \
 --cfgStoreRootSuffix ou=am-config \
 --userStoreDirMgrPwd Ch4ng31t \
 --userStoreHost ds.example.com \
 --userStoreType LDAPv3ForOpenDS \
 --userStorePort 1636 \
 --userStoreSsl SSL \
 --userStoreRootSuffix ou=identities \
 --pwdEncKey MneLwkkOokJx58znp7QyvGmiawmc2vl4
timestamp: Checking license acceptance…​
timestamp: License terms accepted.
timestamp: Checking configuration directory /tomcat/am2.
timestamp: …​Success.
timestamp:Reinitializing system properties.
timestamp:…​Done
timestamp:Configuring server instance.
timestamp: …​Done
timestamp: Installing new plugins…​
timestamp: Plugin installation complete.
timestamp: Setting up monitoring authentication file.
Configuration complete!
```

|   |                                                                                                                                                            |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | To finish adding the second server to the site, you must follow the steps in [Post-installation steps for site deployments](#am-post-install-steps-sites). |

* This command adds a new AM server to the `TestSite01` site. The configuration store details are identical to the first server's, as they share the same DS instance.

* The password for `--adminPwd` must be the same one used for all other servers in the site.

* The `--cookieDomain` must be the same as the one used for the first server (`example.com`).

  If this option isn't set correctly, you might not be able to sign in to the new server.

* The `--pwdEncKey` option specifies the encryption key used by the existing servers in the site. To find this key, sign in to an existing server and go to Deployment > Servers > Server Name > Security > Encryption.

  You must set this option to the correct value. If you don't, the original encryption key will be overwritten, which will prevent the site from reading the configuration and identity stores.

## Configuration options

The following options are available to use with the `install-openam` command:

* `--acceptLicense`

  Indicates the user accepts Amster usage terms and conditions.

* `--authorizedKey` *path*

  The path to an SSH public key file. The content of this file is appended to the `authorized_keys` file of the newly-installed AM instance, allowing users to connect to it with Amster after the install completes.

  Find more information about connecting to AM with Amster in [Connect to AM](../amster/connect-am.html).

* `--cfgDir` *path*

  The configuration directory where AM stores files, such as `$HOME/am`.

* `--cfgStore` *dirServer*

  Set this to `dirServer` to install AM with an external DS server as the configuration store.

  By default, identities are stored in the same directory server instance as the configuration store.

  You must use an external directory server for the configuration store. If you try to install AM with the `--cfgStore embedded` option, the installation fails with the following exception `From AM 8, embedded DS configuration is not supported`.

* `--cfgStoreAdminPort` *port*

  The administration port number for the configuration store, such as `4444`.

* `--cfgStoreDirMgr` *username*

  The bind DN of the configuration store user account, such as `uid=am-config,ou=admins,ou=am-config`.

* `--cfgStoreDirMgrPwd` *password*

  The password for the bind DN. If not set, it takes the password defined for the `--adminPwd` option.

* `--cfgStoreHost` *FQDN*

  The FQDN of the configuration store directory server host, for example, `ds.example.com`.

* `--cfgStorePort` *port*

  The LDAPS or LDAP port number for the configuration store directory server, such as `1636` or `1389`.

* `--cfgStoreRootSuffix` *DN*

  The root suffix DN for the configuration store, such as `ou=am-config`.

* `--cfgStoreSsl [SIMPLE|SSL]`

  Set this to `SSL` to use LDAP with SSL. DS is configured for LDAPS by default. To use LDAP without SSL, set this to `SIMPLE`.

* `--cookieDomain` *domain*

  The name of the trusted DNS domain AM returns to a browser when it grants a session ID to a user.

  Default: FQDN used in the `--serverUrl` option

* `--installLocale` *locale*

  The locale to use during the install process.

  Default: `en_US`

* `--lbPrimaryUrl` *URL*

  The load balancer URL of the site, such as `https://lb.example.com:443/am`

* `--lbSiteName` *name*

  The name of the site to create, if any.

* `--platformLocale` *locale*

  The default locale for the AM installation.

  Default: `en_US`

* `--pwdEncKey` *key*

  The encryption key value used to encrypt passwords in the AM instance. For example `O6QWwHPO4os+zEz3Nqn/2daAYWyiFE32`.

  If you're installing an AM instance that will use existing data, you must provide the same encryption key value originally used to encrypt the passwords in those data stores.

  To locate the encryption key value in an AM instance, navigate to Deployment > Servers > *server name* > Security > Encryption.

  If you are installing a new AM instance that won't use existing data in a data store, you can leave this property empty. AM generates a random encryption key during installation to encrypt the data that will be added to the data store.

  This option is *required* when configuring an AM instance into a site, and must be set to the encryption key configured for the rest of the servers in the site. Failure to set this option to the appropriate value will cause the original encryption key to be overwritten, which will render the site unable to read the configuration, and the identity stores.

  Default: No value; a random encryption key is generated during installation

* `--userStoreDirMgr` *username*

  The bind DN of the identity store user account, such as `uid=am-identity-bind-account,ou=admins,ou=identities`.

* `--userStoreDirMgrPwd` *password*

  The password for the bind DN.

* `--userStoreDomainName` *FQDN*

  The Active Directory Domain Name, such as `ad.example.com`, when the `--userStoreType` option is set to `LDAPv3ForADDC`.

* `--userStoreHost` *FQDN*

  The FQDN of the identity store directory server, such as `ds.example.com`.

* `--userStorePort` *port*

  The LDAPS or LDAP port number for the identity store. Default for LDAPS is `636` and for LDAP is `389`.

* `--userStoreRootSuffix` *DN*

  The root suffix DN for the identity store, such as `ou=identities`.

* `--userStoreSsl [SIMPLE|SSL]`

  Set this to `SSL` to use LDAP with SSL. DS is configured for LDAPS by default. To use LDAP without SSL, set this to SIMPLE.

* `--userStoreType` *type*

  The type of directory server used for the identity store. Possible values for *type* are:

  * `LDAPv3ForAD`: Active Directory with host and port settings

  * `LDAPv3ForADDC`: Active Directory with domain name setting

    If you use this type, you must also set the `--userStoreDomainName` option.

  * `LDAPv3ForADAM`: Active Directory Lightweight Directory Services (AD LDS)

  * `LDAPv3ForForgeRockIAM`: PingDS

    Only use this type if DS is the shared identity store in a Ping Identity Platform deployment. Otherwise, use `LDAPv3ForOpenDS`.

  * `LDAPv3ForOpenDS`: PingDS

  * `LDAPv3ForPingDirectory`: PingDirectory

* `--userStoreDomainName`

  If `--userStoreType` is `LDAPv3ForADDC`, set this to the Active Directory Domain Name, such as `ad.example.com`. Then only set the `--userStoreSsl`, `--userStoreDirMgr`, and `--userStoreDirMgrPwd` options to let Active Directory use DNS to retrieve service locations. Otherwise, don't set this option.

## Post-installation steps for site deployments

All AM servers in a site share the same keystore and secret store infrastructure. This sharing ensures every server in the site can encrypt, decrypt, and verify items like messages and JWTs with the same keys.

The installation process creates these stores only on the first server in the site. You must manually configure them on all other servers you add to the site.

After you've used Amster to add a new server to your site, follow these steps:

1. Make the site keystore infrastructure available to the new instance:

   * Back up the new instance's default keystore and password files in the following locations:

     * `/path/to/am/security/keystores/`

     * `/path/to/am/security/secrets/default/`

   * Make the existing site keystores available to the new server in the same location. For example, you might copy the keystores and their password files, or mount a shared volume.

   * Make sure the keystore files configured in the `/path/to/am/config/boot.json` are available to the new instance.

2. Make the secret store infrastructure in the site available to the new instance:

   * Sign in to the AM admin UI of an existing server in the site and go to Configure > Secret Stores.

   * Review the list of globally configured secret stores and make sure the new server has access to the required stores. For example:

     * For keystore-type secret stores, copy the keystores to the same path on the new server.

     * For filesystem-type secret stores, copy the directory contents to the same path, or make the filesystem available on the same mount point.

     * For HSM-type stores, make sure the new server can access the HSM.

     * For secrets configured as environment variables, make sure the new server's container can access them.

   * Go to Realms > *realm name* > Secret Stores.

   * Review the list of realm-specific secret stores and provide access to the new server as needed.

3. Restart the new server.

   The server is now fully configured and part of the site.

## Troubleshoot AM installations

The following table describes possible errors when installing AM with the `install-openam` command:

| Error                                                                                                                                   | Solution                                                                                     |
| --------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `Invalid Suffix for directory server ds.example.com:1636. No Base Entity dc=incorrectsuffix,dc=com found.`                              | Check that the suffix you are trying to use exists in DS.                                    |
| `Cannot connect to Directory Server. Invalid Credentials.`                                                                              | Check the credentials you're using to connect to DS.                                         |
| `Cannot connect to Directory Server. Connect Error: Connection refused.`                                                                | Check the DS host and connection port.                                                       |
| `Unexpected LDAP exception occurred.`                                                                                                   | Check the DS logs. DS may be stopped or may have become unreachable during the installation. |
| `Cannot connect to Directory Server. Connect Error: The LDAP connection has failed because an error occurred during the SSL handshake.` | Make sure the container where AM is installed trusts the DS SSL certificates.                |

---

---
title: Passive install with FBC
description: Set up PingAM with file-based configuration for passive installation without user interaction at startup
component: pingam
version: 8.1
page_id: pingam:installation:passive-install-fbc
canonical_url: https://docs.pingidentity.com/pingam/8.1/installation/passive-install-fbc.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
page_aliases: ["install-guide:passive-install-fbc.adoc"]
section_ids:
  fbc-startup: FBC initial startup
  mandatory-startup-properties: Mandatory startup properties
  additional-startup-properties: Additional startup properties
  start-with-fbc: Start the server with the mandatory FBC properties
---

# Passive install with FBC

If you store your configuration in JSON files (file-based configuration) you can set up AM with no user interaction when you start the web application container.

The following sections describe the process to install an AM server with (file-based configuration) (FBC).

|   |                                                                                                    |
| - | -------------------------------------------------------------------------------------------------- |
|   | Before you start, read [How AM reads FBC](fbc.html#how-am-reads-FBC) to understand the FBC layers. |

These topics assume you have a DS instance up and running, and that the instance has been installed as an [identity store](https://docs.pingidentity.com/pingds/8.1/install-guide/profile-am-idrepo.html), [CTS store](https://docs.pingidentity.com/pingds/8.1/install-guide/profile-am-cts.html), and [policy and application store](https://docs.pingidentity.com/pingds/8.1/install-guide/profile-am-config.html).

|   |                                                                                                                                                                                    |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | You can find information on setting up an evaluation DS server that stores all three data types in [Step 2. Prepare your datastore](../evaluation/step-2-prepare-data-store.html). |

## FBC initial startup

A passive FBC installation requires a few [mandatory configuration properties](#mandatory-startup-properties) set as environment variables on initial startup. These properties specify that it's a file-based configuration, set the AM server host and port, and set the connection details to the identity and policy stores.

If you don't explicitly set a mandatory configuration property, its default value is used, as listed in the tables in this section. This lets you get started with FBC with minimal configuration upfront and add the required configuration after startup.

FBC installation writes files to the location specified by the value of `com.sun.identity.configuration.directory`. If you don't set a value for this property, AM uses the location of the application container (for example, /path/to/tomcat/webapps/am) and the application context (for example, `/am`) to create a file in `~/openamcfg` with the derived name. That file contains the path to the configuration folder.

### Mandatory startup properties

This table lists the minimum environment variables required to install a server with FBC. If you don't specify a variable listed here, its default value is used on startup.

| Environment variable                               | Description                                                                                            | Valid values                            | Default                                                                                                                                                                                                                                                                                                                |
| -------------------------------------------------- | ------------------------------------------------------------------------------------------------------ | --------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `com.sun.identity.sm.sms_object_filebased_enabled` | Whether FBC is enabled.                                                                                | true, false                             | false                                                                                                                                                                                                                                                                                                                  |
| `com.sun.identity.configuration.directory`         | Path to the folder that holds the configuration files                                                  | Any writeable folder on the file system | `$HOME/application-context`                                                                                                                                                                                                                                                                                            |
| `am.server.protocol`                               | The server protocol used for the AM server instance configuration.                                     | https, http                             | http                                                                                                                                                                                                                                                                                                                   |
| `am.server.fqdn`                                   | The fully qualified domain name that will be used for the AM server instance configuration             | Any valid FQDN                          | `am.localtest.me`                                                                                                                                                                                                                                                                                                      |
| `am.server.port`                                   | The port on which this server instance will be available.                                              | Any valid port number                   | 8080                                                                                                                                                                                                                                                                                                                   |
| `am.server.context`                                | The web application context on which this server instance will be available.                           | /*web application context*              | `/am`                                                                                                                                                                                                                                                                                                                  |
| `am.encryption.key`                                | The encryption key value that will be used to encrypt passwords and other sensitive FBC configuration. | An alphanumeric string                  | A random secret is generated if not providedFor FBC installations, if you use client-side sessions for authentication, you must set an encryption key after the initial install, even if you map a secret label to this key. The key that's generated by default doesn't work for client-side authentication sessions. |
| `am.stores.user.servers`                           | Connection string for the user store in the format *host*:*port*.                                      | A valid server connection string        | `ds.localtest.me:1636`                                                                                                                                                                                                                                                                                                 |
| `am.stores.user.username`                          | Bind DN to connect to the user store.                                                                  | Valid bind DN                           | `uid=admin`                                                                                                                                                                                                                                                                                                            |
| `am.stores.user.password`                          | Bind password for the user store                                                                       | Alphanumeric value                      | `password`                                                                                                                                                                                                                                                                                                             |
| `am.stores.application.servers`                    | Connection string for the application and policy stores in the format *host*:*port*.                   | A valid server connection string        | `ds.localtest.me:1636`                                                                                                                                                                                                                                                                                                 |
| `am.stores.application.password`                   | Bind password for the user store                                                                       | Alphanumeric value                      | `password`                                                                                                                                                                                                                                                                                                             |

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | You can't specify the password of the `amAdmin` user during a passive FBC install. The default `amAdmin` password is `password`. You can use this password to log in to the AM admin UI after the initial install.In production deployments, you *must* set up a secret store to store the `amAdmin` password.Learn more in [Store the amAdmin password in a secret store](../security/securing-administration.html#amadmin-password-secret-store). |

### Additional startup properties

These tables list all the properties you can set as environment variables on startup.

|   |                                                                                                                                                                                                                                                                                                   |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The properties listed in these tables aren't written to the `noninteractive-install.properties` file. After an initial startup, you must specify these values in the deployment configuration layer. Otherwise, you'll need to include them as environment variables for each subsequent startup. |

> **Collapse: General startup properties**
>
> | Environment variable                   | Description                                                                                                                                                  | Valid values                            | Default                    |
> | -------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------ | --------------------------------------- | -------------------------- |
> | `AM_TEST_MODE`                         | Whether AM starts with default test keys and secret stores. Set to `true` for evaluation installs to avoid configuring secret stores manually after startup. | true, false                             | false                      |
> | `com.iplanet.services.debug.directory` | The location of the debug logs.                                                                                                                              | A writeable location on the file system | `am-config-path/var/debug` |

> **Collapse: Startup properties for the identity store**
>
> | Environment variable          | Description                                        | Valid values | Default |
> | ----------------------------- | -------------------------------------------------- | ------------ | ------- |
> | `am.stores.user.ssl.enabled`  | Whether AM connects to the identity store over SSL | true, false  | true    |
> | `am.stores.user.mtls.enabled` | Whether mTLS is enabled for the identity store(1). | true, false  | false   |
>
> (1) This property requires you to configure secrets so you can't set it on an initial install.
>
> The root suffix for the identity store defaults to `ou=identities`.

> **Collapse: Startup properties for the CTS store**
>
> | Environment variable         | Description                                                     | Valid values                     | Default                                                              |
> | ---------------------------- | --------------------------------------------------------------- | -------------------------------- | -------------------------------------------------------------------- |
> | `am.stores.cts.servers`      | Connection string for the CTS store in the format *host*:*port* | A valid server connection string | The value of `am.stores.user.servers`                                |
> | `am.stores.cts.username`     | Bind DN to connect to the CTS store                             | Valid bind DN                    | `uid=openam_cts,ou=admins,ou=famrecords,ou=openam-session,ou=tokens` |
> | `am.stores.cts.password`     | Bind password for the CTS store                                 | Alphanumeric value               | The value of `am.stores.user.password`                               |
> | `am.stores.cts.root.suffix`  | Root suffix for CTS store                                       | Valid base DN                    | `ou=famrecords,ou=openam-session,ou=tokens`                          |
> | `am.stores.cts.ssl.enabled`  | Whether AM connects to the CTS store over SSL                   | true, false                      | The value `am.stores.user.ssl.enabled`, if set, otherwise `true`     |
> | `am.stores.cts.mtls.enabled` | Whether mTLS is enabled for the CTS store                       | true, false                      | false                                                                |
>
> The base DN for the CTS store defaults to `ou=famrecords,ou=openam-session,ou=tokens`.

> **Collapse: Startup properties for the application store**
>
> | Environment variable                 | Description                                                             | Valid values                     | Default                                                          |
> | ------------------------------------ | ----------------------------------------------------------------------- | -------------------------------- | ---------------------------------------------------------------- |
> | `am.stores.application.servers`      | Connection string for the application store in the format *host*:*port* | A valid server connection string | The value of `am.stores.user.servers`                            |
> | `am.stores.application.username`     | Bind DN to connect to the application store                             | Valid bind DN                    | `uid=am-config,ou=admins,ou=am-config`                           |
> | `am.stores.application.password`     | Bind password for the application store                                 | Alphanumeric value               | The value of `am.stores.user.password`                           |
> | `am.stores.application.ssl.enabled`  | Whether AM connects to the application store over SSL                   | true, false                      | The value `am.stores.user.ssl.enabled`, if set, otherwise `true` |
> | `am.stores.application.mtls.enabled` | **Not used for the application store**                                  | –                                | –                                                                |
>
> The base DN for the application store defaults to `ou=services,ou=am-config`.

> **Collapse: Startup properties for the policy store**
>
> | Environment variable           | Description                                                        | Valid values                     | Default                                                                  |
> | ------------------------------ | ------------------------------------------------------------------ | -------------------------------- | ------------------------------------------------------------------------ |
> | `am.stores.policy.servers`     | Connection string for the policy store in the format *host*:*port* | A valid server connection string | The value of `am.stores.application.servers`                             |
> | `am.stores.policy.username`    | Bind DN to connect to the policy store                             | Valid bind DN                    | `uid=am-config,ou=admins,ou=am-config`                                   |
> | `am.stores.policy.password`    | Bind password for the policy store                                 | Alphanumeric value               | The value of `am.stores.application.password`                            |
> | `am.stores.policy.ssl.enabled` | Whether AM connects to the policy store over SSL                   | true, false                      | The value `am.stores.user.application.enabled`, if set, otherwise `true` |
>
> The base DN for the policy store defaults to `ou=services,ou=am-config`.

> **Collapse: Startup properties for UMA stores**
>
> | Environment variable         | Description                                                     | Valid values                     | Default                                                                   |
> | ---------------------------- | --------------------------------------------------------------- | -------------------------------- | ------------------------------------------------------------------------- |
> | `am.stores.uma.servers`      | Connection string for the UMA store in the format *host*:*port* | A valid server connection string | The value of `am.stores.application.servers`                              |
> | `am.stores.uma.username`     | Bind DN to connect to the UMA store                             | Valid bind DN                    | `uid=am-config,ou=admins,ou=am-config`                                    |
> | `am.stores.uma.password`     | Bind password for the UMA store                                 | Alphanumeric value               | The value of `am.stores.application.password`                             |
> | `am.stores.uma.ssl.enabled`  | Whether AM connects to the UMA store over SSL                   | true, false                      | The value `am.stores.user.application.enabled`, if set, otherwise `true`  |
> | `am.stores.uma.mtls.enabled` | Whether mTLS is enabled for the UMA store(1).                   | true, false                      | The value `am.stores.application.mtls.enabled`, if set, otherwise `false` |
>
> (1) This property requires you to configure secrets so you can't set it on an initial install.
>
> The root suffix for the UMA store defaults to `ou=am-config`.

## Start the server with the mandatory FBC properties

The following command assumes you're running AM in Apache Tomcat. It adds the required settings to the `CATALINA_OPTS` variable in the `setenv` file. You can also set these properties as `JAVA_OPTS` environment variables before you start the application container.

|   |                                                                                                                                                                                                                                       |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | If you're evaluating AM, set `AM_TEST_MODE=true` as an environment variable before starting the server. AM then starts with default test keys and secret stores, so you don't need to configure secret stores manually after startup. |

This command sets the following properties:

* FBC to `true`

* Location of configuration files to `/path/to/am-config`

* Identity and application stores to `ds.example.com:1636`

* Identity and application store connection details to the values set if you install your <https://docs.pingidentity.com/pingds/8.1> servers with the corresponding [setup profiles](https://docs.pingidentity.com/pingds/8.1/install-guide/setup-profiles.html).

* Location of truststore to `/path/to/truststore`. Learn more in [Prepare the truststore](prepare-trust-store.html).

* Truststore password to `new-password`

* Truststore type to `jks`

- Linux

- Windows

In `$CATALINA_BASE/bin/setenv.sh`:

```bash
export CATALINA_OPTS="$CATALINA_OPTS -Dcom.sun.identity.sm.sms_object_filebased_enabled=true \
-Dcom.sun.identity.configuration.directory=/path/to/am-config \
-Dam.server.fqdn=am.example.com \
-Dam.stores.user.servers=ds.example.com:1636 \
-Dam.stores.user.username=uid=am-identity-bind-account,ou=admins,ou=identities \
-Dam.stores.user.password=5up35tr0ng \
-Dam.stores.application.servers=ds.example.com:1636 \
-Dam.stores.application.password=5up35tr0ng \
-Djavax.net.ssl.trustStore=/path/to/truststore \
-Djavax.net.ssl.trustStorePassword=new-password \
-Djavax.net.ssl.trustStoreType=jks -server -Xmx2g -XX:MetaspaceSize=256m -XX:MaxMetaspaceSize=256m"
```

In `$CATALINA_BASE/bin/setenv.bat`:

```powershell
set "CATALINA_OPTS=%CATALINA_OPTS% -Dcom.sun.identity.sm.sms_object_filebased_enabled=true -
-Dcom.sun.identity.configuration.directory=/path/to/am-config -
-Dam.server.fqdn=am.example.com -
-Dam.stores.user.servers=ds.example.com:1636 -
-Dam.stores.user.username=uid=am-identity-bind-account,ou=admins,ou=identities -
-Dam.stores.user.password=5up35tr0ng -
-Dam.stores.application.servers=ds.example.com:1636 -
-Dam.stores.application.password=5up35tr0ng -
-Djavax.net.ssl.trustStore=/path/to/truststore -
-Djavax.net.ssl.trustStorePassword=new-password -
-Djavax.net.ssl.trustStoreType=jks -server -Xmx2g -XX:MetaspaceSize=256m -XX:MaxMetaspaceSize=256m"
```

1. Start the web application container where AM runs. For example:

   ```bash
   $ bin/startup.sh
   Using CATALINA_BASE:   /path/to/tomcat10
   Using CATALINA_HOME:   /path/to/tomcat10
   Using CATALINA_TMPDIR: /path/to/tomcat10/temp
   Using JRE_HOME:        /Library/Java/JavaVirtualMachines/temurin-25.jdk/Contents/Home
   Using CLASSPATH:       /path/to/tomcat10/bin/bootstrap.jar:/path/to/tomcat10/bin/tomcat-juli.jar
   Using CATALINA_OPTS:   -Dcom.sun.identity.sm.sms_object_filebased_enabled=true -Dcom.sun.identity.configuration.directory=/path/to/am-config -Dam.server.fqdn=am.example.com -Dam.stores.user.servers=ds.example.com:1636 -Dam.stores.user.username=uid=am-identity-bind-account,ou=admins,ou=identities -Dam.stores.user.password=5up35tr0ng -Dam.stores.application.servers=ds.example.com:1636 -Dam.stores.application.password=5up35tr0ng -Djavax.net.ssl.trustStore=/path/to/truststore -Djavax.net.ssl.trustStorePassword=new-password -Djavax.net.ssl.trustStoreType=jks -server -Xmx2g -XX:MetaspaceSize=256m -XX:MaxMetaspaceSize=256m
   Tomcat started.
   ```

2. In the configuration file directory, locate the `noninteractive-install.properties` file for the FBC installation.

   This file reflects the environment variables you provided at startup:

   ```bash
   $ more am-config/config/services/noninteractive-install.properties
   am.server.fqdn=am.example.com
   am.passwords.dsameuser.encrypted=AQICpxyEaXv0vc5cFxQttsDWoYfqmCqV9Kljs4rByHQ2hHzOTjiF3MdTrUfKNKKyg5ie7FujAhPxWY6unMOpxn8Tj9CJXJ/289YxL04q6pMkxqX9K2tGh55F/um4tv7sqYybySDeAP7UW9X3PpeMB8Ye6e+reEdH9dAmjGcf8gh8rvnZw29hPo0/EA==
   am.server.protocol=http
   am.stores.user.password=5up35tr0ng
   am.server.port=8080
   am.stores.application.servers=ds.example.com:1636
   am.server.context=/am
   am.encryption.key=PL2EdksXsEyCh0xrEwgLdRXwXPzCqf36
   am.stores.user.username=uid=am-identity-bind-account,ou=admins,ou=identities
   am.stores.user.servers=ds.example.com:1636
   am.stores.application.password=5up35tr0ng
   ```

   If you don't explicitly set a variable on startup, the FBC install uses the defaults listed in [Mandatory startup properties](#mandatory-startup-properties).

3. Navigate to the AM admin UI at your deployment URL:

   `am.server.protocol://am.server.fqdn:am.server.port/am.server.context`

   For example, `http://am.example.com:8080/am`.

4. Log in as `amAdmin` with the default password (`password`).

5. Set up a secret store to store the `amAdmin` password.

   Learn more in [Store the amAdmin password in a secret store](../security/securing-administration.html#amadmin-password-secret-store).

6. Review and edit the configuration for the following datastores, as required:

   * [Identity store](../setup/setting-up-identity-stores.html)

   * [CTS store](../cts/cts-openam-config.html)

   * [Application and policy stores](../setup/prepare-policy-and-application-store.html)

   * [UMA stores](../uma/configure-external-uma-stores.html)

7. Configure any required [secret stores](../security/secret-stores.html).

8. Make any additional configuration changes.

|   |                                                                                                                                                                                                                                                                                       |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Any configuration you update in the AM admin UI is written to the deployment configuration layer (under `/path/to/am/config/services`).Any configuration you *don't* update uses the baseline layer and requires the relevant environment variables to be set on subsequent startups. |

---

---
title: Prepare a configuration store
description: Prepare a PingDS server as a configuration datastore for PingAM and enable TLS/LDAPS communication between them
component: pingam
version: 8.1
page_id: pingam:installation:prepare-configuration-store
canonical_url: https://docs.pingidentity.com/pingam/8.1/installation/prepare-configuration-store.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Install", "Configuration Store"]
page_aliases: ["install-guide:prepare-configuration-store.adoc"]
---

# Prepare a configuration store

This page explains how to prepare a single DS server as a configuration datastore. Make sure DS replicas use the same configuration.

Installing DS with a [setup profile](https://docs.pingidentity.com/pingds/8.1/install-guide/setup-profiles.html) creates the required backend, schema, bind user, and indexes:

1. Follow the steps in [Install DS for AM configuration](https://docs.pingidentity.com/pingds/8.1/install-guide/profile-am-config.html) in the PingDS documentation.

2. [Install AM](interactive-install.html) to use the prepared DS directory server as a configuration store.

   The default bind DN of the service account to connect to the configuration store is:

   ```
   uid=am-config,ou=admins,ou=am-config
   ```

3. Share the configuration store certificate with the AM container to prepare for TLS/LDAPS.

   Communication with the configuration store *must* use a secure connection.

   * On the DS host, export the DS CA certificate.

     DS uses a deployment ID and password to generate a CA key pair. Learn more in [Deployment IDs](https://docs.pingidentity.com/pingds/8.1/security-guide/pki.html#about-deployment-ids).

     Use the `dskeymgr` command to export the CA certificate:

     ```bash
     $ /path/to/opendj/bin/dskeymgr \
     export-ca-cert \
     --deploymentId $DEPLOYMENT_ID \
     --deploymentIdPassword password \
     --outputFile /path/to/ca-cert.pem
     ```

   * Copy the `ca-cert.pem` file to an accessible location on the AM host.

   - Import the DS CA certificate into the AM truststore:

     ```bash
     $ keytool \
     -importcert \
     -file /path/to/ca-cert.pem \
     -keystore /path/to/am/security/keystores/truststore
     -storepass truststore-password
     ```

   Learn more about configuring AM's truststore in [Prepare the truststore](prepare-trust-store.html).

4. When the certificate is in place, continue installing AM.

|   |                                                                                                                                                                                                                                                                             |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | After setting up the configuration store, you can enhance security by configuring mTLS authentication to that store and rotating the mTLS certificates periodically. Learn more in [mTLS for configuration stores](../security/secure-connections.html#mtls-config-stores). |

---

---
title: Prepare a web application container
description: Prepare a Java application container to deploy PingAM by configuring your supported container and enforcing HTTPS connections
component: pingam
version: 8.1
page_id: pingam:installation:prepare-containers
canonical_url: https://docs.pingidentity.com/pingam/8.1/installation/prepare-containers.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Install", "Web Container"]
page_aliases: ["install-guide:prepare-containers.adoc"]
---

# Prepare a web application container

As a Java application, AM must be deployed in a Java container. Refer to [Application containers](https://docs.pingidentity.com/pingam/release-notes/requirements.html#prerequisites-application-servers) for the list of supported containers.

The following table summarizes the high-level tasks required to prepare your container:

| Task                                                                                                                                                                                                                                                    | Resources                                                                                                                                       |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| Prepare the container for AMFollow the instructions for your container.                                                                                                                                                                                 | * [Apache Tomcat](prepare-apache-tomcat.html)

* [JBoss and WildFly](prepare-jboss.html)

* [IBM WebSphere Liberty](prepare-ibm-websphere.html) |
| Secure the containerThere are many ways to deploy and configure your environment for AM. Enforce HTTPS connections to AM where possible.If a Java Security Manager is enabled for your web application container, add permissions before installing AM. | - [Secure connections to the AM container](configure-container-HTTPS.html)

- [Use stronger encryption algorithms](prepare-aeswrap.html)        |

---

---
title: Prepare an FQDN
description: Configure PingAM with a fully qualified domain name and set cookie domain names to ensure proper browser cookie handling
component: pingam
version: 8.1
page_id: pingam:installation:prepare-networking
canonical_url: https://docs.pingidentity.com/pingam/8.1/installation/prepare-networking.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Install"]
page_aliases: ["install-guide:prepare-networking.adoc"]
---

# Prepare an FQDN

AM requires that you provide an FQDN when you configure it. Before you set up AM, be sure that your system has an FQDN, such as `am.example.com`. For evaluation purposes, you can give your system an alias using the `/etc/hosts` file on UNIX systems or `%SystemRoot%\system32\drivers\etc\hosts` on Windows. For production deployments, make sure the FQDN is properly assigned using DNS.

Do not use the hostname `localhost` for AM, not even for testing purposes. AM relies on browser cookies, which are returned based on the domain name. You can set the cookie domain name value to an empty string for host-only cookies or to any non-top level domain. For example, if you install AM and use `am.example.com` as the host, you can set the cookie domain name as `example.com`.

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | Do not configure a top-level domain as your cookie domain as browsers will reject them.Top-level domains are browser-specific. Some browsers, like Firefox, also consider special domains like Amazon's web service (for example, ap-southeast-2.compute.amazonaws.com) to be a top-level domain.Check the effective top-level domain list at <https://publicsuffix.org/list/effective_tld_names.dat> to ensure that you do not set your cookie to a domain in the list. |

---

---
title: Prepare datastores
description: Configure datastores to separate different types of information in PingAM, including configuration, identity, policy, application, CTS token, and UMA data
component: pingam
version: 8.1
page_id: pingam:installation:prepare-ext-stores
canonical_url: https://docs.pingidentity.com/pingam/8.1/installation/prepare-ext-stores.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Install", "Configuration Store", "Policy Store", "Identity Store", "Application Store", "CTS Store (Sessions &amp; Tokens)", "User-Managed Access (UMA)"]
page_aliases: ["install-guide:prepare-ext-stores.adoc"]
section_ids:
  ldap_datastores: LDAP datastores
  file_based_configuration_store: File-based configuration store
---

# Prepare datastores

AM stores different types of information. At a high-level, you can divide information into the following types:

* Configuration

  Relatively *static* information that doesn't change frequently after initial setup. Only administrative users can change it.

* Runtime data

  Dynamic information that changes at runtime, often due to end user action. Examples of runtime data are identities, CTS tokens, policies, sessions, and applications.

Apart from identity data, AM stores all data after the installation process in its *configuration store*. This keeps basic deployments simple.

For advanced and high-load deployments, you can configure different sets of replicated DS servers to keep distinct data types separate and to tune DS for different requirements.

AM supports the following datastores:

| Store name                          | Type of data                                                                                                                                                                                                   | Required during installation?                                  |
| ----------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------- |
| Configuration store (PingDS or FBC) | Static configuration (properties and settings used by the AM instance).                                                                                                                                        | Yes                                                            |
| Identity or user store              | Stores identity profiles; that is, information about the users, devices, or things that authenticate to your systems. You can also configure AM to access existing directory servers to get identity profiles. | No, but you can configure one during the installation process. |
| Policy store                        | Stores policy-related data, such as policies, policy sets, and resource types.                                                                                                                                 | No                                                             |
| Application store                   | Stores application-related data, such as web and Java agent configurations, federation entities and configuration, and OAuth 2.0 client definitions.                                                           | No                                                             |
| CTS token store                     | Stores information about sessions, SAML 2.0 assertions, OAuth 2.0 tokens, and session denylists and allowlists.                                                                                                | No                                                             |
| UMA store                           | Stores information about UMA resources, labels, audit messages, and pending requests.                                                                                                                          | No                                                             |

## LDAP datastores

The following table lists the supported directory servers for storing different data types:

**Supported data stores**

| Directory server           | Versions         | Configuration | Apps / policies | CTS | Identities | UMA |
| -------------------------- | ---------------- | ------------- | --------------- | --- | ---------- | --- |
| PingDS                     | 7.3.1 and later  | ✔             | ✔               | ✔   | ✔          | ✔   |
| PingDirectory              | 9.3 and later    |               |                 |     | ✔          |     |
| Oracle Unified Directory   | 12c              |               |                 |     | ✔          |     |
| Microsoft Active Directory | 2019, 2022, 2025 |               |                 |     | ✔          |     |

The procedure for preparing directory servers for AM to use is similar for each data type and includes the following steps:

1. If you don't have an existing directory server, install the directory server software; for example, PingDS.

2. As the directory administrator, you may need to perform the following steps:

   1. Apply the relevant schema to the directory.

   2. Create indexes to optimize data retrieval from the directory server.

   3. Create a user account with the minimum required privileges for AM to bind to the directory server and access necessary data.

To prepare the datastores AM needs during installation, read the following pages:

[icon: handshake, set=fad, size=3x]

#### [Prepare a truststore](prepare-trust-store.html)

Trust datastores' certificates for LDAPS.

[icon: cogs, set=fad, size=3x]

#### [Prepare configuration stores](prepare-configuration-store.html)

Install DS as an AM configuration store.

[icon: user-circle, set=fad, size=3x]

#### [Prepare identity stores](prepare-identity-repository.html)

Install DS as an AM identity store.

> **Collapse: Where do I find more information about the other datastores?**
>
> You can configure all datastores except the configuration store after you install AM:
>
> * [Prepare policy and application stores](../setup/prepare-policy-and-application-store.html)
>
> * [Core Token Service (CTS)](../cts/preface.html)
>
> * [Prepare external UMA datastores](../uma/prepare-uma-store.html)

## File-based configuration store

File-based configuration (FBC) is best-suited to a DevOps-style deployment, with the associated tools and practices of that approach.

Static FBC data is written to configuration files in the file system and checked into a source control system, such as Git.

AM instances are created as Docker images, with the FBC incorporated into the image.

![Kubernetes deployment using file-based configuration.](../_images/docker-deployment.png)

You can insert variables into these configuration files before you check them into source control. The variables are substituted with the appropriate values at runtime when you start the Docker container. Using variables lets you reuse the same base configuration files for multiple instances, and different staging environments. For example, development, QA, or pre-production, which are then promoted to production.

Learn more about FBC in [Store configuration data in JSON files](fbc.html).

Learn more about installing AM instances with Kubernetes in the [ForgeOps](https://docs.pingidentity.com/forgeops/2025.1) documentation.