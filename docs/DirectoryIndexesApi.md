# clientapi_cpanel.DirectoryIndexesApi

All URIs are relative to *https://cpanel-server.tld:2083/execute*

Method | HTTP request | Description
------------- | ------------- | -------------
[**directory_indexes_list_directories**](DirectoryIndexesApi.md#directory_indexes_list_directories) | **GET** /DirectoryIndexes/list_directories | Return subdirectories directory indexing settings
[**get_indexing**](DirectoryIndexesApi.md#get_indexing) | **GET** /DirectoryIndexes/get_indexing | Return directory indexing settings
[**set_indexing**](DirectoryIndexesApi.md#set_indexing) | **GET** /DirectoryIndexes/set_indexing | Update directory indexing settings


# **directory_indexes_list_directories**
> InlineResponse200101 directory_indexes_list_directories(dir)

Return subdirectories directory indexing settings

This function returns the [directory indexing](https://go.cpanel.net/cpaneldocsIndexes) settings of the subdirectories in a directory.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200101 import InlineResponse200101
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
    api_instance = clientapi_cpanel.DirectoryIndexesApi(api_client)
    dir = '/home/example/example.com' # str | The absolute path of the directory for which to return indexing information.

    try:
        # Return subdirectories directory indexing settings
        api_response = api_instance.directory_indexes_list_directories(dir)
        print("The response of DirectoryIndexesApi->directory_indexes_list_directories:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DirectoryIndexesApi->directory_indexes_list_directories: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dir** | **str**| The absolute path of the directory for which to return indexing information. | 

### Return type

[**InlineResponse200101**](InlineResponse200101.md)

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

# **get_indexing**
> InlineResponse200100 get_indexing(dir)

Return directory indexing settings

This function returns the directory indexing settings for a directory on the cPanel account and its subdirectories.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200100 import InlineResponse200100
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
    api_instance = clientapi_cpanel.DirectoryIndexesApi(api_client)
    dir = '/home/example/example.com' # str | The directory for which to check the indexing type.

    try:
        # Return directory indexing settings
        api_response = api_instance.get_indexing(dir)
        print("The response of DirectoryIndexesApi->get_indexing:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DirectoryIndexesApi->get_indexing: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dir** | **str**| The directory for which to check the indexing type. | 

### Return type

[**InlineResponse200100**](InlineResponse200100.md)

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

# **set_indexing**
> InlineResponse200102 set_indexing(dir, type)

Update directory indexing settings

This function configures the [directory indexing](https://go.cpanel.net/cpaneldocsIndexes) settings for a directory on the cPanel account.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200102 import InlineResponse200102
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
    api_instance = clientapi_cpanel.DirectoryIndexesApi(api_client)
    dir = '/home/example/example.com' # str | The directory for which to manage directory indexing.
    type = 'inherit' # str | The type of directory indexing.  * `standard` — The directory uses directory indexing with standard formatting. * `disabled` — The directory doesn't use directory indexing. * `inherit` — The directory uses the system's default settings. * `fancy` — The directory uses directory indexing with Apache FancyIndexing directive. The directory will include additional information such as file size and the date of the file's last update.

    try:
        # Update directory indexing settings
        api_response = api_instance.set_indexing(dir, type)
        print("The response of DirectoryIndexesApi->set_indexing:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DirectoryIndexesApi->set_indexing: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dir** | **str**| The directory for which to manage directory indexing. | 
 **type** | **str**| The type of directory indexing.  * &#x60;standard&#x60; — The directory uses directory indexing with standard formatting. * &#x60;disabled&#x60; — The directory doesn&#39;t use directory indexing. * &#x60;inherit&#x60; — The directory uses the system&#39;s default settings. * &#x60;fancy&#x60; — The directory uses directory indexing with Apache FancyIndexing directive. The directory will include additional information such as file size and the date of the file&#39;s last update. | 

### Return type

[**InlineResponse200102**](InlineResponse200102.md)

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

