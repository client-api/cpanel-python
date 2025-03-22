# clientapi_cpanel.ServiceProxyApi

All URIs are relative to *https://cpanel-server.tld:2083/execute*

Method | HTTP request | Description
------------- | ------------- | -------------
[**serviceproxy_get_service_proxy_backends**](ServiceProxyApi.md#serviceproxy_get_service_proxy_backends) | **GET** /ServiceProxy/get_service_proxy_backends | Return a cPanel account’s service proxying setup
[**serviceproxy_set_service_proxy_backends**](ServiceProxyApi.md#serviceproxy_set_service_proxy_backends) | **GET** /ServiceProxy/set_service_proxy_backends | Add cPanel account service proxying
[**serviceproxy_unset_all_service_proxy_backends**](ServiceProxyApi.md#serviceproxy_unset_all_service_proxy_backends) | **GET** /ServiceProxy/unset_all_service_proxy_backends | Remove cPanel account service proxying


# **serviceproxy_get_service_proxy_backends**
> InlineResponse200452 serviceproxy_get_service_proxy_backends()

Return a cPanel account’s service proxying setup

This function reports a cPanel account's
[service proxying](https://go.cpanel.net/ServiceProxying)
configuration.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200452 import InlineResponse200452
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
    api_instance = clientapi_cpanel.ServiceProxyApi(api_client)

    try:
        # Return a cPanel account’s service proxying setup
        api_response = api_instance.serviceproxy_get_service_proxy_backends()
        print("The response of ServiceProxyApi->serviceproxy_get_service_proxy_backends:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServiceProxyApi->serviceproxy_get_service_proxy_backends: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**InlineResponse200452**](InlineResponse200452.md)

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

# **serviceproxy_set_service_proxy_backends**
> InlineResponse200453 serviceproxy_set_service_proxy_backends(general=general, service_group=service_group, service_group_backend=service_group_backend)

Add cPanel account service proxying

This function lets you configure a cPanel account's
[service proxying](https://go.cpanel.net/ServiceProxying).

**Note:**

* If the [Web Server](https://go.cpanel.net/howtouseserverprofiles#roles) role is active
on the server, this function rebuilds the user's web virtual hosts (vhosts) and restarts
the web server.
* If the system cannot rebuild the user's vhosts, the API call will still succeed. However,
the function returns a failure warning in the metadata.
* To remove an account's service proxying, use the UAPI `unset_all_service_proxy_backends`
function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200453 import InlineResponse200453
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
    api_instance = clientapi_cpanel.ServiceProxyApi(api_client)
    general = clientapi_cpanel.General() # General | The hostname or IP address to assign as the server that handles the account's service proxy requests.  This parameter defaults to the existing service proxy configuration, if one exists. (optional)
    service_group = 'Mail&service-group-1=Mail&service-group-2=Mail' # str | The name of a service group for which to assign a proxy backend. The corresponding `service_group_backend` value will be the service group's new proxy backend.  * `Mail` — The [Mail service group](https://go.cpanel.net/ServiceProxying#Mail).  This parameter defaults to the existing setting, if one exists.  **Note:**   * When you call this parameter, you **must** include a corresponding  `service_group_backend` value.  * To add multiple `service_group` values, increment the parameter name. For example,  `service_group`, `service_group-1`, and `service_group-2`. (optional)
    service_group_backend = clientapi_cpanel.ServiceGroupBackend() # ServiceGroupBackend | The hostname or IP address of the server to assign as the corresponding `service_group` value's proxy backend server.  This parameter defaults to the existing setting, if one exists.  **Note:**   * When you call this parameter, you **must** include a corresponding `service_group`  value.  * To add multiple `service_group_backend` values, increment the parameter name.  For example, `service_group_backend`, `service_group_backend-1`,  and `service_group_backend-2`. (optional)

    try:
        # Add cPanel account service proxying
        api_response = api_instance.serviceproxy_set_service_proxy_backends(general=general, service_group=service_group, service_group_backend=service_group_backend)
        print("The response of ServiceProxyApi->serviceproxy_set_service_proxy_backends:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServiceProxyApi->serviceproxy_set_service_proxy_backends: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **general** | [**General**](.md)| The hostname or IP address to assign as the server that handles the account&#39;s service proxy requests.  This parameter defaults to the existing service proxy configuration, if one exists. | [optional] 
 **service_group** | **str**| The name of a service group for which to assign a proxy backend. The corresponding &#x60;service_group_backend&#x60; value will be the service group&#39;s new proxy backend.  * &#x60;Mail&#x60; — The [Mail service group](https://go.cpanel.net/ServiceProxying#Mail).  This parameter defaults to the existing setting, if one exists.  **Note:**   * When you call this parameter, you **must** include a corresponding  &#x60;service_group_backend&#x60; value.  * To add multiple &#x60;service_group&#x60; values, increment the parameter name. For example,  &#x60;service_group&#x60;, &#x60;service_group-1&#x60;, and &#x60;service_group-2&#x60;. | [optional] 
 **service_group_backend** | [**ServiceGroupBackend**](.md)| The hostname or IP address of the server to assign as the corresponding &#x60;service_group&#x60; value&#39;s proxy backend server.  This parameter defaults to the existing setting, if one exists.  **Note:**   * When you call this parameter, you **must** include a corresponding &#x60;service_group&#x60;  value.  * To add multiple &#x60;service_group_backend&#x60; values, increment the parameter name.  For example, &#x60;service_group_backend&#x60;, &#x60;service_group_backend-1&#x60;,  and &#x60;service_group_backend-2&#x60;. | [optional] 

### Return type

[**InlineResponse200453**](InlineResponse200453.md)

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

# **serviceproxy_unset_all_service_proxy_backends**
> InlineResponse200454 serviceproxy_unset_all_service_proxy_backends()

Remove cPanel account service proxying

This function removes a cPanel account's
[service proxying](https://go.cpanel.net/ServiceProxying).

**Note:**

* If the [Web Server](https://go.cpanel.net/howtouseserverprofiles#roles) role is active on
the server, this function rebuilds the cPanel user's web virtual hosts (vhosts) and restarts
the web server.
* If the system **cannot** rebuild the cPanel user's vhosts, the API call will still succeed.
However, the function returns a failure warning in the metadata.
* To set a service proxying for a cPanel account, use the UAPI
`set_service_proxy_backends` function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200454 import InlineResponse200454
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
    api_instance = clientapi_cpanel.ServiceProxyApi(api_client)

    try:
        # Remove cPanel account service proxying
        api_response = api_instance.serviceproxy_unset_all_service_proxy_backends()
        print("The response of ServiceProxyApi->serviceproxy_unset_all_service_proxy_backends:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServiceProxyApi->serviceproxy_unset_all_service_proxy_backends: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**InlineResponse200454**](InlineResponse200454.md)

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

