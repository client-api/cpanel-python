# clientapi_cpanel.NginxCachingApi

All URIs are relative to *https://cpanel-server.tld:2083/execute*

Method | HTTP request | Description
------------- | ------------- | -------------
[**clear_cache**](NginxCachingApi.md#clear_cache) | **GET** /NginxCaching/clear_cache | Delete NGINX cache contents.
[**disable_cache**](NginxCachingApi.md#disable_cache) | **GET** /NginxCaching/disable_cache | Disable the user&#39;s NGINX cache
[**enable_cache**](NginxCachingApi.md#enable_cache) | **GET** /NginxCaching/enable_cache | Enable the user&#39;s NGINX cache
[**reset_cache_config**](NginxCachingApi.md#reset_cache_config) | **GET** /NginxCaching/reset_cache_config | Reset the user&#39;s NGINX cache configuration


# **clear_cache**
> InlineResponse200361 clear_cache()

Delete NGINX cache contents.

This function clears the user's NGINX cache.

**Note:**

  - You can **only** use this function if you installed the `ea-nginx` package.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200361 import InlineResponse200361
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
    api_instance = clientapi_cpanel.NginxCachingApi(api_client)

    try:
        # Delete NGINX cache contents.
        api_response = api_instance.clear_cache()
        print("The response of NginxCachingApi->clear_cache:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NginxCachingApi->clear_cache: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**InlineResponse200361**](InlineResponse200361.md)

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

# **disable_cache**
> InlineResponse200362 disable_cache()

Disable the user's NGINX cache

This function disables the user's NGINX cache.

**Note:**

  - You can **only** use this function if you installed the `ea-nginx` package.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200362 import InlineResponse200362
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
    api_instance = clientapi_cpanel.NginxCachingApi(api_client)

    try:
        # Disable the user's NGINX cache
        api_response = api_instance.disable_cache()
        print("The response of NginxCachingApi->disable_cache:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NginxCachingApi->disable_cache: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**InlineResponse200362**](InlineResponse200362.md)

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

# **enable_cache**
> InlineResponse200363 enable_cache()

Enable the user's NGINX cache

This function enables the user's NGINX cache.

**Note:**

  - You can **only** use this function if you installed the `ea-nginx` package.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200363 import InlineResponse200363
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
    api_instance = clientapi_cpanel.NginxCachingApi(api_client)

    try:
        # Enable the user's NGINX cache
        api_response = api_instance.enable_cache()
        print("The response of NginxCachingApi->enable_cache:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NginxCachingApi->enable_cache: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**InlineResponse200363**](InlineResponse200363.md)

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

# **reset_cache_config**
> InlineResponse200364 reset_cache_config()

Reset the user's NGINX cache configuration

This function resets the user's NGINX caching configuration.

**Note:**

  - You can **only** use this function if you installed the `ea-nginx` package.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200364 import InlineResponse200364
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
    api_instance = clientapi_cpanel.NginxCachingApi(api_client)

    try:
        # Reset the user's NGINX cache configuration
        api_response = api_instance.reset_cache_config()
        print("The response of NginxCachingApi->reset_cache_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NginxCachingApi->reset_cache_config: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**InlineResponse200364**](InlineResponse200364.md)

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

