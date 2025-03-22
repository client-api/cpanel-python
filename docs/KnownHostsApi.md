# clientapi_cpanel.KnownHostsApi

All URIs are relative to *https://cpanel-server.tld:2083/execute*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create**](KnownHostsApi.md#create) | **GET** /KnownHosts/create | Create host
[**known_hosts_delete**](KnownHostsApi.md#known_hosts_delete) | **GET** /KnownHosts/delete | Delete host
[**known_hosts_update**](KnownHostsApi.md#known_hosts_update) | **GET** /KnownHosts/update | Update host in the known_hosts file
[**verify**](KnownHostsApi.md#verify) | **GET** /KnownHosts/verify | Validate host


# **create**
> InlineResponse200275 create(host_name, port=port)

Create host

This function registers a host in the cPanel account's `/home/user/.ssh/known_hosts` file.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200275 import InlineResponse200275
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
    api_instance = clientapi_cpanel.KnownHostsApi(api_client)
    host_name = clientapi_cpanel.HostName() # HostName | The hostname or IP address to add.
    port = 22 # int | The SSH port to use, if the system uses a non-standard SSH port. (optional) (default to 22)

    try:
        # Create host
        api_response = api_instance.create(host_name, port=port)
        print("The response of KnownHostsApi->create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KnownHostsApi->create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **host_name** | [**HostName**](.md)| The hostname or IP address to add. | 
 **port** | **int**| The SSH port to use, if the system uses a non-standard SSH port. | [optional] [default to 22]

### Return type

[**InlineResponse200275**](InlineResponse200275.md)

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

# **known_hosts_delete**
> InlineResponse200276 known_hosts_delete(host_name, port=port)

Delete host

This function removes a host from the cPanel account's `/home/user/.ssh/known_hosts` file.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200276 import InlineResponse200276
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
    api_instance = clientapi_cpanel.KnownHostsApi(api_client)
    host_name = clientapi_cpanel.HostName1() # HostName1 | The hostname or IP address of the host to delete.
    port = 22 # int | The SSH port to use. (optional) (default to 22)

    try:
        # Delete host
        api_response = api_instance.known_hosts_delete(host_name, port=port)
        print("The response of KnownHostsApi->known_hosts_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KnownHostsApi->known_hosts_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **host_name** | [**HostName1**](.md)| The hostname or IP address of the host to delete. | 
 **port** | **int**| The SSH port to use. | [optional] [default to 22]

### Return type

[**InlineResponse200276**](InlineResponse200276.md)

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

# **known_hosts_update**
> InlineResponse200277 known_hosts_update(host_name, port=port)

Update host in the known_hosts file

This function updates a host's entry in the cPanel account's /home/user/.ssh/known_hosts file.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200277 import InlineResponse200277
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
    api_instance = clientapi_cpanel.KnownHostsApi(api_client)
    host_name = clientapi_cpanel.HostName2() # HostName2 | The host to update.
    port = 22 # int | The SSH port to use. (optional) (default to 22)

    try:
        # Update host in the known_hosts file
        api_response = api_instance.known_hosts_update(host_name, port=port)
        print("The response of KnownHostsApi->known_hosts_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KnownHostsApi->known_hosts_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **host_name** | [**HostName2**](.md)| The host to update. | 
 **port** | **int**| The SSH port to use. | [optional] [default to 22]

### Return type

[**InlineResponse200277**](InlineResponse200277.md)

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

# **verify**
> InlineResponse200278 verify(host_name, port=port)

Validate host

This function checks whether a host's public key exists in the cPanel account's `/home/user/.ssh/known_hosts` file.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200278 import InlineResponse200278
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
    api_instance = clientapi_cpanel.KnownHostsApi(api_client)
    host_name = clientapi_cpanel.HostName3() # HostName3 | The host to query.
    port = 22 # int | The SSH port to use. (optional) (default to 22)

    try:
        # Validate host
        api_response = api_instance.verify(host_name, port=port)
        print("The response of KnownHostsApi->verify:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KnownHostsApi->verify: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **host_name** | [**HostName3**](.md)| The host to query. | 
 **port** | **int**| The SSH port to use. | [optional] [default to 22]

### Return type

[**InlineResponse200278**](InlineResponse200278.md)

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

