---
title: Getting Started
description: This guide uses fundamental workflows to walk you through the steps to get an access token, and begin using the PingOne APIs.
component: pingone-api
page_id: pingone-api:getting-started:introduction
canonical_url: https://developer.pingidentity.com/pingone-api/getting-started/introduction.html
llms_txt: https://developer.pingidentity.com/pingone-api/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
page_aliases: ["index.adoc"]
section_ids:
  what-youll-do: What you'll do
  how-the-workflows-interact: How the workflows interact
  the-postman-choice: The Postman choice
---

# Getting Started

This guide uses fundamental workflows to walk you through the steps to get an access token, and begin using the PingOne APIs.

## What you'll do

There are three inter-related workflows you'll use to:

1. **Task 1:** Sign on to the admin console for your PingOne environment, create an admin-level Worker app, and assign roles to the Worker app. This is the only workflow for which you'll use the admin console. The remaining workflows use the PingOne APIs.

2. **Task 2:** Create and initially configure a new test environment and test user.

   As part of the workflow to create a new environment, you'll get an admin access token (a JSON Web Token) with permissions to call any of the PingOne APIs.

3. **Task 3:** Create a web application and sign-on (SSO) to that application using the test user you created in Task 2.

## How the workflows interact

![Workflows](../_images/p1_tutorial-flow.svg)

## The Postman choice

We use Postman to create our PingOne API docs, and have done so in this Getting Started guide as well. We highly recommend you use Postman to complete the workflows using the PingOne APIs ([Task 2: Create a test environment](create-a-test-environment.html) and [Task 3: Create an SSO workflow](simple-sso-workflow.html)). We've configured a Postman collection for you to download in each of these workflows, so you can call these requests in your own Postman installation. There's also an accompanying Postman Environment template already populated with the necessary variables.

|   |                                                                                                 |
| - | ----------------------------------------------------------------------------------------------- |
|   | Postman offers a free version. Refer to [Download Postman](https://www.postman.com/downloads/). |

If you'd rather not install Postman, this guide doesn't limit or constrain you in that respect. Each Postman request in this guide is well-documented, and has a dropdown list to show the coding language to use for the request. (This is also true for our [Platform Reference API](../platform/introduction.html) docs.)

![RequestLanguage](../_images/p1_requestLanguageList.png)

You can use cURL (the default) and call the request from your command line, or select one of the other coding languages in the dropdown list, copy the request into your IDE, and call it from there.
