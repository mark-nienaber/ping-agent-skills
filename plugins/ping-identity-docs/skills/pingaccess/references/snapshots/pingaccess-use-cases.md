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

---

---
title: Configuring a resource
description: An application resource is a component within an application that requires a different level of security. By configuring resources for your API endpoints, you can add different rules for different endpoints and specify which methods are allowed.
component: pingaccess
version: 9.1
page_id: pingaccess:pingaccess_use_cases:pa_api_gateway_configuring_a_resource
canonical_url: https://docs.pingidentity.com/pingaccess/9.1/pingaccess_use_cases/pa_api_gateway_configuring_a_resource.html
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

---

---
title: Configuring a resource
description: An application resource is a component within an application that requires a different level of security. By configuring resources for your API endpoints, you can add different rules for different endpoints and specify which methods are allowed.
component: pingaccess
version: 9.1
page_id: pingaccess:pingaccess_use_cases:pa_api_sideband_configuring_a_resource
canonical_url: https://docs.pingidentity.com/pingaccess/9.1/pingaccess_use_cases/pa_api_sideband_configuring_a_resource.html
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

---

---
title: Configuring a rule
description: Rules are used to control the circumstances under which users can access the protected API. Rules can grant or deny access based on criteria such as user parameters from the token provider, header values, network ranges, or web session attributes. You can configure any number of rules in your environment.
component: pingaccess
version: 9.1
page_id: pingaccess:pingaccess_use_cases:pa_api_agent_configuring_a_rule
canonical_url: https://docs.pingidentity.com/pingaccess/9.1/pingaccess_use_cases/pa_api_agent_configuring_a_rule.html
llms_txt: https://docs.pingidentity.com/pingaccess/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: February 6, 2023
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Configuring a rule

## About this task

Rules are used to control the circumstances under which users can access the protected API. Rules can grant or deny access based on criteria such as user parameters from the token provider, header values, network ranges, or web session attributes. You can configure any number of rules in your environment.

You can combine rules into rule sets, which combine multiple rules. You can configure rule sets to allow access to a resource if at least one rule's criteria is met, or to only allow access if all rules have their criteria met. Access control rules are processed before processing rules. Each type of rule is otherwise processed in the order you specify when you create the rule set.

You can further combine rule sets into rule set groups, which combine multiple rule sets. As with rule sets, rule set groups can allow access if any one rule set's criteria are met, or only if all rule sets' criteria are met. Rule sets are processed in the order you specify when you create the rule set group.

This example uses an HTTP request *(tooltip: \<div class="paragraph">
\<p>A client transaction sent over HTTP to the server specifying a request method, such as GET, POST, and DELETE, to execute against a resource or resources on the server.\</p>
\</div>)* header rule to demonstrate how rules are created and used. Each environment has different requirements, and you can use any of the rules explained in the [Rule management](../pingaccess_user_interface_reference_guide/pa_rule_management.html) section according to your needs.

## Steps

1. Click **Access**, then go to **Rules > Rules**.

2. Click **[icon: plus, set=fa]Add Rule**.

3. In the **Name** field, enter a unique name. The name can be up to 64 characters long. Special characters and spaces are allowed.

4. From the **Type** menu, select **HTTP Request Header**.

5. In the **Field** column, in the **Header** field, enter the HTTP header *(tooltip: \<div class="paragraph">
   \<p>A section of an HTTP request or response that conveys additional information relevant to the client or server in the transaction.\</p>
   \</div>)* name you want to match in order to grant or not grant the client access.

6. In the **Value** field, enter the values for the header you want to match in order to grant or not grant the client access. The wildcard (`*`) character is supported.

   |   |                                                                                                                                                                                                     |
   | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | If you want to match on the `Host` header, include both the host and port in the **Value** field, or add a wildcard after the host name (`host*` or `host:*`) to match what is in the HTTP request. |

7. If you need additional header pairs, click **Add Row** to add an additional row, then repeat steps 5-6.

8. Click **Save**.

---

---
title: Configuring a rule
description: Rules are used to control the circumstances under which users can access the protected API. Rules can grant or deny access based on criteria such as user parameters from the token provider, header values, network ranges, or web session attributes. You can configure any number of rules in your environment.
component: pingaccess
version: 9.1
page_id: pingaccess:pingaccess_use_cases:pa_api_gateway_configuring_a_rule
canonical_url: https://docs.pingidentity.com/pingaccess/9.1/pingaccess_use_cases/pa_api_gateway_configuring_a_rule.html
llms_txt: https://docs.pingidentity.com/pingaccess/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: February 6, 2023
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Configuring a rule

## About this task

Rules are used to control the circumstances under which users can access the protected API. Rules can grant or deny access based on criteria such as user parameters from the token provider, header values, network ranges, or web session attributes. You can configure any number of rules in your environment.

You can combine rules into rule sets, which combine multiple rules. You can configure rule sets to allow access to a resource if at least one rule's criteria is met, or to only allow access if all rules have their criteria met. Access control rules are processed before processing rules. Each type of rule is otherwise processed in the order you specify when you create the rule set.

You can further combine rule sets into rule set groups, which combine multiple rule sets. As with rule sets, rule set groups can allow access if any one rule set's criteria are met, or only if all rule sets' criteria are met. Rule sets are processed in the order you specify when you create the rule set group.

This example uses an HTTP request *(tooltip: \<div class="paragraph">
\<p>A client transaction sent over HTTP to the server specifying a request method, such as GET, POST, and DELETE, to execute against a resource or resources on the server.\</p>
\</div>)* header rule to demonstrate how rules are created and used. Each environment has different requirements, and you can use any of the rules explained in the [Rule management](../pingaccess_user_interface_reference_guide/pa_rule_management.html) section according to your needs.

## Steps

1. Click **Access**, then go to **Rules > Rules**.

2. Click **[icon: plus, set=fa]Add Rule**.

3. In the **Name** field, enter a unique name. The name can be up to 64 characters long. Special characters and spaces are allowed.

4. From the **Type** menu, select **HTTP Request Header**.

5. In the **Field** column, in the **Header** field, enter the HTTP header *(tooltip: \<div class="paragraph">
   \<p>A section of an HTTP request or response that conveys additional information relevant to the client or server in the transaction.\</p>
   \</div>)* name you want to match in order to grant or not grant the client access.

6. In the **Value** field, enter the values for the header you want to match in order to grant or not grant the client access. The wildcard (`*`) character is supported.

   |   |                                                                                                                                                                                                     |
   | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | If you want to match on the `Host` header, include both the host and port in the **Value** field, or add a wildcard after the host name (`host*` or `host:*`) to match what is in the HTTP request. |

7. If you need additional header pairs, click **Add Row** to add an additional row, then repeat steps 5-6.

8. Click **Save**.

---

---
title: Configuring a rule
description: Rules are used to control the circumstances under which users can access the protected API. Rules can grant or deny access based on criteria such as user parameters from the token provider, header values, network ranges, or web session attributes. You can configure any number of rules in your environment.
component: pingaccess
version: 9.1
page_id: pingaccess:pingaccess_use_cases:pa_api_sideband_configuring_a_rule
canonical_url: https://docs.pingidentity.com/pingaccess/9.1/pingaccess_use_cases/pa_api_sideband_configuring_a_rule.html
llms_txt: https://docs.pingidentity.com/pingaccess/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: February 6, 2023
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Configuring a rule

## About this task

Rules are used to control the circumstances under which users can access the protected API. Rules can grant or deny access based on criteria such as user parameters from the token provider, header values, network ranges, or web session attributes. You can configure any number of rules in your environment.

You can combine rules into rule sets, which combine multiple rules. You can configure rule sets to allow access to a resource if at least one rule's criteria is met, or to only allow access if all rules have their criteria met. Access control rules are processed before processing rules. Each type of rule is otherwise processed in the order you specify when you create the rule set.

You can further combine rule sets into rule set groups, which combine multiple rule sets. As with rule sets, rule set groups can allow access if any one rule set's criteria are met, or only if all rule sets' criteria are met. Rule sets are processed in the order you specify when you create the rule set group.

This example uses an HTTP request *(tooltip: \<div class="paragraph">
\<p>A client transaction sent over HTTP to the server specifying a request method, such as GET, POST, and DELETE, to execute against a resource or resources on the server.\</p>
\</div>)* header rule to demonstrate how rules are created and used. Each environment has different requirements, and you can use any of the rules explained in the [Rule management](../pingaccess_user_interface_reference_guide/pa_rule_management.html) section according to your needs.

## Steps

1. Click **Access**, then go to **Rules > Rules**.

2. Click **[icon: plus, set=fa]Add Rule**.

3. In the **Name** field, enter a unique name. The name can be up to 64 characters long. Special characters and spaces are allowed.

4. From the **Type** menu, select **HTTP Request Header**.

5. In the **Field** column, in the **Header** field, enter the HTTP header *(tooltip: \<div class="paragraph">
   \<p>A section of an HTTP request or response that conveys additional information relevant to the client or server in the transaction.\</p>
   \</div>)* name you want to match in order to grant or not grant the client access.

6. In the **Value** field, enter the values for the header you want to match in order to grant or not grant the client access. The wildcard (`*`) character is supported.

   |   |                                                                                                                                                                                                     |
   | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | If you want to match on the `Host` header, include both the host and port in the **Value** field, or add a wildcard after the host name (`host*` or `host:*`) to match what is in the HTTP request. |

7. If you need additional header pairs, click **Add Row** to add an additional row, then repeat steps 5-6.

8. Click **Save**.

---

---
title: Configuring a rule
description: Rules are used to control the circumstances under which users can access the protected web server. Rules can grant or deny access based on criteria such as user parameters from the token provider, header values, network ranges, or web session attributes. You can configure any number of rules in your environment.
component: pingaccess
version: 9.1
page_id: pingaccess:pingaccess_use_cases:pa_web_agent_configuring_a_rule
canonical_url: https://docs.pingidentity.com/pingaccess/9.1/pingaccess_use_cases/pa_web_agent_configuring_a_rule.html
llms_txt: https://docs.pingidentity.com/pingaccess/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: February 6, 2023
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Configuring a rule

## About this task

Rules are used to control the circumstances under which users can access the protected web server. Rules can grant or deny access based on criteria such as user parameters from the token provider, header values, network ranges, or web session attributes. You can configure any number of rules in your environment.

You can combine rules into rule sets, which combine multiple rules. You can configure rule sets to allow access to a resource if at least one rule's criteria is met, or to only allow access if all rules have their criteria met. Access control rules are processed before processing rules. Each type of rule is otherwise processed in the order you specify when you create the rule set.

You can further combine rule sets into rule set groups, which combine multiple rule sets. As with rule sets, rule set groups can allow access if any one rule set's criteria are met, or only if all rule sets' criteria are met. Rule sets are processed in the order you specify when you create the rule set group.

This example uses an HTTP request *(tooltip: \<div class="paragraph">
\<p>A client transaction sent over HTTP to the server specifying a request method, such as GET, POST, and DELETE, to execute against a resource or resources on the server.\</p>
\</div>)* header rule to demonstrate how rules are created and used. Each environment has different requirements, and you can use any of the rules explained in the [Rule management](../pingaccess_user_interface_reference_guide/pa_rule_management.html) section according to your needs.

## Steps

1. Click **Access**, then go to **Rules > Rules**.

2. Click **[icon: plus, set=fa]Add Rule**.

3. In the **Name** field, enter a unique name. The name can be up to 64 characters long. Special characters and spaces are allowed.

4. From the **Type** menu, select **HTTP Request Header**.

5. In the **Field** column, in the **Header** field, enter the HTTP header *(tooltip: \<div class="paragraph">
   \<p>A section of an HTTP request or response that conveys additional information relevant to the client or server in the transaction.\</p>
   \</div>)* name you want to match in order to grant or not grant the client access.

6. In the **Value** field, enter the values for the header you want to match in order to grant or not grant the client access. The wildcard (`*`) character is supported.

   |   |                                                                                                                                                                                                     |
   | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | If you want to match on the `Host` header, include both the host and port in the **Value** field, or add a wildcard after the host name (`host*` or `host:*`) to match what is in the HTTP request. |

7. If you need additional header pairs, click **Add Row** to add an additional row, then repeat steps 5-6.

8. Click **Save**.

---

---
title: Configuring a rule
description: Rules are used to control the circumstances under which users can access the protected web server. Rules can grant or deny access based on criteria such as user parameters from the token provider, header values, network ranges, or web session attributes. You can configure any number of rules in your environment.
component: pingaccess
version: 9.1
page_id: pingaccess:pingaccess_use_cases:pa_web_gateway_configuring_a_rule
canonical_url: https://docs.pingidentity.com/pingaccess/9.1/pingaccess_use_cases/pa_web_gateway_configuring_a_rule.html
llms_txt: https://docs.pingidentity.com/pingaccess/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: February 6, 2023
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Configuring a rule

## About this task

Rules are used to control the circumstances under which users can access the protected web server. Rules can grant or deny access based on criteria such as user parameters from the token provider, header values, network ranges, or web session attributes. You can configure any number of rules in your environment.

You can combine rules into rule sets, which combine multiple rules. You can configure rule sets to allow access to a resource if at least one rule's criteria is met or to only allow access if all rules have their criteria met. Access control rules are processed before processing rules. Each type of rule is otherwise processed in the order you specify when you create the rule set.

You can further combine rule sets into rule set groups, which combine multiple rule sets. As with rule sets, rule set groups can allow access if any one rule set's criteria are met or only if all rule sets' criteria are met. Rule sets are processed in the order you specify when you create the rule set group.

This example uses an HTTP request *(tooltip: \<div class="paragraph">
\<p>A client transaction sent over HTTP to the server specifying a request method, such as GET, POST, and DELETE, to execute against a resource or resources on the server.\</p>
\</div>)* header rule to demonstrate how rules are created and used. Each environment has different requirements, and you can use any of the rules explained in the [Rule management](../pingaccess_user_interface_reference_guide/pa_rule_management.html) section according to your needs.

## Steps

1. Click **Access**, then go to **Rules > Rules**.

2. Click **[icon: plus, set=fa]Add Rule**.

3. In the **Name** field, enter a unique name.

   The name can be up to 64 characters long. Special characters and spaces are allowed.

4. In the **Type** list, select **HTTP Request Header**.

5. In the **Field** column, in the **Header** field, enter the HTTP header *(tooltip: \<div class="paragraph">
   \<p>A section of an HTTP request or response that conveys additional information relevant to the client or server in the transaction.\</p>
   \</div>)* name you want to match in order to grant or not grant the client access.

6. In the **Value** field, enter the values for the header you want to match in order to grant or not grant the client access.

   The wildcard (`*`) character is supported.

   |   |                                                                                                                                                                                                    |
   | - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | If you want to match on the `Host` header, include both the host and port in the **Value** field, or add a wildcard after the host name (`host*` or `host:*`) to match what's in the HTTP request. |

7. If you need additional header pairs, click **Add Row** to add an additional row, then repeat steps 5-6.

8. Click **Save**.

---

---
title: Configuring a site
description: A site is only used in a proxy deployment. It contains the target address for the protected API and any other information necessary to access the application.
component: pingaccess
version: 9.1
page_id: pingaccess:pingaccess_use_cases:pa_api_gateway_configuring_a_site
canonical_url: https://docs.pingidentity.com/pingaccess/9.1/pingaccess_use_cases/pa_api_gateway_configuring_a_site.html
llms_txt: https://docs.pingidentity.com/pingaccess/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: February 6, 2023
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Configuring a site

## About this task

A site is only used in a proxy deployment. It contains the target address for the protected API and any other information necessary to access the application.

For more information about this procedure, including optional steps that are not included here, see [Adding sites](../pingaccess_user_interface_reference_guide/pa_adding_sites.html).

## Steps

1. Click **Applications**, then go to **Sites > Sites**.

2. Click **[icon: plus, set=fa]Add Site**.

3. In the **Site Name** field, enter a unique name of up to 64 characters, including special characters and spaces. This name is used internally.

4. In the **Targets** field, enter one or more targets.

   These targets are the actual locations of the site. The format for this is `hostname:port` or `IP address:port`. For example, `www.example.com:80`.

5. Select the **Secure** check box if the site is expecting HTTPS connections.

   |   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
   | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | This decision depends on whether the target expects an HTTPS connections from the PingAccess system to the protected web application.If you select **Secure**, you must also select a **Trusted Certificate Group** from the list, or select **Trust Any** to trust any certificate *(tooltip: \<div class="paragraph">&#xA;\<p>A digital file used for identity verification and other security purposes. The certificate, which is often issued by a CA, contains a public key, which can be used to verify the originator's identity.\</p>&#xA;\</div>)* presented by the listed targets. The trusted certificate group defines what certificates or issuing certificate authorities PingAccess will trust when acting as a client to the backend server. For information about importing a certificate and creating a trusted certificate group, see [Importing certificates](../pingaccess_user_interface_reference_guide/pa_importing_certificates.html) and [Creating trusted certificate groups](../pingaccess_user_interface_reference_guide/pa_creating_trusted_certificate_groups.html). |

6. Click **Save**.

   |   |                                                                                                                                                 |
   | - | ----------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | If the target site cannot be contacted, PingAccess saves the site and a displays a warning indicating the reason the site could not be reached. |

---

---
title: Configuring a site
description: A site is only used in a gateway deployment. It contains the target address for the protected web application and any other information necessary to access the application.
component: pingaccess
version: 9.1
page_id: pingaccess:pingaccess_use_cases:pa_web_gateway_configuring_a_site
canonical_url: https://docs.pingidentity.com/pingaccess/9.1/pingaccess_use_cases/pa_web_gateway_configuring_a_site.html
llms_txt: https://docs.pingidentity.com/pingaccess/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: February 6, 2023
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Configuring a site

## About this task

A site is only used in a gateway deployment. It contains the target address for the protected web application and any other information necessary to access the application.

For more information about this procedure, including optional steps that aren't included here, see [Adding sites](../pingaccess_user_interface_reference_guide/pa_adding_sites.html).

## Steps

1. Click **Applications**, then go to **Sites > Sites**.

2. Click **[icon: plus, set=fa]Add Site**.

3. In the **Site Name** field, enter a unique name of up to 64 characters, including special characters and spaces.

   This name is used internally.

4. In the **Targets** field, enter one or more targets.

   These targets are the actual locations of the site. The format for this is `hostname:port` or `IP address:port`, such as `www.example.com:80`.

5. Select the **Secure** check box if the site is expecting HTTPS connections.

   |   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
   | - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | This decision depends on whether the target expects an HTTPS connections from the PingAccess system to the protected web application.If you select **Secure**, you must also select a **Trusted Certificate Group** from the list, or select **Trust Any** to trust any certificate *(tooltip: \<div class="paragraph">&#xA;\<p>A digital file used for identity verification and other security purposes. The certificate, which is often issued by a CA, contains a public key, which can be used to verify the originator's identity.\</p>&#xA;\</div>)* presented by the listed targets. The trusted certificate group defines what certificates or issuing certificate authorities PingAccess will trust when acting as a client to the backend server.For information about importing a certificate and creating a trusted certificate group, see [Importing certificates](../pingaccess_user_interface_reference_guide/pa_importing_certificates.html) and [Creating trusted certificate groups](../pingaccess_user_interface_reference_guide/pa_creating_trusted_certificate_groups.html). |

6. Click **Save**.

   |   |                                                                                                                                             |
   | - | ------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | If the target site can't be contacted, PingAccess saves the site and displays a warning indicating the reason the site couldn't be reached. |

---

---
title: Configuring a virtual host
description: The virtual host is the external-facing portion of an API. In an agent deployment, the virtual host contains the actual host name and port for the protected API.
component: pingaccess
version: 9.1
page_id: pingaccess:pingaccess_use_cases:pa_api_agent_configuring_a_virtual_host
canonical_url: https://docs.pingidentity.com/pingaccess/9.1/pingaccess_use_cases/pa_api_agent_configuring_a_virtual_host.html
llms_txt: https://docs.pingidentity.com/pingaccess/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: February 6, 2023
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Configuring a virtual host

## About this task

The virtual host is the external-facing portion of an API. In an agent deployment, the virtual host contains the actual host name and port for the protected API.

For more information about this procedure, including optional steps that are not included here, see [Creating new virtual hosts](../pingaccess_user_interface_reference_guide/pa_creating_new_virtual_hosts.html).

## Steps

1. Click **Applications**, then go to **Applications > Virtual Hosts**.

2. Click **[icon: plus, set=fa]Add Virtual Host**.

3. In the **Host** field, enter the name for the virtual host.

   This is the host name of the protected API. For example, myHost.com. You can use a wildcard (`*`) for part or all of the host name. For example, `*.example.com` matches all host names ending in .example.com, and `*` matches all host names.

4. In the **Port** field, enter the port number for the virtual host. For example, `443`.

5. Click **Save**.

---

---
title: Configuring a virtual host
description: The virtual host is the external-facing portion of an API. In a proxy deployment, the virtual host contains the host name and port that your users use to reach the protected API.
component: pingaccess
version: 9.1
page_id: pingaccess:pingaccess_use_cases:pa_api_gateway_configuring_a_virtual_host
canonical_url: https://docs.pingidentity.com/pingaccess/9.1/pingaccess_use_cases/pa_api_gateway_configuring_a_virtual_host.html
llms_txt: https://docs.pingidentity.com/pingaccess/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: February 6, 2023
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Configuring a virtual host

## About this task

The virtual host is the external-facing portion of an API. In a proxy deployment, the virtual host contains the host name and port that your users use to reach the protected API.

For more information about this procedure, including optional steps that are not included here, see [Creating new virtual hosts](../pingaccess_user_interface_reference_guide/pa_creating_new_virtual_hosts.html).

## Steps

1. Click **Applications**, then go to **Applications > Virtual Hosts**.

2. Click **[icon: plus, set=fa]Add Virtual Host**.

3. In the **Host** field, enter the name for the virtual host.

   This is the host name used by end users to reach the site. For example, myHost.com. You can use a wildcard (`*`) for part or all of the host name. For example, `*.example.com` matches all host names ending in .example.com, and `*` matches all host names.

4. In the **Port** field, enter the port number for the virtual host. For example, `443`.

5. Click **Save**.

---

---
title: Configuring a virtual host
description: The virtual host is the external-facing portion of an API. In a sideband deployment, the virtual host contains the actual host name and port for the protected API.
component: pingaccess
version: 9.1
page_id: pingaccess:pingaccess_use_cases:pa_api_sideband_configuring_a_virtual_host
canonical_url: https://docs.pingidentity.com/pingaccess/9.1/pingaccess_use_cases/pa_api_sideband_configuring_a_virtual_host.html
llms_txt: https://docs.pingidentity.com/pingaccess/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: February 6, 2023
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Configuring a virtual host

## About this task

The virtual host is the external-facing portion of an API. In a sideband deployment, the virtual host contains the actual host name and port for the protected API.

For more information about this procedure, including optional steps that are not included here, see [Creating new virtual hosts](../pingaccess_user_interface_reference_guide/pa_creating_new_virtual_hosts.html).

## Steps

1. Click **Applications**, then go to **Applications > Virtual Hosts**.

2. Click **[icon: plus, set=fa]Add Virtual Host**.

3. In the **Host** field, enter the name for the virtual host.

   This is the host name of the protected API. For example, myHost.com. You can use a wildcard (`*`) for part or all of the host name. For example, `*.example.com` matches all host names ending in .example.com, and `*` matches all host names.

4. In the **Port** field, enter the port number for the virtual host. For example, `443`.

5. Click **Save**.

---

---
title: Configuring a virtual host
description: The virtual host is the external-facing portion of a web application. In an agent deployment, the virtual host contains the actual host name and port for the protected web application.
component: pingaccess
version: 9.1
page_id: pingaccess:pingaccess_use_cases:pa_web_agent_configuring_a_virtual_host
canonical_url: https://docs.pingidentity.com/pingaccess/9.1/pingaccess_use_cases/pa_web_agent_configuring_a_virtual_host.html
llms_txt: https://docs.pingidentity.com/pingaccess/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: February 6, 2023
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Configuring a virtual host

## About this task

The virtual host is the external-facing portion of a web application. In an agent deployment, the virtual host contains the actual host name and port for the protected web application.

For more information about this procedure, including optional steps that are not included here, see [Creating new virtual hosts](../pingaccess_user_interface_reference_guide/pa_creating_new_virtual_hosts.html).

## Steps

1. Click **Applications**, then go to **Applications > Virtual Hosts**.

2. Click **[icon: plus, set=fa]Add Virtual Host**.

3. In the **Host** field, enter the name for the virtual host.

   This is the host name of the protected web application. For example, myHost.com. You can use a wildcard (`*`) for part or all of the host name. For example, `*.example.com` matches all host names ending in .example.com, and `*` matches all host names.

4. In the **Port** field, enter the port number for the virtual host. For example, `443`.

5. Click **Save**.

---

---
title: Configuring a virtual host
description: The virtual host is the external-facing portion of a web application. In a gateway deployment, the virtual host contains the host name and port that your users use to reach the protected web application.
component: pingaccess
version: 9.1
page_id: pingaccess:pingaccess_use_cases:pa_web_gateway_configuring_a_virtual_host
canonical_url: https://docs.pingidentity.com/pingaccess/9.1/pingaccess_use_cases/pa_web_gateway_configuring_a_virtual_host.html
llms_txt: https://docs.pingidentity.com/pingaccess/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: February 6, 2023
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Configuring a virtual host

## About this task

The virtual host is the external-facing portion of a web application. In a gateway deployment, the virtual host contains the host name and port that your users use to reach the protected web application.

For more information about this procedure, including optional steps that aren't included here, see [Creating new virtual hosts](../pingaccess_user_interface_reference_guide/pa_creating_new_virtual_hosts.html).

## Steps

1. Click **Applications**, then go to **Applications > Virtual Hosts**.

2. Click **[icon: plus, set=fa]Add Virtual Host**.

3. In the **Host** field, enter the name for the virtual host.

   This is the host name used by end users to reach the site, such as `myHost.com`.

   |   |                                                                                                                                                                            |
   | - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | You can use a wildcard (`*`) for part or all of the host name. For example, `*.example.com` matches all host names ending in .example.com, and `*` matches all host names. |

4. In the **Port** field, enter the port number for the virtual host, such as `443`.

5. Click **Save**.

---

---
title: Configuring a web session
description: A web session specifies the details of how user information is stored.
component: pingaccess
version: 9.1
page_id: pingaccess:pingaccess_use_cases:pa_web_agent_configuring_a_web_session
canonical_url: https://docs.pingidentity.com/pingaccess/9.1/pingaccess_use_cases/pa_web_agent_configuring_a_web_session.html
llms_txt: https://docs.pingidentity.com/pingaccess/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: May 10, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
  choose-from: Choose from:
  choose-from-2: Choose from:
---

# Configuring a web session

## About this task

A web session specifies the details of how user information is stored.

For more information about this procedure, including optional steps that are not included here, see [Creating web sessions](../pingaccess_user_interface_reference_guide/pa_creating_web_sessions.html).

## Steps

1. Click **Access**, then go to **Web Sessions > Web Sessions**.

2. Click **[icon: plus, set=fa]Add Web Session**.

3. In the **Name** field, enter a unique name for the web session, up to 64 characters, including special characters and spaces.

4. From the **Cookie Type** list, select **Encrypted JWT**.

5. In the **Audience** field, enter the audience that the PA token is applicable to, represented as a short, unique identifier between one and 32 characters.

   |   |                                                                                                                                                                      |
   | - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | PingAccess rejects requests that contain a PA token with an audience that differs from what is configured in the web session associated with the target application. |

6. From the **OpenID Connect Login Type** list, select **Code**.

   |   |                                                                                                                                                                                                                                                                                        |
   | - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | The **Code** login type is recommended for maximum security and standards interoperability, but other options are available. Learn more about the available profiles in step 6 of [Creating web sessions](../pingaccess_user_interface_reference_guide/pa_creating_web_sessions.html). |

7. In the **Client ID** field, enter the unique identifier (client ID) that was assigned when you created the OAuth *(tooltip: \<div class="paragraph">
   \<p>A standard framework that enables an application (OAuth client) to obtain access tokens from an OAuth authorization server for the purpose of retrieving protected resources on a resource server.\</p>
   \</div>)* relying party (RP) *(tooltip: \<div class="paragraph">
   \<p>An OAuth 2.0 client that requires end-user's authenticity and claims (attributes) from an OpenID provider.\</p>
   \</div>)* client within the token provider (for more information, see [Configuring OAuth clients](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_configuring_oauth_clients.html) in the PingFederate documentation).

8. Select a **Client Credentials Type**. This is required when configuring the **Code** login type.

   ### Choose from:

   * **Secret**

   * **Mutual TLS**

   * **Private Key JWT**

   |   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
   | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | The OAuth client you use with PingAccess web sessions must have an OpenID Connect (OIDC) *(tooltip: \<div class="paragraph">&#xA;\<p>An authentication protocol built on top of OAuth that authenticates users and enables clients (relying parties) of all types to request and receive information about authenticated sessions and users. OIDC is extensible, allowing clients to use optional features such as encryption of identity data, discovery of OpenID Providers (OAuth authorization servers), and session management.\</p>&#xA;\</div>)* policy specified (for more information see [Configuring OpenID Connect Policies](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_configuring_oidc_policies.html). |

9. Provide the information required for the selected credential type.

   ### Choose from:

   * **Secret** – Enter the **Client Secret** assigned when you created the OAuth relying party client in the token provider.

   * **Mutual TLS** – Select a configured **Key Pair** to use for Mutual TLS client authentication.

   * **Private Key JWT** – No additional information is required.

10. In the **Idle Timeout** field, specify the amount of time, in minutes, that the PA token remains active when no activity is detected by the user (the default is `60` minutes).

    |   |                                                                                                                                                                                            |
    | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
    |   | If there is an existing valid PingFederate session for the user, an idle timeout of the PingAccess session might result in its re-establishment without forcing the user to sign on again. |

11. In the **Max Timeout** field, specify the amount of time, in minutes, that the PA token remains active before expiring (the default is `240` minutes).

12. Click **Save**.

---

---
title: Configuring a web session
description: A web session specifies the details of how user information is stored.
component: pingaccess
version: 9.1
page_id: pingaccess:pingaccess_use_cases:pa_web_gateway_configuring_a_web_session
canonical_url: https://docs.pingidentity.com/pingaccess/9.1/pingaccess_use_cases/pa_web_gateway_configuring_a_web_session.html
llms_txt: https://docs.pingidentity.com/pingaccess/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: May 10, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
  choose-from: Choose from:
  choose-from-2: Choose from:
---

# Configuring a web session

## About this task

A web session specifies the details of how user information is stored.

For more information about this procedure, including optional steps that aren't included here, see [Creating web sessions](../pingaccess_user_interface_reference_guide/pa_creating_web_sessions.html).

## Steps

1. Click **Access**, then go to **Web Sessions > Web Sessions**.

2. Click **[icon: plus, set=fa]Add Web Session**.

3. In the **Name** field, enter a unique name for the web session, up to 64 characters, including special characters and spaces.

4. In the **Cookie Type** list, select **Encrypted JWT**.

5. In the **Audience** field, enter the audience that the PingAccess token is applicable to, represented as a short, unique identifier between 1 and 32 characters.

   |   |                                                                                                                                                                              |
   | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | PingAccess rejects requests that contain a PingAccess token with an audience that differs from what is configured in the web session associated with the target application. |

6. In the **OpenID Connect Login Type** list, select **Code**.

   |   |                                                                                                                                                                                                                                                                                        |
   | - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | The **Code** login type is recommended for maximum security and standards interoperability, but other options are available. Learn more about the available profiles in step 6 of [Creating web sessions](../pingaccess_user_interface_reference_guide/pa_creating_web_sessions.html). |

7. In the **Client ID** field, enter the unique identifier (client ID) that was assigned when you created the OAuth *(tooltip: \<div class="paragraph">
   \<p>A standard framework that enables an application (OAuth client) to obtain access tokens from an OAuth authorization server for the purpose of retrieving protected resources on a resource server.\</p>
   \</div>)* relying party (RP) *(tooltip: \<div class="paragraph">
   \<p>An OAuth 2.0 client that requires end-user's authenticity and claims (attributes) from an OpenID provider.\</p>
   \</div>)* client within the token provider.

   Learn more in [Configuring OAuth clients](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_configuring_oauth_clients.html) in the PingFederate documentation.

8. In the **Client Credentials Type** list, select a client credentials type.

   Selecting a client credentials type is required when configuring the **Code** login type.

   ### Choose from:

   * **Secret**

   * **Mutual TLS**

   * **Private Key JWT**

     |   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
     | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
     |   | The OAuth client you use with PingAccess web sessions must have an OpenID Connect (OIDC) *(tooltip: \<div class="paragraph">&#xA;\<p>An authentication protocol built on top of OAuth that authenticates users and enables clients (relying parties) of all types to request and receive information about authenticated sessions and users. OIDC is extensible, allowing clients to use optional features such as encryption of identity data, discovery of OpenID Providers (OAuth authorization servers), and session management.\</p>&#xA;\</div>)* policy specified.Learn more in [Configuring OpenID Connect Policies](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_configuring_oidc_policies.html). |

9. Provide the information required for the selected credential type.

   ### Choose from:

   * **Secret** – Enter the **Client Secret** assigned when you created the OAuth relying party client in the token provider.

   * **Mutual TLS** – Select a configured **Key Pair** to use for Mutual TLS client authentication.

   * **Private Key JWT** – No additional information is required.

10. In the **Idle Timeout** field, specify the amount of time, in minutes, that the PingAccess token remains active when no activity is detected by the user.

    The default is `60` minutes.

    |   |                                                                                                                                                                                            |
    | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
    |   | If there is an existing valid PingFederate session for the user, an idle timeout of the PingAccess session might result in its re-establishment without forcing the user to sign on again. |

11. In the **Max Timeout** field, specify the amount of time, in minutes, that the PingAccess token remains active before expiring.

    The default is `240` minutes.

12. Click **Save**.

---

---
title: Configuring an application
description: The application represents the protected API as a whole. By including the virtual host and the agent, it allows PingAccess to route requests directed at the front-end name to the correct back-end resource. After you create the application and its root resource, you can add one or more rules to control access to the protected API.
component: pingaccess
version: 9.1
page_id: pingaccess:pingaccess_use_cases:pa_api_agent_configuring_an_app
canonical_url: https://docs.pingidentity.com/pingaccess/9.1/pingaccess_use_cases/pa_api_agent_configuring_an_app.html
llms_txt: https://docs.pingidentity.com/pingaccess/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: February 6, 2023
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Configuring an application

## About this task

The application represents the protected API as a whole. By including the virtual host and the agent, it allows PingAccess to route requests directed at the front-end name to the correct back-end resource. After you create the application and its root resource, you can add one or more rules to control access to the protected API.

Within the application, you can add one or more resources. Resources are specific components that require a different degree of security. You can apply different rules to a resource, letting you apply specific controls to portions of an application. This example procedure does not include resources. For information about adding resources to an application, see [Configuring resource ordering in PingAccess](../pingaccess_user_interface_reference_guide/pa_configuring_resource_ordering.html).

For more information about this procedure, including optional steps that are not included here, see [Adding an application](../pingaccess_user_interface_reference_guide/pa_adding_an_app.html).

## Steps

1. Click **Applications**, then go to **Applications > Applications**.

2. Click **[icon: plus, set=fa]Add Application**.

3. In the **Name** field, enter a unique name for the application, up to 64 characters, including special characters and spaces.

4. In the **Context Root** field, enter the context root for the API. This represents the context at which all of the API endpoints are accessed at the site.

   The context root must meet the following criteria:

   * It must start with `/`.

   * It can contain additional `/` path separators.

   * It must not end with `/`.

   * It must not contain wildcards or regular expression strings.

   * The combination of the **Virtual Host** and **Context Root** must be unique.

5. From the **Virtual Host** list, select the virtual host you created.

6. In the **Application Type** section, select **API**.

7. In the **Destination** section, select **Agent**, then select the agent that is installed on the same web server as the API.

8. Click **Save**.

9. Click **Applications**, then go to **Applications > Applications**.

10. Expand the new application in the list and click the pencil icon ![pin1564006721753](_images/pin1564006721753.jpg).

11. Click the **Web Policy** tab.

12. Drag your rule from **Available Rules** onto the policy bar.

13. Click **Save**.

---

---
title: Configuring an application
description: The application represents the protected API as a whole. By including the virtual host and the site, it allows PingAccess to route requests directed at the front-end name to the correct back-end resource. After you create the application and its root resource, you can add one or more rules to control access to the protected API.
component: pingaccess
version: 9.1
page_id: pingaccess:pingaccess_use_cases:pa_api_gateway_configuring_an_app
canonical_url: https://docs.pingidentity.com/pingaccess/9.1/pingaccess_use_cases/pa_api_gateway_configuring_an_app.html
llms_txt: https://docs.pingidentity.com/pingaccess/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: February 6, 2023
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Configuring an application

## About this task

The application represents the protected API as a whole. By including the virtual host and the site, it allows PingAccess to route requests directed at the front-end name to the correct back-end resource. After you create the application and its root resource, you can add one or more rules to control access to the protected API.

Within the application, you can add one or more resources. Resources are specific components that require a different degree of security. You can apply different rules to a resource, letting you apply specific controls to portions of an application. This example procedure does not include resources. For information about adding resources to an application, see [Configuring resource ordering in PingAccess](../pingaccess_user_interface_reference_guide/pa_configuring_resource_ordering.html).

For more information about this procedure, including optional steps that are not included here, see [Adding an application](../pingaccess_user_interface_reference_guide/pa_adding_an_app.html).

## Steps

1. Click **Applications**, then go to **Applications > Applications**.

2. Click **[icon: plus, set=fa]Add Application**.

3. In the **Name** field, enter a unique name for the application, up to 64 characters, including special characters and spaces.

4. In the **Context Root** field, enter the context root for the API. This represents the context at which all of the API endpoints are accessed at the site.

   The context root must meet the following criteria:

   * It must start with `/`.

   * It can contain additional `/` path separators.

   * It must not end with `/`.

   * It must not contain wildcards or regular expression strings.

   * The combination of the **Virtual Host** and **Context Root** must be unique.

5. From the **Virtual Host** list, select the virtual host you created.

6. In the **Application Type** section, select **API**.

7. In the **Destination** section, select **Site**, then select the site you created.

8. Click **Save**.

9. Click **Applications**, then go to **Applications > Applications**.

10. Expand the new application in the list and click the pencil icon ![pin1564006721753](_images/pin1564006721753.jpg).

11. Click the **Web Policy** tab.

12. Drag your rule from **Available Rules** onto the policy bar.

13. Click **Save**.

---

---
title: Configuring an application
description: The application represents the protected API as a whole, including the virtual host, sideband client, and rules. By including the virtual host and sideband client, it allows PingAccess to route requests directed at the front-end name to the correct back-end resource. After you create the application and its root resource, you can add one or more rules to control access to the protected API.
component: pingaccess
version: 9.1
page_id: pingaccess:pingaccess_use_cases:pa_api_sideband_configuring_an_app
canonical_url: https://docs.pingidentity.com/pingaccess/9.1/pingaccess_use_cases/pa_api_sideband_configuring_an_app.html
llms_txt: https://docs.pingidentity.com/pingaccess/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: February 6, 2023
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Configuring an application

## About this task

The application represents the protected API as a whole, including the virtual host, sideband client, and rules. By including the virtual host and sideband client, it allows PingAccess to route requests directed at the front-end name to the correct back-end resource. After you create the application and its root resource, you can add one or more rules to control access to the protected API.

Within the application, you can add one or more resources. Resources are specific components that require a different degree of security. You can apply different rules to a resource, letting you apply specific controls to portions of an application. This example procedure does not include resources. For information about adding resources to an application, see [Configuring resource ordering in PingAccess](../pingaccess_user_interface_reference_guide/pa_configuring_resource_ordering.html).

For more information about this procedure, including optional steps that are not included here, see [Adding an application](../pingaccess_user_interface_reference_guide/pa_adding_an_app.html).

## Steps

1. Click **Applications**, then go to **Applications > Applications**.

2. Click **[icon: plus, set=fa]Add Application**.

3. In the **Name** field, enter a unique name for the application, up to 64 characters, including special characters and spaces.

4. In the **Context Root** field, enter the context root for the API. This represents the context at which all of the API endpoints are accessed at the site.

   The context root must meet the following criteria:

   * It must start with `/`.

   * It can contain additional `/` path separators.

   * It must not end with `/`.

   * It must not contain wildcards or regular expression strings.

   * The combination of the **Virtual Host** and **Context Root** must be unique.

5. From the **Virtual Host** list, select the virtual host you created.

6. In the **Application Type** section, select **API**.

7. In the **Destination** section, select **Sideband**, then select the client that is installed on the API gateway.

8. Click **Save**.

9. Click **Applications**, then go to **Applications > Applications**.

10. Expand the new application in the list and click the pencil icon ![pin1564006721753](_images/pin1564006721753.jpg).

11. Click the **Web Policy** tab.

12. Drag your rule from **Available Rules** onto the policy bar.

13. Click **Save**.