---
title: Apache Tomcat
description: Configure Apache Tomcat as a deployment container for PingAM, including JVM settings, cookie domains, request logging, and security parameters
component: pingam
version: 8.1
page_id: pingam:installation:prepare-apache-tomcat
canonical_url: https://docs.pingidentity.com/pingam/8.1/installation/prepare-apache-tomcat.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Install", "Web Container"]
page_aliases: ["install-guide:prepare-apache-tomcat.adoc"]
section_ids:
  jvm_startup: JVM startup
  slashes_in_resource_names: Slashes in resource names
  cookie_domains: Cookie domains
  log_request_times: Log request times
  encoding_and_security: Encoding and security
---

# Apache Tomcat

AM examples often use Apache Tomcat (Tomcat) as the deployment container. In these examples, Tomcat is installed on `am.example.com` and listens on the default ports without a Java Security Manager enabled.

## JVM startup

AM core services require a minimum JVM heap size of 1 GB, and a metadata space size of up to 256 MB.

|   |                                                                                                                                                                                                                                                                                                                                                              |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | Metadata space (Metaspace) is a dedicated region within Native Memory. It can grow automatically if you don't set a maximum size. The ideal Metaspace size depends on your deployment and the number of scripts you're running. 256 MB is considered a safe value for production deployments, but you might need to tweak this for your specific deployment. |

Set a `CATALINA_OPTS` environment variable with the appropriate tuning for your environment. For example, add the following in your `setenv` file:

* Linux

* Windows

In `$CATALINA_BASE/bin/setenv.sh`:

```bash
export CATALINA_OPTS="$CATALINA_OPTS -server -Xmx2g -XX:MetaspaceSize=256m -XX:MaxMetaspaceSize=256m"
```

In `$CATALINA_BASE/bin/setenv.bat`:

```powershell
set "CATALINA_OPTS=%CATALINA_OPTS% -server -Xmx2g -XX:MetaspaceSize=256m -XX:MaxMetaspaceSize=256m"
```

Some versions of Microsoft Edge support the `Expires` header attribute instead of the `Max-Age` header attribute, which may cause SAML 2.0 and agent logout sequences to fail.

If you have set the `org.apache.catalina.STRICT_SERVLET_COMPLIANCE` Tomcat property to `true`, add the `org.apache.tomcat.util.http.ServerCookie.ALWAYS_ADD_EXPIRE` property in the `setenv` file, to add the `Expires` attribute to the headers:

* Linux

* Windows

In `$CATALINA_BASE/bin/setenv.sh`:

```bash
export CATALINA_OPTS="$CATALINA_OPTS -server -Xmx2g -XX:MetaspaceSize=256m -XX:MaxMetaspaceSize=256m \
-Dorg.apache.tomcat.util.http.ServerCookie.ALWAYS_ADD_EXPIRES=true"
```

In `$CATALINA_BASE/bin/setenv.bat`:

```powershell
set "CATALINA_OPTS=%CATALINA_OPTS% -server -Xmx2g -XX:MetaspaceSize=256m -XX:MaxMetaspaceSize=256m -
-Dorg.apache.tomcat.util.http.ServerCookie.ALWAYS_ADD_EXPIRES=true"
```

## Slashes in resource names

Some AM resources have names that can contain slash characters (`/`), for example, in policy names, application names, and SAML 2.0 entities. These slash characters can cause unexpected behavior when running AM on Tomcat.

Avoid resource names that contain forward slashes.

## Cookie domains

Set the cookie domain name value to an empty string (for *host-only* cookies) or to any non-top level domain (for *domain* cookies).

For example, if you install AM on `am.example.com`, you can set the cookie domain name to `example.com`.

|   |                                                                                                                                                                  |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Because host-only cookies are more secure than domain cookies, you *should* use host-only cookies unless you have a good business case for using domain cookies. |

You can find information on configuring the cookie domain during installation in [Install an instance](interactive-install.html#configure-openam-custom).

## Log request times

Tomcat provides components called valves that can be configured to track access to resources. The Access Log Valve outputs information about request activity to log files for you to analyze or use when troubleshooting.

To record request times in the Access Log Valve log, configure the `pattern` attribute to include the following values:

* `%D`: The time taken to send an entire request in milliseconds. This is the total processing time and may be affected by network conditions.

* `%F`: The time taken to commit the response in milliseconds.

Example `Valve` element in `server.xml`:

```bash
<Valve className="org.apache.catalina.valves.AccessLogValve" directory="logs"
       prefix="localhost_access_log" suffix=".txt"
       pattern="%h %l %u %t "%r" %s %b %D %F" />
```

You can find information about the Access Log Valve configuration in the [Tomcat documentation](https://tomcat.apache.org/tomcat-10.0-doc/config/valve.html#Access_Log_Valve), including the `%F` value.

## Encoding and security

You should edit the Tomcat `<Connector>` configuration to set `URIEncoding="UTF-8"`. UTF-8 URI encoding means the container can correctly decode URL-encoded characters in URI paths. This is particularly useful if your applications use the AM REST APIs and some identifiers, such as usernames, contain special characters.

You should also set the `protocols` property appropriately to define which protocols are supported. Make sure you don't support any unsafe protocols such as the SSL v3.0 protocol (`SSLv3`).

`<Connector>` configuration elements are found in the configuration file, `/path/to/tomcat/conf/server.xml`. The following excerpt shows an example `<Connector>` with the `URIEncoding` and `protocols` attributes set appropriately:

```xml
<Connector port="8443" protocol="HTTP/1.1"
                  SSLEnabled="true"
                  protocols="TLSv1.2,TLSv1.3"
                  maxThreads="150"
                  scheme="https"
                  secure="true"
                  clientAuth="false"
                  URIEncoding="UTF-8" />
```

When you have finished setting up Apache Tomcat, you *should* enforce HTTPS connections to AM. Learn more in [Secure connections to the AM container](configure-container-HTTPS.html).
