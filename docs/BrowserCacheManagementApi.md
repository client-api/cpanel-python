# clientapi_cpanel.BrowserCacheManagementApi

All URIs are relative to *https://cpanel-server.tld:2083/execute*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cache_buster_read**](BrowserCacheManagementApi.md#cache_buster_read) | **GET** /CacheBuster/read | Return web browser cached file override ID
[**update**](BrowserCacheManagementApi.md#update) | **GET** /CacheBuster/update | Create web browser cached file override ID


# **cache_buster_read**
> InlineResponse20058 cache_buster_read()

Return web browser cached file override ID

This function returns the current `CacheBuster` id. The system uses this ID to force the browser to fetch a new resource when that resource already exists in the web browser cache. This is useful when an application has updated the resource on the server. You should append this ID to the end of the url in the query-string. For example, if you are accessing a url like:

`https://example.com/styled/basic/sprites/icon_spritemap.css`

 To force the browser to fetch the updated version, you would append the following:

 `https://example.com/styled/basic/sprites/icon_spritemap.css?<CacheBusterID>`

 **Note**

 The application that updates the resource at this url on the server **must** call the `CacheBuster::update` function when it updates the resource to signify that update.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response20058 import InlineResponse20058
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
    api_instance = clientapi_cpanel.BrowserCacheManagementApi(api_client)

    try:
        # Return web browser cached file override ID
        api_response = api_instance.cache_buster_read()
        print("The response of BrowserCacheManagementApi->cache_buster_read:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BrowserCacheManagementApi->cache_buster_read: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**InlineResponse20058**](InlineResponse20058.md)

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

# **update**
> InlineResponse20059 update()

Create web browser cached file override ID

This function generates a random integer (the CacheBuster ID). Use this ID to work with and around a browser's caching mechanism.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response20059 import InlineResponse20059
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
    api_instance = clientapi_cpanel.BrowserCacheManagementApi(api_client)

    try:
        # Create web browser cached file override ID
        api_response = api_instance.update()
        print("The response of BrowserCacheManagementApi->update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BrowserCacheManagementApi->update: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**InlineResponse20059**](InlineResponse20059.md)

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

