---
title: AcceptTermsAndConditions
description: Resource path:
component: pingam
version: 8.1
page_id: pingam:entity-reference:sec-amster-entity-accepttermsandconditions
canonical_url: https://docs.pingidentity.com/pingam/8.1/entity-reference/sec-amster-entity-accepttermsandconditions.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  sec-amster-entity-accepttermsandconditions-realm-ops: Realm Operations
  sec-amster-entity-accepttermsandconditions-realm-ops-create: create
  sec-amster-entity-accepttermsandconditions-realm-ops-delete: delete
  sec-amster-entity-accepttermsandconditions-realm-ops-gettype: getType
  sec-amster-entity-accepttermsandconditions-realm-ops-getupgradedconfig: getUpgradedConfig
  sec-amster-entity-accepttermsandconditions-realm-ops-query: query
  sec-amster-entity-accepttermsandconditions-realm-ops-read: read
  sec-amster-entity-accepttermsandconditions-realm-ops-update: update
  sec-amster-entity-accepttermsandconditions-realm-ops-versioninfo: versionInfo
---

# AcceptTermsAndConditions

## Realm Operations

Resource path:

```
/realm-config/authentication/authenticationtrees/nodes/AcceptTermsAndConditionsNode/1.0
```

Resource version: `3.0`

### create

**Usage**

```
am> create AcceptTermsAndConditions --realm Realm --id id --body body
```

**Parameters**

* *\--id*

  The unique identifier for the resource.

* *\--body*

  The resource in JSON format, described by the following JSON schema:

  ```json
  {
    "type" : "object",
    "required" : [ ]
  }
  ```

### delete

**Usage**

```
am> delete AcceptTermsAndConditions --realm Realm --id id
```

**Parameters**

* *\--id*

  The unique identifier for the resource.

### getType

List information related to the node such as a name, description, tags and metadata.

**Usage**

```
am> action AcceptTermsAndConditions --realm Realm --actionName getType
```

### getUpgradedConfig

Get the upgraded configuration for the node type.

**Usage**

```
am> action AcceptTermsAndConditions --realm Realm --body body --actionName getUpgradedConfig --targetVersion targetVersion
```

**Parameters**

* *\--body*

  The resource in JSON format, described by the following JSON schema:

  ```json
  {
    "type" : "object",
    "title" : "The current configuration of the node type."
  }
  ```

* *\--targetVersion*

  \=== listOutcomes

List the available outcomes for the node type.

**Usage**

```
am> action AcceptTermsAndConditions --realm Realm --body body --actionName listOutcomes
```

**Parameters**

* *\--body*

  The resource in JSON format, described by the following JSON schema:

  ```json
  {
    "description" : "Some configuration of the node. This does not need to be complete against the configuration schema.",
    "type" : "object",
    "title" : "Node configuration"
  }
  ```

### query

Get the full list of instances of this collection. This query only supports `_queryFilter=true` filter.

**Usage**

```
am> query AcceptTermsAndConditions --realm Realm --filter filter
```

**Parameters**

* *\--filter*

  A CREST formatted query filter, where "true" will query all.

### read

**Usage**

```
am> read AcceptTermsAndConditions --realm Realm --id id
```

**Parameters**

* *\--id*

  The unique identifier for the resource.

### update

**Usage**

```
am> update AcceptTermsAndConditions --realm Realm --id id --body body
```

**Parameters**

* *\--id*

  The unique identifier for the resource.

* *\--body*

  The resource in JSON format, described by the following JSON schema:

  ```json
  {
    "type" : "object",
    "required" : [ ]
  }
  ```

### versionInfo

List the versions available for the node type.

**Usage**

```
am> action AcceptTermsAndConditions --realm Realm --actionName versionInfo
```

---

---
title: AcceptTermsAndConditionsCollection
description: Base resource for the AcceptTermsAndConditionsNode
component: pingam
version: 8.1
page_id: pingam:entity-reference:sec-amster-entity-accepttermsandconditionscollection
canonical_url: https://docs.pingidentity.com/pingam/8.1/entity-reference/sec-amster-entity-accepttermsandconditionscollection.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  sec-amster-entity-accepttermsandconditionscollection-realm-ops: Realm Operations
  sec-amster-entity-accepttermsandconditionscollection-realm-ops-getalltypes: getAllTypes
  sec-amster-entity-accepttermsandconditionscollection-realm-ops-getcreatabletypes: getCreatableTypes
  sec-amster-entity-accepttermsandconditionscollection-realm-ops-getlatesttype: getLatestType
  sec-amster-entity-accepttermsandconditionscollection-realm-ops-gettype: getType
  sec-amster-entity-accepttermsandconditionscollection-realm-ops-nextdescendents: nextdescendents
  sec-amster-entity-accepttermsandconditionscollection-realm-ops-versioninfo: versionInfo
---

# AcceptTermsAndConditionsCollection

## Realm Operations

Base resource for the AcceptTermsAndConditionsNode

Resource path:

```
/realm-config/authentication/authenticationtrees/nodes/AcceptTermsAndConditionsNode
```

Resource version: `3.0`

### getAllTypes

Obtain the collection of all secondary configuration types related to the resource.

**Usage**

```
am> action AcceptTermsAndConditionsCollection --realm Realm --actionName getAllTypes
```

### getCreatableTypes

Obtain the collection of secondary configuration types that have yet to be added to the resource.

**Usage**

```
am> action AcceptTermsAndConditionsCollection --realm Realm --actionName getCreatableTypes
```

### getLatestType

getLatestType.description

**Usage**

```
am> action AcceptTermsAndConditionsCollection --realm Realm --actionName getLatestType
```

### getType

List information related to the node such as a name, description, tags and metadata.

**Usage**

```
am> action AcceptTermsAndConditionsCollection --realm Realm --actionName getType
```

### nextdescendents

Obtain the collection of secondary configuration instances that have been added to the resource.

**Usage**

```
am> action AcceptTermsAndConditionsCollection --realm Realm --actionName nextdescendents
```

### versionInfo

List the versions available for the node type.

**Usage**

```
am> action AcceptTermsAndConditionsCollection --realm Realm --actionName versionInfo
```

---

---
title: AccountActiveCheck
description: Resource path:
component: pingam
version: 8.1
page_id: pingam:entity-reference:sec-amster-entity-accountactivecheck
canonical_url: https://docs.pingidentity.com/pingam/8.1/entity-reference/sec-amster-entity-accountactivecheck.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  sec-amster-entity-accountactivecheck-realm-ops: Realm Operations
  sec-amster-entity-accountactivecheck-realm-ops-create: create
  sec-amster-entity-accountactivecheck-realm-ops-delete: delete
  sec-amster-entity-accountactivecheck-realm-ops-getalltypes: getAllTypes
  sec-amster-entity-accountactivecheck-realm-ops-getcreatabletypes: getCreatableTypes
  sec-amster-entity-accountactivecheck-realm-ops-nextdescendents: nextdescendents
  sec-amster-entity-accountactivecheck-realm-ops-query: query
  sec-amster-entity-accountactivecheck-realm-ops-read: read
  sec-amster-entity-accountactivecheck-realm-ops-update: update
  sec-amster-entity-accountactivecheck-global-ops: Global Operations
  sec-amster-entity-accountactivecheck-global-ops-getalltypes: getAllTypes
  sec-amster-entity-accountactivecheck-global-ops-getcreatabletypes: getCreatableTypes
  sec-amster-entity-accountactivecheck-global-ops-nextdescendents: nextdescendents
  sec-amster-entity-accountactivecheck-global-ops-read: read
  sec-amster-entity-accountactivecheck-global-ops-update: update
---

# AccountActiveCheck

## Realm Operations

Resource path:

```
/realm-config/authentication/modules/accountactivecheck
```

Resource version: `0.0`

### create

**Usage**

```
am> create AccountActiveCheck --realm Realm --id id --body body
```

**Parameters**

* *\--id*

  The unique identifier for the resource.

* *\--body*

  The resource in JSON format, described by the following JSON schema:

  ```json
  {
    "type" : "object",
    "properties" : {
      "authenticationLevel" : {
        "title" : "Authentication Level",
        "description" : "The authentication level associated with this module.<br><br>Each authentication module has an authentication level that can be used to indicate the level of security associated with the module; 0 is the lowest (and the default).",
        "propertyOrder" : null,
        "required" : true,
        "type" : "integer",
        "exampleValue" : ""
      }
    }
  }
  ```

### delete

**Usage**

```
am> delete AccountActiveCheck --realm Realm --id id
```

**Parameters**

* *\--id*

  The unique identifier for the resource.

### getAllTypes

Obtain the collection of all secondary configuration types related to the resource.

**Usage**

```
am> action AccountActiveCheck --realm Realm --actionName getAllTypes
```

### getCreatableTypes

Obtain the collection of secondary configuration types that have yet to be added to the resource.

**Usage**

```
am> action AccountActiveCheck --realm Realm --actionName getCreatableTypes
```

### nextdescendents

Obtain the collection of secondary configuration instances that have been added to the resource.

**Usage**

```
am> action AccountActiveCheck --realm Realm --actionName nextdescendents
```

### query

Get the full list of instances of this collection. This query only supports `_queryFilter=true` filter.

**Usage**

```
am> query AccountActiveCheck --realm Realm --filter filter
```

**Parameters**

* *\--filter*

  A CREST formatted query filter, where "true" will query all.

### read

**Usage**

```
am> read AccountActiveCheck --realm Realm --id id
```

**Parameters**

* *\--id*

  The unique identifier for the resource.

### update

**Usage**

```
am> update AccountActiveCheck --realm Realm --id id --body body
```

**Parameters**

* *\--id*

  The unique identifier for the resource.

* *\--body*

  The resource in JSON format, described by the following JSON schema:

  ```json
  {
    "type" : "object",
    "properties" : {
      "authenticationLevel" : {
        "title" : "Authentication Level",
        "description" : "The authentication level associated with this module.<br><br>Each authentication module has an authentication level that can be used to indicate the level of security associated with the module; 0 is the lowest (and the default).",
        "propertyOrder" : null,
        "required" : true,
        "type" : "integer",
        "exampleValue" : ""
      }
    }
  }
  ```

## Global Operations

Resource path:

```
/global-config/authentication/modules/accountactivecheck
```

Resource version: `1.0`

### getAllTypes

Obtain the collection of all secondary configuration types related to the resource.

**Usage**

```
am> action AccountActiveCheck --global --actionName getAllTypes
```

### getCreatableTypes

Obtain the collection of secondary configuration types that have yet to be added to the resource.

**Usage**

```
am> action AccountActiveCheck --global --actionName getCreatableTypes
```

### nextdescendents

Obtain the collection of secondary configuration instances that have been added to the resource.

**Usage**

```
am> action AccountActiveCheck --global --actionName nextdescendents
```

### read

**Usage**

```
am> read AccountActiveCheck --global
```

### update

**Usage**

```
am> update AccountActiveCheck --global --body body
```

**Parameters**

* *\--body*

  The resource in JSON format, described by the following JSON schema:

  ```json
  {
    "type" : "object",
    "properties" : {
      "defaults" : {
        "properties" : {
          "authenticationLevel" : {
            "title" : "Authentication Level",
            "description" : "The authentication level associated with this module.<br><br>Each authentication module has an authentication level that can be used to indicate the level of security associated with the module; 0 is the lowest (and the default).",
            "propertyOrder" : null,
            "required" : true,
            "type" : "integer",
            "exampleValue" : ""
          }
        },
        "type" : "object",
        "title" : "Realm Defaults"
      }
    }
  }
  ```

---

---
title: AccountActiveDecision
description: Resource path:
component: pingam
version: 8.1
page_id: pingam:entity-reference:sec-amster-entity-accountactivedecision
canonical_url: https://docs.pingidentity.com/pingam/8.1/entity-reference/sec-amster-entity-accountactivedecision.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  sec-amster-entity-accountactivedecision-realm-ops: Realm Operations
  sec-amster-entity-accountactivedecision-realm-ops-create: create
  sec-amster-entity-accountactivedecision-realm-ops-delete: delete
  sec-amster-entity-accountactivedecision-realm-ops-gettype: getType
  sec-amster-entity-accountactivedecision-realm-ops-getupgradedconfig: getUpgradedConfig
  sec-amster-entity-accountactivedecision-realm-ops-query: query
  sec-amster-entity-accountactivedecision-realm-ops-read: read
  sec-amster-entity-accountactivedecision-realm-ops-update: update
  sec-amster-entity-accountactivedecision-realm-ops-versioninfo: versionInfo
---

# AccountActiveDecision

## Realm Operations

Resource path:

```
/realm-config/authentication/authenticationtrees/nodes/AccountActiveDecisionNode/1.0
```

Resource version: `3.0`

### create

**Usage**

```
am> create AccountActiveDecision --realm Realm --id id --body body
```

**Parameters**

* *\--id*

  The unique identifier for the resource.

* *\--body*

  The resource in JSON format, described by the following JSON schema:

  ```json
  {
    "type" : "object",
    "required" : [ ]
  }
  ```

### delete

**Usage**

```
am> delete AccountActiveDecision --realm Realm --id id
```

**Parameters**

* *\--id*

  The unique identifier for the resource.

### getType

List information related to the node such as a name, description, tags and metadata.

**Usage**

```
am> action AccountActiveDecision --realm Realm --actionName getType
```

### getUpgradedConfig

Get the upgraded configuration for the node type.

**Usage**

```
am> action AccountActiveDecision --realm Realm --body body --actionName getUpgradedConfig --targetVersion targetVersion
```

**Parameters**

* *\--body*

  The resource in JSON format, described by the following JSON schema:

  ```json
  {
    "type" : "object",
    "title" : "The current configuration of the node type."
  }
  ```

* *\--targetVersion*

  \=== listOutcomes

List the available outcomes for the node type.

**Usage**

```
am> action AccountActiveDecision --realm Realm --body body --actionName listOutcomes
```

**Parameters**

* *\--body*

  The resource in JSON format, described by the following JSON schema:

  ```json
  {
    "description" : "Some configuration of the node. This does not need to be complete against the configuration schema.",
    "type" : "object",
    "title" : "Node configuration"
  }
  ```

### query

Get the full list of instances of this collection. This query only supports `_queryFilter=true` filter.

**Usage**

```
am> query AccountActiveDecision --realm Realm --filter filter
```

**Parameters**

* *\--filter*

  A CREST formatted query filter, where "true" will query all.

### read

**Usage**

```
am> read AccountActiveDecision --realm Realm --id id
```

**Parameters**

* *\--id*

  The unique identifier for the resource.

### update

**Usage**

```
am> update AccountActiveDecision --realm Realm --id id --body body
```

**Parameters**

* *\--id*

  The unique identifier for the resource.

* *\--body*

  The resource in JSON format, described by the following JSON schema:

  ```json
  {
    "type" : "object",
    "required" : [ ]
  }
  ```

### versionInfo

List the versions available for the node type.

**Usage**

```
am> action AccountActiveDecision --realm Realm --actionName versionInfo
```

---

---
title: AccountActiveDecisionCollection
description: Base resource for the AccountActiveDecisionNode
component: pingam
version: 8.1
page_id: pingam:entity-reference:sec-amster-entity-accountactivedecisioncollection
canonical_url: https://docs.pingidentity.com/pingam/8.1/entity-reference/sec-amster-entity-accountactivedecisioncollection.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  sec-amster-entity-accountactivedecisioncollection-realm-ops: Realm Operations
  sec-amster-entity-accountactivedecisioncollection-realm-ops-getalltypes: getAllTypes
  sec-amster-entity-accountactivedecisioncollection-realm-ops-getcreatabletypes: getCreatableTypes
  sec-amster-entity-accountactivedecisioncollection-realm-ops-getlatesttype: getLatestType
  sec-amster-entity-accountactivedecisioncollection-realm-ops-gettype: getType
  sec-amster-entity-accountactivedecisioncollection-realm-ops-nextdescendents: nextdescendents
  sec-amster-entity-accountactivedecisioncollection-realm-ops-versioninfo: versionInfo
---

# AccountActiveDecisionCollection

## Realm Operations

Base resource for the AccountActiveDecisionNode

Resource path:

```
/realm-config/authentication/authenticationtrees/nodes/AccountActiveDecisionNode
```

Resource version: `3.0`

### getAllTypes

Obtain the collection of all secondary configuration types related to the resource.

**Usage**

```
am> action AccountActiveDecisionCollection --realm Realm --actionName getAllTypes
```

### getCreatableTypes

Obtain the collection of secondary configuration types that have yet to be added to the resource.

**Usage**

```
am> action AccountActiveDecisionCollection --realm Realm --actionName getCreatableTypes
```

### getLatestType

getLatestType.description

**Usage**

```
am> action AccountActiveDecisionCollection --realm Realm --actionName getLatestType
```

### getType

List information related to the node such as a name, description, tags and metadata.

**Usage**

```
am> action AccountActiveDecisionCollection --realm Realm --actionName getType
```

### nextdescendents

Obtain the collection of secondary configuration instances that have been added to the resource.

**Usage**

```
am> action AccountActiveDecisionCollection --realm Realm --actionName nextdescendents
```

### versionInfo

List the versions available for the node type.

**Usage**

```
am> action AccountActiveDecisionCollection --realm Realm --actionName versionInfo
```

---

---
title: AccountLockout
description: Resource path:
component: pingam
version: 8.1
page_id: pingam:entity-reference:sec-amster-entity-accountlockout
canonical_url: https://docs.pingidentity.com/pingam/8.1/entity-reference/sec-amster-entity-accountlockout.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  sec-amster-entity-accountlockout-realm-ops: Realm Operations
  sec-amster-entity-accountlockout-realm-ops-create: create
  sec-amster-entity-accountlockout-realm-ops-delete: delete
  sec-amster-entity-accountlockout-realm-ops-gettype: getType
  sec-amster-entity-accountlockout-realm-ops-getupgradedconfig: getUpgradedConfig
  sec-amster-entity-accountlockout-realm-ops-query: query
  sec-amster-entity-accountlockout-realm-ops-read: read
  sec-amster-entity-accountlockout-realm-ops-update: update
  sec-amster-entity-accountlockout-realm-ops-versioninfo: versionInfo
---

# AccountLockout

## Realm Operations

Resource path:

```
/realm-config/authentication/authenticationtrees/nodes/AccountLockoutNode/1.0
```

Resource version: `3.0`

### create

**Usage**

```
am> create AccountLockout --realm Realm --id id --body body
```

**Parameters**

* *\--id*

  The unique identifier for the resource.

* *\--body*

  The resource in JSON format, described by the following JSON schema:

  ```json
  {
    "type" : "object",
    "properties" : {
      "lockAction" : {
        "title" : "Lock Action",
        "description" : "If the action is set to LOCK, the node will lock the account.",
        "propertyOrder" : 100,
        "type" : "string",
        "exampleValue" : ""
      }
    },
    "required" : [ "lockAction" ]
  }
  ```

### delete

**Usage**

```
am> delete AccountLockout --realm Realm --id id
```

**Parameters**

* *\--id*

  The unique identifier for the resource.

### getType

List information related to the node such as a name, description, tags and metadata.

**Usage**

```
am> action AccountLockout --realm Realm --actionName getType
```

### getUpgradedConfig

Get the upgraded configuration for the node type.

**Usage**

```
am> action AccountLockout --realm Realm --body body --actionName getUpgradedConfig --targetVersion targetVersion
```

**Parameters**

* *\--body*

  The resource in JSON format, described by the following JSON schema:

  ```json
  {
    "type" : "object",
    "title" : "The current configuration of the node type."
  }
  ```

* *\--targetVersion*

  \=== listOutcomes

List the available outcomes for the node type.

**Usage**

```
am> action AccountLockout --realm Realm --body body --actionName listOutcomes
```

**Parameters**

* *\--body*

  The resource in JSON format, described by the following JSON schema:

  ```json
  {
    "description" : "Some configuration of the node. This does not need to be complete against the configuration schema.",
    "type" : "object",
    "title" : "Node configuration"
  }
  ```

### query

Get the full list of instances of this collection. This query only supports `_queryFilter=true` filter.

**Usage**

```
am> query AccountLockout --realm Realm --filter filter
```

**Parameters**

* *\--filter*

  A CREST formatted query filter, where "true" will query all.

### read

**Usage**

```
am> read AccountLockout --realm Realm --id id
```

**Parameters**

* *\--id*

  The unique identifier for the resource.

### update

**Usage**

```
am> update AccountLockout --realm Realm --id id --body body
```

**Parameters**

* *\--id*

  The unique identifier for the resource.

* *\--body*

  The resource in JSON format, described by the following JSON schema:

  ```json
  {
    "type" : "object",
    "properties" : {
      "lockAction" : {
        "title" : "Lock Action",
        "description" : "If the action is set to LOCK, the node will lock the account.",
        "propertyOrder" : 100,
        "type" : "string",
        "exampleValue" : ""
      }
    },
    "required" : [ "lockAction" ]
  }
  ```

### versionInfo

List the versions available for the node type.

**Usage**

```
am> action AccountLockout --realm Realm --actionName versionInfo
```

---

---
title: AccountLockoutCollection
description: Base resource for the AccountLockoutNode
component: pingam
version: 8.1
page_id: pingam:entity-reference:sec-amster-entity-accountlockoutcollection
canonical_url: https://docs.pingidentity.com/pingam/8.1/entity-reference/sec-amster-entity-accountlockoutcollection.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  sec-amster-entity-accountlockoutcollection-realm-ops: Realm Operations
  sec-amster-entity-accountlockoutcollection-realm-ops-getalltypes: getAllTypes
  sec-amster-entity-accountlockoutcollection-realm-ops-getcreatabletypes: getCreatableTypes
  sec-amster-entity-accountlockoutcollection-realm-ops-getlatesttype: getLatestType
  sec-amster-entity-accountlockoutcollection-realm-ops-gettype: getType
  sec-amster-entity-accountlockoutcollection-realm-ops-nextdescendents: nextdescendents
  sec-amster-entity-accountlockoutcollection-realm-ops-versioninfo: versionInfo
---

# AccountLockoutCollection

## Realm Operations

Base resource for the AccountLockoutNode

Resource path:

```
/realm-config/authentication/authenticationtrees/nodes/AccountLockoutNode
```

Resource version: `3.0`

### getAllTypes

Obtain the collection of all secondary configuration types related to the resource.

**Usage**

```
am> action AccountLockoutCollection --realm Realm --actionName getAllTypes
```

### getCreatableTypes

Obtain the collection of secondary configuration types that have yet to be added to the resource.

**Usage**

```
am> action AccountLockoutCollection --realm Realm --actionName getCreatableTypes
```

### getLatestType

getLatestType.description

**Usage**

```
am> action AccountLockoutCollection --realm Realm --actionName getLatestType
```

### getType

List information related to the node such as a name, description, tags and metadata.

**Usage**

```
am> action AccountLockoutCollection --realm Realm --actionName getType
```

### nextdescendents

Obtain the collection of secondary configuration instances that have been added to the resource.

**Usage**

```
am> action AccountLockoutCollection --realm Realm --actionName nextdescendents
```

### versionInfo

List the versions available for the node type.

**Usage**

```
am> action AccountLockoutCollection --realm Realm --actionName versionInfo
```

---

---
title: ActiveDirectory
description: Resource path:
component: pingam
version: 8.1
page_id: pingam:entity-reference:sec-amster-entity-activedirectory
canonical_url: https://docs.pingidentity.com/pingam/8.1/entity-reference/sec-amster-entity-activedirectory.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  sec-amster-entity-activedirectory-realm-ops: Realm Operations
  sec-amster-entity-activedirectory-realm-ops-create: create
  sec-amster-entity-activedirectory-realm-ops-delete: delete
  sec-amster-entity-activedirectory-realm-ops-getalltypes: getAllTypes
  sec-amster-entity-activedirectory-realm-ops-getcreatabletypes: getCreatableTypes
  sec-amster-entity-activedirectory-realm-ops-nextdescendents: nextdescendents
  sec-amster-entity-activedirectory-realm-ops-query: query
  sec-amster-entity-activedirectory-realm-ops-read: read
  sec-amster-entity-activedirectory-realm-ops-update: update
---

# ActiveDirectory

## Realm Operations

Resource path:

```
/realm-config/services/id-repositories/LDAPv3ForAD
```

Resource version: `0.0`

### create

**Usage**

```
am> create ActiveDirectory --realm Realm --id id --body body
```

**Parameters**

* *\--id*

  The unique identifier for the resource.

* *\--body*

  The resource in JSON format, described by the following JSON schema:

  ```json
  {
    "type" : "object",
    "properties" : {
      "ldapsettings" : {
        "type" : "object",
        "title" : "Server Settings",
        "propertyOrder" : 0,
        "properties" : {
          "openam-idrepo-ldapv3-keepalive-searchfilter" : {
            "title" : "LDAP Connection Heartbeat Search Filter",
            "description" : "Defines the search filter to the KeepAlive and Availability Search request.<br><br>This setting controls the search filter to the KeepAlive and Availability search request. The default value for search filter is \"(objectClass=*)\". The Absolute True and False filter \"(&)\" can also be used. The LDAP server connection pool will be marked as unavailable if the search fails with an error, returns no entries, or if more than one entry is returned.",
            "propertyOrder" : 1302,
            "required" : false,
            "type" : "string",
            "exampleValue" : ""
          },
          "openam-idrepo-ldapv3-keepalive-searchbase" : {
            "title" : "LDAP Connection Heartbeat Search Base",
            "description" : "Defines the search base to the KeepAlive and Availability Search request.<br><br>This setting controls the search base to the KeepAlive and Availability search request. The default value for search base DN is \"\". The LDAP server connection pool will be marked as unavailable if the search fails with an error, returns no entries, or if more than one entry is returned.",
            "propertyOrder" : 1301,
            "required" : false,
            "type" : "string",
            "exampleValue" : ""
          },
          "sun-idrepo-ldapv3-config-organization_name" : {
            "title" : "LDAP Organization DN",
            "description" : "",
            "propertyOrder" : 900,
            "required" : true,
            "type" : "string",
            "exampleValue" : ""
          },
          "sun-idrepo-ldapv3-config-ldap-server" : {
            "title" : "LDAP Server",
            "description" : "Format: LDAP server host name:port | server_ID | site_ID",
            "propertyOrder" : 600,
            "required" : true,
            "items" : {
              "type" : "string"
            },
            "minItems" : 1,
            "type" : "array",
            "exampleValue" : ""
          },
          "openam-idrepo-ldapv3-heartbeat-timeunit" : {
            "title" : "LDAP Connection Heartbeat Time Unit",
            "description" : "Defines the time unit corresponding to the Heartbeat Interval setting.<br><br>This setting controls how often OpenAM <b>should</b> send a heartbeat search request to the configured directory. If a connection becomes unresponsive (e.g. due to a network error) then it may take up to the interval period before the problem is detected. Use along with the Heartbeat Interval parameter to define the exact interval.",
            "propertyOrder" : 1400,
            "required" : false,
            "type" : "string",
            "exampleValue" : ""
          },
          "sun-idrepo-ldapv3-config-max-result" : {
            "title" : "Maximum Results Returned from Search",
            "description" : "",
            "propertyOrder" : 1500,
            "required" : false,
            "type" : "integer",
            "exampleValue" : ""
          },
          "sun-idrepo-ldapv3-config-time-limit" : {
            "title" : "Search Timeout",
            "description" : "In seconds.",
            "propertyOrder" : 1600,
            "required" : false,
            "type" : "integer",
            "exampleValue" : ""
          },
          "sun-idrepo-ldapv3-config-connection_pool_min_size" : {
            "title" : "LDAP Connection Pool Minimum Size",
            "description" : "",
            "propertyOrder" : 1100,
            "required" : false,
            "type" : "integer",
            "exampleValue" : ""
          },
          "sun-idrepo-ldapv3-config-search-scope" : {
            "title" : "LDAPv3 Plug-in Search Scope",
            "description" : "",
            "propertyOrder" : 2000,
            "required" : false,
            "type" : "string",
            "exampleValue" : ""
          },
          "sun-idrepo-ldapv3-config-connection-mode" : {
            "title" : "LDAP Connection Mode",
            "description" : "Defines which protocol/operation is used to establish the connection to the LDAP Directory Server.<br><br>If 'LDAP' is selected, the connection <b>won't be secured</b> and passwords are transferred in <b>cleartext</b> over the network.<br/> If 'LDAPS' is selected, the connection is secured via SSL or TLS. <br/> If 'StartTLS' is selected, the connection is secured by using StartTLS extended operation.",
            "propertyOrder" : 1000,
            "required" : false,
            "type" : "string",
            "exampleValue" : ""
          },
          "openam-idrepo-ldapv3-affinity-enabled" : {
            "title" : "Affinity Enabled",
            "description" : "Enables affinity based request load balancing when accessing the user store servers (based on DN). It is imperative that the connection string setting is set to the same value for all OpenAM servers in the deployment when this feature is enabled.",
            "propertyOrder" : 6200,
            "required" : true,
            "type" : "boolean",
            "exampleValue" : ""
          },
          "sun-idrepo-ldapv3-config-authid" : {
            "title" : "LDAP Bind DN",
            "description" : "A user or admin with sufficient access rights to perform the supported operations. This property is ignored if mTLS Enabled is set.",
            "propertyOrder" : 700,
            "required" : false,
            "type" : "string",
            "exampleValue" : ""
          },
          "sun-idrepo-ldapv3-config-authpw" : {
            "title" : "LDAP Bind Password",
            "description" : "This property is ignored if mTLS Enabled is set.",
            "propertyOrder" : 800,
            "required" : false,
            "type" : "string",
            "format" : "password",
            "exampleValue" : ""
          },
          "openam-idrepo-ldapv3-affinity-level" : {
            "title" : "Affinity Level",
            "description" : "Level of affinity used to balance requests across IdRepo servers. Applies only if <code>Affinity Enabled</code> is on. Options are: no affinity, affinity for BIND requests only,  or affinity for all requests.",
            "propertyOrder" : 6350,
            "required" : false,
            "type" : "string",
            "exampleValue" : ""
          },
          "sun-idrepo-ldapv3-config-connection_pool_max_size" : {
            "title" : "LDAP Connection Pool Maximum Size",
            "description" : "",
            "propertyOrder" : 1200,
            "required" : false,
            "type" : "integer",
            "exampleValue" : ""
          },
          "openam-idrepo-ldapv3-heartbeat-interval" : {
            "title" : "LDAP Connection Heartbeat Interval",
            "description" : "Specifies how often should OpenAM send a heartbeat request to the directory.<br><br>This setting controls how often OpenAM <b>should</b> send a heartbeat search request to the configured directory. If a connection becomes unresponsive (e.g. due to a network error) then it may take up to the interval period before the problem is detected. Use along with the Heartbeat Time Unit parameter to define the exact interval. Zero or negative value will result in disabling heartbeat requests.",
            "propertyOrder" : 1300,
            "required" : false,
            "type" : "integer",
            "exampleValue" : ""
          }
        }
      },
      "userconfig" : {
        "type" : "object",
        "title" : "User Configuration",
        "propertyOrder" : 3,
        "properties" : {
          "sun-idrepo-ldapv3-config-isactive" : {
            "title" : "Attribute Name of User Status",
            "description" : "",
            "propertyOrder" : 2600,
            "required" : false,
            "type" : "string",
            "exampleValue" : ""
          },
          "sun-idrepo-ldapv3-config-user-attributes" : {
            "title" : "LDAP User Attributes",
            "description" : "",
            "propertyOrder" : 2400,
            "required" : false,
            "items" : {
              "type" : "string"
            },
            "type" : "array",
            "exampleValue" : ""
          },
          "sun-idrepo-ldapv3-config-auth-kba-index-attr" : {
            "title" : "Knowledge Based Authentication Active Index",
            "description" : "",
            "propertyOrder" : 5400,
            "required" : false,
            "type" : "string",
            "exampleValue" : ""
          },
          "sun-idrepo-ldapv3-config-people-container-value" : {
            "title" : "LDAP People Container Value",
            "description" : "",
            "propertyOrder" : 5100,
            "required" : false,
            "type" : "string",
            "exampleValue" : ""
          },
          "sun-idrepo-ldapv3-config-auth-kba-attr" : {
            "title" : "Knowledge Based Authentication Attribute Name",
            "description" : "",
            "propertyOrder" : 5300,
            "required" : false,
            "items" : {
              "type" : "string"
            },
            "type" : "array",
            "exampleValue" : ""
          },
          "sun-idrepo-ldapv3-config-createuser-attr-mapping" : {
            "title" : "Create User Attribute Mapping",
            "description" : "Format: attribute name or TargetAttributeName=SourceAttributeName",
            "propertyOrder" : 2500,
            "required" : false,
            "items" : {
              "type" : "string"
            },
            "type" : "array",
            "exampleValue" : ""
          },
          "sun-idrepo-ldapv3-config-user-objectclass" : {
            "title" : "LDAP User Object Class",
            "description" : "",
            "propertyOrder" : 2300,
            "required" : false,
            "items" : {
              "type" : "string"
            },
            "type" : "array",
            "exampleValue" : ""
          },
          "sun-idrepo-ldapv3-config-users-search-attribute" : {
            "title" : "LDAP Users  Search Attribute",
            "description" : "",
            "propertyOrder" : 2100,
            "required" : false,
            "type" : "string",
            "exampleValue" : ""
          },
          "sun-idrepo-ldapv3-config-people-container-name" : {
            "title" : "LDAP People Container Naming Attribute",
            "description" : "",
            "propertyOrder" : 5000,
            "required" : false,
            "type" : "string",
            "exampleValue" : ""
          },
          "sun-idrepo-ldapv3-config-inactive" : {
            "title" : "User Status Inactive Value",
            "description" : "",
            "propertyOrder" : 2800,
            "required" : false,
            "type" : "string",
            "exampleValue" : ""
          },
          "sun-idrepo-ldapv3-config-users-search-filter" : {
            "title" : "LDAP Users  Search Filter",
            "description" : "",
            "propertyOrder" : 2200,
            "required" : false,
            "type" : "string",
            "exampleValue" : ""
          },
          "sun-idrepo-ldapv3-config-active" : {
            "title" : "User Status Active Value",
            "description" : "",
            "propertyOrder" : 2700,
            "required" : false,
            "type" : "string",
            "exampleValue" : ""
          },
          "sun-idrepo-ldapv3-config-auth-kba-attempts-attr" : {
            "title" : "Knowledge Based Authentication Attempts Attribute Name",
            "description" : "",
            "propertyOrder" : 5410,
            "required" : false,
            "items" : {
              "type" : "string"
            },
            "type" : "array",
            "exampleValue" : ""
          }
        }
      },
      "pluginconfig" : {
        "type" : "object",
        "title" : "Plug-in Configuration",
        "propertyOrder" : 2,
        "properties" : {
          "sunIdRepoSupportedOperations" : {
            "title" : "LDAPv3 Plug-in Supported Types and Operations",
            "description" : "",
            "propertyOrder" : 1900,
            "required" : false,
            "items" : {
              "type" : "string"
            },
            "type" : "array",
            "exampleValue" : ""
          },
          "sunIdRepoClass" : {
            "title" : "LDAPv3 Repository Plug-in Class Name",
            "description" : "",
            "propertyOrder" : 1700,
            "required" : true,
            "type" : "string",
            "exampleValue" : ""
          },
          "sunIdRepoAttributeMapping" : {
            "title" : "Attribute Name Mapping",
            "description" : "",
            "propertyOrder" : 1800,
            "required" : false,
            "items" : {
              "type" : "string"
            },
            "type" : "array",
            "exampleValue" : ""
          }
        }
      },
      "groupconfig" : {
        "type" : "object",
        "title" : "Group Configuration",
        "propertyOrder" : 5,
        "properties" : {
          "sun-idrepo-ldapv3-config-group-container-name" : {
            "title" : "LDAP Groups Container Naming Attribute",
            "description" : "",
            "propertyOrder" : 3100,
            "required" : false,
            "type" : "string",
            "exampleValue" : ""
          },
          "sun-idrepo-ldapv3-config-group-attributes" : {
            "title" : "LDAP Groups Attributes",
            "description" : "",
            "propertyOrder" : 3400,
            "required" : false,
            "items" : {
              "type" : "string"
            },
            "type" : "array",
            "exampleValue" : ""
          },
          "sun-idrepo-ldapv3-config-uniquemember" : {
            "title" : "Attribute Name of Unique Member",
            "description" : "",
            "propertyOrder" : 3600,
            "required" : false,
            "type" : "string",
            "exampleValue" : ""
          },
          "sun-idrepo-ldapv3-config-group-objectclass" : {
            "title" : "LDAP Groups Object Class",
            "description" : "",
            "propertyOrder" : 3300,
            "required" : false,
            "items" : {
              "type" : "string"
            },
            "type" : "array",
            "exampleValue" : ""
          },
          "sun-idrepo-ldapv3-config-group-container-value" : {
            "title" : "LDAP Groups Container Value",
            "description" : "",
            "propertyOrder" : 3200,
            "required" : false,
            "type" : "string",
            "exampleValue" : ""
          },
          "sun-idrepo-ldapv3-config-groups-search-filter" : {
            "title" : "LDAP Groups Search Filter",
            "description" : "",
            "propertyOrder" : 3000,
            "required" : false,
            "type" : "string",
            "exampleValue" : ""
          },
          "sun-idrepo-ldapv3-config-memberof" : {
            "title" : "Attribute Name for Group Membership",
            "description" : "",
            "propertyOrder" : 3500,
            "required" : false,
            "type" : "string",
            "exampleValue" : ""
          },
          "adRecursiveGroupMembership" : {
            "title" : "AD Recursive Group Membership Evaluation",
            "description" : "Used to enable/disable Active Directory Recursive Group Membership evaluation.<br><br>Enables an Active Directory specific extensible filter called LDAP_MATCHING_RULE_IN_CHAIN that according to MSDN \"walks the chain of ancestry in objects all the way to the root until it finds a match\", meaning that it will resolve all group memberships, including nested groups. This will add a performance overhead on the Active Directory server, indexes may need to be created.",
            "propertyOrder" : 6100,
            "required" : true,
            "type" : "boolean",
            "exampleValue" : ""
          },
          "sun-idrepo-ldapv3-config-groups-search-attribute" : {
            "title" : "LDAP Groups Search Attribute",
            "description" : "",
            "propertyOrder" : 2900,
            "required" : false,
            "type" : "string",
            "exampleValue" : ""
          }
        }
      },
      "errorhandling" : {
        "type" : "object",
        "title" : "Error Handling Configuration",
        "propertyOrder" : 8,
        "properties" : {
          "com.iplanet.am.ldap.connection.delay.between.retries" : {
            "title" : "The Delay Time Between Retries",
            "description" : "In milliseconds.",
            "propertyOrder" : 5800,
            "required" : false,
            "type" : "integer",
            "exampleValue" : ""
          }
        }
      },
      "cachecontrol" : {
        "type" : "object",
        "title" : "Cache Control",
        "propertyOrder" : 9,
        "properties" : {
          "sun-idrepo-ldapv3-dncache-enabled" : {
            "title" : "DN Cache",
            "description" : "Used to enable/disable the DN Cache within the OpenAM repository implementation.<br><br>The DN Cache is used to cache DN lookups which tend to happen in bursts during authentication. The DN Cache can become out of date when a user is moved or renamed in the underlying LDAP store and this is not reflected in a persistent search result. Enable when the underlying LDAP store supports persistent search and move/rename (mod_dn) results are available.",
            "propertyOrder" : 5900,
            "required" : false,
            "type" : "boolean",
            "exampleValue" : ""
          },
          "sun-idrepo-ldapv3-dncache-size" : {
            "title" : "DN Cache Size",
            "description" : "In DN items, only used when DN Cache is enabled.",
            "propertyOrder" : 6000,
            "required" : false,
            "type" : "integer",
            "exampleValue" : ""
          }
        }
      },
      "persistentsearch" : {
        "type" : "object",
        "title" : "Persistent Search Controls",
        "propertyOrder" : 7,
        "properties" : {
          "sun-idrepo-ldapv3-config-psearchbase" : {
            "title" : "Persistent Search Base DN",
            "description" : "",
            "propertyOrder" : 5500,
            "required" : false,
            "type" : "string",
            "exampleValue" : ""
          },
          "sun-idrepo-ldapv3-config-psearch-scope" : {
            "title" : "Persistent Search Scope",
            "description" : "",
            "propertyOrder" : 5700,
            "required" : false,
            "type" : "string",
            "exampleValue" : ""
          }
        }
      },
      "authentication" : {
        "type" : "object",
        "title" : "Authentication Configuration",
        "propertyOrder" : 4,
        "properties" : {
          "sun-idrepo-ldapv3-config-auth-naming-attr" : {
            "title" : "Authentication Naming Attribute",
            "description" : "",
            "propertyOrder" : 5200,
            "required" : false,
            "type" : "string",
            "exampleValue" : ""
          }
        }
      }
    }
  }
  ```

### delete

**Usage**

```
am> delete ActiveDirectory --realm Realm --id id
```

**Parameters**

* *\--id*

  The unique identifier for the resource.

### getAllTypes

Obtain the collection of all secondary configuration types related to the resource.

**Usage**

```
am> action ActiveDirectory --realm Realm --actionName getAllTypes
```

### getCreatableTypes

Obtain the collection of secondary configuration types that have yet to be added to the resource.

**Usage**

```
am> action ActiveDirectory --realm Realm --actionName getCreatableTypes
```

### nextdescendents

Obtain the collection of secondary configuration instances that have been added to the resource.

**Usage**

```
am> action ActiveDirectory --realm Realm --actionName nextdescendents
```

### query

Get the full list of instances of this collection. This query only supports `_queryFilter=true` filter.

**Usage**

```
am> query ActiveDirectory --realm Realm --filter filter
```

**Parameters**

* *\--filter*

  A CREST formatted query filter, where "true" will query all.

### read

**Usage**

```
am> read ActiveDirectory --realm Realm --id id
```

**Parameters**

* *\--id*

  The unique identifier for the resource.

### update

**Usage**

```
am> update ActiveDirectory --realm Realm --id id --body body
```

**Parameters**

* *\--id*

  The unique identifier for the resource.

* *\--body*

  The resource in JSON format, described by the following JSON schema:

  ```json
  {
    "type" : "object",
    "properties" : {
      "ldapsettings" : {
        "type" : "object",
        "title" : "Server Settings",
        "propertyOrder" : 0,
        "properties" : {
          "openam-idrepo-ldapv3-keepalive-searchfilter" : {
            "title" : "LDAP Connection Heartbeat Search Filter",
            "description" : "Defines the search filter to the KeepAlive and Availability Search request.<br><br>This setting controls the search filter to the KeepAlive and Availability search request. The default value for search filter is \"(objectClass=*)\". The Absolute True and False filter \"(&)\" can also be used. The LDAP server connection pool will be marked as unavailable if the search fails with an error, returns no entries, or if more than one entry is returned.",
            "propertyOrder" : 1302,
            "required" : false,
            "type" : "string",
            "exampleValue" : ""
          },
          "openam-idrepo-ldapv3-keepalive-searchbase" : {
            "title" : "LDAP Connection Heartbeat Search Base",
            "description" : "Defines the search base to the KeepAlive and Availability Search request.<br><br>This setting controls the search base to the KeepAlive and Availability search request. The default value for search base DN is \"\". The LDAP server connection pool will be marked as unavailable if the search fails with an error, returns no entries, or if more than one entry is returned.",
            "propertyOrder" : 1301,
            "required" : false,
            "type" : "string",
            "exampleValue" : ""
          },
          "sun-idrepo-ldapv3-config-organization_name" : {
            "title" : "LDAP Organization DN",
            "description" : "",
            "propertyOrder" : 900,
            "required" : true,
            "type" : "string",
            "exampleValue" : ""
          },
          "sun-idrepo-ldapv3-config-ldap-server" : {
            "title" : "LDAP Server",
            "description" : "Format: LDAP server host name:port | server_ID | site_ID",
            "propertyOrder" : 600,
            "required" : true,
            "items" : {
              "type" : "string"
            },
            "minItems" : 1,
            "type" : "array",
            "exampleValue" : ""
          },
          "openam-idrepo-ldapv3-heartbeat-timeunit" : {
            "title" : "LDAP Connection Heartbeat Time Unit",
            "description" : "Defines the time unit corresponding to the Heartbeat Interval setting.<br><br>This setting controls how often OpenAM <b>should</b> send a heartbeat search request to the configured directory. If a connection becomes unresponsive (e.g. due to a network error) then it may take up to the interval period before the problem is detected. Use along with the Heartbeat Interval parameter to define the exact interval.",
            "propertyOrder" : 1400,
            "required" : false,
            "type" : "string",
            "exampleValue" : ""
          },
          "sun-idrepo-ldapv3-config-max-result" : {
            "title" : "Maximum Results Returned from Search",
            "description" : "",
            "propertyOrder" : 1500,
            "required" : false,
            "type" : "integer",
            "exampleValue" : ""
          },
          "sun-idrepo-ldapv3-config-time-limit" : {
            "title" : "Search Timeout",
            "description" : "In seconds.",
            "propertyOrder" : 1600,
            "required" : false,
            "type" : "integer",
            "exampleValue" : ""
          },
          "sun-idrepo-ldapv3-config-connection_pool_min_size" : {
            "title" : "LDAP Connection Pool Minimum Size",
            "description" : "",
            "propertyOrder" : 1100,
            "required" : false,
            "type" : "integer",
            "exampleValue" : ""
          },
          "sun-idrepo-ldapv3-config-search-scope" : {
            "title" : "LDAPv3 Plug-in Search Scope",
            "description" : "",
            "propertyOrder" : 2000,
            "required" : false,
            "type" : "string",
            "exampleValue" : ""
          },
          "sun-idrepo-ldapv3-config-connection-mode" : {
            "title" : "LDAP Connection Mode",
            "description" : "Defines which protocol/operation is used to establish the connection to the LDAP Directory Server.<br><br>If 'LDAP' is selected, the connection <b>won't be secured</b> and passwords are transferred in <b>cleartext</b> over the network.<br/> If 'LDAPS' is selected, the connection is secured via SSL or TLS. <br/> If 'StartTLS' is selected, the connection is secured by using StartTLS extended operation.",
            "propertyOrder" : 1000,
            "required" : false,
            "type" : "string",
            "exampleValue" : ""
          },
          "openam-idrepo-ldapv3-affinity-enabled" : {
            "title" : "Affinity Enabled",
            "description" : "Enables affinity based request load balancing when accessing the user store servers (based on DN). It is imperative that the connection string setting is set to the same value for all OpenAM servers in the deployment when this feature is enabled.",
            "propertyOrder" : 6200,
            "required" : true,
            "type" : "boolean",
            "exampleValue" : ""
          },
          "sun-idrepo-ldapv3-config-authid" : {
            "title" : "LDAP Bind DN",
            "description" : "A user or admin with sufficient access rights to perform the supported operations. This property is ignored if mTLS Enabled is set.",
            "propertyOrder" : 700,
            "required" : false,
            "type" : "string",
            "exampleValue" : ""
          },
          "sun-idrepo-ldapv3-config-authpw" : {
            "title" : "LDAP Bind Password",
            "description" : "This property is ignored if mTLS Enabled is set.",
            "propertyOrder" : 800,
            "required" : false,
            "type" : "string",
            "format" : "password",
            "exampleValue" : ""
          },
          "openam-idrepo-ldapv3-affinity-level" : {
            "title" : "Affinity Level",
            "description" : "Level of affinity used to balance requests across IdRepo servers. Applies only if <code>Affinity Enabled</code> is on. Options are: no affinity, affinity for BIND requests only,  or affinity for all requests.",
            "propertyOrder" : 6350,
            "required" : false,
            "type" : "string",
            "exampleValue" : ""
          },
          "sun-idrepo-ldapv3-config-connection_pool_max_size" : {
            "title" : "LDAP Connection Pool Maximum Size",
            "description" : "",
            "propertyOrder" : 1200,
            "required" : false,
            "type" : "integer",
            "exampleValue" : ""
          },
          "openam-idrepo-ldapv3-heartbeat-interval" : {
            "title" : "LDAP Connection Heartbeat Interval",
            "description" : "Specifies how often should OpenAM send a heartbeat request to the directory.<br><br>This setting controls how often OpenAM <b>should</b> send a heartbeat search request to the configured directory. If a connection becomes unresponsive (e.g. due to a network error) then it may take up to the interval period before the problem is detected. Use along with the Heartbeat Time Unit parameter to define the exact interval. Zero or negative value will result in disabling heartbeat requests.",
            "propertyOrder" : 1300,
            "required" : false,
            "type" : "integer",
            "exampleValue" : ""
          }
        }
      },
      "userconfig" : {
        "type" : "object",
        "title" : "User Configuration",
        "propertyOrder" : 3,
        "properties" : {
          "sun-idrepo-ldapv3-config-isactive" : {
            "title" : "Attribute Name of User Status",
            "description" : "",
            "propertyOrder" : 2600,
            "required" : false,
            "type" : "string",
            "exampleValue" : ""
          },
          "sun-idrepo-ldapv3-config-user-attributes" : {
            "title" : "LDAP User Attributes",
            "description" : "",
            "propertyOrder" : 2400,
            "required" : false,
            "items" : {
              "type" : "string"
            },
            "type" : "array",
            "exampleValue" : ""
          },
          "sun-idrepo-ldapv3-config-auth-kba-index-attr" : {
            "title" : "Knowledge Based Authentication Active Index",
            "description" : "",
            "propertyOrder" : 5400,
            "required" : false,
            "type" : "string",
            "exampleValue" : ""
          },
          "sun-idrepo-ldapv3-config-people-container-value" : {
            "title" : "LDAP People Container Value",
            "description" : "",
            "propertyOrder" : 5100,
            "required" : false,
            "type" : "string",
            "exampleValue" : ""
          },
          "sun-idrepo-ldapv3-config-auth-kba-attr" : {
            "title" : "Knowledge Based Authentication Attribute Name",
            "description" : "",
            "propertyOrder" : 5300,
            "required" : false,
            "items" : {
              "type" : "string"
            },
            "type" : "array",
            "exampleValue" : ""
          },
          "sun-idrepo-ldapv3-config-createuser-attr-mapping" : {
            "title" : "Create User Attribute Mapping",
            "description" : "Format: attribute name or TargetAttributeName=SourceAttributeName",
            "propertyOrder" : 2500,
            "required" : false,
            "items" : {
              "type" : "string"
            },
            "type" : "array",
            "exampleValue" : ""
          },
          "sun-idrepo-ldapv3-config-user-objectclass" : {
            "title" : "LDAP User Object Class",
            "description" : "",
            "propertyOrder" : 2300,
            "required" : false,
            "items" : {
              "type" : "string"
            },
            "type" : "array",
            "exampleValue" : ""
          },
          "sun-idrepo-ldapv3-config-users-search-attribute" : {
            "title" : "LDAP Users  Search Attribute",
            "description" : "",
            "propertyOrder" : 2100,
            "required" : false,
            "type" : "string",
            "exampleValue" : ""
          },
          "sun-idrepo-ldapv3-config-people-container-name" : {
            "title" : "LDAP People Container Naming Attribute",
            "description" : "",
            "propertyOrder" : 5000,
            "required" : false,
            "type" : "string",
            "exampleValue" : ""
          },
          "sun-idrepo-ldapv3-config-inactive" : {
            "title" : "User Status Inactive Value",
            "description" : "",
            "propertyOrder" : 2800,
            "required" : false,
            "type" : "string",
            "exampleValue" : ""
          },
          "sun-idrepo-ldapv3-config-users-search-filter" : {
            "title" : "LDAP Users  Search Filter",
            "description" : "",
            "propertyOrder" : 2200,
            "required" : false,
            "type" : "string",
            "exampleValue" : ""
          },
          "sun-idrepo-ldapv3-config-active" : {
            "title" : "User Status Active Value",
            "description" : "",
            "propertyOrder" : 2700,
            "required" : false,
            "type" : "string",
            "exampleValue" : ""
          },
          "sun-idrepo-ldapv3-config-auth-kba-attempts-attr" : {
            "title" : "Knowledge Based Authentication Attempts Attribute Name",
            "description" : "",
            "propertyOrder" : 5410,
            "required" : false,
            "items" : {
              "type" : "string"
            },
            "type" : "array",
            "exampleValue" : ""
          }
        }
      },
      "pluginconfig" : {
        "type" : "object",
        "title" : "Plug-in Configuration",
        "propertyOrder" : 2,
        "properties" : {
          "sunIdRepoSupportedOperations" : {
            "title" : "LDAPv3 Plug-in Supported Types and Operations",
            "description" : "",
            "propertyOrder" : 1900,
            "required" : false,
            "items" : {
              "type" : "string"
            },
            "type" : "array",
            "exampleValue" : ""
          },
          "sunIdRepoClass" : {
            "title" : "LDAPv3 Repository Plug-in Class Name",
            "description" : "",
            "propertyOrder" : 1700,
            "required" : true,
            "type" : "string",
            "exampleValue" : ""
          },
          "sunIdRepoAttributeMapping" : {
            "title" : "Attribute Name Mapping",
            "description" : "",
            "propertyOrder" : 1800,
            "required" : false,
            "items" : {
              "type" : "string"
            },
            "type" : "array",
            "exampleValue" : ""
          }
        }
      },
      "groupconfig" : {
        "type" : "object",
        "title" : "Group Configuration",
        "propertyOrder" : 5,
        "properties" : {
          "sun-idrepo-ldapv3-config-group-container-name" : {
            "title" : "LDAP Groups Container Naming Attribute",
            "description" : "",
            "propertyOrder" : 3100,
            "required" : false,
            "type" : "string",
            "exampleValue" : ""
          },
          "sun-idrepo-ldapv3-config-group-attributes" : {
            "title" : "LDAP Groups Attributes",
            "description" : "",
            "propertyOrder" : 3400,
            "required" : false,
            "items" : {
              "type" : "string"
            },
            "type" : "array",
            "exampleValue" : ""
          },
          "sun-idrepo-ldapv3-config-uniquemember" : {
            "title" : "Attribute Name of Unique Member",
            "description" : "",
            "propertyOrder" : 3600,
            "required" : false,
            "type" : "string",
            "exampleValue" : ""
          },
          "sun-idrepo-ldapv3-config-group-objectclass" : {
            "title" : "LDAP Groups Object Class",
            "description" : "",
            "propertyOrder" : 3300,
            "required" : false,
            "items" : {
              "type" : "string"
            },
            "type" : "array",
            "exampleValue" : ""
          },
          "sun-idrepo-ldapv3-config-group-container-value" : {
            "title" : "LDAP Groups Container Value",
            "description" : "",
            "propertyOrder" : 3200,
            "required" : false,
            "type" : "string",
            "exampleValue" : ""
          },
          "sun-idrepo-ldapv3-config-groups-search-filter" : {
            "title" : "LDAP Groups Search Filter",
            "description" : "",
            "propertyOrder" : 3000,
            "required" : false,
            "type" : "string",
            "exampleValue" : ""
          },
          "sun-idrepo-ldapv3-config-memberof" : {
            "title" : "Attribute Name for Group Membership",
            "description" : "",
            "propertyOrder" : 3500,
            "required" : false,
            "type" : "string",
            "exampleValue" : ""
          },
          "adRecursiveGroupMembership" : {
            "title" : "AD Recursive Group Membership Evaluation",
            "description" : "Used to enable/disable Active Directory Recursive Group Membership evaluation.<br><br>Enables an Active Directory specific extensible filter called LDAP_MATCHING_RULE_IN_CHAIN that according to MSDN \"walks the chain of ancestry in objects all the way to the root until it finds a match\", meaning that it will resolve all group memberships, including nested groups. This will add a performance overhead on the Active Directory server, indexes may need to be created.",
            "propertyOrder" : 6100,
            "required" : true,
            "type" : "boolean",
            "exampleValue" : ""
          },
          "sun-idrepo-ldapv3-config-groups-search-attribute" : {
            "title" : "LDAP Groups Search Attribute",
            "description" : "",
            "propertyOrder" : 2900,
            "required" : false,
            "type" : "string",
            "exampleValue" : ""
          }
        }
      },
      "errorhandling" : {
        "type" : "object",
        "title" : "Error Handling Configuration",
        "propertyOrder" : 8,
        "properties" : {
          "com.iplanet.am.ldap.connection.delay.between.retries" : {
            "title" : "The Delay Time Between Retries",
            "description" : "In milliseconds.",
            "propertyOrder" : 5800,
            "required" : false,
            "type" : "integer",
            "exampleValue" : ""
          }
        }
      },
      "cachecontrol" : {
        "type" : "object",
        "title" : "Cache Control",
        "propertyOrder" : 9,
        "properties" : {
          "sun-idrepo-ldapv3-dncache-enabled" : {
            "title" : "DN Cache",
            "description" : "Used to enable/disable the DN Cache within the OpenAM repository implementation.<br><br>The DN Cache is used to cache DN lookups which tend to happen in bursts during authentication. The DN Cache can become out of date when a user is moved or renamed in the underlying LDAP store and this is not reflected in a persistent search result. Enable when the underlying LDAP store supports persistent search and move/rename (mod_dn) results are available.",
            "propertyOrder" : 5900,
            "required" : false,
            "type" : "boolean",
            "exampleValue" : ""
          },
          "sun-idrepo-ldapv3-dncache-size" : {
            "title" : "DN Cache Size",
            "description" : "In DN items, only used when DN Cache is enabled.",
            "propertyOrder" : 6000,
            "required" : false,
            "type" : "integer",
            "exampleValue" : ""
          }
        }
      },
      "persistentsearch" : {
        "type" : "object",
        "title" : "Persistent Search Controls",
        "propertyOrder" : 7,
        "properties" : {
          "sun-idrepo-ldapv3-config-psearchbase" : {
            "title" : "Persistent Search Base DN",
            "description" : "",
            "propertyOrder" : 5500,
            "required" : false,
            "type" : "string",
            "exampleValue" : ""
          },
          "sun-idrepo-ldapv3-config-psearch-scope" : {
            "title" : "Persistent Search Scope",
            "description" : "",
            "propertyOrder" : 5700,
            "required" : false,
            "type" : "string",
            "exampleValue" : ""
          }
        }
      },
      "authentication" : {
        "type" : "object",
        "title" : "Authentication Configuration",
        "propertyOrder" : 4,
        "properties" : {
          "sun-idrepo-ldapv3-config-auth-naming-attr" : {
            "title" : "Authentication Naming Attribute",
            "description" : "",
            "propertyOrder" : 5200,
            "required" : false,
            "type" : "string",
            "exampleValue" : ""
          }
        }
      }
    }
  }
  ```

---

---
title: ActiveDirectoryApplicationModeADAM
description: Resource path:
component: pingam
version: 8.1
page_id: pingam:entity-reference:sec-amster-entity-activedirectoryapplicationmodeadam
canonical_url: https://docs.pingidentity.com/pingam/8.1/entity-reference/sec-amster-entity-activedirectoryapplicationmodeadam.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  sec-amster-entity-activedirectoryapplicationmodeadam-realm-ops: Realm Operations
  sec-amster-entity-activedirectoryapplicationmodeadam-realm-ops-create: create
  sec-amster-entity-activedirectoryapplicationmodeadam-realm-ops-delete: delete
  sec-amster-entity-activedirectoryapplicationmodeadam-realm-ops-getalltypes: getAllTypes
  sec-amster-entity-activedirectoryapplicationmodeadam-realm-ops-getcreatabletypes: getCreatableTypes
  sec-amster-entity-activedirectoryapplicationmodeadam-realm-ops-nextdescendents: nextdescendents
  sec-amster-entity-activedirectoryapplicationmodeadam-realm-ops-query: query
  sec-amster-entity-activedirectoryapplicationmodeadam-realm-ops-read: read
  sec-amster-entity-activedirectoryapplicationmodeadam-realm-ops-update: update
---

# ActiveDirectoryApplicationModeADAM

## Realm Operations

Resource path:

```
/realm-config/services/id-repositories/LDAPv3ForADAM
```

Resource version: `0.0`

### create

**Usage**

```
am> create ActiveDirectoryApplicationModeADAM --realm Realm --id id --body body
```

**Parameters**

* *\--id*

  The unique identifier for the resource.

* *\--body*

  The resource in JSON format, described by the following JSON schema:

  ```json
  {
    "type" : "object",
    "properties" : {
      "ldapsettings" : {
        "type" : "object",
        "title" : "Server Settings",
        "propertyOrder" : 0,
        "properties" : {
          "openam-idrepo-ldapv3-affinity-enabled" : {
            "title" : "Affinity Enabled",
            "description" : "Enables affinity based request load balancing when accessing the user store servers (based on DN). It is imperative that the connection string setting is set to the same value for all OpenAM servers in the deployment when this feature is enabled.",
            "propertyOrder" : 6200,
            "required" : true,
            "type" : "boolean",
            "exampleValue" : ""
          },
          "sun-idrepo-ldapv3-config-max-result" : {
            "title" : "Maximum Results Returned from Search",
            "description" : "",
            "propertyOrder" : 1500,
            "required" : false,
            "type" : "integer",
            "exampleValue" : ""
          },
          "openam-idrepo-ldapv3-keepalive-searchbase" : {
            "title" : "LDAP Connection Heartbeat Search Base",
            "description" : "Defines the search base to the KeepAlive and Availability Search request.<br><br>This setting controls the search base to the KeepAlive and Availability search request. The default value for search base DN is \"\". The LDAP server connection pool will be marked as unavailable if the search fails with an error, returns no entries, or if more than one entry is returned.",
            "propertyOrder" : 1301,
            "required" : false,
            "type" : "string",
            "exampleValue" : ""
          },
          "sun-idrepo-ldapv3-config-authpw" : {
            "title" : "LDAP Bind Password",
            "description" : "This property is ignored if mTLS Enabled is set.",
            "propertyOrder" : 800,
            "required" : false,
            "type" : "string",
            "format" : "password",
            "exampleValue" : ""
          },
          "sun-idrepo-ldapv3-config-ldap-server" : {
            "title" : "LDAP Server",
            "description" : "Format: LDAP server host name:port | server_ID | site_ID",
            "propertyOrder" : 600,
            "required" : true,
            "items" : {
              "type" : "string"
            },
            "minItems" : 1,
            "type" : "array",
            "exampleValue" : ""
          },
          "sun-idrepo-ldapv3-config-search-scope" : {
            "title" : "LDAPv3 Plug-in Search Scope",
            "description" : "",
            "propertyOrder" : 2000,
            "required" : false,
            "type" : "string",
            "exampleValue" : ""
          },
          "sun-idrepo-ldapv3-config-connection_pool_min_size" : {
            "title" : "LDAP Connection Pool Minimum Size",
            "description" : "",
            "propertyOrder" : 1100,
            "required" : false,
            "type" : "integer",
            "exampleValue" : ""
          },
          "sun-idrepo-ldapv3-config-authid" : {
            "title" : "LDAP Bind DN",
            "description" : "A user or admin with sufficient access rights to perform the supported operations. This property is ignored if mTLS Enabled is set.",
            "propertyOrder" : 700,
            "required" : false,
            "type" : "string",
            "exampleValue" : ""
          },
          "sun-idrepo-ldapv3-config-time-limit" : {
            "title" : "Search Timeout",
            "description" : "In seconds.",
            "propertyOrder" : 1600,
            "required" : false,
            "type" : "integer",
            "exampleValue" : ""
          },
          "sun-idrepo-ldapv3-config-organization_name" : {
            "title" : "LDAP Organization DN",
            "description" : "",
            "propertyOrder" : 900,
            "required" : true,
            "type" : "string",
            "exampleValue" : ""
          },
          "sun-idrepo-ldapv3-config-connection-mode" : {
            "title" : "LDAP Connection Mode",
            "description" : "Defines which protocol/operation is used to establish the connection to the LDAP Directory Server.<br><br>If 'LDAP' is selected, the connection <b>won't be secured</b> and passwords are transferred in <b>cleartext</b> over the network.<br/> If 'LDAPS' is selected, the connection is secured via SSL or TLS. <br/> If 'StartTLS' is selected, the connection is secured by using StartTLS extended operation.",
            "propertyOrder" : 1000,
            "required" : false,
            "type" : "string",
            "exampleValue" : ""
          },
          "openam-idrepo-ldapv3-keepalive-searchfilter" : {
            "title" : "LDAP Connection Heartbeat Search Filter",
            "description" : "Defines the search filter to the KeepAlive and Availability Search request.<br><br>This setting controls the search filter to the KeepAlive and Availability search request. The default value for search filter is \"(objectClass=*)\". The Absolute True and False filter \"(&)\" can also be used. The LDAP server connection pool will be marked as unavailable if the search fails with an error, returns no entries, or if more than one entry is returned.",
            "propertyOrder" : 1302,
            "required" : false,
            "type" : "string",
            "exampleValue" : ""
          },
          "sun-idrepo-ldapv3-config-connection_pool_max_size" : {
            "title" : "LDAP Connection Pool Maximum Size",
            "description" : "",
            "propertyOrder" : 1200,
            "required" : false,
            "type" : "integer",
            "exampleValue" : ""
          },
          "openam-idrepo-ldapv3-heartbeat-interval" : {
            "title" : "LDAP Connection Heartbeat Interval",
            "description" : "Specifies how often should OpenAM send a heartbeat request to the directory.<br><br>This setting controls how often OpenAM <b>should</b> send a heartbeat search request to the configured directory. If a connection becomes unresponsive (e.g. due to a network error) then it may take up to the interval period before the problem is detected. Use along with the Heartbeat Time Unit parameter to define the exact interval. Zero or negative value will result in disabling heartbeat requests.",
            "propertyOrder" : 1300,
            "required" : false,
            "type" : "integer",
            "exampleValue" : ""
          },
          "openam-idrepo-ldapv3-affinity-level" : {
            "title" : "Affinity Level",
            "description" : "Level of affinity used to balance requests across IdRepo servers. Applies only if <code>Affinity Enabled</code> is on. Options are: no affinity, affinity for BIND requests only,  or affinity for all requests.",
            "propertyOrder" : 6350,
            "required" : false,
            "type" : "string",
            "exampleValue" : ""
          },
          "openam-idrepo-ldapv3-heartbeat-timeunit" : {
            "title" : "LDAP Connection Heartbeat Time Unit",
            "description" : "Defines the time unit corresponding to the Heartbeat Interval setting.<br><br>This setting controls how often OpenAM <b>should</b> send a heartbeat search request to the configured directory. If a connection becomes unresponsive (e.g. due to a network error) then it may take up to the interval period before the problem is detected. Use along with the Heartbeat Interval parameter to define the exact interval.",
            "propertyOrder" : 1400,
            "required" : false,
            "type" : "string",
            "exampleValue" : ""
          }
        }
      },
      "groupconfig" : {
        "type" : "object",
        "title" : "Group Configuration",
        "propertyOrder" : 5,
        "properties" : {
          "sun-idrepo-ldapv3-config-group-container-name" : {
            "title" : "LDAP Groups Container Naming Attribute",
            "description" : "",
            "propertyOrder" : 3100,
            "required" : false,
            "type" : "string",
            "exampleValue" : ""
          },
          "sun-idrepo-ldapv3-config-groups-search-attribute" : {
            "title" : "LDAP Groups Search Attribute",
            "description" : "",
            "propertyOrder" : 2900,
            "required" : false,
            "type" : "string",
            "exampleValue" : ""
          },
          "sun-idrepo-ldapv3-config-groups-search-filter" : {
            "title" : "LDAP Groups Search Filter",
            "description" : "",
            "propertyOrder" : 3000,
            "required" : false,
            "type" : "string",
            "exampleValue" : ""
          },
          "sun-idrepo-ldapv3-config-uniquemember" : {
            "title" : "Attribute Name of Unique Member",
            "description" : "",
            "propertyOrder" : 3600,
            "required" : false,
            "type" : "string",
            "exampleValue" : ""
          },
          "sun-idrepo-ldapv3-config-group-container-value" : {
            "title" : "LDAP Groups Container Value",
            "description" : "",
            "propertyOrder" : 3200,
            "required" : false,
            "type" : "string",
            "exampleValue" : ""
          },
          "adRecursiveGroupMembership" : {
            "title" : "AD Recursive Group Membership Evaluation",
            "description" : "Used to enable/disable Active Directory Recursive Group Membership evaluation.<br><br>Enables an Active Directory specific extensible filter called LDAP_MATCHING_RULE_IN_CHAIN that according to MSDN \"walks the chain of ancestry in objects all the way to the root until it finds a match\", meaning that it will resolve all group memberships, including nested groups. This will add a performance overhead on the Active Directory server, indexes may need to be created.",
            "propertyOrder" : 6100,
            "required" : true,
            "type" : "boolean",
            "exampleValue" : ""
          },
          "sun-idrepo-ldapv3-config-memberof" : {
            "title" : "Attribute Name for Group Membership",
            "description" : "",
            "propertyOrder" : 3500,
            "required" : false,
            "type" : "string",
            "exampleValue" : ""
          },
          "sun-idrepo-ldapv3-config-group-objectclass" : {
            "title" : "LDAP Groups Object Class",
            "description" : "",
            "propertyOrder" : 3300,
            "required" : false,
            "items" : {
              "type" : "string"
            },
            "type" : "array",
            "exampleValue" : ""
          },
          "sun-idrepo-ldapv3-config-group-attributes" : {
            "title" : "LDAP Groups Attributes",
            "description" : "",
            "propertyOrder" : 3400,
            "required" : false,
            "items" : {
              "type" : "string"
            },
            "type" : "array",
            "exampleValue" : ""
          }
        }
      },
      "persistentsearch" : {
        "type" : "object",
        "title" : "Persistent Search Controls",
        "propertyOrder" : 7,
        "properties" : {
          "sun-idrepo-ldapv3-config-psearchbase" : {
            "title" : "Persistent Search Base DN",
            "description" : "",
            "propertyOrder" : 5500,
            "required" : false,
            "type" : "string",
            "exampleValue" : ""
          },
          "sun-idrepo-ldapv3-config-psearch-scope" : {
            "title" : "Persistent Search Scope",
            "description" : "",
            "propertyOrder" : 5700,
            "required" : false,
            "type" : "string",
            "exampleValue" : ""
          }
        }
      },
      "cachecontrol" : {
        "type" : "object",
        "title" : "Cache Control",
        "propertyOrder" : 9,
        "properties" : {
          "sun-idrepo-ldapv3-dncache-enabled" : {
            "title" : "DN Cache",
            "description" : "Used to enable/disable the DN Cache within the OpenAM repository implementation.<br><br>The DN Cache is used to cache DN lookups which tend to happen in bursts during authentication. The DN Cache can become out of date when a user is moved or renamed in the underlying LDAP store and this is not reflected in a persistent search result. Enable when the underlying LDAP store supports persistent search and move/rename (mod_dn) results are available.",
            "propertyOrder" : 5900,
            "required" : false,
            "type" : "boolean",
            "exampleValue" : ""
          },
          "sun-idrepo-ldapv3-dncache-size" : {
            "title" : "DN Cache Size",
            "description" : "In DN items, only used when DN Cache is enabled.",
            "propertyOrder" : 6000,
            "required" : false,
            "type" : "integer",
            "exampleValue" : ""
          }
        }
      },
      "userconfig" : {
        "type" : "object",
        "title" : "User Configuration",
        "propertyOrder" : 3,
        "properties" : {
          "sun-idrepo-ldapv3-config-isactive" : {
            "title" : "Attribute Name of User Status",
            "description" : "",
            "propertyOrder" : 2600,
            "required" : false,
            "type" : "string",
            "exampleValue" : ""
          },
          "sun-idrepo-ldapv3-config-auth-kba-index-attr" : {
            "title" : "Knowledge Based Authentication Active Index",
            "description" : "",
            "propertyOrder" : 5400,
            "required" : false,
            "type" : "string",
            "exampleValue" : ""
          },
          "sun-idrepo-ldapv3-config-createuser-attr-mapping" : {
            "title" : "Create User Attribute Mapping",
            "description" : "Format: attribute name or TargetAttributeName=SourceAttributeName",
            "propertyOrder" : 2500,
            "required" : false,
            "items" : {
              "type" : "string"
            },
            "type" : "array",
            "exampleValue" : ""
          },
          "sun-idrepo-ldapv3-config-people-container-value" : {
            "title" : "LDAP People Container Value",
            "description" : "",
            "propertyOrder" : 5100,
            "required" : false,
            "type" : "string",
            "exampleValue" : ""
          },
          "sun-idrepo-ldapv3-config-active" : {
            "title" : "User Status Active Value",
            "description" : "",
            "propertyOrder" : 2700,
            "required" : false,
            "type" : "string",
            "exampleValue" : ""
          },
          "sun-idrepo-ldapv3-config-users-search-filter" : {
            "title" : "LDAP Users  Search Filter",
            "description" : "",
            "propertyOrder" : 2200,
            "required" : false,
            "type" : "string",
            "exampleValue" : ""
          },
          "sun-idrepo-ldapv3-config-people-container-name" : {
            "title" : "LDAP People Container Naming Attribute",
            "description" : "",
            "propertyOrder" : 5000,
            "required" : false,
            "type" : "string",
            "exampleValue" : ""
          },
          "sun-idrepo-ldapv3-config-user-attributes" : {
            "title" : "LDAP User Attributes",
            "description" : "",
            "propertyOrder" : 2400,
            "required" : false,
            "items" : {
              "type" : "string"
            },
            "type" : "array",
            "exampleValue" : ""
          },
          "sun-idrepo-ldapv3-config-user-objectclass" : {
            "title" : "LDAP User Object Class",
            "description" : "",
            "propertyOrder" : 2300,
            "required" : false,
            "items" : {
              "type" : "string"
            },
            "type" : "array",
            "exampleValue" : ""
          },
          "sun-idrepo-ldapv3-config-users-search-attribute" : {
            "title" : "LDAP Users  Search Attribute",
            "description" : "",
            "propertyOrder" : 2100,
            "required" : false,
            "type" : "string",
            "exampleValue" : ""
          },
          "sun-idrepo-ldapv3-config-inactive" : {
            "title" : "User Status Inactive Value",
            "description" : "",
            "propertyOrder" : 2800,
            "required" : false,
            "type" : "string",
            "exampleValue" : ""
          },
          "sun-idrepo-ldapv3-config-auth-kba-attr" : {
            "title" : "Knowledge Based Authentication Attribute Name",
            "description" : "",
            "propertyOrder" : 5300,
            "required" : false,
            "items" : {
              "type" : "string"
            },
            "type" : "array",
            "exampleValue" : ""
          },
          "sun-idrepo-ldapv3-config-auth-kba-attempts-attr" : {
            "title" : "Knowledge Based Authentication Attempts Attribute Name",
            "description" : "",
            "propertyOrder" : 5410,
            "required" : false,
            "items" : {
              "type" : "string"
            },
            "type" : "array",
            "exampleValue" : ""
          }
        }
      },
      "authentication" : {
        "type" : "object",
        "title" : "Authentication Configuration",
        "propertyOrder" : 4,
        "properties" : {
          "sun-idrepo-ldapv3-config-auth-naming-attr" : {
            "title" : "Authentication Naming Attribute",
            "description" : "",
            "propertyOrder" : 5200,
            "required" : false,
            "type" : "string",
            "exampleValue" : ""
          }
        }
      },
      "pluginconfig" : {
        "type" : "object",
        "title" : "Plug-in Configuration",
        "propertyOrder" : 2,
        "properties" : {
          "sunIdRepoClass" : {
            "title" : "LDAPv3 Repository Plug-in Class Name",
            "description" : "",
            "propertyOrder" : 1700,
            "required" : true,
            "type" : "string",
            "exampleValue" : ""
          },
          "sunIdRepoAttributeMapping" : {
            "title" : "Attribute Name Mapping",
            "description" : "",
            "propertyOrder" : 1800,
            "required" : false,
            "items" : {
              "type" : "string"
            },
            "type" : "array",
            "exampleValue" : ""
          },
          "sunIdRepoSupportedOperations" : {
            "title" : "LDAPv3 Plug-in Supported Types and Operations",
            "description" : "",
            "propertyOrder" : 1900,
            "required" : false,
            "items" : {
              "type" : "string"
            },
            "type" : "array",
            "exampleValue" : ""
          }
        }
      },
      "errorhandling" : {
        "type" : "object",
        "title" : "Error Handling Configuration",
        "propertyOrder" : 8,
        "properties" : {
          "com.iplanet.am.ldap.connection.delay.between.retries" : {
            "title" : "The Delay Time Between Retries",
            "description" : "In milliseconds.",
            "propertyOrder" : 5800,
            "required" : false,
            "type" : "integer",
            "exampleValue" : ""
          }
        }
      }
    }
  }
  ```

### delete

**Usage**

```
am> delete ActiveDirectoryApplicationModeADAM --realm Realm --id id
```

**Parameters**

* *\--id*

  The unique identifier for the resource.

### getAllTypes

Obtain the collection of all secondary configuration types related to the resource.

**Usage**

```
am> action ActiveDirectoryApplicationModeADAM --realm Realm --actionName getAllTypes
```

### getCreatableTypes

Obtain the collection of secondary configuration types that have yet to be added to the resource.

**Usage**

```
am> action ActiveDirectoryApplicationModeADAM --realm Realm --actionName getCreatableTypes
```

### nextdescendents

Obtain the collection of secondary configuration instances that have been added to the resource.

**Usage**

```
am> action ActiveDirectoryApplicationModeADAM --realm Realm --actionName nextdescendents
```

### query

Get the full list of instances of this collection. This query only supports `_queryFilter=true` filter.

**Usage**

```
am> query ActiveDirectoryApplicationModeADAM --realm Realm --filter filter
```

**Parameters**

* *\--filter*

  A CREST formatted query filter, where "true" will query all.

### read

**Usage**

```
am> read ActiveDirectoryApplicationModeADAM --realm Realm --id id
```

**Parameters**

* *\--id*

  The unique identifier for the resource.

### update

**Usage**

```
am> update ActiveDirectoryApplicationModeADAM --realm Realm --id id --body body
```

**Parameters**

* *\--id*

  The unique identifier for the resource.

* *\--body*

  The resource in JSON format, described by the following JSON schema:

  ```json
  {
    "type" : "object",
    "properties" : {
      "ldapsettings" : {
        "type" : "object",
        "title" : "Server Settings",
        "propertyOrder" : 0,
        "properties" : {
          "openam-idrepo-ldapv3-affinity-enabled" : {
            "title" : "Affinity Enabled",
            "description" : "Enables affinity based request load balancing when accessing the user store servers (based on DN). It is imperative that the connection string setting is set to the same value for all OpenAM servers in the deployment when this feature is enabled.",
            "propertyOrder" : 6200,
            "required" : true,
            "type" : "boolean",
            "exampleValue" : ""
          },
          "sun-idrepo-ldapv3-config-max-result" : {
            "title" : "Maximum Results Returned from Search",
            "description" : "",
            "propertyOrder" : 1500,
            "required" : false,
            "type" : "integer",
            "exampleValue" : ""
          },
          "openam-idrepo-ldapv3-keepalive-searchbase" : {
            "title" : "LDAP Connection Heartbeat Search Base",
            "description" : "Defines the search base to the KeepAlive and Availability Search request.<br><br>This setting controls the search base to the KeepAlive and Availability search request. The default value for search base DN is \"\". The LDAP server connection pool will be marked as unavailable if the search fails with an error, returns no entries, or if more than one entry is returned.",
            "propertyOrder" : 1301,
            "required" : false,
            "type" : "string",
            "exampleValue" : ""
          },
          "sun-idrepo-ldapv3-config-authpw" : {
            "title" : "LDAP Bind Password",
            "description" : "This property is ignored if mTLS Enabled is set.",
            "propertyOrder" : 800,
            "required" : false,
            "type" : "string",
            "format" : "password",
            "exampleValue" : ""
          },
          "sun-idrepo-ldapv3-config-ldap-server" : {
            "title" : "LDAP Server",
            "description" : "Format: LDAP server host name:port | server_ID | site_ID",
            "propertyOrder" : 600,
            "required" : true,
            "items" : {
              "type" : "string"
            },
            "minItems" : 1,
            "type" : "array",
            "exampleValue" : ""
          },
          "sun-idrepo-ldapv3-config-search-scope" : {
            "title" : "LDAPv3 Plug-in Search Scope",
            "description" : "",
            "propertyOrder" : 2000,
            "required" : false,
            "type" : "string",
            "exampleValue" : ""
          },
          "sun-idrepo-ldapv3-config-connection_pool_min_size" : {
            "title" : "LDAP Connection Pool Minimum Size",
            "description" : "",
            "propertyOrder" : 1100,
            "required" : false,
            "type" : "integer",
            "exampleValue" : ""
          },
          "sun-idrepo-ldapv3-config-authid" : {
            "title" : "LDAP Bind DN",
            "description" : "A user or admin with sufficient access rights to perform the supported operations. This property is ignored if mTLS Enabled is set.",
            "propertyOrder" : 700,
            "required" : false,
            "type" : "string",
            "exampleValue" : ""
          },
          "sun-idrepo-ldapv3-config-time-limit" : {
            "title" : "Search Timeout",
            "description" : "In seconds.",
            "propertyOrder" : 1600,
            "required" : false,
            "type" : "integer",
            "exampleValue" : ""
          },
          "sun-idrepo-ldapv3-config-organization_name" : {
            "title" : "LDAP Organization DN",
            "description" : "",
            "propertyOrder" : 900,
            "required" : true,
            "type" : "string",
            "exampleValue" : ""
          },
          "sun-idrepo-ldapv3-config-connection-mode" : {
            "title" : "LDAP Connection Mode",
            "description" : "Defines which protocol/operation is used to establish the connection to the LDAP Directory Server.<br><br>If 'LDAP' is selected, the connection <b>won't be secured</b> and passwords are transferred in <b>cleartext</b> over the network.<br/> If 'LDAPS' is selected, the connection is secured via SSL or TLS. <br/> If 'StartTLS' is selected, the connection is secured by using StartTLS extended operation.",
            "propertyOrder" : 1000,
            "required" : false,
            "type" : "string",
            "exampleValue" : ""
          },
          "openam-idrepo-ldapv3-keepalive-searchfilter" : {
            "title" : "LDAP Connection Heartbeat Search Filter",
            "description" : "Defines the search filter to the KeepAlive and Availability Search request.<br><br>This setting controls the search filter to the KeepAlive and Availability search request. The default value for search filter is \"(objectClass=*)\". The Absolute True and False filter \"(&)\" can also be used. The LDAP server connection pool will be marked as unavailable if the search fails with an error, returns no entries, or if more than one entry is returned.",
            "propertyOrder" : 1302,
            "required" : false,
            "type" : "string",
            "exampleValue" : ""
          },
          "sun-idrepo-ldapv3-config-connection_pool_max_size" : {
            "title" : "LDAP Connection Pool Maximum Size",
            "description" : "",
            "propertyOrder" : 1200,
            "required" : false,
            "type" : "integer",
            "exampleValue" : ""
          },
          "openam-idrepo-ldapv3-heartbeat-interval" : {
            "title" : "LDAP Connection Heartbeat Interval",
            "description" : "Specifies how often should OpenAM send a heartbeat request to the directory.<br><br>This setting controls how often OpenAM <b>should</b> send a heartbeat search request to the configured directory. If a connection becomes unresponsive (e.g. due to a network error) then it may take up to the interval period before the problem is detected. Use along with the Heartbeat Time Unit parameter to define the exact interval. Zero or negative value will result in disabling heartbeat requests.",
            "propertyOrder" : 1300,
            "required" : false,
            "type" : "integer",
            "exampleValue" : ""
          },
          "openam-idrepo-ldapv3-affinity-level" : {
            "title" : "Affinity Level",
            "description" : "Level of affinity used to balance requests across IdRepo servers. Applies only if <code>Affinity Enabled</code> is on. Options are: no affinity, affinity for BIND requests only,  or affinity for all requests.",
            "propertyOrder" : 6350,
            "required" : false,
            "type" : "string",
            "exampleValue" : ""
          },
          "openam-idrepo-ldapv3-heartbeat-timeunit" : {
            "title" : "LDAP Connection Heartbeat Time Unit",
            "description" : "Defines the time unit corresponding to the Heartbeat Interval setting.<br><br>This setting controls how often OpenAM <b>should</b> send a heartbeat search request to the configured directory. If a connection becomes unresponsive (e.g. due to a network error) then it may take up to the interval period before the problem is detected. Use along with the Heartbeat Interval parameter to define the exact interval.",
            "propertyOrder" : 1400,
            "required" : false,
            "type" : "string",
            "exampleValue" : ""
          }
        }
      },
      "groupconfig" : {
        "type" : "object",
        "title" : "Group Configuration",
        "propertyOrder" : 5,
        "properties" : {
          "sun-idrepo-ldapv3-config-group-container-name" : {
            "title" : "LDAP Groups Container Naming Attribute",
            "description" : "",
            "propertyOrder" : 3100,
            "required" : false,
            "type" : "string",
            "exampleValue" : ""
          },
          "sun-idrepo-ldapv3-config-groups-search-attribute" : {
            "title" : "LDAP Groups Search Attribute",
            "description" : "",
            "propertyOrder" : 2900,
            "required" : false,
            "type" : "string",
            "exampleValue" : ""
          },
          "sun-idrepo-ldapv3-config-groups-search-filter" : {
            "title" : "LDAP Groups Search Filter",
            "description" : "",
            "propertyOrder" : 3000,
            "required" : false,
            "type" : "string",
            "exampleValue" : ""
          },
          "sun-idrepo-ldapv3-config-uniquemember" : {
            "title" : "Attribute Name of Unique Member",
            "description" : "",
            "propertyOrder" : 3600,
            "required" : false,
            "type" : "string",
            "exampleValue" : ""
          },
          "sun-idrepo-ldapv3-config-group-container-value" : {
            "title" : "LDAP Groups Container Value",
            "description" : "",
            "propertyOrder" : 3200,
            "required" : false,
            "type" : "string",
            "exampleValue" : ""
          },
          "adRecursiveGroupMembership" : {
            "title" : "AD Recursive Group Membership Evaluation",
            "description" : "Used to enable/disable Active Directory Recursive Group Membership evaluation.<br><br>Enables an Active Directory specific extensible filter called LDAP_MATCHING_RULE_IN_CHAIN that according to MSDN \"walks the chain of ancestry in objects all the way to the root until it finds a match\", meaning that it will resolve all group memberships, including nested groups. This will add a performance overhead on the Active Directory server, indexes may need to be created.",
            "propertyOrder" : 6100,
            "required" : true,
            "type" : "boolean",
            "exampleValue" : ""
          },
          "sun-idrepo-ldapv3-config-memberof" : {
            "title" : "Attribute Name for Group Membership",
            "description" : "",
            "propertyOrder" : 3500,
            "required" : false,
            "type" : "string",
            "exampleValue" : ""
          },
          "sun-idrepo-ldapv3-config-group-objectclass" : {
            "title" : "LDAP Groups Object Class",
            "description" : "",
            "propertyOrder" : 3300,
            "required" : false,
            "items" : {
              "type" : "string"
            },
            "type" : "array",
            "exampleValue" : ""
          },
          "sun-idrepo-ldapv3-config-group-attributes" : {
            "title" : "LDAP Groups Attributes",
            "description" : "",
            "propertyOrder" : 3400,
            "required" : false,
            "items" : {
              "type" : "string"
            },
            "type" : "array",
            "exampleValue" : ""
          }
        }
      },
      "persistentsearch" : {
        "type" : "object",
        "title" : "Persistent Search Controls",
        "propertyOrder" : 7,
        "properties" : {
          "sun-idrepo-ldapv3-config-psearchbase" : {
            "title" : "Persistent Search Base DN",
            "description" : "",
            "propertyOrder" : 5500,
            "required" : false,
            "type" : "string",
            "exampleValue" : ""
          },
          "sun-idrepo-ldapv3-config-psearch-scope" : {
            "title" : "Persistent Search Scope",
            "description" : "",
            "propertyOrder" : 5700,
            "required" : false,
            "type" : "string",
            "exampleValue" : ""
          }
        }
      },
      "cachecontrol" : {
        "type" : "object",
        "title" : "Cache Control",
        "propertyOrder" : 9,
        "properties" : {
          "sun-idrepo-ldapv3-dncache-enabled" : {
            "title" : "DN Cache",
            "description" : "Used to enable/disable the DN Cache within the OpenAM repository implementation.<br><br>The DN Cache is used to cache DN lookups which tend to happen in bursts during authentication. The DN Cache can become out of date when a user is moved or renamed in the underlying LDAP store and this is not reflected in a persistent search result. Enable when the underlying LDAP store supports persistent search and move/rename (mod_dn) results are available.",
            "propertyOrder" : 5900,
            "required" : false,
            "type" : "boolean",
            "exampleValue" : ""
          },
          "sun-idrepo-ldapv3-dncache-size" : {
            "title" : "DN Cache Size",
            "description" : "In DN items, only used when DN Cache is enabled.",
            "propertyOrder" : 6000,
            "required" : false,
            "type" : "integer",
            "exampleValue" : ""
          }
        }
      },
      "userconfig" : {
        "type" : "object",
        "title" : "User Configuration",
        "propertyOrder" : 3,
        "properties" : {
          "sun-idrepo-ldapv3-config-isactive" : {
            "title" : "Attribute Name of User Status",
            "description" : "",
            "propertyOrder" : 2600,
            "required" : false,
            "type" : "string",
            "exampleValue" : ""
          },
          "sun-idrepo-ldapv3-config-auth-kba-index-attr" : {
            "title" : "Knowledge Based Authentication Active Index",
            "description" : "",
            "propertyOrder" : 5400,
            "required" : false,
            "type" : "string",
            "exampleValue" : ""
          },
          "sun-idrepo-ldapv3-config-createuser-attr-mapping" : {
            "title" : "Create User Attribute Mapping",
            "description" : "Format: attribute name or TargetAttributeName=SourceAttributeName",
            "propertyOrder" : 2500,
            "required" : false,
            "items" : {
              "type" : "string"
            },
            "type" : "array",
            "exampleValue" : ""
          },
          "sun-idrepo-ldapv3-config-people-container-value" : {
            "title" : "LDAP People Container Value",
            "description" : "",
            "propertyOrder" : 5100,
            "required" : false,
            "type" : "string",
            "exampleValue" : ""
          },
          "sun-idrepo-ldapv3-config-active" : {
            "title" : "User Status Active Value",
            "description" : "",
            "propertyOrder" : 2700,
            "required" : false,
            "type" : "string",
            "exampleValue" : ""
          },
          "sun-idrepo-ldapv3-config-users-search-filter" : {
            "title" : "LDAP Users  Search Filter",
            "description" : "",
            "propertyOrder" : 2200,
            "required" : false,
            "type" : "string",
            "exampleValue" : ""
          },
          "sun-idrepo-ldapv3-config-people-container-name" : {
            "title" : "LDAP People Container Naming Attribute",
            "description" : "",
            "propertyOrder" : 5000,
            "required" : false,
            "type" : "string",
            "exampleValue" : ""
          },
          "sun-idrepo-ldapv3-config-user-attributes" : {
            "title" : "LDAP User Attributes",
            "description" : "",
            "propertyOrder" : 2400,
            "required" : false,
            "items" : {
              "type" : "string"
            },
            "type" : "array",
            "exampleValue" : ""
          },
          "sun-idrepo-ldapv3-config-user-objectclass" : {
            "title" : "LDAP User Object Class",
            "description" : "",
            "propertyOrder" : 2300,
            "required" : false,
            "items" : {
              "type" : "string"
            },
            "type" : "array",
            "exampleValue" : ""
          },
          "sun-idrepo-ldapv3-config-users-search-attribute" : {
            "title" : "LDAP Users  Search Attribute",
            "description" : "",
            "propertyOrder" : 2100,
            "required" : false,
            "type" : "string",
            "exampleValue" : ""
          },
          "sun-idrepo-ldapv3-config-inactive" : {
            "title" : "User Status Inactive Value",
            "description" : "",
            "propertyOrder" : 2800,
            "required" : false,
            "type" : "string",
            "exampleValue" : ""
          },
          "sun-idrepo-ldapv3-config-auth-kba-attr" : {
            "title" : "Knowledge Based Authentication Attribute Name",
            "description" : "",
            "propertyOrder" : 5300,
            "required" : false,
            "items" : {
              "type" : "string"
            },
            "type" : "array",
            "exampleValue" : ""
          },
          "sun-idrepo-ldapv3-config-auth-kba-attempts-attr" : {
            "title" : "Knowledge Based Authentication Attempts Attribute Name",
            "description" : "",
            "propertyOrder" : 5410,
            "required" : false,
            "items" : {
              "type" : "string"
            },
            "type" : "array",
            "exampleValue" : ""
          }
        }
      },
      "authentication" : {
        "type" : "object",
        "title" : "Authentication Configuration",
        "propertyOrder" : 4,
        "properties" : {
          "sun-idrepo-ldapv3-config-auth-naming-attr" : {
            "title" : "Authentication Naming Attribute",
            "description" : "",
            "propertyOrder" : 5200,
            "required" : false,
            "type" : "string",
            "exampleValue" : ""
          }
        }
      },
      "pluginconfig" : {
        "type" : "object",
        "title" : "Plug-in Configuration",
        "propertyOrder" : 2,
        "properties" : {
          "sunIdRepoClass" : {
            "title" : "LDAPv3 Repository Plug-in Class Name",
            "description" : "",
            "propertyOrder" : 1700,
            "required" : true,
            "type" : "string",
            "exampleValue" : ""
          },
          "sunIdRepoAttributeMapping" : {
            "title" : "Attribute Name Mapping",
            "description" : "",
            "propertyOrder" : 1800,
            "required" : false,
            "items" : {
              "type" : "string"
            },
            "type" : "array",
            "exampleValue" : ""
          },
          "sunIdRepoSupportedOperations" : {
            "title" : "LDAPv3 Plug-in Supported Types and Operations",
            "description" : "",
            "propertyOrder" : 1900,
            "required" : false,
            "items" : {
              "type" : "string"
            },
            "type" : "array",
            "exampleValue" : ""
          }
        }
      },
      "errorhandling" : {
        "type" : "object",
        "title" : "Error Handling Configuration",
        "propertyOrder" : 8,
        "properties" : {
          "com.iplanet.am.ldap.connection.delay.between.retries" : {
            "title" : "The Delay Time Between Retries",
            "description" : "In milliseconds.",
            "propertyOrder" : 5800,
            "required" : false,
            "type" : "integer",
            "exampleValue" : ""
          }
        }
      }
    }
  }
  ```

---

---
title: ActiveDirectoryModule
description: Resource path:
component: pingam
version: 8.1
page_id: pingam:entity-reference:sec-amster-entity-activedirectorymodule
canonical_url: https://docs.pingidentity.com/pingam/8.1/entity-reference/sec-amster-entity-activedirectorymodule.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  sec-amster-entity-activedirectorymodule-realm-ops: Realm Operations
  sec-amster-entity-activedirectorymodule-realm-ops-create: create
  sec-amster-entity-activedirectorymodule-realm-ops-delete: delete
  sec-amster-entity-activedirectorymodule-realm-ops-getalltypes: getAllTypes
  sec-amster-entity-activedirectorymodule-realm-ops-getcreatabletypes: getCreatableTypes
  sec-amster-entity-activedirectorymodule-realm-ops-nextdescendents: nextdescendents
  sec-amster-entity-activedirectorymodule-realm-ops-query: query
  sec-amster-entity-activedirectorymodule-realm-ops-read: read
  sec-amster-entity-activedirectorymodule-realm-ops-update: update
  sec-amster-entity-activedirectorymodule-global-ops: Global Operations
  sec-amster-entity-activedirectorymodule-global-ops-getalltypes: getAllTypes
  sec-amster-entity-activedirectorymodule-global-ops-getcreatabletypes: getCreatableTypes
  sec-amster-entity-activedirectorymodule-global-ops-nextdescendents: nextdescendents
  sec-amster-entity-activedirectorymodule-global-ops-read: read
  sec-amster-entity-activedirectorymodule-global-ops-update: update
---

# ActiveDirectoryModule

## Realm Operations

Resource path:

```
/realm-config/authentication/modules/activedirectory
```

Resource version: `0.0`

### create

**Usage**

```
am> create ActiveDirectoryModule --realm Realm --id id --body body
```

**Parameters**

* *\--id*

  The unique identifier for the resource.

* *\--body*

  The resource in JSON format, described by the following JSON schema:

  ```json
  {
    "type" : "object",
    "properties" : {
      "searchScope" : {
        "title" : "Search Scope",
        "description" : "The level in the Directory Server that will be searched for a matching user profile.<br><br>This attribute controls how the directory is searched.<br/><br/><ul><li><code>OBJECT</code>: Only the Base DN is searched.</li><li><code>ONELEVEL</code>: Only the single level below (and not the Base DN) is searched</li><li><code>SUBTREE</code>: The Base DN and all levels below are searched</li></ul>",
        "propertyOrder" : 900,
        "required" : true,
        "type" : "string",
        "exampleValue" : ""
      },
      "userBindDN" : {
        "title" : "Bind User DN",
        "description" : "The DN of an admin user used by the module to authentication to the LDAP server<br><br>The LDAP module requires an administration account in order to perform functionality such as password reset.<br/><br/><i>NB </i><code>cn=Directory Manager</code> should not be used in production systems.",
        "propertyOrder" : 400,
        "required" : true,
        "type" : "string",
        "exampleValue" : ""
      },
      "stopLdapbindAfterInmemoryLockedEnabled" : {
        "title" : "Stop LDAP Binds after in-memory lockout",
        "description" : "If enabled, further bind requests will not be sent to LDAP Server when the user is locked-out using in-memory Account Lockout.",
        "propertyOrder" : 1900,
        "required" : true,
        "type" : "boolean",
        "exampleValue" : ""
      },
      "userBindPassword" : {
        "title" : "Bind User Password",
        "description" : "The password of the administration account.",
        "propertyOrder" : 500,
        "required" : true,
        "type" : "string",
        "format" : "password",
        "exampleValue" : ""
      },
      "authenticationLevel" : {
        "title" : "Authentication Level",
        "description" : "The authentication level associated with this module.<br><br>Each authentication module has an authentication level that can be used to indicate the level of security associated with the module; 0 is the lowest (and the default). ",
        "propertyOrder" : 1800,
        "required" : true,
        "type" : "integer",
        "exampleValue" : ""
      },
      "userProfileRetrievalAttribute" : {
        "title" : "Attribute Used to Retrieve User Profile",
        "description" : "The LDAP module will use this attribute to search of the profile of an authenticated user.<br><br>This is the attribute used to find the profile of the authenticated user. Normally this will be the same attribute used to find the user account. The value will be the name of the user used for authentication.",
        "propertyOrder" : 600,
        "required" : true,
        "type" : "string",
        "exampleValue" : ""
      },
      "connectionHeartbeatInterval" : {
        "title" : "LDAP Connection Heartbeat Interval",
        "description" : "Specifies how often should OpenAM send a heartbeat request to the directory.<br><br>Use this option in case a firewall/loadbalancer can close idle connections, since the heartbeat requests will ensure that the connections won't become idle. Use along with the Heartbeat Time Unit parameter to define the correct interval. Zero or negative value will result in disabling heartbeat requests.",
        "propertyOrder" : 1500,
        "required" : true,
        "type" : "integer",
        "exampleValue" : ""
      },
      "secondaryLdapServer" : {
        "title" : "Secondary Active Directory Server",
        "description" : "Use this list to set the secondary (failover) Active Directory server used for authentication.<br><br>If the primary Active Directory server fails, the Active Directory authentication module will failover to the secondary server. A single entry must be in the format:<br/><br/><code>server:port</code><br/><br/>Multiple entries allow associations between OpenAM servers and an Active Directory server. The format is:<br/><br/><code>local server name | server:port</code><br/><br/><i>NB </i>The local server name is the full name of the server from the list of servers and sites.",
        "propertyOrder" : 200,
        "required" : true,
        "items" : {
          "type" : "string"
        },
        "type" : "array",
        "exampleValue" : ""
      },
      "trustAllServerCertificates" : {
        "title" : "Trust All Server Certificates",
        "description" : "Enables a <code>X509TrustManager</code> that trusts all certificates.<br><br>This feature will allow the LDAP authentication module to connect to LDAP servers protected by self signed or invalid certificates (such as invalid hostname).<br/><br/><i>NB </i>Use this feature with care as it bypasses the normal certificate verification process",
        "propertyOrder" : 1400,
        "required" : true,
        "type" : "boolean",
        "exampleValue" : ""
      },
      "operationTimeout" : {
        "title" : "LDAP operations timeout",
        "description" : "Defines the timeout in seconds OpenAM should wait for a response of the Directory Server - <code>0</code> means no timeout.<br><br>If the Directory Server's host is down completely or the TCP connection became stale OpenAM waits until operation timeouts from the OS or the JVM are applied. However this setting allows more granular control within OpenAM itself. A value of <code>0</code> means NO timeout is applied on OpenAM level and the timeouts from the JVM or OS will apply.",
        "propertyOrder" : 1700,
        "required" : true,
        "type" : "integer",
        "exampleValue" : ""
      },
      "openam-auth-ldap-connection-mode" : {
        "title" : "LDAP Connection Mode",
        "description" : "Defines which protocol/operation is used to establish the connection to the LDAP Directory Server.<br><br>If 'LDAP' is selected, the connection <b>won't be secured</b> and passwords are transferred in <b>cleartext</b> over the network.<br/> If 'LDAPS' is selected, the connection is secured via SSL or TLS. <br/> If 'StartTLS' is selected, the connection is secured by using StartTLS extended operation.",
        "propertyOrder" : 1000,
        "required" : true,
        "type" : "string",
        "exampleValue" : ""
      },
      "returnUserDN" : {
        "title" : "Return User DN to DataStore",
        "description" : "Controls whether the DN or the username is returned as the authentication principal.",
        "propertyOrder" : 1200,
        "required" : true,
        "type" : "boolean",
        "exampleValue" : ""
      },
      "connectionHeartbeatTimeUnit" : {
        "title" : "LDAP Connection Heartbeat Time Unit",
        "description" : "Defines the time unit corresponding to the Heartbeat Interval setting.<br><br>Use this option in case a firewall/loadbalancer can close idle connections, since the heartbeat requests will ensure that the connections won't become idle.",
        "propertyOrder" : 1600,
        "required" : true,
        "type" : "string",
        "exampleValue" : ""
      },
      "profileAttributeMappings" : {
        "title" : "User Creation Attributes",
        "description" : "Controls the mapping of local attribute to external attribute for dynamic profile creation.<br><br>If dynamic profile creation is enabled; this feature allows for a mapping between the attribute/values retrieved from the users authenticated profile and the attribute/values that will be provisioned into their matching account in the data store.<br/><br/>The format of this property is: <br/><br/><code> local attr1|external attr1</code>",
        "propertyOrder" : 1300,
        "required" : true,
        "items" : {
          "type" : "string"
        },
        "type" : "array",
        "exampleValue" : ""
      },
      "userSearchStartDN" : {
        "title" : "DN to Start User Search",
        "description" : "The search for accounts to be authenticated start from this base DN <br><br>For a single server just enter the Base DN to be searched. Multiple OpenAM servers can have different base DNs for the search The format is as follows:<br/><br/><code>local server name | search DN</code><br/><br/><i>NB </i>The local server name is the full name of the server from the list of servers and sites.",
        "propertyOrder" : 300,
        "required" : true,
        "items" : {
          "type" : "string"
        },
        "type" : "array",
        "exampleValue" : ""
      },
      "userSearchAttributes" : {
        "title" : "Attributes Used to Search for a User to be Authenticated",
        "description" : "The attributes specified in this list form the LDAP search filter.<br><br>The default value of uid will form the following search filter of <code>uid=<i>user</i></code>, if there are multiple values such as uid and cn, the module will create a search filter as follows <code>(|(uid=<i>user</i>)(cn=<i>user</i>))</code>",
        "propertyOrder" : 700,
        "required" : true,
        "items" : {
          "type" : "string"
        },
        "type" : "array",
        "exampleValue" : ""
      },
      "primaryLdapServer" : {
        "title" : "Primary Active Directory Server ",
        "description" : "Use this list to set the primary Active Directory server used for authentication. <br><br>The Active Directory authentication module will use this list as the primary server for authentication. A single entry must be in the format:<br/><br/><code>server:port</code><br/><br/>Multiple entries allow associations between OpenAM servers and an Active Directory server. The format is:<br/><br/><code>local server name | server:port</code><br/><br/>The local server name is the full name of the server from the list of servers and sites.",
        "propertyOrder" : 100,
        "required" : true,
        "items" : {
          "type" : "string"
        },
        "type" : "array",
        "exampleValue" : ""
      },
      "userSearchFilter" : {
        "title" : "User Search Filter",
        "description" : "This search filter will be appended to the standard user search filter.<br><br>This attribute can be used to append a custom search filter to the standard filter. For example: <code>(objectClass=person)</code>would result in the following user search filter:<br/><br/><code>(&(uid=<i>user</i>)(objectClass=person))</code>",
        "propertyOrder" : 800,
        "required" : true,
        "type" : "string",
        "exampleValue" : ""
      }
    }
  }
  ```

### delete

**Usage**

```
am> delete ActiveDirectoryModule --realm Realm --id id
```

**Parameters**

* *\--id*

  The unique identifier for the resource.

### getAllTypes

Obtain the collection of all secondary configuration types related to the resource.

**Usage**

```
am> action ActiveDirectoryModule --realm Realm --actionName getAllTypes
```

### getCreatableTypes

Obtain the collection of secondary configuration types that have yet to be added to the resource.

**Usage**

```
am> action ActiveDirectoryModule --realm Realm --actionName getCreatableTypes
```

### nextdescendents

Obtain the collection of secondary configuration instances that have been added to the resource.

**Usage**

```
am> action ActiveDirectoryModule --realm Realm --actionName nextdescendents
```

### query

Get the full list of instances of this collection. This query only supports `_queryFilter=true` filter.

**Usage**

```
am> query ActiveDirectoryModule --realm Realm --filter filter
```

**Parameters**

* *\--filter*

  A CREST formatted query filter, where "true" will query all.

### read

**Usage**

```
am> read ActiveDirectoryModule --realm Realm --id id
```

**Parameters**

* *\--id*

  The unique identifier for the resource.

### update

**Usage**

```
am> update ActiveDirectoryModule --realm Realm --id id --body body
```

**Parameters**

* *\--id*

  The unique identifier for the resource.

* *\--body*

  The resource in JSON format, described by the following JSON schema:

  ```json
  {
    "type" : "object",
    "properties" : {
      "searchScope" : {
        "title" : "Search Scope",
        "description" : "The level in the Directory Server that will be searched for a matching user profile.<br><br>This attribute controls how the directory is searched.<br/><br/><ul><li><code>OBJECT</code>: Only the Base DN is searched.</li><li><code>ONELEVEL</code>: Only the single level below (and not the Base DN) is searched</li><li><code>SUBTREE</code>: The Base DN and all levels below are searched</li></ul>",
        "propertyOrder" : 900,
        "required" : true,
        "type" : "string",
        "exampleValue" : ""
      },
      "userBindDN" : {
        "title" : "Bind User DN",
        "description" : "The DN of an admin user used by the module to authentication to the LDAP server<br><br>The LDAP module requires an administration account in order to perform functionality such as password reset.<br/><br/><i>NB </i><code>cn=Directory Manager</code> should not be used in production systems.",
        "propertyOrder" : 400,
        "required" : true,
        "type" : "string",
        "exampleValue" : ""
      },
      "stopLdapbindAfterInmemoryLockedEnabled" : {
        "title" : "Stop LDAP Binds after in-memory lockout",
        "description" : "If enabled, further bind requests will not be sent to LDAP Server when the user is locked-out using in-memory Account Lockout.",
        "propertyOrder" : 1900,
        "required" : true,
        "type" : "boolean",
        "exampleValue" : ""
      },
      "userBindPassword" : {
        "title" : "Bind User Password",
        "description" : "The password of the administration account.",
        "propertyOrder" : 500,
        "required" : true,
        "type" : "string",
        "format" : "password",
        "exampleValue" : ""
      },
      "authenticationLevel" : {
        "title" : "Authentication Level",
        "description" : "The authentication level associated with this module.<br><br>Each authentication module has an authentication level that can be used to indicate the level of security associated with the module; 0 is the lowest (and the default). ",
        "propertyOrder" : 1800,
        "required" : true,
        "type" : "integer",
        "exampleValue" : ""
      },
      "userProfileRetrievalAttribute" : {
        "title" : "Attribute Used to Retrieve User Profile",
        "description" : "The LDAP module will use this attribute to search of the profile of an authenticated user.<br><br>This is the attribute used to find the profile of the authenticated user. Normally this will be the same attribute used to find the user account. The value will be the name of the user used for authentication.",
        "propertyOrder" : 600,
        "required" : true,
        "type" : "string",
        "exampleValue" : ""
      },
      "connectionHeartbeatInterval" : {
        "title" : "LDAP Connection Heartbeat Interval",
        "description" : "Specifies how often should OpenAM send a heartbeat request to the directory.<br><br>Use this option in case a firewall/loadbalancer can close idle connections, since the heartbeat requests will ensure that the connections won't become idle. Use along with the Heartbeat Time Unit parameter to define the correct interval. Zero or negative value will result in disabling heartbeat requests.",
        "propertyOrder" : 1500,
        "required" : true,
        "type" : "integer",
        "exampleValue" : ""
      },
      "secondaryLdapServer" : {
        "title" : "Secondary Active Directory Server",
        "description" : "Use this list to set the secondary (failover) Active Directory server used for authentication.<br><br>If the primary Active Directory server fails, the Active Directory authentication module will failover to the secondary server. A single entry must be in the format:<br/><br/><code>server:port</code><br/><br/>Multiple entries allow associations between OpenAM servers and an Active Directory server. The format is:<br/><br/><code>local server name | server:port</code><br/><br/><i>NB </i>The local server name is the full name of the server from the list of servers and sites.",
        "propertyOrder" : 200,
        "required" : true,
        "items" : {
          "type" : "string"
        },
        "type" : "array",
        "exampleValue" : ""
      },
      "trustAllServerCertificates" : {
        "title" : "Trust All Server Certificates",
        "description" : "Enables a <code>X509TrustManager</code> that trusts all certificates.<br><br>This feature will allow the LDAP authentication module to connect to LDAP servers protected by self signed or invalid certificates (such as invalid hostname).<br/><br/><i>NB </i>Use this feature with care as it bypasses the normal certificate verification process",
        "propertyOrder" : 1400,
        "required" : true,
        "type" : "boolean",
        "exampleValue" : ""
      },
      "operationTimeout" : {
        "title" : "LDAP operations timeout",
        "description" : "Defines the timeout in seconds OpenAM should wait for a response of the Directory Server - <code>0</code> means no timeout.<br><br>If the Directory Server's host is down completely or the TCP connection became stale OpenAM waits until operation timeouts from the OS or the JVM are applied. However this setting allows more granular control within OpenAM itself. A value of <code>0</code> means NO timeout is applied on OpenAM level and the timeouts from the JVM or OS will apply.",
        "propertyOrder" : 1700,
        "required" : true,
        "type" : "integer",
        "exampleValue" : ""
      },
      "openam-auth-ldap-connection-mode" : {
        "title" : "LDAP Connection Mode",
        "description" : "Defines which protocol/operation is used to establish the connection to the LDAP Directory Server.<br><br>If 'LDAP' is selected, the connection <b>won't be secured</b> and passwords are transferred in <b>cleartext</b> over the network.<br/> If 'LDAPS' is selected, the connection is secured via SSL or TLS. <br/> If 'StartTLS' is selected, the connection is secured by using StartTLS extended operation.",
        "propertyOrder" : 1000,
        "required" : true,
        "type" : "string",
        "exampleValue" : ""
      },
      "returnUserDN" : {
        "title" : "Return User DN to DataStore",
        "description" : "Controls whether the DN or the username is returned as the authentication principal.",
        "propertyOrder" : 1200,
        "required" : true,
        "type" : "boolean",
        "exampleValue" : ""
      },
      "connectionHeartbeatTimeUnit" : {
        "title" : "LDAP Connection Heartbeat Time Unit",
        "description" : "Defines the time unit corresponding to the Heartbeat Interval setting.<br><br>Use this option in case a firewall/loadbalancer can close idle connections, since the heartbeat requests will ensure that the connections won't become idle.",
        "propertyOrder" : 1600,
        "required" : true,
        "type" : "string",
        "exampleValue" : ""
      },
      "profileAttributeMappings" : {
        "title" : "User Creation Attributes",
        "description" : "Controls the mapping of local attribute to external attribute for dynamic profile creation.<br><br>If dynamic profile creation is enabled; this feature allows for a mapping between the attribute/values retrieved from the users authenticated profile and the attribute/values that will be provisioned into their matching account in the data store.<br/><br/>The format of this property is: <br/><br/><code> local attr1|external attr1</code>",
        "propertyOrder" : 1300,
        "required" : true,
        "items" : {
          "type" : "string"
        },
        "type" : "array",
        "exampleValue" : ""
      },
      "userSearchStartDN" : {
        "title" : "DN to Start User Search",
        "description" : "The search for accounts to be authenticated start from this base DN <br><br>For a single server just enter the Base DN to be searched. Multiple OpenAM servers can have different base DNs for the search The format is as follows:<br/><br/><code>local server name | search DN</code><br/><br/><i>NB </i>The local server name is the full name of the server from the list of servers and sites.",
        "propertyOrder" : 300,
        "required" : true,
        "items" : {
          "type" : "string"
        },
        "type" : "array",
        "exampleValue" : ""
      },
      "userSearchAttributes" : {
        "title" : "Attributes Used to Search for a User to be Authenticated",
        "description" : "The attributes specified in this list form the LDAP search filter.<br><br>The default value of uid will form the following search filter of <code>uid=<i>user</i></code>, if there are multiple values such as uid and cn, the module will create a search filter as follows <code>(|(uid=<i>user</i>)(cn=<i>user</i>))</code>",
        "propertyOrder" : 700,
        "required" : true,
        "items" : {
          "type" : "string"
        },
        "type" : "array",
        "exampleValue" : ""
      },
      "primaryLdapServer" : {
        "title" : "Primary Active Directory Server ",
        "description" : "Use this list to set the primary Active Directory server used for authentication. <br><br>The Active Directory authentication module will use this list as the primary server for authentication. A single entry must be in the format:<br/><br/><code>server:port</code><br/><br/>Multiple entries allow associations between OpenAM servers and an Active Directory server. The format is:<br/><br/><code>local server name | server:port</code><br/><br/>The local server name is the full name of the server from the list of servers and sites.",
        "propertyOrder" : 100,
        "required" : true,
        "items" : {
          "type" : "string"
        },
        "type" : "array",
        "exampleValue" : ""
      },
      "userSearchFilter" : {
        "title" : "User Search Filter",
        "description" : "This search filter will be appended to the standard user search filter.<br><br>This attribute can be used to append a custom search filter to the standard filter. For example: <code>(objectClass=person)</code>would result in the following user search filter:<br/><br/><code>(&(uid=<i>user</i>)(objectClass=person))</code>",
        "propertyOrder" : 800,
        "required" : true,
        "type" : "string",
        "exampleValue" : ""
      }
    }
  }
  ```

## Global Operations

Resource path:

```
/global-config/authentication/modules/activedirectory
```

Resource version: `1.0`

### getAllTypes

Obtain the collection of all secondary configuration types related to the resource.

**Usage**

```
am> action ActiveDirectoryModule --global --actionName getAllTypes
```

### getCreatableTypes

Obtain the collection of secondary configuration types that have yet to be added to the resource.

**Usage**

```
am> action ActiveDirectoryModule --global --actionName getCreatableTypes
```

### nextdescendents

Obtain the collection of secondary configuration instances that have been added to the resource.

**Usage**

```
am> action ActiveDirectoryModule --global --actionName nextdescendents
```

### read

**Usage**

```
am> read ActiveDirectoryModule --global
```

### update

**Usage**

```
am> update ActiveDirectoryModule --global --body body
```

**Parameters**

* *\--body*

  The resource in JSON format, described by the following JSON schema:

  ```json
  {
    "type" : "object",
    "properties" : {
      "defaults" : {
        "properties" : {
          "userSearchFilter" : {
            "title" : "User Search Filter",
            "description" : "This search filter will be appended to the standard user search filter.<br><br>This attribute can be used to append a custom search filter to the standard filter. For example: <code>(objectClass=person)</code>would result in the following user search filter:<br/><br/><code>(&(uid=<i>user</i>)(objectClass=person))</code>",
            "propertyOrder" : 800,
            "required" : true,
            "type" : "string",
            "exampleValue" : ""
          },
          "connectionHeartbeatTimeUnit" : {
            "title" : "LDAP Connection Heartbeat Time Unit",
            "description" : "Defines the time unit corresponding to the Heartbeat Interval setting.<br><br>Use this option in case a firewall/loadbalancer can close idle connections, since the heartbeat requests will ensure that the connections won't become idle.",
            "propertyOrder" : 1600,
            "required" : true,
            "type" : "string",
            "exampleValue" : ""
          },
          "authenticationLevel" : {
            "title" : "Authentication Level",
            "description" : "The authentication level associated with this module.<br><br>Each authentication module has an authentication level that can be used to indicate the level of security associated with the module; 0 is the lowest (and the default). ",
            "propertyOrder" : 1800,
            "required" : true,
            "type" : "integer",
            "exampleValue" : ""
          },
          "searchScope" : {
            "title" : "Search Scope",
            "description" : "The level in the Directory Server that will be searched for a matching user profile.<br><br>This attribute controls how the directory is searched.<br/><br/><ul><li><code>OBJECT</code>: Only the Base DN is searched.</li><li><code>ONELEVEL</code>: Only the single level below (and not the Base DN) is searched</li><li><code>SUBTREE</code>: The Base DN and all levels below are searched</li></ul>",
            "propertyOrder" : 900,
            "required" : true,
            "type" : "string",
            "exampleValue" : ""
          },
          "openam-auth-ldap-connection-mode" : {
            "title" : "LDAP Connection Mode",
            "description" : "Defines which protocol/operation is used to establish the connection to the LDAP Directory Server.<br><br>If 'LDAP' is selected, the connection <b>won't be secured</b> and passwords are transferred in <b>cleartext</b> over the network.<br/> If 'LDAPS' is selected, the connection is secured via SSL or TLS. <br/> If 'StartTLS' is selected, the connection is secured by using StartTLS extended operation.",
            "propertyOrder" : 1000,
            "required" : true,
            "type" : "string",
            "exampleValue" : ""
          },
          "userSearchStartDN" : {
            "title" : "DN to Start User Search",
            "description" : "The search for accounts to be authenticated start from this base DN <br><br>For a single server just enter the Base DN to be searched. Multiple OpenAM servers can have different base DNs for the search The format is as follows:<br/><br/><code>local server name | search DN</code><br/><br/><i>NB </i>The local server name is the full name of the server from the list of servers and sites.",
            "propertyOrder" : 300,
            "required" : true,
            "items" : {
              "type" : "string"
            },
            "type" : "array",
            "exampleValue" : ""
          },
          "stopLdapbindAfterInmemoryLockedEnabled" : {
            "title" : "Stop LDAP Binds after in-memory lockout",
            "description" : "If enabled, further bind requests will not be sent to LDAP Server when the user is locked-out using in-memory Account Lockout.",
            "propertyOrder" : 1900,
            "required" : true,
            "type" : "boolean",
            "exampleValue" : ""
          },
          "trustAllServerCertificates" : {
            "title" : "Trust All Server Certificates",
            "description" : "Enables a <code>X509TrustManager</code> that trusts all certificates.<br><br>This feature will allow the LDAP authentication module to connect to LDAP servers protected by self signed or invalid certificates (such as invalid hostname).<br/><br/><i>NB </i>Use this feature with care as it bypasses the normal certificate verification process",
            "propertyOrder" : 1400,
            "required" : true,
            "type" : "boolean",
            "exampleValue" : ""
          },
          "connectionHeartbeatInterval" : {
            "title" : "LDAP Connection Heartbeat Interval",
            "description" : "Specifies how often should OpenAM send a heartbeat request to the directory.<br><br>Use this option in case a firewall/loadbalancer can close idle connections, since the heartbeat requests will ensure that the connections won't become idle. Use along with the Heartbeat Time Unit parameter to define the correct interval. Zero or negative value will result in disabling heartbeat requests.",
            "propertyOrder" : 1500,
            "required" : true,
            "type" : "integer",
            "exampleValue" : ""
          },
          "userBindDN" : {
            "title" : "Bind User DN",
            "description" : "The DN of an admin user used by the module to authentication to the LDAP server<br><br>The LDAP module requires an administration account in order to perform functionality such as password reset.<br/><br/><i>NB </i><code>cn=Directory Manager</code> should not be used in production systems.",
            "propertyOrder" : 400,
            "required" : true,
            "type" : "string",
            "exampleValue" : ""
          },
          "operationTimeout" : {
            "title" : "LDAP operations timeout",
            "description" : "Defines the timeout in seconds OpenAM should wait for a response of the Directory Server - <code>0</code> means no timeout.<br><br>If the Directory Server's host is down completely or the TCP connection became stale OpenAM waits until operation timeouts from the OS or the JVM are applied. However this setting allows more granular control within OpenAM itself. A value of <code>0</code> means NO timeout is applied on OpenAM level and the timeouts from the JVM or OS will apply.",
            "propertyOrder" : 1700,
            "required" : true,
            "type" : "integer",
            "exampleValue" : ""
          },
          "profileAttributeMappings" : {
            "title" : "User Creation Attributes",
            "description" : "Controls the mapping of local attribute to external attribute for dynamic profile creation.<br><br>If dynamic profile creation is enabled; this feature allows for a mapping between the attribute/values retrieved from the users authenticated profile and the attribute/values that will be provisioned into their matching account in the data store.<br/><br/>The format of this property is: <br/><br/><code> local attr1|external attr1</code>",
            "propertyOrder" : 1300,
            "required" : true,
            "items" : {
              "type" : "string"
            },
            "type" : "array",
            "exampleValue" : ""
          },
          "secondaryLdapServer" : {
            "title" : "Secondary Active Directory Server",
            "description" : "Use this list to set the secondary (failover) Active Directory server used for authentication.<br><br>If the primary Active Directory server fails, the Active Directory authentication module will failover to the secondary server. A single entry must be in the format:<br/><br/><code>server:port</code><br/><br/>Multiple entries allow associations between OpenAM servers and an Active Directory server. The format is:<br/><br/><code>local server name | server:port</code><br/><br/><i>NB </i>The local server name is the full name of the server from the list of servers and sites.",
            "propertyOrder" : 200,
            "required" : true,
            "items" : {
              "type" : "string"
            },
            "type" : "array",
            "exampleValue" : ""
          },
          "userProfileRetrievalAttribute" : {
            "title" : "Attribute Used to Retrieve User Profile",
            "description" : "The LDAP module will use this attribute to search of the profile of an authenticated user.<br><br>This is the attribute used to find the profile of the authenticated user. Normally this will be the same attribute used to find the user account. The value will be the name of the user used for authentication.",
            "propertyOrder" : 600,
            "required" : true,
            "type" : "string",
            "exampleValue" : ""
          },
          "primaryLdapServer" : {
            "title" : "Primary Active Directory Server ",
            "description" : "Use this list to set the primary Active Directory server used for authentication. <br><br>The Active Directory authentication module will use this list as the primary server for authentication. A single entry must be in the format:<br/><br/><code>server:port</code><br/><br/>Multiple entries allow associations between OpenAM servers and an Active Directory server. The format is:<br/><br/><code>local server name | server:port</code><br/><br/>The local server name is the full name of the server from the list of servers and sites.",
            "propertyOrder" : 100,
            "required" : true,
            "items" : {
              "type" : "string"
            },
            "type" : "array",
            "exampleValue" : ""
          },
          "returnUserDN" : {
            "title" : "Return User DN to DataStore",
            "description" : "Controls whether the DN or the username is returned as the authentication principal.",
            "propertyOrder" : 1200,
            "required" : true,
            "type" : "boolean",
            "exampleValue" : ""
          },
          "userBindPassword" : {
            "title" : "Bind User Password",
            "description" : "The password of the administration account.",
            "propertyOrder" : 500,
            "required" : true,
            "type" : "string",
            "format" : "password",
            "exampleValue" : ""
          },
          "userSearchAttributes" : {
            "title" : "Attributes Used to Search for a User to be Authenticated",
            "description" : "The attributes specified in this list form the LDAP search filter.<br><br>The default value of uid will form the following search filter of <code>uid=<i>user</i></code>, if there are multiple values such as uid and cn, the module will create a search filter as follows <code>(|(uid=<i>user</i>)(cn=<i>user</i>))</code>",
            "propertyOrder" : 700,
            "required" : true,
            "items" : {
              "type" : "string"
            },
            "type" : "array",
            "exampleValue" : ""
          }
        },
        "type" : "object",
        "title" : "Realm Defaults"
      }
    }
  }
  ```

---

---
title: AdaptiveRiskModule
description: Resource path:
component: pingam
version: 8.1
page_id: pingam:entity-reference:sec-amster-entity-adaptiveriskmodule
canonical_url: https://docs.pingidentity.com/pingam/8.1/entity-reference/sec-amster-entity-adaptiveriskmodule.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  sec-amster-entity-adaptiveriskmodule-realm-ops: Realm Operations
  sec-amster-entity-adaptiveriskmodule-realm-ops-create: create
  sec-amster-entity-adaptiveriskmodule-realm-ops-delete: delete
  sec-amster-entity-adaptiveriskmodule-realm-ops-getalltypes: getAllTypes
  sec-amster-entity-adaptiveriskmodule-realm-ops-getcreatabletypes: getCreatableTypes
  sec-amster-entity-adaptiveriskmodule-realm-ops-nextdescendents: nextdescendents
  sec-amster-entity-adaptiveriskmodule-realm-ops-query: query
  sec-amster-entity-adaptiveriskmodule-realm-ops-read: read
  sec-amster-entity-adaptiveriskmodule-realm-ops-update: update
  sec-amster-entity-adaptiveriskmodule-global-ops: Global Operations
  sec-amster-entity-adaptiveriskmodule-global-ops-getalltypes: getAllTypes
  sec-amster-entity-adaptiveriskmodule-global-ops-getcreatabletypes: getCreatableTypes
  sec-amster-entity-adaptiveriskmodule-global-ops-nextdescendents: nextdescendents
  sec-amster-entity-adaptiveriskmodule-global-ops-read: read
  sec-amster-entity-adaptiveriskmodule-global-ops-update: update
---

# AdaptiveRiskModule

## Realm Operations

Resource path:

```
/realm-config/authentication/modules/adaptiverisk
```

Resource version: `0.0`

### create

**Usage**

```
am> create AdaptiveRiskModule --realm Realm --id id --body body
```

**Parameters**

* *\--id*

  The unique identifier for the resource.

* *\--body*

  The resource in JSON format, described by the following JSON schema:

  ```json
  {
    "type" : "object",
    "properties" : {
      "lastlogin" : {
        "type" : "object",
        "title" : "Time Since Last Login",
        "propertyOrder" : 6,
        "properties" : {
          "saveLastLoginTimeOnSuccessfulLogin" : {
            "title" : "Save time of Successful Login",
            "description" : "The last login time will be saved in a client cookie<br><br>The Adaptive Risk Post Authentication Plug-in will update the last login time",
            "propertyOrder" : 2500,
            "required" : true,
            "type" : "boolean",
            "exampleValue" : ""
          },
          "timeSinceLastLoginCheckEnabled" : {
            "title" : "Time since Last login Check",
            "description" : "Enables the checking of the last time the user successfully authenticated.<br><br>If this check is enabled, the check ensures the user has successfully authenticated within a given interval. If the interval has been exceeded the check will fail. The last authentication for the user is stored in a client cookie.",
            "propertyOrder" : 2200,
            "required" : true,
            "type" : "boolean",
            "exampleValue" : ""
          },
          "timeSinceLastLoginScore" : {
            "title" : "Score",
            "description" : "The amount to increment the score if this check fails.",
            "propertyOrder" : 2600,
            "required" : true,
            "type" : "integer",
            "exampleValue" : ""
          },
          "timeSinceLastLoginCookieName" : {
            "title" : "Cookie Name",
            "description" : "The name of the cookie used to store the time of the last successful authentication.",
            "propertyOrder" : 2300,
            "required" : true,
            "type" : "string",
            "exampleValue" : ""
          },
          "maxTimeSinceLastLogin" : {
            "title" : "Max Time since Last login",
            "description" : "The maximum number of days that can elapse before this test.",
            "propertyOrder" : 2400,
            "required" : true,
            "type" : "string",
            "exampleValue" : ""
          },
          "invertTimeSinceLastLoginScore" : {
            "title" : "Invert Result",
            "description" : "If the check succeeds the score will be included in the total, for failure the score will not be incremented.",
            "propertyOrder" : 2700,
            "required" : true,
            "type" : "boolean",
            "exampleValue" : ""
          }
        }
      },
      "attributecheck" : {
        "type" : "object",
        "title" : "Profile Attribute",
        "propertyOrder" : 7,
        "properties" : {
          "invertProfileRiskAttributeScore" : {
            "title" : "Invert Result",
            "description" : "If the check succeeds the score will be included in the total, for failure the score will not be incremented.",
            "propertyOrder" : 3200,
            "required" : true,
            "type" : "boolean",
            "exampleValue" : ""
          },
          "profileRiskAttributeCheckEnabled" : {
            "title" : "Profile Risk Attribute check",
            "description" : "Enables the checking of the user profile for a matching attribute and value.<br><br>If this check is enabled, the check will pass if the users profile contains the required risk attribute and value.",
            "propertyOrder" : 2800,
            "required" : true,
            "type" : "boolean",
            "exampleValue" : ""
          },
          "profileRiskAttributeName" : {
            "title" : "Attribute Name",
            "description" : "The name of the attribute to retrieve from the user profile in the data store.",
            "propertyOrder" : 2900,
            "required" : true,
            "type" : "string",
            "exampleValue" : ""
          },
          "profileRiskAttributeValue" : {
            "title" : "Attribute Value",
            "description" : "The required value of the named attribute.",
            "propertyOrder" : 3000,
            "required" : true,
            "type" : "string",
            "exampleValue" : ""
          },
          "profileRiskAttributeScore" : {
            "title" : "Score",
            "description" : "The amount to increment the score if this check fails.",
            "propertyOrder" : 3100,
            "required" : true,
            "type" : "integer",
            "exampleValue" : ""
          }
        }
      },
      "devicecookie" : {
        "type" : "object",
        "title" : "Device Cookie",
        "propertyOrder" : 5,
        "properties" : {
          "deviceCookieName" : {
            "title" : "Cookie Name",
            "description" : "The name of the cookie to be checked for (and optionally set) on the client request",
            "propertyOrder" : 3400,
            "required" : true,
            "type" : "string",
            "exampleValue" : ""
          },
          "invertDeviceCookieScore" : {
            "title" : "Invert Result",
            "description" : "If the check succeeds the score will be included in the total, for failure the score will not be incremented.",
            "propertyOrder" : 3700,
            "required" : true,
            "type" : "boolean",
            "exampleValue" : ""
          },
          "deviceCookieScore" : {
            "title" : "Score",
            "description" : "The amount to increment the score if this check fails.",
            "propertyOrder" : 3600,
            "required" : true,
            "type" : "integer",
            "exampleValue" : ""
          },
          "deviceCookieCheckEnabled" : {
            "title" : "Device Registration Cookie Check",
            "description" : "Enables the checking of the client request for a known cookie.<br><br>If this check is enabled, the check will pass if the client request contains the named cookie.",
            "propertyOrder" : 3300,
            "required" : true,
            "type" : "boolean",
            "exampleValue" : ""
          },
          "saveDeviceCookieValueOnSuccessfulLogin" : {
            "title" : "Save Device Registration on Successful Login",
            "description" : "Set the device cookie on the client response<br><br>The Adaptive Risk Post Authentication Plug-in will set the device cookie on the client response",
            "propertyOrder" : 3500,
            "required" : true,
            "type" : "boolean",
            "exampleValue" : ""
          }
        }
      },
      "authfailed" : {
        "type" : "object",
        "title" : "Failed Authentications",
        "propertyOrder" : 1,
        "properties" : {
          "failedAuthenticationCheckEnabled" : {
            "title" : "Failed Authentication Check",
            "description" : "Checks if the user has past authentication failures.<br><br>Check if the OpenAM account lockout mechanism has recorded past authentication failures for the user.<br/><br/><i>NB </i>For this check to function, Account Lockout must be enabled.",
            "propertyOrder" : 300,
            "required" : true,
            "type" : "boolean",
            "exampleValue" : ""
          },
          "invertFailureScore" : {
            "title" : "Invert Result",
            "description" : "If the check succeeds the score will be included in the total, for failure the score will not be incremented.",
            "propertyOrder" : 500,
            "required" : true,
            "type" : "boolean",
            "exampleValue" : ""
          },
          "failureScore" : {
            "title" : "Score",
            "description" : "The amount to increment the score if this check fails.",
            "propertyOrder" : 400,
            "required" : true,
            "type" : "integer",
            "exampleValue" : ""
          }
        }
      },
      "requestheader" : {
        "type" : "object",
        "title" : "Request Header",
        "propertyOrder" : 9,
        "properties" : {
          "requestHeaderScore" : {
            "title" : "Score",
            "description" : "The amount to increment the score if this check fails.",
            "propertyOrder" : 4600,
            "required" : true,
            "type" : "integer",
            "exampleValue" : ""
          },
          "requestHeaderName" : {
            "title" : "Request Header Name",
            "description" : "The name of the required HTTP header ",
            "propertyOrder" : 4400,
            "required" : true,
            "type" : "string",
            "exampleValue" : ""
          },
          "requestHeaderCheckEnabled" : {
            "title" : "Request Header Check",
            "description" : "Enables the checking of the client request for a known header name and value.<br><br>The request header check will pass if the client request contains the required named header and value.",
            "propertyOrder" : 4300,
            "required" : true,
            "type" : "boolean",
            "exampleValue" : ""
          },
          "invertRequestHeaderScore" : {
            "title" : "Invert Result",
            "description" : "If the check succeeds the score will be included in the total, for failure the score will not be incremented.",
            "propertyOrder" : 4700,
            "required" : true,
            "type" : "boolean",
            "exampleValue" : ""
          },
          "requestHeaderValue" : {
            "title" : "Request Header Value",
            "description" : "The required value of the named HTTP header.",
            "propertyOrder" : 4500,
            "required" : true,
            "type" : "string",
            "exampleValue" : ""
          }
        }
      },
      "knowncookie" : {
        "type" : "object",
        "title" : "Known Cookie",
        "propertyOrder" : 4,
        "properties" : {
          "knownCookieName" : {
            "title" : "Cookie Name",
            "description" : "The name of the cookie to set on the client.",
            "propertyOrder" : 1700,
            "required" : true,
            "type" : "string",
            "exampleValue" : ""
          },
          "invertKnownCookieScore" : {
            "title" : "Invert Result",
            "description" : "If the check succeeds the score will be included in the total, for failure the score will not be incremented.",
            "propertyOrder" : 2100,
            "required" : true,
            "type" : "boolean",
            "exampleValue" : ""
          },
          "knownCookieCheckEnabled" : {
            "title" : "Cookie Value Check",
            "description" : "Enables the checking of a known cookie value in the client request<br><br>If this check is enabled, the check looks for a known cookie in the client request. If the cookie exists and has the correct value then the check will pass. ",
            "propertyOrder" : 1600,
            "required" : true,
            "type" : "boolean",
            "exampleValue" : ""
          },
          "createKnownCookieOnSuccessfulLogin" : {
            "title" : "Save Cookie Value on Successful Login",
            "description" : "The cookie will be created on the client after successful login<br><br>The Adaptive Risk Post Authentication Plug-in will set the cookie on the client response",
            "propertyOrder" : 1900,
            "required" : true,
            "type" : "boolean",
            "exampleValue" : ""
          },
          "knownCookieScore" : {
            "title" : "Score",
            "description" : "The amount to increment the score if this check fails.",
            "propertyOrder" : 2000,
            "required" : true,
            "type" : "integer",
            "exampleValue" : ""
          },
          "knownCookieValue" : {
            "title" : "Cookie Value",
            "description" : "The value to be set on the cookie.",
            "propertyOrder" : 1800,
            "required" : true,
            "type" : "string",
            "exampleValue" : ""
          }
        }
      },
      "general" : {
        "type" : "object",
        "title" : "General",
        "propertyOrder" : 0,
        "properties" : {
          "authenticationLevel" : {
            "title" : "Authentication Level",
            "description" : "The authentication level associated with this module.<br><br>Each authentication module has an authentication level that can be used to indicate the level of security associated with the module; 0 is the lowest (and the default).",
            "propertyOrder" : 100,
            "required" : true,
            "type" : "integer",
            "exampleValue" : ""
          },
          "riskThreshold" : {
            "title" : "Risk Threshold",
            "description" : "If the risk threshold value is not reached after executing the different tests, the authentication is considered to be successful.<br><br>Associated with many of the adaptive risk checks is a score; if a check does not passes then the score is added to the current running total. The final score is then compared with the <i>Risk Threshold</i>, if the score is lesser than said threshold the module will be successful. ",
            "propertyOrder" : 200,
            "required" : true,
            "type" : "integer",
            "exampleValue" : ""
          }
        }
      },
      "iprange" : {
        "type" : "object",
        "title" : "IP Address Range",
        "propertyOrder" : 2,
        "properties" : {
          "invertIPRangeScoreEnabled" : {
            "title" : "Invert Result",
            "description" : "If the check succeeds the score will be included in the total, for failure the score will not be incremented.",
            "propertyOrder" : 900,
            "required" : true,
            "type" : "boolean",
            "exampleValue" : ""
          },
          "ipRange" : {
            "title" : "IP Range",
            "description" : "The list of IP address to compare against the client IP address.<br><br>The format of the IP address is as follows:<br/><br/><ul><li>Single IP address: <code>172.16.90.1</code></li><li>CIDR notation: <code>172.16.90.0/24</code></li><li>IP net-block with netmask: <code>172.16.90.0:255.255.255.0</code></li></ul>",
            "propertyOrder" : 700,
            "required" : true,
            "items" : {
              "type" : "string"
            },
            "type" : "array",
            "exampleValue" : ""
          },
          "ipRangeCheckEnabled" : {
            "title" : "IP Range Check",
            "description" : "Enables the checking of the client IP address against a list of IP addresses.<br><br>The IP range check compares the IP of the client against a list of IP addresses, if the client IP is found within said list the check is successful.",
            "propertyOrder" : 600,
            "required" : true,
            "type" : "boolean",
            "exampleValue" : ""
          },
          "ipRangeScore" : {
            "title" : "Score",
            "description" : "The amount to increment the score if this check fails.",
            "propertyOrder" : 800,
            "required" : true,
            "type" : "integer",
            "exampleValue" : ""
          }
        }
      },
      "iphistory" : {
        "type" : "object",
        "title" : "IP Address History",
        "propertyOrder" : 3,
        "properties" : {
          "ipHistoryProfileAttribute" : {
            "title" : "Profile Attribute Name",
            "description" : "The name of the attribute used to store the IP history list in the data store.<br><br>IP history list is stored in the Data Store meaning your Data Store should be able to store values under the configured attribute name. If you're using a directory server as backend, make sure your Data Store configuration contains the necessary objectclass and attribute related settings.",
            "propertyOrder" : 1200,
            "required" : true,
            "type" : "string",
            "exampleValue" : ""
          },
          "saveSuccessfulIP" : {
            "title" : "Save Successful IP Address",
            "description" : "The IP History list will be updated in the data store<br><br>The Adaptive Risk Post Authentication Plug-in will update the IP history list if the overall authentication is successful.",
            "propertyOrder" : 1300,
            "required" : true,
            "type" : "boolean",
            "exampleValue" : ""
          },
          "ipHistoryCheckEnabled" : {
            "title" : "IP History Check",
            "description" : "Enables the checking of client IP address against a list of past IP addresses.<br><br>If this check is enabled; a set number of past IP addresses used by the client to access OpenAM is recorded in the user profile. This check passes if the current client IP address is present in the history list. If the IP address is not present, the check fails and the IP address is added to list if the overall authentication is successful (causing the oldest IP address to be removed).",
            "propertyOrder" : 1000,
            "required" : true,
            "type" : "boolean",
            "exampleValue" : ""
          },
          "ipHistoryCount" : {
            "title" : "History size",
            "description" : "The number of client IP addresses to save in the history list.",
            "propertyOrder" : 1100,
            "required" : true,
            "type" : "integer",
            "exampleValue" : ""
          },
          "ipHistoryScore" : {
            "title" : "Score",
            "description" : "The amount to increment the score if this check fails.",
            "propertyOrder" : 1400,
            "required" : true,
            "type" : "integer",
            "exampleValue" : ""
          },
          "invertIPHistoryScore" : {
            "title" : "Invert Result",
            "description" : "If the check succeeds the score will be included in the total, for failure the score will not be incremented.",
            "propertyOrder" : 1500,
            "required" : true,
            "type" : "boolean",
            "exampleValue" : ""
          }
        }
      },
      "geolocation" : {
        "type" : "object",
        "title" : "Geo Location",
        "propertyOrder" : 8,
        "properties" : {
          "geolocationValidCountryCodes" : {
            "title" : "Valid Country Codes",
            "description" : "The list of country codes that are considered as valid locations for client IPs.<br><br>The list is made up of country codes separated by a | character; for example:<br/><br/><code>gb|us|no|fr</code>",
            "propertyOrder" : 4000,
            "required" : true,
            "type" : "string",
            "exampleValue" : ""
          },
          "geolocationScore" : {
            "title" : "Score",
            "description" : "The amount to increment the score if this check fails.",
            "propertyOrder" : 4100,
            "required" : true,
            "type" : "integer",
            "exampleValue" : ""
          },
          "geolocationCheckEnabled" : {
            "title" : "Geolocation Country Code Check",
            "description" : "Enables the checking of the client IP address against the geolocation database.<br><br>The geolocation database associates IP addresses against their known location. This check passes if the country associated with the client IP address is matched against the list of valid country codes.<br/><br/>The geolocation database is available in binary format at <a href=\"http://www.maxmind.com/app/country\" target=\"_blank\">MaxMind</a>.",
            "propertyOrder" : 3800,
            "required" : true,
            "type" : "boolean",
            "exampleValue" : ""
          },
          "geolocationDatabaseLocation" : {
            "title" : "Geolocation Database location",
            "description" : "The path to the location of the GEO location database.<br><br>The Geolocation database is not distributed with OpenAM, you can get it in binary format from <a href=\"http://www.maxmind.com/app/country\" target=\"_blank\">MaxMind</a>.",
            "propertyOrder" : 3900,
            "required" : true,
            "type" : "string",
            "exampleValue" : ""
          },
          "invertGeolocationScore" : {
            "title" : "Invert Result",
            "description" : "If the check succeeds the score will be included in the total, for failure the score will not be incremented.",
            "propertyOrder" : 4200,
            "required" : true,
            "type" : "boolean",
            "exampleValue" : ""
          }
        }
      }
    }
  }
  ```

### delete

**Usage**

```
am> delete AdaptiveRiskModule --realm Realm --id id
```

**Parameters**

* *\--id*

  The unique identifier for the resource.

### getAllTypes

Obtain the collection of all secondary configuration types related to the resource.

**Usage**

```
am> action AdaptiveRiskModule --realm Realm --actionName getAllTypes
```

### getCreatableTypes

Obtain the collection of secondary configuration types that have yet to be added to the resource.

**Usage**

```
am> action AdaptiveRiskModule --realm Realm --actionName getCreatableTypes
```

### nextdescendents

Obtain the collection of secondary configuration instances that have been added to the resource.

**Usage**

```
am> action AdaptiveRiskModule --realm Realm --actionName nextdescendents
```

### query

Get the full list of instances of this collection. This query only supports `_queryFilter=true` filter.

**Usage**

```
am> query AdaptiveRiskModule --realm Realm --filter filter
```

**Parameters**

* *\--filter*

  A CREST formatted query filter, where "true" will query all.

### read

**Usage**

```
am> read AdaptiveRiskModule --realm Realm --id id
```

**Parameters**

* *\--id*

  The unique identifier for the resource.

### update

**Usage**

```
am> update AdaptiveRiskModule --realm Realm --id id --body body
```

**Parameters**

* *\--id*

  The unique identifier for the resource.

* *\--body*

  The resource in JSON format, described by the following JSON schema:

  ```json
  {
    "type" : "object",
    "properties" : {
      "lastlogin" : {
        "type" : "object",
        "title" : "Time Since Last Login",
        "propertyOrder" : 6,
        "properties" : {
          "saveLastLoginTimeOnSuccessfulLogin" : {
            "title" : "Save time of Successful Login",
            "description" : "The last login time will be saved in a client cookie<br><br>The Adaptive Risk Post Authentication Plug-in will update the last login time",
            "propertyOrder" : 2500,
            "required" : true,
            "type" : "boolean",
            "exampleValue" : ""
          },
          "timeSinceLastLoginCheckEnabled" : {
            "title" : "Time since Last login Check",
            "description" : "Enables the checking of the last time the user successfully authenticated.<br><br>If this check is enabled, the check ensures the user has successfully authenticated within a given interval. If the interval has been exceeded the check will fail. The last authentication for the user is stored in a client cookie.",
            "propertyOrder" : 2200,
            "required" : true,
            "type" : "boolean",
            "exampleValue" : ""
          },
          "timeSinceLastLoginScore" : {
            "title" : "Score",
            "description" : "The amount to increment the score if this check fails.",
            "propertyOrder" : 2600,
            "required" : true,
            "type" : "integer",
            "exampleValue" : ""
          },
          "timeSinceLastLoginCookieName" : {
            "title" : "Cookie Name",
            "description" : "The name of the cookie used to store the time of the last successful authentication.",
            "propertyOrder" : 2300,
            "required" : true,
            "type" : "string",
            "exampleValue" : ""
          },
          "maxTimeSinceLastLogin" : {
            "title" : "Max Time since Last login",
            "description" : "The maximum number of days that can elapse before this test.",
            "propertyOrder" : 2400,
            "required" : true,
            "type" : "string",
            "exampleValue" : ""
          },
          "invertTimeSinceLastLoginScore" : {
            "title" : "Invert Result",
            "description" : "If the check succeeds the score will be included in the total, for failure the score will not be incremented.",
            "propertyOrder" : 2700,
            "required" : true,
            "type" : "boolean",
            "exampleValue" : ""
          }
        }
      },
      "attributecheck" : {
        "type" : "object",
        "title" : "Profile Attribute",
        "propertyOrder" : 7,
        "properties" : {
          "invertProfileRiskAttributeScore" : {
            "title" : "Invert Result",
            "description" : "If the check succeeds the score will be included in the total, for failure the score will not be incremented.",
            "propertyOrder" : 3200,
            "required" : true,
            "type" : "boolean",
            "exampleValue" : ""
          },
          "profileRiskAttributeCheckEnabled" : {
            "title" : "Profile Risk Attribute check",
            "description" : "Enables the checking of the user profile for a matching attribute and value.<br><br>If this check is enabled, the check will pass if the users profile contains the required risk attribute and value.",
            "propertyOrder" : 2800,
            "required" : true,
            "type" : "boolean",
            "exampleValue" : ""
          },
          "profileRiskAttributeName" : {
            "title" : "Attribute Name",
            "description" : "The name of the attribute to retrieve from the user profile in the data store.",
            "propertyOrder" : 2900,
            "required" : true,
            "type" : "string",
            "exampleValue" : ""
          },
          "profileRiskAttributeValue" : {
            "title" : "Attribute Value",
            "description" : "The required value of the named attribute.",
            "propertyOrder" : 3000,
            "required" : true,
            "type" : "string",
            "exampleValue" : ""
          },
          "profileRiskAttributeScore" : {
            "title" : "Score",
            "description" : "The amount to increment the score if this check fails.",
            "propertyOrder" : 3100,
            "required" : true,
            "type" : "integer",
            "exampleValue" : ""
          }
        }
      },
      "devicecookie" : {
        "type" : "object",
        "title" : "Device Cookie",
        "propertyOrder" : 5,
        "properties" : {
          "deviceCookieName" : {
            "title" : "Cookie Name",
            "description" : "The name of the cookie to be checked for (and optionally set) on the client request",
            "propertyOrder" : 3400,
            "required" : true,
            "type" : "string",
            "exampleValue" : ""
          },
          "invertDeviceCookieScore" : {
            "title" : "Invert Result",
            "description" : "If the check succeeds the score will be included in the total, for failure the score will not be incremented.",
            "propertyOrder" : 3700,
            "required" : true,
            "type" : "boolean",
            "exampleValue" : ""
          },
          "deviceCookieScore" : {
            "title" : "Score",
            "description" : "The amount to increment the score if this check fails.",
            "propertyOrder" : 3600,
            "required" : true,
            "type" : "integer",
            "exampleValue" : ""
          },
          "deviceCookieCheckEnabled" : {
            "title" : "Device Registration Cookie Check",
            "description" : "Enables the checking of the client request for a known cookie.<br><br>If this check is enabled, the check will pass if the client request contains the named cookie.",
            "propertyOrder" : 3300,
            "required" : true,
            "type" : "boolean",
            "exampleValue" : ""
          },
          "saveDeviceCookieValueOnSuccessfulLogin" : {
            "title" : "Save Device Registration on Successful Login",
            "description" : "Set the device cookie on the client response<br><br>The Adaptive Risk Post Authentication Plug-in will set the device cookie on the client response",
            "propertyOrder" : 3500,
            "required" : true,
            "type" : "boolean",
            "exampleValue" : ""
          }
        }
      },
      "authfailed" : {
        "type" : "object",
        "title" : "Failed Authentications",
        "propertyOrder" : 1,
        "properties" : {
          "failedAuthenticationCheckEnabled" : {
            "title" : "Failed Authentication Check",
            "description" : "Checks if the user has past authentication failures.<br><br>Check if the OpenAM account lockout mechanism has recorded past authentication failures for the user.<br/><br/><i>NB </i>For this check to function, Account Lockout must be enabled.",
            "propertyOrder" : 300,
            "required" : true,
            "type" : "boolean",
            "exampleValue" : ""
          },
          "invertFailureScore" : {
            "title" : "Invert Result",
            "description" : "If the check succeeds the score will be included in the total, for failure the score will not be incremented.",
            "propertyOrder" : 500,
            "required" : true,
            "type" : "boolean",
            "exampleValue" : ""
          },
          "failureScore" : {
            "title" : "Score",
            "description" : "The amount to increment the score if this check fails.",
            "propertyOrder" : 400,
            "required" : true,
            "type" : "integer",
            "exampleValue" : ""
          }
        }
      },
      "requestheader" : {
        "type" : "object",
        "title" : "Request Header",
        "propertyOrder" : 9,
        "properties" : {
          "requestHeaderScore" : {
            "title" : "Score",
            "description" : "The amount to increment the score if this check fails.",
            "propertyOrder" : 4600,
            "required" : true,
            "type" : "integer",
            "exampleValue" : ""
          },
          "requestHeaderName" : {
            "title" : "Request Header Name",
            "description" : "The name of the required HTTP header ",
            "propertyOrder" : 4400,
            "required" : true,
            "type" : "string",
            "exampleValue" : ""
          },
          "requestHeaderCheckEnabled" : {
            "title" : "Request Header Check",
            "description" : "Enables the checking of the client request for a known header name and value.<br><br>The request header check will pass if the client request contains the required named header and value.",
            "propertyOrder" : 4300,
            "required" : true,
            "type" : "boolean",
            "exampleValue" : ""
          },
          "invertRequestHeaderScore" : {
            "title" : "Invert Result",
            "description" : "If the check succeeds the score will be included in the total, for failure the score will not be incremented.",
            "propertyOrder" : 4700,
            "required" : true,
            "type" : "boolean",
            "exampleValue" : ""
          },
          "requestHeaderValue" : {
            "title" : "Request Header Value",
            "description" : "The required value of the named HTTP header.",
            "propertyOrder" : 4500,
            "required" : true,
            "type" : "string",
            "exampleValue" : ""
          }
        }
      },
      "knowncookie" : {
        "type" : "object",
        "title" : "Known Cookie",
        "propertyOrder" : 4,
        "properties" : {
          "knownCookieName" : {
            "title" : "Cookie Name",
            "description" : "The name of the cookie to set on the client.",
            "propertyOrder" : 1700,
            "required" : true,
            "type" : "string",
            "exampleValue" : ""
          },
          "invertKnownCookieScore" : {
            "title" : "Invert Result",
            "description" : "If the check succeeds the score will be included in the total, for failure the score will not be incremented.",
            "propertyOrder" : 2100,
            "required" : true,
            "type" : "boolean",
            "exampleValue" : ""
          },
          "knownCookieCheckEnabled" : {
            "title" : "Cookie Value Check",
            "description" : "Enables the checking of a known cookie value in the client request<br><br>If this check is enabled, the check looks for a known cookie in the client request. If the cookie exists and has the correct value then the check will pass. ",
            "propertyOrder" : 1600,
            "required" : true,
            "type" : "boolean",
            "exampleValue" : ""
          },
          "createKnownCookieOnSuccessfulLogin" : {
            "title" : "Save Cookie Value on Successful Login",
            "description" : "The cookie will be created on the client after successful login<br><br>The Adaptive Risk Post Authentication Plug-in will set the cookie on the client response",
            "propertyOrder" : 1900,
            "required" : true,
            "type" : "boolean",
            "exampleValue" : ""
          },
          "knownCookieScore" : {
            "title" : "Score",
            "description" : "The amount to increment the score if this check fails.",
            "propertyOrder" : 2000,
            "required" : true,
            "type" : "integer",
            "exampleValue" : ""
          },
          "knownCookieValue" : {
            "title" : "Cookie Value",
            "description" : "The value to be set on the cookie.",
            "propertyOrder" : 1800,
            "required" : true,
            "type" : "string",
            "exampleValue" : ""
          }
        }
      },
      "general" : {
        "type" : "object",
        "title" : "General",
        "propertyOrder" : 0,
        "properties" : {
          "authenticationLevel" : {
            "title" : "Authentication Level",
            "description" : "The authentication level associated with this module.<br><br>Each authentication module has an authentication level that can be used to indicate the level of security associated with the module; 0 is the lowest (and the default).",
            "propertyOrder" : 100,
            "required" : true,
            "type" : "integer",
            "exampleValue" : ""
          },
          "riskThreshold" : {
            "title" : "Risk Threshold",
            "description" : "If the risk threshold value is not reached after executing the different tests, the authentication is considered to be successful.<br><br>Associated with many of the adaptive risk checks is a score; if a check does not passes then the score is added to the current running total. The final score is then compared with the <i>Risk Threshold</i>, if the score is lesser than said threshold the module will be successful. ",
            "propertyOrder" : 200,
            "required" : true,
            "type" : "integer",
            "exampleValue" : ""
          }
        }
      },
      "iprange" : {
        "type" : "object",
        "title" : "IP Address Range",
        "propertyOrder" : 2,
        "properties" : {
          "invertIPRangeScoreEnabled" : {
            "title" : "Invert Result",
            "description" : "If the check succeeds the score will be included in the total, for failure the score will not be incremented.",
            "propertyOrder" : 900,
            "required" : true,
            "type" : "boolean",
            "exampleValue" : ""
          },
          "ipRange" : {
            "title" : "IP Range",
            "description" : "The list of IP address to compare against the client IP address.<br><br>The format of the IP address is as follows:<br/><br/><ul><li>Single IP address: <code>172.16.90.1</code></li><li>CIDR notation: <code>172.16.90.0/24</code></li><li>IP net-block with netmask: <code>172.16.90.0:255.255.255.0</code></li></ul>",
            "propertyOrder" : 700,
            "required" : true,
            "items" : {
              "type" : "string"
            },
            "type" : "array",
            "exampleValue" : ""
          },
          "ipRangeCheckEnabled" : {
            "title" : "IP Range Check",
            "description" : "Enables the checking of the client IP address against a list of IP addresses.<br><br>The IP range check compares the IP of the client against a list of IP addresses, if the client IP is found within said list the check is successful.",
            "propertyOrder" : 600,
            "required" : true,
            "type" : "boolean",
            "exampleValue" : ""
          },
          "ipRangeScore" : {
            "title" : "Score",
            "description" : "The amount to increment the score if this check fails.",
            "propertyOrder" : 800,
            "required" : true,
            "type" : "integer",
            "exampleValue" : ""
          }
        }
      },
      "iphistory" : {
        "type" : "object",
        "title" : "IP Address History",
        "propertyOrder" : 3,
        "properties" : {
          "ipHistoryProfileAttribute" : {
            "title" : "Profile Attribute Name",
            "description" : "The name of the attribute used to store the IP history list in the data store.<br><br>IP history list is stored in the Data Store meaning your Data Store should be able to store values under the configured attribute name. If you're using a directory server as backend, make sure your Data Store configuration contains the necessary objectclass and attribute related settings.",
            "propertyOrder" : 1200,
            "required" : true,
            "type" : "string",
            "exampleValue" : ""
          },
          "saveSuccessfulIP" : {
            "title" : "Save Successful IP Address",
            "description" : "The IP History list will be updated in the data store<br><br>The Adaptive Risk Post Authentication Plug-in will update the IP history list if the overall authentication is successful.",
            "propertyOrder" : 1300,
            "required" : true,
            "type" : "boolean",
            "exampleValue" : ""
          },
          "ipHistoryCheckEnabled" : {
            "title" : "IP History Check",
            "description" : "Enables the checking of client IP address against a list of past IP addresses.<br><br>If this check is enabled; a set number of past IP addresses used by the client to access OpenAM is recorded in the user profile. This check passes if the current client IP address is present in the history list. If the IP address is not present, the check fails and the IP address is added to list if the overall authentication is successful (causing the oldest IP address to be removed).",
            "propertyOrder" : 1000,
            "required" : true,
            "type" : "boolean",
            "exampleValue" : ""
          },
          "ipHistoryCount" : {
            "title" : "History size",
            "description" : "The number of client IP addresses to save in the history list.",
            "propertyOrder" : 1100,
            "required" : true,
            "type" : "integer",
            "exampleValue" : ""
          },
          "ipHistoryScore" : {
            "title" : "Score",
            "description" : "The amount to increment the score if this check fails.",
            "propertyOrder" : 1400,
            "required" : true,
            "type" : "integer",
            "exampleValue" : ""
          },
          "invertIPHistoryScore" : {
            "title" : "Invert Result",
            "description" : "If the check succeeds the score will be included in the total, for failure the score will not be incremented.",
            "propertyOrder" : 1500,
            "required" : true,
            "type" : "boolean",
            "exampleValue" : ""
          }
        }
      },
      "geolocation" : {
        "type" : "object",
        "title" : "Geo Location",
        "propertyOrder" : 8,
        "properties" : {
          "geolocationValidCountryCodes" : {
            "title" : "Valid Country Codes",
            "description" : "The list of country codes that are considered as valid locations for client IPs.<br><br>The list is made up of country codes separated by a | character; for example:<br/><br/><code>gb|us|no|fr</code>",
            "propertyOrder" : 4000,
            "required" : true,
            "type" : "string",
            "exampleValue" : ""
          },
          "geolocationScore" : {
            "title" : "Score",
            "description" : "The amount to increment the score if this check fails.",
            "propertyOrder" : 4100,
            "required" : true,
            "type" : "integer",
            "exampleValue" : ""
          },
          "geolocationCheckEnabled" : {
            "title" : "Geolocation Country Code Check",
            "description" : "Enables the checking of the client IP address against the geolocation database.<br><br>The geolocation database associates IP addresses against their known location. This check passes if the country associated with the client IP address is matched against the list of valid country codes.<br/><br/>The geolocation database is available in binary format at <a href=\"http://www.maxmind.com/app/country\" target=\"_blank\">MaxMind</a>.",
            "propertyOrder" : 3800,
            "required" : true,
            "type" : "boolean",
            "exampleValue" : ""
          },
          "geolocationDatabaseLocation" : {
            "title" : "Geolocation Database location",
            "description" : "The path to the location of the GEO location database.<br><br>The Geolocation database is not distributed with OpenAM, you can get it in binary format from <a href=\"http://www.maxmind.com/app/country\" target=\"_blank\">MaxMind</a>.",
            "propertyOrder" : 3900,
            "required" : true,
            "type" : "string",
            "exampleValue" : ""
          },
          "invertGeolocationScore" : {
            "title" : "Invert Result",
            "description" : "If the check succeeds the score will be included in the total, for failure the score will not be incremented.",
            "propertyOrder" : 4200,
            "required" : true,
            "type" : "boolean",
            "exampleValue" : ""
          }
        }
      }
    }
  }
  ```

## Global Operations

Resource path:

```
/global-config/authentication/modules/adaptiverisk
```

Resource version: `1.0`

### getAllTypes

Obtain the collection of all secondary configuration types related to the resource.

**Usage**

```
am> action AdaptiveRiskModule --global --actionName getAllTypes
```

### getCreatableTypes

Obtain the collection of secondary configuration types that have yet to be added to the resource.

**Usage**

```
am> action AdaptiveRiskModule --global --actionName getCreatableTypes
```

### nextdescendents

Obtain the collection of secondary configuration instances that have been added to the resource.

**Usage**

```
am> action AdaptiveRiskModule --global --actionName nextdescendents
```

### read

**Usage**

```
am> read AdaptiveRiskModule --global
```

### update

**Usage**

```
am> update AdaptiveRiskModule --global --body body
```

**Parameters**

* *\--body*

  The resource in JSON format, described by the following JSON schema:

  ```json
  {
    "type" : "object",
    "properties" : {
      "defaults" : {
        "properties" : {
          "iprange" : {
            "type" : "object",
            "title" : "IP Address Range",
            "propertyOrder" : 2,
            "properties" : {
              "ipRangeCheckEnabled" : {
                "title" : "IP Range Check",
                "description" : "Enables the checking of the client IP address against a list of IP addresses.<br><br>The IP range check compares the IP of the client against a list of IP addresses, if the client IP is found within said list the check is successful.",
                "propertyOrder" : 600,
                "required" : true,
                "type" : "boolean",
                "exampleValue" : ""
              },
              "ipRange" : {
                "title" : "IP Range",
                "description" : "The list of IP address to compare against the client IP address.<br><br>The format of the IP address is as follows:<br/><br/><ul><li>Single IP address: <code>172.16.90.1</code></li><li>CIDR notation: <code>172.16.90.0/24</code></li><li>IP net-block with netmask: <code>172.16.90.0:255.255.255.0</code></li></ul>",
                "propertyOrder" : 700,
                "required" : true,
                "items" : {
                  "type" : "string"
                },
                "type" : "array",
                "exampleValue" : ""
              },
              "invertIPRangeScoreEnabled" : {
                "title" : "Invert Result",
                "description" : "If the check succeeds the score will be included in the total, for failure the score will not be incremented.",
                "propertyOrder" : 900,
                "required" : true,
                "type" : "boolean",
                "exampleValue" : ""
              },
              "ipRangeScore" : {
                "title" : "Score",
                "description" : "The amount to increment the score if this check fails.",
                "propertyOrder" : 800,
                "required" : true,
                "type" : "integer",
                "exampleValue" : ""
              }
            }
          },
          "lastlogin" : {
            "type" : "object",
            "title" : "Time Since Last Login",
            "propertyOrder" : 6,
            "properties" : {
              "maxTimeSinceLastLogin" : {
                "title" : "Max Time since Last login",
                "description" : "The maximum number of days that can elapse before this test.",
                "propertyOrder" : 2400,
                "required" : true,
                "type" : "string",
                "exampleValue" : ""
              },
              "timeSinceLastLoginCheckEnabled" : {
                "title" : "Time since Last login Check",
                "description" : "Enables the checking of the last time the user successfully authenticated.<br><br>If this check is enabled, the check ensures the user has successfully authenticated within a given interval. If the interval has been exceeded the check will fail. The last authentication for the user is stored in a client cookie.",
                "propertyOrder" : 2200,
                "required" : true,
                "type" : "boolean",
                "exampleValue" : ""
              },
              "timeSinceLastLoginScore" : {
                "title" : "Score",
                "description" : "The amount to increment the score if this check fails.",
                "propertyOrder" : 2600,
                "required" : true,
                "type" : "integer",
                "exampleValue" : ""
              },
              "timeSinceLastLoginCookieName" : {
                "title" : "Cookie Name",
                "description" : "The name of the cookie used to store the time of the last successful authentication.",
                "propertyOrder" : 2300,
                "required" : true,
                "type" : "string",
                "exampleValue" : ""
              },
              "invertTimeSinceLastLoginScore" : {
                "title" : "Invert Result",
                "description" : "If the check succeeds the score will be included in the total, for failure the score will not be incremented.",
                "propertyOrder" : 2700,
                "required" : true,
                "type" : "boolean",
                "exampleValue" : ""
              },
              "saveLastLoginTimeOnSuccessfulLogin" : {
                "title" : "Save time of Successful Login",
                "description" : "The last login time will be saved in a client cookie<br><br>The Adaptive Risk Post Authentication Plug-in will update the last login time",
                "propertyOrder" : 2500,
                "required" : true,
                "type" : "boolean",
                "exampleValue" : ""
              }
            }
          },
          "iphistory" : {
            "type" : "object",
            "title" : "IP Address History",
            "propertyOrder" : 3,
            "properties" : {
              "ipHistoryCheckEnabled" : {
                "title" : "IP History Check",
                "description" : "Enables the checking of client IP address against a list of past IP addresses.<br><br>If this check is enabled; a set number of past IP addresses used by the client to access OpenAM is recorded in the user profile. This check passes if the current client IP address is present in the history list. If the IP address is not present, the check fails and the IP address is added to list if the overall authentication is successful (causing the oldest IP address to be removed).",
                "propertyOrder" : 1000,
                "required" : true,
                "type" : "boolean",
                "exampleValue" : ""
              },
              "ipHistoryProfileAttribute" : {
                "title" : "Profile Attribute Name",
                "description" : "The name of the attribute used to store the IP history list in the data store.<br><br>IP history list is stored in the Data Store meaning your Data Store should be able to store values under the configured attribute name. If you're using a directory server as backend, make sure your Data Store configuration contains the necessary objectclass and attribute related settings.",
                "propertyOrder" : 1200,
                "required" : true,
                "type" : "string",
                "exampleValue" : ""
              },
              "invertIPHistoryScore" : {
                "title" : "Invert Result",
                "description" : "If the check succeeds the score will be included in the total, for failure the score will not be incremented.",
                "propertyOrder" : 1500,
                "required" : true,
                "type" : "boolean",
                "exampleValue" : ""
              },
              "ipHistoryCount" : {
                "title" : "History size",
                "description" : "The number of client IP addresses to save in the history list.",
                "propertyOrder" : 1100,
                "required" : true,
                "type" : "integer",
                "exampleValue" : ""
              },
              "ipHistoryScore" : {
                "title" : "Score",
                "description" : "The amount to increment the score if this check fails.",
                "propertyOrder" : 1400,
                "required" : true,
                "type" : "integer",
                "exampleValue" : ""
              },
              "saveSuccessfulIP" : {
                "title" : "Save Successful IP Address",
                "description" : "The IP History list will be updated in the data store<br><br>The Adaptive Risk Post Authentication Plug-in will update the IP history list if the overall authentication is successful.",
                "propertyOrder" : 1300,
                "required" : true,
                "type" : "boolean",
                "exampleValue" : ""
              }
            }
          },
          "general" : {
            "type" : "object",
            "title" : "General",
            "propertyOrder" : 0,
            "properties" : {
              "riskThreshold" : {
                "title" : "Risk Threshold",
                "description" : "If the risk threshold value is not reached after executing the different tests, the authentication is considered to be successful.<br><br>Associated with many of the adaptive risk checks is a score; if a check does not passes then the score is added to the current running total. The final score is then compared with the <i>Risk Threshold</i>, if the score is lesser than said threshold the module will be successful. ",
                "propertyOrder" : 200,
                "required" : true,
                "type" : "integer",
                "exampleValue" : ""
              },
              "authenticationLevel" : {
                "title" : "Authentication Level",
                "description" : "The authentication level associated with this module.<br><br>Each authentication module has an authentication level that can be used to indicate the level of security associated with the module; 0 is the lowest (and the default).",
                "propertyOrder" : 100,
                "required" : true,
                "type" : "integer",
                "exampleValue" : ""
              }
            }
          },
          "knowncookie" : {
            "type" : "object",
            "title" : "Known Cookie",
            "propertyOrder" : 4,
            "properties" : {
              "knownCookieCheckEnabled" : {
                "title" : "Cookie Value Check",
                "description" : "Enables the checking of a known cookie value in the client request<br><br>If this check is enabled, the check looks for a known cookie in the client request. If the cookie exists and has the correct value then the check will pass. ",
                "propertyOrder" : 1600,
                "required" : true,
                "type" : "boolean",
                "exampleValue" : ""
              },
              "knownCookieScore" : {
                "title" : "Score",
                "description" : "The amount to increment the score if this check fails.",
                "propertyOrder" : 2000,
                "required" : true,
                "type" : "integer",
                "exampleValue" : ""
              },
              "knownCookieValue" : {
                "title" : "Cookie Value",
                "description" : "The value to be set on the cookie.",
                "propertyOrder" : 1800,
                "required" : true,
                "type" : "string",
                "exampleValue" : ""
              },
              "invertKnownCookieScore" : {
                "title" : "Invert Result",
                "description" : "If the check succeeds the score will be included in the total, for failure the score will not be incremented.",
                "propertyOrder" : 2100,
                "required" : true,
                "type" : "boolean",
                "exampleValue" : ""
              },
              "createKnownCookieOnSuccessfulLogin" : {
                "title" : "Save Cookie Value on Successful Login",
                "description" : "The cookie will be created on the client after successful login<br><br>The Adaptive Risk Post Authentication Plug-in will set the cookie on the client response",
                "propertyOrder" : 1900,
                "required" : true,
                "type" : "boolean",
                "exampleValue" : ""
              },
              "knownCookieName" : {
                "title" : "Cookie Name",
                "description" : "The name of the cookie to set on the client.",
                "propertyOrder" : 1700,
                "required" : true,
                "type" : "string",
                "exampleValue" : ""
              }
            }
          },
          "devicecookie" : {
            "type" : "object",
            "title" : "Device Cookie",
            "propertyOrder" : 5,
            "properties" : {
              "deviceCookieScore" : {
                "title" : "Score",
                "description" : "The amount to increment the score if this check fails.",
                "propertyOrder" : 3600,
                "required" : true,
                "type" : "integer",
                "exampleValue" : ""
              },
              "saveDeviceCookieValueOnSuccessfulLogin" : {
                "title" : "Save Device Registration on Successful Login",
                "description" : "Set the device cookie on the client response<br><br>The Adaptive Risk Post Authentication Plug-in will set the device cookie on the client response",
                "propertyOrder" : 3500,
                "required" : true,
                "type" : "boolean",
                "exampleValue" : ""
              },
              "deviceCookieName" : {
                "title" : "Cookie Name",
                "description" : "The name of the cookie to be checked for (and optionally set) on the client request",
                "propertyOrder" : 3400,
                "required" : true,
                "type" : "string",
                "exampleValue" : ""
              },
              "invertDeviceCookieScore" : {
                "title" : "Invert Result",
                "description" : "If the check succeeds the score will be included in the total, for failure the score will not be incremented.",
                "propertyOrder" : 3700,
                "required" : true,
                "type" : "boolean",
                "exampleValue" : ""
              },
              "deviceCookieCheckEnabled" : {
                "title" : "Device Registration Cookie Check",
                "description" : "Enables the checking of the client request for a known cookie.<br><br>If this check is enabled, the check will pass if the client request contains the named cookie.",
                "propertyOrder" : 3300,
                "required" : true,
                "type" : "boolean",
                "exampleValue" : ""
              }
            }
          },
          "geolocation" : {
            "type" : "object",
            "title" : "Geo Location",
            "propertyOrder" : 8,
            "properties" : {
              "geolocationDatabaseLocation" : {
                "title" : "Geolocation Database location",
                "description" : "The path to the location of the GEO location database.<br><br>The Geolocation database is not distributed with OpenAM, you can get it in binary format from <a href=\"http://www.maxmind.com/app/country\" target=\"_blank\">MaxMind</a>.",
                "propertyOrder" : 3900,
                "required" : true,
                "type" : "string",
                "exampleValue" : ""
              },
              "geolocationValidCountryCodes" : {
                "title" : "Valid Country Codes",
                "description" : "The list of country codes that are considered as valid locations for client IPs.<br><br>The list is made up of country codes separated by a | character; for example:<br/><br/><code>gb|us|no|fr</code>",
                "propertyOrder" : 4000,
                "required" : true,
                "type" : "string",
                "exampleValue" : ""
              },
              "geolocationCheckEnabled" : {
                "title" : "Geolocation Country Code Check",
                "description" : "Enables the checking of the client IP address against the geolocation database.<br><br>The geolocation database associates IP addresses against their known location. This check passes if the country associated with the client IP address is matched against the list of valid country codes.<br/><br/>The geolocation database is available in binary format at <a href=\"http://www.maxmind.com/app/country\" target=\"_blank\">MaxMind</a>.",
                "propertyOrder" : 3800,
                "required" : true,
                "type" : "boolean",
                "exampleValue" : ""
              },
              "geolocationScore" : {
                "title" : "Score",
                "description" : "The amount to increment the score if this check fails.",
                "propertyOrder" : 4100,
                "required" : true,
                "type" : "integer",
                "exampleValue" : ""
              },
              "invertGeolocationScore" : {
                "title" : "Invert Result",
                "description" : "If the check succeeds the score will be included in the total, for failure the score will not be incremented.",
                "propertyOrder" : 4200,
                "required" : true,
                "type" : "boolean",
                "exampleValue" : ""
              }
            }
          },
          "requestheader" : {
            "type" : "object",
            "title" : "Request Header",
            "propertyOrder" : 9,
            "properties" : {
              "requestHeaderScore" : {
                "title" : "Score",
                "description" : "The amount to increment the score if this check fails.",
                "propertyOrder" : 4600,
                "required" : true,
                "type" : "integer",
                "exampleValue" : ""
              },
              "requestHeaderName" : {
                "title" : "Request Header Name",
                "description" : "The name of the required HTTP header ",
                "propertyOrder" : 4400,
                "required" : true,
                "type" : "string",
                "exampleValue" : ""
              },
              "requestHeaderValue" : {
                "title" : "Request Header Value",
                "description" : "The required value of the named HTTP header.",
                "propertyOrder" : 4500,
                "required" : true,
                "type" : "string",
                "exampleValue" : ""
              },
              "requestHeaderCheckEnabled" : {
                "title" : "Request Header Check",
                "description" : "Enables the checking of the client request for a known header name and value.<br><br>The request header check will pass if the client request contains the required named header and value.",
                "propertyOrder" : 4300,
                "required" : true,
                "type" : "boolean",
                "exampleValue" : ""
              },
              "invertRequestHeaderScore" : {
                "title" : "Invert Result",
                "description" : "If the check succeeds the score will be included in the total, for failure the score will not be incremented.",
                "propertyOrder" : 4700,
                "required" : true,
                "type" : "boolean",
                "exampleValue" : ""
              }
            }
          },
          "authfailed" : {
            "type" : "object",
            "title" : "Failed Authentications",
            "propertyOrder" : 1,
            "properties" : {
              "failureScore" : {
                "title" : "Score",
                "description" : "The amount to increment the score if this check fails.",
                "propertyOrder" : 400,
                "required" : true,
                "type" : "integer",
                "exampleValue" : ""
              },
              "invertFailureScore" : {
                "title" : "Invert Result",
                "description" : "If the check succeeds the score will be included in the total, for failure the score will not be incremented.",
                "propertyOrder" : 500,
                "required" : true,
                "type" : "boolean",
                "exampleValue" : ""
              },
              "failedAuthenticationCheckEnabled" : {
                "title" : "Failed Authentication Check",
                "description" : "Checks if the user has past authentication failures.<br><br>Check if the OpenAM account lockout mechanism has recorded past authentication failures for the user.<br/><br/><i>NB </i>For this check to function, Account Lockout must be enabled.",
                "propertyOrder" : 300,
                "required" : true,
                "type" : "boolean",
                "exampleValue" : ""
              }
            }
          },
          "attributecheck" : {
            "type" : "object",
            "title" : "Profile Attribute",
            "propertyOrder" : 7,
            "properties" : {
              "profileRiskAttributeName" : {
                "title" : "Attribute Name",
                "description" : "The name of the attribute to retrieve from the user profile in the data store.",
                "propertyOrder" : 2900,
                "required" : true,
                "type" : "string",
                "exampleValue" : ""
              },
              "profileRiskAttributeValue" : {
                "title" : "Attribute Value",
                "description" : "The required value of the named attribute.",
                "propertyOrder" : 3000,
                "required" : true,
                "type" : "string",
                "exampleValue" : ""
              },
              "invertProfileRiskAttributeScore" : {
                "title" : "Invert Result",
                "description" : "If the check succeeds the score will be included in the total, for failure the score will not be incremented.",
                "propertyOrder" : 3200,
                "required" : true,
                "type" : "boolean",
                "exampleValue" : ""
              },
              "profileRiskAttributeCheckEnabled" : {
                "title" : "Profile Risk Attribute check",
                "description" : "Enables the checking of the user profile for a matching attribute and value.<br><br>If this check is enabled, the check will pass if the users profile contains the required risk attribute and value.",
                "propertyOrder" : 2800,
                "required" : true,
                "type" : "boolean",
                "exampleValue" : ""
              },
              "profileRiskAttributeScore" : {
                "title" : "Score",
                "description" : "The amount to increment the score if this check fails.",
                "propertyOrder" : 3100,
                "required" : true,
                "type" : "integer",
                "exampleValue" : ""
              }
            }
          }
        },
        "type" : "object",
        "title" : "Realm Defaults"
      }
    }
  }
  ```

---

---
title: ADDecision
description: Resource path:
component: pingam
version: 8.1
page_id: pingam:entity-reference:sec-amster-entity-addecision
canonical_url: https://docs.pingidentity.com/pingam/8.1/entity-reference/sec-amster-entity-addecision.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  sec-amster-entity-addecision-realm-ops: Realm Operations
  sec-amster-entity-addecision-realm-ops-create: create
  sec-amster-entity-addecision-realm-ops-delete: delete
  sec-amster-entity-addecision-realm-ops-gettype: getType
  sec-amster-entity-addecision-realm-ops-getupgradedconfig: getUpgradedConfig
  sec-amster-entity-addecision-realm-ops-query: query
  sec-amster-entity-addecision-realm-ops-read: read
  sec-amster-entity-addecision-realm-ops-update: update
  sec-amster-entity-addecision-realm-ops-versioninfo: versionInfo
---

# ADDecision

## Realm Operations

Resource path:

```
/realm-config/authentication/authenticationtrees/nodes/ADDecisionNode/1.0
```

Resource version: `3.0`

### create

**Usage**

```
am> create ADDecision --realm Realm --id id --body body
```

**Parameters**

* *\--id*

  The unique identifier for the resource.

* *\--body*

  The resource in JSON format, described by the following JSON schema:

  ```json
  {
    "type" : "object",
    "properties" : {
      "returnUserDn" : {
        "title" : "Return User DN to DataStore",
        "description" : "When enabled, the node returns the DN rather than the User ID.",
        "propertyOrder" : 1100,
        "type" : "boolean",
        "exampleValue" : ""
      },
      "adminPassword" : {
        "title" : "Bind User Password",
        "description" : "Specify the password of the account used to bind to the LDAP user data store.If mTLS is enabled, this attribute is ignored.",
        "propertyOrder" : 500,
        "type" : "string",
        "format" : "password",
        "exampleValue" : ""
      },
      "adminDn" : {
        "title" : "Bind User DN",
        "description" : "Specify the user DN used to bind to the LDAP user data store. <br><br><em>Note:</em> Do not use <code>cn=Directory Manager</code> in production systems.If mTLS is enabled, this attribute is ignored.",
        "propertyOrder" : 400,
        "type" : "string",
        "exampleValue" : ""
      },
      "searchFilterAttributes" : {
        "title" : "Attributes Used to Search for a User to be Authenticated",
        "description" : "Specifies the attributes used to match an entry in the directory server to the credentials provided by the user. <br><br>The default value of <code>uid</code> will form the following search filter of <code>uid=user</code>. Specifying multiple values such as <code>uid</code> and <code>cn</code> causes the node to create a search filter of <code>(|(uid=user)(cn=user))</code>. <br><br>Multiple attribute values allow the user to authenticate with any one of the values. For example, if you have both <code>uid</code> and <code>mail</code>, then Barbara Jensen can authenticate with either <code>bjensen</code> or <code>bjensen@example.com</code>.",
        "propertyOrder" : 700,
        "items" : {
          "type" : "string"
        },
        "minItems" : 1,
        "type" : "array",
        "exampleValue" : ""
      },
      "minimumPasswordLength" : {
        "title" : "Minimum Password Length",
        "description" : "Specifies the minimum acceptable password length.",
        "propertyOrder" : 1300,
        "type" : "integer",
        "exampleValue" : ""
      },
      "mixedCaseForPasswordChangeMessages" : {
        "title" : "Use mixed case for password change messages",
        "description" : "Defines whether password change messages returned are in mixed (sentence) case or uppercase. Default: false",
        "propertyOrder" : 1900,
        "type" : "boolean",
        "exampleValue" : ""
      },
      "heartbeatTimeUnit" : {
        "title" : "LDAP Connection Heartbeat Time Unit",
        "description" : "Specifies the time unit corresponding to LDAP Connection Heartbeat Interval.<br><br> Default: Seconds",
        "propertyOrder" : 1700,
        "type" : "string",
        "exampleValue" : ""
      },
      "returnAccountLockedMessage" : {
        "title" : "Return Account Locked Message",
        "description" : "When disabled the node will return a generic authentication failure message when the user account is locked. When enabled the node will return a specific account locked message whether the correct password was provided or not.",
        "propertyOrder" : 1099,
        "type" : "boolean",
        "exampleValue" : ""
      },
      "mtlsSecretLabel" : {
        "title" : "mTLS Secret Label Identifier",
        "description" : "Identifier used to create a secret label for mapping to the mTLS certificate in the secret store. <br>AM uses this label to create a specific secret label for this node. The secret label takes the form <code>am.authentication.nodes.ad.decision.mtls.{{identifier}}.cert</code> where {{identifier}} is the value of mTLS Secret Label Identifier. The label can only contain characters {{a-z}} {{A-Z}} {{0-9}} {{.}} and cannot start or end with {{.}}.",
        "propertyOrder" : 1066,
        "type" : "string",
        "exampleValue" : ""
      },
      "secondaryServers" : {
        "title" : "Secondary LDAP Server",
        "description" : "Specify one or more secondary directory servers. <br><br>Specify each directory server in the following format: <br><code>host:port</code><br><br>Secondary servers are used when none of the primary servers are available.<br><br>For example, <code>directory_services_backup.example.com</code>.",
        "propertyOrder" : 200,
        "items" : {
          "type" : "string"
        },
        "type" : "array",
        "exampleValue" : ""
      },
      "userProfileAttribute" : {
        "title" : "Attribute Used to Retrieve User Profile",
        "description" : "Specifies the attribute used to retrieve the profile of a user from the directory server. <br><br>The user search will have already happened, as specified by the Attributes Used to Search for a User to be Authenticated and User Search Filter properties.",
        "propertyOrder" : 600,
        "type" : "string",
        "exampleValue" : ""
      },
      "userSearchFilter" : {
        "title" : "User Search Filter",
        "description" : "Specifies an additional filter to append to user searches. <br><br>For example, searching for <code>mail</code> and specifying a User Search Filter of <code>(objectClass=inetOrgPerson)</code>, causes AM to use <code>(&amp;(mail=<replaceable>address</replaceable>)(objectClass=inetOrgPerson))</code> as the resulting search filter, where <replaceable>address</replaceable> is the mail address provided by the user.",
        "propertyOrder" : 800,
        "type" : "string",
        "exampleValue" : ""
      },
      "accountSearchBaseDn" : {
        "title" : "DN to Start User Search",
        "description" : "Specify the DN from which to start the user search.<br><br>More specific DNs, such as <code>ou=sales,dc=example,dc=com</code>, result in better search performance.If multiple entries exist in the store with identical attribute values, ensure this property is specific enough to return only one entry.",
        "propertyOrder" : 300,
        "items" : {
          "type" : "string"
        },
        "minItems" : 1,
        "type" : "array",
        "exampleValue" : ""
      },
      "ldapOperationsTimeout" : {
        "title" : "LDAP Operations Timeout",
        "description" : "Defines the timeout in milliseconds that ${am.abbr} should wait for a response from the directory server.<br><br> Default: <code>0</code> (No timeout).",
        "propertyOrder" : 1800,
        "type" : "integer",
        "exampleValue" : ""
      },
      "ldapConnectionMode" : {
        "title" : "LDAP Connection Mode",
        "description" : "Specifies whether to use SSL or StartTLS to connect to the LDAP user data store.  <br><br>AM must be able to trust the certificates used.",
        "propertyOrder" : 1000,
        "type" : "string",
        "exampleValue" : ""
      },
      "heartbeatInterval" : {
        "title" : "LDAP Connection Heartbeat Interval",
        "description" : "Specifies how often AM should send a heartbeat request to the directory server to ensure that the connection does not remain idle. <br><br>Some network administrators configure firewalls and load balancers to drop connections that are idle for too long. You can turn this off by setting the value to <code>0</code> or to a negative number. Set the units for the interval in the LDAP Connection Heartbeat Time Unit property.",
        "propertyOrder" : 1600,
        "type" : "integer",
        "exampleValue" : ""
      },
      "affinityLevel" : {
        "title" : "LDAP Affinity Level",
        "description" : "Level of affinity used to balance requests across LDAP servers. The options are: no affinity, affinity for BIND requests only, affinity for all requests.",
        "propertyOrder" : 2000,
        "type" : "string",
        "exampleValue" : ""
      },
      "primaryServers" : {
        "title" : "Primary LDAP Server",
        "description" : "Specify one or more primary directory servers. <br><br>Specify each directory server in the following format: <br><code>host:port</code><br><br>For example, <code>directory_services.example.com:389</code>.",
        "propertyOrder" : 100,
        "items" : {
          "type" : "string"
        },
        "minItems" : 1,
        "type" : "array",
        "exampleValue" : ""
      },
      "mtlsEnabled" : {
        "title" : "mTLS Enabled",
        "description" : "Enables mTLS (mutual TLS) between AM and this store. When mTLS is enabled:<ul><li>Set connection mode to <code>LDAPS</code>. <li>The values for <code>Bind User DN</code> and <code>Bind User Password</code> are ignored.</li><li>You must provide an <code>mTLS Secret Label Identifier</code>.</li></ul>Instructions for setting up certificates and keystore mappings are in the product documentation.",
        "propertyOrder" : 1033,
        "type" : "boolean",
        "exampleValue" : ""
      },
      "trustAllServerCertificates" : {
        "title" : "Trust All Server Certificates",
        "description" : "When enabled, blindly trust server certificates, including self-signed test certificates. <br><br><em>Note:</em> Use this feature with care as it bypasses the normal certificate verification process.",
        "propertyOrder" : 1500,
        "type" : "boolean",
        "exampleValue" : ""
      },
      "searchScope" : {
        "title" : "Search Scope",
        "description" : "Specifies the extent of searching for users in the directory server. <br><br>Scope <code>OBJECT</code> means search only the entry specified as the DN to Start User Search, whereas <code>ONELEVEL</code> means search only the entries that are directly children of that object. <code>SUBTREE</code> means search the entry specified and every entry under it.",
        "propertyOrder" : 900,
        "type" : "string",
        "exampleValue" : ""
      },
      "userCreationAttrs" : {
        "title" : "User Creation Attributes",
        "description" : "This list lets you map (external) attribute names from the LDAP directory server to (internal) attribute names used by AM. <br><br>The format of this property is: <br><code>local attr1|external attr1</code>",
        "propertyOrder" : 1200,
        "items" : {
          "type" : "string"
        },
        "type" : "array",
        "exampleValue" : ""
      }
    },
    "required" : [ "returnUserDn", "searchFilterAttributes", "minimumPasswordLength", "mixedCaseForPasswordChangeMessages", "heartbeatTimeUnit", "returnAccountLockedMessage", "secondaryServers", "userProfileAttribute", "accountSearchBaseDn", "ldapOperationsTimeout", "ldapConnectionMode", "heartbeatInterval", "affinityLevel", "primaryServers", "mtlsEnabled", "trustAllServerCertificates", "searchScope", "userCreationAttrs" ]
  }
  ```

### delete

**Usage**

```
am> delete ADDecision --realm Realm --id id
```

**Parameters**

* *\--id*

  The unique identifier for the resource.

### getType

List information related to the node such as a name, description, tags and metadata.

**Usage**

```
am> action ADDecision --realm Realm --actionName getType
```

### getUpgradedConfig

Get the upgraded configuration for the node type.

**Usage**

```
am> action ADDecision --realm Realm --body body --actionName getUpgradedConfig --targetVersion targetVersion
```

**Parameters**

* *\--body*

  The resource in JSON format, described by the following JSON schema:

  ```json
  {
    "type" : "object",
    "title" : "The current configuration of the node type."
  }
  ```

* *\--targetVersion*

  \=== listOutcomes

List the available outcomes for the node type.

**Usage**

```
am> action ADDecision --realm Realm --body body --actionName listOutcomes
```

**Parameters**

* *\--body*

  The resource in JSON format, described by the following JSON schema:

  ```json
  {
    "description" : "Some configuration of the node. This does not need to be complete against the configuration schema.",
    "type" : "object",
    "title" : "Node configuration"
  }
  ```

### query

Get the full list of instances of this collection. This query only supports `_queryFilter=true` filter.

**Usage**

```
am> query ADDecision --realm Realm --filter filter
```

**Parameters**

* *\--filter*

  A CREST formatted query filter, where "true" will query all.

### read

**Usage**

```
am> read ADDecision --realm Realm --id id
```

**Parameters**

* *\--id*

  The unique identifier for the resource.

### update

**Usage**

```
am> update ADDecision --realm Realm --id id --body body
```

**Parameters**

* *\--id*

  The unique identifier for the resource.

* *\--body*

  The resource in JSON format, described by the following JSON schema:

  ```json
  {
    "type" : "object",
    "properties" : {
      "returnUserDn" : {
        "title" : "Return User DN to DataStore",
        "description" : "When enabled, the node returns the DN rather than the User ID.",
        "propertyOrder" : 1100,
        "type" : "boolean",
        "exampleValue" : ""
      },
      "adminPassword" : {
        "title" : "Bind User Password",
        "description" : "Specify the password of the account used to bind to the LDAP user data store.If mTLS is enabled, this attribute is ignored.",
        "propertyOrder" : 500,
        "type" : "string",
        "format" : "password",
        "exampleValue" : ""
      },
      "adminDn" : {
        "title" : "Bind User DN",
        "description" : "Specify the user DN used to bind to the LDAP user data store. <br><br><em>Note:</em> Do not use <code>cn=Directory Manager</code> in production systems.If mTLS is enabled, this attribute is ignored.",
        "propertyOrder" : 400,
        "type" : "string",
        "exampleValue" : ""
      },
      "searchFilterAttributes" : {
        "title" : "Attributes Used to Search for a User to be Authenticated",
        "description" : "Specifies the attributes used to match an entry in the directory server to the credentials provided by the user. <br><br>The default value of <code>uid</code> will form the following search filter of <code>uid=user</code>. Specifying multiple values such as <code>uid</code> and <code>cn</code> causes the node to create a search filter of <code>(|(uid=user)(cn=user))</code>. <br><br>Multiple attribute values allow the user to authenticate with any one of the values. For example, if you have both <code>uid</code> and <code>mail</code>, then Barbara Jensen can authenticate with either <code>bjensen</code> or <code>bjensen@example.com</code>.",
        "propertyOrder" : 700,
        "items" : {
          "type" : "string"
        },
        "minItems" : 1,
        "type" : "array",
        "exampleValue" : ""
      },
      "minimumPasswordLength" : {
        "title" : "Minimum Password Length",
        "description" : "Specifies the minimum acceptable password length.",
        "propertyOrder" : 1300,
        "type" : "integer",
        "exampleValue" : ""
      },
      "mixedCaseForPasswordChangeMessages" : {
        "title" : "Use mixed case for password change messages",
        "description" : "Defines whether password change messages returned are in mixed (sentence) case or uppercase. Default: false",
        "propertyOrder" : 1900,
        "type" : "boolean",
        "exampleValue" : ""
      },
      "heartbeatTimeUnit" : {
        "title" : "LDAP Connection Heartbeat Time Unit",
        "description" : "Specifies the time unit corresponding to LDAP Connection Heartbeat Interval.<br><br> Default: Seconds",
        "propertyOrder" : 1700,
        "type" : "string",
        "exampleValue" : ""
      },
      "returnAccountLockedMessage" : {
        "title" : "Return Account Locked Message",
        "description" : "When disabled the node will return a generic authentication failure message when the user account is locked. When enabled the node will return a specific account locked message whether the correct password was provided or not.",
        "propertyOrder" : 1099,
        "type" : "boolean",
        "exampleValue" : ""
      },
      "mtlsSecretLabel" : {
        "title" : "mTLS Secret Label Identifier",
        "description" : "Identifier used to create a secret label for mapping to the mTLS certificate in the secret store. <br>AM uses this label to create a specific secret label for this node. The secret label takes the form <code>am.authentication.nodes.ad.decision.mtls.{{identifier}}.cert</code> where {{identifier}} is the value of mTLS Secret Label Identifier. The label can only contain characters {{a-z}} {{A-Z}} {{0-9}} {{.}} and cannot start or end with {{.}}.",
        "propertyOrder" : 1066,
        "type" : "string",
        "exampleValue" : ""
      },
      "secondaryServers" : {
        "title" : "Secondary LDAP Server",
        "description" : "Specify one or more secondary directory servers. <br><br>Specify each directory server in the following format: <br><code>host:port</code><br><br>Secondary servers are used when none of the primary servers are available.<br><br>For example, <code>directory_services_backup.example.com</code>.",
        "propertyOrder" : 200,
        "items" : {
          "type" : "string"
        },
        "type" : "array",
        "exampleValue" : ""
      },
      "userProfileAttribute" : {
        "title" : "Attribute Used to Retrieve User Profile",
        "description" : "Specifies the attribute used to retrieve the profile of a user from the directory server. <br><br>The user search will have already happened, as specified by the Attributes Used to Search for a User to be Authenticated and User Search Filter properties.",
        "propertyOrder" : 600,
        "type" : "string",
        "exampleValue" : ""
      },
      "userSearchFilter" : {
        "title" : "User Search Filter",
        "description" : "Specifies an additional filter to append to user searches. <br><br>For example, searching for <code>mail</code> and specifying a User Search Filter of <code>(objectClass=inetOrgPerson)</code>, causes AM to use <code>(&amp;(mail=<replaceable>address</replaceable>)(objectClass=inetOrgPerson))</code> as the resulting search filter, where <replaceable>address</replaceable> is the mail address provided by the user.",
        "propertyOrder" : 800,
        "type" : "string",
        "exampleValue" : ""
      },
      "accountSearchBaseDn" : {
        "title" : "DN to Start User Search",
        "description" : "Specify the DN from which to start the user search.<br><br>More specific DNs, such as <code>ou=sales,dc=example,dc=com</code>, result in better search performance.If multiple entries exist in the store with identical attribute values, ensure this property is specific enough to return only one entry.",
        "propertyOrder" : 300,
        "items" : {
          "type" : "string"
        },
        "minItems" : 1,
        "type" : "array",
        "exampleValue" : ""
      },
      "ldapOperationsTimeout" : {
        "title" : "LDAP Operations Timeout",
        "description" : "Defines the timeout in milliseconds that ${am.abbr} should wait for a response from the directory server.<br><br> Default: <code>0</code> (No timeout).",
        "propertyOrder" : 1800,
        "type" : "integer",
        "exampleValue" : ""
      },
      "ldapConnectionMode" : {
        "title" : "LDAP Connection Mode",
        "description" : "Specifies whether to use SSL or StartTLS to connect to the LDAP user data store.  <br><br>AM must be able to trust the certificates used.",
        "propertyOrder" : 1000,
        "type" : "string",
        "exampleValue" : ""
      },
      "heartbeatInterval" : {
        "title" : "LDAP Connection Heartbeat Interval",
        "description" : "Specifies how often AM should send a heartbeat request to the directory server to ensure that the connection does not remain idle. <br><br>Some network administrators configure firewalls and load balancers to drop connections that are idle for too long. You can turn this off by setting the value to <code>0</code> or to a negative number. Set the units for the interval in the LDAP Connection Heartbeat Time Unit property.",
        "propertyOrder" : 1600,
        "type" : "integer",
        "exampleValue" : ""
      },
      "affinityLevel" : {
        "title" : "LDAP Affinity Level",
        "description" : "Level of affinity used to balance requests across LDAP servers. The options are: no affinity, affinity for BIND requests only, affinity for all requests.",
        "propertyOrder" : 2000,
        "type" : "string",
        "exampleValue" : ""
      },
      "primaryServers" : {
        "title" : "Primary LDAP Server",
        "description" : "Specify one or more primary directory servers. <br><br>Specify each directory server in the following format: <br><code>host:port</code><br><br>For example, <code>directory_services.example.com:389</code>.",
        "propertyOrder" : 100,
        "items" : {
          "type" : "string"
        },
        "minItems" : 1,
        "type" : "array",
        "exampleValue" : ""
      },
      "mtlsEnabled" : {
        "title" : "mTLS Enabled",
        "description" : "Enables mTLS (mutual TLS) between AM and this store. When mTLS is enabled:<ul><li>Set connection mode to <code>LDAPS</code>. <li>The values for <code>Bind User DN</code> and <code>Bind User Password</code> are ignored.</li><li>You must provide an <code>mTLS Secret Label Identifier</code>.</li></ul>Instructions for setting up certificates and keystore mappings are in the product documentation.",
        "propertyOrder" : 1033,
        "type" : "boolean",
        "exampleValue" : ""
      },
      "trustAllServerCertificates" : {
        "title" : "Trust All Server Certificates",
        "description" : "When enabled, blindly trust server certificates, including self-signed test certificates. <br><br><em>Note:</em> Use this feature with care as it bypasses the normal certificate verification process.",
        "propertyOrder" : 1500,
        "type" : "boolean",
        "exampleValue" : ""
      },
      "searchScope" : {
        "title" : "Search Scope",
        "description" : "Specifies the extent of searching for users in the directory server. <br><br>Scope <code>OBJECT</code> means search only the entry specified as the DN to Start User Search, whereas <code>ONELEVEL</code> means search only the entries that are directly children of that object. <code>SUBTREE</code> means search the entry specified and every entry under it.",
        "propertyOrder" : 900,
        "type" : "string",
        "exampleValue" : ""
      },
      "userCreationAttrs" : {
        "title" : "User Creation Attributes",
        "description" : "This list lets you map (external) attribute names from the LDAP directory server to (internal) attribute names used by AM. <br><br>The format of this property is: <br><code>local attr1|external attr1</code>",
        "propertyOrder" : 1200,
        "items" : {
          "type" : "string"
        },
        "type" : "array",
        "exampleValue" : ""
      }
    },
    "required" : [ "returnUserDn", "searchFilterAttributes", "minimumPasswordLength", "mixedCaseForPasswordChangeMessages", "heartbeatTimeUnit", "returnAccountLockedMessage", "secondaryServers", "userProfileAttribute", "accountSearchBaseDn", "ldapOperationsTimeout", "ldapConnectionMode", "heartbeatInterval", "affinityLevel", "primaryServers", "mtlsEnabled", "trustAllServerCertificates", "searchScope", "userCreationAttrs" ]
  }
  ```

### versionInfo

List the versions available for the node type.

**Usage**

```
am> action ADDecision --realm Realm --actionName versionInfo
```

---

---
title: ADDecisionCollection
description: Base resource for the ADDecisionNode
component: pingam
version: 8.1
page_id: pingam:entity-reference:sec-amster-entity-addecisioncollection
canonical_url: https://docs.pingidentity.com/pingam/8.1/entity-reference/sec-amster-entity-addecisioncollection.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  sec-amster-entity-addecisioncollection-realm-ops: Realm Operations
  sec-amster-entity-addecisioncollection-realm-ops-getalltypes: getAllTypes
  sec-amster-entity-addecisioncollection-realm-ops-getcreatabletypes: getCreatableTypes
  sec-amster-entity-addecisioncollection-realm-ops-getlatesttype: getLatestType
  sec-amster-entity-addecisioncollection-realm-ops-gettype: getType
  sec-amster-entity-addecisioncollection-realm-ops-nextdescendents: nextdescendents
  sec-amster-entity-addecisioncollection-realm-ops-versioninfo: versionInfo
---

# ADDecisionCollection

## Realm Operations

Base resource for the ADDecisionNode

Resource path:

```
/realm-config/authentication/authenticationtrees/nodes/ADDecisionNode
```

Resource version: `3.0`

### getAllTypes

Obtain the collection of all secondary configuration types related to the resource.

**Usage**

```
am> action ADDecisionCollection --realm Realm --actionName getAllTypes
```

### getCreatableTypes

Obtain the collection of secondary configuration types that have yet to be added to the resource.

**Usage**

```
am> action ADDecisionCollection --realm Realm --actionName getCreatableTypes
```

### getLatestType

getLatestType.description

**Usage**

```
am> action ADDecisionCollection --realm Realm --actionName getLatestType
```

### getType

List information related to the node such as a name, description, tags and metadata.

**Usage**

```
am> action ADDecisionCollection --realm Realm --actionName getType
```

### nextdescendents

Obtain the collection of secondary configuration instances that have been added to the resource.

**Usage**

```
am> action ADDecisionCollection --realm Realm --actionName nextdescendents
```

### versionInfo

List the versions available for the node type.

**Usage**

```
am> action ADDecisionCollection --realm Realm --actionName versionInfo
```

---

---
title: AdvancedProperties
description: An object of property key-value pairs
component: pingam
version: 8.1
page_id: pingam:entity-reference:sec-amster-entity-advancedproperties
canonical_url: https://docs.pingidentity.com/pingam/8.1/entity-reference/sec-amster-entity-advancedproperties.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  sec-amster-entity-advancedproperties-global-ops: Global Operations
  sec-amster-entity-advancedproperties-global-ops-read: read
  sec-amster-entity-advancedproperties-global-ops-update: update
---

# AdvancedProperties

## Global Operations

An object of property key-value pairs

Resource path:

```
/global-config/servers/{serverName}/properties/advanced
```

Resource version: `1.0`

### read

**Usage**

```
am> read AdvancedProperties --global --serverName serverName
```

**Parameters**

* *\--serverName*

  An object of property key-value pairs

### update

**Usage**

```
am> update AdvancedProperties --global --serverName serverName --body body
```

**Parameters**

* *\--serverName*

  An object of property key-value pairs

* *\--body*

  The resource in JSON format, described by the following JSON schema:

  ```json
  {
    "patternProperties" : {
      ".+" : {
        "type" : "string",
        "title" : "Value",
        "description" : "Any string value"
      }
    },
    "$schema" : "http://json-schema.org/draft-04/schema#",
    "description" : "An object of property key-value pairs",
    "type" : "object",
    "title" : "Advanced Properties"
  }
  ```

---

---
title: AgentDataStoreDecision
description: Resource path:
component: pingam
version: 8.1
page_id: pingam:entity-reference:sec-amster-entity-agentdatastoredecision
canonical_url: https://docs.pingidentity.com/pingam/8.1/entity-reference/sec-amster-entity-agentdatastoredecision.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  sec-amster-entity-agentdatastoredecision-realm-ops: Realm Operations
  sec-amster-entity-agentdatastoredecision-realm-ops-create: create
  sec-amster-entity-agentdatastoredecision-realm-ops-delete: delete
  sec-amster-entity-agentdatastoredecision-realm-ops-gettype: getType
  sec-amster-entity-agentdatastoredecision-realm-ops-getupgradedconfig: getUpgradedConfig
  sec-amster-entity-agentdatastoredecision-realm-ops-query: query
  sec-amster-entity-agentdatastoredecision-realm-ops-read: read
  sec-amster-entity-agentdatastoredecision-realm-ops-update: update
  sec-amster-entity-agentdatastoredecision-realm-ops-versioninfo: versionInfo
---

# AgentDataStoreDecision

## Realm Operations

Resource path:

```
/realm-config/authentication/authenticationtrees/nodes/AgentDataStoreDecisionNode/1.0
```

Resource version: `3.0`

### create

**Usage**

```
am> create AgentDataStoreDecision --realm Realm --id id --body body
```

**Parameters**

* *\--id*

  The unique identifier for the resource.

* *\--body*

  The resource in JSON format, described by the following JSON schema:

  ```json
  {
    "type" : "object",
    "required" : [ ]
  }
  ```

### delete

**Usage**

```
am> delete AgentDataStoreDecision --realm Realm --id id
```

**Parameters**

* *\--id*

  The unique identifier for the resource.

### getType

List information related to the node such as a name, description, tags and metadata.

**Usage**

```
am> action AgentDataStoreDecision --realm Realm --actionName getType
```

### getUpgradedConfig

Get the upgraded configuration for the node type.

**Usage**

```
am> action AgentDataStoreDecision --realm Realm --body body --actionName getUpgradedConfig --targetVersion targetVersion
```

**Parameters**

* *\--body*

  The resource in JSON format, described by the following JSON schema:

  ```json
  {
    "type" : "object",
    "title" : "The current configuration of the node type."
  }
  ```

* *\--targetVersion*

  \=== listOutcomes

List the available outcomes for the node type.

**Usage**

```
am> action AgentDataStoreDecision --realm Realm --body body --actionName listOutcomes
```

**Parameters**

* *\--body*

  The resource in JSON format, described by the following JSON schema:

  ```json
  {
    "description" : "Some configuration of the node. This does not need to be complete against the configuration schema.",
    "type" : "object",
    "title" : "Node configuration"
  }
  ```

### query

Get the full list of instances of this collection. This query only supports `_queryFilter=true` filter.

**Usage**

```
am> query AgentDataStoreDecision --realm Realm --filter filter
```

**Parameters**

* *\--filter*

  A CREST formatted query filter, where "true" will query all.

### read

**Usage**

```
am> read AgentDataStoreDecision --realm Realm --id id
```

**Parameters**

* *\--id*

  The unique identifier for the resource.

### update

**Usage**

```
am> update AgentDataStoreDecision --realm Realm --id id --body body
```

**Parameters**

* *\--id*

  The unique identifier for the resource.

* *\--body*

  The resource in JSON format, described by the following JSON schema:

  ```json
  {
    "type" : "object",
    "required" : [ ]
  }
  ```

### versionInfo

List the versions available for the node type.

**Usage**

```
am> action AgentDataStoreDecision --realm Realm --actionName versionInfo
```

---

---
title: AgentDataStoreDecisionCollection
description: Base resource for the AgentDataStoreDecisionNode
component: pingam
version: 8.1
page_id: pingam:entity-reference:sec-amster-entity-agentdatastoredecisioncollection
canonical_url: https://docs.pingidentity.com/pingam/8.1/entity-reference/sec-amster-entity-agentdatastoredecisioncollection.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  sec-amster-entity-agentdatastoredecisioncollection-realm-ops: Realm Operations
  sec-amster-entity-agentdatastoredecisioncollection-realm-ops-getalltypes: getAllTypes
  sec-amster-entity-agentdatastoredecisioncollection-realm-ops-getcreatabletypes: getCreatableTypes
  sec-amster-entity-agentdatastoredecisioncollection-realm-ops-getlatesttype: getLatestType
  sec-amster-entity-agentdatastoredecisioncollection-realm-ops-gettype: getType
  sec-amster-entity-agentdatastoredecisioncollection-realm-ops-nextdescendents: nextdescendents
  sec-amster-entity-agentdatastoredecisioncollection-realm-ops-versioninfo: versionInfo
---

# AgentDataStoreDecisionCollection

## Realm Operations

Base resource for the AgentDataStoreDecisionNode

Resource path:

```
/realm-config/authentication/authenticationtrees/nodes/AgentDataStoreDecisionNode
```

Resource version: `3.0`

### getAllTypes

Obtain the collection of all secondary configuration types related to the resource.

**Usage**

```
am> action AgentDataStoreDecisionCollection --realm Realm --actionName getAllTypes
```

### getCreatableTypes

Obtain the collection of secondary configuration types that have yet to be added to the resource.

**Usage**

```
am> action AgentDataStoreDecisionCollection --realm Realm --actionName getCreatableTypes
```

### getLatestType

getLatestType.description

**Usage**

```
am> action AgentDataStoreDecisionCollection --realm Realm --actionName getLatestType
```

### getType

List information related to the node such as a name, description, tags and metadata.

**Usage**

```
am> action AgentDataStoreDecisionCollection --realm Realm --actionName getType
```

### nextdescendents

Obtain the collection of secondary configuration instances that have been added to the resource.

**Usage**

```
am> action AgentDataStoreDecisionCollection --realm Realm --actionName nextdescendents
```

### versionInfo

List the versions available for the node type.

**Usage**

```
am> action AgentDataStoreDecisionCollection --realm Realm --actionName versionInfo
```

---

---
title: AgentGroups
description: Aggregating Agent Groups handler that is responsible for querying the aggregating agent groups
component: pingam
version: 8.1
page_id: pingam:entity-reference:sec-amster-entity-agentgroups
canonical_url: https://docs.pingidentity.com/pingam/8.1/entity-reference/sec-amster-entity-agentgroups.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  sec-amster-entity-agentgroups-realm-ops: Realm Operations
  sec-amster-entity-agentgroups-realm-ops-getalltypes: getAllTypes
  sec-amster-entity-agentgroups-realm-ops-getcreatabletypes: getCreatableTypes
  sec-amster-entity-agentgroups-realm-ops-nextdescendents: nextdescendents
  sec-amster-entity-agentgroups-realm-ops-query: query
---

# AgentGroups

## Realm Operations

Aggregating Agent Groups handler that is responsible for querying the aggregating agent groups

Resource path:

```
/realm-config/agents/groups
```

Resource version: `0.0`

### getAllTypes

Obtain the collection of all secondary configuration types related to the resource.

**Usage**

```
am> action AgentGroups --realm Realm --actionName getAllTypes
```

### getCreatableTypes

Obtain the collection of secondary configuration types that have yet to be added to the resource.

**Usage**

```
am> action AgentGroups --realm Realm --actionName getCreatableTypes
```

### nextdescendents

Obtain the collection of secondary configuration instances that have been added to the resource.

**Usage**

```
am> action AgentGroups --realm Realm --actionName nextdescendents
```

### query

Querying the aggregating agent groups

**Usage**

```
am> query AgentGroups --realm Realm --filter filter
```

**Parameters**

* *\--filter*

  A CREST formatted query filter, where "true" will query all. Fields that can be queried: \[\*]

---

---
title: AIAgents
description: Agents handler that is responsible for managing agents
component: pingam
version: 8.1
page_id: pingam:entity-reference:sec-amster-entity-aiagents
canonical_url: https://docs.pingidentity.com/pingam/8.1/entity-reference/sec-amster-entity-aiagents.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  sec-amster-entity-aiagents-realm-ops: Realm Operations
  sec-amster-entity-aiagents-realm-ops-create: create
  sec-amster-entity-aiagents-realm-ops-delete: delete
  sec-amster-entity-aiagents-realm-ops-getalltypes: getAllTypes
  sec-amster-entity-aiagents-realm-ops-getcreatabletypes: getCreatableTypes
  sec-amster-entity-aiagents-realm-ops-nextdescendents: nextdescendents
  sec-amster-entity-aiagents-realm-ops-query: query
  sec-amster-entity-aiagents-realm-ops-read: read
  sec-amster-entity-aiagents-realm-ops-update: update
---

# AIAgents

## Realm Operations

Agents handler that is responsible for managing agents

Resource path:

```
/realm-config/agents/AIAgent
```

Resource version: `0.0`

### create

**Usage**

```
am> create AIAgents --realm Realm --id id --body body
```

**Parameters**

* *\--id*

  The unique identifier for the resource.

* *\--body*

  The resource in JSON format, described by the following JSON schema:

  ```json
  {
    "type" : "object",
    "properties" : {
      "overrideOAuth2ClientConfig" : {
        "type" : "object",
        "title" : "OAuth2 Provider Overrides",
        "propertyOrder" : 5,
        "properties" : {
          "accessTokenModificationScript" : {
            "title" : "Access Token Modification Script",
            "description" : "The plugin that is executed when issuing an access token. <p>The plugin can change the access token's internal data structure to include or exclude particular fields.",
            "propertyOrder" : 40400,
            "required" : true,
            "type" : "string",
            "exampleValue" : ""
          },
          "oidcMayActScript" : {
            "title" : "OIDC ID Token May Act Script",
            "description" : "The script that is executed when issuing an OIDC ID Token explicitly to modify the <code>may_act</code> claim placed on the token.",
            "propertyOrder" : 40600,
            "required" : true,
            "type" : "string",
            "exampleValue" : ""
          },
          "usePolicyEngineForScope" : {
            "title" : "Use Policy Engine for Scope decisions",
            "description" : "With this setting enabled, the policy engine is consulted for each scope value that is requested.<br><br>If a policy returns an action of GRANT=true, the scope is consented automatically, and the user is not consulted in a user-interaction flow. If a policy returns an action of GRANT=false, the scope is not added to any resulting token, and the user will not see it in a user-interaction flow. If no policy returns a value for the GRANT action, then if the grant type is user-facing (i.e. authorization or device code flows), the user is asked for consent (or saved consent is used), and if the grant type is not user-facing (password or client credentials), the scope is not added to any resulting token.",
            "propertyOrder" : 40300,
            "required" : true,
            "type" : "boolean",
            "exampleValue" : ""
          },
          "customLoginUrlTemplate" : {
            "title" : "Custom Login URL Template",
            "description" : "Custom URL for handling login, to override the default OpenAM login page.<br><br>Supports Freemarker syntax, with the following variables:<table><tr><th>Variable</th><th>Description</th></tr><tr><td><code>gotoUrl</code></td><td><p>The URL to redirect to after login.</p></td></tr><tr><td><code>acrValues</code></td><td><p>The Authentication Context Class Reference (acr) values for the authorization request.</p></td></tr><tr><td><code>realm</code></td><td><p>The OpenAM realm the authorization request was made on.</p></td></tr><tr><td><code>module</code></td><td><p>The name of the OpenAM authentication module requested to perform resource owner authentication.</p></td></tr><tr><td><code>service</code></td><td><p>The name of the OpenAM authentication chain requested to perform resource owner authentication.</p></td></tr><tr><td><code>locale</code></td><td><p>A space-separated list of locales, ordered by preference.</p></td></tr></table>The following example template redirects users to a non-OpenAM front end to handle login, which will then redirect back to the <code>/oauth2/authorize</code> endpoint with any required parameters:<p> <code>http://mylogin.com/login?goto=${goto}&lt;#if acrValues??&gt;&amp;acr_values=${acrValues}&lt;&#x2F;#if&gt;&lt;#if realm??&gt;&amp;realm=${realm}&lt;&#x2F;#if&gt;&lt;#if module??&gt;&amp;module=${module}&lt;&#x2F;#if&gt;&lt;#if service??&gt;&amp;service=${service}&lt;&#x2F;#if&gt;&lt;#if locale??&gt;&amp;locale=${locale}&lt;&#x2F;#if&gt;</code><br><b>NOTE</b>: Default OpenAM login page is constructed using \"Base URL Source\" service.",
            "propertyOrder" : 40900,
            "required" : false,
            "type" : "string",
            "exampleValue" : ""
          },
          "evaluateScopeClass" : {
            "title" : "Scope Evaluation Plugin Implementation Class",
            "description" : "The plugin that is executed when retrieving access token's information. <p>The plugin can provide a mechanism to associate scopes with profile attribute values, such as if one of the scopes is mail, the resource owner's email address is provided in the information returned. <p>The provided plugin class must implement the scope evaluation plugin interface: <code>org.forgerock.oauth2.core.plugins.ScopeEvaluator</code> <p>If this field is empty and the Plugin Type of JAVA is selected, the default implementation will be used: <code>org.forgerock.oauth2.core.plugins.registry.DefaultScopeEvaluator</code>",
            "propertyOrder" : 42300,
            "required" : false,
            "type" : "string",
            "exampleValue" : ""
          },
          "authorizeEndpointDataProviderPluginType" : {
            "title" : "Authorize Endpoint Data Provider Plugin Type",
            "description" : "When the plugin type is SCRIPTED then the Authorize Endpoint Data Provider Script will be executed and when plugin type is JAVA then the Authorize Endpoint Data Provider Plugin Implementation Class will be executed. If the plugin type is PROVIDER the client override is disabled and the plugin configured on the OAuth2 Provider is used.",
            "propertyOrder" : 42700,
            "required" : true,
            "type" : "string",
            "exampleValue" : ""
          },
          "tokenEncryptionEnabled" : {
            "title" : "Encrypt Client-Side Tokens",
            "description" : "Whether client-side access and refresh tokens should be encrypted.<br><br>Enabling token encryption will disable token signing as encryption is performed using direct symmetric encryption.",
            "propertyOrder" : 41100,
            "required" : true,
            "type" : "boolean",
            "exampleValue" : ""
          },
          "accessTokenMayActScript" : {
            "title" : "OAuth2 Access Token May Act Script",
            "description" : "The script that is executed when issuing an access token explicitly to modify the <code>may_act</code> claim placed on the token.",
            "propertyOrder" : 40500,
            "required" : true,
            "type" : "string",
            "exampleValue" : ""
          },
          "statelessTokensEnabled" : {
            "title" : "Use Client-Side Access & Refresh Tokens",
            "description" : "When enabled, OpenAM issues access and refresh tokens that can be inspected by resource servers.",
            "propertyOrder" : 41000,
            "required" : true,
            "type" : "boolean",
            "exampleValue" : ""
          },
          "evaluateScopePluginType" : {
            "title" : "Scope Evaluation Plugin Type",
            "description" : "When the plugin type is SCRIPTED then the Scope Evaluation Script will be executed and when plugin type is JAVA then the Scope Evaluation Plugin Implementation Class will be executed. If the plugin type is PROVIDER the client override is disabled and the plugin configured on the OAuth2 Provider is used.",
            "propertyOrder" : 42100,
            "required" : true,
            "type" : "string",
            "exampleValue" : ""
          },
          "clientsCanSkipConsent" : {
            "title" : "Allow Clients to Skip Consent",
            "description" : "If enabled, clients may be configured so that the resource owner will not be asked for consent during authorization flows.",
            "propertyOrder" : 41300,
            "required" : true,
            "type" : "boolean",
            "exampleValue" : ""
          },
          "validateScopeClass" : {
            "title" : "Scope Validation Plugin Implementation Class",
            "description" : "The plugin that is executed when validating or customising the set of requested scopes for authorize, access token, refresh token and back channel authorize requests. <p>The provided plugin class must implement the scope validation plugin interface: <code>org.forgerock.oauth2.core.plugins.ScopeValidator</code> <p>If this field is empty and the Plugin Type of JAVA is selected, the default implementation will be used: <code>org.forgerock.oauth2.core.plugins.registry.DefaultScopeValidator</code>",
            "propertyOrder" : 42600,
            "required" : false,
            "type" : "string",
            "exampleValue" : ""
          },
          "evaluateScopeScript" : {
            "title" : "Scope Evaluation Script",
            "description" : "The plugin that is executed when retrieving access token's information. <p>The plugin can provide a mechanism to associate scopes with profile attribute values, such as if one of the scopes is mail, the resource owner's email address is provided in the information returned.",
            "propertyOrder" : 42200,
            "required" : true,
            "type" : "string",
            "exampleValue" : ""
          },
          "authorizeEndpointDataProviderScript" : {
            "title" : "Authorize Endpoint Data Provider Script",
            "description" : "The plugin that is executed to return additional data from the authorization request.",
            "propertyOrder" : 42800,
            "required" : true,
            "type" : "string",
            "exampleValue" : ""
          },
          "providerOverridesEnabled" : {
            "title" : "Enable OAuth2 Provider Overrides",
            "description" : "Enabling this causes the other config in this section to override the default OAuth2 Provider behaviour.",
            "propertyOrder" : 40000,
            "required" : true,
            "type" : "boolean",
            "exampleValue" : ""
          },
          "enableApplicationContext" : {
            "title" : "Enable Application Context",
            "description" : "When enabled, this setting makes the application context available in all OAuth2 / OIDC flows for this client as the <code>oauthApplication</code> binding in scripted decision node scripts.",
            "propertyOrder" : 43500,
            "required" : true,
            "type" : "boolean",
            "exampleValue" : ""
          },
          "remoteConsentServiceId" : {
            "title" : "Remote Consent Service ID",
            "description" : "The ID of an existing remote consent service agent.",
            "propertyOrder" : 41500,
            "required" : false,
            "type" : "string",
            "exampleValue" : ""
          },
          "accessTokenModificationPluginType" : {
            "title" : "Access Token Modification Plugin Type",
            "description" : "When the plugin type is SCRIPTED then the Access Token Modification Script will be executed and when plugin type is JAVA then the Access Token Modifier Plugin Implementation Class will be executed. If the plugin type is PROVIDER the client override is disabled and the plugin configured on the OAuth2 Provider is used.",
            "propertyOrder" : 40390,
            "required" : true,
            "type" : "string",
            "exampleValue" : ""
          },
          "authorizeEndpointDataProviderClass" : {
            "title" : "Authorize Endpoint Data Provider Plugin Implementation Class",
            "description" : "The plugin that is executed to return additional data from the authorization request. <<p>The provided plugin class must implement the scope evaluation plugin interface: <code>org.forgerock.oauth2.core.plugins.AuthorizeEndpointDataProvider</code> <p>If this field is empty and the Plugin Type of JAVA is selected, the default implementation will be used: <code>org.forgerock.oauth2.core.plugins.registry.DefaultEndpointDataProvider</code>",
            "propertyOrder" : 42900,
            "required" : false,
            "type" : "string",
            "exampleValue" : ""
          },
          "oidcClaimsPluginType" : {
            "title" : "OIDC Claims Plugin Type",
            "description" : "When the plugin type is SCRIPTED then the OIDC Claims Script will be executed and when plugin type is JAVA then the OIDC Claims Plugin Implementation Class will be executed. If the plugin type is PROVIDER the client override is disabled and the plugin configured on the OAuth2 Provider is used.",
            "propertyOrder" : 40690,
            "required" : true,
            "type" : "string",
            "exampleValue" : ""
          },
          "acceptAudienceParametersInTokenExchangeRequests" : {
            "title" : "Accept Audience Parameters in Token Exchange Requests",
            "description" : "When enabled, AM validates audience parameter values in Token Exchange requests against the values defined in Allowed Resource Server Audience Values. If validation fails, the token exchange request is rejected.",
            "propertyOrder" : 43600,
            "required" : true,
            "type" : "boolean",
            "exampleValue" : ""
          },
          "oidcClaimsClass" : {
            "title" : "OIDC Claims Plugin Implementation Class",
            "description" : "The plugin that is executed when issuing an ID token or making a request to the <i>userinfo</i> endpoint during OpenID requests.<p>The plugin gathers the scopes and populates claims, and has access to the access token, the user's identity and, if available, the user's session. <p>This plugin provides the custom implementation for the OIDC claims plugin interface: <code>org.forgerock.oauth2.core.plugins.UserInfoClaimsPlugin</code> <p>This field cannot be empty if the Plugin Type of JAVA is selected. Failure to provide a valid implementation of the OIDC claims plugin interface will cause OAuth2 flows to fail.",
            "propertyOrder" : 40710,
            "required" : false,
            "type" : "string",
            "exampleValue" : ""
          },
          "oidcClaimsScript" : {
            "title" : "OIDC Claims Script",
            "description" : "The plugin that is executed when issuing an ID token or making a request to the <i>userinfo</i> endpoint during OpenID requests.<p>The plugin gathers the scopes and populates claims, and has access to the access token, the user's identity and, if available, the user's session.",
            "propertyOrder" : 40700,
            "required" : true,
            "type" : "string",
            "exampleValue" : ""
          },
          "issueRefreshToken" : {
            "title" : "Issue Refresh Tokens",
            "description" : "Whether to issue a refresh token when returning an access token.",
            "propertyOrder" : 40100,
            "required" : true,
            "type" : "boolean",
            "exampleValue" : ""
          },
          "useTokenIntrospectionClaimForJWT" : {
            "title" : "Use token_introspection claim for JWT",
            "description" : "When enabled, the JWT introspection response complies with RFC 9701. This ensures the introspection data is nested within the <code>token_introspection</code> claim in the JWT response. <br><b>Note:</b> Enabling this option also causes the JSON introspection response to include the token's <code>aud</code> claim, if present.",
            "propertyOrder" : 43700,
            "required" : true,
            "type" : "boolean",
            "exampleValue" : ""
          },
          "issueRefreshTokenOnRefreshedToken" : {
            "title" : "Issue Refresh Tokens on Refreshing Access Tokens",
            "description" : "Whether to issue a refresh token when refreshing an access token.",
            "propertyOrder" : 40200,
            "required" : true,
            "type" : "boolean",
            "exampleValue" : ""
          },
          "accessTokenModifierClass" : {
            "title" : "Access Token Modifier Plugin Implementation Class",
            "description" : "The plugin that is executed when issuing an access token. <p>The plugin can change the access token's internal data structure to include or exclude particular fields. <p>This plugin provides the custom implementation for the access token modifier plugin interface: <code>org.forgerock.oauth2.core.plugins.AccessTokenModifier</code> <p>This field cannot be empty if the Plugin Type of JAVA is selected. Failure to provide a valid implementation of the access token modifier plugin interface will cause OAuth2 flows to fail.",
            "propertyOrder" : 40410,
            "required" : false,
            "type" : "string",
            "exampleValue" : ""
          },
          "validateScopeScript" : {
            "title" : "Scope Validation Script",
            "description" : "The plugin that is executed when validating or customising the set of requested scopes for authorize, access token, refresh token and back channel authorize requests.",
            "propertyOrder" : 42500,
            "required" : false,
            "type" : "string",
            "exampleValue" : ""
          },
          "enableRemoteConsent" : {
            "title" : "Enable Remote Consent",
            "description" : "",
            "propertyOrder" : 41400,
            "required" : true,
            "type" : "boolean",
            "exampleValue" : ""
          },
          "useForceAuthnForMaxAge" : {
            "title" : "Use Force Authentication for max_age",
            "description" : "When this setting is <code>false</code> (default)<ul><li>Attempted authorization when the max_age has passed will log the existing session out and start a re-authentication</li></ul> <ul><li>Re-authentication triggered by the max_age parameter will create a new session</li></ul> When this setting is <code>true</code> <ul><li>Attempted authorization when the max_age has passed will not destroy the existing session</li></ul> <ul><li>Re-authentication triggered by the max_age parameter will return the same session. The advanced server property org.forgerock.openam.authentication.forceAuth.enabled must be set to <code>true</code></li></ul> <p>For security reasons, it is strongly recommended that you leave <code>Use Force Authentication for max_age</code> set to the default value (<code>false</code>), so that a new session is created when the user re-authenticates.</p>",
            "propertyOrder" : 40850,
            "required" : true,
            "type" : "boolean",
            "exampleValue" : ""
          },
          "scopesPolicySet" : {
            "title" : "Scopes Policy Set",
            "description" : "The policy set that defines the context in which policy evaluations occur when Use Policy Engine for Scope decisions is enabled on the OAuth2 provider. If blank will default to the oauth2Scopes policy set.",
            "propertyOrder" : 40310,
            "required" : false,
            "type" : "string",
            "exampleValue" : ""
          },
          "overrideableOIDCClaims" : {
            "title" : "Overrideable Id_Token Claims",
            "description" : "List of claims in the id_token that may be overrideable in the OIDC Claims Script. These should be the subset of the core OpenID Connect Claims like aud or azp.",
            "propertyOrder" : 43300,
            "required" : false,
            "items" : {
              "type" : "string"
            },
            "type" : "array",
            "exampleValue" : ""
          },
          "validateScopePluginType" : {
            "title" : "Scope Validation Plugin Type",
            "description" : "When the plugin type is SCRIPTED then the Scope Validation Script will be executed and when plugin type is JAVA then the Scope Validation Plugin Implementation Class will be executed. If the plugin type is PROVIDER the client override is disabled and the plugin configured on the OAuth2 Provider is used.",
            "propertyOrder" : 42400,
            "required" : true,
            "type" : "string",
            "exampleValue" : ""
          }
        }
      },
      "signEncOAuth2ClientConfig" : {
        "type" : "object",
        "title" : "Signing and Encryption",
        "propertyOrder" : 3,
        "properties" : {
          "authorizationResponseEncryptionMethod" : {
            "title" : "Authorization Response JWT Encryption Method",
            "description" : "Encryption method the Authorization Response JWT for this client must be encrypted with.",
            "propertyOrder" : 24804,
            "type" : "object",
            "exampleValue" : "",
            "properties" : {
              "inherited" : {
                "type" : "boolean",
                "required" : true
              },
              "value" : {
                "type" : "string",
                "required" : false
              }
            }
          },
          "idTokenEncryptionAlgorithm" : {
            "title" : "ID Token Encryption Algorithm",
            "description" : "Algorithm the ID Token for this client must be encrypted with.",
            "propertyOrder" : 24700,
            "type" : "object",
            "exampleValue" : "",
            "properties" : {
              "inherited" : {
                "type" : "boolean",
                "required" : true
              },
              "value" : {
                "type" : "string",
                "required" : true
              }
            }
          },
          "requestParameterEncryptedEncryptionAlgorithm" : {
            "title" : "Request parameter encryption method",
            "description" : "JWE enc algorithm for encrypting the request parameter.<br><br>AM supports the following token encryption algorithms:<ul><li><code>A128GCM</code>, <code>A192GCM</code>, and <code>A256GCM</code> - AES in Galois Counter Mode (GCM) authenticated encryption mode.</li><li><code>A128CBC-HS256</code>, <code>A192CBC-HS384</code>, and <code>A256CBC-HS512</code> - AES encryption in CBC mode, with HMAC-SHA-2 for integrity.</li></ul>",
            "propertyOrder" : 27700,
            "type" : "object",
            "exampleValue" : "",
            "properties" : {
              "inherited" : {
                "type" : "boolean",
                "required" : true
              },
              "value" : {
                "type" : "string",
                "required" : true
              }
            }
          },
          "userinfoSignedResponseAlg" : {
            "title" : "User info signed response algorithm",
            "description" : "JWS algorithm for signing UserInfo Responses. If this is specified, the response will be JWT <a href=\"https://tools.ietf.org/html/rfc7519\">JWT</a> serialized, and signed using JWS. The default, if omitted, is for the UserInfo Response to return the Claims as a UTF-8 encoded JSON object using the application/json content-type.",
            "propertyOrder" : 27200,
            "type" : "object",
            "exampleValue" : "",
            "properties" : {
              "inherited" : {
                "type" : "boolean",
                "required" : true
              },
              "value" : {
                "type" : "string",
                "required" : false
              }
            }
          },
          "tokenEndpointAuthSigningAlgorithm" : {
            "title" : "Token Endpoint Authentication Signing Algorithm",
            "description" : "The JWS algorithm that MUST be used for signing the JWT used to authenticate the Client at the Token Endpointfor the private_key_jwt and client_secret_jwt authentication methods. All Token Requests using these authentication methods from this Client MUST be rejected, if the JWT is not signed with this algorithm.",
            "propertyOrder" : 24130,
            "type" : "object",
            "exampleValue" : "",
            "properties" : {
              "inherited" : {
                "type" : "boolean",
                "required" : true
              },
              "value" : {
                "type" : "string",
                "required" : true
              }
            }
          },
          "mTLSTrustedCert" : {
            "title" : "mTLS Self-Signed Certificate",
            "description" : "Self-signed PEM-encoded or DER-encoded X.509 certificate for mTLS client certificate authentication. This value is ignored if you specify a Secret Label Identifier and a corresponding secret mapping.",
            "propertyOrder" : 25405,
            "type" : "object",
            "exampleValue" : "",
            "properties" : {
              "inherited" : {
                "type" : "boolean",
                "required" : true
              },
              "value" : {
                "type" : "string",
                "required" : false
              }
            }
          },
          "tokenIntrospectionEncryptedResponseAlg" : {
            "title" : "Token introspection response encryption algorithm",
            "description" : "JWE \"alg\" algorithm REQUIRED for encrypting introspection responses. Sets the algorithm that will be used to encrypt the Content Encryption Key when the chosen introspection response format is 'signed then encrypted'.",
            "propertyOrder" : 27820,
            "type" : "object",
            "exampleValue" : "",
            "properties" : {
              "inherited" : {
                "type" : "boolean",
                "required" : true
              },
              "value" : {
                "type" : "string",
                "required" : true
              }
            }
          },
          "jwkSet" : {
            "title" : "Json Web Key",
            "description" : "Raw JSON Web Key value containing the client's public keys.",
            "propertyOrder" : 24200,
            "type" : "object",
            "exampleValue" : "",
            "properties" : {
              "inherited" : {
                "type" : "boolean",
                "required" : true
              },
              "value" : {
                "type" : "string",
                "required" : false
              }
            }
          },
          "userinfoResponseFormat" : {
            "title" : "User info response format.",
            "description" : "The user info endpoint offers different output format. See http://openid.net/specs/openid-connect-core-1_0.html#UserInfoResponse",
            "propertyOrder" : 27100,
            "type" : "object",
            "exampleValue" : "",
            "properties" : {
              "inherited" : {
                "type" : "boolean",
                "required" : true
              },
              "value" : {
                "type" : "string",
                "required" : true
              }
            }
          },
          "userinfoEncryptedResponseEncryptionAlgorithm" : {
            "title" : "User info encrypted response encryption algorithm",
            "description" : "JWE enc algorithm for encrypting UserInfo Responses. If userinfo encrypted response algorithm is specified, the default for this value is A128CBC-HS256. When user info encrypted response encryption is included, user info encrypted response algorithm MUST also be provided.<br><br>AM supports the following token encryption algorithms:<ul><li><code>A128GCM</code>, <code>A192GCM</code>, and <code>A256GCM</code> - AES in Galois Counter Mode (GCM) authenticated encryption mode.</li><li><code>A128CBC-HS256</code>, <code>A192CBC-HS384</code>, and <code>A256CBC-HS512</code> - AES encryption in CBC mode, with HMAC-SHA-2 for integrity.</li></ul>",
            "propertyOrder" : 27400,
            "type" : "object",
            "exampleValue" : "",
            "properties" : {
              "inherited" : {
                "type" : "boolean",
                "required" : true
              },
              "value" : {
                "type" : "string",
                "required" : true
              }
            }
          },
          "tokenIntrospectionResponseFormat" : {
            "title" : "Token introspection response format",
            "description" : "The token introspection endpoint offers different output format. see https://tools.ietf.org/html/draft-ietf-oauth-jwt-introspection-response-03",
            "propertyOrder" : 27800,
            "type" : "object",
            "exampleValue" : "",
            "properties" : {
              "inherited" : {
                "type" : "boolean",
                "required" : true
              },
              "value" : {
                "type" : "string",
                "required" : true
              }
            }
          },
          "publicKeyLocation" : {
            "title" : "Public key selector",
            "description" : "Select the public key for this client to come from either the jwks_uri, manual jwks or X509 field.",
            "propertyOrder" : 25700,
            "type" : "object",
            "exampleValue" : "",
            "properties" : {
              "inherited" : {
                "type" : "boolean",
                "required" : true
              },
              "value" : {
                "type" : "string",
                "required" : true
              }
            }
          },
          "tokenIntrospectionEncryptedResponseEncryptionAlgorithm" : {
            "title" : "Token introspection encrypted response encryption algorithm",
            "description" : "JWE 'enc' algorithm REQUIRED for encrypting token introspection responses. Sets the algorithm that will be used to encrypt the Plaintext of a JWE when the chosen introspection response format is 'signed then encrypted'.",
            "propertyOrder" : 27830,
            "type" : "object",
            "exampleValue" : "",
            "properties" : {
              "inherited" : {
                "type" : "boolean",
                "required" : true
              },
              "value" : {
                "type" : "string",
                "required" : true
              }
            }
          },
          "jwkStoreCacheMissCacheTime" : {
            "title" : "JWKs URI content cache miss cache time",
            "description" : "To avoid loading the JWKS URI content for every token signature verification, especially when the kid is not in the jwks content already cached, the JWKS content will be cache for a minimum period of time. This cache miss cache time defines the minimum of time the JWKS URI content is cache.",
            "propertyOrder" : 24120,
            "type" : "object",
            "exampleValue" : "",
            "properties" : {
              "inherited" : {
                "type" : "boolean",
                "required" : true
              },
              "value" : {
                "type" : "integer",
                "required" : true
              }
            }
          },
          "requestParameterEncryptedAlg" : {
            "title" : "Request parameter encryption algorithm",
            "description" : "JWE algorithm for encrypting the request parameter.",
            "propertyOrder" : 27600,
            "type" : "object",
            "exampleValue" : "",
            "properties" : {
              "inherited" : {
                "type" : "boolean",
                "required" : true
              },
              "value" : {
                "type" : "string",
                "required" : false
              }
            }
          },
          "idTokenEncryptionMethod" : {
            "title" : "ID Token Encryption Method",
            "description" : "Encryption method the ID Token for this client must be encrypted with.",
            "propertyOrder" : 24800,
            "type" : "object",
            "exampleValue" : "",
            "properties" : {
              "inherited" : {
                "type" : "boolean",
                "required" : true
              },
              "value" : {
                "type" : "string",
                "required" : true
              }
            }
          },
          "jwksUri" : {
            "title" : "Json Web Key URI",
            "description" : "The uri that contains the client's public keys in Json Web Key format.",
            "propertyOrder" : 24100,
            "type" : "object",
            "exampleValue" : "https://{{jwks-www}}/oauth2/{{realm}}/connect/jwk_uri",
            "properties" : {
              "inherited" : {
                "type" : "boolean",
                "required" : true
              },
              "value" : {
                "type" : "string",
                "required" : false
              }
            }
          },
          "userinfoEncryptedResponseAlg" : {
            "title" : "User info encrypted response algorithm",
            "description" : "JWE algorithm for encrypting UserInfo Responses. If both signing and encryption are requested, the response will be signed then encrypted, with the result being a Nested JWT. The default, if omitted, is that no encryption is performed.",
            "propertyOrder" : 27300,
            "type" : "object",
            "exampleValue" : "",
            "properties" : {
              "inherited" : {
                "type" : "boolean",
                "required" : true
              },
              "value" : {
                "type" : "string",
                "required" : false
              }
            }
          },
          "authorizationResponseEncryptionAlgorithm" : {
            "title" : "Authorization Response JWT Encryption Algorithm",
            "description" : "Algorithm the Authorization Response JWT for this client must be encrypted with.",
            "propertyOrder" : 24803,
            "type" : "object",
            "exampleValue" : "",
            "properties" : {
              "inherited" : {
                "type" : "boolean",
                "required" : true
              },
              "value" : {
                "type" : "string",
                "required" : false
              }
            }
          },
          "requestParameterSignedAlg" : {
            "title" : "Request parameter signing algorithm",
            "description" : "JWS algorithm for signing the request parameter.",
            "propertyOrder" : 27500,
            "type" : "object",
            "exampleValue" : "",
            "properties" : {
              "inherited" : {
                "type" : "boolean",
                "required" : true
              },
              "value" : {
                "type" : "string",
                "required" : false
              }
            }
          },
          "mTLSCertificateBoundAccessTokens" : {
            "title" : "Use Certificate-Bound Access Tokens",
            "description" : "Whether access tokens issued to this client should be bound to the X.509 certificate it uses to authenticate to the token endpoint. If enabled (and the provider supports it) then an x5t#S256 confirmation key will be added to all access tokens with the SHA-256 hash of the client's certificate.",
            "propertyOrder" : 25507,
            "type" : "object",
            "exampleValue" : "",
            "properties" : {
              "inherited" : {
                "type" : "boolean",
                "required" : true
              },
              "value" : {
                "type" : "boolean",
                "required" : true
              }
            }
          },
          "jwksCacheTimeout" : {
            "title" : "JWKs URI content cache timeout in ms",
            "description" : "To avoid loading the JWKS URI content for every token encryption, the JWKS content is cached. This timeout defines the maximum of time the JWKS URI content can be cached before being refreshed.",
            "propertyOrder" : 24110,
            "type" : "object",
            "exampleValue" : "",
            "properties" : {
              "inherited" : {
                "type" : "boolean",
                "required" : true
              },
              "value" : {
                "type" : "integer",
                "required" : true
              }
            }
          },
          "mTLSSubjectDN" : {
            "title" : "mTLS Subject DN",
            "description" : "Expected Subject DN of certificate used for mTLS client certificate authentication. Defaults to CN=&lt;client_id&gt;. Only applicable when using CA-signed certificates.",
            "propertyOrder" : 25406,
            "type" : "object",
            "exampleValue" : "",
            "properties" : {
              "inherited" : {
                "type" : "boolean",
                "required" : true
              },
              "value" : {
                "type" : "string",
                "required" : false
              }
            }
          },
          "idTokenEncryptionEnabled" : {
            "title" : "Enable ID Token Encryption",
            "description" : "Select to enable ID token encryption.",
            "propertyOrder" : 24600,
            "type" : "object",
            "exampleValue" : "",
            "properties" : {
              "inherited" : {
                "type" : "boolean",
                "required" : true
              },
              "value" : {
                "type" : "boolean",
                "required" : true
              }
            }
          },
          "tokenIntrospectionSignedResponseAlg" : {
            "title" : "Token introspection response signing algorithm",
            "description" : "Algorithm used for signing the introspection JWT response.",
            "propertyOrder" : 27810,
            "type" : "object",
            "exampleValue" : "",
            "properties" : {
              "inherited" : {
                "type" : "boolean",
                "required" : true
              },
              "value" : {
                "type" : "string",
                "required" : true
              }
            }
          },
          "idTokenPublicEncryptionKey" : {
            "title" : "ID Token Encryption Public Key",
            "description" : "A Base64 encoded public key for encrypting ID Tokens. This key is ignored if you specify a Secret Label Identifier and the corresponding secret mapping.",
            "propertyOrder" : 24900,
            "type" : "object",
            "exampleValue" : "",
            "properties" : {
              "inherited" : {
                "type" : "boolean",
                "required" : true
              },
              "value" : {
                "type" : "string",
                "required" : false
              }
            }
          },
          "clientJwtPublicKey" : {
            "title" : "Client JWT Bearer Public Key",
            "description" : "A Base64 encoded X509 certificate, containing the public key, represented as a UTF-8 PEM file, of the key pair for signing the Client Bearer JWT. This value is ignored if you specify a Secret Label Identifier and a corresponding secret mapping.",
            "propertyOrder" : 25400,
            "type" : "object",
            "exampleValue" : "",
            "properties" : {
              "inherited" : {
                "type" : "boolean",
                "required" : true
              },
              "value" : {
                "type" : "string",
                "required" : false
              }
            }
          },
          "authorizationResponseSigningAlgorithm" : {
            "title" : "Authorization Response JWT Signing Algorithm",
            "description" : "Algorithm the Authorization Response JWT for this client must be signed with.",
            "propertyOrder" : 24801,
            "type" : "object",
            "exampleValue" : "",
            "properties" : {
              "inherited" : {
                "type" : "boolean",
                "required" : true
              },
              "value" : {
                "type" : "string",
                "required" : true
              }
            }
          },
          "idTokenSignedResponseAlg" : {
            "title" : "ID Token Signing Algorithm",
            "description" : "Algorithm the ID Token for this client must be signed with.",
            "propertyOrder" : 24500,
            "type" : "object",
            "exampleValue" : "",
            "properties" : {
              "inherited" : {
                "type" : "boolean",
                "required" : true
              },
              "value" : {
                "type" : "string",
                "required" : true
              }
            }
          }
        }
      },
      "advancedOAuth2ClientConfig" : {
        "type" : "object",
        "title" : "Advanced",
        "propertyOrder" : 1,
        "properties" : {
          "name" : {
            "title" : "Display name",
            "description" : "A client name that may be relevant to the resource owner when considering approval.<br><br>The name may be entered as a single string or as pipe separated strings for locale and localized name; e.g. \"en|The ExampleCo Intranet\". Locale strings are in the format <code>language + \"_\" + country + \"_\" + variant</code>, e.g. en, en_GB, en_US_WIN. If the locale is omitted, the name is displayed to all users having undefined locales. e.g. \"The ExampleCo Intranet\".",
            "propertyOrder" : 23500,
            "items" : {
              "type" : "string"
            },
            "type" : "object",
            "exampleValue" : "",
            "properties" : {
              "inherited" : {
                "type" : "boolean",
                "required" : true
              },
              "value" : {
                "type" : "array",
                "required" : false
              }
            }
          },
          "logoUri" : {
            "title" : "Logo URI",
            "description" : "The URI for the client's logo, for use in user-facing UIs such as consent pages and application pages.",
            "propertyOrder" : 25350,
            "items" : {
              "type" : "string"
            },
            "type" : "object",
            "exampleValue" : "",
            "properties" : {
              "inherited" : {
                "type" : "boolean",
                "required" : true
              },
              "value" : {
                "type" : "array",
                "required" : false
              }
            }
          },
          "grantTypes" : {
            "title" : "Grant Types",
            "description" : "The set of Grant Types (OAuth2 Flows) that are permitted to be used by this client.<br><br>If no Grant Types (OAuth2 Flows) are configured then AUTHORIZATION_CODE flow would be permitted by default.",
            "propertyOrder" : 23800,
            "items" : {
              "type" : "string"
            },
            "type" : "object",
            "exampleValue" : "",
            "properties" : {
              "inherited" : {
                "type" : "boolean",
                "required" : true
              },
              "value" : {
                "type" : "array",
                "required" : true
              }
            }
          },
          "subjectType" : {
            "title" : "Subject Type",
            "description" : "The subject type added to responses for this client. This value must be included in \"Subject Type Supported\" in OAuth2 Provider service setting.",
            "propertyOrder" : 24400,
            "type" : "object",
            "exampleValue" : "",
            "properties" : {
              "inherited" : {
                "type" : "boolean",
                "required" : true
              },
              "value" : {
                "type" : "string",
                "required" : true
              }
            }
          },
          "responseTypes" : {
            "title" : "Response Types",
            "description" : "Response types this client will support and use.",
            "propertyOrder" : 23800,
            "items" : {
              "type" : "string"
            },
            "type" : "object",
            "exampleValue" : "",
            "properties" : {
              "inherited" : {
                "type" : "boolean",
                "required" : true
              },
              "value" : {
                "type" : "array",
                "required" : true
              }
            }
          },
          "softwareIdentity" : {
            "title" : "Software Identity",
            "description" : "A unique identifier assigned by the client developer or software publisher to identity the client software.",
            "propertyOrder" : 35400,
            "type" : "object",
            "exampleValue" : "",
            "properties" : {
              "inherited" : {
                "type" : "boolean",
                "required" : true
              },
              "value" : {
                "type" : "string",
                "required" : false
              }
            }
          },
          "policyUri" : {
            "title" : "Privacy Policy URI",
            "description" : "The URI for the client's privacy policy, for use in user-facing consent pages.",
            "propertyOrder" : 25375,
            "items" : {
              "type" : "string"
            },
            "type" : "object",
            "exampleValue" : "",
            "properties" : {
              "inherited" : {
                "type" : "boolean",
                "required" : true
              },
              "value" : {
                "type" : "array",
                "required" : false
              }
            }
          },
          "allowedResourceServerAudienceValues" : {
            "title" : "Allowed Resource Server Audience Values",
            "description" : "List of audience (aud) claim values that are allowed for resource servers. The value(s) must match those expected by the resource server for which the access tokens are requested.",
            "propertyOrder" : 35900,
            "items" : {
              "type" : "string"
            },
            "type" : "object",
            "exampleValue" : "",
            "properties" : {
              "inherited" : {
                "type" : "boolean",
                "required" : true
              },
              "value" : {
                "type" : "array",
                "required" : false
              }
            }
          },
          "customProperties" : {
            "title" : "Custom Properties",
            "description" : "Additional properties that allow users to augment the set of properties supported by the OAuth2 Client. <br> Examples: <br> customproperty=custom-value1 <br> customlist[0]=customlist-value-0 <br> customlist[1]=customlist-value-1 <br> custommap[key1]=custommap-value-1 <br> custommap[key2]=custommap-value-2",
            "propertyOrder" : 35100,
            "items" : {
              "type" : "string"
            },
            "type" : "object",
            "exampleValue" : "",
            "properties" : {
              "inherited" : {
                "type" : "boolean",
                "required" : true
              },
              "value" : {
                "type" : "array",
                "required" : false
              }
            }
          },
          "sectorIdentifierUri" : {
            "title" : "Sector Identifier URI",
            "description" : "The Host component of this URL is used in the computation of pairwise Subject Identifiers.",
            "propertyOrder" : 24300,
            "type" : "object",
            "exampleValue" : "",
            "properties" : {
              "inherited" : {
                "type" : "boolean",
                "required" : true
              },
              "value" : {
                "type" : "string",
                "required" : false
              }
            }
          },
          "acceptedJwtIssuers" : {
            "title" : "Accepted JWT Issuers",
            "description" : "List of JWT issuers that will be accepted in addition to client_id for private key JWT authentication.",
            "propertyOrder" : 24250,
            "items" : {
              "type" : "string"
            },
            "type" : "object",
            "exampleValue" : "",
            "properties" : {
              "inherited" : {
                "type" : "boolean",
                "required" : true
              },
              "value" : {
                "type" : "array",
                "required" : false
              }
            }
          },
          "isConsentImplied" : {
            "title" : "Implied consent",
            "description" : "When enabled, the resource owner will not be asked for consent during authorization flows. The OAuth2 Provider must be configured to allow clients to skip consent.",
            "propertyOrder" : 26200,
            "type" : "object",
            "exampleValue" : "",
            "properties" : {
              "inherited" : {
                "type" : "boolean",
                "required" : true
              },
              "value" : {
                "type" : "boolean",
                "required" : true
              }
            }
          },
          "require_pushed_authorization_requests" : {
            "title" : "Require Pushed Authorization Requests",
            "description" : "If enabled, the client must use the PAR endpoint to initiate authorization requests. Note that, even if this value is set to false, the authorization server may be configured to enforce PAR for all clients.",
            "propertyOrder" : 35600,
            "type" : "object",
            "exampleValue" : "",
            "properties" : {
              "inherited" : {
                "type" : "boolean",
                "required" : true
              },
              "value" : {
                "type" : "boolean",
                "required" : true
              }
            }
          },
          "mixUpMitigation" : {
            "title" : "OAuth 2.0 Mix-Up Mitigation enabled",
            "description" : "Enables OAuth 2.0 mix-up mitigation on the authorization server side.<br><br>Enable this setting only if this OAuth 2.0 client supports the <a href=\"https://tools.ietf.org/html/draft-ietf-oauth-mix-up-mitigation-01\">OAuth 2.0 Mix-Up Mitigation draft</a>, otherwise AM will fail to validate access token requests received from this client.",
            "propertyOrder" : 26300,
            "type" : "object",
            "exampleValue" : "",
            "properties" : {
              "inherited" : {
                "type" : "boolean",
                "required" : true
              },
              "value" : {
                "type" : "boolean",
                "required" : true
              }
            }
          },
          "updateAccessToken" : {
            "title" : "Access Token",
            "description" : "The access token used to update the client.",
            "propertyOrder" : 25100,
            "type" : "object",
            "exampleValue" : "",
            "properties" : {
              "inherited" : {
                "type" : "boolean",
                "required" : true
              },
              "value" : {
                "type" : "string",
                "required" : false
              }
            }
          },
          "tokenEndpointAuthMethod" : {
            "title" : "Token Endpoint Authentication Method",
            "description" : "The authentication method with which a client authenticates to the authorization server at the token endpoint. The authentication method applies to OIDC requests with the openid scope.",
            "propertyOrder" : 24000,
            "type" : "object",
            "exampleValue" : "",
            "properties" : {
              "inherited" : {
                "type" : "boolean",
                "required" : true
              },
              "value" : {
                "type" : "string",
                "required" : true
              }
            }
          },
          "javascriptOrigins" : {
            "title" : "JavaScript Origins",
            "description" : "",
            "propertyOrder" : 23650,
            "items" : {
              "type" : "string"
            },
            "type" : "object",
            "exampleValue" : "",
            "properties" : {
              "inherited" : {
                "type" : "boolean",
                "required" : true
              },
              "value" : {
                "type" : "array",
                "required" : false
              }
            }
          },
          "refreshTokenGracePeriod" : {
            "title" : "Refresh Token Grace Period (seconds)",
            "description" : "The period, in seconds, that a refresh token can be replayed. This allows a client to recover if the response from the original refresh request is not received due to a network problem or other transient issue. <br>Applies only to tokens in a one-to-one storage scheme. Keep this value as short as possible â it must not exceed 120 seconds. To deactivate the grace period set the value to â1. If this value is set to 0, the Refresh Token Grace Period of the OAuth2 Provider will be used instead.",
            "propertyOrder" : 26150,
            "type" : "object",
            "exampleValue" : "",
            "properties" : {
              "inherited" : {
                "type" : "boolean",
                "required" : true
              },
              "value" : {
                "type" : "integer",
                "required" : true
              }
            }
          },
          "treeName" : {
            "title" : "Tree Name",
            "description" : "The name of the tree that the client is associated with.<br><br>When a client is associated with a tree, the configured Authentication Context Mapper is not executed. Instead, AM redirects to the configured tree.",
            "propertyOrder" : 25670,
            "type" : "object",
            "exampleValue" : "",
            "properties" : {
              "inherited" : {
                "type" : "boolean",
                "required" : true
              },
              "value" : {
                "type" : "string",
                "required" : false
              }
            }
          },
          "tokenExchangeAuthLevel" : {
            "title" : "Token Exchange Auth Level",
            "description" : "Auth level granted to tokens generated as a result of a Token Exchange, where the input token had no original auth_level claim. (e.g. When exchanging ID Token for an Access Token)",
            "propertyOrder" : 10100,
            "type" : "object",
            "exampleValue" : "",
            "properties" : {
              "inherited" : {
                "type" : "boolean",
                "required" : true
              },
              "value" : {
                "type" : "integer",
                "required" : true
              }
            }
          },
          "clientUri" : {
            "title" : "Client URI",
            "description" : "The URI for finding further information about the client from user-facing UIs.",
            "propertyOrder" : 25325,
            "items" : {
              "type" : "string"
            },
            "type" : "object",
            "exampleValue" : "",
            "properties" : {
              "inherited" : {
                "type" : "boolean",
                "required" : true
              },
              "value" : {
                "type" : "array",
                "required" : false
              }
            }
          },
          "contacts" : {
            "title" : "Contacts",
            "description" : "Email addresses of users who can administrate this client.",
            "propertyOrder" : 23900,
            "items" : {
              "type" : "string"
            },
            "type" : "object",
            "exampleValue" : "",
            "properties" : {
              "inherited" : {
                "type" : "boolean",
                "required" : true
              },
              "value" : {
                "type" : "array",
                "required" : false
              }
            }
          },
          "softwareVersion" : {
            "title" : "Software Version",
            "description" : "A version identifier string for the identifier defined in the Software Identity.",
            "propertyOrder" : 35500,
            "type" : "object",
            "exampleValue" : "",
            "properties" : {
              "inherited" : {
                "type" : "boolean",
                "required" : true
              },
              "value" : {
                "type" : "string",
                "required" : false
              }
            }
          },
          "requestUris" : {
            "title" : "Request uris",
            "description" : "Array of request_uri values that are pre-registered by the RP for use at the OP.<br><br>The entire Request URI MUST NOT exceed 512 ASCII characters and MUST use either HTTP or HTTPS. Otherwise the value will be ignored.",
            "propertyOrder" : 23700,
            "items" : {
              "type" : "string"
            },
            "type" : "object",
            "exampleValue" : "",
            "properties" : {
              "inherited" : {
                "type" : "boolean",
                "required" : true
              },
              "value" : {
                "type" : "array",
                "required" : false
              }
            }
          },
          "descriptions" : {
            "title" : "Display description",
            "description" : "A description of the client or other information that may be relevant to the resource owner when considering approval.<br><br>The description may be entered as a single string or as pipe separated strings for locale and localized name; e.g. \"en|The company intranet is requesting the following access permission\". Locale strings are in the format <code>language + \"_\" + country + \"_\" + variant</code>, e.g. en, en_GB, en_US_WIN. If the locale is omitted, the description is displayed to all users having undefined locales. e.g. \"The company intranet is requesting the following access permission\".",
            "propertyOrder" : 23600,
            "items" : {
              "type" : "string"
            },
            "type" : "object",
            "exampleValue" : "",
            "properties" : {
              "inherited" : {
                "type" : "boolean",
                "required" : true
              },
              "value" : {
                "type" : "array",
                "required" : false
              }
            }
          },
          "tosURI" : {
            "title" : "Terms of Service URI",
            "description" : "The URI for the client's terms of service.",
            "propertyOrder" : 25390,
            "items" : {
              "type" : "string"
            },
            "type" : "object",
            "exampleValue" : "",
            "properties" : {
              "inherited" : {
                "type" : "boolean",
                "required" : true
              },
              "value" : {
                "type" : "array",
                "required" : false
              }
            }
          }
        }
      },
      "coreOAuth2ClientConfig" : {
        "type" : "object",
        "title" : "Core",
        "propertyOrder" : 0,
        "properties" : {
          "loopbackInterfaceRedirection" : {
            "title" : "Allow wildcard ports in redirect URIs",
            "description" : "This flag indicates whether wildcards can be used for port numbers in redirect URIs. When this toggle is set to true and a wildcard is used the only allowed combinations of protocols and hosts are: http://127.0.0.1, https://127.0.0.1, http://[::1], https://[::1], http://localhost, https://localhost The wild cards are permitted only for the port values. For example - <code>http://localhost:80*</code>, <code>http://localhost:80?0/{path}</code>, <code>http://localhost:80[8-9]0/{path}</code>",
            "propertyOrder" : 23150,
            "type" : "object",
            "exampleValue" : "",
            "properties" : {
              "inherited" : {
                "type" : "boolean",
                "required" : true
              },
              "value" : {
                "type" : "boolean",
                "required" : false
              }
            }
          },
          "accessTokenLifetime" : {
            "title" : "Access Token Lifetime (seconds)",
            "description" : "The time in seconds an access token is valid for. <i>NB</i> If this field is set to zero, Access Token Lifetime of the OAuth2 Provider is used instead of.",
            "propertyOrder" : 26000,
            "type" : "object",
            "exampleValue" : "",
            "properties" : {
              "inherited" : {
                "type" : "boolean",
                "required" : true
              },
              "value" : {
                "type" : "integer",
                "required" : true
              }
            }
          },
          "clientName" : {
            "title" : "Client Name",
            "description" : "This value is a readable name for this client.",
            "propertyOrder" : 25300,
            "items" : {
              "type" : "string"
            },
            "type" : "object",
            "exampleValue" : "",
            "properties" : {
              "inherited" : {
                "type" : "boolean",
                "required" : true
              },
              "value" : {
                "type" : "array",
                "required" : false
              }
            }
          },
          "scopes" : {
            "title" : "Scope(s)",
            "description" : "Scope(s). Scopes are strings that are presented to the user for approval and included in tokens so that the protected resource may make decisions about what to give access to.<br><br>Scopes may be entered as simple strings or pipe separated strings representing the internal scope name, locale, and localized description; e.g. \"read|en|Permission to view email messages in your account\". Locale strings are in the format <code>language + \"_\" + country + \"_\" + variant</code>, e.g. en, en_GB, en_US_WIN. If the locale and pipe is omitted, the description is displayed to all users having undefined locales. e.g. \"read|Permission to view email messages in your account\". <i>NB</i> If the description is also omitted, nothing is displayed to all users, e.g. specifying \"read|\" would allow the scope \"read\" to be used by the client, but would not display it to the user when it was requested.",
            "propertyOrder" : 23300,
            "items" : {
              "type" : "string"
            },
            "type" : "object",
            "exampleValue" : "",
            "properties" : {
              "inherited" : {
                "type" : "boolean",
                "required" : true
              },
              "value" : {
                "type" : "array",
                "required" : false
              }
            }
          },
          "userpassword" : {
            "title" : "Client secret",
            "description" : "Client secret. Used when the client authenticates to AM if you don't store client secret in a secret store.This secret is ignored if you specify a Secret Label Identifier and the corresponding secret mapping.",
            "propertyOrder" : 23000,
            "required" : true,
            "type" : "string",
            "format" : "password",
            "exampleValue" : ""
          },
          "clientType" : {
            "title" : "Client type",
            "description" : "Type of OAuth 2.0 client. Confidential clients can keep their password secret, and are typically web apps or other server-based clients. Public clients run the risk of exposing their password to a host or user agent, such as rich browser applications or desktop clients.",
            "propertyOrder" : 23100,
            "type" : "object",
            "exampleValue" : "",
            "properties" : {
              "inherited" : {
                "type" : "boolean",
                "required" : true
              },
              "value" : {
                "type" : "string",
                "required" : true
              }
            }
          },
          "defaultScopes" : {
            "title" : "Default Scope(s)",
            "description" : "Default Scope(s). Scopes automatically given to tokens.<br><br>Default Scopes may be entered as simple strings or pipe separated strings representing the internal scope name, locale, and localized description; e.g. \"read|en|Permission to view email messages in your account\". Locale strings are in the format <code>language + \"_\" + country + \"_\" + variant</code>, e.g. en, en_GB, en_US_WIN. If the locale and pipe is omitted, the description is displayed to all users having undefined locales. e.g. \"read|Permission to view email messages in your account\". <i>NB</i> If the description is also omitted, nothing is displayed to all users, e.g. specifying \"read|\" would allow the scope \"read\" to be used by the client, but would not display it to the user when it was requested.",
            "propertyOrder" : 23700,
            "items" : {
              "type" : "string"
            },
            "type" : "object",
            "exampleValue" : "",
            "properties" : {
              "inherited" : {
                "type" : "boolean",
                "required" : true
              },
              "value" : {
                "type" : "array",
                "required" : false
              }
            }
          },
          "redirectionUris" : {
            "title" : "Redirection URIs",
            "description" : "Redirection URIs (optional for confidential clients). Complete URIs or URIs consisting of protocol + authority + path are registered so that the OAuth 2.0 provider can trust that tokens are sent to trusted entities. If multiple URI's are registered, the client MUST specify the URI that the user should be redirected to following approval. May not contain a fragment (#).",
            "propertyOrder" : 23200,
            "items" : {
              "type" : "string"
            },
            "type" : "object",
            "exampleValue" : "",
            "properties" : {
              "inherited" : {
                "type" : "boolean",
                "required" : true
              },
              "value" : {
                "type" : "array",
                "required" : false
              }
            }
          },
          "authorizationCodeLifetime" : {
            "title" : "Authorization Code Lifetime (seconds)",
            "description" : "The time in seconds an authorization code is valid for. <i>NB</i> If this field is set to zero, Authorization Code Lifetime of the OAuth2 Provider is used instead of.",
            "propertyOrder" : 25800,
            "type" : "object",
            "exampleValue" : "",
            "properties" : {
              "inherited" : {
                "type" : "boolean",
                "required" : true
              },
              "value" : {
                "type" : "integer",
                "required" : true
              }
            }
          },
          "status" : {
            "title" : "Status",
            "description" : "Status of the agent configuration.",
            "propertyOrder" : 200,
            "type" : "object",
            "exampleValue" : "",
            "properties" : {
              "inherited" : {
                "type" : "boolean",
                "required" : true
              },
              "value" : {
                "type" : "string",
                "required" : true
              }
            }
          },
          "refreshTokenLifetime" : {
            "title" : "Refresh Token Lifetime (seconds)",
            "description" : "The time in seconds a refresh token is valid for. <i>NB</i> If this field is set to zero, Refresh Token Lifetime of the OAuth2 Provider is used instead. If this field is set to -1, the token will never expire.",
            "propertyOrder" : 25900,
            "type" : "object",
            "exampleValue" : "",
            "properties" : {
              "inherited" : {
                "type" : "boolean",
                "required" : true
              },
              "value" : {
                "type" : "integer",
                "required" : true
              }
            }
          },
          "agentgroup" : {
            "title" : "Group",
            "description" : "Add the client to a group to allow inheritance of property values from the group. <br>Changing the group will update inherited property values. <br>Inherited property values are copied to the client.",
            "propertyOrder" : 100,
            "required" : false,
            "type" : "string",
            "exampleValue" : ""
          },
          "secretLabelIdentifier" : {
            "title" : "Secret Label Identifier",
            "description" : "AM uses this identifier to create secret labels, using the following templates: <br> <ul> <li><code>am.applications.oauth2.client.{{identifier}}.secret</code> for the <b>Client secret</b></li> <li><code>am.applications.oauth2.client.{{identifier}}.jwt.public.key</code> for the <b>Client JWT Bearer Public Key</b></li> <li><code>am.applications.oauth2.client.{{identifier}}.mtls.trusted.cert</code> for the <b>mTLS Self-Signed Certificate</b></li> <li><code>am.applications.oauth2.client.{{identifier}}.id.token.enc.public.key</code> for the <b>ID Token Encryption Public Key</b></li> </ul> where {{identifier}} is the Secret Label Identifier. <br> The Secret Label Identifier can only contain characters {{a-z}} {{A-Z}} {{0-9}} {{.}} and cannot start or end with {{.}}. <br>As a best practice, use a different Secret Label Identifier per OAuth2 client.",
            "propertyOrder" : 23050,
            "type" : "object",
            "exampleValue" : "",
            "properties" : {
              "inherited" : {
                "type" : "boolean",
                "required" : true
              },
              "value" : {
                "type" : "string",
                "required" : false
              }
            }
          }
        }
      },
      "coreOpenIDClientConfig" : {
        "type" : "object",
        "title" : "OpenID Connect",
        "propertyOrder" : 2,
        "properties" : {
          "defaultMaxAge" : {
            "title" : "Default Max Age",
            "description" : "Minimum value 0. Sets the maximum length of time in seconds a session may be active after the authorization service has succeeded before the user must actively re-authenticate.",
            "propertyOrder" : 25500,
            "type" : "object",
            "exampleValue" : "",
            "properties" : {
              "inherited" : {
                "type" : "boolean",
                "required" : true
              },
              "value" : {
                "type" : "integer",
                "required" : true
              }
            }
          },
          "defaultMaxAgeEnabled" : {
            "title" : "Default Max Age Enabled",
            "description" : "Whether or not the default max age is enforced.",
            "propertyOrder" : 25600,
            "type" : "object",
            "exampleValue" : "",
            "properties" : {
              "inherited" : {
                "type" : "boolean",
                "required" : true
              },
              "value" : {
                "type" : "boolean",
                "required" : true
              }
            }
          },
          "postLogoutRedirectUri" : {
            "title" : "Post Logout Redirect URIs",
            "description" : "URIs that can be redirected to after the client logout process.",
            "propertyOrder" : 25000,
            "items" : {
              "type" : "string"
            },
            "type" : "object",
            "exampleValue" : "",
            "properties" : {
              "inherited" : {
                "type" : "boolean",
                "required" : true
              },
              "value" : {
                "type" : "array",
                "required" : false
              }
            }
          },
          "jwtTokenLifetime" : {
            "title" : "OpenID Connect JWT Token Lifetime (seconds)",
            "description" : "The time in seconds a JWT is valid for. <i>NB</i> If this field is set to zero, JWT Token Lifetime of the OAuth2 Provider is used instead of.",
            "propertyOrder" : 26100,
            "type" : "object",
            "exampleValue" : "",
            "properties" : {
              "inherited" : {
                "type" : "boolean",
                "required" : true
              },
              "value" : {
                "type" : "integer",
                "required" : true
              }
            }
          },
          "backchannel_logout_session_required" : {
            "title" : "Backchannel Logout Session Required",
            "description" : "Boolean value specifying whether the RP requires that a sid (session ID) Claim be included in the Logout Token to identify the RP session with the OP when the Backchannel Logout URL is used.",
            "propertyOrder" : 35300,
            "type" : "object",
            "exampleValue" : "",
            "properties" : {
              "inherited" : {
                "type" : "boolean",
                "required" : true
              },
              "value" : {
                "type" : "boolean",
                "required" : true
              }
            }
          },
          "clientSessionUri" : {
            "title" : "Client Session URI",
            "description" : "This is the URI that will be used to check messages sent to the session management endpoints. This URI must match the origin of the message",
            "propertyOrder" : 25200,
            "type" : "object",
            "exampleValue" : "",
            "properties" : {
              "inherited" : {
                "type" : "boolean",
                "required" : true
              },
              "value" : {
                "type" : "string",
                "required" : false
              }
            }
          },
          "defaultAcrValues" : {
            "title" : "Default ACR values",
            "description" : "Default requested Authentication Context Class Reference values.<br><br>Array of strings that specifies the default acr values that the OP is being requested to use for processing requests from this Client, with the values appearing in order of preference. The Authentication Context Class satisfied by the authentication performed is returned as the acr Claim Value in the issued ID Token. The acr Claim is requested as a Voluntary Claim by this parameter. The acr_values_supported discovery element contains a list of the acr values supported by this server. Values specified in the acr_values request parameter or an individual acr Claim request override these default values.",
            "propertyOrder" : 25650,
            "items" : {
              "type" : "string"
            },
            "type" : "object",
            "exampleValue" : "",
            "properties" : {
              "inherited" : {
                "type" : "boolean",
                "required" : true
              },
              "value" : {
                "type" : "array",
                "required" : false
              }
            }
          },
          "claims" : {
            "title" : "Claim(s)",
            "description" : "List of claim name translations, which will override those specified for the AS. Claims are values that are presented to the user to inform them what data is being made available to the Client.<br><br>Claims may be entered as simple strings or pipe separated strings representing the internal claim name, locale, and localized description; e.g. \"name|en|Your full name\". Locale strings are in the format <code>language + \"_\" + country + \"_\" + variant</code>, e.g. en, en_GB, en_US_WIN. If the locale and pipe is omitted, the description is displayed to all users having undefined locales. e.g. \"name|Your full name\". <i>NB</i> If the description is also omitted, nothing is displayed to all users, e.g. specifying \"name|\" would allow the claim \"name\" to be used by the client, but would not display it to the user when it was requested.<p>If a value is not given here, the value will be computed from the OAuth 2 Provider settings.</p>",
            "propertyOrder" : 23400,
            "items" : {
              "type" : "string"
            },
            "type" : "object",
            "exampleValue" : "",
            "properties" : {
              "inherited" : {
                "type" : "boolean",
                "required" : true
              },
              "value" : {
                "type" : "array",
                "required" : false
              }
            }
          },
          "backchannel_logout_uri" : {
            "title" : "Backchannel Logout URL",
            "description" : "RP URL that will cause the RP to log itself out when sent a Logout Token by the OP. This URL SHOULD use the https scheme and MAY contain port, path, and query parameter components; however, it MAY use the http scheme, provided that the Client Type is confidential, as defined in Section 2.1 of OAuth 2.0 [RFC6749], and provided the OP allows the use of http RP URIs.",
            "propertyOrder" : 35200,
            "type" : "object",
            "exampleValue" : "",
            "properties" : {
              "inherited" : {
                "type" : "boolean",
                "required" : true
              },
              "value" : {
                "type" : "string",
                "required" : false
              }
            }
          }
        }
      },
      "coreUmaClientConfig" : {
        "type" : "object",
        "title" : "UMA",
        "propertyOrder" : 4,
        "properties" : {
          "claimsRedirectionUris" : {
            "title" : "Claims Redirection URIs",
            "description" : "Redirection URIs for returning to the client from UMA claims collection. If multiple URIs are registered, the client MUST specify the URI that the user should be redirected to following approval. May not contain a fragment (#).",
            "propertyOrder" : 23200,
            "items" : {
              "type" : "string"
            },
            "type" : "object",
            "exampleValue" : "",
            "properties" : {
              "inherited" : {
                "type" : "boolean",
                "required" : true
              },
              "value" : {
                "type" : "array",
                "required" : false
              }
            }
          }
        }
      }
    }
  }
  ```

### delete

**Usage**

```
am> delete AIAgents --realm Realm --id id
```

**Parameters**

* *\--id*

  The unique identifier for the resource.

### getAllTypes

Obtain the collection of all secondary configuration types related to the resource.

**Usage**

```
am> action AIAgents --realm Realm --actionName getAllTypes
```

### getCreatableTypes

Obtain the collection of secondary configuration types that have yet to be added to the resource.

**Usage**

```
am> action AIAgents --realm Realm --actionName getCreatableTypes
```

### nextdescendents

Obtain the collection of secondary configuration instances that have been added to the resource.

**Usage**

```
am> action AIAgents --realm Realm --actionName nextdescendents
```

### query

Querying the agents of a specific type

**Usage**

```
am> query AIAgents --realm Realm --filter filter
```

**Parameters**

* *\--filter*

  A CREST formatted query filter, where "true" will query all.

### read

**Usage**

```
am> read AIAgents --realm Realm --id id
```

**Parameters**

* *\--id*

  The unique identifier for the resource.

### update

**Usage**

```
am> update AIAgents --realm Realm --id id --body body
```

**Parameters**

* *\--id*

  The unique identifier for the resource.

* *\--body*

  The resource in JSON format, described by the following JSON schema:

  ```json
  {
    "type" : "object",
    "properties" : {
      "overrideOAuth2ClientConfig" : {
        "type" : "object",
        "title" : "OAuth2 Provider Overrides",
        "propertyOrder" : 5,
        "properties" : {
          "accessTokenModificationScript" : {
            "title" : "Access Token Modification Script",
            "description" : "The plugin that is executed when issuing an access token. <p>The plugin can change the access token's internal data structure to include or exclude particular fields.",
            "propertyOrder" : 40400,
            "required" : true,
            "type" : "string",
            "exampleValue" : ""
          },
          "oidcMayActScript" : {
            "title" : "OIDC ID Token May Act Script",
            "description" : "The script that is executed when issuing an OIDC ID Token explicitly to modify the <code>may_act</code> claim placed on the token.",
            "propertyOrder" : 40600,
            "required" : true,
            "type" : "string",
            "exampleValue" : ""
          },
          "usePolicyEngineForScope" : {
            "title" : "Use Policy Engine for Scope decisions",
            "description" : "With this setting enabled, the policy engine is consulted for each scope value that is requested.<br><br>If a policy returns an action of GRANT=true, the scope is consented automatically, and the user is not consulted in a user-interaction flow. If a policy returns an action of GRANT=false, the scope is not added to any resulting token, and the user will not see it in a user-interaction flow. If no policy returns a value for the GRANT action, then if the grant type is user-facing (i.e. authorization or device code flows), the user is asked for consent (or saved consent is used), and if the grant type is not user-facing (password or client credentials), the scope is not added to any resulting token.",
            "propertyOrder" : 40300,
            "required" : true,
            "type" : "boolean",
            "exampleValue" : ""
          },
          "customLoginUrlTemplate" : {
            "title" : "Custom Login URL Template",
            "description" : "Custom URL for handling login, to override the default OpenAM login page.<br><br>Supports Freemarker syntax, with the following variables:<table><tr><th>Variable</th><th>Description</th></tr><tr><td><code>gotoUrl</code></td><td><p>The URL to redirect to after login.</p></td></tr><tr><td><code>acrValues</code></td><td><p>The Authentication Context Class Reference (acr) values for the authorization request.</p></td></tr><tr><td><code>realm</code></td><td><p>The OpenAM realm the authorization request was made on.</p></td></tr><tr><td><code>module</code></td><td><p>The name of the OpenAM authentication module requested to perform resource owner authentication.</p></td></tr><tr><td><code>service</code></td><td><p>The name of the OpenAM authentication chain requested to perform resource owner authentication.</p></td></tr><tr><td><code>locale</code></td><td><p>A space-separated list of locales, ordered by preference.</p></td></tr></table>The following example template redirects users to a non-OpenAM front end to handle login, which will then redirect back to the <code>/oauth2/authorize</code> endpoint with any required parameters:<p> <code>http://mylogin.com/login?goto=${goto}&lt;#if acrValues??&gt;&amp;acr_values=${acrValues}&lt;&#x2F;#if&gt;&lt;#if realm??&gt;&amp;realm=${realm}&lt;&#x2F;#if&gt;&lt;#if module??&gt;&amp;module=${module}&lt;&#x2F;#if&gt;&lt;#if service??&gt;&amp;service=${service}&lt;&#x2F;#if&gt;&lt;#if locale??&gt;&amp;locale=${locale}&lt;&#x2F;#if&gt;</code><br><b>NOTE</b>: Default OpenAM login page is constructed using \"Base URL Source\" service.",
            "propertyOrder" : 40900,
            "required" : false,
            "type" : "string",
            "exampleValue" : ""
          },
          "evaluateScopeClass" : {
            "title" : "Scope Evaluation Plugin Implementation Class",
            "description" : "The plugin that is executed when retrieving access token's information. <p>The plugin can provide a mechanism to associate scopes with profile attribute values, such as if one of the scopes is mail, the resource owner's email address is provided in the information returned. <p>The provided plugin class must implement the scope evaluation plugin interface: <code>org.forgerock.oauth2.core.plugins.ScopeEvaluator</code> <p>If this field is empty and the Plugin Type of JAVA is selected, the default implementation will be used: <code>org.forgerock.oauth2.core.plugins.registry.DefaultScopeEvaluator</code>",
            "propertyOrder" : 42300,
            "required" : false,
            "type" : "string",
            "exampleValue" : ""
          },
          "authorizeEndpointDataProviderPluginType" : {
            "title" : "Authorize Endpoint Data Provider Plugin Type",
            "description" : "When the plugin type is SCRIPTED then the Authorize Endpoint Data Provider Script will be executed and when plugin type is JAVA then the Authorize Endpoint Data Provider Plugin Implementation Class will be executed. If the plugin type is PROVIDER the client override is disabled and the plugin configured on the OAuth2 Provider is used.",
            "propertyOrder" : 42700,
            "required" : true,
            "type" : "string",
            "exampleValue" : ""
          },
          "tokenEncryptionEnabled" : {
            "title" : "Encrypt Client-Side Tokens",
            "description" : "Whether client-side access and refresh tokens should be encrypted.<br><br>Enabling token encryption will disable token signing as encryption is performed using direct symmetric encryption.",
            "propertyOrder" : 41100,
            "required" : true,
            "type" : "boolean",
            "exampleValue" : ""
          },
          "accessTokenMayActScript" : {
            "title" : "OAuth2 Access Token May Act Script",
            "description" : "The script that is executed when issuing an access token explicitly to modify the <code>may_act</code> claim placed on the token.",
            "propertyOrder" : 40500,
            "required" : true,
            "type" : "string",
            "exampleValue" : ""
          },
          "statelessTokensEnabled" : {
            "title" : "Use Client-Side Access & Refresh Tokens",
            "description" : "When enabled, OpenAM issues access and refresh tokens that can be inspected by resource servers.",
            "propertyOrder" : 41000,
            "required" : true,
            "type" : "boolean",
            "exampleValue" : ""
          },
          "evaluateScopePluginType" : {
            "title" : "Scope Evaluation Plugin Type",
            "description" : "When the plugin type is SCRIPTED then the Scope Evaluation Script will be executed and when plugin type is JAVA then the Scope Evaluation Plugin Implementation Class will be executed. If the plugin type is PROVIDER the client override is disabled and the plugin configured on the OAuth2 Provider is used.",
            "propertyOrder" : 42100,
            "required" : true,
            "type" : "string",
            "exampleValue" : ""
          },
          "clientsCanSkipConsent" : {
            "title" : "Allow Clients to Skip Consent",
            "description" : "If enabled, clients may be configured so that the resource owner will not be asked for consent during authorization flows.",
            "propertyOrder" : 41300,
            "required" : true,
            "type" : "boolean",
            "exampleValue" : ""
          },
          "validateScopeClass" : {
            "title" : "Scope Validation Plugin Implementation Class",
            "description" : "The plugin that is executed when validating or customising the set of requested scopes for authorize, access token, refresh token and back channel authorize requests. <p>The provided plugin class must implement the scope validation plugin interface: <code>org.forgerock.oauth2.core.plugins.ScopeValidator</code> <p>If this field is empty and the Plugin Type of JAVA is selected, the default implementation will be used: <code>org.forgerock.oauth2.core.plugins.registry.DefaultScopeValidator</code>",
            "propertyOrder" : 42600,
            "required" : false,
            "type" : "string",
            "exampleValue" : ""
          },
          "evaluateScopeScript" : {
            "title" : "Scope Evaluation Script",
            "description" : "The plugin that is executed when retrieving access token's information. <p>The plugin can provide a mechanism to associate scopes with profile attribute values, such as if one of the scopes is mail, the resource owner's email address is provided in the information returned.",
            "propertyOrder" : 42200,
            "required" : true,
            "type" : "string",
            "exampleValue" : ""
          },
          "authorizeEndpointDataProviderScript" : {
            "title" : "Authorize Endpoint Data Provider Script",
            "description" : "The plugin that is executed to return additional data from the authorization request.",
            "propertyOrder" : 42800,
            "required" : true,
            "type" : "string",
            "exampleValue" : ""
          },
          "providerOverridesEnabled" : {
            "title" : "Enable OAuth2 Provider Overrides",
            "description" : "Enabling this causes the other config in this section to override the default OAuth2 Provider behaviour.",
            "propertyOrder" : 40000,
            "required" : true,
            "type" : "boolean",
            "exampleValue" : ""
          },
          "enableApplicationContext" : {
            "title" : "Enable Application Context",
            "description" : "When enabled, this setting makes the application context available in all OAuth2 / OIDC flows for this client as the <code>oauthApplication</code> binding in scripted decision node scripts.",
            "propertyOrder" : 43500,
            "required" : true,
            "type" : "boolean",
            "exampleValue" : ""
          },
          "remoteConsentServiceId" : {
            "title" : "Remote Consent Service ID",
            "description" : "The ID of an existing remote consent service agent.",
            "propertyOrder" : 41500,
            "required" : false,
            "type" : "string",
            "exampleValue" : ""
          },
          "accessTokenModificationPluginType" : {
            "title" : "Access Token Modification Plugin Type",
            "description" : "When the plugin type is SCRIPTED then the Access Token Modification Script will be executed and when plugin type is JAVA then the Access Token Modifier Plugin Implementation Class will be executed. If the plugin type is PROVIDER the client override is disabled and the plugin configured on the OAuth2 Provider is used.",
            "propertyOrder" : 40390,
            "required" : true,
            "type" : "string",
            "exampleValue" : ""
          },
          "authorizeEndpointDataProviderClass" : {
            "title" : "Authorize Endpoint Data Provider Plugin Implementation Class",
            "description" : "The plugin that is executed to return additional data from the authorization request. <<p>The provided plugin class must implement the scope evaluation plugin interface: <code>org.forgerock.oauth2.core.plugins.AuthorizeEndpointDataProvider</code> <p>If this field is empty and the Plugin Type of JAVA is selected, the default implementation will be used: <code>org.forgerock.oauth2.core.plugins.registry.DefaultEndpointDataProvider</code>",
            "propertyOrder" : 42900,
            "required" : false,
            "type" : "string",
            "exampleValue" : ""
          },
          "oidcClaimsPluginType" : {
            "title" : "OIDC Claims Plugin Type",
            "description" : "When the plugin type is SCRIPTED then the OIDC Claims Script will be executed and when plugin type is JAVA then the OIDC Claims Plugin Implementation Class will be executed. If the plugin type is PROVIDER the client override is disabled and the plugin configured on the OAuth2 Provider is used.",
            "propertyOrder" : 40690,
            "required" : true,
            "type" : "string",
            "exampleValue" : ""
          },
          "acceptAudienceParametersInTokenExchangeRequests" : {
            "title" : "Accept Audience Parameters in Token Exchange Requests",
            "description" : "When enabled, AM validates audience parameter values in Token Exchange requests against the values defined in Allowed Resource Server Audience Values. If validation fails, the token exchange request is rejected.",
            "propertyOrder" : 43600,
            "required" : true,
            "type" : "boolean",
            "exampleValue" : ""
          },
          "oidcClaimsClass" : {
            "title" : "OIDC Claims Plugin Implementation Class",
            "description" : "The plugin that is executed when issuing an ID token or making a request to the <i>userinfo</i> endpoint during OpenID requests.<p>The plugin gathers the scopes and populates claims, and has access to the access token, the user's identity and, if available, the user's session. <p>This plugin provides the custom implementation for the OIDC claims plugin interface: <code>org.forgerock.oauth2.core.plugins.UserInfoClaimsPlugin</code> <p>This field cannot be empty if the Plugin Type of JAVA is selected. Failure to provide a valid implementation of the OIDC claims plugin interface will cause OAuth2 flows to fail.",
            "propertyOrder" : 40710,
            "required" : false,
            "type" : "string",
            "exampleValue" : ""
          },
          "oidcClaimsScript" : {
            "title" : "OIDC Claims Script",
            "description" : "The plugin that is executed when issuing an ID token or making a request to the <i>userinfo</i> endpoint during OpenID requests.<p>The plugin gathers the scopes and populates claims, and has access to the access token, the user's identity and, if available, the user's session.",
            "propertyOrder" : 40700,
            "required" : true,
            "type" : "string",
            "exampleValue" : ""
          },
          "issueRefreshToken" : {
            "title" : "Issue Refresh Tokens",
            "description" : "Whether to issue a refresh token when returning an access token.",
            "propertyOrder" : 40100,
            "required" : true,
            "type" : "boolean",
            "exampleValue" : ""
          },
          "useTokenIntrospectionClaimForJWT" : {
            "title" : "Use token_introspection claim for JWT",
            "description" : "When enabled, the JWT introspection response complies with RFC 9701. This ensures the introspection data is nested within the <code>token_introspection</code> claim in the JWT response. <br><b>Note:</b> Enabling this option also causes the JSON introspection response to include the token's <code>aud</code> claim, if present.",
            "propertyOrder" : 43700,
            "required" : true,
            "type" : "boolean",
            "exampleValue" : ""
          },
          "issueRefreshTokenOnRefreshedToken" : {
            "title" : "Issue Refresh Tokens on Refreshing Access Tokens",
            "description" : "Whether to issue a refresh token when refreshing an access token.",
            "propertyOrder" : 40200,
            "required" : true,
            "type" : "boolean",
            "exampleValue" : ""
          },
          "accessTokenModifierClass" : {
            "title" : "Access Token Modifier Plugin Implementation Class",
            "description" : "The plugin that is executed when issuing an access token. <p>The plugin can change the access token's internal data structure to include or exclude particular fields. <p>This plugin provides the custom implementation for the access token modifier plugin interface: <code>org.forgerock.oauth2.core.plugins.AccessTokenModifier</code> <p>This field cannot be empty if the Plugin Type of JAVA is selected. Failure to provide a valid implementation of the access token modifier plugin interface will cause OAuth2 flows to fail.",
            "propertyOrder" : 40410,
            "required" : false,
            "type" : "string",
            "exampleValue" : ""
          },
          "validateScopeScript" : {
            "title" : "Scope Validation Script",
            "description" : "The plugin that is executed when validating or customising the set of requested scopes for authorize, access token, refresh token and back channel authorize requests.",
            "propertyOrder" : 42500,
            "required" : false,
            "type" : "string",
            "exampleValue" : ""
          },
          "enableRemoteConsent" : {
            "title" : "Enable Remote Consent",
            "description" : "",
            "propertyOrder" : 41400,
            "required" : true,
            "type" : "boolean",
            "exampleValue" : ""
          },
          "useForceAuthnForMaxAge" : {
            "title" : "Use Force Authentication for max_age",
            "description" : "When this setting is <code>false</code> (default)<ul><li>Attempted authorization when the max_age has passed will log the existing session out and start a re-authentication</li></ul> <ul><li>Re-authentication triggered by the max_age parameter will create a new session</li></ul> When this setting is <code>true</code> <ul><li>Attempted authorization when the max_age has passed will not destroy the existing session</li></ul> <ul><li>Re-authentication triggered by the max_age parameter will return the same session. The advanced server property org.forgerock.openam.authentication.forceAuth.enabled must be set to <code>true</code></li></ul> <p>For security reasons, it is strongly recommended that you leave <code>Use Force Authentication for max_age</code> set to the default value (<code>false</code>), so that a new session is created when the user re-authenticates.</p>",
            "propertyOrder" : 40850,
            "required" : true,
            "type" : "boolean",
            "exampleValue" : ""
          },
          "scopesPolicySet" : {
            "title" : "Scopes Policy Set",
            "description" : "The policy set that defines the context in which policy evaluations occur when Use Policy Engine for Scope decisions is enabled on the OAuth2 provider. If blank will default to the oauth2Scopes policy set.",
            "propertyOrder" : 40310,
            "required" : false,
            "type" : "string",
            "exampleValue" : ""
          },
          "overrideableOIDCClaims" : {
            "title" : "Overrideable Id_Token Claims",
            "description" : "List of claims in the id_token that may be overrideable in the OIDC Claims Script. These should be the subset of the core OpenID Connect Claims like aud or azp.",
            "propertyOrder" : 43300,
            "required" : false,
            "items" : {
              "type" : "string"
            },
            "type" : "array",
            "exampleValue" : ""
          },
          "validateScopePluginType" : {
            "title" : "Scope Validation Plugin Type",
            "description" : "When the plugin type is SCRIPTED then the Scope Validation Script will be executed and when plugin type is JAVA then the Scope Validation Plugin Implementation Class will be executed. If the plugin type is PROVIDER the client override is disabled and the plugin configured on the OAuth2 Provider is used.",
            "propertyOrder" : 42400,
            "required" : true,
            "type" : "string",
            "exampleValue" : ""
          }
        }
      },
      "signEncOAuth2ClientConfig" : {
        "type" : "object",
        "title" : "Signing and Encryption",
        "propertyOrder" : 3,
        "properties" : {
          "authorizationResponseEncryptionMethod" : {
            "title" : "Authorization Response JWT Encryption Method",
            "description" : "Encryption method the Authorization Response JWT for this client must be encrypted with.",
            "propertyOrder" : 24804,
            "type" : "object",
            "exampleValue" : "",
            "properties" : {
              "inherited" : {
                "type" : "boolean",
                "required" : true
              },
              "value" : {
                "type" : "string",
                "required" : false
              }
            }
          },
          "idTokenEncryptionAlgorithm" : {
            "title" : "ID Token Encryption Algorithm",
            "description" : "Algorithm the ID Token for this client must be encrypted with.",
            "propertyOrder" : 24700,
            "type" : "object",
            "exampleValue" : "",
            "properties" : {
              "inherited" : {
                "type" : "boolean",
                "required" : true
              },
              "value" : {
                "type" : "string",
                "required" : true
              }
            }
          },
          "requestParameterEncryptedEncryptionAlgorithm" : {
            "title" : "Request parameter encryption method",
            "description" : "JWE enc algorithm for encrypting the request parameter.<br><br>AM supports the following token encryption algorithms:<ul><li><code>A128GCM</code>, <code>A192GCM</code>, and <code>A256GCM</code> - AES in Galois Counter Mode (GCM) authenticated encryption mode.</li><li><code>A128CBC-HS256</code>, <code>A192CBC-HS384</code>, and <code>A256CBC-HS512</code> - AES encryption in CBC mode, with HMAC-SHA-2 for integrity.</li></ul>",
            "propertyOrder" : 27700,
            "type" : "object",
            "exampleValue" : "",
            "properties" : {
              "inherited" : {
                "type" : "boolean",
                "required" : true
              },
              "value" : {
                "type" : "string",
                "required" : true
              }
            }
          },
          "userinfoSignedResponseAlg" : {
            "title" : "User info signed response algorithm",
            "description" : "JWS algorithm for signing UserInfo Responses. If this is specified, the response will be JWT <a href=\"https://tools.ietf.org/html/rfc7519\">JWT</a> serialized, and signed using JWS. The default, if omitted, is for the UserInfo Response to return the Claims as a UTF-8 encoded JSON object using the application/json content-type.",
            "propertyOrder" : 27200,
            "type" : "object",
            "exampleValue" : "",
            "properties" : {
              "inherited" : {
                "type" : "boolean",
                "required" : true
              },
              "value" : {
                "type" : "string",
                "required" : false
              }
            }
          },
          "tokenEndpointAuthSigningAlgorithm" : {
            "title" : "Token Endpoint Authentication Signing Algorithm",
            "description" : "The JWS algorithm that MUST be used for signing the JWT used to authenticate the Client at the Token Endpointfor the private_key_jwt and client_secret_jwt authentication methods. All Token Requests using these authentication methods from this Client MUST be rejected, if the JWT is not signed with this algorithm.",
            "propertyOrder" : 24130,
            "type" : "object",
            "exampleValue" : "",
            "properties" : {
              "inherited" : {
                "type" : "boolean",
                "required" : true
              },
              "value" : {
                "type" : "string",
                "required" : true
              }
            }
          },
          "mTLSTrustedCert" : {
            "title" : "mTLS Self-Signed Certificate",
            "description" : "Self-signed PEM-encoded or DER-encoded X.509 certificate for mTLS client certificate authentication. This value is ignored if you specify a Secret Label Identifier and a corresponding secret mapping.",
            "propertyOrder" : 25405,
            "type" : "object",
            "exampleValue" : "",
            "properties" : {
              "inherited" : {
                "type" : "boolean",
                "required" : true
              },
              "value" : {
                "type" : "string",
                "required" : false
              }
            }
          },
          "tokenIntrospectionEncryptedResponseAlg" : {
            "title" : "Token introspection response encryption algorithm",
            "description" : "JWE \"alg\" algorithm REQUIRED for encrypting introspection responses. Sets the algorithm that will be used to encrypt the Content Encryption Key when the chosen introspection response format is 'signed then encrypted'.",
            "propertyOrder" : 27820,
            "type" : "object",
            "exampleValue" : "",
            "properties" : {
              "inherited" : {
                "type" : "boolean",
                "required" : true
              },
              "value" : {
                "type" : "string",
                "required" : true
              }
            }
          },
          "jwkSet" : {
            "title" : "Json Web Key",
            "description" : "Raw JSON Web Key value containing the client's public keys.",
            "propertyOrder" : 24200,
            "type" : "object",
            "exampleValue" : "",
            "properties" : {
              "inherited" : {
                "type" : "boolean",
                "required" : true
              },
              "value" : {
                "type" : "string",
                "required" : false
              }
            }
          },
          "userinfoResponseFormat" : {
            "title" : "User info response format.",
            "description" : "The user info endpoint offers different output format. See http://openid.net/specs/openid-connect-core-1_0.html#UserInfoResponse",
            "propertyOrder" : 27100,
            "type" : "object",
            "exampleValue" : "",
            "properties" : {
              "inherited" : {
                "type" : "boolean",
                "required" : true
              },
              "value" : {
                "type" : "string",
                "required" : true
              }
            }
          },
          "userinfoEncryptedResponseEncryptionAlgorithm" : {
            "title" : "User info encrypted response encryption algorithm",
            "description" : "JWE enc algorithm for encrypting UserInfo Responses. If userinfo encrypted response algorithm is specified, the default for this value is A128CBC-HS256. When user info encrypted response encryption is included, user info encrypted response algorithm MUST also be provided.<br><br>AM supports the following token encryption algorithms:<ul><li><code>A128GCM</code>, <code>A192GCM</code>, and <code>A256GCM</code> - AES in Galois Counter Mode (GCM) authenticated encryption mode.</li><li><code>A128CBC-HS256</code>, <code>A192CBC-HS384</code>, and <code>A256CBC-HS512</code> - AES encryption in CBC mode, with HMAC-SHA-2 for integrity.</li></ul>",
            "propertyOrder" : 27400,
            "type" : "object",
            "exampleValue" : "",
            "properties" : {
              "inherited" : {
                "type" : "boolean",
                "required" : true
              },
              "value" : {
                "type" : "string",
                "required" : true
              }
            }
          },
          "tokenIntrospectionResponseFormat" : {
            "title" : "Token introspection response format",
            "description" : "The token introspection endpoint offers different output format. see https://tools.ietf.org/html/draft-ietf-oauth-jwt-introspection-response-03",
            "propertyOrder" : 27800,
            "type" : "object",
            "exampleValue" : "",
            "properties" : {
              "inherited" : {
                "type" : "boolean",
                "required" : true
              },
              "value" : {
                "type" : "string",
                "required" : true
              }
            }
          },
          "publicKeyLocation" : {
            "title" : "Public key selector",
            "description" : "Select the public key for this client to come from either the jwks_uri, manual jwks or X509 field.",
            "propertyOrder" : 25700,
            "type" : "object",
            "exampleValue" : "",
            "properties" : {
              "inherited" : {
                "type" : "boolean",
                "required" : true
              },
              "value" : {
                "type" : "string",
                "required" : true
              }
            }
          },
          "tokenIntrospectionEncryptedResponseEncryptionAlgorithm" : {
            "title" : "Token introspection encrypted response encryption algorithm",
            "description" : "JWE 'enc' algorithm REQUIRED for encrypting token introspection responses. Sets the algorithm that will be used to encrypt the Plaintext of a JWE when the chosen introspection response format is 'signed then encrypted'.",
            "propertyOrder" : 27830,
            "type" : "object",
            "exampleValue" : "",
            "properties" : {
              "inherited" : {
                "type" : "boolean",
                "required" : true
              },
              "value" : {
                "type" : "string",
                "required" : true
              }
            }
          },
          "jwkStoreCacheMissCacheTime" : {
            "title" : "JWKs URI content cache miss cache time",
            "description" : "To avoid loading the JWKS URI content for every token signature verification, especially when the kid is not in the jwks content already cached, the JWKS content will be cache for a minimum period of time. This cache miss cache time defines the minimum of time the JWKS URI content is cache.",
            "propertyOrder" : 24120,
            "type" : "object",
            "exampleValue" : "",
            "properties" : {
              "inherited" : {
                "type" : "boolean",
                "required" : true
              },
              "value" : {
                "type" : "integer",
                "required" : true
              }
            }
          },
          "requestParameterEncryptedAlg" : {
            "title" : "Request parameter encryption algorithm",
            "description" : "JWE algorithm for encrypting the request parameter.",
            "propertyOrder" : 27600,
            "type" : "object",
            "exampleValue" : "",
            "properties" : {
              "inherited" : {
                "type" : "boolean",
                "required" : true
              },
              "value" : {
                "type" : "string",
                "required" : false
              }
            }
          },
          "idTokenEncryptionMethod" : {
            "title" : "ID Token Encryption Method",
            "description" : "Encryption method the ID Token for this client must be encrypted with.",
            "propertyOrder" : 24800,
            "type" : "object",
            "exampleValue" : "",
            "properties" : {
              "inherited" : {
                "type" : "boolean",
                "required" : true
              },
              "value" : {
                "type" : "string",
                "required" : true
              }
            }
          },
          "jwksUri" : {
            "title" : "Json Web Key URI",
            "description" : "The uri that contains the client's public keys in Json Web Key format.",
            "propertyOrder" : 24100,
            "type" : "object",
            "exampleValue" : "https://{{jwks-www}}/oauth2/{{realm}}/connect/jwk_uri",
            "properties" : {
              "inherited" : {
                "type" : "boolean",
                "required" : true
              },
              "value" : {
                "type" : "string",
                "required" : false
              }
            }
          },
          "userinfoEncryptedResponseAlg" : {
            "title" : "User info encrypted response algorithm",
            "description" : "JWE algorithm for encrypting UserInfo Responses. If both signing and encryption are requested, the response will be signed then encrypted, with the result being a Nested JWT. The default, if omitted, is that no encryption is performed.",
            "propertyOrder" : 27300,
            "type" : "object",
            "exampleValue" : "",
            "properties" : {
              "inherited" : {
                "type" : "boolean",
                "required" : true
              },
              "value" : {
                "type" : "string",
                "required" : false
              }
            }
          },
          "authorizationResponseEncryptionAlgorithm" : {
            "title" : "Authorization Response JWT Encryption Algorithm",
            "description" : "Algorithm the Authorization Response JWT for this client must be encrypted with.",
            "propertyOrder" : 24803,
            "type" : "object",
            "exampleValue" : "",
            "properties" : {
              "inherited" : {
                "type" : "boolean",
                "required" : true
              },
              "value" : {
                "type" : "string",
                "required" : false
              }
            }
          },
          "requestParameterSignedAlg" : {
            "title" : "Request parameter signing algorithm",
            "description" : "JWS algorithm for signing the request parameter.",
            "propertyOrder" : 27500,
            "type" : "object",
            "exampleValue" : "",
            "properties" : {
              "inherited" : {
                "type" : "boolean",
                "required" : true
              },
              "value" : {
                "type" : "string",
                "required" : false
              }
            }
          },
          "mTLSCertificateBoundAccessTokens" : {
            "title" : "Use Certificate-Bound Access Tokens",
            "description" : "Whether access tokens issued to this client should be bound to the X.509 certificate it uses to authenticate to the token endpoint. If enabled (and the provider supports it) then an x5t#S256 confirmation key will be added to all access tokens with the SHA-256 hash of the client's certificate.",
            "propertyOrder" : 25507,
            "type" : "object",
            "exampleValue" : "",
            "properties" : {
              "inherited" : {
                "type" : "boolean",
                "required" : true
              },
              "value" : {
                "type" : "boolean",
                "required" : true
              }
            }
          },
          "jwksCacheTimeout" : {
            "title" : "JWKs URI content cache timeout in ms",
            "description" : "To avoid loading the JWKS URI content for every token encryption, the JWKS content is cached. This timeout defines the maximum of time the JWKS URI content can be cached before being refreshed.",
            "propertyOrder" : 24110,
            "type" : "object",
            "exampleValue" : "",
            "properties" : {
              "inherited" : {
                "type" : "boolean",
                "required" : true
              },
              "value" : {
                "type" : "integer",
                "required" : true
              }
            }
          },
          "mTLSSubjectDN" : {
            "title" : "mTLS Subject DN",
            "description" : "Expected Subject DN of certificate used for mTLS client certificate authentication. Defaults to CN=&lt;client_id&gt;. Only applicable when using CA-signed certificates.",
            "propertyOrder" : 25406,
            "type" : "object",
            "exampleValue" : "",
            "properties" : {
              "inherited" : {
                "type" : "boolean",
                "required" : true
              },
              "value" : {
                "type" : "string",
                "required" : false
              }
            }
          },
          "idTokenEncryptionEnabled" : {
            "title" : "Enable ID Token Encryption",
            "description" : "Select to enable ID token encryption.",
            "propertyOrder" : 24600,
            "type" : "object",
            "exampleValue" : "",
            "properties" : {
              "inherited" : {
                "type" : "boolean",
                "required" : true
              },
              "value" : {
                "type" : "boolean",
                "required" : true
              }
            }
          },
          "tokenIntrospectionSignedResponseAlg" : {
            "title" : "Token introspection response signing algorithm",
            "description" : "Algorithm used for signing the introspection JWT response.",
            "propertyOrder" : 27810,
            "type" : "object",
            "exampleValue" : "",
            "properties" : {
              "inherited" : {
                "type" : "boolean",
                "required" : true
              },
              "value" : {
                "type" : "string",
                "required" : true
              }
            }
          },
          "idTokenPublicEncryptionKey" : {
            "title" : "ID Token Encryption Public Key",
            "description" : "A Base64 encoded public key for encrypting ID Tokens. This key is ignored if you specify a Secret Label Identifier and the corresponding secret mapping.",
            "propertyOrder" : 24900,
            "type" : "object",
            "exampleValue" : "",
            "properties" : {
              "inherited" : {
                "type" : "boolean",
                "required" : true
              },
              "value" : {
                "type" : "string",
                "required" : false
              }
            }
          },
          "clientJwtPublicKey" : {
            "title" : "Client JWT Bearer Public Key",
            "description" : "A Base64 encoded X509 certificate, containing the public key, represented as a UTF-8 PEM file, of the key pair for signing the Client Bearer JWT. This value is ignored if you specify a Secret Label Identifier and a corresponding secret mapping.",
            "propertyOrder" : 25400,
            "type" : "object",
            "exampleValue" : "",
            "properties" : {
              "inherited" : {
                "type" : "boolean",
                "required" : true
              },
              "value" : {
                "type" : "string",
                "required" : false
              }
            }
          },
          "authorizationResponseSigningAlgorithm" : {
            "title" : "Authorization Response JWT Signing Algorithm",
            "description" : "Algorithm the Authorization Response JWT for this client must be signed with.",
            "propertyOrder" : 24801,
            "type" : "object",
            "exampleValue" : "",
            "properties" : {
              "inherited" : {
                "type" : "boolean",
                "required" : true
              },
              "value" : {
                "type" : "string",
                "required" : true
              }
            }
          },
          "idTokenSignedResponseAlg" : {
            "title" : "ID Token Signing Algorithm",
            "description" : "Algorithm the ID Token for this client must be signed with.",
            "propertyOrder" : 24500,
            "type" : "object",
            "exampleValue" : "",
            "properties" : {
              "inherited" : {
                "type" : "boolean",
                "required" : true
              },
              "value" : {
                "type" : "string",
                "required" : true
              }
            }
          }
        }
      },
      "advancedOAuth2ClientConfig" : {
        "type" : "object",
        "title" : "Advanced",
        "propertyOrder" : 1,
        "properties" : {
          "name" : {
            "title" : "Display name",
            "description" : "A client name that may be relevant to the resource owner when considering approval.<br><br>The name may be entered as a single string or as pipe separated strings for locale and localized name; e.g. \"en|The ExampleCo Intranet\". Locale strings are in the format <code>language + \"_\" + country + \"_\" + variant</code>, e.g. en, en_GB, en_US_WIN. If the locale is omitted, the name is displayed to all users having undefined locales. e.g. \"The ExampleCo Intranet\".",
            "propertyOrder" : 23500,
            "items" : {
              "type" : "string"
            },
            "type" : "object",
            "exampleValue" : "",
            "properties" : {
              "inherited" : {
                "type" : "boolean",
                "required" : true
              },
              "value" : {
                "type" : "array",
                "required" : false
              }
            }
          },
          "logoUri" : {
            "title" : "Logo URI",
            "description" : "The URI for the client's logo, for use in user-facing UIs such as consent pages and application pages.",
            "propertyOrder" : 25350,
            "items" : {
              "type" : "string"
            },
            "type" : "object",
            "exampleValue" : "",
            "properties" : {
              "inherited" : {
                "type" : "boolean",
                "required" : true
              },
              "value" : {
                "type" : "array",
                "required" : false
              }
            }
          },
          "grantTypes" : {
            "title" : "Grant Types",
            "description" : "The set of Grant Types (OAuth2 Flows) that are permitted to be used by this client.<br><br>If no Grant Types (OAuth2 Flows) are configured then AUTHORIZATION_CODE flow would be permitted by default.",
            "propertyOrder" : 23800,
            "items" : {
              "type" : "string"
            },
            "type" : "object",
            "exampleValue" : "",
            "properties" : {
              "inherited" : {
                "type" : "boolean",
                "required" : true
              },
              "value" : {
                "type" : "array",
                "required" : true
              }
            }
          },
          "subjectType" : {
            "title" : "Subject Type",
            "description" : "The subject type added to responses for this client. This value must be included in \"Subject Type Supported\" in OAuth2 Provider service setting.",
            "propertyOrder" : 24400,
            "type" : "object",
            "exampleValue" : "",
            "properties" : {
              "inherited" : {
                "type" : "boolean",
                "required" : true
              },
              "value" : {
                "type" : "string",
                "required" : true
              }
            }
          },
          "responseTypes" : {
            "title" : "Response Types",
            "description" : "Response types this client will support and use.",
            "propertyOrder" : 23800,
            "items" : {
              "type" : "string"
            },
            "type" : "object",
            "exampleValue" : "",
            "properties" : {
              "inherited" : {
                "type" : "boolean",
                "required" : true
              },
              "value" : {
                "type" : "array",
                "required" : true
              }
            }
          },
          "softwareIdentity" : {
            "title" : "Software Identity",
            "description" : "A unique identifier assigned by the client developer or software publisher to identity the client software.",
            "propertyOrder" : 35400,
            "type" : "object",
            "exampleValue" : "",
            "properties" : {
              "inherited" : {
                "type" : "boolean",
                "required" : true
              },
              "value" : {
                "type" : "string",
                "required" : false
              }
            }
          },
          "policyUri" : {
            "title" : "Privacy Policy URI",
            "description" : "The URI for the client's privacy policy, for use in user-facing consent pages.",
            "propertyOrder" : 25375,
            "items" : {
              "type" : "string"
            },
            "type" : "object",
            "exampleValue" : "",
            "properties" : {
              "inherited" : {
                "type" : "boolean",
                "required" : true
              },
              "value" : {
                "type" : "array",
                "required" : false
              }
            }
          },
          "allowedResourceServerAudienceValues" : {
            "title" : "Allowed Resource Server Audience Values",
            "description" : "List of audience (aud) claim values that are allowed for resource servers. The value(s) must match those expected by the resource server for which the access tokens are requested.",
            "propertyOrder" : 35900,
            "items" : {
              "type" : "string"
            },
            "type" : "object",
            "exampleValue" : "",
            "properties" : {
              "inherited" : {
                "type" : "boolean",
                "required" : true
              },
              "value" : {
                "type" : "array",
                "required" : false
              }
            }
          },
          "customProperties" : {
            "title" : "Custom Properties",
            "description" : "Additional properties that allow users to augment the set of properties supported by the OAuth2 Client. <br> Examples: <br> customproperty=custom-value1 <br> customlist[0]=customlist-value-0 <br> customlist[1]=customlist-value-1 <br> custommap[key1]=custommap-value-1 <br> custommap[key2]=custommap-value-2",
            "propertyOrder" : 35100,
            "items" : {
              "type" : "string"
            },
            "type" : "object",
            "exampleValue" : "",
            "properties" : {
              "inherited" : {
                "type" : "boolean",
                "required" : true
              },
              "value" : {
                "type" : "array",
                "required" : false
              }
            }
          },
          "sectorIdentifierUri" : {
            "title" : "Sector Identifier URI",
            "description" : "The Host component of this URL is used in the computation of pairwise Subject Identifiers.",
            "propertyOrder" : 24300,
            "type" : "object",
            "exampleValue" : "",
            "properties" : {
              "inherited" : {
                "type" : "boolean",
                "required" : true
              },
              "value" : {
                "type" : "string",
                "required" : false
              }
            }
          },
          "acceptedJwtIssuers" : {
            "title" : "Accepted JWT Issuers",
            "description" : "List of JWT issuers that will be accepted in addition to client_id for private key JWT authentication.",
            "propertyOrder" : 24250,
            "items" : {
              "type" : "string"
            },
            "type" : "object",
            "exampleValue" : "",
            "properties" : {
              "inherited" : {
                "type" : "boolean",
                "required" : true
              },
              "value" : {
                "type" : "array",
                "required" : false
              }
            }
          },
          "isConsentImplied" : {
            "title" : "Implied consent",
            "description" : "When enabled, the resource owner will not be asked for consent during authorization flows. The OAuth2 Provider must be configured to allow clients to skip consent.",
            "propertyOrder" : 26200,
            "type" : "object",
            "exampleValue" : "",
            "properties" : {
              "inherited" : {
                "type" : "boolean",
                "required" : true
              },
              "value" : {
                "type" : "boolean",
                "required" : true
              }
            }
          },
          "require_pushed_authorization_requests" : {
            "title" : "Require Pushed Authorization Requests",
            "description" : "If enabled, the client must use the PAR endpoint to initiate authorization requests. Note that, even if this value is set to false, the authorization server may be configured to enforce PAR for all clients.",
            "propertyOrder" : 35600,
            "type" : "object",
            "exampleValue" : "",
            "properties" : {
              "inherited" : {
                "type" : "boolean",
                "required" : true
              },
              "value" : {
                "type" : "boolean",
                "required" : true
              }
            }
          },
          "mixUpMitigation" : {
            "title" : "OAuth 2.0 Mix-Up Mitigation enabled",
            "description" : "Enables OAuth 2.0 mix-up mitigation on the authorization server side.<br><br>Enable this setting only if this OAuth 2.0 client supports the <a href=\"https://tools.ietf.org/html/draft-ietf-oauth-mix-up-mitigation-01\">OAuth 2.0 Mix-Up Mitigation draft</a>, otherwise AM will fail to validate access token requests received from this client.",
            "propertyOrder" : 26300,
            "type" : "object",
            "exampleValue" : "",
            "properties" : {
              "inherited" : {
                "type" : "boolean",
                "required" : true
              },
              "value" : {
                "type" : "boolean",
                "required" : true
              }
            }
          },
          "updateAccessToken" : {
            "title" : "Access Token",
            "description" : "The access token used to update the client.",
            "propertyOrder" : 25100,
            "type" : "object",
            "exampleValue" : "",
            "properties" : {
              "inherited" : {
                "type" : "boolean",
                "required" : true
              },
              "value" : {
                "type" : "string",
                "required" : false
              }
            }
          },
          "tokenEndpointAuthMethod" : {
            "title" : "Token Endpoint Authentication Method",
            "description" : "The authentication method with which a client authenticates to the authorization server at the token endpoint. The authentication method applies to OIDC requests with the openid scope.",
            "propertyOrder" : 24000,
            "type" : "object",
            "exampleValue" : "",
            "properties" : {
              "inherited" : {
                "type" : "boolean",
                "required" : true
              },
              "value" : {
                "type" : "string",
                "required" : true
              }
            }
          },
          "javascriptOrigins" : {
            "title" : "JavaScript Origins",
            "description" : "",
            "propertyOrder" : 23650,
            "items" : {
              "type" : "string"
            },
            "type" : "object",
            "exampleValue" : "",
            "properties" : {
              "inherited" : {
                "type" : "boolean",
                "required" : true
              },
              "value" : {
                "type" : "array",
                "required" : false
              }
            }
          },
          "refreshTokenGracePeriod" : {
            "title" : "Refresh Token Grace Period (seconds)",
            "description" : "The period, in seconds, that a refresh token can be replayed. This allows a client to recover if the response from the original refresh request is not received due to a network problem or other transient issue. <br>Applies only to tokens in a one-to-one storage scheme. Keep this value as short as possible â it must not exceed 120 seconds. To deactivate the grace period set the value to â1. If this value is set to 0, the Refresh Token Grace Period of the OAuth2 Provider will be used instead.",
            "propertyOrder" : 26150,
            "type" : "object",
            "exampleValue" : "",
            "properties" : {
              "inherited" : {
                "type" : "boolean",
                "required" : true
              },
              "value" : {
                "type" : "integer",
                "required" : true
              }
            }
          },
          "treeName" : {
            "title" : "Tree Name",
            "description" : "The name of the tree that the client is associated with.<br><br>When a client is associated with a tree, the configured Authentication Context Mapper is not executed. Instead, AM redirects to the configured tree.",
            "propertyOrder" : 25670,
            "type" : "object",
            "exampleValue" : "",
            "properties" : {
              "inherited" : {
                "type" : "boolean",
                "required" : true
              },
              "value" : {
                "type" : "string",
                "required" : false
              }
            }
          },
          "tokenExchangeAuthLevel" : {
            "title" : "Token Exchange Auth Level",
            "description" : "Auth level granted to tokens generated as a result of a Token Exchange, where the input token had no original auth_level claim. (e.g. When exchanging ID Token for an Access Token)",
            "propertyOrder" : 10100,
            "type" : "object",
            "exampleValue" : "",
            "properties" : {
              "inherited" : {
                "type" : "boolean",
                "required" : true
              },
              "value" : {
                "type" : "integer",
                "required" : true
              }
            }
          },
          "clientUri" : {
            "title" : "Client URI",
            "description" : "The URI for finding further information about the client from user-facing UIs.",
            "propertyOrder" : 25325,
            "items" : {
              "type" : "string"
            },
            "type" : "object",
            "exampleValue" : "",
            "properties" : {
              "inherited" : {
                "type" : "boolean",
                "required" : true
              },
              "value" : {
                "type" : "array",
                "required" : false
              }
            }
          },
          "contacts" : {
            "title" : "Contacts",
            "description" : "Email addresses of users who can administrate this client.",
            "propertyOrder" : 23900,
            "items" : {
              "type" : "string"
            },
            "type" : "object",
            "exampleValue" : "",
            "properties" : {
              "inherited" : {
                "type" : "boolean",
                "required" : true
              },
              "value" : {
                "type" : "array",
                "required" : false
              }
            }
          },
          "softwareVersion" : {
            "title" : "Software Version",
            "description" : "A version identifier string for the identifier defined in the Software Identity.",
            "propertyOrder" : 35500,
            "type" : "object",
            "exampleValue" : "",
            "properties" : {
              "inherited" : {
                "type" : "boolean",
                "required" : true
              },
              "value" : {
                "type" : "string",
                "required" : false
              }
            }
          },
          "requestUris" : {
            "title" : "Request uris",
            "description" : "Array of request_uri values that are pre-registered by the RP for use at the OP.<br><br>The entire Request URI MUST NOT exceed 512 ASCII characters and MUST use either HTTP or HTTPS. Otherwise the value will be ignored.",
            "propertyOrder" : 23700,
            "items" : {
              "type" : "string"
            },
            "type" : "object",
            "exampleValue" : "",
            "properties" : {
              "inherited" : {
                "type" : "boolean",
                "required" : true
              },
              "value" : {
                "type" : "array",
                "required" : false
              }
            }
          },
          "descriptions" : {
            "title" : "Display description",
            "description" : "A description of the client or other information that may be relevant to the resource owner when considering approval.<br><br>The description may be entered as a single string or as pipe separated strings for locale and localized name; e.g. \"en|The company intranet is requesting the following access permission\". Locale strings are in the format <code>language + \"_\" + country + \"_\" + variant</code>, e.g. en, en_GB, en_US_WIN. If the locale is omitted, the description is displayed to all users having undefined locales. e.g. \"The company intranet is requesting the following access permission\".",
            "propertyOrder" : 23600,
            "items" : {
              "type" : "string"
            },
            "type" : "object",
            "exampleValue" : "",
            "properties" : {
              "inherited" : {
                "type" : "boolean",
                "required" : true
              },
              "value" : {
                "type" : "array",
                "required" : false
              }
            }
          },
          "tosURI" : {
            "title" : "Terms of Service URI",
            "description" : "The URI for the client's terms of service.",
            "propertyOrder" : 25390,
            "items" : {
              "type" : "string"
            },
            "type" : "object",
            "exampleValue" : "",
            "properties" : {
              "inherited" : {
                "type" : "boolean",
                "required" : true
              },
              "value" : {
                "type" : "array",
                "required" : false
              }
            }
          }
        }
      },
      "coreOAuth2ClientConfig" : {
        "type" : "object",
        "title" : "Core",
        "propertyOrder" : 0,
        "properties" : {
          "loopbackInterfaceRedirection" : {
            "title" : "Allow wildcard ports in redirect URIs",
            "description" : "This flag indicates whether wildcards can be used for port numbers in redirect URIs. When this toggle is set to true and a wildcard is used the only allowed combinations of protocols and hosts are: http://127.0.0.1, https://127.0.0.1, http://[::1], https://[::1], http://localhost, https://localhost The wild cards are permitted only for the port values. For example - <code>http://localhost:80*</code>, <code>http://localhost:80?0/{path}</code>, <code>http://localhost:80[8-9]0/{path}</code>",
            "propertyOrder" : 23150,
            "type" : "object",
            "exampleValue" : "",
            "properties" : {
              "inherited" : {
                "type" : "boolean",
                "required" : true
              },
              "value" : {
                "type" : "boolean",
                "required" : false
              }
            }
          },
          "accessTokenLifetime" : {
            "title" : "Access Token Lifetime (seconds)",
            "description" : "The time in seconds an access token is valid for. <i>NB</i> If this field is set to zero, Access Token Lifetime of the OAuth2 Provider is used instead of.",
            "propertyOrder" : 26000,
            "type" : "object",
            "exampleValue" : "",
            "properties" : {
              "inherited" : {
                "type" : "boolean",
                "required" : true
              },
              "value" : {
                "type" : "integer",
                "required" : true
              }
            }
          },
          "clientName" : {
            "title" : "Client Name",
            "description" : "This value is a readable name for this client.",
            "propertyOrder" : 25300,
            "items" : {
              "type" : "string"
            },
            "type" : "object",
            "exampleValue" : "",
            "properties" : {
              "inherited" : {
                "type" : "boolean",
                "required" : true
              },
              "value" : {
                "type" : "array",
                "required" : false
              }
            }
          },
          "scopes" : {
            "title" : "Scope(s)",
            "description" : "Scope(s). Scopes are strings that are presented to the user for approval and included in tokens so that the protected resource may make decisions about what to give access to.<br><br>Scopes may be entered as simple strings or pipe separated strings representing the internal scope name, locale, and localized description; e.g. \"read|en|Permission to view email messages in your account\". Locale strings are in the format <code>language + \"_\" + country + \"_\" + variant</code>, e.g. en, en_GB, en_US_WIN. If the locale and pipe is omitted, the description is displayed to all users having undefined locales. e.g. \"read|Permission to view email messages in your account\". <i>NB</i> If the description is also omitted, nothing is displayed to all users, e.g. specifying \"read|\" would allow the scope \"read\" to be used by the client, but would not display it to the user when it was requested.",
            "propertyOrder" : 23300,
            "items" : {
              "type" : "string"
            },
            "type" : "object",
            "exampleValue" : "",
            "properties" : {
              "inherited" : {
                "type" : "boolean",
                "required" : true
              },
              "value" : {
                "type" : "array",
                "required" : false
              }
            }
          },
          "userpassword" : {
            "title" : "Client secret",
            "description" : "Client secret. Used when the client authenticates to AM if you don't store client secret in a secret store.This secret is ignored if you specify a Secret Label Identifier and the corresponding secret mapping.",
            "propertyOrder" : 23000,
            "required" : true,
            "type" : "string",
            "format" : "password",
            "exampleValue" : ""
          },
          "clientType" : {
            "title" : "Client type",
            "description" : "Type of OAuth 2.0 client. Confidential clients can keep their password secret, and are typically web apps or other server-based clients. Public clients run the risk of exposing their password to a host or user agent, such as rich browser applications or desktop clients.",
            "propertyOrder" : 23100,
            "type" : "object",
            "exampleValue" : "",
            "properties" : {
              "inherited" : {
                "type" : "boolean",
                "required" : true
              },
              "value" : {
                "type" : "string",
                "required" : true
              }
            }
          },
          "defaultScopes" : {
            "title" : "Default Scope(s)",
            "description" : "Default Scope(s). Scopes automatically given to tokens.<br><br>Default Scopes may be entered as simple strings or pipe separated strings representing the internal scope name, locale, and localized description; e.g. \"read|en|Permission to view email messages in your account\". Locale strings are in the format <code>language + \"_\" + country + \"_\" + variant</code>, e.g. en, en_GB, en_US_WIN. If the locale and pipe is omitted, the description is displayed to all users having undefined locales. e.g. \"read|Permission to view email messages in your account\". <i>NB</i> If the description is also omitted, nothing is displayed to all users, e.g. specifying \"read|\" would allow the scope \"read\" to be used by the client, but would not display it to the user when it was requested.",
            "propertyOrder" : 23700,
            "items" : {
              "type" : "string"
            },
            "type" : "object",
            "exampleValue" : "",
            "properties" : {
              "inherited" : {
                "type" : "boolean",
                "required" : true
              },
              "value" : {
                "type" : "array",
                "required" : false
              }
            }
          },
          "redirectionUris" : {
            "title" : "Redirection URIs",
            "description" : "Redirection URIs (optional for confidential clients). Complete URIs or URIs consisting of protocol + authority + path are registered so that the OAuth 2.0 provider can trust that tokens are sent to trusted entities. If multiple URI's are registered, the client MUST specify the URI that the user should be redirected to following approval. May not contain a fragment (#).",
            "propertyOrder" : 23200,
            "items" : {
              "type" : "string"
            },
            "type" : "object",
            "exampleValue" : "",
            "properties" : {
              "inherited" : {
                "type" : "boolean",
                "required" : true
              },
              "value" : {
                "type" : "array",
                "required" : false
              }
            }
          },
          "authorizationCodeLifetime" : {
            "title" : "Authorization Code Lifetime (seconds)",
            "description" : "The time in seconds an authorization code is valid for. <i>NB</i> If this field is set to zero, Authorization Code Lifetime of the OAuth2 Provider is used instead of.",
            "propertyOrder" : 25800,
            "type" : "object",
            "exampleValue" : "",
            "properties" : {
              "inherited" : {
                "type" : "boolean",
                "required" : true
              },
              "value" : {
                "type" : "integer",
                "required" : true
              }
            }
          },
          "status" : {
            "title" : "Status",
            "description" : "Status of the agent configuration.",
            "propertyOrder" : 200,
            "type" : "object",
            "exampleValue" : "",
            "properties" : {
              "inherited" : {
                "type" : "boolean",
                "required" : true
              },
              "value" : {
                "type" : "string",
                "required" : true
              }
            }
          },
          "refreshTokenLifetime" : {
            "title" : "Refresh Token Lifetime (seconds)",
            "description" : "The time in seconds a refresh token is valid for. <i>NB</i> If this field is set to zero, Refresh Token Lifetime of the OAuth2 Provider is used instead. If this field is set to -1, the token will never expire.",
            "propertyOrder" : 25900,
            "type" : "object",
            "exampleValue" : "",
            "properties" : {
              "inherited" : {
                "type" : "boolean",
                "required" : true
              },
              "value" : {
                "type" : "integer",
                "required" : true
              }
            }
          },
          "agentgroup" : {
            "title" : "Group",
            "description" : "Add the client to a group to allow inheritance of property values from the group. <br>Changing the group will update inherited property values. <br>Inherited property values are copied to the client.",
            "propertyOrder" : 100,
            "required" : false,
            "type" : "string",
            "exampleValue" : ""
          },
          "secretLabelIdentifier" : {
            "title" : "Secret Label Identifier",
            "description" : "AM uses this identifier to create secret labels, using the following templates: <br> <ul> <li><code>am.applications.oauth2.client.{{identifier}}.secret</code> for the <b>Client secret</b></li> <li><code>am.applications.oauth2.client.{{identifier}}.jwt.public.key</code> for the <b>Client JWT Bearer Public Key</b></li> <li><code>am.applications.oauth2.client.{{identifier}}.mtls.trusted.cert</code> for the <b>mTLS Self-Signed Certificate</b></li> <li><code>am.applications.oauth2.client.{{identifier}}.id.token.enc.public.key</code> for the <b>ID Token Encryption Public Key</b></li> </ul> where {{identifier}} is the Secret Label Identifier. <br> The Secret Label Identifier can only contain characters {{a-z}} {{A-Z}} {{0-9}} {{.}} and cannot start or end with {{.}}. <br>As a best practice, use a different Secret Label Identifier per OAuth2 client.",
            "propertyOrder" : 23050,
            "type" : "object",
            "exampleValue" : "",
            "properties" : {
              "inherited" : {
                "type" : "boolean",
                "required" : true
              },
              "value" : {
                "type" : "string",
                "required" : false
              }
            }
          }
        }
      },
      "coreOpenIDClientConfig" : {
        "type" : "object",
        "title" : "OpenID Connect",
        "propertyOrder" : 2,
        "properties" : {
          "defaultMaxAge" : {
            "title" : "Default Max Age",
            "description" : "Minimum value 0. Sets the maximum length of time in seconds a session may be active after the authorization service has succeeded before the user must actively re-authenticate.",
            "propertyOrder" : 25500,
            "type" : "object",
            "exampleValue" : "",
            "properties" : {
              "inherited" : {
                "type" : "boolean",
                "required" : true
              },
              "value" : {
                "type" : "integer",
                "required" : true
              }
            }
          },
          "defaultMaxAgeEnabled" : {
            "title" : "Default Max Age Enabled",
            "description" : "Whether or not the default max age is enforced.",
            "propertyOrder" : 25600,
            "type" : "object",
            "exampleValue" : "",
            "properties" : {
              "inherited" : {
                "type" : "boolean",
                "required" : true
              },
              "value" : {
                "type" : "boolean",
                "required" : true
              }
            }
          },
          "postLogoutRedirectUri" : {
            "title" : "Post Logout Redirect URIs",
            "description" : "URIs that can be redirected to after the client logout process.",
            "propertyOrder" : 25000,
            "items" : {
              "type" : "string"
            },
            "type" : "object",
            "exampleValue" : "",
            "properties" : {
              "inherited" : {
                "type" : "boolean",
                "required" : true
              },
              "value" : {
                "type" : "array",
                "required" : false
              }
            }
          },
          "jwtTokenLifetime" : {
            "title" : "OpenID Connect JWT Token Lifetime (seconds)",
            "description" : "The time in seconds a JWT is valid for. <i>NB</i> If this field is set to zero, JWT Token Lifetime of the OAuth2 Provider is used instead of.",
            "propertyOrder" : 26100,
            "type" : "object",
            "exampleValue" : "",
            "properties" : {
              "inherited" : {
                "type" : "boolean",
                "required" : true
              },
              "value" : {
                "type" : "integer",
                "required" : true
              }
            }
          },
          "backchannel_logout_session_required" : {
            "title" : "Backchannel Logout Session Required",
            "description" : "Boolean value specifying whether the RP requires that a sid (session ID) Claim be included in the Logout Token to identify the RP session with the OP when the Backchannel Logout URL is used.",
            "propertyOrder" : 35300,
            "type" : "object",
            "exampleValue" : "",
            "properties" : {
              "inherited" : {
                "type" : "boolean",
                "required" : true
              },
              "value" : {
                "type" : "boolean",
                "required" : true
              }
            }
          },
          "clientSessionUri" : {
            "title" : "Client Session URI",
            "description" : "This is the URI that will be used to check messages sent to the session management endpoints. This URI must match the origin of the message",
            "propertyOrder" : 25200,
            "type" : "object",
            "exampleValue" : "",
            "properties" : {
              "inherited" : {
                "type" : "boolean",
                "required" : true
              },
              "value" : {
                "type" : "string",
                "required" : false
              }
            }
          },
          "defaultAcrValues" : {
            "title" : "Default ACR values",
            "description" : "Default requested Authentication Context Class Reference values.<br><br>Array of strings that specifies the default acr values that the OP is being requested to use for processing requests from this Client, with the values appearing in order of preference. The Authentication Context Class satisfied by the authentication performed is returned as the acr Claim Value in the issued ID Token. The acr Claim is requested as a Voluntary Claim by this parameter. The acr_values_supported discovery element contains a list of the acr values supported by this server. Values specified in the acr_values request parameter or an individual acr Claim request override these default values.",
            "propertyOrder" : 25650,
            "items" : {
              "type" : "string"
            },
            "type" : "object",
            "exampleValue" : "",
            "properties" : {
              "inherited" : {
                "type" : "boolean",
                "required" : true
              },
              "value" : {
                "type" : "array",
                "required" : false
              }
            }
          },
          "claims" : {
            "title" : "Claim(s)",
            "description" : "List of claim name translations, which will override those specified for the AS. Claims are values that are presented to the user to inform them what data is being made available to the Client.<br><br>Claims may be entered as simple strings or pipe separated strings representing the internal claim name, locale, and localized description; e.g. \"name|en|Your full name\". Locale strings are in the format <code>language + \"_\" + country + \"_\" + variant</code>, e.g. en, en_GB, en_US_WIN. If the locale and pipe is omitted, the description is displayed to all users having undefined locales. e.g. \"name|Your full name\". <i>NB</i> If the description is also omitted, nothing is displayed to all users, e.g. specifying \"name|\" would allow the claim \"name\" to be used by the client, but would not display it to the user when it was requested.<p>If a value is not given here, the value will be computed from the OAuth 2 Provider settings.</p>",
            "propertyOrder" : 23400,
            "items" : {
              "type" : "string"
            },
            "type" : "object",
            "exampleValue" : "",
            "properties" : {
              "inherited" : {
                "type" : "boolean",
                "required" : true
              },
              "value" : {
                "type" : "array",
                "required" : false
              }
            }
          },
          "backchannel_logout_uri" : {
            "title" : "Backchannel Logout URL",
            "description" : "RP URL that will cause the RP to log itself out when sent a Logout Token by the OP. This URL SHOULD use the https scheme and MAY contain port, path, and query parameter components; however, it MAY use the http scheme, provided that the Client Type is confidential, as defined in Section 2.1 of OAuth 2.0 [RFC6749], and provided the OP allows the use of http RP URIs.",
            "propertyOrder" : 35200,
            "type" : "object",
            "exampleValue" : "",
            "properties" : {
              "inherited" : {
                "type" : "boolean",
                "required" : true
              },
              "value" : {
                "type" : "string",
                "required" : false
              }
            }
          }
        }
      },
      "coreUmaClientConfig" : {
        "type" : "object",
        "title" : "UMA",
        "propertyOrder" : 4,
        "properties" : {
          "claimsRedirectionUris" : {
            "title" : "Claims Redirection URIs",
            "description" : "Redirection URIs for returning to the client from UMA claims collection. If multiple URIs are registered, the client MUST specify the URI that the user should be redirected to following approval. May not contain a fragment (#).",
            "propertyOrder" : 23200,
            "items" : {
              "type" : "string"
            },
            "type" : "object",
            "exampleValue" : "",
            "properties" : {
              "inherited" : {
                "type" : "boolean",
                "required" : true
              },
              "value" : {
                "type" : "array",
                "required" : false
              }
            }
          }
        }
      }
    }
  }
  ```

---

---
title: AmsterJwtDecisionNodeCollection
description: Base resource for the AmsterJwtDecisionNode
component: pingam
version: 8.1
page_id: pingam:entity-reference:sec-amster-entity-amsterjwtdecisionnodecollection
canonical_url: https://docs.pingidentity.com/pingam/8.1/entity-reference/sec-amster-entity-amsterjwtdecisionnodecollection.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  sec-amster-entity-amsterjwtdecisionnodecollection-realm-ops: Realm Operations
  sec-amster-entity-amsterjwtdecisionnodecollection-realm-ops-getalltypes: getAllTypes
  sec-amster-entity-amsterjwtdecisionnodecollection-realm-ops-getcreatabletypes: getCreatableTypes
  sec-amster-entity-amsterjwtdecisionnodecollection-realm-ops-getlatesttype: getLatestType
  sec-amster-entity-amsterjwtdecisionnodecollection-realm-ops-gettype: getType
  sec-amster-entity-amsterjwtdecisionnodecollection-realm-ops-nextdescendents: nextdescendents
  sec-amster-entity-amsterjwtdecisionnodecollection-realm-ops-versioninfo: versionInfo
---

# AmsterJwtDecisionNodeCollection

## Realm Operations

Base resource for the AmsterJwtDecisionNode

Resource path:

```
/realm-config/authentication/authenticationtrees/nodes/AmsterJwtDecisionNode
```

Resource version: `3.0`

### getAllTypes

Obtain the collection of all secondary configuration types related to the resource.

**Usage**

```
am> action AmsterJwtDecisionNodeCollection --realm Realm --actionName getAllTypes
```

### getCreatableTypes

Obtain the collection of secondary configuration types that have yet to be added to the resource.

**Usage**

```
am> action AmsterJwtDecisionNodeCollection --realm Realm --actionName getCreatableTypes
```

### getLatestType

getLatestType.description

**Usage**

```
am> action AmsterJwtDecisionNodeCollection --realm Realm --actionName getLatestType
```

### getType

List information related to the node such as a name, description, tags and metadata.

**Usage**

```
am> action AmsterJwtDecisionNodeCollection --realm Realm --actionName getType
```

### nextdescendents

Obtain the collection of secondary configuration instances that have been added to the resource.

**Usage**

```
am> action AmsterJwtDecisionNodeCollection --realm Realm --actionName nextdescendents
```

### versionInfo

List the versions available for the node type.

**Usage**

```
am> action AmsterJwtDecisionNodeCollection --realm Realm --actionName versionInfo
```

---

---
title: AuthenticationTreesConfiguration
description: Sub-path parent for all authentication tree configuration.
component: pingam
version: 8.1
page_id: pingam:entity-reference:sec-amster-entity-authenticationtreesconfiguration
canonical_url: https://docs.pingidentity.com/pingam/8.1/entity-reference/sec-amster-entity-authenticationtreesconfiguration.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  sec-amster-entity-authenticationtreesconfiguration-realm-ops: Realm Operations
  sec-amster-entity-authenticationtreesconfiguration-realm-ops-getalltypes: getAllTypes
  sec-amster-entity-authenticationtreesconfiguration-realm-ops-getcreatabletypes: getCreatableTypes
  sec-amster-entity-authenticationtreesconfiguration-realm-ops-nextdescendents: nextdescendents
  sec-amster-entity-authenticationtreesconfiguration-global-ops: Global Operations
  sec-amster-entity-authenticationtreesconfiguration-global-ops-getalltypes: getAllTypes
  sec-amster-entity-authenticationtreesconfiguration-global-ops-getcreatabletypes: getCreatableTypes
  sec-amster-entity-authenticationtreesconfiguration-global-ops-nextdescendents: nextdescendents
  sec-amster-entity-authenticationtreesconfiguration-global-ops-read: read
  sec-amster-entity-authenticationtreesconfiguration-global-ops-update: update
---

# AuthenticationTreesConfiguration

## Realm Operations

Sub-path parent for all authentication tree configuration.

Resource path:

```
/realm-config/authentication/authenticationtrees
```

Resource version: `0.0`

### getAllTypes

Obtain the collection of all secondary configuration types related to the resource.

**Usage**

```
am> action AuthenticationTreesConfiguration --realm Realm --actionName getAllTypes
```

### getCreatableTypes

Obtain the collection of secondary configuration types that have yet to be added to the resource.

**Usage**

```
am> action AuthenticationTreesConfiguration --realm Realm --actionName getCreatableTypes
```

### nextdescendents

Obtain the collection of secondary configuration instances that have been added to the resource.

**Usage**

```
am> action AuthenticationTreesConfiguration --realm Realm --actionName nextdescendents
```

## Global Operations

Resource path:

```
/global-config/authentication/authenticationtrees
```

Resource version: `1.0`

### getAllTypes

Obtain the collection of all secondary configuration types related to the resource.

**Usage**

```
am> action AuthenticationTreesConfiguration --global --actionName getAllTypes
```

### getCreatableTypes

Obtain the collection of secondary configuration types that have yet to be added to the resource.

**Usage**

```
am> action AuthenticationTreesConfiguration --global --actionName getCreatableTypes
```

### nextdescendents

Obtain the collection of secondary configuration instances that have been added to the resource.

**Usage**

```
am> action AuthenticationTreesConfiguration --global --actionName nextdescendents
```

### read

**Usage**

```
am> read AuthenticationTreesConfiguration --global
```

### update

**Usage**

```
am> update AuthenticationTreesConfiguration --global --body body
```

**Parameters**

* *\--body*

  The resource in JSON format, described by the following JSON schema:

  ```json
  {
    "type" : "object"
  }
  ```