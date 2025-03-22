# clientapi_cpanel.BlockIPApi

All URIs are relative to *https://cpanel-server.tld:2083/execute*

Method | HTTP request | Description
------------- | ------------- | -------------
[**blockip_add_ip**](BlockIPApi.md#blockip_add_ip) | **GET** /BlockIP/add_ip | Add IP address to cPanel account&#39;s block list
[**blockip_remove_ip**](BlockIPApi.md#blockip_remove_ip) | **GET** /BlockIP/remove_ip | Remove IP address from cPanel account&#39;s block list


# **blockip_add_ip**
> InlineResponse20015 blockip_add_ip(ip)

Add IP address to cPanel account's block list

This function blocks IP addresses from accessing the domains on a cPanel account.

**Important**

When you disable the Web Server role, the system disables this function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response20015 import InlineResponse20015
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
    api_instance = clientapi_cpanel.BlockIPApi(api_client)
    ip = '192.168.0.1/16' # str | The IP address or IP address range that you wish to block.

    try:
        # Add IP address to cPanel account's block list
        api_response = api_instance.blockip_add_ip(ip)
        print("The response of BlockIPApi->blockip_add_ip:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BlockIPApi->blockip_add_ip: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ip** | **str**| The IP address or IP address range that you wish to block. | 

### Return type

[**InlineResponse20015**](InlineResponse20015.md)

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

# **blockip_remove_ip**
> InlineResponse20016 blockip_remove_ip(ip)

Remove IP address from cPanel account's block list

This function unblocks IP addresses from accessing domains on a cPanel account.

**Important**

When you disable the Web Server role, the system disables this function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response20016 import InlineResponse20016
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
    api_instance = clientapi_cpanel.BlockIPApi(api_client)
    ip = '192.168.0.1/16' # str | The IP address or IP address range that you wish to unblock.

    try:
        # Remove IP address from cPanel account's block list
        api_response = api_instance.blockip_remove_ip(ip)
        print("The response of BlockIPApi->blockip_remove_ip:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BlockIPApi->blockip_remove_ip: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ip** | **str**| The IP address or IP address range that you wish to unblock. | 

### Return type

[**InlineResponse20016**](InlineResponse20016.md)

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

