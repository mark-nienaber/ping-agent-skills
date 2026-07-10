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

---

---
title: Best practices
description: Best practices for writing effective directory client applications, covering authentication, connection reuse, filters, modifications, and security.
component: pingds
version: 8.1
page_id: pingds:getting-started:best-practices
canonical_url: https://docs.pingidentity.com/pingds/8.1/getting-started/best-practices.html
llms_txt: https://docs.pingidentity.com/pingds/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2025-10-22T14:42:39Z
keywords: ["Evaluation", "LDAP"]
section_ids:
  authenticate-correctly: Authenticate correctly
  reuse-connections: Reuse connections
  health-check-connections: Check connection health
  request-what-you-need-all-at-once: Request exactly what you need all at once
  use-specific-filters: Use specific LDAP filters
  make-modifications-specific: Make modifications specific
  trust-result-codes: Trust result codes
  handle-input-securely: Handle input securely
  ismemberof-for-membership: Check group membership on the account, not the group
  ask-directory-what-it-supports: Check support for features you use
  storing-large-attributes: Store large attribute values by reference
  careful-with-persistent-search-and-server-side-sorting: Take care with persistent search and server-side sorting
  reuse-schemas: Reuse schemas where possible
  initialize-with-server-schemas: Read directory server schemas during initialization
  handle-referrals: Handle referrals
  check-result-codes: "Troubleshooting: check result codes"
  check-log-files: "Troubleshooting: check server logs"
  inspect-network-traffic: "Troubleshooting: inspect network traffic"
---

# Best practices

Follow these best practices for writing effective, maintainable, high-performance directory client applications.

## Authenticate correctly

Unless your application performs only read operations, authenticate to the directory server. Some directory services require authentication *(tooltip: \<div class="paragraph">
\<p>The act of confirming the identity of a principal.\</p>
\</div>)* to read directory data.

Once you authenticate (bind), directory servers make authorization *(tooltip: \<div class="paragraph">
\<p>The act of determining whether to grant or deny a user access to a resource.\</p>
\</div>)* decisions based on your identity. With servers that support proxied authorization, once authenticated, your application can request an operation on behalf of another identity, such as the identity of the end user.

Your application therefore should have an account, such as `cn=My App,ou=Apps,dc=example,dc=com`. The directory administrator can authorize appropriate access for your application's account, and monitor your application's requests to help you troubleshoot problems if they arise.

Applications can use simple, password-based authentication. When using password-based authentication, use secure connections to protect credentials over the network. For applications, prefer certificate-based authentication if possible.

## Reuse connections

LDAP is a stateful protocol. You authenticate (bind), you perform operations, you unbind. The server maintains a context that lets it make authorization decisions concerning your requests. Therefore, reuse connections whenever possible.

Because LDAP supports asynchronous requests, it is normal and expected to make multiple requests over the same connection. Your application can share a pool of connections to avoid the overhead of setting them up and tearing them down.

## Check connection health

In a network built for HTTP applications, your long-lived LDAP connections can get cut by network equipment configured to treat idle and old connections as stale resources to reclaim.

When you maintain a particularly long-lived connection, such as a connection for a persistent search, periodically perform a health check to maintain the connection operational.

A health check involves reading or writing an attribute on a well-known entry in your data. It can serve the purposes of maintaining the connection operational, and of verifying access to your data. A success result for a read indicates that the data is available, and the application can read it. A success result for a write indicates that the data is available, and the application can write to it. The exact check to perform depends on how your application uses the directory. Under some circumstances, your data might be temporarily read-only, for example.

When using a connection timeout, take care not to set the timeout so low that long operations, such as unindexed searches, fail to complete before the timeout.

## Request exactly what you need all at once

By the time your application makes it to production, you should know what attributes you want. Request them explicitly, and request all the attributes in the same search.

For example, if you require `mail` and `cn`, then specify both attributes in your search request.

## Use specific LDAP filters

The difference in results between a general filter `(mail=*@example.com)`, and a good, specific filter like `(mail=user@example.com)` can be huge numbers of entries and enormous amounts of processing time, both for the directory server that has to return search results, and for your application that has to sort through them.

Many use cases can be handled with short, specific filters. As a rule, prefer equality filters over substring filters.

DS servers reject unindexed searches by default, because unindexed searches are resource-intensive. If your application needs to use a filter that results in an unindexed search, work with the directory administrator to find a solution, such as adding the indexes required for your search filters.

Always use `&` with `!` to restrict the potential result set before returning all entries that do not match part of the filter. For example, `(&(location=Oslo)(!(mail=birthday.girl@example.com)))`.

## Make modifications specific

Specific modifications help directory servers apply and replicate your changes more effectively.

When you modify attributes with multiple values, such as a static group member attribute, replace or delete specific values individually, rather than replacing the entire list of values.

## Trust result codes

Trust the LDAP result code from the directory server. For example, if you request a modification, and you get a success result, consider the operation a success. Do not immediately issue a search to get the modified entry.

LDAP replication model is loosely convergent. In other words, the directory server sends you the success result *before* replicating the change to every directory server replica across the network. If you issue a read immediately after a write, a load balancer may direct the request to another replica. The result might differ from what you expect.

The loosely convergent model means that the entry could have changed since you read it. If needed, use LDAP assertions to set conditions for your LDAP operations.

## Handle input securely

When taking input directly from a user or another program, use appropriate methods to sanitize the data. Failure to sanitize the input data can leave your application vulnerable to injection attacks.

For Java applications, the PingDS `format()` methods for filters and DNs *(tooltip: \<div class="paragraph">
\<p>A name uniquely identifying an object within the hierarchy of a directory tree.\</p>
\</div>)* are similar to the Java `String.format()` methods. In addition to formatting the output, they escape the input objects. When building a search filter, use one of the methods of the DS APIs to escape input.

## Check group membership on the account, not the group

Reading an entire large static group entry to check membership is wasteful.

If you need to determine which groups an account belongs to, request the DS virtual attribute, `isMemberOf`, when you read the account entry. Other directory servers use other names for this attribute that identifies the groups to an account belongs to.

## Check support for features you use

Directory servers expose their capabilities as operational attribute values on the root DSE, which is the entry whose DN is an empty string, `""`.

This lets your application discover capabilities at run time, rather than storing configuration separately. Putting effort into checking directory capabilities makes your application easier to deploy and to maintain.

For example, rather than hard-coding `dc=example,dc=com` as a base DN in your configuration, read the root DSE `namingContexts` attribute.

Directory servers also expose their schema over LDAP. The root DSE attribute `subschemaSubentry` shows the DN of the entry for LDAP schema definitions.

## Store large attribute values by reference

To serve results quickly with high availability, directory servers cache content and replicate it everywhere. If you already store large attribute values elsewhere, such as photos or audio messages, keep only a reference to external content in a user's account.

## Take care with persistent search and server-side sorting

A persistent search lets your application receive updates from the server as they happen by keeping the connection open and forcing the server to check whether to return additional results any time it performs a modification in the scope of your search. Directory administrators therefore might hesitate to grant persistent search access to your application.

DS servers expose a change log to let you discover updates with less overhead. If you do have to use a persistent search instead, try to narrow the scope of your search.

DS servers support a resource-intensive, standard operation called server-side sorting. When your application requests a server-side sort, the directory server retrieves all matching entries, sorts the entries in memory, and returns the results. For result sets of any size, server-side sorting ties up server resources that could be used elsewhere. Alternatives include sorting the results after your application receives them, or working with the directory administrator to enable appropriate browsing (virtual list view) indexes for applications that must regularly page through long lists of search results.

## Reuse schemas where possible

DS servers come with schema definitions for a wide range of standard object classes and attribute types. Directories use unique, [IANA](https://www.iana.org/)-registered OIDs *(tooltip: \<div class="paragraph">
\<p>A hierarchical string of digits and dots to uniquely identify an object.\</p>
\</div>)* to avoid object class and attribute type name clashes. The overall goal is Internet-wide interoperability.

Therefore, reuse schema definitions that already exist whenever you reasonably can. Reuse them as is. Do not try to redefine existing schema definitions.

If you must add schema definitions for your application, extend existing object classes with AUXILIARY classes. Take care to name your schemas such that they do not clash with other names.

When you have defined schema required for your application, work with the directory administrator to add your definitions to the directory service. DS servers let directory administrators update schema definitions over LDAP. There is no need to interrupt the service to add your application. Directory administrators can, however, have other reasons why they hesitate to add your schema definitions. Coming to the discussion prepared with good schema definitions, explanations of why they should be added, and evident regard for interoperability makes it easier for the directory administrator to grant your request.

## Read directory server schemas during initialization

By default, PingDS APIs use a minimal, built-in core schema, rather than reading the schema from the server. Doing so automatically would incur a significant performance cost. Unless schemas change, your application only needs to read them once.

When you start your application, read directory server schemas as a one-off initialization step.

Once you have the directory server schema definitions, use them to validate entries.

## Handle referrals

When a directory server returns a search result, the result is not necessarily an entry. If the result is a referral, then your application should follow up with an additional search based on the URIs provided in the result.

## Troubleshooting: check result codes

LDAP result codes are standard, and listed in [LDAP result codes](../ldap-reference/ldap-result-codes.html).

When your application receives a result, it must rely on the result code value to determine what action to take. When the result is not what you expect, read or at least log the additional message information.

## Troubleshooting: check server logs

If you can read the directory server access log, then check what the server did with your application's request. The following excerpt shows a successful search by `cn=My App,ou=Apps,dc=example,dc=com`:

> **Collapse: Show excerpt**
>
> ```json
> {"eventName":"DJ-LDAP","client":{"ip":"<clientIp>","port":12345},"server":{"ip":"<serverIp>","port":1636},"request":{"protocol":"LDAPS","operation":"CONNECT","connId":4},"transactionId":"0","response":{"status":"SUCCESSFUL","statusCode":"0","elapsedTime":0,"elapsedTimeUnits":"MILLISECONDS"},"timestamp":"<timestamp>","_id":"<uuid>"}
> {"eventName":"DJ-LDAP","client":{"ip":"<clientIp>","port":12345},"server":{"ip":"<serverIp>","port":1636},"request":{"protocol":"LDAPS","operation":"TLS","connId":4},"transactionId":"0","response":{"status":"SUCCESSFUL","statusCode":"0","elapsedTime":0,"elapsedTimeUnits":"MILLISECONDS"},"security":{"protocol":"TLSv1.3","cipher":"TLS_AES_128_GCM_SHA256","ssf":128},"timestamp":"<timestamp>","_id":"<uuid>"}
> {"eventName":"DJ-LDAP","client":{"ip":"<clientIp>","port":12345},"server":{"ip":"<serverIp>","port":1636},"request":{"protocol":"LDAPS","operation":"BIND","connId":4,"msgId":1,"version":"3","dn":"cn=My App,ou=Apps,dc=example,dc=com","authType":"SIMPLE"},"transactionId":"<uuid>","response":{"status":"SUCCESSFUL","statusCode":"0","elapsedTime":1,"elapsedQueueingTime":0,"elapsedProcessingTime":1,"elapsedTimeUnits":"MILLISECONDS","additionalItems":{"ssf":128}},"userId":"cn=My App,ou=Apps,dc=example,dc=com","timestamp":"<timestamp>","_id":"<uuid>"}
> {"eventName":"DJ-LDAP","client":{"ip":"<clientIp>","port":12345},"server":{"ip":"<serverIp>","port":1636},"request":{"protocol":"LDAPS","operation":"SEARCH","connId":4,"msgId":2,"dn":"dc=example,dc=com","scope":"sub","filter":"(uid=kvaughan)","attrs":["isMemberOf"]},"transactionId":"<uuid>","response":{"status":"SUCCESSFUL","statusCode":"0","elapsedTime":3,"elapsedQueueingTime":0,"elapsedProcessingTime":3,"elapsedTimeUnits":"MILLISECONDS","nentries":1,"entrySize":430},"userId":"cn=My App,ou=Apps,dc=example,dc=com","timestamp":"<timestamp>","_id":"<uuid>"}
> {"eventName":"DJ-LDAP","client":{"ip":"<clientIp>","port":12345},"server":{"ip":"<serverIp>","port":1636},"request":{"protocol":"LDAPS","operation":"UNBIND","connId":4,"msgId":3},"transactionId":"<uuid>","timestamp":"<timestamp>","_id":"<uuid>"}
> {"eventName":"DJ-LDAP","client":{"ip":"<clientIp>","port":12345},"server":{"ip":"<serverIp>","port":1636},"request":{"protocol":"LDAPS","operation":"DISCONNECT","connId":4},"transactionId":"0","response":{"status":"SUCCESSFUL","statusCode":"0","elapsedTime":0,"elapsedTimeUnits":"MILLISECONDS","reason":"Client Unbind"},"timestamp":"<timestamp>","_id":"<uuid>"}
> ```

Notice these features of the messages:

* The request operation types appear in upper case.

* The messages track the client information and identify the specific sequence of operations with connection ID (`connId`) and message ID (`msgID`) numbers.

* The `elapsedTime` for the response indicates the total time to complete the request. The `elapsedQueueingTime` is the time the request waited in the queue. The `elapsedProcessingTime` is the time actively processing the request.

* A status code 0 corresponds to a successful result, as described in [RFC 4511](https://www.rfc-editor.org/rfc/rfc4511.html#section-4.1.9).

For details about the message format, refer to [Access log format](../logging-guide/about-logs.html#log-common-audit).

## Troubleshooting: inspect network traffic

If result codes and server logs are not enough, many network tools can interpret HTTP and LDAP packets. Install the necessary keys to decrypt encrypted packet content.

---

---
title: Glossary
description: Glossary of directory service terms used across the PingDS documentation.
component: pingds
version: 8.1
page_id: pingds:getting-started:glossary
canonical_url: https://docs.pingidentity.com/pingds/8.1/getting-started/glossary.html
llms_txt: https://docs.pingidentity.com/pingds/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2025-10-22T14:42:39Z
---

# Glossary

* access control

  Control to grant or to deny access to a resource.

* access control instruction (ACI)

  An instruction or rule that can be used to grant or deny access to users to perform operations on a server.

* access control list (ACL)

  A list connecting a user or group of users to one or more security entitlements.

* access log

  A server log tracing the operations the server processes including timestamps, connection information, and information about the operation itself.

* account lockout

  The act of making an account temporarily or permanently inactive after successive authentication failures.

* active user

  A user with valid credentials and the ability to authenticate and use the services.

* approximate index

  Matches values that sound like those provided in the filter.

* attribute value assertion (AVA)

  An attribute description and a matching rule assertion value for the attribute used to determine whether an entry matches the assertion.

* audit log

  A server access log with changes in LDIF format.

* authentication

  The act of confirming the identity of a principal.

* authorization

  The act of determining whether to grant or deny a user access to a resource.

* backend

  A repository to store directory data. Different implementations with different capabilities exist.

* branch

  The distinguished name of a non-leaf entry in the Directory Information Tree and its subordinates.

* certificate authority (CA)

  An entity that issues digital certificates.

* change sequence number (CSN)

  An opaque string uniquely identifying a single change to directory data and when it occurred.

* collective attribute

  A standard mechanism for defining attributes on all the entries in a particular subtree.

* database cache

  Memory space set aside for database content.

* directory information tree (DIT)

  A set of directory entries organized hierarchically in a tree structure.

* directory server agent (DSA)

  A single directory server.

* directory superuser (superuser)

  An account with full administration privileges to bypass access control evaluation, change access controls, and change administrative privileges. Analogous to the Linux root and Windows Administrator accounts.

* distinguished name (DN)

  A name uniquely identifying an object within the hierarchy of a directory tree.

* DSA-specific entry (DSE)

  An entry holding information for use by the directory, not returned in searches by default.

* dynamic group

  A group specifying members with LDAP URLs.

* elapsed time (etime)

  Time to process a request, starting from the moment a worker thread can process the decoded operation.

* entry

  An object in the directory having one of more object classes and their attributes.

* entry cache

  Memory space set aside for frequently accessed, large entries.

* equality index

  Matches values that correspond exactly, optionally for case sensitivity, to those provided in the filter.

* errors log

  A server log tracing server events, error conditions, and warnings, categorized and identified by severity.

* export

  Save directory data to an LDIF file.

* extensible match index

  Matches with a matching rule like generalized time other than approximate, equality, ordering, presence, substring or VLV.

* generation ID

  An initial state identifier for a replication base DN based on the first 1000 entries.

* HDAP gateway

  A standalone HDAP web application.

* HTTP directory access protocol (HDAP)

  The DS feature providing REST APIs and HTTP access to directory data.

* import

  Read in and index directory data from an LDIF file.

* inactive user

  A user who can't authenticate or use the services.

* index

  A backend feature for quick entry lookup based on attribute values.

* index entry limit

  The maximum number of entries listed for an index key, beyond which the server stops maintaining the list for that key.

* LDAP abandon operation (abandon)

  Stop processing a request in progress and drop the connection without a reply to the client application.

* LDAP add operation (add)

  Adds a new entry or entries to the directory.

* LDAP anonymous bind operation (anonymous bind)

  Simple authentication with an empty DN and an empty password, allowing anonymous access like reading public information.

* LDAP attribute (attribute)

  A property of a directory entry, stored as one or more key-value pairs.

* LDAP bind operation (bind)

  Authenticates the client application. The server uses the identity to make authorization decisions.

* LDAP compare operation (compare)

  Compares a specified attribute value with the value stored on an entry in the directory.

* LDAP control (control)

  An addition to an LDAP message to specify how to process the operation.

* LDAP Data Interchange Format (LDIF)

  An IETF standard file format for representing LDAP directory content and modifications to directory content. Typically used to import and export LDAP-based directory information.

* LDAP delete operation (delete)

  Removes an existing entry or entries from the directory.

* LDAP extended operation (extended operation)

  An LDAP operation not included in the original standards.

* LDAP group (group)

  An entry identifying a set of member entries in the directory.

* LDAP modify DN operation (rename)

  Changes the distinguished name of an entry.

* LDAP modify operation (modify)

  Changes one or more attributes of an entry.

* LDAP operational attribute (operational attribute)

  An attribute with a special, operational meaning for the server, not returned in searches by default.

* LDAP schema (schema)

  Definitions of object classes, attributes types, attribute value syntaxes, matching rules, and other constrains on entries.

* LDAP search filter (filter)

  An expression the server uses to find entries matching a search request.

* LDAP search operation (search)

  Return entries based on an LDAP filter, a base DN, and a scope.

* LDAP static group (static group)

  An entry enumerating member entries.

* LDAP subentry (subentry)

  An entry residing with user data but holding operational data, not returned in searches by default.

* LDAP unbind operation (unbind)

  Release resources at the end of a session.

* LDAP Uniform Resource Locator (LDAP URL)

  A standard uniform resource locator for accessing entries in a directory.

* LDAP user attribute (user attribute)

  An attribute for storing user or application data on a directory entry.

* LDAP virtual attribute (virtual attribute)

  An attribute with dynamically generated values not persistently stored in the backend.

* LDAP virtual static group (virtual static group)

  An entry representing dynamic groups as static groups.

* LDAPS

  LDAP over TLS.

* Lightweight Directory Access Protocol (LDAP)

  An open, cross-platform protocol used for interacting with directory services.

* matching rule

  A rule for matching operations against assertion values, associated with attribute syntaxes.

* naming context

  A base DN under which client applications can look for user data.

* object identifier (OID)

  A hierarchical string of digits and dots to uniquely identify an object.

* ordering index

  Matches values for a filter that specifies a range.

* password policy

  A set of rules for sequence of characters constituting an acceptable password.

* password reset

  Password change performed by a user other than the user who owns the entry.

* password storage scheme

  A mechanism for encoding user passwords stored on directory entries.

* password validator

  A mechanism to accept or reject a proposed password.

* presence index

  Matches when an attribute's present on the entry, regardless of the value.

* principal

  Represents a successfully authenticated entity, such as a user, a device, or an application.

* privilege

  A server setting controlling access to an administrative operation.

* referential integrity

  The act of ensuring group membership remains consistent following changes to member entries.

* referint log

  A server log tracing referential integrity events, with entries similar to the errors log.

* referral

  A reference to another directory location where the server can process the current operation.

* relative distinguished name (RDN)

  The initial portion of a DN distinguishing the entry from all others at the same level.

* replica

  A directory server configured to use replication.

* replication

  Data synchronization to ensure all participating servers eventually share a consistent set of directory data.

* root DSA-specific entry (root DSE)

  The entry with an empty string DN ("") exposing information about the directory server itself.

* simple authentication

  Bind with a user's entry DN and password.

* substring index

  Matches values specified with wildcards in the filter.

* suffix

  The DN of a root entry in the DIT and all its subordinate entries taken together as a single object of administrative tasks.

* task

  A mechanism for remote access to server administrative actions.

* unindexed search

  A search operation for which the server has no appropriate index.

* virtual list view index (VLV index)

  Matches browsing requests for paging through a long list of results.

* X.500 directory standards (X.500)

  A family of standardized protocols for accessing, browsing, and maintaining a directory, predating LDAP.

---

---
title: Install DS
description: Download, install, and set up a PingDS server with the evaluation profile for local hands-on exploration.
component: pingds
version: 8.1
page_id: pingds:getting-started:install
canonical_url: https://docs.pingidentity.com/pingds/8.1/getting-started/install.html
llms_txt: https://docs.pingidentity.com/pingds/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2025-12-09T13:43:30Z
keywords: ["Evaluation", "Install", "LDAP"]
section_ids:
  before-you-start: Prepare for installation
  download: Download DS software
  install-server: Install a directory server
---

# Install DS

|   |                                                                                                                                                                                                                                                              |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | DS software has no GUI. Instead, DS software is bundled with command-line tools.Because LDAP is standard, you can use third-party GUI tools to view and edit directory data. For a short list, refer to [Try third-party tools](further.html#further-tools). |

## Prepare for installation

1. To evaluate DS software, make sure you have 10 GB free disk space for the software and for sample data.

2. Verify that you have a supported Java version installed on your local computer.

   Learn more in [Java requirements](https://docs.pingidentity.com/pingds/release-notes/requirements.html#prerequisites-java).

3. If you plan to [Learn HDAP](rest.html), make sure the `curl` command is available.

   For details, refer to the [curl site](https://curl.haxx.se).

## Download DS software

1. If you do not have an account on [Ping Identity Backstage](https://backstage.pingidentity.com), sign up for one.

2. Sign in to Ping Identity Backstage.

3. Find and download the latest PingDS ZIP distribution.

## Install a directory server

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | Example commands in the documentation favor ease of use for evaluation, often including passwords. When you deploy DS in production, don't put secrets in commands, environment variables, or Java system properties. Don't sacrifice security for ease of use in production deployments.**Protect secrets you don't store in DS, such as keystore PINs or passwords for administrative commands. Put them in files or enter them interactively.**When you set file permissions correctly, the operating system grants access only to authorized accounts, such as the account to run the DS server process. Other accounts can't read the secret from a properly protected file.Including secrets in commands, environment variables, or Java system properties isn't secure:- Operating system processes can access the full command to run another process. Those processes can read any secrets you set in the command to run DS, for example.

- Operating system processes can access the environment variables of the DS server process.

- Monitoring software, command-line tools, and support tools like the `supportextract` command extract values of Java system properties and can share them with other systems.DS servers can [use an HSM for asymmetric keys](../security-guide/pki-hsm.html), but not for passwords or symmetric keys. DS servers don't store secrets in secret vaults or other external services. |

1. Unzip the `.zip` file into the file system directory where you want to install the server.

   The documentation shows the installation file system directory as `/path/to/opendj`.

   For example:

   * Bash

   * PowerShell

   * Zsh

   ```console
   $ unzip ~/Downloads/DS-8.1.1.zip -d /path/to
   ```

   ```powershell
   Expand-Archive DS-8.1.1.zip C:\path\to
   ```

   This example installs DS files with the cross-platform zip. When using the native installer, refer to [Use the Windows MSI](../install-guide/install-files.html#install-files-msi).

   ```console
   $ unzip ~/Downloads/DS-8.1.1.zip -d /path/to
   ```

2. Generate and save a deployment ID using the deployment ID password of your choice.

   Use this ID and its password when setting up DS servers in your deployment. The DS server uses the two together when generating other keys to protect shared secret keys and secure connections to other DS servers:

   * Bash

   * PowerShell

   * Zsh

   ```console
   $ /path/to/opendj/bin/dskeymgr create-deployment-id --deploymentIdPassword password
   $ export DEPLOYMENT_ID=<deployment-id>
   ```

   ```powershell
   C:\path\to\opendj\bat\dskeymgr.bat create-deployment-id --deploymentIdPassword password
   set DEPLOYMENT_ID=<deployment-id>
   ```

   ```console
   $ /path/to/opendj/bin/dskeymgr create-deployment-id --deploymentIdPassword password
   $ export DEPLOYMENT_ID=<deployment-id>
   ```

3. Use the `setup` command to set up a server with the `ds-evaluation` profile. The evaluation profile includes Example.com sample data, more lenient access control, and some other features.

   |   |                                                                |
   | - | -------------------------------------------------------------- |
   |   | You must have write access to the folder where you install DS. |

   The following example runs the command non-interactively. Use the same settings shown here to copy and paste the commands shown in these pages:

   * Bash

   * PowerShell

   * Zsh

   ```console
   $ /path/to/opendj/setup \
    --serverId first-ds \
    --deploymentId $DEPLOYMENT_ID \
    --deploymentIdPassword password \
    --rootUserDn uid=admin \
    --rootUserPassword password \
    --monitorUserPassword password \
    --hostname localhost \
    --ldapPort 1389 \
    --ldapsPort 1636 \
    --httpsPort 8443 \
    --adminConnectorPort 4444 \
    --replicationPort 8989 \
    --profile ds-evaluation \
    --start \
    --acceptLicense
   ```

   > **Collapse: Show output**
   >
   > ```
   > Validating parameters..... Done
   > Configuring certificates..... Done
   > Configuring server... Done
   > Configuring profile DS evaluation..................... Done
   > Starting directory server............... Done
   >
   > To see basic server status and configuration, you can launch
   > editable:dsBasePath[/path/to/opendj]/bin/status
   > ```

   ```powershell
   C:\path\to\opendj\setup.bat `
    --serverId first-ds `
    --deploymentId <deployment-id> `
    --deploymentIdPassword password `
    --rootUserDn uid=admin `
    --rootUserPassword password `
    --monitorUserPassword password `
    --hostname localhost `
    --ldapPort 1389 `
    --ldapsPort 1636 `
    --httpsPort 8443 `
    --adminConnectorPort 4444 `
    --replicationPort 8989 `
    --profile ds-evaluation `
    --start `
    --acceptLicense
   ```

   > **Collapse: Show output**
   >
   > ```
   > Validating parameters..... Done
   > Configuring certificates..... Done
   > Configuring server..... Done
   > Configuring profile DS evaluation..................... Done
   > Starting directory server............... Done
   >
   > To see basic server status and configuration, you can launch
   > editable:dsWindowsBasePath[C:\path\to\opendj]\bat\status
   > ```

   ```console
   $ /path/to/opendj/setup \
    --serverId first-ds \
    --deploymentId $DEPLOYMENT_ID \
    --deploymentIdPassword password \
    --rootUserDn uid=admin \
    --rootUserPassword password \
    --monitorUserPassword password \
    --hostname localhost \
    --ldapPort 1389 \
    --ldapsPort 1636 \
    --httpsPort 8443 \
    --adminConnectorPort 4444 \
    --replicationPort 8989 \
    --profile ds-evaluation \
    --start \
    --acceptLicense
   ```

   > **Collapse: Show output**
   >
   > ```
   > Validating parameters..... Done
   > Configuring certificates..... Done
   > Configuring server... Done
   > Configuring profile DS evaluation..................... Done
   > Starting directory server............... Done
   >
   > To see basic server status and configuration, you can launch
   > editable:dsBasePath[/path/to/opendj]/bin/status
   > ```

   > **Collapse: More about setup options**
   >
   > The `setup` command shown here has the following options:
   >
   > * `--serverId first-ds`
   >
   >   A server identifier string that's unique across servers in your deployment.
   >
   > * `--deploymentId <deployment-id>`
   >
   >   The *deployment ID* is a random string generated using the `dskeymgr` command. It's paired with a *deployment ID password*, a random string you choose and must keep secret.
   >
   >   Together, the deployment ID and password serve to generate the shared master key that DS servers in the deployment require for protecting shared encryption secrets. By default, they also serve to generate a private CA and keys for TLS to protect communication between DS servers.
   >
   >   When you deploy multiple servers together, reuse the same deployment ID and password for each server installation.
   >
   > * `--deploymentIdPassword password`
   >
   >   This is a random string that you choose, and that you must keep secret. It is paired with the deployment ID.
   >
   > * `--rootUserDn uid=admin`
   >
   >   These options set the credentials for the directory superuser. This user has privileges to perform all administrative operations and isn't subject to access control. It's called the *root user* due to the similarity to the Linux root user.
   >
   >   The root user distinguished name (DN) *(tooltip: \<div class="paragraph">
   >   \<p>A name uniquely identifying an object within the hierarchy of a directory tree.\</p>
   >   \</div>)* identifies the directory superuser (superuser) *(tooltip: \<div class="paragraph">
   >   \<p>An account with full administration privileges to bypass access control evaluation, change access controls, and change administrative privileges. Analogous to the Linux root and Windows Administrator accounts.\</p>
   >   \</div>)*. In LDAP, a DN is the fully qualified name for a directory entry. The default name is `uid=admin`.
   >
   > * `--monitorUserPassword password`
   >
   >   The monitor user has the privilege to read monitoring data. This example doesn't set the `--monitorUserDn` option, so the DN defaults to `uid=Monitor`.
   >
   > * `--hostname localhost`
   >
   >   The server uses the fully qualified domain name for identification between replicated servers.
   >
   >   Using `localhost` is a shortcut suitable only for evaluation on your local computer. In production, set this to the fully qualified domain name, such as `ds.example.com`.
   >
   > * `--ldapPort 1389`
   >
   >   The reserved port for LDAP is `389`. Use StartTLS to secure connections to this port. The connections aren't secure by default.
   >
   >   Examples in the documentation use `1389`, which is accessible to non-privileged users.
   >
   > * `--ldapsPort 1636`
   >
   >   The reserved port for LDAPS is `636`. Secure connections to this port with TLS.
   >
   >   Examples in the documentation use `1636`, which is accessible to non-privileged users.
   >
   > * `--httpsPort 8443`
   >
   >   The reserved port for HTTPS is `443`.
   >
   >   HTTP client applications access directory data and monitoring information on this port.
   >
   >   Examples in the documentation use `8443`, which is accessible to non-privileged users.
   >
   > * `--adminConnectorPort 4444`
   >
   >   This is the service port to configure the server, run tasks, and respond to administrative requests. It supports both LDAPS and HTTPS requests.
   >
   >   Secure connections to this port with TLS.
   >
   >   The port used in the documentation is `4444`, which is the initial port suggested during interactive setup.
   >
   > * `--replicationPort 8989`
   >
   >   This is the service port used for replication messages.
   >
   >   The port used in the documentation is `8989`, which is the initial port suggested during interactive setup.
   >
   > * `--profile ds-evaluation`
   >
   >   The setup profile adds hard-coded entries for users like Babs Jensen, and groups like Directory Administrators. It also generates 100,000 sample LDAP user entries. All generated users have the same password, literally `password`. The generated user accounts are helpful for performance testing.
   >
   >   This profile adds entries under the base DN `dc=example,dc=com`. A base DN is the suffix shared by all DNs in a set of directory data.
   >
   >   A directory arranges LDAP entries hierarchically. The hierarchical organization resembles a file system on a PC or a web server, often visualized as an upside down tree structure, or a pyramid. In the same way that a full path uniquely identifies each file or folder in a file system, a DN uniquely identifies each LDAP entry.
   >
   >   Each DN consists of components separated by commas, such as `uid=bjensen,ou=People,dc=example,dc=com`. The base DN matches the final components of each DN in that branch of the directory. A DN's components reflect the hierarchy of directory entries. The user entry with DN `uid=bjensen,ou=People,dc=example,dc=com` is under the organizational unit entry `ou=People,dc=example,dc=com`, which in turn is under `dc=example,dc=com`.
   >
   >   Basic components have the form `attribute-name=attribute-value`, such as `dc=com`. In the example `dc=com`, the attribute `dc` (DNS domain component) has the value `com`. The DN `dc=example,dc=com` reflects the DNs domain name `example.com`.
   >
   > * `--start`
   >
   >   By default, the `setup` command doesn't start the server. This lets you complete any necessary configuration steps before starting the server for the first time, which may start the replication process.
   >
   >   In this case, you have no further configuration to do. This option causes the server to start immediately.
   >
   > * `--acceptLicense`
   >
   >   Remove this option to read the license and then accept it interactively.

   You can also run the `setup` command interactively by starting it without options.

4. Add the DS tools to your PATH to avoid having to specify the full path for each command:

   * Bash

   * PowerShell

   * Zsh

   ```console
   $ export PATH=/path/to/opendj/bin:${PATH}
   ```

   ```powershell
   $env:PATH += ";C:\path\to\opendj\bat"
   ```

   ```console
   $ export PATH=/path/to/opendj/bin:${PATH}
   ```

5. Run the `status` command:

   * Bash

   * PowerShell

   * Zsh

   ```console
   $ status \
    --bindDn uid=admin \
    --bindPassword password \
    --hostname localhost \
    --port 4444 \
    --trustStorePath /path/to/opendj/config/keystore \
    --trustStoreType PKCS12 \
    --trustStorePassword:file /path/to/opendj/config/keystore.pin
   ```

   ```powershell
   status.bat `
    --bindDn uid=admin `
    --bindPassword password `
    --hostname localhost `
    --port 4444 `
    --trustStorePath C:\path\to\opendj\config\
    --trustStoreType PKCS12 \keystore `
    --trustStorePassword:file C:\path\to\opendj\config\keystore.pin
   ```

   ```console
   $ status \
    --bindDn uid=admin \
    --bindPassword password \
    --hostname localhost \
    --port 4444 \
    --trustStorePath /path/to/opendj/config/keystore \
    --trustStoreType PKCS12 \
    --trustStorePassword:file /path/to/opendj/config/keystore.pin
   ```

   The `status` command uses a secure connection to the administration port. To trust the server's certificate, the command uses the server's own truststore.

   Read the output that the `status` command displays.

---

---
title: Learn access control
description: Learn how access control instructions (ACIs) work in PingDS and try examples that configure access for users, groups, and anonymous clients.
component: pingds
version: 8.1
page_id: pingds:getting-started:acis
canonical_url: https://docs.pingidentity.com/pingds/8.1/getting-started/acis.html
llms_txt: https://docs.pingidentity.com/pingds/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2025-10-22T14:42:39Z
keywords: ["Authorization", "Evaluation", "LDAP"]
section_ids:
  about-acis: About ACIs
  use-acis: Use ACIs
  example-acis: Example ACIs
  access-control-own-entry: "ACI: access own entry"
  access-control-subschemasubentry: "ACI: access subSchemaSubEntry attribute"
  access-control-selfwrite-group: "ACI: manage group membership"
  access-control-self-service-group: "ACI: manage self-service groups"
  access-control-full-access: "ACI: full access"
  access-control-anonymous-reads: "ACI: anonymous reads and searches"
  access-control-loopback-only: "ACI: permit insecure access over loopback only"
---

# Learn access control

Until now, you have used the evaluation setup profile, which makes it easy to access Example.com data. It helps you learn and demonstrate directory services without explicitly granting access after server setup.

In a production directory service where security is important, access is under tighter control. In most cases, access is denied by default to prevent accidental information leaks. You must explicitly grant access where required. To grant access, use ACIs *(tooltip: \<div class="paragraph">
\<p>An instruction or rule that can be used to grant or deny access to users to perform operations on a server.\</p>
\</div>)*.

|   |                                                                                                                                                                            |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The sample ACIs described on this page demonstrate some but not all ACI features.For a deeper dive into the subject, read [Access control](../security-guide/access.html). |

## About ACIs

ACIs are implemented as operational attributes *(tooltip: \<div class="paragraph">
\<p>An attribute with a special, operational meaning for the server, not returned in searches by default.\</p>
\</div>)*.

Operational attributes aren't meant to store application data but to influence server behavior. They hold internal information for the server's own use, like replication data, timestamps, or ACIs, which the server needs to provide features like replication *(tooltip: \<div class="paragraph">
\<p>Data synchronization to ensure all participating servers eventually share a consistent set of directory data.\</p>
\</div>)*, account lockout *(tooltip: \<div class="paragraph">
\<p>The act of making an account temporarily or permanently inactive after successive authentication failures.\</p>
\</div>)*, or access control *(tooltip: \<div class="paragraph">
\<p>Control to grant or to deny access to a resource.\</p>
\</div>)*. Directory servers only return operational attributes in search results when explicitly requested.

Each ACI influences server behavior by indicating:

* Which directory data it targets

* Which permissions it allows or denies

* Which users or groups it applies to

* Under which conditions (time, network origin, connection security, user properties) it applies

> **Collapse: Example ACI with explanation**
>
> The following example ACI gives users access to change their own passwords:
>
> ```ldif
> aci: (targetattr = "authPassword || userPassword")
>  (version 3.0;acl "Allow users to change their own passwords";
>  allow (write)(userdn = "ldap:///self");)
> ```
>
> Consider the characteristics of this ACI attribute:
>
> * Target Entries and Scope
>
>   The target entries and scope for this ACI are implicit.
>
>   The default target is the entry with this `aci` attribute.
>
>   The default scope includes the target entry and all its subordinates.
>
>   In other words, if you set this ACI on `ou=People,dc=example,dc=com`, it affects all users under that base entry. For example, Babs Jensen, `uid=bjensen,ou=People,dc=example,dc=com`, can set her own password.
>
> * Target Attributes
>
>   This ACI affects operations on either of the standard password attributes: `(targetattr = "authPassword || userPassword")`.
>
>   The ACI only has an effect when an operation targets either `authPassword` or `userPassword` and any subtypes of those attribute types.
>
> * Permissions
>
>   This ACI affects only operations that change affected attributes: `allow (write)`.
>
>   If this is the only ACI that targets password attributes, users have access to change their own passwords, but they do not have access to *read* passwords.
>
> * Subjects
>
>   This ACI has an effect when the target entry is the same as the bind DN: `(userdn = "ldap:///self")`.
>
>   This means the user must authenticate before changing their password.
>
> * Documentation
>
>   The wrapper around the permissions and subjects contains human-readable documentation about the ACI: `(version 3.0;acl "Allow users to change their own passwords"; …​ ;)`.
>
>   Version 3.0 is the only supported ACI version.
>
> * Conditions
>
>   This ACI does not define any conditions. It applies all the time, for connections from all networks, and so forth.
>
>   Server configuration settings can further constrain how clients connect. Such constraints are not specified by this ACI, however.

## Use ACIs

To write ACI attributes:

* A user must have the `modify-acl` administrative privilege.

  Privileges are server configuration settings that control access to administrative operations.

* An ACI must give the user permission to change `aci` attributes.

|   |                                                                                                                                                                                                                                                                                                                                                                                                                     |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | By default, only the directory superuser has the right to add, delete, or modify ACI attributes. The directory superuser account has a `bypass-acl` privilege to perform operations without regard to ACIs.Any account with permission to change ACIs is dangerous because the power can be misused. The user with permissions to change ACIs can give themselves full access to all directory data in their scope. |

Prepare to use the examples:

> **Collapse: Stop running servers**
>
> Use each server's `stop-ds` command to stop any DS servers running on your computer.
>
> This lets the new server use ports another server was already using.

> **Collapse: Get sample data**
>
> 1. Download the [Example.ldif](../_attachments/ldif/Example.ldif) file, shown in the following listing:
>
>    > **Collapse: Show listing**
>    >
>    > ```ldif
>    > #
>    > # Copyright © 2020 - 2026 Ping Identity Corporation
>    > #
>    > # This code is to be used exclusively in connection with Ping Identity Corporation software or services.
>    > # Ping Identity Corporation only offers such software or services to legal entities
>    > # who have entered into a binding license agreement with Ping Identity Corporation.
>    > #
>    > dn: dc=example,dc=com
>    > objectClass: domain
>    > objectClass: top
>    > dc: example
>    >
>    > dn: ou=Groups,dc=example,dc=com
>    > objectClass: organizationalUnit
>    > objectClass: top
>    > ou: Groups
>    >
>    > dn: ou=Self Service,ou=Groups,dc=example,dc=com
>    > objectClass: organizationalUnit
>    > objectClass: top
>    > description: Groups that authenticated users can manage on their own
>    > ou: Self Service
>    >
>    > dn: ou=People,dc=example,dc=com
>    > objectClass: organizationalUnit
>    > objectClass: top
>    > description: Description on ou=People
>    > ou: People
>    >
>    > dn: uid=ACI Admin,ou=People,dc=example,dc=com
>    > objectClass: person
>    > objectClass: inetOrgPerson
>    > objectClass: organizationalPerson
>    > objectClass: top
>    > cn: ACI Admin
>    > givenName: ACI
>    > mail: aci-admin@example.com
>    > ou: People
>    > sn: Admin
>    > uid: ACI Admin
>    > userPassword: 5up35tr0ng
>    >
>    > dn: uid=bjensen,ou=People,dc=example,dc=com
>    > objectClass: person
>    > objectClass: inetOrgPerson
>    > objectClass: organizationalPerson
>    > objectClass: top
>    > cn: Babs Jensen
>    > givenName: Barbara
>    > mail: bjensen@example.com
>    > ou: People
>    > sn: Jensen
>    > uid: bjensen
>    > userPassword: 5up35tr0ng
>    > ```
>
> 2. Save the file to your computer's temporary directory, such as `/tmp` or `C:\Temp` .

> **Collapse: Install server with secure settings**
>
> 1. Unzip the DS server `.zip` file into the folder where you want to install the server.
>
> 2. Set up the directory server using the LDIF you downloaded.
>
>    Set up the server without the evaluation setup profile, *so the access control settings are secure by default.* The default password policies require stronger passwords. The configuration grants very little access to regular users. Only `uid=admin` has access to the data:
>
>    * Bash
>
>    * PowerShell
>
>    * Zsh
>
>    ```console
>    $ /path/to/opendj/setup \
>     --serverId learn-acis \
>     --deploymentId $DEPLOYMENT_ID \
>     --deploymentIdPassword password \
>     --rootUserDn uid=admin \
>     --rootUserPassword str0ngAdm1nPa55word \
>     --hostname localhost \
>     --ldapPort 1389 \
>     --ldapsPort 1636 \
>     --httpsPort 8443 \
>     --adminConnectorPort 4444 \
>     --acceptLicense
>    $ dsconfig \
>     create-backend \
>     --backend-name exampleData \
>     --type je \
>     --set enabled:true \
>     --set base-dn:dc=example,dc=com \
>     --offline \
>     --no-prompt
>    $ import-ldif \
>     --backendId exampleData \
>     --ldifFile /tmp/Example.ldif \
>     --offline
>    $ start-ds --quiet
>    ```
>
>    ```powershell
>    C:\path\to\opendj\setup.bat `
>     --serverId learn-acis `
>     --deploymentId <deployment-id> `
>     --deploymentIdPassword password `
>     --rootUserDn uid=admin `
>     --rootUserPassword str0ngAdm1nPa55word `
>     --hostname localhost `
>     --ldapPort 1389 `
>     --ldapsPort 1636 `
>     --httpsPort 8443 `
>     --adminConnectorPort 4444 `
>     --acceptLicense
>    C:\path\to\opendj\bat\dsconfig.bat `
>     create-backend `
>     --backend-name exampleData `
>     --type je `
>     --set enabled:true `
>     --set base-dn:dc=example,dc=com `
>     --offline `
>     --no-prompt
>    C:\path\to\opendj\bat\import-ldif.bat `
>     --backendId exampleData `
>     --ldifFile C:\Temp\Example.ldif `
>     --offline
>    C:\path\to\opendj\bat\start-ds.bat --quiet
>    ```
>
>    ```console
>    $ /path/to/opendj/setup \
>     --serverId learn-acis \
>     --deploymentId $DEPLOYMENT_ID \
>     --deploymentIdPassword password \
>     --rootUserDn uid=admin \
>     --rootUserPassword str0ngAdm1nPa55word \
>     --hostname localhost \
>     --ldapPort 1389 \
>     --ldapsPort 1636 \
>     --httpsPort 8443 \
>     --adminConnectorPort 4444 \
>     --acceptLicense
>    $ dsconfig \
>     create-backend \
>     --backend-name exampleData \
>     --type je \
>     --set enabled:true \
>     --set base-dn:dc=example,dc=com \
>     --offline \
>     --no-prompt
>    $ import-ldif \
>     --backendId exampleData \
>     --ldifFile /tmp/Example.ldif \
>     --offline
>    $ start-ds --quiet
>    ```

> **Collapse: Grant ACI admin access**
>
> Grant the `ACI Admin` user access to modify ACIs:
>
> * Bash
>
> * PowerShell
>
> * Zsh
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
>  --bindPassword str0ngAdm1nPa55word << EOF
> dn: dc=example,dc=com
> changetype: modify
> add: aci
> aci: (targetattr = "aci") (version 3.0;acl "ACI Admin can manage ACI attributes";
>  allow (write) userdn = "ldap:///uid=ACI Admin,ou=People,dc=example,dc=com";)
>
> dn: uid=ACI Admin,ou=People,dc=example,dc=com
> changetype: modify
> add: ds-privilege-name
> ds-privilege-name: modify-acl
> EOF
> ```
>
> ```powershell
> New-Item -Path . -Name "aci-admin.ldif" -ItemType "file" -Value @"
> dn: dc=example,dc=com
> changetype: modify
> add: aci
> aci: (targetattr = "aci") (version 3.0;acl "ACI Admin can manage ACI attributes";
>  allow (write) userdn = "ldap:///uid=ACI Admin,ou=People,dc=example,dc=com";)
>
> dn: uid=ACI Admin,ou=People,dc=example,dc=com
> changetype: modify
> add: ds-privilege-name
> ds-privilege-name: modify-acl
> "@
> ldapmodify.bat `
>  --hostname localhost `
>  --port 1636 `
>  --useSsl `
>  --trustStorePath C:\path\to\opendj\config\
>  --trustStoreType PKCS12 \keystore `
>  --trustStorePassword:file C:\path\to\opendj\config\keystore.pin `
>  --bindDn uid=admin `
>  --bindPassword str0ngAdm1nPa55word `
>  aci-admin.ldif
> ```
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
>  --bindPassword str0ngAdm1nPa55word << EOF
> dn: dc=example,dc=com
> changetype: modify
> add: aci
> aci: (targetattr = "aci") (version 3.0;acl "ACI Admin can manage ACI attributes";
>  allow (write) userdn = "ldap:///uid=ACI Admin,ou=People,dc=example,dc=com";)
>
> dn: uid=ACI Admin,ou=People,dc=example,dc=com
> changetype: modify
> add: ds-privilege-name
> ds-privilege-name: modify-acl
> EOF
> ```

> **Collapse: (Optional) Try LDAP examples**
>
> Try examples from [Learn LDAP](ldap.html).
>
> Babs Jensen does not have the access she had with the evaluation setup profile. For production servers, the best practice is to grant access only when required.

## Example ACIs

Prepare to use the examples before trying them. The `ACI Admin` account must have access to manage ACIs. After you add an example ACI, test users' access. For inspiration, refer to the examples in [Learn LDAP](ldap.html).

ACI syntax is powerful and sometimes challenging to get right. For details, refer to [Access control](../security-guide/access.html).

### ACI: access own entry

The following example grants authenticated users access to read their own entry, and modify some attributes:

* Bash

* PowerShell

* Zsh

```console
$ ldapmodify \
 --hostname localhost \
 --port 1636 \
 --useSsl \
 --trustStorePath /path/to/opendj/config/keystore \
 --trustStoreType PKCS12 \
 --trustStorePassword:file /path/to/opendj/config/keystore.pin \
 --bindDn "uid=ACI Admin,ou=People,dc=example,dc=com" \
 --bindPassword 5up35tr0ng << EOF
dn: dc=example,dc=com
changetype: modify
add: aci
aci: (targetattr = "*") (version 3.0;acl "Users can read their entries";
 allow (read, search, compare) (userdn = "ldap:///self");)
-
add: aci
aci: (targetattr = "authPassword || description || displayName || homePhone ||
 jpegPhoto || preferredLanguage || userPassword")
 (version 3.0;acl "Self-service modifications for basic attributes";
 allow (write) (userdn = "ldap:///self");)
EOF
```

```powershell
New-Item -Path . -Name "self-access.ldif" -ItemType "file" -Value @"
dn: dc=example,dc=com
changetype: modify
add: aci
aci: (targetattr = "*") (version 3.0;acl "Users can read their entries";
 allow (read, search, compare) (userdn = "ldap:///self");)
-
add: aci
aci: (targetattr = "authPassword || description || displayName || homePhone ||
 jpegPhoto || preferredLanguage || userPassword")
 (version 3.0;acl "Self-service modifications for basic attributes";
 allow (write) (userdn = "ldap:///self");)
"@
ldapmodify.bat `
 --hostname localhost `
 --port 1636 `
 --useSsl `
 --trustStorePath C:\path\to\opendj\config\
 --trustStoreType PKCS12 \keystore `
 --trustStorePassword:file C:\path\to\opendj\config\keystore.pin `
 --bindDn "uid=ACI Admin,ou=People,dc=example,dc=com" `
 --bindPassword 5up35tr0ng `
 self-access.ldif
```

```console
$ ldapmodify \
 --hostname localhost \
 --port 1636 \
 --useSsl \
 --trustStorePath /path/to/opendj/config/keystore \
 --trustStoreType PKCS12 \
 --trustStorePassword:file /path/to/opendj/config/keystore.pin \
 --bindDn "uid=ACI Admin,ou=People,dc=example,dc=com" \
 --bindPassword 5up35tr0ng << EOF
dn: dc=example,dc=com
changetype: modify
add: aci
aci: (targetattr = "*") (version 3.0;acl "Users can read their entries";
 allow (read, search, compare) (userdn = "ldap:///self");)
-
add: aci
aci: (targetattr = "authPassword || description || displayName || homePhone ||
 jpegPhoto || preferredLanguage || userPassword")
 (version 3.0;acl "Self-service modifications for basic attributes";
 allow (write) (userdn = "ldap:///self");)
EOF
```

In this example, the list of attributes users can read includes all user attributes. The list users can modify is limited. Other applications may manage other attributes; for example, a user's manager could require a change through an HR system.

### ACI: access subSchemaSubEntry attribute

The `subSchemaSubEntry` attribute indicates the entry with the LDAP schema definitions for the current entry. Many applications retrieve this attribute and the associated schema to properly display or validate attribute values.

The following example demonstrates how to grant access to read this attribute on directory entries:

* Bash

* PowerShell

* Zsh

```console
$ ldapmodify \
 --hostname localhost \
 --port 1636 \
 --useSsl \
 --trustStorePath /path/to/opendj/config/keystore \
 --trustStoreType PKCS12 \
 --trustStorePassword:file /path/to/opendj/config/keystore.pin \
 --bindDn "uid=ACI Admin,ou=People,dc=example,dc=com" \
 --bindPassword 5up35tr0ng << EOF
dn: dc=example,dc=com
changetype: modify
add: aci
aci: (targetattr = "subSchemaSubEntry")
 (version 3.0;acl "Authenticated users can read subSchemaSubEntry";
 allow (read, search, compare) (userdn = "ldap:///all");)
EOF
```

```powershell
New-Item -Path . -Name "subSchemaSubentry-access.ldif" -ItemType "file" -Value @"
dn: dc=example,dc=com
changetype: modify
add: aci
aci: (targetattr = "subSchemaSubEntry")
 (version 3.0;acl "Authenticated users can read subSchemaSubEntry";
 allow (read, search, compare) (userdn = "ldap:///all");)
"@
ldapmodify.bat `
 --hostname localhost `
 --port 1636 `
 --useSsl `
 --trustStorePath C:\path\to\opendj\config\
 --trustStoreType PKCS12 \keystore `
 --trustStorePassword:file C:\path\to\opendj\config\keystore.pin `
 --bindDn "uid=ACI Admin,ou=People,dc=example,dc=com" `
 --bindPassword 5up35tr0ng `
 subSchemaSubentry-access.ldif
```

```console
$ ldapmodify \
 --hostname localhost \
 --port 1636 \
 --useSsl \
 --trustStorePath /path/to/opendj/config/keystore \
 --trustStoreType PKCS12 \
 --trustStorePassword:file /path/to/opendj/config/keystore.pin \
 --bindDn "uid=ACI Admin,ou=People,dc=example,dc=com" \
 --bindPassword 5up35tr0ng << EOF
dn: dc=example,dc=com
changetype: modify
add: aci
aci: (targetattr = "subSchemaSubEntry")
 (version 3.0;acl "Authenticated users can read subSchemaSubEntry";
 allow (read, search, compare) (userdn = "ldap:///all");)
EOF
```

### ACI: manage group membership

For some static groups, you might choose to let users manage their own memberships. The following example lets members of self-service groups manage their own membership:

* Bash

* PowerShell

* Zsh

```console
$ ldapmodify \
 --hostname localhost \
 --port 1636 \
 --useSsl \
 --trustStorePath /path/to/opendj/config/keystore \
 --trustStoreType PKCS12 \
 --trustStorePassword:file /path/to/opendj/config/keystore.pin \
 --bindDn "uid=ACI Admin,ou=People,dc=example,dc=com" \
 --bindPassword 5up35tr0ng << EOF
dn: ou=Self Service,ou=Groups,dc=example,dc=com
changetype: modify
add: aci
aci: (targetattr = "member") (version 3.0;acl "Self registration";
 allow (selfwrite) (userdn = "ldap:///uid=*,ou=People,dc=example,dc=com");)
EOF
```

```powershell
New-Item -Path . -Name "self-service-groups.ldif" -ItemType "file" -Value @"
dn: ou=Self Service,ou=Groups,dc=example,dc=com
changetype: modify
add: aci
aci: (targetattr = "member") (version 3.0;acl "Self registration";
 allow (selfwrite) (userdn = "ldap:///uid=*,ou=People,dc=example,dc=com");)
"@
ldapmodify.bat `
 --hostname localhost `
 --port 1636 `
 --useSsl `
 --trustStorePath C:\path\to\opendj\config\
 --trustStoreType PKCS12 \keystore `
 --trustStorePassword:file C:\path\to\opendj\config\keystore.pin `
 --bindDn "uid=ACI Admin,ou=People,dc=example,dc=com" `
 --bindPassword 5up35tr0ng `
 self-service-groups.ldif
```

```console
$ ldapmodify \
 --hostname localhost \
 --port 1636 \
 --useSsl \
 --trustStorePath /path/to/opendj/config/keystore \
 --trustStoreType PKCS12 \
 --trustStorePassword:file /path/to/opendj/config/keystore.pin \
 --bindDn "uid=ACI Admin,ou=People,dc=example,dc=com" \
 --bindPassword 5up35tr0ng << EOF
dn: ou=Self Service,ou=Groups,dc=example,dc=com
changetype: modify
add: aci
aci: (targetattr = "member") (version 3.0;acl "Self registration";
 allow (selfwrite) (userdn = "ldap:///uid=*,ou=People,dc=example,dc=com");)
EOF
```

The `selfwrite` permission is for adding or deleting one's own DN from a group.

### ACI: manage self-service groups

This example lets users create and delete self-managed groups:

* Bash

* PowerShell

* Zsh

```console
$ ldapmodify \
 --hostname localhost \
 --port 1636 \
 --useSsl \
 --trustStorePath /path/to/opendj/config/keystore \
 --trustStoreType PKCS12 \
 --trustStorePassword:file /path/to/opendj/config/keystore.pin \
 --bindDn "uid=ACI Admin,ou=People,dc=example,dc=com" \
 --bindPassword 5up35tr0ng << EOF
dn: ou=Self Service,ou=Groups,dc=example,dc=com
changetype: modify
add: aci
aci: (targattrfilters="add=objectClass:(objectClass=groupOfNames)")
 (version 3.0; acl "Users can create self-service groups";
 allow (add) (userdn = "ldap:///uid=*,ou=People,dc=example,dc=com");)
-
add: aci
aci: (version 3.0; acl "Owner can delete self-service groups";
 allow (delete) (userattr = "owner#USERDN");)
EOF
```

```powershell
New-Item -Path . -Name "self-managed-groups.ldif" -ItemType "file" -Value @"
dn: ou=Self Service,ou=Groups,dc=example,dc=com
changetype: modify
add: aci
aci: (targattrfilters="add=objectClass:(objectClass=groupOfNames)")
 (version 3.0; acl "Users can create self-service groups";
 allow (add) (userdn = "ldap:///uid=*,ou=People,dc=example,dc=com");)
-
add: aci
aci: (version 3.0; acl "Owner can delete self-service groups";
 allow (delete) (userattr = "owner#USERDN");)
"@
ldapmodify.bat `
 --hostname localhost `
 --port 1636 `
 --useSsl `
 --trustStorePath C:\path\to\opendj\config\
 --trustStoreType PKCS12 \keystore `
 --trustStorePassword:file C:\path\to\opendj\config\keystore.pin `
 --bindDn "uid=ACI Admin,ou=People,dc=example,dc=com" `
 --bindPassword 5up35tr0ng `
 self-managed-groups.ldif
```

```console
$ ldapmodify \
 --hostname localhost \
 --port 1636 \
 --useSsl \
 --trustStorePath /path/to/opendj/config/keystore \
 --trustStoreType PKCS12 \
 --trustStorePassword:file /path/to/opendj/config/keystore.pin \
 --bindDn "uid=ACI Admin,ou=People,dc=example,dc=com" \
 --bindPassword 5up35tr0ng << EOF
dn: ou=Self Service,ou=Groups,dc=example,dc=com
changetype: modify
add: aci
aci: (targattrfilters="add=objectClass:(objectClass=groupOfNames)")
 (version 3.0; acl "Users can create self-service groups";
 allow (add) (userdn = "ldap:///uid=*,ou=People,dc=example,dc=com");)
-
add: aci
aci: (version 3.0; acl "Owner can delete self-service groups";
 allow (delete) (userattr = "owner#USERDN");)
EOF
```

### ACI: full access

The following ACI grants Babs Jensen permission to perform all LDAP operations, allowing her full administrator access to the directory data under `dc=example,dc=com`. Babs can read and write directory data, rename and move entries, and use proxied authorization. Some operations also require administrative privileges not shown in this example:

* Bash

* PowerShell

* Zsh

```console
$ ldapmodify \
 --hostname localhost \
 --port 1636 \
 --useSsl \
 --trustStorePath /path/to/opendj/config/keystore \
 --trustStoreType PKCS12 \
 --trustStorePassword:file /path/to/opendj/config/keystore.pin \
 --bindDn "uid=ACI Admin,ou=People,dc=example,dc=com" \
 --bindPassword 5up35tr0ng << EOF
dn: dc=example,dc=com
changetype: modify
add: aci
aci: (targetattr = "* || +") (version 3.0;acl "Babs has full access";
 allow (all, export, import, proxy) (userdn = "ldap:///uid=bjensen,ou=People,dc=example,dc=com");)
EOF
```

```powershell
New-Item -Path . -Name "full-access.ldif" -ItemType "file" -Value @"
dn: dc=example,dc=com
changetype: modify
add: aci
aci: (targetattr = "* || +") (version 3.0;acl "Babs has full access";
 allow (all, export, import, proxy) (userdn = "ldap:///uid=bjensen,ou=People,dc=example,dc=com");)
"@
ldapmodify.bat `
 --hostname localhost `
 --port 1636 `
 --useSsl `
 --trustStorePath C:\path\to\opendj\config\
 --trustStoreType PKCS12 \keystore `
 --trustStorePassword:file C:\path\to\opendj\config\keystore.pin `
 --bindDn "uid=ACI Admin,ou=People,dc=example,dc=com" `
 --bindPassword 5up35tr0ng `
 full-access.ldif
```

```console
$ ldapmodify \
 --hostname localhost \
 --port 1636 \
 --useSsl \
 --trustStorePath /path/to/opendj/config/keystore \
 --trustStoreType PKCS12 \
 --trustStorePassword:file /path/to/opendj/config/keystore.pin \
 --bindDn "uid=ACI Admin,ou=People,dc=example,dc=com" \
 --bindPassword 5up35tr0ng << EOF
dn: dc=example,dc=com
changetype: modify
add: aci
aci: (targetattr = "* || +") (version 3.0;acl "Babs has full access";
 allow (all, export, import, proxy) (userdn = "ldap:///uid=bjensen,ou=People,dc=example,dc=com");)
EOF
```

`(targetattr = "* || +")` permits access to all user attributes and all operational attributes. `allow (all, import, export, proxy)` permits all user operations, modify DN operations, and proxied authorization. Notice `all` doesn't allow modify DN or proxied authorization.

### ACI: anonymous reads and searches

In LDAP, an anonymous user is one who does not provide bind credentials. By default, most setup profiles only allow anonymous access to read information about the server's capabilities or before using the StartTLS operation to get a secure connection before providing credentials.

Unless you set up the server with the evaluation profile, anonymous users cannot read application data by default. You can grant them access, however. First, change the global configuration to allow unauthenticated requests. Second, add an ACI to grant access to the entries.

The following command changes the global configuration property, `unauthenticated-requests-policy`, to allow unauthenticated requests:

* Bash

* PowerShell

* Zsh

```console
$ dsconfig \
 set-global-configuration-prop \
 --hostname localhost \
 --port 4444 \
 --bindDN uid=admin \
 --bindPassword str0ngAdm1nPa55word \
 --set unauthenticated-requests-policy:allow \
 --trustStorePath /path/to/opendj/config/keystore \
 --trustStoreType PKCS12 \
 --trustStorePassword:file /path/to/opendj/config/keystore.pin \
 --no-prompt
```

```powershell
dsconfig.bat `
 set-global-configuration-prop `
 --hostname localhost `
 --port 4444 `
 --bindDN uid=admin `
 --bindPassword str0ngAdm1nPa55word `
 --set unauthenticated-requests-policy:allow `
 --trustStorePath C:\path\to\opendj\config\
 --trustStoreType PKCS12 \keystore `
 --trustStorePassword:file C:\path\to\opendj\config\keystore.pin `
 --no-prompt
```

```console
$ dsconfig \
 set-global-configuration-prop \
 --hostname localhost \
 --port 4444 \
 --bindDN uid=admin \
 --bindPassword str0ngAdm1nPa55word \
 --set unauthenticated-requests-policy:allow \
 --trustStorePath /path/to/opendj/config/keystore \
 --trustStoreType PKCS12 \
 --trustStorePassword:file /path/to/opendj/config/keystore.pin \
 --no-prompt
```

This ACI makes all user attributes in `dc=example,dc=com` data (except passwords) world-readable:

* Bash

* PowerShell

* Zsh

```console
$ ldapmodify \
 --hostname localhost \
 --port 1636 \
 --useSsl \
 --trustStorePath /path/to/opendj/config/keystore \
 --trustStoreType PKCS12 \
 --trustStorePassword:file /path/to/opendj/config/keystore.pin \
 --bindDn "uid=ACI Admin,ou=People,dc=example,dc=com" \
 --bindPassword 5up35tr0ng << EOF
dn: dc=example,dc=com
changetype: modify
add: aci
aci: (targetattr != "authPassword || userPassword") (version 3.0;acl "Anonymous read-search access";
 allow (read, search, compare) (userdn = "ldap:///anyone");)
EOF
```

```powershell
New-Item -Path . -Name "anon-access.ldif" -ItemType "file" -Value @"
dn: dc=example,dc=com
changetype: modify
add: aci
aci: (targetattr != "authPassword || userPassword") (version 3.0;acl "Anonymous read-search access";
 allow (read, search, compare) (userdn = "ldap:///anyone");)
"@
ldapmodify.bat `
 --hostname localhost `
 --port 1636 `
 --useSsl `
 --trustStorePath C:\path\to\opendj\config\
 --trustStoreType PKCS12 \keystore `
 --trustStorePassword:file C:\path\to\opendj\config\keystore.pin `
 --bindDn "uid=ACI Admin,ou=People,dc=example,dc=com" `
 --bindPassword 5up35tr0ng `
 anon-access.ldif
```

```console
$ ldapmodify \
 --hostname localhost \
 --port 1636 \
 --useSsl \
 --trustStorePath /path/to/opendj/config/keystore \
 --trustStoreType PKCS12 \
 --trustStorePassword:file /path/to/opendj/config/keystore.pin \
 --bindDn "uid=ACI Admin,ou=People,dc=example,dc=com" \
 --bindPassword 5up35tr0ng << EOF
dn: dc=example,dc=com
changetype: modify
add: aci
aci: (targetattr != "authPassword || userPassword") (version 3.0;acl "Anonymous read-search access";
 allow (read, search, compare) (userdn = "ldap:///anyone");)
EOF
```

Notice `ldap:///anyone` designates anonymous users and authenticated users. Do not confuse it with `ldap:///all`, which designates authenticated users only.

### ACI: permit insecure access over loopback only

This ACI uses IP address and Security Strength Factor subjects to prevent insecure remote access to `dc=example,dc=com` data. In most cases, you explicitly grant permission with `allow`, making it easier to understand and to explain why the server permits a given operation. This demonstrates one use case where it makes sense to *deny* permission:

* Bash

* PowerShell

* Zsh

```console
$ ldapmodify \
 --hostname localhost \
 --port 1636 \
 --useSsl \
 --trustStorePath /path/to/opendj/config/keystore \
 --trustStoreType PKCS12 \
 --trustStorePassword:file /path/to/opendj/config/keystore.pin \
 --bindDn "uid=ACI Admin,ou=People,dc=example,dc=com" \
 --bindPassword 5up35tr0ng << EOF
dn: dc=example,dc=com
changetype: modify
add: aci
aci: (targetattr = "* || +") (version 3.0;acl "Restrict insecure LDAP to the loopback address";
 deny (all) (ip != "127.0.0.1" and ssf <= "1");)
EOF
```

```powershell
New-Item -Path . -Name "deny-cleartext.ldif" -ItemType "file" -Value @"
dn: dc=example,dc=com
changetype: modify
add: aci
aci: (targetattr = "* || +") (version 3.0;acl "Restrict insecure LDAP to the loopback address";
 deny (all) (ip != "127.0.0.1" and ssf <= "1");)
"@
ldapmodify.bat `
 --hostname localhost `
 --port 1636 `
 --useSsl `
 --trustStorePath C:\path\to\opendj\config\
 --trustStoreType PKCS12 \keystore `
 --trustStorePassword:file C:\path\to\opendj\config\keystore.pin `
 --bindDn "uid=ACI Admin,ou=People,dc=example,dc=com" `
 --bindPassword 5up35tr0ng `
 deny-cleartext.ldif
```

```console
$ ldapmodify \
 --hostname localhost \
 --port 1636 \
 --useSsl \
 --trustStorePath /path/to/opendj/config/keystore \
 --trustStoreType PKCS12 \
 --trustStorePassword:file /path/to/opendj/config/keystore.pin \
 --bindDn "uid=ACI Admin,ou=People,dc=example,dc=com" \
 --bindPassword 5up35tr0ng << EOF
dn: dc=example,dc=com
changetype: modify
add: aci
aci: (targetattr = "* || +") (version 3.0;acl "Restrict insecure LDAP to the loopback address";
 deny (all) (ip != "127.0.0.1" and ssf <= "1");)
EOF
```

* `ssf = 1` means TLS is configured without a cipher.

  The server verifies integrity using packet checksums, but all content is sent in plain text.

* `ssf = 0` means the content is sent plain text with no connection security.

---

---
title: Learn HDAP
description: Learn how to use HDAP (HTTP Directory Access Protocol) to create, read, update, and delete directory resources in PingDS over HTTPS.
component: pingds
version: 8.1
page_id: pingds:getting-started:rest
canonical_url: https://docs.pingidentity.com/pingds/8.1/getting-started/rest.html
llms_txt: https://docs.pingidentity.com/pingds/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2025-10-22T14:42:39Z
keywords: ["Evaluation", "LDAP", "REST API"]
section_ids:
  before-rest: Prepare
  create-rest: Create
  read-rest: Read
  update-rest: Update
  delete-rest: Delete
---

# Learn HDAP

PingDS let you access LDAP data over HTTP using HTTP directory access protocol (HDAP) *(tooltip: \<div class="paragraph">
\<p>The DS feature providing REST APIs and HTTP access to directory data.\</p>
\</div>)* APIs that transform HTTP operations into LDAP operations.

Before you try the examples, follow the instructions in [Install DS](install.html).

## Prepare

Get the deployment CA certificate to trust the server:

* Bash

* PowerShell

* Zsh

```console
$ dskeymgr \
 export-ca-cert \
 --deploymentId $DEPLOYMENT_ID \
 --deploymentIdPassword password \
 --outputFile ca-cert.pem
```

Configure Windows to trust the deployment CA certificate. Import the deployment CA from the server truststore using Microsoft Management Console (MMC):

1. Run Microsoft Management Console (`mmc.exe`).

2. Add the certificates snap-in to import the deployment CA certificate:

   * In the console, select File > Add/Remove Snap-in, then Add.

   * Select Certificates from the list of snap-ins and click Add.

   * Finish the wizard.

3. Import the deployment CA certificate using the snap-in:

   * Select Console Root > Trusted Root Certification Authorities > Certificates.

   * In the Action menu, select Import to open the wizard.

   * Use the wizard to import the deployment CA certificate from the server truststore file, `C:\path\to\opendj\config\keystore`.

     The truststore password is the text in the file `C:\path\to\opendj\config\keystore.pin`.

```console
$ dskeymgr \
 export-ca-cert \
 --deploymentId $DEPLOYMENT_ID \
 --deploymentIdPassword password \
 --outputFile ca-cert.pem
```

## Create

Use HDAP to create a user resource:

* Bash

* JavaScript

* PowerShell

* Python

* Ruby

* Zsh

```console
$ curl \
--request POST \
--cacert ca-cert.pem \
--user uid=admin:password \
--header 'Content-Type: application/json' \
--data '{
  "_id" : "dc=com/dc=example/ou=People/uid=newuser",
  "objectClass" : [ "person", "inetOrgPerson", "organizationalPerson", "top" ],
  "cn" : [ "New User" ],
  "givenName" : [ "New" ],
  "mail" : [ "newuser@example.com" ],
  "manager" : [ "dc=com/dc=example/ou=People/uid=bjensen" ],
  "sn" : [ "User" ],
  "telephoneNumber" : [ "+1 408 555 1212" ],
  "uid" : [ "newuser" ]
}' \
'https://localhost:8443/hdap/dc=com/dc=example/ou=People?_prettyPrint=true'
```

> **Collapse: Show output**
>
> ```
> {
>   "_id" : "dc=com/dc=example/ou=People/uid=newuser",
>   "_rev" : "<revision>",
>   "objectClass" : [ "person", "inetOrgPerson", "organizationalPerson", "top" ],
>   "cn" : [ "New User" ],
>   "givenName" : [ "New" ],
>   "mail" : [ "newuser@example.com" ],
>   "manager" : [ "dc=com/dc=example/ou=People/uid=bjensen" ],
>   "sn" : [ "User" ],
>   "telephoneNumber" : [ "+1 408 555 1212" ],
>   "uid" : [ "newuser" ]
> }
> ```

```javascript
const { doRequest, getOptions } = require('./utils')

const options = getOptions({
    path: '/hdap/dc=com/dc=example/ou=People?_action=create',
    credentials: 'uid=admin:password',
    method: 'POST',
    body: {
        "_id": "dc=com/dc=example/ou=People/uid=newuser",
        "objectClass": ["person", "inetOrgPerson", "organizationalPerson", "top"],
        "cn": ["New User"],
        "givenName": ["New"],
        "mail": ["newuser@example.com"],
        "manager": ["dc=com/dc=example/ou=People/uid=bjensen"],
        "sn": ["User"],
        "telephoneNumber": ["+1 408 555 1212"],
        "uid": ["newuser"]
    }
})

doRequest('HDAP: create with POST', options)
    .then(response => { console.log(response) })
    .catch(error => { console.error(error) })
```

Source files for this sample: [create-newuser.js](../_attachments/hdap/js/create-newuser.js), [utils.js](../_attachments/hdap/js/utils.js)

```powershell
$Credentials = [System.Convert]::ToBase64String([System.Text.Encoding]::ASCII.GetBytes("uid=admin:password"))
$Headers = @{
    Authorization = "Basic $Credentials"
}
Invoke-RestMethod `
 -Uri https://localhost:8443/hdap/dc=com/dc=example/ou=People `
 -Method Post `
 -Headers $Headers `
 -ContentType application/json `
 -Body @"
 {
    "_id" : "dc=com/dc=example/ou=People/uid=newuser",
    "objectClass" : [ "person", "inetOrgPerson", "organizationalPerson", "top" ],
    "cn" : [ "New User" ],
    "givenName" : [ "New" ],
    "mail" : [ "newuser@example.com" ],
    "manager" : [ "dc=com/dc=example/ou=People/uid=bjensen" ],
    "sn" : [ "User" ],
    "telephoneNumber" : [ "+1 408 555 1212" ],
    "uid" : [ "newuser" ]
 }
"@ | ConvertTo-JSON
```

> **Collapse: Show output**
>
> ```
> {
>     "_id" : "dc=com/dc=example/ou=People/uid=newuser",
>     "_rev" : "<revision>",
>     "objectClass" : [ "person", "inetOrgPerson", "organizationalPerson", "top" ],
>     "cn" : [ "New User" ],
>     "givenName" : [ "New" ],
>     "mail" : [ "newuser@example.com" ],
>     "manager" : [ "dc=com/dc=example/ou=People/uid=bjensen" ],
>     "sn" : [ "User" ],
>     "telephoneNumber" : [ "+1 408 555 1212" ],
>     "uid" : [ "newuser" ]
> }
> ```

```python
#!/usr/bin/env python3

import requests
from requests.auth import HTTPBasicAuth
import utils

body = {
    '_id': 'dc=com/dc=example/ou=People/uid=newuser',
    'objectClass': ['person', 'inetOrgPerson', 'organizationalPerson', 'top'],
    'cn': ['New User'],
    'givenName': ['New'],
    'mail': ['newuser@example.com'],
    'manager': ['dc=com/dc=example/ou=People/uid=bjensen'],
    'sn': ['User'],
    'telephoneNumber': ['+1 408 555 1212'],
    'uid': ['newuser']
}
headers = { 'Content-Type': 'application/json' }
response = requests.post(
    f'https://{utils.host}:{utils.port}/hdap/dc=com/dc=example/ou=People',
    auth=HTTPBasicAuth('uid=admin', 'password'),
    headers=headers,
    json=body,
    verify=utils.ca_pem)
print('Status code: %d\nJSON: %s' % (response.status_code, response.json()))
```

Source files for this sample: [utils.py](../_attachments/hdap/py/utils.py), [create-newuser.py](../_attachments/hdap/py/create-newuser.py)

```ruby
require_relative 'utils.rb'
require 'faraday'
require 'json'

utils = Utils.new('', '')
options = { ca_file: utils.ca_pem }
hdap = Faraday.new(url: "https://#{utils.host}:#{utils.port}/hdap/", ssl: options) do |f|
    f.headers['Content-Type'] = 'application/json'
    f.request :authorization, :basic, 'uid=admin', 'password'
end
body = {
    '_id' => "dc=com/dc=example/ou=People/uid=newuser",
    'objectClass' => ["person", "inetOrgPerson", "organizationalPerson", "top"],
    'cn' => ["New User"],
    'givenName' => ["New"],
    'mail' => ["newuser@example.com"],
    'manager' => ["dc=com/dc=example/ou=People/uid=bjensen"],
    'sn' => ["User"],
    'telephoneNumber' => ["+1 408 555 1212"],
    'uid' => ["newuser"]
}
response = hdap.post do |h|
    h.path = 'dc=com/dc=example/ou=People'
    h.body = JSON.generate(body)
end

puts "Status code: #{response.status}\nJSON: #{response.body}"
```

Source files for this sample: [utils.rb](../_attachments/hdap/rb/utils.rb), [create-newuser.rb](../_attachments/hdap/rb/create-newuser.rb)

HDAP Ruby examples require Ruby 3.2 and the `faraday` and `json` gems.

```console
$ curl \
--request POST \
--cacert ca-cert.pem \
--user uid=admin:password \
--header 'Content-Type: application/json' \
--data '{
  "_id" : "dc=com/dc=example/ou=People/uid=newuser",
  "objectClass" : [ "person", "inetOrgPerson", "organizationalPerson", "top" ],
  "cn" : [ "New User" ],
  "givenName" : [ "New" ],
  "mail" : [ "newuser@example.com" ],
  "manager" : [ "dc=com/dc=example/ou=People/uid=bjensen" ],
  "sn" : [ "User" ],
  "telephoneNumber" : [ "+1 408 555 1212" ],
  "uid" : [ "newuser" ]
}' \
'https://localhost:8443/hdap/dc=com/dc=example/ou=People?_prettyPrint=true'
```

> **Collapse: Show output**
>
> ```
> {
>   "_id" : "dc=com/dc=example/ou=People/uid=newuser",
>   "_rev" : "<revision>",
>   "objectClass" : [ "person", "inetOrgPerson", "organizationalPerson", "top" ],
>   "cn" : [ "New User" ],
>   "givenName" : [ "New" ],
>   "mail" : [ "newuser@example.com" ],
>   "manager" : [ "dc=com/dc=example/ou=People/uid=bjensen" ],
>   "sn" : [ "User" ],
>   "telephoneNumber" : [ "+1 408 555 1212" ],
>   "uid" : [ "newuser" ]
> }
> ```

* The command makes a secure connection to the server using HTTPS.

* The user performing the HTTP POST is the directory superuser.

  The default authorization mechanism for HTTP access is HTTP Basic authentication. The superuser's *(tooltip: \<div class="paragraph">
  \<p>An account with full administration privileges to bypass access control evaluation, change access controls, and change administrative privileges. Analogous to the Linux root and Windows Administrator accounts.\</p>
  \</div>)* HTTP user ID, `admin`, maps to the LDAP distinguished name (DN) *(tooltip: \<div class="paragraph">
  \<p>A name uniquely identifying an object within the hierarchy of a directory tree.\</p>
  \</div>)*, `uid=admin`. HDAP uses the DN and password to perform a simple LDAP bind *(tooltip: \<div class="paragraph">
  \<p>Bind with a user's entry DN and password.\</p>
  \</div>)* for authentication. The directory uses its LDAP-based access control mechanisms to authorize the operation.

* The successful response is the JSON resource that the command created.

  Fields names starting with an underscore like `_id` are reserved. For details, refer to [HDAP API reference](../rest-guide/rest-operations.html).

For additional details, refer to [HDAP API reference](../rest-guide/rest-operations.html) and [Create](../rest-guide/create-rest.html).

## Read

Use HDAP to read a user resource:

* Bash

* JavaScript

* PowerShell

* Python

* Ruby

* Zsh

```console
$ curl \
--request GET \
--cacert ca-cert.pem \
--user dc=com/dc=example/ou=People/uid=bjensen:hifalutin \
--header 'Content-Type: application/json' \
'https://localhost:8443/hdap/dc=com/dc=example/ou=People/uid=newuser?_prettyPrint=true'
```

> **Collapse: Show output**
>
> ```
> {
>   "_id" : "dc=com/dc=example/ou=People/uid=newuser",
>   "_rev" : "<revision>",
>   "objectClass" : [ "top", "person", "organizationalPerson", "inetOrgPerson" ],
>   "cn" : [ "New User" ],
>   "givenName" : [ "New" ],
>   "mail" : [ "newuser@example.com" ],
>   "manager" : [ "dc=com/dc=example/ou=People/uid=bjensen" ],
>   "sn" : [ "User" ],
>   "telephoneNumber" : [ "+1 408 555 1212" ],
>   "uid" : [ "newuser" ]
> }
> ```

```javascript
const { doRequest, getOptions } = require('./utils')

const options = getOptions({
    path: '/hdap/dc=com/dc=example/ou=People/uid=newuser'
})

doRequest('HDAP: read with GET', options)
    .then(response => { console.log(response) })
    .catch(error => { console.error(error) })
```

Source files for this sample: [read-newuser.js](../_attachments/hdap/js/read-newuser.js), [utils.js](../_attachments/hdap/js/utils.js)

```powershell
$Credentials = [System.Convert]::ToBase64String([System.Text.Encoding]::ASCII.GetBytes("dc=com/dc=example/ou=People/uid=bjensen:hifalutin"))
$Headers = @{
    Authorization = "Basic $Credentials"
}
Invoke-RestMethod `
 -Uri https://localhost:8443/hdap/dc=com/dc=example/ou=People/uid=newuser `
 -Method Get `
 -Headers $Headers `
 -ContentType application/json | ConvertTo-JSON
```

> **Collapse: Show output**
>
> ```
> {
>     "_id" : "dc=com/dc=example/ou=People/uid=newuser",
>     "_rev" : "<revision>",
>     "objectClass" : [ "top", "person", "organizationalPerson", "inetOrgPerson" ],
>     "cn" : [ "New User" ],
>     "givenName" : [ "New" ],
>     "mail" : [ "newuser@example.com" ],
>     "manager" : [ "dc=com/dc=example/ou=People/uid=bjensen" ],
>     "sn" : [ "User" ],
>     "telephoneNumber" : [ "+1 408 555 1212" ],
>     "uid" : [ "newuser" ]
> }
> ```

```python
#!/usr/bin/env python3

import requests
from requests.auth import HTTPBasicAuth
import utils

response = requests.get(
    f'https://{utils.host}:{utils.port}/hdap/dc=com/dc=example/ou=People/uid=newuser',
    auth=HTTPBasicAuth('dc=com/dc=example/ou=People/uid=kvaughan', 'bribery'),
    verify=utils.ca_pem)
print('Status code: %d\nJSON: %s' % (response.status_code, response.json()))
```

Source files for this sample: [utils.py](../_attachments/hdap/py/utils.py), [read-newuser.py](../_attachments/hdap/py/read-newuser.py)

```ruby
require_relative 'utils.rb'
require 'faraday'

utils = Utils.new('', '')
options = { ca_file: utils.ca_pem }
hdap = Faraday.new(url: "https://#{utils.host}:#{utils.port}/hdap/", ssl: options) do |f|
    f.headers['Content-Type'] = 'application/json'
    f.request :authorization, :basic, 'dc=com/dc=example/ou=People/uid=bjensen', 'hifalutin'
end
response = hdap.get('dc=com/dc=example/ou=People/uid=newuser')

puts "Status code: #{response.status}\nJSON: #{response.body}"
```

Source files for this sample: [utils.rb](../_attachments/hdap/rb/utils.rb), [read-newuser.rb](../_attachments/hdap/rb/read-newuser.rb)

HDAP Ruby examples require Ruby 3.2 and the `faraday` and `json` gems.

```console
$ curl \
--request GET \
--cacert ca-cert.pem \
--user dc=com/dc=example/ou=People/uid=bjensen:hifalutin \
--header 'Content-Type: application/json' \
'https://localhost:8443/hdap/dc=com/dc=example/ou=People/uid=newuser?_prettyPrint=true'
```

> **Collapse: Show output**
>
> ```
> {
>   "_id" : "dc=com/dc=example/ou=People/uid=newuser",
>   "_rev" : "<revision>",
>   "objectClass" : [ "top", "person", "organizationalPerson", "inetOrgPerson" ],
>   "cn" : [ "New User" ],
>   "givenName" : [ "New" ],
>   "mail" : [ "newuser@example.com" ],
>   "manager" : [ "dc=com/dc=example/ou=People/uid=bjensen" ],
>   "sn" : [ "User" ],
>   "telephoneNumber" : [ "+1 408 555 1212" ],
>   "uid" : [ "newuser" ]
> }
> ```

Authenticate when making this HTTP GET request. If no credentials are specified, the response is the HTTP 401 Unauthorized:

```json
{"code":401,"reason":"Unauthorized","message":"Invalid Credentials"}
```

In other words, the HTTP Basic authorization mechanism requires authentication even for read operations.

For additional details, refer to [HDAP API reference](../rest-guide/rest-operations.html) and [Read](../rest-guide/read-rest.html). You can also query collections of resources, as described in [Query](../rest-guide/query-rest.html).

## Update

Use HDAP to update a user resource:

* Bash

* JavaScript

* PowerShell

* Python

* Ruby

* Zsh

```console
$ curl \
--request PUT \
--cacert ca-cert.pem \
--user uid=admin:password \
--header 'Content-Type: application/json' \
--header "If-Match: *" \
--data '{
  "cn" : [ "Updated User" ],
  "givenName" : [ "Updated" ],
  "mail" : [ "updated.user@example.com" ],
  "telephoneNumber" : [ "+1 234 567 8910" ]
}' \
'https://localhost:8443/hdap/dc=com/dc=example/ou=People/uid=newuser?_prettyPrint=true'
```

> **Collapse: Show output**
>
> ```
> {
>   "_id" : "dc=com/dc=example/ou=People/uid=newuser",
>   "_rev" : "<revision>",
>   "objectClass" : [ "top", "person", "organizationalPerson", "inetOrgPerson" ],
>   "cn" : [ "Updated User" ],
>   "givenName" : [ "Updated" ],
>   "mail" : [ "updated.user@example.com" ],
>   "manager" : [ "dc=com/dc=example/ou=People/uid=bjensen" ],
>   "sn" : [ "User" ],
>   "telephoneNumber" : [ "+1 234 567 8910" ],
>   "uid" : [ "newuser" ]
> }
> ```

```javascript
const { doRequest, getOptions } = require('./utils')

const options = getOptions({
    path: '/hdap/dc=com/dc=example/ou=People/uid=newuser',
    credentials: 'uid=admin:password',
    method: 'PUT',
    body: {
        "cn": ["Updated User"],
        "givenName": ["Updated"],
        "mail": ["updated.user@example.com"],
        "telephoneNumber": ["+1 234 567 8910"]
    }
})

doRequest('HDAP: update newuser', options)
    .then(response => { console.log(response) })
    .catch(error => { console.error(error) })
```

Source files for this sample: [update-newuser.js](../_attachments/hdap/js/update-newuser.js), [utils.js](../_attachments/hdap/js/utils.js)

```powershell
$Credentials = [System.Convert]::ToBase64String([System.Text.Encoding]::ASCII.GetBytes("uid=admin:password"))
$Headers = @{
    "Authorization" = "Basic $Credentials"
    "If-Match"      = "*"
}
Invoke-RestMethod `
 -Uri https://localhost:8443/hdap/dc=com/dc=example/ou=People/uid=newuser `
 -Method Put `
 -Headers $Headers `
 -ContentType application/json `
 -Body @"
 {
    "cn" : [ "Updated User" ],
    "givenName" : [ "Updated" ],
    "mail" : [ "updated.user@example.com" ],
    "telephoneNumber" : [ "+1 234 567 8910" ]
 }
"@ | ConvertTo-JSON
```

> **Collapse: Show output**
>
> ```
> {
>     "_id" : "dc=com/dc=example/ou=People/uid=newuser",
>     "_rev" : "<revision>",
>     "objectClass" : [ "top", "person", "organizationalPerson", "inetOrgPerson" ],
>     "cn" : [ "Updated User" ],
>     "givenName" : [ "Updated" ],
>     "mail" : [ "updated.user@example.com" ],
>     "manager" : [ "dc=com/dc=example/ou=People/uid=bjensen" ],
>     "sn" : [ "User" ],
>     "telephoneNumber" : [ "+1 234 567 8910" ],
>     "uid" : [ "newuser" ]
> }
> ```

```python
#!/usr/bin/env python3

import requests
from requests.auth import HTTPBasicAuth
import utils

body = {
    'cn': ['Updated User'],
    'givenName': ['Updated'],
    'mail': ['updated.user@example.com'],
    'telephoneNumber': ['+1 234 567 8910']
}
headers = { 'Content-Type': 'application/json' }
response = requests.put(
    f'https://{utils.host}:{utils.port}/hdap/dc=com/dc=example/ou=People/uid=newuser',
    auth=HTTPBasicAuth('uid=admin', 'password'),
    headers=headers,
    json=body,
    verify=utils.ca_pem)
print('Status code: %d\nJSON: %s' % (response.status_code, response.json()))
```

Source files for this sample: [utils.py](../_attachments/hdap/py/utils.py), [update-newuser.py](../_attachments/hdap/py/update-newuser.py)

```ruby
require_relative 'utils.rb'
require 'faraday'
require 'json'

utils = Utils.new('', '')
options = { ca_file: utils.ca_pem }
fields = { '_fields': 'telephoneNumber' }
hdap = Faraday.new(url: "https://#{utils.host}:#{utils.port}/hdap/", params: fields, ssl: options) do |f|
    f.headers['Content-Type'] = 'application/json'
    f.request :authorization, :basic, 'uid=admin', 'password'
end
body = {
    "cn" => ["Updated User"],
    "givenName" => ["Updated"],
    "mail" => ["updated.user@example.com"],
    "telephoneNumber" => ["+1 234 567 8910"]
}
response = hdap.put do |h|
    h.path = 'dc=com/dc=example/ou=People/uid=newuser'
    h.body = JSON.generate(body)
end

puts "Status code: #{response.status}\nJSON: #{response.body}"
```

Source files for this sample: [utils.rb](../_attachments/hdap/rb/utils.rb), [update-newuser.rb](../_attachments/hdap/rb/update-newuser.rb)

HDAP Ruby examples require Ruby 3.2 and the `faraday` and `json` gems.

```console
$ curl \
--request PUT \
--cacert ca-cert.pem \
--user uid=admin:password \
--header 'Content-Type: application/json' \
--header "If-Match: *" \
--data '{
  "cn" : [ "Updated User" ],
  "givenName" : [ "Updated" ],
  "mail" : [ "updated.user@example.com" ],
  "telephoneNumber" : [ "+1 234 567 8910" ]
}' \
'https://localhost:8443/hdap/dc=com/dc=example/ou=People/uid=newuser?_prettyPrint=true'
```

> **Collapse: Show output**
>
> ```
> {
>   "_id" : "dc=com/dc=example/ou=People/uid=newuser",
>   "_rev" : "<revision>",
>   "objectClass" : [ "top", "person", "organizationalPerson", "inetOrgPerson" ],
>   "cn" : [ "Updated User" ],
>   "givenName" : [ "Updated" ],
>   "mail" : [ "updated.user@example.com" ],
>   "manager" : [ "dc=com/dc=example/ou=People/uid=bjensen" ],
>   "sn" : [ "User" ],
>   "telephoneNumber" : [ "+1 234 567 8910" ],
>   "uid" : [ "newuser" ]
> }
> ```

HDAP versions resources with revision numbers. A revision is specified in the resource's `_rev` field.

The `--header "If-Match: *"` tells HDAP to replace the resource regardless of its revision. Alternatively, set `--header "If-Match: revision"` to replace the resource only if its revision matches.

For additional details, refer to [HDAP API reference](../rest-guide/rest-operations.html) and [Update](../rest-guide/update-rest.html). You can also patch resources instead of replacing them entirely. Refer to [Patch](../rest-guide/patch-rest.html).

## Delete

Use HDAP to delete a user resource:

* Bash

* JavaScript

* PowerShell

* Python

* Ruby

* Zsh

```console
$ curl \
--request DELETE \
--cacert ca-cert.pem \
--user uid=admin:password \
--header 'Content-Type: application/json' \
'https://localhost:8443/hdap/dc=com/dc=example/ou=People/uid=newuser?_prettyPrint=true'
```

> **Collapse: Show output**
>
> ```
> {
>   "_id" : "dc=com/dc=example/ou=People/uid=newuser",
>   "_rev" : "<revision>",
>   "objectClass" : [ "top", "person", "organizationalPerson", "inetOrgPerson" ],
>   "cn" : [ "Updated User" ],
>   "givenName" : [ "Updated" ],
>   "mail" : [ "updated.user@example.com" ],
>   "manager" : [ "dc=com/dc=example/ou=People/uid=bjensen" ],
>   "sn" : [ "User" ],
>   "telephoneNumber" : [ "+1 234 567 8910" ],
>   "uid" : [ "newuser" ]
> }
> ```

```javascript
const { doRequest, getOptions } = require('./utils')

const options = getOptions({
    path: '/hdap/dc=com/dc=example/ou=People/uid=newuser',
    credentials: 'uid=admin:password',
    method: 'DELETE'
})

doRequest('HDAP: delete newuser', options)
    .then(response => { console.log(response) })
    .catch(error => { console.error(error) })
```

Source files for this sample: [delete-newuser.js](../_attachments/hdap/js/delete-newuser.js), [utils.js](../_attachments/hdap/js/utils.js)

```powershell
$Credentials = [System.Convert]::ToBase64String([System.Text.Encoding]::ASCII.GetBytes("uid=admin:password"))
$Headers = @{
    Authorization = "Basic $Credentials"
}
Invoke-RestMethod `
 -Uri https://localhost:8443/hdap/dc=com/dc=example/ou=People/uid=newuser `
 -Method Delete `
 -Headers $Headers `
 -ContentType application/json | ConvertTo-JSON
```

> **Collapse: Show output**
>
> ```
> {
>     "_id" : "dc=com/dc=example/ou=People/uid=newuser",
>     "_rev" : "<revision>",
>     "objectClass" : [ "top", "person", "organizationalPerson", "inetOrgPerson" ],
>     "cn" : [ "Updated User" ],
>     "givenName" : [ "Updated" ],
>     "mail" : [ "updated.user@example.com" ],
>     "manager" : [ "dc=com/dc=example/ou=People/uid=bjensen" ],
>     "sn" : [ "User" ],
>     "telephoneNumber" : [ "+1 234 567 8910" ],
>     "uid" : [ "newuser" ]
> }
> ```

```python
#!/usr/bin/env python3

import requests
from requests.auth import HTTPBasicAuth
import utils

response = requests.delete(
    f'https://{utils.host}:{utils.port}/hdap/dc=com/dc=example/ou=People/uid=newuser',
    auth=HTTPBasicAuth('uid=admin', 'password'),
    verify=utils.ca_pem)
print('Status code: %d\nJSON: %s' % (response.status_code, response.json()))
```

Source files for this sample: [utils.py](../_attachments/hdap/py/utils.py), [delete-newuser.py](../_attachments/hdap/py/delete-newuser.py)

```ruby
require_relative 'utils.rb'
require 'faraday'

utils = Utils.new('', '')
options = { ca_file: utils.ca_pem }
hdap = Faraday.new(url: "https://#{utils.host}:#{utils.port}/hdap/", ssl: options) do |f|
    f.headers['Content-Type'] = 'application/json'
    f.request :authorization, :basic, 'uid=admin', 'password'
end
response = hdap.delete('dc=com/dc=example/ou=People/uid=newuser')

puts "Status code: #{response.status}\nJSON: #{response.body}"
```

Source files for this sample: [utils.rb](../_attachments/hdap/rb/utils.rb), [delete-newuser.rb](../_attachments/hdap/rb/delete-newuser.rb)

HDAP Ruby examples require Ruby 3.2 and the `faraday` and `json` gems.

```console
$ curl \
--request DELETE \
--cacert ca-cert.pem \
--user uid=admin:password \
--header 'Content-Type: application/json' \
'https://localhost:8443/hdap/dc=com/dc=example/ou=People/uid=newuser?_prettyPrint=true'
```

> **Collapse: Show output**
>
> ```
> {
>   "_id" : "dc=com/dc=example/ou=People/uid=newuser",
>   "_rev" : "<revision>",
>   "objectClass" : [ "top", "person", "organizationalPerson", "inetOrgPerson" ],
>   "cn" : [ "Updated User" ],
>   "givenName" : [ "Updated" ],
>   "mail" : [ "updated.user@example.com" ],
>   "manager" : [ "dc=com/dc=example/ou=People/uid=bjensen" ],
>   "sn" : [ "User" ],
>   "telephoneNumber" : [ "+1 234 567 8910" ],
>   "uid" : [ "newuser" ]
> }
> ```

For additional details, refer to [HDAP API reference](../rest-guide/rest-operations.html) and [Delete](../rest-guide/delete-rest.html).

---

---
title: Learn LDAP
description: Learn how to use PingDS command-line tools to send LDAP search, modify, add, and delete requests against a local server.
component: pingds
version: 8.1
page_id: pingds:getting-started:ldap
canonical_url: https://docs.pingidentity.com/pingds/8.1/getting-started/ldap.html
llms_txt: https://docs.pingidentity.com/pingds/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2025-10-22T14:42:39Z
keywords: ["Evaluation", "LDAP"]
section_ids:
  search-ldap: Search
  modify-ldap: Modify
  add-ldap: Add
  delete-ldap: Delete
---

# Learn LDAP

Lightweight Directory Access Protocol (LDAP) *(tooltip: \<div class="paragraph">
\<p>An open, cross-platform protocol used for interacting with directory services.\</p>
\</div>)* is a standard internet protocol. The following examples show you how to use bundled DS command-line tools to send LDAP requests.

Before you try the examples, set up a server, as described in [Install DS](install.html). Make sure you added the command-line tools to your PATH:

* Bash

* PowerShell

* Zsh

```console
$ export PATH=/path/to/opendj/bin:${PATH}
```

```powershell
$env:PATH += ";C:\path\to\opendj\bat"
```

```console
$ export PATH=/path/to/opendj/bin:${PATH}
```

## Search

Searching the directory is like looking for someone's phone number when all you know is their name. You use the value of an attribute you know—​in this case, their name—​to find their profile. Their profile—​in LDAP, their entry—​has other attributes of interest like their phone number or email address.

When looking up a person's entry by their name, more information helps narrow down your search. If two people with the same name live in Los Angeles and New York, you need to know where they live to choose the right person. In an LDAP directory, you need to know at least the base distinguished name (DN) *(tooltip: \<div class="paragraph">
\<p>A name uniquely identifying an object within the hierarchy of a directory tree.\</p>
\</div>)* for the search.

For this example, assume you know a user's full name, `Babs Jensen`, and that Babs Jensen's entry is under the base DN `dc=example,dc=com`. You want to look up Babs Jensen's email and office location. The following command sends an appropriate LDAP search request to the server you installed:

* Bash

* PowerShell

* Zsh

```console
$ ldapsearch \
 --hostname localhost \
 --port 1636 \
 --useSsl \
 --trustStorePath /path/to/opendj/config/keystore \
 --trustStoreType PKCS12 \
 --trustStorePassword:file /path/to/opendj/config/keystore.pin \
 --bindDN uid=bjensen,ou=People,dc=example,dc=com \
 --bindPassword hifalutin \
 --baseDn dc=example,dc=com \
 "(cn=Babs Jensen)" \
 cn mail street l
```

> **Collapse: Show output**
>
> ```
> dn: uid=bjensen,ou=People,dc=example,dc=com
> cn: Barbara Jensen
> cn: Babs Jensen
> l: San Francisco
> mail: bjensen@example.com
> street: 201 Mission Street Suite 2900
> ```

```powershell
ldapsearch.bat `
 --hostname localhost `
 --port 1636 `
 --useSsl `
 --trustStorePath C:\path\to\opendj\config\
 --trustStoreType PKCS12 \keystore `
 --trustStorePassword:file C:\path\to\opendj\config\keystore.pin `
 --bindDN uid=bjensen,ou=People,dc=example,dc=com `
 --bindPassword hifalutin `
 --baseDn dc=example,dc=com `
 "(cn=Babs Jensen)" `
 cn mail street l
```

> **Collapse: Show output**
>
> ```
> dn: uid=bjensen,ou=People,dc=example,dc=com
> cn: Barbara Jensen
> cn: Babs Jensen
> l: San Francisco
> mail: bjensen@example.com
> street: 201 Mission Street Suite 2900
> ```

```console
$ ldapsearch \
 --hostname localhost \
 --port 1636 \
 --useSsl \
 --trustStorePath /path/to/opendj/config/keystore \
 --trustStoreType PKCS12 \
 --trustStorePassword:file /path/to/opendj/config/keystore.pin \
 --bindDN uid=bjensen,ou=People,dc=example,dc=com \
 --bindPassword hifalutin \
 --baseDn dc=example,dc=com \
 "(cn=Babs Jensen)" \
 cn mail street l
```

> **Collapse: Show output**
>
> ```
> dn: uid=bjensen,ou=People,dc=example,dc=com
> cn: Barbara Jensen
> cn: Babs Jensen
> l: San Francisco
> mail: bjensen@example.com
> street: 201 Mission Street Suite 2900
> ```

> **Collapse: More about the search example**
>
> Notice the following characteristics of the search:
>
> * The command makes a secure connection to the server using LDAPS *(tooltip: \<div class="paragraph">
>   \<p>LDAP over TLS.\</p>
>   \</div>)*.
>
>   The command relies on the server's truststore to trust the CA certificate used to sign the server certificate.
>
> * The base DN option, `--baseDn dc=example,dc=com`, tells the server where to look for Babs Jensen's entry. Servers can hold data for multiple base DNs, so this is important information.
>
>   It is possible to restrict the scope of the search, but the default is to search the entire subtree under the base DN.
>
> * The command uses a LDAP search filter (filter) *(tooltip: \<div class="paragraph">
>   \<p>An expression the server uses to find entries matching a search request.\</p>
>   \</div>)*, `"(cn=Babs Jensen)"`, which tells the server, "Find entries whose `cn` attribute exactly matches the string `Babs Jensen` without regard to case."
>
>   The `cn` (`commonName`) attribute is a standard attribute for full names.
>
>   Internally, the directory server has an equality index for the `cn` attribute. The directory uses the index to quickly find matches for `babs jensen`. The default behavior in LDAP is to ignore case, so `"(cn=Babs Jensen)"`, `"(cn=babs jensen)"`, and `"(CN=BABS JENSEN)"` are equivalent.
>
>   If more than one entry matches the filter, the server returns multiple entries.
>
> * The filter is followed by a list of attributes *(tooltip: \<div class="paragraph">
>   \<p>A property of a directory entry, stored as one or more key-value pairs.\</p>
>   \</div>)*, `cn mail street l`. This tells the server to return only the specified attributes in the search result entries. By default, if you do not specify the attributes to return, the server returns all the user attributes that you have the right to read.
>
> * The result shows attributes from a single entry. Notice that an LDAP entry, represented here in the standard LDIF format, has a flat structure with no nesting.
>
>   The DN that uniquely identifies the entry is `uid=bjensen,ou=People,dc=example,dc=com`. Multiple entries can have the same attribute values, but each must have a unique DN. This is the same as saying that the leading relative distinguished name (RDN) *(tooltip: \<div class="paragraph">
>   \<p>The initial portion of a DN distinguishing the entry from all others at the same level.\</p>
>   \</div>)* value must be unique at this level in the hierarchy. Only one entry directly under `ou=People,dc=example,dc=com` has the RDN `uid=bjensen`.
>
>   The `mail`, `street`, `l` (location), and `uid` attributes are all standard LDAP attributes like `cn`.

For additional examples, refer to [LDAP search](../ldap-guide/search-ldap.html).

## Modify

You installed the server with the `ds-evaluation` profile. That profile grants access to search Example.com data without authenticating to the directory. When modifying directory data, however, you must authenticate first. LDAP servers must know who you are to determine what you have access to.

In the following example Babs Jensen modifies the description on her own entry:

* Bash

* PowerShell

* Zsh

```console
$ ldapmodify \
 --hostname localhost \
 --port 1636 \
 --useSsl \
 --trustStorePath /path/to/opendj/config/keystore \
 --trustStoreType PKCS12 \
 --trustStorePassword:file /path/to/opendj/config/keystore.pin \
 --bindDn uid=bjensen,ou=People,dc=example,dc=com \
 --bindPassword hifalutin <<EOF
dn: uid=bjensen,ou=People,dc=example,dc=com
changetype: modify
replace: description
description: New description
EOF
```

> **Collapse: Show output**
>
> ```
> # MODIFY operation successful for DN uid=bjensen,ou=People,dc=example,dc=com
> ```

```powershell
New-Item -Path . -Name "description.ldif" -ItemType "file" -Value @"
dn: uid=bjensen,ou=People,dc=example,dc=com
changetype: modify
replace: description
description: New description
"@
ldapmodify.bat `
 --hostname localhost `
 --port 1636 `
 --useSsl `
 --trustStorePath C:\path\to\opendj\config\
 --trustStoreType PKCS12 \keystore `
 --trustStorePassword:file C:\path\to\opendj\config\keystore.pin `
 --bindDn uid=bjensen,ou=People,dc=example,dc=com `
 --bindPassword hifalutin `
 description.ldif
```

> **Collapse: Show output**
>
> ```
> # MODIFY operation successful for DN uid=bjensen,ou=People,dc=example,dc=com
> ```

```console
$ ldapmodify \
 --hostname localhost \
 --port 1636 \
 --useSsl \
 --trustStorePath /path/to/opendj/config/keystore \
 --trustStoreType PKCS12 \
 --trustStorePassword:file /path/to/opendj/config/keystore.pin \
 --bindDn uid=bjensen,ou=People,dc=example,dc=com \
 --bindPassword hifalutin <<EOF
dn: uid=bjensen,ou=People,dc=example,dc=com
changetype: modify
replace: description
description: New description
EOF
```

> **Collapse: Show output**
>
> ```
> # MODIFY operation successful for DN uid=bjensen,ou=People,dc=example,dc=com
> ```

> **Collapse: More about the modify example**
>
> * Babs Jensen's authentication credentials are provided with the `--bindDn` and `--bindPassword` options. Notice that the user identifier is Babs Jensen's DN.
>
>   Authentication operations bind an LDAP identity to a connection. In LDAP, a client application connects to the server, then binds an identity to the connection. An LDAP client application keeps its connection open until it finishes performing its operations. The server uses the identity bound to the connection to make authorization *(tooltip: \<div class="paragraph">
>   \<p>The act of determining whether to grant or deny a user access to a resource.\</p>
>   \</div>)* decisions for subsequent operations, such as search and modify requests.
>
>   If no credentials are provided, then the identity for the connection is that of an anonymous user. As a directory administrator, you can configure access controls for anonymous users just as you configure access controls for other users.
>
>   A simple bind *(tooltip: \<div class="paragraph">
>   \<p>Bind with a user's entry DN and password.\</p>
>   \</div>)* involving a DN and a password is just one of several supported authentication mechanisms. The documentation frequently shows simple binds in examples because this kind of authentication is so familiar. Alternatives include authenticating with a digital certificate, or using Kerberos.
>
> * The modification is expressed in standard LDAP Data Interchange Format (LDIF).
>
>   The LDIF specifies the DN of the target entry to modify. It then indicates that the change to perform is an LDAP modify, and that the value `New description` is to replace existing values of the `description` attribute.
>
> * Notice that the result is a comment indicating success. The command's return code—​0, but not shown in the example—​also indicates success.
>
>   The scripts and applications that you write should use and trust LDAP return codes.

For additional examples, refer to [LDAP updates](../ldap-guide/write-ldap.html) and [Passwords and accounts](../ldap-guide/passwords-and-accounts.html).

## Add

Authorized users can modify attributes, and can also add and delete directory entries.

The following example adds a new user entry to the directory:

* Bash

* PowerShell

* Zsh

```console
$ ldapmodify \
 --hostname localhost \
 --port 1636 \
 --useSsl \
 --trustStorePath /path/to/opendj/config/keystore \
 --trustStoreType PKCS12 \
 --trustStorePassword:file /path/to/opendj/config/keystore.pin \
 --bindDn uid=admin \
 --bindPassword password <<EOF
dn: uid=newuser,ou=People,dc=example,dc=com
uid: newuser
objectClass: person
objectClass: organizationalPerson
objectClass: inetOrgPerson
objectClass: top
cn: New User
sn: User
ou: People
mail: newuser@example.com
userPassword: chngthspwd
EOF
```

> **Collapse: Show output**
>
> ```
> # ADD operation successful for DN uid=newuser,ou=People,dc=example,dc=com
> ```

```powershell
New-Item -Path . -Name "user.ldif" -ItemType "file" -Value @"
dn: uid=newuser,ou=People,dc=example,dc=com
uid: newuser
objectClass: person
objectClass: organizationalPerson
objectClass: inetOrgPerson
objectClass: top
cn: New User
sn: User
ou: People
mail: newuser@example.com
userPassword: chngthspwd
"@
ldapmodify.bat `
 --hostname localhost `
 --port 1636 `
 --useSsl `
 --trustStorePath C:\path\to\opendj\config\
 --trustStoreType PKCS12 \keystore `
 --trustStorePassword:file C:\path\to\opendj\config\keystore.pin `
 --bindDn uid=admin `
 --bindPassword password `
 user.ldif
```

> **Collapse: Show output**
>
> ```
> # ADD operation successful for DN uid=newuser,ou=People,dc=example,dc=com
> ```

```console
$ ldapmodify \
 --hostname localhost \
 --port 1636 \
 --useSsl \
 --trustStorePath /path/to/opendj/config/keystore \
 --trustStoreType PKCS12 \
 --trustStorePassword:file /path/to/opendj/config/keystore.pin \
 --bindDn uid=admin \
 --bindPassword password <<EOF
dn: uid=newuser,ou=People,dc=example,dc=com
uid: newuser
objectClass: person
objectClass: organizationalPerson
objectClass: inetOrgPerson
objectClass: top
cn: New User
sn: User
ou: People
mail: newuser@example.com
userPassword: chngthspwd
EOF
```

> **Collapse: Show output**
>
> ```
> # ADD operation successful for DN uid=newuser,ou=People,dc=example,dc=com
> ```

> **Collapse: More about the add example**
>
> * The bind DN for the user requesting the add is `uid=admin`. It is also possible to authorize regular users to add entries.
>
> * The entry to add is expressed in standard LDIF.

For additional examples, refer to [LDAP updates](../ldap-guide/write-ldap.html).

## Delete

The following example deletes the user added in [Add](#add-ldap):

* Bash

* PowerShell

* Zsh

```console
$ ldapdelete \
 --hostname localhost \
 --port 1636 \
 --useSsl \
 --trustStorePath /path/to/opendj/config/keystore \
 --trustStoreType PKCS12 \
 --trustStorePassword:file /path/to/opendj/config/keystore.pin \
 --bindDn uid=admin \
 --bindPassword password \
 uid=newuser,ou=People,dc=example,dc=com
```

> **Collapse: Show output**
>
> ```
> # DELETE operation successful for DN uid=newuser,ou=People,dc=example,dc=com
> ```

```powershell
ldapdelete.bat `
 --hostname localhost `
 --port 1636 `
 --useSsl `
 --trustStorePath C:\path\to\opendj\config\
 --trustStoreType PKCS12 \keystore `
 --trustStorePassword:file C:\path\to\opendj\config\keystore.pin `
 --bindDn uid=admin `
 --bindPassword password `
 uid=newuser,ou=People,dc=example,dc=com
```

> **Collapse: Show output**
>
> ```
> # DELETE operation successful for DN uid=newuser,ou=People,dc=example,dc=com
> ```

```console
$ ldapdelete \
 --hostname localhost \
 --port 1636 \
 --useSsl \
 --trustStorePath /path/to/opendj/config/keystore \
 --trustStoreType PKCS12 \
 --trustStorePassword:file /path/to/opendj/config/keystore.pin \
 --bindDn uid=admin \
 --bindPassword password \
 uid=newuser,ou=People,dc=example,dc=com
```

> **Collapse: Show output**
>
> ```
> # DELETE operation successful for DN uid=newuser,ou=People,dc=example,dc=com
> ```

Notice that the `ldapdelete` command specifies the entry to delete by its DN.

For additional examples, refer to [LDAP updates](../ldap-guide/write-ldap.html).

---

---
title: Learn replication
description: Learn how to set up a PingDS replica, test data synchronization under normal and disrupted conditions, and read the external change log.
component: pingds
version: 8.1
page_id: pingds:getting-started:replication
canonical_url: https://docs.pingidentity.com/pingds/8.1/getting-started/replication.html
llms_txt: https://docs.pingidentity.com/pingds/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2025-10-22T14:42:39Z
keywords: ["Evaluation", "Replication", "LDAP"]
section_ids:
  setup-repl: Add a replica
  try-repl: Try replication
  read-changelog: Notifications
---

# Learn replication

Replication provides automatic data synchronization between directory servers. It ensures that all directory servers eventually share a consistent set of directory data.

> **Collapse: More about replication**
>
> Replication requires two or more directory servers and additional configuration. This page takes you though the setup process quickly, providing commands that you can reuse. It does not explain each command in detail.
>
> ![Two replicated DS servers with a client application using each server](../_images/replication.png)
>
> For a full discussion of the subject, refer to [Replication](../config-guide/replication.html) and the related pages.

## Add a replica

High-level steps:

1. Unpack the files for a second directory server in a different folder.

2. Set up the new server as a replica of the first server using the generated `<deployment-id>` from [Install DS](install.html).

The following example demonstrates the process:

* Bash

* PowerShell

* Zsh

```bash
# Unpack files for a second, replica server in a different folder:
cd ~/Downloads && unzip ~/Downloads/DS-8.1.1.zip && mv opendj /path/to/replica

# Set up a second, replica server:
/path/to/replica/setup \
 --serverId second-ds \
 --deploymentId $DEPLOYMENT_ID \
 --deploymentIdPassword password \
 --rootUserDn uid=admin \
 --rootUserPassword password \
 --hostname localhost \
 --ldapPort 11389 \
 --ldapsPort 11636 \
 --adminConnectorPort 14444 \
 --replicationPort 18989 \
 --bootstrapReplicationServer localhost:8989 \
 --profile ds-evaluation \
 --start \
 --acceptLicense
```

```powershell
# Unpack files for a second, replica server in a different folder:
Expand-Archive DS-8.1.1.zip C:\Temp
Rename-Item -Path C:\Temp\opendj -NewName C:\Temp\replica
Move-Item C:\Temp\replica C:\path\to

# Set up a second, replica server:
C:\path\to\replica\setup.bat `
 --serverId second-ds `
 --deploymentId <deployment-id> `
 --deploymentIdPassword password `
 --rootUserDn uid=admin `
 --rootUserPassword password `
 --hostname localhost `
 --ldapPort 11389 `
 --ldapsPort 11636 `
 --adminConnectorPort 14444 `
 --replicationPort 18989 \
 --bootstrapReplicationServer locahost:8989 \
 --profile ds-evaluation `
 --start `
 --acceptLicense
```

```zsh
# Unpack files for a second, replica server in a different folder:
cd ~/Downloads && unzip ~/Downloads/DS-8.1.1.zip && mv opendj /path/to/replica

# Set up a second, replica server:
/path/to/replica/setup \
 --serverId second-ds \
 --deploymentId $DEPLOYMENT_ID \
 --deploymentIdPassword password \
 --rootUserDn uid=admin \
 --rootUserPassword password \
 --hostname localhost \
 --ldapPort 11389 \
 --ldapsPort 11636 \
 --adminConnectorPort 14444 \
 --replicationPort 18989 \
 --bootstrapReplicationServer localhost:8989 \
 --profile ds-evaluation \
 --start \
 --acceptLicense
```

## Try replication

With the new replica set up and started, show that replication works:

* Bash

* PowerShell

* Zsh

```bash
# Update a description on the first server:
ldapmodify \
 --hostname localhost \
 --port 1636 \
 --useSsl \
 --trustStorePath /path/to/opendj/config/keystore \
 --trustStoreType PKCS12 \
 --trustStorePassword:file /path/to/opendj/config/keystore.pin \
 --bindDn uid=bjensen,ou=People,dc=example,dc=com \
 --bindPassword hifalutin << EOF
dn: uid=bjensen,ou=People,dc=example,dc=com
changetype: modify
replace: description
description: Replicate this
EOF

# On the first server, read the description to see the effects of your change:
ldapsearch \
 --hostname localhost \
 --port 1636 \
 --useSsl \
 --trustStorePath /path/to/opendj/config/keystore \
 --trustStoreType PKCS12 \
 --trustStorePassword:file /path/to/opendj/config/keystore.pin \
 --bindDN uid=bjensen,ou=People,dc=example,dc=com \
 --bindPassword hifalutin \
 --baseDn dc=example,dc=com \
 "(cn=Babs Jensen)" \
 description

# On the second server, read the description to see the change has been replicated:
ldapsearch \
 --hostname localhost \
 --port 11636 \
 --useSsl \
 --trustStorePath /path/to/opendj/config/keystore \
 --trustStoreType PKCS12 \
 --trustStorePassword:file /path/to/opendj/config/keystore.pin \
 --bindDN uid=bjensen,ou=People,dc=example,dc=com \
 --bindPassword hifalutin \
 --baseDn dc=example,dc=com \
 "(cn=Babs Jensen)" \
 description
```

```powershell
# Update a description on the first server:
New-Item -Path . -Name "mod-desc.ldif" -ItemType "file" -Value @"
dn: uid=bjensen,ou=People,dc=example,dc=com
changetype: modify
replace: description
description: Replicate this
"@

ldapmodify.bat `
 --hostname localhost `
 --port 1636 `
 --useSsl `
 --trustStorePath C:\path\to\opendj\config\
 --trustStoreType PKCS12 \keystore `
 --trustStorePassword:file C:\path\to\opendj\config\keystore.pin `
 --bindDn uid=bjensen,ou=People,dc=example,dc=com `
 --bindPassword password `
 mod-desc.ldif

# On the first server, read the description to see the effects of your change:
ldapsearch.bat `
 --hostname localhost `
 --port 1636 `
 --useSsl `
 --trustStorePath C:\path\to\opendj\config\
 --trustStoreType PKCS12 \keystore `
 --trustStorePassword:file C:\path\to\opendj\config\keystore.pin `
 --bindDN uid=bjensen,ou=People,dc=example,dc=com `
 --bindPassword hifalutin `
 --baseDn dc=example,dc=com `
 "(cn=Babs Jensen)" `
 description

# On the second server, read the description to see the change has been replicated:
ldapsearch.bat `
 --hostname localhost `
 --port 11636 `
 --useSsl `
 --trustStorePath C:\path\to\opendj\config\
 --trustStoreType PKCS12 \keystore `
 --trustStorePassword:file C:\path\to\opendj\config\keystore.pin `
 --bindDN uid=bjensen,ou=People,dc=example,dc=com `
 --bindPassword hifalutin `
 --baseDn dc=example,dc=com `
 "(cn=Babs Jensen)" `
 description
```

```zsh
# Update a description on the first server:
ldapmodify \
 --hostname localhost \
 --port 1636 \
 --useSsl \
 --trustStorePath /path/to/opendj/config/keystore \
 --trustStoreType PKCS12 \
 --trustStorePassword:file /path/to/opendj/config/keystore.pin \
 --bindDn uid=bjensen,ou=People,dc=example,dc=com \
 --bindPassword hifalutin << EOF
dn: uid=bjensen,ou=People,dc=example,dc=com
changetype: modify
replace: description
description: Replicate this
EOF

# On the first server, read the description to see the effects of your change:
ldapsearch \
 --hostname localhost \
 --port 1636 \
 --useSsl \
 --trustStorePath /path/to/opendj/config/keystore \
 --trustStoreType PKCS12 \
 --trustStorePassword:file /path/to/opendj/config/keystore.pin \
 --bindDN uid=bjensen,ou=People,dc=example,dc=com \
 --bindPassword hifalutin \
 --baseDn dc=example,dc=com \
 "(cn=Babs Jensen)" \
 description

# On the second server, read the description to see the change has been replicated:
ldapsearch \
 --hostname localhost \
 --port 11636 \
 --useSsl \
 --trustStorePath /path/to/opendj/config/keystore \
 --trustStoreType PKCS12 \
 --trustStorePassword:file /path/to/opendj/config/keystore.pin \
 --bindDN uid=bjensen,ou=People,dc=example,dc=com \
 --bindPassword hifalutin \
 --baseDn dc=example,dc=com \
 "(cn=Babs Jensen)" \
 description
```

Show replication works despite crashes and network interruptions:

* Bash

* PowerShell

* Zsh

```bash
# Stop the second server to simulate a network outage or server crash:
/path/to/replica/bin/stop-ds

# On the first server, update the description again:
ldapmodify \
 --hostname localhost \
 --port 1636 \
 --useSsl \
 --trustStorePath /path/to/opendj/config/keystore \
 --trustStoreType PKCS12 \
 --trustStorePassword:file /path/to/opendj/config/keystore.pin \
 --bindDn uid=bjensen,ou=People,dc=example,dc=com \
 --bindPassword hifalutin <<EOF
dn: uid=bjensen,ou=People,dc=example,dc=com
changetype: modify
replace: description
description: Second server is stopped
EOF

# On the first server, read the description to see the change:
ldapsearch \
 --hostname localhost \
 --port 1636 \
 --useSsl \
 --trustStorePath /path/to/opendj/config/keystore \
 --trustStoreType PKCS12 \
 --trustStorePassword:file /path/to/opendj/config/keystore.pin \
 --bindDN uid=bjensen,ou=People,dc=example,dc=com \
 --bindPassword hifalutin \
 --baseDn dc=example,dc=com \
 "(cn=Babs Jensen)" \
 description

# Start the second server again to simulate recovery:
/path/to/replica/bin/start-ds

# On the second server, read the description to check that replication has resumed:
ldapsearch \
 --hostname localhost \
 --port 11636 \
 --useSsl \
 --trustStorePath /path/to/opendj/config/keystore \
 --trustStoreType PKCS12 \
 --trustStorePassword:file /path/to/opendj/config/keystore.pin \
 --bindDN uid=bjensen,ou=People,dc=example,dc=com \
 --bindPassword hifalutin \
 --baseDn dc=example,dc=com \
 "(cn=Babs Jensen)" \
 description
```

```powershell
# Stop the second server to simulate a network outage or server crash:
C:\path\to\replica\bat\stop-ds.bat

# On the first server, update the description again:
New-Item -Path . -Name "mod-desc2.ldif" -ItemType "file" -Value @"
dn: uid=bjensen,ou=People,dc=example,dc=com
changetype: modify
replace: description
description: Second server is stopped
"@

ldapmodify.bat `
 --hostname localhost `
 --port 1636 `
 --useSsl `
 --trustStorePath C:\path\to\opendj\config\
 --trustStoreType PKCS12 \keystore `
 --trustStorePassword:file C:\path\to\opendj\config\keystore.pin `
 --bindDn uid=bjensen,ou=People,dc=example,dc=com `
 --bindPassword password `
mod-desc2.ldif

# On the first server, read the description to see the change:
ldapsearch.bat `
 --hostname localhost `
 --port 1636 `
 --useSsl `
 --trustStorePath C:\path\to\opendj\config\
 --trustStoreType PKCS12 \keystore `
 --trustStorePassword:file C:\path\to\opendj\config\keystore.pin `
 --bindDN uid=bjensen,ou=People,dc=example,dc=com `
 --bindPassword hifalutin `
 --baseDn dc=example,dc=com `
 "(cn=Babs Jensen)" `
 description

# Start the second server again to simulate recovery:
C:\path\to\replica\bat\start-ds.bat

# On the second server, read the description to check that replication has resumed:
ldapsearch.bat `
 --hostname localhost `
 --port 11636 `
 --useSsl `
 --trustStorePath C:\path\to\opendj\config\
 --trustStoreType PKCS12 \keystore `
 --trustStorePassword:file C:\path\to\opendj\config\keystore.pin `
 --bindDN uid=bjensen,ou=People,dc=example,dc=com `
 --bindPassword hifalutin `
 --baseDn dc=example,dc=com `
 "(cn=Babs Jensen)" `
 description
```

```zsh
# Stop the second server to simulate a network outage or server crash:
/path/to/replica/bin/stop-ds

# On the first server, update the description again:
ldapmodify \
 --hostname localhost \
 --port 1636 \
 --useSsl \
 --trustStorePath /path/to/opendj/config/keystore \
 --trustStoreType PKCS12 \
 --trustStorePassword:file /path/to/opendj/config/keystore.pin \
 --bindDn uid=bjensen,ou=People,dc=example,dc=com \
 --bindPassword hifalutin <<EOF
dn: uid=bjensen,ou=People,dc=example,dc=com
changetype: modify
replace: description
description: Second server is stopped
EOF

# On the first server, read the description to see the change:
ldapsearch \
 --hostname localhost \
 --port 1636 \
 --useSsl \
 --trustStorePath /path/to/opendj/config/keystore \
 --trustStoreType PKCS12 \
 --trustStorePassword:file /path/to/opendj/config/keystore.pin \
 --bindDN uid=bjensen,ou=People,dc=example,dc=com \
 --bindPassword hifalutin \
 --baseDn dc=example,dc=com \
 "(cn=Babs Jensen)" \
 description

# Start the second server again to simulate recovery:
/path/to/replica/bin/start-ds

# On the second server, read the description to check that replication has resumed:
ldapsearch \
 --hostname localhost \
 --port 11636 \
 --useSsl \
 --trustStorePath /path/to/opendj/config/keystore \
 --trustStoreType PKCS12 \
 --trustStorePassword:file /path/to/opendj/config/keystore.pin \
 --bindDN uid=bjensen,ou=People,dc=example,dc=com \
 --bindPassword hifalutin \
 --baseDn dc=example,dc=com \
 "(cn=Babs Jensen)" \
 description
```

Unlike some databases, DS replication does not operate in active-passive mode. Instead, you read and write on any running server. Replication replays your changes as soon as possible. Show this to check your understanding:

1. Stop the first server.

   > **Collapse: Hint**
   >
   > Use the `stop-ds` command.

2. Modify an entry on the second server.

   > **Collapse: Hint**
   >
   > Refer to [Modify](ldap.html#modify-ldap).

3. Restart the first server.

   > **Collapse: Hint**
   >
   > Use the `start-ds` command.

4. Search for the modified entry on the first server to check that replication replays the change.

   > **Collapse: Hint**
   >
   > Refer to [Search](ldap.html#search-ldap).

## Notifications

Some applications require notification when directory data updates occur. For example, IDM can sync directory data with another database. Other applications do more processing when certain updates occur.

Replicated DS directory servers publish an external change log over LDAP. This changelog lets authorized client applications read changes to directory data:

* Bash

* PowerShell

* Zsh

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

```powershell
ldapsearch.bat `
 --hostname localhost `
 --port 1636 `
 --useSsl `
 --trustStorePath C:\path\to\opendj\config\
 --trustStoreType PKCS12 \keystore `
 --trustStorePassword:file C:\path\to\opendj\config\keystore.pin `
 --bindDN uid=admin `
 --bindPassword password `
 --baseDN cn=changelog `
 --control "ecl:true" `
 "(objectclass=*)" `
 changes changeLogCookie targetDN
```

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

When looking at the output of the command (not shown here), notice that the `changes` values are base64-encoded in LDIF because they include line breaks. You can use the DS `base64` command to decode them. For details, refer to [Changelog for notifications](../config-guide/changelog.html).

---

---
title: Measure performance
description: Measure PingDS throughput and response times for LDAP modifications and searches using the modrate and searchrate command-line tools.
component: pingds
version: 8.1
page_id: pingds:getting-started:performance
canonical_url: https://docs.pingidentity.com/pingds/8.1/getting-started/performance.html
llms_txt: https://docs.pingidentity.com/pingds/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2025-10-22T14:42:39Z
keywords: ["Evaluation", "Performance", "LDAP"]
section_ids:
  perfs-mods: Measure modification rates
  perfs-searches: Measure search rates
  perfs-check-repl: Check replication
---

# Measure performance

DS directory servers offer high throughput and low response times for most operations. DS software includes the following command-line tools for measuring performance of common LDAP operations:

* `addrate` measures LDAP adds and deletes

* `authrate` measures LDAP binds

* `modrate` measures LDAP modifications

* `searchrate` measures LDAP searches

|   |                                                                                                                                                                                                                                                                                                                               |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Before trying the examples that follow, work through the previous examples. You should have two directory server replicas running on your local computer, as described in [Learn replication](replication.html):![Two replicated DS servers with a client application running a performance tool](../_images/performance.png) |

The following examples show how to measure and verify basic directory performance. For a deeper dive into the subject, read [Performance tuning](../config-guide/tuning.html).

## Measure modification rates

In deployment, you can expect many directory client applications to change directory data in parallel. The directory has to serve all these requests with high throughput (lots of requests) and low latency (quick responses), so all the client applications can get their work done quickly.

As a first step towards tuning your directory service performance, get a sense of the throughput and response times you can expect by measuring the LDAP modification rate with the `modrate` command:

* Bash

* PowerShell

* Zsh

```shell
# Run modrate for 10 seconds against the first server:
modrate \
 --maxDuration 10 \
 --hostname localhost \
 --port 1636 \
 --useSsl \
 --trustStorePath /path/to/opendj/config/keystore \
 --trustStoreType PKCS12 \
 --trustStorePassword:file /path/to/opendj/config/keystore.pin \
 --bindDn uid=kvaughan,ou=People,dc=example,dc=com \
 --bindPassword bribery \
 --noRebind \
 --numConnections 4 \
 --numConcurrentRequests 4 \
 --targetDn "uid=user.{1},ou=people,dc=example,dc=com" \
 --argument "rand(0,100000)" \
 --argument "randstr(16)" \
 "description:{2}"

# Read number of modify requests on the LDAPS port:
ldapsearch \
 --hostname localhost \
 --port 1636 \
 --useSsl \
 --trustStorePath /path/to/opendj/config/keystore \
 --trustStoreType PKCS12 \
 --trustStorePassword:file /path/to/opendj/config/keystore.pin \
 --bindDN uid=monitor \
 --bindPassword password \
 --baseDN "cn=LDAPS,cn=connection handlers,cn=monitor" \
 "(&)" \
 ds-mon-requests-modify
```

```powershell
# Run modrate for 10 seconds against the first server, and observe the performance numbers:
modrate.bat `
 --maxDuration 10 `
 --hostname localhost `
 --port 1636 `
 --useSsl `
 --trustStorePath C:\path\to\opendj\config\
 --trustStoreType PKCS12 \keystore `
 --trustStorePassword:file C:\path\to\opendj\config\keystore.pin `
 --bindDn uid=kvaughan,ou=People,dc=example,dc=com `
 --bindPassword bribery `
 --noRebind `
 --numConnections 4 `
 --numConcurrentRequests 4 `
 --targetDn "uid=user.{1},ou=people,dc=example,dc=com" `
 --argument "rand(0,100000)" `
 --argument "randstr(16)" `
 "description:{2}"

# Read number of modify requests on the LDAPS port:
ldapsearch.bat `
 --hostname localhost `
 --port 1636 `
 --useSsl `
 --trustStorePath C:\path\to\opendj\config\
 --trustStoreType PKCS12 \keystore `
 --trustStorePassword:file C:\path\to\opendj\config\keystore.pin `
 --bindDN uid=monitor `
 --bindPassword password `
 --baseDN "cn=LDAPS,cn=connection handlers,cn=monitor" `
 "(objectclass=*)" `
 ds-mon-requests-modify
```

```shell
# Run modrate for 10 seconds against the first server:
modrate \
 --maxDuration 10 \
 --hostname localhost \
 --port 1636 \
 --useSsl \
 --trustStorePath /path/to/opendj/config/keystore \
 --trustStoreType PKCS12 \
 --trustStorePassword:file /path/to/opendj/config/keystore.pin \
 --bindDn uid=kvaughan,ou=People,dc=example,dc=com \
 --bindPassword bribery \
 --noRebind \
 --numConnections 4 \
 --numConcurrentRequests 4 \
 --targetDn "uid=user.{1},ou=people,dc=example,dc=com" \
 --argument "rand(0,100000)" \
 --argument "randstr(16)" \
 "description:{2}"

# Read number of modify requests on the LDAPS port:
ldapsearch \
 --hostname localhost \
 --port 1636 \
 --useSsl \
 --trustStorePath /path/to/opendj/config/keystore \
 --trustStoreType PKCS12 \
 --trustStorePassword:file /path/to/opendj/config/keystore.pin \
 --bindDN uid=monitor \
 --bindPassword password \
 --baseDN "cn=LDAPS,cn=connection handlers,cn=monitor" \
 "(&)" \
 ds-mon-requests-modify
```

When reading the `modrate` command output, notice that it shows statistics for throughput (operations/second), response times (milliseconds), and errors/second. If you expect all operations to succeed and yet `err/sec` is not 0.0, the command options are no doubt incorrectly set. For an explanation of the command output, refer to [modrate](../tools-reference/modrate.html).

Notice that the monitoring attributes hold similar, alternative statistics.

## Measure search rates

Your directory service exists to hold identity data and to make it easy and quick to find. Almost all directory client applications search the directory. Some applications, such as those providing naming services or those in a call path, require very low latency.

To get a sense of the throughput and response times you can expect from your directory even before you tune performance, measure the LDAP search rate with the `searchrate` command:

* Bash

* PowerShell

* Zsh

```shell
# Run searchrate for 10 seconds against the first server:
searchrate \
 --maxDuration 10 \
 --hostname localhost \
 --port 1636 \
 --useSsl \
 --trustStorePath /path/to/opendj/config/keystore \
 --trustStoreType PKCS12 \
 --trustStorePassword:file /path/to/opendj/config/keystore.pin \
 --bindDn uid=bjensen,ou=People,dc=example,dc=com \
 --bindPassword hifalutin \
 --noRebind \
 --numConnections 4 \
 --numConcurrentRequests 4 \
 --baseDn "dc=example,dc=com" \
 --argument "rand(0,100000)" \
 "(uid=user.{})"

# Read number of subtree search requests on the LDAPS port:
ldapsearch \
 --hostname localhost \
 --port 1636 \
 --useSsl \
 --trustStorePath /path/to/opendj/config/keystore \
 --trustStoreType PKCS12 \
 --trustStorePassword:file /path/to/opendj/config/keystore.pin \
 --bindDN uid=monitor \
 --bindPassword password \
 --baseDN "cn=LDAPS,cn=connection handlers,cn=monitor" \
 "(&)" \
 ds-mon-requests-search-sub
```

```powershell
# Run searchrate for 10 seconds against the first server:
searchrate.bat `
 --maxDuration 10 `
 --hostname localhost `
 --port 1636 `
 --useSsl `
 --trustStorePath C:\path\to\opendj\config\
 --trustStoreType PKCS12 \keystore `
 --trustStorePassword:file C:\path\to\opendj\config\keystore.pin `
 --bindDn uid=bjensen,ou=People,dc=example,dc=com `
 --bindPassword password `
 --noRebind `
 --numConnections 4 `
 --numConcurrentRequests 4 `
 --baseDn "dc=example,dc=com" `
 --argument "rand(0,100000)" `
 "(uid=user.{})"

# Read number of subtree search requests on the LDAPS port:
ldapsearch.bat `
 --hostname localhost `
 --port 1636 `
 --useSsl `
 --trustStorePath C:\path\to\opendj\config\
 --trustStoreType PKCS12 \keystore `
 --trustStorePassword:file C:\path\to\opendj\config\keystore.pin `
 --bindDN uid=monitor `
 --bindPassword password `
 --baseDN "cn=LDAPS,cn=connection handlers,cn=monitor" `
 "(objectclass=*)" `
 ds-mon-requests-search-sub
```

```shell
# Run searchrate for 10 seconds against the first server:
searchrate \
 --maxDuration 10 \
 --hostname localhost \
 --port 1636 \
 --useSsl \
 --trustStorePath /path/to/opendj/config/keystore \
 --trustStoreType PKCS12 \
 --trustStorePassword:file /path/to/opendj/config/keystore.pin \
 --bindDn uid=bjensen,ou=People,dc=example,dc=com \
 --bindPassword hifalutin \
 --noRebind \
 --numConnections 4 \
 --numConcurrentRequests 4 \
 --baseDn "dc=example,dc=com" \
 --argument "rand(0,100000)" \
 "(uid=user.{})"

# Read number of subtree search requests on the LDAPS port:
ldapsearch \
 --hostname localhost \
 --port 1636 \
 --useSsl \
 --trustStorePath /path/to/opendj/config/keystore \
 --trustStoreType PKCS12 \
 --trustStorePassword:file /path/to/opendj/config/keystore.pin \
 --bindDN uid=monitor \
 --bindPassword password \
 --baseDN "cn=LDAPS,cn=connection handlers,cn=monitor" \
 "(&)" \
 ds-mon-requests-search-sub
```

Notice that `searchrate` command output resembles that of the `modrate` command. The `searchrate` output also indicates how many entries each search returned. For an explanation of the command output, refer to [searchrate](../tools-reference/searchrate.html).

## Check replication

When you measured directory performance, the `modrate` command made many changes to user's entries. Replication between your two DS replicas should replay each change so client applications get the same response regardless of which replica they use to read a user's entry.

Check the data on both replicas is synchronized. The following example uses monitoring metrics to check replication delay is zero on each replica:

* Bash

* PowerShell

* Zsh

```console
$ ldapsearch \
 --hostname localhost \
 --port 1636 \
 --useSsl \
 --trustStorePath /path/to/opendj/config/keystore \
 --trustStoreType PKCS12 \
 --trustStorePassword:file /path/to/opendj/config/keystore.pin \
 --bindDN uid=monitor \
 --bindPassword password \
 --baseDN cn=monitor \
 "(ds-mon-current-delay=*)" \
 ds-mon-current-delay
```

> **Collapse: Show output**
>
> ```
> dn: ds-mon-domain-name=cn=schema,cn=replicas,cn=replication,cn=monitor
> ds-mon-current-delay: 0
>
> dn: ds-mon-server-id=second-ds,cn=remote replicas,ds-mon-domain-name=cn=schema,cn=replicas,cn=replication,cn=monitor
> ds-mon-current-delay: 0
>
> dn: ds-mon-domain-name=dc=example\,dc=com,cn=replicas,cn=replication,cn=monitor
> ds-mon-current-delay: 0
>
> dn: ds-mon-server-id=second-ds,cn=remote replicas,ds-mon-domain-name=dc=example\,dc=com,cn=replicas,cn=replication,cn=monitor
> ds-mon-current-delay: 0
>
> dn: ds-mon-domain-name=uid=monitor,cn=replicas,cn=replication,cn=monitor
> ds-mon-current-delay: 0
>
> dn: ds-mon-server-id=second-ds,cn=remote replicas,ds-mon-domain-name=uid=monitor,cn=replicas,cn=replication,cn=monitor
> ds-mon-current-delay: 0
> ```

```powershell
ldapsearch.bat `
 --hostname localhost `
 --port 1636 `
 --useSsl `
 --trustStorePath C:\path\to\opendj\config\
 --trustStoreType PKCS12 \keystore `
 --trustStorePassword:file C:\path\to\opendj\config\keystore.pin `
 --bindDN uid=monitor `
 --bindPassword password `
 --baseDN cn=monitor `
 "(ds-mon-current-delay=*)" `
 ds-mon-current-delay
```

> **Collapse: Show output**
>
> ```
> dn: ds-mon-domain-name=cn=schema,cn=replicas,cn=replication,cn=monitor
> ds-mon-current-delay: 0
>
> dn: ds-mon-server-id=second-ds,cn=remote replicas,ds-mon-domain-name=cn=schema,cn=replicas,cn=replication,cn=monitor
> ds-mon-current-delay: 0
>
> dn: ds-mon-domain-name=dc=example\,dc=com,cn=replicas,cn=replication,cn=monitor
> ds-mon-current-delay: 0
>
> dn: ds-mon-server-id=second-ds,cn=remote replicas,ds-mon-domain-name=dc=example\,dc=com,cn=replicas,cn=replication,cn=monitor
> ds-mon-current-delay: 0
>
> dn: ds-mon-domain-name=uid=monitor,cn=replicas,cn=replication,cn=monitor
> ds-mon-current-delay: 0
>
> dn: ds-mon-server-id=second-ds,cn=remote replicas,ds-mon-domain-name=uid=monitor,cn=replicas,cn=replication,cn=monitor
> ds-mon-current-delay: 0
> ```

```console
$ ldapsearch \
 --hostname localhost \
 --port 1636 \
 --useSsl \
 --trustStorePath /path/to/opendj/config/keystore \
 --trustStoreType PKCS12 \
 --trustStorePassword:file /path/to/opendj/config/keystore.pin \
 --bindDN uid=monitor \
 --bindPassword password \
 --baseDN cn=monitor \
 "(ds-mon-current-delay=*)" \
 ds-mon-current-delay
```

> **Collapse: Show output**
>
> ```
> dn: ds-mon-domain-name=cn=schema,cn=replicas,cn=replication,cn=monitor
> ds-mon-current-delay: 0
>
> dn: ds-mon-server-id=second-ds,cn=remote replicas,ds-mon-domain-name=cn=schema,cn=replicas,cn=replication,cn=monitor
> ds-mon-current-delay: 0
>
> dn: ds-mon-domain-name=dc=example\,dc=com,cn=replicas,cn=replication,cn=monitor
> ds-mon-current-delay: 0
>
> dn: ds-mon-server-id=second-ds,cn=remote replicas,ds-mon-domain-name=dc=example\,dc=com,cn=replicas,cn=replication,cn=monitor
> ds-mon-current-delay: 0
>
> dn: ds-mon-domain-name=uid=monitor,cn=replicas,cn=replication,cn=monitor
> ds-mon-current-delay: 0
>
> dn: ds-mon-server-id=second-ds,cn=remote replicas,ds-mon-domain-name=uid=monitor,cn=replicas,cn=replication,cn=monitor
> ds-mon-current-delay: 0
> ```

---

---
title: Next steps
description: "Next steps after the getting-started examples: explore PingDS documentation, use the LDAP SDK, try third-party tools, and integrate with PingAM or PingIDM."
component: pingds
version: 8.1
page_id: pingds:getting-started:further
canonical_url: https://docs.pingidentity.com/pingds/8.1/getting-started/further.html
llms_txt: https://docs.pingidentity.com/pingds/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-01-27T13:21:24Z
keywords: ["Evaluation", "LDAP"]
section_ids:
  further-replication: Learn about replication
  further-ds-docs: Browse DS documentation
  further-sdk: Use the LDAP SDK
  further-tools: Try third-party tools
  further-am: Use DS with AM
  further-idm: Use DS with IDM
  further-uninstall: Remove DS software
---

# Next steps

After you work through the examples in these pages, try the following suggestions:

## Learn about replication

Data replication is sometimes called the "killer feature" of LDAP directories. Its strengths are in enabling very high availability for directory services even during network outages, and automatically resolving conflicts that can occur when the network is down, for example. LDAP directories have been improving and hardening replication features for decades.

Its weaknesses are that replication protocols have not been standardized for interoperability, and that unwary developers can misunderstand its property of eventual consistency if they are too used to the strong, immediate consistency of monolithic, transactional databases.

Replication necessarily involves multiple servers and additional configuration. You can learn more about it by reading [Replication](../config-guide/replication.html) and the related pages.

## Browse DS documentation

| Category                                                                         | Topics Covered                                                                               |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| *[Release notes](https://docs.pingidentity.com/pingds/release-notes/index.html)* | DS features, fixes, and known issues                                                         |
| *[Use cases](../use-cases/preface.html)*                                         | Implementing common use cases for directory services                                         |
| *[Deployment](../deployment-guide/preface.html)*                                 | Deploying PingDS in on-premises and cloud environments                                       |
| *[Installation](../install-guide/preface.html)*                                  | Installing DS software                                                                       |
| *[Upgrade](../upgrade-guide/preface.html)*                                       | Upgrading DS software                                                                        |
| *[Configuration](../config-guide/preface.html)*                                  | Configuring DS servers after installation                                                    |
| *[Security](../security-guide/preface.html)*                                     | Ensuring a PingDS deployment is secure                                                       |
| *[Maintenance](../maintenance-guide/preface.html)*                               | Day-to-day operations for maintaining DS servers                                             |
| *[Logging](../logging-guide/preface.html)*                                       | Configuring DS server logs                                                                   |
| *[Monitoring](../monitoring-guide/preface.html)*                                 | What to monitor when running DS servers, and where to look for metrics and other information |
| *[Use LDAP](../ldap-guide/preface.html)*                                         | How to use LDAP features and command-line tools                                              |
| *[Use HDAP](../rest-guide/preface.html)*                                         | How to configure and use DS REST APIs for HTTP access (HDAP)                                 |
| *[Configuration reference](../configref/preface.html)*                           | The `dsconfig` subcommands and server configuration properties                               |
| *[DS Javadoc](../_attachments/javadoc/index.html)*                               | Evolving LDAP SDK and server APIs, including common APIs                                     |
| *[LDAP reference](../ldap-reference/preface.html)*                               | LDAP-specific features of DS software                                                        |
| *[LDAP schema reference](../schemaref/preface.html)*                             | All default LDAP schema, including monitoring attributes and object classes                  |
| *[Log reference](../log-reference/index.html)*                                   | DS server error log messages by category and ID                                              |
| *[Tools reference](../tools-reference/preface.html)*                             | Tools bundled with DS software                                                               |

## Use the LDAP SDK

The [UnboundID LDAP SDK for Java](https://github.com/pingidentity/ldapsdk) is a fast, powerful, user-friendly, and completely free and open source Java library for communicating with LDAP directory servers. It offers better performance, better ease of use, and more features than other Java-based LDAP APIs. It is developed by Ping Identity Corporation and is actively being maintained and enhanced as a critical component of Ping Identity client and server software.

## Try third-party tools

LDAP is a standard protocol, and so you can use LDAP-compliant third-party tools to manage directory data:

* [Admin4](http://www.admin4.org/)

* [Apache Directory Studio](https://directory.apache.org/studio/)

* [JXplorer and JXWorkBench](https://jxplorer.org/)

* [phpLDAPadmin](https://github.com/leenooks/phpLDAPadmin/wiki)

* [Softerra LDAP Administrator](https://www.ldapadministrator.com/)

* [web2ldap](https://pypi.org/project/web2ldap/)

Many software solutions include support for LDAP authentication *(tooltip: \<div class="paragraph">
\<p>The act of confirming the identity of a principal.\</p>
\</div>)* and LDAP-based address books.

*Ping Identity does not endorse or support third-party tools.*

## Use DS with AM

* [Backend directory servers](https://docs.pingidentity.com/pingam/8.1/deployment-planning/deploy-topologies-onprem.html#backend-ds) in the AM *Deployment planning* documentation

* [Prepare external stores](https://docs.pingidentity.com/pingam/8.1/installation/prepare-ext-stores.html) in the AM *Installation* documentation

* [Configure CTS token stores](https://docs.pingidentity.com/pingam/8.1/cts/cts-openam-config.html) in the AM *Core token service* documentation.

* You can install DS directory servers for use as external AM stores.

  For details, refer to [Setup profiles](../install-guide/setup-profiles.html).

## Use DS with IDM

* [External DS repository](https://docs.pingidentity.com/pingidm/8.1/install-guide/external-ds.html) and [Select a repository](https://docs.pingidentity.com/pingidm/8.1/install-guide/chap-repository.html) in the IDM *Installation* documentation

  Also refer to [Install DS as an IDM repository](../install-guide/profile-idm-repo.html).

* [One-way synchronization from LDAP to IDM](https://docs.pingidentity.com/pingidm/8.1/samples-guide/sync-with-ldap.html), [Two-way synchronization between LDAP and IDM](https://docs.pingidentity.com/pingidm/8.1/samples-guide/sync-with-ldap-bidirectional.html), and other LDAP-related pages in the IDM *Samples* documentation

* [DS repository configuration](https://docs.pingidentity.com/pingidm/8.1/objects-guide/repo-config.html#repo-ds-json) and [Mappings with a DS repository](https://docs.pingidentity.com/pingidm/8.1/objects-guide/explicit-generic-mapping-ds.html) in the IDM *Object modeling* documentation

* [Synchronize passwords with DS](https://docs.pingidentity.com/pingidm/8.1/pwd-plugin-guide/chap-sync-dj.html) in the IDM *Password synchronization* documentation

## Remove DS software

For details, refer to [Uninstallation](../install-guide/uninstall.html).

---

---
title: Start here
description: "Hands-on introduction to PingDS: install a server, learn LDAP and HTTP access, set up replication, measure performance, and explore access control."
component: pingds
version: 8.1
page_id: pingds:getting-started:preface
canonical_url: https://docs.pingidentity.com/pingds/8.1/getting-started/preface.html
llms_txt: https://docs.pingidentity.com/pingds/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2025-10-22T14:42:39Z
keywords: ["Evaluation", "LDAP"]
page_aliases: ["index.adoc"]
---

# Start here

Use these pages to get a quick, hands-on look at what PingDS software can do. You will download, install, and use DS on your local computer.

Estimated time to complete: 30-45 minutes *(tooltip: This assumes familiarity with command-line tools.)*

[icon: wrench, set=fas, size=3x]

#### [Install DS](install.html)

Install DS software.

[icon: sitemap, set=fas, size=3x]

#### [Learn LDAP](ldap.html)

Use DS LDAP tools.

[icon: cubes, set=fas, size=3x]

#### [Learn REST/HTTP](rest.html)

Access DS over HTTP.

[icon: clone, set=fas, size=3x]

#### [Learn replication](replication.html)

Replicate DS data.

[icon: rocket, set=fas, size=3x]

#### [Measure performance](performance.html)

Measure LDAP operations.

[icon: lock, set=fas, size=3x]

#### [Learn access control](acis.html)

Learn DS ACIs *(tooltip: \<div class="paragraph">
\<p>An instruction or rule that can be used to grant or deny access to users to perform operations on a server.\</p>
\</div>)*.