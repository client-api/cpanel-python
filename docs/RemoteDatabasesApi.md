# clientapi_cpanel.RemoteDatabasesApi

All URIs are relative to *https://cpanel-server.tld:2083/execute*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_host**](RemoteDatabasesApi.md#add_host) | **GET** /Mysql/add_host | Enable remote MySQL host access
[**delete_host**](RemoteDatabasesApi.md#delete_host) | **GET** /Mysql/delete_host | Disable remote MySQL host access
[**get_host_notes**](RemoteDatabasesApi.md#get_host_notes) | **GET** /Mysql/get_host_notes | Return remote MySQL host notes
[**mysql_add_host_note**](RemoteDatabasesApi.md#mysql_add_host_note) | **GET** /Mysql/add_host_note | Add remote MySQL host note


# **add_host**
> InlineResponse200336 add_host(host)

Enable remote MySQL host access

This function authorizes a remote MySQL® host to access the account's databases.

**Important:**

When you disable the [MySQL role](https://go.cpanel.net/serverroles)
 and remote MySQL is **not** already configured,
 the system **disables** this function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200336 import InlineResponse200336
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
    api_instance = clientapi_cpanel.RemoteDatabasesApi(api_client)
    host = clientapi_cpanel.Host3() # Host3 | The remote MySQL server's hostname or IP address.  You may use the following IP address formats:  * `192.168.1.6` — IP address. * `192.168.%.%` — Range with the percent (%) symbol as a wildcard. * `192.168.0.0/16` — Range in CIDR format.

    try:
        # Enable remote MySQL host access
        api_response = api_instance.add_host(host)
        print("The response of RemoteDatabasesApi->add_host:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RemoteDatabasesApi->add_host: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **host** | [**Host3**](.md)| The remote MySQL server&#39;s hostname or IP address.  You may use the following IP address formats:  * &#x60;192.168.1.6&#x60; — IP address. * &#x60;192.168.%.%&#x60; — Range with the percent (%) symbol as a wildcard. * &#x60;192.168.0.0/16&#x60; — Range in CIDR format. | 

### Return type

[**InlineResponse200336**](InlineResponse200336.md)

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

# **delete_host**
> InlineResponse200342 delete_host(host)

Disable remote MySQL host access

This function removes a remote MySQL® host's access to the account's databases.

**Important:**

When you disable the [MySQL role](https://go.cpanel.net/serverroles) and remote MySQL is not already configured, the system **disables** this function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200342 import InlineResponse200342
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
    api_instance = clientapi_cpanel.RemoteDatabasesApi(api_client)
    host = 'remote.example.com' # str | The remote MySQL server's hostname, IP Address, or IP address range.  **Note:** You may use the following IP address formats:  192.168.1.6 — IP address. 192.168.%.% — Range with the percent (%) symbol as a wildcard. 192.168.0.0/16 — Range in CIDR format.

    try:
        # Disable remote MySQL host access
        api_response = api_instance.delete_host(host)
        print("The response of RemoteDatabasesApi->delete_host:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RemoteDatabasesApi->delete_host: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **host** | **str**| The remote MySQL server&#39;s hostname, IP Address, or IP address range.  **Note:** You may use the following IP address formats:  192.168.1.6 — IP address. 192.168.%.% — Range with the percent (%) symbol as a wildcard. 192.168.0.0/16 — Range in CIDR format. | 

### Return type

[**InlineResponse200342**](InlineResponse200342.md)

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

# **get_host_notes**
> InlineResponse200345 get_host_notes()

Return remote MySQL host notes

This function returns the notes associated with the account's remote MySQL® hosts.

**Important:**

  When you disable the [*MySQL/MariaDB* role](https://go.cpanel.net/serverroles)
  **and** remote MySQL is **not** already configured, the system **disables** this function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200345 import InlineResponse200345
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
    api_instance = clientapi_cpanel.RemoteDatabasesApi(api_client)

    try:
        # Return remote MySQL host notes
        api_response = api_instance.get_host_notes()
        print("The response of RemoteDatabasesApi->get_host_notes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RemoteDatabasesApi->get_host_notes: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**InlineResponse200345**](InlineResponse200345.md)

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

# **mysql_add_host_note**
> InlineResponse200337 mysql_add_host_note(host, note)

Add remote MySQL host note

This function adds a note about a remote MySQL® server.

**Important:**

* If you attempt to add a note to an unauthorized remote MySQL server, the function will fail.
* When you **disable** the [MySQL role](https://go.cpanel.net/serverroles), the system disables this function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200337 import InlineResponse200337
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
    api_instance = clientapi_cpanel.RemoteDatabasesApi(api_client)
    host = clientapi_cpanel.Host4() # Host4 | The remote MySQL server's hostname or IP address.  You may use the following IP address formats:  * `192.168.1.6` — IP address. * `192.168.%.%` — Range with the percent (%) symbol as a wildcard. * `192.168.0.0/16` — Range in CIDR format.
    note = 'A remote mysql server for storing my data' # str | note that describes the remote MySQL server.

    try:
        # Add remote MySQL host note
        api_response = api_instance.mysql_add_host_note(host, note)
        print("The response of RemoteDatabasesApi->mysql_add_host_note:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RemoteDatabasesApi->mysql_add_host_note: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **host** | [**Host4**](.md)| The remote MySQL server&#39;s hostname or IP address.  You may use the following IP address formats:  * &#x60;192.168.1.6&#x60; — IP address. * &#x60;192.168.%.%&#x60; — Range with the percent (%) symbol as a wildcard. * &#x60;192.168.0.0/16&#x60; — Range in CIDR format. | 
 **note** | **str**| note that describes the remote MySQL server. | 

### Return type

[**InlineResponse200337**](InlineResponse200337.md)

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

