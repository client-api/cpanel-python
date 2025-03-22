# clientapi_cpanel.DirectoryProtectionApi

All URIs are relative to *https://cpanel-server.tld:2083/execute*

Method | HTTP request | Description
------------- | ------------- | -------------
[**directory_protection_list_directories**](DirectoryProtectionApi.md#directory_protection_list_directories) | **GET** /DirectoryProtection/list_directories | Return Directory Protection settings


# **directory_protection_list_directories**
> InlineResponse200109 directory_protection_list_directories(dir)

Return Directory Protection settings

This function returns the
[leech protection](https://go.cpanel.net/cpaneldocsLeechProtection)
settings of the subdirectories in a directory.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200109 import InlineResponse200109
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
    api_instance = clientapi_cpanel.DirectoryProtectionApi(api_client)
    dir = '/home/example/example.com' # str | The absolute or relative file path in the user's `home` directory for which to return leech protection information.

    try:
        # Return Directory Protection settings
        api_response = api_instance.directory_protection_list_directories(dir)
        print("The response of DirectoryProtectionApi->directory_protection_list_directories:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DirectoryProtectionApi->directory_protection_list_directories: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dir** | **str**| The absolute or relative file path in the user&#39;s &#x60;home&#x60; directory for which to return leech protection information. | 

### Return type

[**InlineResponse200109**](InlineResponse200109.md)

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

