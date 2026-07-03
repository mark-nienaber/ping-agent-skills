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
