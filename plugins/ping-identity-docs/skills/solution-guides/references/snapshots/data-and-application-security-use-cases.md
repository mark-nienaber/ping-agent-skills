---
title: Authenticating to EKS
description: After you have configured OIDC for EKS, PingOne users can execute the kubectl command to authenticate to EKS.
component: solution-guides
page_id: solution-guides:data_and_application_security_use_cases:htg_config_oidc_authn_aws_eks_custers_authn_eks
canonical_url: https://docs.pingidentity.com/solution-guides/data_and_application_security_use_cases/htg_config_oidc_authn_aws_eks_custers_authn_eks.html
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
