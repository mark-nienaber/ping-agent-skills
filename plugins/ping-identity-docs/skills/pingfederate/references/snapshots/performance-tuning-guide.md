---
title: About Performance Tuning
description: This section shows you to how to fine-tune a few simple application and system level settings to enable PingFederate to achieve maximum performance of the hardware chosen for your deployment.
component: pingfederate
version: 13.1
page_id: pingfederate:performance_tuning_guide:pf_about_performance_tuning
canonical_url: https://docs.pingidentity.com/pingfederate/13.1/performance_tuning_guide/pf_about_performance_tuning.html
llms_txt: https://docs.pingidentity.com/pingfederate/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 8, 2024
---

# About Performance Tuning

This section shows you to how to fine-tune a few simple application and system level settings to enable PingFederate to achieve maximum performance of the hardware chosen for your deployment.

The default configuration since PingFederate 10.2 is acceptable for most small size deployments. Mission-critical and high-transaction volume deployments might require additional tuning.

This guide addresses several areas of tuning such as logging, concurrency, memory, and Java-specific tuning options. It is not designed as a one-size-fits-all set of instructions to optimize PingFederate, but more as a checklist of suggestions for areas of the product that can be tuned to improve performance, and any tradeoffs associated with those changes. For ultimate reassurance that any fine-tuned settings will meet your expectations, performance testing in a lab environment is recommended.
