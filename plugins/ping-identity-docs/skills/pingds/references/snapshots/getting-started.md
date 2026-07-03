---
title: About directories
description: Introduction to LDAP directory concepts including data model, communication, controls, indexes, schema, access control, replication, and HTTP access.
component: pingds
version: 8.1
page_id: pingds:getting-started:directory-services
canonical_url: https://docs.pingidentity.com/pingds/8.1/getting-started/directory-services.html
llms_txt: https://docs.pingidentity.com/pingds/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2025-10-22T14:42:39Z
keywords: ["Evaluation", "LDAP"]
section_ids:
  ldap-directory-history: LDAP history
  directory-data: LDAP data
  ldap-client-server-communication: Communication
  standard-ldap-controls-extensions: Controls and extensions
  about-directory-indexes: Indexes
  schema-overview: Schema
  about-access-control: Access control
  about-replication: Replication
  automated_conflict_resolution: Automated conflict resolution
  scaling_up: Scaling up
  eventual_consistency: Eventual consistency
  rest-and-ldap: HTTP access
  about-building-directory-services: Deployment
---

# About directories

A directory resembles a dictionary. If you know a word, you can look up its entry in the dictionary to learn its definition or its pronunciation. If you are bored, curious, or have lots of time, you can also read through the dictionary or the directory.

Where a directory differs from a paper dictionary is in how entries are indexed. Dictionaries typically have only one method of indexation: alphabetical order. In contrast, directories index multiple attributes of their entries. They have indexes names, user identifiers, email addresses, and telephone numbers. You can look up a directory entry by any of these attributes.

PingDS implements the Lightweight Directory Access Protocol (LDAP) *(tooltip: \<div class="paragraph">
\<p>An open, cross-platform protocol used for interacting with directory services.\</p>
\</div>)*. Nearly all of what follows is an introduction to LDAP.

PingDS also provides HTTP access to directory data. It helps to understand the underlying LDAP model whether you use HTTP or LDAP.

## LDAP history

Phone companies have been managing directories for many decades. The internet itself has relied on distributed directory services like DNS since the mid-1980s.

In the late 1980s, experts from what is now the International Telecommunications Union published the X.500 directory standards (X.500) *(tooltip: \<div class="paragraph">
\<p>A family of standardized protocols for accessing, browsing, and maintaining a directory, predating LDAP.\</p>
\</div>)* set of international standards, including the Directory Access Protocol (DAP). The X.500 standards specify Open Systems Interconnect (OSI) protocols and data definitions for general purpose directory services. The X.500 standards were designed to meet the needs of systems built according to the X.400 standards, covering electronic mail services.

LDAP was developed in the early 1990s. LDAP was developed as an alternative for directory access over internet protocols (TCP/IP) rather than OSI protocols. TCP/IP is lightweight enough for desktop implementations. By the mid-1990s, LDAP directory servers were widely used.

LDAP directory servers replicate data. If one server goes down, lookups can continue on other servers. Until the late 1990s, LDAP servers were designed primarily for fast, highly available lookups. If the service needs to support more lookups, you add another replicated directory server.

As organizations rolled out bigger directories for more applications, they also needed fast, highly available updates. Around the year 2000, directories began to support replication with multiple read-write servers. After an update on one server, the service replays it on other peer servers. Adding more servers doesn't make updates faster because each server must replay each update. The organizations with the very largest directories had trouble replicating all the changes fast enough.

The DS code base began in the mid-2000s when engineers decided the cost of adapting the existing C-based directory technology for high-performance updates would be higher than the cost of building new, high-performance directory using Java technology.

## LDAP data

LDAP directory data is organized into entries, similar to the entries for words in the dictionary. LDAP entries usually hold identity data:

```ldif
dn: uid=bjensen,ou=People,dc=example,dc=com
uid: bjensen
cn: Babs Jensen
cn: Barbara Jensen
facsimileTelephoneNumber: +1 408 555 1992
gidNumber: 1000
givenName: Barbara
homeDirectory: /home/bjensen
l: San Francisco
mail: bjensen@example.com
objectClass: inetOrgPerson
objectClass: organizationalPerson
objectClass: person
objectClass: posixAccount
objectClass: top
ou: People
ou: Product Development
roomNumber: 0209
sn: Jensen
telephoneNumber: +1 408 555 1862
uidNumber: 1076
```

Barbara Jensen's entry has a number of attributes, such as `uid: bjensen`, `telephoneNumber: +1 408 555 1862`, and `objectClass: posixAccount`. (The `objectClass` attribute type indicates the required and optional attributes for the entry. You can update object classes online and change the definitions of object classes and attributes. Unlike many databases, directories let you extend the schema for the data while they're running.) When you look up Babs's entry in the directory, you specify one or more attributes and values to match. The directory server finds matching entries using one more of its indexes, returning them as it finds them.

Attribute values are not necessarily strings. Some attribute values, like certificates and photos, are binary.

Each entry has a unique identifier. The previous example shows the identifier at the top of the entry, `dn: uid=bjensen,ou=People,dc=example,dc=com`. DN is an acronym for *Distinguished Name*. No two entries in the directory have the same DN.

You must escape some characters when using them in DNs. The following example shows an entry with escaped characters in the DN:

* Bash

* PowerShell

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
 "(uid=escape)"
```

> **Collapse: Show output**
>
> ```
> dn: cn=DN Escape Characters \" \# \+ \, \; \< = \> \\,dc=example,dc=com
> objectClass: person
> objectClass: inetOrgPerson
> objectClass: organizationalPerson
> objectClass: top
> givenName: DN Escape Characters
> uid: escape
> cn: DN Escape Characters " # + , ; < = > \
> sn: " # + , ; < = > \
> mail: escape@example.com
> ```

```powershell
ldapsearch.bat `
 --hostname localhost `
 --port 1636 `
 --useSsl `
 --trustStorePath C:\path\to\opendj\config\
 --trustStoreType PKCS12 \keystore `
 --trustStorePassword:file C:\path\to\opendj\config\keystore.pin `
 --bindDN uid=kvaughan,ou=People,dc=example,dc=com `
 --bindPassword bribery `
 --baseDN dc=example,dc=com `
 "(uid=escape)"
```

> **Collapse: Show output**
>
> ```
> dn: cn=DN Escape Characters \" \# \+ \, \; \< = \> \\,dc=example,dc=com
> objectClass: person
> objectClass: inetOrgPerson
> objectClass: organizationalPerson
> objectClass: top
> givenName: DN Escape Characters
> uid: escape
> cn: DN Escape Characters " # + , ; < = > \
> sn: " # + , ; < = > \
> mail: escape@example.com
> ```

LDAP entries are arranged hierarchically in the directory. The hierarchical organization resembles a file system on a PC or a web server. Some illustrations picture this as an upside down tree structure or a pyramid. The DN consists of components separated by commas, `uid=bjensen,ou=People,dc=example,dc=com`. The names are little-endian. The components reflect the hierarchy of directory entries.

![Hierarchical directory data view](../_images/directory-data.png)

Barbara Jensen's entry is located under an entry with DN `ou=People,dc=example,dc=com`. This is the organizational unit (OU) and parent entry for the people at Example.com. The `ou=People` entry is under `dc=example,dc=com`, the base entry for Example.com. DC is an acronym for *Domain Component*. The directory has other base entries, such as `cn=config` for the server configuration.

A directory can serve multiple organizations, too. You might find `dc=example,dc=com`, `dc=mycompany,dc=com`, and `o=myOrganization` in the same LDAP directory. When you look up entries, you specify the base DN to look under in the same way you need to know whether to look in an English or a French dictionary for a given word.

The root entry for the directory, technically the entry with DN `""` (the empty string), is called the *root DSE*. It contains information about what the server supports and the base DNs it serves.

A directory server stores two kinds of attributes in a directory entry: user attributes *(tooltip: \<div class="paragraph">
\<p>An attribute for storing user or application data on a directory entry.\</p>
\</div>)* and operational attributes *(tooltip: \<div class="paragraph">
\<p>An attribute with a special, operational meaning for the server, not returned in searches by default.\</p>
\</div>)*. User attributes hold the information for users of the directory. All attributes shown in the entry above are user attributes. Operational attributes hold information used by the directory itself. Examples of operational attributes include `entryUUID`, `modifyTimestamp`, and `subschemaSubentry`.

When an LDAP search operation finds an entry in the directory, the directory server returns all the visible user attributes unless the search request restricts the list of attributes by specifying those attributes explicitly. The directory server doesn't return any operational attributes unless the search request specifically asks for them.

Generally speaking, applications should change only user attributes and leave updates of operational attributes to the server. Use the public server interfaces and commands to change server behavior. An exception is access control instruction (ACI) *(tooltip: \<div class="paragraph">
\<p>An instruction or rule that can be used to grant or deny access to users to perform operations on a server.\</p>
\</div>)* (`aci`) attributes. ACIs are operational attributes that control access to directory data.

## Communication

Most HTTP applications connect to the server for each request and close the connection after the response comes.

LDAP has a different model. In LDAP, the client application connects to the server and authenticates. The client then requests any number of operations, perhaps processing results in between requests. The client finally disconnects when done, potentially days later.

The standard operations are as follows:

* Bind (authenticate)

  The first operation in an LDAP session usually involves the client binding to the LDAP server with the server authenticating the client.

  Authentication identifies the client's identity in LDAP terms, the identity the server uses to authorize access to directory data the client wants to read or change.

  If the client does not bind explicitly, the server treats the client as an anonymous client. What the server lets anonymous users do depends on access control and configuration settings.

  The client can bind again (rebind) on the same connection.

* Search (lookup)

  After binding, the client can look up entries under a specified base DN matching an LDAP filter. For example, to look up people with the email address `bjensen@example.com` at Example.com, you specify `ou=People,dc=example,dc=com` as the base DN and `(mail=bjensen@example.com)` as the LDAP filter.

* Compare

  After binding, the client can compare a specified attribute value with the value stored on an entry in the directory.

* Modify

  After binding, the client can change one or more attribute values on an entry. Administrators usually restrict the attributes client applications can change.

* Add

  After binding, the client can add one or more new LDAP entries to the server assuming it has access to do so.

* Delete

  After binding, the client can delete one or more entries assuming it has access to do so. To delete an entry with other entries underneath, first delete the children, then the parent.

* Modify DN

  After binding, the client can change an entry DN assuming it has access to do so. This renames the entry or moves it to another location.

  For example, if Barbara changes her unique identifier from `bjensen` to something else, her DN would have to change. For another example, if you decide to consolidate `ou=Customers` and `ou=Employees` under `ou=People` instead, all the entries underneath must change distinguished names.

  Renaming entire branches of entries can be a major operation for the directory, so avoid moving entire branches if you can.

* Unbind

  When done making requests, the client can request an unbind operation to end the LDAP session.

* Abandon

  When a request takes too long to complete or when a search request returns too many entries, the client can send an abandon request to drop the operation in progress.

  The server doesn't have to send a response and drops the connection without a reply to the client application.

## Controls and extensions

LDAP has standardized two mechanisms for extending what directory servers can do beyond the basic operations:

* LDAP controls

* LDAP extended operations

*LDAP controls* are information added to an LDAP message to specify how an LDAP operation should be processed:

* The server-side sort request control tells the server to return search results in sorted order.

* The subtree delete request control tells the server to remove child entries with the target entry.

* The persistent search control lets the client application get change notifications with an ongoing server. Whenever changes happen in the scope of the search, the server sends additional search results. Persistent searches are "permanent" though they can be idle for long periods of time.

* A directory server can send response controls when the response contains special information. Examples include responses for entry change notification, password policy, and paged results.

For the list of supported LDAP controls, refer to [Supported LDAP controls](../ldap-reference/controls.html).

*LDAP extended operations* are additional LDAP operations not included in the original standard list:

* The cancel extended operation works like an abandon operation with a response from the server.

* The StartTLS extended operation lets you connect on an unsecure port and start Transport Layer Security (TLS) negotiations to protect communications.

For the list of supported LDAP extended operations, refer to [Supported LDAP extended operations](../ldap-reference/extended-ops.html).

## Indexes

Directories have indexes for multiple attributes. By default, DS does not let normal users perform unindexed searches because servers have to scan an entire directory database when looking for matches.

As directory administrator, you make sure directory data is properly indexed. DS software provides tools for building and managing indexes. For details, refer to [Indexes](../config-guide/indexing.html).

## Schema

Some databases hold huge amounts of data per application in an application-specific layout. Although such databases can support multiple applications, data organization depends on the applications served.

In contrast, directories are designed for shared, centralized services. The shared, centralized nature of directory services fosters interoperability in practice. It has helped directory services be successful in the long term.

LDAP schemas make the shared model of directory user information possible. LDAP schemas define the data the directory can contain. Directory entries are not arbitrary objects. Their attributes are completely predictable from publicly readable definitions. Many schema definitions are literally standard and defined by RFCs. They are the same not just across a directory service but across different directory services.

Unlike some databases, a directory service can also LDAP schema updates over LDAP while it is running. This gives you great flexibility in adapting the directory to store new data without changing existing data and without stopping the directory service.

For a closer look, refer to [LDAP schema](../config-guide/schema.html).

## Access control

Directory services support fine-grained access control.

The directory administrator controls who can access specific data and when, how, where, and under what conditions they can do so with access control instructions (ACIs); for example, ACIs let you:

* Permit only specific directory operations.

* Scope controls to apply to the whole directory or to a single entry.

* Specify network conditions and the encryption strength required for an operation.

ACIs are stored on entries in the directory, so you can update access controls while the service is running. You can delegate control over ACIs to client applications. DS software combines ACIs and separate administrative privileges to secure access to directory data.

For more information, read [Access control](../security-guide/access.html).

## Replication

DS replication consists of copying each update to the directory service to multiple directory servers. This brings both redundancy, in the case of network partitions or of crashes, and scalability for read operations. Most directory deployments involve multiple servers replicating together.

### Automated conflict resolution

With writable replicated servers, replication conflicts can arise; for example, two applications write different values to the same attribute on the same entry on the two replicas.

In nearly all cases, DS replication can resolve these situations automatically. This makes the directory service resilient and safe even in the unpredictable real world.

### Scaling up

It's easier to scale a directory service for read operations than for write operations.

To add capacity for read operations, add replicated servers.

Adding servers doesn't scale up write operations because each write operation must be replayed everywhere. If you have N servers, you have N updates to replay.

### Eventual consistency

Replication is *eventually consistent*.

When directory data changes on one server, it eventually converges to be the same everywhere. The data isn't necessarily the same everywhere at any particular time, depending on the rate of changes.

Client applications sometimes get this wrong. They write to a pool of load balanced directory servers, immediately read back what they wrote, and can't tolerate the possible differences. If application users complain about consistency, try mitigating poor application practices with a directory proxy.

## HTTP access

DS software maps LDAP data as JSON resources over HTTP for REST clients (HDAP).

LDAP schemas define the HDAP data model:

* LDAP entries hold sets of attributes, not arbitrarily nested objects.

  Each HDAP resource is an JSON object with fields at the top level:

  ```json
  {
    "_id" : "dc=com/dc=example/ou=People/uid=bjensen",
    "_rev" : "<revision>",
    "mail" : [ "bjensen@example.com" ],
    "cn" : [ "Barbara Jensen", "Babs Jensen" ],
    "sn" : [ "Jensen" ]
  }
  ```

* JSON has arrays, ordered collections that can contain duplicates.

  LDAP attributes are sets, unordered collections without duplicates.

  HDAP arrays have set semantics in which no duplicates are allowed, and the element order is arbitrary.

If you want a field with nested JSON or an array instead of a set, define a `json` syntax attribute. For details, refer to [Schema and JSON](../config-guide/schema.html#json-in-ldap).

You can deploy HDAP as a separate gateway servlet or through an HTTP connection handler on a DS server.

## Deployment

When you have understood enough of the concepts to build directory services, prepare the service and test it thoroughly before you roll out shared, centralized services for your organization.

Start with [Deployment](../deployment-guide/preface.html) when beginning your project.
