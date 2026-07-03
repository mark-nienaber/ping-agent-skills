---
title: AI agent logging and auditing
description: Use the Audit page to review information about AI agent events and actions in PingOne.
component: pingone
page_id: pingone:ai_agents:p1_ai_agent_logging
canonical_url: https://docs.pingidentity.com/pingone/ai_agents/p1_ai_agent_logging.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  steps: Steps
  result: Result
---

# AI agent logging and auditing

You can run reports to see a summary of AI agent events or actions performed in PingOne. Learn more in [Running an audit report](../monitoring/p1_running_audit_report.html).

You can find a complete list of events logged in PingOne in [Audit Reporting Events](https://developer.pingidentity.com/pingone-api/platform/reference/audit-reporting-events.html) in the PingOne API documentation.

## Steps

1. In the PingOne admin console, go to **Monitoring > Audit**.

2. Enter the report parameters:

   * **Time Range**: Limit the report results to a specified range of time.

     |   |                                                                                                                                                                                                                                                                                                                                                                                                                       |
     | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
     |   | Data up to 14 days old relative to the current date is available immediately. Data older than 14 days must be requested from the **Audit** page or using the API, and you can't request data for dates that are more than 2 years (730 days) before the current date. You can run reports a maximum of 14 days at a time. If you enter an invalid time range, you're prompted to adjust it before you run the report. |

   * **Selected Fields**: Specify which columns appear in the results list.

   * **Time Zone**: Specify which time zone to use in the results list. The timestamp shows the date and time for the selected time zone.

   * **Filter Type**: Select any of the following filter types to limit the results to AI agent activity and then select a filter. AI agent events use the application event types.

     | **Filter Type** | **Filter**                                                                                                                                                              |
     | --------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
     | **Application** | Select the AI agent for which you want to limit results.                                                                                                                |
     | **Event Type**  | Select any of the following to limit the event types to application-related event types:- **Application Created**

     - **Application Deleted**

     - **Application Updated** |
     | **Resource ID** | Paste the ID of an AI agent to limit results. You can find the ID on the **Overview** tab of the AI agent.                                                              |

     ![A screen capture of the Audit Parameters for AI agent events.](_images/p1_ai_agent_audit_parameters.png)

   * **Secondary Filter Type**: Specify a secondary filter to limit the results to a particular type, user, or resource. You must specify a primary filter type before you can select a secondary filter type.

3. Click **Run**.

## Result

Results display based on the parameters you selected. The following image shows results for AI agent events:

![A screen capture of the Audit Results for AI agent events.](_images/p1_ai_agent_audit_logging.png)

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | * The **Available Dates (UTC)** section lists the dates for the data that's available to query or has been requested.

* Depending on the number of days requested and the average number of events logged per day, the process can take from 2 to 24 hours. You can request a maximum of 14 days of data from within the data retention period and you can't request additional data while another request is pending.

  If you have a valid email address in PingOne, you'll be notified when the requested data is available. At that point, you can return to the **Audit** page and run queries against the data for the timeframe requested. The retrieved data is available for 14 days from the date of the retrieval request. |
