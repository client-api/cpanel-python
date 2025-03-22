# clientapi_cpanel.BrandingApi

All URIs are relative to *https://cpanel-server.tld:2083/execute*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_application_information**](BrandingApi.md#get_application_information) | **GET** /Branding/get_application_information | Return single app&#39;s info from dynamicui.conf
[**get_applications**](BrandingApi.md#get_applications) | **GET** /Branding/get_applications | Return multiple apps&#39; info from dynamicui.conf
[**get_available_applications**](BrandingApi.md#get_available_applications) | **GET** /Branding/get_available_applications | Return current user&#39;s cPanel application details
[**get_information_for_applications**](BrandingApi.md#get_information_for_applications) | **GET** /Branding/get_information_for_applications | Return app&#39;s info from sitemap.json


# **get_application_information**
> InlineResponse20042 get_application_information(app_key)

Return single app's info from dynamicui.conf

This function retrieves an application's information from the `dynamicui.conf` file.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response20042 import InlineResponse20042
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
    api_instance = clientapi_cpanel.BrandingApi(api_client)
    app_key = 'boxtrapper' # str | The application's feature name. This value **must** match a feature's `app_key` value. For a list of app_key values, read our [Guide to cPanel Interface Customization - Appkeys](https://go.cpanel.net/appkey) documentation.

    try:
        # Return single app's info from dynamicui.conf
        api_response = api_instance.get_application_information(app_key)
        print("The response of BrandingApi->get_application_information:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BrandingApi->get_application_information: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_key** | **str**| The application&#39;s feature name. This value **must** match a feature&#39;s &#x60;app_key&#x60; value. For a list of app_key values, read our [Guide to cPanel Interface Customization - Appkeys](https://go.cpanel.net/appkey) documentation. | 

### Return type

[**InlineResponse20042**](InlineResponse20042.md)

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

# **get_applications**
> InlineResponse20043 get_applications(app_keys=app_keys)

Return multiple apps' info from dynamicui.conf

This function retrieves an application's information from a specific theme's `dynamicui.conf` file.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response20043 import InlineResponse20043
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
    api_instance = clientapi_cpanel.BrandingApi(api_client)
    app_keys = 'addon_domains,ftp_accounts,anonymous_ftp' # str | A comma-separated list of an application feature names. If you do not specify this parameter, the output will include all of the applications that the `dynamicui.conf` file contains.  **Note:**  * This value must match an application's `feature` value in the `dynamicui.conf` file. * For more information, read our [Guide to cPanel Interface Customization - Appkeys](https://go.cpanel.net/appkey) documentation. (optional)

    try:
        # Return multiple apps' info from dynamicui.conf
        api_response = api_instance.get_applications(app_keys=app_keys)
        print("The response of BrandingApi->get_applications:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BrandingApi->get_applications: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_keys** | **str**| A comma-separated list of an application feature names. If you do not specify this parameter, the output will include all of the applications that the &#x60;dynamicui.conf&#x60; file contains.  **Note:**  * This value must match an application&#39;s &#x60;feature&#x60; value in the &#x60;dynamicui.conf&#x60; file. * For more information, read our [Guide to cPanel Interface Customization - Appkeys](https://go.cpanel.net/appkey) documentation. | [optional] 

### Return type

[**InlineResponse20043**](InlineResponse20043.md)

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

# **get_available_applications**
> InlineResponse20044 get_available_applications(nvarglist=nvarglist)

Return current user's cPanel application details

This function retrieves information about the groups and applications in the authenticated user's cPanel interface.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response20044 import InlineResponse20044
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
    api_instance = clientapi_cpanel.BrandingApi(api_client)
    nvarglist = 'pref|software|domains' # str | A pipe-separated list of group names denoting the order in which to sort the groups. If you do not supply a value, the function does not sort the groups.  **Note:**  `arglist` is an alias for this parameter. (optional)

    try:
        # Return current user's cPanel application details
        api_response = api_instance.get_available_applications(nvarglist=nvarglist)
        print("The response of BrandingApi->get_available_applications:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BrandingApi->get_available_applications: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **nvarglist** | **str**| A pipe-separated list of group names denoting the order in which to sort the groups. If you do not supply a value, the function does not sort the groups.  **Note:**  &#x60;arglist&#x60; is an alias for this parameter. | [optional] 

### Return type

[**InlineResponse20044**](InlineResponse20044.md)

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

# **get_information_for_applications**
> InlineResponse20045 get_information_for_applications(docroot, app_keys=app_keys)

Return app's info from sitemap.json

This function retrieves an application's information from a specific
theme's `sitemap.json` file.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response20045 import InlineResponse20045
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
    api_instance = clientapi_cpanel.BrandingApi(api_client)
    docroot = '/usr/local/cpanel/base/webmail/jupiter' # str | The absolute path to the directory containing the `sitemap.json` file. This is the path to your theme's document root.
    app_keys = 'email_filters' # str | A comma-separated list of Appkey names. If you do **not** specify this parameter, the output will include all of the applications that the `sitemap.json` file contains.  **Note:**  This value **must** match an application's `key` value in the `sitemap.json` file. For more information, read our [Guide to cPanel Interface Customization - Appkeys](https://go.cpanel.net/appkey) documentation. (optional)

    try:
        # Return app's info from sitemap.json
        api_response = api_instance.get_information_for_applications(docroot, app_keys=app_keys)
        print("The response of BrandingApi->get_information_for_applications:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BrandingApi->get_information_for_applications: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **docroot** | **str**| The absolute path to the directory containing the &#x60;sitemap.json&#x60; file. This is the path to your theme&#39;s document root. | 
 **app_keys** | **str**| A comma-separated list of Appkey names. If you do **not** specify this parameter, the output will include all of the applications that the &#x60;sitemap.json&#x60; file contains.  **Note:**  This value **must** match an application&#39;s &#x60;key&#x60; value in the &#x60;sitemap.json&#x60; file. For more information, read our [Guide to cPanel Interface Customization - Appkeys](https://go.cpanel.net/appkey) documentation. | [optional] 

### Return type

[**InlineResponse20045**](InlineResponse20045.md)

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

