---
title: Securing AI agents with PingOne Advanced Services
description: Instructions on configuring AI use cases with PingOne Advanced Services.
component: pingoneadvancedservices
page_id: pingoneadvancedservices:securing_AI_agents:p1as_secure_AI_agents
canonical_url: https://docs.pingidentity.com/pingoneadvancedservices/securing_AI_agents/p1as_secure_AI_agents.html
---

# Securing AI agents with PingOne Advanced Services

If you're currently using PingOne Advanced Services for your employees, you already have what you need to secure AI agents. You just need to configure PingFederate to process token exchange requests and issue delegated access tokens.

These tokens can be scoped to the absolute minimum required for the specific task, which means the agent only gets permission to do exactly what you asked it to do and nothing more. Every exchanged token is auditable end-to-end, so you can see which original user and client led to which delegated token and call.

To design and configure your AI agent use cases on PingOne Advanced Services, follow the steps outlined in [Securing AI Agents with PingFederate using delegated access tokens](https://developer.pingidentity.com/identity-for-ai/use-cases/idai-securing-agents-pingfed.html), in the Identity for AI guide.

This guide explains the token exchange architecture and token exchange patterns, and provides detailed instructions for defining scopes, configuring and mapping token exchange policies, and registering the agent as an OAuth client.
