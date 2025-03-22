# clientapi_cpanel.HandlerManagementApi

All URIs are relative to *https://cpanel-server.tld:2083/execute*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_handler**](HandlerManagementApi.md#add_handler) | **GET** /Mime/add_handler | Add web server MIME type handler
[**delete_handler**](HandlerManagementApi.md#delete_handler) | **GET** /Mime/delete_handler | Remove web server MIME type handler
[**list_handlers**](HandlerManagementApi.md#list_handlers) | **GET** /Mime/list_handlers | Return web server&#39;s MIME handlers
[**redirect_info**](HandlerManagementApi.md#redirect_info) | **GET** /Mime/redirect_info | Return redirect information


# **add_handler**
> InlineResponse200316 add_handler(extension, handler)

Add web server MIME type handler

This function creates an Apache MIME type handler for a file extension.

**Important:**

When you disable the [Web Server](https://go.cpanel.net/serverroles) role, the system **disables** this function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200316 import InlineResponse200316
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
    api_instance = clientapi_cpanel.HandlerManagementApi(api_client)
    extension = '.foo' # str | The file extension.
    handler = 'txt-foo' # str | The Apache MIME handler.

    try:
        # Add web server MIME type handler
        api_response = api_instance.add_handler(extension, handler)
        print("The response of HandlerManagementApi->add_handler:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HandlerManagementApi->add_handler: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **extension** | **str**| The file extension. | 
 **handler** | **str**| The Apache MIME handler. | 

### Return type

[**InlineResponse200316**](InlineResponse200316.md)

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

# **delete_handler**
> InlineResponse200320 delete_handler(extension)

Remove web server MIME type handler

This function deletes an Apache MIME type handler.

**Important:**

  When you disable the [WebServer role](https://go.cpanel.net/serverroles), the system **disables** this function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200320 import InlineResponse200320
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
    api_instance = clientapi_cpanel.HandlerManagementApi(api_client)
    extension = '.foo' # str | The file extension.

    try:
        # Remove web server MIME type handler
        api_response = api_instance.delete_handler(extension)
        print("The response of HandlerManagementApi->delete_handler:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HandlerManagementApi->delete_handler: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **extension** | **str**| The file extension. | 

### Return type

[**InlineResponse200320**](InlineResponse200320.md)

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

# **list_handlers**
> InlineResponse200325 list_handlers(type)

Return web server's MIME handlers

This function lists all of Apache's MIME handlers.

**Important:**

  When you disable the [WebServer role](https://go.cpanel.net/serverroles),
  the system **disables** this function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200325 import InlineResponse200325
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
    api_instance = clientapi_cpanel.HandlerManagementApi(api_client)
    type = 'user' # str | Whether to retrieve system or user handlers.

    try:
        # Return web server's MIME handlers
        api_response = api_instance.list_handlers(type)
        print("The response of HandlerManagementApi->list_handlers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HandlerManagementApi->list_handlers: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| Whether to retrieve system or user handlers. | 

### Return type

[**InlineResponse200325**](InlineResponse200325.md)

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

# **redirect_info**
> InlineResponse200329 redirect_info(domain, url)

Return redirect information

This function retrieves redirect information for a URL or `** All Public Domains **`.

**Important:**

When you disable the [Web Server role](https://go.cpanel.net/serverroles), the system **disables** this function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200329 import InlineResponse200329
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
    api_instance = clientapi_cpanel.HandlerManagementApi(api_client)
    domain = 'example.com' # str | The domain for which to retrieve redirector information.
    url = 'http://redirect.example.com' # str | The URL for which to retrieve redirector information.

    try:
        # Return redirect information
        api_response = api_instance.redirect_info(domain, url)
        print("The response of HandlerManagementApi->redirect_info:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HandlerManagementApi->redirect_info: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**| The domain for which to retrieve redirector information. | 
 **url** | **str**| The URL for which to retrieve redirector information. | 

### Return type

[**InlineResponse200329**](InlineResponse200329.md)

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

