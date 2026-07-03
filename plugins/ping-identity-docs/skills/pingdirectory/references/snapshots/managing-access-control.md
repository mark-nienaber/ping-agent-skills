---
title: $attr.attrName macro
description: The ($attr.attrName) macro extracts a value from a specified attribute in the target entry rather than extracting a value from a field with the same number in the target distinguished name (DN).
component: pingdirectory
version: 11.1
page_id: pingdirectory:managing_access_control:pd_ds_attr_attrname_macro
canonical_url: https://docs.pingidentity.com/pingdirectory/11.1/managing_access_control/pd_ds_attr_attrname_macro.html
llms_txt: https://docs.pingidentity.com/pingdirectory/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: September 13, 2023
---

# $attr.attrName macro

The `($attr.attrName)` macro extracts a value from a specified attribute in the target entry rather than extracting a value from a field with the same number in the target distinguished name (DN).

For example, `($attr.description)` is replaced with the value of the `description` attribute in the target entry. If there are multiple values for the specified attribute, then multiple actualized DNs are produced for the bind DN, and the first matching actualized DN is used.

The `($attr.attrName)` macro expands only the attribute's value so that you can extract values from the target DN and build relative distinguished names (RDNs) with different attribute names and types. Because the `($attr.attrName)` macro extracts only the attribute's value, you can combine it with a type other than what is in the target DN.
