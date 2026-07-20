---
title: Authenticating to EKS
description: After you have configured OIDC for EKS, PingOne users can execute the kubectl command to authenticate to EKS.
component: solution-guides
page_id: solution-guides:data_and_application_security_use_cases:htg_config_oidc_authn_aws_eks_custers_authn_eks
canonical_url: https://docs.pingidentity.com/solution-guides/data_and_application_security_use_cases/htg_config_oidc_authn_aws_eks_custers_authn_eks.html
llms_txt: https://docs.pingidentity.com/solution-guides/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: April 29, 2024
---

# Authenticating to EKS

After you have configured OIDC for EKS, PingOne users can execute the `kubectl` command to authenticate to EKS.

Executing `kubectl get svc` opens a new window in the user's default browser and redirects them to authenticate with PingOne.

![Screen capture showing the Ping Identity Sign On window.](_images/qky1619121562643.png)

Upon successful authentication, PingOne redirects the user to the Kubelogin successful login page, indicating that they are now authenticated to the cluster.

With verbose `kubectl` logging enabled, the output of the `kubectl get svc` command is shown here.

```
I0408 16:45:16.147985   34902 get_token.go:53] WARNING: log may contain your secrets such as token or password
I0408 16:45:16.148119   34902 get_token.go:60] acquiring a lock get-token-8000-18000
I0408 16:45:16.148190   34902 get_token.go:72] finding a token from cache directory /Users/peterholko/.kube/cache/oidc-login
I0408 16:45:16.148501   34902 authentication.go:76] checking expiration of the existing token
I0408 16:45:16.148566   34902 authentication.go:85] you already have a valid token until 2021-04-08 16:46:39 -0700 PDT
I0408 16:45:16.148607   34902 get_token.go:104] you got a token: {
  "sub": "emma.sharp@pingidentity.com",
  "aud": "7e29215f-b6c3-42f5-9153-85147e3de93a",
  "acr": "urn:oasis:names:tc:SAML:2.0:ac:classes:Password",
  "idpid": "db6dccae-f491-426d-a16e-052eb4214011",
  "auth_time": 1617925299,
  "iss": "https://sso.connect.pingidentity.com/7e29215f-b6c3-42f5-9153-85147e3de93a",
  "exp": 1617925599,
  "iat": 1617925299,
  "nonce": "rsWXrEH2MT5JPaBBPMU6PJ_s3kepPbkBtgcG_X7Orfo"
}
I0408 16:45:16.148620   34902 get_token.go:107] you already have a valid token until 2021-04-08 16:46:39 -0700 PDT
I0408 16:45:16.148630   34902 get_token.go:114] writing the token to client-go

NAME         TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)   AGE
kubernetes   ClusterIP   10.100.0.1   <none>        443/TCP   8d
```

---

---
title: Configuring kubectl for OIDC
description: Configure the kubectl command line tool to work with OIDC.
component: solution-guides
page_id: solution-guides:data_and_application_security_use_cases:htg_config_oidc_authn_aws_eks_custers_kubectl
canonical_url: https://docs.pingidentity.com/solution-guides/data_and_application_security_use_cases/htg_config_oidc_authn_aws_eks_custers_kubectl.html
llms_txt: https://docs.pingidentity.com/solution-guides/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: April 29, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
  result: Result
---

# Configuring kubectl for OIDC

## About this task

Configure the `kubectl` command line tool to work with OIDC.

## Steps

1. Update your context to the cluster.

   ```
   aws eks update-kubeconfig --name tech-partners --region us-west-2
   ```

2. Configure the kubectl OIDC login by using the **Issuer URL**, **Client ID**, and **Client Secret** created in the PingOne EKS application.

   ```
   ubectl oidc-login setup --oidc-issuer-url=https://sso.connect.pingidentity.com/
   7e29215f-b6c3-42f5-9153-85147e3de93a --oidc-client-id=7e29215f-b6c3-42f5-9153-85147e3de93a
   --oidc-client-secret=nJ1GHnQzlmyhtOLMNNOOGokiYqPc7YaZ3p7clTbF3m9KuYkdHTxfPJV53P7KovVnO
   ```

3. Bind a Cluster Role to a PingOne account.

   ```
   kubectl create clusterrolebinding oidc-cluster-admin --clusterrole=cluster-admin
   --user='https://sso.connect.pingidentity.com/7e29215f-b6c3-42f5-9153-85147e3de93a
   #emma.sharp@pingidentity.com'
   ```

4. Set up the kubeconfig with the OIDC PingOne configuration.

   ```
   kubectl config set-credentials oidc \
   --exec-api-version=client.authentication.k8s.io/v1beta1 \
   --exec-command=kubectl \
   --exec-arg=oidc-login \
   --exec-arg=get-token \  --exec-arg=--oidc-issuer-url=https://sso.connect.pingidentity.com/
   7e29215f-b6c3-42f5-9153-85147e3de93a \
   --exec-arg=--oidc-client-id=7e29215f-b6c3-42f5-9153-85147e3de93a \ --exec-arg=--oidc-client-
   secret=nJ1GHnQzlmyhtOLMNNOOGokiYqPc7YaZ3p7clTbF3m9KuYkdHTxfPJV53P7KovVnO
   --exec-arg -v1
   ```

   |   |                                                                                            |
   | - | ------------------------------------------------------------------------------------------ |
   |   | The `--exec-arg -v1` sets kubectl to verbose logging, which is useful for troubleshooting. |

## Result

OIDC for EKS is configured, and PingOne users can authenticate to EKS by executing any `kubectl` command.

---

---
title: Configuring medium-grained application access control through Azure AD, PingFederate, and PingAccess
description: PingAccess can interact directly with an OIDC IdP provider, so you don't need to use PingFederate to authenticate against Azure AD.
component: solution-guides
page_id: solution-guides:data_and_application_security_use_cases:htg_config_med_grained_app
canonical_url: https://docs.pingidentity.com/solution-guides/data_and_application_security_use_cases/htg_config_med_grained_app.html
llms_txt: https://docs.pingidentity.com/solution-guides/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 18, 2022
section_ids:
  components: Components
  before-you-begin: Before you begin
  setting-up-azure-ad-as-an-oidc-provider-in-pingfederate: Setting up Azure AD as an OIDC provider in PingFederate
  steps: Steps
  example: Example:
  setting-up-azure-ad-as-an-oidc-provider-for-pingaccess-in-pingfederate: Setting up Azure AD as an OIDC provider for PingAccess in PingFederate
  about-this-task: About this task
  steps-2: Steps
  result: Result:
---

# Configuring medium-grained application access control through Azure AD, PingFederate, and PingAccess

PingAccess can interact directly with an OIDC IdP provider, so you don't need to use PingFederate to authenticate against Azure AD.

However, when you add PingFederate to the equation, you gain additional features such as session management, data transformation from Azure AD before it gets sent to PingAccess, and local datastore lookups for additional information outside of Azure AD.

## Components

* PingFederate 8.3

* PingAccess 4.2

* Microsoft® Azure Active Directory (Azure AD)

|   |                                                                                                                                                                                                |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | This use case was developed with the specified product versions. With more recent product versions, the general workflow should apply although specific menu options and screens might differ. |

## Before you begin

* Make sure that the components are installed and running.

* For Azure AD, ensure that you have a verified domain name and at least one user and one group for testing.

## Setting up Azure AD as an OIDC provider in PingFederate

### Steps

1. Access your Azure AD OIDC discovery document and record the `Issuer` value from the `/.well-known/openid-configuration` endpoint.

   #### Example:

   For example, if the Azure AD verified domain is "myglobalco.org", the URL is: <https://login.microsoftonline.com/myglobalco.org/v2.0/.well-known/openid-configuration>.

2. Log in to PingFederate as an administrator, and create an SP configuration for Azure AD using the `Issuer` value from the previous step as explained in [Create an OpenID Connect IdP connection](https://cdn-docs.pingidentity.com/archive/pdf/pingfederate/pingfederate-91.pdf#page=460).

3. Open a new tab and log in as Azure AD administrator to <https://apps.dev.microsoft.com/#/appList>.

4. Add a new app that has a friendly and descriptive name to show on the Azure AD login screen for your application.

5. Obtain an Application ID and Application Secret from Azure AD, and record them.

6. In your PingFederate IdP **Connection** tab, add the Azure Application ID in the **Client ID** field and the Azure Application Secret in the **Client Secret** field. See [Create an OpenID Connect IdP connection](https://cdn-docs.pingidentity.com/archive/pdf/pingfederate/pingfederate-91.pdf#page=460).

7. To verify browser SSO settings, click **Configure Browser SSO**.

8. In the **Activation and Summary** screen, change your connection status to Active, record the redirect URI, and click **Save**.

   |   |                                                              |
   | - | ------------------------------------------------------------ |
   |   | To aid initial testing, record the SSO application endpoint. |

9. In the Azure AD administrator app list configuration, select your application from PingFederate, click **Add Platform**, select type **Web**, and paste your redirect URI.

10. Change any other MS Graph Permissions, logo, Terms of Service or Privacy Statement options that you need to change, and click **Save**.

    |   |                                                                                                                              |
    | - | ---------------------------------------------------------------------------------------------------------------------------- |
    |   | To obtain group information, choose **Advanced Options → Application Manifest** and change "groupMembershipClaims" to "All". |

11. To verify that your OIDC IdP connection is working, go to your SSO Application endpoint from PingFederate.

    You should be redirected to login with your Azure AD credentials, and you should be SSO'd into your SP adapter if one is configured.

## Setting up Azure AD as an OIDC provider for PingAccess in PingFederate

### About this task

This procedure assumes that you have configured PingFederate and PingAccess to talk to each other through OIDC. You need to add Azure AD as an authentication source for PingAccess in PingFederate.

For general instructions, see [Create an OpenID Connect IdP connection](https://cdn-docs.pingidentity.com/archive/pdf/pingfederate/pingfederate-91.pdf#page=460)

### Steps

1. From the Authentication Selector screen in PingFederate, select the **Add or Update AuthN Context Attribute**box next to the PingAccess entry, update your selector result values to include Azure AD as an authentication requirement, and click **Save**. See [Configure the Requested AuthN Context Authentication Selector](https://cdn-docs.pingidentity.com/archive/pdf/pingfederate/pingfederate-91.pdf#page=61).

2. Ensure there is a path in your authentication policy tree to include your new authentication requirement for Azure, verify that you are fulfilling your policy contracts, and click **Save**. See [Defining authentication policies](https://cdn-docs.pingidentity.com/archive/pdf/pingfederate/pingfederate-91.pdf#page=233) and [Define authentication policies based on group membership information](https://cdn-docs.pingidentity.com/archive/pdf/pingfederate/pingfederate-91.pdf#page=237).

3. Under **Authorization Server Settings**, extend the persistent grant to map the Azure AD group into the OIDC token to PingAccess. See [Define grant contract fulfillment for IdP adapter mapping](https://cdn-docs.pingidentity.com/archive/pdf/pingfederate/pingfederate-91.pdf#page=286).

4. Extend the access token attribute contract to include groups, fulfill the persistent grants from the authentication policy contract, and fulfill the access token mapping with the persistent grant. See [Configure policy and ID token settings](https://cdn-docs.pingidentity.com/archive/pdf/pingfederate/pingfederate-91.pdf#page=316).

5. In your OIDC policy, map from the access token or perform any additional lookups against local data stores. See [Configure IdP adapter attribute sources and user lookup](https://cdn-docs.pingidentity.com/archive/pdf/pingfederate/pingfederate-91.pdf#page=227).

6. Go to PingAccess and write a web session attribute rule for the group membership to which the rule applies. See [Configure session management](https://cdn-docs.pingidentity.com/archive/pdf/pingaccess/pingaccess-72.pdf#page=121).

   |   |                                                                                                   |
   | - | ------------------------------------------------------------------------------------------------- |
   |   | Azure AD does not provide friendly names for their groups and instead returns them as object IDs. |

   Apply this rule as needed for your specific use case, application, or API.

   #### Result:

   PingAccess verifies group membership in Azure AD and uses this group membership to enforce medium-grained access control.

---

---
title: Configuring OIDC authentication for AWS EKS clusters
description: Open ID Connect (OIDC) supports authentication for Amazon Web Services (AWS) Elastic Kubernetes Service (EKS) clusters. You can configure PingOne as an identity provider (IdP) to provide strong user authentication to your EKS clusters.
component: solution-guides
page_id: solution-guides:data_and_application_security_use_cases:htg_config_oidc_authn_aws_eks_custers
canonical_url: https://docs.pingidentity.com/solution-guides/data_and_application_security_use_cases/htg_config_oidc_authn_aws_eks_custers.html
llms_txt: https://docs.pingidentity.com/solution-guides/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: December 29, 2022
section_ids:
  components: Components
  before-you-begin: Before you begin
  creating-a-pingone-oidc-application: Creating a PingOne OIDC application
  about-this-task: About this task
  steps: Steps
  configuring-kubectl-for-oidc: Configuring kubectl for OIDC
  about-this-task-2: About this task
  steps-2: Steps
  result: Result
  authenticating-to-eks: Authenticating to EKS
---

# Configuring OIDC authentication for AWS EKS clusters

Open ID Connect (OIDC) supports authentication for Amazon Web Services (AWS) Elastic Kubernetes Service (EKS) clusters. You can configure PingOne as an identity provider (IdP) to provide strong user authentication to your EKS clusters.

Integrating OpenID Connect (OIDC) within AWS EKS involves creating a PingOne OIDC application and configuring the `kubectl` CLI for OIDC.

You can use the PingOne IdP as an alternative, or in addition, to AWS Identity and Access Management (IAM). With this feature, you can manage user access to your cluster by leveraging an existing identity management life cycle through your OIDC identity provider.

The features and benefits of this configuration are:

* Centralized Authentication Policy

  User authentication to the EKS can leverage the centralized PingOne Identity Provider policy.

* Extended Multi-Factor Authentication

  By using PingOne, strong multi-factor authentication can be extended to your EKS user authentication.

* Strengthened security using PingOne Protect

  By analyzing multiple risk signals, PingOne Protect can identify anomalous activity to block attacks or require strong authentication methods, providing a greater level of assurance of your users' identities.

## Components

* PingOne for Enterprise

* AWS EKS cluster 1.6+

* Kubelogin plugin for kubectl (<https://github.com/int128/kubelogin>)

## Before you begin

Make sure you have the following:

* A basic understanding of OIDC and OAuth 2.0 protocols

* An understanding of JSON Web Tokens

* A local installation of AWD CLI for configuring the OIDC integration within Amazon EKS

* AWS CLI installed and configured to the existing AWS EKS Cluster

* A PingOne for Enterprise account (<https://www.pingidentity.com/en/trials/p14e-trial.html>)

For more information, see [Integrating an OIDC application](https://docs.pingidentity.com/pingoneforenterprise/pingone_sso_for_saas_apps/p14saas_integrate_oidc_application.html).

## Creating a PingOne OIDC application

### About this task

To configure your AWS EKS cluster for OIDC authentication, you must first create a PingOne OIDC application to acquire the required OIDC Issuer URL and OIDC Client ID.

To create a PingOne OIDC application:

### Steps

1. Sign on to your PingOne for Enterprise tenant.

2. Go to **Applications → My Applications → OIDC**.

3. Select **Advanced Configuration**, and click **Next**.

   ![Screen capture showing how to select the Advanced Configuration option for the OIDC application.](_images/fpl1619118809683.png)

4. Type the **Application Name** and **Description**, and click **Next**.

5. In the **Authorization Settings** section, check **Authorization Code** for the **Allowed Grant Types**.

6. To include a client secret, click **Add Secret**. Record the **Client ID** and **Client Secret** for later use. Click **Next**.

   ![Screen capture showing how to configure the Allowed Grant Type authorization setting and where to add a secret for the OIDC application.](_images/zdh1619119258210.png)

7. In the **SSO Flow and Authentication Settings** section, enter the following:

   1. In the **Start SSO URL** field, enter `https://localhost`.

   2. In the **Redirect URIs** field, enter `http://locallhost:8000` and `http://localhost:18000`.

   3. Click **Next**.

      ![Screen capture showing how to add the Start SSO URL and Redirect URIs.](_images/gtk1619119659796.png)

8. Leave the default configuration for **Default User Profile Attribute Contract** and **Connect Scopes**.

9. Configure the required **Attribute Mapping** for the `subject` attribute. Click **Next**.

   ![Screen capture showing how to configure the attribute mapping for the subject attribute.](_images/jvk1619119922504.png)

10. Assign any required **PingOne Groups** for access, and then click **Done**.

## Configuring kubectl for OIDC

### About this task

Configure the `kubectl` command line tool to work with OIDC.

### Steps

1. Update your context to the cluster.

   ```
   aws eks update-kubeconfig --name tech-partners --region us-west-2
   ```

2. Configure the kubectl OIDC login by using the **Issuer URL**, **Client ID**, and **Client Secret** created in the PingOne EKS application.

   ```
   ubectl oidc-login setup --oidc-issuer-url=https://sso.connect.pingidentity.com/
   7e29215f-b6c3-42f5-9153-85147e3de93a --oidc-client-id=7e29215f-b6c3-42f5-9153-85147e3de93a
   --oidc-client-secret=nJ1GHnQzlmyhtOLMNNOOGokiYqPc7YaZ3p7clTbF3m9KuYkdHTxfPJV53P7KovVnO
   ```

3. Bind a Cluster Role to a PingOne account.

   ```
   kubectl create clusterrolebinding oidc-cluster-admin --clusterrole=cluster-admin
   --user='https://sso.connect.pingidentity.com/7e29215f-b6c3-42f5-9153-85147e3de93a
   #emma.sharp@pingidentity.com'
   ```

4. Set up the kubeconfig with the OIDC PingOne configuration.

   ```
   kubectl config set-credentials oidc \
   --exec-api-version=client.authentication.k8s.io/v1beta1 \
   --exec-command=kubectl \
   --exec-arg=oidc-login \
   --exec-arg=get-token \  --exec-arg=--oidc-issuer-url=https://sso.connect.pingidentity.com/
   7e29215f-b6c3-42f5-9153-85147e3de93a \
   --exec-arg=--oidc-client-id=7e29215f-b6c3-42f5-9153-85147e3de93a \ --exec-arg=--oidc-client-
   secret=nJ1GHnQzlmyhtOLMNNOOGokiYqPc7YaZ3p7clTbF3m9KuYkdHTxfPJV53P7KovVnO
   --exec-arg -v1
   ```

   |   |                                                                                            |
   | - | ------------------------------------------------------------------------------------------ |
   |   | The `--exec-arg -v1` sets kubectl to verbose logging, which is useful for troubleshooting. |

### Result

OIDC for EKS is configured, and PingOne users can authenticate to EKS by executing any `kubectl` command.

## Authenticating to EKS

After you have configured OIDC for EKS, PingOne users can execute the `kubectl` command to authenticate to EKS.

Executing `kubectl get svc` opens a new window in the user's default browser and redirects them to authenticate with PingOne.

![Screen capture showing the Ping Identity Sign On window.](_images/qky1619121562643.png)

Upon successful authentication, PingOne redirects the user to the Kubelogin successful login page, indicating that they are now authenticated to the cluster.

With verbose `kubectl` logging enabled, the output of the `kubectl get svc` command is shown here.

```
I0408 16:45:16.147985   34902 get_token.go:53] WARNING: log may contain your secrets such as token or password
I0408 16:45:16.148119   34902 get_token.go:60] acquiring a lock get-token-8000-18000
I0408 16:45:16.148190   34902 get_token.go:72] finding a token from cache directory /Users/peterholko/.kube/cache/oidc-login
I0408 16:45:16.148501   34902 authentication.go:76] checking expiration of the existing token
I0408 16:45:16.148566   34902 authentication.go:85] you already have a valid token until 2021-04-08 16:46:39 -0700 PDT
I0408 16:45:16.148607   34902 get_token.go:104] you got a token: {
  "sub": "emma.sharp@pingidentity.com",
  "aud": "7e29215f-b6c3-42f5-9153-85147e3de93a",
  "acr": "urn:oasis:names:tc:SAML:2.0:ac:classes:Password",
  "idpid": "db6dccae-f491-426d-a16e-052eb4214011",
  "auth_time": 1617925299,
  "iss": "https://sso.connect.pingidentity.com/7e29215f-b6c3-42f5-9153-85147e3de93a",
  "exp": 1617925599,
  "iat": 1617925299,
  "nonce": "rsWXrEH2MT5JPaBBPMU6PJ_s3kepPbkBtgcG_X7Orfo"
}
I0408 16:45:16.148620   34902 get_token.go:107] you already have a valid token until 2021-04-08 16:46:39 -0700 PDT
I0408 16:45:16.148630   34902 get_token.go:114] writing the token to client-go

NAME         TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)   AGE
kubernetes   ClusterIP   10.100.0.1   <none>        443/TCP   8d
```

---

---
title: Configuring PingAccess to protect a web application
description: Add your PingFederate server certificate under Trusted Certificate Groups as described in Importing certificates and create a trusted certificate group.
component: solution-guides
page_id: solution-guides:data_and_application_security_use_cases:htg_connect_pf_pa_oidc_web_app
canonical_url: https://docs.pingidentity.com/solution-guides/data_and_application_security_use_cases/htg_connect_pf_pa_oidc_web_app.html
llms_txt: https://docs.pingidentity.com/solution-guides/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: April 29, 2024
section_ids:
  steps: Steps
---

# Configuring PingAccess to protect a web application

## Steps

1. Add your PingFederate server certificate under **Trusted Certificate Groups** as described in [Importing certificates and create a trusted certificate group](https://cdn-docs.pingidentity.com/archive/pdf/pingaccess/pingaccess-63.pdf#page=519).

2. Configure PingFederate runtime settings as described in [Configuring the token provider](https://cdn-docs.pingidentity.com/archive/pdf/pingaccess/pingaccess-63.pdf#page=520) using the following values.

   | Parameter                     | Value                                                              |
   | ----------------------------- | ------------------------------------------------------------------ |
   | **Host**                      | Enter your PingFederate host name.                                 |
   | **Port**                      | Enter your PingFederate port number.                               |
   | **Secure**                    | **Yes**                                                            |
   | **Trusted Certificate Group** | Select the group to which you added your PingFederate certificate. |
   | All other parameters          | Accept the defaults.                                               |

3. Configure PingFederate administration settings as described in [Configuring the token provider](https://cdn-docs.pingidentity.com/archive/pdf/pingaccess/pingaccess-63.pdf#page=520) using the following values.

   | Parameter                     | Value                                                              |
   | ----------------------------- | ------------------------------------------------------------------ |
   | **Host**                      | Enter your PingFederate host name.                                 |
   | **Port**                      | Enter your PingFederate port number.                               |
   | **Admin Username**            | Enter the login name for your PingFederate administrator.          |
   | **Admin Password**            | Enter the password for your PingFederate administrator.            |
   | **Secure**                    | **Yes**                                                            |
   | **Trusted Certificate Group** | Select the group to which you added your PingFederate certificate. |
   | All other parameters          | Accept the defaults.                                               |

4. Configure PingFederate OAuth server settings as described in [Configuring the token provider](https://cdn-docs.pingidentity.com/archive/pdf/pingaccess/pingaccess-63.pdf#page=520) using the following values.

   | Parameter                  | Value                     |
   | -------------------------- | ------------------------- |
   | **Client ID**              | **pa\_rs**                |
   | **Client Secret**          | Enter your client secret. |
   | **Subject Attribute Name** | **UserName**              |
   | All other parameters       | Accept the defaults.      |

5. Go to **Main → Sites → Sites** to add a site for PingFederate to protect.

   Detailed steps differ by deployment. For more information, see [Adding sites](https://cdn-docs.pingidentity.com/archive/pdf/pingaccess/pingaccess-63.pdf#page=256).

6. Add an identity mapping for your site as described in [Creating JWT identity mappings](https://cdn-docs.pingidentity.com/archive/pdf/pingaccess/pingaccess-63.pdf#page=304) using the following values.

   | Parameter            | Value                                                                                            |
   | -------------------- | ------------------------------------------------------------------------------------------------ |
   | **Name**             | Enter a name for the identity mapping.                                                           |
   | **Type**             | Select **Header Identity Mapping**, and create a sub attribute with a header name of **X-USER**. |
   | All other parameters | Accept the defaults.                                                                             |

7. Add a web session for your site as described in [Creating web sessions](https://cdn-docs.pingidentity.com/archive/pdf/pingaccess/pingaccess-63.pdf#page=308) using the following values.

   | Parameter                     | Value                                    |
   | ----------------------------- | ---------------------------------------- |
   | **Name**                      | Enter a name for your web session.       |
   | **Cookie Type**               | **Encrypted JWT**                        |
   | **Audience**                  | **global**                               |
   | **OpenID Connect Login Type** | **Code**                                 |
   | **Client ID**                 | **pa\_wam**                              |
   | **Client Secret**             | Enter your organization's client secret. |
   | All other parameters          | Accept the defaults.                     |

8. Add an application to protect within the site as described in [Adding application resources](https://cdn-docs.pingidentity.com/archive/pdf/pingaccess/pingaccess-63.pdf#page=245).

9. Enable your application.

---

---
title: Connecting OAuth 2.0 and OpenID Connect with PingAccess
description: Sign on to your PingFederate administrative console.
component: solution-guides
page_id: solution-guides:data_and_application_security_use_cases:htg_connect_pf_pa_oidc_oauth2
canonical_url: https://docs.pingidentity.com/solution-guides/data_and_application_security_use_cases/htg_connect_pf_pa_oidc_oauth2.html
llms_txt: https://docs.pingidentity.com/solution-guides/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: April 29, 2024
section_ids:
  steps: Steps
---

# Connecting OAuth 2.0 and OpenID Connect with PingAccess

## Steps

1. Sign on to your PingFederate administrative console.

2. Enable OAuth 2.0 and OpenID Connect as described in [Configuring authorization server settings](https://cdn-docs.pingidentity.com/archive/pdf/pingfederate/pingfederate-103.pdf#page=488).

   Go to **Server Configuration → Server Settings → Roles & Protocols** and select **Enable OAuth 2.0 Authorization Server (AS) Role** and **OpenID Connect**.

3. Set up your IdP adapters for PingAccess.

   |   |                                                                                                                                                                                   |
   | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | Detailed steps differ by deployment. For more information, see [Managing IdP adapters](https://cdn-docs.pingidentity.com/archive/pdf/pingfederate/pingfederate-103.pdf#page=396). |

4. Configure scope values and scope descriptions for OAuth Authorization Server settings as described in [Defining Scopes](https://cdn-docs.pingidentity.com/archive/pdf/pingfederate/pingfederate-103.pdf#page=506) using the following values.

   | Scope Value | Scope Description |
   | ----------- | ----------------- |
   | **address** | address           |
   | **email**   | email             |
   | **openid**  | openid            |
   | **phone**   | phone             |
   | **profile** | profile           |

   |   |                                                                                          |
   | - | ---------------------------------------------------------------------------------------- |
   |   | In the **Default Scopes** field, enter a default scope description for your environment. |

5. Configure access token management for OAuth Authorization Server settings as described in [Configuring authorization server settings](https://cdn-docs.pingidentity.com/archive/pdf/pingfederate/pingfederate-103.pdf#page=488) using the following values.

   | Parameter                           | Value                                   |
   | ----------------------------------- | --------------------------------------- |
   | **Instance Name**                   | GeneralAccessToken                      |
   | **Instance ID**                     | **GeneralAccessToken**                  |
   | **Type**                            | **Internally Managed Reference Tokens** |
   | **Instance Configuration**          | Accept the defaults.                    |
   | **Session Validation**              |                                         |
   | **Access Token Attribute Contract** | **UserName**                            |
   | **Resource URIs**                   | Accept the defaults.                    |
   | **Access Control**                  | Accept the defaults.                    |

6. Configure your OpenID Connect policy as described in [Configuring OpenID Connect policies](https://cdn-docs.pingidentity.com/archive/pdf/pingfederate/pingfederate-103.pdf#page=587) using the following values.

   | Parameter                                   | Value                  |
   | ------------------------------------------- | ---------------------- |
   | **Policy ID**                               | **OIDC**               |
   | **Name**                                    | **OIDC**               |
   | **Access Token Manager**                    | **GeneralAccessToken** |
   | **Attribute Contract**                      | Accept the defaults.   |
   | **Attribute Sources & Lookup**              | Accept the defaults.   |
   | **Contract Fulfillment Attribute Contract** | **sub**                |
   | **Contract Fulfillment Source**             | **Access Token**       |
   | **Issuance Criteria**                       | Accept the defaults.   |

7. Configure a PingAccess Resource Server OAuth client as described in [Configuring OAuth Clients](https://cdn-docs.pingidentity.com/archive/pdf/pingfederate/pingfederate-103.pdf#page=529) using the following values.

   | Parameter               | Value                                                                                                                                                             |
   | ----------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   | **Client ID**           | **pa\_rs**                                                                                                                                                        |
   | **Name**                | **PingAccess Resource Server**                                                                                                                                    |
   | **Client Secret**       | Generate a unique client secret.&#xA;&#xA;Although you can manually enter a client secret, allowing PingFederate to generate the secret provides better security. |
   | **Allowed Grant Types** | **Access Token Validation (Client is a Resource Server)**                                                                                                         |
   | All other parameters    | Accept the defaults.                                                                                                                                              |

8. Configure a PingAccess Web Management OAuth client as described in [Configuring OAuth Clients](https://cdn-docs.pingidentity.com/archive/pdf/pingfederate/pingfederate-103.pdf#page=529) using the following values.

   | Parameter                         | Value                                                                                                 |
   | --------------------------------- | ----------------------------------------------------------------------------------------------------- |
   | **Client ID**                     | **pa\_wam**                                                                                           |
   | **Name**                          | **PingAccess Web Management**                                                                         |
   | **Client Authentication**         | The client secret that you generated for the PingAccess Resource Server should fill in automatically. |
   | **Redirection URI**               | https\://*\<PA\_HOST>*:*\<PA\_USER\_PORT>*/pa/oidc/cb                                                 |
   | **Bypass Authorization Approval** | **Bypass**                                                                                            |
   | **Allowed Grant Types**           | **Authorization Code**                                                                                |
   | All other parameters              | Accept the defaults.                                                                                  |

9. Verify all client settings and click **Save** on the **Client Management** tab.

10. Configure your IdP adapters to work with OAuth as described in [Managing IdP adapter grant mapping](https://cdn-docs.pingidentity.com/archive/pdf/pingfederate/pingfederate-103.pdf#page=543) using the following values

    | Parameter                           | Value                                                                                                                     |
    | ----------------------------------- | ------------------------------------------------------------------------------------------------------------------------- |
    | **Source Adapter Instance**         | Select the HTML Form adapter or adapters that you want to use for PingAccess.                                             |
    | **Attribute Sources & User Lookup** | For each adapter, accept the defaults.                                                                                    |
    | **Contract Fulfillment**            | For each adapter, select the adapter as your source and set your unique identifiers for **USER\_KEY** and **USER\_NAME**. |
    | **Issuance Criteria**               | Accept the defaults.                                                                                                      |

11. Map your address tokens for OAuth as described in [Managing access token mappings](https://cdn-docs.pingidentity.com/archive/pdf/pingfederate/pingfederate-103.pdf#page=564) using the following values.

    | Parameter                           | Value                                                                                            |
    | ----------------------------------- | ------------------------------------------------------------------------------------------------ |
    | **Attribute Sources & User Lookup** | Accept the defaults.                                                                             |
    | **Contract Fulfillment**            | For the username, select **Persistent Grant** as your source and set the value as **USER\_KEY**. |
    | **Issuance Criteria**               | Accept the defaults.                                                                             |

12. Verify your settings on the **Summary** tab, then click **Save**.

13. Export the SSL certificate to use for connecting securely with PingAccess as described in [Manage SSL server certificates](https://cdn-docs.pingidentity.com/archive/pdf/pingfederate/pingfederate-103.pdf#page=617).

---

---
title: Connecting PingFederate to PingAccess using the OIDC protocol
description: Configure authentication between PingFederate and PingAccess using the OpenID Connect (OIDC) protocol.
component: solution-guides
page_id: solution-guides:data_and_application_security_use_cases:htg_connect_pf_pa_oidc
canonical_url: https://docs.pingidentity.com/solution-guides/data_and_application_security_use_cases/htg_connect_pf_pa_oidc.html
llms_txt: https://docs.pingidentity.com/solution-guides/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 18, 2022
section_ids:
  components: Components
  before-you-begin: Before you begin
  connecting-oauth-2-0-and-openid-connect-with-pingaccess: Connecting OAuth 2.0 and OpenID Connect with PingAccess
  steps: Steps
  configuring-pingaccess-to-protect-a-web-application: Configuring PingAccess to protect a web application
  steps-2: Steps
  performing-final-steps: Performing final steps
  steps-3: Steps
  result: Result:
---

# Connecting PingFederate to PingAccess using the OIDC protocol

Configure authentication between PingFederate and PingAccess using the OpenID Connect (OIDC) protocol.

## Components

* PingFederate 10.3

* PingAccess 6.3

## Before you begin

* Verify that the components are installed and running.

* Have an application that you want to protect by using PingAccess.

## Connecting OAuth 2.0 and OpenID Connect with PingAccess

### Steps

1. Sign on to your PingFederate administrative console.

2. Enable OAuth 2.0 and OpenID Connect as described in [Configuring authorization server settings](https://cdn-docs.pingidentity.com/archive/pdf/pingfederate/pingfederate-103.pdf#page=488).

   Go to **Server Configuration → Server Settings → Roles & Protocols** and select **Enable OAuth 2.0 Authorization Server (AS) Role** and **OpenID Connect**.

3. Set up your IdP adapters for PingAccess.

   |   |                                                                                                                                                                                   |
   | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | Detailed steps differ by deployment. For more information, see [Managing IdP adapters](https://cdn-docs.pingidentity.com/archive/pdf/pingfederate/pingfederate-103.pdf#page=396). |

4. Configure scope values and scope descriptions for OAuth Authorization Server settings as described in [Defining Scopes](https://cdn-docs.pingidentity.com/archive/pdf/pingfederate/pingfederate-103.pdf#page=506) using the following values.

   | Scope Value | Scope Description |
   | ----------- | ----------------- |
   | **address** | address           |
   | **email**   | email             |
   | **openid**  | openid            |
   | **phone**   | phone             |
   | **profile** | profile           |

   |   |                                                                                          |
   | - | ---------------------------------------------------------------------------------------- |
   |   | In the **Default Scopes** field, enter a default scope description for your environment. |

5. Configure access token management for OAuth Authorization Server settings as described in [Configuring authorization server settings](https://cdn-docs.pingidentity.com/archive/pdf/pingfederate/pingfederate-103.pdf#page=488) using the following values.

   | Parameter                           | Value                                   |
   | ----------------------------------- | --------------------------------------- |
   | **Instance Name**                   | GeneralAccessToken                      |
   | **Instance ID**                     | **GeneralAccessToken**                  |
   | **Type**                            | **Internally Managed Reference Tokens** |
   | **Instance Configuration**          | Accept the defaults.                    |
   | **Session Validation**              |                                         |
   | **Access Token Attribute Contract** | **UserName**                            |
   | **Resource URIs**                   | Accept the defaults.                    |
   | **Access Control**                  | Accept the defaults.                    |

6. Configure your OpenID Connect policy as described in [Configuring OpenID Connect policies](https://cdn-docs.pingidentity.com/archive/pdf/pingfederate/pingfederate-103.pdf#page=587) using the following values.

   | Parameter                                   | Value                  |
   | ------------------------------------------- | ---------------------- |
   | **Policy ID**                               | **OIDC**               |
   | **Name**                                    | **OIDC**               |
   | **Access Token Manager**                    | **GeneralAccessToken** |
   | **Attribute Contract**                      | Accept the defaults.   |
   | **Attribute Sources & Lookup**              | Accept the defaults.   |
   | **Contract Fulfillment Attribute Contract** | **sub**                |
   | **Contract Fulfillment Source**             | **Access Token**       |
   | **Issuance Criteria**                       | Accept the defaults.   |

7. Configure a PingAccess Resource Server OAuth client as described in [Configuring OAuth Clients](https://cdn-docs.pingidentity.com/archive/pdf/pingfederate/pingfederate-103.pdf#page=529) using the following values.

   | Parameter               | Value                                                                                                                                                             |
   | ----------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   | **Client ID**           | **pa\_rs**                                                                                                                                                        |
   | **Name**                | **PingAccess Resource Server**                                                                                                                                    |
   | **Client Secret**       | Generate a unique client secret.&#xA;&#xA;Although you can manually enter a client secret, allowing PingFederate to generate the secret provides better security. |
   | **Allowed Grant Types** | **Access Token Validation (Client is a Resource Server)**                                                                                                         |
   | All other parameters    | Accept the defaults.                                                                                                                                              |

8. Configure a PingAccess Web Management OAuth client as described in [Configuring OAuth Clients](https://cdn-docs.pingidentity.com/archive/pdf/pingfederate/pingfederate-103.pdf#page=529) using the following values.

   | Parameter                         | Value                                                                                                 |
   | --------------------------------- | ----------------------------------------------------------------------------------------------------- |
   | **Client ID**                     | **pa\_wam**                                                                                           |
   | **Name**                          | **PingAccess Web Management**                                                                         |
   | **Client Authentication**         | The client secret that you generated for the PingAccess Resource Server should fill in automatically. |
   | **Redirection URI**               | https\://*\<PA\_HOST>*:*\<PA\_USER\_PORT>*/pa/oidc/cb                                                 |
   | **Bypass Authorization Approval** | **Bypass**                                                                                            |
   | **Allowed Grant Types**           | **Authorization Code**                                                                                |
   | All other parameters              | Accept the defaults.                                                                                  |

9. Verify all client settings and click **Save** on the **Client Management** tab.

10. Configure your IdP adapters to work with OAuth as described in [Managing IdP adapter grant mapping](https://cdn-docs.pingidentity.com/archive/pdf/pingfederate/pingfederate-103.pdf#page=543) using the following values

    | Parameter                           | Value                                                                                                                     |
    | ----------------------------------- | ------------------------------------------------------------------------------------------------------------------------- |
    | **Source Adapter Instance**         | Select the HTML Form adapter or adapters that you want to use for PingAccess.                                             |
    | **Attribute Sources & User Lookup** | For each adapter, accept the defaults.                                                                                    |
    | **Contract Fulfillment**            | For each adapter, select the adapter as your source and set your unique identifiers for **USER\_KEY** and **USER\_NAME**. |
    | **Issuance Criteria**               | Accept the defaults.                                                                                                      |

11. Map your address tokens for OAuth as described in [Managing access token mappings](https://cdn-docs.pingidentity.com/archive/pdf/pingfederate/pingfederate-103.pdf#page=564) using the following values.

    | Parameter                           | Value                                                                                            |
    | ----------------------------------- | ------------------------------------------------------------------------------------------------ |
    | **Attribute Sources & User Lookup** | Accept the defaults.                                                                             |
    | **Contract Fulfillment**            | For the username, select **Persistent Grant** as your source and set the value as **USER\_KEY**. |
    | **Issuance Criteria**               | Accept the defaults.                                                                             |

12. Verify your settings on the **Summary** tab, then click **Save**.

13. Export the SSL certificate to use for connecting securely with PingAccess as described in [Manage SSL server certificates](https://cdn-docs.pingidentity.com/archive/pdf/pingfederate/pingfederate-103.pdf#page=617).

## Configuring PingAccess to protect a web application

### Steps

1. Add your PingFederate server certificate under **Trusted Certificate Groups** as described in [Importing certificates and create a trusted certificate group](https://cdn-docs.pingidentity.com/archive/pdf/pingaccess/pingaccess-63.pdf#page=519).

2. Configure PingFederate runtime settings as described in [Configuring the token provider](https://cdn-docs.pingidentity.com/archive/pdf/pingaccess/pingaccess-63.pdf#page=520) using the following values.

   | Parameter                     | Value                                                              |
   | ----------------------------- | ------------------------------------------------------------------ |
   | **Host**                      | Enter your PingFederate host name.                                 |
   | **Port**                      | Enter your PingFederate port number.                               |
   | **Secure**                    | **Yes**                                                            |
   | **Trusted Certificate Group** | Select the group to which you added your PingFederate certificate. |
   | All other parameters          | Accept the defaults.                                               |

3. Configure PingFederate administration settings as described in [Configuring the token provider](https://cdn-docs.pingidentity.com/archive/pdf/pingaccess/pingaccess-63.pdf#page=520) using the following values.

   | Parameter                     | Value                                                              |
   | ----------------------------- | ------------------------------------------------------------------ |
   | **Host**                      | Enter your PingFederate host name.                                 |
   | **Port**                      | Enter your PingFederate port number.                               |
   | **Admin Username**            | Enter the login name for your PingFederate administrator.          |
   | **Admin Password**            | Enter the password for your PingFederate administrator.            |
   | **Secure**                    | **Yes**                                                            |
   | **Trusted Certificate Group** | Select the group to which you added your PingFederate certificate. |
   | All other parameters          | Accept the defaults.                                               |

4. Configure PingFederate OAuth server settings as described in [Configuring the token provider](https://cdn-docs.pingidentity.com/archive/pdf/pingaccess/pingaccess-63.pdf#page=520) using the following values.

   | Parameter                  | Value                     |
   | -------------------------- | ------------------------- |
   | **Client ID**              | **pa\_rs**                |
   | **Client Secret**          | Enter your client secret. |
   | **Subject Attribute Name** | **UserName**              |
   | All other parameters       | Accept the defaults.      |

5. Go to **Main → Sites → Sites** to add a site for PingFederate to protect.

   Detailed steps differ by deployment. For more information, see [Adding sites](https://cdn-docs.pingidentity.com/archive/pdf/pingaccess/pingaccess-63.pdf#page=256).

6. Add an identity mapping for your site as described in [Creating JWT identity mappings](https://cdn-docs.pingidentity.com/archive/pdf/pingaccess/pingaccess-63.pdf#page=304) using the following values.

   | Parameter            | Value                                                                                            |
   | -------------------- | ------------------------------------------------------------------------------------------------ |
   | **Name**             | Enter a name for the identity mapping.                                                           |
   | **Type**             | Select **Header Identity Mapping**, and create a sub attribute with a header name of **X-USER**. |
   | All other parameters | Accept the defaults.                                                                             |

7. Add a web session for your site as described in [Creating web sessions](https://cdn-docs.pingidentity.com/archive/pdf/pingaccess/pingaccess-63.pdf#page=308) using the following values.

   | Parameter                     | Value                                    |
   | ----------------------------- | ---------------------------------------- |
   | **Name**                      | Enter a name for your web session.       |
   | **Cookie Type**               | **Encrypted JWT**                        |
   | **Audience**                  | **global**                               |
   | **OpenID Connect Login Type** | **Code**                                 |
   | **Client ID**                 | **pa\_wam**                              |
   | **Client Secret**             | Enter your organization's client secret. |
   | All other parameters          | Accept the defaults.                     |

8. Add an application to protect within the site as described in [Adding application resources](https://cdn-docs.pingidentity.com/archive/pdf/pingaccess/pingaccess-63.pdf#page=245).

9. Enable your application.

## Performing final steps

### Steps

1. Test your application in a web browser.

   Access your application behind PingAccess (for example, https\://localhost:3000/*\<APP\_NAME>*).

   #### Result:

   You're redirected to PingFederate to authenticate and can access the application.

2. Add header printing to your application to verify that your application has access to the data that PingAccess is sending.

   Detailed steps differ by application and programming language. The following resources provide more information for specific programming languages.

   | Language | Sample Header Code                                                                                |
   | -------- | ------------------------------------------------------------------------------------------------- |
   | Java     | `https://docs.oracle.com/en/java/javase/21/docs/api/java.net.http/java/net/http/HttpHeaders.html` |
   | C#       | `https://learn.microsoft.com/dotnet/api/system.net.httpwebresponse.getresponseheader`             |
   | PHP      | `http://php.net/manual/en/function.headers-list.php`                                              |
   | Drupal   | `https://api.drupal.org/api/drupal/includes%21bootstrap.inc/function/drupal_get_http_header/7.x`  |

3. Remove any local login to your application because your application is now behind PingAccess.

   Detailed steps differ by application and programming language.

4. Configure your application to use headers for login.

   Detailed steps differ by application and programming language.

---

---
title: Creating a key pair associated with the new PingFederate host name
description: Go to Security → Key Pairs.
component: solution-guides
page_id: solution-guides:data_and_application_security_use_cases:htg_protect_pf_gateway_deploy_pa_create_key_pair
canonical_url: https://docs.pingidentity.com/solution-guides/data_and_application_security_use_cases/htg_protect_pf_gateway_deploy_pa_create_key_pair.html
llms_txt: https://docs.pingidentity.com/solution-guides/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: May 1, 2024
section_ids:
  steps: Steps
---

# Creating a key pair associated with the new PingFederate host name

## Steps

1. Go to **Security → Key Pairs**.

2. Click **Add Key Pair** and enter the applicable parameters using the following table as a guide.

   | Parameter                             | Example Value                 |
   | ------------------------------------- | ----------------------------- |
   | `Alias`                               | PF Master                     |
   | `Common Name`                         | `https://<pingfederate_host>` |
   | `Subject Alternative Name - DNS Name` | `https://<pingfederate_host>` |
   | All other parameters                  | Accept the defaults           |

   |   |                                                                                                                                                                                                                                                                                                                                                                                                      |
   | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | To avoid a "Not Secure" warning in your browser, a signed certificate is required. Use PingFederate to generate a certificate signing request (CSR) and import the CSR response, as described in [Manage SSL server certificates](https://cdn-docs.pingidentity.com/archive/pdf/pingfederate/pingfederate-92.pdf#page=210). The certificate can be self-signed or signed by a certificate authority. |

3. Click **Save**.

---

---
title: Creating a PingAccess application leveraging the site and the virtual host
description: Go to Applications → Add Application.
component: solution-guides
page_id: solution-guides:data_and_application_security_use_cases:htg_protect_pf_gateway_deploy_pa_create_app_host
canonical_url: https://docs.pingidentity.com/solution-guides/data_and_application_security_use_cases/htg_protect_pf_gateway_deploy_pa_create_app_host.html
llms_txt: https://docs.pingidentity.com/solution-guides/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: May 1, 2024
section_ids:
  steps: Steps
---

# Creating a PingAccess application leveraging the site and the virtual host

## Steps

1. Go to **Applications → Add Application**.

2. Enter the applicable parameters using the following table as a guide.

   | Parameter              | Example Value                     |
   | ---------------------- | --------------------------------- |
   | `Name`                 | PF                                |
   | `Context Root`         | /                                 |
   | `Virtual Host(s)`      | `https://<pingfederate_host>:443` |
   | `Application Type`     | Web                               |
   | `Web Session`          | None                              |
   | `Web Identity Mapping` | None                              |
   | `Destination`          | Site                              |
   | `Site`                 | PF                                |
   | `Require HTTPS`        | Yes                               |
   | `Enabled`              | Yes                               |
   | All other parameters   | Accept the defaults               |

3. Click **Save**.

---

---
title: Creating a PingAccess site to protect PingFederate
description: Go to Sites → Add Site.
component: solution-guides
page_id: solution-guides:data_and_application_security_use_cases:htg_protect_pf_gateway_deploy_pa_create_pa_site
canonical_url: https://docs.pingidentity.com/solution-guides/data_and_application_security_use_cases/htg_protect_pf_gateway_deploy_pa_create_pa_site.html
llms_txt: https://docs.pingidentity.com/solution-guides/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: May 1, 2024
section_ids:
  steps: Steps
---

# Creating a PingAccess site to protect PingFederate

## Steps

1. Go to **Sites → Add Site**.

2. Create a PingAccess site using the following table as a guide.

   | Parameter                   | Example Value             |
   | --------------------------- | ------------------------- |
   | `Name`                      | PF                        |
   | `Targets`                   | `<load balancer VIP>:443` |
   | `Secure`                    | Yes                       |
   | `Trusted Certificate Group` | PF                        |
   | All other parameters        | Accept the defaults       |

3. Click **Save**.

---

---
title: Creating a PingAccess virtual host
description: Go to Access → Virtual Hosts.
component: solution-guides
page_id: solution-guides:data_and_application_security_use_cases:htg_protect_pf_gateway_deploy_pa_create_pa_host
canonical_url: https://docs.pingidentity.com/solution-guides/data_and_application_security_use_cases/htg_protect_pf_gateway_deploy_pa_create_pa_host.html
llms_txt: https://docs.pingidentity.com/solution-guides/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: May 1, 2024
section_ids:
  steps: Steps
---

# Creating a PingAccess virtual host

## Steps

1. Go to **Access → Virtual Hosts**.

2. Click **Add Virtual Host**.

3. Enter the host name that you will use to access the PingFederate runtime engines using the following table as a guide.

   | Parameter                      | Example Value                 |
   | ------------------------------ | ----------------------------- |
   | `Host`                         | `https://<pingfederate_host>` |
   | `Port`                         | 443                           |
   | `Agent Resource Cache TTL (S)` | 900                           |
   | All other parameters           | Accept the defaults           |

4. Click **Save**.

---

---
title: Creating a PingOne OIDC application
description: To configure your AWS EKS cluster for OIDC authentication, you must first create a PingOne OIDC application to acquire the required OIDC Issuer URL and OIDC Client ID.
component: solution-guides
page_id: solution-guides:data_and_application_security_use_cases:htg_config_oidc_authn_aws_eks_custers_p1_oidc
canonical_url: https://docs.pingidentity.com/solution-guides/data_and_application_security_use_cases/htg_config_oidc_authn_aws_eks_custers_p1_oidc.html
llms_txt: https://docs.pingidentity.com/solution-guides/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: April 29, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Creating a PingOne OIDC application

## About this task

To configure your AWS EKS cluster for OIDC authentication, you must first create a PingOne OIDC application to acquire the required OIDC Issuer URL and OIDC Client ID.

To create a PingOne OIDC application:

## Steps

1. Sign on to your PingOne for Enterprise tenant.

2. Go to **Applications → My Applications → OIDC**.

3. Select **Advanced Configuration**, and click **Next**.

   ![Screen capture showing how to select the Advanced Configuration option for the OIDC application.](_images/fpl1619118809683.png)

4. Type the **Application Name** and **Description**, and click **Next**.

5. In the **Authorization Settings** section, check **Authorization Code** for the **Allowed Grant Types**.

6. To include a client secret, click **Add Secret**. Record the **Client ID** and **Client Secret** for later use. Click **Next**.

   ![Screen capture showing how to configure the Allowed Grant Type authorization setting and where to add a secret for the OIDC application.](_images/zdh1619119258210.png)

7. In the **SSO Flow and Authentication Settings** section, enter the following:

   1. In the **Start SSO URL** field, enter `https://localhost`.

   2. In the **Redirect URIs** field, enter `http://locallhost:8000` and `http://localhost:18000`.

   3. Click **Next**.

      ![Screen capture showing how to add the Start SSO URL and Redirect URIs.](_images/gtk1619119659796.png)

8. Leave the default configuration for **Default User Profile Attribute Contract** and **Connect Scopes**.

9. Configure the required **Attribute Mapping** for the `subject` attribute. Click **Next**.

   ![Screen capture showing how to configure the attribute mapping for the subject attribute.](_images/jvk1619119922504.png)

10. Assign any required **PingOne Groups** for access, and then click **Done**.

---

---
title: Data and Application Security Use Cases
description: Configuring OIDC authentication for AWS EKS clusters
component: solution-guides
page_id: solution-guides:data_and_application_security_use_cases:htg_data_and_app_security_use_cases
canonical_url: https://docs.pingidentity.com/solution-guides/data_and_application_security_use_cases/htg_data_and_app_security_use_cases.html
llms_txt: https://docs.pingidentity.com/solution-guides/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: January 19, 2024
---

# Data and Application Security Use Cases

| Use case                                                                                                                                        | Description                                                                                                                                                                                                                                 |
| ----------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Configuring OIDC authentication for AWS EKS clusters](htg_config_oidc_authn_aws_eks_custers.html)                                              | Open ID Connect (OIDC) supports authentication for Amazon Web Services (AWS) Elastic Kubernetes Service (EKS) clusters. You can configure PingOne as an identity provider (IdP) to provide strong user authentication to your EKS clusters. |
| [Configuring medium-grained application access control through Azure AD, PingFederate, and PingAccess](htg_config_med_grained_app.html)         | PingAccess can interact directly with an OIDC IdP provider, so you don't need to use PingFederate to authenticate against Azure AD.                                                                                                         |
| [Connecting PingFederate to PingAccess using the OIDC protocol](htg_connect_pf_pa_oidc.html)                                                    | Configure authentication between PingFederate and PingAccess using the OpenID Connect (OIDC) protocol.                                                                                                                                      |
| [Protecting PingAccess resources through external IdPs with PingFederate acting as an SP (leveraging FedHub)](htg_protect_pa_resources_pf.html) | Protect PingAccess resources through external IdPs with PingFederate acting as an SP (leveraging FedHub).                                                                                                                                   |
| [Protecting PingFederate behind a gateway deployment of PingAccess](htg_protect_pf_gateway_deployment_pa.html)                                  | Learn how to proxy PingAccess to protect PingFederate in a gateway deployment.                                                                                                                                                              |

---

---
title: Exporting the PingFederate certificate that protects the runtime listener
description: Log in to your PingFederate administration console.
component: solution-guides
page_id: solution-guides:data_and_application_security_use_cases:htg_protect_pf_gateway_deploy_pa_export_pf_cert
canonical_url: https://docs.pingidentity.com/solution-guides/data_and_application_security_use_cases/htg_protect_pf_gateway_deploy_pa_export_pf_cert.html
llms_txt: https://docs.pingidentity.com/solution-guides/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: May 1, 2024
section_ids:
  steps: Steps
---

# Exporting the PingFederate certificate that protects the runtime listener

## Steps

1. Log in to your PingFederate administration console.

2. Go to **Security → SSL Server Certificates**.

3. Go to **Select Action → Export**.

4. Select **Certificate Only** and click **Next**.

5. Click **Export**.

6. Save the certificate file to a location you can easily reference.

---

---
title: Importing the certificate in PingAccess
description: Log in to your PingAccess administration console.
component: solution-guides
page_id: solution-guides:data_and_application_security_use_cases:htg_protect_pf_gateway_deploy_pa_import_cert
canonical_url: https://docs.pingidentity.com/solution-guides/data_and_application_security_use_cases/htg_protect_pf_gateway_deploy_pa_import_cert.html
llms_txt: https://docs.pingidentity.com/solution-guides/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: May 1, 2024
section_ids:
  steps: Steps
---

# Importing the certificate in PingAccess

## Steps

1. Log in to your PingAccess administration console.

2. Go to **Security → Certificates**.

3. To import a new certificate, click the plus icon ([icon: circle-plus, set=fa]).

4. Under **Name**, specify **PF**.

5. Click **Choose File** and select the certificate from Step 1. Click **Add**.

6. Drag the imported certificate from the Certificates pane to the Trusted Certificate Groups pane.

---

---
title: Performing final steps
description: Test your application in a web browser.
component: solution-guides
page_id: solution-guides:data_and_application_security_use_cases:htg_connect_pf_pa_oidc_final_steps
canonical_url: https://docs.pingidentity.com/solution-guides/data_and_application_security_use_cases/htg_connect_pf_pa_oidc_final_steps.html
llms_txt: https://docs.pingidentity.com/solution-guides/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: April 29, 2024
section_ids:
  steps: Steps
  result: Result:
---

# Performing final steps

## Steps

1. Test your application in a web browser.

   Access your application behind PingAccess (for example, https\://localhost:3000/*\<APP\_NAME>*).

   ### Result:

   You're redirected to PingFederate to authenticate and can access the application.

2. Add header printing to your application to verify that your application has access to the data that PingAccess is sending.

   Detailed steps differ by application and programming language. The following resources provide more information for specific programming languages.

   | Language | Sample Header Code                                                                                |
   | -------- | ------------------------------------------------------------------------------------------------- |
   | Java     | `https://docs.oracle.com/en/java/javase/21/docs/api/java.net.http/java/net/http/HttpHeaders.html` |
   | C#       | `https://learn.microsoft.com/dotnet/api/system.net.httpwebresponse.getresponseheader`             |
   | PHP      | `http://php.net/manual/en/function.headers-list.php`                                              |
   | Drupal   | `https://api.drupal.org/api/drupal/includes%21bootstrap.inc/function/drupal_get_http_header/7.x`  |

3. Remove any local login to your application because your application is now behind PingAccess.

   Detailed steps differ by application and programming language.

4. Configure your application to use headers for login.

   Detailed steps differ by application and programming language.

---

---
title: Protecting PingAccess resources through external IdPs with PingFederate acting as an SP (leveraging FedHub)
description: Components
component: solution-guides
page_id: solution-guides:data_and_application_security_use_cases:htg_protect_pa_resources_pf
canonical_url: https://docs.pingidentity.com/solution-guides/data_and_application_security_use_cases/htg_protect_pa_resources_pf.html
llms_txt: https://docs.pingidentity.com/solution-guides/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: February 16, 2022
section_ids:
  before-you-begin: Before you begin
  about-this-task: About this task
  steps: Steps
  result: Result:
  result-2: Result:
  result-3: Result:
  result-4: Result:
  result-5: Result:
  result-6: Result:
  result-7: Result:
---

# Protecting PingAccess resources through external IdPs with PingFederate acting as an SP (leveraging FedHub)

## Before you begin

**Components**

* PingFederate 10.3

* PingAccess 6.3

## About this task

Follow these steps to connect PingFederate as an SP to external IdP and configure an SP connection to bridge the IdP connection for the Federation Hub flow.

## Steps

1. In PingFederate admin console, from **Authentication → Integration → IdP Connections**, click **Create Connection**.

2. Connect and configure PingFederate as the service provider (SP) to your external identity provider (IdP)

3. Create a new authentication policy contract with the attributes needed to be passed to PingAccess.

   |   |                                                                               |
   | - | ----------------------------------------------------------------------------- |
   |   | If you have previously integrated PingFederate and PingAccess, bypass step 3. |

   1. From **Authentication → Policies → Policy Contracts**, click **Create New Contract**.

   2. Configure the **Contract Info** and **Contract Attributes** tabs and then click **Next**. Click **Done**.

4. Create a new IdP connection to the SP.

   |   |                                                                                                                                                                                                                |
   | - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | If you created a test SP connection to have PingFederate function as the test IdP, configure the IdP connection to match the SP connection. Otherwise, configure the IdP connection to match your external SP. |

   1. From **Authentication → Integration → IdP Connections**, click **Create Connection**.

   2. On the **Connection Type** screen, select the **Browser SSO Profiles** checkbox. Click **Next**.

   3. On the **Connection Options** screen, select the **Browser SSO** and **OAuth Attribute Mapping** checkboxes. Click **Next**.

   4. Configure the **General Info** screen. Click **Next**.

   5. On the **Browser SSO** screen, click **Configure Browser SSO**.

   6. On the **SAML Profiles** screen, select the **IDP-Initiated SSO** and**SP-Initiated SSO** checkboxes. Click **Next**.

   7. On the **User-Session Created** screen, click **Configure User-Session Creation**.

      ### Result:

      The **User-Session Creation** window displays.

   8. On the **Identity Mapping** screen, select **Account Mapping**. Click **Next**.

   9. On the **Attribute Contract** screen, configure the same attributes as Step 3. Click **Next**.

   10. On the **Target Session Mapping** screen, click **Map New Authentication Policy**.

       ### Result:

       The **Authentication Policy Mapping** window displays.

   11. From the **Authentication Policy Contract** menu, select the appropriate contract. Click **Next**.

   12. Configure the rest of the Authentication Policy Mapping screens. Click **Done**.

       ### Result:

       After clicking **Done**, the system will automatically return you to the **User-Session Creation** screen.

   13. Click **Next** and **Done**.

       ### Result:

       You return to the **Browser SSO** screen.

   14. On the **OAuth Attribute Mapping**tab, click **Map to OAuth via Authentication Policy Contract** and then select the appropriate contact from the **Map to OAuth Via Authentication Policy Contract** list. Click **Next**.

   15. Click **Configure Protocol Settings**.

       ### Result:

       The **Protocol Settings** screen displays.

   16. Configure the **Protocol Settings** tabs and then click **Next**. Click **Done**.

       ### Result:

       You automatically return to the Browser SSO tab on the IdP Connection window.

   17. On the **Credentials** screen, click **Configure Credentials**. Configure the credentials and then click **Next**. Click **Done**.

       ### Result:

       You automatically return to the **Credentials** tab on the **IdP Connection** window.

   18. On the **Activation & Summary** screen, click **Save** and then click **Done**.

5. Configure the authentication policy contract mapping.

   |   |                                                              |
   | - | ------------------------------------------------------------ |
   |   | If you are using an existing policy contract, bypass step 5. |

   1. Go to **Main → OAuth Server → Authentication Policy Contract Mapping**.

   2. Click the**Authentication Policy Contract** drop-down menu and select a policy contract. Click **Add Mapping**.

   3. Configure the mapping and then click **Save**. Click **Done**.

6. Configure the access token mapping.

   1. From **Applications → OAuth → Access Token Mappings**, map the contract to the access token you are using for PingAccess.

      |   |                                                                                                                                                                                                                                                            |
      | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
      |   | For more information about access token management creation, see [Configuring an access token management instance](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_configuring_access_token_management_instance.html). |

7. From **Authentication → Policies → Policies**, click **Add Policy** and configure a policy to invoke your IdP connection.

8. From **Authentication → Policies → Sessions**, select the **Enable Sessions** checkbox for the session to be saved.

   |   |                                                                                                               |
   | - | ------------------------------------------------------------------------------------------------------------- |
   |   | The **Enable Authentication Sessions for All Sources** checkbox must be selected for the session to be saved. |

9. Click **Save**.

---

---
title: Protecting PingFederate behind a gateway deployment of PingAccess
description: Learn how to proxy PingAccess to protect PingFederate in a gateway deployment.
component: solution-guides
page_id: solution-guides:data_and_application_security_use_cases:htg_protect_pf_gateway_deployment_pa
canonical_url: https://docs.pingidentity.com/solution-guides/data_and_application_security_use_cases/htg_protect_pf_gateway_deployment_pa.html
llms_txt: https://docs.pingidentity.com/solution-guides/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: January 19, 2023
section_ids:
  components: Components
  before-you-begin: Before you begin
  exporting-the-pingfederate-certificate-that-protects-the-runtime-listener: Exporting the PingFederate certificate that protects the runtime listener
  steps: Steps
  importing-the-certificate-in-pingaccess: Importing the certificate in PingAccess
  steps-2: Steps
  creating-a-pingaccess-site-to-protect-pingfederate: Creating a PingAccess site to protect PingFederate
  steps-3: Steps
  creating-a-pingaccess-virtual-host: Creating a PingAccess virtual host
  steps-4: Steps
  creating-a-pingaccess-application-leveraging-the-site-and-the-virtual-host: Creating a PingAccess application leveraging the site and the virtual host
  steps-5: Steps
  creating-a-key-pair-associated-with-the-new-pingfederate-host-name: Creating a key pair associated with the new PingFederate host name
  steps-6: Steps
  tying-the-newly-imported-key-pair-to-the-associated-virtual-host: Tying the newly imported key pair to the associated virtual host
  steps-7: Steps
  setting-pingaccesss-token-provider-to-match-the-pingaccess-application: Setting PingAccess's token provider to match the PingAccess application
  steps-8: Steps
  updating-pingfederates-base-url: Updating PingFederate's base URL
  steps-9: Steps
  verifying-that-access-to-pingfederate-routes-through-pingaccess: Verifying that access to PingFederate routes through PingAccess
  steps-10: Steps
---

# Protecting PingFederate behind a gateway deployment of PingAccess

Learn how to proxy PingAccess to protect PingFederate in a gateway deployment.

## Components

* PingFederate 9.2

* PingAccess 5.2

## Before you begin

Make sure the components are installed and running.

|   |                                                                |
| - | -------------------------------------------------------------- |
|   | This configuration does not support X.509 and IWA connections. |

## Exporting the PingFederate certificate that protects the runtime listener

### Steps

1. Log in to your PingFederate administration console.

2. Go to **Security → SSL Server Certificates**.

3. Go to **Select Action → Export**.

4. Select **Certificate Only** and click **Next**.

5. Click **Export**.

6. Save the certificate file to a location you can easily reference.

## Importing the certificate in PingAccess

### Steps

1. Log in to your PingAccess administration console.

2. Go to **Security → Certificates**.

3. To import a new certificate, click the plus icon ([icon: circle-plus, set=fa]).

4. Under **Name**, specify **PF**.

5. Click **Choose File** and select the certificate from Step 1. Click **Add**.

6. Drag the imported certificate from the Certificates pane to the Trusted Certificate Groups pane.

## Creating a PingAccess site to protect PingFederate

### Steps

1. Go to **Sites → Add Site**.

2. Create a PingAccess site using the following table as a guide.

   | Parameter                   | Example Value             |
   | --------------------------- | ------------------------- |
   | `Name`                      | PF                        |
   | `Targets`                   | `<load balancer VIP>:443` |
   | `Secure`                    | Yes                       |
   | `Trusted Certificate Group` | PF                        |
   | All other parameters        | Accept the defaults       |

3. Click **Save**.

## Creating a PingAccess virtual host

### Steps

1. Go to **Access → Virtual Hosts**.

2. Click **Add Virtual Host**.

3. Enter the host name that you will use to access the PingFederate runtime engines using the following table as a guide.

   | Parameter                      | Example Value                 |
   | ------------------------------ | ----------------------------- |
   | `Host`                         | `https://<pingfederate_host>` |
   | `Port`                         | 443                           |
   | `Agent Resource Cache TTL (S)` | 900                           |
   | All other parameters           | Accept the defaults           |

4. Click **Save**.

## Creating a PingAccess application leveraging the site and the virtual host

### Steps

1. Go to **Applications → Add Application**.

2. Enter the applicable parameters using the following table as a guide.

   | Parameter              | Example Value                     |
   | ---------------------- | --------------------------------- |
   | `Name`                 | PF                                |
   | `Context Root`         | /                                 |
   | `Virtual Host(s)`      | `https://<pingfederate_host>:443` |
   | `Application Type`     | Web                               |
   | `Web Session`          | None                              |
   | `Web Identity Mapping` | None                              |
   | `Destination`          | Site                              |
   | `Site`                 | PF                                |
   | `Require HTTPS`        | Yes                               |
   | `Enabled`              | Yes                               |
   | All other parameters   | Accept the defaults               |

3. Click **Save**.

## Creating a key pair associated with the new PingFederate host name

### Steps

1. Go to **Security → Key Pairs**.

2. Click **Add Key Pair** and enter the applicable parameters using the following table as a guide.

   | Parameter                             | Example Value                 |
   | ------------------------------------- | ----------------------------- |
   | `Alias`                               | PF Master                     |
   | `Common Name`                         | `https://<pingfederate_host>` |
   | `Subject Alternative Name - DNS Name` | `https://<pingfederate_host>` |
   | All other parameters                  | Accept the defaults           |

   |   |                                                                                                                                                                                                                                                                                                                                                                                                      |
   | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | To avoid a "Not Secure" warning in your browser, a signed certificate is required. Use PingFederate to generate a certificate signing request (CSR) and import the CSR response, as described in [Manage SSL server certificates](https://cdn-docs.pingidentity.com/archive/pdf/pingfederate/pingfederate-92.pdf#page=210). The certificate can be self-signed or signed by a certificate authority. |

3. Click **Save**.

## Tying the newly imported key pair to the associated virtual host

### Steps

1. Go to **Networking → Listeners**.

2. In the Engine Key Pairs pane, change `PF Master` to the base URL of the PingAccess virtual host and then click **Save**. Accept the defaults for all other parameters.

## Setting PingAccess's token provider to match the PingAccess application

### Steps

1. Go to **System → Token Provider**.

2. Create the token provider using the following table as a guide.

   |   |                                                                                                                                                        |
   | - | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
   |   | The host and port must match the host and port settings in [Creating a PingAccess virtual host](htg_protect_pf_gateway_deploy_pa_create_pa_host.html). |

   | Parameter            | Example Value                 |
   | -------------------- | ----------------------------- |
   | `Host`               | `https://<pingfederate_host>` |
   | `Port`               | 443                           |
   | `Audit Level`        | Yes                           |
   | All other parameters | Accept the defaults           |

3. Click **Save**.

## Updating PingFederate's base URL

### Steps

1. Log in to your PingFederate administration console.

2. Go to **System → Protocol Settings → Federation Info** and change `Base URL` to the base URL and port of the PingAccess virtual host. Click **Save**.

   |   |                                                                                                                     |
   | - | ------------------------------------------------------------------------------------------------------------------- |
   |   | If the base URL is invalid, PingFederate will not be accessible. Make sure the base URL is valid before proceeding. |

## Verifying that access to PingFederate routes through PingAccess

### Steps

1. In a browser window, go to `https://Virtual Host and Port/pf/heartbeat.ping`. This should produce a valid response from PingFederate.

2. In a browser window, go to `https://Virtual Host and Port/pa/heartbeat.ping`. This should produce a valid response from PingAccess.

---

---
title: Setting PingAccess&#8217;s token provider to match the PingAccess application
description: Go to System → Token Provider.
component: solution-guides
page_id: solution-guides:data_and_application_security_use_cases:htg_protect_pf_gateway_deploy_pa_match_token_app
canonical_url: https://docs.pingidentity.com/solution-guides/data_and_application_security_use_cases/htg_protect_pf_gateway_deploy_pa_match_token_app.html
llms_txt: https://docs.pingidentity.com/solution-guides/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: May 1, 2024
section_ids:
  steps: Steps
---

# Setting PingAccess's token provider to match the PingAccess application

## Steps

1. Go to **System → Token Provider**.

2. Create the token provider using the following table as a guide.

   |   |                                                                                                                                                        |
   | - | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
   |   | The host and port must match the host and port settings in [Creating a PingAccess virtual host](htg_protect_pf_gateway_deploy_pa_create_pa_host.html). |

   | Parameter            | Example Value                 |
   | -------------------- | ----------------------------- |
   | `Host`               | `https://<pingfederate_host>` |
   | `Port`               | 443                           |
   | `Audit Level`        | Yes                           |
   | All other parameters | Accept the defaults           |

3. Click **Save**.

---

---
title: Setting up Azure AD as an OIDC provider for PingAccess in PingFederate
description: This procedure assumes that you have configured PingFederate and PingAccess to talk to each other through OIDC. You need to add Azure AD as an authentication source for PingAccess in PingFederate.
component: solution-guides
page_id: solution-guides:data_and_application_security_use_cases:htg_config_med_grained_app_ad_oidc_pa
canonical_url: https://docs.pingidentity.com/solution-guides/data_and_application_security_use_cases/htg_config_med_grained_app_ad_oidc_pa.html
llms_txt: https://docs.pingidentity.com/solution-guides/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: April 29, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
  result: Result:
---

# Setting up Azure AD as an OIDC provider for PingAccess in PingFederate

## About this task

This procedure assumes that you have configured PingFederate and PingAccess to talk to each other through OIDC. You need to add Azure AD as an authentication source for PingAccess in PingFederate.

For general instructions, see [Create an OpenID Connect IdP connection](https://cdn-docs.pingidentity.com/archive/pdf/pingfederate/pingfederate-91.pdf#page=460)

## Steps

1. From the Authentication Selector screen in PingFederate, select the **Add or Update AuthN Context Attribute**box next to the PingAccess entry, update your selector result values to include Azure AD as an authentication requirement, and click **Save**. See [Configure the Requested AuthN Context Authentication Selector](https://cdn-docs.pingidentity.com/archive/pdf/pingfederate/pingfederate-91.pdf#page=61).

2. Ensure there is a path in your authentication policy tree to include your new authentication requirement for Azure, verify that you are fulfilling your policy contracts, and click **Save**. See [Defining authentication policies](https://cdn-docs.pingidentity.com/archive/pdf/pingfederate/pingfederate-91.pdf#page=233) and [Define authentication policies based on group membership information](https://cdn-docs.pingidentity.com/archive/pdf/pingfederate/pingfederate-91.pdf#page=237).

3. Under **Authorization Server Settings**, extend the persistent grant to map the Azure AD group into the OIDC token to PingAccess. See [Define grant contract fulfillment for IdP adapter mapping](https://cdn-docs.pingidentity.com/archive/pdf/pingfederate/pingfederate-91.pdf#page=286).

4. Extend the access token attribute contract to include groups, fulfill the persistent grants from the authentication policy contract, and fulfill the access token mapping with the persistent grant. See [Configure policy and ID token settings](https://cdn-docs.pingidentity.com/archive/pdf/pingfederate/pingfederate-91.pdf#page=316).

5. In your OIDC policy, map from the access token or perform any additional lookups against local data stores. See [Configure IdP adapter attribute sources and user lookup](https://cdn-docs.pingidentity.com/archive/pdf/pingfederate/pingfederate-91.pdf#page=227).

6. Go to PingAccess and write a web session attribute rule for the group membership to which the rule applies. See [Configure session management](https://cdn-docs.pingidentity.com/archive/pdf/pingaccess/pingaccess-72.pdf#page=121).

   |   |                                                                                                   |
   | - | ------------------------------------------------------------------------------------------------- |
   |   | Azure AD does not provide friendly names for their groups and instead returns them as object IDs. |

   Apply this rule as needed for your specific use case, application, or API.

   ### Result:

   PingAccess verifies group membership in Azure AD and uses this group membership to enforce medium-grained access control.