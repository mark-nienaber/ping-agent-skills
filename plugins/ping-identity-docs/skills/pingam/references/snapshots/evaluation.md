---
title: Evaluation
description: Get a test or demo PingAM instance running quickly with a single PingDS server as the configuration, identity, and token store
component: pingam
version: 8.1
page_id: pingam:evaluation:preface
canonical_url: https://docs.pingidentity.com/pingam/8.1/evaluation/preface.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Evaluation"]
page_aliases: ["index.adoc", "eval-guide:preface.adoc"]
---

# Evaluation

These topics cover the tasks you need to get a test or demo PingAM instance running quickly with a single PingDS server acting as the configuration store, identity store and CTS token store.

[icon: book, set=fad, size=3x]

#### [PingAM](about-am.html)

Learn about AM.

[icon: check-circle, set=fad, size=3x]

#### [Step 1. Prepare your servers](step-1-prepare-server.html)

Prepare your computer to host AM and DS.

[icon: cogs, set=fad, size=3x]

#### [Step 2. Prepare your datastore](step-2-prepare-data-store.html)

Prepare your DS server.

[icon: download, set=fad, size=3x]

#### [Step 3. Deploy AM](step-3-deploy-am.html)

Deploy the AM `.war` file into Tomcat.

[icon: wrench, set=fad, size=3x]

#### [Step 4. Configure AM](step-4-configure-am.html)

Create a realm, an authentication tree and a test user.

[icon: users, set=fad, size=3x]

#### [Step 5. Authenticate to AM](step-5-try-am.html)

Log in for the first time, using your authentication tree.

[icon: map-signs, set=fad, size=3x]

#### [Next steps](next-steps.html)

Discover what else AM has to offer.

---

---
title: Next steps
description: "Explore PingAM's advanced features including user self-service, single sign-on, SAML 2.0 federation, OAuth 2.0 integration, access policies, and developer APIs"
component: pingam
version: 8.1
page_id: pingam:evaluation:next-steps
canonical_url: https://docs.pingidentity.com/pingam/8.1/evaluation/next-steps.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Evaluation", "Features"]
page_aliases: ["eval-guide:next-steps.adoc"]
section_ids:
  user-self-service-features: User self-service features
  sso-features: Single sign-on
  federation: SAML 2.0 federation
  oauth2-features: OAuth 2.0 and OAuth 2.0-based standards federation
  policy-and-xacml: Policy enforcement points and access policies
  modern-api: Modern APIs for developers
---

# Next steps

AM can do much more than authenticate users. In addition to being the right foundation for building highly available, Internet-scale access management services, AM has a rich set of features that make it a strong choice for a variety of different deployments.

Find out more about them:

[icon: id-card, set=fad, size=3x]

#### [User self-service features](next-steps.html#user-self-service-features)

Discover how end users can manage their profiles.

[icon: users, set=fad, size=3x]

#### [Single sign-on](next-steps.html#sso-features)

Create seamless end user journeys.

[icon: handshake, set=fad, size=3x]

#### [SAML 2.0 federation](next-steps.html#federation)

Federate identities with the SAML 2.0 standard.

[icon: user-plus, set=fad, size=3x]

#### [OAuth 2.0-based federation](next-steps.html#oauth2-features)

Protect applications with OAuth 2.0, OpenID Connect 1.0, and UMA 2.0.

[icon: hand-paper, set=fad, size=3x]

#### [Access policies and policy enforcement](next-steps.html#policy-and-xacml)

Centrally control access to your organization's applications.

[icon: code, set=fad, size=3x]

#### [Modern APIs for developers](next-steps.html#modern-api)

Discover the REST and Java APIs that AM exposes.

## User self-service features

AM provides user self-registration and password reset services that allow users access to applications without the need to call your help desk.

AM has access to the identity stores that store user profiles. AM is therefore well-placed to help you manage self-service features that involve user profiles.

* **User self-registration**. AM provides user self-registration as a feature of AM's REST APIs. New users can easily self-register in AM without assistance from administrators or help desk staff.

  You can find details on configuring self-registration in [Configure user registration](../user-self-service/configuring-user-self-registration.html).

  You can find details on building your own self-registration application using the REST API in [Register a user](../user-self-service/uss-registering-users.html).

* **Password reset**. With AM's self-service password reset, users can help reset passwords, as well as update their existing passwords. AM handles both the case where a user knows their password and wants to change it, and also the case where the user has forgotten their password and needs to reset it, possibly after answering security questions.

  You can find details on setting up password reset capabilities in [Configure forgotten password reset](../user-self-service/configuring-forgotten-password.html).

  You can find details on building your own application to handle password reset using the REST API in [Reset forgotten passwords](../user-self-service/uss-forgotten-password.html).

* **Dashboard service**. Users often have a number of applications assigned to them, especially if your organization has standardized SaaS, for example for email, document sharing, support ticketing, customer relationship management, web conferencing, and so forth. You can create an interface for users to access these web-based and internal applications using AM's dashboard service.

  The AM cloud dashboard service makes this relatively easy to set up. Learn more in [Dashboards](../setup/dashboard-service.html).

AM's user-facing pages are fully customizable and easy to skin for your organization. [UI customization](../ui-customization/preface.html) has details on how to customize user-facing pages.

## Single sign-on

Single sign-on (SSO) and cross-domain single sign-on (CDSSO) are core features of AM. Once you have set up AM, you protect as many applications in the network domain as you want. Simply install web or Java agents for the additional servers, and add policies for the resources served by the applications. Users can authenticate to start an authenticated session on any site in the domain and stay authenticated for all sites in the domain without needing to log in again (unless the session ends, or a policy requires stronger authentication).

Many organizations manage more than one domain. When you have multiple distinct domains in a single organization, cookies set in one domain are not returned to servers in another domain. In many organizations, sub-domains are controlled independently. These domains need to be protected from surreptitious takeovers like session cookie hijacking. AM's CDSSO provides a safe mechanism for your AM servers in one domain to work with web or Java agents from other domains, while allowing users to sign-on once across many domains without needing to reauthenticate. CDSSO allows users to sign on in one of your domains and not have to sign on again when they visit another of your domains.

You can find details on configuring web and Java agents for CDSSO in [Implement CDSSO](../am-authentication/about-sso.html#implementing-cdsso).

## SAML 2.0 federation

Security Assertion Markup Language (SAML) 2.0 grew out of earlier work on SAML v1.x and the Liberty Alliance. SAML defines XML-based, standard formats and profiles for federating identities. SAML 2.0 is supported by a wide range of applications including major software as a service (SaaS) offerings. AM can function as a hub in deployments where different standards are used. Learn more in [SAML 2.0](../am-saml2/preface.html).

When your deployment serves as an identity provider for a SAML federation, AM makes it easy to develop applications called Fedlets that your service providers can easily deploy to participate in the federation. You can find details in [Implement SAML 2.0 SPs by using Fedlets](../am-saml2/saml2-implementation-fedlet.html).

## OAuth 2.0 and OAuth 2.0-based standards federation

OAuth 2.0 and OpenID Connect 1.0 are open standards for authorization using REST APIs to allow users to authorize third-party access to their resources. These standards make it easier to federate modern web applications. User-Managed Access (UMA) 2.0 takes OpenID Connect a step further, and lets the end user manage access to their resources.

AM can serve as the authorization server for your clients, or as a client to another authorization server. As an authorization server, AM supports capabilities such as:

* Dynamic client registration

* Using macaroons as access and refresh tokens

* Client-side access and refresh tokens

* Proof-of-possession

* Scripted OpenID Connect claims

* Authentication requirements for ID tokens.

Learn more in:

* [OAuth 2.0](../am-oauth2/preface.html)

* [OpenID Connect 1.0](../am-oidc1/preface.html)

* [User-Managed Access (UMA) 2.0](../uma/preface.html)

## Policy enforcement points and access policies

AM can handle large numbers of access policies, each of which gives you control over user provisioning and user entitlements. Learn more in [Authorization](../am-authorization/preface.html).

AM also supports standards-based access policies defined using the eXtensible Access Control Markup Language (XACML). XACML defines an XML Attribute-Based Access Control (ABAC) language with Role-Based Access Control (RBAC) features as well. You can find details on using XACML policies with AM in [Import and export policies](../am-authorization/import-export-policy.html).

AM also includes web agents and Java agents, which are add-on components that operate as a policy enforcement point (PEP) for a website or application. For example, you can install a web agent to enforce AM's authorization decisions on Apache HTTP Server. Learn more in the [Web Agents documentation](https://docs.pingidentity.com/web-agents/2025.3) and the [Java Agents documentation](https://docs.pingidentity.com/java-agents/2025.3).

Furthermore, [PingGateway](https://docs.pingidentity.com/pinggateway/2025.11) works with applications where you want to protect access, but can't install a web or Java agent. For example, you might have a web application running in a server for which no agent has been developed. Or you might be protecting an application where you simply cannot install an agent. In that case, PingGateway functions as a flexible reverse proxy with standard SAML 2.0 capabilities.

## Modern APIs for developers

For client application developers, AM offers REST and Java APIs.

* AM REST APIs make the common CRUD (create, read, update, delete) easy to use in modern web applications. They also offer extended actions and query capabilities for access management functionality.

  You can find details in the [REST API](../am-rest/preface.html).

* AM Java APIs let your Java and Java applications call on AM for authentication and authorization in both AM and federated environments.

  Learn more in the [PingAM Java API Specification](../_attachments/apidocs/index.html).

AM provides built-in support for many identity stores, web servers and web application containers, access management standards, and all the flexible, configurable capabilities mentioned in this page. Yet, for some deployments you might still need to extend what AM's capabilities. For such cases, AM defines Service Provider Interfaces (SPIs) where you can integrate your own plugins. You can find details about extension points, and some examples, in the following links:

* [Customize authentication trees](../am-authentication/authn-implementation-authn.html#customizing-auth-trees)

* [Policy condition script API functionality](../am-authorization/scripted-policy-condition.html#scripting-api-policy)

* [Customize identity stores](../setup/setting-up-identity-stores.html#customizing-data-stores)

* [Customizing OAuth 2.0 scope handling](../am-oauth2/oauth2-scopes.html#customizing-oauth2-scopes)

---

---
title: PingAM (AM)
description: PingAM provides centralized access management through authentication trees and authorization policies to manage user access to network resources
component: pingam
version: 8.1
page_id: pingam:evaluation:about-am
canonical_url: https://docs.pingidentity.com/pingam/8.1/evaluation/about-am.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Evaluation"]
page_aliases: ["eval-guide:about-am.adoc"]
---

# PingAM (AM)

AM provides a service called *access management*, which manages access to resources, such as a web page, an application, or a web service, that are available over the network. Once it is set up, AM provides an infrastructure for managing users, roles, and access to resources. In this chapter, you manage access to a single web page.

AM centralizes access control by handling both *authentication* and *authorization*. Authentication is the process of identifying an individual, for example, by confirming a successful login. Authorization is the process of granting access to resources to authenticated individuals.

AM uses *trees* to provide fine-grained authentication. Authentication trees are made up of *nodes*, which allow multiple paths and decision points throughout the authentication flow. Each node performs a single task during authentication, such as collecting a username or making a simple decision. Authentication nodes can have multiple outcomes beyond just success or failure. AM lets you create complex yet customer-friendly authentication experiences by linking nodes together, creating loops, and nesting nodes within a tree.

AM centralizes authorization by letting you manage access policies separate from applications and resources. Instead of building an access policy into a web application, you install an agent with the web application to request policy decisions from AM. This approach avoids issues caused by embedding policy decisions into applications. If a policy changes or an issue is found after the application is deployed, you only have to change the policy definition in AM instead of deploying a new version of the application. AM makes the authorization decisions, and web and Java agents enforce the decisions on AM's behalf.

Keep on reading to try AM's access management capabilities by installing AM and configuring an authentication tree.

---

---
title: Step 1. Prepare your servers
description: Prepare your servers for PingAM installation by checking disk space, configuring fully qualified domain names, installing a supported JDK and Apache Tomcat, and downloading PingAM and PingDS
component: pingam
version: 8.1
page_id: pingam:evaluation:step-1-prepare-server
canonical_url: https://docs.pingidentity.com/pingam/8.1/evaluation/step-1-prepare-server.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Evaluation", "Install"]
page_aliases: ["eval-guide:step-1-prepare-server.adoc"]
section_ids:
  prepare-fqdn: Prepare a fully qualified domain name
  install-jdk-and-apache-tomcat: Install a JDK and Apache Tomcat
---

# Step 1. Prepare your servers

To install AM in a demo or test environment with a single DS server acting as the configuration store, identity store and CTS token store, perform the following prerequisite tasks:

* Check disk space

  For initial installation, make sure you have at least 10 GB free disk space.

  You can find more information on disk storage requirements in [Deployment requirements](../deployment-planning/deploy-hardware-requirements.html) and in [Sizing systems](https://docs.pingidentity.com/pingds/8.1/deployment-guide/prerequisites.html#size-systems) in the DS documentation.

* Prepare a fully qualified domain name (FQDN)

  You must use fully qualified domain names. AM uses HTTP cookies to keep track of sessions for single sign-on (SSO), and setting and reading cookies depends on the server name and domain.

  You can find information on preparing an FQDN in [Prepare a fully qualified domain name](#prepare-fqdn).

* Install a supported Java development kit (JDK)

  Because AM and DS are Java web applications, you must download and install a supported JDK. You can find a list of supported JDK versions in [Java requirements](https://docs.pingidentity.com/pingam/release-notes/requirements.html#prerequisites-java) and in [Java](https://docs.pingidentity.com/pingds/release-notes/requirements.html#prerequisites-java) in the DS documentation.

  You can find information on installing a JDK in [Install a JDK and Apache Tomcat](#install-jdk-and-apache-tomcat).

* Install a supported web container

  AM can run in a number of web application containers. For the purposes of this evaluation, download [Apache Tomcat](https://tomcat.apache.org/).

  You can find a list of supported versions in [Application containers](https://docs.pingidentity.com/pingam/release-notes/requirements.html#prerequisites-application-servers).

  You can find information on installing Apache Tomcat in [Install a JDK and Apache Tomcat](#install-jdk-and-apache-tomcat).

* Download PingAM and PingDS

  The [Ping Identity Download Center](https://backstage.pingidentity.com/downloads) hosts downloadable versions of AM and DS.

  You can find a list of supported operating systems in the [Operating system requirements](https://docs.pingidentity.com/pingam/release-notes/requirements.html#operating-systems) and in [Operating systems](https://docs.pingidentity.com/pingds/release-notes/requirements.html#prerequisites-operating-systems) in the DS documentation.

|   |                                                                                                                                                           |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The instructions to set up the software are written for use on a UNIX-like system.If you are running Microsoft Windows, adapt these examples accordingly. |

## Prepare a fully qualified domain name

Before deploying and installing AM and DS, assign your AM server a DNS alias, such as `am .example.com` and your DS server a DNS alias, such as `ds.example.com`.

You can add DNS aliases by editing your [hosts file](https://en.wikipedia.org/wiki/Hosts_\(file\)).

|   |                                                                                                                                                                        |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | If you already have a DNS server set up, or use a service, such as [localtest.me](https://readme.localtest.me/), you can use those instead of editing your hosts file. |

1. Add the aliases to your hosts file using your preferred text editor. For example:

   ```bash
   # Edit /etc/hosts
   $ sudo vi /etc/hosts
   Password:

   $ cat /etc/hosts | grep am
   127.0.0.1    localhost am.example.com ds.example.com
   ```

2. Proceed to [install a JDK and Apache Tomcat](#install-jdk-and-apache-tomcat).

## Install a JDK and Apache Tomcat

AM runs as a Java web application inside an application container. Apache Tomcat is an application container that runs on a variety of platforms. The following instructions are loosely based on the `RUNNING.txt` file delivered with Apache Tomcat:

1. Extract the JDK download file:

   ```bash
   $ mkdir -p /path/to/JDK
   $ unzip ~/Downloads/openjdk-X_bin.zip -d /path/to/JDK
   ```

2. Extract the Apache Tomcat download file:

   ```bash
   $ mkdir -p /path/to/tomcat
   $ unzip ~/Downloads/apache-tomcat-X.X.XX.zip -d /path/to/tomcat
   ```

3. Create an Apache Tomcat script to set the `JAVA_HOME` environment variable to the file system location of the JDK and to set the heap and metaspace size appropriately. For example:

   * Unix/Linux

   * Windows

   Create a `setenv.sh` script in `/path/to/tomcat/bin/`:

   ```bash
   export JAVA_HOME="/path/to/usr/jdk"
   export CATALINA_OPTS="$CATALINA_OPTS -Xmx2g -XX:MaxMetaspaceSize=256m"
   ```

   Create a `setenv.bat` script in `\path\to\tomcat\bin\`:

   ```powershell
   PS C:\path\to> $env:JAVA_HOME += ";C:\path\to\usr\jdk"
   PS C:\path\to> $env:CATALINA_OPTS += ";-Xmx2g -XX:MaxMetaspaceSize=256m"
   ```

4. (UNIX-like systems only) Make the scripts in Apache Tomcat's `bin/` directory executable:

   ```bash
   $ chmod +x /path/to/tomcat/bin/*.sh
   ```

5. If you have a custom installation that differs from the documented Apache Tomcat installation, make sure to set Apache Tomcat's `CATALINA_TMPDIR` to a writable directory to ensure the installation succeeds. This temporary directory is used by the JVM (`java.io.tmpdir`) to write disk-based storage policies and other temporary files.

6. Make sure your system's firewall doesn't block the port that Apache Tomcat uses (`8080` by default).

   Read the Apache documentation for instructions for allowing traffic through the firewall on a specific port for the version of Apache Tomcat on your system. A variety of firewalls are in use on Linux systems. The version your system uses depends on your specific distribution.

7. Start Apache Tomcat:

   ```bash
   $ /path/to/tomcat/bin/startup.sh
   ```

   It might take Apache Tomcat several seconds to start. When it has successfully started, you should see information indicating how long startup took in the `/path/to/tomcat/logs/catalina.out` log file.

   ```
   INFO: Server startup in 4655 ms
   ```

8. Go to Apache Tomcat's homepage. For example, `http://am.example.com:8080`.

   If Apache Tomcat works correctly, the homepage displays a success message: "If you're seeing this, you've successfully installed Tomcat. Congratulations!".

9. Proceed to [Step 2. Prepare your datastore](step-2-prepare-data-store.html).

---

---
title: Step 2. Prepare your datastore
description: Prepare a PingDS datastore as a configuration store, identity store, and CTS token store for PingAM evaluation
component: pingam
version: 8.1
page_id: pingam:evaluation:step-2-prepare-data-store
canonical_url: https://docs.pingidentity.com/pingam/8.1/evaluation/step-2-prepare-data-store.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Evaluation", "Install"]
page_aliases: ["eval-guide:step-2-prepare-data-store.adoc"]
section_ids:
  create-deployment-id: Create a deployment ID
  prepare-am-trust-store: Create a truststore for AM
  install-ds: Install DS
---

# Step 2. Prepare your datastore

To prepare a single DS server as a configuration store, identity store, and CTS token store for evaluation purposes, perform the following tasks:

## Create a deployment ID

1. Unzip the DS `.zip` file into the file system directory where you want to install the server.

   ```bash
   $ unzip ~/Downloads/DS-8.1.1.zip -d /path/to/opendj
   ```

2. Generate a deployment ID using a deployment ID password of `password`.

   ```bash
   $ /path/to/opendj/bin/dskeymgr \
   create-deployment-id \
   --deploymentIdPassword password
   deployment-id
   ```

   You'll use this deployment ID and password when setting up your DS server and generating the keys required to connect securely from AM to DS:

   |   |                                                                                                     |
   | - | --------------------------------------------------------------------------------------------------- |
   |   | When configuring DS for real-world use, don't use this password. It is only to get started with AM. |

3. Save the deployment ID as an environment variable:

   ```bash
   $ export DEPLOYMENT_ID=deployment-id
   ```

## Create a truststore for AM

These steps create a copy of the default JVM truststore, and configure the AM web application container to use the new truststore:

1. Copy the default truststore. For example, `$JAVA_HOME/lib/security/cacerts`, name it `truststore`, and place it in a directory of your choice:

   ```bash
   $ cp $JAVA_HOME/lib/security/cacerts /path/to/truststore
   ```

   |   |                                                                                                                                                                                                                                                                                                                     |
   | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | If you place the truststore in the `/path/to/am` directory *before* you install AM, the installation process detects the directory isn't empty and the installation fails.After AM is installed, you can move the truststore to a different directory. For example, the `/path/to/am/security/keystores` directory. |

   The default password of the `$JAVA_HOME/lib/security/cacerts` truststore is `changeit`. In a production deployment, you should change the default truststore password. Read the documentation for your JVM for instructions.

2. Export the DS certificate.

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

3. Import the DS CA certificate into the new truststore:

   ```bash
   $ keytool \
   -importcert \
   -file /path/to/ca-cert.pem \
   -keystore /path/to/truststore
   -storepass truststore-password
   ```

   Confirm you trust this certificate when prompted.

4. To configure the truststore in Apache Tomcat so that AM can access it, append the truststore settings to the `CATALINA_OPTS` variable in the `setenv` file.

   For example:

   * Linux

   * Windows

   In `$CATALINA_BASE/bin/setenv.sh`:

   ```bash
   export CATALINA_OPTS="$CATALINA_OPTS -server -Xmx2g -XX:MetaspaceSize=256m -XX:MaxMetaspaceSize=256m \
   -Djavax.net.ssl.trustStore=/path/to/truststore \
   -Djavax.net.ssl.trustStorePassword=new-password \
   -Djavax.net.ssl.trustStoreType=jks"
   ```

   In `$CATALINA_BASE/bin/setenv.bat`:

   ```powershell
   set "CATALINA_OPTS=%CATALINA_OPTS% -server -Xmx2g -XX:MetaspaceSize=256m -XX:MaxMetaspaceSize=256m -
   -Djavax.net.ssl.trustStore=/path/to/truststore -
   -Djavax.net.ssl.trustStorePassword=new-password -
   -Djavax.net.ssl.trustStoreType=jks"
   ```

   Read your specific container's documentation for information on configuring truststores.

   After AM is installed, you can move the truststore to a different location. For example, the `/path/to/am/security/keystores/`. If you do, remember to update the truststore path in the container configuration.

## Install DS

These steps install DS as the configuration store, identity store, and CTS token store.

1. Use the `setup` command to install DS with the `am-config`, `am-cts`, and `am-identity-store` profiles. For example:

   ```bash
   $ /path/to/opendj/setup \
   --deploymentId $DEPLOYMENT_ID \
   --deploymentIdPassword password \
   --rootUserDN uid=admin \
   --rootUserPassword str0ngAdm1nPa55word \
   --monitorUserPassword str0ngMon1torPa55word \
   --hostname ds.example.com \
   --adminConnectorPort 4444 \
   --ldapPort 1389 \
   --enableStartTls \
   --ldapsPort 1636 \
   --profile am-config \
   --set am-config/amConfigAdminPassword:5up35tr0ng \
   --profile am-cts \
   --set am-cts/amCtsAdminPassword:5up35tr0ng \
   --set am-cts/tokenExpirationPolicy:am-sessions-only \
   --profile am-identity-store \
   --set am-identity-store/amIdentityStoreAdminPassword:5up35tr0ng \
   --start \
   --acceptLicense
   ```

   Learn more about installing DS in the [PingDS Installation documentation](https://docs.pingidentity.com/pingds/8.1/install-guide/preface.html).

2. Restart Tomcat:

   ```bash
   $ /path/to/tomcat/bin/shutdown.sh
   $ /path/to/tomcat/bin/startup.sh
   ```

3. Proceed to [Step 3. Deploy AM](step-3-deploy-am.html).

---

---
title: Step 3. Deploy AM
description: Deploy PingAM into Apache Tomcat and configure the default amAdmin user, server settings, configuration data store, and user data store
component: pingam
version: 8.1
page_id: pingam:evaluation:step-3-deploy-am
canonical_url: https://docs.pingidentity.com/pingam/8.1/evaluation/step-3-deploy-am.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Evaluation", "Deployment"]
page_aliases: ["eval-guide:step-3-deploy-am.adoc"]
---

# Step 3. Deploy AM

Deploying AM creates a default configuration you can access as AM's administrative user, `amAdmin`.

Deploy AM into Apache Tomcat and configure it for use:

1. Copy the AM `.war` file to deploy in Apache Tomcat as `am.war` :

   ```bash
   $ cp AM-8.1.1.war /path/to/tomcat/webapps/am.war
   ```

   It can take Apache Tomcat several seconds to deploy AM.

2. Go to the deployed AM application. For example, `http://am.example.com:8080/am`.

3. On the initial configuration page, click Create New Configuration.

4. Review the software license agreement. If you agree to the license, click I accept the license agreement, and click Continue.

5. Set the Default User \[amAdmin] password to `changeit`, and click Next.

   |   |                                                                                                                                                                                                        |
   | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
   |   | Don't use this password when configuring AM for real-world use. It is only to get started with AM. The `amAdmin` user is the default AM administrator, who has full control over the AM configuration. |

6. On the Server Settings page, enter the following details and click Next:

   * Server URL

     `http://am.example.com:8080`

   * Cookie Domain

     `am.example.com`

   * Platform Locale

     `en_US`

   * Configuration Directory

     `<$HOME>/am` making sure you replace `<$HOME>` with the full path to your `$HOME` directory.

7. On the Configuration Data Store Settings page, enter the following details and click Next:

   * SSL/TLS Enabled

     Select this option to use LDAPS to communicate with the configuration store. DS is configured for LDAPS by default.

   * Host Name

     `ds.example.com`

   * Port

     `1636`

   * Encryption Key

     Keep the randomly generated key.

   * Root Suffix

     `ou=am-config`

   * Login ID

     `uid=am-config,ou=admins,ou=am-config`

   * Password

     `5up35tr0ng`

   * Server configuration

     Leave the `New deployment` option selected.

8. On the User Data Store page, enter the following details and click Next:

   * User Data Store Type

     Leave the `ForgeRock Directory Services (DS)` option selected.

   * SSL/TLS Enabled

     Select this option to use a secure connection.

   * Directory Name

     `ds.example.com`

   * Port

     `1636`

   * Root Suffix

     `ou=identities`

   * Login ID

     `uid=am-identity-bind-account,ou=admins,ou=identities`

   * Password

     `5up35tr0ng`

9. On the Site Configuration page, leave the `No` option selected and click Next.

10. Check the details on the Configurator Summary page.

    * If anything needs changing, click Previous to return to earlier pages and update as needed.

    * If everything is correct, click Create Configuration to proceed. The configuration progress is shown in the browser and also output to the installation log.

    |   |                                                                                                                                        |
    | - | -------------------------------------------------------------------------------------------------------------------------------------- |
    |   | If your installation fails, find troubleshooting advice in [Troubleshoot installations](../installation/install-troubleshooting.html). |

11. When the configuration process completes, click Proceed to Login, and log in as the `amAdmin` administrator with the password you configured in a previous step,`changeit`.

    After logging in, the Realms page is displayed.

    AM stores its configuration in a directory named after the deployment URI. For example, if AM is deployed under `/am`, it saves its configuration under `$HOME/am/`.

    AM is now configured, and ready for use.

12. After successfully logging in to the AM admin UI, proceed to [Step 4. Configure AM](step-4-configure-am.html).

---

---
title: Step 4. Configure AM
description: Configure PingAM with minimum configuration to authenticate a user by creating a realm, setting up an authentication tree, and creating a test user
component: pingam
version: 8.1
page_id: pingam:evaluation:step-4-configure-am
canonical_url: https://docs.pingidentity.com/pingam/8.1/evaluation/step-4-configure-am.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Evaluation", "Setup &amp; Configuration", "Nodes &amp; Trees"]
page_aliases: ["eval-guide:step-4-configure-am.adoc"]
section_ids:
  create-alpha-realm: Create a realm
  configure-authentication-trees: Configure an authentication tree
  create-test-user: Create a test user
---

# Step 4. Configure AM

To configure AM with the minimum configuration needed to authenticate a user, perform these tasks.

## Create a realm

1. On the Realms page of the AM admin UI, click New Realm.

2. Enter `alpha` for the realm name and click Create.

Learn more in [Realms](../setup/am-realms.html).

## Configure an authentication tree

Authentication trees provide fine-grained authentication by allowing multiple paths and decision points throughout the authentication flow.

Authentication trees are made up of authentication nodes, which define actions taken during authentication. Authentication nodes are granular, with each node performing a single task, such as collecting a username or making a simple decision. Authentication nodes can have multiple outcomes rather than just success or failure.

|   |                                                                                                                                                                                                         |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | AM provides a number of sample authentication trees to demonstrate how nodes can be put together. Find information on setting up authentication trees in [Trees](../am-authentication/auth-trees.html). |

Follow these steps to create an authentication tree that you can use to log in to AM:

1. On the Realms page of the AM admin UI, select the `alpha` realm.

2. Select Authentication > Trees from the menu on the left and click Create Tree.

3. Enter `myAuthTree` for the tree name and click Create.

   The authentication tree designer is displayed, with the `Start` entry point connected to the `Failure` exit point, and a `Success` node.

   The authentication tree designer provides the following features on the toolbar:

   **Authentication tree designer toolbar**

   | Button                                                      | Usage                                                                          |
   | ----------------------------------------------------------- | ------------------------------------------------------------------------------ |
   | ![Trees auto layout](../_images/icon-trees-auto-layout.png) | Lay out and align nodes according to the order they are connected.             |
   | ![Trees full screen](../_images/icon-trees-full-screen.png) | Toggle the designer window between normal and full-screen layout.              |
   | ![Trees delete node](../_images/icon-trees-delete-node.png) | Remove the selected node. Note that the `Start` entry point cannot be deleted. |

4. Drag the following nodes from the Components panel on the left-hand side and drop them into the designer area:

   * [Page node](https://docs.pingidentity.com/auth-node-ref/8.1/page.html)

   * [Username Collector node](https://docs.pingidentity.com/auth-node-ref/8.1/am-only/username-collector.html)

   * [Password Collector node](https://docs.pingidentity.com/auth-node-ref/8.1/am-only/password-collector.html)

   * [Data Store Decision node](https://docs.pingidentity.com/auth-node-ref/8.1/data-store-decision.html)

   The Data Store Decision authentication node uses the credentials to authenticate the user against the identity stores configured for the realm. In this example, the username and password are obtained by a combination of the Username Collector and Password Collector nodes.

5. Drag and drop the Username Collector and Password Collector onto the Page node, so that they will both appear on the same page when logging in.

6. Connect the nodes as follows:

   ![A tree that can be used to authenticate a user.](_images/trees-node-login-example.png)

   |   |                                                                                                                                                                                                                              |
   | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | You can configure the node properties by using the panel on the right side of the page. Find more information on the available properties for each node in [Node reference](../am-authentication/auth-nodes-reference.html). |

   Find more information on setting up more complex authentication trees in [Trees](../am-authentication/auth-trees.html).

## Create a test user

Follow these steps to create a test user that you can use to log in to AM:

1. On the Realms page of the AM admin UI, select the `alpha` realm.

2. Select Identities from the menu on the left and click Add Identity.

3. Create a test user with the following details and click Create.

   * User ID

     `bjensen`

   * Password

     `Ch4ng31t`

   * Email address

     `bjensen@example.com`

4. Add the following details and click Save Changes.

   * First Name

     `Babs`

   * Last Name

     `Jensen`

   * Full Name

     `Babs Jensen`

5. You're now ready to authenticate your test user!

   Proceed to [Step 5. Authenticate to AM](step-5-try-am.html).

---

---
title: Step 5. Authenticate to AM
description: Test authentication to PingAM using an authentication tree, log in as a demo user, and understand how SSO tokens and authenticated sessions work
component: pingam
version: 8.1
page_id: pingam:evaluation:step-5-try-am
canonical_url: https://docs.pingidentity.com/pingam/8.1/evaluation/step-5-try-am.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Evaluation", "Authentication", "Sessions"]
page_aliases: ["eval-guide:step-5-try-am.adoc"]
---

# Step 5. Authenticate to AM

After you've completed [Step 4. Configure AM](step-4-configure-am.html), you can use the `myAuthTree` you created to authenticate `bjensen` in the `alpha` realm.

To test your authentication tree in a web browser, go to a URL similar to the following:

```none
http://am.example.com:8080/am/XUI/?realm=alpha&service=myAuthTree
```

Use the correct FQDN, port number, and deployment path for your environment. Also make sure you use the correct authentication tree name and realm. In the example above, the tree is named `myAuthTree` and the realm is called `alpha`.

Log in as `bjensen`, with the password `Ch4ng31t`.

![Log in as bjensen as described in the instructions.](_images/openam-login.png)

On successful login, AM creates a cookie named `iPlanetDirectoryPro` in your browser for your domain; for example, `example.com`. That cookie is then available to all servers in the `example.com` domain, such as `am.example.com`.

If you examine this cookie, you see that it has a value such as `AQI5wM2L...*AAJTS...`. This is the SSO token value. The value is an encrypted reference to the session that is stored only by AM. Only AM can determine whether you are actually logged in, or whether the authenticated session is no longer valid, and you need to reauthenticate.

The AM authenticated session is used for SSO. When the browser presents the cookie to a server in the domain, the agent on the server can check with AM using the SSO Token as a reference to the session. This lets AM make policy decisions based on who is authenticated, or prompt for additional authentication, if necessary.

Your authenticated session can end in a few ways. For example, when examining the cookie in your browser, you should notice that it expires when the browser session ends (when you shut down your browser). Alternatively, you can log out of AM explicitly.

Authenticated sessions can also expire. AM sets two limits: one that causes your authenticated session to expire if it remains inactive for a configurable period of time (default: 30 minutes), and another that caps the authenticated session lifetime (default: 2 hours).

Congratulations on authenticating your first user with AM!

See what else can AM do for you by reading [Next steps](next-steps.html).