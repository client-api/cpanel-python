# clientapi_cpanel.WeblogSettingsApi

All URIs are relative to *https://cpanel-server.tld:2083/execute*

Method | HTTP request | Description
------------- | ------------- | -------------
[**stats_manager_get_configuration**](WeblogSettingsApi.md#stats_manager_get_configuration) | **GET** /StatsManager/get_configuration | Returns weblog analyzers&#39; configuration
[**stats_manager_save_configuration**](WeblogSettingsApi.md#stats_manager_save_configuration) | **POST** /StatsManager/save_configuration | Save current user&#39;s weblog analyzers configuration


# **stats_manager_get_configuration**
> InlineResponse200493 stats_manager_get_configuration()

Returns weblog analyzers' configuration

This function lists the configuration of the web log anayzers for each domain on the cPanel account.

**Important:**

When you disable the WebServer role the system disables this function. For more information, read our How to Use [Server Profiles documentation](https://docs.cpanel.net/knowledge-base/general-systems-administration/how-to-use-server-profiles/).

**Note**

Additional web log analyzer configuration such as if the user can edit their own configuration is provided in the metadata section of the return.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200493 import InlineResponse200493
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
    api_instance = clientapi_cpanel.WeblogSettingsApi(api_client)

    try:
        # Returns weblog analyzers' configuration
        api_response = api_instance.stats_manager_get_configuration()
        print("The response of WeblogSettingsApi->stats_manager_get_configuration:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WeblogSettingsApi->stats_manager_get_configuration: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**InlineResponse200493**](InlineResponse200493.md)

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

# **stats_manager_save_configuration**
> InlineResponse200494 stats_manager_save_configuration(stats_manager_save_configuration_body=stats_manager_save_configuration_body)

Save current user's weblog analyzers configuration

This function saves the users choice about which web log anayzers are enabled for each domain on their cPanel users account.
If the log anayzers are controlled by the reseller or root account, the user cannot manage which log analyzers are enabled or disabled.

**Important:**

When you disable the WebServer role the system disables this function. For more information, read our How to Use Server Profiles documentation.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200494 import InlineResponse200494
from clientapi_cpanel.models.stats_manager_save_configuration_body import StatsManagerSaveConfigurationBody
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
    api_instance = clientapi_cpanel.WeblogSettingsApi(api_client)
    stats_manager_save_configuration_body = clientapi_cpanel.StatsManagerSaveConfigurationBody() # StatsManagerSaveConfigurationBody | List of domains and what web log analyzers to change. (optional)

    try:
        # Save current user's weblog analyzers configuration
        api_response = api_instance.stats_manager_save_configuration(stats_manager_save_configuration_body=stats_manager_save_configuration_body)
        print("The response of WeblogSettingsApi->stats_manager_save_configuration:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WeblogSettingsApi->stats_manager_save_configuration: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stats_manager_save_configuration_body** | [**StatsManagerSaveConfigurationBody**](StatsManagerSaveConfigurationBody.md)| List of domains and what web log analyzers to change. | [optional] 

### Return type

[**InlineResponse200494**](InlineResponse200494.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | HTTP Request was successful. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

