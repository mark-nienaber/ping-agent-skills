---
title: About Web Agent and PingOne Advanced Identity Cloud
description: Overview of how PingAM Web Agent works with PingOne Advanced Identity Cloud to enforce resource-based policies across clouds and on-premise.
component: web-agents
version: 2026
page_id: web-agents:identity-cloud-guide:about
canonical_url: https://docs.pingidentity.com/web-agents/2026/identity-cloud-guide/about.html
---

# About Web Agent and PingOne Advanced Identity Cloud

Advanced Identity Cloud simplifies the consumption of an identity platform. However, many organizations have business web applications and APIs deployed across multiple clouds, or on-premise. This guide provides an example of how to use Web Agent with Advanced Identity Cloud, without changing the architecture of the agent-based model.

The following image illustrates the flow of an inbound request to a website, through a Web Agent, and the agent's interaction with Advanced Identity Cloud to enforce resource-based policies.

![Web Agent enforces policies from Advanced Identity Cloud.](_images/web-agent-cloud.svg)

For information about Advanced Identity Cloud, refer to the [PingOne Advanced Identity Cloud documentation](https://docs.pingidentity.com/pingoneaic/home.html).

---

---
title: Enforce policy decisions from Advanced Identity Cloud
description: Set up PingOne Advanced Identity Cloud as the policy decision point for requests processed by PingAM Web Agent.
component: web-agents
version: 2026
page_id: web-agents:identity-cloud-guide:pep
canonical_url: https://docs.pingidentity.com/web-agents/2026/identity-cloud-guide/pep.html
---

# Enforce policy decisions from Advanced Identity Cloud

This example sets up Advanced Identity Cloud as a policy decision point for requests processed by Web Agent. For more information about Web Agent, refer to the [User guide](../user-guide/preface.html).

1. Using the [Advanced Identity Cloud documentation](https://docs.pingidentity.com/pingoneaic/home.html), log in to Advanced Identity Cloud as an administrator.

2. Make sure you are managing the `alpha` realm. If not, [switch realms](https://docs.pingidentity.com/pingoneaic/realms/realm-settings.html#switch_realms).

3. [Create a policy set and policy](installation.html#create-policy).

4. [Create an agent profile](installation.html#create-agent-profile).

   When a policy set is assigned to the agent profile during creation, the agent uses that policy set. If a suitable policy set isn't available during creation, select Edit advanced settings to edit or create one and assign it to the agent profile.

5. Test the setup:

   1. Go to `https://agent.example.com:443`. The Advanced Identity Cloud login page is displayed.

   2. Log in to Advanced Identity Cloud as user `bjensen`, password `Ch4ng3!t`, to access the web page protected by the Web Agent.

---

---
title: PingOne Advanced Identity Cloud guide
description: Guide for using PingAM Web Agent with PingOne Advanced Identity Cloud with installation and configuration guidance.
component: web-agents
version: 2026
page_id: web-agents:identity-cloud-guide:preface
canonical_url: https://docs.pingidentity.com/web-agents/2026/identity-cloud-guide/preface.html
page_aliases: ["index.adoc"]
section_ids:
  preface-examples: Example installation for this guide
---

# PingOne Advanced Identity Cloud guide

This guide is for customers using an agent-based integration model, with AM on-premise, or another on-premise access management solution. The guide provides an example of how to transition from on-premise access management to Advanced Identity Cloud without changing the architecture of the agent-based model.

Advanced Identity Cloud is described in the [PingOne Advanced Identity Cloud documentation](https://docs.pingidentity.com/pingoneaic/home.html).

## Example installation for this guide

Unless otherwise stated, the examples in this guide assume the following installation:

* Web Agent installed on `https://agent.example.com:443`, in the `alpha` realm.

* An Advanced Identity Cloud tenant with the default configuration, as described in the [PingOne Advanced Identity Cloud documentation](https://docs.pingidentity.com/pingoneaic/home.html).

When using Advanced Identity Cloud, you need to know the value of the following properties:

* The URL of your Advanced Identity Cloud tenant. For example, `https://tenant.forgeblocks.com`.

  The URL of the AM component of Advanced Identity Cloud is the root URL of your Advanced Identity Cloud tenant followed by `/am`. For example, `https://tenant.forgeblocks.com/am`.

* The realm where you work. The examples in this guide use `alpha`.

  Prefix each realm in the hierarchy with the `realms` keyword. For example, `/realms/root/realms/alpha`.

If you use a different configuration, substitute in the procedures accordingly.

---

---
title: Prepare for installation
description: "Prepare PingOne Advanced Identity Cloud for PingAM Web Agent: add a test user, create a policy set, and configure an agent profile."
component: web-agents
version: 2026
page_id: web-agents:identity-cloud-guide:installation
canonical_url: https://docs.pingidentity.com/web-agents/2026/identity-cloud-guide/installation.html
section_ids:
  demo-user: Add a test user in Advanced Identity Cloud
  create-policy: Create a policy set and policy in Advanced Identity Cloud
  create-agent-profile: Create an agent profile in Advanced Identity Cloud
  secret-label-identifier-changes: Secret Label Identifier changes
---

# Prepare for installation

For information about installing Web Agent, refer to the [Installation](../installation-guide/preface.html). This section summarizes considerations for using the agent with Advanced Identity Cloud:

* Configure Advanced Identity Cloud and set up a policy before you install the agent. When you configure the agent in the Advanced Identity Cloud admin UI, you can select the policy.

* For environments with load balancers or reverse proxies, consider the communication between the agent and the Advanced Identity Cloud tenants, and between the agent and the client. Do one of the following:

  * Configure the environment before you install the agent.

  * Install the agent using [agentadmin --s --forceInstall](../installation-guide/agentadmin.html#agentadmin-s) to prevent the agent from trying to connect to Advanced Identity Cloud before installation.

## Add a test user in Advanced Identity Cloud

Add a user so you can test the examples in this guide.

1. In the Advanced Identity Cloud admin UI, select [icon: people, set=material, size=inline] Identities > Manage > Alpha realm - Users.

2. Add a new user with the following values:

   * Username : `bjensen`

   * First name : `Babs`

   * Last name : `Jensen`

   * Email Address : `bjensen@example.com`

   * Password : `Ch4ng3!t`

## Create a policy set and policy in Advanced Identity Cloud

1. In the Advanced Identity Cloud admin UI, select [icon: open_in_new, set=material, size=inline] Native Consoles > Access Management. The AM admin UI is displayed.

2. In the AM admin UI, select Authorization > Policy Sets > New Policy Set, and add a policy set with the following values:

   * Id : `PEP`

   * Resource Types : `URL`

3. In the policy set, add a policy with the following values:

   * Name : `PEP-policy`

   * Resource Type : `URL`

   * Resource pattern : `*://*:*/*`

   * Resource value : `*://*:*/*`

4. On the Actions tab, add actions to allow HTTP `GET` and `POST`.

5. On the Subjects tab, remove any default subject conditions, add a subject condition for all `Authenticated Users`.

## Create an agent profile in Advanced Identity Cloud

1. In the Advanced Identity Cloud admin UI, go to [icon: verified_user, set=material, size=inline] Gateways & Agents > New Gateway/Agent, and add a Web Agent with the following values:

   * Agent ID : `web-agent`

   * Password : `password`

   * Application URL : `https://agent.example.com:443`

   * Use Secret Store for password: (Optional) Enable to use a secret store for the agent profile password.

     Once enabled, the Secret Label Identifier field displays.

   * Secret Label Identifier: Enter a value that represents the `identifier` part of the secret label for the agent. This value should clearly identify the agent (for example, `web-agent`). Advanced Identity Cloud uses the identifier to generate a secret label in the following format: `am.application.agents.identifier.secret`.

     Learn more in [Secret labels](https://docs.pingidentity.com/pingoneaic/tenants/esvs-signing-encryption.html#secret-labels) and [Map ESV secrets to secret labels](https://docs.pingidentity.com/pingoneaic/tenants/esvs-signing-encryption.html#map-esv-secrets-to-secret-labels).

2. Click Save Profile and Done.

3. On the agent profile page, enable Use Policy Authorization, select a policy set to assign to the profile, and then click Save.

   If a suitable policy set isn't available, select Edit advanced settings to edit or create one.

### Secret Label Identifier changes

Advanced Identity Cloud maintains secret mappings when the Secret Label Identifier is changed as follows:

* If you update the Secret Label Identifier:

  * If no other agent shares that secret mapping, Advanced Identity Cloud updates any corresponding secret mapping for the previous identifier.

  * If another agent shares that secret mapping, Advanced Identity Cloud creates a new secret mapping for the updated identifier and copies its aliases from the previously shared secret mapping.

* If you delete the Secret Label Identifier, Advanced Identity Cloud deletes any corresponding secret mapping for the previous identifier, provided no other agent shares that secret mapping.