---
title: Network guide
description: PingOne Advanced Services provides you with your own virtual private cloud (VPC) network that you define. This virtual network can connect to any data source and closely resembles the network you operate in your data centers, but in a scalable, secure, cloud environment with data and resource isolation.
component: pingoneadvancedservices
page_id: pingoneadvancedservices:network_guide:p1as_network_guide
canonical_url: https://docs.pingidentity.com/pingoneadvancedservices/network_guide/p1as_network_guide.html
llms_txt: https://docs.pingidentity.com/pingoneadvancedservices/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: January 21, 2026
section_ids:
  _items_not_supported: Items not supported
  _region_deployment_models: Regions and deployment models
  region-deployment-models: Region deployment models
  _network_options: Network options
  choosing_right_model: Choosing the right model
  _internet_only_network: Internet-only network
  internet-only-network-endpoints: Internet-only network endpoints
  _simple_network: Simple network
  _simple_vpn_network: Simple VPN network
  _aws_privatelink_network: AWS PrivateLink network
  _simple_network_endpoints: Simple network endpoints
  _advanced_network: Advanced network
  _ip_requirements: IP requirements
  _direct_connect: Direct Connect (DX) network
  _transit_gateway: Transit Gateway (TGW) network
  _vpn_network: VPN network
  _advanced_network_endpoints: Advanced network endpoints
  _setup_considerations: Setup considerations
  section_tjr_kdh_2cc: VPN setup requirements
  section_ynt_ldh_2cc: AWS PrivateLink requirements
  section_dcn_mdh_2cc: Direct Connect (DX) requirements
  section_cc4_ndh_2cc: Transit Gateway (TGW) peering requirements
  section_xkf_4dh_2cc: Transit Gateway (TGW) RAM share requirements
---

# Network guide

PingOne Advanced Services provides you with your own virtual private cloud (VPC) network that you define. This virtual network can connect to any data source and closely resembles the network you operate in your data centers, but in a scalable, secure, cloud environment with data and resource isolation.

This guide describes each of the network options available for PingOne Advanced Services and the regions and deployment models available. Review this information to become familiar with your options, and work with your Ping Identity team members to select the options that are right for you.

Learn more:

* [Items not supported](#_items_not_supported)

* [Regions and deployment models](#_region_deployment_models)

* [Network options](#_network_options)

* [Setup considerations](#_setup_considerations)

## Items not supported

Although PingOne Advanced Services is hosted in AWS, it doesn't have all the features and functionality available with AWS. Much of the network is automated, so PingOne Advanced Services only supports items and settings that its automation supports.

The PingOne Advanced Services customer hub can only be connected to a single network.The platform does not allow for a production or non-production split.

Nor does it support:

* Authenticated BGP for AWS Site-to-Site VPN tunnels.

* Split the DNS forwarders to on-premise DNS servers (production or non-production, or by environment).

* Private endpoint cross-region redundancy.

Private endpoints cannot be accessed within the cluster due to a NAT loopback limitation with the AWS Network Load Balancer (NLB). For example, PingFederate should not connect to the PingDirectory private ingress, but rather the PingDirectory internal cluster name.

## Regions and deployment models

The regions available to you depend on how your account is set up. AWS provides [a wide variety of available regions](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-regions-availability-zones.html#concepts-available-regions), and although PingOne Advanced Services runs within the AWS framework, not all of these regions are supported in PingOne Advanced Services.

The following table lists the regions supported.

| Region group      | Code (region)                      | Name                     |
| ----------------- | ---------------------------------- | ------------------------ |
| **Asia**          | ap-Southeast-1 (url region "sg1" ) | Asia Pacific (Singapore) |
|                   | ap-Southeast-2 (url region "au1" ) | Asia Pacific (Sydney)    |
|                   | ap-Southeast-4 (url region "au2")  | Asia Pacific (Melbourne) |
| **Canada**        | ca-Central-1 (url region "ca1" )   | Canada (Central)         |
| **Europe**        | eu-Central-1 (url region "eu1" )   | Europe (Frankfurt)       |
|                   | eu-West-1 (url region "eu2" )      | Europe (Ireland)         |
| **United States** | us-East-2 (url region "us1" )      | US East (Ohio)           |
|                   | us-West-2 (url region "us2" )      | US West (Oregon)         |

### Region deployment models

Regions can be deployed in a variety of ways, and it's important to choose the model right for you. You can have up to three different regions in a global cluster, or you can deploy close to your user's geographic locations to reduce network latency.

* **Single-region deployments**: With this model, the platform is deployed in 1 of our supported regions. Within each region, the platform is deployed across three availability zones, which are active-active-active within a region.

  > **Collapse: Network diagram**
  >
  > ![A view of a virtual private cloud network with the availability zones.](_images/uzr1721063067374.jpg)

* **Multi-region siloed deployments**: With this model, the platform is deployed in multiple regions, but each region is independent of the others. There is no global cluster. For example, you can have a US region and an EU region, but there is no synchronization between them. Each region has its own administrative accounts and changes must be made manually.

  You might also want your multi-region deployments to remain separate from others. For example, you can have 2 US multi-region deployments and 2 EU multi-region deployments that are siloed from each other and do not communicate.

* **Multi-region clustered deployments**: With this model, the platform can be deployed in up to three different regions in a global cluster, and data and configurations are synchronized across regions using the active-active model, or the active-active-active model, depending on the type of deployment. Note that the Dev and Test environments are always deployed in a single-region format, and Stage and Prod environments are deployed in a multi-region format.

  > **Collapse: Network diagram**
  >
  > ![A diagram of a multi-region clustered deployment.](_images/owk1721074332013.jpg)

## Network options

As you begin your journey with PingOne Advanced Services, it's important to understand the differences between the different network options available. Learn more about these options in [Choosing the right model](#choosing_right_model), and work with your Ping Identity partners to determine which option is right for you:

* **Internet-only network**: The simplest model deployed, with all connectivity into and out of PingOne Advanced Services done over the internet. Ideal for situations where your solutions do not require connections to on-premise systems that are not accessible through the internet. When using this deployment model, you can use other Ping Identity products, such as PingOne and its associated gateways, to access on-premise systems.

  Learn more about the [Internet-only network](#_internet_only_network) option.

* **Simple network**: This option provides connectivity between your on-premise systems, AWS, and third-party cloud environments using HTTPS and LDAPS protocols. Kerberos and RADIUS are not currently supported.

  There are two different options:

  * The Simple VPN option, which requires you to provide IP addresses).

  * The [AWS PrivateLink](https://docs.aws.amazon.com/vpc/latest/privatelink/what-is-privatelink.html) option, which does not require this information and can be used if you have your own AWS instances that you can connect to.

    Learn more about the [Simple network](#_simple_network) option.

* **Advanced network**: With this option, all connectivity options and protocols can be used to integrate your network with your PingOne Advanced Services tenant. Since this is a fully routable deployment, it has a larger IP requirement than the Simple network option.

  Learn more about the [Advanced network](#_advanced_network) option.

  |   |                                                                                                                                                                                                                                        |
  | - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | With this platform, request headers are passed from the client to the AWS Network Load Balancer and through the ingress controller unchanged, but the **X-Forwarded-For** and **X-Real-IP** headers replace whatever is already there. |

### Choosing the right model

If you're unsure of which option might be right for you, answer the following questions:

* Do you need to access systems within your network over a private connection using TCP protocols, such as HTTP, HTTPS, LDAP and LDAPs?

  Both the Simple and Advanced network offer this type of outbound connection from PingOne Advanced Services to your network. With the Internet-only option, you don't have access to the default LDAPS endpoint, but you can request access to the internet-facing endpoint.

* Do you need Kerberos or Radius Authentication?

  The Advanced network model is the only model that supports Kerberos, RADIUS, and other UDPs.

* Are you planning to use PingAccess hosted in PingOne Advanced Services to proxy application traffic back to the application within your network?

  The Advanced network model using AWS DirectConnect and transit gateway peering is an ideal solution for this situation. Although the Simple network model might work, the Site-to-Site VPN is limited to 1.25 GBs, which might not be enough bandwidth. AWS PrivateLink could also be used, but has a limit on the number of services that can be used, and requires teams to coordinate when new applications are added.

* Do you need a redundant connectivity setup?

  A simple VPN allows for only 1 VPN connection (2 if split between production and non-production environments). For redundant connections, Advanced networking is ideal because it allows you to have as many connections as you need.

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | If you select one of these network models and find that it doesn't meet your needs, you can migrate to a different model. Potential migration options are:* From the **Internet only** model to the **Simple network** model

* From the **Simple network** model to the **Internet only** model

* From the **Advanced network** model to the **Internet only** model

* From the **Advanced network** model to the **Simple network** model |

### Internet-only network

The Internet-only option allows you to access your on-premise and cloud-based resources using the public internet. With this option, you can also connect to on-premise directories for authentication purposes. Although you don't have access to the default LDAPS endpoint, you can request access to the internet-facing endpoint.

This option is best if you have cloud and premise-based applications that can be exposed to the public internet and when:

* PingFederate is used as a global authentication authority.

* Standards-based integrations are used to access applications on your network.

* Standards-based integrations are used with SaaS applications.

* Identity and access management solutions are used on your network.

> **Collapse: Internet-only network diagram**
>
> ![A diagram of an Internet-only network.](_images/ynx1721693135026.jpg)

#### Internet-only network endpoints

Public and private endpoints for the Internet-only network model are listed here.

> **Collapse: Default public endpoints**
>
> | Default public endpoints   | URLs                                                                       |
> | -------------------------- | -------------------------------------------------------------------------- |
> | PingAccess                 | `https://pingaccess.<environment>-<customer>.<region>.ping.cloud/`         |
> | PingAccess agent           | `https://pingaccess-agent.<environment>-<customer>.<region>.ping.cloud/`   |
> | PingFederate               | `https://pingfederate.<environment>-<customer>.<region>.ping.cloud/`       |
> | Environment logs           | `https://logs.<environment>-<customer>.<region>.ping.cloud/`               |
> | Environment monitoring     | `https://monitoring.<environment>-<customer>.<region>.ping.cloud/`         |
> | PingFederate admin console | `https://pingfederate-admin.<environment>-<customer>.<region>.ping.cloud/` |
> | PingAccess admin console   | `https://pingaccess-admin.<environment>-<customer>.<region>.ping.cloud/`   |
> | PingCentral                | `https://pingcentral-admin.<customer>.<region>.ping.cloud`                 |
> | Argo CD                    | `https://argocd.<customer>.<region>.ping.cloud/`                           |
> | Prometheus                 | `https://prometheus.<environment>-<customer>.<region>.ping.cloud/`         |

> **Collapse: Optional public endpoints**
>
> | Optional public endpoints                                                                                                 | URLs                                                                              |
> | ------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- |
> | PingFederate admin API                                                                                                    | `https://ext-pingfederate-admin-api.<environment>-<customer>.<region>.ping.cloud` |
> | PingAccess admin API                                                                                                      | `https://ext-pingaccess-admin-api.<environment>-<customer>.<region>.ping.cloud`   |
> | PingDirectory&#xA;&#xA;PingDirectory LDAPS endpoints must be on the allowed list in the PingDirectory connection handler. | `ldaps://ext-pingdirectory-admin.<environment>-<customer>.<region>.ping.cloud`    |
> | PingDirectory API                                                                                                         | `https://ext-pingdirectory.<environment>-<customer>.<region>.ping.cloud`          |
> | PingDelegator                                                                                                             | `https://ext-pingdelegator.<environment>-<customer>.<region>.ping.cloud`          |
> | PingFederate global (multi-region only)                                                                                   | `https://pf.<environment>.global.<customer>.ping.cloud`                           |
> | PingAccess global (multi-region only)                                                                                     | `https://pa.<environment>.global.<customer>.ping.cloud`                           |

### Simple network

The Simple network option offers secure connectivity between your resources in on-premise, AWS, or third-party cloud environments.

This option is best if you:

* Complete authentication from PingOne Advanced Services to a data source located either on-premise or in another cloud environment.

* Can have log streaming available on either a public or private network.

There are two different types of Simple network options available:

* [Simple VPN network](#_simple_vpn_network)

* [AWS PrivateLink network](#_aws_privatelink_network)

#### Simple VPN network

The Simple VPN network option supports a wide range of protocols, such as LDAPS and HTTPS, to connect to your resources, including Oracle, Active Directory, and LDAP. The VPN connection also supports REST and some custom protocols in your network.

There are two different types of Simple VPN networks:

* Single VPN network

  This model uses a single VPN connection for each region.

  > **Collapse: Single VPN network diagram**
  >
  > ![Diagram of a Single VPN network.](_images/ofs1721836467336.jpg)

* Split VPN network

  With this model, one connection is used for production environments (Prod and Stage), and the other connection is used for non-production environments (Dev and Test). If a split VPN connection is configured, the customer must supply a unique, customer-side router IP address for each connection. They are not redundant connections. Refer to the following diagram for details.

  > **Collapse: Split VPN network diagram**
  >
  > ![Diagram of a split VPN network.](_images/xmi1721753896703.jpg)

Additional items to consider include:

* The type of VPN used must be on the [list of VPNs supported by AWS](https://ec2-downloads.s3.amazonaws.com/2009-07-15/customer-gateway-config-formats.xml).

* A Site-to-Site VPN connection is used to connect your remote network to a VPC, which requires you to provide IP addresses. Each Site-to-Site VPN connection has two tunnels, with each tunnel using a unique public IP address. You should configure both tunnels for redundancy. Learn more in [Tunnel options for your Site-to-Site VPN connection](https://docs.aws.amazon.com/vpn/latest/s2svpn/VPNTunnels.html) in the AWS documentation.

* For this type of network, you will need to provide a /24 CIDR block from your RFC1918 IP space for the VPN landing zone. All the private PingOne Advanced Services private endpoints that you connect to will be within the specified IP range in your AWS account.

* These networks are not mutually exclusive, so both can be used at the same time, if appropriate.

  Learn more in [What is AWS Site-to-Site VPN?](https://docs.aws.amazon.com/vpn/latest/s2svpn/VPC_VPN.html) in the AWS documentation. Learn more about setup items you might need to consider in [Setup considerations](#_setup_considerations).

#### AWS PrivateLink network

If you have your own AWS infrastructure and already established network connectivity and routing to and from it, the AWS PrivateLink network might be the right option for you. It does not require you to provide IP addresses for development or connectivity because IP space is hosted within your AWS Virtual Private Cloud (VPC).

This network option might also be appropriate if you need TCP connectivity and can be used in conjunction with a Simple VPN network.

Unlike the Simple VPN network, it is not a multipurpose connection. Instead, consider which services will be exposed for each environment and ensure they can be accessed using the appropriate protocol, such as HTTPS (API endpoints for PingAccess, PingFederate, and PingDirectory) and LDAPS.

1. Set up AWS PrivateLink for each of your PingOne Advanced Services environments.

2. Then, set up AWS PrivateLink endpoints in your AWS account that point to the exposed services.

3. Finally, set up a private hosted zone that contains the required hostnames in DNS records for the exposed services.

> **Collapse: AWS PrivateLink network diagram**
>
> ![Diagram of an AWS PrivateLink network.](_images/bva1721771819136.jpg)

Learn more in [What is AWS PrivateLink?](https://docs.aws.amazon.com/vpc/latest/privatelink/what-is-privatelink.html) in the AWS documentation. Learn more about setup items you might need to consider in [Setup considerations](#_setup_considerations).

#### Simple network endpoints

Public and private endpoints for the Simple network model are listed here.

> **Collapse: Default public endpoints**
>
> | Default public endpoints   | URLs                                                                       |
> | -------------------------- | -------------------------------------------------------------------------- |
> | PingAccess                 | `https://pingaccess.<environment>-<customer>.<region>.ping.cloud/`         |
> | PingAccess agent           | `https://pingaccess-agent.<environment>-<customer>.<region>.ping.cloud/`   |
> | PingFederate               | `https://pingfederate.<environment>-<customer>.<region>.ping.cloud/`       |
> | Environment logs           | `https://logs.<environment>-<customer>.<region>.ping.cloud/`               |
> | Environment monitoring     | `https://monitoring.<environment>-<customer>.<region>.ping.cloud/`         |
> | PingFederate admin console | `https://pingfederate-admin.<environment>-<customer>.<region>.ping.cloud/` |
> | PingAccess admin console   | `https://pingaccess-admin.<environment>-<customer>.<region>.ping.cloud/`   |
> | PingCentral                | `https://pingcentral-admin.<customer>.<region>.ping.cloud/`                |
> | Argo CD                    | `https://argocd.<customer>.<region>.ping.cloud/`                           |
> | Prometheus                 | `https://prometheus.<environment>-<customer>.<region>.ping.cloud/`         |

> **Collapse: Optional public endpoints**
>
> | Optional public endpoints                                                                                                 | URLs                                                                              |
> | ------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- |
> | PingFederate admin API                                                                                                    | `https://ext-pingfederate-admin-api.<environment>-<customer>.<region>.ping.cloud` |
> | PingAccess admin API                                                                                                      | `https://ext-pingaccess-admin-api.<environment>-<customer>.<region>.ping.cloud`   |
> | PingDirectory&#xA;&#xA;PingDirectory LDAPS endpoints must be on the allowed list on the PingDirectory connection handler. | `ldaps://ext-pingdirectory-admin.<environment>-<customer>.<region>.ping.cloud`    |
> | PingDirectory API                                                                                                         | `https://ext-pingdirectory.<environment>-<customer>.<region>.ping.cloud`          |
> | PingDelegator                                                                                                             | `https://ext-pingdelegator.<environment>-<customer>.<region>.ping.cloud`          |
> | PingFederate global (multi-region only)                                                                                   | `https://pf.<environment>.global.<customer>.ping.cloud`                           |
> | PingAccess global (multi-region only)                                                                                     | `https://pa.<environment>.global.<customer>.ping.cloud`                           |

> **Collapse: Optional private endpoints**
>
> | Optional private endpoints                                                                                              | URLs                                                                               |
> | ----------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
> | PingFederate admin API                                                                                                  | `https://int-pingfederate-admin-api.<environment>-<customer>.<region>.ping.cloud/` |
> | PingAccess admin API                                                                                                    | `https://int-pingaccess-admin-api.<environment>-<customer>.<region>.ping.cloud/`   |
> | PingDirectory&#xA;&#xA;PingDirectory LDAPS endpoints must be on the allow list on the PingDirectory connection handler. | `ldaps://int-pingdirectory-admin.<environment>-<customer>.<region>.ping.cloud/`    |
> | PingDirectory API                                                                                                       | `https://int-pingdirectory.<environment>-<customer>.<region>.ping.cloud`           |
> | PingDelegator                                                                                                           | `https://int-pingdelegator.<environment>-<customer>.<region>.ping.cloud/`          |
>
> |   |                                                                                                                                        |
> | - | -------------------------------------------------------------------------------------------------------------------------------------- |
> |   | If the AWS PrivateLink network model is used, an `int` prefix is added to all private endpoint URLs to ensure that they're recognized. |

### Advanced network

The Advanced network option is designed for the most sophisticated networking needs. You connect to your on-premise and cloud-based environments using a secure, private connection, and there is no limit to the number of connections you can have.

With this type of network model, an extension of your network is created and deployed in the private IP space and is fully routable within your network. Learn more in [IP requirements](#_ip_requirements).

This option also supports all protocols that will allow you to design a network that meets the unique needs of your organization.

This option is best if you:

* Have multiple data center connections using AWS Site-to-Site VPN or AWS Direct Connect.

* Have multi-cloud connections in your tenant using AWS Site-to-Site VPN, or have dedicated interconnectivity provided by third-party providers to AWS and other cloud environments (Azure, GCP, and Oracle Cloud).

* Use Kerberos and Radius protocols.

* Have redundant connectivity in their cloud or on-premise data centers.

* Require greater amounts of bandwidth than is typically available on a VPN network. Review the IP requirements.

There are several different types of Advanced network options available:

* [Direct Connect (DX) network](#_direct_connect)

* [Transit Gateway (TGW) network](#_transit_gateway)

* [VPN network](#_vpn_network)

#### IP requirements

Because of its fully routable nature, the IP requirements will be greater for the Advanced network model than a Simple VPN model. Each VPC deployed in PingOne Advanced Services will require a /22 network CIDR assigned to it from your RFC1918 IP space. The exact number of IPs you will need will vary and depend on the types of environments you have.

Keep in mind that Ping Identity is not just deploying servers into AWS. Each VPN is a self-contained full data center with all the components that go along with it.

Environments required for all deployments:

* Primary production environment

* Primary development environment

* Primary customer hub environment

* Primary staging environment if a child region is also being deployed

Optional environments:

* Primary testing environment

* Primary staging environment for a single region

Learn more in [Environments](../environments/p1as_environments.html).

If you need a secondary customer hub environment, a secondary staging environment is required if a child region is also being deployed, but a secondary production environment is not. The same is true if you need a tertiary customer hub environment. A tertiary staging environment is required if a child region is also being deployed, but a tertiary production environment is not.

These environments are required because they're needed to handle increases in AWS services and the number of endpoints used, and to provide the elasticity needed to autoscale the environment to meet traffic demands. You can specify which /22 network CIDR goes to each environment, or leave it up to your implementation partners to make these decisions when they build the environments.

Learn more in [Data storage considerations](../environments/p1as_data_storage.html).

#### Direct Connect (DX) network

The Direct Connect (DX) network uses DX to connect to you or to a global mesh network. Your network traffic remains on the AWS global network and never touches the public internet.

Unlike other network options that can have many different vendors involved, you purchase your connection directly from DX. AWS also maintains a list of [AWS Direct Connect Delivery Partners](https://aws.amazon.com/directconnect/partners/), who can help you establish your connections.

This option is best if:

* You want to improve application performance by connecting directly to AWS and bypassing the public internet.

* You want to secure your data as it moves between your network and AWS with multiple encryption options.

* You are willing to cover the cost of the connection, which will vary depending on the agreement made with your DX partners. PingOne Advanced Services receives the virtual interfaces (VIFs) for the AWS services included, but does not maintain the connection.

Learn more in [AWS Direct Connect](https://aws.amazon.com/directconnect/?nc=sn\&loc=0) in the Amazon documentation.

> **Collapse: DX network diagram**
>
> ![Diagram of a DX network.](_images/rch1721854627619.jpg)

Learn more about items you might need to consider regarding setup in [Setup considerations](#_setup_considerations).

#### Transit Gateway (TGW) network

If you have your own AWS presence but need a connection method that can support Kerberos and Radius protocols, which PrivateLink cannot, the Transit Gateway (TGW) network might be the right option for you.

There are two different types of TGW networks:

* TGW peering network

  With this model, the TGW peers to the TGW in the customer hub environment in PingOne Advanced Services. Traffic from all environments in a PingOne Advanced Services region will travel across this peering connection.

> **Collapse: TGW peering network diagram**
>
> ![Diagram of a TGW peering network.](_images/anq1721918396925.jpg)

Learn more about items you might need to consider regarding setup in [Setup considerations](#_setup_considerations).

* TGW RAM share network

  With this model, the TGW is connected to each VPC instead using the customer hub environment, which allows for data separation.

> **Collapse: TGW RAM share network diagram**
>
> ![Diagram of a TGW RAM share network.](_images/tri1721918561314.jpg)

Learn more about items you might need to consider regarding setup in [Setup considerations](#_setup_considerations).

#### VPN network

VPNs are typically used in advanced network situations where you need to connect to an on-premise infrastructure, and a large amount of bandwidth is not required. Although you can make the same type of connection with a Direct Connect (DC) network, which offers more bandwidth, the cost of the connection is separate from PingOne Advanced Services.

You can also set up as many VPN connections as you need. Border Gateway Protocol (BGP) and static routing are both supported. If BGP is used, we'll ask that you share your routes. PingOne Advanced Services is designed in the hub-and-spoke model, which does not allow routes to propagate to the VPCs behind the Transit Gateway.

This option is best if you:

* Need to connect to an on-premise infrastructure.

* Do not need a large amount of bandwidth.

* Do not want to cover the cost of having this connection.

This network model uses the AWS VPN service, which is a route-based solution. For details regarding this connection:

* Learn more about Appliances in [Customer Gateway Configuration Formats](https://ec2-downloads.s3.amazonaws.com/2009-07-15/customer-gateway-config-formats.xml).

* Learn more about VPN settings in [Tunnel options for your Site-to-Site VPN connection](https://docs.aws.amazon.com/vpn/latest/s2svpn/VPNTunnels.html) in the *AWS Site-to-Site VPN User Guide*.

* A Site-to-Site VPN connection consists of two tunnels, each terminating in a different availability zone, to provide increased availability to your VPC. If there's a device failure within AWS, your VPN connection automatically fails over to the second tunnel so that your access isn't interrupted. From time to time, AWS also performs routine maintenance on your VPN connection, which might briefly disable one of the two tunnels of your VPN connection, which is why it's important to configure both tunnels. Learn more about tunnel resiliency in [Site-to-Site VPN tunnel endpoint replacements](https://docs.aws.amazon.com/vpn/latest/s2svpn/endpoint-replacements.html).

If a gateway device terminating the VPN tunnels uses policy-based routing:

* Each VPN connection consists of two separate tunnels.

* Each tunnel contains an IKE security association and a BGP peering connection.

* You are limited to one unique security association (SA) pair per tunnel, (one inbound and one outbound).

This limitation requires that each PingOne Advanced Services region uses IP space that does not overlap and can be summarized into a single supernet to allow for a single SA per region VPN.

Learn more about VPN networks in [Your customer gateway device](https://docs.aws.amazon.com/vpn/latest/s2svpn/your-cgw.html) in the AWS Site-to-Site VPN User Guide.

> **Collapse: VPN network diagram**
>
> ![Diagram of a VPN network.](_images/rwb1721919418583.jpg)

Learn more about items you might need to consider regarding setup in [Setup considerations](#_setup_considerations).

#### Advanced network endpoints

Public and private endpoints for the Advanced network model are listed here.

> **Collapse: Default public endpoints**
>
> | Default public endpoints   | URLs                                                                       |
> | -------------------------- | -------------------------------------------------------------------------- |
> | PingAccess                 | `https://pingaccess.<environment>-<customer>.<region>.ping.cloud/`         |
> | PingAccess agent           | `https://pingaccess-agent.<environment>-<customer>.<region>.ping.cloud/`   |
> | PingFederate               | `https://pingfederate.<environment>-<customer>.<region>.ping.cloud/`       |
> | Environment logs           | `https://logs.<environment>-<customer>.<region>.ping.cloud/`               |
> | Environment monitoring     | `https://monitoring.<environment>-<customer>.<region>.ping.cloud/`         |
> | PingFederate admin console | `https://pingfederate-admin.<environment>-<customer>.<region>.ping.cloud/` |
> | PingAccess admin console   | `https://pingaccess-admin.<environment>-<customer>.<region>.ping.cloud/`   |
> | PingCentral                | `https://pingcentral-admin.<customer>.<region>.ping.cloud/`                |
> | Prometheus                 | `https://prometheus.<environment>-<customer>.<region>.ping.cloud/`         |

> **Collapse: Optional public endpoints**
>
> | Optional public endpoints                                                                                               | URLs                                                                              |
> | ----------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- |
> | PingFederate admin API                                                                                                  | `https://ext-pingfederate-admin-api.<environment>-<customer>.<region>.ping.cloud` |
> | PingAccess admin API                                                                                                    | `https://ext-pingaccess-admin-api.<environment>-<customer>.<region>.ping.cloud`   |
> | PingDirectory&#xA;&#xA;PingDirectory LDAPS endpoints must be on the allow list on the PingDirectory connection handler. | `ldaps://ext-pingdirectory-admin.<environment>-<customer>.<region>.ping.cloud`    |
> | PingDirectory API                                                                                                       | `https://ext-pingdirectory.<environment>-<customer>.<region>.ping.cloud`          |
> | PingDelegator                                                                                                           | `https://ext-pingdelegator.<environment>-<customer>.<region>.ping.cloud`          |
> | PingFederate global (multi-region only)                                                                                 | `https://pf.<environment>.global.<customer>.ping.cloud`                           |
> | PingAccess global (multi-region only)                                                                                   | `https://pa.<environment>.global.<customer>.ping.cloud`                           |

> **Collapse: Default private endpoints**
>
> | Default public endpoints | URLs                                                                           |
> | ------------------------ | ------------------------------------------------------------------------------ |
> | PingFederate admin API   | `https://pingfederate-admin-api.<environment>-<customer>.<region>.ping.cloud/` |
> | PingAccess admin API     | `https://pingaccess-admin-api.<environment>-<customer>.<region>.ping.cloud/`   |

## Setup considerations

Items you might need to consider regarding setup depend on the network model you're investigating.

### VPN setup requirements

To set up a VPN network, you can provide your own VPN inside tunnel CIDRS, or we will pick from the applicable range. A size /30 CIDR block is required from the 169.254.0.0/16 range (x2), but not in these reserved ranges:

* 169.254.0.0/30

* 169.254.1.0/30

* 169.254.2.0/30

* 169.254.3.0/30

* 169.254.4.0/30

* 169.254.5.0/30

* 169.254.169.252/30

|   |                                                                                                                                                                                                                                                                                         |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | If you're considering the Simple VPN network, you will need to provide a /24 CIDR block from your RFC1918 IP space for the VPN landing zone. All the private PingOne Advanced Services private endpoints that you connect to will be within the specified IP range in your AWS account. |

The VPN should be on [the list of VPNs that AWS supports](https://ec2-downloads.s3.amazonaws.com/2009-07-15/customer-gateway-config-formats.xml). You'll also need to share:

* The outer IP address

* The VPN vendor

* The VPN model and series

* The software version

Learn more in [Tunnel options for your Site-to-Site VPN connection](https://docs.aws.amazon.com/vpn/latest/s2svpn/VPNTunnels.html) in the AWS Site-to-Site VPN User Guide.

This type of network supports BGP or static routing.

* If BGP routing is used, you'll need to share the ASN values that should be used for BGP setup. We also ask that you share your routes. PingOne Advanced Services is designed in the hub-and-spoke model, which does not allow routes to propagate to the VPCs behind the Transit Gateway.

* If static routing is used, we ask that you share the list of routes. Ideally, provide this information as subnets, and when possible, combine into larger subnets.

AWS will generate a VPN configuration sample document that includes the pre-shared key and public IP addresses to connect to. This document will be sent to your network team using an encrypted email so the VPN setup can be completed.

### AWS PrivateLink requirements

To set up an AWS PrivateLink network, we ask that you share:

* Your AWS Account ID

* A list of the services you want to consume:

  * LDAPS

  * DataSync

  * APIs (PingFederate, PingAccess, and PingDirectory)

  * The environment that you want to be connected

If you expose AWS PrivateLink services to us, we'll also need:

* The AWS account that the connection is coming from

* The PingOne Advanced Services environment that you want to connect to

* The hostname of the services that you want to be connected to

### Direct Connect (DX) requirements

There are two different ways to set up a DX network:

* You can provide us with:

  * DX VIF IDs

  * VIP environment mapping information, which explains which gateways are associated with which VIFs and the associated PingOne Advanced Services customer environment VPCs (dev\\|test\\|stage\\|prod\\|customer-hub)

* You can have PingOne Advanced Services initiate contact with Direct Connect and provide:

  * The PingOne Advanced Services AWS region

  * The PingOne Advanced Services customer hub AWS account ID

Then, we ask that you share the Direct Connect VIFs with us, which will be associated with a Direct Connect Gateway attached to the PingOne Advanced Services environment VPCs.

### Transit Gateway (TGW) peering requirements

To set up a TGW peering network, we ask that you share:

* The AWS region

* The AWS Account ID of the AWS account hosting your transit gateway

* The AWS Transit Gateway ID

Static routing will return to the transit gateway listed.

TGW peering is initiated from the PingOne Advanced Services platform. To create the connection, the peering will be initiated, and you'll need to accept the transit gateway peering request.

### Transit Gateway (TGW) RAM share requirements

You initiate the TGW RAM share from your transit gateway infrastructure. Configure that gateway using:

* The PingOne Advanced Services AWS region

* The PingOne Advanced Services AWS account IDs

Then, configure RAM share using:

* Your Transit Gateway IDs

* A document that maps transit gateway to PingOne Advanced Services and explains which networks will be connected to which environments

Static routing will return to the transit gateway listed.