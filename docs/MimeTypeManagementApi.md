# clientapi_cpanel.MimeTypeManagementApi

All URIs are relative to *https://cpanel-server.tld:2083/execute*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_mime**](MimeTypeManagementApi.md#add_mime) | **GET** /Mime/add_mime | Add MIME type to web server
[**delete_mime**](MimeTypeManagementApi.md#delete_mime) | **GET** /Mime/delete_mime | Remove MIME type from web server
[**list_mime**](MimeTypeManagementApi.md#list_mime) | **GET** /Mime/list_mime | Return web server&#39;s MIME types


# **add_mime**
> InlineResponse200318 add_mime(extension, type)

Add MIME type to web server

This function adds a MIME type to Apache.

**Important:**

When you disable the [Web Server](https://go.cpanel.net/serverroles) role, the system **disables** this function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200318 import InlineResponse200318
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
    api_instance = clientapi_cpanel.MimeTypeManagementApi(api_client)
    extension = '.foo' # str | The file extension.
    type = 'text/foo' # str | The MIME type.

    try:
        # Add MIME type to web server
        api_response = api_instance.add_mime(extension, type)
        print("The response of MimeTypeManagementApi->add_mime:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MimeTypeManagementApi->add_mime: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **extension** | **str**| The file extension. | 
 **type** | **str**| The MIME type. | 

### Return type

[**InlineResponse200318**](InlineResponse200318.md)

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

# **delete_mime**
> InlineResponse200322 delete_mime(type)

Remove MIME type from web server

This function removes a MIME type from Apache.

**Important:**

  When you disable the [WebServer role](https://go.cpanel.net/serverroles), the system **disables** this function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200322 import InlineResponse200322
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
    api_instance = clientapi_cpanel.MimeTypeManagementApi(api_client)
    type = 'text/foo' # str | The MIME type.

    try:
        # Remove MIME type from web server
        api_response = api_instance.delete_mime(type)
        print("The response of MimeTypeManagementApi->delete_mime:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MimeTypeManagementApi->delete_mime: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| The MIME type. | 

### Return type

[**InlineResponse200322**](InlineResponse200322.md)

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

# **list_mime**
> InlineResponse200327 list_mime(type)

Return web server's MIME types

This function lists all of Apache's MIME types.

**Note:**

  This function does **not** list PHP versions with MIME types when the user or domain enables PHP-FPM. The system displays **only** custom MIME types.

**Important:**

  When you disable the [Web Server role](https://go.cpanel.net/serverroles), the system **disables** this function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200327 import InlineResponse200327
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
    api_instance = clientapi_cpanel.MimeTypeManagementApi(api_client)
    type = 'user' # str | The MIME types to list. * `system` — List the Apache system MIME types. * `user` — List the Apache user MIME types.

    try:
        # Return web server's MIME types
        api_response = api_instance.list_mime(type)
        print("The response of MimeTypeManagementApi->list_mime:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MimeTypeManagementApi->list_mime: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| The MIME types to list. * &#x60;system&#x60; — List the Apache system MIME types. * &#x60;user&#x60; — List the Apache user MIME types. | 

### Return type

[**InlineResponse200327**](InlineResponse200327.md)

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

