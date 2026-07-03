---
title: An improved index in the database table for OAuth clients
description: PingFederate 8.4 added the value column to an existing index (IDX_FIELD_NAME) in the pingfederate_oauth_clients_ext table as a general improvement.
component: pingfederate
version: 13.1
page_id: pingfederate:upgrading_pingfederate:pf_improv_index_datab_table_oauth_cli
canonical_url: https://docs.pingidentity.com/pingfederate/13.1/upgrading_pingfederate/pf_improv_index_datab_table_oauth_cli.html
llms_txt: https://docs.pingidentity.com/pingfederate/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 5, 2022
section_ids:
  related-links: Related links
---

# An improved index in the database table for OAuth clients

PingFederate 8.4 added the `value` column to an existing index (`IDX_FIELD_NAME`) in the `pingfederate_oauth_clients_ext` table as a general improvement.

This information is applicable only to customers who configured PingFederate to store OAuth clients on a database server.

You must modify the index in your existing `pingfederate_oauth_clients_ext` table.

Although there is no alter-table script provided, you can derive the setup from the new table-setup scripts in the `<pf_install>/pingfederate/server/default/conf/oauth-client-management/sql-scripts/oauth-client-management-<databaseServer>.sql` file.

|   |                                                                                                           |
| - | --------------------------------------------------------------------------------------------------------- |
|   | If your initial installation of PingFederate was version 8.4 or later, you don't need to run this script. |

## Related links

* [Configuring external databases for client storage](../administrators_reference_guide/pf_configuring_external_databases_client_storage.html).
