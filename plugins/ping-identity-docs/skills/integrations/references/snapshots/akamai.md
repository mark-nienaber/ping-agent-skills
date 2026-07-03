---
title: Akamai Account Protector IdP Adapter settings reference
description: Descriptions of standard and advanced fields that you can configure for the Akamai Account Protector IdP Adapter.
component: akamai
page_id: akamai:setup:pf-akamai-p7-adapter-settings-ref
canonical_url: https://docs.pingidentity.com/integrations/akamai/setup/pf-akamai-p7-adapter-settings-ref.html
revdate: March 30, 2026
---

# Akamai Account Protector IdP Adapter settings reference

Field descriptions for the Akamai Account Protector IdP Adapter configuration page.

> **Collapse: Standard fields**
>
> | Field Name             | Description                                                                                                                                                                                                                                                                                                                                                                                                                              |
> | ---------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
> | **Medium Limit**       | Scores less than or equal to the configured **Medium Limit** value are classified as `LOW` risk. For requests with a low risk score, the `level` core contract attribute is set to `low`.The default value is `25`.                                                                                                                                                                                                                      |
> | **High Limit**         | Scores greater than the configured **Medium Limit** and less than or equal to the configured **High Limit** value are classified as `MEDIUM` risk. For requests with a medium risk score, the `level` core contract attribute is set to `medium`.Scores exceeding the **High Limit** are classified as `HIGH` risk. For requests with a high risk score, the `level` core contract attribute is set to `high`.The default value is `50`. |
> | **Save Akamai Header** | If you select this checkbox, the adapter exposes any additional key and value pairs it parses from the Akamai Account Protector header as adapter attributes.&#xA;&#xA;The adapter provides the score and level core contract attributes regardless of whether this checkbox is selected.This checkbox is cleared by default.                                                                                                            |

> **Collapse: Advanced fields**
>
> | Field Name                               | Description                                                                                |
> | ---------------------------------------- | ------------------------------------------------------------------------------------------ |
> | **Akamai Account Protector Header Name** | The Akamai Account Protector HTTP header to parse.The default value is `Akamai-User-Risk`. |
