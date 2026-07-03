---
title: Automatically update and remove PingID users
description: The PingID Connector synchronizes user identities and their profile attributes from a configured datastore within PingFederate to PingID.
component: pingid
page_id: pingid:pingid_user_life_cycle_management:pid_automatically_update_remove_pid_users
canonical_url: http://docs.pingidentity.com/pingid/pingid_user_life_cycle_management/pid_automatically_update_remove_pid_users.html
llms_txt: http://docs.pingidentity.com/pingid/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: April 15, 2026
section_ids:
  processing-steps: Processing steps
---

# Automatically update and remove PingID users

The PingID Connector synchronizes user identities and their profile attributes from a configured datastore within PingFederate to PingID.

Ping Identity offers a catalog of connectors that provide provisioning capabilities to software as a service (SaaS) providers. The connectors act as mediators to handle transactions safely and securely. The PingID Connector offers profile management solutions to multiple directory types, such as LDAP, Active Directory (AD), and PingDirectory.

![Diagram showing how the PingID Connector interacts with PingFederate, PingOne, and Active Directory.](_images/ccr1564020537891.png)

## Processing steps

1. PingFederate polls the user directory for any changes to user records at regular intervals, configurable in PingFederate.

2. Records requiring action found during step one are stored within PingFederate's intermediary database and marked as a requiring an update in PingID (PingOne).

3. The connector pulls the marked record from the intermediary database and performs the necessary Read (Get), Update, or Delete operation against the PingID record. These changes are reflected in the PingOne admin portal.

   The PingID Connector:

   * Provides support for PingID API 4.9

   * Includes support for user lifecycle management including updates, disabling users, and deleting users

   * Includes configuration options for workflow capabilities, such as the ability to disable updates.

Download the PingID for PingFederate connector in [PingFederate Server SaaS Connectors](https://www.pingidentity.com/en/resources/downloads/pingfederate.html).

Learn more about how to configure the PingID for PingFederate connector in [PingID Provisioner](http://docs.pingidentity.com/integrations/pingid/pf_pid_connector.html) in the PingFederate documentation.
