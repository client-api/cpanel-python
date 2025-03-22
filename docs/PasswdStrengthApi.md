# clientapi_cpanel.PasswdStrengthApi

All URIs are relative to *https://cpanel-server.tld:2083/execute*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_required_strength**](PasswdStrengthApi.md#get_required_strength) | **GET** /PasswdStrength/get_required_strength | Return minimum required password strength


# **get_required_strength**
> InlineResponse200374 get_required_strength(app)

Return minimum required password strength

This function retrieves an application's minimum required password strength.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200374 import InlineResponse200374
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
    api_instance = clientapi_cpanel.PasswdStrengthApi(api_client)
    app = 'webdisk' # str | The application's name.

    try:
        # Return minimum required password strength
        api_response = api_instance.get_required_strength(app)
        print("The response of PasswdStrengthApi->get_required_strength:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PasswdStrengthApi->get_required_strength: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app** | **str**| The application&#39;s name. | 

### Return type

[**InlineResponse200374**](InlineResponse200374.md)

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

