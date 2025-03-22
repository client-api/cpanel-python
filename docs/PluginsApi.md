# clientapi_cpanel.PluginsApi

All URIs are relative to *https://cpanel-server.tld:2083/execute*

Method | HTTP request | Description
------------- | ------------- | -------------
[**plugins_can_show_promotions**](PluginsApi.md#plugins_can_show_promotions) | **GET** /Plugins/can_show_promotions | Enable plugin promotions


# **plugins_can_show_promotions**
> InlineResponse200377 plugins_can_show_promotions(plugin)

Enable plugin promotions

This function determines if plugin promotions show in cPanel.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200377 import InlineResponse200377
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
    api_instance = clientapi_cpanel.PluginsApi(api_client)
    plugin = 'koality' # str | The plugin whose promotions to target.  **Note:**  The only valid value is 'koality', which targets Site Quality Monitoring.

    try:
        # Enable plugin promotions
        api_response = api_instance.plugins_can_show_promotions(plugin)
        print("The response of PluginsApi->plugins_can_show_promotions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PluginsApi->plugins_can_show_promotions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **plugin** | **str**| The plugin whose promotions to target.  **Note:**  The only valid value is &#39;koality&#39;, which targets Site Quality Monitoring. | 

### Return type

[**InlineResponse200377**](InlineResponse200377.md)

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

