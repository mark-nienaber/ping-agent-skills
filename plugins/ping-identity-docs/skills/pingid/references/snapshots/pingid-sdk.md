---
title: Automatic synchronization of PingID SDK with a PingFederate user directory
description: The PingID SDK Connector synchronizes user identities and their profile attributes from a configured datastore within PingFederate to PingID SDK.
component: pingid
page_id: pingid:pingid_sdk:pid_automatic_syn_of_pid_sdk_with_pf
canonical_url: http://docs.pingidentity.com/pingid/pingid_sdk/pid_automatic_syn_of_pid_sdk_with_pf.html
llms_txt: http://docs.pingidentity.com/pingid/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: January 23, 2024
section_ids:
  the-pingid-sdk-connector-flow: The PingID SDK Connector flow:
---

# Automatic synchronization of PingID SDK with a PingFederate user directory

The PingID SDK Connector synchronizes user identities and their profile attributes from a configured datastore within PingFederate to PingID SDK.

Ping Identity offers a catalog of connectors that provide provisioning capabilities to SaaS providers. The connectors act as a mediator to handle transactions safely and securely. The PingID SDK Connector offers profile management solutions to multiple directory types, such as LDAP, Active Directory (AD), and PingDirectory.

The PingID SDK Connector:

* Includes support for user life cycle management that lets you create, update, disable, and delete users

* Includes configuration options for workflow capabilities, such as the ability to disable updates

![Diagram illustrating the flow between Active Directory, PingFederate and the PingID SDK Connector, and PingOne.](_images/qzj1564021075991.png)

## The PingID SDK Connector flow:

1. PingFederate polls the user directory for any changes to user records at regular intervals, configurable in PingFederate.

2. Returned records are stored within PingFederate's intermediary database and marked as requiring an update in PingID SDK (PingOne).

3. The connector pulls the marked record from the intermediary database and performs the necessary operation (Create, Get, Update, Delete) against the PingID SDK record. These changes are reflected in the PingOne admin portal.

To download the PingID SDK for PingFederate connector, go to [PingID Server SaaS Connectors](https://www.pingidentity.com/en/resources/downloads/pingfederate.html).

For more information on configuring the PingID SDK for PingFederate connector, see [PingFederate PingID SDK Connector Guide](https://support.pingidentity.com/s/document-item?bundleId=integrations\&topicId=zyw1565632179137.html).
