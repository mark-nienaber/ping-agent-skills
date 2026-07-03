---
title: Account Recovery
description: This page explains what we mean by account recovery and the context required to integrate it.
component: recognize
page_id: recognize:mobile-sdk:mobile-sdk-account-recovery
canonical_url: https://docs.pingidentity.com/recognize/mobile-sdk/mobile-sdk-account-recovery.html
llms_txt: https://docs.pingidentity.com/recognize/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: April 20, 2026
section_ids:
  what-is-account-recovery: What Is Account Recovery?
  client-state: Client State
---

# Account Recovery

## What Is Account Recovery?

Account recovery describes the use case where a user is known to the customer (that is, registered in PingOne Recognize) but needs to be authenticated on a new device. Typically this is where:

* The user was previously enrolled on a device but no longer has access to it.

* The user is adding a backup device.

* The user is known to the customer (for example, submitted a selfie during onboarding) but has not yet authenticated on a device via Mobile SDK in the customer app (which would require [PingOne Recognize IDV Bridge](../idv-bridge/idv-bridge-on-premise.html)).

## Client State

PingOne Recognize can recover an account from the PingOne Recognize [client state](../introduction/account_recovery.html).

The client state is obtained either:

1. From your backend through PingOne Recognize IDV Bridge:

   * To generate this state, see [IDV Bridge SaaS](../idv-bridge/idv-bridge-saas.html) or [IDV On-Premise](../idv-bridge/idv-bridge-on-premise.html).

   * Then refer to [New Device Activation](mobile-sdk-new-device-activation.html) to learn how to use this state to bind a user ID to a new device.

2. From your client app using the PingOne Recognize Mobile SDK:

   * [Generate the client state](mobile-sdk-generating-client-state.html) during live enrollment or authentication.

   * Then refer to [New Device Activation](mobile-sdk-new-device-activation.html) to learn how to use this state to bind a user ID to a new device.
