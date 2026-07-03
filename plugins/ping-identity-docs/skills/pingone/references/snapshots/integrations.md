---
title: Adding a RADIUS gateway
description: Add a RADIUS gateway to allow PingOne to communicate with your RADIUS clients.
component: pingone
page_id: pingone:integrations:p1_add_radius_gateway
canonical_url: https://docs.pingidentity.com/pingone/integrations/p1_add_radius_gateway.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: August 22, 2024
section_ids:
  steps: Steps
  result: Result:
  next-steps: Next steps
---

# Adding a RADIUS gateway

Add a RADIUS gateway to allow PingOne to communicate with your RADIUS clients.

## Steps

1. Go to **Integrations → Gateways**.

2. Click the **[icon: plus, set=fa]**icon.

3. Enter the following and click **Next**:

   * **Name**: A name for the gateway. The name must be unique within the environment.

   * **Gateway Type**: Select **RADIUS**.

   * **Description** (optional): A brief description of the gateway.

4. **Optional:** In the **Authentication Port** field, enter the relevant port number. The default is 1812.

   |   |                                                                                      |
   | - | ------------------------------------------------------------------------------------ |
   |   | You must stop all active gateway instances before modifying the authentication port. |

5. In the **DaVinci Policy ID** field, select the DaVinci Policy ID that you want to apply to the RADIUS gateway.

6. If you want to define a **Default Shared Secret**, enter it here.

   If no default is defined, you must enter a **Client Shared-Secret** for each **Client IP address** that you add.

   |   |                                                                                 |
   | - | ------------------------------------------------------------------------------- |
   |   | For security reasons, you should rotate the shared secret at least once a year. |

7. **Optional:** To incorporate a Network Policy Server (NPS), configure the following settings:

   1. Select the **Use RADIUS Remote Network Policy Server** check box.

   2. Enter the relevant NPS **Server IP** and **Server port**.

      |   |                                                                                                                                                                                                               |
      | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
      |   | Because validation of the client IP shared secret is performed on the RADIUS gateway side and the NPS side, you must make sure the shared secret on the client matches the shared secret on the endpoint NPS. |

8. In the **RADIUS clients** area, for each client that you want to add:

   1. Click **Add Client**.

   2. In the new row, enter the **Client IP address** of the VPN server or remote access system and the **Client Shared Secret**.

      If the **Client Shared Secret** field is left empty, the **Default Shared Secret** is used.

   3. (Optional) To mitigate the risk of a Blast-RADIUS attack, select the **RADIUS Security Enhancement** checkbox and then select either:

      * **Require Message-Authenticator**: RADIUS gateway requires this attribute in every client request, and also includes it as the first attribute in every RADIUS response.

      * **Limit Proxy-State**: RADIUS Gateway ignores requests that contain one or more Proxy-State attribute if they do not include the **Message-Authenticator** attribute. This option should only be used for legacy clients that don't support sending the **Message-Authenticator** attribute and are not acting as a proxy client.

        |   |                                                                                                                                                                                                                                                                                                                                                                  |
        | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
        |   | Learn more about Blast RADIUS mitigations in the IETF article [Deprecating Insecure Practices in RADIUS](https://datatracker.ietf.org/doc/draft-ietf-radext-deprecating-radius/) and [RADIUS vulnerability CVE-2024-3596](https://support.pingidentity.com/s/article/RADIUS-Vulnerability-CVE-2024-3596) in the Ping Identity Knowledge Base (requires sign-on). |

9. Click **Save**.

   ### Result:

   The new gateway displays in the **Gateways** list. PingOne generates a gateway credential, which the gateway uses to authenticate with PingOne.

   |   |                                                                                                                                                                                                                                                                            |
   | - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | A gateway credential is like a password, so keep it protected. For security reasons, PingOne does not store the generated gateway credentials, but you can always create a new one in the PingOne console. Multiple gateway instances can use the same gateway credential. |

10. Copy the credential and paste it to a secure location.

    You'll use the credential later when starting a gateway instance.

11. **Optional:** Click **Show me the Docker command** and copy it to a secure location.

12. Click **Done**.

## Next steps

[Start a gateway instance](p1_starting_gateway_instance_radius.html)
