---
title: Akamai Account Protector node
description: Use the Akamai Account Protector node to inject the Akamai risk score into an Advanced Identity Cloud authentication journey
component: pingoneaic
page_id: pingoneaic:release-notes:rapid-channel/akamai-acc-protect-node
canonical_url: https://docs.pingidentity.com/pingoneaic/release-notes/rapid-channel/akamai-acc-protect-node.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  compatibility: Compatibility
  inputs: Inputs
  dependencies: Dependencies
  akamai-acc-prot-setup: Configure Akamai Account Protector
  enable_account_protector_on_the_akamai_edge: Enable Account Protector on the Akamai Edge
  add_the_username_parameter_to_akamai_account_protector: Add the username parameter to Akamai Account Protector
  configuration: Configuration
  outputs: Outputs
  example: Example
---

# Akamai Account Protector node

Use the Akamai Account Protector node to inject the Akamai risk score into your authentication journey. When the Akamai Account Protector feature is enabled for your application, the Akamai Edge service provides the risk score in the HTTP header. Learn more in the [Akamai Account Protector](https://techdocs.akamai.com/cloud-security/docs/account-protector) documentation.

## Compatibility

| Product                               | Compatible? |
| ------------------------------------- | ----------- |
| Advanced Identity Cloud               | Yes         |
| PingAM (self-managed)                 | Yes         |
| Ping Identity Platform (self-managed) | Yes         |

## Inputs

This node retrieves user risk data from the Akamai-User-Risk HTTP request header.

## Dependencies

You must set up [Akamai Account Protector](https://www.akamai.com/resources/product-brief/account-protector) and enable it in your web application before using the Akamai Account Protector node.

### Configure Akamai Account Protector

Akamai Account Protector detects malicious activities and assigns risk scores to requests. To inject the akamai-user-risk header, follow these steps:

#### Enable Account Protector on the Akamai Edge

1. Log in to Akamai Control Center.

2. Navigate to Security Configuration and select your existing security policy or create a new one.

3. Enable Account Protector under Bot Management settings.

4. Ensure that risk scoring is enabled and that Akamai adds the akamai-user-risk HTTP header.

##### Add the username parameter to Akamai Account Protector

1. In the Akamai Control Center, create an API Definition to PingOne AIC's hostname.

2. Add an API Resource with the following:

   * **Name:** Authenticate

   * **Path:** `/am/json/realms/root/realms/alpha/authenticate`

3. Check the `POST` method and set the request parameters. For example:

   ![akamai acc prot set par](../_images/akamai-acc-prot-set-par.png)

4. Similarly, set the response parameters.

   > **Collapse: The sample JSON/XML Schema script used in this node.**
   >
   > ```
   > {
   >   "requestBody": {
   >     "content": {
   >       "application/json": {
   >         "schema": {
   >           "type": "object",
   >           "required": [
   >             "callbacks"
   >           ],
   >           "properties": {
   >             "callbacks": {
   >               "type": "array",
   >               "items": {
   >                 "type": "object",
   >                 "properties": {
   >                   "input": {
   >                     "type": "array",
   >                     "items": {
   >                       "type": "object",
   >                       "properties": {
   >                         "name": {
   >                           "type": "string"
   >                         }
   >                       }
   >                     }
   >                   }
   >                 }
   >               },
   >               "description": "callbacks"
   >             }
   >           }
   >         }
   >       },
   >       "application/xml": {
   >         "schema": {
   >           "type": "object",
   >           "required": [
   >             "callbacks"
   >           ],
   >           "properties": {
   >             "callbacks": {
   >               "type": "array",
   >               "items": {
   >                 "type": "object",
   >                 "properties": {
   >                   "input": {
   >                     "type": "array",
   >                     "items": {
   >                       "type": "object",
   >                       "properties": {
   >                         "name": {
   >                           "type": "array",
   >                           "items": {
   >                             "type": "string"
   >                           },
   >                           "maxItems": 1
   >                         }
   >                       }
   >                     }
   >                   }
   >                 }
   >               },
   >               "description": "callbacks"
   >             }
   >           },
   >           "xml": {
   >             "name": "root"
   >           }
   >         }
   >       }
   >     },
   >     "required": true
   >   }
   > }
   > ```

## Configuration

| Property                           | Usage                                                                                                                                                                                                 |
| ---------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| High Risk Threshold                | The maximum user risk score for a high risk assessment. Scores above medium assessment and up to this value are categorized as high risk. Scores above this value are categorized as a critical risk. |
| Medium Risk Threshold              | The maximum user risk score for a medium risk assessment. Scores between the the Low Risk Threshold and this value are categorized as medium risk.                                                    |
| Low Risk Threshold                 | The maximum user risk score for a low risk assessment. Scores up to this value are categorized as low risk.                                                                                           |
| Save Akamai Header to Shared State | If selected, the node writes the Akamai-User-Risk header value to the shared state.                                                                                                                   |

## Outputs

By default, this node writes the Akamai-User-Risk HTTP request header value to the transient state. If Save Akamai Header to Shared State is selected, then the value is stored in shared state.

## Example

The following example journey illustrates the use of Akamai Account Protector node.

![Journey using Akamai Account Protector node](../_images/akamai-account-protector-journey.png)

The inner journey shown above is contained in an outer journey which performs user authentication and collects the username to the Akamai Account Protector node. The Akamai Account Protector node parses the Akamai-User-Risk HTTP request header and extracts the user risk score. Based on the risk score, the authentication journey progresses through the appropriate outcome.
