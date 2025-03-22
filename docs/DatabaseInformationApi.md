# clientapi_cpanel.DatabaseInformationApi

All URIs are relative to *https://cpanel-server.tld:2083/execute*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_server_information**](DatabaseInformationApi.md#get_server_information) | **GET** /Mysql/get_server_information | Return MySQL server host information and version
[**locate_server**](DatabaseInformationApi.md#locate_server) | **GET** /Mysql/locate_server | Return MySQL server host information


# **get_server_information**
> InlineResponse200348 get_server_information()

Return MySQL server host information and version

This function returns information about the account's MySQL® host.

**Important:**

  When you disable the [MySQL role](https://go.cpanel.net/serverroles) **and** remote MySQL is **not** already configured, the system **disables** this function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200348 import InlineResponse200348
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
    api_instance = clientapi_cpanel.DatabaseInformationApi(api_client)

    try:
        # Return MySQL server host information and version
        api_response = api_instance.get_server_information()
        print("The response of DatabaseInformationApi->get_server_information:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatabaseInformationApi->get_server_information: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**InlineResponse200348**](InlineResponse200348.md)

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

# **locate_server**
> InlineResponse200352 locate_server()

Return MySQL server host information

This function returns information about the account's MySQL® host.

**Important:**

When you disable the [MySQL/MariaDB role](https://go.cpanel.net/serverroles#roles) **and** remote MySQL is **not** already configured, the system **disables** this function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200352 import InlineResponse200352
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
    api_instance = clientapi_cpanel.DatabaseInformationApi(api_client)

    try:
        # Return MySQL server host information
        api_response = api_instance.locate_server()
        print("The response of DatabaseInformationApi->locate_server:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatabaseInformationApi->locate_server: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**InlineResponse200352**](InlineResponse200352.md)

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

