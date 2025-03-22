# clientapi_cpanel.LogsApi

All URIs are relative to *https://cpanel-server.tld:2083/execute*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_settings**](LogsApi.md#get_settings) | **GET** /LogManager/get_settings | Retrieve cPanel account&#39;s log archival settings
[**list_archives**](LogsApi.md#list_archives) | **GET** /LogManager/list_archives | Return cPanel account&#39;s archive files list
[**set_settings**](LogsApi.md#set_settings) | **GET** /LogManager/set_settings | Save cPanel account&#39;s log archive settings


# **get_settings**
> InlineResponse200294 get_settings()

Retrieve cPanel account's log archival settings

This function retrieves the account's log archival settings.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200294 import InlineResponse200294
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
    api_instance = clientapi_cpanel.LogsApi(api_client)

    try:
        # Retrieve cPanel account's log archival settings
        api_response = api_instance.get_settings()
        print("The response of LogsApi->get_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LogsApi->get_settings: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**InlineResponse200294**](InlineResponse200294.md)

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

# **list_archives**
> InlineResponse200295 list_archives()

Return cPanel account's archive files list

This function returns a list of the user's archive files.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200295 import InlineResponse200295
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
    api_instance = clientapi_cpanel.LogsApi(api_client)

    try:
        # Return cPanel account's archive files list
        api_response = api_instance.list_archives()
        print("The response of LogsApi->list_archives:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LogsApi->list_archives: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**InlineResponse200295**](InlineResponse200295.md)

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

# **set_settings**
> InlineResponse200296 set_settings(archive_logs=archive_logs, prune_archive=prune_archive)

Save cPanel account's log archive settings

This function saves the account's log archive settings.

**Note:**

You **must** pass either the `archive_logs` or the `prune_archives` parameter.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200296 import InlineResponse200296
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
    api_instance = clientapi_cpanel.LogsApi(api_client)
    archive_logs = 1 # int | Whether to archive log files to your home directory after the system processes statistics. * `1` — Archive the logs. * `0` — Do **not** archive the logs.  **Note:**  * This parameter defaults to the `archive-logs` setting's value in the user's `~/.cpanel-logs` file. * If this file does **not** exist, this parameter defaults to the `default_archive-logs` key's value in the [`cpanel.config`](https://go.cpanel.net/cpanelconfiginvalid) file. (optional)
    prune_archive = 1 # int | Whether to remove the previous month's archived logs from the `~/logs directory` at the end of each month. * `1` — Remove the logs. * `0` — Do **not** remove the logs.  **Note:**  * This parameter defaults to the `remove-old-archived-logs` setting's value in the user's `~/.cpanel-logs` file. * If this file doesn't exist, this parameter defaults to the `default_remove-old-archive-logs` key's value in the [`cpanel.config`](https://go.cpanel.net/cpanelconfiginvalid) file. (optional)

    try:
        # Save cPanel account's log archive settings
        api_response = api_instance.set_settings(archive_logs=archive_logs, prune_archive=prune_archive)
        print("The response of LogsApi->set_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LogsApi->set_settings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **archive_logs** | **int**| Whether to archive log files to your home directory after the system processes statistics. * &#x60;1&#x60; — Archive the logs. * &#x60;0&#x60; — Do **not** archive the logs.  **Note:**  * This parameter defaults to the &#x60;archive-logs&#x60; setting&#39;s value in the user&#39;s &#x60;~/.cpanel-logs&#x60; file. * If this file does **not** exist, this parameter defaults to the &#x60;default_archive-logs&#x60; key&#39;s value in the [&#x60;cpanel.config&#x60;](https://go.cpanel.net/cpanelconfiginvalid) file. | [optional] 
 **prune_archive** | **int**| Whether to remove the previous month&#39;s archived logs from the &#x60;~/logs directory&#x60; at the end of each month. * &#x60;1&#x60; — Remove the logs. * &#x60;0&#x60; — Do **not** remove the logs.  **Note:**  * This parameter defaults to the &#x60;remove-old-archived-logs&#x60; setting&#39;s value in the user&#39;s &#x60;~/.cpanel-logs&#x60; file. * If this file doesn&#39;t exist, this parameter defaults to the &#x60;default_remove-old-archive-logs&#x60; key&#39;s value in the [&#x60;cpanel.config&#x60;](https://go.cpanel.net/cpanelconfiginvalid) file. | [optional] 

### Return type

[**InlineResponse200296**](InlineResponse200296.md)

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

