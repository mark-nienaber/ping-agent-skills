---
title: Accept Terms and Conditions node
description: Prompts users to accept the active terms and conditions during registration or sign-on journeys in PingAM.
component: auth-node-ref
version: 8.1
page_id: auth-node-ref::accept-terms-and-conditions
canonical_url: https://docs.pingidentity.com/auth-node-ref/latest/accept-terms-and-conditions.html
llms_txt: https://docs.pingidentity.com/auth-node-ref/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Nodes &amp; Trees", "Journeys", "Terms &amp; Conditions"]
page_aliases: ["auth-node-accept-terms-and-conditions.adoc"]
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

# Accept Terms and Conditions node

The Accept Terms and Conditions node prompts the user to accept the currently active terms and conditions, configured in the Platform UI *(tooltip: Advanced Identity Cloud admin console)*.

Use this node for registration, or combined with the [Terms and Conditions Decision node](terms-and-conditions-decision.html) for progressive profiling or log in.

## Example

For progressive profiling, include this node after a [Terms and Conditions Decision node](terms-and-conditions-decision.html). If the user has not accepted the latest version of the terms and conditions, evaluation takes them to a page that requires them to accept the current terms and conditions.

The [Patch Object node](patch-object.html) stores the acceptance response in the underlying identity service (PingIDM) if the user accepts:

![Storing acceptance of terms and conditions](_images/trees-node-accept-terms-conditions-tree-example.png)

## Availability

| Product                               | Available? |
| ------------------------------------- | ---------- |
| PingOne Advanced Identity Cloud       | Yes        |
| PingAM (self-managed)                 | Yes 1      |
| Ping Identity Platform (self-managed) | Yes        |

1 This functionality requires that you configure AM as part of a [Ping Identity Platform deployment](https://docs.pingidentity.com/platform/8.1/sample-setup/).

## Inputs

None. This node doesn't read shared state data.

## Dependencies

This node depends on the underlying identity service (PingIDM) for the active terms and conditions.

## Configuration

This node has no configurable properties.

## Outputs

The node writes a `termsAccepted` object to the shared node state. The object contains these fields:

* `acceptDate`: A timestamp string indicating when the user accepted the terms.

* `termsVersion`: A string indicating the version of the accepted terms.

## Outcomes

Single outcome path; the user accepted the terms and conditions.

## Errors

This node doesn't log any error or warning messages of its own.
