# clientapi_cpanel.SitePublisherManagementApi

All URIs are relative to *https://cpanel-server.tld:2083/execute*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_site_templates**](SitePublisherManagementApi.md#list_site_templates) | **GET** /SiteTemplates/list_site_templates | Return available Site Publisher templates
[**list_user_settings**](SitePublisherManagementApi.md#list_user_settings) | **GET** /SiteTemplates/list_user_settings | Return Site Publisher websites&#39; information
[**publish**](SitePublisherManagementApi.md#publish) | **GET** /SiteTemplates/publish | Add Site Publisher website


# **list_site_templates**
> InlineResponse200469 list_site_templates()

Return available Site Publisher templates

This function lists available templates for cPanel's [Site Publisher](https://go.cpanel.net/cpaneldocsSitePublisher) feature.

* If you call this function as the `root` or `system` user, the function lists the `root` user's templates.
* If you call this function as a reseller, the function lists the `root` user's templates **and** the reseller's templates.
* If you call this function as a cPanel user, the function's output depends on the account's owner:
  * If the `root` user owns the account, the function only lists the `root` user's templates.
  * If a reseller owns the account, the function lists the `root` user's templates **and** that reseller's templates.

**Note:**

  The template directory's location depends on whether the `root` user or a reseller owns the template:
  * `/var/cpanel/customizations/site_templates/` — The `root` user's templates.
  * `/home/username/var/cpanel/reseller/site_templates/` — A reseller's templates, where `username` represents the reseller's username.
  * `/usr/local/cpanel/3rdparty/share/site_templates/` — cPanel-provided templates.

**Important:**

  When you disable the [Web Server role](https://go.cpanel.net/serverroles), the system **disables** this function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200469 import InlineResponse200469
from clientapi_cpanel.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://cpanel-server.tld:2083/execute
# See configuration.py for a list of all supported configuration parameters.
configuration = clientapi_cpanel.Configuration(
    host = "https://cpanel-server.tld:2083/execute"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = clientapi_cpanel.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with clientapi_cpanel.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = clientapi_cpanel.SitePublisherManagementApi(api_client)

    try:
        # Return available Site Publisher templates
        api_response = api_instance.list_site_templates()
        print("The response of SitePublisherManagementApi->list_site_templates:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SitePublisherManagementApi->list_site_templates: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**InlineResponse200469**](InlineResponse200469.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | HTTP Request was successful. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_user_settings**
> InlineResponse200470 list_user_settings()

Return Site Publisher websites' information

This function lists information for the cPanel account's [Site Publisher](https://go.cpanel.net/cpaneldocsSitePublisher) websites.

**Note:**

  To retrieve the list of Site Publisher website information, the function queries the `configurations.json` file in each domain's document root. For more information, read our [Guide to Site Publisher Templates](https://go.cpanel.net/SitePublisherTemplates) documentation.

**Important:**

  When you disable the [Web Server role](https://go.cpanel.net/howtouseserverprofiles#roles), the system **disables** this function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200470 import InlineResponse200470
from clientapi_cpanel.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://cpanel-server.tld:2083/execute
# See configuration.py for a list of all supported configuration parameters.
configuration = clientapi_cpanel.Configuration(
    host = "https://cpanel-server.tld:2083/execute"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = clientapi_cpanel.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with clientapi_cpanel.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = clientapi_cpanel.SitePublisherManagementApi(api_client)

    try:
        # Return Site Publisher websites' information
        api_response = api_instance.list_user_settings()
        print("The response of SitePublisherManagementApi->list_user_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SitePublisherManagementApi->list_user_settings: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**InlineResponse200470**](InlineResponse200470.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | HTTP Request was successful. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **publish**
> InlineResponse200471 publish(target__or__docroot, parameter_name=parameter_name, path=path, source=source, template=template)

Add Site Publisher website

This function publishes a [Site Publisher](https://go.cpanel.net/cpaneldocsSitePublisher) website.
* This function uses the `/scripts/process_site_template` script to publish the Site Publisher website.
* This function creates the `configurations.json` file in the specified directory.
  * This file contains the user-entered data for the Site Publisher website and uses `0700` permissions.
  * For more information, read our [Guide to Site Publisher Templates](https://go.cpanel.net/SitePublisherTemplates) documentation.
* When users publish a Site Publisher website, the system first creates a backup tarball of the target directory's contents in the `/site_publisher/backups/` directory within the user's home directory.

**Notes:**

  * When users publish a Site Publisher website, the system logs template information and the target directory to the `/usr/local/cpanel/logs/error_log` file.
  * The template directory's location depends on whether the `root` user or a reseller owns the template:
    * `/var/cpanel/customizations/site_templates/` — The `root` user's templates.
    * `/home/username/var/cpanel/reseller/site_templates/` — A reseller's templates, where `username` represents the reseller's username.
    * `/usr/local/cpanel/3rdparty/share/site_templates/` — cPanel-provided templates.

**Important:**

  When you disable the [_Web Server_](https://go.cpanel.net/howtouseserverprofiles#roles) role, the system **disables** this function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200471 import InlineResponse200471
from clientapi_cpanel.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://cpanel-server.tld:2083/execute
# See configuration.py for a list of all supported configuration parameters.
configuration = clientapi_cpanel.Configuration(
    host = "https://cpanel-server.tld:2083/execute"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = clientapi_cpanel.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with clientapi_cpanel.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = clientapi_cpanel.SitePublisherManagementApi(api_client)
    target__or__docroot = '/home/example/public_html' # str | The directory that will contain the Site Publisher website.
    parameter_name = 'My Website' # str | The template's variables and values.  **Note:**  * Use each variable's name as a parameter name for a parameter and value pair. * The template that you specify determines the values to define. * You **must** include the appropriate data for the selected template. If you use a cPanel-provided template, read our [Guide to Site Publisher Templates](https://go.cpanel.net/guide-to-site-publisher-templates-template-files) documentation for more information. If you use a third-party template, consult that template's documentation or its `meta.json` file. (optional)
    path = '/usr/local/cpanel/3rdparty/share/site_templates/' # str | The directory that contains the template's source directory. * `/var/cpanel/customizations/site_templates/` — The `root` user's templates. * `/home/username/var/cpanel/reseller/site_templates/` — A reseller's templates, where `username` represents the reseller's username. * `/usr/local/cpanel/3rdparty/share/site_templates/` — cPanel-provided templates.  **Note:**  You **must** include either the `source` parameter **or** the `path` and `template` parameters. (optional)
    source = '/usr/local/cpanel/3rdparty/share/site_templates/under_construction' # str | The absolute path to a template directory that exists in one of the following directories:  * `/var/cpanel/customizations/site_templates/` — The `root` user's templates. * `/home/username/var/cpanel/reseller/site_templates/` — A reseller's templates, where `username` represents the reseller's username. * `/usr/local/cpanel/3rdparty/share/site_templates/` — cPanel-provided templates.  If you do not specify a value, the system uses the path and template values to determine the template's source directory.  **Note:**   You **must** include either the `source` parameter **or** the `path` and `template` parameters. (optional)
    template = 'under_construction' # str | The template's directory's name.  **Note:**  You **must** include either the `source` parameter **or** the `path` and `template` parameters. (optional)

    try:
        # Add Site Publisher website
        api_response = api_instance.publish(target__or__docroot, parameter_name=parameter_name, path=path, source=source, template=template)
        print("The response of SitePublisherManagementApi->publish:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SitePublisherManagementApi->publish: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **target__or__docroot** | **str**| The directory that will contain the Site Publisher website. | 
 **parameter_name** | **str**| The template&#39;s variables and values.  **Note:**  * Use each variable&#39;s name as a parameter name for a parameter and value pair. * The template that you specify determines the values to define. * You **must** include the appropriate data for the selected template. If you use a cPanel-provided template, read our [Guide to Site Publisher Templates](https://go.cpanel.net/guide-to-site-publisher-templates-template-files) documentation for more information. If you use a third-party template, consult that template&#39;s documentation or its &#x60;meta.json&#x60; file. | [optional] 
 **path** | **str**| The directory that contains the template&#39;s source directory. * &#x60;/var/cpanel/customizations/site_templates/&#x60; — The &#x60;root&#x60; user&#39;s templates. * &#x60;/home/username/var/cpanel/reseller/site_templates/&#x60; — A reseller&#39;s templates, where &#x60;username&#x60; represents the reseller&#39;s username. * &#x60;/usr/local/cpanel/3rdparty/share/site_templates/&#x60; — cPanel-provided templates.  **Note:**  You **must** include either the &#x60;source&#x60; parameter **or** the &#x60;path&#x60; and &#x60;template&#x60; parameters. | [optional] 
 **source** | **str**| The absolute path to a template directory that exists in one of the following directories:  * &#x60;/var/cpanel/customizations/site_templates/&#x60; — The &#x60;root&#x60; user&#39;s templates. * &#x60;/home/username/var/cpanel/reseller/site_templates/&#x60; — A reseller&#39;s templates, where &#x60;username&#x60; represents the reseller&#39;s username. * &#x60;/usr/local/cpanel/3rdparty/share/site_templates/&#x60; — cPanel-provided templates.  If you do not specify a value, the system uses the path and template values to determine the template&#39;s source directory.  **Note:**   You **must** include either the &#x60;source&#x60; parameter **or** the &#x60;path&#x60; and &#x60;template&#x60; parameters. | [optional] 
 **template** | **str**| The template&#39;s directory&#39;s name.  **Note:**  You **must** include either the &#x60;source&#x60; parameter **or** the &#x60;path&#x60; and &#x60;template&#x60; parameters. | [optional] 

### Return type

[**InlineResponse200471**](InlineResponse200471.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | HTTP Request was successful. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

