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

---

---
title: Authentication (binds)
description: Authenticate LDAP clients to PingDS using simple binds, SASL mechanisms, and identity mappers to map user IDs to DNs.
component: pingds
version: 8.1
page_id: pingds:ldap-guide:client-auth
canonical_url: https://docs.pingidentity.com/pingds/8.1/ldap-guide/client-auth.html
llms_txt: https://docs.pingidentity.com/pingds/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2025-10-22T14:42:39Z
keywords: ["Authentication", "LDAP"]
section_ids:
  client-auth-identity-mappers: Identity mappers
---

# Authentication (binds)

Authentication is the act of confirming the identity of a principal. Authorization is the act of determining whether to grant or to deny access to a principal. Authentication is performed to make authorization decisions.

DS servers implement fine-grained access control for authorization. Authorization for an operation depends on who is requesting the operation. DS servers must authenticate the principal before making an authorization decision. In LDAP, the bind operation authenticates the principal.

Clients bind by providing a means to find their principal's entry, and credentials to check against the entry:

* In a simple bind operation, the client provides an LDAP name, usually the DN identifying its entry, and the corresponding password stored in the entry.

  In the simplest bind operation, the client provides a zero-length name and a zero-length password. This results in an LDAP anonymous bind operation (anonymous bind) *(tooltip: \<div class="paragraph">
  \<p>Simple authentication with an empty DN and an empty password, allowing anonymous access like reading public information.\</p>
  \</div>)*. LDAP servers may allow anonymous binds to read public information, such as root DSE attributes.

* Other bind mechanisms involve digital certificates, Kerberos tickets, or challenge response mechanisms that prove the client knows a password.

A user rarely knows, let alone enters, their DN. Instead, a user provides a client application with an identifying string stored in their entry, such as a user ID or an email address. The client application builds the DN directly from the user's identity string, or searches for the user entry based on the user's identity string to find the DN. The client application performs a simple bind with the resulting DN.

For example, suppose Babs Jensen enters her email address, `bjensen@example.com`, and password. The client application might search for the entry matching `(mail=bjensen@example.com)` under base DN `dc=example,dc=com`. Alternatively, the client application might extract the user ID `bjensen` from the address, then build the corresponding DN, `uid=bjensen,ou=people,dc=example,dc=com`, without a lookup.

## Identity mappers

When the mapping from the user identifier to the DN is known, DS servers can use an identity mapper to do the translation. Identity mappers are used to perform PLAIN SASL authentication (with a user name and password), SASL GSSAPI authentication (Kerberos V5), SASL CRAM MD5, and DIGEST MD5 authentication. They also map authorization IDs to DNs for password modify extended operations and proxied authorization.

One use of PLAIN SASL is to translate user names from HTTP Basic authentication to LDAP authentication. The following example shows PLAIN SASL authentication using the default exact match identity mapper. In this example, Babs Jensen has access to read the hashed value of her password. Notice the authentication ID is her user ID, `u:bjensen`, rather than the DN of her entry:

```console
$ ldapsearch \
 --hostname localhost \
 --port 1636 \
 --useSsl \
 --trustStorePath /path/to/opendj/config/keystore \
 --trustStoreType PKCS12 \
 --trustStorePassword:file /path/to/opendj/config/keystore.pin \
 --baseDN dc=example,dc=com \
 --saslOption mech=PLAIN \
 --saslOption authid=u:bjensen \
 --bindPassword hifalutin \
 "(cn=Babs Jensen)" \
 userPassword
```

> **Collapse: Show output**
>
> ```
> dn: uid=bjensen,ou=People,dc=example,dc=com
> userPassword: {PBKDF2-HMAC-SHA256}10:<hash>
> ```

The [Exact Match Identity Mapper](../configref/objects-exact-match-identity-mapper.html) searches for a match between the string (here, `bjensen`), and the value of a specified attribute (by default, the `uid` attribute). By default, the identity mapper searches all public naming contexts local to the server. If duplicate entries exist, or if the required indexes are not available for all backends, this behavior can be restricted using the `match-base-dn` property.

You can configure multiple identity mappers, if necessary. When resolving the identity, the server uses the first identity mapper that finds a match. If multiple identity mappers match different entries, however, then the server returns LDAP error code 19, Constraint Violation.

If you know that users are entering their email addresses, you could create an exact match identity mapper for email addresses, then use that for PLAIN SASL authentication:

> **Collapse: Show example**
>
> ```console
> $ dsconfig \
>  create-identity-mapper \
>  --hostname localhost \
>  --port 4444 \
>  --bindDN uid=admin \
>  --bindPassword password \
>  --mapper-name "Email Mapper" \
>  --type exact-match \
>  --set match-attribute:mail \
>  --set enabled:true \
>  --trustStorePath /path/to/opendj/config/keystore \
>  --trustStoreType PKCS12 \
>  --trustStorePassword:file /path/to/opendj/config/keystore.pin \
>  --no-prompt
> $ dsconfig \
>  set-sasl-mechanism-handler-prop \
>  --hostname localhost \
>  --port 4444 \
>  --bindDN uid=admin \
>  --bindPassword password \
>  --handler-name PLAIN \
>  --set identity-mapper:"Email Mapper" \
>  --trustStorePath /path/to/opendj/config/keystore \
>  --trustStoreType PKCS12 \
>  --trustStorePassword:file /path/to/opendj/config/keystore.pin \
>  --no-prompt
> $ ldapsearch \
>  --hostname localhost \
>  --port 1636 \
>  --useSsl \
>  --trustStorePath /path/to/opendj/config/keystore \
>  --trustStoreType PKCS12 \
>  --trustStorePassword:file /path/to/opendj/config/keystore.pin \
>  --baseDN dc=example,dc=com \
>  --saslOption mech=PLAIN \
>  --saslOption authid=u:bjensen@example.com \
>  --bindPassword hifalutin \
>  "(cn=Babs Jensen)" \
>  userPassword
> ```
>
> Output
>
> ```
> dn: uid=bjensen,ou=People,dc=example,dc=com
> userPassword: {PBKDF2-HMAC-SHA256}10:<hash>
> ```

A [Regular Expression Identity Mapper](../configref/objects-regular-expression-identity-mapper.html) uses a regular expression to extract a substring from the string provided. The server searches for a match between the substring and the value of a specified attribute. When an email address is user ID + @ + domain, you can use the default regular expression identity mapper in the same way as the email mapper in the example above. The default regular expression pattern is `^([^@]+)@.+$`, and the part of the identity string matching `([^@]+)` is used to find the entry by user ID:

```console
$ dsconfig \
 set-sasl-mechanism-handler-prop \
 --hostname localhost \
 --port 4444 \
 --bindDN uid=admin \
 --bindPassword password \
 --handler-name PLAIN \
 --set identity-mapper:"Regular Expression" \
 --trustStorePath /path/to/opendj/config/keystore \
 --trustStoreType PKCS12 \
 --trustStorePassword:file /path/to/opendj/config/keystore.pin \
 --no-prompt
$ ldapsearch \
 --hostname localhost \
 --port 1636 \
 --useSsl \
 --trustStorePath /path/to/opendj/config/keystore \
 --trustStoreType PKCS12 \
 --trustStorePassword:file /path/to/opendj/config/keystore.pin \
 --baseDN dc=example,dc=com \
 --saslOption mech=PLAIN \
 --saslOption authid=u:bjensen@example.com \
 --bindPassword hifalutin \
 "(cn=Babs Jensen)" \
 userPassword
```

> **Collapse: Show output**
>
> ```
> dn: uid=bjensen,ou=People,dc=example,dc=com
> userPassword: {PBKDF2-HMAC-SHA256}10:<hash>
> ```

Use the `dsconfig` command interactively to experiment with `match-pattern` and `replace-pattern` settings for the regular expression identity mapper. The `match-pattern` can be any `javax.util.regex.Pattern` regular expression.

Like the exact match identity mapper, the regular expression identity mapper searches all public naming contexts local to the server by default. If duplicate entries exist, this behavior can be restricted using the `match-base-dn` property.

---

---
title: LDAP compare
description: Use the LDAP compare operation to check whether a specified attribute value matches a value stored in a PingDS directory entry.
component: pingds
version: 8.1
page_id: pingds:ldap-guide:compare-ldap
canonical_url: https://docs.pingidentity.com/pingds/8.1/ldap-guide/compare-ldap.html
llms_txt: https://docs.pingidentity.com/pingds/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2025-10-22T14:42:39Z
keywords: ["LDAP"]
---

# LDAP compare

The LDAP compare operation checks whether an attribute value you specify matches the attribute value stored on one or more directory entries.

In this example, Kirsten Vaughan uses the `ldapcompare` command to check whether the value matches the value of the `description` attribute:

```console
$ ldapcompare \
 --hostname localhost \
 --port 1636 \
 --useSsl \
 --trustStorePath /path/to/opendj/config/keystore \
 --trustStoreType PKCS12 \
 --trustStorePassword:file /path/to/opendj/config/keystore.pin \
 --bindDN "uid=kvaughan,ou=people,dc=example,dc=com" \
 --bindPassword bribery \
 'description:Description on ou=People' \
 uid=kvaughan,ou=people,dc=example,dc=com
```

> **Collapse: Show output**
>
> ```
> # Comparing type description with value Description on ou=People in entry uid=kvaughan,ou=people,dc=example,dc=com
> # Compare operation returned true for entry uid=kvaughan,ou=people,dc=example,dc=com
> ```

---

---
title: LDAP schema
description: "Understand LDAP schema in PingDS: read attribute types and object classes, handle schema violations, and work with extensibleObject."
component: pingds
version: 8.1
page_id: pingds:ldap-guide:schema
canonical_url: https://docs.pingidentity.com/pingds/8.1/ldap-guide/schema.html
llms_txt: https://docs.pingidentity.com/pingds/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2025-10-22T14:42:39Z
keywords: ["Integration", "LDAP", "Standards"]
section_ids:
  getting-schema-information: Read schema
  example-finding-schema: Find LDAP schema
  example-reading-schema-definition: Object class schema
  example-reading-attribute-definitions: Attribute schema
  respecting-schema: Schema errors
  example-object-class-violations: Object class violations
  example-invalid-attribute-syntax: Invalid attribute syntax
  abusing-schema: Workarounds
  example-extensible-object: ExtensibleObject
---

# LDAP schema

LDAP services are based on X.500 directory standards (X.500) *(tooltip: \<div class="paragraph">
\<p>A family of standardized protocols for accessing, browsing, and maintaining a directory, predating LDAP.\</p>
\</div>)* Directory Services, which are telecommunications standards. In telecommunications, interoperability is paramount. Competitors must cooperate to the extent that they use each other's systems. For directory services, the protocols for exchanging data and the descriptions of the data are standardized. LDAP defines LDAP schema (schema) *(tooltip: \<div class="paragraph">
\<p>Definitions of object classes, attributes types, attribute value syntaxes, matching rules, and other constrains on entries.\</p>
\</div>)* that describe what attributes a given LDAP entry must have and may optionally have, and what attribute values can contain and how they can be matched. Formal schema definitions protect interoperability when many applications read and write to the same directory service. Directory data are much easier to share when you understand how to use LDAP schema.

[LDAP schema](../config-guide/schema.html) covers LDAP schema from the server administrator's perspective. Administrators can update LDAP directory schema. DS servers support a large number of standard schema definitions by default. Administrators can also adjust how strictly each DS server applies schema definitions. For the list of standard definitions that DS servers provide, refer to [Standard schema](../config-guide/schema.html#standard-schema).

As a script developer, you use the available schema, and accept the server's application of schema when updating directory entries.

## Read schema

Directory servers publish information about services they provide as operational attributes of the root DSA-specific entry (root DSE) *(tooltip: \<div class="paragraph">
\<p>The entry with an empty string DN ("") exposing information about the directory server itself.\</p>
\</div>)*. The root DSE is the entry with an empty string DN, `""`. The DSA-specific entry (DSE) *(tooltip: \<div class="paragraph">
\<p>An entry holding information for use by the directory, not returned in searches by default.\</p>
\</div>)* differs by server but is almost identical for replicas.

DS servers publish the DN of the entry with schema definitions the `subschemaSubentry` attribute:

### Find LDAP schema

Look up the schema DN:

```console
$ ldapsearch \
 --hostname localhost \
 --port 1636 \
 --useSsl \
 --trustStorePath /path/to/opendj/config/keystore \
 --trustStoreType PKCS12 \
 --trustStorePassword:file /path/to/opendj/config/keystore.pin \
 --bindDN "uid=kvaughan,ou=people,dc=example,dc=com" \
 --bindPassword bribery \
 --baseDN dc=example,dc=com \
 --searchScope base \
 "(&)" \
 subschemaSubentry
```

> **Collapse: Show output**
>
> ```
> dn: dc=example,dc=com
> subschemaSubentry: cn=schema
> ```

By default, the DN for the schema entry is `cn=schema`.

The schema entry has the following attributes whose values are schema definitions:

* `attributeTypes`

  Attribute type definitions describe attributes of directory entries, such as `givenName` or `mail`.

  Consider the following features of LDAP attributes:

  * Attributes can have multiple names.

    Many common attributes take advantage of this feature. For example, `cn` and `commonName` both refer to the same attribute type. The same is true of `dc` and `domainComponent`, `l` and `localityName`, and others.

  * The definition specifies the attribute's syntax and the matching rules for indexing the attribute and searching its values for matches.

    The index for a telephone number is not the same as the index for a digital certificate. By default, you must take the attribute's syntax into account when adding or updating its values.

  * LDAP attributes can have multiple values by default.

    Think of the values as a set, rather than an array. LDAP does not require directory servers to order the values in any particular way, and it does not allow duplicates.

    The definition must label the attribute type as `SINGLE-VALUE` to change this, even for boolean attributes. Keep this in mind when defining your own attributes.

  * Some attributes are intended for use by the directory server, rather than external applications.

    This is the case, for example, when you observe `NO-USER-MODIFICATION` in the definition. These definitions also set `USAGE` to an operational attribute type: `directoryOperation`, `distributedOperation`, or `dSAOperation`.

* `objectClasses`

  Object class definitions identify the attribute types that an entry must have, and may have. Examples of object classes include `person` and `organizationalUnit`. Object classes inherit from other object classes. For example, `inetOrgPerson` inherits from `person`.

  Object classes are specified as values of an entry's `objectClass` attribute.

  An object class can be one of the following:

  * Structural object classes define the core structure of the entry, generally representing a real-world object.

    By default, DS directory entries have a single structural object class or at least a single line of structural object class inheritance.

    The `person` object class is structural, for example.

  * Auxiliary object classes define additional characteristics of entries.

    The `posixAccount` object class is auxiliary, for example.

  * Abstract object classes define base characteristics for other object classes to inherit, and cannot themselves inherit from other object classes.

    The `top` object class from which others inherit is abstract, for example.

* `ldapSyntaxes`

  An attribute syntax constrains what directory clients can store as attribute values.

* `matchingRules`

  A matching rule determines how the directory server compares attribute values to assertion values for LDAP search and LDAP compare operations.

  For example, in a search having the filter `(uid=bjensen)` the assertion value is `bjensen`.

* `nameForms`

  A name form specifies which attribute can be the relative distinguished name (RDN) *(tooltip: \<div class="paragraph">
  \<p>The initial portion of a DN distinguishing the entry from all others at the same level.\</p>
  \</div>)* for a structural object class.

* `dITStructureRules`

  A directory information tree (DIT) *(tooltip: \<div class="paragraph">
  \<p>A set of directory entries organized hierarchically in a tree structure.\</p>
  \</div>)* structure rule defines a relationship between directory entries by identifying the name form allowed for subordinate entries of a given superior entry.

### Object class schema

The schema entry in a server is large because it contains all of the schema definitions. Filter the results when reading a specific schema definition.

The example below reads the definition for the `person` object class:

```console
$ grep \'person\' <(ldapsearch \
 --hostname localhost \
 --port 1636 \
 --useSsl \
 --trustStorePath /path/to/opendj/config/keystore \
 --trustStoreType PKCS12 \
 --trustStorePassword:file /path/to/opendj/config/keystore.pin \
 --bindDN "uid=kvaughan,ou=people,dc=example,dc=com" \
 --bindPassword bribery \
 --baseDN "cn=schema" \
 --searchScope base \
 "(objectClass=subschema)" \
 objectClasses)
```

> **Collapse: Show output**
>
> ```
> objectClasses: ( 2.5.6.6 NAME 'person' SUP top STRUCTURAL MUST ( sn $ cn ) MAY ( userPassword $ telephoneNumber $ seeAlso $ description ) X-ORIGIN 'RFC 4519' X-SCHEMA-FILE '00-core.ldif' )
> ```

Notice the use of the object class name in `grep \'person\'` to filter search results.

The object class defines which attributes an entry of that object class *must* have, and which attributes the entry *may* optionally have. A `person` entry must have a `cn` and an `sn` attribute. A `person` entry may optionally have `userPassword`, `telephoneNumber`, `seeAlso`, and `description` attributes.

To determine the definitions of those attributes, read the LDAP schema:

### Attribute schema

The following example shows you how to read the schema definition for the `cn` attribute:

```console
$ grep \'cn\' <(ldapsearch \
 --hostname localhost \
 --port 1636 \
 --useSsl \
 --trustStorePath /path/to/opendj/config/keystore \
 --trustStoreType PKCS12 \
 --trustStorePassword:file /path/to/opendj/config/keystore.pin \
 --bindDN "uid=kvaughan,ou=people,dc=example,dc=com" \
 --bindPassword bribery \
 --baseDN "cn=schema" \
 --searchScope base \
 "(objectClass=subschema)" \
 attributeTypes)
```

> **Collapse: Show output**
>
> ```
> attributeTypes: ( 2.5.4.3 NAME ( 'cn' 'commonName' ) SUP name X-ORIGIN 'RFC 4519' X-SCHEMA-FILE '00-core.ldif' )
> ```

The `cn` attribute inherits its definition from the `name` attribute. That attribute definition indicates attribute syntax and matching rules as shown in the following example:

```console
$ grep \'name\' <(ldapsearch \
 --hostname localhost \
 --port 1636 \
 --useSsl \
 --trustStorePath /path/to/opendj/config/keystore \
 --trustStoreType PKCS12 \
 --trustStorePassword:file /path/to/opendj/config/keystore.pin \
 --bindDN "uid=kvaughan,ou=people,dc=example,dc=com" \
 --bindPassword bribery \
 --baseDN "cn=schema" \
 --searchScope base \
 "(objectClass=subschema)" \
 attributeTypes)
```

> **Collapse: Show output**
>
> ```
> attributeTypes: ( 2.5.4.41 NAME 'name' EQUALITY caseIgnoreMatch SUBSTR caseIgnoreSubstringsMatch SYNTAX 1.3.6.1.4.1.1466.115.121.1.15 X-ORIGIN 'RFC 4519' X-SCHEMA-FILE '00-core.ldif' )
> ```

This means that the server ignores case when matching a common name value. Use the OID to read the syntax as shown in the following example:

```console
$ grep 1.3.6.1.4.1.1466.115.121.1.15 <(ldapsearch \
 --hostname localhost \
 --port 1636 \
 --useSsl \
 --trustStorePath /path/to/opendj/config/keystore \
 --trustStoreType PKCS12 \
 --trustStorePassword:file /path/to/opendj/config/keystore.pin \
 --bindDN "uid=kvaughan,ou=people,dc=example,dc=com" \
 --bindPassword bribery \
 --baseDN "cn=schema" \
 --searchScope base \
 "(objectClass=subschema)" \
 ldapSyntaxes)
```

> **Collapse: Show output**
>
> ```
> ldapSyntaxes: ( 1.3.6.1.4.1.1466.115.121.1.15 DESC 'Directory String' X-ORIGIN 'RFC 4517' )
> ```

Taken together with the information for the `name` attribute, the common name attribute value is a Directory String of at most 32,768 characters. For details about syntaxes, read [RFC 4517, Lightweight Directory Access Protocol (LDAP): Syntaxes and Matching Rules](https://www.rfc-editor.org/info/rfc4517). That document describes a Directory String as one or more UTF-8 characters.

## Schema errors

For the sake of interoperability and to avoid polluting directory data, scripts and applications should respect LDAP schema. In the simplest case, scripts and applications can use the schemas already defined.

DS servers do accept updates to schema definitions over LDAP while the server is running. This means that when a new application calls for attributes that are not yet defined by existing directory schemas, the directory administrator can easily add them, as described in [Update LDAP schema](../config-guide/schema.html#update-schema), as long as the new definitions do not conflict with existing definitions.

General purpose applications handle many different types of data. Such applications must manage schema compliance at run time. Software development kits provide mechanisms for reading schema definitions at run time, and checking whether entry data is valid according to the schema definitions.

Many scripts do not require run time schema checking. When schema checking is not required, it is sufficient to check schema-related LDAP result codes when writing to the directory:

* LDAP result code: 17 (Undefined attribute type)

  The requested operation failed because it referenced an attribute that is not defined in the server schema.

* LDAP result code: 18 (Inappropriate matching)

  The requested operation failed because it attempted to perform an inappropriate type of matching against an attribute.

* LDAP result code: 20 (Attribute or value exists)

  The requested operation failed because it would have resulted in a conflict with an existing attribute or attribute value in the target entry.

  For example, the request tried to add a second value to a single-valued attribute.

* LDAP result code: 21 (Invalid attribute syntax)

  The requested operation failed because it violated the syntax for a specified attribute.

* LDAP result code: 34 (Invalid DN syntax)

  The requested operation failed because it would have resulted in an entry with an invalid or malformed DN.

* LDAP result code: 64 (Naming violation)

  The requested operation failed because it would have violated the server's naming configuration.

  For example, the request did not respect a name form definition.

* LDAP result code: 65 (Object class violation)

  The requested operation failed because it would have resulted in an entry that violated the server schema.

  For example, the request tried to remove a required attribute, or tried to add an attribute that is not allowed.

* LDAP result code: 69 (Object class mods prohibited)

  The requested operation failed because it would have modified the object classes associated with an entry in an illegal manner.

When you encounter an error, take the time to read the additional information. The additional information from a server is often sufficient to allow you to resolve the problem directly.

[Object class violations](#example-object-class-violations), and [Invalid attribute syntax](#example-invalid-attribute-syntax) show some common problems that can result from schema violations.

### Object class violations

A number of schema violations show up as object class violations. The following request fails to add an `undefined` attribute:

```console
$ ldapmodify \
 --hostname localhost \
 --port 1636 \
 --useSsl \
 --trustStorePath /path/to/opendj/config/keystore \
 --trustStoreType PKCS12 \
 --trustStorePassword:file /path/to/opendj/config/keystore.pin \
 --bindDN "uid=kvaughan,ou=people,dc=example,dc=com" \
 --bindPassword bribery << EOF
dn: uid=bjensen,ou=People,dc=example,dc=com
changetype: modify
add: undefined
undefined: This attribute is not defined.
EOF
```

> **Collapse: Show output**
>
> ```
> # The LDAP modify request failed: 65 (Object Class Violation)
> # Additional Information:  Entry uid=bjensen,ou=People,dc=example,dc=com cannot be modified because the resulting entry would have violated the server schema: Entry "uid=bjensen,ou=People,dc=example,dc=com" violates the schema because it contains attribute "undefined" which is not allowed by any of the object classes in the entry
> ```

The solution is to define the `undefined` attribute, and to ensure that it is allowed by one of the object classes defined for the entry.

The following request fails to add a second structural object class:

```console
$ ldapmodify \
 --hostname localhost \
 --port 1636 \
 --useSsl \
 --trustStorePath /path/to/opendj/config/keystore \
 --trustStoreType PKCS12 \
 --trustStorePassword:file /path/to/opendj/config/keystore.pin \
 --bindDN "uid=kvaughan,ou=people,dc=example,dc=com" \
 --bindPassword bribery << EOF
dn: uid=bjensen,ou=People,dc=example,dc=com
changetype: modify
add: objectClass
objectClass: organizationalUnit
EOF
```

> **Collapse: Show output**
>
> ```
> # The LDAP modify request failed: 65 (Object Class Violation)
> # Additional Information:  Entry uid=bjensen,ou=People,dc=example,dc=com cannot be modified because the resulting entry would have violated the server schema: Entry "uid=bjensen,ou=People,dc=example,dc=com" violates the schema because it contains multiple conflicting structural object classes "inetOrgPerson" and "organizationalUnit". Only a single structural object class is allowed in an entry
> ```

The solution in this case is to define only one structural object class for the entry. Either Babs Jensen is a person or an organizational unit, but not both.

### Invalid attribute syntax

The following request fails to add an empty string as a common name attribute value:

```console
$ ldapmodify \
 --hostname localhost \
 --port 1636 \
 --useSsl \
 --trustStorePath /path/to/opendj/config/keystore \
 --trustStoreType PKCS12 \
 --trustStorePassword:file /path/to/opendj/config/keystore.pin \
 --bindDN "uid=kvaughan,ou=people,dc=example,dc=com" \
 --bindPassword bribery << EOF
dn: uid=bjensen,ou=People,dc=example,dc=com
changetype: modify
add: cn
cn:
EOF
```

> **Collapse: Show output**
>
> ```
> # The LDAP modify request failed: 21 (Invalid Attribute Syntax)
> # Additional Information:  When attempting to modify entry uid=bjensen,ou=People,dc=example,dc=com to add one or more values for attribute cn, value "" was found to be invalid according to the associated syntax: The operation attempted to assign a zero-length value to an attribute with the directory string syntax
> ```

As mentioned in [Attribute schema](#example-reading-attribute-definitions), a Directory String has one or more UTF-8 characters.

## Workarounds

Follow the suggestions in [Schema errors](#respecting-schema) as much as possible. In particular, follow these rules of thumb:

* Test with a private DS server to resolve schema issues before going live.

* Adapt your scripts and applications to avoid violating schema definitions.

* When existing schemas are not sufficient, request schema updates to add definitions that do not conflict with any already in use.

When it is not possible to respect the schema definitions, you can sometimes work around LDAP schema constraints without changing the server configuration. The schema defines an `extensibleObject` object class. The `extensibleObject` object class is auxiliary. It effectively allows entries to hold any user attribute, even attributes that are not defined in the schema.

### ExtensibleObject

The following example adds one attribute that is undefined and another that is not allowed:

```console
$ ldapmodify \
 --hostname localhost \
 --port 1636 \
 --useSsl \
 --trustStorePath /path/to/opendj/config/keystore \
 --trustStoreType PKCS12 \
 --trustStorePassword:file /path/to/opendj/config/keystore.pin \
 --bindDN "uid=kvaughan,ou=people,dc=example,dc=com" \
 --bindPassword bribery << EOF
dn: uid=bjensen,ou=People,dc=example,dc=com
changetype: modify
add: objectClass
objectClass: extensibleObject
-
add: undefined
undefined: This attribute is not defined in the LDAP schema.
-
add: serialNumber
serialNumber: This attribute is not allowed according to the object classes.
EOF
```

> **Collapse: Show output**
>
> ```
> # MODIFY operation successful for DN uid=bjensen,ou=People,dc=example,dc=com
> ```

Use of the `extensibleObject` object class can be abused and can prevent interoperability. Restrict its use to cases where no better alternative is available.

---

---
title: LDAP search
description: Search PingDS directories using LDAP filters, substring and extensible matches, JSON query filters, server-side sort, and DN patterns.
component: pingds
version: 8.1
page_id: pingds:ldap-guide:search-ldap
canonical_url: https://docs.pingidentity.com/pingds/8.1/ldap-guide/search-ldap.html
llms_txt: https://docs.pingidentity.com/pingds/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2025-10-22T14:42:39Z
keywords: ["LDAP"]
section_ids:
  simple-filter-search: Simple LDAP filter
  complex-filter-search: Complex LDAP filter
  substring-seaches: Substring searches
  operational-attrs-search: Return operational attributes
  attr-desc-list-search: Return attributes of an object class
  approximate-match-search: Approximate match
  escape-characters-in-filter: Escape characters in filters
  root-dse-search: Read directory capabilities
  extensible-match-search: Active accounts
  localized-search: Language subtypes
  filter-operators: LDAP filter operators
  json-search: JSON query filters
  json-token-search: JSON assertions
  server-side-sort: Server-side sort
  dn-pattern-matching: DN patterns
---

# LDAP search

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Examples in this documentation depend on features activated in [the `ds-evaluation` setup profile](../install-guide/setup-ds.html#about-ds-evaluation).The code samples demonstrate how to contact the server over HTTPS using the deployment CA certificate. Before trying the samples, generate the CA certificate in PEM format from the server deployment ID and password:```console
$ dskeymgr \
 export-ca-cert \
 --deploymentId $DEPLOYMENT_ID \
 --deploymentIdPassword password \
 --outputFile ca-cert.pem
``` |

Searching the directory is like searching for a phone number in a paper phone book. You can look up a phone number because you know the last name of a subscriber's entry. In other words, you use the value of one attribute of the entry to find entries that have another attribute you want.

Whereas a phone book has only one index (alphabetical order by name), the directory has many indexes. When performing a search, you specify which attributes to use, and the server derives the corresponding indexes.

The phone book might be divided into white pages for residential subscribers and yellow pages for businesses. If you look up an individual's phone number, you limit your search to the white pages. Directory services divide entries in various ways. For example, they can store organizations and groups in different locations from user entries or printer accounts. When searching the directory, you therefore also specify where to search.

The `ldapsearch` command requires arguments for at least the search base DN option and an LDAP filter. The search base DN identifies where in the directory to search for entries that match the filter. For example, if you are looking for printers, you might use `ou=Printers,dc=example,dc=com`. In the `GNB00` office, you could look up a printer as shown in the following example:

```console
$ ldapsearch --baseDN ou=Printers,dc=example,dc=com "(printerLocation=GNB00)"
```

In the example above, the LDAP filter matches printer entries where the `printerLocation` attribute is equal to `GNB00`.

You also specify the host and port to access directory services, and the protocol to use, such as LDAP or LDAPS. If the directory service does not allow anonymous access to the data you want to search, you supply credentials, such as a username and password, or a public key certificate. You can optionally specify a list of attributes to return. If you do not specify attributes, then the search returns all user attributes for the entry.

For details about the operators that can be used in search filters, refer to [LDAP filter operators](#filter-operators).

## Simple LDAP filter

The following example searches for entries with user IDs (`sn`) equal to `hall`, returning only DNs and user ID values:

```console
$ ldapsearch \
 --hostname localhost \
 --port 1636 \
 --useSsl \
 --trustStorePath /path/to/opendj/config/keystore \
 --trustStoreType PKCS12 \
 --trustStorePassword:file /path/to/opendj/config/keystore.pin \
 --bindDN uid=kvaughan,ou=People,dc=example,dc=com \
 --bindPassword bribery \
 --baseDN dc=example,dc=com \
 "(sn=hall)" \
 uid
```

> **Collapse: Show output**
>
> ```
> dn: uid=ahall,ou=People,dc=example,dc=com
> uid: ahall
>
> dn: uid=bhal2,ou=People,dc=example,dc=com
> uid: bhal2
>
> dn: uid=bhall,ou=People,dc=example,dc=com
> uid: bhall
> ```

## Complex LDAP filter

The following example returns entries with `sn` equal to `jensen` for users located in San Francisco:

```console
$ ldapsearch \
 --hostname localhost \
 --port 1636 \
 --useSsl \
 --trustStorePath /path/to/opendj/config/keystore \
 --trustStoreType PKCS12 \
 --trustStorePassword:file /path/to/opendj/config/keystore.pin \
 --bindDN uid=kvaughan,ou=People,dc=example,dc=com \
 --bindPassword bribery \
 --baseDN ou=people,dc=example,dc=com \
 "(&(sn=jensen)(l=San Francisco))" \
 @person
```

> **Collapse: Show output**
>
> ```
> dn: uid=bjensen,ou=People,dc=example,dc=com
> objectClass: person
> objectClass: cos
> objectClass: oauth2TokenObject
> objectClass: inetOrgPerson
> objectClass: organizationalPerson
> objectClass: posixAccount
> objectClass: top
> cn: Barbara Jensen
> cn: Babs Jensen
> description: Original description
> sn: Jensen
> telephoneNumber: +1 408 555 1862
>
> dn: uid=rjensen,ou=People,dc=example,dc=com
> objectClass: person
> objectClass: cos
> objectClass: inetOrgPerson
> objectClass: organizationalPerson
> objectClass: posixAccount
> objectClass: top
> cn: Richard Jensen
> description: Description on ou=People
> sn: Jensen
> telephoneNumber: +1 408 555 5957
> ```

The command returns the attributes associated with the `person` object class.

Complex filters can use both "and" syntax, `(&(filtercomp)(filtercomp))`, and "or" syntax, `(|(filtercomp)(filtercomp))`.

## Substring searches

Sometimes you only have part of the value that the search must match. Use a *substring search* in this case.

The following example returns entries with phone numbers that contain `5551212`:

```console
$ ldapsearch \
 --hostname localhost \
 --port 1636 \
 --useSsl \
 --trustStorePath /path/to/opendj/config/keystore \
 --trustStoreType PKCS12 \
 --trustStorePassword:file /path/to/opendj/config/keystore.pin \
 --bindDN uid=kvaughan,ou=People,dc=example,dc=com \
 --bindPassword bribery \
 --baseDN ou=people,dc=example,dc=com \
 "(telephoneNumber=*5551212*)"
```

The following example returns entries where the full name (common name) starts with `Barb`:

```console
$ ldapsearch \
 --hostname localhost \
 --port 1636 \
 --useSsl \
 --trustStorePath /path/to/opendj/config/keystore \
 --trustStoreType PKCS12 \
 --trustStorePassword:file /path/to/opendj/config/keystore.pin \
 --bindDN uid=kvaughan,ou=People,dc=example,dc=com \
 --bindPassword bribery \
 --baseDN ou=people,dc=example,dc=com \
 "(cn=barb*)"
```

The filter has `barb` in lower case because the `cn` attribute is case-insensitive. Many standard LDAP attributes are case-insensitive.

The following example returns entries where the full name ends with `ensen`:

```console
$ ldapsearch \
 --hostname localhost \
 --port 1636 \
 --useSsl \
 --trustStorePath /path/to/opendj/config/keystore \
 --trustStoreType PKCS12 \
 --trustStorePassword:file /path/to/opendj/config/keystore.pin \
 --bindDN uid=kvaughan,ou=People,dc=example,dc=com \
 --bindPassword bribery \
 --baseDN ou=people,dc=example,dc=com \
 "(sn=*ensen)"
```

|   |                                                                                                                                                                                               |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | If you had the whole last name, such as `Jensen`, then you would use `(sn=jensen)` as the search filter. Substring searches are useful, but they are also more expensive than exact searches. |

## Return operational attributes

Operational attributes are returned only when explicitly requested. Use `+` in the attribute list after the filter to return all operational attributes:

```console
$ ldapsearch \
 --hostname localhost \
 --port 1636 \
 --useSsl \
 --trustStorePath /path/to/opendj/config/keystore \
 --trustStoreType PKCS12 \
 --trustStorePassword:file /path/to/opendj/config/keystore.pin \
 --bindDN uid=kvaughan,ou=People,dc=example,dc=com \
 --bindPassword bribery \
 --baseDN dc=example,dc=com \
 "(uid=bjensen)" \
 +
```

> **Collapse: Show output**
>
> ```
> dn: uid=bjensen,ou=People,dc=example,dc=com
> collectiveAttributeSubentries: cn=Bronze Class of Service,dc=example,dc=com
> collectiveAttributeSubentries: cn=Inherit Department Number From Manager,dc=example,dc=com
> collectiveAttributeSubentries: cn=Inherit From Locality,dc=example,dc=com
> collectiveAttributeSubentries: cn=Inherit Description From Parent,dc=example,dc=com
> ds-pwp-state-json: { "require-secure-authentication": true, "password-policy-dn": "cn=Default Password Policy,cn=Password Policies,cn=config", "force-change-on-reset": false, "account-is-expired": false, "account-is-idle-locked": false, "account-is-disabled": false, "account-is-reset-locked": false, "must-change-password": false, "password-is-expired": false, "is-within-minimum-password-age": false, "account-is-usable": true, "require-secure-password-changes": true, "force-change-on-add": false }
> entryDN: uid=bjensen,ou=People,dc=example,dc=com
> entryUUID: <uuid>
> etag: <etag>
> hasSubordinates: false
> isMemberOf: cn=Carpoolers,ou=Self Service,ou=Groups,dc=example,dc=com
> numSubordinates: 0
> pwdPolicySubentry: cn=Default Password Policy,cn=Password Policies,cn=config
> structuralObjectClass: inetOrgPerson
> subschemaSubentry: cn=schema
> ```

Alternatively, specify operational attributes by name.

## Return attributes of an object class

Use `@objectClass` in the attribute list to return all attributes of a particular object class:

```console
$ ldapsearch \
 --hostname localhost \
 --port 1636 \
 --useSsl \
 --trustStorePath /path/to/opendj/config/keystore \
 --trustStoreType PKCS12 \
 --trustStorePassword:file /path/to/opendj/config/keystore.pin \
 --bindDN uid=kvaughan,ou=People,dc=example,dc=com \
 --bindPassword bribery \
 --baseDN dc=example,dc=com \
 "(uid=bjensen)" \
  @person
```

> **Collapse: Show output**
>
> ```
> dn: uid=bjensen,ou=People,dc=example,dc=com
> objectClass: person
> objectClass: cos
> objectClass: oauth2TokenObject
> objectClass: inetOrgPerson
> objectClass: organizationalPerson
> objectClass: posixAccount
> objectClass: top
> cn: Barbara Jensen
> cn: Babs Jensen
> description: Original description
> sn: Jensen
> telephoneNumber: +1 408 555 1862
> ```

## Approximate match

DS servers support searches for an approximate match of the filter. Approximate match searches use the `~=` comparison operator, described in [LDAP filter operators](#filter-operators). They rely on `approximate` type indexes, which are configured as shown in [Approximate index](../config-guide/idx-config.html#approx-index-example).

The following example configures an approximate match index for the surname (`sn`) attribute, and then rebuilds the index:

```console
$ dsconfig \
 set-backend-index-prop \
 --hostname localhost \
 --port 4444 \
 --bindDN uid=admin \
 --bindPassword password \
 --backend-name dsEvaluation \
 --index-name sn \
 --set index-type:approximate \
 --trustStorePath /path/to/opendj/config/keystore \
 --trustStoreType PKCS12 \
 --trustStorePassword:file /path/to/opendj/config/keystore.pin \
 --no-prompt
$ rebuild-index \
 --hostname localhost \
 --port 4444 \
 --bindDN uid=admin \
 --bindPassword password \
 --trustStorePath /path/to/opendj/config/keystore \
 --trustStoreType PKCS12 \
 --trustStorePassword:file /path/to/opendj/config/keystore.pin \
 --baseDN dc=example,dc=com \
 --index sn
```

Once the index is built, it is ready for use in searches. The following example shows a search using the approximate comparison operator:

```console
$ ldapsearch \
 --hostname localhost \
 --port 1636 \
 --useSsl \
 --trustStorePath /path/to/opendj/config/keystore \
 --trustStoreType PKCS12 \
 --trustStorePassword:file /path/to/opendj/config/keystore.pin \
 --bindDN uid=kvaughan,ou=People,dc=example,dc=com \
 --bindPassword bribery \
 --baseDN dc=example,dc=com \
 "(sn~=jansen)" \
 sn
```

> **Collapse: Show output**
>
> ```
> dn: uid=ajensen,ou=People,dc=example,dc=com
> sn: Jensen
>
> dn: uid=bjense2,ou=People,dc=example,dc=com
> sn: Jensen
>
> dn: uid=bjensen,ou=People,dc=example,dc=com
> sn: Jensen
>
> dn: uid=ejohnson,ou=People,dc=example,dc=com
> sn: Johnson
>
> dn: uid=gjensen,ou=People,dc=example,dc=com
> sn: Jensen
>
> dn: uid=jjensen,ou=People,dc=example,dc=com
> sn: Jensen
>
> dn: uid=kjensen,ou=People,dc=example,dc=com
> sn: Jensen
>
> dn: uid=rjense2,ou=People,dc=example,dc=com
> sn: Jensen
>
> dn: uid=rjensen,ou=People,dc=example,dc=com
> sn: Jensen
>
> dn: uid=tjensen,ou=People,dc=example,dc=com
> sn: Jensen
> ```

Notice that `jansen` matches `Jensen` and `Johnson`.

## Escape characters in filters

[RFC 4515](https://www.rfc-editor.org/info/rfc4515), *Lightweight Directory Access Protocol (LDAP): String Representation of Search Filters*, mentions a number of characters that require special handing in search filters.

For a filter like `(attr=value)`, the following list indicates characters that you must replace with a backslash (`\`) followed by two hexadecimal digits when using them as part of the value string:

* Replace `*` with `\2a`.

* Replace `(` with `\28`.

* Replace `)` with `\29`.

* Replace `\` with `\5c`.

* Replace NUL (0x00) with `\00`.

The following example shows a filter with escaped characters matching an actual value:

```console
$ ldapsearch \
 --hostname localhost \
 --port 1636 \
 --useSsl \
 --trustStorePath /path/to/opendj/config/keystore \
 --trustStoreType PKCS12 \
 --trustStorePassword:file /path/to/opendj/config/keystore.pin \
 --bindDN uid=kvaughan,ou=People,dc=example,dc=com \
 --bindPassword bribery \
 --baseDN dc=example,dc=com \
 "(cn=\28A \5cgreat\5c name\2a\29)" \
 cn
```

> **Collapse: Show output**
>
> ```
> dn: uid=bjensen,ou=People,dc=example,dc=com
> cn: Barbara Jensen
> cn: Babs Jensen
> cn: (A \great\ name*)
> ```

## Read directory capabilities

The root DSE is a single entry describing server capabilities in operational attributes.

Use `ldapsearch --baseDn "" --searchScope base "(&)" +` to read the operational attributes of the root DSE:

```console
$ ldapsearch \
 --hostname localhost \
 --port 1636 \
 --useSsl \
 --usePkcs12TrustStore /path/to/opendj/config/keystore \
 --trustStorePassword:file /path/to/opendj/config/keystore.pin \
 --baseDN "" \
 --searchScope base \
 "(&)" \
 +
```

## Active accounts

DS servers support extensible matching rules. Use a filter that specifies a matching rule OID that extends the matching operator.

DS servers support time-based matching rules for use with attributes that hold timestamp values:

* Name: `relativeTimeOrderingMatch.gt`

  Greater-than relative time matching rule for time-based searches.

  Use this in a filter to match attributes with values greater than the current time +/- an offset.

  The filter `(pwdExpirationTime:1.3.6.1.4.1.26027.1.4.5:=5d)` matches entries where the password expiration time is greater than the current time plus five days. In other words, entries whose passwords expire in more than five days.

* Name: `relativeTimeOrderingMatch.lt`

  Less-than relative time matching rule for time-based searches.

  Use this in a filter to match attributes with values less than the current time +/- an offset.

  The filter `(ds-last-login-time:1.3.6.1.4.1.26027.1.4.6:=-4w)` matches entries where the last login time is less than the current time minus four weeks. In other words, accounts that have not been active in the last four weeks.

* Name: `partialDateAndTimeMatchingRule`

  Partial date and time matching rule for matching parts of dates in time-based searches.

  The filter `(ds-last-login-time:1.3.6.1.4.1.26027.1.4.7:=2020)` matches entries where the last login time was in 2020.

The following example uses the `ds-last-login-time` attribute, which is an operational attribute (`USAGE directoryOperation`) with [Generalized Time](../schemaref/s-GeneralizedTime.html) syntax (`SYNTAX 1.3.6.1.4.1.1466.115.121.1.24`).

When checking schema compliance, the server skips operational attributes. The server can therefore add operational attributes to an entry without changing the entry's object classes.

Operational attributes hold information for the directory, rather than information targeting client applications. The server returns operational attributes only when explicitly requested, and client applications generally should not be able to modify them.

As the `ds-last-login-time` attribute is operational, it has limited visibility. This helps prevent client applications from modifying its value unless specifically allowed to.

Configure the applicable password policy to write the last login timestamp when a user authenticates.

The following command configures a subentry password policy. On successful authentication, the policy causes the server to write a timestamp in generalized time format to the user's `ds-last-login-time` operational attribute:

```console
$ ldapmodify \
 --hostname localhost \
 --port 1636 \
 --useSsl \
 --trustStorePath /path/to/opendj/config/keystore \
 --trustStoreType PKCS12 \
 --trustStorePassword:file /path/to/opendj/config/keystore.pin \
 --bindDN uid=admin \
 --bindPassword password << EOF
dn: cn=Record last login,dc=example,dc=com
objectClass: top
objectClass: subentry
objectClass: ds-pwp-password-policy
cn: Record last login
ds-pwp-password-attribute: userPassword
ds-pwp-default-password-storage-scheme: PBKDF2-HMAC-SHA256
ds-pwp-last-login-time-attribute: ds-last-login-time
ds-pwp-last-login-time-format: yyyyMMddHH'Z'
subtreeSpecification: { base "ou=people" }
EOF
```

The `ds-pwp-last-login-time-format` setting must:

* Match the syntax of the `ds-pwp-last-login-time-attribute` attribute, which in this example is `GeneralizedTime`.

* Be a valid format string for the `java.text.SimpleDateFormat` class.

With the setting shown in the example, `ds-pwp-last-login-time-format: yyyyMMddHH'Z'`, DS records last login time to the nearest hour. For each bind where the timestamp changes, DS updates the timestamp on the entry. So this recommended setting avoids updating entries often for users who bind repeatedly over a short period. If the deployment requires a fine-grained last login timestamp, use a format that includes minutes or seconds. For example, to get last login times that are accurate to the second, use `ds-pwp-last-login-time-format:"yyyyMMddHHmmss'Z'"`.

Configure and build an index for time-based searches on the `ds-last-login-time` attribute:

```console
$ dsconfig \
 create-backend-index \
 --hostname localhost \
 --port 4444 \
 --bindDN uid=admin \
 --bindPassword password \
 --backend-name dsEvaluation \
 --set index-type:extensible \
 --set index-extensible-matching-rule:1.3.6.1.4.1.26027.1.4.5 \
 --set index-extensible-matching-rule:1.3.6.1.4.1.26027.1.4.6 \
 --set index-extensible-matching-rule:1.3.6.1.4.1.26027.1.4.7 \
 --index-name ds-last-login-time \
 --trustStorePath /path/to/opendj/config/keystore \
 --trustStoreType PKCS12 \
 --trustStorePassword:file /path/to/opendj/config/keystore.pin \
 --no-prompt
$ rebuild-index \
 --hostname localhost \
 --port 4444 \
 --bindDN uid=admin \
 --bindPassword password \
 --trustStorePath /path/to/opendj/config/keystore \
 --trustStoreType PKCS12 \
 --trustStorePassword:file /path/to/opendj/config/keystore.pin \
 --baseDN dc=example,dc=com \
 --index ds-last-login-time
```

Make sure you have some users who have authenticated recently:

```console
$ ldapsearch \
 --hostname localhost \
 --port 1636 \
 --useSsl \
 --trustStorePath /path/to/opendj/config/keystore \
 --trustStoreType PKCS12 \
 --trustStorePassword:file /path/to/opendj/config/keystore.pin \
 --bindDN uid=bjensen,ou=people,dc=example,dc=com \
 --bindPassword hifalutin \
 --baseDN dc=example,dc=com \
 "(uid=bjensen)" \
 1.1
$ ldapsearch \
 --hostname localhost \
 --port 1636 \
 --useSsl \
 --trustStorePath /path/to/opendj/config/keystore \
 --trustStoreType PKCS12 \
 --trustStorePassword:file /path/to/opendj/config/keystore.pin \
 --bindDN uid=kvaughan,ou=people,dc=example,dc=com \
 --bindPassword bribery \
 --baseDN dc=example,dc=com \
 "(uid=bjensen)" \
 1.1
```

The following search returns users who have authenticated in the last 13 weeks:

```console
$ ldapsearch \
 --hostname localhost \
 --port 1636 \
 --useSsl \
 --trustStorePath /path/to/opendj/config/keystore \
 --trustStoreType PKCS12 \
 --trustStorePassword:file /path/to/opendj/config/keystore.pin \
 --bindDN uid=admin \
 --bindPassword password \
 --baseDN dc=example,dc=com \
 "(ds-last-login-time:1.3.6.1.4.1.26027.1.4.5:=-13w)" \
 1.1
```

> **Collapse: Show output**
>
> ```
> dn: uid=bjensen,ou=People,dc=example,dc=com
>
> dn: uid=kvaughan,ou=People,dc=example,dc=com
> ```

The following search returns users who have authenticated this year:

```console
$ ldapsearch \
 --hostname localhost \
 --port 1636 \
 --useSsl \
 --trustStorePath /path/to/opendj/config/keystore \
 --trustStoreType PKCS12 \
 --trustStorePassword:file /path/to/opendj/config/keystore.pin \
 --bindDN uid=admin \
 --bindPassword password \
 --baseDN dc=example,dc=com \
 "(ds-last-login-time:1.3.6.1.4.1.26027.1.4.7:=$(date +%Y))" \
 1.1
```

> **Collapse: Show output**
>
> ```
> dn: uid=bjensen,ou=People,dc=example,dc=com
>
> dn: uid=kvaughan,ou=People,dc=example,dc=com
> ```

## Language subtypes

DS servers support the language subtypes listed in [Support for languages and locales](../ldap-reference/l10n.html).

When you perform a search you can request the language subtype by OID or by language subtype string. For example, the following search gets the French version of a common name. The example uses the DS `base64` command to decode the attribute value:

```console
$ ldapsearch \
 --hostname localhost \
 --port 1636 \
 --useSsl \
 --trustStorePath /path/to/opendj/config/keystore \
 --trustStoreType PKCS12 \
 --trustStorePassword:file /path/to/opendj/config/keystore.pin \
 --bindDN uid=kvaughan,ou=People,dc=example,dc=com \
 --bindPassword bribery \
 --baseDN dc=example,dc=com \
 "(cn=Frederique Dupont)" cn\;lang-fr
```

> **Collapse: Show output**
>
> ```
> dn: uid=fdupont,ou=People,dc=example,dc=com
> cn;lang-fr:: RnJlZMOpcmlxdWUgRHVwb250
> ```

```console
$ base64 decode --encodedData RnJlZMOpcmlxdWUgRHVwb250
```

> **Collapse: Show output**
>
> ```
> Fredérique Dupont
> ```

At the end of the OID or language subtype, further specify the matching rule as follows:

* Add `.1` for less than

* Add `.2` for less than or equal to

* Add `.3` for equal to (default)

* Add `.4` for greater than or equal to

* Add `.5` for greater than

* Add `.6` for substring

## LDAP filter operators

| Operator        | Definition                                                                                                                                                                                                                                                                                                                | Example                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| --------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `=`             | Equality comparison, as in `(sn=Jensen)`.This can also be used with substring matches. For example, to match last names starting with `Jen`, use the filter `(sn=Jen*)`. Substrings are more expensive for the directory server to index. Substring searches might not be permitted, depending on the attribute.          | `"(cn=My App)"` matches entries with common name `My App`.`"(sn=Jen*)"` matches entries with surname starting with `Jen`.                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| `<=`            | Less than or equal to comparison, which works alphanumerically.                                                                                                                                                                                                                                                           | `"(cn<=App)"` matches entries with `commonName` up to those starting with App (case-insensitive) in alphabetical order.                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| `>=`            | Greater than or equal to comparison, which works alphanumerically.                                                                                                                                                                                                                                                        | `"(uidNumber>=1151)"` matches entries with `uidNumber` greater than 1151.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| `=*`            | Presence comparison. For example, to match all entries with a `userPassword` attribute, use the filter `(userPassword=*)`.                                                                                                                                                                                                | `"(member=*)"` matches entries with a `member` attribute.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| `~=`            | Approximate comparison, matching attribute values similar to the value you specify.                                                                                                                                                                                                                                       | `"(sn~=jansen)"` matches entries with a surname that sounds similar to `Jansen` (Johnson, Jensen, and other surnames).                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| `[:dn][:oid]:=` | Extensible match comparison.At the end of the OID or language subtype, you further specify the matching rule as follows:- Add `.1` for less than

- Add `.2` for less than or equal to

- Add `.3` for equal to (default)

- Add `.4` for greater than or equal to

- Add `.5` for greater than

- Add `.6` for substring | `(uid:dn:=bjensen)` matches entries with DN component `uid=bjensen`.`(ds-last-login-time: 1.3.6.1.4.1.26027.1.4.5:=-13w)` matches entries with a last login time more recent than 13 weeks.Extensible match filters work with localized values. DS servers support internationalized locales, each of which has an OID for collation order, such as `1.3.6.1.4.1.42.2.27.9.4.76.1` for French. DS software lets you use the language subtype, such as `fr`, instead of the OID.`"(cn:dn:=My App)"` matches entries with `cn: My App` and DN component `cn=My App`. |
| `!`             | NOT operator, to find entries that do not match the specified filter component.Take care to limit your search when using `!` to avoid matching so many entries that the server treats your search as unindexed.                                                                                                           | `'!(objectclass=person)'` matches non-person entries.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| `&`             | AND operator, to find entries that match all specified filter components.                                                                                                                                                                                                                                                 | `'(&(l=San Francisco)(!(uid=bjensen)))'` matches entries for users in San Francisco other than the user with ID `bjensen`.                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| `\|`            | OR operator, to find entries that match one of the specified filter components.                                                                                                                                                                                                                                           | `"\|(sn=Jensen)(sn=Johnson)"` matches entries with surname Jensen or surname Johnson.                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |

## JSON query filters

DS servers support attribute values that have JSON syntax. This makes it possible to index JSON values, and to search for them using Common REST query filters, as described in [HDAP API reference](../rest-guide/rest-operations.html).

The following examples depend on settings applied with the `ds-evaluation` setup profile.

The first example uses a custom JSON query index for an `oauth2Token` JSON attribute. The index lets you search with Common REST query filters. The search finds the entry with `"access_token": "123"`:

```console
$ ldapsearch \
 --hostname localhost \
 --port 1636 \
 --useSsl \
 --trustStorePath /path/to/opendj/config/keystore \
 --trustStoreType PKCS12 \
 --trustStorePassword:file /path/to/opendj/config/keystore.pin \
 --bindDN uid=kvaughan,ou=People,dc=example,dc=com \
 --bindPassword bribery \
 --baseDN dc=example,dc=com \
 "(oauth2Token=access_token eq '123')" \
 oauth2Token
```

> **Collapse: Show output**
>
> ```
> dn: uid=bjensen,ou=People,dc=example,dc=com
> oauth2Token: {"access_token":"123","expires_in":59,"token_type":"Bearer","refresh_token":"456"}
> ```

You can combine Common REST query filter syntax filters with other LDAP search filter to form complex filters, as demonstrated in [Complex LDAP filter](#complex-filter-search). For example, `(&(oauth2Token=access_token eq '123')(mail=bjensen@example.com))`.

The next example relies on a default JSON query index for equality, part of the `ds-evaluation` setup profile. The index applies to a `json` attribute that holds arbitrary JSON objects. The search finds an entry with a `json` attribute that has an "array" field containing an array of objects:

```console
$ ldapsearch \
 --hostname localhost \
 --port 1636 \
 --useSsl \
 --trustStorePath /path/to/opendj/config/keystore \
 --trustStoreType PKCS12 \
 --trustStorePassword:file /path/to/opendj/config/keystore.pin \
 --bindDN uid=kvaughan,ou=People,dc=example,dc=com \
 --bindPassword bribery \
 --baseDN dc=example,dc=com \
 "(json=array[x eq 1 and y eq 2])" \
 json
```

> **Collapse: Show output**
>
> ```
> dn: uid=abarnes,ou=People,dc=example,dc=com
> json: {"array":[{"x":1,"y":2},{"x":3,"y":4}]}
> ```

Notice the value of the `json` attribute: `{"array":[{"x":1,"y":2},{"x":3,"y":4}]}`:

* The filter `"(json=array[x eq 1 and y eq 2])"` matches because it matches the first object of the array.

* The filter `"(array[x eq 1] and array[y eq 4])"` matches because it matches both objects in the array.

* The filter `"(json=array[x eq 1 and y eq 4])"` fails to match, because the array has no object `{"x":1,"y":4}`.

## JSON assertions

In addition to searches with query filters, JSON attributes can be matched with filters using JSON in the assertion. This example demonstrates a case where JSON objects are considered equal if their "id" fields match. This example depends on settings applied with the `ds-evaluation` setup profile.

Search for entries with a `jsonToken` attribute:

```console
$ ldapsearch \
 --hostname localhost \
 --port 1636 \
 --useSsl \
 --trustStorePath /path/to/opendj/config/keystore \
 --trustStoreType PKCS12 \
 --trustStorePassword:file /path/to/opendj/config/keystore.pin \
 --bindDN uid=kvaughan,ou=People,dc=example,dc=com \
 --bindPassword bribery \
 --baseDN dc=example,dc=com \
 '(jsonToken={"id":"HgAaB6xDhLom4JbM"})' \
 jsonToken
```

> **Collapse: Show output**
>
> ```
> jsonToken: {"id":"HgAaB6xDhLom4JbM","scopes":["read","write"],"expires":"2018-01-10T10:08:34Z"}
> ```

## Server-side sort

If permitted by the directory administrator, you can request that the server sort the search results. When your application requests a server-side sort, the server retrieves the entries matching your search, and then returns the whole set of entries in sorted order.

The following example grants access to use the server-side sort control:

> **Collapse: Show example**
>
> ```console
> $ ldapmodify \
>  --hostname localhost \
>  --port 1636 \
>  --useSsl \
>  --trustStorePath /path/to/opendj/config/keystore \
>  --trustStoreType PKCS12 \
>  --trustStorePassword:file /path/to/opendj/config/keystore.pin \
>  --bindDn uid=admin \
>  --bindPassword password << EOF
> dn: dc=example,dc=com
> changetype: modify
> add: aci
> aci: (targetcontrol = "ServerSideSort")
>  (version 3.0;acl "Allow Server-Side Sort for Kirsten Vaughan";
>  allow (read)(userdn = "ldap:///uid=kvaughan,ou=People,dc=example,dc=com");)
> EOF
> ```

This process consumes memory resources on the server, so the best practice is to sort results on the client side, or to browse results with a search that matches a virtual list view index, as demonstrated in [Virtual list view index](../config-guide/idx-config.html#configure-vlv).

DS supports the following sort key forms. The `ldapsearch` command `--sortOrder` option takes these forms as arguments:

* `[+|-]attr`

  Use this form with standard LDAP attributes.

  The optional plus or minus sign defines the order, and *attr* is the name of the LDAP attribute to sort on.

  For example, `cn` and `+cn` sort by common name in ascending order. `-sn` sorts by surname in descending order.

  The following example sorts the results in ascending order by surname using `--sortOrder +sn`:

  > **Collapse: Show example**
  >
  > ```console
  > $ ldapsearch \
  >  --hostname localhost \
  >  --port 1636 \
  >  --useSsl \
  >  --trustStorePath /path/to/opendj/config/keystore \
  >  --trustStoreType PKCS12 \
  >  --trustStorePassword:file /path/to/opendj/config/keystore.pin \
  >  --bindDn uid=kvaughan,ou=people,dc=example,dc=com \
  >  --bindPassword bribery \
  >  --baseDn dc=example,dc=com \
  >  --sortOrder +sn \
  >  "(&(sn=*)(cn=babs*))" \
  >  cn
  > ```
  >
  > Output
  >
  > ```
  > dn: uid=user.94643,ou=People,dc=example,dc=com
  > cn: Babs Bautista
  >
  > dn: uid=user.81225,ou=People,dc=example,dc=com
  > cn: Babs Bawek
  >
  > dn: uid=user.67807,ou=People,dc=example,dc=com
  > cn: Babs Baxter
  >
  > dn: uid=user.54389,ou=People,dc=example,dc=com
  > cn: Babs Bayer
  >
  > dn: uid=user.40971,ou=People,dc=example,dc=com
  > cn: Babs Bayerkohler
  >
  > dn: uid=user.27553,ou=People,dc=example,dc=com
  > cn: Babs Bayless
  >
  > dn: uid=user.14135,ou=People,dc=example,dc=com
  > cn: Babs Bayley
  >
  > dn: uid=user.717,ou=People,dc=example,dc=com
  > cn: Babs Bayly
  >
  > dn: uid=bjensen,ou=People,dc=example,dc=com
  > cn: Barbara Jensen
  > cn: Babs Jensen
  >
  > dn: uid=user.89830,ou=People,dc=example,dc=com
  > cn: Babs Pdesupport
  >
  > dn: uid=user.76412,ou=People,dc=example,dc=com
  > cn: Babs Peacemaker
  >
  > dn: uid=user.62994,ou=People,dc=example,dc=com
  > cn: Babs Peacocke
  >
  > dn: uid=user.49576,ou=People,dc=example,dc=com
  > cn: Babs Peake
  >
  > dn: uid=user.36158,ou=People,dc=example,dc=com
  > cn: Babs Pearce
  >
  > dn: uid=user.22740,ou=People,dc=example,dc=com
  > cn: Babs Pearcy
  >
  > dn: uid=user.9322,ou=People,dc=example,dc=com
  > cn: Babs Pearse
  > ```

* `[+|-]jsonAttr:customJsonOrderingMatchingRule`

  Use this form to sort on predefined fields in LDAP attributes whose values are JSON objects.

  Here, *jsonAttr* is the attribute name of the JSON attribute, and *customJsonOrderingMatchingRule* is one defined in the LDAP schema and backed by a custom schema provider. For details, refer to [Schema and JSON](../config-guide/schema.html#json-in-ldap).

  The following example sorts the results in ascending order by the "id" field of the `jsonToken` attribute. The custom matching rule, `caseIgnoreJsonTokenIDMatch`, is defined by the `ds-evaluation` setup profile:

  > **Collapse: Show example**
  >
  > ```console
  > $ ldapsearch \
  >  --hostname localhost \
  >  --port 1636 \
  >  --useSsl \
  >  --trustStorePath /path/to/opendj/config/keystore \
  >  --trustStoreType PKCS12 \
  >  --trustStorePassword:file /path/to/opendj/config/keystore.pin \
  >  --bindDn uid=kvaughan,ou=people,dc=example,dc=com \
  >  --bindPassword bribery \
  >  --baseDn dc=example,dc=com \
  >  --sortOrder +jsonToken:caseIgnoreJsonTokenIDMatch \
  >  "(objectClass=jsonTokenObject)" \
  >  jsonToken
  > ```
  >
  > Output
  >
  > ```
  > dn: uid=mjablons,ou=People,dc=example,dc=com
  > jsonToken: {"id":"HgAaB6xDhLom4JbM","scopes":["read","write"],"expires":"2018-01-10T10:08:34Z"}
  >
  > dn: uid=awhite,ou=People,dc=example,dc=com
  > jsonToken: {"id":"HkV5KzDrOgqN4prp","scopes":["read"],"expires":"2018-01-10T11:09:12Z"}
  > ```

* `[+|-]jsonAttr:extensibleJsonOrderingMatch:caseSensitive?:ignoreSpace?:/jsonPath[:/jsonPath…​]`

  Use this form to sort on arbitrary fields in LDAP attributes whose values are JSON objects.

  DS creates a matching rule on demand, if necessary. In that case, the search is unindexed.

  The following example uses this sort key form to mimic the previous example that used a custom JSON ordering rule:

  > **Collapse: Show example**
  >
  > ```console
  > $ ldapsearch \
  >  --hostname localhost \
  >  --port 1636 \
  >  --useSsl \
  >  --trustStorePath /path/to/opendj/config/keystore \
  >  --trustStoreType PKCS12 \
  >  --trustStorePassword:file /path/to/opendj/config/keystore.pin \
  >  --bindDn uid=kvaughan,ou=people,dc=example,dc=com \
  >  --bindPassword bribery \
  >  --baseDn dc=example,dc=com \
  >  --sortOrder +jsonToken:extensibleJsonOrderingMatch:true:true:/id \
  >  "(objectClass=jsonTokenObject)" \
  >  jsonToken
  > ```
  >
  > Output
  >
  > ```
  > dn: uid=mjablons,ou=People,dc=example,dc=com
  > jsonToken: {"id":"HgAaB6xDhLom4JbM","scopes":["read","write"],"expires":"2018-01-10T10:08:34Z"}
  >
  > dn: uid=awhite,ou=People,dc=example,dc=com
  > jsonToken: {"id":"HkV5KzDrOgqN4prp","scopes":["read"],"expires":"2018-01-10T11:09:12Z"}
  > ```

  This form has these required parameters:

  * Start with `extensibleJsonOrderingMatch`, or the OID `1.3.6.1.4.1.36733.2.1.4.6`.

  * Set *caseSensitive?* to `true` to respect case when comparing values, `false` otherwise.

  * Set *ignoreSpace?* to `true` to ignore whitespace when comparing values, `false` otherwise.

  * Each */jsonPath* specifies a field inside the JSON object. Specify at least one */jsonPath*.

## DN patterns

LDAP attributes such as `manager` have DN values. After adding an extensible match index for these attributes, you can use wildcards to find matches for specific RDNs in the DN, for example.

The following example demonstrates adding an index, so you can search for Torrey Rigden's (`uid=trigden`) employees, regardless of which company Torrey works for now.

The example that follows creates an extensible match index using the DN pattern matching rule, `distinguishedNamePatternMatch`, which has numeric OID `1.3.6.1.4.1.36733.2.1.4.13`. This supports searches that include wildcards.

The example also indexes `manager` for equality for search filters. The equality index is not required, but can be useful for searches the match entire DNs.

These commands create and rebuild the new index, then search for Torrey Ridgden's employees:

```console
$ dsconfig \
 create-backend-index \
 --backend-name dsEvaluation \
 --index-name manager \
 --set index-extensible-matching-rule:1.3.6.1.4.1.36733.2.1.4.13 \
 --set index-type:equality \
 --set index-type:extensible \
 --type generic \
 --hostname localhost \
 --port 4444 \
 --bindDN uid=admin \
 --bindPassword password \
 --trustStorePath /path/to/opendj/config/keystore \
 --trustStoreType PKCS12 \
 --trustStorePassword:file /path/to/opendj/config/keystore.pin \
 --no-prompt
$ rebuild-index \
 --index manager \
 --baseDn dc=example,dc=com \
 --hostname localhost \
 --port 4444 \
 --bindDN uid=admin \
 --bindPassword password \
 --trustStorePath /path/to/opendj/config/keystore \
 --trustStoreType PKCS12 \
 --trustStorePassword:file /path/to/opendj/config/keystore.pin \
 --no-prompt
$ ldapsearch \
 --hostname localhost \
 --port 1636 \
 --useSsl \
 --trustStorePath /path/to/opendj/config/keystore \
 --trustStoreType PKCS12 \
 --trustStorePassword:file /path/to/opendj/config/keystore.pin \
 --bindDN uid=kvaughan,ou=People,dc=example,dc=com \
 --bindPassword bribery \
 --baseDn dc=example,dc=com \
 "(manager:distinguishedNamePatternMatch:=uid=trigden,**)" \
 manager
```

> **Collapse: Show output**
>
> ```
> dn: uid=bjensen,ou=People,dc=example,dc=com
> manager: uid=trigden, ou=People, dc=example,dc=com
> ...
> ```

Notice the search filter, `(manager:distinguishedNamePatternMatch:=uid=trigden,**)`. In DN pattern matching filters:

* `*` matches a single RDN component, or a single RDN component value.

* `**` matches multiple RDN components, or a single RDN component value.

* `+` is the separator for multiple AVAs *(tooltip: \<div class="paragraph">
  \<p>An attribute description and a matching rule assertion value for the attribute used to determine whether an entry matches the assertion.\</p>
  \</div>)* in the same RDN component, as in `sn=smith+givenName=jane,ou=people,dc=example,dc=com`, which matches `sn=*+givenName=*,ou=people,dc=example,dc=com`, for example.

For details, refer to [distinguishedNamePatternMatch](../schemaref/mr-distinguishedNamePatternMatch.html).

---

---
title: LDAP updates
description: Add, modify, rename, move, and delete entries in PingDS directories using LDAP operations and LDIF.
component: pingds
version: 8.1
page_id: pingds:ldap-guide:write-ldap
canonical_url: https://docs.pingidentity.com/pingds/8.1/ldap-guide/write-ldap.html
llms_txt: https://docs.pingidentity.com/pingds/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2025-10-22T14:42:39Z
keywords: ["LDAP"]
section_ids:
  add-ldap: Add entries
  add-two-users: Add users
  bulk-add: Bulk adds
  modify-ldap: Modify entries
  modify-add-attribute: Add attributes
  modify-replace-attribute: Change an attribute
  modify-delete-attribute: Delete an attribute
  modify-delete-attribute-value: Delete one attribute value
  modify-stdin: From standard input
  modify-optimistic-concurrency: Optimistic concurrency (MVCC)
  json-update: JSON attribute
  filter-adds-modifies: Change incoming updates
  attr-cleanup-rename: Rename attributes
  attr-cleanup-remove: Remove attributes
  rename-ldap: Rename entries
  rename-moddn: Move entries
  move-entries-in-same-backend: Move a branch
  move-entry-example: Move an entry
  delete-ldap: Delete entries
  delete-subtree: Remove a branch
  delete-stdin: From standard input
---

# LDAP updates

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Examples in this documentation depend on features activated in [the `ds-evaluation` setup profile](../install-guide/setup-ds.html#about-ds-evaluation).The code samples demonstrate how to contact the server over HTTPS using the deployment CA certificate. Before trying the samples, generate the CA certificate in PEM format from the server deployment ID and password:```console
$ dskeymgr \
 export-ca-cert \
 --deploymentId $DEPLOYMENT_ID \
 --deploymentIdPassword password \
 --outputFile ca-cert.pem
``` |

For details on the LDIF format shown in the examples that follow, refer to [RFC 2849](https://www.rfc-editor.org/info/rfc2849).

## Add entries

### Add users

The following example adds two new users:

```console
$ ldapmodify \
 --hostname localhost \
 --port 1636 \
 --useSsl \
 --trustStorePath /path/to/opendj/config/keystore \
 --trustStoreType PKCS12 \
 --trustStorePassword:file /path/to/opendj/config/keystore.pin \
 --bindDN "uid=kvaughan,ou=people,dc=example,dc=com" \
 --bindPassword bribery << EOF
dn: cn=Arsene Lupin,ou=Special Users,dc=example,dc=com
objectClass: person
objectClass: top
cn: Arsene Lupin
telephoneNumber: +33 1 23 45 67 89
sn: Lupin

dn: cn=Horace Velmont,ou=Special Users,dc=example,dc=com
objectClass: person
objectClass: top
cn: Horace Velmont
telephoneNumber: +33 1 12 23 34 45
sn: Velmont
EOF
```

### Bulk adds

The following example adds 10,000 generated entries, using the `--numConnections` option to perform multiple add operations in parallel. It generates user entries with user IDs larger than existing user IDS, removes container entries, and bulk adds users:

```console
$ makeldif \
 --outputLdif output.ldif \
 <(sed "s/<sequential:0>/<sequential:100000>/" /path/to/opendj/config/MakeLDIF/example.template)
$ sed '1,10d' output.ldif > /tmp/generated-users.ldif
$ ldapmodify \
 --hostname localhost \
 --port 1636 \
 --useSsl \
 --trustStorePath /path/to/opendj/config/keystore \
 --trustStoreType PKCS12 \
 --trustStorePassword:file /path/to/opendj/config/keystore.pin \
 --bindDN "uid=kvaughan,ou=people,dc=example,dc=com" \
 --bindPassword bribery \
 --numConnections 64 \
 /tmp/generated-users.ldif
```

When you use the `--numConnections` option, the number of connection is rounded up to the nearest power of two for performance reasons.

## Modify entries

### Add attributes

The following example shows you how to add a description and JPEG photo, [picture.jpg](../_attachments/images/picture.jpg), to Sam Carter's entry:

```console
$ ldapmodify \
 --hostname localhost \
 --port 1636 \
 --useSsl \
 --trustStorePath /path/to/opendj/config/keystore \
 --trustStoreType PKCS12 \
 --trustStorePassword:file /path/to/opendj/config/keystore.pin \
 --bindDN "uid=kvaughan,ou=people,dc=example,dc=com" \
 --bindPassword bribery << EOF
dn: uid=scarter,ou=people,dc=example,dc=com
changetype: modify
add: description
description: Accounting Manager
-
add: jpegphoto
jpegphoto:<file:///tmp/picture.jpg
EOF
```

### Change an attribute

The following example replaces the description on Sam Carter's entry:

```console
$ ldapmodify \
 --hostname localhost \
 --port 1636 \
 --useSsl \
 --trustStorePath /path/to/opendj/config/keystore \
 --trustStoreType PKCS12 \
 --trustStorePassword:file /path/to/opendj/config/keystore.pin \
 --bindDN "uid=kvaughan,ou=people,dc=example,dc=com" \
 --bindPassword bribery << EOF
dn: uid=scarter,ou=people,dc=example,dc=com
changetype: modify
replace: description
description: New description
EOF
```

### Delete an attribute

The following example deletes the JPEG photo on Sam Carter's entry:

```console
$ ldapmodify \
 --hostname localhost \
 --port 1636 \
 --useSsl \
 --trustStorePath /path/to/opendj/config/keystore \
 --trustStoreType PKCS12 \
 --trustStorePassword:file /path/to/opendj/config/keystore.pin \
 --bindDN "uid=kvaughan,ou=people,dc=example,dc=com" \
 --bindPassword bribery << EOF
dn: uid=scarter,ou=people,dc=example,dc=com
changetype: modify
delete: jpegphoto
EOF
```

### Delete one attribute value

The following example deletes a single CN value on Barbara Jensen's entry:

```console
$ ldapmodify \
 --hostname localhost \
 --port 1636 \
 --useSsl \
 --trustStorePath /path/to/opendj/config/keystore \
 --trustStoreType PKCS12 \
 --trustStorePassword:file /path/to/opendj/config/keystore.pin \
 --bindDN "uid=kvaughan,ou=people,dc=example,dc=com" \
 --bindPassword bribery << EOF
dn: uid=bjensen,ou=People,dc=example,dc=com
changetype: modify
delete: cn
cn: Barbara Jensen
EOF
```

### From standard input

A double dash, `--`, signifies the end of command options. After the double dash, only trailing arguments are allowed. To indicate standard input as a trailing argument, use a bare dash, `-`, after the double dash.

Consider the following changes expressed in LDIF:

```ldif
dn: uid=bjensen,ou=People,dc=example,dc=com
changetype: modify
replace: description
description: New description from standard input
```

To send these changes to the `ldapmodify` command on standard input, use either of the following equivalent constructions:

* With dashes:

  ```console
  $ cat bjensen-stdin-description.ldif | ldapmodify \
   --hostname localhost \
   --port 1636 \
   --useSsl \
   --trustStorePath /path/to/opendj/config/keystore \
   --trustStoreType PKCS12 \
   --trustStorePassword:file /path/to/opendj/config/keystore.pin \
   --bindDN "uid=kvaughan,ou=people,dc=example,dc=com" \
   --bindPassword bribery \
   -- -
  ```

* Without dashes:

  ```console
  $ cat bjensen-stdin-description.ldif | ldapmodify \
   --hostname localhost \
   --port 1636 \
   --useSsl \
   --trustStorePath /path/to/opendj/config/keystore \
   --trustStoreType PKCS12 \
   --trustStorePassword:file /path/to/opendj/config/keystore.pin \
   --bindDN "uid=kvaughan,ou=people,dc=example,dc=com" \
   --bindPassword bribery
  ```

### Optimistic concurrency (MVCC)

Consider an application that lets end users update user profiles through a browser. It stores user profiles as DS entries. End users can look up user profiles and modify them. The application assumes that the end users can tell the right information when they observe it, and updates profiles exactly as users observe them on their screens.

Suppose two users, Alice and Bob, are busy and often interrupted. Alice has Babs Jensen's new phone and room numbers. Bob has Babs's new location and description. Both assume that they have all the information that has changed. What can you do to make sure that your application applies the right changes when Alice and Bob simultaneously update Babs Jensen's profile?

DS servers have two features to help you in this situation. One of the features is the LDAP Assertion Control, described in [Supported LDAP controls](../ldap-reference/controls.html), used to tell the directory server to perform the modification only if an assertion you make stays true. The other feature is DS support for [entity tag](https://www.rfc-editor.org/rfc/rfc2616#section-3.11) (ETag) attributes, making it easy to check whether the entry in the directory is the same as the entry you read.

Alice and Bob both get Babs's entry. In LDIF, the relevant attributes from the entry look like the following. The ETag is a generated value:

```console
$ ldapsearch \
 --hostname localhost \
 --port 1636 \
 --useSsl \
 --trustStorePath /path/to/opendj/config/keystore \
 --trustStoreType PKCS12 \
 --trustStorePassword:file /path/to/opendj/config/keystore.pin \
 --bindDN uid=kvaughan,ou=People,dc=example,dc=com \
 --bindPassword bribery \
 --baseDN dc=example,dc=com \
 "(uid=bjensen)" \
 telephoneNumber roomNumber l ETag
```

> **Collapse: Show output**
>
> ```
> dn: uid=bjensen,ou=People,dc=example,dc=com
> l: San Francisco
> roomNumber: 0209
> telephoneNumber: +1 408 555 1862
> ETag: ETAG
> ```

Bob prepares his changes in your application. Bob is almost ready to submit the new location and description when Carol stops by to ask Bob a few questions.

Alice starts just after Bob, but manages to submit her changes without interruption. Now Babs's entry has a new phone number, room number, and ETag:

```console
$ ldapsearch \
 --hostname localhost \
 --port 1636 \
 --useSsl \
 --trustStorePath /path/to/opendj/config/keystore \
 --trustStoreType PKCS12 \
 --trustStorePassword:file /path/to/opendj/config/keystore.pin \
 --bindDN uid=kvaughan,ou=People,dc=example,dc=com \
 --bindPassword bribery \
 --baseDN dc=example,dc=com \
 "(uid=bjensen)" \
 telephoneNumber roomNumber l ETag
```

> **Collapse: Show output**
>
> ```
> dn: uid=bjensen,ou=People,dc=example,dc=com
> telephoneNumber: +47 2108 1746
> roomNumber: 1389
> l: San Francisco
> ETag: NEW_ETAG
> ```

In your application, you use the ETag value with the assertion control to prevent Bob's update from succeeding. The application tries the equivalent of the following commands with Bob's updates:

```console
$ ldapmodify \
 --hostname localhost \
 --port 1636 \
 --useSsl \
 --trustStorePath /path/to/opendj/config/keystore \
 --trustStoreType PKCS12 \
 --trustStorePassword:file /path/to/opendj/config/keystore.pin \
 --bindDN "uid=kvaughan,ou=people,dc=example,dc=com" \
 --bindPassword bribery \
 --assertionFilter "(ETag=${ETAG})" << EOF
dn: uid=bjensen,ou=People,dc=example,dc=com
changetype: modify
replace: l
l: Grenoble
-
add: description
description: Employee of the Month
EOF
```

> **Collapse: Show output**
>
> ```
> # The LDAP modify request failed: 122 (Assertion Failed)
> # Additional Information:  Entry uid=bjensen,ou=People,dc=example,dc=com cannot be modified because the request contained an LDAP assertion control and the associated filter did not match the contents of the entry
> ```

The application reloads Babs's entry with the new ETag value, and tries Bob's update again. This time Bob's changes do not collide with other changes. Babs's entry is successfully updated:

```console
$ ldapmodify \
 --hostname localhost \
 --port 1636 \
 --useSsl \
 --trustStorePath /path/to/opendj/config/keystore \
 --trustStoreType PKCS12 \
 --trustStorePassword:file /path/to/opendj/config/keystore.pin \
 --bindDN "uid=kvaughan,ou=people,dc=example,dc=com" \
 --bindPassword bribery \
 --assertionFilter "(ETag=${NEW_ETAG})" << EOF
dn: uid=bjensen,ou=People,dc=example,dc=com
changetype: modify
replace: l
l: Grenoble
-
add: description
description: Employee of the Month
EOF
```

> **Collapse: Show output**
>
> ```
> # MODIFY operation successful for DN uid=bjensen,ou=People,dc=example,dc=com
> ```

### JSON attribute

DS servers support attribute values that have JSON syntax as demonstrated in [JSON query filters](search-ldap.html#json-search).

This example depends on the configuration and sample data used in [JSON query matching rule index](../config-guide/idx-config.html#json-index-example). Unless you have installed the server with the evaluation profile, perform the commands in that example to prepare the server before trying this one.

The following example replaces the existing JSON value with a new JSON value:

```console
$ ldapmodify \
 --hostname localhost \
 --port 1636 \
 --useSsl \
 --trustStorePath /path/to/opendj/config/keystore \
 --trustStoreType PKCS12 \
 --trustStorePassword:file /path/to/opendj/config/keystore.pin \
 --bindDN "uid=kvaughan,ou=people,dc=example,dc=com" \
 --bindPassword bribery << EOF
dn: uid=bjensen,ou=people,dc=example,dc=com
changetype: modify
add: objectClass
objectClass: jsonObject
-
add: json
json: {"stuff":["things","devices","paraphernalia"]}
EOF
```

Notice that the JSON object is replaced entirely.

When DS servers receive update requests for `Json` syntax attributes, they expect valid JSON objects. By default, `Json` syntax attribute values must comply with *The JavaScript Object Notation (JSON) Data Interchange Format*, described in [RFC 7159](https://www.rfc-editor.org/info/rfc7159). You can use the advanced core schema configuration option `json-validation-policy` to have the server be more lenient in what it accepts, or to disable JSON syntax checking.

The following example relaxes JSON syntax checking to allow comments, single quotes, and unquoted control characters such as newlines, in strings:

```console
$ dsconfig \
 set-schema-provider-prop \
 --hostname localhost \
 --port 4444 \
 --bindDN uid=admin \
 --bindPassword password \
 --provider-name "Core Schema" \
 --set json-validation-policy:lenient \
 --trustStorePath /path/to/opendj/config/keystore \
 --trustStoreType PKCS12 \
 --trustStorePassword:file /path/to/opendj/config/keystore.pin \
 --no-prompt
```

## Change incoming updates

Some client applications send updates including attributes with names that differ from the attribute names defined in the LDAP schema. Other client applications might try to update attributes they should not update, such as the operational attributes `creatorsName`, `createTimestamp`, `modifiersName`, and `modifyTimestamp`. Ideally, you would fix the client application behavior, but that is not always possible. You can configure the attribute cleanup plugin to filter add and modify requests, rename attributes in requests using incorrect names, and remove attributes that applications should not change.

### Rename attributes

The following example renames incoming `email` attributes to `mail` attributes:

1. Configure the attribute cleanup plugin to rename the inbound attribute:

   ```console
   $ dsconfig \
    create-plugin \
    --hostname localhost \
    --port 4444 \
    --bindDN uid=admin \
    --bindPassword password \
    --type attribute-cleanup \
    --plugin-name "Rename email to mail" \
    --set enabled:true \
    --set rename-inbound-attributes:email:mail \
    --trustStorePath /path/to/opendj/config/keystore \
    --trustStoreType PKCS12 \
    --trustStorePassword:file /path/to/opendj/config/keystore.pin \
    --no-prompt
   ```

2. Confirm that it worked as expected:

   ```console
   $ ldapmodify \
    --hostname localhost \
    --port 1636 \
    --useSsl \
    --trustStorePath /path/to/opendj/config/keystore \
    --trustStoreType PKCS12 \
    --trustStorePassword:file /path/to/opendj/config/keystore.pin \
    --bindDN "uid=kvaughan,ou=people,dc=example,dc=com" \
    --bindPassword bribery << EOF
   dn: uid=newuser,ou=People,dc=example,dc=com
   uid: newuser
   objectClass: person
   objectClass: organizationalPerson
   objectClass: inetOrgPerson
   objectClass: top
   cn: New User
   sn: User
   ou: People
   email: newuser@example.com
   userPassword: chngthspwd
   EOF
   $ ldapsearch \
    --hostname localhost \
    --port 1636 \
    --useSsl \
    --trustStorePath /path/to/opendj/config/keystore \
    --trustStoreType PKCS12 \
    --trustStorePassword:file /path/to/opendj/config/keystore.pin \
    --bindDN uid=kvaughan,ou=People,dc=example,dc=com \
    --bindPassword bribery \
    --baseDN dc=example,dc=com \
    "(uid=newuser)" \
     mail
   ```

   > **Collapse: Show output**
   >
   > ```
   > dn: uid=newuser,ou=People,dc=example,dc=com
   > mail: newuser@example.com
   > ```

### Remove attributes

The following example prevents client applications from adding or modifying `creatorsName`, `createTimestamp`, `modifiersName`, and `modifyTimestamp` attributes.

1. Set up the attribute cleanup plugin:

   ```console
   $ dsconfig \
    create-plugin \
    --type attribute-cleanup \
    --plugin-name "Remove attrs" \
    --set enabled:true \
    --set remove-inbound-attributes:creatorsName \
    --set remove-inbound-attributes:createTimestamp \
    --set remove-inbound-attributes:modifiersName \
    --set remove-inbound-attributes:modifyTimestamp \
    --hostname localhost \
    --port 4444 \
    --bindDN uid=admin \
    --bindPassword password \
    --trustStorePath /path/to/opendj/config/keystore \
    --trustStoreType PKCS12 \
    --trustStorePassword:file /path/to/opendj/config/keystore.pin \
    --no-prompt
   ```

2. Confirm that it worked as expected:

   ```console
   $ ldapmodify \
    --hostname localhost \
    --port 1636 \
    --useSsl \
    --trustStorePath /path/to/opendj/config/keystore \
    --trustStoreType PKCS12 \
    --trustStorePassword:file /path/to/opendj/config/keystore.pin \
    --bindDN "uid=kvaughan,ou=people,dc=example,dc=com" \
    --bindPassword bribery << EOF
   dn: uid=badattr,ou=People,dc=example,dc=com
   uid: newuser
   objectClass: person
   objectClass: organizationalPerson
   objectClass: inetOrgPerson
   objectClass: top
   cn: Bad Attr
   sn: Attr
   ou: People
   mail: badattr@example.com
   userPassword: chngthspwd
   creatorsName: cn=Bad Attr
   createTimestamp: Never in a million years.
   modifiersName: uid=admin
   modifyTimestamp: 20110930164937Z
   EOF
   $ ldapsearch \
    --hostname localhost \
    --port 1636 \
    --useSsl \
    --trustStorePath /path/to/opendj/config/keystore \
    --trustStoreType PKCS12 \
    --trustStorePassword:file /path/to/opendj/config/keystore.pin \
    --bindDN uid=kvaughan,ou=People,dc=example,dc=com \
    --bindPassword bribery \
    --baseDN dc=example,dc=com \
    "(uid=badattr)" \
    creatorsName createTimestamp modifiersTimestamp modifyTimestamp
   ```

   > **Collapse: Show output**
   >
   > ```
   > dn: uid=badattr,ou=People,dc=example,dc=com
   > createTimestamp: <timestamp>
   > creatorsName: uid=kvaughan,ou=People,dc=example,dc=com
   > ```

## Rename entries

The relative distinguished name (RDN) *(tooltip: \<div class="paragraph">
\<p>The initial portion of a DN distinguishing the entry from all others at the same level.\</p>
\</div>)* refers to the part of an entry's DN that differentiates it from all other DNs at the same level in the directory tree. For example, `uid=bjensen` is the RDN of the entry with the DN `uid=bjensen,ou=People,dc=example,dc=com`. When you change the RDN of the entry, you rename the entry, modifying the naming attribute and DN.

In this example, Sam Carter is changing her last name to Jensen, and changing her login from `scarter` to `sjensen`. The following example shows you how to rename and change Sam Carter's entry. Notice the boolean field, `deleteoldrdn: 1`, which indicates that the previous RDN, `uid: scarter`, should be removed. Setting `deleteoldrdn: 0` instead would preserve `uid: scarter` on the entry:

```console
$ ldapmodify \
 --hostname localhost \
 --port 1636 \
 --useSsl \
 --trustStorePath /path/to/opendj/config/keystore \
 --trustStoreType PKCS12 \
 --trustStorePassword:file /path/to/opendj/config/keystore.pin \
 --bindDN "uid=kvaughan,ou=people,dc=example,dc=com" \
 --bindPassword bribery << EOF
dn: uid=scarter,ou=people,dc=example,dc=com
changetype: modrdn
newrdn: uid=sjensen
deleteoldrdn: 1

dn: uid=sjensen,ou=people,dc=example,dc=com
changetype: modify
replace: cn
cn: Sam Jensen
-
replace: sn
sn: Jensen
-
replace: homeDirectory
homeDirectory: /home/sjensen
-
replace: mail
mail: sjensen@example.com
EOF
```

## Move entries

When you rename an entry with child entries, the directory has to move all the entries underneath it.

|   |                                                                                                                                                                                                                    |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | DS directory servers support the modify DN operation only for moving entries in the same backend, under the same base DN. Depending on the number of entries you move, this can be a resource-intensive operation. |

### Move a branch

The following example moves all entries at and below `ou=People,dc=example,dc=com` under `ou=Subscribers,dc=example,dc=com`. All the entries in this example are in the same backend. The line `deleteoldrdn: 1` indicates that the old RDN, `ou: People`, should be removed:

```console
$ ldapmodify \
 --hostname localhost \
 --port 1636 \
 --useSsl \
 --trustStorePath /path/to/opendj/config/keystore \
 --trustStoreType PKCS12 \
 --trustStorePassword:file /path/to/opendj/config/keystore.pin \
 --bindDN uid=admin \
 --bindPassword password << EOF
dn: ou=People,dc=example,dc=com
changetype: modrdn
newrdn: ou=Subscribers
deleteoldrdn: 1
newsuperior: dc=example,dc=com
EOF
```

Be aware that the move doesn't modify ACIs *(tooltip: \<div class="paragraph">
\<p>An instruction or rule that can be used to grant or deny access to users to perform operations on a server.\</p>
\</div>)* and other values that depend on `ou=People`. You must also edit any affected entries.

### Move an entry

The following example moves an application entry that is under `dc=example,dc=com` under `ou=Apps,dc=example,dc=com` instead. The line `deleteoldrdn: 0` indicates that old RDN, `cn`, should be preserved:

```console
$ ldapmodify \
 --hostname localhost \
 --port 1636 \
 --useSsl \
 --trustStorePath /path/to/opendj/config/keystore \
 --trustStoreType PKCS12 \
 --trustStorePassword:file /path/to/opendj/config/keystore.pin \
 --bindDN "uid=kvaughan,ou=people,dc=example,dc=com" \
 --bindPassword bribery << EOF
dn: cn=New App,dc=example,dc=com
changetype: moddn
newrdn: cn=An App
deleteoldrdn: 0
newsuperior: ou=Apps,dc=example,dc=com
EOF
```

## Delete entries

### Remove a branch

|   |                                                                                                                                  |
| - | -------------------------------------------------------------------------------------------------------------------------------- |
|   | This can be a resource-intensive operation. The resources required to remove a branch depend on the number of entries to delete. |

The following example shows you how to give an administrator access to use the subtree delete control, and to use the subtree delete option to remove an entry and its child entries:

```console
$ dsconfig \
 set-access-control-handler-prop \
 --hostname localhost \
 --port 4444 \
 --bindDN uid=admin \
 --bindPassword password \
 --add global-aci:"(targetcontrol=\"SubtreeDelete\")\
 (version 3.0; acl \"Allow Subtree Delete\"; allow(read) \
 userdn=\"ldap:///uid=kvaughan,ou=People,dc=example,dc=com\";)" \
 --trustStorePath /path/to/opendj/config/keystore \
 --trustStoreType PKCS12 \
 --trustStorePassword:file /path/to/opendj/config/keystore.pin \
 --no-prompt
$ ldapdelete \
 --hostname localhost \
 --port 1636 \
 --useSsl \
 --trustStorePath /path/to/opendj/config/keystore \
 --trustStoreType PKCS12 \
 --trustStorePassword:file /path/to/opendj/config/keystore.pin \
--bindDN "uid=kvaughan,ou=People,dc=example,dc=com" \
--bindPassword bribery \
--deleteSubtree "ou=Special Users,dc=example,dc=com"
```

### From standard input

A double dash, `--`, signifies the end of command options. After the double dash, only trailing arguments are allowed. To indicate standard input as a trailing argument, use a bare dash, `-`, after the double dash.

Consider the following list of [users to delete](../_attachments/text/users-to-delete.txt):

```console
$ cat users-to-delete.txt
```

Output

```
uid=sfarmer,ou=People,dc=example,dc=com
uid=skellehe,ou=People,dc=example,dc=com
uid=slee,ou=People,dc=example,dc=com
uid=smason,ou=People,dc=example,dc=com
uid=speterso,ou=People,dc=example,dc=com
uid=striplet,ou=People,dc=example,dc=com
```

To send this list to the `ldapdelete` command on standard input, use either of the following equivalent constructions:

* With dashes:

  ```console
  $ cat users-to-delete.txt | ldapdelete \
   --hostname localhost \
   --port 1636 \
   --useSsl \
   --trustStorePath /path/to/opendj/config/keystore \
   --trustStoreType PKCS12 \
   --trustStorePassword:file /path/to/opendj/config/keystore.pin \
   --bindDN uid=kvaughan,ou=people,dc=example,dc=com \
   --bindPassword bribery \
   -- -
  ```

* Without dashes:

  ```console
  $ cat users-to-delete.txt | ldapdelete \
   --hostname localhost \
   --port 1636 \
   --useSsl \
   --trustStorePath /path/to/opendj/config/keystore \
   --trustStoreType PKCS12 \
   --trustStorePassword:file /path/to/opendj/config/keystore.pin \
   --bindDN uid=kvaughan,ou=people,dc=example,dc=com \
   --bindPassword bribery
  ```

---

---
title: LDIF tools
description: Use PingDS LDIF command-line tools to generate test data, search, update, and compare LDIF files.
component: pingds
version: 8.1
page_id: pingds:ldap-guide:ldif-tools
canonical_url: https://docs.pingidentity.com/pingds/8.1/ldap-guide/ldif-tools.html
llms_txt: https://docs.pingidentity.com/pingds/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2025-10-22T14:42:39Z
keywords: ["Integration", "LDAP", "Storage"]
section_ids:
  generating-ldif: Generate test data
  ldifsearch-example: Search LDIF
  ldifmodify-example: Update LDIF
  ldifdiff-example: Compare LDIF
  ldiftools-stdin: Use standard input
---

# LDIF tools

## Generate test data

The [makeldif](../tools-reference/makeldif.html) command uses templates to generate sample data with great flexibility. Default templates are located in the `opendj/config/MakeLDIF/` directory.

|   |                                                                                                                                                                                                                                                                               |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The quickest way to generate user entries is to use the `ds-evaluation` setup profile. The profile lets you generate an arbitrary number of Example.com users as part of the setup process.For details, refer to [Install DS for evaluation](../install-guide/setup-ds.html). |

1. Write a template file for your generated LDIF.

   The `example.template` file used in the examples creates `inetOrgPerson` entries. To learn how to generate test data that matches your production data more closely, read [makeldif-template](../tools-reference/makeldif-template.html).

2. Create additional data files for your template.

   Additional data files are located in the same directory as your template file.

3. Decide whether to generate the same test data each time you use the same template.

   If so, provide the same `randomSeed` integer each time you run the command.

4. Run the `makeldif` command to generate your LDIF file.

   The following command demonstrates use of the example MakeLDIF template:

   ```console
   $ makeldif \
    --outputLdif example.ldif \
    --randomSeed 42 \
    /path/to/opendj/config/MakeLDIF/example.template
   ```

   > **Collapse: Show output**
   >
   > ```
   > LDIF processing complete.
   > ```

## Search LDIF

The `ldifsearch` command searches for entries in LDIF files:

```console
$ ldifsearch \
 --baseDN dc=example,dc=com \
 example.ldif \
 "(sn=Grenier)" \
 uid
```

> **Collapse: Show output**
>
> ```
> dn: uid=user.4630,ou=People,dc=example,dc=com
> uid: user.4630
> ```

## Update LDIF

The `ldifmodify` command applies changes, generating a new version of the LDIF.

The following [changes.ldif](../_attachments/ldif/changes.ldif) file holds the changes:

```ldif
dn: uid=user.0,ou=People,dc=example,dc=com
changetype: modify
replace: description
description: New description.
-
replace: initials
initials: ZZZ
```

This example command applies the changes:

```console
$ ldifmodify \
 --outputLdif new.ldif \
 example.ldif \
 changes.ldif
```

The resulting target LDIF file is approximately the same size as the source LDIF file. The order of entries in the file isn't guaranteed to be identical.

## Compare LDIF

The `ldifdiff` command reports differences between two LDIF files in LDIF format:

```console
$ ldifdiff example.ldif new.ldif
```

> **Collapse: Show output**
>
> ```
> dn: uid=user.0,ou=People,dc=example,dc=com
> changetype: modify
> delete: description
> description: This is the description for Aaccf Amar.
> -
> add: description
> description: New description.
> -
> delete: initials
> initials: AAA
> -
> add: initials
> initials: ZZZ
> -
> ```

The `ldifdiff` command reads files into memory to compare their contents. The command is designed to work with small files and fragments, and can quickly run out of memory when calculating the differences between large files.

## Use standard input

For each LDIF tool, a double dash, `--`, signifies the end of command options. After the double dash, only trailing arguments are allowed.

To indicate standard input as a trailing argument, use a bare dash, `-`, after the double dash. How bare dashes are used after a double dash depends on the tool:

* `ldifdiff`

  The bare dash can replace either the source LDIF file, or the target LDIF file argument.

  To take the source LDIF from standard input, use the following construction:

  ```
  ldifdiff [options] -- - target.ldif
  ```

  To take the target LDIF from standard input, use the following construction:

  ```
  ldifdiff [options] -- source.ldif -
  ```

* `ldifmodify`

  The bare dash can replace either the source.ldif or changes.ldif file arguments.

  To take the source LDIF from standard input, use the following construction:

  ```
  ldifmodify [options] -- - changes.ldif [changes.ldif ...]
  ```

  To take the changes in LDIF from standard input, use the following construction:

  ```
  ldifmodify [options] -- source.ldif -
  ```

* `ldifsearch`

  The bare dash lets you take the source LDIF from standard input with the following construction:

  ```
  ldifsearch [options] -- - filter [attributes ...]
  ```

---

---
title: Notification of changes
description: Use persistent search or the external change log to receive real-time and incremental LDAP change notifications in PingDS.
component: pingds
version: 8.1
page_id: pingds:ldap-guide:change-notification
canonical_url: https://docs.pingidentity.com/pingds/8.1/ldap-guide/change-notification.html
llms_txt: https://docs.pingidentity.com/pingds/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2025-10-22T14:42:39Z
keywords: ["Change Notification", "LDAP"]
section_ids:
  persistent-search: Use persistent search
  use-ecl: Use the external change log
---

# Notification of changes

Applications that need change notification can use a persistent search or read the external change log.

## Use persistent search

Defined in the Internet-Draft, [Persistent Search: A Simple LDAP Change Notification Mechanism](https://datatracker.ietf.org/doc/html/draft-ietf-ldapext-psearch), a persistent search is like a regular search that never stops returning results. Every time a change happens in the scope of the search, the server returns an additional response:

1. Grant access to perform a persistent search, by adding an access control instruction (ACI) *(tooltip: \<div class="paragraph">
   \<p>An instruction or rule that can be used to grant or deny access to users to perform operations on a server.\</p>
   \</div>)* to use the persistent search control.

   Persistent searches consume server resources, so servers do not allow them by default. If an application does not have access, the request fails with an unavailable critical extension error:

   ```
   The LDAP search request failed: 12 (Unavailable Critical Extension)
   Additional Information:  The request control with Object Identifier (OID) "2.16.840.1.113730.3.4.3"
   cannot be used due to insufficient access rights
   ```

   The following command grants access under `dc=example,dc=com` to `My App`:

   ```console
   $ ldapmodify \
    --hostname localhost \
    --port 1636 \
    --useSsl \
    --trustStorePath /path/to/opendj/config/keystore \
    --trustStoreType PKCS12 \
    --trustStorePassword:file /path/to/opendj/config/keystore.pin \
    --bindDN uid=admin \
    --bindPassword password << EOF
   dn: dc=example,dc=com
   changetype: modify
   add: aci
   aci: (targetcontrol = "PSearch")
    (version 3.0;acl "Allow Persistent Search for My App";
    allow (read)(userdn = "ldap:///cn=My App,ou=Apps,dc=example,dc=com");)
   EOF
   ```

2. Start the persistent search.

   The following example initiates a persistent search, where notifications are sent for all update operations, only notifications about changed entries are returned, and no additional information are returned:

   ```console
   $ ldapsearch \
    --hostname localhost \
    --port 1636 \
    --useSsl \
    --trustStorePath /path/to/opendj/config/keystore \
    --trustStoreType PKCS12 \
    --trustStorePassword:file /path/to/opendj/config/keystore.pin \
    --bindDN 'cn=My App,ou=Apps,dc=example,dc=com' \
    --bindPassword password \
    --baseDN dc=example,dc=com \
    --persistentSearch ps:all:true:false \
    '(&)' >> /tmp/psearch.txt &
   $ export PSEARCH_PID=$!
   ```

   Notice the search filter, `(&)`, which is always true, meaning that it matches all entries. For details on settings for a persistent search, refer to the `--persistentSearch` option in [ldapsearch Options](../tools-reference/ldapsearch.html#ldapsearch-options).

3. Make changes that impact the persistent search results.

   > **Collapse: Show commands**
   >
   > To prepare to modify an entry, save the following as the LDIF file, [description.ldif](../_attachments/ldif/description.ldif):
   >
   > ```ldif
   > dn: uid=bjensen,ou=People,dc=example,dc=com
   > changetype: modify
   > replace: description
   > description: Hello, persistent search
   > ```
   >
   > The following commands perform a modify operation and a delete operation:
   >
   > ```console
   > $ ldapmodify \
   >  --hostname localhost \
   >  --port 1636 \
   >  --useSsl \
   >  --trustStorePath /path/to/opendj/config/keystore \
   >  --trustStoreType PKCS12 \
   >  --trustStorePassword:file /path/to/opendj/config/keystore.pin \
   >  --bindDN uid=kvaughan,ou=People,dc=example,dc=com \
   >  --bindPassword bribery << EOF
   > dn: uid=bjensen,ou=People,dc=example,dc=com
   > changetype: modify
   > replace: description
   > description: Hello, persistent search
   > EOF
   > $ ldapdelete \
   >  --hostname localhost \
   >  --port 1636 \
   >  --useSsl \
   >  --trustStorePath /path/to/opendj/config/keystore \
   >  --trustStoreType PKCS12 \
   >  --trustStorePassword:file /path/to/opendj/config/keystore.pin \
   >  --bindDN uid=kvaughan,ou=People,dc=example,dc=com \
   >  --bindPassword bribery \
   >  uid=tpierce,ou=People,dc=example,dc=com
   > ```

   > **Collapse: Show persistent search results**
   >
   > The result is the following responses to the persistent search:
   >
   > ```ldif
   > dn: uid=bjensen,ou=People,dc=example,dc=com
   > objectClass: person
   > objectClass: cos
   > objectClass: oauth2TokenObject
   > objectClass: inetOrgPerson
   > objectClass: organizationalPerson
   > objectClass: posixAccount
   > objectClass: top
   > classOfService: bronze
   > cn: Barbara Jensen
   > cn: Babs Jensen
   > description: Hello, persistent search
   > facsimileTelephoneNumber: +1 408 555 1992
   > gidNumber: 1000
   > givenName: Barbara
   > homeDirectory: /home/bjensen
   > l: San Francisco
   > mail: bjensen@example.com
   > manager: uid=trigden, ou=People, dc=example,dc=com
   > oauth2Token: {"access_token":"123","expires_in":59,"token_type":"Bearer","refresh_token":"456"}
   > ou: Product Development
   > ou: People
   > preferredLanguage: en, ko;q=0.8
   > roomNumber: 0209
   > sn: Jensen
   > telephoneNumber: +1 408 555 1862
   > uid: bjensen
   > uidNumber: 1076
   > userPassword: {PBKDF2-HMAC-SHA256}10:<hash>
   > dn: uid=tpierce,ou=People,dc=example,dc=com
   > objectClass: person
   > objectClass: cos
   > objectClass: inetOrgPerson
   > objectClass: organizationalPerson
   > objectClass: posixAccount
   > objectClass: top
   > classOfService: gold
   > cn: Tobias Pierce
   > departmentNumber: 1000
   > description: Description on ou=People
   > diskQuota: 100 GB
   > facsimileTelephoneNumber: +1 408 555 9332
   > gidNumber: 1000
   > givenName: Tobias
   > homeDirectory: /home/tpierce
   > l: Bristol
   > mail: tpierce@example.com
   > mailQuota: 10 GB
   > manager: uid=scarter, ou=People, dc=example,dc=com
   > ou: Accounting
   > ou: People
   > preferredLanguage: en-gb
   > roomNumber: 1383
   > sn: Pierce
   > street: Broad Quay House, Prince Street
   > telephoneNumber: +1 408 555 1531
   > uid: tpierce
   > uidNumber: 1042
   > userPassword: {PBKDF2-HMAC-SHA256}10:<hash>
   > ```
   >
   > If the data is replicated, the results include the entry `dc=example,dc=com`. Replication updates the `ds-sync-*` operational attributes on `dc=example,dc=com`, and those changes appear in the results because the entry is in the scope of the persistent search.

4. Terminate the persistent search.

   Interrupt the command with `CTRL`+`C` (`SIGINT`) or `SIGTERM`:

   ```console
   $ kill -s SIGTERM $PSEARCH_PID
   ```

## Use the external change log

You read the external change log over LDAP. When you poll the change log, you can get the list of updates that happened since your last request.

The external change log mechanism uses an LDAP control with OID `1.3.6.1.4.1.26027.1.5.4`. This control allows the client application to bookmark the last changes observed. The control returns a cookie that the application sends to the server to read the next batch of changes.

These steps show the client binding as directory superuser (`uid=admin`) to read the change log. Other accounts require sufficient access and privileges to read the change log. For instructions, refer to [Let a user read the changelog](../config-guide/changelog.html#read-ecl-as-regular-user):

1. Send an initial search request using the LDAP control with no cookie value.

   In this example, two changes appear in the changelog:

   ```console
   $ ldapsearch \
    --hostname localhost \
    --port 1636 \
    --useSsl \
    --trustStorePath /path/to/opendj/config/keystore \
    --trustStoreType PKCS12 \
    --trustStorePassword:file /path/to/opendj/config/keystore.pin \
    --bindDN uid=admin \
    --bindPassword password \
    --baseDN cn=changelog \
    --control "ecl:true" \
    "(&)" \
    changes changeLogCookie targetDN
   ```

   > **Collapse: Show output**
   >
   > ```
   > dn: cn=changelog
   >
   > dn: replicationCSN=<CSN1>,dc=example,dc=com,cn=changelog
   > changes:: <base64Changes1>
   > targetDN: uid=bjensen,ou=People,dc=example,dc=com
   > changeLogCookie: <COOKIE1>
   >
   > dn: replicationCSN=<CSN2>,dc=example,dc=com,cn=changelog
   > changes:: <base64Changes2>
   > targetDN: uid=bjensen,ou=People,dc=example,dc=com
   > changeLogCookie: <COOKIE2>
   > ```

   The changes are base64-encoded. You can decode them using the `base64` command. This example decodes a change:

   ```console
   $ base64 decode --encodedData cmVwbGFjZTogZGVzY3JpcHRpb24KZGVzY3JpcHRpb246IE5ldyBkZXNjcmlwdGlvbgotCnJlcGxhY2U6IG1vZGlmaWVyc05hbWUKbW9kaWZpZXJzTmFtZTogdWlkPWJqZW5zZW4sb3U9UGVvcGxlLGRjPWV4YW1wbGUsZGM9Y29tCi0KcmVwbGFjZTogbW9kaWZ5VGltZXN0YW1wCm1vZGlmeVRpbWVzdGFtcDogMjAxNjEwMTQxNTA5MTJaCi0K
   ```

   > **Collapse: Show output**
   >
   > ```
   > replace: description
   > description: New description
   > -
   > replace: modifiersName
   > modifiersName: uid=bjensen,ou=People,dc=example,dc=com
   > -
   > replace: modifyTimestamp
   > modifyTimestamp: <timestamp>
   > -
   > ```

2. To start reading a particular change in the changelog, provide the cookie with the control:

   ```console
   $ ldapsearch \
    --hostname localhost \
    --port 1636 \
    --useSsl \
    --trustStorePath /path/to/opendj/config/keystore \
    --trustStoreType PKCS12 \
    --trustStorePassword:file /path/to/opendj/config/keystore.pin \
    --bindDN uid=admin \
    --bindPassword password \
    --baseDN cn=changelog \
    --control "ecl:true:$COOKIE1" \
    "(&)" \
    changes changeLogCookie targetDN
   ```

   > **Collapse: Show output**
   >
   > ```
   > dn: replicationCSN=<CSN2>,dc=example,dc=com,cn=changelog
   > changes:: <base64Changes2>
   > targetDN: uid=bjensen,ou=People,dc=example,dc=com
   > changeLogCookie: <COOKIE2>
   > ```

   This command decodes the change returned:

   ```console
   $ base64 decode --encodedData cmVwbGFjZTogZGVzY3JpcHRpb24KZGVzY3JpcHRpb246IE5ldywgaW1wcm92ZWQgZGVzY3JpcHRpb24KLQpyZXBsYWNlOiBtb2RpZmllcnNOYW1lCm1vZGlmaWVyc05hbWU6IHVpZD1iamVuc2VuLG91PVBlb3BsZSxkYz1leGFtcGxlLGRjPWNvbQotCnJlcGxhY2U6IG1vZGlmeVRpbWVzdGFtcAptb2RpZnlUaW1lc3RhbXA6IDIwMTYxMDE0MTUwOTE5WgotCg==
   ```

   > **Collapse: Show output**
   >
   > ```
   > replace: description
   > description: New, improved description
   > -
   > replace: modifiersName
   > modifiersName: uid=bjensen,ou=People,dc=example,dc=com
   > -
   > replace: modifyTimestamp
   > modifyTimestamp: <timestamp>
   > -
   > ```

3. If you lose the cookie, start over from the earliest available change by sending a request with no cookie.

---

---
title: Passwords and accounts
description: "Manage PingDS passwords and accounts: reset or change passwords, check password quality, and read account usability and policy state."
component: pingds
version: 8.1
page_id: pingds:ldap-guide:passwords-and-accounts
canonical_url: https://docs.pingidentity.com/pingds/8.1/ldap-guide/passwords-and-accounts.html
llms_txt: https://docs.pingidentity.com/pingds/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2025-10-22T14:42:39Z
keywords: ["Authentication", "LDAP"]
page_aliases: ["change-password.adoc"]
section_ids:
  password-reset: Reset a password
  change-own-password: Change your password
  password-quality-check: Check password quality
  non-ascii-password: Passwords with special characters
  ldap-read-pwp-state: Read password policy state
  ldap-action-account-usability: Check account usability
---

# Passwords and accounts

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Examples in this documentation depend on features activated in [the `ds-evaluation` setup profile](../install-guide/setup-ds.html#about-ds-evaluation).The code samples demonstrate how to contact the server over HTTPS using the deployment CA certificate. Before trying the samples, generate the CA certificate in PEM format from the server deployment ID and password:```console
$ dskeymgr \
 export-ca-cert \
 --deploymentId $DEPLOYMENT_ID \
 --deploymentIdPassword password \
 --outputFile ca-cert.pem
``` |

The `ldappasswordmodify` command lets authorized users change their own passwords and reset other users' passwords.

## Reset a password

Whenever one user changes another user's password, DS servers consider it a password reset. Often password policies specify that users must change their passwords again after a password reset.

Assume password administrator Kirsten Vaughan has the `password-reset` privilege. The following example shows Kirsten resetting Andy Hall's password:

```console
$ ldappasswordmodify \
 --hostname localhost \
 --port 1636 \
 --useSsl \
 --trustStorePath /path/to/opendj/config/keystore \
 --trustStoreType PKCS12 \
 --trustStorePassword:file /path/to/opendj/config/keystore.pin \
 --bindDN "uid=kvaughan,ou=people,dc=example,dc=com" \
 --bindPassword bribery \
 --authzID "dn:uid=ahall,ou=people,dc=example,dc=com"
```

> **Collapse: Show output**
>
> ```
> The LDAP password modify operation was successful
> Generated Password:  <password>
> ```

> **Collapse: More information**
>
> If a client application performs the LDAP password modify extended operation on a connection that is bound to a user (in other words, when a user first does a bind on the connection, then requests the LDAP Password Modify extended operation), then the operation is performed as the user associated with the connection. If the user associated with the connection is not the same user whose password is being changed, then DS servers consider it a password reset.
>
> To change, rather than reset, the password as the user while binding as an application or an administrator, use the LDAP Password Modify extended operation with an authorization ID. Alternatively, use proxied authorization, as described in [Proxied authorization](proxied-authz.html).

If you reset a password, and do not want it to count as a password reset, use the `manage-account` command with the `set-password-is-reset` hidden option, supported only for testing:

```console
$ manage-account \
 set-password-is-reset \
 --hostname localhost \
 --port 4444 \
 --bindDN uid=admin \
 --bindPassword password \
 --targetDN uid=ahall,ou=people,dc=example,dc=com \
 --operationValue true \
 --trustStorePath /path/to/opendj/config/keystore \
 --trustStoreType PKCS12 \
 --trustStorePassword:file /path/to/opendj/config/keystore.pin
```

## Change your password

Users can change their own passwords with the `ldappasswordmodify` command as long as they know their current password:

```console
$ ldappasswordmodify \
 --hostname localhost \
 --port 1636 \
 --useSsl \
 --trustStorePath /path/to/opendj/config/keystore \
 --trustStoreType PKCS12 \
 --trustStorePassword:file /path/to/opendj/config/keystore.pin \
 --bindDN "uid=ahunter,ou=people,dc=example,dc=com" \
 --bindPassword egregious \
 --newPassword chngthspwd
```

The same operation works for directory superusers, such as `uid=admin`:

```console
$ ldappasswordmodify \
 --hostname localhost \
 --port 1636 \
 --useSsl \
 --trustStorePath /path/to/opendj/config/keystore \
 --trustStoreType PKCS12 \
 --trustStorePassword:file /path/to/opendj/config/keystore.pin \
 --authzID dn:uid=admin \
 --currentPassword password \
 --newPassword OzNOkkfkTJDSW9Bg
```

## Check password quality

The `ldappasswordmodify` and `ldapmodify` commands support password quality advice controls to get additional information about why a password update failed. When you use the request control and a password update fails, the server can send the response control with details indicating which validators rejected the new password.

You can use this as a means to test a password, and to evaluate the effectiveness of a new password policy.

|   |                                                           |
| - | --------------------------------------------------------- |
|   | The new LDAP control has interface stability: *Evolving*. |

The following commands demonstrate how the tools show the information from the response control:

```console
$ ldapmodify \
 --hostname localhost \
 --port 1636 \
 --useSsl \
 --trustStorePath /path/to/opendj/config/keystore \
 --trustStoreType PKCS12 \
 --trustStorePassword:file /path/to/opendj/config/keystore.pin \
 --bindDN uid=admin \
 --bindPassword password << EOF
dn: dc=example,dc=com
changetype: modify
add: aci
aci: (targetcontrol="PasswordQualityAdvice") (version 3.0; acl
  "Authenticated users can check password quality";
  allow(read) userdn="ldap:///all";)
EOF
$ ldapmodify \
 --hostname localhost \
 --port 1636 \
 --useSsl \
 --trustStorePath /path/to/opendj/config/keystore \
 --trustStoreType PKCS12 \
 --trustStorePassword:file /path/to/opendj/config/keystore.pin \
 --bindDN uid=admin \
 --bindPassword password << EOF
dn: cn=Minimum length policy,dc=example,dc=com
objectClass: top
objectClass: subentry
objectClass: ds-pwp-password-policy
objectClass: ds-pwp-validator
objectClass: ds-pwp-length-based-validator
cn: Minimum length policy
ds-pwp-password-attribute: userPassword
ds-pwp-default-password-storage-scheme: PBKDF2-HMAC-SHA512
ds-pwp-length-based-min-password-length: 8
subtreeSpecification: {base "ou=people", specificationFilter "(uid=pshelton)" }
EOF
$ ldappasswordmodify \
 --hostname localhost \
 --port 1636 \
 --useSsl \
 --trustStorePath /path/to/opendj/config/keystore \
 --trustStoreType PKCS12 \
 --trustStorePassword:file /path/to/opendj/config/keystore.pin \
 --bindDN uid=pshelton,ou=People,dc=example,dc=com \
 --bindPassword nosedive \
 --control PasswordQualityAdvice:true \
 --control NoOp \
 --newPassword passwd
```

> **Collapse: Show output**
>
> ```
> The LDAP password modify operation failed: 19 (Constraint Violation)
> Additional Information:  The provided new password failed the validation checks defined in the server: The provided
> password is shorter than the minimum required length of 8 characters
>
> The new password was rejected by the password policy located in "cn=Minimum length policy,dc=example,dc=com"
>
> The following password quality criteria were not satisfied:
> * length-based with parameters {max-password-length=0, min-password-length=8}
> ```

Notice that the check can be performed as a no-op.

## Passwords with special characters

DS servers expect passwords to be UTF-8 encoded and base64-encoded when included in LDIF. UTF-8 characters such as `à` or `ô` must be correctly encoded:

```console
$ export LANG=en_US.UTF-8
$ ldappasswordmodify \
 --hostname localhost \
 --port 1636 \
 --useSsl \
 --trustStorePath /path/to/opendj/config/keystore \
 --trustStoreType PKCS12 \
 --trustStorePassword:file /path/to/opendj/config/keystore.pin \
 --bindDN uid=wlutz,ou=People,dc=example,dc=com \
 --bindPassword bassinet \
 --newPassword pàsswȏrd
$ ldapsearch \
 --hostname localhost \
 --port 1636 \
 --useSsl \
 --trustStorePath /path/to/opendj/config/keystore \
 --trustStoreType PKCS12 \
 --trustStorePassword:file /path/to/opendj/config/keystore.pin \
 --bindDN uid=wlutz,ou=People,dc=example,dc=com \
 --bindPassword pàsswȏrd \
 --baseDN dc=example,dc=com \
 "(uid=wlutz)" \
 1.1
```

> **Collapse: Show output**
>
> ```
> dn: uid=wlutz,ou=People,dc=example,dc=com
> ```

## Read password policy state

DS servers have a password policy state virtual attribute enabled by default. It provides information similar to the `manage-account get-all` command.

Accounts with access to read the operational attribute `ds-pwp-state-json` get information from the following fields. Many of the fields only appear when the situation requires:

| Field                                          | Description                                                                           |
| ---------------------------------------------- | ------------------------------------------------------------------------------------- |
| `account-expiration-time`                      | Expiration time                                                                       |
| `account-is-disabled`                          | Boolean                                                                               |
| `account-is-expired`                           | Boolean                                                                               |
| `account-is-idle-locked`                       | Boolean                                                                               |
| `account-is-reset-locked`                      | Boolean, `true` if the password was not changed soon enough after reset               |
| `account-is-usable`                            | Boolean                                                                               |
| `authentication-failure-times`                 | Authentication failure times                                                          |
| `current-authentication-failure-count`         | Number of recorded authentication failures                                            |
| `expire-passwords-without-warning`             | Boolean                                                                               |
| `failure-lockout-count`                        | Maximum number of authentication failures allowed before lockout                      |
| `failure-lockout-expiration-interval`          | Duration in seconds of account lockout after too many authentication failures         |
| `force-change-on-add`                          | Boolean, `true` when the password must change immediately after DS adds the account   |
| `force-change-on-reset`                        | Boolean, `true` when the password must change after another user resets it            |
| `grace-login-use-times`                        | Grace login times                                                                     |
| `idle-lockout-interval-seconds`                | Maximum seconds an account can remain idle (no recent authentications) before lockout |
| `idle-lockout-time`                            | Time account locks for being idle (no recent authentications)                         |
| `idle-lockout`                                 | Seconds until the account locks for being idle                                        |
| `is-within-minimum-password-age`               | Boolean, whether the password is too new to change                                    |
| `last-login-time`                              | Time of the last successful authentication                                            |
| `max-password-reset-age-seconds`               | Maximum seconds to change the password after reset                                    |
| `maximum-grace-login-count`                    | Number of grace logins allowed after expiration to set a new password                 |
| `maximum-password-age-seconds`                 | Maximum seconds the password can remain the same                                      |
| `maximum-password-history-count`               | Maximum number of records allowed in the account's list of old password               |
| `maximum-password-history-duration-seconds`    | Maximum number of seconds DS retains old passwords                                    |
| `minimum-password-age-expiration-time`         | Time the password is old enough to change                                             |
| `minimum-password-age-seconds`                 | Minimum seconds between password changes                                              |
| `must-change-password`                         | Boolean, `true` when the password must change as the next action on the account       |
| `password-change-time`                         | Time the password changed                                                             |
| `password-expiration-time`                     | Time the password expires                                                             |
| `password-expiration-warning-interval-seconds` | Seconds before bind responses include expiry notifications                            |
| `password-expiration-warning-issued`           | Boolean, `true` if DS has returned a notification about expiry                        |
| `password-expiration-warning-time`             | Time DS first returned a notification about expiry                                    |
| `password-expiration-warning`                  | Seconds ago DS first returned a notification about expiry                             |
| `password-expiration`                          | Seconds until the password expires                                                    |
| `password-is-expired`                          | Boolean                                                                               |
| `password-policy-dn`                           | The password policy governing the current account                                     |
| `recent-login-history`                         | Array, times of the last successful authentications                                   |
| `remaining-authentication-failure-count`       | Number, difference between the maximum and current authentication failures            |
| `remaining-grace-login-count`                  | Number, difference between the maximum and used grace login count                     |
| `require-secure-authentication`                | Boolean, `true` when authentication must prevent exposing the credentials             |
| `require-secure-password-changes`              | Boolean, `true` when password changes must prevent exposing the credentials           |
| `reset-lockout-time`                           | Time the account locks after reset unless the password changes                        |
| `seconds-remaining-in-failure-lockout`         | Number of seconds before the locked account unlocks                                   |
| `seconds-remaining-in-minimum-password-age`    | Seconds until the password is old enough to change                                    |
| `seconds-since-account-expiration`             | Seconds since the account expired                                                     |
| `seconds-since-idle-lockout`                   | Seconds since the account locked for being idle (no recent authentications)           |
| `seconds-since-last-login`                     | Seconds since the last successful authentication                                      |
| `seconds-since-password-change`                | Seconds since the password changed                                                    |
| `seconds-since-password-expiration-warning`    | Seconds since DS sent the first bind response with an expiry notification             |
| `seconds-since-password-expiration`            | Seconds since the password expired                                                    |
| `seconds-until-account-expiration`             | Seconds until the account expires                                                     |
| `seconds-until-idle-lockout`                   | Seconds until the account locks for being idle (no recent authentications)            |
| `seconds-until-password-expiration-warning`    | Seconds until DS starts sending bind responses with expiry notifications              |
| `seconds-until-password-expiration`            | Seconds until the password expires                                                    |
| `seconds-until-reset-lockout`                  | Seconds until the account locks after reset unless the password changes               |
| `used-grace-login-count`                       | Number of recorded grace logins                                                       |

To read the attribute:

1. Make sure the reader has access:

   ```console
   $ ldapmodify \
    --hostname localhost \
    --port 1636 \
    --useSsl \
    --trustStorePath /path/to/opendj/config/keystore \
    --trustStoreType PKCS12 \
    --trustStorePassword:file /path/to/opendj/config/keystore.pin \
    --bindDN uid=admin \
    --bindPassword password << EOF
   dn: dc=example,dc=com
   changetype: modify
   add: aci
   aci: (targetattr="ds-pwp-state-json")(version 3.0;
     acl "Read pwp state"; allow (read,search,compare)
     userdn="ldap:///uid=kvaughan,ou=people,dc=example,dc=com";)
   EOF
   ```

2. Read the attribute on an account:

   ```console
   $ ldapsearch \
    --hostname localhost \
    --port 1636 \
    --useSsl \
    --trustStorePath /path/to/opendj/config/keystore \
    --trustStoreType PKCS12 \
    --trustStorePassword:file /path/to/opendj/config/keystore.pin \
    --bindDN uid=kvaughan,ou=people,dc=example,dc=com \
    --bindPassword bribery \
    --baseDN dc=example,dc=com \
    "(uid=bjensen)" \
    ds-pwp-state-json
   ```

   > **Collapse: Show output**
   >
   > ```
   > dn: uid=bjensen,ou=People,dc=example,dc=com
   > ds-pwp-state-json: { "require-secure-authentication": true, "password-policy-dn": "cn=Default Password Policy,cn=Password Policies,cn=config", "force-change-on-reset": false, "account-is-expired": false, "account-is-idle-locked": false, "account-is-disabled": false, "account-is-reset-locked": false, "must-change-password": false, "password-is-expired": false, "is-within-minimum-password-age": false, "account-is-usable": true, "require-secure-password-changes": true, "force-change-on-add": false }
   > ```

## Check account usability

The [account usability control](../ldap-reference/controls.html#account-usability-control) lets a password administrator read information about whether the user can authenticate to the directory:

* The remote LDAP directory service must support the LDAP control, which has OID `1.3.6.1.4.1.42.2.27.9.5.8`.

* The password administrator must be able to use the LDAP control.

To try the account usability control:

1. Enable the password administrator to use the LDAP account usability control.

   The following example sets a global access control instruction (ACI) *(tooltip: \<div class="paragraph">
   \<p>An instruction or rule that can be used to grant or deny access to users to perform operations on a server.\</p>
   \</div>)* for Kirsten Vaughan:

   ```console
   $ dsconfig \
    set-access-control-handler-prop \
    --hostname localhost \
    --port 4444 \
    --bindDN uid=admin \
    --bindPassword password \
    --add global-aci:"(targetcontrol=\"AccountUsability\")\
    (version 3.0; acl \"Account usability access\"; allow(read) \
    userdn=\"ldap:///uid=kvaughan,ou=People,dc=example,dc=com\";)" \
    --trustStorePath /path/to/opendj/config/keystore \
    --trustStoreType PKCS12 \
    --trustStorePassword:file /path/to/opendj/config/keystore.pin \
    --no-prompt
   ```

2. Use a password policy that produces results for account usability, as in the following example:

   ```console
   $ ldapmodify \
    --hostname localhost \
    --port 1636 \
    --useSsl \
    --trustStorePath /path/to/opendj/config/keystore \
    --trustStoreType PKCS12 \
    --trustStorePassword:file /path/to/opendj/config/keystore.pin \
    --bindDN uid=admin \
    --bindPassword password << EOF
   dn: cn=Lockout with max age and grace logins,dc=example,dc=com
   objectClass: top
   objectClass: subentry
   objectClass: ds-pwp-password-policy
   cn: Lockout with max age and grace logins
   ds-pwp-password-attribute: userPassword
   ds-pwp-default-password-storage-scheme: PBKDF2-HMAC-SHA256
   ds-pwp-lockout-failure-expiration-interval: 10 m
   ds-pwp-grace-login-count: 3
   ds-pwp-lockout-duration: 5 m
   ds-pwp-lockout-failure-count: 3
   ds-pwp-max-password-age: 30 d
   subtreeSpecification: { base "ou=people", specificationFilter "(uid=bjensen)" }
   EOF
   ```

3. Use the account usability control to get information about an account:

   ```console
   $ ldapsearch \
    --hostname localhost \
    --port 1636 \
    --useSsl \
    --trustStorePath /path/to/opendj/config/keystore \
    --trustStoreType PKCS12 \
    --trustStorePassword:file /path/to/opendj/config/keystore.pin \
    --bindDN uid=kvaughan,ou=people,dc=example,dc=com \
    --bindPassword bribery \
    --baseDN dc=example,dc=com \
    --control AccountUsability:true \
    "(uid=bjensen)" \
    1.1
   ```

   > **Collapse: Show output**
   >
   > ```
   > # Account Usability Response Control
   > # The account is usable
   > # Time until password expiration:  <time>
   > dn: uid=bjensen,ou=People,dc=example,dc=com
   > ```

4. Perform actions to change the account usability information on the account:

   ```console
   $ ldapsearch \
    --hostname localhost \
    --port 1636 \
    --useSsl \
    --trustStorePath /path/to/opendj/config/keystore \
    --trustStoreType PKCS12 \
    --trustStorePassword:file /path/to/opendj/config/keystore.pin \
    --bindDN uid=bjensen,ou=people,dc=example,dc=com \
    --bindPassword wrong-password \
    --baseDN dc=example,dc=com \
    "(uid=bjensen)" \
    1.1
   $ ldapsearch \
    --hostname localhost \
    --port 1636 \
    --useSsl \
    --trustStorePath /path/to/opendj/config/keystore \
    --trustStoreType PKCS12 \
    --trustStorePassword:file /path/to/opendj/config/keystore.pin \
    --bindDN uid=bjensen,ou=people,dc=example,dc=com \
    --bindPassword wrong-password \
    --baseDN dc=example,dc=com \
    "(uid=bjensen)" \
    1.1
   $ ldapsearch \
    --hostname localhost \
    --port 1636 \
    --useSsl \
    --trustStorePath /path/to/opendj/config/keystore \
    --trustStoreType PKCS12 \
    --trustStorePassword:file /path/to/opendj/config/keystore.pin \
    --bindDN uid=bjensen,ou=people,dc=example,dc=com \
    --bindPassword wrong-password \
    --baseDN dc=example,dc=com \
    "(uid=bjensen)" \
    1.1
   ```

5. Use the account usability control again to get the changes:

   ```console
   $ ldapsearch \
    --hostname localhost \
    --port 1636 \
    --useSsl \
    --trustStorePath /path/to/opendj/config/keystore \
    --trustStoreType PKCS12 \
    --trustStorePassword:file /path/to/opendj/config/keystore.pin \
    --bindDN uid=kvaughan,ou=people,dc=example,dc=com \
    --bindPassword bribery \
    --baseDN dc=example,dc=com \
    --control AccountUsability:true \
    "(uid=bjensen)" \
    1.1
   ```

   > **Collapse: Show output**
   >
   > ```
   > # Account Usability Response Control
   > # The account is not usable
   > # The account is locked
   > # Time until the account is unlocked:  <time>
   > ```

---

---
title: Proxied authorization
description: Configure PingDS proxied authorization to allow a proxy to make LDAP requests on behalf of other users per RFC 4370.
component: pingds
version: 8.1
page_id: pingds:ldap-guide:proxied-authz
canonical_url: https://docs.pingidentity.com/pingds/8.1/ldap-guide/proxied-authz.html
llms_txt: https://docs.pingidentity.com/pingds/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2025-10-22T14:42:39Z
keywords: ["Authorization", "LDAP"]
---

# Proxied authorization

Proxied authorization, defined in [RFC 4370](https://www.rfc-editor.org/info/rfc4370), provides a mechanism for binding as a proxy, and making requests on behalf of other users. For example, an application binds with its credentials, but each request is made as a user who logs in through the application.

To use proxied authorization, the proxy user must have:

* Permission to use the LDAP Proxy Authorization Control.

  Grant access to this control using an access control instruction (ACI) *(tooltip: \<div class="paragraph">
  \<p>An instruction or rule that can be used to grant or deny access to users to perform operations on a server.\</p>
  \</div>)* with a `targetcontrol` list that includes the Proxy Authorization Control OID `ProxiedAuthV2` (`2.16.840.1.113730.3.4.18`). The ACI must grant `allow(read)` permission to the proxy.

  This calls for an ACI with a target scope that includes the entry of the proxy user binding to the directory.

* Permission to proxy as the given authorization user.

  This calls for an ACI with a target scope that includes the entry of the authorization user. The ACI must grant `allow(proxy)` permission to the proxy.

* The privilege to use proxied authorization.

  Add `ds-privilege-name: proxied-auth` to the proxy's entry.

The following table shows whether proxied authorization allows an operation on the target.

|                         | Bind DN no access | Bind DN has access |
| ----------------------- | ----------------- | ------------------ |
| **Proxy ID no access**  | No                | No                 |
| **Proxy ID has access** | Yes               | Yes                |

The following steps rely on the access settings available in the evaluation setup profile, described in [Learn about the evaluation setup profile](../install-guide/setup-ds.html#about-ds-evaluation), to demonstrate proxied authorization for an Example.com application. In the evaluation profile, `kvaughan` is a directory administrator user with access to modify `bjensen`'s entry.

If you are using a different profile, make sure you have granted access to the bind DN user and the proxy ID user:

1. Grant access to applications to use the Proxy Authorization control, and to use proxied authorization:

   ```console
   $ ldapmodify \
    --hostname localhost \
    --port 1636 \
    --useSsl \
    --trustStorePath /path/to/opendj/config/keystore \
    --trustStoreType PKCS12 \
    --trustStorePassword:file /path/to/opendj/config/keystore.pin \
    --bindDN uid=admin \
    --bindPassword password << EOF
   dn: dc=example,dc=com
   changetype: modify
   add: aci
   aci: (targetcontrol="ProxiedAuthV2")
     (version 3.0; acl "Apps can use the Proxy Authorization Control";
     allow(read) userdn="ldap:///cn=*,ou=Apps,dc=example,dc=com";)
   aci: (target="ldap:///dc=example,dc=com") (targetattr ="*")
     (version 3.0; acl "Allow apps proxied auth";
     allow(proxy) (userdn = "ldap:///cn=*,ou=Apps,dc=example,dc=com");)
   EOF
   ```

   The latter ACI allows any user whose DN matches `cn=*,ou=Apps,dc=example,dc=com` to proxy as any user under the ACI target of `dc=example,dc=com`. For example, `cn=My App,ou=Apps,dc=example,dc=com` can proxy as any Example.com user, but cannot proxy as the directory superuser `uid=admin`. The target of the ACI does not include `uid=admin`.

2. Grant My App the privilege to use proxied authorization:

   ```console
   $ ldapmodify \
    --hostname localhost \
    --port 1636 \
    --useSsl \
    --trustStorePath /path/to/opendj/config/keystore \
    --trustStoreType PKCS12 \
    --trustStorePassword:file /path/to/opendj/config/keystore.pin \
    --bindDN uid=admin \
    --bindPassword password << EOF
   dn: cn=My App,ou=Apps,dc=example,dc=com
   changetype: modify
   add: ds-privilege-name
   ds-privilege-name: proxied-auth
   EOF
   ```

   Other applications without this privilege cannot yet use proxied authorization.

3. Test that My App can use proxied authorization:

   ```console
   $ ldapmodify \
    --hostname localhost \
    --port 1636 \
    --useSsl \
    --trustStorePath /path/to/opendj/config/keystore \
    --trustStoreType PKCS12 \
    --trustStorePassword:file /path/to/opendj/config/keystore.pin \
    --bindDN "cn=My App,ou=Apps,dc=example,dc=com" \
    --bindPassword password \
    --proxyAs "dn:uid=kvaughan,ou=People,dc=example,dc=com" << EOF
   dn: uid=bjensen,ou=People,dc=example,dc=com
   changetype: modify
   replace: description
   description: Changed through proxied auth
   EOF
   ```

   > **Collapse: Show output**
   >
   > ```
   > # MODIFY operation successful for DN uid=bjensen,ou=People,dc=example,dc=com
   > ```

Use an identity mapper if identifiers have the `u:authzid` (user ID) form rather than `dn:authzid` form. Specify the identity mapper with the global configuration setting, `proxied-authorization-identity-mapper`.

For details, refer to [Identity mappers](client-auth.html#client-auth-identity-mappers).

---

---
title: Use LDAP
description: Landing page for the PingDS LDAP guide, covering tools, authentication, searches, comparisons, updates, and password management.
component: pingds
version: 8.1
page_id: pingds:ldap-guide:preface
canonical_url: https://docs.pingidentity.com/pingds/8.1/ldap-guide/preface.html
llms_txt: https://docs.pingidentity.com/pingds/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2025-10-22T14:42:39Z
keywords: ["LDAP"]
page_aliases: ["index.adoc"]
---

# Use LDAP

These pages show you how to use DS LDAP features and command-line tools.

[icon: wrench, set=fas, size=3x]

#### [Tools](about-tools.html)

Find DS tools.

[icon: id-card, set=fas, size=3x]

#### [Authentication](client-auth.html)

Understand LDAP binds.

[icon: search, set=fas, size=3x]

#### [Searches](search-ldap.html)

Look up DS entries.

[icon: equals, set=fas, size=3x]

#### [Comparisons](compare-ldap.html)

Compare LDAP attributes.

[icon: edit, set=fas, size=3x]

#### [Updates](write-ldap.html)

Add, modify, rename, delete.

[icon: user-secret, set=fas, size=3x]

#### [Passwords](change-password.html)

Manage passwords.