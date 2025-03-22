# clientapi_cpanel.ModSecurityApi

All URIs are relative to *https://cpanel-server.tld:2083/execute*

Method | HTTP request | Description
------------- | ------------- | -------------
[**disable_all_domains**](ModSecurityApi.md#disable_all_domains) | **GET** /ModSecurity/disable_all_domains | Disable ModSecurity for all domains
[**disable_domains**](ModSecurityApi.md#disable_domains) | **GET** /ModSecurity/disable_domains | Disable ModSecurity for selected domains
[**enable_all_domains**](ModSecurityApi.md#enable_all_domains) | **GET** /ModSecurity/enable_all_domains | Enable ModSecurity for all domains
[**enable_domains**](ModSecurityApi.md#enable_domains) | **GET** /ModSecurity/enable_domains | Enable ModSecurity for selected domains
[**has_modsecurity_installed**](ModSecurityApi.md#has_modsecurity_installed) | **GET** /ModSecurity/has_modsecurity_installed | Return ModSecurity installation status
[**mod_security_list_domains**](ModSecurityApi.md#mod_security_list_domains) | **GET** /ModSecurity/list_domains | Return ModSecurity domains&#39; status


# **disable_all_domains**
> InlineResponse200330 disable_all_domains()

Disable ModSecurity for all domains

This function disables ModSecurity™ on a cPanel account's domains.

**Important:**

When you disable the [WebServer role](https://go.cpanel.net/serverroles#roles), the system **disables** this function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200330 import InlineResponse200330
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
    api_instance = clientapi_cpanel.ModSecurityApi(api_client)

    try:
        # Disable ModSecurity for all domains
        api_response = api_instance.disable_all_domains()
        print("The response of ModSecurityApi->disable_all_domains:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ModSecurityApi->disable_all_domains: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**InlineResponse200330**](InlineResponse200330.md)

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

# **disable_domains**
> InlineResponse200331 disable_domains(domains)

Disable ModSecurity for selected domains

This function disables ModSecurity™ on specified domains.

**Important:**

When you disable the [WebServer role](https://go.cpanel.net/serverroles#roles), the system **disables** this function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200331 import InlineResponse200331
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
    api_instance = clientapi_cpanel.ModSecurityApi(api_client)
    domains = 'example.com,dallas.example.com,galveston.example.com' # str | A comma-separated list of domains that the cPanel account owns.  **Important:**  The authenticated cPanel account **must** own these domains.

    try:
        # Disable ModSecurity for selected domains
        api_response = api_instance.disable_domains(domains)
        print("The response of ModSecurityApi->disable_domains:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ModSecurityApi->disable_domains: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domains** | **str**| A comma-separated list of domains that the cPanel account owns.  **Important:**  The authenticated cPanel account **must** own these domains. | 

### Return type

[**InlineResponse200331**](InlineResponse200331.md)

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

# **enable_all_domains**
> InlineResponse200332 enable_all_domains()

Enable ModSecurity for all domains

This function enables ModSecurity™ on a cPanel account's domains.

**Important:**

When you disable the [WebServer role](https://go.cpanel.net/serverroles#roles), the system **disables** this function

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200332 import InlineResponse200332
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
    api_instance = clientapi_cpanel.ModSecurityApi(api_client)

    try:
        # Enable ModSecurity for all domains
        api_response = api_instance.enable_all_domains()
        print("The response of ModSecurityApi->enable_all_domains:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ModSecurityApi->enable_all_domains: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**InlineResponse200332**](InlineResponse200332.md)

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

# **enable_domains**
> InlineResponse200333 enable_domains(domains)

Enable ModSecurity for selected domains

This function enables ModSecurity™ for specified domains.

**Important:**

When you disable the [WebServer role](https://go.cpanel.net/serverroles#roles), the system **disables** this function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200333 import InlineResponse200333
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
    api_instance = clientapi_cpanel.ModSecurityApi(api_client)
    domains = 'example.com,dallas.example.com,galveston.example.com' # str | A comma-separated list of domains for which to enable ModSecurity.  **Important:**  The authenticated cPanel account **must** own these domains.

    try:
        # Enable ModSecurity for selected domains
        api_response = api_instance.enable_domains(domains)
        print("The response of ModSecurityApi->enable_domains:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ModSecurityApi->enable_domains: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domains** | **str**| A comma-separated list of domains for which to enable ModSecurity.  **Important:**  The authenticated cPanel account **must** own these domains. | 

### Return type

[**InlineResponse200333**](InlineResponse200333.md)

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

# **has_modsecurity_installed**
> InlineResponse200334 has_modsecurity_installed()

Return ModSecurity installation status

This function checks whether ModSecurity™ is installed on a server.

**Important:**

When you disable the [Web Server role](https://go.cpanel.net/serverroles#roles), the system **disables** this function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200334 import InlineResponse200334
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
    api_instance = clientapi_cpanel.ModSecurityApi(api_client)

    try:
        # Return ModSecurity installation status
        api_response = api_instance.has_modsecurity_installed()
        print("The response of ModSecurityApi->has_modsecurity_installed:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ModSecurityApi->has_modsecurity_installed: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**InlineResponse200334**](InlineResponse200334.md)

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

# **mod_security_list_domains**
> InlineResponse200335 mod_security_list_domains()

Return ModSecurity domains' status

This function returns ModSecurity's™ status for a cPanel account's domains.

**Important:**

When you disable the [WebServer role](https://go.cpanel.net/serverroles#roles), the system **disables** this function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200335 import InlineResponse200335
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
    api_instance = clientapi_cpanel.ModSecurityApi(api_client)

    try:
        # Return ModSecurity domains' status
        api_response = api_instance.mod_security_list_domains()
        print("The response of ModSecurityApi->mod_security_list_domains:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ModSecurityApi->mod_security_list_domains: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**InlineResponse200335**](InlineResponse200335.md)

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

