# clientapi_cpanel.WebmailAppsApi

All URIs are relative to *https://cpanel-server.tld:2083/execute*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_webmail_apps**](WebmailAppsApi.md#list_webmail_apps) | **GET** /WebmailApps/list_webmail_apps | Return available webmail clients


# **list_webmail_apps**
> InlineResponse200555 list_webmail_apps(theme=theme)

Return available webmail clients

This function lists the account's available webmail clients.

**Important:**

When you disable the [Receive Mail role](https://go.cpanel.net/howtouseserverprofiles#roles), the system **disables** this function. 

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200555 import InlineResponse200555
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
    api_instance = clientapi_cpanel.WebmailAppsApi(api_client)
    theme = 'the server's default theme' # str | The webmail theme. (optional) (default to 'the server's default theme')

    try:
        # Return available webmail clients
        api_response = api_instance.list_webmail_apps(theme=theme)
        print("The response of WebmailAppsApi->list_webmail_apps:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebmailAppsApi->list_webmail_apps: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **theme** | **str**| The webmail theme. | [optional] [default to &#39;the server&#39;s default theme&#39;]

### Return type

[**InlineResponse200555**](InlineResponse200555.md)

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

