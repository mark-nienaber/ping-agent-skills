---
title: identitycloud-go-client (Go)
description: Install and configure the identitycloud-go-client Go module to connect your application to the Advanced Identity Cloud tenant management API
component: config-automation-management-sdks
page_id: config-automation-management-sdks::products/pingone_advanced_identity_cloud/languages/go/getting_started
canonical_url: https://developer.pingidentity.com/config-automation-management-sdks/products/pingone_advanced_identity_cloud/languages/go/getting_started.html
llms_txt: https://developer.pingidentity.com/config-automation-management-sdks/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: March 19, 2025
section_ids:
  prerequisites: Prerequisites
  getting-started: Getting started
  connect-to-the-service: Connect to the service
  service-account: Service account
  more-information: More information
---

# identitycloud-go-client (Go)

|   |                                                                                                                                                                                                                                  |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The `identitycloud-go-client` SDK has not yet been released to version 1.0.0. Although general use of the SDK is not expected to change and is stable, later versions could contain minor changes to package and function names. |

Use the PingOne Advanced Identity Cloud Go SDK to connect your Go application to your Advanced Identity Cloud deployment.

The [identitycloud-go-client](https://github.com/pingidentity/identitycloud-go-client) module provides API bindings to the Advanced Identity Cloud configuration API, allowing developers to invoke API services simply using strongly typed request and response payloads. The module can be included as a dependency in developer code.

|   |                                                                                                                                                                                                                  |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The `identitycloud-go-client` module currently only supports tenant management APIs described at [Advanced Identity Cloud API](https://docs.pingidentity.com/pingoneaic/latest/_attachments/api/) documentation. |

## Prerequisites

The `identitycloud-go-client` module requires a valid Advanced Identity Cloud tenant to be provisioned and accessible.

## Getting started

The following example shows how to include the `identitycloud-go-client` module in a developer project.

If you haven't done so already, initialize a new Go module project:

```
go mod init github.com/mygithubuser/my-go-project
```

Use the standard Go commands to install `identitycloud-go-client` to the project:

```
go get github.com/pingidentity/identitycloud-go-client
```

## Connect to the service

The following sections describe the available options to connect the configuration management SDK to the Advanced Identity Cloud service.

### Service account

When connecting to the Advanced Identity Cloud service, a service account that has been provisioned access the required API features must be used.

Learn more about the Identity Cloud REST API, how to configure access using service accounts and find the complete list of available scopes at the [Advanced Identity Cloud Service accounts](https://docs.pingidentity.com/pingoneaic/latest/tenants/service-accounts.html) documentation.

When initiating the Go client SDK, the service account credentials should be provided with the list of scopes the application needs, as shown in the following example:

```go
package main

import (
	"context"
	"fmt"

	"github.com/pingidentity/identitycloud-go-client/identitycloud"
)

func main() {

	aicEnvironmentFqdn := "my-aic-fqdn.id.forgerock.io"
	aicServiceAccountId := "service-account-id-value"
	aicServiceAccountPrivateKey := `{"keys":[{"alg":"RS256","e":"AQAB","n":"....","kty":"RSA","use":"sig"}]}`
	aicServiceAccountScopes := []string{
		"fr:idc:certificate:*",
		"fr:idc:content-security-policy:*",
		"fr:idc:cookie-domain:*",
		"fr:idc:custom-domain:*",
		"fr:idc:esv:*",
		"fr:idc:promotion:*",
		"fr:idc:sso-cookie:*",
	}

	// Initialize the API client
	clientConfig := identitycloud.NewConfiguration()
	clientConfig.Servers = identitycloud.ServerConfigurations{
		{
			URL: fmt.Sprintf("https://%s", aicEnvironmentFqdn),
		},
	}

	apiClient := identitycloud.NewAPIClient(clientConfig)

	// Set OAuth 2.0 credentials in the Go context
	oauth2AuthContext := context.WithValue(context.Background(), identitycloud.ContextOAuth2, identitycloud.ServiceAccountTokenSource{
		TenantFqdn:               aicEnvironmentFqdn,
		ServiceAccountId:         aicServiceAccountId,
		ServiceAccountPrivateKey: aicServiceAccountPrivateKey,
		Scopes:                   aicServiceAccountScopes,
	})

	// Call an API from the `apiClient` object
	readResponse, httpResponse, err := apiClient.PromotionAPI.CheckLock(oauth2AuthContext).Execute()
	if err != nil {
		panic(err)
	}

	fmt.Printf("Response HTTP Code: %d", httpResponse.StatusCode)
	fmt.Printf("Response: %v", readResponse)
}
```

## More information

* [PingOne Advanced Identity Cloud documentation](https://docs.pingidentity.com/pingoneaic/latest/overview.html)

* [`identitycloud-go-client` on the Go Package Repository](https://pkg.go.dev/github.com/pingidentity/identitycloud-go-client/identitycloud)

* [`identitycloud-go-client` on GitHub](https://github.com/pingidentity/identitycloud-go-client)

---

---
title: Introduction to PingDirectory Configuration and User Management SDKs
description: Connect applications to your PingDirectory deployment using the PingDirectory Go client SDK to automate administrative functions
component: config-automation-management-sdks
page_id: config-automation-management-sdks::products/pingdirectory/introduction
canonical_url: https://developer.pingidentity.com/config-automation-management-sdks/products/pingdirectory/introduction.html
llms_txt: https://developer.pingidentity.com/config-automation-management-sdks/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: March 19, 2025
section_ids:
  go-client-sdk: Go Client SDK
---

# Introduction to PingDirectory Configuration and User Management SDKs

Connect your applications and services to perform administrative actions on your PingDirectory deployment.

Use the following SDK client projects to automate administrative functions (including configuration deployment) and to integrate product features with your own code.

The following client libraries and modules are provided by Ping Identity and available to use.

## Go Client SDK

Use the `pingdirectory-go-client` Go module SDK to connect your Go application to your PingDirectory deployment.

[Get Started](languages/go/getting_started.html)

---

---
title: Introduction to PingFederate Configuration and User Management SDKs
description: Connect applications to your PingFederate deployment using the PingFederate Go client SDK to automate administrative functions
component: config-automation-management-sdks
page_id: config-automation-management-sdks::products/pingfederate/introduction
canonical_url: https://developer.pingidentity.com/config-automation-management-sdks/products/pingfederate/introduction.html
llms_txt: https://developer.pingidentity.com/config-automation-management-sdks/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: March 19, 2025
section_ids:
  go-client-sdk: Go Client SDK
---

# Introduction to PingFederate Configuration and User Management SDKs

Connect your applications and services to perform administrative actions on your PingFederate deployment.

Use the following SDK client projects to automate administrative functions (including configuration deployment) and to integrate product features with your own code.

The following client libraries and modules are provided by Ping Identity and available to use.

## Go Client SDK

Use the `pingfederate-go-client` Go module SDK to connect your Go application to your PingFederate deployment.

[Get Started](languages/go/getting_started.html)

---

---
title: Introduction to PingOne Advanced Identity Cloud Configuration and User Management SDKs
description: Connect applications to your PingOne Advanced Identity Cloud tenant using the Go client SDK to automate tenant management
component: config-automation-management-sdks
page_id: config-automation-management-sdks::products/pingone_advanced_identity_cloud/introduction
canonical_url: https://developer.pingidentity.com/config-automation-management-sdks/products/pingone_advanced_identity_cloud/introduction.html
llms_txt: https://developer.pingidentity.com/config-automation-management-sdks/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: March 19, 2025
section_ids:
  go-client-sdk: Go Client SDK
---

# Introduction to PingOne Advanced Identity Cloud Configuration and User Management SDKs

Connect your applications and services to perform administrative actions on your PingOne Advanced Identity Cloud tenant.

|   |                                                                                                                                                                                                                                      |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | The available Configuration and User Management SDKs currently supports only tenant management APIs described in the [Advanced Identity Cloud API](https://docs.pingidentity.com/pingoneaic/latest/_attachments/api/) documentation. |

Use the following SDK client projects to automate administrative functions (including configuration deployment) and to integrate product features with your own code.

The following client libraries and modules are provided by Ping Identity and available to use.

## Go Client SDK

Use the `identitycloud-go-client` Go module SDK to connect your Go application to your Advanced Identity Cloud deployment.

[Get Started](languages/go/getting_started.html)

---

---
title: pingdirectory-go-client (Go)
description: Install and configure the pingdirectory-go-client Go module to connect your application to the PingDirectory configuration API
component: config-automation-management-sdks
page_id: config-automation-management-sdks::products/pingdirectory/languages/go/getting_started
canonical_url: https://developer.pingidentity.com/config-automation-management-sdks/products/pingdirectory/languages/go/getting_started.html
llms_txt: https://developer.pingidentity.com/config-automation-management-sdks/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: March 19, 2025
section_ids:
  prerequisites: Prerequisites
  getting-started: Getting started
  connect-to-the-service: Connect to the service
  http-basic-authentication: HTTP basic authentication
  more-information: More information
---

# pingdirectory-go-client (Go)

|   |                                                                                                                                                                                                                               |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The `pingdirectory-go-client` SDK has not yet been released to version 1.0.0. While general use of the SDK is not expected to change and is stable, later versions could contain minor changes to package and function names. |

Use the PingDirectory Go SDK to connect your Go application to your PingDirectory deployment.

The [pingdirectory-go-client](https://github.com/pingidentity/pingdirectory-go-client) module provides API bindings to the PingDirectory configuration API, allowing developers to invoke API services simply using strongly typed request and response payloads. The module can be included as a dependency in developer code.

## Prerequisites

The `pingdirectory-go-client` module requires a running PingDirectory instance. The module requires the use of the PingDirectory Configuration API, which must be enabled on the service and should be configured to run on the HTTPS Connection Handler.

Learn more about the PingDirectory Configuration API in [Using the Configuration API](https://docs.pingidentity.com/pingdirectory/latest/pingdirectoryproxy_server_administration_guide/pd_proxy_use_config_api.html) in the PingDirectory documentation.

## Getting started

The following example shows how to include the `pingdirectory-go-client` module in a developer project.

If you haven't done so already, initialize a new Go module project:

```
go mod init github.com/mygithubuser/my-go-project
```

To determine the version of the `pingdirectory-go-client` to use, take the full PingDirectory server version and omit the version separator.

For example, for a client for PingDirectory version 10.2.0.0, the version of the Go client to use will be v10200.

Use the standard Go commands to install `pingdirectory-go-client` to the project for your version of PingDirectory:

```
go get github.com/pingidentity/pingdirectory-go-client/v10200
```

## Connect to the service

The following sections describe the available options to connect the configuration management SDK to the PingDirectory service.

### HTTP basic authentication

When connecting to the PingDirectory service, you can use HTTP basic authentication, as in the following example:

```go
package main

import (
	"context"
	"crypto/tls"
	"fmt"
	"net/http"

	pingdirectory "github.com/pingidentity/pingdirectory-go-client/v10200/configurationapi"
)

func main() {

	pdHttpHost := "https://localhost:1443"
	pdUsername := "cn=administrator"
	pdPassword := "my-admin-password"

	// Initialize the API client
	clientConfig := pingdirectory.NewConfiguration()
	clientConfig.Servers = pingdirectory.ServerConfigurations{
		{
			URL: pdHttpHost + "/config",
		},
	}
	tr := &http.Transport{
		TLSClientConfig: &tls.Config{
			InsecureSkipVerify: false,
		},
	}
	clientConfig.HTTPClient = &http.Client{Transport: tr}

	apiClient := pingdirectory.NewAPIClient(clientConfig)

	// Set Basic Auth credentials in the Go context
	basicAuthContext := context.WithValue(context.Background(), pingdirectory.ContextBasicAuth, pingdirectory.BasicAuth{
		UserName: pdUsername,
		Password: pdPassword,
	})

	// Call an API from the `apiClient` object
	readResponse, httpResponse, err := apiClient.RootDnAPI.GetRootDn(basicAuthContext).Execute()
	if err != nil {
		panic(err)
	}

	fmt.Printf("Response HTTP Code: %d", httpResponse.StatusCode)
	fmt.Printf("Response: %v", readResponse)
}
```

## More information

* [PingDirectory documentation](https://docs.pingidentity.com/pingdirectory/latest/pd_ds_landing_page.html)

* [`pingdirectory-go-client` on the Go Package Repository](https://pkg.go.dev/github.com/pingidentity/pingdirectory-go-client)

* [`pingdirectory-go-client` on GitHub](https://github.com/pingidentity/pingdirectory-go-client)

---

---
title: pingfederate-go-client (Go)
description: Install and configure the pingfederate-go-client Go module to connect your application to the PingFederate administrative API
component: config-automation-management-sdks
page_id: config-automation-management-sdks::products/pingfederate/languages/go/getting_started
canonical_url: https://developer.pingidentity.com/config-automation-management-sdks/products/pingfederate/languages/go/getting_started.html
llms_txt: https://developer.pingidentity.com/config-automation-management-sdks/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: March 19, 2025
section_ids:
  prerequisites: Prerequisites
  getting-started: Getting started
  connect-to-the-service: Connect to the service
  oauth-2-0-client-credentials: OAuth 2.0 client credentials
  http-basic-authentication: HTTP basic authentication
  more-information: More information
---

# pingfederate-go-client (Go)

|   |                                                                                                                                                                                                                              |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The `pingfederate-go-client` SDK has not yet been released to version 1.0.0. While general use of the SDK is not expected to change and is stable, later versions could contain minor changes to package and function names. |

Use the PingFederate Go SDK to connect your Go application to your PingFederate deployment.

The [pingfederate-go-client](https://github.com/pingidentity/pingfederate-go-client) module provides API bindings to the PingFederate configuration API, allowing developers to invoke API services simply using strongly typed request and response payloads. The module can be included as a dependency in developer code.

## Prerequisites

The `pingfederate-go-client` module requires a running PingFederate admin node instance. The module requires the use of the PingFederate administrative API.

Learn more about the PingFederate administrative API and how to configure access in the [PingFederate administrative API](https://docs.pingidentity.com/pingfederate/latest/developers_reference_guide/pf_admin_api.html) documentation.

## Getting started

The following example shows how to include the `pingfederate-go-client` module in a developer project.

If you haven't done so already, initialize a new Go module project:

```
go mod init github.com/mygithubuser/my-go-project
```

To determine the version of the `pingfederate-go-client` to use, take the full PingFederate server version and omit the version separator.

For example, for a client for PingFederate version 12.2.0, the version of the Go client to use will be v1220.

Use the standard Go commands to install `pingfederate-go-client` to the project for your version of PingFederate:

```
go get github.com/pingidentity/pingfederate-go-client/v1220
```

## Connect to the service

The following sections describe the available options to connect the configuration management SDK to the PingFederate service.

### OAuth 2.0 client credentials

When connecting to the PingFederate service, you can use the OAuth 2.0 client credentials grant as in the following example:

```go
package main

import (
	"context"
	"crypto/tls"
	"fmt"
	"net/http"

	pingfederate "github.com/pingidentity/pingfederate-go-client/v1220/configurationapi"
)

func main() {

	pfHttpHost := "https://localhost:9999"
	pfAdminApiPath := "/pf-admin-api/v1"
	pfTokenUrl := "https://localhost:9031/as/token.oauth2"
	pfClientId := "my-client-id"
	pfClientSecret := "my-client-secret"
	pfScopes := []string{"test-scope1", "test-scope2"}

	// Initialize the API client
	clientConfig := pingfederate.NewConfiguration()
	clientConfig.DefaultHeader["X-Xsrf-Header"] = "PingFederate"
	clientConfig.DefaultHeader["X-BypassExternalValidation"] = "false"
	clientConfig.Servers = pingfederate.ServerConfigurations{
		{
			URL: pfHttpHost + pfAdminApiPath,
		},
	}
	tr := &http.Transport{
		TLSClientConfig: &tls.Config{
			InsecureSkipVerify: false,
		},
	}
	clientConfig.HTTPClient = &http.Client{Transport: tr}

	apiClient := pingfederate.NewAPIClient(clientConfig)

	// Set OAuth 2.0 credentials in the Go context
	oauth2AuthContext := context.WithValue(context.Background(), pingfederate.ContextOAuth2, pingfederate.OAuthValues{
		Transport:    tr,
		TokenUrl:     pfTokenUrl,
		ClientId:     pfClientId,
		ClientSecret: pfClientSecret,
		Scopes:       pfScopes,
	})

	// Call an API from the `apiClient` object
	readResponse, httpResponse, err := apiClient.IdpAdaptersAPI.GetIdpAdapters(oauth2AuthContext).Execute()
	if err != nil {
		panic(err)
	}

	fmt.Printf("Response HTTP Code: %d", httpResponse.StatusCode)
	fmt.Printf("Response: %v", readResponse)
}
```

### HTTP basic authentication

When connecting to the PingFederate service, you can use HTTP basic authentication as in the following example:

```go
package main

import (
	"context"
	"crypto/tls"
	"fmt"
	"net/http"

	pingfederate "github.com/pingidentity/pingfederate-go-client/v1220/configurationapi"
)

func main() {

	pfHttpHost := "https://localhost:9999"
	pfAdminApiPath := "/pf-admin-api/v1"
	pfUsername := "administrator"
	pfPassword := "my-admin-password"

	// Initialize the API client
	clientConfig := pingfederate.NewConfiguration()
	clientConfig.DefaultHeader["X-Xsrf-Header"] = "PingFederate"
	clientConfig.DefaultHeader["X-BypassExternalValidation"] = "false"
	clientConfig.Servers = pingfederate.ServerConfigurations{
		{
			URL: pfHttpHost + pfAdminApiPath,
		},
	}
	tr := &http.Transport{
		TLSClientConfig: &tls.Config{
			InsecureSkipVerify: false,
		},
	}
	clientConfig.HTTPClient = &http.Client{Transport: tr}

	apiClient := pingfederate.NewAPIClient(clientConfig)

	// Set Basic Auth credentials in the Go context
	basicAuthContext := context.WithValue(context.Background(), pingfederate.ContextBasicAuth, pingfederate.BasicAuth{
		UserName: pfUsername,
		Password: pfPassword,
	})

	// Call an API from the `apiClient` object
	readResponse, httpResponse, err := apiClient.IdpAdaptersAPI.GetIdpAdapters(basicAuthContext).Execute()
	if err != nil {
		panic(err)
	}

	fmt.Printf("Response HTTP Code: %d", httpResponse.StatusCode)
	fmt.Printf("Response: %v", readResponse)
}
```

## More information

* [PingFederate documentation](https://docs.pingidentity.com/pingfederate/latest/pf_pf_landing_page.html)

* [`pingfederate-go-client` on the Go Package Repository](https://pkg.go.dev/github.com/pingidentity/pingfederate-go-client)

* [`pingfederate-go-client` on GitHub](https://github.com/pingidentity/pingfederate-go-client)