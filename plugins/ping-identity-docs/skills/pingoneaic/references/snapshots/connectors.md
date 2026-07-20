---
title: Connectors
description: Overview of connectors in Advanced Identity Cloud, including built-in connectors and remote connectors that run on an external remote connector server
component: pingoneaic
page_id: pingoneaic:connectors:connectors
canonical_url: https://docs.pingidentity.com/pingoneaic/connectors/connectors.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
page_aliases: ["connector-reference:connectors.adoc"]
section_ids:
  built_in_connectors: Built-in connectors
  remote_connectors: Remote connectors
---

# Connectors

Connectors are a tool to connect PingOne Advanced Identity Cloud to external resources and services and are built using the PingOne Open Connector Framework (ICF). Some connectors are built into Advanced Identity Cloud to let you easily connect to datastores in other services and are configurable using the IDM native admin console. Additional connectors are available to set up and run remotely using a remote connector server (RCS).

|   |                                                                                                                                                                                                                                                                                                                                                                                                                    |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | If you configure a connector with a password, you must update the connector's Advanced Identity Cloud configuration to replace the password's encrypted object with an ESV placeholder. This makes the connector's configuration compatible with the promotion process. Learn more in [Insert an ESV placeholder into an LDAP connector](../tenants/configuration-placeholders-api.html#configure-ldap-connector). |

## Built-in connectors

Advanced Identity Cloud includes several built-in connectors to connect easily to data stores in other services. These built-in connectors are accessed through the IDM native admin console. For a complete list of connectors bundled with Advanced Identity Cloud, refer to your tenant.

|   |                                                                                                                                                                                                                                                 |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Learn more about provisioning connectors using the application management section of Advanced Identity Cloud in [Provision settings for an application](../app-management/provision-an-application.html#provision_settings_for_an_application). |

## Remote connectors

Ping Identity provides many additional connectors that can be run remotely for continuous, two-way synchronization with external datastores that reside on-premises, in a private cloud, or in a public cloud.

Remote connectors run on a remote connector server (RCS) hosted outside of Advanced Identity Cloud. They communicate inbound with your Advanced Identity Cloud tenant.

Step-by-step instructions for configuring Advanced Identity Cloud and an RCS using the Advanced Identity Cloud admin console are included in [Sync identities](../identities/sync-identities.html).

Learn more about installing and configuring an RCS in [Remote connectors](https://docs.pingidentity.com/openicf/connector-reference/remote-connector.html) in the [ICF documentation](https://docs.pingidentity.com/openicf/index.html).

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | When used with Advanced Identity Cloud, the RCS must be configured to initiate the connection to Advanced Identity Cloud, also known as **client mode**. This configuration is included in [the step-by-step instructions](../identities/sync-identities.html#task-5-configure-a-remote-server) if you're configuring your RCS using the Advanced Identity Cloud admin console.If you are configuring Advanced Identity Cloud and your RCS through REST, learn more in [Configure RCS in client mode](https://docs.pingidentity.com/openicf/connector-reference/configure-server.html#configure-rcs-client-mode) in the [ICF documentation](https://docs.pingidentity.com/openicf/index.html). |