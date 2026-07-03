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
