---
title: IDM glossary
description: Glossary of PingIDM terms, including managed objects, reconciliation, synchronization, roles, mappings, REST, and JWT
component: pingidm
version: 8.1
page_id: pingidm::glossary
canonical_url: https://docs.pingidentity.com/pingidm/8.1/glossary.html
llms_txt: https://docs.pingidentity.com/pingidm/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["JSON", "Configuration", "Reconciliation", "Rest", "Synchronization"]
---

# IDM glossary

* correlation query

  A correlation query specifies an expression that matches existing entries in a source repository to one or more entries in a target repository. A correlation query might be built with a script, but it is not the same as a correlation script. For more information, refer to [Correlate source objects with existing target objects](synchronization-guide/chap-correlation.html).

* correlation script

  A correlation script matches existing entries in a source repository, and returns the IDs of one or more matching entries on a target repository. While it skips the intermediate step associated with a `correlation query`, a correlation script can be relatively complex, based on the operations of the script.

* entitlement

  An entitlement is a collection of attributes that can be added to a user entry via roles. As such, it is a specialized type of `assignment`. A user or device with an entitlement gets access rights to specified resources. An entitlement is a property of a managed object.

* JCE

  Java Cryptographic Extension, which is part of the Java Cryptography Architecture, provides a framework for encryption, key generation, and digital signatures.

* JSON

  JavaScript Object Notation, a lightweight data interchange format based on a subset of JavaScript syntax. For more information, refer to the [JSON](https://www.json.org) site.

* JSON Pointer

  A JSON Pointer defines a string syntax for identifying a specific value within a JSON document. For information about JSON Pointer syntax, refer to the [JSON Pointer RFC](https://www.rfc-editor.org/rfc/rfc6901.html).

- JWT

  JSON Web Token. As noted in [RFC 8725](https://www.rfc-editor.org/rfc/rfc8725.html), "JSON Web Tokens, also known as JWTs, are URL-safe JSON-based security tokens that contain a set of claims that can be signed and/or encrypted." For IDM, the JWT is associated with the `JWT_SESSION` authentication module.

- managed object

  An object that represents the identity-related data managed by IDM. Managed objects are configurable, JSON-based data structures that IDM stores in its pluggable repository. The default configuration of a managed object is that of a user, but you can define any kind of managed object, for example, groups or roles.

- mapping

  A policy that is defined between a source object and a target object during reconciliation or synchronization. A mapping can also define a trigger for validation, customization, filtering, and transformation of source and target objects.

- OSGi

  A module system and service platform for the Java programming language that implements a complete and dynamic component model. For more information, refer to [What is OSGi?](https://www.osgi.org/resources/what-is-osgi/) Currently, only the [Apache Felix](http://felix.apache.org/) container is supported.

- reconciliation

  During reconciliation, comparisons are made between managed objects and objects on source or target systems. Reconciliation can result in one or more specified actions, including, but not limited to, synchronization.

- resource

  An external system, database, directory server, or other source of identity data to be managed and audited by the identity management system.

* REST

  Representational State Transfer. A software architecture style for exposing resources, using the technologies and protocols of the World Wide Web. REST describes how distributed data objects, or resources, can be defined and addressed.

* role

  IDM distinguishes between two distinct role types - provisioning roles and authorization roles. For more information, refer to [Managed Roles](objects-guide/roles.html#managed-roles).

* source object

  In the context of reconciliation, a source object is a data object on the source system, that IDM scans before attempting to find a corresponding object on the target system. Depending on the defined mapping, IDM then adjusts the object on the target system (target object).

* synchronization

  The synchronization process creates, updates, or deletes objects on a target system, based on the defined mappings from the source system. Synchronization can be scheduled or on demand.

* system object

  A pluggable representation of an object on an external system. For example, a user entry that is stored in an external LDAP directory is represented as a system object in IDM for the period during which IDM requires access to that entry. System objects follow the same RESTful resource-based design principles as managed objects.

* target object

  In the context of reconciliation, a target object is a data object on the target system, that IDM scans after locating its corresponding object on the source system. Depending on the defined mapping, IDM then adjusts the target object to match the corresponding source object.