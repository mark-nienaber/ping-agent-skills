---
title: Before You Start
description: Identity Governance server software requires the following hardware and software requirements to run in your production environment.
component: identity-governance
version: 7.1.2
page_id: identity-governance:release-notes:chap-before-you-install
canonical_url: https://docs.pingidentity.com/identity-governance/7.1.2/release-notes/chap-before-you-install.html
section_ids:
  sec-idm-version: Ping Identity Management
  sec-operating-systems: Operating Systems
  sec-java-requirements: Java Requirements
  sec-system-requirements: System Requirements
---

# Before You Start

Identity Governance server software requires the following hardware and software requirements to run in your production environment.

## Ping Identity Management

Ping Identity Governance supports the following PingIDM versions for installation:

**Table 1: Identity Management Requirements**

|         |                   |
| ------- | ----------------- |
| PingIDM | 6.5, 7.x.x, 8.0.x |

## Operating Systems

Ping Identity Governance is supported on the following operating system:

**Table 2: Operating System Requirements**

| Vendor                          | Versions               |
| ------------------------------- | ---------------------- |
| Red Hat Enterprise Linux/CentOS | 6.6, 6.7, 7.0, and 8.0 |
| Ubuntu Linux                    | 16.04, 18.04           |
| Windows Server                  | 2012 R2, 2016, 2019    |

## Java Requirements

Identity Governance software supports the following Java environments:

**Table 3: Java Requirements**

| Vendor                                                                                                                            | Versions                                                                    |
| --------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------- |
| OpenJDK, including OpenJDK-based distributions:- AdoptOpenJDK/Eclipse Adoptium

- Amazon Corretto

- Azul Zulu

- Red Hat OpenJDK | 8, 11                                                                       |
| Oracle Java                                                                                                                       | 8, 11 (specifically at least the Java Standard Edition runtime environment) |

## System Requirements

Ping Identity Governance requires at least 100MB disk space and 4GB memory for non-production implementations. Production sizing depends on user population, audit requirements and expected request volume.
