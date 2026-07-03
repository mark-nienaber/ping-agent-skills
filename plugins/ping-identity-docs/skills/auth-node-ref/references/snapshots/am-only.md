---
title: Amster Jwt Decision node
description: Configure the Amster JWT Decision node to authenticate Amster connections to PingAM using SSH key pairs stored in an authorized_keys file.
component: auth-node-ref
version: 8.1
page_id: auth-node-ref:am-only:amster-jwt-decision
canonical_url: https://docs.pingidentity.com/auth-node-ref/latest/am-only/amster-jwt-decision.html
llms_txt: https://docs.pingidentity.com/auth-node-ref/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Nodes &amp; Trees", "Journeys", "Amster"]
section_ids:
  example: Example
  availability: Availability
  inputs: Inputs
  dependencies: Dependencies
  configuration: Configuration
  outputs: Outputs
  outcomes: Outcomes
  errors: Errors
---

# Amster Jwt Decision node

The Amster Jwt Decision node lets AM authenticate Amster connections using SSH keys.

The Amster client signs the JWT using a local private key. AM verifies the signature using the list of public keys in the `authorized_keys` file. Specify the path to the `authorized_keys` file in the node configuration.

If the entry in the authorized keys file contains a `from` parameter, only connections originating from a qualifying host are permitted.

Find more information in [Private key connections](https://docs.pingidentity.com/pingam/8.1/amster/connect-am.html#private-login).

## Example

This node is used only by the `amsterService` authentication tree:

![journey amster service](_images/journey-amster-service.png)

|   |                                                                            |
| - | -------------------------------------------------------------------------- |
|   | Changing or removing this tree could prevent Amster from connecting to AM. |

## Availability

| Product                               | Available? |
| ------------------------------------- | ---------- |
| PingOne Advanced Identity Cloud       | No         |
| PingAM (self-managed)                 | Yes        |
| Ping Identity Platform (self-managed) | Yes        |

## Inputs

The node reads the `NONCE_STATE_KEY` from the Amster client.

## Dependencies

This node has no dependencies.

## Configuration

| Property        | Usage                                                                                                                                                                                                            |
| --------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Authorized Keys | Location of the `authorized_keys` file used to validate remote Amster connections.This file has the same format as an [OpenSSH `authorized_keys`](https://www.ssh.com/academy/ssh/authorized-keys-openssh) file. |

## Outputs

This node doesn't change the shared state.

## Outcomes

* True

  The journey follows this outcome if the node can validate the incoming private key against the public keys in the `authentication_keys` file. Successful authentication creates an `amAdmin` session in AM.

* False

  The journey follows this outcome if the node can't validate the incoming private key against the public keys in the `authentication_keys` file, either because the incoming key is invalid, or because the `authentication_keys` file is inaccessible.

## Errors

If the node can't read the `authorized_keys` file, it returns the error `AmsterJwtDecisionNode: Could not read authorized keys file filename`.
