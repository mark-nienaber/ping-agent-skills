---
title: Configuring SIEM Streaming
description: Configure SIEM streaming to send DaVinci events to a webhook configured in PingOne.
component: davinci
page_id: davinci:configuring_siem_streaming:davinci_configuring_siem_streaming
canonical_url: https://docs.pingidentity.com/davinci/configuring_siem_streaming/davinci_configuring_siem_streaming.html
llms_txt: https://docs.pingidentity.com/davinci/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: October 25, 2023
section_ids:
  about-this-task: About this task
  steps: Steps
  siem-streaming-payload-structure: SIEM streaming payload structure
  event-types: Event Types
  payload-structure: Payload Structure
  custom-analytics-example: Custom Analytics Example
  start-interaction-example: Start Interaction Example
  receive-request-example: Receive Request Example
  send-response-example: Send Response Example
  send-error-response-example: Send Error Response Example
---

# Configuring SIEM Streaming

Configure SIEM streaming to send DaVinci events to a webhook configured in PingOne.

## About this task

After you configure the PingOne webhook, it receives DaVinci events. These events are not affected by the logging level in the flow. The events use the payload structure described below.

|   |                                                                                                                                                         |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | This is not a real-time service. There can be a delay between when the DaVinci event occurs and when it appears in PingOne or in a third-party service. |

## Steps

1. Sign on to PingOne.

2. Create a new webhook as described in the [PingOne documentation](https://docs.pingidentity.com/pingone/integrations/p1_create_webhook.html).

   In the **Event types** list, select the **DaVinci** event type.

## SIEM streaming payload structure

SIEM streaming events use the payload structure and properties described here.

### Event Types

These event types generate a payload.

* Custom Analytics

  This event is sent by a [Flow Analytics connector](https://docs.pingidentity.com/connectors/flow_analytics_connector.html) node within a flow. This node can be configured to send information about the flow outcome.

* Start Interaction

  This event is sent when a flow execution starts. It can be used to count the number of flow invocations during a particular time period.

* Receive Request

  This event is sent when a connector receives an event. It contains information about the capability to be used and its required inputs.

  |   |                                |
  | - | ------------------------------ |
  |   | This event type is deprecated. |

* Send Response

  This event is sent after a connector has successfully executed a capability. It contains output information from the capability that successfully ran.

  |   |                                |
  | - | ------------------------------ |
  |   | This event type is deprecated. |

* Send Error Response

  This event is sent after a connector has failed to execute a capability. It contains information about the error.

### Payload Structure

All events use this payload structure.

```json
{
  "id" : "payload ID",
  "recordedAt" : "timestamp",
  "correlationId" : "correlation ID",
  "action" : {
    "type" : "DAVINCI_INTERACTION.interaction_type",
    "description" : "description"
  },
  "actors" : {
    "user" : {
      "id" : "bf29e0d1-279c-4d83-bc9a-b7490c13d9ba",
      "name" : "testdv",
      "environment" : {
        "id" : "c0ddf48d-605b-4173-9871-8fdf21d4a061"
      },
      "type" : "USER"
    }
  },
  "resources" : {
    "id" : "flow ID",
    "type" : "DAVINCI_INTERACTION",
    "name" : "flow name",
    "environment" : {
      "id" : "company ID"
    }
  },
  "result" : {
    "status" : "status"
  },
  "_embedded" : {
    "flowInteractionEvent" : {
    	// Actual Davinci Event Payload
    }
  }
}
```

**Table 1. Event Properties**

| Property             | Description                                                                                                             |
| -------------------- | ----------------------------------------------------------------------------------------------------------------------- |
| `id`                 | A unique identifier for the event payload.                                                                              |
| `recordedAt`         | The UTC timestamp when the event was recorded.                                                                          |
| `correlationId`      | A correlation ID for the event.                                                                                         |
| `action.type`        | The type of event. Valid values are `START_INTERACTION`, `RECEIVE_REQUEST`, `SEND_RESPONSE`, and `SEND_ERROR_RESPONSE`. |
| `action.description` | A description of the event type.                                                                                        |

**Table 2. Actor Properties**

| Property              | Description                                                    |
| --------------------- | -------------------------------------------------------------- |
| `user.id`             | The user ID.                                                   |
| `user.name`           | The user name.                                                 |
| `user.environment.id` | The company ID.                                                |
| `type`                | The type of actor. All events currently have a type of `USER`. |

**Table 3. Resource Properties**

| Property         | Description                                                                         |
| ---------------- | ----------------------------------------------------------------------------------- |
| `id`             | The flow ID.                                                                        |
| `type`           | The type of interaction. All events currently have a type of `DAVINCI_INTERACTION`. |
| `name`           | The flow name.                                                                      |
| `environment.id` | The company ID.                                                                     |

**Table 4. Result Properties**

| Property      | Description                                                                              |
| ------------- | ---------------------------------------------------------------------------------------- |
| `status`      | The result status. Valid values are `SUCCESS` and `FAILURE`.                             |
| `description` | A description of the response. This property is only present for `SEND_RESPONSE` events. |

**Table 5. Embedded Properties**

| Property                 | Description                                                                                                                                                                |
| ------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `eventMessage`           | The event type. Valid values are `StartInteraction`, `Receive Request`, `Send Response`, and `Send Error Response`.                                                        |
| `companyId`              | The company ID.                                                                                                                                                            |
| `interactionId`          | A unique identifier for the flow execution.                                                                                                                                |
| `flowVersionId`          | The flow version ID. If the version ID is not available, the value is `-1`.                                                                                                |
| `identity`               | The service that generated the event.                                                                                                                                      |
| `tsEms`                  | The UTC timestamp when the event completed in DaVinci.                                                                                                                     |
| `flowID`                 | The ID of the flow.                                                                                                                                                        |
| `flowName`               | The name of the flow.                                                                                                                                                      |
| `ID`                     | The node ID.This parameter is not sent for `START_INTERACTION` events for AP flows.	This property will be deprecated in a future release.                                  |
| `nodeID`                 | The node ID.This parameter is not sent for `START_INTERACTION` events for AP flows.                                                                                        |
| `originalCapabilityName` | The name of the capability used by the node.This parameter is not sent for `START_INTERACTION` events for AP flows.                                                        |
| `succcess`               | A boolean value that indicates whether the capability succeeded or failed.This parameter is not sent for `START_INTERACTION` events for AP flows.                          |
| `connectorId`            | The ID of the connector.This parameter is not sent for `START_INTERACTION` events for AP flows.                                                                            |
| `nodeTitle`              | The title of the node.This parameter is not sent for `START_INTERACTION` events for AP flows.                                                                              |
| `nodeDescription`        | The description value for the node.This parameter is not sent for `START_INTERACTION` events for AP flows.                                                                 |
| `outcomeType`            | The outcome type sent by the flow analytics connector (for example, login or enrollment).This parameter is only sent for custom analytics events.                          |
| `outcomeStatus`          | The outcome status sent by the flow analytics connector (for example, success, error, denied, fraud, or approved).This parameter is only sent for custom analytics events. |
| `connectionId`           | The ID of the flow analytics connector used to send the event.This parameter is only sent for custom analytics events.                                                     |

**Table 6. Parent Flow Properties**

| Property         | Description                                                                                                                                                                       |
| ---------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `companyId`      | The company ID of the parent flow.                                                                                                                                                |
| `flowID`         | The ID of the flow.                                                                                                                                                               |
| `flowVersionId`  | The flow version ID. If the version ID is not available, the value is `-1`.                                                                                                       |
| `ID`             | The node ID in the parent flow that triggered the current flow.                                                                                                                   |
| `connectionId`   | The ID of the flow conductor connector used to launch the subflow.                                                                                                                |
| `connectorId`    | The name of the connector that launched the subflow.                                                                                                                              |
| `capabilityName` | The name of the capability used to launch the subflow. Valid values are `startUiSubFlow` for subflows with a UI component and `startSubFlow` for subflows without a UI component. |
| `success`        | Indicates whether the subflow node was successful                                                                                                                                 |
| `respondToUser`  | Indicates whether the node presented a UI component to the user.                                                                                                                  |
| `interactionId`  | The interaction ID for the parent flow.                                                                                                                                           |

### Custom Analytics Example

```json
{
  "id" : "c452dcdf-a535-43f6-8cc3-a09ccb440e91",
  "recordedAt" : "2024-02-15T16:07:03.995Z",
  "correlationId" : "002ec717-c5a6-44ca-9d6f-ec9a86282fe7",
  "action" : {
    "type" : "DAVINCI_INTERACTION.CUSTOM_ANALYTICS",
    "description" : "Davinci Interaction Custom Analytics"
  },
  "actors" : {
    "user" : {
      "id" : "bf29e0d1-279c-4d83-bc9a-b7470c13d9ba",
      "name" : "username",
      "environment" : {
        "id" : "c0ddf48d-605b-4173-9871-8fdf21d4a061"
      },
      "type" : "USER"
    }
  },
  "resources" : [ {
    "type" : "DAVINCI_INTERACTION",
    "id" : "79f303c7-f2cf-ae6c-5ce2-21dc013c80c5",
    "name" : "PingOne Sign On Augmented with Custom Analytics",
    "environment" : {
      "id" : "9f835dca-fa37-489b-b835-6587ef71e5d8"
    }
  } ],
  "result" : {
    "status" : "SUCCESS"
  },
 "_embedded" : {
   "flowInteractionEvent" : {
     "eventMessage" : "Custom Analytics",
     "interactionId" : "002ec717-c5a6-44ca-9d6f-ec9a86282fe7",
     "flowVersionId" : 4,
     "connectorId" : "analyticsConnector",
     "originalCapabilityName" : "logOutcome",
     "flowName" : "PingOne Sign On Augmented with Custom Analytics",
     "outcomeType" : "enrollment",
     "usageTransactionType" : "COUNTED",
     "companyId" : "9f835dca-fa37-489b-b835-6587ef71e5d8",
     "identity" : "analyticsConnector",
     "success" : true,
     "outcomeStatus" : "success",
     "packetProtocol" : "action",
     "connectionId" : "b50fb6e57556c2b3535d152758902e90",
     "nodeId" : "ezmu5wo88g",
     "tsEms" : "2024-02-15T16:07:03.947Z",
     "flowId" : "79f303c7f2cfae6c5ce221dc013c80c5"
    }
  }
}
```

### Start Interaction Example

```json
{
  "id" : "c84142a4-3b71-422c-aa77-9296e88d2881",
  "recordedAt" : "2023-03-22T04:28:55.395Z",
  "action" : {
    "type" : "DAVINCI_INTERACTION.START_INTERACTION"
  },
  "actors" : {
    "user" : {
      "id" : "bf29e0d1-279c-4d83-bc9a-b7470c13d9ba",
      "name" : "username",
      "environment" : {
        "id" : "c0ddf48d-605b-4173-9871-8fdf21d4a061"
      },
      "type" : "USER"
    }
  },
  "resources" : [ {
    "id" : "8f43a71f-85b5-2501-09e7-cf4b705b1446",
    "type" : "DAVINCI_INTERACTION",
    "name" : "8f43a71f85b5250109e7cf4b705b1446",
    "environment" : {
      "id" : "b5bbc401-7a1f-4738-b589-b3ea05bc46e4"
    }
  } ],
  "result" : {
    "status" : "SUCCESS"
  },
  "_embedded" : {
    "flowInteractionEvent" : {
      "eventMessage" : "Start Interaction",
      "companyId" : "b5bbc401-7a1f-4738-b589-b3ea05bc46e4",
      "interactionId" : "00467d91-1bb0-4ff7-ac70-307f49c3dcd2",
      "tsInteractionId" : "1679459335395 + 00467d91-1bb0-4ff7-ac70-307f49c3dcd2",
      "flowVersionId" : -1,
      "capabilityName" : "add",
      "identity" : "api",
      "tsEms" : "2023-03-22T04:28:55.395Z",
      "flowId" : "8f43a71f85b5250109e7cf4b705b1446",
      "packetTimestamp" : 1679459335395
    }
  }
}
```

### Receive Request Example

```json
{
  "id" : "2f8748d2-5c6b-4323-ba22-3276a5d54b86",
  "recordedAt" : "2023-03-22T04:28:55.456Z",
  "action" : {
    "type" : "DAVINCI_INTERACTION.RECEIVE_REQUEST"
  },
  "actors" : {
    "user" : {
      "id" : "bf29e0d1-279c-4d83-bc9a-b7470c13d9ba",
      "name" : "username",
      "environment" : {
        "id" : "c0ddf48d-605b-4173-9871-8fdf21d4a061"
      },
      "type" : "USER"
    }
  },
  "resources" : [ {
    "id" : "8f43a71f-85b5-2501-09e7-cf4b705b1446",
    "type" : "DAVINCI_INTERACTION",
    "name" : "8f43a71f85b5250109e7cf4b705b1446",
    "environment" : {
      "id" : "b5bbc401-7a1f-4738-b589-b3ea05bc46e4"
    }
  } ],
  "result" : {
    "status" : "SUCCESS"
  },
  "_embedded" : {
    "flowInteractionEvent" : {
      "eventMessage" : "Receive Request",
      "packetTo" : "httpConnector",
      "interactionId" : "00467d91-1bb0-4ff7-ac70-307f49c3dcd2",
      "flowVersionId" : 21,
      "capabilityName" : "add",
      "connectorId" : "httpConnector",
      "originalCapabilityName" : "customHtmlMessage",
      "companyId" : "b5bbc401-7a1f-4738-b589-b3ea05bc46e4",
      "tsInteractionId" : "1679459335456 + 00467d91-1bb0-4ff7-ac70-307f49c3dcd2",
      "identity" : "httpConnector",
      "packetProtocol" : "action",
      "connectionId" : "867ed4363b2bc21c860085ad2baa817d",
      "id" : "nzeo7no4po",
      "tsEms" : "2023-03-22T04:28:55.456Z",
      "flowId" : "8f43a71f85b5250109e7cf4b705b1446",
      "packetTimestamp" : 1679459335456
    }
  }
}
```

### Send Response Example

```json
{
  "id" : "971b5fd8-1b59-4e77-8836-00ab9941ff67",
  "recordedAt" : "2023-03-22T04:28:55.512Z",
  "action" : {
    "type" : "DAVINCI_INTERACTION.SEND_RESPONSE"
  },
  "actors" : {
    "user" : {
      "id" : "bf29e0d1-279c-4d83-bc9a-b7470c13d9ba",
      "name" : "username",
      "environment" : {
        "id" : "c0ddf48d-605b-4173-9871-8fdf21d4a061"
      },
      "type" : "USER"
    }
  },
  "resources" : [ {
    "id" : "8f43a71f-85b5-2501-09e7-cf4b705b1446",
    "type" : "DAVINCI_INTERACTION",
    "name" : "8f43a71f85b5250109e7cf4b705b1446",
    "environment" : {
      "id" : "b5bbc401-7a1f-4738-b589-b3ea05bc46e4"
    }
  } ],
  "result" : {
    "status" : "SUCCESS",
    "description" : "Send Response successful for flowId: 8f43a71f85b5250109e7cf4b705b1446, connector: httpConnector and capability: customHtmlMessage"
  },
  "_embedded" : {
    "flowInteractionEvent" : {
      "eventMessage" : "Send Response",
      "packetTo" : "httpConnector",
      "interactionId" : "00467d91-1bb0-4ff7-ac70-307f49c3dcd2",
      "flowVersionId" : 21,
      "capabilityName" : "add",
      "connectorId" : "httpConnector",
      "originalCapabilityName" : "customHtmlMessage",
      "companyId" : "b5bbc401-7a1f-4738-b589-b3ea05bc46e4",
      "tsInteractionId" : "1679459335512 + 00467d91-1bb0-4ff7-ac70-307f49c3dcd2",
      "identity" : "httpConnector",
      "success" : true,
      "packetProtocol" : "action",
      "connectionId" : "867ed4363b2bc21c860085ad2baa817d",
      "id" : "nzeo7no4po",
      "tsEms" : "2023-03-22T04:28:55.512Z",
      "flowId" : "8f43a71f85b5250109e7cf4b705b1446",
      "packetTimestamp" : 1679459335512
    }
  }
}
```

### Send Error Response Example

```json
{
  "id" : "ccb8d1ec-61ed-4big-a0c4-a190ca677ad1",
  "recordedAt" : "2023-03-22T09:18:45.448Z",
  "action" : {
    "type" : "DAVINCI_INTERACTION.SEND_ERROR_RESPONSE"
  },
  "actors" : {
    "user" : {
      "id" : "bf29e0d1-279c-4d83-bc9a-b7470c13d9ba",
      "name" : "username",
      "environment" : {
        "id" : "c0ddf48d-605b-4173-9871-8fdf21d4a061"
      },
      "type" : "USER"
    }
  },
  "resources" : [ {
    "id" : "8f43a71f-85b5-2501-09e7-cf4b705b1446",
    "type" : "DAVINCI_INTERACTION",
    "name" : "8f43a71f85b5250109e7cf4b705b1446",
    "environment" : {
      "id" : "b5bbc401-7a1f-4738-b589-b3ea05bc46e4"
    }
  } ],
  "result" : {
    "status" : "SUCCESS"
  },
  "_embedded" : {
    "flowInteractionEvent" : {
      "eventMessage" : "Send Error Response",
      "packetTo" : "httpConnector",
      "interactionId" : "00152de6-e4db-4bbb-9bc7-1d09dc50492c",
      "flowVersionId" : 24,
      "capabilityName" : "add",
      "connectorId" : "httpConnector",
      "originalCapabilityName" : "makeRestApiCall",
      "companyId" : "b5bbc401-7a1f-4738-b589-b3ea05bc46e4",
      "tsInteractionId" : "1679476725448 + 00152de6-e4db-4bbb-9bc7-1d09dc50492c",
      "identity" : "httpConnector",
      "packetProtocol" : "action",
      "connectionId" : "867ed4363b2bc21c860085ad2baa817d",
      "id" : "yg52xyeh81",
      "tsEms" : "2023-03-22T09:18:45.448Z",
      "flowId" : "8f43a71f85b5250109e7cf4b705b1446",
      "packetTimestamp" : 1679476725448
    }
  }
}
```