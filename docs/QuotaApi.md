# clientapi_cpanel.QuotaApi

All URIs are relative to *https://cpanel-server.tld:2083/execute*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_local_quota_info**](QuotaApi.md#get_local_quota_info) | **GET** /Quota/get_local_quota_info | Return local disk quota information
[**get_quota_info**](QuotaApi.md#get_quota_info) | **GET** /Quota/get_quota_info | Return disk quota information


# **get_local_quota_info**
> InlineResponse200393 get_local_quota_info()

Return local disk quota information

This function retrieves the cPanel account's quota for the server where you run the function. For example, a [distributed cPanel account](https://go.cpanel.net/glossaryD) could approach its quota. The servers will balance that cPanel user's quota between the parent and the child node.

**Note:**

  This function runs on **only** the local server. To retrieve the cPanel account's total quota, use the UAPI `Quota::get_quota` function instead.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200393 import InlineResponse200393
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
    api_instance = clientapi_cpanel.QuotaApi(api_client)

    try:
        # Return local disk quota information
        api_response = api_instance.get_local_quota_info()
        print("The response of QuotaApi->get_local_quota_info:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QuotaApi->get_local_quota_info: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**InlineResponse200393**](InlineResponse200393.md)

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

# **get_quota_info**
> InlineResponse200394 get_quota_info()

Return disk quota information

This function retrieves the cPanel account's quota.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200394 import InlineResponse200394
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
    api_instance = clientapi_cpanel.QuotaApi(api_client)

    try:
        # Return disk quota information
        api_response = api_instance.get_quota_info()
        print("The response of QuotaApi->get_quota_info:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QuotaApi->get_quota_info: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**InlineResponse200394**](InlineResponse200394.md)

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

