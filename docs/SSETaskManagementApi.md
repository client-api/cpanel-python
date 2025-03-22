# clientapi_cpanel.SSETaskManagementApi

All URIs are relative to *https://cpanel-server.tld:2083/execute*

Method | HTTP request | Description
------------- | ------------- | -------------
[**retrieve**](SSETaskManagementApi.md#retrieve) | **GET** /UserTasks/retrieve | Return task queue information
[**user_tasks_delete**](SSETaskManagementApi.md#user_tasks_delete) | **GET** /UserTasks/delete | Remove item from task queue


# **retrieve**
> InlineResponse200538 retrieve()

Return task queue information

This function retrieves a cPanel account's user task queue information.

Each cPanel account uses a separate user task queue in order to ensure that
processes for one user do not impede another user on the server.

* For example, the [*Git Version Control*](https://go.cpanel.net/GitVersionControl)
interface (*cPanel >> Home >> Files >> Git Version Control*) uses the user task queue
to clone repositories (via the `VersionControl::create` function).
* For more information, read our
[Task Queue Monitor](https://go.cpanel.net/whmdocsTaskQueueMonitor) documentation.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200538 import InlineResponse200538
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
    api_instance = clientapi_cpanel.SSETaskManagementApi(api_client)

    try:
        # Return task queue information
        api_response = api_instance.retrieve()
        print("The response of SSETaskManagementApi->retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SSETaskManagementApi->retrieve: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**InlineResponse200538**](InlineResponse200538.md)

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

# **user_tasks_delete**
> InlineResponse200537 user_tasks_delete(id)

Remove item from task queue

This function deletes a process from the user task queue.

Each cPanel account uses a separate user task queue in order to ensure that
processes for one user do not impede another user on the server.

* For example, the [*Git Version Control*](https://go.cpanel.net/GitVersionControl)
interface (*cPanel >> Home >> Files >> Git Version Control*) uses the user task queue
to clone repositories (via the `VersionControl::create` function).
* For more information, read our
[Task Queue Monitor](https://go.cpanel.net/whmdocsTaskQueueMonitor) documentation.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200537 import InlineResponse200537
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
    api_instance = clientapi_cpanel.SSETaskManagementApi(api_client)
    id = '00000000/5a9ec8dd4c345d' # str | The task's ID number.

    try:
        # Remove item from task queue
        api_response = api_instance.user_tasks_delete(id)
        print("The response of SSETaskManagementApi->user_tasks_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SSETaskManagementApi->user_tasks_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The task&#39;s ID number. | 

### Return type

[**InlineResponse200537**](InlineResponse200537.md)

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

