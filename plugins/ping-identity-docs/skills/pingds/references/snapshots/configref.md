---
title: About this reference
description: This reference describes server configuration settings that you can view and edit with the dsconfig command. The dsconfig command is the primary tool for managing the server configuration, which follows an object-oriented configuration model. Each configuration object has its own properties. Configuration objects can be related to each other by inheritance and by reference.
component: pingds
version: 8.1
page_id: pingds:configref:preface
canonical_url: https://docs.pingidentity.com/pingds/8.1/configref/preface.html
llms_txt: https://docs.pingidentity.com/pingds/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
page_aliases: ["index.adoc"]
---

# About this reference

This reference describes server configuration settings that you can view and edit with the `dsconfig` command. The `dsconfig` command is the primary tool for managing the server configuration, which follows an object-oriented configuration model. Each configuration object has its own properties. Configuration objects can be related to each other by inheritance and by reference.

The server configuration model exposes a wide range of configurable features. As a consequence, the `dsconfig` command has many subcommands.

Subcommands exist to create, list, and delete configuration objects, and to get and set properties of configuration objects. Their names reflect these five actions:

* `create-`*object*

* `list-`*objects*

* `delete-`*object*

* `get-`*object*`-prop`

* `set-`*object*`-prop`

Each configuration *object* has a user-friendly name, such as `Connection Handler`. Subcommand names use lower-case, hyphenated versions of the friendly names, as in `create-connection-handler`.
