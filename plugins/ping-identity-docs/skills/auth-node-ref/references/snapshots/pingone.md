---
title: PingOne Authorize node
description: Configure the PingOne Authorize node to send policy decision requests to a PingOne Authorize environment and evaluate authorization levels in a journey.
component: auth-node-ref
version: 8.1
page_id: auth-node-ref:pingone:pingone-authorize
canonical_url: https://docs.pingidentity.com/auth-node-ref/latest/pingone/pingone-authorize.html
llms_txt: https://docs.pingidentity.com/auth-node-ref/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  example: Example
  availability: Availability
  inputs: Inputs
  dependencies: Dependencies
  configuration: Configuration
  outputs: Outputs
  outcomes: Outcomes
---

# PingOne Authorize node

The PingOne Authorize node sends a decision request to a specified decision endpoint in your PingOne Authorize environment. These authorizations include:

* [Evaluate a Decision Request](https://developer.pingidentity.com/pingone-api/authorize/authorization-decisions/decision-evaluation/execute-a-decision-request.html)

* [Authorize Client with Individual Decision](https://developer.pingidentity.com/pingauthorize/pingauthorize/policy-decision/json-pdp/individual-requests/authorize-client-with-individual-decision.html)

To use the PingOne Authorize node, you must first set up the [PingOne Service](pingone-service.html).

## Example

The following example journey illustrates how to use the PingOne Authorize node:

![PingOne Authorize node example](_images/p1-authorize-journey.png)

The PingOne Authorize node gets the username from Username Collector node and evaluates the level authorization for the user. Based on the authorization level, further action is taken.

## Availability

| Product                               | Available? |
| ------------------------------------- | ---------- |
| PingOne Advanced Identity Cloud       | Yes        |
| PingAM (self-managed)                 | Yes 1      |
| Ping Identity Platform (self-managed) | Yes 1      |

1 For self-managed products, download the node from the [Ping Identity Marketplace](https://marketplace.pingone.com/item/ping-authorize).

## Inputs

This node retrieves the attribute map from the shared state.

Additionally, the node first attempts to locate in shared state the `PingOne Authorize Policy Attribute(s)` defined in the policy that corresponds to the active decision endpoint.

## Dependencies

You must set up the following before using the PingOne Authorize node:

* [Authorization policies](https://docs.pingidentity.com/pingone/authorization_using_pingone_authorize/p1az_policies.html)

* [Adding a worker application for the PingOne Authorize service](https://docs.pingidentity.com/pingone/authorization_using_pingone_authorize/p1az_adding_worker_app.html)

  * Requires the [Identity Data Admin](https://developer.pingidentity.com/pingone-api/platform/roles.html) role

* [PingOne Worker service](https://docs.pingidentity.com/pingam/8.1/setup/services-configuration.html#realm-pingone-worker-service)

## Configuration

| Property               | Usage                                                                                                                                                                                                                                                                                                            |
| ---------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| PingOne Worker Service | Service for specific PingOne Worker application.                                                                                                                                                                                                                                                                 |
| Decision Endpoint ID   | The Decision Endpoint ID from the PingOne Authorize service.                                                                                                                                                                                                                                                     |
| Attribute Map          | The attribute map is to overcome the name differences between shared state attributes in PingOne Advanced Identity Cloud and the request parameters in PingOne. For example, if the shared store `firstName` refers to `givenName` in PingOne, then the `Attribute Map` entry would be: `firstName ⇒ givenName`. |
| Statement Codes        | Set the node outcomes based on the statements from the PingOne Authorize decision.                                                                                                                                                                                                                               |
| Continue               | Use the `Continue` toggle for a single outcome case.                                                                                                                                                                                                                                                             |

## Outputs

This node doesn't change the shared state.

## Outcomes

* `Permit`

  Satisfied the active policy's permit condition and authorized the user.

* `Deny`

  Satisfied the active policy's deny condition and did not authorize the user.

* `Indeterminate`

  Does not satisfy the active policy's permit or deny conditions.

* `Error`

  There was an error during the authorization process.

  If this node logs an error, review the log messages to find the reason for the error and address the issue appropriately.
