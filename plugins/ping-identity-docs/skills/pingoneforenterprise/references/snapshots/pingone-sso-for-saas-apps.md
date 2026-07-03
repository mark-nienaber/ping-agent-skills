---
title: .NET Redirect Sample
component: pingoneforenterprise
page_id: pingoneforenterprise:pingone_sso_for_saas_apps:p14saas_net_redirect_sample
canonical_url: https://docs.pingidentity.com/pingoneforenterprise/pingone_sso_for_saas_apps/p14saas_net_redirect_sample.html
revdate: March 30, 2023
---

# .NET Redirect Sample

```
<%@ Page Language="C#" %>
<script runat="server">

  protected String GetIdpId()
  {
      //Implement me!
      return "testidp.admin.pingidentity.com";
  }

/**
 * The saasid value is the GUID associated with the application. This is displayed in parentheses below the
 * application name on the My Applications page.
 * You will need to replace the saasid value in "${saasId}" in the sample below with the GUID for your application.
 * For example: String saasId = "18a6ada7-8f37-4d77-86f4-173046796193";
 */

  protected override void OnLoad(EventArgs e)
  {
      String saasId = "${saasId}";
      String idpId = GetIdpId();
      String baseUrl = "${tokenServiceBaseUrl}/sso/sp/initsso";
      String initSsoUrl = String.Format("{0}?saasid={1}&idpid={2}", baseUrl,
                                       saasId, idpId);
      Response.Redirect(initSsoUrl);
      base.OnLoad(e);
  }
</script>
```
