# clientapi_cpanel.SpamFilteringGreylistingApi

All URIs are relative to *https://cpanel-server.tld:2083/execute*

Method | HTTP request | Description
------------- | ------------- | -------------
[**c_p_grey_list_disable_all_domains**](SpamFilteringGreylistingApi.md#c_p_grey_list_disable_all_domains) | **GET** /cPGreyList/disable_all_domains | Disable Greylisting for all domains
[**c_p_grey_list_disable_domains**](SpamFilteringGreylistingApi.md#c_p_grey_list_disable_domains) | **GET** /cPGreyList/disable_domains | Disable Greylisting for specified domains
[**c_p_grey_list_enable_all_domains**](SpamFilteringGreylistingApi.md#c_p_grey_list_enable_all_domains) | **GET** /cPGreyList/enable_all_domains | Enable Greylisting for all domains
[**c_p_grey_list_enable_domains**](SpamFilteringGreylistingApi.md#c_p_grey_list_enable_domains) | **GET** /cPGreyList/enable_domains | Enable Greylisting for specified domains
[**c_p_grey_list_list_domains**](SpamFilteringGreylistingApi.md#c_p_grey_list_list_domains) | **GET** /cPGreyList/list_domains | Return Greylisting status for domains
[**has_greylisting_enabled**](SpamFilteringGreylistingApi.md#has_greylisting_enabled) | **GET** /cPGreyList/has_greylisting_enabled | Return whether Greylisting is enabled


# **c_p_grey_list_disable_all_domains**
> InlineResponse200581 c_p_grey_list_disable_all_domains()

Disable Greylisting for all domains

This function disables Greylisting on a cPanel account's domains.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200581 import InlineResponse200581
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
    api_instance = clientapi_cpanel.SpamFilteringGreylistingApi(api_client)

    try:
        # Disable Greylisting for all domains
        api_response = api_instance.c_p_grey_list_disable_all_domains()
        print("The response of SpamFilteringGreylistingApi->c_p_grey_list_disable_all_domains:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SpamFilteringGreylistingApi->c_p_grey_list_disable_all_domains: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**InlineResponse200581**](InlineResponse200581.md)

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

# **c_p_grey_list_disable_domains**
> InlineResponse200582 c_p_grey_list_disable_domains(domains)

Disable Greylisting for specified domains

This function disables Greylisting on a cPanel account's selected domains.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200582 import InlineResponse200582
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
    api_instance = clientapi_cpanel.SpamFilteringGreylistingApi(api_client)
    domains = 'domain=example.com domain=example1.com domain=example2.com' # str | The domain on which to disable Greylisting.  **Note:**  To disable Greylisting on multiple domains, use the `domains` parameter multiple times.

    try:
        # Disable Greylisting for specified domains
        api_response = api_instance.c_p_grey_list_disable_domains(domains)
        print("The response of SpamFilteringGreylistingApi->c_p_grey_list_disable_domains:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SpamFilteringGreylistingApi->c_p_grey_list_disable_domains: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domains** | **str**| The domain on which to disable Greylisting.  **Note:**  To disable Greylisting on multiple domains, use the &#x60;domains&#x60; parameter multiple times. | 

### Return type

[**InlineResponse200582**](InlineResponse200582.md)

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

# **c_p_grey_list_enable_all_domains**
> InlineResponse200583 c_p_grey_list_enable_all_domains()

Enable Greylisting for all domains

This function enables Greylisting on all of the cPanel account's domains.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200583 import InlineResponse200583
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
    api_instance = clientapi_cpanel.SpamFilteringGreylistingApi(api_client)

    try:
        # Enable Greylisting for all domains
        api_response = api_instance.c_p_grey_list_enable_all_domains()
        print("The response of SpamFilteringGreylistingApi->c_p_grey_list_enable_all_domains:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SpamFilteringGreylistingApi->c_p_grey_list_enable_all_domains: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**InlineResponse200583**](InlineResponse200583.md)

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

# **c_p_grey_list_enable_domains**
> InlineResponse200584 c_p_grey_list_enable_domains(domains)

Enable Greylisting for specified domains

This function enables Greylisting on a cPanel account's selected domains.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200584 import InlineResponse200584
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
    api_instance = clientapi_cpanel.SpamFilteringGreylistingApi(api_client)
    domains = 'domain=example.com&domain=example1.com&domain=example2.com' # str | The domain on which to enable Greylisting.  **Note:**   To enable Greylisting on multiple domains, use the `domains` parameter multiple times.

    try:
        # Enable Greylisting for specified domains
        api_response = api_instance.c_p_grey_list_enable_domains(domains)
        print("The response of SpamFilteringGreylistingApi->c_p_grey_list_enable_domains:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SpamFilteringGreylistingApi->c_p_grey_list_enable_domains: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domains** | **str**| The domain on which to enable Greylisting.  **Note:**   To enable Greylisting on multiple domains, use the &#x60;domains&#x60; parameter multiple times. | 

### Return type

[**InlineResponse200584**](InlineResponse200584.md)

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

# **c_p_grey_list_list_domains**
> InlineResponse200586 c_p_grey_list_list_domains()

Return Greylisting status for domains

This function returns Greylisting's status for a cPanel account's domains.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200586 import InlineResponse200586
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
    api_instance = clientapi_cpanel.SpamFilteringGreylistingApi(api_client)

    try:
        # Return Greylisting status for domains
        api_response = api_instance.c_p_grey_list_list_domains()
        print("The response of SpamFilteringGreylistingApi->c_p_grey_list_list_domains:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SpamFilteringGreylistingApi->c_p_grey_list_list_domains: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**InlineResponse200586**](InlineResponse200586.md)

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

# **has_greylisting_enabled**
> InlineResponse200585 has_greylisting_enabled()

Return whether Greylisting is enabled

This function checks whether Greylisting is enabled for the cPanel account.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200585 import InlineResponse200585
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
    api_instance = clientapi_cpanel.SpamFilteringGreylistingApi(api_client)

    try:
        # Return whether Greylisting is enabled
        api_response = api_instance.has_greylisting_enabled()
        print("The response of SpamFilteringGreylistingApi->has_greylisting_enabled:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SpamFilteringGreylistingApi->has_greylisting_enabled: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**InlineResponse200585**](InlineResponse200585.md)

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

