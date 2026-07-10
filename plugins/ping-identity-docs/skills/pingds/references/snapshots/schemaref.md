---
title: 1.3.6.1.4.1.26027.1.4.8.1.3.6.1.4.1.26027.1.3.6
description: OID
component: pingds
version: 8.1
page_id: pingds:schemaref:mr-1.3.6.1.4.1.26027.1.4.8.1.3.6.1.4.1.26027.1.3.6
canonical_url: https://docs.pingidentity.com/pingds/8.1/schemaref/mr-1.3.6.1.4.1.26027.1.4.8.1.3.6.1.4.1.26027.1.3.6.html
llms_txt: https://docs.pingidentity.com/pingds/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
---

# 1.3.6.1.4.1.26027.1.4.8.1.3.6.1.4.1.26027.1.3.6

|                    |                                                                 |
| ------------------ | --------------------------------------------------------------- |
| *OID*              | 1.3.6.1.4.1.26027.1.4.8.1.3.6.1.4.1.26027.1.3.6                 |
| *Description*      | Collective Conflict Behavior enumeration ordering matching rule |
| *Assertion syntax* | [CollectiveConflictBehavior](s-CollectiveConflictBehavior.html) |
| *Origin*           | OpenDJ X-ENUM Syntax                                            |

---

---
title: About This Reference
description: This reference describes the default directory schema. Each schema definition has its own section, with links to related sections. Reference pages for the most commonly used elements may include additional descriptions and examples that are not present in the directory schema definitions.
component: pingds
version: 8.1
page_id: pingds:schemaref:preface
canonical_url: https://docs.pingidentity.com/pingds/8.1/schemaref/preface.html
llms_txt: https://docs.pingidentity.com/pingds/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
page_aliases: ["index.adoc"]
---

# About This Reference

This reference describes the default directory schema. Each schema definition has its own section, with links to related sections. Reference pages for the most commonly used elements may include additional descriptions and examples that are not present in the directory schema definitions.

This reference does not include directory configuration attributes and object classes, collation matching rules.

LDAP directory schema defines how data can be stored in the directory. When a directory server receives a request to update directory data, it can check the data changes against the directory schema, refusing any request that would result in a violation of the directory schema and directory data corruption.

Schema checking prevents errors such as the following:

* Adding inappropriate attributes to an entry

* Removing required attributes from an entry

* Using an attribute value that has the wrong syntax

* Adding the wrong type of subordinate object

LDAP directory schema consists of definitions for the following:

* Attribute types

  Define attributes of directory entries, including their syntaxes and matching rules

* Directory Information Tree (DIT) content rules

  Define the content of entries with a given structural object class

* DIT structure rules

  Define the names entries may have, and how entries may be related to each other

* Matching rules

  Define how values of attributes are matched and compared

* Matching rule uses

  List attributes that can be used with an extensibleMatch search filter

* Name forms

  Define naming relations for structural object classes

* Object classes

  Define the types of objects that an entry represents, and the required and optional attributes for entries of those types

* Syntaxes

  Define the encodings used in LDAP

For a technical description of LDAP directory schema, read *Directory Schema* in [*Lightweight Directory Access Protocol (LDAP): Directory Information Models*](https://www.rfc-editor.org/rfc/rfc4512.html#section-4) (RFC 4512).

LDAP directory servers allow client applications to access directory schema while the server is running. This enables applications to validate their changes against the schema before sending an update request to the server. As a result, LDAP schema definitions are optimized for applications, not humans. The reader must resolve relationships between schema definitions, and must find most documentation elsewhere.

---

---
title: account
description: Entries of this object class represent computer accounts.
component: pingds
version: 8.1
page_id: pingds:schemaref:oc-account
canonical_url: https://docs.pingidentity.com/pingds/8.1/schemaref/oc-account.html
llms_txt: https://docs.pingidentity.com/pingds/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
---

# account

Entries of this object class represent computer accounts.

Use `uid` as the naming attribute.

|                       |                                                                                                                                        |
| --------------------- | -------------------------------------------------------------------------------------------------------------------------------------- |
| *OID*                 | 0.9.2342.19200300.100.4.5                                                                                                              |
| *Names*               | account                                                                                                                                |
| *Superior classes*    | [top](oc-top.html)                                                                                                                     |
| *Class type*          | STRUCTURAL: for structural specification of the DIT. Entries have only one structural object class superclass chain.                   |
| *Required attributes* | [objectClass](at-objectClass.html), [uid](at-uid.html)                                                                                 |
| *Optional attributes* | [description](at-description.html), [host](at-host.html), [l](at-l.html), [o](at-o.html), [ou](at-ou.html), [seeAlso](at-seeAlso.html) |
| *Origin*              | [RFC 4524](https://datatracker.ietf.org/doc/html/rfc4524)                                                                              |
| *Schema file*         | 00-core.ldif                                                                                                                           |

---

---
title: aci
description: Values are Access Control Instructions (ACI). See the directory documentation for details.
component: pingds
version: 8.1
page_id: pingds:schemaref:at-aci
canonical_url: https://docs.pingidentity.com/pingds/8.1/schemaref/at-aci.html
llms_txt: https://docs.pingidentity.com/pingds/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
---

# aci

Values are Access Control Instructions (ACI). See the directory documentation for details.

|                             |                                                                                   |
| --------------------------- | --------------------------------------------------------------------------------- |
| *OID*                       | 2.16.840.1.113730.3.1.55                                                          |
| *Names*                     | aci                                                                               |
| *Description*               | Sun-defined access control information attribute type                             |
| *Syntax*                    | [Sun-definedAccessControlInformation](s-Sun-definedAccessControlInformation.html) |
| *Equality matching rule*    | [octetStringMatch](mr-octetStringMatch.html)                                      |
| *Ordering matching rule*    | [octetStringOrderingMatch](mr-octetStringOrderingMatch.html)                      |
| *Single value*              | false: multiple values allowed                                                    |
| *User modification allowed* | true                                                                              |
| *Usage*                     | directoryOperation                                                                |
| *Origin*                    | Sun Java System Directory Server                                                  |
| *Schema file*               | 00-core.ldif                                                                      |

---

---
title: aclRights
description: Shows effective access rights. See the directory documentation for details.
component: pingds
version: 8.1
page_id: pingds:schemaref:at-aclRights
canonical_url: https://docs.pingidentity.com/pingds/8.1/schemaref/at-aclRights.html
llms_txt: https://docs.pingidentity.com/pingds/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
---

# aclRights

Shows effective access rights. See the directory documentation for details.

|                             |                                                                |
| --------------------------- | -------------------------------------------------------------- |
| *OID*                       | 1.3.6.1.4.1.42.2.27.9.1.39                                     |
| *Names*                     | aclRights                                                      |
| *Description*               | Sun-defined access control effective rights attribute type     |
| *Syntax*                    | [DirectoryString](s-DirectoryString.html)                      |
| *Equality matching rule*    | [caseIgnoreMatch](mr-caseIgnoreMatch.html)                     |
| *Ordering matching rule*    | [caseIgnoreOrderingMatch](mr-caseIgnoreOrderingMatch.html)     |
| *Substring matching rule*   | [caseIgnoreSubstringsMatch](mr-caseIgnoreSubstringsMatch.html) |
| *Single value*              | true                                                           |
| *User modification allowed* | false                                                          |
| *Usage*                     | directoryOperation                                             |
| *Origin*                    | Sun Java System Directory Server                               |
| *Schema file*               | 00-core.ldif                                                   |

---

---
title: aclRightsInfo
description: Shows how the server calculates effective access rights. See the directory documentation for details.
component: pingds
version: 8.1
page_id: pingds:schemaref:at-aclRightsInfo
canonical_url: https://docs.pingidentity.com/pingds/8.1/schemaref/at-aclRightsInfo.html
llms_txt: https://docs.pingidentity.com/pingds/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
---

# aclRightsInfo

Shows how the server calculates effective access rights. See the directory documentation for details.

|                             |                                                                        |
| --------------------------- | ---------------------------------------------------------------------- |
| *OID*                       | 1.3.6.1.4.1.42.2.27.9.1.40                                             |
| *Names*                     | aclRightsInfo                                                          |
| *Description*               | Sun-defined access control effective rights information attribute type |
| *Syntax*                    | [DirectoryString](s-DirectoryString.html)                              |
| *Equality matching rule*    | [caseIgnoreMatch](mr-caseIgnoreMatch.html)                             |
| *Ordering matching rule*    | [caseIgnoreOrderingMatch](mr-caseIgnoreOrderingMatch.html)             |
| *Substring matching rule*   | [caseIgnoreSubstringsMatch](mr-caseIgnoreSubstringsMatch.html)         |
| *Single value*              | true                                                                   |
| *User modification allowed* | false                                                                  |
| *Usage*                     | directoryOperation                                                     |
| *Origin*                    | Sun Java System Directory Server                                       |
| *Schema file*               | 00-core.ldif                                                           |

---

---
title: administratorsAddress
description: An address for contacting the administrator who manages the server. For example, mailto:helpdesk@example.com.
component: pingds
version: 8.1
page_id: pingds:schemaref:at-administratorsAddress
canonical_url: https://docs.pingidentity.com/pingds/8.1/schemaref/at-administratorsAddress.html
llms_txt: https://docs.pingidentity.com/pingds/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
---

# administratorsAddress

An address for contacting the administrator who manages the server. For example, `mailto:helpdesk@example.com`.

|                             |                                                                                              |
| --------------------------- | -------------------------------------------------------------------------------------------- |
| *OID*                       | 1.3.6.1.4.1.1466.101.120.1                                                                   |
| *Names*                     | administratorsAddress                                                                        |
| *Syntax*                    | [IA5String](s-IA5String.html)                                                                |
| *Equality matching rule*    | [caseIgnoreMatch](mr-caseIgnoreMatch.html)                                                   |
| *Ordering matching rule*    | [caseIgnoreOrderingMatch](mr-caseIgnoreOrderingMatch.html)                                   |
| *Substring matching rule*   | [caseIgnoreSubstringsMatch](mr-caseIgnoreSubstringsMatch.html)                               |
| *Single value*              | false: multiple values allowed                                                               |
| *User modification allowed* | true                                                                                         |
| *Usage*                     | directoryOperation                                                                           |
| *Origin*                    | [draft-wahl-ldap-adminaddr](https://datatracker.ietf.org/doc/html/draft-wahl-ldap-adminaddr) |
| *Schema file*               | 00-core.ldif                                                                                 |

---

---
title: alias
description: Entry pointing to another entry, using an aliasedObjectName attribute value.
component: pingds
version: 8.1
page_id: pingds:schemaref:oc-alias
canonical_url: https://docs.pingidentity.com/pingds/8.1/schemaref/oc-alias.html
llms_txt: https://docs.pingidentity.com/pingds/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
---

# alias

Entry pointing to another entry, using an `aliasedObjectName` attribute value.

An alias name is an alternative name for an entry. Alias objects are leaf entries (no subordinates).

ForgeRock servers do not support alias dereferencing.

|                       |                                                                                                                      |
| --------------------- | -------------------------------------------------------------------------------------------------------------------- |
| *OID*                 | 2.5.6.1                                                                                                              |
| *Names*               | alias                                                                                                                |
| *Superior classes*    | [top](oc-top.html)                                                                                                   |
| *Class type*          | STRUCTURAL: for structural specification of the DIT. Entries have only one structural object class superclass chain. |
| *Required attributes* | [aliasedObjectName](at-aliasedObjectName.html), [objectClass](at-objectClass.html)                                   |
| *Origin*              | [RFC 4512](https://datatracker.ietf.org/doc/html/rfc4512)                                                            |
| *Schema file*         | 00-core.ldif                                                                                                         |

---

---
title: aliasedObjectName
description: Holds the name of the entry that an alias points to.
component: pingds
version: 8.1
page_id: pingds:schemaref:at-aliasedObjectName
canonical_url: https://docs.pingidentity.com/pingds/8.1/schemaref/at-aliasedObjectName.html
llms_txt: https://docs.pingidentity.com/pingds/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
---

# aliasedObjectName

Holds the name of the entry that an alias points to.

An alias name is an alternative name for an entry. Alias objects are leaf entries (no subordinates).

ForgeRock servers do not support alias dereferencing.

|                             |                                                                |
| --------------------------- | -------------------------------------------------------------- |
| *OID*                       | 2.5.4.1                                                        |
| *Names*                     | aliasedObjectName                                              |
| *Syntax*                    | [DN](s-DN.html)                                                |
| *Equality matching rule*    | [distinguishedNameMatch](mr-distinguishedNameMatch.html)       |
| *Substring matching rule*   | [caseIgnoreSubstringsMatch](mr-caseIgnoreSubstringsMatch.html) |
| *Single value*              | true                                                           |
| *User modification allowed* | true                                                           |
| *Usage*                     | userApplications                                               |
| *Origin*                    | [RFC 4512](https://datatracker.ietf.org/doc/html/rfc4512)      |
| *Schema file*               | 00-core.ldif                                                   |
| *Used by*                   | [alias](oc-alias.html)                                         |

---

---
title: alive
description: OID
component: pingds
version: 8.1
page_id: pingds:schemaref:at-alive
canonical_url: https://docs.pingidentity.com/pingds/8.1/schemaref/at-alive.html
llms_txt: https://docs.pingidentity.com/pingds/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
---

# alive

|                             |                                       |
| --------------------------- | ------------------------------------- |
| *OID*                       | 1.3.6.1.4.1.36733.2.1.1.507           |
| *Names*                     | alive                                 |
| *Description*               | Indicates whether the server is alive |
| *Syntax*                    | [Boolean](s-Boolean.html)             |
| *Equality matching rule*    | [booleanMatch](mr-booleanMatch.html)  |
| *Single value*              | true                                  |
| *User modification allowed* | false                                 |
| *Usage*                     | dSAOperation                          |
| *Origin*                    | OpenDJ Directory Server               |
| *Schema file*               | 00-core.ldif                          |

---

---
title: altServer
description: This operational attribute lists URIs of alternate servers to contact when this server is not available.
component: pingds
version: 8.1
page_id: pingds:schemaref:at-altServer
canonical_url: https://docs.pingidentity.com/pingds/8.1/schemaref/at-altServer.html
llms_txt: https://docs.pingidentity.com/pingds/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
---

# altServer

This operational attribute lists URIs of alternate servers to contact when this server is not available.

|                             |                                                                |
| --------------------------- | -------------------------------------------------------------- |
| *OID*                       | 1.3.6.1.4.1.1466.101.120.6                                     |
| *Names*                     | altServer                                                      |
| *Syntax*                    | [IA5String](s-IA5String.html)                                  |
| *Equality matching rule*    | [caseIgnoreMatch](mr-caseIgnoreMatch.html)                     |
| *Ordering matching rule*    | [caseIgnoreOrderingMatch](mr-caseIgnoreOrderingMatch.html)     |
| *Substring matching rule*   | [caseIgnoreSubstringsMatch](mr-caseIgnoreSubstringsMatch.html) |
| *Single value*              | false: multiple values allowed                                 |
| *User modification allowed* | true                                                           |
| *Usage*                     | dSAOperation                                                   |
| *Origin*                    | [RFC 4512](https://datatracker.ietf.org/doc/html/rfc4512)      |
| *Schema file*               | 00-core.ldif                                                   |

---

---
title: applicationEntity
description: Represents an OSI application.
component: pingds
version: 8.1
page_id: pingds:schemaref:oc-applicationEntity
canonical_url: https://docs.pingidentity.com/pingds/8.1/schemaref/oc-applicationEntity.html
llms_txt: https://docs.pingidentity.com/pingds/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
---

# applicationEntity

Represents an OSI application.

|                       |                                                                                                                                                                                      |
| --------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| *OID*                 | 2.5.6.12                                                                                                                                                                             |
| *Names*               | applicationEntity                                                                                                                                                                    |
| *Superior classes*    | [top](oc-top.html)                                                                                                                                                                   |
| *Class type*          | STRUCTURAL: for structural specification of the DIT. Entries have only one structural object class superclass chain.                                                                 |
| *Required attributes* | [cn](at-cn.html), [objectClass](at-objectClass.html), [presentationAddress](at-presentationAddress.html)                                                                             |
| *Optional attributes* | [description](at-description.html), [l](at-l.html), [o](at-o.html), [ou](at-ou.html), [seeAlso](at-seeAlso.html), [supportedApplicationContext](at-supportedApplicationContext.html) |
| *Origin*              | [RFC 2256](https://datatracker.ietf.org/doc/html/rfc2256)                                                                                                                            |
| *Schema file*         | 00-core.ldif                                                                                                                                                                         |

---

---
title: applicationProcess
description: Represents an application executing in a computer system.
component: pingds
version: 8.1
page_id: pingds:schemaref:oc-applicationProcess
canonical_url: https://docs.pingidentity.com/pingds/8.1/schemaref/oc-applicationProcess.html
llms_txt: https://docs.pingidentity.com/pingds/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
---

# applicationProcess

Represents an application executing in a computer system.

|                       |                                                                                                                      |
| --------------------- | -------------------------------------------------------------------------------------------------------------------- |
| *OID*                 | 2.5.6.11                                                                                                             |
| *Names*               | applicationProcess                                                                                                   |
| *Superior classes*    | [top](oc-top.html)                                                                                                   |
| *Class type*          | STRUCTURAL: for structural specification of the DIT. Entries have only one structural object class superclass chain. |
| *Required attributes* | [cn](at-cn.html), [objectClass](at-objectClass.html)                                                                 |
| *Optional attributes* | [description](at-description.html), [l](at-l.html), [ou](at-ou.html), [seeAlso](at-seeAlso.html)                     |
| *Origin*              | [RFC 4519](https://datatracker.ietf.org/doc/html/rfc4519)                                                            |
| *Schema file*         | 00-core.ldif                                                                                                         |

---

---
title: aRecord
description: A type A (address) DNS resource record.
component: pingds
version: 8.1
page_id: pingds:schemaref:at-aRecord
canonical_url: https://docs.pingidentity.com/pingds/8.1/schemaref/at-aRecord.html
llms_txt: https://docs.pingidentity.com/pingds/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
---

# aRecord

A type A (address) DNS resource record.

|                             |                                                                |
| --------------------------- | -------------------------------------------------------------- |
| *OID*                       | 0.9.2342.19200300.100.1.26                                     |
| *Names*                     | aRecord                                                        |
| *Syntax*                    | [IA5String](s-IA5String.html)                                  |
| *Equality matching rule*    | [caseIgnoreMatch](mr-caseIgnoreMatch.html)                     |
| *Ordering matching rule*    | [caseIgnoreOrderingMatch](mr-caseIgnoreOrderingMatch.html)     |
| *Substring matching rule*   | [caseIgnoreSubstringsMatch](mr-caseIgnoreSubstringsMatch.html) |
| *Single value*              | false: multiple values allowed                                 |
| *User modification allowed* | true                                                           |
| *Usage*                     | userApplications                                               |
| *Origin*                    | [RFC 1274](https://datatracker.ietf.org/doc/html/rfc1274)      |
| *Schema file*               | 00-core.ldif                                                   |
| *Used by*                   | [dNSDomain](oc-dNSDomain.html)                                 |

---

---
title: assignedDashboard
description: OID
component: pingds
version: 8.1
page_id: pingds:schemaref:at-assignedDashboard
canonical_url: https://docs.pingidentity.com/pingds/8.1/schemaref/at-assignedDashboard.html
llms_txt: https://docs.pingidentity.com/pingds/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
---

# assignedDashboard

|                             |                                                                               |
| --------------------------- | ----------------------------------------------------------------------------- |
| *OID*                       | 1.3.6.1.4.1.36733.2.2.1.3.1                                                   |
| *Names*                     | assignedDashboard                                                             |
| *Description*               | Dashboard App registry                                                        |
| *Syntax*                    | [DirectoryString](s-DirectoryString.html)                                     |
| *Equality matching rule*    | [caseIgnoreMatch](mr-caseIgnoreMatch.html)                                    |
| *Ordering matching rule*    | [caseIgnoreOrderingMatch](mr-caseIgnoreOrderingMatch.html)                    |
| *Substring matching rule*   | [caseIgnoreSubstringsMatch](mr-caseIgnoreSubstringsMatch.html)                |
| *Single value*              | false: multiple values allowed                                                |
| *User modification allowed* | true                                                                          |
| *Usage*                     | userApplications                                                              |
| *Interface stability*       | Internal use only. Do not remove or modify. Subject to change without notice. |
| *Origin*                    | OpenAM                                                                        |
| *Schema file*               | 60-identity-store-ds-dashboard.ldif                                           |
| *Used by*                   | [forgerock-am-dashboard-service](oc-forgerock-am-dashboard-service.html)      |

---

---
title: associatedDomain
description: An attribute for specifying DNS hostnames associated with an object. For example, the entry with DN dc=example,dc=com could have an associated domain of example.com.
component: pingds
version: 8.1
page_id: pingds:schemaref:at-associatedDomain
canonical_url: https://docs.pingidentity.com/pingds/8.1/schemaref/at-associatedDomain.html
llms_txt: https://docs.pingidentity.com/pingds/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
---

# associatedDomain

An attribute for specifying DNS hostnames associated with an object. For example, the entry with DN `dc=example,dc=com` could have an associated domain of `example.com`.

Values of this attribute conform to the following ABNF:

```
domain = root / label *( DOT label )
root   = SPACE
label  = LETDIG [ *61( LETDIG / HYPHEN ) LETDIG ]
LETDIG = %x30-39 / %x41-5A / %x61-7A ; "0" - "9" / "A"-"Z" / "a"-"z"
SPACE  = %x20                        ; space (" ")
HYPHEN = %x2D                        ; hyphen ("-")
DOT    = %x2E                        ; period (".")
```

|                             |                                                                      |
| --------------------------- | -------------------------------------------------------------------- |
| *OID*                       | 0.9.2342.19200300.100.1.37                                           |
| *Names*                     | associatedDomain                                                     |
| *Syntax*                    | [IA5String](s-IA5String.html)                                        |
| *Equality matching rule*    | [caseIgnoreIA5Match](mr-caseIgnoreIA5Match.html)                     |
| *Ordering matching rule*    | [caseIgnoreOrderingMatch](mr-caseIgnoreOrderingMatch.html)           |
| *Substring matching rule*   | [caseIgnoreIA5SubstringsMatch](mr-caseIgnoreIA5SubstringsMatch.html) |
| *Single value*              | false: multiple values allowed                                       |
| *User modification allowed* | true                                                                 |
| *Usage*                     | userApplications                                                     |
| *Origin*                    | [RFC 4524](https://datatracker.ietf.org/doc/html/rfc4524)            |
| *Schema file*               | 00-core.ldif                                                         |
| *Used by*                   | [domainRelatedObject](oc-domainRelatedObject.html)                   |

---

---
title: associatedName
description: DNs of entries associated with a DNS domain.
component: pingds
version: 8.1
page_id: pingds:schemaref:at-associatedName
canonical_url: https://docs.pingidentity.com/pingds/8.1/schemaref/at-associatedName.html
llms_txt: https://docs.pingidentity.com/pingds/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
---

# associatedName

DNs of entries associated with a DNS domain.

|                             |                                                                                                      |
| --------------------------- | ---------------------------------------------------------------------------------------------------- |
| *OID*                       | 0.9.2342.19200300.100.1.38                                                                           |
| *Names*                     | associatedName                                                                                       |
| *Syntax*                    | [DN](s-DN.html)                                                                                      |
| *Equality matching rule*    | [distinguishedNameMatch](mr-distinguishedNameMatch.html)                                             |
| *Substring matching rule*   | [caseIgnoreSubstringsMatch](mr-caseIgnoreSubstringsMatch.html)                                       |
| *Single value*              | false: multiple values allowed                                                                       |
| *User modification allowed* | true                                                                                                 |
| *Usage*                     | userApplications                                                                                     |
| *Origin*                    | [RFC 4524](https://datatracker.ietf.org/doc/html/rfc4524)                                            |
| *Schema file*               | 00-core.ldif                                                                                         |
| *Used by*                   | [dNSDomain](oc-dNSDomain.html), [domain](oc-domain.html), [rFC822LocalPart](oc-rFC822LocalPart.html) |

---

---
title: Attribute Type Description
description: Values of this syntax define attribute types.
component: pingds
version: 8.1
page_id: pingds:schemaref:s-AttributeTypeDescription
canonical_url: https://docs.pingidentity.com/pingds/8.1/schemaref/s-AttributeTypeDescription.html
llms_txt: https://docs.pingidentity.com/pingds/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
---

# Attribute Type Description

Values of this syntax define attribute types.

The syntax corresponds to the `AttributeTypeDescription` ASN.1 type defined by X.501.

|               |                                                           |
| ------------- | --------------------------------------------------------- |
| *OID*         | 1.3.6.1.4.1.1466.115.121.1.3                              |
| *Description* | Attribute Type Description                                |
| *Origin*      | [RFC 4517](https://datatracker.ietf.org/doc/html/rfc4517) |

---

---
title: Attribute types
description: This part covers schema definitions for attribute types:
component: pingds
version: 8.1
page_id: pingds:schemaref:attribute-types
canonical_url: https://docs.pingidentity.com/pingds/8.1/schemaref/attribute-types.html
llms_txt: https://docs.pingidentity.com/pingds/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
---

# Attribute types

This part covers schema definitions for attribute types:

* [aci](at-aci.html)

* [aclRights](at-aclRights.html)

* [aclRightsInfo](at-aclRightsInfo.html)

* [administratorsAddress](at-administratorsAddress.html)

* [aliasedObjectName](at-aliasedObjectName.html)

* [alive](at-alive.html)

* [altServer](at-altServer.html)

* [aRecord](at-aRecord.html)

* [assignedDashboard](at-assignedDashboard.html)

* [associatedDomain](at-associatedDomain.html)

* [associatedName](at-associatedName.html)

* [attributeMap](at-attributeMap.html)

* [attributeTypes](at-attributeTypes.html)

* [audio](at-audio.html)

* [authenticationMethod](at-authenticationMethod.html)

* [authorityRevocationList](at-authorityRevocationList.html)

* [authPassword](at-authPassword.html)

* [automountInformation](at-automountInformation.html)

* [automountKey](at-automountKey.html)

* [automountMapName](at-automountMapName.html)

* [bindTimeLimit](at-bindTimeLimit.html)

* [blockInheritance](at-blockInheritance.html)

* [bootFile](at-bootFile.html)

* [bootParameter](at-bootParameter.html)

* [boundDevices](at-boundDevices.html)

* [buildingName](at-buildingName.html)

* [businessCategory](at-businessCategory.html)

* [c-FacsimileTelephoneNumber](at-c-FacsimileTelephoneNumber.html)

* [c-InternationalISDNNumber](at-c-InternationalISDNNumber.html)

* [c-l](at-c-l.html)

* [c-o](at-c-o.html)

* [c-ou](at-c-ou.html)

* [c-PhysicalDeliveryOfficeName](at-c-PhysicalDeliveryOfficeName.html)

* [c-PostalAddress](at-c-PostalAddress.html)

* [c-PostalCode](at-c-PostalCode.html)

* [c-PostOfficeBox](at-c-PostOfficeBox.html)

* [c-st](at-c-st.html)

* [c-street](at-c-street.html)

* [c-TelephoneNumber](at-c-TelephoneNumber.html)

* [c-TelexNumber](at-c-TelexNumber.html)

* [c](at-c.html)

* [cACertificate](at-cACertificate.html)

* [calCalAdrURI](at-calCalAdrURI.html)

* [calCalURI](at-calCalURI.html)

* [calCAPURI](at-calCAPURI.html)

* [calFBURL](at-calFBURL.html)

* [calOtherCalAdrURIs](at-calOtherCalAdrURIs.html)

* [calOtherCalURIs](at-calOtherCalURIs.html)

* [calOtherCAPURIs](at-calOtherCAPURIs.html)

* [calOtherFBURLs](at-calOtherFBURLs.html)

* [carLicense](at-carLicense.html)

* [certificateRevocationList](at-certificateRevocationList.html)

* [changeInitiatorsName](at-changeInitiatorsName.html)

* [changelog](at-changelog.html)

* [changeLogCookie](at-changeLogCookie.html)

* [changeNumber](at-changeNumber.html)

* [changes](at-changes.html)

* [changeTime](at-changeTime.html)

* [changeType](at-changeType.html)

* [cn](at-cn.html)

* [cNAMERecord](at-cNAMERecord.html)

* [co](at-co.html)

* [collectiveAttributeSubentries](at-collectiveAttributeSubentries.html)

* [collectiveConflictBehavior](at-collectiveConflictBehavior.html)

* [collectiveExclusions](at-collectiveExclusions.html)

* [corbaIor](at-corbaIor.html)

* [corbaRepositoryId](at-corbaRepositoryId.html)

* [coreTokenDate01](at-coreTokenDate01.html)

* [coreTokenDate02](at-coreTokenDate02.html)

* [coreTokenDate03](at-coreTokenDate03.html)

* [coreTokenDate04](at-coreTokenDate04.html)

* [coreTokenDate05](at-coreTokenDate05.html)

* [coreTokenExpirationDate](at-coreTokenExpirationDate.html)

* [coreTokenId](at-coreTokenId.html)

* [coreTokenInteger01](at-coreTokenInteger01.html)

* [coreTokenInteger02](at-coreTokenInteger02.html)

* [coreTokenInteger03](at-coreTokenInteger03.html)

* [coreTokenInteger04](at-coreTokenInteger04.html)

* [coreTokenInteger05](at-coreTokenInteger05.html)

* [coreTokenInteger06](at-coreTokenInteger06.html)

* [coreTokenInteger07](at-coreTokenInteger07.html)

* [coreTokenInteger08](at-coreTokenInteger08.html)

* [coreTokenInteger09](at-coreTokenInteger09.html)

* [coreTokenInteger10](at-coreTokenInteger10.html)

* [coreTokenMultiString01](at-coreTokenMultiString01.html)

* [coreTokenMultiString02](at-coreTokenMultiString02.html)

* [coreTokenMultiString03](at-coreTokenMultiString03.html)

* [coreTokenObject](at-coreTokenObject.html)

* [coreTokenString01](at-coreTokenString01.html)

* [coreTokenString02](at-coreTokenString02.html)

* [coreTokenString03](at-coreTokenString03.html)

* [coreTokenString04](at-coreTokenString04.html)

* [coreTokenString05](at-coreTokenString05.html)

* [coreTokenString06](at-coreTokenString06.html)

* [coreTokenString07](at-coreTokenString07.html)

* [coreTokenString08](at-coreTokenString08.html)

* [coreTokenString09](at-coreTokenString09.html)

* [coreTokenString10](at-coreTokenString10.html)

* [coreTokenString11](at-coreTokenString11.html)

* [coreTokenString12](at-coreTokenString12.html)

* [coreTokenString13](at-coreTokenString13.html)

* [coreTokenString14](at-coreTokenString14.html)

* [coreTokenString15](at-coreTokenString15.html)

* [coreTokenTtlDate](at-coreTokenTtlDate.html)

* [coreTokenType](at-coreTokenType.html)

* [coreTokenUserId](at-coreTokenUserId.html)

* [createTimestamp](at-createTimestamp.html)

* [creatorsName](at-creatorsName.html)

* [credentialLevel](at-credentialLevel.html)

* [crossCertificatePair](at-crossCertificatePair.html)

* [dc](at-dc.html)

* [debugsearchindex](at-debugsearchindex.html)

* [defaultSearchBase](at-defaultSearchBase.html)

* [defaultSearchScope](at-defaultSearchScope.html)

* [defaultServerList](at-defaultServerList.html)

* [deleteOldRDN](at-deleteOldRDN.html)

* [deltaRevocationList](at-deltaRevocationList.html)

* [departmentNumber](at-departmentNumber.html)

* [dereferenceAliases](at-dereferenceAliases.html)

* [description](at-description.html)

* [destinationIndicator](at-destinationIndicator.html)

* [devicePrintProfiles](at-devicePrintProfiles.html)

* [deviceProfiles](at-deviceProfiles.html)

* [displayName](at-displayName.html)

* [distinguishedName](at-distinguishedName.html)

* [dITContentRules](at-dITContentRules.html)

* [dITRedirect](at-dITRedirect.html)

* [dITStructureRules](at-dITStructureRules.html)

* [dmdName](at-dmdName.html)

* [dnQualifier](at-dnQualifier.html)

* [documentAuthor](at-documentAuthor.html)

* [documentIdentifier](at-documentIdentifier.html)

* [documentLocation](at-documentLocation.html)

* [documentPublisher](at-documentPublisher.html)

* [documentTitle](at-documentTitle.html)

* [documentVersion](at-documentVersion.html)

* [drink](at-drink.html)

* [ds-certificate-fingerprint](at-ds-certificate-fingerprint.html)

* [ds-certificate-issuer-dn](at-ds-certificate-issuer-dn.html)

* [ds-certificate-subject-dn](at-ds-certificate-subject-dn.html)

* [ds-last-login-time](at-ds-last-login-time.html)

* [ds-mon-abandoned-requests](at-ds-mon-abandoned-requests.html)

* [ds-mon-active-connections-count](at-ds-mon-active-connections-count.html)

* [ds-mon-active-persistent-searches](at-ds-mon-active-persistent-searches.html)

* [ds-mon-admin-connector-connections](at-ds-mon-admin-connector-connections.html)

* [ds-mon-admin-hostport](at-ds-mon-admin-hostport.html)

* [ds-mon-alias](at-ds-mon-alias.html)

* [ds-mon-alive-errors](at-ds-mon-alive-errors.html)

* [ds-mon-alive](at-ds-mon-alive.html)

* [ds-mon-backend-degraded-index-count](at-ds-mon-backend-degraded-index-count.html)

* [ds-mon-backend-degraded-index](at-ds-mon-backend-degraded-index.html)

* [ds-mon-backend-entry-count](at-ds-mon-backend-entry-count.html)

* [ds-mon-backend-entry-size-read](at-ds-mon-backend-entry-size-read.html)

* [ds-mon-backend-entry-size-written](at-ds-mon-backend-entry-size-written.html)

* [ds-mon-backend-filter-indexed](at-ds-mon-backend-filter-indexed.html)

* [ds-mon-backend-filter-unindexed](at-ds-mon-backend-filter-unindexed.html)

* [ds-mon-backend-filter-use-start-time](at-ds-mon-backend-filter-use-start-time.html)

* [ds-mon-backend-filter-use](at-ds-mon-backend-filter-use.html)

* [ds-mon-backend-is-private](at-ds-mon-backend-is-private.html)

* [ds-mon-backend-proxy-base-dn](at-ds-mon-backend-proxy-base-dn.html)

* [ds-mon-backend-proxy-shard](at-ds-mon-backend-proxy-shard.html)

* [ds-mon-backend-ttl-entries-deleted](at-ds-mon-backend-ttl-entries-deleted.html)

* [ds-mon-backend-ttl-is-running](at-ds-mon-backend-ttl-is-running.html)

* [ds-mon-backend-ttl-last-run-time](at-ds-mon-backend-ttl-last-run-time.html)

* [ds-mon-backend-ttl-queue-size](at-ds-mon-backend-ttl-queue-size.html)

* [ds-mon-backend-ttl-thread-count](at-ds-mon-backend-ttl-thread-count.html)

* [ds-mon-backend-untrusted-index-count](at-ds-mon-backend-untrusted-index-count.html)

* [ds-mon-backend-untrusted-index](at-ds-mon-backend-untrusted-index.html)

* [ds-mon-backend-writability-mode](at-ds-mon-backend-writability-mode.html)

* [ds-mon-base-dn-entry-count](at-ds-mon-base-dn-entry-count.html)

* [ds-mon-base-dn](at-ds-mon-base-dn.html)

* [ds-mon-build-number](at-ds-mon-build-number.html)

* [ds-mon-build-time](at-ds-mon-build-time.html)

* [ds-mon-bytes-read](at-ds-mon-bytes-read.html)

* [ds-mon-bytes-written](at-ds-mon-bytes-written.html)

* [ds-mon-cache-entry-count](at-ds-mon-cache-entry-count.html)

* [ds-mon-cache-max-entry-count](at-ds-mon-cache-max-entry-count.html)

* [ds-mon-cache-max-size-bytes](at-ds-mon-cache-max-size-bytes.html)

* [ds-mon-cache-misses](at-ds-mon-cache-misses.html)

* [ds-mon-cache-size-bytes](at-ds-mon-cache-size-bytes.html)

* [ds-mon-cache-total-tries](at-ds-mon-cache-total-tries.html)

* [ds-mon-certificate-expires-at](at-ds-mon-certificate-expires-at.html)

* [ds-mon-certificate-issuer-dn](at-ds-mon-certificate-issuer-dn.html)

* [ds-mon-certificate-serial-number](at-ds-mon-certificate-serial-number.html)

* [ds-mon-certificate-subject-dn](at-ds-mon-certificate-subject-dn.html)

* [ds-mon-changelog-file-count](at-ds-mon-changelog-file-count.html)

* [ds-mon-changelog-hostport](at-ds-mon-changelog-hostport.html)

* [ds-mon-changelog-id](at-ds-mon-changelog-id.html)

* [ds-mon-changelog-purge-delay](at-ds-mon-changelog-purge-delay.html)

* [ds-mon-collective-attribute-subentries-count](at-ds-mon-collective-attribute-subentries-count.html)

* [ds-mon-compact-version](at-ds-mon-compact-version.html)

* [ds-mon-config-dn](at-ds-mon-config-dn.html)

* [ds-mon-connected-to-server-hostport](at-ds-mon-connected-to-server-hostport.html)

* [ds-mon-connected-to-server-id](at-ds-mon-connected-to-server-id.html)

* [ds-mon-connection](at-ds-mon-connection.html)

* [ds-mon-connections](at-ds-mon-connections.html)

* [ds-mon-current-connections](at-ds-mon-current-connections.html)

* [ds-mon-current-receive-window](at-ds-mon-current-receive-window.html)

* [ds-mon-current-time](at-ds-mon-current-time.html)

* [ds-mon-db-cache-evict-internal-nodes-count](at-ds-mon-db-cache-evict-internal-nodes-count.html)

* [ds-mon-db-cache-evict-leaf-nodes-count](at-ds-mon-db-cache-evict-leaf-nodes-count.html)

* [ds-mon-db-cache-leaf-nodes](at-ds-mon-db-cache-leaf-nodes.html)

* [ds-mon-db-cache-misses-internal-nodes](at-ds-mon-db-cache-misses-internal-nodes.html)

* [ds-mon-db-cache-misses-leaf-nodes](at-ds-mon-db-cache-misses-leaf-nodes.html)

* [ds-mon-db-cache-size-active](at-ds-mon-db-cache-size-active.html)

* [ds-mon-db-cache-size-total](at-ds-mon-db-cache-size-total.html)

* [ds-mon-db-cache-total-tries-internal-nodes](at-ds-mon-db-cache-total-tries-internal-nodes.html)

* [ds-mon-db-cache-total-tries-leaf-nodes](at-ds-mon-db-cache-total-tries-leaf-nodes.html)

* [ds-mon-db-checkpoint-count](at-ds-mon-db-checkpoint-count.html)

* [ds-mon-db-log-cleaner-file-deletion-count](at-ds-mon-db-log-cleaner-file-deletion-count.html)

* [ds-mon-db-log-files-open](at-ds-mon-db-log-files-open.html)

* [ds-mon-db-log-files-opened](at-ds-mon-db-log-files-opened.html)

* [ds-mon-db-log-size-active](at-ds-mon-db-log-size-active.html)

* [ds-mon-db-log-size-total](at-ds-mon-db-log-size-total.html)

* [ds-mon-db-log-utilization-max](at-ds-mon-db-log-utilization-max.html)

* [ds-mon-db-log-utilization-min](at-ds-mon-db-log-utilization-min.html)

* [ds-mon-db-version](at-ds-mon-db-version.html)

* [ds-mon-disk-dir](at-ds-mon-disk-dir.html)

* [ds-mon-disk-free](at-ds-mon-disk-free.html)

* [ds-mon-disk-full-threshold](at-ds-mon-disk-full-threshold.html)

* [ds-mon-disk-low-threshold](at-ds-mon-disk-low-threshold.html)

* [ds-mon-disk-root](at-ds-mon-disk-root.html)

* [ds-mon-disk-state](at-ds-mon-disk-state.html)

* [ds-mon-domain-generation-id](at-ds-mon-domain-generation-id.html)

* [ds-mon-domain-name](at-ds-mon-domain-name.html)

* [ds-mon-dynamic-groups-count](at-ds-mon-dynamic-groups-count.html)

* [ds-mon-entries-acis-count](at-ds-mon-entries-acis-count.html)

* [ds-mon-entries-awaiting-updates-count](at-ds-mon-entries-awaiting-updates-count.html)

* [ds-mon-entries-with-aci-attributes-count](at-ds-mon-entries-with-aci-attributes-count.html)

* [ds-mon-fix-ids](at-ds-mon-fix-ids.html)

* [ds-mon-full-version](at-ds-mon-full-version.html)

* [ds-mon-global-acis-count](at-ds-mon-global-acis-count.html)

* [ds-mon-group-id](at-ds-mon-group-id.html)

* [ds-mon-healthy-errors](at-ds-mon-healthy-errors.html)

* [ds-mon-healthy](at-ds-mon-healthy.html)

* [ds-mon-index-cost](at-ds-mon-index-cost.html)

* [ds-mon-index-uses](at-ds-mon-index-uses.html)

* [ds-mon-index](at-ds-mon-index.html)

* [ds-mon-install-path](at-ds-mon-install-path.html)

* [ds-mon-instance-path](at-ds-mon-instance-path.html)

* [ds-mon-jvm-architecture](at-ds-mon-jvm-architecture.html)

* [ds-mon-jvm-arguments](at-ds-mon-jvm-arguments.html)

* [ds-mon-jvm-available-cpus](at-ds-mon-jvm-available-cpus.html)

* [ds-mon-jvm-class-path](at-ds-mon-jvm-class-path.html)

* [ds-mon-jvm-classes-loaded](at-ds-mon-jvm-classes-loaded.html)

* [ds-mon-jvm-classes-unloaded](at-ds-mon-jvm-classes-unloaded.html)

* [ds-mon-jvm-java-home](at-ds-mon-jvm-java-home.html)

* [ds-mon-jvm-java-vendor](at-ds-mon-jvm-java-vendor.html)

* [ds-mon-jvm-java-version](at-ds-mon-jvm-java-version.html)

* [ds-mon-jvm-memory-heap-init](at-ds-mon-jvm-memory-heap-init.html)

* [ds-mon-jvm-memory-heap-max](at-ds-mon-jvm-memory-heap-max.html)

* [ds-mon-jvm-memory-heap-reserved](at-ds-mon-jvm-memory-heap-reserved.html)

* [ds-mon-jvm-memory-heap-used](at-ds-mon-jvm-memory-heap-used.html)

* [ds-mon-jvm-memory-init](at-ds-mon-jvm-memory-init.html)

* [ds-mon-jvm-memory-max](at-ds-mon-jvm-memory-max.html)

* [ds-mon-jvm-memory-non-heap-init](at-ds-mon-jvm-memory-non-heap-init.html)

* [ds-mon-jvm-memory-non-heap-max](at-ds-mon-jvm-memory-non-heap-max.html)

* [ds-mon-jvm-memory-non-heap-reserved](at-ds-mon-jvm-memory-non-heap-reserved.html)

* [ds-mon-jvm-memory-non-heap-used](at-ds-mon-jvm-memory-non-heap-used.html)

* [ds-mon-jvm-memory-reserved](at-ds-mon-jvm-memory-reserved.html)

* [ds-mon-jvm-memory-used](at-ds-mon-jvm-memory-used.html)

* [ds-mon-jvm-supported-tls-ciphers](at-ds-mon-jvm-supported-tls-ciphers.html)

* [ds-mon-jvm-supported-tls-protocols](at-ds-mon-jvm-supported-tls-protocols.html)

* [ds-mon-jvm-threads-blocked-count](at-ds-mon-jvm-threads-blocked-count.html)

* [ds-mon-jvm-threads-count](at-ds-mon-jvm-threads-count.html)

* [ds-mon-jvm-threads-daemon-count](at-ds-mon-jvm-threads-daemon-count.html)

* [ds-mon-jvm-threads-deadlock-count](at-ds-mon-jvm-threads-deadlock-count.html)

* [ds-mon-jvm-threads-deadlocks](at-ds-mon-jvm-threads-deadlocks.html)

* [ds-mon-jvm-threads-new-count](at-ds-mon-jvm-threads-new-count.html)

* [ds-mon-jvm-threads-runnable-count](at-ds-mon-jvm-threads-runnable-count.html)

* [ds-mon-jvm-threads-terminated-count](at-ds-mon-jvm-threads-terminated-count.html)

* [ds-mon-jvm-threads-timed-waiting-count](at-ds-mon-jvm-threads-timed-waiting-count.html)

* [ds-mon-jvm-threads-waiting-count](at-ds-mon-jvm-threads-waiting-count.html)

* [ds-mon-jvm-vendor](at-ds-mon-jvm-vendor.html)

* [ds-mon-jvm-version](at-ds-mon-jvm-version.html)

* [ds-mon-last-received-update](at-ds-mon-last-received-update.html)

* [ds-mon-last-replayed-update](at-ds-mon-last-replayed-update.html)

* [ds-mon-last-seen](at-ds-mon-last-seen.html)

* [ds-mon-ldap-hostport](at-ds-mon-ldap-hostport.html)

* [ds-mon-ldap-starttls-hostport](at-ds-mon-ldap-starttls-hostport.html)

* [ds-mon-ldaps-hostport](at-ds-mon-ldaps-hostport.html)

* [ds-mon-listen-address](at-ds-mon-listen-address.html)

* [ds-mon-lost-connections](at-ds-mon-lost-connections.html)

* [ds-mon-major-version](at-ds-mon-major-version.html)

* [ds-mon-max-connections](at-ds-mon-max-connections.html)

* [ds-mon-minor-version](at-ds-mon-minor-version.html)

* [ds-mon-newest-change-number](at-ds-mon-newest-change-number.html)

* [ds-mon-newest-csn-timestamp](at-ds-mon-newest-csn-timestamp.html)

* [ds-mon-newest-csn](at-ds-mon-newest-csn.html)

* [ds-mon-oldest-change-number](at-ds-mon-oldest-change-number.html)

* [ds-mon-oldest-csn-timestamp](at-ds-mon-oldest-csn-timestamp.html)

* [ds-mon-oldest-csn](at-ds-mon-oldest-csn.html)

* [ds-mon-os-architecture](at-ds-mon-os-architecture.html)

* [ds-mon-os-name](at-ds-mon-os-name.html)

* [ds-mon-os-version](at-ds-mon-os-version.html)

* [ds-mon-password-policy-subentries-count](at-ds-mon-password-policy-subentries-count.html)

* [ds-mon-point-version](at-ds-mon-point-version.html)

* [ds-mon-process-id](at-ds-mon-process-id.html)

* [ds-mon-product-name](at-ds-mon-product-name.html)

* [ds-mon-protocol](at-ds-mon-protocol.html)

* [ds-mon-receive-delay](at-ds-mon-receive-delay.html)

* [ds-mon-replay-delay](at-ds-mon-replay-delay.html)

* [ds-mon-replayed-internal-updates](at-ds-mon-replayed-internal-updates.html)

* [ds-mon-replayed-updates-conflicts-resolved](at-ds-mon-replayed-updates-conflicts-resolved.html)

* [ds-mon-replayed-updates-conflicts-unresolved](at-ds-mon-replayed-updates-conflicts-unresolved.html)

* [ds-mon-replayed-updates](at-ds-mon-replayed-updates.html)

* [ds-mon-replication-domain](at-ds-mon-replication-domain.html)

* [ds-mon-replication-protocol-version](at-ds-mon-replication-protocol-version.html)

* [ds-mon-requests-abandon](at-ds-mon-requests-abandon.html)

* [ds-mon-requests-add](at-ds-mon-requests-add.html)

* [ds-mon-requests-bind](at-ds-mon-requests-bind.html)

* [ds-mon-requests-compare](at-ds-mon-requests-compare.html)

* [ds-mon-requests-delete](at-ds-mon-requests-delete.html)

* [ds-mon-requests-extended](at-ds-mon-requests-extended.html)

* [ds-mon-requests-failure-client-invalid-request](at-ds-mon-requests-failure-client-invalid-request.html)

* [ds-mon-requests-failure-client-redirect](at-ds-mon-requests-failure-client-redirect.html)

* [ds-mon-requests-failure-client-referral](at-ds-mon-requests-failure-client-referral.html)

* [ds-mon-requests-failure-client-resource-limit](at-ds-mon-requests-failure-client-resource-limit.html)

* [ds-mon-requests-failure-client-security](at-ds-mon-requests-failure-client-security.html)

* [ds-mon-requests-failure-server](at-ds-mon-requests-failure-server.html)

* [ds-mon-requests-failure-uncategorized](at-ds-mon-requests-failure-uncategorized.html)

* [ds-mon-requests-get](at-ds-mon-requests-get.html)

* [ds-mon-requests-in-queue](at-ds-mon-requests-in-queue.html)

* [ds-mon-requests-modify-dn](at-ds-mon-requests-modify-dn.html)

* [ds-mon-requests-modify](at-ds-mon-requests-modify.html)

* [ds-mon-requests-patch](at-ds-mon-requests-patch.html)

* [ds-mon-requests-post](at-ds-mon-requests-post.html)

* [ds-mon-requests-psearch](at-ds-mon-requests-psearch.html)

* [ds-mon-requests-put](at-ds-mon-requests-put.html)

* [ds-mon-requests-search-base](at-ds-mon-requests-search-base.html)

* [ds-mon-requests-search-one](at-ds-mon-requests-search-one.html)

* [ds-mon-requests-search-sub](at-ds-mon-requests-search-sub.html)

* [ds-mon-requests-submitted](at-ds-mon-requests-submitted.html)

* [ds-mon-requests-unbind](at-ds-mon-requests-unbind.html)

* [ds-mon-requests-uncategorized](at-ds-mon-requests-uncategorized.html)

* [ds-mon-revision](at-ds-mon-revision.html)

* [ds-mon-sent-updates](at-ds-mon-sent-updates.html)

* [ds-mon-server-id](at-ds-mon-server-id.html)

* [ds-mon-server-is-local](at-ds-mon-server-is-local.html)

* [ds-mon-server-state](at-ds-mon-server-state.html)

* [ds-mon-short-name](at-ds-mon-short-name.html)

* [ds-mon-ssl-encryption](at-ds-mon-ssl-encryption.html)

* [ds-mon-start-time](at-ds-mon-start-time.html)

* [ds-mon-static-group-size-less-or-equal-to-100](at-ds-mon-static-group-size-less-or-equal-to-100.html)

* [ds-mon-static-group-size-less-or-equal-to-1000](at-ds-mon-static-group-size-less-or-equal-to-1000.html)

* [ds-mon-static-group-size-less-or-equal-to-10000](at-ds-mon-static-group-size-less-or-equal-to-10000.html)

* [ds-mon-static-group-size-less-or-equal-to-100000](at-ds-mon-static-group-size-less-or-equal-to-100000.html)

* [ds-mon-static-group-size-less-or-equal-to-1000000](at-ds-mon-static-group-size-less-or-equal-to-1000000.html)

* [ds-mon-static-group-size-less-or-equal-to-inf](at-ds-mon-static-group-size-less-or-equal-to-inf.html)

* [ds-mon-static-groups-count](at-ds-mon-static-groups-count.html)

* [ds-mon-status-last-changed](at-ds-mon-status-last-changed.html)

* [ds-mon-status](at-ds-mon-status.html)

* [ds-mon-supported-log-category](at-ds-mon-supported-log-category.html)

* [ds-mon-system-name](at-ds-mon-system-name.html)

* [ds-mon-total-connections](at-ds-mon-total-connections.html)

* [ds-mon-total-update-entry-count](at-ds-mon-total-update-entry-count.html)

* [ds-mon-total-update-entry-left](at-ds-mon-total-update-entry-left.html)

* [ds-mon-total-update](at-ds-mon-total-update.html)

* [ds-mon-updates-already-in-progress](at-ds-mon-updates-already-in-progress.html)

* [ds-mon-updates-in-progress](at-ds-mon-updates-in-progress.html)

* [ds-mon-updates-in-queue](at-ds-mon-updates-in-queue.html)

* [ds-mon-updates-inbound-queue](at-ds-mon-updates-inbound-queue.html)

* [ds-mon-updates-outbound-queue](at-ds-mon-updates-outbound-queue.html)

* [ds-mon-updates-totals-per-replay-thread](at-ds-mon-updates-totals-per-replay-thread.html)

* [ds-mon-vendor-name](at-ds-mon-vendor-name.html)

* [ds-mon-version-qualifier](at-ds-mon-version-qualifier.html)

* [ds-mon-virtual-static-groups-count](at-ds-mon-virtual-static-groups-count.html)

* [ds-mon-working-directory](at-ds-mon-working-directory.html)

* [ds-private-naming-contexts](at-ds-private-naming-contexts.html)

* [ds-privilege-name](at-ds-privilege-name.html)

* [ds-pwp-account-disabled](at-ds-pwp-account-disabled.html)

* [ds-pwp-account-expiration-time](at-ds-pwp-account-expiration-time.html)

* [ds-pwp-account-status-notification-handler](at-ds-pwp-account-status-notification-handler.html)

* [ds-pwp-allow-expired-password-changes](at-ds-pwp-allow-expired-password-changes.html)

* [ds-pwp-allow-multiple-password-values](at-ds-pwp-allow-multiple-password-values.html)

* [ds-pwp-allow-pre-encoded-passwords](at-ds-pwp-allow-pre-encoded-passwords.html)

* [ds-pwp-allow-user-password-changes](at-ds-pwp-allow-user-password-changes.html)

* [ds-pwp-attribute-value-check-substrings](at-ds-pwp-attribute-value-check-substrings.html)

* [ds-pwp-attribute-value-match-attribute](at-ds-pwp-attribute-value-match-attribute.html)

* [ds-pwp-attribute-value-min-substring-length](at-ds-pwp-attribute-value-min-substring-length.html)

* [ds-pwp-attribute-value-test-reversed-password](at-ds-pwp-attribute-value-test-reversed-password.html)

* [ds-pwp-character-set-allow-unclassified-characters](at-ds-pwp-character-set-allow-unclassified-characters.html)

* [ds-pwp-character-set-character-set-ranges](at-ds-pwp-character-set-character-set-ranges.html)

* [ds-pwp-character-set-character-set](at-ds-pwp-character-set-character-set.html)

* [ds-pwp-character-set-min-character-sets](at-ds-pwp-character-set-min-character-sets.html)

* [ds-pwp-default-password-storage-scheme](at-ds-pwp-default-password-storage-scheme.html)

* [ds-pwp-deprecated-password-storage-scheme](at-ds-pwp-deprecated-password-storage-scheme.html)

* [ds-pwp-dictionary-case-sensitive-validation](at-ds-pwp-dictionary-case-sensitive-validation.html)

* [ds-pwp-dictionary-check-substrings](at-ds-pwp-dictionary-check-substrings.html)

* [ds-pwp-dictionary-data](at-ds-pwp-dictionary-data.html)

* [ds-pwp-dictionary-min-substring-length](at-ds-pwp-dictionary-min-substring-length.html)

* [ds-pwp-dictionary-test-reversed-password](at-ds-pwp-dictionary-test-reversed-password.html)

* [ds-pwp-expire-passwords-without-warning](at-ds-pwp-expire-passwords-without-warning.html)

* [ds-pwp-force-change-on-add](at-ds-pwp-force-change-on-add.html)

* [ds-pwp-force-change-on-reset](at-ds-pwp-force-change-on-reset.html)

* [ds-pwp-grace-login-count](at-ds-pwp-grace-login-count.html)

* [ds-pwp-idle-lockout-interval](at-ds-pwp-idle-lockout-interval.html)

* [ds-pwp-last-login-time-attribute](at-ds-pwp-last-login-time-attribute.html)

* [ds-pwp-last-login-time-format](at-ds-pwp-last-login-time-format.html)

* [ds-pwp-last-login-time](at-ds-pwp-last-login-time.html)

* [ds-pwp-length-based-max-password-length](at-ds-pwp-length-based-max-password-length.html)

* [ds-pwp-length-based-min-password-length](at-ds-pwp-length-based-min-password-length.html)

* [ds-pwp-lockout-duration](at-ds-pwp-lockout-duration.html)

* [ds-pwp-lockout-failure-count](at-ds-pwp-lockout-failure-count.html)

* [ds-pwp-lockout-failure-expiration-interval](at-ds-pwp-lockout-failure-expiration-interval.html)

* [ds-pwp-max-password-age](at-ds-pwp-max-password-age.html)

* [ds-pwp-max-password-reset-age](at-ds-pwp-max-password-reset-age.html)

* [ds-pwp-min-password-age](at-ds-pwp-min-password-age.html)

* [ds-pwp-password-attribute](at-ds-pwp-password-attribute.html)

* [ds-pwp-password-change-requires-current-password](at-ds-pwp-password-change-requires-current-password.html)

* [ds-pwp-password-changed-by-required-time](at-ds-pwp-password-changed-by-required-time.html)

* [ds-pwp-password-expiration-time](at-ds-pwp-password-expiration-time.html)

* [ds-pwp-password-expiration-warning-interval](at-ds-pwp-password-expiration-warning-interval.html)

* [ds-pwp-password-history-count](at-ds-pwp-password-history-count.html)

* [ds-pwp-password-history-duration](at-ds-pwp-password-history-duration.html)

* [ds-pwp-password-policy-dn](at-ds-pwp-password-policy-dn.html)

* [ds-pwp-previous-last-login-time-format](at-ds-pwp-previous-last-login-time-format.html)

* [ds-pwp-random-password-character-set](at-ds-pwp-random-password-character-set.html)

* [ds-pwp-random-password-format](at-ds-pwp-random-password-format.html)

* [ds-pwp-repeated-characters-case-sensitive-validation](at-ds-pwp-repeated-characters-case-sensitive-validation.html)

* [ds-pwp-repeated-characters-max-consecutive-length](at-ds-pwp-repeated-characters-max-consecutive-length.html)

* [ds-pwp-require-change-by-time](at-ds-pwp-require-change-by-time.html)

* [ds-pwp-require-secure-authentication](at-ds-pwp-require-secure-authentication.html)

* [ds-pwp-require-secure-password-changes](at-ds-pwp-require-secure-password-changes.html)

* [ds-pwp-reset-time](at-ds-pwp-reset-time.html)

* [ds-pwp-similarity-based-min-password-difference](at-ds-pwp-similarity-based-min-password-difference.html)

* [ds-pwp-skip-validation-for-administrators](at-ds-pwp-skip-validation-for-administrators.html)

* [ds-pwp-state-json](at-ds-pwp-state-json.html)

* [ds-pwp-state-update-failure-policy](at-ds-pwp-state-update-failure-policy.html)

* [ds-pwp-unique-characters-case-sensitive-validation](at-ds-pwp-unique-characters-case-sensitive-validation.html)

* [ds-pwp-unique-characters-min-unique-characters](at-ds-pwp-unique-characters-min-unique-characters.html)

* [ds-pwp-warned-time](at-ds-pwp-warned-time.html)

* [ds-rlim-idle-time-limit](at-ds-rlim-idle-time-limit.html)

* [ds-rlim-lookthrough-limit](at-ds-rlim-lookthrough-limit.html)

* [ds-rlim-max-candidate-set-size](at-ds-rlim-max-candidate-set-size.html)

* [ds-rlim-size-limit](at-ds-rlim-size-limit.html)

* [ds-rlim-time-limit](at-ds-rlim-time-limit.html)

* [ds-sync-conflict](at-ds-sync-conflict.html)

* [ds-sync-delay](at-ds-sync-delay.html)

* [ds-sync-domain-state](at-ds-sync-domain-state.html)

* [ds-sync-fractional-exclude](at-ds-sync-fractional-exclude.html)

* [ds-sync-fractional-include](at-ds-sync-fractional-include.html)

* [ds-sync-generation-id](at-ds-sync-generation-id.html)

* [ds-sync-hist](at-ds-sync-hist.html)

* [ds-sync-is-available](at-ds-sync-is-available.html)

* [ds-sync-state](at-ds-sync-state.html)

* [ds-target-group-dn](at-ds-target-group-dn.html)

* [ds-topology-advertised-address](at-ds-topology-advertised-address.html)

* [ds-topology-location](at-ds-topology-location.html)

* [ds-topology-server-id](at-ds-topology-server-id.html)

* [dSAQuality](at-dSAQuality.html)

* [emailAddress](at-emailAddress.html)

* [employeeNumber](at-employeeNumber.html)

* [employeeType](at-employeeType.html)

* [enhancedSearchGuide](at-enhancedSearchGuide.html)

* [entryDN](at-entryDN.html)

* [entryUUID](at-entryUUID.html)

* [etag](at-etag.html)

* [facsimileTelephoneNumber](at-facsimileTelephoneNumber.html)

* [firstChangeNumber](at-firstChangeNumber.html)

* [followReferrals](at-followReferrals.html)

* [fr-idm-account-applicationId](at-fr-idm-account-applicationId.html)

* [fr-idm-account-constraint](at-fr-idm-account-constraint.html)

* [fr-idm-account-id](at-fr-idm-account-id.html)

* [fr-idm-account-name](at-fr-idm-account-name.html)

* [fr-idm-account-owner](at-fr-idm-account-owner.html)

* [fr-idm-account-state](at-fr-idm-account-state.html)

* [fr-idm-account-type](at-fr-idm-account-type.html)

* [fr-idm-accountStatus](at-fr-idm-accountStatus.html)

* [fr-idm-agent-id](at-fr-idm-agent-id.html)

* [fr-idm-agent-oauth2-client-id](at-fr-idm-agent-oauth2-client-id.html)

* [fr-idm-agent-reference](at-fr-idm-agent-reference.html)

* [fr-idm-assignment-condition](at-fr-idm-assignment-condition.html)

* [fr-idm-cluster-json](at-fr-idm-cluster-json.html)

* [fr-idm-condition](at-fr-idm-condition.html)

* [fr-idm-consentedMapping](at-fr-idm-consentedMapping.html)

* [fr-idm-custom-attrs](at-fr-idm-custom-attrs.html)

* [fr-idm-effectiveApplications](at-fr-idm-effectiveApplications.html)

* [fr-idm-effectiveAssignment](at-fr-idm-effectiveAssignment.html)

* [fr-idm-effectiveGroup](at-fr-idm-effectiveGroup.html)

* [fr-idm-effectiveRole](at-fr-idm-effectiveRole.html)

* [fr-idm-internal-role-authzmembers-internal-user](at-fr-idm-internal-role-authzmembers-internal-user.html)

* [fr-idm-internal-role-authzmembers-managed-user](at-fr-idm-internal-role-authzmembers-managed-user.html)

* [fr-idm-internal-user-authzroles-internal-role](at-fr-idm-internal-user-authzroles-internal-role.html)

* [fr-idm-internal-user-authzroles-managed-role](at-fr-idm-internal-user-authzroles-managed-role.html)

* [fr-idm-json](at-fr-idm-json.html)

* [fr-idm-kbaInfo](at-fr-idm-kbaInfo.html)

* [fr-idm-lastSync](at-fr-idm-lastSync.html)

* [fr-idm-link-firstid-constraint](at-fr-idm-link-firstid-constraint.html)

* [fr-idm-link-firstid](at-fr-idm-link-firstid.html)

* [fr-idm-link-firstiduniqueid](at-fr-idm-link-firstiduniqueid.html)

* [fr-idm-link-qualifier](at-fr-idm-link-qualifier.html)

* [fr-idm-link-secondid-constraint](at-fr-idm-link-secondid-constraint.html)

* [fr-idm-link-secondid](at-fr-idm-link-secondid.html)

* [fr-idm-link-secondidqualifier](at-fr-idm-link-secondidqualifier.html)

* [fr-idm-link-secondiduniqueid](at-fr-idm-link-secondiduniqueid.html)

* [fr-idm-link-type](at-fr-idm-link-type.html)

* [fr-idm-lock-nodeid](at-fr-idm-lock-nodeid.html)

* [fr-idm-managed-application-json](at-fr-idm-managed-application-json.html)

* [fr-idm-managed-application-member](at-fr-idm-managed-application-member.html)

* [fr-idm-managed-application-name](at-fr-idm-managed-application-name.html)

* [fr-idm-managed-application-owner](at-fr-idm-managed-application-owner.html)

* [fr-idm-managed-assignment-json](at-fr-idm-managed-assignment-json.html)

* [fr-idm-managed-assignment-member](at-fr-idm-managed-assignment-member.html)

* [fr-idm-managed-group-condition](at-fr-idm-managed-group-condition.html)

* [fr-idm-managed-group-json](at-fr-idm-managed-group-json.html)

* [fr-idm-managed-organization-admin-roleid](at-fr-idm-managed-organization-admin-roleid.html)

* [fr-idm-managed-organization-admin](at-fr-idm-managed-organization-admin.html)

* [fr-idm-managed-organization-child](at-fr-idm-managed-organization-child.html)

* [fr-idm-managed-organization-json](at-fr-idm-managed-organization-json.html)

* [fr-idm-managed-organization-member](at-fr-idm-managed-organization-member.html)

* [fr-idm-managed-organization-name](at-fr-idm-managed-organization-name.html)

* [fr-idm-managed-organization-owner-roleid](at-fr-idm-managed-organization-owner-roleid.html)

* [fr-idm-managed-organization-owner](at-fr-idm-managed-organization-owner.html)

* [fr-idm-managed-organization-parent](at-fr-idm-managed-organization-parent.html)

* [fr-idm-managed-role-applications](at-fr-idm-managed-role-applications.html)

* [fr-idm-managed-role-assignments](at-fr-idm-managed-role-assignments.html)

* [fr-idm-managed-role-json](at-fr-idm-managed-role-json.html)

* [fr-idm-managed-user-activate-account](at-fr-idm-managed-user-activate-account.html)

* [fr-idm-managed-user-active-date](at-fr-idm-managed-user-active-date.html)

* [fr-idm-managed-user-authzroles-internal-role](at-fr-idm-managed-user-authzroles-internal-role.html)

* [fr-idm-managed-user-authzroles-managed-role](at-fr-idm-managed-user-authzroles-managed-role.html)

* [fr-idm-managed-user-custom-attrs](at-fr-idm-managed-user-custom-attrs.html)

* [fr-idm-managed-user-expire-account](at-fr-idm-managed-user-expire-account.html)

* [fr-idm-managed-user-groups](at-fr-idm-managed-user-groups.html)

* [fr-idm-managed-user-inactive-date](at-fr-idm-managed-user-inactive-date.html)

* [fr-idm-managed-user-json](at-fr-idm-managed-user-json.html)

* [fr-idm-managed-user-manager](at-fr-idm-managed-user-manager.html)

* [fr-idm-managed-user-memberoforgid](at-fr-idm-managed-user-memberoforgid.html)

* [fr-idm-managed-user-meta](at-fr-idm-managed-user-meta.html)

* [fr-idm-managed-user-notifications](at-fr-idm-managed-user-notifications.html)

* [fr-idm-managed-user-roles](at-fr-idm-managed-user-roles.html)

* [fr-idm-managed-user-task-principals](at-fr-idm-managed-user-task-principals.html)

* [fr-idm-name](at-fr-idm-name.html)

* [fr-idm-notification-json](at-fr-idm-notification-json.html)

* [fr-idm-oauth2-client-id](at-fr-idm-oauth2-client-id.html)

* [fr-idm-owners-reference](at-fr-idm-owners-reference.html)

* [fr-idm-password](at-fr-idm-password.html)

* [fr-idm-pending-account-applicationId](at-fr-idm-pending-account-applicationId.html)

* [fr-idm-pending-account-constraint](at-fr-idm-pending-account-constraint.html)

* [fr-idm-pending-account-name](at-fr-idm-pending-account-name.html)

* [fr-idm-pending-account-owner](at-fr-idm-pending-account-owner.html)

* [fr-idm-pending-account-type](at-fr-idm-pending-account-type.html)

* [fr-idm-permission](at-fr-idm-permission.html)

* [fr-idm-preferences](at-fr-idm-preferences.html)

* [fr-idm-privilege](at-fr-idm-privilege.html)

* [fr-idm-recon-id](at-fr-idm-recon-id.html)

* [fr-idm-recon-targetIds](at-fr-idm-recon-targetIds.html)

* [fr-idm-reconassoc-finishtime](at-fr-idm-reconassoc-finishtime.html)

* [fr-idm-reconassoc-isanalysis](at-fr-idm-reconassoc-isanalysis.html)

* [fr-idm-reconassoc-mapping](at-fr-idm-reconassoc-mapping.html)

* [fr-idm-reconassoc-reconid](at-fr-idm-reconassoc-reconid.html)

* [fr-idm-reconassoc-sourceresourcecollection](at-fr-idm-reconassoc-sourceresourcecollection.html)

* [fr-idm-reconassoc-targetresourcecollection](at-fr-idm-reconassoc-targetresourcecollection.html)

* [fr-idm-reconassocentry-action](at-fr-idm-reconassocentry-action.html)

* [fr-idm-reconassocentry-ambiguoustargetobjectids](at-fr-idm-reconassocentry-ambiguoustargetobjectids.html)

* [fr-idm-reconassocentry-exception](at-fr-idm-reconassocentry-exception.html)

* [fr-idm-reconassocentry-linkqualifier](at-fr-idm-reconassocentry-linkqualifier.html)

* [fr-idm-reconassocentry-message](at-fr-idm-reconassocentry-message.html)

* [fr-idm-reconassocentry-messagedetail](at-fr-idm-reconassocentry-messagedetail.html)

* [fr-idm-reconassocentry-phase](at-fr-idm-reconassocentry-phase.html)

* [fr-idm-reconassocentry-reconid](at-fr-idm-reconassocentry-reconid.html)

* [fr-idm-reconassocentry-situation](at-fr-idm-reconassocentry-situation.html)

* [fr-idm-reconassocentry-sourceobjectid](at-fr-idm-reconassocentry-sourceobjectid.html)

* [fr-idm-reconassocentry-status](at-fr-idm-reconassocentry-status.html)

* [fr-idm-reconassocentry-targetobjectid](at-fr-idm-reconassocentry-targetobjectid.html)

* [fr-idm-reference-1](at-fr-idm-reference-1.html)

* [fr-idm-reference-10](at-fr-idm-reference-10.html)

* [fr-idm-reference-2](at-fr-idm-reference-2.html)

* [fr-idm-reference-3](at-fr-idm-reference-3.html)

* [fr-idm-reference-4](at-fr-idm-reference-4.html)

* [fr-idm-reference-5](at-fr-idm-reference-5.html)

* [fr-idm-reference-6](at-fr-idm-reference-6.html)

* [fr-idm-reference-7](at-fr-idm-reference-7.html)

* [fr-idm-reference-8](at-fr-idm-reference-8.html)

* [fr-idm-reference-9](at-fr-idm-reference-9.html)

* [fr-idm-relationship-json](at-fr-idm-relationship-json.html)

* [fr-idm-resource-reference](at-fr-idm-resource-reference.html)

* [fr-idm-resourcedata](at-fr-idm-resourcedata.html)

* [fr-idm-role](at-fr-idm-role.html)

* [fr-idm-subject-id](at-fr-idm-subject-id.html)

* [fr-idm-subject-reference](at-fr-idm-subject-reference.html)

* [fr-idm-subjectgroup-reference](at-fr-idm-subjectgroup-reference.html)

* [fr-idm-syncqueue-context](at-fr-idm-syncqueue-context.html)

* [fr-idm-syncqueue-createdate](at-fr-idm-syncqueue-createdate.html)

* [fr-idm-syncqueue-mapping](at-fr-idm-syncqueue-mapping.html)

* [fr-idm-syncqueue-newobject](at-fr-idm-syncqueue-newobject.html)

* [fr-idm-syncqueue-nodeid](at-fr-idm-syncqueue-nodeid.html)

* [fr-idm-syncqueue-objectrev](at-fr-idm-syncqueue-objectrev.html)

* [fr-idm-syncqueue-oldobject](at-fr-idm-syncqueue-oldobject.html)

* [fr-idm-syncqueue-remainingretries](at-fr-idm-syncqueue-remainingretries.html)

* [fr-idm-syncqueue-resourcecollection](at-fr-idm-syncqueue-resourcecollection.html)

* [fr-idm-syncqueue-resourceid](at-fr-idm-syncqueue-resourceid.html)

* [fr-idm-syncqueue-state](at-fr-idm-syncqueue-state.html)

* [fr-idm-syncqueue-syncaction](at-fr-idm-syncqueue-syncaction.html)

* [fr-idm-temporal-constraints](at-fr-idm-temporal-constraints.html)

* [fr-idm-token](at-fr-idm-token.html)

* [fr-idm-uuid](at-fr-idm-uuid.html)

* [fullVendorVersion](at-fullVendorVersion.html)

* [gecos](at-gecos.html)

* [generationQualifier](at-generationQualifier.html)

* [gidNumber](at-gidNumber.html)

* [givenName](at-givenName.html)

* [governingStructureRule](at-governingStructureRule.html)

* [hasSubordinates](at-hasSubordinates.html)

* [healthy](at-healthy.html)

* [homeDirectory](at-homeDirectory.html)

* [homePhone](at-homePhone.html)

* [homePostalAddress](at-homePostalAddress.html)

* [host](at-host.html)

* [houseIdentifier](at-houseIdentifier.html)

* [includedAttributes](at-includedAttributes.html)

* [inetUserHttpURL](at-inetUserHttpURL.html)

* [inetUserStatus](at-inetUserStatus.html)

* [info](at-info.html)

* [inheritable](at-inheritable.html)

* [inheritAttribute](at-inheritAttribute.html)

* [inheritFromBaseRDN](at-inheritFromBaseRDN.html)

* [inheritFromDNAttribute](at-inheritFromDNAttribute.html)

* [inheritFromDNParent](at-inheritFromDNParent.html)

* [inheritFromRDNAttribute](at-inheritFromRDNAttribute.html)

* [inheritFromRDNType](at-inheritFromRDNType.html)

* [initials](at-initials.html)

* [internationaliSDNNumber](at-internationaliSDNNumber.html)

* [ipHostNumber](at-ipHostNumber.html)

* [iplanet-am-auth-configuration](at-iplanet-am-auth-configuration.html)

* [iplanet-am-auth-login-failure-url](at-iplanet-am-auth-login-failure-url.html)

* [iplanet-am-auth-login-success-url](at-iplanet-am-auth-login-success-url.html)

* [iplanet-am-auth-post-login-process-class](at-iplanet-am-auth-post-login-process-class.html)

* [iplanet-am-session-destroy-sessions](at-iplanet-am-session-destroy-sessions.html)

* [iplanet-am-session-get-valid-sessions](at-iplanet-am-session-get-valid-sessions.html)

* [iplanet-am-session-max-caching-time](at-iplanet-am-session-max-caching-time.html)

* [iplanet-am-session-max-idle-time](at-iplanet-am-session-max-idle-time.html)

* [iplanet-am-session-max-session-time](at-iplanet-am-session-max-session-time.html)

* [iplanet-am-session-quota-limit](at-iplanet-am-session-quota-limit.html)

* [iplanet-am-session-service-status](at-iplanet-am-session-service-status.html)

* [iplanet-am-user-account-life](at-iplanet-am-user-account-life.html)

* [iplanet-am-user-admin-start-dn](at-iplanet-am-user-admin-start-dn.html)

* [iplanet-am-user-alias-list](at-iplanet-am-user-alias-list.html)

* [iplanet-am-user-auth-config](at-iplanet-am-user-auth-config.html)

* [iplanet-am-user-auth-modules](at-iplanet-am-user-auth-modules.html)

* [iplanet-am-user-failure-url](at-iplanet-am-user-failure-url.html)

* [iplanet-am-user-login-status](at-iplanet-am-user-login-status.html)

* [iplanet-am-user-password-reset-force-reset](at-iplanet-am-user-password-reset-force-reset.html)

* [iplanet-am-user-password-reset-options](at-iplanet-am-user-password-reset-options.html)

* [iplanet-am-user-password-reset-question-answer](at-iplanet-am-user-password-reset-question-answer.html)

* [iplanet-am-user-service-status](at-iplanet-am-user-service-status.html)

* [iplanet-am-user-success-url](at-iplanet-am-user-success-url.html)

* [ipNetmaskNumber](at-ipNetmaskNumber.html)

* [ipNetworkNumber](at-ipNetworkNumber.html)

* [ipProtocolNumber](at-ipProtocolNumber.html)

* [ipServicePort](at-ipServicePort.html)

* [ipServiceProtocol](at-ipServiceProtocol.html)

* [ipTnetNumber](at-ipTnetNumber.html)

* [ipTnetTemplateName](at-ipTnetTemplateName.html)

* [isMemberOf](at-isMemberOf.html)

* [janetMailbox](at-janetMailbox.html)

* [javaClassName](at-javaClassName.html)

* [javaClassNames](at-javaClassNames.html)

* [javaCodebase](at-javaCodebase.html)

* [javaDoc](at-javaDoc.html)

* [javaFactory](at-javaFactory.html)

* [javaReferenceAddress](at-javaReferenceAddress.html)

* [javaSerializedData](at-javaSerializedData.html)

* [jpegPhoto](at-jpegPhoto.html)

* [kbaActiveIndex](at-kbaActiveIndex.html)

* [kbaInfo](at-kbaInfo.html)

* [kbaInfoAttempts](at-kbaInfoAttempts.html)

* [knowledgeInformation](at-knowledgeInformation.html)

* [l](at-l.html)

* [labeledURI](at-labeledURI.html)

* [labeledURL](at-labeledURL.html)

* [lastChangeNumber](at-lastChangeNumber.html)

* [lastEmailSent](at-lastEmailSent.html)

* [lastExternalChangelogCookie](at-lastExternalChangelogCookie.html)

* [lastModifiedBy](at-lastModifiedBy.html)

* [lastModifiedTime](at-lastModifiedTime.html)

* [ldapSyntaxes](at-ldapSyntaxes.html)

* [loginShell](at-loginShell.html)

* [macAddress](at-macAddress.html)

* [mail](at-mail.html)

* [mailPreferenceOption](at-mailPreferenceOption.html)

* [manager](at-manager.html)

* [matchingRules](at-matchingRules.html)

* [matchingRuleUse](at-matchingRuleUse.html)

* [mDRecord](at-mDRecord.html)

* [member](at-member.html)

* [memberGid](at-memberGid.html)

* [memberNisNetgroup](at-memberNisNetgroup.html)

* [memberof](at-memberof.html)

* [memberUid](at-memberUid.html)

* [memberURL](at-memberURL.html)

* [mgrpRFC822MailMember](at-mgrpRFC822MailMember.html)

* [mobile](at-mobile.html)

* [modifiersName](at-modifiersName.html)

* [modifyTimestamp](at-modifyTimestamp.html)

* [mxRecord](at-mxRecord.html)

* [name](at-name.html)

* [nameForms](at-nameForms.html)

* [namingContexts](at-namingContexts.html)

* [newRDN](at-newRDN.html)

* [newSuperior](at-newSuperior.html)

* [nisDomain](at-nisDomain.html)

* [nisMapEntry](at-nisMapEntry.html)

* [nisMapName](at-nisMapName.html)

* [nisNetgroupTriple](at-nisNetgroupTriple.html)

* [nisNetIdGroup](at-nisNetIdGroup.html)

* [nisNetIdHost](at-nisNetIdHost.html)

* [nisNetIdUser](at-nisNetIdUser.html)

* [nisplusTimeZone](at-nisplusTimeZone.html)

* [nisPublicKey](at-nisPublicKey.html)

* [nisSecretKey](at-nisSecretKey.html)

* [nsds50ruv](at-nsds50ruv.html)

* [nSRecord](at-nSRecord.html)

* [nsUniqueId](at-nsUniqueId.html)

* [numSubordinates](at-numSubordinates.html)

* [o](at-o.html)

* [oath2faEnabled](at-oath2faEnabled.html)

* [oathDeviceProfiles](at-oathDeviceProfiles.html)

* [objectClass](at-objectClass.html)

* [objectClasses](at-objectClasses.html)

* [objectclassMap](at-objectclassMap.html)

* [oncRpcNumber](at-oncRpcNumber.html)

* [organizationalStatus](at-organizationalStatus.html)

* [otherMailbox](at-otherMailbox.html)

* [ou](at-ou.html)

* [owner](at-owner.html)

* [pager](at-pager.html)

* [personalSignature](at-personalSignature.html)

* [personalTitle](at-personalTitle.html)

* [photo](at-photo.html)

* [physicalDeliveryOfficeName](at-physicalDeliveryOfficeName.html)

* [postalAddress](at-postalAddress.html)

* [postalCode](at-postalCode.html)

* [postOfficeBox](at-postOfficeBox.html)

* [preferredDeliveryMethod](at-preferredDeliveryMethod.html)

* [preferredLanguage](at-preferredLanguage.html)

* [preferredLocale](at-preferredLocale.html)

* [preferredServerList](at-preferredServerList.html)

* [preferredTimeZone](at-preferredTimeZone.html)

* [presentationAddress](at-presentationAddress.html)

* [printer-aliases](at-printer-aliases.html)

* [printer-charset-configured](at-printer-charset-configured.html)

* [printer-charset-supported](at-printer-charset-supported.html)

* [printer-color-supported](at-printer-color-supported.html)

* [printer-compression-supported](at-printer-compression-supported.html)

* [printer-copies-supported](at-printer-copies-supported.html)

* [printer-current-operator](at-printer-current-operator.html)

* [printer-delivery-orientation-supported](at-printer-delivery-orientation-supported.html)

* [printer-document-format-supported](at-printer-document-format-supported.html)

* [printer-finishings-supported](at-printer-finishings-supported.html)

* [printer-generated-natural-language-supported](at-printer-generated-natural-language-supported.html)

* [printer-info](at-printer-info.html)

* [printer-ipp-versions-supported](at-printer-ipp-versions-supported.html)

* [printer-job-k-octets-supported](at-printer-job-k-octets-supported.html)

* [printer-job-priority-supported](at-printer-job-priority-supported.html)

* [printer-location](at-printer-location.html)

* [printer-make-and-model](at-printer-make-and-model.html)

* [printer-media-local-supported](at-printer-media-local-supported.html)

* [printer-media-supported](at-printer-media-supported.html)

* [printer-more-info](at-printer-more-info.html)

* [printer-multiple-document-jobs-supported](at-printer-multiple-document-jobs-supported.html)

* [printer-name](at-printer-name.html)

* [printer-natural-language-configured](at-printer-natural-language-configured.html)

* [printer-number-up-supported](at-printer-number-up-supported.html)

* [printer-output-features-supported](at-printer-output-features-supported.html)

* [printer-pages-per-minute-color](at-printer-pages-per-minute-color.html)

* [printer-pages-per-minute](at-printer-pages-per-minute.html)

* [printer-print-quality-supported](at-printer-print-quality-supported.html)

* [printer-resolution-supported](at-printer-resolution-supported.html)

* [printer-service-person](at-printer-service-person.html)

* [printer-sides-supported](at-printer-sides-supported.html)

* [printer-stacking-order-supported](at-printer-stacking-order-supported.html)

* [printer-uri](at-printer-uri.html)

* [printer-xri-supported](at-printer-xri-supported.html)

* [profileTTL](at-profileTTL.html)

* [protocolInformation](at-protocolInformation.html)

* [push2faEnabled](at-push2faEnabled.html)

* [pushDeviceProfiles](at-pushDeviceProfiles.html)

* [pwdAccountLockedTime](at-pwdAccountLockedTime.html)

* [pwdAllowUserChange](at-pwdAllowUserChange.html)

* [pwdAttribute](at-pwdAttribute.html)

* [pwdChangedTime](at-pwdChangedTime.html)

* [pwdCheckQuality](at-pwdCheckQuality.html)

* [pwdExpireWarning](at-pwdExpireWarning.html)

* [pwdFailureCountInterval](at-pwdFailureCountInterval.html)

* [pwdFailureTime](at-pwdFailureTime.html)

* [pwdGraceAuthNLimit](at-pwdGraceAuthNLimit.html)

* [pwdGraceUseTime](at-pwdGraceUseTime.html)

* [pwdHistory](at-pwdHistory.html)

* [pwdInHistory](at-pwdInHistory.html)

* [pwdLockout](at-pwdLockout.html)

* [pwdLockoutDuration](at-pwdLockoutDuration.html)

* [pwdMaxAge](at-pwdMaxAge.html)

* [pwdMaxFailure](at-pwdMaxFailure.html)

* [pwdMinAge](at-pwdMinAge.html)

* [pwdMinLength](at-pwdMinLength.html)

* [pwdMustChange](at-pwdMustChange.html)

* [pwdPolicySubentry](at-pwdPolicySubentry.html)

* [pwdReset](at-pwdReset.html)

* [pwdSafeModify](at-pwdSafeModify.html)

* [ref](at-ref.html)

* [registeredAddress](at-registeredAddress.html)

* [replicaIdentifier](at-replicaIdentifier.html)

* [replicationCSN](at-replicationCSN.html)

* [retryLimitNodeCount](at-retryLimitNodeCount.html)

* [rfc822mailMember](at-rfc822mailMember.html)

* [roleOccupant](at-roleOccupant.html)

* [roomNumber](at-roomNumber.html)

* [sambaAcctFlags](at-sambaAcctFlags.html)

* [sambaAlgorithmicRidBase](at-sambaAlgorithmicRidBase.html)

* [sambaBadPasswordCount](at-sambaBadPasswordCount.html)

* [sambaBadPasswordTime](at-sambaBadPasswordTime.html)

* [sambaBoolOption](at-sambaBoolOption.html)

* [sambaDomainName](at-sambaDomainName.html)

* [sambaForceLogoff](at-sambaForceLogoff.html)

* [sambaGroupType](at-sambaGroupType.html)

* [sambaHomeDrive](at-sambaHomeDrive.html)

* [sambaHomePath](at-sambaHomePath.html)

* [sambaIntegerOption](at-sambaIntegerOption.html)

* [sambaKickoffTime](at-sambaKickoffTime.html)

* [sambaLMPassword](at-sambaLMPassword.html)

* [sambaLockoutDuration](at-sambaLockoutDuration.html)

* [sambaLockoutObservationWindow](at-sambaLockoutObservationWindow.html)

* [sambaLockoutThreshold](at-sambaLockoutThreshold.html)

* [sambaLogoffTime](at-sambaLogoffTime.html)

* [sambaLogonHours](at-sambaLogonHours.html)

* [sambaLogonScript](at-sambaLogonScript.html)

* [sambaLogonTime](at-sambaLogonTime.html)

* [sambaLogonToChgPwd](at-sambaLogonToChgPwd.html)

* [sambaMaxPwdAge](at-sambaMaxPwdAge.html)

* [sambaMinPwdAge](at-sambaMinPwdAge.html)

* [sambaMinPwdLength](at-sambaMinPwdLength.html)

* [sambaMungedDial](at-sambaMungedDial.html)

* [sambaNextGroupRid](at-sambaNextGroupRid.html)

* [sambaNextRid](at-sambaNextRid.html)

* [sambaNextUserRid](at-sambaNextUserRid.html)

* [sambaNTPassword](at-sambaNTPassword.html)

* [sambaOptionName](at-sambaOptionName.html)

* [sambaPasswordHistory](at-sambaPasswordHistory.html)

* [sambaPrimaryGroupSID](at-sambaPrimaryGroupSID.html)

* [sambaPrivilegeList](at-sambaPrivilegeList.html)

* [sambaProfilePath](at-sambaProfilePath.html)

* [sambaPwdCanChange](at-sambaPwdCanChange.html)

* [sambaPwdHistoryLength](at-sambaPwdHistoryLength.html)

* [sambaPwdLastSet](at-sambaPwdLastSet.html)

* [sambaPwdMustChange](at-sambaPwdMustChange.html)

* [sambaRefuseMachinePwdChange](at-sambaRefuseMachinePwdChange.html)

* [sambaShareName](at-sambaShareName.html)

* [sambaSID](at-sambaSID.html)

* [sambaSIDList](at-sambaSIDList.html)

* [sambaStringListOption](at-sambaStringListOption.html)

* [sambaStringOption](at-sambaStringOption.html)

* [sambaTrustFlags](at-sambaTrustFlags.html)

* [sambaUserWorkstations](at-sambaUserWorkstations.html)

* [searchGuide](at-searchGuide.html)

* [searchTimeLimit](at-searchTimeLimit.html)

* [secretary](at-secretary.html)

* [seeAlso](at-seeAlso.html)

* [serialNumber](at-serialNumber.html)

* [service-advert-attribute-authenticator](at-service-advert-attribute-authenticator.html)

* [service-advert-scopes](at-service-advert-scopes.html)

* [service-advert-service-type](at-service-advert-service-type.html)

* [service-advert-url-authenticator](at-service-advert-url-authenticator.html)

* [serviceAuthenticationMethod](at-serviceAuthenticationMethod.html)

* [serviceCredentialLevel](at-serviceCredentialLevel.html)

* [serviceSearchDescriptor](at-serviceSearchDescriptor.html)

* [shadowExpire](at-shadowExpire.html)

* [shadowFlag](at-shadowFlag.html)

* [shadowInactive](at-shadowInactive.html)

* [shadowLastChange](at-shadowLastChange.html)

* [shadowMax](at-shadowMax.html)

* [shadowMin](at-shadowMin.html)

* [shadowWarning](at-shadowWarning.html)

* [singleLevelQuality](at-singleLevelQuality.html)

* [sn](at-sn.html)

* [sOARecord](at-sOARecord.html)

* [SolarisAttrKeyValue](at-SolarisAttrKeyValue.html)

* [SolarisAttrLongDesc](at-SolarisAttrLongDesc.html)

* [SolarisAttrReserved1](at-SolarisAttrReserved1.html)

* [SolarisAttrReserved2](at-SolarisAttrReserved2.html)

* [SolarisAttrShortDesc](at-SolarisAttrShortDesc.html)

* [SolarisAuditAlways](at-SolarisAuditAlways.html)

* [SolarisAuditNever](at-SolarisAuditNever.html)

* [SolarisAuthMethod](at-SolarisAuthMethod.html)

* [SolarisBindDN](at-SolarisBindDN.html)

* [SolarisBindPassword](at-SolarisBindPassword.html)

* [SolarisBindTimeLimit](at-SolarisBindTimeLimit.html)

* [SolarisCacheTTL](at-SolarisCacheTTL.html)

* [SolarisCertificatePassword](at-SolarisCertificatePassword.html)

* [SolarisCertificatePath](at-SolarisCertificatePath.html)

* [SolarisDataSearchDN](at-SolarisDataSearchDN.html)

* [SolarisKernelSecurityPolicy](at-SolarisKernelSecurityPolicy.html)

* [SolarisLDAPServers](at-SolarisLDAPServers.html)

* [SolarisPreferredServer](at-SolarisPreferredServer.html)

* [SolarisPreferredServerOnly](at-SolarisPreferredServerOnly.html)

* [SolarisProfileId](at-SolarisProfileId.html)

* [SolarisProfileType](at-SolarisProfileType.html)

* [SolarisProjectAttr](at-SolarisProjectAttr.html)

* [SolarisProjectID](at-SolarisProjectID.html)

* [SolarisProjectName](at-SolarisProjectName.html)

* [SolarisSearchBaseDN](at-SolarisSearchBaseDN.html)

* [SolarisSearchReferral](at-SolarisSearchReferral.html)

* [SolarisSearchScope](at-SolarisSearchScope.html)

* [SolarisSearchTimeLimit](at-SolarisSearchTimeLimit.html)

* [SolarisTransportSecurity](at-SolarisTransportSecurity.html)

* [SolarisUserQualifier](at-SolarisUserQualifier.html)

* [st](at-st.html)

* [street](at-street.html)

* [structuralObjectClass](at-structuralObjectClass.html)

* [subschemaSubentry](at-subschemaSubentry.html)

* [subtreeMaximumQuality](at-subtreeMaximumQuality.html)

* [subtreeMinimumQuality](at-subtreeMinimumQuality.html)

* [subtreeSpecification](at-subtreeSpecification.html)

* [sun-fm-saml2-nameid-info](at-sun-fm-saml2-nameid-info.html)

* [sun-fm-saml2-nameid-infokey](at-sun-fm-saml2-nameid-infokey.html)

* [sun-printer-bsdaddr](at-sun-printer-bsdaddr.html)

* [sun-printer-kvp](at-sun-printer-kvp.html)

* [sunAMAuthInvalidAttemptsData](at-sunAMAuthInvalidAttemptsData.html)

* [sunIdentityMSISDNNumber](at-sunIdentityMSISDNNumber.html)

* [sunKeyValue](at-sunKeyValue.html)

* [sunPluginSchema](at-sunPluginSchema.html)

* [sunserviceID](at-sunserviceID.html)

* [sunServiceSchema](at-sunServiceSchema.html)

* [sunsmspriority](at-sunsmspriority.html)

* [sunxmlKeyValue](at-sunxmlKeyValue.html)

* [supportedAlgorithms](at-supportedAlgorithms.html)

* [supportedApplicationContext](at-supportedApplicationContext.html)

* [supportedAuthPasswordSchemes](at-supportedAuthPasswordSchemes.html)

* [supportedControl](at-supportedControl.html)

* [supportedExtension](at-supportedExtension.html)

* [supportedFeatures](at-supportedFeatures.html)

* [supportedLDAPVersion](at-supportedLDAPVersion.html)

* [supportedSASLMechanisms](at-supportedSASLMechanisms.html)

* [supportedTLSCiphers](at-supportedTLSCiphers.html)

* [supportedTLSProtocols](at-supportedTLSProtocols.html)

* [targetDN](at-targetDN.html)

* [targetEntryUUID](at-targetEntryUUID.html)

* [telephoneNumber](at-telephoneNumber.html)

* [teletexTerminalIdentifier](at-teletexTerminalIdentifier.html)

* [telexNumber](at-telexNumber.html)

* [template-major-version-number](at-template-major-version-number.html)

* [template-minor-version-number](at-template-minor-version-number.html)

* [template-url-syntax](at-template-url-syntax.html)

* [textEncodedORAddress](at-textEncodedORAddress.html)

* [title](at-title.html)

* [uddiAccessPoint](at-uddiAccessPoint.html)

* [uddiAddressLine](at-uddiAddressLine.html)

* [uddiAuthorizedName](at-uddiAuthorizedName.html)

* [uddiBindingKey](at-uddiBindingKey.html)

* [uddiBusinessKey](at-uddiBusinessKey.html)

* [uddiCategoryBag](at-uddiCategoryBag.html)

* [uddiDescription](at-uddiDescription.html)

* [uddiDiscoveryURLs](at-uddiDiscoveryURLs.html)

* [uddiEMail](at-uddiEMail.html)

* [uddiFromKey](at-uddiFromKey.html)

* [uddiHostingRedirector](at-uddiHostingRedirector.html)

* [uddiIdentifierBag](at-uddiIdentifierBag.html)

* [uddiInstanceDescription](at-uddiInstanceDescription.html)

* [uddiInstanceParms](at-uddiInstanceParms.html)

* [uddiIsHidden](at-uddiIsHidden.html)

* [uddiIsProjection](at-uddiIsProjection.html)

* [uddiKeyedReference](at-uddiKeyedReference.html)

* [uddiLang](at-uddiLang.html)

* [uddiName](at-uddiName.html)

* [uddiOperator](at-uddiOperator.html)

* [uddiOverviewDescription](at-uddiOverviewDescription.html)

* [uddiOverviewURL](at-uddiOverviewURL.html)

* [uddiPersonName](at-uddiPersonName.html)

* [uddiPhone](at-uddiPhone.html)

* [uddiServiceKey](at-uddiServiceKey.html)

* [uddiSortCode](at-uddiSortCode.html)

* [uddiTModelKey](at-uddiTModelKey.html)

* [uddiToKey](at-uddiToKey.html)

* [uddiUseType](at-uddiUseType.html)

* [uddiUUID](at-uddiUUID.html)

* [uddiv3BindingKey](at-uddiv3BindingKey.html)

* [uddiv3BriefResponse](at-uddiv3BriefResponse.html)

* [uddiv3BusinessKey](at-uddiv3BusinessKey.html)

* [uddiv3DigitalSignature](at-uddiv3DigitalSignature.html)

* [uddiv3EntityCreationTime](at-uddiv3EntityCreationTime.html)

* [uddiv3EntityDeletionTime](at-uddiv3EntityDeletionTime.html)

* [uddiv3EntityKey](at-uddiv3EntityKey.html)

* [uddiv3EntityModificationTime](at-uddiv3EntityModificationTime.html)

* [uddiv3ExpiresAfter](at-uddiv3ExpiresAfter.html)

* [uddiv3MaxEntities](at-uddiv3MaxEntities.html)

* [uddiv3NodeId](at-uddiv3NodeId.html)

* [uddiv3NotificationInterval](at-uddiv3NotificationInterval.html)

* [uddiv3ServiceKey](at-uddiv3ServiceKey.html)

* [uddiv3SubscriptionFilter](at-uddiv3SubscriptionFilter.html)

* [uddiv3SubscriptionKey](at-uddiv3SubscriptionKey.html)

* [uddiv3TModelKey](at-uddiv3TModelKey.html)

* [uid](at-uid.html)

* [uidNumber](at-uidNumber.html)

* [uniqueIdentifier](at-uniqueIdentifier.html)

* [uniqueMember](at-uniqueMember.html)

* [userCertificate](at-userCertificate.html)

* [userClass](at-userClass.html)

* [userPassword](at-userPassword.html)

* [userPKCS12](at-userPKCS12.html)

* [userSMIMECertificate](at-userSMIMECertificate.html)

* [vendorName](at-vendorName.html)

* [vendorVersion](at-vendorVersion.html)

* [webauthnDeviceProfiles](at-webauthnDeviceProfiles.html)

* [winAccountName](at-winAccountName.html)

* [x121Address](at-x121Address.html)

* [x500UniqueIdentifier](at-x500UniqueIdentifier.html)

---

---
title: attributeMap
description: OID
component: pingds
version: 8.1
page_id: pingds:schemaref:at-attributeMap
canonical_url: https://docs.pingidentity.com/pingds/8.1/schemaref/at-attributeMap.html
llms_txt: https://docs.pingidentity.com/pingds/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
---

# attributeMap

|                             |                                                                        |
| --------------------------- | ---------------------------------------------------------------------- |
| *OID*                       | 1.3.6.1.4.1.11.1.3.1.1.9                                               |
| *Names*                     | attributeMap                                                           |
| *Description*               | Attribute mappings used, required, or supported by an agent or service |
| *Syntax*                    | [IA5String](s-IA5String.html)                                          |
| *Equality matching rule*    | [caseIgnoreIA5Match](mr-caseIgnoreIA5Match.html)                       |
| *Ordering matching rule*    | [caseIgnoreOrderingMatch](mr-caseIgnoreOrderingMatch.html)             |
| *Substring matching rule*   | [caseIgnoreSubstringsMatch](mr-caseIgnoreSubstringsMatch.html)         |
| *Single value*              | false: multiple values allowed                                         |
| *User modification allowed* | true                                                                   |
| *Usage*                     | userApplications                                                       |
| *Origin*                    | [RFC 4876](https://datatracker.ietf.org/doc/html/rfc4876)              |
| *Schema file*               | 05-rfc4876.ldif                                                        |
| *Used by*                   | [DUAConfigProfile](oc-DUAConfigProfile.html)                           |