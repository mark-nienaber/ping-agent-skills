---
title: Build an iOS Sample App with AI
description: Build an iOS authentication app with device binding using the AIC MCP Server and Ping agent skills in Claude Code through natural language prompts.
component: build-with-ai
page_id: build-with-ai:use-cases:build-ios-app
canonical_url: https://developer.pingidentity.com/build-with-ai/use-cases/build-ios-app.html
llms_txt: https://developer.pingidentity.com/build-with-ai/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: May 22, 2026
keywords: ["Use Case", "iOS", "SwiftUI", "AIC MCP Server", "Agent Skills", "Claude Code", "Ping Orchestration SDK", "OIDC", "Device Binding"]
section_ids:
  build-ios-app-description: Description
  build-ios-app-goals: Goals
  build-ios-app-prereqs: Prerequisites
  demo: Demo
  build-ios-app-tasks: Tasks
  build-ios-app-task-1: "Task 1: Create a device binding journey"
  build-ios-app-task-2: "Task 2: Update the journey for passwordless login"
  build-ios-app-task-3: "Task 3: Create an OIDC application"
  build-ios-app-task-4: "Task 4: Scaffold the iOS app"
  build-ios-app-task-5: "Task 5: Run the app"
  build-ios-app-validation: Validation
  build-ios-app-explore-further: Explore further
  build-ios-app-reference-material: Reference material
---

# Build an iOS Sample App with AI

[icon: circle-check, set=far]PingOne Advanced Identity Cloud [icon: apple, set=fab]iOS

## Description

Estimated time to complete: 15 minutes

This use case shows AI-first headless identity in action. Using Claude Code connected to the [AIC MCP Server](../aic-mcp-server/overview.html) and the [Mobile and Web App Integration Agent Skills](../agent-skills/overview.html), you go from a blank slate to a running iOS authentication app, creating the PingOne Advanced Identity Cloud Journey, making server-side configuration changes, setting up the OIDC application, and scaffolding the SwiftUI client, entirely through natural language prompts, without leaving your IDE.

In this use case, you will build with AI and:

* Create a device binding journey in PingOne Advanced Identity Cloud using the AIC MCP Server

* Update the journey to support passwordless login using device binding and Face ID

* Create a matching OIDC application in PingOne Advanced Identity Cloud

* Rapidly generate an iOS sample app using the Mobile and Web App Integration Agent Skills

* Run the app against your PingOne Advanced Identity Cloud development tenant

### Goals

After completing this use case, you will understand:

* How to use the AIC MCP Server to manage journeys and applications from your IDE

* How the Mobile and Web App Integration Agent Skills rapidly generates an iOS sample app with authentication flows

* How to combine MCP tools and agent skills in a single natural language workflow

## Prerequisites

Before you begin:

* [Claude Code](https://claude.ai/code) is installed and running

* The [AIC MCP Server](../aic-mcp-server/getting-started.html) is configured and authenticated against an PingOne Advanced Identity Cloud sandbox or development tenant

* The [Mobile and Web App Integration Agent Skills](../agent-skills/overview.html#mobile-web-app-integration) are installed in Claude Code

* Xcode is installed with an iOS simulator or physical device available

## Demo

**Video (Brightcove)**

\<https\://players.brightcove.net/771836189001/default\_default/index.html?videoId=6396329895112>

## Tasks

### Task 1: Create a device binding journey

Prompt Claude Code to create a new device binding journey in PingOne Advanced Identity Cloud. The AIC MCP Server translates your natural language prompt into the appropriate API calls, configuring nodes and transitions without you touching the Admin UI.

Example prompt:

```none
Create a new journey in my AIC sandbox called "iOS Device Binding Login". The journey should start with a Page Node containing a Username Collector and Password Collector. After successful credential validation using a Data Store Decision node, check if the user has a registered device using a Device Profile Collector node. If no device is registered, route to a Device Binding node to register the device, then proceed to a Success node. If a device is already registered, route to a Device Authentication node to verify the binding, then proceed to a Success node. If credential validation fails, increment a Retry Limit node and after 5 failed attempts lock the account and route to a Failure node. Make sure all node connections are wired correctly.
```

### Task 2: Update the journey for passwordless login

With the journey created, prompt Claude Code to update it to support passwordless login for returning users. If a device is already registered, the user skips the password step entirely and authenticates using device binding, such as Face ID.

Example prompt:

```none
Update the "iOS Device Binding Login" journey so that when a user attempts to log in, it first checks if they have a registered device. If a device is registered, skip the password step entirely and authenticate using Device Authentication (Face ID / biometrics) for a passwordless login experience. If no device is registered, fall back to the existing username and password flow followed by Device Binding to register their device for future logins. Make sure all node connections are wired correctly.
```

### Task 3: Create an OIDC application

Prompt Claude Code to create a matching OIDC/OAuth 2.0 application in PingOne Advanced Identity Cloud tied to the journey. Claude Code captures the client ID and redirect URI needed for the mobile app.

Example prompt:

```none
Create a native OIDC application in AIC for my iOS app using the journey we just created.
```

### Task 4: Scaffold the iOS app

Prompt Claude Code to invoke the Mobile and Web App Integration Agent Skills and generate a SwiftUI sample app wired to the journey and OIDC application. Be explicit about the screens and behavior you want so the skill produces a complete, runnable starting point.

Example prompt:

```none
Using the Ping Orchestration Agent Skills, scaffold an iOS SwiftUI sample app that integrates with the "iOS Device Binding Login" journey and OIDC app we just configured. The app should have a dedicated login screen where the user enters their credentials or is prompted for Face ID if a device is already bound. After a successful login, show a home screen with the authenticated user's profile and a clearly visible logout button that ends the session and returns the user to the login screen.
```

### Task 5: Run the app

Build and run the scaffolded app in Xcode against your live PingOne Advanced Identity Cloud sandbox to complete the end-to-end flow.

|   |                                                                                                                                                                                        |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | You don't have to issue these as separate prompts. Describe the entire goal at once and Claude Code will use the AIC MCP Server and the SDK skill in whatever order the task requires. |

## Validation

To confirm everything is working:

1. Open the running app in your iOS simulator or device.

2. Enter credentials for a test user in your PingOne Advanced Identity Cloud sandbox to register a device on first login.

3. Log out, then log in again and confirm the app skips the password step and prompts for Face ID.

4. After authenticating, confirm the home screen displays the user's profile and a logout button.

5. Tap logout and confirm the session ends and the app returns to the login screen.

## Explore further

### Reference material

| Resource                                                                                                       | Description                                                                                            |
| -------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------ |
| [Mobile and Web App Integration Agent Skills on GitHub](https://github.com/pingidentity/ping-sdk-agent-skills) | The agent skills repository, including the iOS SDK skill used in this use case.                        |
| [Ping iOS SDK](https://github.com/ForgeRock/ping-ios-sdk/)                                                     | The Ping Orchestration iOS SDK that the generated sample app is built on.                              |
| [iOS SDK sample apps](https://github.com/ForgeRock/sdk-sample-apps/tree/main/iOS)                              | Sample iOS apps showing common authentication patterns with the Ping iOS SDK.                          |
| [AIC MCP Server available tools](../aic-mcp-server/available-tools.html)                                       | Full reference for all MCP tools used to manage journeys, applications, and server-side configuration. |
| [Agent Skills overview](../agent-skills/overview.html)                                                         | All available agent skill collections, including Android and ReactJS in addition to iOS.               |