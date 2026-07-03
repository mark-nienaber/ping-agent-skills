---
title: Amster
description: Install and integrate Amster with PingAM, including connecting to instances and importing and exporting configuration data
component: pingam
version: 8.1
page_id: pingam:amster:preface
canonical_url: https://docs.pingidentity.com/pingam/8.1/amster/preface.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
page_aliases: ["index.adoc", "user-guide:preface.adoc"]
---

# Amster

This guide shows you how to install Amster, and how to integrate with PingAM. Read the [release notes](https://docs.pingidentity.com/pingam/release-notes/preface.html) before you get started.

[icon: cogs, set=fad, size=3x]

#### [Install Amster](install-amster.html)

Install and start using Amster.

[icon: exchange-alt, set=fad, size=3x]

#### [Connect to AM](connect-am.html)

Connect Amster to an AM instance.

[icon: upload, set=fad, size=3x]

#### [Export AM configuration](export-config.html)

Export AM configuration data using Amster.

[icon: download, set=fad, size=3x]

#### [Import AM configuration](import-config.html)

Import partial and full AM configuration data using Amster

---

---
title: Amster usage examples
description: Learn common tasks with Amster, including cloning PingAM instances and using sample scripts for configuration management
component: pingam
version: 8.1
page_id: pingam:amster:usage-examples
canonical_url: https://docs.pingidentity.com/pingam/8.1/amster/usage-examples.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
page_aliases: ["user-guide:amster-usage-examples.adoc"]
section_ids:
  clone-example: Clone an PingAM instance
  amster-samples: Amster sample scripts
---

# Amster usage examples

In this section, you can find examples of tasks you can do with Amster.

|   |                                                                                                                                           |
| - | ----------------------------------------------------------------------------------------------------------------------------------------- |
|   | Find Amster examples in Docker and Kubernetes deployments in the [ForgeOps](https://docs.pingidentity.com/forgeops/2025.1) documentation. |

## Clone an PingAM instance

This example shows the high-level steps required to clone an AM instance, from exporting the configuration of the original instance, to installing the new instance and importing the configuration into it.

Follow these steps to clone an AM instance using Amster:

1. Create a transport key in the original AM instance, if one does not exist already. Learn more in [Create transport keys to export configuration data](transport-keys.html).

2. Keep the transport key safe by exporting it to another keystore. The key is required to import the configuration into the new AM instance. Learn more in [Duplicate and install a transport key](transport-keys.html#duplicate-key).

3. Connect to the original AM instance using the `amster` command. Learn more in [Connect to AM](connect-am.html).

4. Export all the configuration of the original AM instance using the `export-config` command. Learn more in [Export configuration data](export-config.html).

5. Take note of the value of the Password Encryption Key field on the original AM, for example, `O6QWwHPO4os+zEz3Nqn/2daAYWyiFE32`.

   To locate it, log in to the original AM instance, and navigate to Deployment > Servers > *server name* > Security > Encryption.

6. In the new server, deploy the AM `.war` file in a web container, but don't configure it.

7. Install the new AM instance using the `install-openam` command, specifying the original AM password encryption key with the `--pwdEncKey` option. For example:

   ```
   am> install-openam \
    --serverUrl \https://am.example.com:8443/am \
    --adminPwd password \
    --pwdEncKey O6QWwHPO4os+zEz3Nqn/2daAYWyiFE32 \
    --acceptLicense
   ```

   Learn more in [Passive install using Amster](../installation/passive-install-amster.html).

8. Import the transport key of the original AM instance into the keystore of the new AM instance. Learn more in [Duplicate and install a transport key](transport-keys.html#duplicate-key).

9. Connect to the new AM instance using the `amster` command. Learn more in [Connect to AM](connect-am.html).

10. Import the configuration of the original AM instance using the `import-config` command. Learn more in [Import configuration data](import-config.html).

## Amster sample scripts

This section covers sample scripts and files found in the `/path/to/amster/samples` directory:

* `transport-key.sh`

  Shell script to manage transport keys. You can use it as a template for your own scripts to create, delete, and export the key to another keystore.

  Invoke the script's help for a list of possible actions:

  ```
  $ ./transport-key.sh help
  ```

  Find more information about the transport key in [Create transport keys to export configuration data](transport-keys.html).

* `realm.amster`

  Amster script containing an example of different operations that can be done at realm level, such as creating a data store, displaying its configuration, modifying it, and deleting it.

  Find more information about writing scripts for Amster in [Scripts](scripts.html).

* `import-example.amster`

  Amster script containing an example of the `import-config` command.

  Find more information about writing scripts for Amster in [Scripts](scripts.html).

* `export-example.amster`

  Amster script containing an example of the `export-config` command.

---

---
title: Configuration expressions in exported configuration files
description: Use configuration expressions in Amster-exported files to substitute values from environment variables, shell variables, and expression files when importing configuration into PingAM instances
component: pingam
version: 8.1
page_id: pingam:amster:config-expressions
canonical_url: https://docs.pingidentity.com/pingam/8.1/amster/config-expressions.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
page_aliases: ["user-guide:amster-usage-expressions.adoc"]
section_ids:
  working-with-expressions: Expressions
  expression-order: Expression evaluation and order of precedence
  environment_variables: Environment variables
  java_system_properties: Java system properties
  amster_shell_variables: Amster shell variables
  expression_files: Expression files
  expression_evaluation: Expression evaluation
  transforming-expressions: Transforming data types
  example-expressions: Expression example files
---

# Configuration expressions in exported configuration files

Amster supports the use of configuration expressions as the values of configuration properties in the exported configuration files. Amster substitutes the expressions with values obtained from the Amster shell, expression files, environment variables, and others, when importing the configuration files into an AM instance. Property value substitution enables you to achieve the following:

* Define a configuration that is specific to a single instance.

  For example, setting the location of the keystore on a particular host.

* Define a configuration whose parameters vary between different environments.

  For example, the URLs and passwords for test, development, and production environments.

* Disable certain capabilities on specific AM instances.

  For example, you might want to disable a particular instance from sending notifications to agents.

Property value substitution uses expressions to introduce variables into the server configuration. You set expressions as the values of configuration properties. The effective property values can be evaluated in a number of ways.

## Expressions

Expressions share their syntax and underlying implementation with other Ping Advanced Identity Software components. Expressions have the following characteristics:

* To distinguish them from static values, configuration expressions are preceded by an ampersand (`&` ) and enclosed in braces (`{}` ). Use the dot (`.` ) character as a separator character for the *expression token*. For example, `&{smtp.port}`.

* You can use a default value in a configuration expression by including it after a vertical bar (`|` ) character following the token.

  For example, the following SMTP port expression sets the default value of the SMTP port to 1349: `&{smtp.port|1349}`.

* A configuration property can include a mix of static values and expressions.

  For example, suppose `hostname` is set to `am`. Then `&{hostname}.example.com` evaluates to `am.example.com`.

  You can also use expressions in conjunction with Unix environment variables once these are made available to the Amster shell. Learn more in [Scripts](scripts.html).

* You can define *nested* properties (that is, a property definition within another property definition).

  For example, suppose `listen.port` is set to `&{port.prefix}636`, and `port.prefix` is set to `2`. Then `&{listen.port}` evaluates to `2636`.

* To use an expression in the key of a key:value pair, use the special `AMSTER` marker, rather than the dollar sign (`$`).

  For example, to update the fully-qualified domain name mappings, you could use syntax such as the following:

  `"com.sun.identity.server.fqdnMap[AMSTER{realm.dns.alias}]" : "${realm.dns.alias}"`

Amster defines the following expressions by default:

* `&{amster.import.dir}`

  This expression is resolved in the following ways:

  * As the directory containing the configuration files being imported into AM when using the `import-config --path directory` command.

  * As the parent directory of the configuration file being imported into AM when using the `import-config --path file` command.

* `&{amster.import.url}`

  This expression is resolved in the same way as `&{amster.import.dir}`, but in URL format. For example, `file://path/to/directory`.

## Expression evaluation and order of precedence

You must define expression values before importing the configuration into AM. When evaluated, an expression must return the appropriate type for the configuration property. For example, the `smtp.port` property takes an integer. If you set the property using an expression, the result of the evaluated expression must be an integer.

If the type is wrong, AM may fail to start after a configuration import, with unexpected errors. Find more information about data type coercion in [Transforming data types](#transforming-expressions).

Amster can obtain expressions from the following sources.

### Environment variables

You set an environment variable in your operating system shell. For example, `export SMTP_PORT=1342`.

The environment variable name must be composed of uppercase characters and underscores. The name maps to the expression token as follows:

* Uppercase characters are converted into lower case characters.

* Underscores (`_` ) are replaced with dot (`.` ) characters.

In other words, the value of `SMTP_PORT` replaces `&{smtp.port}` in the AM configuration files.

### Java system properties

You set a Java system property to hold the value when you call the `amster` command with parameters. For example:

```none
"-Dsmtp.port=3306"
```

### Amster shell variables

You set Amster shell variables to hold values.

To define expressions as Amster shell variables, remove the dot (`.`) character, and use the standard camel case notation for naming variables in Groovy.

For example, the `&{smtp.port}` expression would be defined as:

```
am> smtpPort = "1342"
===> 1342
```

In the configuration file, however, you still define the expression as `&{smtp.port}.`

|   |                                                                                                                                                                                                           |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Find more information about how to convert Java system properties and environment variables into Amster shell variables in [Variables in Amster scripts](integrate-amster.html#amster-variables-scripts). |

### Expression files

You set a key in a `.json` or `.properties` file to hold the value.

Keys in `.properties` files must match expression tokens exactly. In other words, the value of the `smtp.port` key replaces `&{smtp.port}` in the server configuration.

The following is an example properties expression file:

```javascript
smtp.port=1342
smtp.user=Greg
stateless.tokens.enabled=true
```

JSON expression files can contain nested objects.

JSON field names map to expression tokens as follows:

* The JSON path name matches the expression token.

* The `.` character serves as the JSON path separator character.

The following is an example of a JSON expression file:

```json
{
   "smtp" : {
      "port" : 1342,
      "user" : "Greg"
   },
   "stateless" : {
      "tokens" : {
         "enabled" : "true"
      }
   },
   "blacklist" : {
      "java" : {
         "classes" : [
            "java.lang.Class",
            "java.security.AccessController",
            "java.lang.reflect.*"
         ]
      }
   }
}
```

You can set multiple configuration files to store your properties. For example, you could have a file to store authentication tree values and another file to store policy-related values.

Note the following constraints when using expression files:

* Amster scans the files in the provided directory in a non-deterministic order.

* Amster reads all files with `.json` and `.properties` extensions.

* Amster does not have a predictable order of precedence for handling multiple configuration tokens with the same name. You are responsible for ensuring name uniqueness of configuration tokens across multiple expression files.

To provide expression files to Amster, use the `envconfig` command followed by the full path to a directory or a file. For example:

```
am> envconfig /path/to/expressionfiles/
```

### Expression evaluation

Expressions are evaluated and replaced with the expected values when importing a configuration into an AM instance. Attempting to import AM JSON configuration files containing expressions that are not defined causes an error message similar to the following:

```
amster am.example.com:8443> import-config \
 --path /tmp/myExportedConfigFiles/realms/root/EmailService.json
Importing file /tmp/myExportedConfigFiles/realms/root/EmailService.json
---------------------------------------------------------------------
IMPORT ERRORS
---------------------------------------------------------------------
Failed to import /tmp/myExportedConfigFiles/realms/root/EmailService.json  :
Can't substitute source vale: unresolved variables ([email.service.port]) or cycles detected ([])
```

The following list reflects the order of precedence:

* Environment variables override default expressions, Amster variables, Java system properties and settings in expression files.

* Amster variables override Java system properties, tokens found in expression files, and default expressions.

* Java system properties override tokens found in expression files and the default expression tokens.

## Transforming data types

By default, when configuration tokens are resolved, the result is always a string. However, when evaluated, an expression must return the appropriate type for the configuration property. For example, the `smtp.port` property takes an integer. If you set the property using an expression, the result of the evaluated expression must be an integer. If the type is wrong, AM may fail to start after a configuration import, with unexpected errors.

You can transform the output type of the evaluated token to match the type that is required by the property. Amster can coerce expressions to resolve as the following types:

* `$int`. Coerce to an integer.

* `$number`. Coerce to integers, doubles, longs, and floats.

* `$bool`. Coerce to a boolean. For example, `true`.

* `$array`. Coerce to a JSON array. For example, `["a","b","c"]`.

* `$list`. Coerce to a JSON list. For example, `1,2,3`.

* `$object`. Coerce to a JSON object. For example, `{"a","b"}`.

* `$base64-encode` and `$base64-decode`. Encode or decode the string to or from Base64.

To convert the value of a property into a different type in the exported configuration file, specify the new type as follows:

```json
"port" : {
    "$int" : "&{smtp.port}"
}
```

You can also replace configuration values with the contents of a file by using the `$inline` coercion function. You can specify the path to the file, or replace it with an expression. For example:

```json
{
 "message" : {
    "$inline" : "&{config.path}/emailcontent.txt"
 },
 "message2" : {
    "$inline" : "/path/to/emailcontent.txt"
 }
}
```

Consider the following points when using the `$inline` coercion function:

* When the file contains a script, such as an authentication script, you must transform its value to Base-64. For example:

  ```json
  "script": {
    "$base64:encode": {
      "$inline": "/path/to/scripted-decision.groovy"
    }
  }
  ```

* When the file contains a value of a type that is different from the configuration value type, you must transform its value. For example:

  ```json
  "port": {
    "$int": {
        "$inline": "myfile.txt"
    }
  }
  ```

|   |                                                                                                                                                                                                                                                                                                             |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Recognizing the type of a particular configuration property in the JSON files may not always be straightforward. When in doubt, try the following approaches:* Check the property in the AM console.

* Configure the property in the AM console, then export the configuration with Amster for an example. |

## Expression example files

This section contains an example expression file, and some excerpts of exported configuration files with expressions inserted in them.

Expression file

```json
 {
   "env" : {
      "name" : "DEV"
   },
   "oath" : {
      "authmodule" : {
         "issuer" : "dev-oathissuer.example.com",
         "authlevel" : 2,
         "checksum" : "true"
      },
      "devprof" : {
         "kstore" : {
            "path" : "&{product.install.dir}/&{env.name}/keystore.jceks",
            "type" : "JCEKS",
            "encpas" : "AAAAA0FFUwIQ1WDDMsxGoZMiRHhDQ+ywUfTMdGtYqEsvZZLV9W8ygfHi/5kBWjMpyg=="
         }
      }
   }
}
```

As well as configuration details, such as hostnames and ports, passwords and secrets are likely to differ between AM instances.

The previous example demonstrates an expression file tailored for the development environment. Note how the `&{devprof.kstore.encpas}` expression holds the value of the encrypted keystore password for the OATH device profile keystore configuration.

For security reasons, Amster only exports passwords in configuration files if the [transport key](#amster-transport-keys) exists in AM's keystore.

If your environments have different passwords, you could manage passwords using expressions as follows:

1. Configure AM with the desired password values for each of your environments.

2. Export the configurations *using the same transport key*.

Using this technique ensures that the passwords for all the environments are properly encrypted. You can safely create expression files by environment with the appropriate values.

Configuration file excerpts

```json
{
   "data":{
      "_id":"",
      "defaults":{
         "oathIssuerName":"&{oath.authmodule.issuer}",
         "totpTimeStepsInWindow":2,
         "authenticationLevel":{
            "$int":"&{oath.authmodule.authlevel}"
         }
      },
      "passwordLength":"6",
      "addChecksumToOtpEnabled":{
         "$bool":"&{oath.authmodule.checksum}"
      }
   },
   "data":{
      "_id":"",
      "defaults":{
         "oathAttrName":"oathDeviceProfiles",
         "authenticatorOATHDeviceSettingsEncryptionKeystorePrivateKeyPassword":null,
         "authenticatorOATHDeviceSettingsEncryptionScheme":"NONE",
         "authenticatorOATHDeviceSettingsEncryptionKeystore":"&{oath.devprof.kstore.path}",
         "authenticatorOATHDeviceSettingsEncryptionKeystoreType":"&{oath.devprof.kstore.type}",
         "authenticatorOATHDeviceSettingsEncryptionKeystorePassword":null,
         "authenticatorPushDeviceSettingsEncryptionKeystorePassword-encrypted":"&{oath.devprof.kstore.encpas}",
         "authenticatorOATHDeviceSettingsEncryptionKeystoreKeyPairAlias":null,
         "authenticatorOATHSkippableName":"oath2faEnabled"
      }
   },
   "data":{
      "_id":"01e1a3c0-038b-4c16-956a-6c9d89328cff",
      "name":"Authentication Tree Decision Node Script &{env.name}",
      "description":"&{product.install.dir}/&{env.name}/authdecisionnode_desc.txt",
      "script":{
         "$base64:encode":{
            "$inline":"&{product.install.dir}/&{env.name}/scripted-decision.groovy"
         }
      }
   }
}
```

Note how the files used by the `$inline` coercion function are stored under a directory that is referenced by the `&{env.name}` expression. For example:

```none
"$inline":"&{product.install.dir}/&{env.name}/scripted-decision.groovy"
```

This is just an example of how you can separate your configuration files by environment.

---

---
title: Connect to AM
description: Connect Amster to AM using interactive login or RSA/ECDSA key files over HTTP or HTTPS, with support for self-signed certificates and remote connections
component: pingam
version: 8.1
page_id: pingam:amster:connect-am
canonical_url: https://docs.pingidentity.com/pingam/8.1/amster/connect-am.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
page_aliases: ["user-guide:amster-connecting.adoc"]
section_ids:
  interactive-login: Interactive login connections
  proc-interactive-login: Connect with interactive login
  private-login: Private key connections
  private-login-local: Connect locally with default private key files
  sec-getting-started-connect-keys: Connect to a remote AM instance
  create-RSA-keys: Create and configure a private key pair
---

# Connect to AM

Amster can connect to an AM instance using interactive login or using RSA or ECDSA key files, either over HTTP or HTTPS protocols. If you use self-signed certificates for AM, you must either:

* Import the certificates into the JVM `cacerts` keystore on the Amster client.

* Run the `amster` command, specifying the truststore containing the certificates and its type. For example:

  ```
  $ ./amster \
   -D javax.net.ssl.trustStore=/path/to/keystore.jceks \
   -D javax.net.ssl.trustStoreType=jceks
  ```

## Interactive login connections

To establish an interactive connection with AM, Amster uses the default authentication tree for administrator users, configured in the AM instance. The authentication tree is specified in the Administrator Authentication Configuration property under Realms > Top Level Realm > Authentication > Settings > Core.

The `ldapService` authentication tree, configured by default after AM installation, requires a valid user in AM. Log in as an administrative user, for example `amadmin`, to perform operations such as export and import of the configuration.

### Connect with interactive login

This procedure assumes the use of the `ldapService` tree. Perform the following steps to connect to a local or remote AM instance using interactive login:

1. Start the Amster command-line interface.

2. Run the `connect` command with the `--interactive` or the `-i` options:

   ```
   am> connect --interactive https://am.example.com:8443/am
   ```

   |   |                                                                                                                                                                                                                                                                                                                                 |
   | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | When using the `amster` command to import or export a significant amount of data, the default timeout of 10 seconds may be insufficient.To increase the default timeout, add the `--connection-timeout seconds` option. For example:```
   am> connect --connection-timeout 45 \
    --interactive https://am.example.com:8443/am
   ``` |

3. Specify the username and password to authenticate to PingAM:

   ```
   Sign in to OpenAM
   User Name: amadmin
   Password: *************
   amster am.example.com:8443>
   ```

## Private key connections

Amster can connect to an AM instance by using a private key pair and an authentication tree in AM. The private key must be available to the Amster client, and the AM instance must trust the client IP address and have the public key in its `authorized_keys` file. Successful connections create an `amAdmin` session in AM.

An installation, or an upgrade of AM creates the following infrastructure for Amster:

* The `amsterService` authentication tree. Changing or removing this tree could prevent Amster connecting to AM.

* The following RSA key pair files, in PKCS#1 PEM format:

  **Default private keypair files**

  | File name                                          | Description                                                                                                                                                                                                                                                                                                                                                                                                              |
  | -------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
  | `/path/to/am/security/keys/amster/authorized_keys` | Holds the public keys of trusted Amster clients. AM checks incoming Amster connections against these trusted keys. By default, contains a copy of the public key of a generated key pair that Amster can use.If this file exists in the configuration directory before a new installation is performed, the file is not overwritten; the contents of the newly-created `amster_rsa.pub` file are appended to it instead. |
  | `/path/to/am/security/keys/amster/amster_rsa`      | Contains the private key of a generated key pair that Amster can use.                                                                                                                                                                                                                                                                                                                                                    |
  | `/path/to/am/security/keys/amster/amster_rsa.pub`  | Contains the public key of a generated key pair that Amster can use.                                                                                                                                                                                                                                                                                                                                                     |

### Connect locally with default private key files

An Amster installation local to a new AM instance can connect without further configuration.

1. Start the Amster command-line interface.

2. Run the `connect` command with the `--private-key`, or the `-k` options:

   ```
   am> connect --private-key /path/to/am/security/keys/amster/amster_rsa \
    https://am.example.com:8443/am
   amster am.example.com:8443>
   ```

### Connect to a remote AM instance

To connect to a remote AM instance, create a private key pair for Amster, and append the contents of the public key to the `authorized_keys` file of the instance.

#### Create and configure a private key pair

Create a new key pair and append the public key to the AM instance:

1. Login to the Amster server.

2. Create a directory for the keys, for example, `/path/to/.ssh` .

3. Run the `ssh-keygen` command to generate a key pair without passphrase. You can create RSA or ECDSA key pairs:

   * To create an RSA key pair, run the `ssh-keygen` command with the `-t rsa` option:

     ```
     $ ssh-keygen -t rsa -N "" -f /path/to/.ssh/id_rsa -b 2048
     Generating public/private rsa key pair.
     Your identification has been saved in id_rsa.
     Your public key has been saved in id_rsa.pub.
     The key fingerprint is:
     78:ca:43:bc:0a:84:b0:ab:ac:40:96:49:48:84:80:63 root@amster_server
     ```

   * To create an ECDSA keypair, run the `ssh-keygen` command with the `-t ecdsa` option. You can create key pairs of 256, 384, or 521 curve sizes.

     For example:

     ```
     $ ssh-keygen -t ecdsa -N "" -f /path/to/.ssh/id_ecdsa -b 521
     Generating public/private ecdsa key pair.
     Your identification has been saved in id_ecdsa.
     Your public key has been saved in id_ecdsa.pub.
     The key fingerprint is:
     6b:b9:75:cb:42:07:91:25:a7:bf:d6:d0:bc:6f:5a:d7 root@amster_server
     ```

     |   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
     | - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
     |   | AM requires the private key to be in PKCS#1 PEM format. Recent versions of the OpenSSH `ssh-keygen` tool creates keys in its own format, which AM cannot process.If your generated private key (`id_ras`) begins with `-----BEGIN OPENSSH PRIVATE KEY-----`, you will need to recreate your keypair in PKCS#1 PEM format.Append the `-m pem` option to the `ssh-keygen` commands above to create a new pair in the supported PKCS#1 PEM format.For example:```
     $ ssh-keygen -m pem -t rsa -N "" -f $HOME/.ssh/id_rsa -b 2048
     ``` |

   These commands generate two files, `id_rsa.pub` or `id_ecdsa.pub` containing the public key, and `id_rsa` or `id_ecdsa` containing the private key.

4. Append the contents of the `id_rsa.pub` or `id_ecdsa.pub` files into the `authorized_keys` file in your AM instance(s); for example, into `/path/to/am/security/keys/amster/authorized_keys`.

5. Start the Amster command-line interface.

6. To connect to AM using a specific private key file, run the `connect` command with the `--private-key`, or the `-k` options, specifying the path to the private key file. For example:

   ```
   am> connect --private-key $HOME/.ssh/id_rsa \
    https://am.example.com:8443/am
   amster am.example.com:8443>
   ```

---

---
title: Create transport keys to export configuration data
description: Generate and install transport keys in PingAM keystores to enable encrypted password export and import during configuration migration between instances
component: pingam
version: 8.1
page_id: pingam:amster:transport-keys
canonical_url: https://docs.pingidentity.com/pingam/8.1/amster/transport-keys.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
page_aliases: ["user-guide:amster-transport-keys.adoc"]
section_ids:
  generate-new-key: Generate and install a new transport key
  duplicate-key: Duplicate and install a transport key
  delete-transport-key: Delete a transport key
---

# Create transport keys to export configuration data

To import and export encrypted password values in the configuration files you must generate a *transport key*, and install it in the keystore of each AM instance that you'll be transporting passwords between.

The transport key must be stored in the default AM keystore, located at `/path/to/am/security/keystores/keystore.jceks`, and should have a key alias of `sms.transport.key`.

The presence of the transport key causes additional fields containing encrypted password values to appear in the exported configuration files. These additional fields have a `-encrypted` suffix, as shown below:

```json
{"authenticatorPushDeviceSettingsEncryptionKeystorePassword":null,
 "authenticatorPushDeviceSettingsEncryptionKeystorePassword-encrypted":"encrypted-pwd"}
```

Encrypted password fields will only be added to REST calls made by administrative users, such as `amAdmin`.

Performance of an AM instance with a transport key present will be significantly impacted. You **MUST** [delete the transport key](#delete-transport-key) when imports and exports have been completed.

Without a transport key present, all password fields are set to `null` in the exported configuration files, regardless of their actual value in the configuration.

## Generate and install a new transport key

Use the `keytool` command to generate the transport key by performing the following steps:

1. Run the `keytool` command, specifying the location of the `.storepass` file as the password to use for the keystore, and the location of the `.keypass` file as the password to use for the key aliases:

   ```
   $ keytool -genseckey -alias "sms.transport.key" -keyalg AES -keysize 128 \
     -storetype jceks -keystore "/path/to/am/security/keystores/keystore.jceks" \
     -storepass:file "/path/to/am/security/secrets/default/.storepass" \
     -keypass:file "/path/to/am/security/secrets/default/.keypass"
   ```

2. You must restart AM for the transport key change to take effect.

   The instance will now be able to include encrypted passwords in the exported configuration files.

To decrypt and import configuration files that contain encrypted passwords, you must install the same transport key used to encrypt it into the keystore of the target AM instance.

## Duplicate and install a transport key

Use the `keytool` command to export the transport key from the source instance keystore, and then install the result on the target instance keystore, by performing the following steps:

1. On the source instance, export the transport key into a keystore that can be transported to another instance by executing the following `keytool` command:

   ```
   $ keytool -importkeystore -srcstoretype jceks -srcalias "sms.transport.key" \
     -deststoretype jceks -destalias "sms.transport.key" \
     -srckeystore "/path/to/am/security/keystores/keystore.jceks" \
     -destkeystore "/path/to/am/security/keystores/transport_keystore.jceks" \
     -srckeypass:file "/path/to/am/security/secrets/default/.keypass" \
     -srcstorepass:file "/path/to/am/security/secrets/default/.storepass" \
     -destkeypass "myTransp0rtK3yP4ssword" \
     -deststorepass "myTransp0rtK3yP4ssword"
   ```

   This command exports the transport key to a temporary keystore file `/path/to/am/security/keystores/transport_keystore.jceks`, and set a store and key password of `myTransp0rtK3yP4ssword`. You need to use these temporary passwords when importing to the target instance.

2. Move the keystore file created in the previous step, in this example `transport_keystore.jceks`, to the filesystem of the target server.

3. On the target server, import the transport key into the AM keystore by executing the following `keytool` command:

   ```
   $ keytool -importkeystore -srcstoretype jceks -srcalias "sms.transport.key" \
     -deststoretype jceks -destalias "sms.transport.key" \
     -srckeystore "/path/to/am/security/keystores/transport_keystore.jceks" \
     -destkeystore "/path/to/am/security/keystores/keystore.jceks" \
     -srckeypass "myTransp0rtK3yP4ssword" \
     -srcstorepass "myTransp0rtK3yP4ssword" \
     -destkeypass:file "/path/to/am/security/secrets/default/.keypass" \
     -deststorepass:file "/path/to/am/security/secrets/default/.storepass"
   ```

   This command imports the transport key from the temporary keystore file `/path/to/am/security/keystores/transport_keystore.jceks` into the AM keystore, and set the transport key password to match the password used by the target keystore.

4. You must restart the target AM instance for the transport key change to take effect.

   The target instance will now be able to correctly decrypt passwords stored in the imported configuration files.

|   |                                                                                                                                                                                                                                                                      |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The presence of the transport key includes encrypted passwords in requests made by an administrative user, causing significant performance degradation. You **MUST** [delete the transport key](#delete-transport-key) when imports and exports have been completed. |

## Delete a transport key

1. Run the following `keytool` command:

   ```
   $ keytool -delete -alias "sms.transport.key" -storetype jceks \
     -storepass:file "/path/to/am/security/secrets/default/.storepass" \
     -keystore "/path/to/am/security/keystores/keystore.jceks"
   ```

2. You must restart the target AM instance for the transport key change to take effect.

   The target instance will no longer include encrypted passwords, nor be able to correctly decrypt passwords stored in configuration files.

---

---
title: Export configuration data
description: Export configuration data from a PingAM instance to JSON-formatted files organized by realm and node version
component: pingam
version: 8.1
page_id: pingam:amster:export-config
canonical_url: https://docs.pingidentity.com/pingam/8.1/amster/export-config.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
page_aliases: ["user-guide:amster-export-config.adoc"]
section_ids:
  export-data-examples: Examples
  export_entire_configuration: Export entire configuration
  export_selected_configuration: Export selected configuration
---

# Export configuration data

Amster can export configuration data from an AM instance. Export configuration data using the `export-config` command.

The exported configuration data is written to a number of JSON-formatted files. The files are arranged in a hierarchy of global and realm configuration data. If you have configuration data for multiple node versions, the data is written to separate node folders.

The following example shows files for version 1 and version 2 of the Username Collector node:

```none
`-- realms
    `-- root
        |-- ...
        |-- UsernameCollector
        |   |-- 6c40132d-c3a5-492e-86b6-23f7978c8d47.json
        |   `-- 8f9d2280-caa7-433f-93a9-1f64f4cae60a.json
        |-- UsernameCollector2
        |   `-- f6a0a1fe-11f0-841a-8de9-0242ac120002.json
        |-- ...
```

To export encrypted password values in the configuration files you must generate and install a *transport key*. Learn more in [Create transport keys to export configuration data](transport-keys.html).

**Usage:**

```
am> export-config --path Path [options]
```

* `--path Path`

  The path to the directory where Amster should save the exported configuration files.

  Existing files are overwritten if they exist. The path is created if it doesn't exist.

**Options:**

* `--realms "Realm" […​]`

  Space-separated list of realms to export. Specify the full path of each realm, and enclose the list in quotation marks. Use a single forward-slash (`/`) to represent the top-level root realm.

  Example: `export-config --realms "/ /subRealm1 /subRealm2"`

  Default: all

* `--realmEntities Entity […​]`

  Space-separated list of realm-based entities to export.

  Use a space character in single-quotes (`' '`) to exclude realm-based entities from the export.

  Find a list of the available entities in the [Entity reference](../entity-reference/preface.html).

  Default: all

* `--globalEntities Entity […​]`

  Space-separated list of global entities to export.

  Use a space character in single-quotes (`' '`) to exclude global entities from the export.

  Find a list of the available entities in the [Entity reference](../entity-reference/preface.html).

  Default: all

* `--failOnError [true|false]`

  If specified, the export process stops if an error occurs.

  Default: `false`

* `--listPasswords [true|false]`

  If specified, the export process creates a listing of entities that contain password data. The listing is stored in a file in the root of the specified export directory.

  Default: `false`

## Examples

Before trying the following examples, start the Amster command-line interface, and connect to the AM instance from which to export data.

Find information on connecting to AM instances in [Connect to AM](connect-am.html).

### Export entire configuration

This example exports all configuration data, and fails immediately if an error occurs.

```
am> export-config --path /tmp/myExportedConfigFiles --failOnError true
Export completed successfully
```

### Export selected configuration

This example exports the configuration for the `DataStoreDecision`, `Scripts`, and `OAuth2Provider` entities in a subrealm of the root realm named `mySubRealm`.

Configuration data for global entities isn't exported.

```
am> export-config --path /tmp/myExportedConfigFiles --realms '/mySubRealm' \
  --realmEntities 'DataStoreDecision Scripts OAuth2Provider' --globalEntities ' '
Export completed successfully
```

---

---
title: Import configuration data
description: Use the import-config command to import configuration data into a PingAM instance
component: pingam
version: 8.1
page_id: pingam:amster:import-config
canonical_url: https://docs.pingidentity.com/pingam/8.1/amster/import-config.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
page_aliases: ["user-guide:amster-import-config.adoc"]
section_ids:
  import-data-examples: Example
---

# Import configuration data

Amster can import configuration data to an AM instance. Import configuration data by using the `import-config` command.

|   |                                                                                                 |
| - | ----------------------------------------------------------------------------------------------- |
|   | A successful import overwrites any configuration that already exists in the target AM instance. |

Before importing configuration data to an AM instance, consider the following points:

* You must connect to the AM instance where you're importing the configuration data after starting the Amster command-line interface. Learn more in [Connect to AM](connect-am.html).

* Make sure the configuration data you're trying to import is compatible with the version of AM you've deployed.

  For example, don't try to import configuration data exported from an AM 7.5 instance into an AM 8.1 instance.

* AM validates that external data stores are configured and available when creating connections to them, including when importing using Amster.

  Make sure each external datastore configured in the source instance has an equivalent datastore available and running before importing Amster configuration into the destination AM instance.

* When importing a full set of configuration data from an instance of AM, specify the `--clean` option to remove configuration settings from the target instance.

  The `--clean` option removes the following items from the target AM instance:

  * Realms, other than the Top Level Realm.

  * Authentication trees.

  * Server and site settings, other than the current server.

  * Services.

  * Secret ID Mappings and secret definitions.

  * Scripts.

  * Audit settings.

  * Policies, policy sets and resource types.

  * Identity store configuration.

  * Agents, and agent groups.

  |   |                                                                                                                                                                                                                                                              |
  | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
  |   | Don't use the `--clean` option if you are only importing a partial Amster export.The target AM instance might not have the settings required to start up and operate if you don't replace the deleted settings by importing a complete set of configuration. |

* By default, Amster configures the value of the `com.iplanet.am.lbcookie.value` property as the value of the server ID.

  To override the default during import, prefix the new value with `override-server-id:` in the configuration files. For example:

  ```none
  "com.iplanet.am.lbcookie.value" : "override-server-id:myLBCookieValue"
  ```

* To import encrypted password values in the configuration files you must install the *transport key* used to encrypt the data. Learn more in [Create transport keys to export configuration data](transport-keys.html).

* Make sure any special characters in names and passwords in Amster shell variables are escaped as required by the Groovy language.

  For example, the dollar `$` character is a special character in Groovy. The following are two possible ways of escaping the `$` character:

  ```
  variable.name="/pa$$word/"
  variable.name='pa\\$\\$word'
  ```

  You can't use variables, such as `${varname}`, or configuration expressions, such as `&{varname}` if you convert a double-quoted string into a single-quoted string.

  Read the [Groovy documentation](http://groovy-lang.org/syntax.html#all-strings) for more information on escaping special characters in strings.

**Usage:**

```
am> import-config --path Path [options]
```

* `--path Path`

  The path to the directory containing configuration files to import or an individual JSON file to import.

  If you specify a directory, all valid JSON files in that directory and any sub-directories are included in the import.

**Options:**

* `--failOnError [true|false]`

  If specified, the import process stops if an error occurs.

  Default: `false`

* `--clean [true|false]`

  If specified, all configuration data is removed from the target AM instance before the import is performed.

  Only set this option to `true` when importing a **full** set of configuration files into a new AM instance. Otherwise, the target instance might not function correctly.

  Default: `false`

## Example

Before trying the following examples, start the Amster command-line interface, and connect to the AM instance where you're importing the configuration data.

Find information on connecting to AM instances in [Connect to AM](connect-am.html).

This example cleans all configuration from the target AM instance before importing a full set of configuration data, but won't stop the import if an error occurs.

```
am> import-config --path /tmp/myExportedConfigFiles --clean true --failOnError false
Cleaning global settings
Deleting JSON: Global JSON Handler
Deleting Scripting: 9de3eb62-f131-4fac-a294-7bd170fd4acb
Deleting Scripting: 7e3d7067-d50f-4674-8c76-a3e13a810c33
Deleting Scripting: c827d2b4-3608-4693-868e-bbcf86bd87c7
Global settings cleaned
Importing directory /tmp/myExportedConfigFiles
…​
Import completed successfully
```

---

---
title: Install Amster
description: Download and extract Amster to install the standalone client tool for managing PingAM configurations
component: pingam
version: 8.1
page_id: pingam:amster:install-amster
canonical_url: https://docs.pingidentity.com/pingam/8.1/amster/install-amster.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
page_aliases: ["user-guide:amster-install.adoc"]
section_ids:
  sec-prerequisites: Prerequisites
  install_process: Install process
  amster-firststeps: First steps
---

# Install Amster

## Prerequisites

Amster is a standalone client that doesn't need any other Ping Advanced Identity Software component to run. Before you install, check the following prerequisites:

* Amster requires a Java developer environment. Check the output of the `java -version` command to make sure your version is supported.

* The `JAVA_HOME` environment variable must be set.

## Install process

The [Ping Identity Download Center](https://backstage.pingidentity.com/downloads/browse/am/featured) hosts downloadable versions of Amster. For each release of AM you can download Amster as a `.zip` file.

Download `Amster-8.1.1.zip` and extract it in the file system directory where you want to run it:

```
$ unzip ~/Downloads/Amster-8.1.1.zip -d /path/to/
```

> **Collapse: File and directory reference**
>
> The following files and directories are extracted:
>
> * `bcprov-jdk15on-1.55.jar`
>
>   Third-party cryptography library, by Bouncy Castle.
>
> * `bcpkix-jdk15on-1.55.jar`
>
>   Third-party cryptography library, by Bouncy Castle.
>
> * `amster`
>
>   The `amster` command.
>
> * `README.md`
>
>   Amster readme file, with quick-start information.
>
> * `LICENSE`
>
>   Ping's Amster terms of license.
>
> * `amster-8.1.1.jar`
>
>   The main Amster Java library.
>
> * `/legal-notices`
>
>   Directory containing legal notices relating to the Amster distribution.
>
> * `/samples`
>
>   Directory containing sample scripts for export, import, and others. Learn more in [Amster sample scripts](usage-examples.html#amster-samples).

## First steps

Once Amster is extracted, run the `amster` command to start the client:

```
$ cd /path/to/amster
$ ./amster

Amster OpenAM Shell (version build build, JVM: version)
Type ':help' or ':h' for help
------------------------------------------------------------------------------
am>
```

The version of Amster is included in the first line of output, as well as the version of the running JDK.

|   |                                                                                                                                       |
| - | ------------------------------------------------------------------------------------------------------------------------------------- |
|   | If the `amster` command fails to load, make sure the `JAVA_HOME` environment variable is set, and that your JDK version is supported. |

To exit the client, run the `:exit` or `:q` commands:

```
am> :exit
$
```

To get a list of the commands available to the client, run the `:help` command:

```
am> :help

For information about Groovy, visit:
   http://groovy-lang.org

Available commands:
   connect         (am  ) Connect to an OpenAM instance
   create          (c   ) Create an OpenAM entity
   read            (r   ) Read an OpenAM entity
   update          (u   ) Update an OpenAM entity
   delete          (d   ) Delete an OpenAM entity
   query           (q   ) Query an OpenAM entity
   action          (a   ) Perform action an OpenAM entity
   import-config   (i   ) Import configuration into OpenAM
   export-config   (x   ) Export configuration from OpenAM
   replace         (rep ) Replace all matching text
   install-openam  (inst) Install OpenAM
   :help           (:h  ) Display this help message
   ?               (:?  ) Alias to: :help
   :exit           (:x  ) Exit the shell
   :quit           (:q  ) Alias to: :exit
   :load           (:l  ) Load a file or URL into the buffer
   .               (:.  ) Alias to: :load

For help on a specific command type:
   :help command
```

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | To run an `update` command on an entity that contains a large number of key/value pairs, such as [DefaultAdvancedProperties](../entity-reference/sec-amster-entity-defaultadvancedproperties.html#sec-amster-entity-defaultadvancedproperties-global-ops-update), you must provide the entire JSON body, even if you only need to update a small subset of data.A simple way to do this is to run a `read` command, copy and edit the output, and paste it into the body of the `update` command. Alternatively, you can run `export-config`, copy the specific entity file to an identical empty file structure, edit the file, and call `import-config` setting the path to the top directory of the updated file structure. |

To show help information available for a particular command, run `:help command`. For example:

```
am> :help connect

usage: connect [options] <baseurl>
Options:

  -i, --interactive
        If specified you will be prompted for credentials. Defaults to private
        key authentication.

  -k, --private-key
        Path to a private key file or directory containing one of amster_rsa,
        id_rsa or id_ecdsa. Defaults to {USER_HOME}/.ssh.

  -t, --connection-timeout
        The default timeout is 10 seconds. If specified, this parameter sets
        the timeout in seconds.

Connect to the OpenAM instance at the given URL.
Example:

  connect -i https://am.example.com/am

  connect -i -t 30 https://am.example.com/am
```

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | When a command does not proceed as expected, it can sometimes be helpful to start the `amster` command in debug mode and try again. To activate debug mode, start the `amster` command using the `-d` flag. For example:```
$ ./amster -d
Listening for transport dt_socket at address: 6006
DEBUG [org.codehaus.groovy.tools.shell.BufferManager] Created new buffer with index: 0
DEBUG [org.codehaus.groovy.tools.shell.BufferManager] Buffers reset
DEBUG [org.codehaus.groovy.tools.shell.Parser] Using parser flavor: rigid
…​
```While in debug mode, the `amster` command output shows additional information, such as connection handshakes and Groovy calls. |

---

---
title: Integrate Amster in your environment
description: Export and customize PingAM configuration across environments using Amster, with support for configuration variables and scripted deployment automation
component: pingam
version: 8.1
page_id: pingam:amster:integrate-amster
canonical_url: https://docs.pingidentity.com/pingam/8.1/amster/integrate-amster.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
page_aliases: ["user-guide:amster-integration.adoc"]
---

# Integrate Amster in your environment

Amster allows you to export the configuration of an AM instance, and customize it ready for import into any other AM instance in your environment. For example, you can export the configuration from the development environment, customize the passwords and keystore values, and import it in your QA or integration environment for testing.

To make this process easier, Amster allows you to configure variables inside the exported configuration files, and also, to script a series of commands and Amster tasks, so they can be easily included in your processes or pipelines.

[icon: code, set=fas, size=3x]

#### [Use configuration expressions](config-expressions.html)

Learn Amster configuration expressions.

[icon: terminal, set=fas, size=3x]

#### [Script amster commands](scripts.html)

Execute scripts with Amster.

---

---
title: Scripts
description: Create script files to load and execute series of Amster commands with variables, supporting looping and conditional structures using Groovy syntax
component: pingam
version: 8.1
page_id: pingam:amster:scripts
canonical_url: https://docs.pingidentity.com/pingam/8.1/amster/scripts.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
page_aliases: ["user-guide:amster-usage-scripts.adoc"]
section_ids:
  amster-errors-scripts: Check for errors when running in scripts
  amster-variables-scripts: Variables in Amster scripts
  amster_shell_variables: Amster shell variables
  operating_system_environment_variables: Operating system environment variables
  java_system_properties: Java system properties
---

# Scripts

You can create script files containing a series of commands and variable declarations, which can be loaded and executed within Amster.

Start each separate command or variable declaration on a new line. Use the backslash (kbd:\[\\]) character to represent line continuations.

For example, the following script installs an AM instance, and then exits the Amster command-line interface:

```groovy
install-openam \
 --serverUrl https://am.example.com:8443/am \
 --authorizedKey /var/amster/authorized_keys \
 --cookieDomain .example.com \
 --adminPwd password \
 --cfgStoreHost ds.example.com \
 --cfgStoreDirMgrPwd password  \
 --cfgStoreAdminPort 4444 \
 --cfgStorePort 1636 \
 --cfgStoreSsl SSL \
 --cfgStore dirServer \
 --cfgDir /root/am \
 --userStoreDirMgrPwd password \
 --userStoreHost ds.example.com \
 --userStoreType LDAPv3ForOpenDS \
 --userStorePort 1636 \
 --userStoreSsl SSL \
 --userStoreRootSuffix ou=identities \
 --acceptLicense
 :exit
```

To load and execute the commands within a script, use the `:load` command, as follows:

```
am> :load myScript.amster
```

You can specify more than one script to load. Scripts are loaded and executed in the order they are specified. If a command in a script fails, execution continues with the next command.

You can also invoke scripts by passing them as a parameter to the `amster` command.

For example:

```
$ vi samples/myScript.amster
  connect https://am.example.com:8443/am -k /home/Ping/am/amster_rsa
  :exit
$ ./amster samples/myScript.amster

Amster OpenAM Shell (version build build, JVM: version)
Type ':help' or ':h' for help.
--------------------------------------------------------------------------------
am> :load samples/myScript.amster

===> true
```

The Amster shell supports an `eval(String)` function, which evaluates any Amster command expressed as a string. For example, the function is required within looping structures:

```groovy
for (i = 0; i < 4; i++) {
    eval("create DataStoreModule --realm / --body '{\"_id\":\"myDataStore$i\"}'")
 }
```

You must also use the `eval(String)` function when using Amster commands in conditional structures:

```groovy
dbStatus = databaseName
    ? 'Found'
    : eval("create DataStoreModule --realm / --body '{\"_id\":\"myDataStore\"}'")
```

|   |                                                                                                                              |
| - | ---------------------------------------------------------------------------------------------------------------------------- |
|   | Amster includes a number of [sample scripts](usage-examples.html#amster-samples) in the `/path/to/amster/samples` directory. |

## Check for errors when running in scripts

There is no way to exit with a non-zero status code when an `amster` command produces a result other than success.

To monitor `amster` command errors, send the command output to a file, then search that file for success or failure conditions.

For example:

```
$ ./amster samples/myScript.amster >> myOutputfile.txt
```

Note that error and success messages can change between versions, so any scripts that rely on these messages should be reviewed during upgrades.

## Variables in Amster scripts

When scripting Amster tasks, it is often useful to use variables. An example would be storing the AM connection string in a variable, the value of which is swapped among environments.

You can define variables in the Amster Groovy shell directly, or you can import them to the shell if they are defined as Java properties or as operating system environment variables:

### Amster shell variables

Define Amster shell variables using the standard camel case notation for naming variables in Groovy. For example:

```
am> smtpPort = "1342"
===> 1342
```

You can define maps as shell variables, but Amster commands cannot access the contents of the map directly. Assign key values to Amster shell variables so that commands can use them. For example:

```
am> myMap= [ AM_URL: "https://am.example.com:8443/am", AMSTER_KEY: "/opt/am/id_rsa" ]
===> [AM_URL:https://am.example.com:8443/am, AMSTER_KEY:/opt/am/id_rsa]
am> myAM= myMap.AM_URL
===> https://am.example.com:8443/am
am> myKey= myMap.AMSTER_KEY
===> /opt/am/id_rsa
am> connect -k myKey myAM
```

### Operating system environment variables

Import environment variables into the Amster shell using Groovy syntax.

The following commands are examples of operations you can perform in a Groovy shell. Learn more in the Groovy documentation.

To see all the environment variables available for import from a Unix shell, run the following command:

```
am> System.getenv()
===> [PATH:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin:/opt/X11/bin,
         SHELL:/bin/bash, JAVA_HOME:/path/to/jvm, TERM:xterm-256color,
         USER:Ping, LANG:en_GB.UTF-8, PWD:/Users/Ping/amster…​…​]
```

To assign the value of an environment variable to an Amster shell variable, run the following command:

```
am> myShell=System.getenv("SHELL")
===> /bin/bash
```

To assign all the environment variables to a map and then list them, run the following commands:

```
am> ENV=System.getenv()
===> [SHELL:/bin/bash, USER:Ping, LANG:en_GB.UTF-8, PWD:/Users/Ping/amster,
      AMURL:https://am.example.com:8443/am, CFGDIR:/opt/am…​…​]
am> ENV.each { println it }
SHELL:/bin/bash
USER:Ping
LANG:en_GB.UTF-8
PWD:/Users/Ping/amster
AMURL:https://am.example.com:8443/am
CFGDIR:/opt/am
…​…​
```

Amster commands cannot access the contents of a map directly; you must assign key values to Amster shell variables before commands can use them. For example:

```
am> myAM = ENV.AMURL
===> https://am.example.com:8443/am
am> myCfgDir = ENV.CFGDIR
===> /opt/am> install-openam --serverURL myAM --adminPWd password --cfgDir myCfgDir --acceptLicense
```

The following is an example of an Amster script that assigns the value of environment variables to Amster shell variables:

```groovy
myAM = System.getenv("AMURL")
myCfgDir = System.getenv("CFGDIR")
install-openam --serverURL myAM --adminPWd password --cfgDir myCfgDir --acceptLicense
:exit
```

### Java system properties

You can pass environment variables to the Amster shell when executing the `amster` command with the `-D` parameter.

For example, you could create the following bash script to call the `amster` command:

```bash
#!/bin/bash
amUrl="https://am.example.com:8443/am"
amsterKey="/root/am/amster_rsa"
configPath="/root/am-config"
./amster export-config.amster -D AM_URL=${amUrl} -D AMSTER_KEY=${amsterKey} \
-D AM_CONFIG_PATH=${configPath}
```

To see all properties available from the Java runtime, run the following command:

```
am> System.getProperties()
===> [java.runtime.name:Java™ SE Runtime Environment, AM_URL:https://am.example.com:8443/am,
      java.vm.version:_version_, gopherProxySet:false, …​, path.separator::, …​]
```

To import the Java variables into the Groovy shell, run the following command:

```
am> amUrl = System.getProperty("AM_URL")
===> https://am.example.com:8443/am
am> amsterKey = System.getProperty("AMSTER_KEY")
===> /root/am/amster_rsa
am> exportPath = System.getProperty("AM_CONFIG_PATH")
===> /root/am-config
```

You can use the variables in an Amster script by importing them in Groovy first. For example:

```groovy
amUrl = System.getProperty("AM_URL")
amsterKey = System.getProperty("AMSTER_KEY")
exportPath = System.getProperty("AM_CONFIG_PATH")

connect amUrl -k amsterKey
export-config --path exportPath --failOnError
:exit
```

To see all the environment variables defined in the Amster shell, run the following command:

```
am> binding.variables.each{ println it.key println it.value }
eval
org.codehaus.groovy.runtime.MethodClosure@3f270e0a
_
/bin/bash
amUrl
https://am.example.com:8443/am
smtpPort
1342
amsterKey
/root/am/amster_rsa
exportPath
/root/am-config
myShell
/bin/bash
===> [eval:org.codehaus.groovy.runtime.MethodClosure@3f270e0a, _:/bin/bash,
      amUrl:https://am.example.com:8443/am, smtpPort:1342,
      amsterKey:/root/am/amster_rsa, exportPath:/root/am-config, myShell:/bin/bash]
```

---

---
title: What is Amster?
description: Command-line interface for scripted PingAM deployments, configuration export and import, and managing deployments through DevOps processes
component: pingam
version: 8.1
page_id: pingam:amster:introduction
canonical_url: https://docs.pingidentity.com/pingam/8.1/amster/introduction.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
page_aliases: ["user-guide:amster-introduction.adoc"]
---

# What is Amster?

Amster is a command-line interface built upon the PingAM REST interface. Use Amster in DevOps processes, such as continuous integration, command-line installations, and scripted cloud deployments.

Amster provides the following features:

* **Remote, scripted deployments**. Script AM deployments by using the Groovy scripting support within Amster.

  Learn more in [Scripts](scripts.html) and [Passive install using Amster](../installation/passive-install-amster.html).

* **AM configuration import and export**. Amster can export all the configuration related to an AM instance, and import it back to the same, or a different instance.

  Amster only manages configuration data. User information in data stores isn't imported or exported, or modified in any way.

  Learn more in [Export configuration data](export-config.html) and [Import configuration data](import-config.html).

* **Configuration stored in JSON**. Amster exports configuration to a hierarchy of JSON format text files on the local filesystem.

  Global defaults and configuration are exported to the `global` folder, and the configuration for realms is exported into subfolders of the `realms` folder.

  The following is a simplified example of an exported hierarchy, including the top-level `root` realm:

  ```none
  |-- global
      |-- GlobalScripts
      |   |-- 157298c0-7d31-4059-a95b-eeb08473b7e5.json
      |   `-- 36863ffb-40ec-48b9-94b1-9a99f71cc3b5.json
      |-- Realms
      |   `-- root.json
      |-- Servers
      |   |-- 01
      |   |   |-- AdvancedProperties.json
      |   |   |-- CtsDataStoreProperties.json
      |   |   |-- DirectoryConfiguration.json
      |   |   |-- GeneralProperties.json
      |   |   |-- SdkProperties.json
      |   |   |-- SecurityProperties.json
      |   |   `-- SessionProperties.json
      |   `-- 01.json
      `-- Session.json
  `-- realms
      `-- root
          |-- AuthTree
          |   |-- Agent.json
          |   |-- amsterService.json
          |   `-- ldapService.json
          `-- Scripts
              |-- 9de3eb62-f131-4fac-a294-7bd170fd4acb.json
              `-- c827d2b4-3608-4693-868e-bbcf86bd87c7.json
  ```

  Store these files in a version control system to manage and maintain AM configurations.

  Find a list of the available entities in the [Entity reference](../entity-reference/preface.html).

* **Encryption of sensitive data**. Amster can encrypt exported passwords and sensitive data in the configuration files that are stored on disk. Only a correctly configured AM instance with the required transport key installed is able to decrypt and import the values.

  Learn more in [Create transport keys to export configuration data](transport-keys.html).