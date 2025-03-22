# clientapi_cpanel.CPAddonsApi

All URIs are relative to *https://cpanel-server.tld:2083/execute*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_available_addons**](CPAddonsApi.md#get_available_addons) | **GET** /cPAddons/get_available_addons | Return available cPAddons
[**get_instance_settings**](CPAddonsApi.md#get_instance_settings) | **GET** /cPAddons/get_instance_settings | Return deployed cPAddons instance&#39;s settings
[**list_addon_instances**](CPAddonsApi.md#list_addon_instances) | **GET** /cPAddons/list_addon_instances | Return deployed cPAddons instances


# **get_available_addons**
> InlineResponse200578 get_available_addons()

Return available cPAddons

This function lists an account's available cPAddons.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200578 import InlineResponse200578
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
    api_instance = clientapi_cpanel.CPAddonsApi(api_client)

    try:
        # Return available cPAddons
        api_response = api_instance.get_available_addons()
        print("The response of CPAddonsApi->get_available_addons:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CPAddonsApi->get_available_addons: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**InlineResponse200578**](InlineResponse200578.md)

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

# **get_instance_settings**
> InlineResponse200579 get_instance_settings(unique_id)

Return deployed cPAddons instance's settings

This function lists a cPAddons instance's settings.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200579 import InlineResponse200579
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
    api_instance = clientapi_cpanel.CPAddonsApi(api_client)
    unique_id = 'cPanel::Blogs::WordPressX.0.1486754861' # str | The unique identifier of the cPAddon.  **Note:**  To find this identifier, run the `list_addon_instances` function.

    try:
        # Return deployed cPAddons instance's settings
        api_response = api_instance.get_instance_settings(unique_id)
        print("The response of CPAddonsApi->get_instance_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CPAddonsApi->get_instance_settings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **unique_id** | **str**| The unique identifier of the cPAddon.  **Note:**  To find this identifier, run the &#x60;list_addon_instances&#x60; function. | 

### Return type

[**InlineResponse200579**](InlineResponse200579.md)

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

# **list_addon_instances**
> InlineResponse200580 list_addon_instances(addon=addon)

Return deployed cPAddons instances

This function lists an account's deployed cPAddons instances.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200580 import InlineResponse200580
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
    api_instance = clientapi_cpanel.CPAddonsApi(api_client)
    addon = 'cPanel::Blogs::WordPressX' # str | The cPAddon for which to return the instances data. (optional)

    try:
        # Return deployed cPAddons instances
        api_response = api_instance.list_addon_instances(addon=addon)
        print("The response of CPAddonsApi->list_addon_instances:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CPAddonsApi->list_addon_instances: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **addon** | **str**| The cPAddon for which to return the instances data. | [optional] 

### Return type

[**InlineResponse200580**](InlineResponse200580.md)

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

