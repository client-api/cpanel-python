# clientapi_cpanel.AccountEnhancementsApi

All URIs are relative to *https://cpanel-server.tld:2083/execute*

Method | HTTP request | Description
------------- | ------------- | -------------
[**account_enhancements_has_enhancement**](AccountEnhancementsApi.md#account_enhancements_has_enhancement) | **GET** /AccountEnhancements/has_enhancement | Validate Account Enhancement assignment
[**account_enhancements_list**](AccountEnhancementsApi.md#account_enhancements_list) | **GET** /AccountEnhancements/list | Return all cPanel account&#39;s Account Enhancements


# **account_enhancements_has_enhancement**
> InlineResponse200 account_enhancements_has_enhancement(id)

Validate Account Enhancement assignment

This function returns whether a cPanel account has a specific [Account Enhancement](https://go.cpanel.net/account-enhancements).

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200 import InlineResponse200
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
    api_instance = clientapi_cpanel.AccountEnhancementsApi(api_client)
    id = 'sample-enhancement-id' # str | The identifier for a specific Account Enhancement.  **Note:**  To retrieve a list of all Account Enhancements IDs on the server, run the WHM API 1 `list_account_enhancements` function.

    try:
        # Validate Account Enhancement assignment
        api_response = api_instance.account_enhancements_has_enhancement(id)
        print("The response of AccountEnhancementsApi->account_enhancements_has_enhancement:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountEnhancementsApi->account_enhancements_has_enhancement: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The identifier for a specific Account Enhancement.  **Note:**  To retrieve a list of all Account Enhancements IDs on the server, run the WHM API 1 &#x60;list_account_enhancements&#x60; function. | 

### Return type

[**InlineResponse200**](InlineResponse200.md)

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

# **account_enhancements_list**
> InlineResponse2001 account_enhancements_list()

Return all cPanel account's Account Enhancements

This function lists a cPanel account's [Account Enhancements](https://go.cpanel.net/account-enhancements).

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response2001 import InlineResponse2001
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
    api_instance = clientapi_cpanel.AccountEnhancementsApi(api_client)

    try:
        # Return all cPanel account's Account Enhancements
        api_response = api_instance.account_enhancements_list()
        print("The response of AccountEnhancementsApi->account_enhancements_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountEnhancementsApi->account_enhancements_list: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

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

