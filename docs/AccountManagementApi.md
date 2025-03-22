# clientapi_cpanel.AccountManagementApi

All URIs are relative to *https://cpanel-server.tld:2083/execute*

Method | HTTP request | Description
------------- | ------------- | -------------
[**change_password**](AccountManagementApi.md#change_password) | **GET** /UserManager/change_password | Update cPanel account password


# **change_password**
> InlineResponse200526 change_password(newpass, oldpass, enablemysql=enablemysql)

Update cPanel account password

This function updates the cPanel account's password.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200526 import InlineResponse200526
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
    api_instance = clientapi_cpanel.AccountManagementApi(api_client)
    newpass = 'MyNewPassw0rd!' # str | The new password.
    oldpass = 'ThisWasMyPassword!' # str | The current password.
    enablemysql = 0 # int | Whether to update the cPanel account's MySQL password. * `1` - Update MySQL password. * `0` - Do not update MySQL passowrd. (optional) (default to 0)

    try:
        # Update cPanel account password
        api_response = api_instance.change_password(newpass, oldpass, enablemysql=enablemysql)
        print("The response of AccountManagementApi->change_password:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountManagementApi->change_password: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **newpass** | **str**| The new password. | 
 **oldpass** | **str**| The current password. | 
 **enablemysql** | **int**| Whether to update the cPanel account&#39;s MySQL password. * &#x60;1&#x60; - Update MySQL password. * &#x60;0&#x60; - Do not update MySQL passowrd. | [optional] [default to 0]

### Return type

[**InlineResponse200526**](InlineResponse200526.md)

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

