---
title: Configuring a resource
description: An application resource is a component within an application that requires a different level of security. By configuring resources for your API endpoints, you can add different rules for different endpoints and specify which methods are allowed.
component: pingaccess
version: 9.1
page_id: pingaccess:pingaccess_use_cases:pa_api_agent_configuring_a_resource
canonical_url: https://docs.pingidentity.com/pingaccess/9.1/pingaccess_use_cases/pa_api_agent_configuring_a_resource.html
llms_txt: https://docs.pingidentity.com/pingaccess/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: February 6, 2023
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Configuring a resource

## About this task

An application resource is a component within an application that requires a different level of security. By configuring resources for your API endpoints, you can add different rules for different endpoints and specify which methods are allowed.

For more information about this procedure, including optional steps that are not included here, see [Adding application resources](../pingaccess_user_interface_reference_guide/pa_adding_application_resources.html).

## Steps

1. Click **Applications**, then go to **Applications > Applications**.

2. Click to expand the application you created in the previous procedure.

3. Click the **Pencil** icon.

4. Click the **Resources** tab.

5. Click **[icon: plus, set=fa]Add Resource**.

6. In the **Name** field, enter a unique name up to 64 characters, including special characters and spaces.

7. In the **Path Patterns** field, enter a list of Uniform Resource Locator (URL) *(tooltip: \<div class="paragraph">
   \<p>Identifies a resource according to its internet location.\</p>
   \</div>)* path patterns, within the context root, that identify this resource.

   |   |                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
   | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | The path pattern must start with a forward slash (/). It begins after the application context root and extends to the end of the URL.When automatic path pattern evaluation ordering is in use (default), patterns can contain one or more wildcard characters (`*`). No use of wildcards is assumed. For example, there is a difference between `/app/` and `/app/*`. If a request matches more than one resource, the most specific match is used. |

8. In the **Resource Authentication** section, select **Standard**, using the same authentication for the resource as for the root application.

9. In the **Methods** field, enter the methods supported by the resource.

   Leave the asterisk default if the resource supports all HTTP methods, including custom methods.

   |   |                                                                                                                                                                                                                                                                                         |
   | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | Defining methods for a resource allows more fine-grained access control policies on API resources. If you have a server optimized for writing data (POST, PUT) and a server optimized for reading data (GET), you might want to segment traffic based on the operation being performed. |

10. To log information about the transaction to the audit store, select the **Audit** check box.

11. To enable the resource, select the **Enabled** check box.

12. Click **Save**.
