---
title: Getting started with Ping CLI and PingOne
description: Connecting Ping CLI to PingOne for interactive sign-on means the CLI runs with the same role permissions as the signed-in user, the same permissions the user has in the PingOne admin console. Environment administrators control who can sign on and can require MFA, so access governance applies equally to the CLI. All actions are audited under the user's identity.
component: pingcli
version: 1.11
page_id: pingcli:pingone:getting-started
canonical_url: https://developer.pingidentity.com/pingcli/1.11/pingone/getting-started.html
llms_txt: https://developer.pingidentity.com/pingcli/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 25, 2026
section_ids:
  before-you-begin: Before you begin
  step-1-create-a-pingone-worker-application: "Step 1: Create a PingOne worker application"
  step-2-configure-ping-cli: "Step 2: Configure Ping CLI"
  create-a-new-cli-profile: Create a new CLI profile
  guided-initialization: Guided initialization
  sign-on: Sign on
  next-steps: Next steps
  learn-more: Learn more
---

# Getting started with Ping CLI and PingOne

Connecting Ping CLI to PingOne for interactive sign-on means the CLI runs with the same role permissions as the signed-in user, the same permissions the user has in the PingOne admin console. Environment administrators control who can sign on and can require MFA, so access governance applies equally to the CLI. All actions are audited under the user's identity.

|   |                                                                                                                                                                                                           |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | PingOne also supports the device code flow for headless environments, and client credentials for CI/CD pipelines. This guide covers interactive user sign-on using the authorization code flow with PKCE. |

Connect Ping CLI to PingOne in three steps: create an application in the PingOne admin console, configure Ping CLI with its credentials, and authenticate.

## Before you begin

* Ping CLI installed and available on your PATH. Refer to [Getting started](../using_pingcli/getting-started.html).

* A licensed or trial PingOne cloud subscription. [Try Ping Identity here](https://www.pingidentity.com/en/try-ping.html)

* Administrator access to the [PingOne admin console](https://docs.pingidentity.com/pingone/managing_your_pingone_user_profile/p1_signin.html)

## Step 1: Create a PingOne worker application

Before configuring Ping CLI, create an application in the PingOne admin console. The application type depends on which authentication flow you intend to use.

1. Sign on to your PingOne admin console.

2. Open an environment that contains admin users, typically the Administrators environment. Note that any environment can be used, but using the Administrators environment is recommended for management operations.

3. Navigate to the Applications link.

4. Add a new Application with the [icon: plus, set=fa]icon.

5. For Application Name and Description, enter a unique identifier for the application and a brief characterization of the application.

   > **Collapse: Expand Screenshot**
   >
   > ![PingOne admin console](_images/pingone-console-add-application.png)

6. Select Worker as the application type and click Save.

   Result: The worker application is created, and the Roles tab displays.

7. No roles should be granted to the application when CLI users log in interactively. When the user signs on to the Ping CLI using the created worker app, the CLI inherits the user's assigned roles instead of roles assigned to the application.

8. On the Configuration tab, click the edit icon to change the application's settings.

9. To allow users to sign on using the authorization code method:

   1. Set Response Type to Code.

   2. Set Grant Type to Authorization Code and Refresh Token (deselecting all others)

   3. For PKCE Enforcement, select S256_REQUIRED

   4. Refresh Token Duration, Refresh Token Rolling Duration and Refresh Token Rolling Grace Period can be left with default values, but can be changed as required.

   5. Add `http://127.0.0.1:7464/callback` to Redirect URIs

   6. Set Token Endpoint Authentication Method to None

      > **Collapse: Expand Screenshot**
      >
      > ![PingOne admin console](_images/pingone-console-edit-application-settings-auth-code.png)

10. Click the toggle to enable the application.

    > **Collapse: Expand Screenshot**
    >
    > ![PingOne admin console](_images/pingone-console-edit-application-header.png)

11. On the Overview tab, take note of the Client ID because it's needed when configuring Ping CLI.

## Step 2: Configure Ping CLI

The following steps configure Ping CLI to use the configured worker application in a new profile.

### Create a new CLI profile

Run the following command to create a new configuration profile within the CLI. For the profile name and profile description, enter a unique identifier for the profile and a brief characterization of the profile.

```shell
pingcli config profiles add
```

```text
New profile name: getting-started
New profile description: : A profile to use while getting started with Ping CLI
Set new profile as active: : y
```

### Guided initialization

Ping CLI includes a guided experience for connecting the PingOne platform.

1. Initialize the CLI for PingOne with the guided experience.

   ```shell
   pingcli pingone init
   ```

2. Use the arrow keys to select the Authorization Code option.

   ```text
   PingOne Authentication Setup
   ============================
   This will guide you through setting up authentication for PingOne.
   Select the OAuth grant type
   Use the arrow keys to navigate: ↓ ↑ → ←
   ? Authentication Method:
       Client Credentials (recommended for automation)
     ▸ Authorization Code (browser-based)
       Device Code (device flow)
   ```

3. When prompted, use arrow keys to select the root domain of the PingOne tenant (for example, `pingone.com`).

4. When prompted, copy and paste the environment ID for the worker application that was created earlier.

5. When prompted, copy and paste the client ID for the worker application that was created earlier.

6. Complete the guided initialization process.

   ```text
   ✔ PingOne authentication configured successfully!
   Run 'pingcli pingone auth login' to authenticate.
   ```

### Sign on

After initialization completes, sign on to the PingOne tenant.

```shell
pingcli pingone auth login
```

A browser window opens, allowing you to sign on to the PingOne tenant as an administrator, as usual.

After signing on, the browser window and Ping CLI confirm the successful sign on.

> **Collapse: Expand Screenshot**
>
> ![Ping CLI successful sign on callback page.  The page confirms successful authorization and prompts the user to close the browser window.](_images/pingone-console-sign-on-successful.png)

```text
✔ Successfully authenticated with authorization code
```

Ping CLI is now configured with the PingOne service. Try a command to view tenant configuration:

```shell
pingcli pingone environments list
```

```text
✔ Fetched 29 items
ID                                    NAME                                     DISPLAY NAME                             DESCRIPTION
9457b794-836e-493c-ade4-3a50c6cf877f  Administrators                           Administrators (PRODUCTION)              This is the administrator environmen...
...
```

## Next steps

[icon: sliders, set=fas, size=3x]

#### [Configure the CLI](../using_pingcli/configure-settings.html)

Set up multiple profiles, environment variables, and advanced configuration options.

[icon: cubes, set=fas, size=3x]

#### [Manage resources](../using_pingcli/managing-resources-overview.html)

Learn about the options available to manage resources within the PingOne tenant.

[icon: terminal, set=fas, size=3x]

#### [Command reference](../command_reference/pingcli_pingone.html)

Browse every PingOne command, subcommand, and flag available in Ping CLI.

## Learn more

* [pingcli config set](../command_reference/pingcli_config_set.html)

* [pingcli pingone auth login](../command_reference/pingcli_pingone_auth_login.html)

* [Configuration settings reference](../settings_reference/configuration-settings-reference.html)