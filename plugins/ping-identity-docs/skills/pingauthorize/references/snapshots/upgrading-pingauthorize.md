---
title: Backing up policies
description: Back up Policy Editor policies before upgrading by exporting policy snapshots from Branch Manager.
component: pingauthorize
version: 11.1
page_id: pingauthorize:upgrading_pingauthorize:paz_back_up_policies
canonical_url: https://docs.pingidentity.com/pingauthorize/11.1/upgrading_pingauthorize/paz_back_up_policies.html
llms_txt: https://docs.pingidentity.com/pingauthorize/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 1, 2026
section_ids:
  about-this-task: About this task
  steps: Steps
  result: Result:
  result-2: Result:
---

# Backing up policies

Back up existing policies before upgrading the Policy Editor. Do this by exporting policy snapshots.

## About this task

Back up policies manually as described below or rely on the automatic backups covered in [Policy database backups](../pingauthorize_server_administration_guide/paz_policy_db_backups.html).

## Steps

1. Sign on to the Policy Editor and choose any existing branch to go to the main landing page.

2. To display your current branches, select Branch Manager → Version Control.

3. From the Branches list, click a branch that you want to export.

   ### Result:

   You should see a list of the commits for that branch, and the most recent version of the branch is named Uncommitted Changes.

4. Identify the commit that represents the snapshot that you want to export and click the hamburger menu in the Options column.

5. Choose Export Snapshot.

   ### Result:

   Your browser downloads the file.

6. Repeat for any additional branches that you want to back up.
