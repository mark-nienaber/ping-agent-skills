---
title: Create a read policy
description: In the PingOne Privilege admin console, click the admin name and select Settings in the list.
component: privilege
page_id: privilege:procyonreadpolicy:create-read-policy
canonical_url: https://docs.pingidentity.com/privilege/procyonreadpolicy/create-read-policy.html
llms_txt: https://docs.pingidentity.com/privilege/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
---

# Create a read policy

1. In the PingOne Privilege admin console, click the admin name and select Settings in the list.

2. On the Read Policy tab, click Add New to open the Create Policy modal.

   ![procyonreadpolicy 4](_images/procyonreadpolicy-4.png)

3. Complete the form by entering:

   * Read Policy Name

   * Key

   * Value

   * Resource Type (matching the entries from the tag policy)

4. Select the non-admin users in the Add Reader section for whom the policy applies.

5. Click Create to activate the policy.

   ![procyonreadpolicy 5](_images/procyonreadpolicy-5.png)

---

---
title: Create a tag policy
description: In the PingOne Privilege admin console, click the admin name and select Settings in the list.
component: privilege
page_id: privilege:procyonreadpolicy:create-tag-policy
canonical_url: https://docs.pingidentity.com/privilege/procyonreadpolicy/create-tag-policy.html
llms_txt: https://docs.pingidentity.com/privilege/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
---

# Create a tag policy

1. In the PingOne Privilege admin console, click the admin name and select Settings in the list.

2. On the Tag Policy tab, click Add New to open the Create Tag modal.

   ![procyonreadpolicy 2](_images/procyonreadpolicy-2.png)

3. Fill out the modal form with the following details:

   * Tag Policy Name

   * RegEx Pattern

   * Resource Types

   * Custom Tags

     |   |                                                                                                 |
     | - | ----------------------------------------------------------------------------------------------- |
     |   | For a read policy, select the Read Group custom tag option and enter the relevant custom value. |

4. Click Create to activate the policy.

   ![procyonreadpolicy 3](_images/procyonreadpolicy-3.png)

---

---
title: Enable LimitRead
description: "The PingOne Privilege Team will assist in setting the \"LimitRead\" key to 'true' for the specified tenant. After this is enabled, non-admin users will be restricted from viewing any resources in their profiles."
component: privilege
page_id: privilege:procyonreadpolicy:enable-limitread
canonical_url: https://docs.pingidentity.com/privilege/procyonreadpolicy/enable-limitread.html
llms_txt: https://docs.pingidentity.com/privilege/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  step-1: Step 1
---

# Enable LimitRead

## Step 1

The PingOne Privilege Team will assist in setting the "LimitRead" key to 'true' for the specified tenant. After this is enabled, non-admin users will be restricted from viewing any resources in their profiles.

![procyonreadpolicy 1](_images/procyonreadpolicy-1.png)

---

---
title: Visibility of resources
description: The selected non-admin users will now be able to view all resources that match the regex pattern defined earlier.
component: privilege
page_id: privilege:procyonreadpolicy:visibility-of-resources
canonical_url: https://docs.pingidentity.com/privilege/procyonreadpolicy/visibility-of-resources.html
llms_txt: https://docs.pingidentity.com/privilege/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
---

# Visibility of resources

The selected non-admin users will now be able to view all resources that match the regex pattern defined earlier.

![procyonreadpolicy 6](_images/procyonreadpolicy-6.png)