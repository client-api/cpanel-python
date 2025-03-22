# clientapi_cpanel.DirectLinkProtectionHotlinkApi

All URIs are relative to *https://cpanel-server.tld:2083/execute*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_hotlink**](DirectLinkProtectionHotlinkApi.md#add_hotlink) | **GET** /Mime/add_hotlink | Enable hotlink protection
[**delete_hotlink**](DirectLinkProtectionHotlinkApi.md#delete_hotlink) | **GET** /Mime/delete_hotlink | Disable hotlink protection
[**list_hotlinks**](DirectLinkProtectionHotlinkApi.md#list_hotlinks) | **GET** /Mime/list_hotlinks | Return domains with hotlink protection


# **add_hotlink**
> InlineResponse200317 add_hotlink(extensions, redirect_url, urls, allow_null=allow_null)

Enable hotlink protection

This function adds hotlink protection for a site. Hotlink protection will redirect users to another URL if they navigate to a file with a specified extension, but an allowed URL did not refer them.

**Important:**

  When you disable the [WebServer role](https://go.cpanel.net/serverroles), the system **disables** this function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200317 import InlineResponse200317
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
    api_instance = clientapi_cpanel.DirectLinkProtectionHotlinkApi(api_client)
    extensions = 'foo,bar' # str | File types to hotlink protect.  **Note:**  To protect multiple file types, use a comma-separated list.
    redirect_url = 'http://redirect.example.com/' # str | The URL to which the system sends hotlinkers.
    urls = 'http://example.com/ http://foobar.com/' # str | The site to hotlink protect.  **Note:**  To protect multiple URLs, separate each URL with a newline character.
    allow_null = 1 # int | Whether the domain allows hotlinks. * `1` - Allows. * `0` - Does **not** allow. (optional)

    try:
        # Enable hotlink protection
        api_response = api_instance.add_hotlink(extensions, redirect_url, urls, allow_null=allow_null)
        print("The response of DirectLinkProtectionHotlinkApi->add_hotlink:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DirectLinkProtectionHotlinkApi->add_hotlink: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **extensions** | **str**| File types to hotlink protect.  **Note:**  To protect multiple file types, use a comma-separated list. | 
 **redirect_url** | **str**| The URL to which the system sends hotlinkers. | 
 **urls** | **str**| The site to hotlink protect.  **Note:**  To protect multiple URLs, separate each URL with a newline character. | 
 **allow_null** | **int**| Whether the domain allows hotlinks. * &#x60;1&#x60; - Allows. * &#x60;0&#x60; - Does **not** allow. | [optional] 

### Return type

[**InlineResponse200317**](InlineResponse200317.md)

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

# **delete_hotlink**
> InlineResponse200321 delete_hotlink()

Disable hotlink protection

This function removes hotlink protection.

**Important:**

  When you disable the [Web Server](https://go.cpanel.net/serverroles) role, the system **disables** this function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200321 import InlineResponse200321
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
    api_instance = clientapi_cpanel.DirectLinkProtectionHotlinkApi(api_client)

    try:
        # Disable hotlink protection
        api_response = api_instance.delete_hotlink()
        print("The response of DirectLinkProtectionHotlinkApi->delete_hotlink:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DirectLinkProtectionHotlinkApi->delete_hotlink: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**InlineResponse200321**](InlineResponse200321.md)

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

# **list_hotlinks**
> InlineResponse200326 list_hotlinks()

Return domains with hotlink protection

This function lists domains with hotlink protection.

**Important:**

When you **disable** the [Web Server](https://go.cpanel.net/serverroles) role, the system **disables** this function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200326 import InlineResponse200326
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
    api_instance = clientapi_cpanel.DirectLinkProtectionHotlinkApi(api_client)

    try:
        # Return domains with hotlink protection
        api_response = api_instance.list_hotlinks()
        print("The response of DirectLinkProtectionHotlinkApi->list_hotlinks:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DirectLinkProtectionHotlinkApi->list_hotlinks: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**InlineResponse200326**](InlineResponse200326.md)

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

