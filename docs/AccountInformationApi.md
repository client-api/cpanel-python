# clientapi_cpanel.AccountInformationApi

All URIs are relative to *https://cpanel-server.tld:2083/execute*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_accounts**](AccountInformationApi.md#list_accounts) | **GET** /Resellers/list_accounts | Return reseller&#39;s cPanel accounts
[**variables_get_user_information**](AccountInformationApi.md#variables_get_user_information) | **GET** /Variables/get_user_information | Return cPanel account&#39;s configuration settings


# **list_accounts**
> InlineResponse200395 list_accounts()

Return reseller's cPanel accounts

This function lists all of a reseller's cPanel accounts.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200395 import InlineResponse200395
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
    api_instance = clientapi_cpanel.AccountInformationApi(api_client)

    try:
        # Return reseller's cPanel accounts
        api_response = api_instance.list_accounts()
        print("The response of AccountInformationApi->list_accounts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountInformationApi->list_accounts: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**InlineResponse200395**](InlineResponse200395.md)

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

# **variables_get_user_information**
> InlineResponse200541 variables_get_user_information(name=name)

Return cPanel account's configuration settings

This function retrieves the user's account configuration settings.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200541 import InlineResponse200541
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
    api_instance = clientapi_cpanel.AccountInformationApi(api_client)
    name = 'name-1=mailbox_format&name-2=home&name-3=shell' # str | The user configuration variables to retrieve. If you don't use this parameter, this function returns **all** of the user's configuration data.  **Note:**  To retrieve multiple account configuration settings for a user, increment the parameter name. For example: `name-0`, `name-1`, and `name-2`. (optional)

    try:
        # Return cPanel account's configuration settings
        api_response = api_instance.variables_get_user_information(name=name)
        print("The response of AccountInformationApi->variables_get_user_information:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountInformationApi->variables_get_user_information: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The user configuration variables to retrieve. If you don&#39;t use this parameter, this function returns **all** of the user&#39;s configuration data.  **Note:**  To retrieve multiple account configuration settings for a user, increment the parameter name. For example: &#x60;name-0&#x60;, &#x60;name-1&#x60;, and &#x60;name-2&#x60;. | [optional] 

### Return type

[**InlineResponse200541**](InlineResponse200541.md)

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

