---
title: About DS tools
description: Overview of PingDS command-line tools for LDAP operations, including trust store setup and default connection settings.
component: pingds
version: 8.1
page_id: pingds:ldap-guide:about-tools
canonical_url: https://docs.pingidentity.com/pingds/8.1/ldap-guide/about-tools.html
llms_txt: https://docs.pingidentity.com/pingds/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2025-10-22T14:42:39Z
keywords: ["Features", "LDAP"]
section_ids:
  cli-tools: Client tools
  trusted_certificates: Trusted certificates
  tools-properties: Default settings
---

# About DS tools

## Client tools

* Add DS client command-line tools to your PATH:

  * Bash

  * PowerShell

  ```console
  $ export PATH=/path/to/opendj/bin:${PATH}
  ```

  ```powershell
  $env:PATH += ";C:\path\to\opendj\bat"
  ```

* For reference information, use the `--help` option with any DS tool.

* All commands call Java programs. This means every command starts a JVM, so it takes longer to start than a native binary.

| Command(1)           | Description                                                                                                                                                             |
| -------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `addrate`            | Measure add and delete throughput and response time.                                                                                                                    |
| `authrate`           | Measure bind throughput and response time.                                                                                                                              |
| `base64`             | Encode and decode data in base64 format.Base64-encoding represents binary data in ASCII, and can be used to encode character strings in LDIF, for example.              |
| `ldapcompare`        | Compare the attribute values you specify with those stored on entries in the directory.                                                                                 |
| `ldapdelete`         | Delete entries from the directory.                                                                                                                                      |
| `ldapmodify`         | Modify the specified attribute values for the specified entries.                                                                                                        |
| `ldappasswordmodify` | Modify user passwords.                                                                                                                                                  |
| `ldapsearch`         | Search a branch of directory data for entries that match the LDAP filter you specify.                                                                                   |
| `ldifdiff`           | Display differences between two LDIF files, with the resulting output having LDIF format.                                                                               |
| `ldifmodify`         | Modify specified attribute values for specified entries in an LDIF file.                                                                                                |
| `ldifsearch`         | Search a branch of data in LDIF for entries matching the LDAP filter you specify.                                                                                       |
| `makeldif`           | Generate directory data in LDIF based on templates that define how the data should appear.Also refer to [makeldif-template](../tools-reference/makeldif-template.html). |
| `modrate`            | Measure modification throughput and response time.                                                                                                                      |
| `searchrate`         | Measure search throughput and response time.                                                                                                                            |

(1) Linux names for the commands. Equivalent Windows commands have .bat extensions.

## Trusted certificates

When a client tool initiates a secure connection to a server, the server presents its digital certificate.

The tool must decide whether it does trust the server certificate and continues to negotiate a secure connection, or doesn't trust the server certificate and drops the connection. To trust the server certificate, the tool's truststore must contain the trusted certificate. The trusted certificate is a CA certificate, or the self-signed server certificate.

The following table explains how the tools locate the truststore.

| Truststore Option                        | Truststore Used                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| ---------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| None                                     | The default truststore, `user.home/.opendj/keystore`, where *user.home* is the Java system property. *user.home* is `$HOME` on Linux and `%USERPROFILE%` on Windows. The keystore password is `OpenDJ`. Do not change the file name or the password.- In interactive mode, DS command-line tools prompt for approval to trust an unrecognized certificate, and whether to store it in the default truststore for future use.

- In silent mode, the tools rely on the default truststore. |
| `--use<Type>TrustStore {trustStorePath}` | DS only uses the specified truststore. The *\<Type>* in the option name reflects the trust store type.The tool fails with an error if it can't trust the server certificate.                                                                                                                                                                                                                                                                                                              |

## Default settings

You can set defaults in the `~/.opendj/tools.properties` file, as in the following example:

```ini
hostname=localhost
port=1636
bindDN=uid=kvaughan,ou=People,dc=example,dc=com
bindPassword\:file=/path/to/.pwd
useSsl=true
```

When you use an option with a colon, such as `bindPassword:file`, escape the colon with a backslash (`\:`) in the properties file.

The file location on Windows is `%UserProfile%\.opendj\tools.properties`.
