# clientapi_cpanel.BrandManagementApi

All URIs are relative to *https://cpanel-server.tld:2083/execute*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_dom**](BrandManagementApi.md#get_dom) | **GET** /Chrome/get_dom | Return cPanel theme header and footer HTML


# **get_dom**
> InlineResponse20062 get_dom(page_title)

Return cPanel theme header and footer HTML

This function returns header and footer HTML. You can use this HTML to create a page with the same visual appearance as your cPanel theme.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response20062 import InlineResponse20062
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
    api_instance = clientapi_cpanel.BrandManagementApi(api_client)
    page_title = 'Test' # str | The title of the page to wrap in the theme's headers and footers.

    try:
        # Return cPanel theme header and footer HTML
        api_response = api_instance.get_dom(page_title)
        print("The response of BrandManagementApi->get_dom:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BrandManagementApi->get_dom: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_title** | **str**| The title of the page to wrap in the theme&#39;s headers and footers. | 

### Return type

[**InlineResponse20062**](InlineResponse20062.md)

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

