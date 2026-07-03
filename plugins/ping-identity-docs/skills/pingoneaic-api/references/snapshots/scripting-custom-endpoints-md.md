---
title: Custom endpoints
description: You can use custom endpoints to run arbitrary JavaScript code through the REST API. Custom endpoint scripts are extremely flexible and can extend Advanced Identity Cloud behavior in many ways:
component: pingoneaic-api
page_id: pingoneaic-api::scripting-custom-endpoints
canonical_url: https://developer.pingidentity.com/pingoneaic-api/scripting-custom-endpoints.html
keywords: ["Extensibility", "Scripts", "REST API"]
section_ids:
  custom-endpoints-scripting-introduction: Custom endpoints scripting introduction
  manage-custom-endpoints: Manage custom endpoints
  create-a-custom-endpoint: Create a custom endpoint
  generate_a_curl_request_for_a_custom_endpoint: Generate a cURL request for a custom endpoint
  run_a_test_request_for_a_custom_endpoint: Run a test request for a custom endpoint
  http_request_methods_mapped_to_script_request_method_property_values: HTTP request methods mapped to script request.method property values
---

# Custom endpoints

You can use custom endpoints to run arbitrary JavaScript code through the REST API. Custom endpoint scripts are extremely flexible and can extend Advanced Identity Cloud behavior in many ways:

* Validate user input fields before storing them in a user profile.

* Create utility functions, such as getting today's date.

* Mandate user input fields during registration to support delegated administration decisions.

* Query identities with a particular relationship, such as being a member of an organization, and page the results.

You can consume custom endpoints within Advanced Identity Cloud or integrate them into your external UIs or system applications.

## Custom endpoints scripting introduction

For an introduction to custom endpoints scripting, read the following:

* [Create custom endpoints to launch scripts](https://docs.pingidentity.com/pingoneaic/latest/idm-scripting/script-custom-endpoints.html)

* [Variables available to scripts in custom endpoints](https://docs.pingidentity.com/pingoneaic/latest/idm-scripting/script-variables-custom-endpoints.html)

|   |                                                                                                                                                                                                                    |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | To understand how to create identity object query expressions to use in the `request.queryExpression` property, learn more in [Queries](https://docs.pingidentity.com/pingoneaic/latest/idm-objects/queries.html). |

|   |                                                                                                                                                                                                                                                                                                                                                                                    |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Scripts can potentially emit the personally identifiable information (PII) of your end users into Advanced Identity Cloud logs, and then into external services that consume Advanced Identity Cloud logs.Ping Identity recommends that you establish a review and testing process for all scripts to prevent PII leaking out of your Advanced Identity Cloud tenant environments. |

## Manage custom endpoints

To manage your custom endpoints, go to *Realm* > Scripts > Custom Endpoints.

On the Custom Endpoints page, you can view a list of existing custom endpoints. To edit, duplicate, or delete a custom endpoint, click its More ([icon: ellipsis-h, set=fa]) menu.

The edit option in the More menu opens the custom endpoint script in a lightweight editor. The editor features syntax highlighting and validation checking. Maximize the editor to full screen to edit larger scripts:

![idcloudui custom endpoints editor](_images/idcloudui-custom-endpoints-editor.png)

① Endpoint name\
② JavaScript editor\
③ Fullscreen option\
④ Syntax highlighting\
⑤ Validation checking\
⑥ cURL request tab, learn more in [Generate a cURL request for a custom endpoint](#generate_a_curl_request_for_a_custom_endpoint)\
⑦ Test tab, learn more in [Run a test request for a custom endpoint](#run_a_test_request_for_a_custom_endpoint)

## Create a custom endpoint

1. Go to *Realm* > Scripts > Custom Endpoints, then click + New Script.

2. Enter a Name for your new endpoint; for example, `getDate`.

   * Access the new custom endpoint over HTTP at:\
     `https://<tenant-env-fqdn>/openidm/endpoint/<name>`

   * Access the new custom endpoint in a script using:\
     `openidm.read('endpoint/<name>')`

3. (Optional) Enter a Description for your new endpoint; for example, `Get the current date`.

4. Next, use the editor to create your script. The editor is prepopulated with a default script, which is intended as a starting point for your custom script.

5. To test your script, click Save, then either:

   1. [Generate a cURL request for a custom endpoint](#generate_a_curl_request_for_a_custom_endpoint)

   2. [Run a test request for a custom endpoint](#run_a_test_request_for_a_custom_endpoint)

6. When your testing is complete, click Save and Close.

## Generate a cURL request for a custom endpoint

In the script editor:

1. Click the angled brackets icon (**<>**) to open the cURL Request tab.

2. In the Method field, choose an HTTP request method for the cURL request. Learn more about how HTTP request methods relate to the script `request.method` property values in this [mapping table](#http_request_methods_mapped_to_script_request_method_property_values).

3. (Optional) In the Body field, enter a JSON-formatted body for the cURL request (except when using the `GET` HTTP request method). For example:

   ```json
   {
       "param1": "foo",
       "param2": "bar"
   }
   ```

   |   |                                                                                                                                                               |
   | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | In the script, you can access the body using the `request.content` property. The example above maps to `request.content.param1` and `request.content.param2`. |

4. Click Generate to output the cURL request, which appears below your script. The cURL request is complete with an access bearer token and ready to run.

5. Click the copy icon ([icon: clone, set=fa]) to copy the cURL request from the editor, then paste and run it in a terminal window.

## Run a test request for a custom endpoint

In the script editor:

1. Click the triangle icon ([icon: play, set=fa]) to open the Test tab.

2. In the form field, enter a JSON-formatted configuration object for the cURL request. The form field is prepopulated with a default configuration object:

   ```json
     {
       "request": {
         "method": "create"
       }
     }
   ```

   This default configuration object creates a request using the `POST` HTTP request method. Learn more about how HTTP request methods relate to the script `request.method` variable parameter values in this [mapping table](#http_request_methods_mapped_to_script_request_method_property_values).

3. (Optional) To supply a body with the request, add a `request.content` property:

   ```json
     {
       "request": {
         "method": "create",
         "content": {
           "param1": "foo",
           "param2": "bar"
         }
       }
     }
   ```

   |   |                                                                                                                                                           |
   | - | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | In the script, you access the body using the `request.content` property. The example above maps to `request.content.param1` and `request.content.param2`. |

4. Click Run to run the cURL request. The result appears below the editor.

## HTTP request methods mapped to script `request.method` property values

| HTTP request method | Script `request.method` |
| ------------------- | ----------------------- |
| `GET`               | `read`                  |
| `POST`              | `create`                |
| `PUT`               | `update`                |
| `PATCH`             | `patch`                 |
| `DELETE`            | `delete`                |
