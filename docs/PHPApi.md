# clientapi_cpanel.PHPApi

All URIs are relative to *https://cpanel-server.tld:2083/execute*

Method | HTTP request | Description
------------- | ------------- | -------------
[**e_a4_get_php_recommendations**](PHPApi.md#e_a4_get_php_recommendations) | **GET** /get_php_recommendations | Get custom PHP recommendations.


# **e_a4_get_php_recommendations**
> InlineResponse200587 e_a4_get_php_recommendations()

Get custom PHP recommendations.

This function returns a list of recommended PHP versions.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200587 import InlineResponse200587
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
    api_instance = clientapi_cpanel.PHPApi(api_client)

    try:
        # Get custom PHP recommendations.
        api_response = api_instance.e_a4_get_php_recommendations()
        print("The response of PHPApi->e_a4_get_php_recommendations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PHPApi->e_a4_get_php_recommendations: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**InlineResponse200587**](InlineResponse200587.md)

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

