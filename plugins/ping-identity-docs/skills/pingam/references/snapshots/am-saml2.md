---
title: Configure IdPs and SPs with trees
description: Configure authentication trees for SAML 2.0 identity and service providers to customize single sign-on flows and enforce additional security requirements
component: pingam
version: 8.1
page_id: pingam:am-saml2:configure-providers
canonical_url: https://docs.pingidentity.com/pingam/8.1/am-saml2/configure-providers.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["SAML 2.0", "Single Sign-on (SSO)", "Federation"]
section_ids:
  config-redirect-tree: Redirect to a tree on the hosted SP
  samlapp-tree: Set a SAML 2.0 application tree for a remote SP
---

# Configure IdPs and SPs with trees

After you have set up the entity providers, you can tailor the SAML 2.0 flow to your business needs by configuring the provider settings.

## Redirect to a tree on the hosted SP

For [IdP-initiated SSO in integrated mode](saml2-integrated-mode.html#idpinit-sso-integrated-mode), you must configure the hosted SP to send the user to an authentication tree after validating the SAML 2.0 assertion from the IdP. This lets you perform SAML 2.0 authentication on the SP side.

You can also define additional actions the user must fulfill, such as performing multi-factor authentication or checking organizational details before accessing the SAML 2.0 application.

|   |                                                                                                                                    |
| - | ---------------------------------------------------------------------------------------------------------------------------------- |
|   | Include a Scripted Decision node in the tree and query the `samlApplication` binding to access the assertion and response details. |

If a `local authentication URL` is configured, it takes precedence, but AM doesn't validate that the specified tree exists on the hosted SP.

If you haven't configured a tree in either setting, an IdP-initiated SSO SAML flow results in an invalid request error.

For SP-initiated SSO, the flow continues in the originating tree, ignoring any redirect tree configured on the hosted SP.

To configure a redirect tree:

1. Go to Realms > *realm name* > Applications > Federation > Entity Providers > *Hosted SP Name*.

2. Under Assertion Processing > Redirect Tree, select the name of your authentication tree from the Redirect Tree Name list.

   Learn about the `Redirect Tree Name` property in the [hosted SP configuration](saml2-reference.html#config-redirect-tree).

3. Save your changes.

|   |                                                                            |
| - | -------------------------------------------------------------------------- |
|   | You can't delete a tree if it's set as the redirect tree in the hosted SP. |

## Set a SAML 2.0 application tree for a remote SP

Configure the remote SP so that a specific authentication tree is always run for users authenticating with your SAML 2.0 app. The SAML flow invokes the associated tree regardless of any existing sessions or requested or configured authentication contexts.

To configure a SAML 2.0 app tree:

1. Go to Realms > *realm name* > Applications > Federation > Entity Providers > *Remote SP Name*.

2. Under Advanced > Tree Name, select the name of your authentication tree from the list.

   Learn about the `Tree Name` property in the [remote SP configuration](saml2-reference.html#config-treename).

3. Save your changes.

When you configure an app tree, the processing of the SAML request depends on the authentication context requested by the SP. The following table shows the SAML response for a configured comparison type and the requested authentication context.

| Authentication context                     | Comparison type                  | Response                         |
| ------------------------------------------ | -------------------------------- | -------------------------------- |
| SP requested authn context                 | `Exact` / `None`                 | Requested authn context included |
| SP requested authn context                 | `Better` / `Maximum` / `Minimum` | `UNSPECIFIED`                    |
| SP doesn't request authn context           | -                                | `UNSPECIFIED`                    |
| IdP-initiated (no requested authn context) | -                                | `UNSPECIFIED`                    |

|   |                                                                                                                                                                                                                                                                                                                                                                                    |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | * To prevent users from authenticating directly through this tree, either for security reasons or because the tree is insufficient as a complete authentication service, configure it as a [transactional authentication tree](../am-authentication/configure-auth-trees.html#configure-transactional-auth-tree).

* You can't delete a tree if it's referenced by a SAML 2.0 app. |

---

---
title: Create and configure the Fedlet
description: Create and configure a Java Fedlet to add SAML 2.0 service provider capabilities to your web application
component: pingam
version: 8.1
page_id: pingam:am-saml2:create-configure-fedlet
canonical_url: https://docs.pingidentity.com/pingam/8.1/am-saml2/create-configure-fedlet.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["SAML 2.0", "Single Sign-on (SSO)", "Federation", "Fedlet", "Java", "URI", "Logs", "Cryptographic Keys"]
page_aliases: ["saml2-guide:create-configure-fedlet.adoc"]
section_ids:
  unconfigured-fedlet-conf: Contents of the Java Fedlet distribution .zip file
  unconfigured-fedlet-properties: Configuring Java Fedlet Properties
  deployment_url_settings: Deployment URL settings
  log_and_statistics_settings: Log and Statistics Settings
  unconfigured-fedlet-properties-keys: Public and private key settings
  alternative-impl-settings: Alternative implementation settings
  unconfigured-fedlet-cot: Configure circles of trust
  unconfigured-fedlet-cot-single: Configure a circle of trust with a single IdP
  unconfigured-fedlet-cot-discovery: Configure a circle of trust with multiple IdPs
  unconfigured-fedlet-cot-multiple: Configure multiple circles of trust
  unconfigured-fedlet-idp: Configure the IdPs
  unconfigured-fedlet-idp-standard: IdP standard XML
  unconfigured-fedlet-idp-extended: IdP extended XML
  unconfigured-fedlet-idp-extended-idpssoconfig: "Identity provider extended XML: IDPSSOConfig settings"
  unconfigured-fedlet-sp: Configure the SPs
  unconfigured-fedlet-sp-standard: Service provider standard XML
  unconfigured-fedlet-sp-standard-sso: "Single Sign-On and Logout: SPSSODescriptor Element"
  unconfigured-fedlet-sp-extended: Service Provider Extended XML
  unconfigured-fedlet-sp-extended-spssoconfig: "Service Provider Extended XML: SPSSOConfig Settings"
  unconfigured-fedlet-sp-extended-attributequeryconfig: "Service Provider Extended XML: AttributeQueryConfig Settings"
  unconfigured-fedlet-sp-extended-xacmlauthzdecisionqueryconfig: "Service Provider Extended XML: XACMLAuthzDecisionQueryConfig Settings"
---

# Create and configure the Fedlet

An AM Fedlet is a small web application that makes it easy to add SAML 2.0 service provider (SP) capabilities to your Java web application.

The full AM distribution file, `AM-8.1.1.zip`, includes the Java Fedlet package, `Fedlet-8.1.1.zip`, that you can use as the basis of your Fedlet. This section covers how to configure a Java Fedlet using that distribution, by editing the circle of trust, Java properties, and IdP and SP XML configuration templates.

The high-level steps are:

* Determine the roles that the IdP(s) and Fedlet play in SAML 2.0 Circles of Trust.

* Unpack the Fedlet from the full AM distribution `.zip` file to access the Fedlet `.war` file and template configuration files.

* Prepare the Fedlet configuration, including setting up a configuration directory and keystore if needed.

* Obtain SAML 2.0 metadata configuration files from the IdP(s), and add them to the Fedlet configuration.

* Finish preparing the Fedlet configuration by editing the remaining Fedlet template configuration files.

* Share the Fedlet SAML 2.0 configuration files with the IdP(s).

  An IdP relies on the standard SAML 2.0 metadata to communicate with the Fedlet.

* Deploy and test the Fedlet.

## Contents of the Java Fedlet distribution `.zip` file

Unpack the Java Fedlet distribution `.zip` file into a working directory:

```bash
$ mkdir fedlet && cd fedlet
$ unzip ../Fedlet-8.1.1.zip
```

The `Fedlet-8.1.1.zip` file contains the following files:

* `fedlet.war`

  This file contains a Java Fedlet web application that serves as an example, and that you can embed in your applications.

* `README`

  This file describes Fedlet features.

* `conf/`

  This folder contains the Fedlet configuration templates that you edit as appropriate for your deployment.

  When editing the templates, place copies of the files in the Fedlet home directory on the system where you deploy the Fedlet. By default the Fedlet home directory is `user.home/uri`, where *user.home* is the value of the Java system property `user.home` for the user running the web container where you deploy the Fedlet, and *uri* is the path of the URI where you deploy the Fedlet, such as `/fedlet`.

  For example, if *user.home* is the `/home/user` folder, that user could have a `/home/user/fedlet` folder for Fedlet configuration files:

  ```bash
  $ mkdir ~/fedlet
  ```

  |   |                                                                                                                                                                                                            |
  | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | To change the location, set the system property `com.sun.identity.fedlet.home` when starting the container where the Fedlet runs:```bash
  $ java -Dcom.sun.identity.fedlet.home=/path/to/fedlet/conf …​
  ``` |

* `conf/FederationConfig.properties`

  This file defines settings for the Fedlet as a web application. It doesn't address the SAML 2.0 configuration.

  Find more information about this file in [Configuring Java Fedlet Properties](#unconfigured-fedlet-properties).

* `conf/fedlet.cot-template`

  This template defines settings for a SAML 2.0 circle of trust to which the Fedlet belongs, and should be named `fedlet.cot` after configuration.

  Find more information about this file in [Configure circles of trust](#unconfigured-fedlet-cot).

* `conf/idp.xml` (not provided)

  The `idp.xml` file is standard SAML 2.0 metadata that describes the IdP configuration.

  Templates for other SAML 2.0 configuration files are provided, but no `idp.xml` template file is provided.

  Instead you must obtain the SAML 2.0 metadata from the IdP, and add it as an `idp.xml` file here, alongside the other SAML 2.0 configuration files. How you obtain this file from the IdP depends on the IdP implementation.

  Learn more about obtaining this information from an AM instance in [Create a hosted IdP or SP](saml2-providers-and-cots.html#create-hosted-providers).

* `conf/idp-extended.xml-template`

  This template holds extended SAML 2.0 IdP settings that AM uses, and should be named `idp-extended.xml` after configuration.

  Find more information about this file in [Configure the IdPs](#unconfigured-fedlet-idp).

* `conf/sp.xml-template`

  This template describes standard SAML 2.0 SP settings, and should be named `sp.xml` after configuration.

  Find more information about this file in [Configure the SPs](#unconfigured-fedlet-sp).

* `conf/sp-extended.xml-template`

  This template describes extended SAML 2.0 SP settings that the Fedlet uses, and should be named `sp-extended.xml` after configuration.

  Find more information about this file in [Configure the SPs](#unconfigured-fedlet-sp).

To configure a Fedlet, make copies of the template files listed above, configure the necessary properties and values, and provide the resulting files to the person administering the SP, ready to deploy. Learn more in [Deploy and test the Fedlet on the SP](fedlet-deploy-test.html).

## Configuring Java Fedlet Properties

**File: `FederationConfig.properties`**

The Java Fedlet to configure by hand includes a `FederationConfig.properties` file that defines settings for the Fedlet as a web application. The configuration for a single Java Fedlet includes only one `FederationConfig.properties` file, regardless of how many IdP and SP configurations are involved. This file doesn't address the SAML 2.0 configuration.

When configured this file contains sensitive properties such as the value of `am.encryption.pwd`. Make sure it's readable only by the user running the Fedlet application.

### Deployment URL settings

The following settings define the Fedlet deployment URL.

* `com.iplanet.am.server.protocol`

  Set this to the protocol portion of the URL, such as HTTP or HTTPS.

* `com.iplanet.am.server.host`

  Set this to the host portion of the URL, such as `www.sp.com`.

* `com.iplanet.am.server.port`

  Set this to the port portion of the URL, such as 80, 443, 8080, or 8443.

* `com.iplanet.am.services.deploymentDescriptor`

  Set this to path portion of the URL, starting with a `/`, such as `/fedlet`.

### Log and Statistics Settings

The following settings define the Fedlet configuration for logging and monitoring statistics.

* `com.iplanet.am.logstatus`

  This sets whether the Fedlet actively writes debug log files.

  Default: `ACTIVE`

* `com.iplanet.services.debug.level`

  This sets the debug log level.

  The following settings are available, in order of increasing verbosity:

  1. `off`

  2. `error`

  3. `warning`

  4. `message`

  Default: `message`

* `com.iplanet.services.debug.directory`

  This sets the location of the debug log folder.

  Trailing spaces in the file names are significant. Even on Windows systems, use slashes to separate directories.

  Examples: `/home/user/fedlet/debug`, `C:/fedlet/debug`

* `com.iplanet.am.stats.interval`

  This sets the interval at which statistics are written, in seconds.

  The shortest interval supported is 5 seconds. Settings less than 5 (seconds) are taken as 5 seconds.

  Default: `60`

* `com.iplanet.services.stats.state`

  This sets how the Fedlet writes monitoring statistics.

  The following settings are available:\
  `off`\
  `console` (write to the container logs)\
  `file` (write to Fedlet stats logs)

  Default: `file`

* `com.iplanet.services.stats.directory`

  This sets the location of the stats file folder.

  Trailing spaces in the file names are significant. Even on Windows systems, use slashes to separate directories.

  Examples: `/home/user/fedlet/stats`, `C:/fedlet/stats`

### Public and private key settings

The following settings define settings for access to certificates and private keys used in signing and encryption.

Other sections in this guide explain how to configure a Fedlet for signing and encryption including how to work with the keystores that these settings reference, and how to specify public key certificates in standard SAML 2.0 metadata. Learn more in [Enable signing and encryption in a Fedlet](fedlet-sign-encrypt.html) if you're working with a Java Fedlet.

* `com.sun.identity.saml.xmlsig.keystore`

  This sets the path to the keystore file that holds public key certificates of IdPs and key pairs for the Fedlet.

  Find information on generating a keystore file with a key pair in [Change default key aliases](../security/change-signing-key.html).

  Example: `@FEDLET_HOME@/keystore.jceks`

* `com.sun.identity.saml.xmlsig.storepass`

  This sets the path to the file that contains the keystore password encoded by using the symmetric key set as the value of `am.encryption.pwd`.

  When creating the file, encode the cleartext password by using your own test copy (not a production version) of AM.

  * In the AM admin UI, go to Deployment > Servers > *server name* > Security > Encryption, and set the Password Encryption Key to your symmetric key.

    Don't do this in a production system where the existing symmetric key is already in use!

  * Switch to the `encode.jsp` page, such as `https://am.example.com:8443/am/encode.jsp`, enter the cleartext password to encode with your symmetric key, and select Encode.

  * Copy the encoded password to your file.

  Example: `@FEDLET_HOME@/.storepass`

* `com.sun.identity.saml.xmlsig.keypass`

  This sets the path to the file that contains the private key password encoded by using the symmetric key set as the value of `am.encryption.pwd`.

  To encode the cleartext password, follow the same steps for the password used when setting `com.sun.identity.saml.xmlsig.storepass`.

  Example: `@FEDLET_HOME@/.keypass`

* `com.sun.identity.saml.xmlsig.certalias`

  This sets the alias of the Fedlet's public key certificate.

  Example: `fedlet-cert`

* `com.sun.identity.saml.xmlsig.storetype`

  The sets the type of keystore.

  Default: `JKS` (`JCEKS` is recommended.)

* `am.encryption.pwd`

  This sets the symmetric key that used to encrypt and decrypt passwords.

  Example: `uu4dHvBkJJpIjPQWM74pxH3brZJ5gJje`

### Alternative implementation settings

The Java Fedlet properties file includes settings that let you plug in alternative implementations of Fedlet capabilities. You can safely use the default settings, as specified in the following list. The list uses the same order for the keys you find in the file.

* `com.sun.identity.plugin.configuration.class`

  Default: `com.sun.identity.plugin.configuration.impl.FedletConfigurationImpl`

* `com.sun.identity.plugin.datastore.class.default`

  Default: `com.sun.identity.plugin.datastore.impl.FedletDataStoreProvider`

* `com.sun.identity.plugin.log.class`

  Default: `com.sun.identity.plugin.log.impl.FedletLogger`

* `com.sun.identity.plugin.session.class`

  Default: `com.sun.identity.plugin.session.impl.FedletSessionProvider`

* `com.sun.identity.plugin.monitoring.agent.class`

  Default: `com.sun.identity.plugin.monitoring.impl.FedletAgentProvider`

* `com.sun.identity.plugin.monitoring.saml2.class`

  Default: `com.sun.identity.plugin.monitoring.impl.FedletMonSAML2SvcProvider`

* `com.sun.identity.plugin.monitoring.idff.class`

  Default: `com.sun.identity.plugin.monitoring.impl.FedletMonIDFFSvcProvider`

* `com.sun.identity.saml.xmlsig.keyprovider.class`

  Default: `com.sun.identity.saml.xmlsig.JKSKeyProvider`

  Despite the name, this provider supports JCEKS keystores.

* `com.sun.identity.saml.xmlsig.signatureprovider.class`

  Default: `com.sun.identity.saml.xmlsig.AMSignatureProvider`

* `com.sun.identity.common.serverMode`

  Default: `false`

* `com.sun.identity.webcontainer`

  Default: `WEB_CONTAINER`

* `com.sun.identity.saml.xmlsig.passwordDecoder`

  Default: `com.sun.identity.fedlet.FedletEncodeDecode`

* `com.iplanet.services.comm.server.pllrequest.maxContentLength`

  Default: `16384`

* `com.iplanet.security.SecureRandomFactoryImpl`

  Default: `com.iplanet.am.util.SecureRandomFactoryImpl`

* `com.iplanet.security.SSLSocketFactoryImpl`

  Default: `com.sun.identity.shared.ldap.factory.JSSESocketFactory`

* `com.iplanet.security.encryptor`

  Default: `com.iplanet.services.util.JCEEncryption`

* `com.sun.identity.jss.donotInstallAtHighestPriority`

  Default: `true`

* `com.iplanet.services.configpath`

  Default: `@BASE_DIR@`

## Configure circles of trust

**File: `fedlet.cot`**

This file defines settings for a SAML 2.0 circle of trust. The Fedlet belongs to at least one circle of trust.

### Configure a circle of trust with a single IdP

When the Fedlet is involved in only a single circle of trust with one IdP and the Fedlet as an SP, the only settings to change are `cot-name` and `sun-fm-trusted-providers`.

1. Save a copy of the template as a `fedlet.cot` file in the configuration folder, as in the following example:

   ```bash
   $ cp ~/Downloads/fedlet/conf/fedlet.cot-template ~/fedlet/fedlet.cot
   ```

2. Set `cot-name` to the name of the circle of trust.

3. Set `sun-fm-trusted-providers` to a comma-separated list of the entity names for the IdP and SP.

   For example, if the IdP is AM with entity ID `https://am.example.com:8443/am` and the SP is the Fedlet with entity ID `https://sp.example.net:8443/fedlet`, then set the property as follows:

   ```properties
   sun-fm-trusted-providers=https://am.example.com:8443/am,https://sp.example.net:8443/fedlet
   ```

### Configure a circle of trust with multiple IdPs

When the circle of trust involves multiple IdPs, use the Fedlet in combination with the AM IdP Discovery service.

|   |                                                                                                         |
| - | ------------------------------------------------------------------------------------------------------- |
|   | For this to work, the IdPs must be configured to use IdP discovery, and users must have preferred IdPs. |

1. Set up the AM IdP Discovery service.

   Learn more in [Deploy the IdP Discovery service](deploy-idp-discovery.html).

2. Configure the circle of trust as described in [Configure a circle of trust with a single IdP](#unconfigured-fedlet-cot-single), but specifying multiple IdPs, including the IdP that provides the IDP Discovery service.

3. Set the `sun-fm-saml2-readerservice-url` and the `sun-fm-saml2-writerservice-url` properties as defined for the IDP Discovery service.

### Configure multiple circles of trust

This procedure concerns deployments where the Fedlet participates as SP in multiple Circles of Trust, each involving their own IdP.

1. For each circle of trust, save a copy of the template in the configuration folder.

   The following example involves two circles of trust:

   ```bash
   $ cp ~/Downloads/fedlet/conf/fedlet.cot-template ~/fedlet/fedlet.cot
   $ cp ~/Downloads/fedlet/conf/fedlet.cot-template ~/fedlet/fedlet2.cot
   ```

2. Set up IdP XML files for each IdP as described in [Configure the IdPs](#unconfigured-fedlet-idp).

3. For each circle of trust, set up the cot file as described in [Configure a circle of trust with a single IdP](#unconfigured-fedlet-cot-single).

4. In the extended SP XML file described in [Configure the IdPs](#unconfigured-fedlet-idp), set the Attribute element with name `cotlist` to include values for all circles of trust. The values are taken from the `cot-name` settings in the cot files.

   The following example works with two circles of trust, `cot` and `cot2`.

   ```xml
   <Attribute name="cotlist">
       <Value>cot</Value>
       <Value>cot2</Value>
   </Attribute>
   ```

   The same Attribute element is also available in extended IdP XML files for cases where an IdP belongs to multiple circles of trust.

## Configure the IdPs

**Files: `idp.xml`, `idp-extended.xml`**

As described in [Contents of the Java Fedlet distribution `.zip` file](#unconfigured-fedlet-conf), the IdP provides its standard SAML 2.0 metadata as XML, which you save in the configuration folder as a `idp.xml` file. If the IdP uses AM, the IdP can also provide extended SAML 2.0 metadata as XML, which you save in the configuration folder as a `idp-extended.xml` file, rather than using the template for extended information.

If you have multiple IdPs, then number the configuration files, as in `idp.xml`, `idp2.xml`, `idp3.xml`, and also `idp-extended.xml`, `idp2-extended.xml`, `idp3-extended.xml`, and so on.

### IdP standard XML

This section covers the configuration in the `idp.xml` file. The `idp.xml` file contains standard SAML 2.0 metadata for an IdP in a circle of trust that includes the Fedlet as SP. The IdP provides you the content of this file.

If the IdP uses AM then the administrator can export the metadata using the `/ExportSamlMetadata` endpoint under the AM deployment URL.

If the IdP uses an implementation different from AM, read the documentation for details on obtaining the standard metadata. The standard, product-independent metadata are covered in [Metadata for the OASIS Security Assertion Markup Language (SAML) 2.0](http://docs.oasis-open.org/security/saml/v2.0/saml-metadata-2.0-os.pdf). The standard XML namespace describing the XML document has identifier `urn:oasis:names:tc:SAML:2.0:metadata`. An XML schema description for this namespace is found online at <http://docs.oasis-open.org/security/saml/v2.0/saml-schema-metadata-2.0.xsd>.

### IdP extended XML

This section covers the configuration in the `idp-extended.xml` file. Most extended metadata are specific to the AM implementation of SAML 2.0.

The extended metadata file describes an `EntityConfig` element, defined by the namespace with the identifier `urn:sun:fm:SAML:2.0:entityconfig`.

The unconfigured Fedlet includes a template file, `conf/idp-extended.xml-template`. This extended metadata template for the IdP requires that you edit at least the `IDP_ENTITY_ID` and `fedletcot` values to reflect the IdP entity ID used in the standard metadata and the circle of trust name defined in the `fedlet.cot` file, respectively. The `hosted` attribute on the `EntityConfig` element must remain set to `hosted="0"`, meaning that the IdP is remote. The IdP is likely to play at least the role of single sign-on IdP, though the namespace defines elements for the attribute authority and policy decision point roles shown in the template, as well as the others defined in the standard governing SAML 2.0 metadata.

The extended metadata file is essentially a series of XML maps of key-value pairs specifying IdP configuration for each role. All role-level elements can take a `metaAlias` attribute that the Fedlet uses when communicating with the IdP. Each child element of a role element defines an `Attribute` whose `name` is the key. Each `Attribute` element can contain multiple `Value` elements. The `Value` elements' contents comprise the values for the key. All values are strings, sometimes with a format that is meaningful to AM. The basic example in the IdP template shows the minimal configuration for the single sign-on IdP role.

In the following example, the `description` is empty and the name of the circle of trust is `fedletcot`.

```xml
<IDPSSOConfig>
   <Attribute name="description">
     <Value/>
   </Attribute>
   <Attribute name="cotlist">
     <Value>fedletcot</Value>
   </Attribute>
</IDPSSOConfig>
<AttributeAuthorityConfig>
   <Attribute name="cotlist">
     <Value>fedletcot</Value>
   </Attribute>
</AttributeAuthorityConfig>
<XACMLPDPConfig>
   <Attribute name="wantXACMLAuthzDecisionQuerySigned">
     <Value></Value>
   </Attribute>
   <Attribute name="cotlist">
     <Value>fedletcot</Value>
   </Attribute>
</XACMLPDPConfig>
```

### Identity provider extended XML: IDPSSOConfig settings

This section covers elements for the IdP single sign-on role, arranged in the order they appear in the template.

* `description`

  Description of the file.

* `cotlist`

  Specifies the circle of trust(s) to which the provider belongs.

  Default: `fedletcot`

## Configure the SPs

**Files: `sp.xml`, `sp-extended.xml`**

As mentioned in [Contents of the Java Fedlet distribution `.zip` file](#unconfigured-fedlet-conf), the Fedlet SAML 2.0 configuration is defined in two XML files, the standard metadata in a `sp.xml` file and the extended metadata in a `sp-extended.xml` file.

If the Fedlet has multiple SP personalities, then number the configuration files, as in `sp.xml`, `sp2.xml`, `sp3.xml`, and also `sp-extended.xml`, `sp2-extended.xml`, `sp3-extended.xml`, and so on.

### Service provider standard XML

This section covers the configuration in the `sp.xml` file. The `sp.xml` file contains standard SAML 2.0 metadata for the Fedlet as SP. If you edit the standard metadata, make sure that you provide the new version to your IdP, as the IdP software relies on the metadata to get the Fedlet's configuration.

The standard metadata are covered in [Metadata for the OASIS Security Assertion Markup Language (SAML) 2.0](http://docs.oasis-open.org/security/saml/v2.0/saml-metadata-2.0-os.pdf). The standard XML namespace describing the XML document has identifier `urn:oasis:names:tc:SAML:2.0:metadata`. An XML schema description for this namespace is found online at <http://docs.oasis-open.org/security/saml/v2.0/saml-schema-metadata-2.0.xsd>.

A standard metadata file describes the SAML 2.0 roles that the Fedlet plays. The default base element of the file is an `EntityDescriptor`, which is a container for role descriptor elements. The `EntityDescriptor` element can therefore contain multiple role descriptor elements. The namespace for the standard metadata document is `urn:oasis:names:tc:SAML:2.0:metadata`. You can get the corresponding XML schema description online at <http://docs.oasis-open.org/security/saml/v2.0/saml-schema-metadata-2.0.xsd>. In general, you can find standard SAML 2.0-related XML schema definitions at <http://docs.oasis-open.org/security/saml/v2.0/>.

Fedlets don't support all arbitrary SP configurations. As lightweight SP components, Fedlets are built to play the SP role in web single sign-on and single logout, to perform attribute queries and XACML policy decision requests, and to work with multiple IDPs including circles of trust with an IDP discovery service. Find a list of what Fedlets support in [Fedlet Support for SAML 2.0 Features](saml2-implementation-fedlet.html#fedlet-saml2-features).

When preparing a standard SP metadata file, follow these suggestions.

* Start either with an existing example or with the template file, `conf/sp.xml-template`.

* When using the template, replace the following placeholders.

  * `FEDLET_ENTITY_ID`

    The Fedlet entity ID used when communicating with the IdP.

    AM often uses the deployment URL as the entity ID, though that is a convention rather than a requirement.

  * `FEDLET_PROTOCOL`

    The Fedlet deployment protocol (`http`, `https`)

  * `FEDLET_HOST`

    The Fedlet deployment host name

  * `FEDLET_PORT`

    The Fedlet deployment port number

  * `FEDLET_DEPLOY_URI`

    The Fedlet application deployment path

* Add and edit role elements as children depending on the roles the Fedlet plays as described in the following sections.

#### Single Sign-On and Logout: SPSSODescriptor Element

Add an `SPSSODescriptor` element to play the SP role in web single sign-on and logout. An `SPSSODescriptor` element has attributes specifying whether requests and assertion responses should be digitally signed.

* The `AuthnRequestsSigned` attribute indicates whether the Fedlet signs authentication requests.

  If you set the `AuthnRequestsSigned` attribute to true, then you must also configure the `SPSSODescriptor` element to allow the Fedlet to sign requests. Learn more in [Enable signing and encryption in a Fedlet](fedlet-sign-encrypt.html).

* The `WantAssertionsSigned` attribute indicates whether the Fedlet requests signed assertion responses from the IdP.

An `SPSSODescriptor` element's children indicate what name ID formats the Fedlet supports, and where the IdP can call the following services on the Fedlet.

* The `AssertionConsumerService` elements specify endpoints that support the SAML Authentication Request protocols.

  You must specify at least one of these. The template specifies two, with the endpoint supporting the HTTP POST binding as the default.

* The optional `SingleLogoutService` elements specify endpoints that support the SAML Single Logout protocols.

### Service Provider Extended XML

This section covers the configuration in the `sp-extended.xml` file. The extended metadata are specific to the AM implementation of SAML 2.0.

The extended metadata file describes an `EntityConfig` element, defined by the namespace with the identifier `urn:sun:fm:SAML:2.0:entityconfig`.

The unconfigured Fedlet does include a template file, `conf/sp-extended.xml-template`. This extended metadata template for the IdP requires that you edit at least the `FEDLET_ENTITY_ID` placeholder value, the `appLogoutUrl` attribute value in the `SPSSOConfig` element, and the `fedletcot` values. The `FEDLET_ENTITY_ID` value must reflect the SP entity ID used in the standard metadata. For the single logout profile, the `appLogoutUrl` attribute value must match the Fedlet URL based on the values used in the `FederationConfig.properties` file. The `fedletcot` values must correspond to the circle of trust name defined in the `fedlet.cot` file.

The `hosted` attribute on the `EntityConfig` element must remain set to `hosted="1"`, meaning that the SP is hosted (local to the Fedlet). If you provide a copy of the file to your IdP running AM, however, then set `hosted="0"` for the IdP, as the Fedlet is remote to the IdP.

The extended metadata file is essentially a series of XML maps of key-value pairs specifying IdP configuration for each role. All role-level elements can take a `metaAlias` attribute that the Fedlet uses when communicating with the IdP. Each child element of a role element defines an `Attribute` whose `name` is the key. Each `Attribute` element can contain multiple `Value` elements. The `Value` elements' contents comprise the values for the key. All values are strings, sometimes with a format that is meaningful to the Fedlet. The basic example in the SP template shows the configuration options, documented in the following lists.

#### Service Provider Extended XML: SPSSOConfig Settings

This section covers elements for the SP single sign-on role, arranged in the order they appear in the template.

* `description`

  Human-readable description of the Fedlet in the SP single sign-on role

* `signingCertAlias`

  Alias of the public key certificate for the key pair used when signing messages to the IDP

  The key pair is found in the Fedlet's keystore, and the certificate is included in the standard metadata. Learn more in [Public and private key settings](#unconfigured-fedlet-properties-keys) and [Service provider standard XML](#unconfigured-fedlet-sp-standard).

* `encryptionCertAlias`

  Alias of the public key certificate for the key pair used when encrypting messages to the IDP

  The key pair is found in the Fedlet's keystore, and the certificate is included in the standard metadata. Learn more in [Public and private key settings](#unconfigured-fedlet-properties-keys) and [Service provider standard XML](#unconfigured-fedlet-sp-standard).

* `basicAuthOn`

  Set this to true to use HTTP Basic authorization with the IdP.

  Default: false

* `basicAuthUser`

  When using HTTP Basic authorization with the IdP, this value is the username.

* `basicAuthPassword`

  When using HTTP Basic authorization with the IdP, this value is the password.

  Encrypt the password using the `encode.jsp` page of your test copy of AM that you might also have used to encode keystore passwords as described in [Public and private key settings](#unconfigured-fedlet-properties-keys).

* `autofedEnabled`

  Set to `true` to enable automatic federation with AM, based on the value of a profile attribute common to user profiles in AM and in the Fedlet's context.

  Default: false

* `autofedAttribute`

  If you enable automatic federation, set this property to the name of the user profile attribute used for automatic federation.

* `transientUser`

  Use this effective identity for users with transient identifiers.

  Default: anonymous

* `spAdapter`

  Class name for a plugin SP adapter

  This class must extend `com.sun.identity.saml2.plugins.SAML2ServiceProviderAdapter`.

* `spAdapterEnv`

  When using a plugin SP adapter, this attribute's values optionally take a map of settings `key=value` used to initialize the plugin.

* `fedletAdapter`

  Class name for an alternate fedlet adapter. Default is an empty value.

* `fedletAdapterEnv`

  When using an alternate fedlet adapter, this attribute's values optionally take a map of settings `key=value` used to initialize the plugin.

* `spAccountMapper`

  Class name for an implementation mapping SAML protocol objects to local user profiles

  Default: `com.sun.identity.saml2.plugins.DefaultLibrarySPAccountMapper`

* `useNameIDAsSPUserID`

  Use the Name ID from the incoming Assertion to find the local user as the final resort if other means don't apply.

  Default: false

* `transientUser`

  If specified, this is the mapped SP user for transient federation.

* `responseArtifactMessageEncoding`

  Artifact message encoding; either `URI` or `FORM`.

  Default: `URI`

* `spAttributeMapper`

  Class name for an implementation mapping SAML assertion attributes to local user profile attributes

  Default: `com.sun.identity.saml2.plugins.DefaultSPAttributeMapper`

* `spAuthncontextMapper`

  Class name for an implementation determining the authentication context to set in an authentication request, and mapping the authentication context to an authentication level

  Default: `com.sun.identity.saml2.plugins.DefaultSPAuthnContextMapper`

* `spAuthncontextClassrefMapping`

  String defining how the SAML authentication context classes map to authentication levels and indicate the default context class

  Format: `authnContextClass|authLevel[|default]`

  Default: `urn:oasis:names:tc:SAML:2.0:ac:classes:PasswordProtectedTransport|0|default`

* `spAuthncontextComparisonType`

  How to evaluate authentication context class identifiers.

  * `exact`

    Assertion context must exactly match a context in the list

  * `minimum`

    Assertion context must be at least as strong as a context in the list

  * `maximum`

    Assertion context must be no stronger than a context in the list

  * `better`

    Assertion context must be stronger than all contexts in the list

  Default: `exact`

* `includeRequestedAuthnContext`

  Enable to include the Requested Authentication Context in the Authentication Request.

  Default: true

* `attributeMap`

  Map of SAML assertion attributes to local user profile attributes

  Default: `*=*`

* `saml2AuthModuleName`

  Name of an alternative SAML 2.0 authentication module

* `localAuthURL`

  URL to a login page on the Fedlet side

  Use this to override the Assertion Consumer Service URL from the standard metadata when consuming assertions.

* `intermediateUrl`

  URL to an intermediate page returned before the user accesses the final protected resource

* `defaultRelayState`

  If no RelayState is specified in a SAML request, redirect to this URL after successful single sign-on.

  URL-encode the `defaultRelayState` value.

* `appLogoutUrl`

  One or more Fedlet URLs that initiate single logout

  Replace the placeholders in the default with the values for your Fedlet.

  Default: `FEDLET_PROTOCOL://FEDLET_HOST:FEDLET_PORT/FEDLET_DEPLOY_URI/logout`

* `assertionTimeSkew`

  Tolerate clock skew between the Fedlet and the IdP of at most this number of seconds.

  Default: 300

* `wantAttributeEncrypted`

  Set to true to request the IdP to encrypt attributes in the response

* `wantAssertionEncrypted`

  Set to true to request the IdP to encrypt the SAML assertion in the response

* `wantNameIDEncrypted`

  Set to true to request the IdP to encrypt the name ID in the response

* `wantPOSTResponseSigned`

  Set to true to request the IDP to sign the response when using HTTP POST

* `wantArtifactResponseSigned`

  Set to true to request the IDP to sign the response when using HTTP Artifact

* `wantLogoutRequestSigned`

  Set to true to request that the IDP sign single logout requests

* `wantLogoutResponseSigned`

  Set to true to request that the IDP sign single logout responses

* `wantMNIRequestSigned`

  Set to true to request that the IDP manage name ID requests

* `wantMNIResponseSigned`

  Set to true to request that the IDP manage name ID responses

* `cotlist`

  Set this to the circle of trust name used in [Configure circles of trust](#unconfigured-fedlet-cot).

  Default: `fedletcot`

* `saeAppSecretList`

  When using Secure Attribute Exchange with AM this represents the Application Security Configuration settings.

  Values take the format `url=FedletURL|type=symmetric|secret=EncodedSharedSecret[|encryptionalgorithm=EncAlg|encryptionkeystrength=EncStrength]` or `url=FedletURL|type=asymmetric|privatekeyalias=FedletSigningCertAlias[|encryptionalgorithm=EncAlg|encryptionkeystrength=EncStrength|pubkeyalias=FedletPublicKeyAlias]`

  You can omit the `privatekeyalias` setting if the signing certifcate is specified in the standard metadata.

* `saeSPUrl`

  When using Secure Attribute Exchange (SAE) with AM this is the Fedlet URL that handles SAE requests. If this is omitted, then SAE isn't enabled.

* `saeSPLogoutUrl`

  When using Secure Attribute Exchange with AM this is the Fedlet URL that handles SAE global logout requests.

* `ECPRequestIDPListFinderImpl`

  When using the Enhanced Client and Proxy profile this is the class name for the implementation that returns a list of preferred IDPs trusted by the ECP.

  Default: `com.sun.identity.saml2.plugins.ECPIDPFinder`

* `ECPRequestIDPList`

  When using the Enhanced Client and Proxy profile this is the list of IDPs for the ECP to contact.

  When not specified the list finder implementation is used.

* `enableIDPProxy`

  Set this to true to enable IDP proxy functionality.

  Default: false

* `idpProxyList`

  A list of preferred IDPs that the Fedlet can proxy to

* `idpProxyCount`

  Number of IDP proxies that the Fedlet can have

  Default: 0

* `useIntroductionForIDPProxy`

  Set this to true to pick a preferred IDP based on a SAML 2.0 introduction cookie.

  Default: false

* `spSessionSyncEnabled`

  If this is enabled, when a session times out, the SP notifies all IdPs to log out. A session may time out, for example, when `max-idle` time or `max-session` time is reached.

  Default: false

#### Service Provider Extended XML: AttributeQueryConfig Settings

This section covers elements for the Attribute Requester role, arranged in the order they appear in the template.

* `signingCertAlias`

  Alias of the public key certificate for the key pair used when signing messages to the IDP

  The key pair is found in the Fedlet's keystore, and the certificate is included in the standard metadata. Learn more in [Public and private key settings](#unconfigured-fedlet-properties-keys) and [Service provider standard XML](#unconfigured-fedlet-sp-standard).

* `encryptionCertAlias`

  Alias of the public key certificate for the key pair used when encrypting messages to the IDP

  The key pair is found in the Fedlet's keystore, and the certificate is included in the standard metadata. Learn more in [Public and private key settings](#unconfigured-fedlet-properties-keys) and [Service provider standard XML](#unconfigured-fedlet-sp-standard).

* `wantNameIDEncrypted`

  Set to true to request that the IDP encrypt the name ID

* `cotlist`

  Set this to the circle of trust name used in [Configure circles of trust](#unconfigured-fedlet-cot).

  Default: `fedletcot`

#### Service Provider Extended XML: XACMLAuthzDecisionQueryConfig Settings

This section covers elements for the XACML decision requester role, enabling the Fedlet to act as a Policy Enforcement Point, arranged in the order they appear in the template.

* `signingCertAlias`

  Alias of the public key certificate for the key pair used when signing messages to the IDP

  The key pair is found in the Fedlet's keystore, and the certificate is included in the standard metadata. Learn more in [Public and private key settings](#unconfigured-fedlet-properties-keys) and [Service provider standard XML](#unconfigured-fedlet-sp-standard).

* `encryptionCertAlias`

  Alias of the public key certificate for the key pair used when encrypting messages to the IDP

  The key pair is found in the Fedlet's keystore, and the certificate is included in the standard metadata. Learn more in [Public and private key settings](#unconfigured-fedlet-properties-keys) and [Service provider standard XML](#unconfigured-fedlet-sp-standard).

* `basicAuthOn`

  Set to true to use HTTP Basic authorization when contacting the Policy Decision Provider

  Default: false

* `basicAuthUser`

  When using Basic authorization to contact the Policy Decision Provider, use this value as the username

* `basicAuthPassword`

  When using Basic authorization to contact the Policy Decision Provider, use this value as the password

  Encrypt the password using the `encode.jsp` page of your test copy of AM that you might also have used to encode keystore passwords as described in [Public and private key settings](#unconfigured-fedlet-properties-keys).

* `wantXACMLAuthzDecisionResponseSigned`

  Set this to true to request that the Policy Decision Provider sign the XACML response

* `wantAssertionEncrypted`

  Set this to true to request that the Policy Decision Provider encrypt the SAML assertion response

* `cotlist`

  Set this to the circle of trust name used in [Configure circles of trust](#unconfigured-fedlet-cot).

  Default: `fedletcot`

---

---
title: Create identities automatically with auto-federation
description: Configure PingAM to automatically create user accounts on service providers using SAML assertion attributes during federated single sign-on
component: pingam
version: 8.1
page_id: pingam:am-saml2:auto-federate-with-dynamic-creation
canonical_url: https://docs.pingidentity.com/pingam/8.1/am-saml2/auto-federate-with-dynamic-creation.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["SAML 2.0", "Single Sign-on (SSO)", "Federation"]
page_aliases: ["saml2-guide:auto-federate-with-dynamic-creation.adoc"]
section_ids:
  to-auto-federate-with-dynamic-creation: Create and link identities based on attribute values
---

# Create identities automatically with auto-federation

On occasion, there may not yet be an identity to link with on the SP. For example, if it is the first time a user is attempting to access the service, and they do not have an account in the SP identity store.

You can configure AM to dynamically create an account for the user in the SP identity store, using the values in the assertion as profile properties, as defined in the attribute mappings.

## Create and link identities based on attribute values

Before attempting to configure auto-federation to create identities based on attribute values, ensure that you have configured AM for SAML 2.0, created the identity and SPs, and configured a circle of trust. You must also have configured AM to support single sign-on. For information on performing those tasks, see [Deployment considerations](saml2-configuration.html) and [Implement SSO and SLO](saml2-sso-slo.html).

The following steps demonstrate how to dynamically create missing accounts on the SP:

1. Go to Realms > *realm name* > Applications > Federation > Entity Providers, and click on the name of the hosted provider.

   > **Collapse: How do I switch between SP and IdP configuration for a given provider?**
   >
   > AM only displays the configuration of a single role. Click on the labels to select the role view:
   >
   > ![saml-roles](_images/saml-roles.png)

2. On the hosted IdP:

   * Go to the Assertion Processing tab.

   * Review the Attribute Map configuration. If the attributes you want to populate when creating the new user are not in the map already, add them.

     The IdP will send these attributes in the assertion, and the SP will then map them using its own attribute map.

     > **Collapse: Tips to configure the attribute map on the IdP**
     >
     > Before user profile attributes can be mapped, they must be allowed in user profiles and also specified for the identity store. Find more information in [Add custom user profile attributes](../setup/customizing-data-stores.html#sec-maint-datastore-customattr).
     >
     > To see the profile attributes available for an LDAP identity store, log in to the AM admin UI, and go to Realms > *realm name* > Identity Stores > User Configuration. Check the LDAP User Attributes list.
     >
     > By default, you can map single-valued attributes to either user profile attributes or static values.
     >
     > To map a static value, enclose the value in double quotes (`"`), for example:
     >
     > ![The static value is enclosed in double quotes.](_images/static-attr-mapping.png)
     >
     > Figure 1. Example of mapping a static value
     >
     > To map multi-valued attributes, you must implement a [custom IdP attribute mapper](custom-idp-attribute-mapper.html).

   * Save your work.

3. On the hosted SP:

   * Go to the Assertion Processing tab.

   * Review the Attribute Map configuration, and ensure that the attribute mappings on the IdP are represented in the map.

     > **Collapse: Tips to configure the attribute map on the SP**
     >
     > The value of Key is a SAML attribute sent in an assertion, and the value of Value is a property in the authenticated session, or an attribute of the user's profile.
     >
     > By default, the SP maps the SAML attributes it receives to equivalent-named session properties. However, when the SP is configured to create identities during autofederation and the identity does not exist yet, the SP maps the SAML attributes to their equivalents in the newly-created user profile.
     >
     > The special mapping `Key: *, Value: *` means that the SP maps each attribute it receives in the assertion to equivalent-named properties or attributes. For example, if the SP receives `mail` and `firstname` in the assertion, it maps them to `mail` and `firstname` respectively.
     >
     > Remove the special mapping and add key pairs to the map if:
     >
     > * (During autofederation) The attributes in the IdP's and the SP's identity stores do not match.
     >
     > * You need control over the names of the session properties.
     >
     > * You need control over which attributes the SP should map, because the IdP adds too many to the assertion.
     >
     > For example, if the SAML attribute is `firstname` and you want the SP to map it to a session property/user profile attribute called `cn`, create a mapping similar to `Key: firstname, Value: cn`.

   * Enable auto-federation.

     In the attribute property, enter the SAML attribute name that the SP will use to link accounts, as configured in the Attribute Map.

     |   |                                                                                                               |
     | - | ------------------------------------------------------------------------------------------------------------- |
     |   | The value of the named attribute is used as the username of the created user when auto-federation is enabled. |

   * Save your work.

   * Go to Realms > *realm name* > Authentication > Settings.

   * On the User Profile tab, in the User Profile field, select Dynamic or Dynamic with User Alias.

     For more information the user profile property, see [User Profile](../am-authentication/authn-core-settings.html#authn-core-user-profile).

   * Save your work.

4. To test your work:

   * Create a new user on the IdP, including values for any attributes you mapped in the providers.

   * Log out of the AM admin UI and initiate SSO. For example, as described in [IdP-Initiated SSO URLs](saml2-standalone-mode.html#saml2-sso-standalone-idpssoinit).

   * Authenticate as the new user you created in the IdP.

   * On success, check `https://www.sp.com:8443/am/XUI/#profile/details` to see the new user account created on the SP, and the attributes that were copied from the assertion.

---

---
title: Customize SAML 2.0
description: Extend SAML 2.0 functionality in PingAM using custom Java implementations or scripts for attribute mapping, adapters, and NameID customization
component: pingam
version: 8.1
page_id: pingam:am-saml2:customize-saml2-plugins
canonical_url: https://docs.pingidentity.com/pingam/8.1/am-saml2/customize-saml2-plugins.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["SAML 2.0", "Single Sign-on (SSO)", "Federation", "Customization", "Java", "Scripts"]
page_aliases: ["saml2-guide:customize-saml2-plugins.adoc"]
section_ids:
  java_implementation: Java implementation
  scripted_implementation: Scripted implementation
---

# Customize SAML 2.0

AM includes several customization points that let you extend SAML 2.0 functionality. AM provides some default implementation for these extension points, but you can also configure your own custom implementation per entity provider.

You can implement a custom SAML 2.0 customization in *Java*, or for the extension points described in this section, using a *script*.

Configure AM to use your custom implementation in the entity provider settings. For information about configuration settings, refer to the [Reference](saml2-reference.html) section.

|   |                                                                                                                                                                                                         |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | If configured, a scripted implementation takes precedence over any Java class that is specified. To make sure the Java class is used, clear any `Script` settings in the entity provider configuration. |

The following table provides an overview of the SAML 2.0 extension points that you can implement in Java or with a script.

| Extension point                                          | Description                                                                                               |
| -------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- |
| [IdP attribute mapper](custom-idp-attribute-mapper.html) | Customize the default IdP attribute mapper to specify which user attributes are included in an assertion. |
| [IdP adapter](custom-idp-adapter.html)                   | Customize SAML responses and browser redirects.                                                           |
| [SP account mapper](custom-sp-account-mapper.html)       | Customize the mapping between user attributes and the SAML 2.0 assertion.                                 |
| [SP adapter](custom-sp-adapter.html)                     | Customize configuration in the hosted SP adapter environment.                                             |
| [NameID mapper](custom-nameid-mapper.html)               | Customize the value of the NameID attribute in the SAML assertion.                                        |

## Java implementation

The plugin interfaces and default Java implementation can be found in the `openam-federation-library`.

To view the supported plugin interfaces, refer to these packages:

* `org.forgerock.openam.saml2.plugins`

* `com.sun.identity.saml2.plugins`

## Scripted implementation

AM provides a scripting engine and template scripts for you to extend SAML 2.0 behavior by running scripts stored as configuration, rather than by updating code. Creating and modifying plugin scripts enables rapid development without the need to change or recompile core AM.

* To explore the default scripts in the AM admin UI, including the available script properties, go to Realms > *realm name* > Scripts and select the script you want to examine.

* For all available sample scripts, refer to [Sample scripts](../am-scripting/sample-scripts.html).

* To view the available bindings for SAML scripts, refer to [SAML 2.0 scripting API](../am-scripting/saml2-scripting-api.html).

---

---
title: Deploy and test the Fedlet on the SP
description: Deploy the Fedlet on a service provider and test SAML 2.0 single sign-on and single logout functionality
component: pingam
version: 8.1
page_id: pingam:am-saml2:fedlet-deploy-test
canonical_url: https://docs.pingidentity.com/pingam/8.1/am-saml2/fedlet-deploy-test.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["SAML 2.0", "Single Sign-on (SSO)", "Federation", "Fedlet", "Java"]
page_aliases: ["saml2-guide:fedlet-deploy-test.adoc"]
section_ids:
  install-fedlet-as-demo: Install and configure the Fedlet as a demo application
  unconfigured-fedlet-embedding: Embed the Java Fedlet in a web application
  testing-fedlet-sso-slo: Test Fedlet single sign-on and single logout
---

# Deploy and test the Fedlet on the SP

This page covers the two options for deploying the Fedlet.

## Install and configure the Fedlet as a demo application

To deploy the Fedlet on the SP, you require the following:

* The configuration files, as created in [Create and configure the Fedlet](create-configure-fedlet.html).

* The Fedlet `.war` file, provided in the `Fedlet-8.1.1.zip`, within the AM distribution file; `AM-8.1.1.zip`.

  1. Create a `fedlet` directory, in the home directory of the user that runs the AM web container:

     ```bash
     $ cd $HOME
     $ mkdir fedlet
     ```

  2. Copy the fedlet configuration files to the `$HOME/fedlet` directory.

     The result may resemble the following:

     ```bash
     $ cd /Users/tomcat-user/fedlet
     $ ls -A1
     FederationConfig.properties
       fedlet.cot
       idp-extended.xml
       idp.xml
       sp-extended.xml
       sp.xml
     ```

  3. Deploy the Fedlet `.war` file into your web container:

     ```bash
     $ cp fedlet.war /path/to/tomcat/webapps
     ```

     Upon completion, you can proceed to [Test Fedlet single sign-on and single logout](#testing-fedlet-sso-slo).

## Embed the Java Fedlet in a web application

The Fedlet `.war` file, `fedlet.war`, serves as an example and to provide the code needed to embed the Fedlet in your web application.

The basic steps for using the Fedlet in your application are as follows:

1. Unpack the Fedlet `.zip` file to a working directory, remove any files you do not want to keep, such as `index.jsp` or `fedletEncode.jsp`, and merge the Fedlet files with those of your web application.

2. To integrate single sign-on into your application, modify the functionality in the `fedletSampleApp.jsp` page or add it to your application's logic.

   If you add it to your application's logic, then you must also edit your application's deployment descriptor file, `web.xml`, to set the assertion consumer URI, which by default is `/fedletapplication` in the basic SP XML for the Fedlet. Add `servlet` and `servlet-mapping` elements as shown in the following example.

   ```xml
   <servlet>
       <servlet-name>yourapplication</servlet-name>
       <jsp-file>/your-application.jsp</jsp-file>
   </servlet>
   <servlet-mapping>
       <servlet-name>yourapplication</servlet-name>
       <url-pattern>/fedletapplication</url-pattern>
   </servlet-mapping>
   ```

3. Build a `.war` file from your web application with embedded Fedlet files.

   This is the version of the application to deploy. When you deploy your `.war` file, also provide the Fedlet configuration files. For information on where to put the configuration files and how to deploy the `.war` file with embedded Fedlet, see [Install and configure the Fedlet as a demo application](#install-fedlet-as-demo).

## Test Fedlet single sign-on and single logout

To test single sign-on and single logout from the Fedlet, go to the Fedlet URL. For example, `https://sp.example.com:8443/fedlet`.

Try one or more examples from the Fedlet home page:

![The home page for the demo Fedlet lets you try SP-(Fedlet-)initiated and IdP-initiated single sign-on and single logout.](_images/fedlet-demo.png)

You can log in to the IdP with a test user.

---

---
title: Deploy the IdP Discovery service
description: Deploy the IdP Discovery service as a separate web application to help service providers discover which identity provider corresponds to a user request in a multi-IdP circle of trust
component: pingam
version: 8.1
page_id: pingam:am-saml2:deploy-idp-discovery
canonical_url: https://docs.pingidentity.com/pingam/8.1/am-saml2/deploy-idp-discovery.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["SAML 2.0", "Single Sign-on (SSO)", "Federation", "Setup &amp; Configuration", "Installation", "Web Container"]
page_aliases: ["saml2-guide:deploy-idp-discovery.adoc"]
section_ids:
  deploy-idpdisco-on-tomcat: Deploy the Discovery service on Tomcat
  add-idpdisco-to-circle-of-trust: Add the Discovery service to your circles of trust
---

# Deploy the IdP Discovery service

When your circle of trust includes multiple IdPs, SPs must discover which IdP corresponds to a request. You can deploy the IdP Discovery service for this purpose as a separate web application.

Browsers only send cookies for the originating domain. Therefore, when a browser accesses the SP in the `sp.example.com` domain, the SP has no way of knowing whether the user has possibly authenticated at `this-idp.example.com`, or at `that-idp.example.com`. The providers therefore host an IdP Discovery service in a common domain, such as `discovery.example.com`, and use that service to discover where the user logged in. The IdP Discovery service essentially writes and reads cookies from the common domain. The providers configure their circle of trust to use the IdP Discovery service as part of SAML 2.0 federation.

Before you continue, ensure that you have a CoT with more than one IdP configured, and at least one SP. See [Deployment considerations](saml2-configuration.html). You will configure the IdP Discovery service in the CoT later.

Deploying the IdP Discovery service involves the following stages:

1. Deploy the `.war` file into your web application container.

2. Configure the Discovery service.

3. Add the Discovery service endpoints for writing cookies to and reading cookies from the common domain to the CoT.

## Deploy the Discovery service on Tomcat

How you deploy the Discovery service `.war` file depends on your web application container. The procedure in this section shows how to deploy on Apache Tomcat.

1. Copy the `IDPDiscovery-8.1.1.war` file to the `webapps/` directory.

   ```bash
   $ cp ~/Downloads/openam/IDPDiscovery-8.1.1.war /path/to/tomcat/webapps/disco.war
   ```

2. Access the configuration screen through your browser.

   In this example, Apache Tomcat listens for HTTP requests on `discovery.example.com:8443`, and Tomcat has unpacked the application under `/disco`, so the URL is `https://discovery.example.com:8443/disco`, which redirects to `Configurator.jsp`.

   ![Configure the IdP Discovery service.](_images/idp-disco-config.png)Figure 1. Completed Discovery Service Configuration Screen

   The configuration screen shows the following fields:

   * Debug Directory

     The Discovery service logs to flat files in this directory.

   * Debug Level

     Default is `error`. Other options include `error`, `warning`, `message`, and `off`.

     Set this to `message` in order to see the service working when you run your initial tests.

   * Cookie Type

     Set to PERSISTENT if you have configured AM to use persistent cookies, meaning single sign-on cookies that can continue to be valid after the browser is closed.

   * Cookie Domain

     The cookie domain is the common cookie domain used in your circle of trust for IdP discovery; in this case, `example.com`.

   * Secure Cookie

     Set this to true if clients should only return cookies when a secure connection is used.

   * Encode Cookie

     Leave this true unless your AM installation requires that you do not encode cookies. Normally, cookies are encoded such that cookies remain valid in HTTP.

   * HTTP-Only Cookie

     Set to true to use HTTPOnly cookies if needed to help prevent third-party programs and scripts from accessing the cookies.

   * Valid Redirects

     A list of valid URLs the user can be redirected to once the IdP Discovery process is complete. For example, the SPs in your CoT.

     Incoming requests with URLs specified in the `RelayState` parameter that are not configured in this field are rejected.

     Add each URL in a new line, for example, by pressing the enter key after each one.

     Use wildcards (`*`) to match one or more resources in the URL.

     |   |                                                                                                                                                                                                                                                          |
     | - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
     |   | You must configure the same URLs in the Validation service of each of the IdPs *in the Top Level Realm*.For more information, see [Configure the Validation service](../am-authentication/redirection-url-precedence.html#configure-validation-service). |

3. Restrict permissions to the Discovery service configuration file in `$HOME/libIdPDiscoveryConfig.properties`, where `$HOME` corresponds to the user who runs the web container where you deployed the service.

## Add the Discovery service to your circles of trust

Each provider has a circle of trust including itself. You configure each of these circles of trust to use the IdP Discovery service as described in the following steps:

1. On the SP console, log in as AM Administrator.

2. On the SP console, under Realms > *realm name* > Applications > Federation > Circle of Trust > *circle of trust name*, add SAML2 Writer and Reader Service URLs for the IdP Discovery service endpoints, and save your work.

   In this example, the writer URL is `https://discovery.example.com:8443/disco/saml2writer`, and the reader URL is `https://discovery.example.com:8443/disco/saml2reader`.

3. On each IdP console, log in as AM Administrator.

4. On the IdP console, under Realms > *realm name* > Applications > Federation > Entity Providers > Circle of Trust > *circle of trust name*, also add SAML2 Writer and Reader service URLs for the IdP Discovery service endpoints, and save your work.

---

---
title: Deployment considerations
description: Plan SAML 2.0 deployment in PingAM by considering circles of trust, keystore configuration, attribute mapping, and session state options
component: pingam
version: 8.1
page_id: pingam:am-saml2:saml2-configuration
canonical_url: https://docs.pingidentity.com/pingam/8.1/am-saml2/saml2-configuration.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["SAML 2.0", "Single Sign-on (SSO)", "Federation", "Setup &amp; Configuration", "Planning"]
page_aliases: ["saml2-guide:saml2-configuration.adoc"]
section_ids:
  saml2-and-session-state: Session state considerations
  sso_and_session_storage: SSO and session storage
  single_log_out_slo: Single log out (SLO)
  client_side_sessions_and_cookie_size_limits: Client-side sessions and cookie size limits
  configure_saml_2_0: Configure SAML 2.0
---

# Deployment considerations

Before you set up SAML 2.0 in AM, you should:

* Know which providers will participate in circles of trust (CoTs).

* Know how AM installations act as IdPs or SPs.

* Define how to map shared user attributes in identity information exchanged with other participants in a CoT. Local user profile attribute names should map to user profile attribute names at other providers.

  For example, if you exchange user identifiers with your partners, and you call it `uid`, but your partner calls it `userid`, then you map your `uid` to your partner's `userid`.

* Import the keys used to sign assertions into the keystore in your AM configuration directory. Use the Java `keytool` command.

  You can find more information about AM keystores, including location and different types of keystores available and how to change the default keys, in [Secrets, certificates, and keys](../security/secrets-certs-keys.html).

* Agree with other providers on a synchronized time service.

* Determine whether your session state configuration limits your usage of certain SAML 2.0 profiles. Learn more in [Session state considerations](#saml2-and-session-state).

* Consider increasing DS search size limits if you intend to create many SAML 2.0 entities. To ensure searches for defined entities work as expected, configure the DS search properties `ds-rlim-size-limit` and `ds-rlimit-time-limit` appropriately.

  Learn more in [Enforce limits](https://docs.pingidentity.com/pingds/8.1/use-cases/limits.html) in the DS documentation.

## Session state considerations

SAML 2.0 uses a combination of the CTS and browser-based data to store the progress of SAML 2.0 single sign-on (SSO) operations. This combination lets AM instances continue SSO flows that started at a different instance, without needing sticky load balancing in most scenarios.

### SSO and session storage

SSO progress is stored in a JSON web token (JWT) in the browser's session storage.

The JWT created in the browser's session storage doesn't expire. Instead, the time allowed to complete the SSO flow is determined by the configurable [maximum duration](../am-authentication/suspended-auth.html#maximum-duration) of the journey session.

The browser must [support the sessionStorage API](https://developer.mozilla.org/en-US/docs/Web/API/Web_Storage_API#window.sessionstorage) to handle SSO without the need for sticky load balancing of AM instances. You **must** configure sticky load balancing to support SAML 2.0 SSO with clients that don't support session storage and on IdP proxy implementations.

Session storage is similar to local storage but is more limited:

* Session storage exists only within the current browser tab.

* Another tab that displays the same page will have a different session storage.

* Session storage is shared between frames in the same tab (assuming they come from the same origin).

* Session storage data survives a page refresh, but not closing and opening the tab.

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | To enable session storage support in WebView components on Android, set the following property:```
settings.setDomStorageEnabled(true)
```You can't use session storage when using multiple WebView components simultaneously. Learn more in [WebSettings - setDomStorageEnabled](https://developer.android.com/reference/android/webkit/WebSettings#setDomStorageEnabled\(boolean\)) in the *Android Developers* documentation. |

The JWT created in the browser's session storage is encrypted using the `am.global.services.saml2.client.storage.jwt.encryption` secret label, which by default is mapped to the `directenctest` certificate alias. Learn more in [Secrets, certificates, and keys](../security/secrets-certs-keys.html).

### Single log out (SLO)

Performing SLO operations with more than one AM instance has the following caveats:

* AM instances cache information about SLO progress in memory. After the initial request, you must send each subsequent request in an SLO flow to the same instance; for example, by enabling sticky load balancing.

* Use the HTTP-POST or HTTP-Redirect bindings for SAML 2.0 SLO. The SOAP binding isn't supported.

### Client-side sessions and cookie size limits

Browsers allow cookie sizes between 4,000 and 5,200 bytes, depending on the browser. When using [client-side](../am-sessions/client-based-sessions.html) sessions, some SAML 2.0 features can cause the session cookie to exceed the browser's cookie size limit. This can occur in the following situations:

* In standalone mode, when performing SSO, the IdP adds the full login URL (`FullLoginURL` property) to the session cookie, which includes the authentication request data, adding to cookie size.

* In integrated mode, AM adds to the session those SAML 2.0 attributes mapped to AM attributes.

If a client-side session cookie exceeds the supported size in any of these cases, you can configure a custom post-authentication tree hook to remove unwanted properties or attributes, at the realm level. Removing properties or attributes in a custom SAML 2.0 SP adapter isn't supported.

You can find more information about post-authentication tree hooks in [Create post-authentication hooks for trees](../am-authentication/auth-nodes-and-journeys.html#post-authn-plugins-treehook).

## Configure SAML 2.0

The following table summarizes the high-level tasks required to configure SAML 2.0:

| Task                                                                                                                                                                                                                                                                                                                     | Resources                                                                         |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------- |
| **Configure an SP, an IdP, and a CoT**Decide if AM will be an SP, an IdP, or both, and determine what metadata you need to import from other providers.For example, if AM is the IdP for another service, you must import the metadata of the remote SP.Ensure that SPs and IdPs that work together are in the same CoT. | [Set up IdPs and SPs in a CoT](saml2-providers-and-cots.html)                     |
| **Secure your providers**Configure signing and encryption secrets for your environment.                                                                                                                                                                                                                                  | [Sign and encrypt messages](saml2-encryption.html)                                |
| **Deploy the IdP discovery service**If you have more than one IdP in your CoT, use the IdP discovery service as a proxy between SPs and IdPs.                                                                                                                                                                            | [Deploy the IdP Discovery service](deploy-idp-discovery.html)                     |
| **Configure your environment for SSO and SLO**AM provides integrated and standalone modes for implementing SSO and SLO.Choose the mode that's most appropriate for your environment.                                                                                                                                     | [Implement SSO and SLO](saml2-sso-slo.html)                                       |
| **Decide how to federate identities**AM supports different ways to federate identities, depending on the configuration and whether user profiles already exist in the SP.                                                                                                                                                | [Federate identities](saml2-linking-accounts.html)                                |
| **Configure AM as a SAML 2.0 Gateway for Legacy Applications**Use AM Secure Attribute Exchange and PingGateway to integrate legacy applications into your SAML 2.0 deployment.                                                                                                                                           | [Implement a SAML 2.0 gateway by using Secure Attribute Exchange](saml2-sae.html) |
| **Use fedlets as lightweight SPs**AM provides Fedlets, which are small Java applications that can act as SPs without a full AM installation. Fedlets redirect to AM for SSO and to retrieve SAML assertions.                                                                                                             | [Implement SAML 2.0 SPs by using Fedlets](saml2-implementation-fedlet.html)       |

---

---
title: Enable signing and encryption in a Fedlet
description: Configure the Java Fedlet to sign and encrypt SAML assertions and XML data using keystores and certificates
component: pingam
version: 8.1
page_id: pingam:am-saml2:fedlet-sign-encrypt
canonical_url: https://docs.pingidentity.com/pingam/8.1/am-saml2/fedlet-sign-encrypt.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["SAML 2.0", "Single Sign-on (SSO)", "Federation", "Fedlet", "Encryption"]
page_aliases: ["saml2-guide:fedlet-sign-encrypt.adoc"]
section_ids:
  fedlet-conf-signing-encryption: Configure the Fedlet for signing and encryption
---

# Enable signing and encryption in a Fedlet

Signing and encryption aren't configured by default when you create the Java Fedlet. You can, however, set up AM and the Fedlet to sign and verify XML signatures, and to encrypt and decrypt data such as SAML assertions.

Enabling signing and encryption for the Java Fedlet involves the following high-level stages:

* Before you create the Fedlet, configure the IdP to sign and encrypt data. See Realms > *realm name* > Applications > Federation > Entity Providers > *IdP name* > Signing and Encryption in the AM admin UI.

  For evaluation, you can use the `test` certificate delivered with AM.

* Initially deploy and configure the Fedlet, but do not use the Fedlet until you finish.

* On the Fedlet side, set up a JCEKS keystore used for signing and encryption. For evaluation, you can use copy the `keystore.jceks` file delivered with AM. You can find the file in the `$HOME/am/security/keystores/` directory for a server instance with the base URI `openam`. The built-in keystore includes the `test` certificate.

  You must also set up the `.storepass` and `.keypass` files using the `fedletEncode.jsp` page, such as `https://am.example.com:8443/fedlet/fedletEncode.jsp`, to encode passwords on the Fedlet side.

  The passwords for the test keystore and private key are recorded in the AM `.storepass` and `.keypass` files. These files are located in the `/path/to/am/security/secrets/defaults/` directory.

* Configure the Fedlet to perform signing and encryption by ensuring the Fedlet has access to the keystore, and by updating the SP metadata for the Fedlet.

* Import the updated SP metadata into the IdP to replace the default Fedlet configuration.

* Restart the Fedlet or container in which the Fedlet runs for the changes you made on the Fedlet side to take effect.

## Configure the Fedlet for signing and encryption

The `FederationConfig.properties` file specifies the paths to the keystore holding the signing or encryption keys for the Fedlet, the keystore password file, and the private key password file.

1. After setting up your keystore and password files as described above, edit the properties file in the configuration directory, such as `$HOME/fedlet/FederationConfig.properties`, to point to the keystore and password files.

2. Export the certificate to use for signing and encryption purposes.

   ```bash
   $ keytool -export -rfc -keystore keystore.jceks -alias test
   Enter keystore password:
   -----BEGIN CERTIFICATE-----
   MIIDaDCCAlCgAwIBAgIDcB/YMA0GCSqGSIb3DQEBCwUAMGUxCzAJBgNVBAYTAlVL
   MRAwDgYDVQQIEwdCcmlzdG9sMRAwDgYDVQQHEwdCcmlzdG9sMRIwEAYDVQQKEwlG
   b3JnZVJvY2sxDzANBgNVBAsTBk9wZW5BTTENMAsGA1UEAxMEdGVzdDAeFw0xNjAz
   MTgxMTU2MjhaFw0yNjAzMTYxMTU2MjhaMGUxCzAJBgNVBAYTAlVLMRAwDgYDVQQI
   EwdCcmlzdG9sMRAwDgYDVQQHEwdCcmlzdG9sMRIwEAYDVQQKEwlGb3JnZVJvY2sx
   DzANBgNVBAsTBk9wZW5BTTENMAsGA1UEAxMEdGVzdDCCASIwDQYJKoZIhvcNAQEB
   BQADggEPADCCAQoCggEBAKNbl89eP6B8kZATNSPe3+OZ3esLx31hjX+dakHtPwXC
   AaCKqJFwjwKdxyRuPdsVG+8Dbk3PGhk26aJrSE93EpxeqmQqxNPMeD+N0/8pjkuV
   YWwPIQ/ts2iTiWOVn7wzlE4ASfvupqOR5pjuYMWNo/pd4L7QNjUCKoAt9H11HMyi
   P+6roo/EYgX4AH7OAhfUMncYsopWhkW/ze9z8wTXc8BAEgDmt8zFCez1CtqJB/Ml
   SBUGDgk8oHYDsHKmx05baBaOBQ8LRGP5SULSbRtu34eLFootBIn0FvUZSnwTiSpb
   aHHRgWrMOVm07oSLWBuO3h/bj38zBuuqqVsAK8YuyoECAwEAAaMhMB8wHQYDVR0O
   BBYEFHxfAbr6PQ5Xgc+jVx+AGTPnnpWZMA0GCSqGSIb3DQEBCwUAA4IBAQAZBMJ2
   9/2idv1ztC6ArHtB4kw/nHHwthXFwtWAN7sRPB8tLW7fD8aJ43RQr5107Bg1Lgkm
   t+FZxpafqUC/mukjIzGzbW0COMSOTcWUGss+HxK6M6Fl9aOzKJMct1uOSpPFgjIt
   cGqydGZXR2FH93vXWoAotUwtZ119IixIdxpOJwYJg0HFn+GEfpU1PmiLfq2/uwqJ
   0hGCNfNcm9puagzhQrcDFOnolxjnYPSfSkU5wxlGo99yE5eJwoHXXU7csaZVttmx
   7sPj1lUENogXUM6JMqzSyEIm1XCOCL8rZJkZ781W5CwZhuJTNzV31sBREs8FaaCe
   ksu7Y48BmkUqw6E9
   -----END CERTIFICATE-----
   ```

3. Edit the standard metadata file for the Fedlet, such as `$HOME/fedlet/sp.xml`, to include the certificate in KeyDescriptor elements, that are children of the SPSSODescriptor element.

   ```xml
   <EntityDescriptor
       xmlns="urn:oasis:names:tc:SAML:2.0:metadata"
       entityID="http://www.example.com:8080/fedlet">
    <SPSSODescriptor
        AuthnRequestsSigned="true"
        WantAssertionsSigned="true"
        protocolSupportEnumeration="urn:oasis:names:tc:SAML:2.0:protocol">
     <KeyDescriptor use="signing">
      <ds:KeyInfo xmlns:ds="http://www.w3.org/2000/09/xmldsig#">
       <ds:X509Data>
        <ds:X509Certificate>
         MIIDaDCCAlCgAwIBAgIDcB/YMA0GCSqGSIb3DQEBCwUAMGUxCzAJBgNVBAYTAlVL
         MRAwDgYDVQQIEwdCcmlzdG9sMRAwDgYDVQQHEwdCcmlzdG9sMRIwEAYDVQQKEwlG
         b3JnZVJvY2sxDzANBgNVBAsTBk9wZW5BTTENMAsGA1UEAxMEdGVzdDAeFw0xNjAz
         MTgxMTU2MjhaFw0yNjAzMTYxMTU2MjhaMGUxCzAJBgNVBAYTAlVLMRAwDgYDVQQI
         EwdCcmlzdG9sMRAwDgYDVQQHEwdCcmlzdG9sMRIwEAYDVQQKEwlGb3JnZVJvY2sx
         DzANBgNVBAsTBk9wZW5BTTENMAsGA1UEAxMEdGVzdDCCASIwDQYJKoZIhvcNAQEB
         BQADggEPADCCAQoCggEBAKNbl89eP6B8kZATNSPe3+OZ3esLx31hjX+dakHtPwXC
         AaCKqJFwjwKdxyRuPdsVG+8Dbk3PGhk26aJrSE93EpxeqmQqxNPMeD+N0/8pjkuV
         YWwPIQ/ts2iTiWOVn7wzlE4ASfvupqOR5pjuYMWNo/pd4L7QNjUCKoAt9H11HMyi
         P+6roo/EYgX4AH7OAhfUMncYsopWhkW/ze9z8wTXc8BAEgDmt8zFCez1CtqJB/Ml
         SBUGDgk8oHYDsHKmx05baBaOBQ8LRGP5SULSbRtu34eLFootBIn0FvUZSnwTiSpb
         aHHRgWrMOVm07oSLWBuO3h/bj38zBuuqqVsAK8YuyoECAwEAAaMhMB8wHQYDVR0O
         BBYEFHxfAbr6PQ5Xgc+jVx+AGTPnnpWZMA0GCSqGSIb3DQEBCwUAA4IBAQAZBMJ2
         9/2idv1ztC6ArHtB4kw/nHHwthXFwtWAN7sRPB8tLW7fD8aJ43RQr5107Bg1Lgkm
         t+FZxpafqUC/mukjIzGzbW0COMSOTcWUGss+HxK6M6Fl9aOzKJMct1uOSpPFgjIt
         cGqydGZXR2FH93vXWoAotUwtZ119IixIdxpOJwYJg0HFn+GEfpU1PmiLfq2/uwqJ
         0hGCNfNcm9puagzhQrcDFOnolxjnYPSfSkU5wxlGo99yE5eJwoHXXU7csaZVttmx
         7sPj1lUENogXUM6JMqzSyEIm1XCOCL8rZJkZ781W5CwZhuJTNzV31sBREs8FaaCe
         ksu7Y48BmkUqw6E9
        </ds:X509Certificate>
       </ds:X509Data>
      </ds:KeyInfo>
     </KeyDescriptor>
     <KeyDescriptor use="encryption">
      <ds:KeyInfo xmlns:ds="http://www.w3.org/2000/09/xmldsig#">
       <ds:X509Data>
        <ds:X509Certificate>
         MIIDaDCCAlCgAwIBAgIDcB/YMA0GCSqGSIb3DQEBCwUAMGUxCzAJBgNVBAYTAlVL
         MRAwDgYDVQQIEwdCcmlzdG9sMRAwDgYDVQQHEwdCcmlzdG9sMRIwEAYDVQQKEwlG
         b3JnZVJvY2sxDzANBgNVBAsTBk9wZW5BTTENMAsGA1UEAxMEdGVzdDAeFw0xNjAz
         MTgxMTU2MjhaFw0yNjAzMTYxMTU2MjhaMGUxCzAJBgNVBAYTAlVLMRAwDgYDVQQI
         EwdCcmlzdG9sMRAwDgYDVQQHEwdCcmlzdG9sMRIwEAYDVQQKEwlGb3JnZVJvY2sx
         DzANBgNVBAsTBk9wZW5BTTENMAsGA1UEAxMEdGVzdDCCASIwDQYJKoZIhvcNAQEB
         BQADggEPADCCAQoCggEBAKNbl89eP6B8kZATNSPe3+OZ3esLx31hjX+dakHtPwXC
         AaCKqJFwjwKdxyRuPdsVG+8Dbk3PGhk26aJrSE93EpxeqmQqxNPMeD+N0/8pjkuV
         YWwPIQ/ts2iTiWOVn7wzlE4ASfvupqOR5pjuYMWNo/pd4L7QNjUCKoAt9H11HMyi
         P+6roo/EYgX4AH7OAhfUMncYsopWhkW/ze9z8wTXc8BAEgDmt8zFCez1CtqJB/Ml
         SBUGDgk8oHYDsHKmx05baBaOBQ8LRGP5SULSbRtu34eLFootBIn0FvUZSnwTiSpb
         aHHRgWrMOVm07oSLWBuO3h/bj38zBuuqqVsAK8YuyoECAwEAAaMhMB8wHQYDVR0O
         BBYEFHxfAbr6PQ5Xgc+jVx+AGTPnnpWZMA0GCSqGSIb3DQEBCwUAA4IBAQAZBMJ2
         9/2idv1ztC6ArHtB4kw/nHHwthXFwtWAN7sRPB8tLW7fD8aJ43RQr5107Bg1Lgkm
         t+FZxpafqUC/mukjIzGzbW0COMSOTcWUGss+HxK6M6Fl9aOzKJMct1uOSpPFgjIt
         cGqydGZXR2FH93vXWoAotUwtZ119IixIdxpOJwYJg0HFn+GEfpU1PmiLfq2/uwqJ
         0hGCNfNcm9puagzhQrcDFOnolxjnYPSfSkU5wxlGo99yE5eJwoHXXU7csaZVttmx
         7sPj1lUENogXUM6JMqzSyEIm1XCOCL8rZJkZ781W5CwZhuJTNzV31sBREs8FaaCe
         ksu7Y48BmkUqw6E9
        </ds:X509Certificate>
       </ds:X509Data>
      </ds:KeyInfo>
      <EncryptionMethod Algorithm="http://www.w3.org/2001/04/xmlenc#aes128-cbc">
       <xenc:KeySize xmlns:xenc="http://www.w3.org/2001/04/xmlenc#">
        128
       </xenc:KeySize>
      </EncryptionMethod>
     </KeyDescriptor>
     <SingleLogoutService
         Binding="urn:oasis:names:tc:SAML:2.0:bindings:HTTP-Redirect"
         Location="http://www.example.com:8080/fedlet/fedletSloRedirect"
         ResponseLocation="http://www.example.com:8080/fedlet/fedletSloRedirect" />
     <SingleLogoutService
         Binding="urn:oasis:names:tc:SAML:2.0:bindings:HTTP-POST"
         Location="http://www.example.com:8080/fedlet/fedletSloPOST"
         ResponseLocation="http://www.example.com:8080/fedlet/fedletSloPOST" />
     <SingleLogoutService
         Binding="urn:oasis:names:tc:SAML:2.0:bindings:SOAP"
         Location="http://www.example.com:8080/fedlet/fedletSloSoap" />
     <NameIDFormat>
      urn:oasis:names:tc:SAML:2.0:nameid-format:transient
     </NameIDFormat>
     <AssertionConsumerService
         index="0"
         isDefault="true"
         Binding="urn:oasis:names:tc:SAML:2.0:bindings:HTTP-POST"
         Location="http://www.example.com:8080/fedlet/fedletapplication" />
     <AssertionConsumerService
         index="1"
         Binding="urn:oasis:names:tc:SAML:2.0:bindings:HTTP-Artifact"
         Location="http://www.example.com:8080/fedlet/fedletapplication" />
    </SPSSODescriptor>
    <RoleDescriptor
        xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
        xmlns:query="urn:oasis:names:tc:SAML:metadata:ext:query"
        xsi:type="query:AttributeQueryDescriptorType"
        protocolSupportEnumeration="urn:oasis:names:tc:SAML:2.0:protocol">
    </RoleDescriptor>
    <XACMLAuthzDecisionQueryDescriptor
        WantAssertionsSigned="false"
        protocolSupportEnumeration="urn:oasis:names:tc:SAML:2.0:protocol" />
   </EntityDescriptor>
   ```

4. Edit the extended metadata file for the Fedlet, such as `$HOME/fedlet/sp-extended.xml`.

   Set the certificate alias names to the alias for the Fedlet certificate, and the `want*Signed` and `want*Encrypted` values to `true`.

   If you reformat the file, take care not to add white space around string values in elements.

   ```xml
   <?xml version="1.0"?>
   <EntityConfig xmlns="urn:sun:fm:SAML:2.0:entityconfig"
    xmlns:fm="urn:sun:fm:SAML:2.0:entityconfig"
    hosted="1"
    entityID="http://www.example.com:8080/fedlet">
     <SPSSOConfig metaAlias="/sp">
       <Attribute name="description">
         <Value/>
       </Attribute>
       <Attribute name="signingCertAlias">
         <Value>test</Value>
       </Attribute>
       <Attribute name="encryptionCertAlias">
         <Value>test</Value>
       </Attribute>
       <Attribute name="basicAuthOn">
         <Value>false</Value>
       </Attribute>
       <Attribute name="basicAuthUser">
         <Value/>
       </Attribute>
       <Attribute name="basicAuthPassword">
         <Value/>
       </Attribute>
       <Attribute name="autofedEnabled">
         <Value>false</Value>
       </Attribute>
       <Attribute name="autofedAttribute">
         <Value/>
       </Attribute>
       <Attribute name="transientUser">
         <Value>anonymous</Value>
       </Attribute>
       <Attribute name="spAdapter">
         <Value/>
       </Attribute>
       <Attribute name="spAdapterEnv">
         <Value/>
       </Attribute>
       <Attribute name="fedletAdapter">
         <Value>com.sun.identity.saml2.plugins.DefaultFedletAdapter</Value>
       </Attribute>
       <Attribute name="fedletAdapterEnv">
         <Value/>
       </Attribute>
       <Attribute name="spAccountMapper">
         <Value>com.sun.identity.saml2.plugins.DefaultLibrarySPAccountMapper</Value>
       </Attribute>
       <Attribute name="useNameIDAsSPUserID">
         <Value>false</Value>
       </Attribute>
       <Attribute name="spAttributeMapper">
         <Value>com.sun.identity.saml2.plugins.DefaultSPAttributeMapper</Value>
       </Attribute>
       <Attribute name="spAuthncontextMapper">
         <Value>com.sun.identity.saml2.plugins.DefaultSPAuthnContextMapper</Value>
       </Attribute>
       <Attribute name="spAuthncontextClassrefMapping">
         <Value>urn:oasis:names:tc:SAML:2.0:ac:classes:PasswordProtectedTransport\|0\|default</Value>
       </Attribute>
       <Attribute name="spAuthncontextComparisonType">
         <Value>exact</Value>
       </Attribute>
       <Attribute name="attributeMap">
         <Value>*=*</Value>
       </Attribute>
       <Attribute name="saml2AuthModuleName">
         <Value/>
       </Attribute>
       <Attribute name="localAuthURL">
         <Value/>
       </Attribute>
       <Attribute name="intermediateUrl">
         <Value/>
       </Attribute>
       <Attribute name="defaultRelayState">
         <Value/>
       </Attribute>
       <Attribute name="appLogoutUrl">
         <Value>http://www.example.com:8080/fedlet/logout</Value>
       </Attribute>
       <Attribute name="assertionTimeSkew">
         <Value>300</Value>
       </Attribute>
       <Attribute name="wantAttributeEncrypted">
         <Value>true</Value>
       </Attribute>
       <Attribute name="wantAssertionEncrypted">
         <Value>true</Value>
       </Attribute>
       <Attribute name="wantNameIDEncrypted">
         <Value>true</Value>
       </Attribute>
       <Attribute name="wantPOSTResponseSigned">
         <Value/>
       </Attribute>
       <Attribute name="wantArtifactResponseSigned">
         <Value/>
       </Attribute>
       <Attribute name="wantLogoutRequestSigned">
         <Value/>
       </Attribute>
       <Attribute name="wantLogoutResponseSigned">
         <Value/>
       </Attribute>
       <Attribute name="wantMNIRequestSigned">
         <Value/>
       </Attribute>
       <Attribute name="wantMNIResponseSigned">
         <Value/>
       </Attribute>
       <Attribute name="responseArtifactMessageEncoding">
         <Value>URI</Value>
       </Attribute>
       <Attribute name="cotlist">
         <Value>fedlet-cot</Value>
       </Attribute>
       <Attribute name="saeAppSecretList">
        </Attribute>
       <Attribute name="saeSPUrl">
         <Value/>
       </Attribute>
       <Attribute name="saeSPLogoutUrl">
        </Attribute>
       <Attribute name="ECPRequestIDPListFinderImpl">
         <Value>com.sun.identity.saml2.plugins.ECPIDPFinder</Value>
       </Attribute>
       <Attribute name="ECPRequestIDPList">
         <Value/>
       </Attribute>
       <Attribute name="ECPRequestIDPListGetComplete">
         <Value/>
       </Attribute>
       <Attribute name="enableIDPProxy">
         <Value>false</Value>
       </Attribute>
       <Attribute name="idpProxyList">
         <Value/>
       </Attribute>
       <Attribute name="idpProxyCount">
         <Value>0</Value>
       </Attribute>
       <Attribute name="useIntroductionForIDPProxy">
         <Value>false</Value>
       </Attribute>
       <Attribute name="spSessionSyncEnabled">
         <Value>false</Value>
       </Attribute>
       <Attribute name="relayStateUrlList">
        </Attribute>
     </SPSSOConfig>
     <AttributeQueryConfig metaAlias="/attrQuery">
       <Attribute name="signingCertAlias">
         <Value>test</Value>
       </Attribute>
       <Attribute name="encryptionCertAlias">
         <Value>test</Value>
       </Attribute>
       <Attribute name="wantNameIDEncrypted">
         <Value>true</Value>
       </Attribute>
       <Attribute name="cotlist">
         <Value>fedlet-cot</Value>
       </Attribute>
     </AttributeQueryConfig>
     <XACMLAuthzDecisionQueryConfig metaAlias="/pep">
       <Attribute name="signingCertAlias">
         <Value>test</Value>
       </Attribute>
       <Attribute name="encryptionCertAlias">
         <Value>test</Value>
       </Attribute>
       <Attribute name="basicAuthOn">
         <Value>false</Value>
       </Attribute>
       <Attribute name="basicAuthUser">
         <Value/>
       </Attribute>
       <Attribute name="basicAuthPassword">
         <Value/>
       </Attribute>
       <Attribute name="wantXACMLAuthzDecisionResponseSigned">
         <Value>false</Value>
       </Attribute>
       <Attribute name="wantAssertionEncrypted">
         <Value>true</Value>
       </Attribute>
       <Attribute name="cotlist">
         <Value>fedlet-cot</Value>
       </Attribute>
     </XACMLAuthzDecisionQueryConfig>
   </EntityConfig>
   ```

5. Make a copy of the `sp-extended.xml` file, called `sp-extended-copy.xml`, and set `hosted="0"` in the root element of the copy.

   Use the copied file, `sp-extended-copy.xml`, when importing the Fedlet configuration into AM. AM must register the Fedlet as a *remote* SP.

6. In the AM admin UI, delete the original SP entity configuration for the Fedlet, and then import the updated metadata for the new configuration into AM on the IdP side.

7. Restart the Fedlet or the container in which it runs in order for the Fedlet to pick up the changes to the configuration properties and the metadata.

---

---
title: Federate identities
description: Configure PingAM to federate identities between identity providers and service providers using persistent or transient linking, automatic federation, or authentication service-based linking
component: pingam
version: 8.1
page_id: pingam:am-saml2:saml2-linking-accounts
canonical_url: https://docs.pingidentity.com/pingam/8.1/am-saml2/saml2-linking-accounts.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["SAML 2.0", "Single Sign-on (SSO)", "Federation"]
page_aliases: ["saml2-guide:saml2-linking-accounts.adoc"]
---

# Federate identities

AM supports linking, or *federating*, identities between the IdP and the SP.

See the following table for a list of tasks to configure how AM federates identities:

| Task                                                                                                                                                                                                                                                                                        | Resources                                                                                                                                                                        |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Decide whether to permanently link identities**AM lets you choose whether to maintain the link between federated entities after logout (persistent federation) or to create a new link each time the user logs in (transient federation).Also, learn how to manage persistent federation. | * [Persistent or transient federation](persistent-or-transient-federation.html)                                                                                                  |
| **Link identities automatically**Configure AM to link identities automatically when they exist in both the IdP and the SP, or to create an account on the SP when the `NameID` that the IdP provides unequivocally identifies the identity.                                                 | - [Link identities automatically with auto-federation](auto-federation.html)

- [Create identities automatically with auto-federation](auto-federate-with-dynamic-creation.html) |
| **Link identities using the authentication service**Configure AM to link identities when the `NameID` that the IdP provides is not enough to unequivocally identify the identity.                                                                                                           | * [Link identities for authentication](linking-auth-tree.html)                                                                                                                   |
| **Link identities in the IdP to a single, shared account on the SP**Configure AM to temporarily link an identity in the IdP to, for example, the `anonymous` user in the SP.                                                                                                                | - [Link identities to a single, shared account](auto-federate-using-anonymous.html)                                                                                              |

---

---
title: IdP adapter
description: "Extend PingAM's SAML 2.0 IdP processing by implementing custom adapters to alter authentication requests, responses, and failure handling at specific points in the SAML journey"
component: pingam
version: 8.1
page_id: pingam:am-saml2:custom-idp-adapter
canonical_url: https://docs.pingidentity.com/pingam/8.1/am-saml2/custom-idp-adapter.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["SAML 2.0", "Single Sign-on (SSO)", "Federation", "Fedlet", "Java", "Scripts"]
page_aliases: ["plugins-idp-adapter.adoc", "saml2-guide:custom-idp-adapter.adoc"]
section_ids:
  java_example: Java example
  idp-adapter-script-examples: Scripted examples
  example-idp-adapter-legacy: Redirect a journey using a legacy script
  example-idp-adapter-nextgen: Set a custom header using a next-generation script
---

# IdP adapter

Use the IdP adapter to alter the processing of the authentication request at a particular point in the SAML journey, such as to redirect the user before SSO takes place, or before a failure response is sent.

This task assumes your environment is already correctly configured for SSO using SAML 2.0, where AM is the hosted IdP.

The IdP adapter provides hooks at the following points in assertion processing:

| Extension point        | Description                                                                                                                                |
| ---------------------- | ------------------------------------------------------------------------------------------------------------------------------------------ |
| preSingleSignOn        | Invoked when the authentication request is first received. Only applicable to SP-initiated flows.                                          |
| preAuthentication      | Invoked before the request is redirected for authentication. Only applicable to SP-initiated flows.                                        |
| preSendResponse        | Invoked after the user has successfully authenticated or for an existing valid session, before the response is sent.                       |
| preSignResponse        | Invoked after the response has been constructed, but before the response is signed, to let you customize the content of the SAML response. |
| preSendFailureResponse | Invoked before a SAML error response is returned. Only applicable to SP-initiated flows.                                                   |

## Java example

To create a custom IdP adapter in Java, follow these high-level steps:

1. Include the `openam-federation-library` as a dependency in your Maven project.

2. Write a Java class that implements the [org.forgerock.openam.saml2.plugins.IDPAdapter](../_attachments/apidocs/org/forgerock/openam/saml2/plugins/IDPAdapter.html) interface, or extends the `com.sun.identity.saml2.plugins.DefaultIDPAdapter` class.

3. Override one of the methods described in the [extension points table](#idp-adapter-points) to customize the authentication journey.

4. Package your custom class in a JAR file and copy to the `/WEB-INF/lib` folder where you deployed AM.

5. Configure AM to use the new Java plugin.

   1. In the AM admin UI, go to Realms > *realm name* > Applications > Federation > Entity Providers > *hosted IdP* > Advanced.

   2. In the IDP Adapter Class field, type the fully qualified name of your custom class.

   3. Save your changes.

6. Restart AM or the container in which it runs.

7. Test your changes using an appropriate mode of single-sign on.

   For example, note that some extension points are only invoked during SP-initiated flows.

## Scripted examples

Learn about IdP adapter scripts from the following resources:

* Legacy example script

  [SAML2 IDP Adapter Script](../am-scripting/sample-scripts.html#saml2-idp-adapter-js)

* Next-generation example script

  [SAML2 IDP Adapter Script (Next Gen)](../am-scripting/sample-scripts.html#saml2-idp-adapter-nextgen-js)

* Scripting API

  [IdP adapter scripting API](../am-scripting/saml2-idp-adapter-api.html)

### Redirect a journey using a legacy script

Complete the following steps to implement an example IdP adapter script that determines whether the authentication journey should be redirected based on the evaluation of a policy.

1. For this example, configure a policy that belongs to a policy set named `saml`:

   1. In the AM admin UI, go to Realms > *realm name* > Authorization > Resource Types to create a [new resource type](../am-authorization/resource-types-ui.html) with the following values:

      * **Name**: `SAML SP Access`

      * **Pattern**: `*`

      * **Action**: Assert (Default State: Deny)

   2. Go to Policy Sets to create a [new policy set](../am-authorization/policy-sets-ui.html):

      * **Id**: `saml`

      * **Name**: `saml`

      * **Resource Types**: `SAML SP Access`

   3. Add a [new policy](../am-authorization/policies-ui.html):

      * **Name**: `SAML Access Policy`

      * **Resource Types**: `SAML SP Access`

      * **Resources**: `*`

      * **Actions**: `ASSERT:Denied`

      * **Response Attributes**: `redirect_uri: https://example.com`

      * **Subjects**: `"type": "AuthenticatedUsers"`

2. To modify the default script, go to Scripts, and click SAML2 IDP Adapter Script.

   Alternatively, [create a new legacy script](../am-scripting/manage-scripts-console.html) of type `Saml2 IDP Adapter`.

   1. In the Script field, add code to the `preSendResponse` function to redirect or send an error response if the policy for the SP evaluates to false. For example:

      ```javascript
      function preSendResponse () {

        var frJava = JavaImporter(
          com.sun.identity.saml2.common.SAML2Exception);

        try {
          // set realm DN if you want to use an LDAP filter condition in the SAML access policy
          var env = new java.util.HashMap();
          var realmDn = new java.util.HashSet();
          realmDn.add("dc=am,dc=example,dc=com");
          env.put("am.policy.realmDN", realmDn);

          var subject = idpAdapterScriptHelper.getSubjectForToken(session);
          var resources = idpAdapterScriptHelper.getResourcesForToken(authnRequest);

          var ents = idpAdapterScriptHelper.getEntitlements(
            "saml", realm, subject, resources, env).iterator();

          while(ents.hasNext()){
            var entitlement = ents.next();
            var isAllowed = entitlement.getActionValue("Assert");

            if(isAllowed != null && isAllowed == true){
              return false;
            } else{
              var redirectUris = entitlement.getAttributes().get("redirect_uri");

              if (redirectUris == null || redirectUris.isEmpty()){
                logger.error("No redirect_uri");
                response.sendError(403);
              } else{
                var redirectUri = redirectUris.iterator().next();
                response.sendRedirect(redirectUri);
              } return true;
            }
          }
        } catch(error) {
          logger.error("Error in preSend reponse. " + error);
          throw new frJava.SAML2Exception(error);
        }
      }
      ```

   2. Validate and save your changes.

3. Configure AM to use the updated IdP adapter script.

   1. Still in the AM admin UI, go to Applications > Federation > Entity Providers > *hosted IdP* > Advanced.

   2. Under IDP Adapter, select your customized script from the IDP Adapter Script list.

   3. Save your changes.

4. Test your changes using an SP-initiated flow and verify that the user is redirected to the `redirect_uri` (in this example, `https://example.com`).

### Set a custom header using a next-generation script

1. In the AM admin UI, [create a new script](../am-scripting/manage-scripts-console.html) with the following values:

   * Name

     `Example Next-Generation IdP Adapter`

   * Script Type

     `Saml2 IDP Adapter`

   * Evaluator Version

     `Next Generation`

2. In the Script field, replace the `preSendFailureResponse` function with the following script:

   ```javascript
   function preSendFailureResponse() {
     // set custom header in event of failure
     try {
       if (responseHelper) {
         responseHelper.setHeader("CUSTOM-SAML-FAILURE", "true");
       }
     } catch (e) {
       logger.error("Error in preSendFailureResponse: " + e.message);
     }

     logger.error("CUSTOM-SAML-FAILURE response header set");
   }
   ```

3. Validate and save your changes.

4. Configure AM to use the updated IdP adapter script:

   1. Go to Applications > Federation > Entity Providers > *hosted IdP* > Advanced.

   2. Select your custom script, `Example Next-Generation IdP Adapter`, from the IDP Adapter Script list.

   3. Save your changes.

5. Test your changes using an SP-initiated flow that ends in failure. Verify that the response contains the custom header, for example:

   ```bash
   HTTP/1.1 500
   X-Frame-Options: SAMEORIGIN
   ...
   CUSTOM-SAML-FAILURE: true
   ...
   ```

---

---
title: IdP attribute mapper
description: Map user-configured attributes to SAML attribute objects in generated SAML assertions using the IdP attribute mapper in PingAM
component: pingam
version: 8.1
page_id: pingam:am-saml2:custom-idp-attribute-mapper
canonical_url: https://docs.pingidentity.com/pingam/8.1/am-saml2/custom-idp-attribute-mapper.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["SAML 2.0", "Single Sign-on (SSO)", "Federation", "Customization", "Java", "Scripts"]
page_aliases: ["plugins-idp-attribute-mapper.adoc", "saml2-guide:custom-idp-attribute-mapper.adoc"]
section_ids:
  java_example: Java example
  scripted_examples: Scripted examples
  example-idm-attribute-mapper-legacy: Add attributes with a legacy script
  example-idp-attribute-mapper-nextgen: Update username with a next-generation script
---

# IdP attribute mapper

Use the IdP attribute mapper to map user-configured attributes to SAML attribute objects to insert into the generated SAML assertion.

The default implementation is to retrieve the mapped attribute values from the user profile first. If the attribute values aren't present in the user's profile, then the IdP attribute mapper attempts to retrieve them from the authenticated session.

These steps assume your environment is already correctly configured for SSO using SAML 2.0, where AM is the hosted IdP.

## Java example

* Java interface

  `IDPAttributeMapper`

* Default Java class

  `com.sun.identity.saml2.plugins.DefaultIDPAttributeMapper`

To create a custom IdP attribute mapper in Java, follow these high-level steps:

1. Include the `openam-federation-library` as a dependency in your Maven project.

2. Write a Java class that implements the `com.sun.identity.saml2.plugins.IDPAttributeMapper` interface, or extends the `com.sun.identity.saml2.plugins.DefaultIDPAttributeMapper` class.

3. Override the `getAttributes()` method to customize the list of the attributes returned.

4. Package your custom class in a JAR file and copy to the `/WEB-INF/lib` folder where you deployed AM.

5. Configure AM to use the new Java plugin.

   1. In the AM admin UI, go to Realms > *realm name* > Applications > Federation > Entity Providers > *hosted IdP* > Assertion Processing.

   2. In the Attribute Mapper field, type the fully qualified name of your custom class.

   3. Save your changes.

6. Restart AM or the container in which it runs.

|   |                                                                                                                                                                                                                   |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Learn more in [How do I create a custom SAML2 IDP attribute mapper in PingAM?](https://support.pingidentity.com/s/article/How-do-I-create-a-custom-SAML2-IdP-attribute-mapper-in-PingAM) in the *Knowledge Base*. |

## Scripted examples

Learn about IdP attribute mapper scripts from the following resources:

* Legacy example script

  [SAML2 IDP Attribute Mapper Script](../am-scripting/sample-scripts.html#saml2-idp-attribute-mapper-js)

* Next-generation example script

  [SAML2 IDP Attribute Mapper Script (Next Gen)](../am-scripting/sample-scripts.html#saml2-idp-attribute-mapper-next-gen-js)

* Scripting API

  [IdP attribute mapper scripting API](../am-scripting/saml2-idp-attribute-mapper-api.html)

### Add attributes with a legacy script

Complete the following steps to implement an example IdP attribute mapper script that adds SAML attributes to the assertion returned by the IdP.

1. In the AM admin UI, go to Realms > *realm name* > Scripts, and click SAML2 IDP Attribute Mapper Script to modify the default script. Alternatively, [create a legacy script](../am-scripting/manage-scripts-console.html) of type `Saml2 IDP Attribute Mapper`.

2. In the Script field, insert one of the following example code snippets before the `return attributes;` line (around line 150):

   * Add a static single-value attribute:

     ```javascript
     var customSet = new java.util.HashSet();
     customSet.add("test");
     attributes.add(idpAttributeMapperScriptHelper.createSAMLAttribute("customSAMLAttribute", null, customSet));
     ```

   * Add a static multi-value attribute:

     ```javascript
     var customSet = new java.util.HashSet();
     var attributes = new java.util.ArrayList();
     customSet.add("test1");
     customSet.add("test2");
     customSet.add("test3");
     attributes.add(idpAttributeMapperScriptHelper.createSAMLAttribute("customMultiValueAttribute", null, customSet));
     ```

3. Validate and save your changes.

4. Configure AM to use the updated IdP attribute mapper script.

   1. Still in the AM admin UI, go to Applications > Federation > Entity Providers > *hosted IdP* > Assertion Processing.

   2. Under Attribute Mapper, select your customized script from the Attribute Mapper Script drop-down list.

   3. Save your changes.

5. Test your changes and verify that the `AttributeStatement` element in the SAML assertion contains the custom attribute.

   * Example single-value attribute assertion:

     ```xml
     <saml:AttributeStatement>
       <saml:Attribute Name="customSAMLAttribute">
         <saml:AttributeValue
             xmlns:xs="http://www.w3.org/2001/XMLSchema"
             xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
             xsi:type="xs:string">test
         </saml:AttributeValue>
       </saml:Attribute>
     </saml:AttributeStatement>
     ```

   * Example multi-value attribute assertion:

     ```xml
     <saml:AttributeStatement>
       <saml:Attribute Name="customMultiValueAttribute">
         <saml:AttributeValue
             xmlns:xs="http://www.w3.org/2001/XMLSchema"
             xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
             xsi:type="xs:string">test1
         </saml:AttributeValue>
         <saml:AttributeValue
             xmlns:xs="http://www.w3.org/2001/XMLSchema"
             xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
             xsi:type="xs:string">test2
         </saml:AttributeValue>
         <saml:AttributeValue
             xmlns:xs="http://www.w3.org/2001/XMLSchema"
             xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
             xsi:type="xs:string">test3
         </saml:AttributeValue>
       </saml:Attribute>
     </saml:AttributeStatement>
     ```

### Update username with a next-generation script

1. In the AM admin UI, [create a new script](../am-scripting/manage-scripts-console.html) with the following values:

   * Name

     `Example Next-Generation IdP Attribute Mapper`

   * Script Type

     `Saml2 IDP Attribute Mapper`

   * Evaluator Version

     `Next Generation`

2. In the Script field, replace the default script with the following:

   ```javascript
   // returns the list of attributes for the current session
   var attributes = idpAttributeMapperScriptHelper.getStandardAttributes();

   for (var attr of attributes) {
     if (attr.name === "username") {
       var upperCaseValues = [];
       for (var val of attr.values) {
         upperCaseValues.push(val.toUpperCase());
       }
       attr.values = upperCaseValues;
     }
   }
   // return the modified list of attributes
   attributes;
   ```

   |   |                                                                                                                                                                                                                    |
   | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
   |   | Make sure the last line of your script is the list of the attributes to return. It must be in the following format:```json
   [
     {
       "name:": "...",
       "nameFormat": "...",
       "values": ["..."]
     },
   ...
   ]
   ``` |

3. Validate and save your changes.

4. Configure AM to use the updated IdP attribute mapper script:

   1. Still in the AM admin UI, go to Applications > Federation > Entity Providers > *hosted IdP* > Assertion Processing.

   2. Add the following mapping to the Attribute Map:

      * SAML Attribute

        `username`

      * Local Attribute

        `uid`

   3. Select your custom script, `Example Next-Generation IdP Attribute Mapper`, from the Attribute Mapper Script list.

   4. Save your changes.

5. Test your changes using an SP-initiated flow to verify that the SAML assertion contains the updated `username` value. For example:

   ```xml
   <saml:AttributeStatement>
     <saml:Attribute Name="username">
     <saml:AttributeValue
       xmlns:saml="urn:oasis:names:tc:SAML:2.0:assertion"
       xmlns:xs="http://www.w3.org/2001/XMLSchema"
       xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
       xsi:type="xs:string">BJENSEN
       </saml:AttributeValue>
     </saml:Attribute>
   </saml:AttributeStatement>
   ```

   |   |                                                                                                                                                                                                                                                                                                                                                      |
   | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | If you run an [SP-initiated SSO integrated mode flow](saml2-integrated-mode.html#spinit-sso-integrated-mode), you can include a Scripted Decision node to output the assertion value using the `samlApplication` binding.Learn more in [Query SAML application and authentication request](../am-scripting/scripting-api-node.html#samlapp-binding). |

---

---
title: Implement a SAML 2.0 gateway by using Secure Attribute Exchange
description: Configure PingAM to act as a SAML 2.0 gateway using Secure Attribute Exchange to retrieve identity information from legacy authentication systems
component: pingam
version: 8.1
page_id: pingam:am-saml2:saml2-sae
canonical_url: https://docs.pingidentity.com/pingam/8.1/am-saml2/saml2-sae.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["SAML 2.0", "Single Sign-on (SSO)", "Federation", "Encryption"]
page_aliases: ["saml2-guide:saml2-sae.adoc"]
section_ids:
  sae-install-prerequisites: Install the SAE samples
  sae-security-prerequisites: Prepare to secure SAE communications
  sae-secure-idp: Secure the IdP side
  sae-secure-sp: Secure the SP side
  sae-trying-it-out: Try it out
---

# Implement a SAML 2.0 gateway by using Secure Attribute Exchange

Most deployments can rely on AM to handle authentication and provide identity assertions. AM provides basic authentication journeys out of the box with the expectation that you'll add custom authentication journeys to suit your deployment.

PingGateway lets you integrate legacy systems into your access management deployment.

In a deployment where you need AM to act as a SAML 2.0 gateway to a legacy application that serves as an IdP, you can use AM Secure Attribute Exchange (SAE). On the IdP side, SAE lets AM retrieve the information needed to create assertions from an external authentication service, bypassing AM authentication and trusting the external service as the authoritative source of authentication. On the SP side, SAE lets AM securely provide attributes to an application that makes its own policy decision based on the attributes rather than rely on AM for the policy decision.

![External applications use SAE to communicate with AM providers. The providers in turn use SAML 2.0 to communicate with other providers.](_images/sae.png)

When you use SAE on the IdP side, an external application acts as the authoritative source of authentication. After a user authenticates successfully, the application tells AM to create an authenticated session by sending a secure HTTP GET or POST to AM that asserts the identity of the user. AM processes the assertion to create a session for the user. If the user is already authenticated and comes back to access the application, the application sends a secure HTTP POST to AM to assert both the user's identity and also any necessary attributes related to the user. AM processes the assertion to create the session for the user and populate the attributes in the authenticated session. When the user logs out, the external authentication application can initiate single logout from the IdP AM server by sending the `sun.cmd=logout` attribute to AM using SAE.

On the SP side, AM communicates using SAML 2.0 with AM on the IdP side. AM can use SAE to transmit attributes to an application through a secure HTTP POST.

SAE relies either on shared keys and symmetric encryption, or on public and private keys and asymmetric encryption to protect attributes communicated between AM and external applications.

AM ships with sample JSPs that demonstrate secure attribute exchange. To try the sample, you must set up an AM circle of trust to include an IdP and an SP, install the SDK sample web application on each provider, and then configure the providers appropriately as described in this page to secure communications with the sample SAE applications on both the IdP and SP sides.

## Install the SAE samples

Set up an AM server as an IdP, and another as an SP, connecting the two in a circle of trust called `samplesaml2cot`. Configure both the hosted providers and also the remote providers as described in [Set up IdPs and SPs in a CoT](saml2-providers-and-cots.html). This chapter assumes you set up the hosted IdP at `https://www.idp.com:8443/am` and the hosted SP at `https://www.sp.com:8443/am`. Make sure federation is working before you add secure attribute exchange applications that rely on functioning SAML 2.0 communications between the providers.

The SAE samples are not delivered with AM. Instead, you find them with the client SDK samples in `openam-examples/openam-example-clientsdk-war` folder of the `openam-public` repo. The SAE samples are under `/saml2/sae` where you install the samples. `saeIDPApp.jsp` is the IdP side external application. `saeSPApp.jsp` is the SP side external application.

## Prepare to secure SAE communications

In order for SAE to be secure, you must both set up a trust relationship between the application on the IdP side and the AM server acting as IdP, and set up a trust relationship between the application on the SP side and the AM server acting as the SP. These trust relationships can be based on a shared secret and symmetric encryption, or on public and private key pairs and asymmetric encryption. The trust relationships on either side are independent. For example, you can use a shared secret on the IdP side and certificates on the SP side.

When using symmetric encryption, you must define a shared secret string used both for the application and the provider. The sample uses `secret12` as the shared secret. To simplify configuration, the sample uses the same shared secret, and thus symmetric encryption, for both trust relationships.

When using symmetric encryption, you must also use the encoded version of your shared secret. To get the encoded version of a shared secret string, use the `encode.jsp` page on the provider, as in `https://www.idp.com:8443/am/encode.jsp` and `https://www.sp.com:8443/am/encode.jsp`. An encoded version of `secret12` looks something like `AQICEcFhDWmb6sVmMuCJuVh43306HVacDte9`.

When using asymmetric encryption, you must obtain a public-private key pair for the application, and store the keys in a keystore on the application side. Also store the public key from AM which is acting as the provider in the application's keystore. Make note of the certificate aliases for your application's private key, and for AM's public key. Also note the path to the keystore for your application, the keystore password, and the private key password.

## Secure the IdP side

This configuration uses the default sample settings with a shared secret of `secret12`, without encryption of the attributes:

1. Log in as `amAdmin` to the AM server console where you set up the hosted identity provider (IdP).

2. The sample includes a `branch` attribute not found in user profiles by default. Therefore, under Realms > *realm name* > Authentication > Settings > User Profile, set User Profile to `Ignored`, and save your work.

3. Under Realms > *realm name* > Applications > Federation > Entity Providers, select the name of the hosted IdP to access the IdP configuration:

   * Under Assertion Processing > Attribute Mapper, add both `mail=mail` and `branch=branch` to the attribute map, and save your work.

   * Under Advanced > SAE Configuration, make sure the IDP URL reflects an endpoint on the IdP such as `https://www.idp.com:8443/am/idpsaehandler/metaAlias/idp`, and save your work.

   * Also under Advanced > SAE Configuration > Application Security Configuration, add the URL value for the kind of encryption you are using, and save your work.

     When using the defaults, the value is something like `url=https://www.idp.com:8443/samples/saml2/sae/saeIDPApp.jsp|type=symmetric|secret=encoded-secret`, where the AM SDK sample web application is deployed on the IdP side with context root `/samples` and the *encoded-secret* is something like `AQICEcFhDWmb6sVmMuCJuVh43306HVacDte9`.

     If you use a different mechanism to secure the communications between the SAE application and the provider, read the online help in the console to see how to construct your URL value.

4. Under Realms > *realm name* > Applications > Federation > Entity Providers, select the name of the remote SP to access the SP configuration on the IdP side:

   * Under Assertion Processing > Attribute Mapper, add both `mail=mail` and `branch=branch` to the attribute map, and save your work.

   * Under Advanced > SAE Configuration, make sure the SP URL reflects an endpoint on the SP, such as `https://www.sp.com:8443/am/spsaehandler/metaAlias/sp`, and save your work.

   * Also under Advanced > SAE Configuration, add the URL to the sample SAE application as the SP Logout URL, such as `https://www.sp.com:8443/samples/saml2/sae/saeSPApp.jsp`, and save your work.

## Secure the SP side

This configuration uses the default sample setting of symmetric encryption, with a shared secret of `secret12`.

Login as `amAdmin` to the AM server console where you set up the hosted service provider (SP):

1. The sample includes a `branch` attribute not found in user profiles by default. Therefore, under Realms > *realm name* > Authentication > Settings > User Profile, set User Profile to `Ignored`, and save your work.

2. Under Realms > *realm name* > Applications > Federation > Entity Providers, select the name of the hosted SP to access the SP configuration:

   * Under Assertion Processing > Attribute Mapper, add both `mail=mail` and `branch=branch` to the attribute map, and save your work.

   * Also under Assertion Processing > Attribute Mapper > Auto Federation, select Enabled, set the Attribute to `mail`, and save your work.

   * Under Advanced > SAE Configuration, make sure the SP URL reflects an endpoint on the SP such as `https://www.sp.com:8443/am/spsaehandler/metaAlias/sp`, and save your work.

   * Furthermore, under Advanced > SAE Configuration, add the URL to the sample SAE application as the SP Logout URL such as `https://www.sp.com:8443/samples/saml2/sae/saeSPApp.jsp`, and save your work.

   * Also under Advanced > SAE Configuration > Application Security Configuration, add the URL value for the kind of encryption you are using, and save your work.

     When using the defaults, the value is something like `url=https://www.sp.com:8443/samples/saml2/sae/saeSPApp.jsp|type=symmetric|secret=encoded-secret`, where the AM SDK sample web application is deployed on the IdP side with context root `/samples` and the *encoded-secret* is something like `AQICkX24RbZboAVgr2FG1kWoqRv1zM2a6KEH`.

     If you use a different mechanism to secure the communications between the SAE application and the provider, read the online help in the console to see how to construct your URL value.

## Try it out

After completing the setup described above, go to the IdP-side SAE application; for example, at `https://www.idp.com:8443/samples/saml2/sae/saeIDPApp.jsp`.

Make sure you set the `SP App URL` and `SAE URL on IDP end` to fit your configuration. For example, if you used the settings above, use the following values:

* SP App URL

  `https://www.sp.com:8443/samples/saml2/sae/saeSPApp.jsp`

* SAE URL on IDP end

  `https://www.idp.com:8443/am/idpsaehandler/metaAlias/idp`

Check the settings, and select Generate URL to open the Secure Attributes Exchange IDP APP SAMPLE page.

Select the `ssourl` link to start the exchange.

The resulting web page shows the attributes exchanged, including the mail and branch values used. The text of that page is something like the following:

```none
SAE SP APP SAMPLE

Secure Attrs :
mail            testuser@foo.com
sun.idpentityid https://www.idp.com:8443/am
sun.spentityid  https://www.sp.com:8443/am
branch          mainbranch
sun.authlevel   0
```

---

---
title: Implement SAML 2.0 SPs by using Fedlets
description: Deploy lightweight SAML 2.0 service providers as Fedlets without requiring a full PingAM installation
component: pingam
version: 8.1
page_id: pingam:am-saml2:saml2-implementation-fedlet
canonical_url: https://docs.pingidentity.com/pingam/8.1/am-saml2/saml2-implementation-fedlet.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["SAML 2.0", "Single Sign-on (SSO)", "Federation", "Fedlet"]
page_aliases: ["saml2-guide:saml2-implementation-fedlet.adoc"]
---

# Implement SAML 2.0 SPs by using Fedlets

An AM *Fedlet* is a small Java web application that can act as an SP for a specific IdP without requiring that you install all of AM.

When your organization acts as the IdP and you want to enable SPs to federate their services with yours, you can generate configuration files for a Fedlet.

Fedlets are easy to integrate into Java web applications; they do not require an entire AM installation alongside your application, but instead can redirect to AM for single sign-on, and to retrieve SAML assertions.

> **Collapse: Fedlet Support for SAML 2.0 Features**
>
> **Fedlet support for SAML 2.0 features**
>
> | SAML 2.0 Feature                                    | Java Fedlet |
> | --------------------------------------------------- | ----------- |
> | IdP and SP-initiated single sign-on (HTTP Artifact) | Supported   |
> | IdP and SP-initiated single sign-on (HTTP POST)     | Supported   |
> | IdP and SP-initiated single logout (HTTP POST)      | Supported   |
> | IdP and SP-initiated single logout (HTTP Redirect)  | Supported   |
> | Sign requests and responses                         | Supported   |
> | Encrypt assertion, attribute, and NameID elements   | Supported   |
> | Export SP Metadata                                  | Supported   |
> | Multiple IdPs                                       | Supported   |
> | External IdP discovery service                      | Supported   |
> | Bundled IdP reader service for discovery            | Supported   |

After receiving the configuration files for the Fedlet, the SP administrator installs them, and then obtains the Fedlet web application from the AM distribution and installs it in the application web container.

The following table summarizes the high-level tasks required to configure Fedlets:

| Task                                                                                                                                                                                      | Resources                                                                                                                            |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------ |
| **Create and configure the Fedlet**Configure the Fedlet files and its keystore for your environment, add the metadata from the IdPs to it, and share the Fedlet's metadata with the IdPs. | * [Create and configure the Fedlet](create-configure-fedlet.html)                                                                    |
| **Ensure the Fedlet is secure**By default, signing and encryption are not configured. You should configure them to sign and encrypt data, such as assertions.                             | - [Enable signing and encryption in a Fedlet](fedlet-sign-encrypt.html)                                                              |
| **Test the Fedlet**You can test the Fedlet as a standalone application, or by integrating it inside one of your applications.                                                             | * [Deploy and test the Fedlet on the SP](fedlet-deploy-test.html)

* [Integrate with the Fedlet WAR File](fedlet-war-integrate.html) |

---

---
title: Implement SSO and SLO
description: Implement SAML 2.0 single sign-on and single logout with PingAM using integrated or standalone mode
component: pingam
version: 8.1
page_id: pingam:am-saml2:saml2-sso-slo
canonical_url: https://docs.pingidentity.com/pingam/8.1/am-saml2/saml2-sso-slo.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["SAML 2.0", "Single Sign-on (SSO)", "Federation"]
page_aliases: ["saml2-guide:saml2-sso-slo.adoc"]
section_ids:
  sso-integrated: Integrated or standalone mode
---

# Implement SSO and SLO

You can implement both single sign-on (SSO) and single logout (SLO) with AM SAML 2.0.

SSO is the ability to log in once but access multiple applications, whereas SLO is the ability to terminate multiple login sessions by logging out of one central place.

AM provides two ways to implement SSO: *integrated mode* and *standalone mode*. You must use standalone mode to implement SLO because integrated mode supports SSO only.

SSO can be initiated either from the SP or the IdP:

* SP-initiated SSO

  The SP initiates the login request.

  A common reason to choose SP-initiated SSO is the ability for end users to access specific URLs within the application immediately upon login.

  For example:

  1. If an end user navigates to the SP first, then the SP directs them to the IdP for the login.

  2. If the end user already has a session on the IdP, then the IdP redirects them back to the SP with a SAML assertion.

  3. If the end user doesn't have a session, they enter their credentials. After a successful login, they are redirected back to the SP with a SAML assertion.

  4. The end user can access the SP application.

  Find an example use case in [Grant access to Google Workspace](saml2-introduction.html#saml2-use-case-spinit).

* IdP-initiated SSO

  The IdP initiates the login to the SP.

  An IdP-initiated SSO flow can simplify the user experience by making an application appear part of the IdP's portal.

  For example:

  1. The end user is already logged into the IdP and clicks the application (SP) they want to access.

  2. The IdP sends a SAML assertion to the SP.

  3. The end user is allowed access to the SP application.

  Find an example use case in [Grant access to a pension application through a workplace portal](saml2-introduction.html#saml2-use-case-idpinit).

## Integrated or standalone mode

Your deployment requirements determine whether you should implement SAML 2.0 in integrated or standalone mode.

* Integrated mode

  This option uses nodes and trees to integrate SAML 2.0 SSO into the AM authentication process. SP-initiated SSO in integrated mode must use the [SAML2 Authentication node](https://docs.pingidentity.com/auth-node-ref/8.1/saml2.html).

* Standalone mode

  Access servlet URLs to initiate SSO and SLO.

  |   |                                                                                                                                                                                      |
  | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
  |   | You can also configure web and Java agents to work alongside AM when performing SSO and SLO. Find out more in [Web or Java agents SSO and SLO](using-saml2-with-policy-agents.html). |

**Integrated or standalone mode?**

| Deployment task or requirement                                                            | Implementation mode                                                                                                                                                                                                        |
| ----------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| You want to deploy only SAML 2.0 SSO using the easiest technique.                         | Use [integrated mode](saml2-integrated-mode.html).                                                                                                                                                                         |
| You want to deploy both SAML 2.0 SSO and SLO.                                             | Use [standalone mode](saml2-standalone-mode.html).                                                                                                                                                                         |
| You want to deploy SAML 2.0 IdP-initiated SSO.                                            | Use a [standalone URL](saml2-standalone-mode.html) to trigger the flow\.Set [configuration](saml2-integrated-mode.html#saml2-integrated-mode-sso-trees-procedure) to run in [integrated mode](saml2-integrated-mode.html). |
| You want to use the SAML 2.0 Enhanced Client or Proxy (ECP) SSO profile.                  | Use [standalone mode](saml2-standalone-mode.html).                                                                                                                                                                         |
| Your IdP and SP instances are using the same domain name; for example, `mydomain.net`.(1) | Use [standalone mode](saml2-standalone-mode.html).                                                                                                                                                                         |

(1) You can't use integrated mode when both the IdP and SP share a domain name because of the way it tracks the authentication status using a cookie.

---

---
title: Integrate with the Fedlet WAR File
description: Integrate your applications with the Java Fedlet to perform SAML 2.0 service provider operations and single sign-on
component: pingam
version: 8.1
page_id: pingam:am-saml2:fedlet-war-integrate
canonical_url: https://docs.pingidentity.com/pingam/8.1/am-saml2/fedlet-war-integrate.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["SAML 2.0", "Single Sign-on (SSO)", "Federation", "Fedlet", "Integration"]
page_aliases: ["saml2-guide:fedlet-war-integrate.adoc"]
section_ids:
  hello-world-with-fedlet: Integrate your application
  fedlet-perform-sso: Perform single sign-on
  fedlet-perform-slo: Perform single logout
---

# Integrate with the Fedlet WAR File

You can integrate your applications with the Java Fedlet to perform many of the SAML 2.0 SP operations. The Java Fedlet offers the SAML 2.0 capabilities identified in [Fedlet Support for SAML 2.0 Features](saml2-implementation-fedlet.html#fedlet-saml2-features).

## Integrate your application

The Fedlet includes the following files that you can use when building your own SP application:

* `conf/`

  Configuration files copied to the `$HOME/fedlet` directory when you first deploy and configure the Fedlet. When deploying your application, you can move these to an alternate location passed to the Java virtual machine for the web application container at startup. For example, if you store the configuration under the `/export/fedlet/` directory, then you could pass the following property to the JVM.

  ```
  -Dcom.sun.identity.fedlet.home=/export/fedlet/conf
  ```

  You do not need to include these files in your application.

* `fedletAttrQuery.jsp`

  Sample SAML attribute query and response handlers.

* `fedletEncode.jsp`

  Utility JSP to encode a password, such as the password used to protect a Java keystore.

* `fedletSampleApp.jsp`

  Demo application. You can remove these before deployment to replace them with your application.

* `fedletXACMLQuery.jsp`

  Sample SAML XACML query and response handlers.

* `logout.jsp`

  Utility page to perform single log out.

* `saml2/jsp/`

  JSPs to initiate single sign-on and single logout, and to handle errors, and also a JSP for obtaining Fedlet metadata, `saml2/jsp/exportmetadata.jsp`.

* `WEB-INF/classes/`

  Localized Java properties files for strings used in the Fedlet user interface.

* `WEB-INF/lib/`

  Fedlet libraries required by your application.

* `WEB-INF/web.xml`

  Fedlet web application configuration, showing how JSPs map to URLs used in the Fedlet. Add mappings for your application before deployment.

  In the `web.xml` mappings, your application must be mapped to `/fedletapplication`, as this is the assertion consumer URL set in the Fedlet metadata.

  ```xml
  <servlet>
    <servlet-name>yourApp</servlet-name>
    <jsp-file>/fedletSampleApp.jsp</jsp-file>
  </servlet>
  <servlet-mapping>
    <servlet-name>yourApp</servlet-name>
    <url-pattern>/fedletapplication</url-pattern>
  </servlet-mapping>
  ```

Follow these steps for a demonstration of how to customize demo pages within the Fedlet:

1. Backup the `fedletSampleApp.jsp` file.

   ```bash
   $ cd /path/to/tomcat/webapps/fedlet/
   $ cp fedletSampleApp.jsp fedletSampleApp.jsp.orig
   ```

2. Edit the `fedletSampleApp.jsp` file to reduce it to a single redirection to the `myapp.jsp` page. An implementation of the `<html>` element of the file follows below.

   ```html
   <html>
       <head>
           <title>Fedlet Sample Application</title>
           <meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1" />
       </head>
       <body>
           <%
            // BEGIN : following code is a must for Fedlet (SP) side application
            Map map;
            try {
                // invoke the Fedlet processing logic. this will do all the
                // necessary processing conforming to {saml2_abbr} specifications,
                // such as XML signature validation, Audience and Recipient
                // validation etc.
                map = SPACSUtils.processResponseForFedlet(request, response,
                new PrintWriter(out, true));
                response.sendRedirect("myapp.jsp");
            } catch (SAML2Exception sme) {
                SAMLUtils.sendError(request, response,
                response.SC_INTERNAL_SERVER_ERROR, "failedToProcessSSOResponse",
                sme.getMessage());
                return;
            } catch (IOException ioe) {
                SAMLUtils.sendError(request, response,
                response.SC_INTERNAL_SERVER_ERROR, "failedToProcessSSOResponse",
                ioe.getMessage());
                return;
            } catch (SessionException se) {
                SAMLUtils.sendError(request, response,
                response.SC_INTERNAL_SERVER_ERROR, "failedToProcessSSOResponse",
                se.getMessage());
                return;
            } catch (ServletException se) {
                SAMLUtils.sendError(request, response,
                response.SC_BAD_REQUEST, "failedToProcessSSOResponse",
                se.getMessage());
                return;
            }
            // END : code is a must for Fedlet (SP) side application
           %>
       </body>
   </html>
   ```

3. Add a `myapp.jsp` page to the Fedlet, such as the following:

   ```html
   <html>
       <head>
           <title>My Application</title>
           <meta http-equiv="Content-Type" content="text/html" />
       </head>
       <body>
           <h1>My Application</h1>
           <p>After you change the <code>fedletSampleApp.jsp</code>, all it does
              is redirect to this home page after successful login.</p>
       </body>
   </html>
   ```

4. Go to the Fedlet URL, such as `https://am.example.com:8443/fedlet/`, and try one of the login methods.

   After login, you are redirected to the `myapp.jsp` page.

## Perform single sign-on

The Java Fedlet includes a JSP file, `saml2/jsp/fedletSSOInit.jsp`, that you can call to initiate single sign-on from the Fedlet (SP) side. The Fedlet home page, `index.jsp`, calls this page when the user does Fedlet-initiated single sign-on.

When calling this JSP, the parameters to use are those also used by the `saml2/jsp/spSSOInit.jsp` page in AM. The parameters are described in [Implement SSO and SLO](saml2-sso-slo.html).

For IdP-initiated single sign-on, call the appropriate page on the IdP. AM's page is described in [Implement SSO and SLO](saml2-sso-slo.html).

After single sign-on, the user-agent is directed by default to the assertion consumer URI set in the Fedlet metadata, which by default is `/fedletapplication`. Also by default, that URI points to the JSP, `fedletSampleApp.jsp`.

## Perform single logout

The Java Fedlet includes a JSP file, `saml2/jsp/spSingleLogoutInit.jsp`, that you can call to initiate single logout from the Fedlet (SP) side. The Fedlet assertion consumer page, `fedletSampleApp.jsp`, calls this when the user does Fedlet-initiated single logout.

When calling this JSP, the parameters to use are those also used by the `saml2/jsp/spSingleLogoutInit.jsp` page in AM. Those parameters are described in [Implement SSO and SLO](saml2-sso-slo.html).

For IdP-initiated single logout, call the appropriate page on the IdP. AM's page is described in [Implement SSO and SLO](saml2-sso-slo.html).

Set the `RelayState` parameter when initiating logout to redirect the user-agent appropriately when the process is complete.

---

---
title: Introduction to SAML 2.0
description: Learn how SAML 2.0 enables federated identity and single sign-on by allowing organizations to share identities and services through identity providers and service providers that trust each other
component: pingam
version: 8.1
page_id: pingam:am-saml2:saml2-introduction
canonical_url: https://docs.pingidentity.com/pingam/8.1/am-saml2/saml2-introduction.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["SAML 2.0", "Single Sign-on (SSO)"]
page_aliases: ["saml2-guide:saml2-introduction.adoc"]
section_ids:
  saml2-terminology: Terminology
  saml2-concepts: Concepts
  saml2-exmaple-flow: Example flow
  use_cases: Use cases
  saml2-use-case-spinit: Grant access to Google Workspace
  saml2-use-case-idpinit: Grant access to a pension application through a workplace portal
---

# Introduction to SAML 2.0

SAML 2.0 helps organizations share, or *federate* identities and services, without having to manage the identities or credentials themselves. The credentials are managed by a single entity, known as the *identity provider* (IdP). The services are provided by *service providers* (SPs). Both providers are configured to trust one another.

![A high-level overview of the SAML 2.0 participants in AM.](_images/saml2-high-level.png)Figure 1. Overview of SAML 2.0 in AM

AM uses the concept of the *circle of trust* to manage the relationship between IdPs and SPs.

## Terminology

| Term                            | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| ------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **End user**                    | The person who is attempting to access the resource or application. In SAML 2.0, the end user is often referred to as the *subject*.The end user uses a *user-agent*, usually a web browser, when performing a SAML 2.0 flow.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| **Single sign-on (SSO)**        | The ability for an end user to authenticate once but gain access to multiple applications, without having to authenticate separately to each one.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| **Single log out (SLO)**        | The ability for an end user to log out once but terminate sessions in multiple applications, without having to log out separately from each one.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| **Assertions**                  | An assertion is a set of statements about an authenticated user that let services make authorization decisions, that is, whether to allow that user to access the service, and what functionality they can use.SAML assertions are XML-formatted tokens. Assertions issued by AM can contain the following information about an end user:- Their attributes, such as pieces of information from the user's profile.

- The level of authentication they have performed.                                                                                                                                                                                                                                                                                                 |
| **Identity provider (IdP)**     | The IdP is responsible for authenticating end users, managing their account, and issuing SAML assertions about them.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| **Service provider (SP)**       | The provider of the service or application that the end user is trying to access.The SP has a trust relationship with the IdP, which enables the SP to rely on the assertions it receives from the IdP.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| **Circle of trust (CoT)**       | A circle of trust is an AM concept that groups at least one IdP and at least one SP who agrees to share authentication information.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| **Hosted and remote providers** | A *hosted* provider is one served by the current AM instance; a *remote* provider is one hosted elsewhere.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| **Metadata**                    | Providers in SAML 2.0 share *metadata*, which represents the configuration of the provider, as well as the mechanisms it can use to communicate with other providers.For example, the metadata may contain necessary certificates for signing verification, as well as which of the SAML 2.0 bindings are supported.Sharing metadata greatly simplifies the creation of SAML 2.0 providers in a circle of trust. AM can import the XML-formatted metadata provided by remote providers. You can also export the metadata from hosted providers.For more information about metadata, refer to [Metadata for the OASIS Security Assertion Markup Language (SAML) 2.0](http://docs.oasis-open.org/security/saml/v2.0/saml-metadata-2.0-os.pdf) in the *SAML 2.0 Standard*. |

## Concepts

Security Assertion Markup Language (SAML) 2.0 is a standard that lets users access multiple services with a single set of credentials. The services may be provided by different organizations, using multiple domains. In summary, SAML 2.0 provides cross-domain single sign-on (CDSSO).

For more information, refer to [Security Assertion Markup Language (SAML) 2.0](https://www.oasis-open.org/standards#samlv2.0).

SAML 2.0 depends on standards for describing how the providers interact and exchange information. The SAML 2.0 standards describe the messages sent between providers, how they are relayed, how they are exchanged, and common use cases.

In federation deployments where not all providers support SAML 2.0, AM can act as a multi-protocol hub; translating for providers that rely on other and older standards, such as WS-Federation. You can find an integration example in [How do I configure PingAM as an Identity Provider for Microsoft Office 365 and Azure using WS-Federation?](https://support.pingidentity.com/s/article/How-do-I-configure-PingAM-as-an-Identity-Provider-for-Microsoft-Office-365-and-Azure-using-WSFederation) in the *Knowledge Base*.

When your organization acts as the IdP and you want to enable SPs to federate their services with yours, you can generate configuration files for a *fedlet*.

An AM fedlet is a small Java web application that can act as an SP for a specific IdP without requiring that you install all of AM. For more information on fedlets, refer to [Implement SAML 2.0 SPs by using Fedlets](saml2-implementation-fedlet.html).

## Example flow

When configuring AM to provide single sign-on using SAML 2.0, you can:

* Map accounts at the IdP to accounts at the SP, including mapping to an anonymous user.

* As the IdP, make assertions to the SP, for example, to attest that the end user has authenticated with the IdP.

  The SP then consumes assertions from the IdP to make authorization decisions, for example, to let an authenticated user complete a purchase that gets charged to the user's account at the IdP.

![A possible SAML 2.0 flow.](_images/saml2-flow.svg)Figure 2. SAML 2.0 flow

1. An unauthenticated user attempts to access a SAML 2.0 SP.

2. The SP determines the IdP associated with the end user, and redirects the user's browser to the IdP, using an HTTP 302 Redirect message. A SAML 2.0 authentication request is included in the query string.

   This is an example of *HTTP-Redirect* binding and is the default when requesting SAML authentication by AM. AM also supports the *HTTP-POST* binding for processing SAML 2.0 authentication requests.

   AM provides two deployment models to support single sign-on (SSO) when contacting the SP initially. For details, refer to [Implement SSO and SLO](saml2-sso-slo.html).

3. The IdP validates the request, determines the authentication method that should be used, and authenticates the user.

   The SP can specify a particular [tree for authentication](saml2-providers-and-cots.html#samlapp-tree), or it can include requirements for the user such as to authenticate with multiple factors.

4. The IdP creates a *SAML Artifact*, which contains a unique artifact ID for the SAML 2.0 response.

   The IdP redirects the end user's browser to the SP, and includes the SAML Artifact in the query parameters. The browser only has access to the artifact ID rather than the SAML response itself, reducing risk of malicious interference.

5. The SP communicates directly with the IdP using the SOAP protocol to retrieve the SAML response relating to the artifact ID.

   The IdP returns the SAML response, including the assertion using the SOAP protocol, directly to the SP.

   The information in the SAML response is not shared with the user agent. This is an example of *HTTP-Artifact* binding, and is the default when AM is returning SAML assertions. AM also supports the *HTTP-POST* binding for transmitting SAML 2.0 assertions.

6. The SP validates the SAML response and that the signature matches the public key it holds for the IdP.

   Optionally, the SP can choose to create a new account locally for the user or associate an identifier in the assertion with a user account it already has locally. Linked accounts are often referred to as a *federated identity*. Refer to [Federate identities](saml2-linking-accounts.html).

   |   |                                                                                                                                                                                                                               |
   | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | To link to an existing account, the SP can require the end user to also authenticate to the SP to determine the matching local account. After linking, the user only needs to authenticate at the IdP when attempting access. |

7. The SP can now use the information in the assertion and the local federated identity to authorize the user and decide whether to grant access to its services.

## Use cases

The following use cases describe how AM SAML 2.0 can meet different authentication requirements.

### Grant access to Google Workspace

A common use case for SAML 2.0 is giving your staff access Google Workspace applications, such as Google Docs and Google Sheets. This section explains how AM provides this solution.

In this scenario, Google acts as the SP, and AM acts as the IdP for a hypothetical organization, Example.com.

1. In AM, an admin user configures an AM instance as the IdP.

2. The admin user then configures Google Workspace as a remote SP and provides the values that Google requires to use AM as its IdP. For example, the login and logout URLs, profile management URLs, and validation certificate.

3. The Google Workspace administrator enters the provided URLs and certificate into the Google Workspace Admin console for the domain being configured.

4. After configuration, users attempting to access a Google Workspace service must provide their corporate email address:

   ![Provide Google with your corporate email address, so the relevant IdP can be determined.](_images/scenario-gsuite-identify-to-google.png)

5. Based on the domain of the email address, Google redirects the user to sign in to AM, acting as the IdP.

6. After successfully authenticating with AM, the user is redirected back to the Google Workspace application, for example, Google Docs.

   Google, acting as the SP, creates a federated identity in its systems to manage local account options, such as privacy settings. The user can now access any of the Google Workspace apps, by authenticating to the IdP using their corporate Example.com account:

   ![Google Docs showing a federated identity authenticated by AM, the trusted IdP.](_images/scenario-gsuite-federated-identity.png)

Learn more about this SAML flow in [SP-initiated SSO integrated mode flow](saml2-integrated-mode.html#spinit-sso-integrated-mode).

### Grant access to a pension application through a workplace portal

This scenario describes an employee who wants to check their pension details from their company website. The company, Example.com, provides an application dashboard to its employees, which includes an option to access their pension provider, MyPension.

An IdP-initiated SSO flow in integrated mode lets the employee authenticate with the third-party workplace portal and bypass the pension app's login page.

1. In AM, the admin user configures MyPension as the hosted SP and imports the metadata for the remote IdP (Example.com) to create a circle of trust.

   The hosted SP configuration includes a login journey to handle the pension provider's authentication requirements, such as adding multi-factor authentication.

2. MyPension provides a URL for Example.com to embed in its website.

   Learn more about configuring this URL in [Assertion Consumer Service](saml2-reference.html#config-hosted-sp-acs).

3. The employee provides their credentials to Example.com and clicks the embedded link to the pension app in the dashboard.

4. As the IdP, Example.com authenticates the employee and redirects them to MyPension (the SP).

5. AM, acting as the SP, validates the IdP, identifies the employee, and runs the authentication journey.

   The authentication journey verifies that the employee has the required authorization level for their organization.

6. The employee is redirected to the MyPension website and granted access to their pension details.

Learn more about this SAML flow in [IdP-initiated SSO integrated mode flow](saml2-integrated-mode.html#idpinit-sso-integrated-mode).

---

---
title: Link identities automatically with auto-federation
description: Configure PingAM to automatically link identities across SAML 2.0 providers based on matching attribute values
component: pingam
version: 8.1
page_id: pingam:am-saml2:auto-federation
canonical_url: https://docs.pingidentity.com/pingam/8.1/am-saml2/auto-federation.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["SAML 2.0", "Single Sign-on (SSO)", "Federation"]
page_aliases: ["saml2-guide:auto-federation.adoc"]
section_ids:
  auto-federate-based-on-attribute: Link identities automatically based on an attribute value
---

# Link identities automatically with auto-federation

AM lets you configure the SP to automatically link identities based on an attribute value in the assertion returned from the IdP, known as *auto-federation*.

When you know the user accounts on both the IdP and the SP share a common attribute value, such as an email address or other unique user identifier, you can configure AM to map the attributes to each other, and link identities, without the user having to authenticate to the SP.

## Link identities automatically based on an attribute value

This procedure demonstrates how to automatically link identities based on an attribute value that is the same in both accounts.

Before attempting to configure auto-federation, ensure that you have configured AM for SAML 2.0, created the identity and SPs, and configured a circle of trust. You must also have configured AM to support single sign-on. For information on performing those tasks, see [Deployment considerations](saml2-configuration.html) and [Implement SSO and SLO](saml2-sso-slo.html).

Perform the following steps on the hosted IdP(s), and again on the hosted SP(s):

1. Go to Realms > *realm name* > Applications > Federation > Entity Providers, and click on the name of the hosted provider.

AM only displays the configuration of a single role. Click on the labels to select the role view:

![saml-roles](_images/saml-roles.png)

1. On the hosted IdP:

   * Go to the Assertion Processing tab.

   * Review the Attribute Map configuration. If the attributes you want to use to link the accounts on the IdP and the SP are not in the map already, add them.

     The IdP will send these attributes in the assertion, and the SP will then map them using its own attribute map.

     > **Collapse: Tips to configure the Attribute Map on the IdP**
     >
     > Before user profile attributes can be mapped, they must be allowed in user profiles and also specified for the identity store. Find more information in [Add custom user profile attributes](../setup/customizing-data-stores.html#sec-maint-datastore-customattr).
     >
     > To see the profile attributes available for an LDAP identity store, log in to the AM admin UI, and go to Realms > *realm name* > Identity Stores > User Configuration. Check the LDAP User Attributes list.
     >
     > By default, you can map single-valued attributes to either user profile attributes or static values.
     >
     > To map a static value, enclose the value in double quotes (`"`), for example:
     >
     > ![The static value is enclosed in double quotes.](_images/static-attr-mapping.png)
     >
     > Figure 1. Example of mapping a static value
     >
     > To map multi-valued attributes, you must implement a [custom IdP attribute mapper](custom-idp-attribute-mapper.html).

   * Save your work.

2. On the hosted SP:

   * Go to the Assertion Processing tab.

   * Review the Attribute Map configuration, and ensure that the attribute mappings you created on the IdP are represented in the map.

     > **Collapse: Tips to Configure the Attribute Map on the SP**
     >
     > The value of Key is a SAML attribute sent in an assertion, and the value of Value is a property in the authenticated session, or an attribute of the user's profile.
     >
     > By default, the SP maps the SAML attributes it receives to equivalent-named session properties. However, when the SP is configured to create identities during autofederation and the identity does not exist yet, the SP maps the SAML attributes to their equivalents in the newly-created user profile.
     >
     > The special mapping `Key: *, Value: *` means that the SP maps each attribute it receives in the assertion to equivalent-named properties or attributes. For example, if the SP receives `mail` and `firstname` in the assertion, it maps them to `mail` and `firstname` respectively.
     >
     > Remove the special mapping and add key pairs to the map if:
     >
     > * (During autofederation) The attributes in the IdP's and the SP's identity stores do not match.
     >
     > * You need control over the names of the session properties.
     >
     > * You need control over which attributes the SP should map, because the IdP adds too many to the assertion.
     >
     > For example, if the SAML attribute is `firstname` and you want the SP to map it to a session property/user profile attribute called `cn`, create a mapping similar to `Key: firstname, Value: cn`.

   * Enable Auto Federation. In the Attribute property, enter the SAML attribute name that the SP will use to link accounts, as configured in the Attribute Map.

   * Save your work.

3. To test your work, initiate single sign-on; for example, as described in [IdP-initiated SSO URLs](saml2-standalone-mode.html#saml2-sso-standalone-idpssoinit).

   Authenticate to the IdP as a test user. Attempt to access the SP. Notice that the user has an authenticated session, and can access their profile page on the SP without having to authenticate again.

---

---
title: Link identities for authentication
description: Link identities between IdP and SP accounts using pseudonym identifiers and authentication trees in PingAM
component: pingam
version: 8.1
page_id: pingam:am-saml2:linking-auth-tree
canonical_url: https://docs.pingidentity.com/pingam/8.1/am-saml2/linking-auth-tree.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["SAML 2.0", "Single Sign-on (SSO)", "Federation", "Authentication", "Accounts", "Nodes &amp; Trees", "Scripts"]
page_aliases: ["saml2-guide:linking-auth-tree.adoc"]
section_ids:
  first_authentication_to_the_sp: First authentication to the SP
  subsequent_authentications_to_the_sp: Subsequent authentications to the SP
  configure-authentication-linking: Configure authentication mechanisms to link accounts
  saml2-integrated-mode-sso-persistent-standard: Link accounts persistently (standalone AM)
  saml2-integrated-mode-sso-persistent-platform: Link accounts persistently (Ping Advanced Identity Software deployment)
---

# Link identities for authentication

IdPs and SPs must be able to communicate information about users. Sometimes the IdP chooses to share a minimum amount of information about an authenticated user.

For example, the IdP can return a generated, opaque `NameID` that can't directly be used to locate an identity in the SP identity store.

AM can use these pseudonym identifiers to establish links between otherwise unrelated accounts, by requiring that the user authenticates to the SP using a linking authentication mechanism.

## First authentication to the SP

The following flow shows the sequence of events that occurs when a user first attempts to authenticate to the AM SP:

![Sequence diagram: first authentication to the SP](_images/linking-auth-tree-first-auth.svg)Figure 1. First authentication to the SP flow

1. **Accessing the SP**

   A user attempts to access a service and is redirected to the AM server acting as the SP.

   The redirect URL specifies an authentication tree containing the [SAML2 Authentication node](https://docs.pingidentity.com/auth-node-ref/8.1/saml2.html). For example, `https://www.sp.com:8443/am/XUI/#login/&service=spSAMLTree`.

2. **Authentication at the IdP**

   AM redirects the user to the IdP. The user authenticates successfully at the IdP. The IdP returns a SAML assertion to AM.

3. **SP attempts to access a federated identity**

   AM attempts to locate the identity in its user store but finds no link between the IdP identity and a local identity.

4. **Invocation of the linking authentication node(s)**

   Because no link is found, AM uses the configured authentication tree to authenticate the user.

5. **Identity federation**

   After successfully authenticating the user, AM writes the name ID from the assertion into the user's local profile, creating a permanent link between the two identities.

   Find information on creating permanent links between identities in [Persistent or transient federation](persistent-or-transient-federation.html).

   Find an example of an authentication tree that links identities in [Create accounts dynamically during federation](saml2-integrated-mode.html#saml2-integrated-mode-sso-dynamic-standard).

## Subsequent authentications to the SP

The following flow shows the sequence of events that occurs during subsequent authentication attempts after the user's identities on the IdP and SP have been federated:

![Sequence diagram: subsequent authentications to the SP](_images/linking-auth-tree-subsequent-auth.svg)Figure 2. Subsequent authentications to the SP flow

1. **Accessing the SP**

   A returning user attempts to access their service and is redirected to the AM server acting as the SP.

   Their login URL specifies the authentication tree containing the [SAML2 Authentication node](https://docs.pingidentity.com/auth-node-ref/8.1/saml2.html) and the [Write Federation Information node](https://docs.pingidentity.com/auth-node-ref/8.1/write-federation-information.html). For example, `https://www.sp.com:8443/am/XUI/#login/&service=spSAMLTree`.

2. **Authentication at the IdP**

   AM redirects the user to the IdP, and the user authenticates successfully at the IdP. The IdP returns a SAML assertion to AM.

3. **SP attempts to access a federated identity**

   AM attempts to locate the name ID in its user store. The search for the name ID succeeds.

   Because there's a match, the user doesn't need to authenticate to AM and can access the service.

## Configure authentication mechanisms to link accounts

If you aren't using auto-federation, configure AM to link accounts in one of the following ways, depending on whether AM is standalone or part of an integrated Ping Advanced Identity Software deployment.

### Link accounts persistently (standalone AM)

Configure a tree similar to the following:

![Example tree to link accounts persistently](../am-authentication/_images/trees-node-write-federation-information-example.png)

1. Add a [SAML2 Authentication node](https://docs.pingidentity.com/auth-node-ref/8.1/saml2.html).

   Make sure that the NameID Format specified is `persistent`.

   The node processes the assertion, makes its contents available to the authentication tree's state in the `userInfo` object, and tries to map the assertion's nameID using the `uid` mapping in the SP's assertion map.

   If the node finds a match, the tree continues through the `Account Exists` output. Otherwise, the tree continues through the `No Account Exists` output.

2. On the `No Account Exists` outcome, configure nodes to authenticate the user to the SP.

3. Add a [Write Federation Information node](https://docs.pingidentity.com/auth-node-ref/8.1/write-federation-information.html).

### Link accounts persistently (Ping Advanced Identity Software deployment)

Configure a journey similar to the following:

![Example tree to link accounts persistently](_images/link-accounts-platform-example.png)

1. Add a [SAML2 Authentication node](https://docs.pingidentity.com/auth-node-ref/8.1/saml2.html).

   Make sure that the NameID Format specified is `persistent`.

   The node processes the assertion, makes its contents available to the tree's state in the `userInfo` object, and tries to map the assertion's nameID using the `uid` mapping in the SP's assertion map.

   If the node finds a match, the tree continues through the `Account Exists` outcome. Otherwise, the tree continues through the `No Account Exists` outcome.

   Regardless of the outcome, because the node's `nameID` mapping isn't configurable, this example adds nodes to process the `userInfo` object and match it to the managed user's schema.

2. Add a [Scripted Decision node](https://docs.pingidentity.com/auth-node-ref/8.1/scripted-decision.html) to copy the information from the assertion to the authentication tree's shared state.

   > **Collapse: Example next-generation script**
   >
   > ```javascript
   > if (nodeState.get("userInfo")) {
   >   if (nodeState.get("objectAttributes")) {
   >     nodeState.remove("objectAttributes");
   >   }
   >   var userName=null,sn=null,mail=null;
   >
   >   try {
   >     var attribs = nodeState.get("userInfo")["attributes"];
   >
   >     userName=attribs["uid"][0];
   >     sn=attribs["sn"][0];
   >     mail=attribs["mail"][0];
   >
   >   } catch (e) {
   >     logger.error("Error getting userInfo: " + e);
   >   }
   >   nodeState.putShared("username", userName);
   >   nodeState.putShared("objectAttributes", {"userName":userName,"sn":sn,"mail":mail, "givenName": userName});
   > }
   > action.goTo("true");
   > ```
   >
   > |   |                                                                                       |
   > | - | ------------------------------------------------------------------------------------- |
   > |   | You can also query the `samlApplication` binding on the SP side to get the assertion. |

3. Add an [Identify Existing User node](https://docs.pingidentity.com/auth-node-ref/8.1/identify-existing-user.html) to search the user with the appropriate attribute.

   For example, `userName`.

4. Authenticate the user to the SP.

5. Add the [Write Federation Information node](https://docs.pingidentity.com/auth-node-ref/8.1/write-federation-information.html) to the successful outcome of the authentication process to create the link between the accounts.

   If a transient link exists, it is converted into a persistent one.

---

---
title: Link identities to a single, shared account
description: Link identities to a single, shared account on the SP to exchange attributes without creating user-specific accounts using SAML 2.0 federation
component: pingam
version: 8.1
page_id: pingam:am-saml2:auto-federate-using-anonymous
canonical_url: https://docs.pingidentity.com/pingam/8.1/am-saml2/auto-federate-using-anonymous.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["SAML 2.0", "Single Sign-on (SSO)", "Federation", "Accounts"]
page_aliases: ["saml2-guide:auto-federate-using-anonymous.adoc"]
section_ids:
  link_identities_to_an_sp_account: Link identities to an SP account
---

# Link identities to a single, shared account

You temporarily map identities on the IdP to a single account on the SP, for example, the `anonymous` account, to exchange attributes about the user without a user-specific account on the SP.

This approach can be useful when the SP either needs no user-specific account to provide a service, or when you don't want to create or retain identity data on the SP, but instead you make authorization decisions based on attribute values from the IdP.

## Link identities to an SP account

The following steps demonstrate how to auto-federate using a single user account on the SP.

Before attempting these steps, ensure that you have configured AM for SAML 2.0, created the identity and SPs, and configured a circle of trust. You must also have configured AM to support single sign-on. For information on performing those tasks, see [Deployment considerations](saml2-configuration.html) and [Implement SSO and SLO](saml2-sso-slo.html).

1. On the hosted IdP:

   * In the AM admin UI, go to Realms > *realm name* > Applications > Federation > Entity Providers > *hosted IdP*.

   * On the Assertion Processing tab, if the attributes you want to access from the SP are not yet included in the Attribute Map property, add the attribute mappings.

     Enter attribute map values using the following format: `SAML Attribute Name=Profile Attribute Name`.

   * Save your work.

2. On the hosted SP:

   * In the AM admin UI, go to Realms > *realm name* > Applications > Federation > Entity Providers > *hosted SP*.

   * On the Assertion Processing tab, if the attributes you want to access from the IdP are not yet included in the Attribute Map property, add the attribute mappings.

     Enter attribute map values using the following format: `SAML Attribute Name=Profile Attribute Name`.

     |   |                                                                                                                                                                    |
     | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
     |   | You can use a special wildcard mapping of `*=*`, which maps each attribute in the assertion to an identically named attribute on the SP, using the relevant value. |

   * Ensure that the Auto Federation property is not selected.

   * In the Transient User field, add the account name AM will use to link all identities from the IdP, for example; `anonymous`.

   * Save your work.

3. To test your work:

   * Create a new user on the IdP, including values for any attributes you mapped in the providers.

   * Log out of the AM admin UI, and initiate SSO using transient federation; for example, as described in [Enable transient federation](persistent-or-transient-federation.html#transient-federation).

   * Authenticate to the IdP as the new user you created.

   * After successfully authenticating to the IdP, check that the identity is linked to a transient account by performing the following steps:

     * In a separate browser or private window, log in to the AM admin UI of the SP.

     * Go to Realms > *realm name* > Sessions.

     * Enter the transient user name you configured earlier; for example, `anonymous`.

       You will see one or more sessions of users who have initiated single sign-on and been temporarily linked to the transient user account.

---

---
title: NameID mapper
description: Customize the NameID attribute value returned in SAML assertions using Java or JavaScript extensions
component: pingam
version: 8.1
page_id: pingam:am-saml2:custom-nameid-mapper
canonical_url: https://docs.pingidentity.com/pingam/8.1/am-saml2/custom-nameid-mapper.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["SAML 2.0", "Single Sign-on (SSO)", "Federation", "Customization", "Java", "Scripts"]
page_aliases: ["saml2-guide:custom-nameid-mapper.adoc"]
section_ids:
  java_example: Java example
  scripted_example: Scripted example
---

# NameID mapper

Use this extension point to customize the value of the NameID attribute returned in the SAML assertion.

These steps assume your environment is already correctly configured for SSO using SAML 2.0, where AM is the hosted IdP.

## Java example

To create a custom NameID mapper in Java, follow these high-level steps:

1. Clone the [am-external](https://github.com/ForgeRock/am-external) Git repository. For example:

   ```bash
   $ git clone https://github.com/ForgeRock/am-external.git
   ```

   Learn about using AM source code in [How do I access the proprietary Maven repositories?](https://support.pingidentity.com/s/article/How-do-I-access-the-proprietary-Maven-repositories).

2. Check out the branch for your release version, for example:

   ```bash
   $ cd am-external
   $ git checkout releases/[.replaceable]##version##
   $ cd openam-federation
   ```

3. Create a new Java project and add the `openam-federation-library` as a Maven dependency, for example:

   ```bash
   <dependency>
     <groupId>org.forgerock.am</groupId>
     <artifactId>openam-federation-library</artifactId>
   </dependency>
   ```

4. Write a Java class that extends the `com.sun.identity.saml2.plugins.DefaultIDPAccountMapper` class.

   Refer to the [com.sun.identity.saml2.plugins.IDPAccountMapper](../_attachments/apidocs/com/sun/identity/saml2/plugins/IDPAccountMapper.html) interface for implementation details.

5. Override the `getNameID()` method to return a customized NameID value. For example:

   ```bash
   public class CustomIDPAccountMapper extends DefaultIDPAccountMapper{

       @Override
       public NameID getNameID(Object session, String hostEntityID, String remoteEntityID,
               String realm, String nameIDFormat) throws SAML2Exception {

           NameID myNameID = super.getNameID(session, hostEntityID, remoteEntityID, realm, nameIDFormat);

           if (remoteEntityID.equals("https://sp.example.com:8443/am") {
               myNameID.setValue(myNameID.getValue() + "@sp.example.com");
           }

           return myNameID;
       }
   }
   ```

6. Package your custom class in a JAR file and copy to the `/WEB-INF/lib` folder where you deployed AM.

7. Configure AM to use the new Java plugin.

   1. In the AM admin UI, go to Realms > *realm name* > Applications > Federation > Entity Providers > *hosted IdP* > Assertion Processing.

   2. In the Account Mapper field, type the fully qualified name of your custom class.

   3. Save your changes.

8. Restart AM or the container in which it runs.

9. Test your changes.

## Scripted example

Learn about NameID mapper scripts from the following resources:

* Next-generation example script

  [SAML2 NameID Mapper Script](../am-scripting/sample-scripts.html#saml2-nameid-mapper-js)

* Scripting API

  [NameID mapper scripting API](../am-scripting/saml2-nameid-mapper-api.html)

Follow these steps to use an example script to customize the NameID value:

1. In the AM admin UI, go to Realms > *realm name* > Scripts, and [create a new script](../am-scripting/manage-scripts-console.html) of type `Saml2 NameID Mapper`.

   |   |                                                                                                                                                   |
   | - | ------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | The NameID mapper script type is a [next-generation script](../am-scripting/next-generation-scripts.html) only and must be written in JavaScript. |

2. In the Script field, set a custom value for NameID. For example:

   ```javascript
   /*
    * Retrieve nameID value from Java plugin and modify
   */
   function getModifiedNameID() {
     var nameIDValue = nameIDScriptHelper.getNameIDValue();

     if (nameIDValue.includes(".com")) {
         return nameIDValue.replace(".com", ".org");
     }
     return nameIDValue;
   }

   /*
    * Use identity binding to gather attributes
   */
   function getIdentityNameID() {
     var givenName = identity.getAttributeValues("givenName")[0];
     var lastName = identity.getAttributeValues("sn")[0];

     return givenName + "_" + lastName;
   }

   getModifiedNameID();
   //getIdentityNameID();
   ```

3. Validate and save your changes.

4. Configure AM to use the updated NameID mapper script.

   1. In the AM admin UI, go to Realms > *realm name* > Applications > Federation > Entity Providers > *remote SP* > Assertion Processing.

   2. Under Account Mapper, select your script from the SAML2 Name ID Mapper Script drop-down list.

   3. Save your changes.

5. Test your changes using an SP-initiated flow.

   Verify that the SAML 2.0 assertion shows an updated value, for example:

   ```xml
   <saml:NameID Format="urn:oasis:names:tc:SAML:1.1:nameid-format:emailAddress"
                NameQualifier="idp"
                SPNameQualifier="sp">bjensen@example.org</saml:NameID>
   ```