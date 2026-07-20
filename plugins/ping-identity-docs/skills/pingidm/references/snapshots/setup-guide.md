---
title: Architectural overview
description: Overview of the PingIDM architecture, including the OSGi framework, infrastructure modules, core services, and REST and UI access layer
component: pingidm
version: 8.1
page_id: pingidm:setup-guide:chap-overview
canonical_url: https://docs.pingidentity.com/pingidm/8.1/setup-guide/chap-overview.html
llms_txt: https://docs.pingidentity.com/pingidm/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Setup", "Configuration", "Architecture", "Modules", "Core Module"]
section_ids:
  openidm-modular-framework: Modular framework
  openidm-infrastructure-modules: Infrastructure modules
  openidm-core-services: Core services
  openidm-access-layer: Access layer
---

# Architectural overview

This topic introduces the IDM architecture, and describes component modules and services, such as:

* How IDM uses the OSGi framework as a basis for its modular architecture.

* How the infrastructure modules provide the features required for IDM's core services.

* What those core services are and how they fit in to the overall architecture.

* How IDM provides access to the resources it manages.

## Modular framework

IDM implements infrastructure modules that run in an OSGi framework. It exposes core services through RESTful APIs to client applications.

![IDM consists of infrastructure modules running in an OSGi framework, exposing core services through RESTful APIs to client applications.](_images/idm-arch.svg)Figure 1. Modular Architecture Overview

The IDM framework is based on OSGi:

* OSGi

  OSGi is a module system and service platform for the Java programming language that implements a complete and dynamic component model. For more information, refer to [What is OSGi?](https://www.osgi.org/resources/what-is-osgi/) IDM runs in [Apache Felix](https://felix.apache.org/), an implementation of the OSGi Framework and Service Platform.

* Servlet

  The Servlet layer provides RESTful HTTP access to the managed objects and services. IDM embeds the Jetty Servlet Container, which can be configured for either HTTP or HTTPS access.

|   |                                                                                                                                                                                                                                                                                                                     |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Custom servlet filters aren't supported in IDM 8.0 and later. The only `servletfilter-*` configurations you can continue to use are `CrossOriginFilter` and `LargePayloadServletFilter`. Learn more in [Discontinued functionality](../release-notes/removed-functionality.html#removed-custom-servlet-filters-80). |

## Infrastructure modules

The infrastructure modules provide the underlying features needed for core services:

* BPMN 2.0 Workflow Engine

  The embedded workflow and business process engine is based on Flowable and the Business Process Model and Notation (BPMN) 2.0 standard.

  For more information, refer to [Workflow](../workflow-guide/preface.html).

* Task Scanner

  The [task scanner](../schedules-guide/task-scanner.html) performs a batch scan for a specified property, on a scheduled interval, then executes a task when the value of that property matches a specified value.

* Scheduler

  The [scheduler](../schedules-guide/schedules.html) supports Quartz [SimpleTriggers](https://www.quartz-scheduler.org/documentation/quartz-2.5.x/tutorials/tutorial-lesson-05.html) and [CronTriggers](https://www.quartz-scheduler.org/documentation/quartz-2.5.x/tutorials/crontrigger.html). Use the scheduler to trigger regular reconciliations, liveSync, and scripts, to collect and run reports, to trigger workflows, and to perform custom logging.

* Script Engine

  The script engine is a pluggable module that provides the triggers and plugin points for IDM.

  IDM supports JavaScript and Groovy.

* Policy Service

  An extensible [policy service](../objects-guide/policies.html) applies validation requirements to objects and properties, when they are created or updated.

* Audit Logging

  Auditing logs all relevant system activity to the configured log stores. This includes the data from reconciliation as a basis for reporting, as well as detailed activity logs to capture operations on the internal (managed) and external (system) objects.

  For more information, refer to [Configure audit logging](../audit-guide/audit.html).

* Repository

  The repository provides a common abstraction for a pluggable persistence layer. IDM supports reconciliation and synchronization with several major external data stores in production, including relational databases, LDAP servers, and even flat CSV and XML files.

  The repository API uses a JSON-based object model with RESTful principles consistent with the other IDM services. Before you use IDM, you must [Select a repository](../install-guide/chap-repository.html).

## Core services

The core services are the heart of the resource-oriented unified object model and architecture:

* Object Model

  Artifacts handled by IDM are Java object representations of the JavaScript object model as defined by JSON. The object model supports interoperability and potential integration with many applications, services, and programming languages.

  IDM can serialize and deserialize these structures to and from JSON as required. IDM also exposes a set of triggers and functions that you can define in scripts, which can natively read and modify these JSON-based object model structures.

* Managed Objects

  A *managed object* is an object that represents the identity-related data managed by IDM. Managed objects are configurable, JSON-based data structures that IDM stores in its pluggable repository. The default managed object configuration includes users and roles, but you can define any kind of managed object, for example, groups or devices.

  You can access managed objects over the REST interface with a query similar to the following:

  ```none
  curl \
  --header "X-OpenIDM-Username: openidm-admin" \
  --header "X-OpenIDM-Password: openidm-admin" \
  --header "Accept-API-Version: resource=1.0" \
  --request GET \
  "http://localhost:8080/openidm/managed/..."
  ```

* System Objects

  *System objects* are pluggable representations of objects on external systems. For example, a user entry that is stored in an external LDAP directory is represented as a system object in IDM.

  System objects follow the same RESTful resource-based design principles as managed objects. They can be accessed over the REST interface with a query similar to the following:

  ```none
  curl \
  --header "X-OpenIDM-Username: openidm-admin" \
  --header "X-OpenIDM-Password: openidm-admin" \
  --header "Accept-API-Version: resource=1.0" \
  --request GET \
  "http://localhost:8080/openidm/system/..."
  ```

  There is a default implementation for the ICF framework, that allows any connector object to be represented as a system object.

* Mappings

  *Mappings* define policies between source and target objects and their attributes during synchronization and reconciliation. Mappings can also define triggers for validation, customization, filtering, and transformation of source and target objects.

  For more information, refer to [Resource mapping](../synchronization-guide/mappings.html).

* Reconciliation and Automatic Synchronization

  *Reconciliation* enables on-demand and scheduled resource comparisons between the managed object repository and the source or target systems. Comparisons can result in different actions, depending on the mappings defined between the systems.

  *Automatic synchronization* enables creating, updating, and deleting resources from a source to a target system, either on demand or according to a schedule.

  For more information, refer to [Synchronization types](../synchronization-guide/sync-types.html).

## Access layer

The access layer provides the user interfaces and public APIs for accessing and managing the repository and its functions:

* RESTful Interfaces

  IDM provides REST APIs for CRUD operations, for invoking synchronization and reconciliation, and to access several other services.

  For more information, refer to the [REST API reference](../rest-api-reference/preface.html).

* User Interfaces

  User interfaces provide access to most of the functionality available over the REST API.

---

---
title: Command-line interface
description: Use the PingIDM command-line interface to export and import configuration, configure connectors, encrypt values, hash strings, and manage keys
component: pingidm
version: 8.1
page_id: pingidm:setup-guide:chap-cli
canonical_url: https://docs.pingidentity.com/pingidm/8.1/setup-guide/chap-cli.html
llms_txt: https://docs.pingidentity.com/pingidm/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Setup", "Configuration", "CLI"]
section_ids:
  cli-configexport: configexport
  cli-configimport: configimport
  cli-configureconnector: configureconnector
  cli-encrypt: encrypt`
  cli-secure-hash: secureHash
  cli-keytool: keytool
  cli-validate: validate
---

# Command-line interface

This topic describes the basic command-line interface (CLI). The CLI includes a number of utilities for managing an IDM instance. Each utility is subcommand of the `cli.sh` (UNIX) or `cli.bat` (Windows) scripts. To use the utilities, you can run the applicable subcommand or launch the `cli` script and then run the utility. For example, to run the `encrypt` utility on a UNIX system:

```console
/path/to/openidm/cli.sh
Using boot properties at /path/to/openidm/resolver/boot.properties
openidm# encrypt ...
```

The command-line utilities run with the security properties defined in your project's `conf/secrets.json` file.

If you run the `cli.sh` command by itself, it opens an IDM-specific shell prompt:

```console
openidm#
```

|   |                                                                                                                                         |
| - | --------------------------------------------------------------------------------------------------------------------------------------- |
|   | For more information about startup and shutdown scripts, refer to [Startup configuration](../install-guide/startup-configuration.html). |

The following topics describe the subcommands and their use. Examples assume you are running the commands on a UNIX system. For Windows systems, use `cli.bat` instead of `cli.sh`.

For a list of subcommands available from the `openidm#` prompt, run the `cli.sh help` command. The following `help` and `exit` options are self-explanatory. The other subcommands are explained in the subsections that follow.

```
local:secureHash   Hash the input string.
local:keytool      Export or import a SecretKeyEntry. The Java Keytool does not allow for exporting or importing SecretKeyEntries.
local:encrypt      Encrypt the input string.
local:validate     Validates all json configuration files in the configuration (default: /conf) folder.
basic:help   Displays available commands.
basic:exit   Exit from the console.
remote:configureconnector   Generate connector configuration.
remote:configexport         Exports all configurations.
remote:configimport         Imports the configuration set from local file/directory.
```

The following options are common to the `configexport`, `` configimport` ``, and `configureconnector` subcommands:

* -u or --user USER\[:PASSWORD]

  Allows you to specify the server user and password. Specifying a username is mandatory. If you do not specify a username, the following error is output to the OSGi console: `Remote operation failed: Unauthorized`. If you do not specify a password, you are prompted for one. This option is used by all three subcommands.

* \--url URL

  The URL of the REST service. The default URL is `http://localhost:8080/openidm/`. This can be used to import configuration files from a remote running IDM instance. This option is used by all three subcommands.

* -P or --port PORT

  The port number associated with the REST service. If specified, this option overrides any port number specified with the `--url` option. The default port is `8080`. This option is used by all three subcommands.

## `configexport`

The `configexport` subcommand exports all configuration objects to a specified location, enabling you to reuse a system configuration in another environment. For example, you can test a configuration in a development environment, then export it and import it into a production environment. This subcommand also enables you to inspect the active configuration of an IDM instance.

OpenIDM must be running when you execute this command.

Usage is as follows:

```bash
./cli.sh configexport --user username:password export-location
```

For example:

```bash
./cli.sh configexport --user openidm-admin:openidm-admin /tmp/conf
```

On Windows systems, the export-location must be provided in quotation marks, for example:

```dos
C:\openidm\cli.bat configexport --user openidm-admin:openidm-admin "C:\temp\openidm"
```

Configuration objects are exported as `.json` files to the specified directory. The command creates the directory if needed. Configuration files that are present in this directory are renamed as backup files, with a timestamp; for example, `audit.json.2014-02-19T12-00-28.bkp`, and are not overwritten. The following configuration objects are exported:

* The internal repository table configuration (`repo.ds.json` or `repo.jdbc.json` ) and the datasource connection configuration, for JDBC repositories (`datasource.jdbc-default.json` )

* The script configuration (`script.json` )

* The log configuration (`audit.json` )

* The authentication configuration (`authentication.json` )

* The cluster configuration (`cluster.json` )

* The configuration of the outbound email service (`external.email.json)`

* Custom configuration information (`info-name.json` )

* The managed object configuration (`managed.json` )

* The connector configuration (`provisioner.openicf-*.json` )

* The router service configuration (`router.json` )

* The scheduler service configuration (`scheduler.json` )

* Any configured schedules (`schedule-*.json` )

* Standard security questions (`selfservice.kba.json)`

* The [mapping](../synchronization-guide/mappings.html) configuration

* If workflows are defined, the configuration of the workflow engine (`workflow.json` ) and the workflow access configuration (`process-access.json` )

* Any configuration files related to the user interface (`ui-*.json` )

* The configuration of any custom endpoints (`endpoint-*.json` )

* The configuration of servlet filters (`servletfilter-*.json` )

* The policy configuration (`policy.json` )

## `configimport`

The `configimport` subcommand imports configuration objects from the specified directory, enabling you to reuse a system configuration from another environment. For example, you can test a configuration in a development environment, then export it and import it into a production environment.

The command updates the existing configuration from the import-location over the REST interface. By default, if configuration objects are present in the import-location and not in the existing configuration, these objects are added. If configuration objects are present in the existing location but not in the import-location, these objects are left untouched in the existing configuration.

The subcommand takes the following options:

* `-r`, `--replaceall`, `--replaceAll`

  Replaces the entire list of configuration files with the files in the specified import location.

  |   |                                                                                                                                                                                                                |
  | - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | This option wipes out the existing configuration and replaces it with the configuration in the import-location. Objects in the existing configuration that are not present in the import-location are deleted. |

* `--retries` (integer)

  This option specifies the number of times the command should attempt to update the configuration if the server is not ready.

  Default value : 10

* `--retryDelay` (integer)

  This option specifies the delay (in milliseconds) between configuration update retries if the server is not ready.

  Default value : 500

Usage is as follows:

```bash
./cli.sh configimport --user username:password [--replaceAll] [--retries integer] [--retryDelay integer] import-location
```

For example:

```bash
./cli.sh configimport --user openidm-admin:openidm-admin --retries 5 --retryDelay 250 --replaceAll /tmp/conf
```

On Windows systems, the import-location must be provided in quotation marks, for example:

```dos
C:\openidm\cli.bat configimport --user openidm-admin:openidm-admin --replaceAll "C:\temp\openidm"
```

Configuration objects are imported as `.json` files from the specified directory to the `conf` directory. The configuration objects that are imported are the same as those for the `export` command described in the previous section.

## `configureconnector`

The `configureconnector` subcommand generates a configuration for an ICF connector.

Usage is as follows:

```bash
./cli.sh configureconnector --user username:password --name connector-name
```

Select the type of connector that you want to configure. The following example configures a new CSV connector:

```none
./cli.sh configureconnector --user openidm-admin:openidm-admin --name myCsvConnector
Executing ./cli.sh...
Starting shell in /path/to/openidm
Mar 26, 2020 06:08:52 PM org.forgerock.openidm.core.FilePropertyAccessor loadProps
0. SSH Connector version 1.5.20.31
1. ServiceNow Connector version 1.5.20.31
2. Scripted SQL Connector version 1.5.20.31
3. Scripted REST Connector version 1.5.20.31
4. Scim Connector version 1.5.20.31
5. Salesforce Connector version 1.5.20.31
6. MSGraphAPI Connector version 1.5.20.31
7. MongoDB Connector version 1.5.20.31
8. Marketo Connector version 1.5.20.31
9. LDAP Connector version 1.5.20.31
10. Kerberos Connector version 1.5.20.31
11. Scripted Poolable Groovy Connector version 1.5.20.31
12. Scripted Groovy Connector version 1.5.20.31
13. GoogleApps Connector version 1.5.20.31
14. Database Table Connector version 1.5.20.31
15. CSV File Connector version 1.5.20.31
16. Adobe Marketing Cloud Connector version 1.5.20.31
17. Exit
Select [0..17]:   15
Edit the configuration file and run the command again. The configuration was saved to
  /path/to/openidm/temp/provisioner.openicf-myCsvConnector.json
```

The basic configuration is saved in a file named `/openidm/temp/provisioner.openicf-connector-name.json`. Edit at least the `configurationProperties` parameter in this file to complete the connector configuration. For example, for a CSV connector:

```json
"configurationProperties" : {
    "headerPassword" : "password",
    "csvFile" : "&{idm.instance.dir}/data/csvConnectorData.csv",
    "newlineString" : "\n",
    "headerUid" : "uid",
    "quoteCharacter" : "\"",
    "fieldDelimiter" : ",",
    "syncFileRetentionCount" : 3
}
```

For more information about the connector configuration properties, refer to [Configure connectors](https://docs.pingidentity.com/openicf/connector-reference/configure-connector.html).

When you have modified the file, rerun the `configureconnector` command so that IDM can pick up the new connector configuration:

```
./cli.sh configureconnector --user openidm-admin:openidm-admin --name myCsvConnector
Executing ./cli.sh...
Starting shell in /path/to/openidm
Using boot properties at /path/to/openidm/resolver/boot.properties
Configuration was found and read from: /path/to/openidm/temp/provisioner.openicf-myCsvConnector.json
```

Copy the new `provisioner.openicf-myCsvConnector.json` file to your project's `conf/` subdirectory.

You can also configure connectors over the REST interface or through the admin UI. For more information, refer to [Configure connectors](https://docs.pingidentity.com/openicf/connector-reference/configure-connector.html).

## `` encrypt` ``

The `encrypt` subcommand encrypts an input string, or JSON object, provided at the command line. This subcommand can be used to encrypt passwords or other sensitive data to be stored in the repository. The encrypted value is output to standard output and provides details of the cryptography key used to encrypt the data.

Usage is as follows:

```bash
./cli.sh encrypt [-j] string
```

If you do not enter the string as part of the command, the command prompts for the string to be encrypted. If you enter the string as part of the command, special characters, such as quotation marks, must be escaped.

* -j or --json

  Indicates that the string to be encrypted is a JSON object, and validates the object. If the object is malformed JSON and you use the `-j` option, the command throws an error. It is easier to input JSON objects in interactive mode. If you input the JSON object on the command-line, the object must be surrounded by quotes, and any special characters, including curly braces, must be escaped. The rules for escaping these characters are fairly complex. For more information, refer to the [OSGi specification](https://docs.osgi.org/specification/).

  For example:

  ```bash
  ./cli.sh encrypt \
  --json '\{\"password\":\"myPassw0rd\"\}'
  ```

The following example encrypts a normal string value:

```bash
./cli.sh encrypt \
mypassword
Executing ./cli.sh...
Starting shell in /path/to/openidm
-----BEGIN ENCRYPTED VALUE-----
{
  "$crypto" : {
    "type" : "x-simple-encryption",
    "value" : {
      "cipher" : "AES/CBC/PKCS5Padding",
      "stableId" : "openidm-sym-default",
      "salt" : "vdz6bUztiT6QsExNrZQAEA==",
      "data" : "RgMLRbX0guxF80nwrtaZkkoFFGqSQdNWF7Ve0zS+N1I=",
      "keySize" : 16,
      "purpose" : "idm.config.encryption",
      "iv" : "R9w1TcWfbd9FPmOjfvMhZQ==",
      "mac" : "9pXtSKAt9+dO3Mu0NlrJsQ=="
    }
  }
}
------END ENCRYPTED VALUE------
```

The following example prompts for a JSON object to be encrypted:

```
./cli.sh encrypt --json
Using boot properties at /path/to/openidm/resolver/boot.properties
Enter the Json value

> Press ctrl-D to finish input
Start data input: {"password":"myPassw0rd"}
^D
-----BEGIN ENCRYPTED VALUE-----
{
  "$crypto" : {
    "type" : "x-simple-encryption",
    "value" : {
      "cipher" : "AES/CBC/PKCS5Padding",
      "stableId" : "openidm-sym-default",
      "salt" : "vdz6bUztiT6QsExNrZQAEA==",
      "data" : "RgMLRbX0guxF80nwrtaZkkoFFGqSQdNWF7Ve0zS+N1I=",
      "keySize" : 16,
      "purpose" : "idm.config.encryption",
      "iv" : "R9w1TcWfbd9FPmOjfvMhZQ==",
      "mac" : "9pXtSKAt9+dO3Mu0NlrJsQ=="
    }
  }
}
------END ENCRYPTED VALUE------
```

## `secureHash`

The `secureHash` subcommand hashes an input string or JSON object using the specified hash algorithm configuration. Use this subcommand to hash password values or other sensitive data to be stored in the repository. The hashed value is output to standard output and provides details of the algorithm configuration used to hash the data.

Usage is as follows:

```
/path/to/openidm/cli.sh secureHash --algorithm --config [--json] string
```

* -a or --algorithm

  Specifies the hash algorithm to use.

* -c or --config

  Lets you provide additional hashing configuration options, as a JSON object. For a list of supported hash algorithms and their configuration, refer to [Salted Hash Algorithms](../security-guide/encoding-attribute-values.html#encoding-salted-hash).

* -j or --json

  Indicates that the string to be encrypted is a JSON object, and validates the object. If the object is malformed JSON and you use the `-j` option, the command throws an error. It is easier to input JSON objects in interactive mode. If you input the JSON object on the command-line, the object must be surrounded by quotes, and any special characters, including curly braces, must be escaped. The rules for escaping these characters are fairly complex. For more information, refer to the [OSGi specification](https://docs.osgi.org/specification/).

  For example:

  ```
  /path/to/openidm/cli.sh secureHash \
  --algorithm SHA-384 \
  --json '\{\"password\":\"myPassw0rd\"\}'
  ```

If you do not enter the string as part of the command, the command prompts for the string to be hashed. If you enter the string as part of the command, any special characters, for example quotation marks, must be escaped.

The following example hashes a password value (`mypassword`) using the `PBKDF2` algorithm:

```
/path/to/openidm/cli.sh secureHash \
--algorithm PBKDF2 \
--config '{\"hashLength\":16\,\"saltLength\":16\,\"iterations\":20000\,\"hmac\":\"SHA3-256\"}' \
"mypassword"
Executing ./cli.sh...
Starting shell in /path/to/openidm
...
-----BEGIN HASHED VALUE-----
{
  "$crypto" : {
    "value" : {
      "algorithm" : "PBKDF2",
      "data" : "9/1IIaAVxAMFdCzlMGtkXMmotKqBafIdx2KFUeKHX0k=",
      "config" : {
        "hashLength" : 16,
        "saltLength" : 16,
        "iterations" : 20000,
        "hmac" : "SHA3-256"
      }
    },
    "type" : "salted-hash"
  }
}
------END HASHED VALUE------
```

The following example prompts for a JSON object to be hashed:

```
/path/to/openidm/cli.sh secureHash --algorithm SHA-384 --json
Executing ./cli.sh...
Executing ./cli.sh...
Starting shell in /path/to/openidm
Nov 14, 2017 1:24:26 PM org.forgerock.openidm.core.FilePropertyAccessor loadProps
INFO: Using properties at /path/to/openidm/resolver/boot.properties
Enter the Json value

> Press ctrl-D to finish input
Start data input: {"password":"myPassw0rd"}
^D
-----BEGIN HASHED VALUE-----
{
  "$crypto" : {
    "value" : {
      "algorithm" : "SHA-384",
      "data" : "7Caabx7d+vOZ7d3VMwdQObQJdTQ3uGOItsX5AwR4ViygUfARR/XuxRIBQt1LRq58ZOQXFwuw+3rvzK7Kld8pSg=="
    },
    "type" : "salted-hash"
  }
}
------END HASHED VALUE------
```

## `keytool`

The `keytool` subcommand exports or imports secret key values.

The Java `keytool` command enables you to export and import public keys and certificates but not secret or symmetric keys. The IDM `keytool` subcommand provides this functionality.

Usage is as follows:

```
./cli.sh keytool [--export, --import] alias
```

For example, to export the default IDM symmetric key, run the following command:

```
./cli.sh keytool --export openidm-sym-default
Executing ./cli.sh...
Starting shell in /home/idm/openidm
Use KeyStore from: /openidm/security/keystore.jceks
Please enter the password:
[OK] Secret key entry with algorithm AES
AES:606d80ae316be58e94439f91ad8ce1c0
```

The default keystore password is `changeit`. For security reasons, you *must* change this password in a production environment. For information about changing the keystore password, refer to [The IDM keystore](../security-guide/default-keystore.html).

To import a new secret key named my-new-key, run the following command:

```
./cli.sh keytool --import my-new-key
Using boot properties at /openidm/resolver/boot.properties
Use KeyStore from: /openidm/security/keystore.jceks
Please enter the password:
Enter the key:
AES:606d80ae316be58e94439f91ad8ce1c0
```

If a secret key with that name already exists, IDM returns the following error:

```
"KeyStore contains a key with this alias"
```

## `validate`

The `validate` subcommand validates all .json configuration files in your project's `conf/` directory.

Usage is as follows:

```none
./cli.sh validate
Executing ./cli.sh
Starting shell in /path/to/openidm
Using boot properties at /path/to/openidm/resolver/boot.properties
...................................................................
[Validating] Load JSON configuration files from:
[Validating] 	/path/to/openidm/conf
[Validating] audit.json .................................. SUCCESS
[Validating] authentication.json ......................... SUCCESS
    ...
[Validating] sync.json ................................... SUCCESS
[Validating] ui-configuration.json ....................... SUCCESS
[Validating] ui-countries.json ........................... SUCCESS
[Validating] workflow.json ............................... SUCCESS
```

---

---
title: Configuration changes
description: Understand how PingIDM handles configuration changes, including the repository as authoritative source, file encoding, and persistent configuration
component: pingidm
version: 8.1
page_id: pingidm:setup-guide:changing-configuration
canonical_url: https://docs.pingidentity.com/pingidm/8.1/setup-guide/changing-configuration.html
llms_txt: https://docs.pingidentity.com/pingidm/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Setup", "Configuration", "Objects"]
---

# Configuration changes

When you change configuration objects, take the following points into account:

* IDM's authoritative configuration source is its repository. Although the JSON files provide a view of the configuration objects, they do not represent the authoritative source.

  Unless you have disabled file writes, IDM updates JSON files after you make configuration changes over REST. You can also edit those JSON files directly. For information on disabling file writes, refer to [Disable automatic configuration updates](../security-guide/disabling-auto-config-updates.html).

* While running, IDM recognizes changes to JSON files. The server *must* be running when you delete configuration objects, even if you do so by editing the JSON files.

* The `openidm.config.file.encoding` property sets the encoding to be used when reading from, or writing to configuration files. The default encoding is UTF-8. Acceptable values include:

  * US-ASCII

  * ISO-8859-1

  * UTF-8

  * UTF-16BE

  * UTF-16LE

  * UTF-16

  |   |                                                                                                                                                                                                                                                        |
  | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
  |   | All configuration files are encoded using UTF-8 by default. If you change the encoding to a different character set, you must re-encode the files before you restart IDM with the new encoding. Failure to do so will result in errors on IDM startup. |

* Avoid editing configuration objects directly in the repository. Rather, edit the configuration over the REST API, or in the configuration JSON files to ensure consistent behavior and that operations are logged.

* By default, IDM stores its configuration in the repository. If you remove an IDM instance and do not specifically drop the repository, the configuration remains in effect for a new instance that uses that repository. You can disable this *persistent configuration* in your project's `conf/system.properties` file by setting the following property:

  ```properties
  openidm.config.repo.enabled=false
  ```

  Disabling persistent configuration means that IDM stores its configuration in memory only.

---

---
title: Configure the server over REST
description: Read and modify PingIDM configuration objects over the REST API using GET, PUT, and PATCH requests on the /openidm/config endpoint
component: pingidm
version: 8.1
page_id: pingidm:setup-guide:configuring-over-rest
canonical_url: https://docs.pingidentity.com/pingidm/8.1/setup-guide/configuring-over-rest.html
llms_txt: https://docs.pingidentity.com/pingidm/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Setup", "Configuration", "REST"]
---

# Configure the server over REST

IDM exposes configuration objects under the `/openidm/config` context path.

The optional `waitForCompletion` parameter is available to the `config` endpoint for create, update, and patch requests. Requests to the endpoint with `waitForCompletion=true` delay the response until an OSGi service event confirms the change has been consumed by the corresponding service or the request times out.

The following server properties support additional configuration of the `waitForCompletion` behavior. For more information, refer to [Property value substitution](using-property-substitution.html).

* `openidm.config.waitByDefault`

  Default Value: `false`

  Specifies whether to wait for the OSGi service event if the `waitForCompletion` parameter is missing from the request.

* `openidm.config.waitTimeout`

  Default Value: `5000`

  The amount of time, in milliseconds, to wait for OSGi service events before timing out.

To list the configuration on the local host, perform a GET request on `http://localhost:8080/openidm/config`.

> **Collapse: Example GET Request**
>
> The following REST call includes excerpts of the default configuration for an IDM instance started with the `sync-with-csv` sample:
>
> ```
> curl \
> --request GET \
> --header "X-OpenIDM-Username: openidm-admin" \
> --header "X-OpenIDM-Password: openidm-admin" \
> --header "Accept-API-Version: resource=1.0" \
> http://localhost:8080/openidm/config
> {
>   "_id": "",
>   "configurations": [
>     {
>       "_id": "router",
>       "pid": "router",
>       "factoryPid": null
>     },
>     {
>       "_id": "info/login",
>       "pid": "info.f01fc3ed-5871-408d-a5f0-bef00ccc4c8f",
>       "factoryPid": "info"
>     },
>     {
>       "_id": "provisioner.openicf/csvfile",
>       "pid": "provisioner.openicf.9009f4a1-ea47-4227-94e6-69c345864ba7",
>       "factoryPid": "provisioner.openicf"
>     },
>     {
>       "_id": "endpoint/usernotifications",
>       "pid": "endpoint.e2751afc-d169-4a23-a88e-7211d340bccb",
>       "factoryPid": "endpoint"
>     },
>     ...
>   ]
> }
> ```

Single instance configuration objects are located under `openidm/config/object-name`.

> **Collapse: Example Audit Output**
>
> The following example shows the `audit` configuration of the [sync-with -csv sample](../samples-guide/sync-with-csv.html).
>
> ```
> curl \
> --header "X-OpenIDM-Username: openidm-admin" \
> --header "X-OpenIDM-Password: openidm-admin" \
> --header "Accept-API-Version: resource=1.0" \
> "http://localhost:8080/openidm/config/audit"
> {
>   "_id": "audit",
>   "auditServiceConfig": {
>     "handlerForQueries": "json",
>     "availableAuditEventHandlers": [
>       "org.forgerock.audit.handlers.csv.CsvAuditEventHandler",
>       "org.forgerock.audit.handlers.jms.JmsAuditEventHandler",
>       "org.forgerock.audit.handlers.json.JsonAuditEventHandler",
>       "org.forgerock.audit.handlers.json.stdout.JsonStdoutAuditEventHandler",
>       "org.forgerock.openidm.audit.impl.RepositoryAuditEventHandler",
>       "org.forgerock.openidm.audit.impl.RouterAuditEventHandler",
>       "org.forgerock.audit.handlers.syslog.SyslogAuditEventHandler"
>     ],
>     "filterPolicies": {
>       "field": {
>         "excludeIf": [],
>         "includeIf": []
>       }
>     },
>     "caseInsensitiveFields": [
>       "/access/http/request/headers",
>       "/access/http/response/headers"
>     ]
>   },
>   "eventHandlers": [
>     {
>       "class": "org.forgerock.audit.handlers.json.JsonAuditEventHandler",
>       "config": {
>         "name": "json",
>         "enabled": {
>           "$bool": "&{openidm.audit.handler.json.enabled|true}"
>         },
>         "logDirectory": "&{idm.data.dir}/audit",
>         "buffering": {
>           "maxSize": 100000,
>           "writeInterval": "100 millis"
>         },
>         "topics": [
>           "access",
>           "activity",
>           "sync",
>           "authentication",
>           "config"
>         ]
>       }
>     },
>     {
>       "class": "org.forgerock.audit.handlers.json.stdout.JsonStdoutAuditEventHandler",
>       "config": {
>         "name": "stdout",
>         "enabled": {
>           "$bool": "&{openidm.audit.handler.stdout.enabled|false}"
>         },
>         "topics": [
>           "access",
>           "activity",
>           "sync",
>           "authentication",
>           "config"
>         ]
>       }
>     },
>     {
>       "class": "org.forgerock.openidm.audit.impl.RepositoryAuditEventHandler",
>       "config": {
>         "name": "repo",
>         "enabled": {
>           "$bool": "&{openidm.audit.handler.repo.enabled|false}"
>         },
>         "topics": [
>           "access",
>           "activity",
>           "sync",
>           "authentication",
>           "config"
>         ]
>       }
>     }
>   ],
>   "eventTopics": {
>     "config": {
>       "filter": {
>         "actions": [
>           "create",
>           "update",
>           "delete",
>           "patch",
>           "action"
>         ]
>       }
>     },
>     "activity": {
>       "filter": {
>         "actions": [
>           "create",
>           "update",
>           "delete",
>           "patch",
>           "action"
>         ]
>       },
>       "watchedFields": [],
>       "passwordFields": [
>         "password"
>       ]
>     }
>   },
>   "exceptionFormatter": {
>     "type": "text/javascript",
>     "file": "bin/defaults/script/audit/stacktraceFormatter.js"
>   }
> }
> ```

Multiple instance configuration objects are found under `openidm/config/object-name/instance-name`.

> **Collapse: Example Multiple Instance Configuration**
>
> The following example shows the configuration for the CSV connector from the [sync-with-csv sample](../samples-guide/sync-with-csv.html).
>
> ```
> curl \
> --header "X-OpenIDM-Username: openidm-admin" \
> --header "X-OpenIDM-Password: openidm-admin" \
> --header "Accept-API-Version: resource=1.0" \
> "http://localhost:8080/openidm/config/provisioner.openicf/csvfile"
> {
>   "_id": "provisioner.openicf/csvfile",
>   "connectorRef": {
>     "bundleName": "org.forgerock.openicf.connectors.csvfile-connector",
>     "bundleVersion": "[1.5.19.0,1.6.0.0)",
>     "connectorName": "org.forgerock.openicf.csvfile.CSVFileConnector"
>   },
>   "operationTimeout": {
>     "CREATE": -1,
>     "VALIDATE": -1,
>     "TEST": -1,
>     "SCRIPT_ON_CONNECTOR": -1,
>     "SCHEMA": -1,
>     "DELETE": -1,
>     "UPDATE": -1,
>     "SYNC": -1,
>     "AUTHENTICATE": -1,
>     "GET": -1,
>     "SCRIPT_ON_RESOURCE": -1,
>     "SEARCH": -1
>   },
>   "configurationProperties": {
>     "csvFile": "&{idm.instance.dir}/data/csvConnectorData.csv"
>   },
>   "resultsHandlerConfig": {
>     "enableAttributesToGetSearchResultsHandler": true
>   },
>   "syncFailureHandler": {
>     "maxRetries": 5,
>     "postRetryAction": "logged-ignore"
>   },
>   "objectTypes": {
>     "account": {
>       "$schema": "http://json-schema.org/draft-03/schema",
>       "id": "ACCOUNT",
>       "type": "object",
>       "nativeType": "ACCOUNT",
>       "properties": {
>         "description": {
>           "type": "string",
>           "nativeName": "description",
>           "nativeType": "string"
>         },
>         "firstname": {
>           "type": "string",
>           "nativeName": "firstname",
>           "nativeType": "string"
>         },
>         "email": {
>           "type": "string",
>           "nativeName": "email",
>           "nativeType": "string"
>         },
>         "name": {
>           "type": "string",
>           "required": true,
>           "nativeName": "NAME",
>           "nativeType": "string"
>         },
>         "lastname": {
>           "type": "string",
>           "required": true,
>           "nativeName": "lastname",
>           "nativeType": "string"
>         },
>         "mobileTelephoneNumber": {
>           "type": "string",
>           "required": true,
>           "nativeName": "mobileTelephoneNumber",
>           "nativeType": "string"
>         },
>         "roles": {
>           "type": "string",
>           "required": false,
>           "nativeName": "roles",
>           "nativeType": "string"
>         }
>       }
>     }
>   },
>   "operationOptions": {}
> }
> ```

You can change the configuration over REST by using an HTTP PUT or HTTP PATCH request to modify the required configuration object.

> **Collapse: Example PUT Request**
>
> The following example uses a PUT request to modify the configuration of the scheduler service, increasing the maximum number of threads that are available for the concurrent execution of scheduled tasks:
>
> ```
> curl \
> --header "X-OpenIDM-Username: openidm-admin" \
> --header "X-OpenIDM-Password: openidm-admin" \
> --header "Content-Type: application/json" \
> --header "Accept-API-Version: resource=1.0" \
> --request PUT \
> --data '{
>   "threadPool": {
>     "threadCount": 20
>   },
>   "scheduler": {
>     "executePersistentSchedules": {
>       "$bool": "&{openidm.scheduler.execute.persistent.schedules}"
>     }
>   }
> }' \
> "http://localhost:8080/openidm/config/scheduler"
> {
>   "_id": "scheduler",
>   "threadPool": {
>     "threadCount": 20
>   },
>   "scheduler": {
>     "executePersistentSchedules": {
>       "$bool": "&{openidm.scheduler.execute.persistent.schedules}"
>     }
>   }
> }
> ```

> **Collapse: Example PATCH Request**
>
> The following example uses a PATCH request to reset the number of threads to their original value.
>
> ```
> curl \
> --header "X-OpenIDM-Username: openidm-admin" \
> --header "X-OpenIDM-Password: openidm-admin" \
> --header "Content-Type: application/json" \
> --header "Accept-API-Version: resource=1.0" \
> --request PATCH \
> --data '[
>   {
>     "operation" : "replace",
>     "field" : "/threadPool/threadCount",
>     "value" : 10
>   }
> ]' \
> "http://localhost:8080/openidm/config/scheduler"
> {
>   "_id": "scheduler",
>   "threadPool": {
>     "threadCount": 10
>   },
>   "scheduler": {
>     "executePersistentSchedules": {
>       "$bool": "&{openidm.scheduler.execute.persistent.schedules}"
>     }
>   }
> }
> ```

|   |                                                                                                                                                                                                              |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | Multi-version concurrency control (MVCC) is not supported for configuration objects so you do not need to specify a revision during updates to the configuration, and no revision is returned in the output. |

For more information about using the REST API to update objects, refer to the [REST API Reference](../rest-api-reference/preface.html).

---

---
title: HTTP clients
description: Configure PingIDM HTTP client properties including connection timeouts, proxy settings, SSL algorithm, hostname verification, and connection pooling
component: pingidm
version: 8.1
page_id: pingidm:setup-guide:http-client-config
canonical_url: https://docs.pingidentity.com/pingidm/8.1/setup-guide/http-client-config.html
llms_txt: https://docs.pingidentity.com/pingidm/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Setup", "Configuration", "HTTP", "Clients"]
---

# HTTP clients

Several IDM modules, such as the external REST service and identity provider service, need to make HTTP(S) requests to external systems.

HTTP client settings can be configured through any expression resolver (in `resolver/boot.properties`, environment variables, or Java system properties). Configuration for specific clients can be set in that client's JSON configuration file. For example, `conf/external.rest.json` configures the external REST service and properties set there override the expression resolvers. For more information on property resolution, refer to [Expression Resolvers and Order of Precedence](using-property-substitution.html#expression-evaluation).

You can set the following properties for HTTP clients:

* `openidm.http.client.connectionTimeout`

  The TCP connection timeout for new HTTP connections, in seconds. The default timeout is 10 seconds.

* `openidm.http.client.hostnameVerifier` (string)

  Specifies whether the client should check that the hostname to which it has connected is allowed by the certificate that is presented by the server.

  The property can take the following values:

  * `STRICT`: Hostnames are validated

  * `ALLOW_ALL`: The client doesn't attempt to match the URL hostname to the SSL certificate Common Name, as part of its validation process

    If you don't set this property, the behavior is to validate hostnames (the equivalent of setting `"hostnameVerifier": "STRICT"`). In production environments, you *should* set this property to `STRICT`.

* `openidm.http.client.maxConnections` (integer)

  The maximum number of connections that should be pooled by the HTTP client. At most 64 connections will be pooled by default.

* `openidm.http.client.proxy.password`

  The password of the account for the specified proxy.

  |   |                                                                                                                                                                                                                                                                                                                                                                    |
  | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
  |   | This property is [deprecated](../release-notes/deprecated-functionality.html#deprecation-proxy-properties-purpose). Use the `idm.http.client.proxy.credentials` purpose to store the proxy username and password instead. Learn more about configuring the proxy in [Configuring proxy secret stores](../security-guide/secret-stores.html#proxy-secret-rotation). |

* `openidm.http.client.proxy.uri`

  Specifies that the client should make its HTTP(S) requests through the specified proxy server.

* `openidm.http.client.proxy.useSystem` (true or false)

  If `true`, specifies a system-wide proxy with the JVM system properties, `http.proxyHost`, `http.proxyPort`, and (optionally) `http.nonProxyHosts`.

  If `openidm.http.client.proxy.uri` is set, and not empty, that setting overrides the system proxy setting.

* `openidm.http.client.proxy.userName`

  The username of the account for the specified proxy.

  |   |                                                                                                                                                                                                                                                                                                                                                                    |
  | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
  |   | This property is [deprecated](../release-notes/deprecated-functionality.html#deprecation-proxy-properties-purpose). Use the `idm.http.client.proxy.credentials` purpose to store the proxy username and password instead. Learn more about configuring the proxy in [Configuring proxy secret stores](../security-guide/secret-stores.html#proxy-secret-rotation). |

* `openidm.http.client.reuseConnections` (true or false)

  Specifies whether HTTP connections should be kept alive and reused for additional requests. By default, connections will be reused if possible.

* `openidm.http.client.retryRequests` (true or false)

  Specifies whether requests should be retried if a failure is detected. By default requests will be retried.

* `openidm.http.client.socketTimeout`

  The TCP socket timeout, in seconds, when waiting for HTTP responses. The default timeout is 10 seconds.

* `openidm.http.client.sslAlgorithm`

  The cipher to be used when making SSL/TLS connections, for example, `AES`, `CBC`, or `PKCS5Padding`. Defaults to the system SSL algorithm.

* []()`openidm.http.client.userAgent`

  Overrides the default value for the `User-Agent` header. If not specified, the default `"PingIdentity"` value is used. Request-level headers take precedence over both the IDM configuration and the default value.

---

---
title: HTTP I/O buffer
description: Configure PingIDM HTTP I/O buffer properties for in-memory and file-based temporary storage of large HTTP request payloads
component: pingidm
version: 8.1
page_id: pingidm:setup-guide:temp-storage
canonical_url: https://docs.pingidentity.com/pingidm/8.1/setup-guide/temp-storage.html
llms_txt: https://docs.pingidentity.com/pingidm/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Setup", "Configuration", "HTTP I/O", "Requests"]
---

# HTTP I/O buffer

When HTTP I/O requests exceed the memory limit, caching switches to a temporary file. The following lines from `boot.properties` display the default values related to buffer size:

```properties
# initial size of the in-memory I/O buffer for HTTP requests
#openidm.temporarystorage.initialLength.bytes=8192

# maximum size of the in-memory I/O buffer for HTTP requests
#openidm.temporarystorage.memoryLimit.bytes=65536

# maximum size of the filesystem I/O buffer for HTTP requests, for when memoryLimit is exceeded
#openidm.temporarystorage.fileLimit.bytes=1073741824

# absolute directory path of filesystem I/O buffer for HTTP requests, and uses system property java.io.tmpdir by default
#openidm.temporarystorage.directory=/var/tmp
```

* `openidm.temporarystorage.initialLength.bytes`

  Initial size of the memory buffer in bytes.

  Default: 8192 bytes (8 KB). Maximum: The value of `openidm.temporarystorage.memoryLimit.bytes`.

* `openidm.temporarystorage.memoryLimit.bytes`

  Maximum size of the in-memory I/O buffer for HTTP requests. When the memory buffer is full, the content is transferred to a temporary file.

  Default: 65536 bytes (64 KB). Maximum: 2147483647 bytes (2 GB).

* `openidm.temporarystorage.fileLimit.bytes`

  Maximum size of the temporary storage file. If the downloaded file is larger than this value, IDM throws the exception `HTTP 413 Payload Too Large`.

  Default: 1073741824 bytes (1 GB). Maximum: 2147483647 bytes (2 GB).

* `openidm.temporarystorage.directory`

  The absolute directory path of the filesystem I/O buffer for HTTP requests.

  Default: The value of the system property `java.io.tmpdir`.

---

---
title: Install the end-user UI
description: Install the PingIDM end-user UI behind a standalone Nginx server or as a Docker container for self-service account management
component: pingidm
version: 8.1
page_id: pingidm:setup-guide:idm-enduser-ui
canonical_url: https://docs.pingidentity.com/pingidm/8.1/setup-guide/idm-enduser-ui.html
llms_txt: https://docs.pingidentity.com/pingidm/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Setup", "End-user UI", "Nginx", "Docker"]
section_ids:
  idm-enduser-ui-prereqs: Before you begin
  idm-enduser-ui-download: Download and extract the artifact
  idm-enduser-ui-nginx: Install behind a standalone Nginx server
  idm-enduser-ui-docker: Install with Docker
  idm-enduser-ui-access: Access the IDM end-user UI
  idm-enduser-ui-env-ref: Environment variables reference
---

# Install the end-user UI

|   |                                                                                                                                                                                                                                                                                                                                                                      |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | To use any IDM UI in a production environment, it must only be accessed in an HTTPS context. You can accomplish this using a separate server (such as an SSL-terminating reverse proxy) or directly configuring the web server hosting the UI files to support HTTPS. The specific implementation choice for using HTTPS is outside the scope of this documentation. |

The IDM end-user UI provides role-based access to self-service tasks and allows users to manage certain aspects of their own accounts. It ships as a separate downloadable artifact from the [Backstage download site](https://backstage.forgerock.com/downloads), and is not bundled with the IDM `.zip`.

You can deploy the IDM end-user UI in either of two ways from the same artifact:

* Behind a standalone Nginx server.

* As a Docker container you build from the included `Dockerfile`.

## Before you begin

Before you install the end-user UI, make sure you have the following:

* IDM 8.1 or later, running and reachable from the host that serves the UI.

* For the Nginx path: Nginx 1.18 or later.

* For the Docker path: Docker 20.10 or later.

## Download and extract the artifact

1. Download the IDM end-user UI artifact (`PingIDM-Enduser-UI-8.1.1.zip`) from the [Backstage download site](https://backstage.forgerock.com/downloads).

2. Extract the `.zip` archive to a working directory:

   ```bash
   unzip ~/Downloads/PingIDM-Enduser-UI-8.1.1.zip -d ~/Downloads/tmp
   ```

   The archive contains the following structure:

   ```console
   IDMEnduserUI/
   ├── www/
   │   └── enduser/              # Production build output
   ├── Dockerfile                # Production image (Nginx + Alpine)
   ├── nginx.conf                # Example config for standalone Nginx
   ├── nginx.docker.conf         # Example config for Docker
   ├── entrypoint.sh             # Container entrypoint
   ├── variable_replacement.sh   # envsubst script for static assets
   └── DEPLOYMENT.md
   ```

## Install behind a standalone Nginx server

Use this path when you want to serve the UI directly from Nginx without Docker.

Consult the [Nginx documentation](https://nginx.org/en/docs/) for your operating system, as you might need to adjust the instructions in this overview. Examples include nesting the `server` block inside the `http` block of your main `/etc/nginx/nginx.conf` or placing `nginx.conf` as a standalone file in `/etc/nginx/conf.d/`.

1. Change to the extracted directory:

   ```bash
   cd ~/Downloads/tmp/IDMEnduserUI
   ```

2. Set the environment variables for your deployment. The `variable_replacement.sh` script substitutes these values into the compiled JavaScript bundles. The following defaults assume IDM is reachable through the same Nginx host:

   ```bash
   export IDM_REST_URL=/openidm
   export IDM_ADMIN_URL=
   ```

   For the full list of supported variables and defaults, refer to [Environment variables reference](#idm-enduser-ui-env-ref).

3. Run the variable replacement script against the compiled JavaScript:

   ```bash
   ./variable_replacement.sh www/enduser/js/*.js
   ```

4. [Install Nginx](https://nginx.org/en/docs/install.html) using the package manager for your operating system. For example:

   * Debian/Ubuntu

   * RHEL/CentOS/Fedora

   ```console
   sudo apt update
   sudo apt install nginx
   ```

   ```console
   sudo yum install nginx
   ```

5. Copy the UI assets into the Nginx `html` webroot:

   ```bash
   cp -r www/enduser /usr/share/nginx/html/
   ```

   |   |                                                                                                         |
   | - | ------------------------------------------------------------------------------------------------------- |
   |   | The default Nginx webroot varies by distribution (commonly `/usr/share/nginx/html` or `/var/www/html`). |

6. Edit the `nginx.conf` file from the extracted archive:

   1. Update the `root` directive to point to your Nginx webroot. For example, `/usr/share/nginx/html`.

   2. Update the `proxy_pass` directive to point to your IDM instance. For example, `http://localhost:8080/openidm`.

      Example `nginx.conf` excerpt

      ```nginx
      ...
      server {
          listen       8083;        (1)
          server_name  localhost;

          root /usr/share/nginx/html;
          ...
          location /openidm {
              proxy_pass http://localhost:8080/openidm;
              proxy_set_header Host $host;
              proxy_set_header X-Real-IP $remote_addr;
              proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
              proxy_set_header X-Forwarded-Proto $scheme;
          }
      }
      ```

      |       |                                                                                                             |
      | ----- | ----------------------------------------------------------------------------------------------------------- |
      | **1** | The server listens on port `8083` to avoid conflicts with IDM (port `8080`) and the admin UI (port `8082`). |

7. Copy the modified `nginx.conf` to the Nginx configuration directory:

   ```console
   cp ~/Downloads/tmp/IDMEnduserUI/nginx.conf /etc/nginx/nginx.conf
   ```

   |   |                                                                                                                                                                                                                                                                                                                                     |
   | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | If you're already using Nginx for other site configurations, don't overwrite your existing `nginx.conf`. Read about [managing Nginx configuration files](https://docs.nginx.com/nginx/admin-guide/basic-functionality/managing-configuration-files/) for guidance on integrating additional server blocks into your existing setup. |

8. Test the modified `nginx.conf` configuration for syntax errors:

   ```console
   nginx -t
   nginx: the configuration file /etc/nginx/nginx.conf syntax is ok
   nginx: configuration file /etc/nginx/nginx.conf test is successful
   ```

9. Restart Nginx:

   ```console
   systemctl restart nginx
   ```

## Install with Docker

Use this path when you want to run the UI as a container. The included `Dockerfile` produces a production image based on `nginxinc/nginx-unprivileged`.

You can download Docker from [the official Docker homepage](https://www.docker.com).

1. Change to the extracted directory:

   ```bash
   cd ~/Downloads/tmp/IDMEnduserUI
   ```

2. From the extracted archive, build the image.

   The `Dockerfile` accepts two optional build arguments:

   | Argument            | Default             | Description                                 |
   | ------------------- | ------------------- | ------------------------------------------- |
   | `WEB_ROOT_LOCATION` | `www/enduser`       | Path to the built UI assets                 |
   | `NGINX_CONF`        | `nginx.docker.conf` | Server block config to copy into the image. |

   * Build without arguments

   * Build with arguments

   ```bash
   docker build -t idm-enduser-ui:latest .
   ```

   ```bash
   docker build \
     --build-arg WEB_ROOT_LOCATION=my/assets \
     --build-arg NGINX_CONF=my-nginx.conf \
     -t idm-enduser-ui:latest .
   ```

3. Run the container, passing your environment variables as `-e` flags. For the full list of supported variables and defaults, refer to [Environment variables reference](#idm-enduser-ui-env-ref).

   ```bash
   docker run -d --name idm-enduser -p 8083:8080 \
     -e IDM_REST_URL="/openidm" \
     -e IDM_ADMIN_URL="" \
     idm-enduser-ui:latest
   ```

   The Docker entrypoint runs `variable_replacement.sh` against the compiled bundles before starting Nginx, so the UI picks up your runtime values without rebuilding the image.

4. To use your own Nginx server block instead of the one built into the image, mount it over `default.conf` at runtime:

   ```bash
   docker run -d -p 8083:8080 \
     -v /path/to/my-nginx.conf:/etc/nginx/conf.d/default.conf:ro \
     idm-enduser-ui:latest
   ```

## Access the IDM end-user UI

With IDM running, go to the Nginx host and port you configured. For the defaults shown previously, the UI is available at:

`http://localhost:8083`

## Environment variables reference

The entrypoint passes every variable in the following table through `envsubst` and into the compiled JavaScript bundles. Build the image (or extract the artifact) once, then configure per environment.

| Variable        | Default    | Description                                                                                                                                                                             |
| --------------- | ---------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `IDM_REST_URL`  | `/openidm` | IDM REST API URL                                                                                                                                                                        |
| `IDM_ADMIN_URL` | *(empty)*  | IDM admin console URL. Set to the URL of your admin UI (for example, `http://localhost:8082/platform`). Leave blank if you don't need a link to the admin console from the end-user UI. |

---

---
title: Install the legacy admin UI
description: (Deprecated; use Platform admin UI) Install the PingIDM legacy admin UI and API Explorer behind an Nginx reverse proxy
component: pingidm
version: 8.1
page_id: pingidm:setup-guide:legacy-admin-ui
canonical_url: https://docs.pingidentity.com/pingidm/8.1/setup-guide/legacy-admin-ui.html
llms_txt: https://docs.pingidentity.com/pingidm/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  before_you_begin: Before you begin
  download_and_extract_the_artifact: Download and extract the artifact
  install_and_configure_nginx: Install and configure Nginx
  verify_the_installation: Verify the installation
---

# Install the legacy admin UI

|   |                                                                                                                                             |
| - | ------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The legacy IDM admin UI is deprecated and will be removed in a future release. Use the [Platform admin UI](platform-admin-ui.html) instead. |

|   |                                                                                                                                                                                                                                                                                                                                                                      |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | To use any IDM UI in a production environment, it must only be accessed in an HTTPS context. You can accomplish this using a separate server (such as an SSL-terminating reverse proxy) or directly configuring the web server hosting the UI files to support HTTPS. The specific implementation choice for using HTTPS is outside the scope of this documentation. |

Starting with IDM 8.1, the legacy admin UI and API Explorer are no longer bundled with the IDM `.zip` distribution. They are available as a standalone artifact that you deploy behind an Nginx reverse proxy.

## Before you begin

* IDM is installed and running on `localhost:8080` (adjust for the host and port of your deployment).

* You have administrator privileges to install packages on the host.

## Download and extract the artifact

1. Download the applicable version of the PingIDM Legacy Admin UI `.zip` archive from the [Backstage download site](https://backstage.forgerock.com/downloads).

2. Extract the `.zip` archive:

   ```
   unzip ~/Downloads/PingIDM-Legacy-AdminUI-8.1.1.zip -d /Downloads/tmp/
   ```

   The archive contains the following structure:

   ```none
   PingIDM-Legacy-Admin-UI/
   ├── nginx.conf
   └── www/
       ├── admin/    (1)
       ├── api/      (2)
       └── errors/   (3)
   ```

   |       |                     |
   | ----- | ------------------- |
   | **1** | The legacy admin UI |
   | **2** | The API Explorer    |
   | **3** | Error pages         |

## Install and configure Nginx

Consult the [Nginx documentation](https://nginx.org/en/docs/) for your operating system, as you might need to adjust the instructions in this overview. Examples include nesting the `server` block inside the `http` block of your main `/etc/nginx/nginx.conf` or placing `nginx.conf` as a standalone file in `/etc/nginx/conf.d/`.

1. [Install Nginx](https://nginx.org/en/docs/install.html) using the package manager for your operating system. For example:

   * Debian/Ubuntu

   * RHEL/CentOS/Fedora

   ```console
   sudo apt update
   sudo apt install nginx
   ```

   ```console
   sudo yum install nginx
   ```

2. Copy the contents of the `www/` directory from the PingIDM Legacy Admin UI extracted archive into the Nginx `html` webroot:

   ```console
   cp -r ~/Downloads/tmp/PingIDM-Legacy-Admin-UI/www/* /usr/share/nginx/html/
   ```

   |   |                                                                                                          |
   | - | -------------------------------------------------------------------------------------------------------- |
   |   | The default Nginx web root varies by distribution (commonly `/usr/share/nginx/html` or `/var/www/html`). |

3. If you want to disable the API Explorer, delete the `api/` directory from your Nginx `html` webroot.

4. Edit the `nginx.conf` file from the PingIDM Legacy Admin UI extracted archive:

   1. Update the `root` directive to point to your Nginx web root. For example, `/usr/share/nginx/html`.

   2. Update the `proxy_pass` directive to point to your IDM instance. For example, `http://localhost:8080/openidm`.

   Example `nginx.conf` excerpt

   ```nginx
   ...
   server {
       listen       8082;        (1)
       server_name  localhost;

       root /usr/share/nginx/html;
       ...
       location /openidm {
           proxy_pass http://localhost:8080/openidm;
           proxy_set_header Host $host;
           proxy_set_header X-Real-IP $remote_addr;
           proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
           proxy_set_header X-Forwarded-Proto $scheme;
       }
   }
   ```

   |       |                                                                                                     |
   | ----- | --------------------------------------------------------------------------------------------------- |
   | **1** | The server listens on port `8082` to avoid conflicts with IDM, which typically runs on port `8080`. |

5. Copy the modified `nginx.conf` to the Nginx configuration directory:

   ```console
   cp ~/Downloads/tmp/PingIDM-Legacy-Admin-UI/nginx.conf /etc/nginx/nginx.conf
   ```

   |   |                                                                                                                                                                                                                                                                                                                                      |
   | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
   |   | If you're already using Nginx for other site configurations, do not overwrite your existing `nginx.conf`. Read about [managing Nginx configuration files](https://docs.nginx.com/nginx/admin-guide/basic-functionality/managing-configuration-files/) for guidance on integrating additional server blocks into your existing setup. |

6. Test the modified `nginx.conf` configuration for syntax errors:

   ```console
   nginx -t
   nginx: the configuration file /etc/nginx/nginx.conf syntax is ok
   nginx: configuration file /etc/nginx/nginx.conf test is successful
   ```

7. Restart Nginx:

   ```console
   systemctl restart nginx
   ```

## Verify the installation

|   |                                                                                                                                                                                                                                                                                                                                                                      |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | To use any IDM UI in a production environment, it must only be accessed in an HTTPS context. You can accomplish this using a separate server (such as an SSL-terminating reverse proxy) or directly configuring the web server hosting the UI files to support HTTPS. The specific implementation choice for using HTTPS is outside the scope of this documentation. |

Make sure IDM is running and then go to the UIs:

* **Admin UI**: `http://localhost:8082/admin`

* **API Explorer**: `http://localhost:8082/api`

* **API Explorer (from Admin)**: `http://localhost:8082/admin/#apiExplorer`

---

---
title: Install the Platform admin UI for standalone IDM
description: Install the PingIDM Platform admin UI behind a standalone Nginx server or as a Docker container to replace the legacy admin UI
component: pingidm
version: 8.1
page_id: pingidm:setup-guide:platform-admin-ui
canonical_url: https://docs.pingidentity.com/pingidm/8.1/setup-guide/platform-admin-ui.html
llms_txt: https://docs.pingidentity.com/pingidm/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Setup", "Platform Admin UI", "Nginx", "Docker"]
section_ids:
  platform-admin-ui-prereqs: Before you begin
  platform-admin-ui-download: Download and extract the artifact
  platform-admin-ui-nginx: Install behind a standalone Nginx server
  platform-admin-ui-docker: Install with Docker
  platform-admin-ui-access: Access the Platform admin UI
  platform-admin-ui-env-ref: Environment variables reference
---

# Install the Platform admin UI for standalone IDM

|   |                                                                                                                                                                                                                                                                                                                                                                      |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | To use any IDM UI in a production environment, it must only be accessed in an HTTPS context. You can accomplish this using a separate server (such as an SSL-terminating reverse proxy) or directly configuring the web server hosting the UI files to support HTTPS. The specific implementation choice for using HTTPS is outside the scope of this documentation. |

The Platform admin UI is the replacement for the [deprecated legacy admin UI](legacy-admin-ui.html). Starting with IDM 8.1, it ships as a separate downloadable artifact from the [Backstage download site](https://backstage.forgerock.com/downloads), and is not bundled with the IDM `.zip`.

You can deploy the Platform admin UI in either of two ways from the same artifact:

* Behind a standalone Nginx server.

* As a Docker container you build from the included `Dockerfile`.

|   |                                                                                                                                                                                                       |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The Platform admin UI and the legacy admin UI are independent artifacts. You can install one or both on different Nginx servers or different ports. New deployments should use the Platform admin UI. |

## Before you begin

* IDM 8.1 or later, running and reachable from the host that serves the UI.

* For the Nginx path: Nginx 1.18 or later.

* For the Docker path: Docker 20.10 or later.

## Download and extract the artifact

1. Download the Platform admin UI artifact (`PingIDM-Admin-UI-8.1.1.zip`) from the [Backstage download site](https://backstage.forgerock.com/downloads).

2. Extract the `.zip` archive to a working directory:

   ```bash
   unzip ~/Downloads/PingIDM-Admin-UI-8.1.1.zip -d ~/Downloads/tmp
   ```

   The archive contains the following structure:

   ```console
   IDMAdminUI/
   ├── www/
   │   └── platform/             # Production build output
   ├── Dockerfile                # Production image (Nginx + Alpine)
   ├── nginx.conf                # Example config for standalone Nginx
   ├── nginx.docker.conf         # Example config for Docker
   ├── entrypoint.sh             # Container entrypoint
   ├── variable_replacement.sh   # envsubst script for static assets
   └── DEPLOYMENT.md
   ```

## Install behind a standalone Nginx server

Use this path when you want to serve the UI directly from Nginx without Docker.

Consult the [Nginx documentation](https://nginx.org/en/docs/) for your operating system, as you might need to adjust the instructions in this overview. Examples include nesting the `server` block inside the `http` block of your main `/etc/nginx/nginx.conf` or placing `nginx.conf` as a standalone file in `/etc/nginx/conf.d/`.

1. Change to the extracted directory:

   ```bash
   cd ~/Downloads/tmp/IDMAdminUI
   ```

2. Set the environment variables for your deployment. The `variable_replacement.sh` script substitutes these values into the compiled JavaScript bundles. The following defaults assume IDM is reachable through the same Nginx host:

   ```bash
   export IDM_REST_URL=/openidm
   export IDM_UPLOAD_URL=/upload
   export IDM_EXPORT_URL=/export
   export MENUS_FILE=menus.idm
   export ROUTES_FILE=routes.idm
   export DEPLOYMENT_TYPE=IDM
   export ENABLE_WORKFORCE=false
   export AM_URL=
   export AM_ADMIN_URL=
   ```

   For the full list of supported variables and defaults, refer to [Environment variables reference](#platform-admin-ui-env-ref).

3. Run the variable replacement script against the compiled JavaScript:

   ```bash
   ./variable_replacement.sh www/platform/js/*.js
   ```

4. [Install Nginx](https://nginx.org/en/docs/install.html) using the package manager for your operating system. For example:

   * Debian/Ubuntu

   * RHEL/CentOS/Fedora

   ```console
   sudo apt update
   sudo apt install nginx
   ```

   ```console
   sudo yum install nginx
   ```

5. Copy the UI assets into the Nginx `html` webroot:

   ```bash
   cp -r www/platform /usr/share/nginx/html/
   ```

   |   |                                                                                                         |
   | - | ------------------------------------------------------------------------------------------------------- |
   |   | The default Nginx webroot varies by distribution (commonly `/usr/share/nginx/html` or `/var/www/html`). |

6. Edit the `nginx.conf` file from the extracted archive:

   1. Update the `root` directive to point to your Nginx webroot. For example, `/usr/share/nginx/html`.

   2. Update the `proxy_pass` directive to point to your IDM instance. For example, `http://localhost:8080/openidm`.

   Example `nginx.conf` excerpt

   ```nginx
   ...
   server {
       listen       8082;        (1)
       server_name  localhost;

       root /usr/share/nginx/html;
       ...
       location /openidm {
           proxy_pass http://localhost:8080/openidm;
           proxy_set_header Host $host;
           proxy_set_header X-Real-IP $remote_addr;
           proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
           proxy_set_header X-Forwarded-Proto $scheme;
       }
   }
   ```

   |       |                                                                                                     |
   | ----- | --------------------------------------------------------------------------------------------------- |
   | **1** | The server listens on port `8082` to avoid conflicts with IDM, which typically runs on port `8080`. |

7. Copy the modified `nginx.conf` to the Nginx configuration directory:

   ```console
   cp ~/Downloads/tmp/IDMAdminUI/nginx.conf /etc/nginx/nginx.conf
   ```

   |   |                                                                                                                                                                                                                                                                                                                                     |
   | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | If you're already using Nginx for other site configurations, don't overwrite your existing `nginx.conf`. Read about [managing Nginx configuration files](https://docs.nginx.com/nginx/admin-guide/basic-functionality/managing-configuration-files/) for guidance on integrating additional server blocks into your existing setup. |

8. Test the modified `nginx.conf` configuration for syntax errors:

   ```console
   nginx -t
   nginx: the configuration file /etc/nginx/nginx.conf syntax is ok
   nginx: configuration file /etc/nginx/nginx.conf test is successful
   ```

9. Restart Nginx:

   ```console
   systemctl restart nginx
   ```

## Install with Docker

Use this path when you want to run the UI as a container. The included `Dockerfile` produces a production image based on `nginxinc/nginx-unprivileged`.

You can download Docker from [the official Docker homepage](https://www.docker.com).

1. Change to the extracted directory:

   ```bash
   cd ~/Downloads/tmp/IDMAdminUI
   ```

2. From the extracted archive, build the image.

   The `Dockerfile` accepts two optional build arguments:

   | Argument            | Default             | Description                                 |
   | ------------------- | ------------------- | ------------------------------------------- |
   | `WEB_ROOT_LOCATION` | `www/platform`      | Path to the built UI assets                 |
   | `NGINX_CONF`        | `nginx.docker.conf` | Server block config to copy into the image. |

   * Build without arguments

   * Build with arguments

   ```bash
   docker build -t platform-admin-ui:latest .
   ```

   ```bash
   docker build \
     --build-arg WEB_ROOT_LOCATION=my/assets \
     --build-arg NGINX_CONF=my-nginx.conf \
     -t platform-admin-ui:latest .
   ```

3. Run the container, passing your environment variables as `-e` flags. For the full list of supported variables and defaults, refer to [Environment variables reference](#platform-admin-ui-env-ref).

   ```bash
   docker run -d --name idm-admin -p 8082:8080 \
     -e IDM_REST_URL="/openidm" \
     -e IDM_UPLOAD_URL="/upload" \
     -e IDM_EXPORT_URL="/export" \
     -e MENUS_FILE="menus.idm" \
     -e ROUTES_FILE="routes.idm" \
     -e DEPLOYMENT_TYPE="IDM" \
     -e ENABLE_WORKFORCE="false" \
     -e AM_URL="" \
     -e AM_ADMIN_URL="" \
     platform-admin-ui:latest
   ```

   The Docker entrypoint runs `variable_replacement.sh` against the compiled bundles before starting Nginx, so the UI picks up your runtime values without rebuilding the image.

4. To use your own Nginx server block instead of the one built into the image, mount it over `default.conf` at runtime:

   ```bash
   docker run -d -p 8082:8080 \
     -v /path/to/my-nginx.conf:/etc/nginx/conf.d/default.conf:ro \
     platform-admin-ui:latest
   ```

## Access the Platform admin UI

With IDM running, go to the Nginx host and port you configured. For the defaults shown previously, the UI is available at:

`http://localhost:8082/platform`

## Environment variables reference

The entrypoint passes every variable in the following table through `envsubst` and into the compiled JavaScript bundles. Build the image (or extract the artifact) once, then configure per environment.

| Variable           | Default      | Description                                             |
| ------------------ | ------------ | ------------------------------------------------------- |
| `IDM_REST_URL`     | `/openidm`   | IDM REST API URL                                        |
| `IDM_UPLOAD_URL`   | `/upload`    | IDM upload URL                                          |
| `IDM_EXPORT_URL`   | `/export`    | IDM export URL                                          |
| `MENUS_FILE`       | `menus.idm`  | IDM menus file                                          |
| `ROUTES_FILE`      | `routes.idm` | IDM routes file                                         |
| `DEPLOYMENT_TYPE`  | `IDM`        | Deployment type. Leave set to `IDM` for standalone IDM. |
| `ENABLE_WORKFORCE` | `false`      | Workforce features. Leave `false` for standalone IDM.   |
| `AM_URL`           | *(empty)*    | PingAM URL. Leave blank for standalone IDM.             |
| `AM_ADMIN_URL`     | *(empty)*    | PingAM admin URL. Leave blank for standalone IDM.       |

---

---
title: Manage dashboards
description: (Deprecated) Create and manage PingIDM legacy admin UI dashboards, add widgets, and configure settings in ui-dashboard.json
component: pingidm
version: 8.1
page_id: pingidm:setup-guide:managing-dashboards
canonical_url: https://docs.pingidentity.com/pingidm/8.1/setup-guide/managing-dashboards.html
llms_txt: https://docs.pingidentity.com/pingidm/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Setup", "Configuration", "Dashboards"]
section_ids:
  default_dashboards: Default dashboards
  quick_start_dashboard: Quick start dashboard
  system_monitoring_dashboard: System monitoring dashboard
  resource_report: Resource report
  business_report: Business report
  custom_dashboards: Custom dashboards
  to-create-a-dashboard: Create a new dashboard
  to-add-widgets: Add and move widgets
  default-widgets: Admin UI widgets
  widget-reporting: admin UI reporting widgets
  widget-system: System status widgets
  widget-utilities: Utility widgets
---

# Manage dashboards

|   |                                                                                                                                                                                          |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Widgets are deprecated and will be removed in a future release of IDM. For more information, refer to [Deprecation](../release-notes/deprecated-functionality.html#deprecation-widgets). |

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Starting with IDM 8.1, the [legacy admin UI is deprecated](../release-notes/deprecated-functionality.html#legacy-admin-ui-deprecated) and is no longer bundled with IDM. New deployments should use the [Platform admin UI](platform-admin-ui.html), which is the replacement for the legacy admin UI.Both UIs are available as separate downloads from the [Backstage download site](https://backstage.forgerock.com/downloads):- To install the Platform admin UI, follow the steps in [Install the Platform admin UI for standalone IDM](platform-admin-ui.html).

- To continue using the legacy admin UI, follow the steps in [Install the legacy admin UI](legacy-admin-ui.html). |

Dashboards let you make shortcuts to frequently-required tasks. The Quick Start dashboard displays by default when you log in to the admin UI. You can create additional dashboards, or add and remove widgets from the existing dashboards.

## Default dashboards

To display all configured dashboards, select Dashboards > Manage Dashboards. The following dashboards are provided by default.

### Quick start dashboard

Quick Start cards support one-click access to common administrative tasks:

[icon: database, set=fad, size=3x]

#### [Add Connector](link:https://docs.pingidentity.com/openicf/connector-reference/configure-connector.html)

Configure connections to external resources.

[icon: map-marker-alt, set=fad, size=3x]

#### [Create Mapping](../synchronization-guide/mappings.html)

Configure mappings to synchronize objects between resources.

[icon: check-square, set=fad, size=3x]

#### [Manage Roles](../objects-guide/managed-roles.html)

Set up provisioning or authorization roles.

[icon: tablet-alt, set=fad, size=3x]

#### [Add Device](../objects-guide/creating-modifying-managed-objects.html)

Configure managed objects, including users, groups, roles, and devices.

[icon: user, set=fad, size=3x]

#### [Manage Users](../objects-guide/users.html)

Manage users in the repository.

[icon: user, set=fad, size=3x]

#### [Configure System Preferences](../workflow-guide/preface.html)

Configure server settings for Audit, Workflow, and more.

### System monitoring dashboard

The System Monitoring Dashboard includes information about:

Audit Events

Includes information on [audit](../audit-guide/audit.html) data, organized by date.

![Audit Event Widget](_images/auditEventWidget.png)

Cluster Node Status

Includes information on cluster nodes.

![Cluster Node Status Widget](_images/clusterNodeWidget.png)

System Health

Includes information on system resource usage.

![System Health Widget](_images/systemHealthWidget.png)

Last Reconciliation

Includes data from the most recent data reconciliation.

![Last Recon Widget](_images/lastReconWidget.png)

### Resource report

Show Me

![Resource Report Dashboard](_images/resourceReportDashboard.png)

* The Resource Report includes widgets that show the number of active users, configured roles, and active connectors.

* The Resources widget shows all configured connectors, mappings, and managed object types.

### Business report

Show Me

![Business Report Dashboard](_images/businessReportDash.png)

The Business Report includes widgets related to login and registration activity.

## Custom dashboards

You can set up additional dashboards for customized views of the admin UI.

### Create a new dashboard

To create a new dashboard, select Dashboards > New Dashboard. Enter a dashboard name and select whether this dashboard should be the default board that is displayed when you load the admin UI.

For a customized view of the admin UI, select Widgets as the Dashboard Type, click Create Dashboard, and add the widgets that you want exposed in that view.

You can also customize the view by starting with an existing dashboard. In the upper-right corner of the UI, next to the Add Widget button, click the overflow menu [icon: ellipsis-v, set=fas]> widget, and select Rename or Duplicate.

## Add and move widgets

To add a widget to a dashboard, click Add Widget and select the widget type. Widgets are grouped in categories. Scroll down to the category of the widget you want to add.

To change the position of a widget on a dashboard, click and drag the move button [icon: arrows-alt, set=fas].

To add a new Quick Start widget, select the overflow menu [icon: ellipsis-v, set=fas]> widget in the upper right corner of the widget, and click Settings.

To embed an admin UI sub-widget in the Quick Start widget, specify the destination URL. If you are linking to a specific page in the admin UI, the destination URL can be the part of admin UI address. For example, to create a quick start link to the Audit Configuration tab, at `{secureHostname}/admin/#settings/audit/`, enter `#settings/audit` in the destination URL text box.

Any changes to the dashboards are persisted in your project's `conf/ui-dashboard.json` file, which has the following properties:

**admin UI Widget Properties in ui-dashboard.json**

| Property    | Values                                                        | Description                                                                                                                                                                         |
| ----------- | ------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `name`      | String                                                        | Dashboard name.                                                                                                                                                                     |
| `isDefault` | `true` or `false`                                             | Default dashboard. You can only set one default.                                                                                                                                    |
| `widgets`   | Different attributes based on `type`                          | Attributes that define the widget.                                                                                                                                                  |
| `type`      | `lastRecon`, `resourceList`, `quickStart`, `userRelationship` | Widget type.                                                                                                                                                                        |
| `size`      | `x-small`, `small`, `medium`, or `large`                      | Width of widget, based on a 12-column grid system, where x-small=4, small=6, medium=8, and large=12. For more information, refer to [Bootstrap CSS](https://getbootstrap.com/css/). |
| `barchart`  | `true` or `false`                                             | Reconciliation bar chart; applies only to the Last Reconciliation widget.                                                                                                           |

## Admin UI widgets

The following tables list the available widgets:

### admin UI reporting widgets

| Name                        | Description                                                                                                                                                 |
| --------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Audit Events                | Graphical display of [audit events](../audit-guide/audit-admin-ui.html).                                                                                    |
| Count Widget                | A *count* widget that provides an instant count of specific objects; for example, active managed users.                                                     |
| Dropwizard Table With Graph | Does not appear in the list of widgets unless [metrics](../monitoring-guide/monitoring.html) are active.                                                    |
| Graph Widget                | Provides a graphical view of a specific managed resource; for example, managed users, based on some metric.                                                 |
| Last Reconciliation         | Shows statistics from the most recent [reconciliation](../synchronization-guide/manage-recon.html#recon-details), shown on the System Monitoring dashboard. |
| Resources                   | Connectors, mappings, managed objects; shown in Administration dashboard.                                                                                   |
| Sign-Ins                    | The number of managed users that have signed in to the service that week.                                                                                   |

### System status widgets

| Name                       | Description                                                                                                          |
| -------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| Memory Usage (JVM Heap)    | Displays the JVM memory usage. Refer to [API metrics](../monitoring-guide/api-metrics.html).                         |
| Memory Usage (JVM NonHeap) | Displays the JVM non-heap memory usage. Refer to [API metrics](../monitoring-guide/api-metrics.html).                |
| System Health              | Includes information on system resource usage.                                                                       |
| CPU Usage                  | Displays the system CPU usage.                                                                                       |
| System Health              | Includes information on system resource usage.                                                                       |
| Cluster Node Status        | Lists the instances in a [cluster](../install-guide/manage-cluster-nodes.html#managing-nodes-ui), with their status. |

### Utility widgets

| Name                                 | Description                                                                                                                                                                                              |
| ------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Quick Start                          | Links to common tasks; shown in the Administration dashboard.                                                                                                                                            |
| Identity Relationships               | Graphical display of [relationships](../objects-guide/view-relationships-ui.html#viewing-relationships-ui) between identities.                                                                           |
| Managed Objects Relationship Diagram | Graphical diagram with connections between managed object properties; also refer to [View the Relationship Configuration in the UI](../objects-guide/ui-relationships.html#relationship-objects-widget). |

---

---
title: Property value substitution
description: Use PingIDM property value substitution with configuration expressions to inject environment-specific values from environment variables, system properties, or expression files
component: pingidm
version: 8.1
page_id: pingidm:setup-guide:using-property-substitution
canonical_url: https://docs.pingidentity.com/pingidm/8.1/setup-guide/using-property-substitution.html
llms_txt: https://docs.pingidentity.com/pingidm/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["ESV", "Properties"]
section_ids:
  expression-evaluation: Expression resolvers
  environment_variables: Environment variables
  java_system_properties: Java system properties
  expression_files: Expression files
  framework_configuration_properties: Framework configuration properties
  configuration_files: Configuration files
  order-of-precedence: Evaluation order of precedence
  value-coercion: Transforming data types
  substitution-repository: Configuration property value storage
  substitution-limitations: Limitations of property value substitution
  substitution-limitations-ui: Admin UI limitations
  substitution-limitations-connectors: Connector configuration limitations
---

# Property value substitution

Property value substitution lets you achieve the following:

* Define a configuration that is specific to a single instance. For example, setting the location of the keystore on a particular host.

* Define a configuration whose parameters vary between different environments. For example, the URLs for test, development, and production environments.

* Disable certain capabilities on specific nodes. For example, you might want to disable the workflow engine on specific instances.

Property value substitution uses *configuration expressions* to introduce variables into the server configuration. You set configuration expressions as the values of configuration properties. The effective property values can be evaluated in a number of ways. For more information about property evaluation, refer to [Expression Resolvers](#expression-evaluation).

Configuration expressions have the following characteristics:

* To distinguish them from static values, configuration expressions are preceded by an ampersand and enclosed in braces. For example: `&{openidm.port.http}`. The configuration token in the example is `openidm.port.http`. The `.` serves as the separator character.

* You can use a default value in a configuration expression by including it after a vertical bar following the token.

  For example, the following expression sets the default HTTP port value to 8080: `&{openidm.port.http|8080}`.

  With this configuration, the server attempts to substitute `openidm.port.http` with a defined configuration token. If no token definition is found, the server uses the default value, `8080`.

* A configuration property can include a mix of static values and expressions.

  For example, suppose `hostname` is set to `ds`. Then, `&{hostname}.example.com` evaluates to `ds.example.com`.

* Configuration token evaluation is recursive.

  For example, suppose `port` is set to `&{port.prefix}389`, and `port.prefix` is set to `2`. Then `&{port}` evaluates to `2389`.

You can define *nested* properties (that is a property definition within another property definition) and you can combine system properties, boot properties, and environment variables.

|   |                                                                                                                                                               |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Property substitution is *not* available for any configuration not processed by the IDM backend, such as `ui-themeconfig` or any user-supplied configuration. |

## Expression resolvers

At server startup, expression resolvers evaluate property values to determine the effective configuration. You must define expression values before you start the IDM server that uses them.

When configuration tokens are resolved, the result is always a string. However, you can *coerce* the output type of the evaluated token to match the type that is required by the property. Ultimately, the expression must return the appropriate data type for the configuration property. For example, the `port` property takes an integer. If you set it using an expression, the result of the evaluated expression must be an integer. If the type is wrong, the server fails to start due to a syntax error. For more information about data type coercion, refer to [Transforming Data Types](#value-coercion).

Expression resolvers can obtain values from the following sources:

### Environment variables

You set an environment variable to hold the property value.

For example: `export OPENIDM_PORT_HTTP=8080`.

The environment variable name must be composed of uppercase characters and underscores. The name maps to the expression token as follows:

* Uppercase characters are converted to lowercase.

* Underscores (`_`) are replaced with `.` characters.

In other words, the value of `OPENIDM_PORT_HTTP` replaces `&{openidm.port.http}` in the server configuration.

### Java system properties

You set a Java system property to hold the value.

Java system property names must match expression tokens exactly. In other words, the value of the `openidm.repo.port` system property replaces `&{openidm.repo.port}` in the server configuration.

Java system properties can be set in a number of ways. One way of setting system properties for IDM servers is to pass them through the `OPENIDM_OPTS` environment variable.

For example: `export OPENIDM_OPTS="-Dopenidm.repo.port=3306"`

System properties can also be declared in your project's `conf/system.properties`.

This example uses property value substitution with a standard system property. The example modifies the audit configuration, changing the `audit.json` file to redirect JSON audit logs to the user's home directory. The `user.home` property is a default Java System property:

```json
"eventHandlers" : [
    {
        "class" : "org.forgerock.audit.handlers.json.JsonAuditEventHandler",
        "config" : {
            "name" : "json",
            "logDirectory" : "&{user.home}/audit",
            ...
        }
    },
    ...
]
```

### Expression files

You set a key in a `.json` or `.properties` file to hold the value. To use an expression file, set the `IDM_ENVCONFIG_DIRS` environment variable, or the `idm.envconfig.dirs` Java system property as described below. By default, IDM sets `idm.envconfig.dirs` to `&{idm.install.dir}/resolver/`.

The default property resolver file in IDM is `resolver/boot.properties` but you can specify additional files that might hold property values.

Keys in `.properties` files must match expression tokens exactly. In other words, the value of the `openidm.repo.port` key replaces `&{openidm.repo.port}` in the server configuration.

The following example expression properties file sets the repository port:

```properties
openidm.repo.port=1389
```

JSON expression files can contain nested objects.

JSON field names map to expression tokens as follows:

* The JSON path name matches the expression token.

* The `.` character serves as the JSON path separator character.

The following example JSON expression file uses property value substitution to set the host in the LDAP connector configuration:

```json
{
    "openidm" : {
        "provisioner" : {
            "ldap" : {
                "host" : "ds.example.com"
            }
        }
    }
   }
 }
```

To substitute this value in the configuration, the LDAP provisioner file would include the following:

```json
{
    ...
    "configurationProperties" : {
        "host" : &{openidm.provisioner.ldap.host|localhost},
        ...
    }
}
```

If the server does not find a configuration token for the host name, it substitutes the default (`localhost`).

To use expression files, set the environment variable, `IDM_ENVCONFIG_DIRS`, or the Java system property, `idm.envconfig.dirs`, to a comma-separated list of the directories containing the expression files.

When reading these files, the server browses the directories in the order specified. It reads all the files with `.json` and `.properties` extensions, and attempts to use them to evaluate expression tokens.

For example, if you define `idm.envconfig.dirs=/directory1,/directory2` and a configuration token is defined in both `directory1` and `directory2`, the resolved value will be the value defined in `directory1`. If the configuration token is defined only in `directory2`, the resolved value will be the value defined in `directory2`.

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Using expression files are subject to the following constraints:- Although IDM scans the directories in a specified order, within a directory IDM scans the files in a nondeterministic order.

- IDM does not scan subdirectories.

- Do *not* define the same configuration token more than once in a file.

  If you define the same property twice in the same file, one definition will be used and the other will be ignored. The server will not throw an error, but because files are scanned in a nondeterministic order, you have no way of knowing which value will be used.

- You cannot define the same configuration token in more than one file in a single directory. The server generates an error in this case.

  This constraint implies that you cannot have backup .properties and .json files, in a single directory if they define the same tokens.

- If the same token occurs once in several files that are located in different directories, IDM uses the first value that is read. |

### Framework configuration properties

You can use the `conf/config.properties` file to override values used by the OSGI framework.

### Configuration files

All the properties declared in the `.json` files in your project's `conf/` directory.

## Evaluation order of precedence

The following list displays the order of precedence, from greatest to least:

1. Environment variables override system properties, default token settings, and settings in expression files.

2. System properties override default token settings, and any settings in expression files.

3. Default token settings.

4. If `IDM_ENVCONFIG_DIRS` or `idm.envconfig.dirs` is set, the server uses the settings found in expression files.

5. Framework configuration properties.

6. Hardcoded property values.

7. Properties passed to the startup script [with options such as: -P, -w, and -s.](../install-guide/startup-configuration.html)

## Transforming data types

When configuration tokens are resolved, the result is always a string. However, you can transform or *coerce* the output type of the evaluated token to match the type that is required by the property.

You transform a property's data type by setting `$type` before the property value.

The following coercion types are supported:

* array (`$array`)

* boolean (`$bool`)

* decodeBase64 (`$base64:decode`)

  Transforms a base64-encoded string into a decoded string.

* encodeBase64 (`$base64:encode`)

  Transforms a string into a base64-encoded string.

* integer (`$int`)

* list (`$list`)

* number (`$number`)

  This type can coerce integers, doubles, longs, and floats.

* object (`$object`)

  This type can coerce a JSON object such as an encrypted password.

> **Collapse: Type Coercion to Integer**
>
> This example JSON expression file sets the value of the port in the LDAP connector configuration:
>
> ```json
> {
>     "openidm" : {
>         "provisioner" : {
>             "ldap" : {
>                 "port" : 6389
>             }
>         }
>     }
> }
> ```
>
> When the expression is evaluated, the port is evaluated as a `string` value, (which would cause an error). To coerce the port value to an integer, substitute the value in the LDAP provisioner file as follows:
>
> ```json
> {
>     ...
>     "configurationProperties" : {
>         "port" : {
>             "$int" : "&{openidm.provisioner.ldap.port|1389}",
>         },
>         ...
>     }
> }
> ```
>
> With this configuration, the server evaluates the LDAP port property to the integer `6389`. If the server does not find a configuration token for the port, it substitutes the default (`1389`).

> **Collapse: Type Coercion to Array**
>
> This example JSON expression file sets a value for the failover servers in an LDAP connector configuration:
>
> ```json
> "openidm" : {
>     "provisioner" : {
>         "ldap" : {
>             "failover" : ["ldap://host1.domain.com:1389", "ldap://host2.domain.com:1389"]
>         }
>     }
> }
> ```
>
> When the expression is evaluated, the URLs would be evaluated as a single `string`. To coerce the value to an array, substitute the value in the LDAP provisioner file as follows:
>
> ```json
> {
>     ...
>     "configurationProperties" : {
>         "failover" : {
>             "$array":"&{openidm.provisioner.ldap.failover}"
>         },
>         ...
>     }
> }
> ```
>
> |   |                                                                                                                                                                                                                                                                                                                           |
> | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
> |   | If you set the failover URLs in a `.properties` file, instead of in a `.json` file, you *must* escape the JSON object. This example sets the failover servers array in the `boot.properties` file:```properties
> openidm.provisioner.ldap.failover=[\"ldap://host1.domain.com:1389\",\"ldap://host2.domain.com:1389\"]
> ``` |

> **Collapse: Type Coercion From List to Array**
>
> The `$list` function is similar to `$array`, but lets you specify values in a `.properties` file as a list of strings, separated by a comma (`,`).
>
> For example, you could list the LDAP failover servers in `boot.properties` as follows:
>
> ```properties
> openidm.provisioner.ldap.failover=ldap://host1.domain.com:1389,ldap://host2.domain.com:1389
> ```
>
> To coerce the value to an array, your property definition in the LDAP provisioner file would be:
>
> ```json
> {
>     ...
>     "configurationProperties" : {
>         "failover" : {
>             "$list":"&{openidm.provisioner.ldap.failover}",
>         },
>         ...
>     }
> }
> ```
>
> This configuration would be converted to:
>
> ```json
> "openidm" : {
>     "provisioner" : {
>         "ldap" : {
>             "failover" : ["ldap://host1.domain.com:1389", "ldap://host2.domain.com:1389"]
>         }
>     }
> }
> ```

## Configuration property value storage

The values of configuration properties that are set explicitly (in `conf/*.json` files) are stored in the repository. You can manage these configuration objects over REST or by using the JSON files themselves.

Properties that use value substitution are stored in the repository as *variables*. You store the *value* of each variable in `.properties` files. You can use different `.properties` files to change the configuration for multiple nodes in a cluster.

The following table shows how specific configuration properties can be set:

**Configuration Property Variables**

| Variable             | Description                                                   | Environment Variables | System Variables | boot.properties |
| -------------------- | ------------------------------------------------------------- | --------------------- | ---------------- | --------------- |
| `idm.install.dir`    | Directory of files from unpacked IDM binary                   | YES                   | YES              | YES             |
| `idm.data.dir`       | Working location directory                                    | YES                   | YES              | YES             |
| `idm.instance.dir`   | Project directory with IDM configuration files                | YES                   | YES              | YES             |
| `idm.envconfig.dirs` | Directory with environment files, including `boot.properties` | YES                   | YES              |                 |

You can access configuration properties in scripts using `identityServer.getProperty()`. For more information, refer to [The identityServer Variable](../scripting-guide/script-variables-identity-server.html).

## Limitations of property value substitution

Property value substitution is limited in the following areas:

### Admin UI limitations

|   |                                                                                                                                                                                                                    |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | Fields configured to use property substitution are read-only and appear greyed out in the Admin UI. To make changes, you must use the API or edit the file directly.![greyed out field](_images/subs-field-UI.png) |

Support for property value substitution in the admin UI is limited to the following categories:

* String substitution, where `&{some.property|DefaultValue}`

* Number and integer substitution, including:

  * `"$number" : "&{openidm.port|1234}"`

  * `"$int" : "&{openidm.port|5678}"`

* Base64 substitution, such as: `"$base64:decode" : "&{some.property|YWRtaW4=}"`

* Cryptographic substitution, where for passwords and client secrets, IDM substitutes `"********"` for `$crypto`

### Connector configuration limitations

You cannot use property substitution for connector reference (`connectorRef`) properties. For example, the following configuration is *not* valid:

```json
"connectorRef" : {
    "connectorName" : "&{connectorName}",
    "bundleName" : "org.forgerock.openicf.connectors.ldap-connector",
    "bundleVersion" : "&{LDAP.BundleVersion}"
    ...
}
```

The `connectorName` must be the precise string from the connector configuration. To specify multiple connector version numbers, use a range of versions. For example:

```json
"connectorRef" : {
    "connectorName" : "org.identityconnectors.ldap.LdapConnector",
    "bundleName" : "org.forgerock.openicf.connectors.ldap-connector",
    "bundleVersion" : "[1.5.0.0,2.0.0.0)",
    ...
}
```

---

---
title: Reset user passwords
description: Reset user passwords in PingIDM using the admin UI or configure an external password reset URL using ui-configuration.json
component: pingidm
version: 8.1
page_id: pingidm:setup-guide:ui-password-reset
canonical_url: https://docs.pingidentity.com/pingidm/8.1/setup-guide/ui-password-reset.html
llms_txt: https://docs.pingidentity.com/pingidm/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Setup", "Configuration", "Password Reset"]
section_ids:
  ui-internal-password-change: Change user passwords using the admin UI
  ui-external-password-reset: Use an external password reset system
---

# Reset user passwords

When working with end users, administrators frequently have to reset their passwords. You can do so directly using the admin UI.

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Starting with IDM 8.1, the [legacy admin UI is deprecated](../release-notes/deprecated-functionality.html#legacy-admin-ui-deprecated) and is no longer bundled with IDM. New deployments should use the [Platform admin UI](platform-admin-ui.html), which is the replacement for the legacy admin UI.Both UIs are available as separate downloads from the [Backstage download site](https://backstage.forgerock.com/downloads):- To install the Platform admin UI, follow the steps in [Install the Platform admin UI for standalone IDM](platform-admin-ui.html).

- To continue using the legacy admin UI, follow the steps in [Install the legacy admin UI](legacy-admin-ui.html). |

## Change user passwords using the admin UI

1. From the navigation bar, click Manage > User, and click a user.

2. Click the Password tab, and change the password.

## Use an external password reset system

By default, the Password Reset mechanism is handled within IDM. You can reroute Password Reset in the event that a user has forgotten their password, by specifying an external URL to which Password Reset requests are sent. Note that this URL applies to the Password Reset link on the login page only, not to the security data change facility that is available after a user has logged in.

To set an external URL to handle Password Reset, set the `passwordResetLink` parameter in `conf/ui-configuration.json`. The following example sets the `passwordResetLink` to `https://accounts.example.com/account/reset-password`:

```json
passwordResetLink: "https://accounts.example.com/reset-password"
```

The `passwordResetLink` parameter takes either an empty string as a value (which indicates that no external link is used) or a full URL to the external system that handles Password Reset requests.

|   |                                                                                                                                                                                                                                                                                                 |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | External Password Reset and security questions for internal Password Reset are mutually exclusive. Therefore, if you set a value for the `passwordResetLink` parameter, users will not be prompted with any security questions, regardless of the setting of the `securityQuestions` parameter. |

---

---
title: Server configuration
description: "Understand PingIDM server configuration: single- and multiple-instance objects, JSON file naming, and how configuration is loaded and stored"
component: pingidm
version: 8.1
page_id: pingidm:setup-guide:chap-configuration
canonical_url: https://docs.pingidentity.com/pingidm/8.1/setup-guide/chap-configuration.html
llms_txt: https://docs.pingidentity.com/pingidm/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Setup", "Configuration", "Server", "Objects"]
section_ids:
  configuration-objects: Configuration objects
  single-instance-configuration-objects: Single instance configuration objects
  multiple-instance-configuration-objects: Multiple instance configuration objects
---

# Server configuration

This chapter describes how IDM loads and stores its configuration, and how to modify it.

The configuration is a combination of `.properties` files, container configuration files, and dynamic configuration objects. Most of the configuration files are stored in your project's `conf/` directory.

## Configuration objects

IDM exposes internal configuration objects in JSON format. Configuration elements can be either single instance or multiple instance for an IDM installation.

### Single instance configuration objects

Single instance configuration objects correspond to services that have at most one instance per installation. JSON file views of these configuration objects are named `object-name.json`.

|   |                                                                                                                                                                                                                                       |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | If you create custom configuration files, do not use spaces or special characters in the filenames, in accordance with the [OSGi specification](https://docs.osgi.org/specification/osgi.core/8.0.0/framework.service.html#i3043166). |

The following list describes the single instance configuration objects:

|                  |                                                                                                            |
| ---------------- | ---------------------------------------------------------------------------------------------------------- |
| `audit`          | Specifies how to log audit events.                                                                         |
| `authentication` | Controls REST access.                                                                                      |
| `cluster`        | Defines a clustered IDM instance.                                                                          |
| `endpoint`       | Controls custom REST endpoints.                                                                            |
| `managed`        | Defines managed objects and their schemas.                                                                 |
| `policy`         | Defines the policy validation service.                                                                     |
| `process-access` | Defines access to configured workflows.                                                                    |
| `repo.repo-type` | Defines the IDM repository; for example, `repo.ds` or `repo.jdbc`.                                         |
| `router`         | Specifies filters to apply for specific operations.                                                        |
| `script`         | Defines the parameters that are used when compiling, debugging, and running JavaScript and Groovy scripts. |
| `sync`           | Defines the mappings that IDM uses when it synchronizes and reconciles managed objects.                    |
| `ui`             | Defines the configurable aspects of the default user interfaces.                                           |
| `workflow`       | Defines the configuration of the workflow engine.                                                          |

### Multiple instance configuration objects

Multiple instance configuration objects correspond to services that can have many instances per installation. Multiple instance configuration objects are named `objectname/instancename`; for example, `provisioner.openicf/csvfile`. *JSON file* views of these configuration objects are named `objectname-instancename.json`, for example, `provisioner.openicf-csvfile.json.`

IDM provides the following multiple instance configuration objects:

* Multiple `schedule` configurations can run reconciliations and other tasks on different schedules.

* Multiple `provisioner.openicf` configurations correspond to connected resources.

* Multiple `servletfilter` configurations can be used for different servlet filters, such as the Cross Origin and GZip filters.

  You can order servlet filters by specifying the `order` property in the servlet filter configuration. The default order is `0`, which is assigned to all servlet filters and results in a non-deterministic loading order.

  An `order` property of `0` has the highest priority.

  You can add the `order` property to any of the three IDM servlet filters. The following sample configuration shows how you can add an `order` property of `1` to `servletfilter-payload.json`, which prioritizes this filter after `servletfilter-cors` and `servletfilter-upload` with an `order` property of `0`:

  ```json
  {
      "classPathURLs" : [ ],
      "systemProperties" : { },
      "requestAttributes" : { },
      "scriptExtensions" : { },
      "initParams" : {
          "maxRequestSizeInMegabytes" : 5
      },
      "urlPatterns" : [
          "&{openidm.servlet.alias}/*"
      ],
      "filterClass" : "org.forgerock.openidm.jetty.LargePayloadServletFilter",
      "order" : 1
  }
  ```

---

---
title: Setup
description: Understanding the PingIDM core architecture and getting an initial IDM deployment up and running
component: pingidm
version: 8.1
page_id: pingidm:setup-guide:preface
canonical_url: https://docs.pingidentity.com/pingidm/8.1/setup-guide/preface.html
llms_txt: https://docs.pingidentity.com/pingidm/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Setup", "Configuration"]
page_aliases: ["index.adoc"]
---

# Setup

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Starting with IDM 8.1, the [legacy admin UI is deprecated](../release-notes/deprecated-functionality.html#legacy-admin-ui-deprecated) and is no longer bundled with IDM. New deployments should use the [Platform admin UI](platform-admin-ui.html), which is the replacement for the legacy admin UI.Both UIs are available as separate downloads from the [Backstage download site](https://backstage.forgerock.com/downloads):- To install the Platform admin UI, follow the steps in [Install the Platform admin UI for standalone IDM](platform-admin-ui.html).

- To continue using the legacy admin UI, follow the steps in [Install the legacy admin UI](legacy-admin-ui.html). |

In this guide, you will learn about the core PingIDM (IDM) IDM architecture, the IDM configuration model, and how to get a basic IDM deployment up and running after installation.

[icon: cubes, set=fad, size=3x]

#### [Architecture](chap-overview.html)

IDM architecture, component modules, and services.

[icon: cogs, set=fad, size=3x]

#### [Configuration](chap-configuration.html)

IDM configuration.

[icon: terminal, set=fad, size=3x]

#### [Command-Line Interface](chap-cli.html)

IDM command-line interface (CLI) and utilities.

[icon: mouse-pointer, set=fad, size=3x]

#### [User Interface](chap-ui.html)

IDM's user interfaces.

---

---
title: User interfaces
description: "Overview of PingIDM user interfaces: the Platform admin UI, the legacy admin UI, and the end-user UI, with access and installation pointers"
component: pingidm
version: 8.1
page_id: pingidm:setup-guide:chap-ui
canonical_url: https://docs.pingidentity.com/pingidm/8.1/setup-guide/chap-ui.html
llms_txt: https://docs.pingidentity.com/pingidm/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Setup", "Configuration", "User Interface"]
section_ids:
  platform-admin-ui-overview: Platform admin UI
  legacy-admin-ui-overview: Legacy admin UI
  idm-enduser-ui-overview: End-user UI
---

# User interfaces

|   |                                                                                                                                                                                                                                                                                                                                                                      |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | To use any IDM UI in a production environment, it must only be accessed in an HTTPS context. You can accomplish this using a separate server (such as an SSL-terminating reverse proxy) or directly configuring the web server hosting the UI files to support HTTPS. The specific implementation choice for using HTTPS is outside the scope of this documentation. |

You can use the browser-based admin UIs for configuring and managing users and roles, setting up synchronization between resources, configuring connectors, and more.

|   |                                                                                                                                                                                                       |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The Platform admin UI and the legacy admin UI are independent artifacts. You can install one or both on different Nginx servers or different ports. New deployments should use the Platform admin UI. |

## Platform admin UI

The Platform admin UI replaces the legacy admin UI for administering standalone IDM. Starting with IDM 8.1, you download it as a separate artifact from the [Backstage download site](https://backstage.forgerock.com/downloads) and serve it from either:

* A standalone Nginx server.

* A Docker container built from the included `Dockerfile`.

For installation steps, refer to [Install the Platform admin UI for standalone IDM](platform-admin-ui.html).

After installation, you can access the Platform admin UI at the Nginx host and port (for example, `http://localhost:8082/platform`).

## Legacy admin UI

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Starting with IDM 8.1, the [legacy admin UI is deprecated](../release-notes/deprecated-functionality.html#legacy-admin-ui-deprecated) and is no longer bundled with IDM. New deployments should use the [Platform admin UI](platform-admin-ui.html), which is the replacement for the legacy admin UI.Both UIs are available as separate downloads from the [Backstage download site](https://backstage.forgerock.com/downloads):- To install the Platform admin UI, follow the steps in [Install the Platform admin UI for standalone IDM](platform-admin-ui.html).

- To continue using the legacy admin UI, follow the steps in [Install the legacy admin UI](legacy-admin-ui.html). |

The legacy admin UI is the administration UI that shipped in earlier releases and is available as a separate download for customers who still depend on it. New deployments should use the Platform admin UI.

For installation steps, refer to [Install the legacy admin UI](legacy-admin-ui.html).

After installation, you can access the legacy admin UI at the Nginx host and port (for example, `http://localhost:8082/admin`).

## End-user UI

The IDM end-user UI provides role-based access to specific tasks and allows users to manage certain aspects of their own accounts. You can download it as a separate artifact from the [Backstage download site](https://backstage.forgerock.com/downloads) and serve it from either:

* A standalone Nginx server

* A Docker container built from the included `Dockerfile`

Learn more in [Install the end-user UI](idm-enduser-ui.html).

After installation, you can access the IDM end-user UI at the Nginx host and port (for example, `http://localhost:8083`).

|   |                                                                                                                                                                                                                                                                                                                                                                                                          |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Browser ad blocker extensions can inadvertently block some UI functionality, particularly if your configuration includes strings such as `ad`. For example, a connection to an Active Directory server might be configured at the endpoint `system/ad`. To avoid problems related to blocked UI functionality, remove the extension, or configure a safelist to ensure access to the targeted endpoints. |