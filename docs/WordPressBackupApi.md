# clientapi_cpanel.WordPressBackupApi

All URIs are relative to *https://cpanel-server.tld:2083/execute*

Method | HTTP request | Description
------------- | ------------- | -------------
[**any_running**](WordPressBackupApi.md#any_running) | **GET** /WordPressBackup/any_running | Return all WordPress sites&#39; backup status
[**cancel**](WordPressBackupApi.md#cancel) | **GET** /WordPressBackup/cancel | Stop WordPress site backup
[**cleanup**](WordPressBackupApi.md#cleanup) | **GET** /WordPressBackup/cleanup | Delete WordPress backup temporary files
[**get_available_backups**](WordPressBackupApi.md#get_available_backups) | **GET** /WordPressBackup/get_available_backups | Return WordPress site backups
[**is_running**](WordPressBackupApi.md#is_running) | **GET** /WordPressBackup/is_running | Return WordPress site backup status
[**start**](WordPressBackupApi.md#start) | **GET** /WordPressBackup/start | Backup WordPress site


# **any_running**
> InlineResponse200556 any_running()

Return all WordPress sites' backup status

This function checks for any active WordPress® site backups on the cPanel account.

**Note:**

You **must** install the [WordPress Manager](https://go.cpanel.net/wordpressmanager) cPanel plugin to access this API function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200556 import InlineResponse200556
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
    api_instance = clientapi_cpanel.WordPressBackupApi(api_client)

    try:
        # Return all WordPress sites' backup status
        api_response = api_instance.any_running()
        print("The response of WordPressBackupApi->any_running:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WordPressBackupApi->any_running: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**InlineResponse200556**](InlineResponse200556.md)

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

# **cancel**
> InlineResponse200557 cancel(site)

Stop WordPress site backup

This function cancels a WordPress® site backup.

**Note:**

  You **must** install the [WordPress Manager](https://go.cpanel.net/wordpressmanager) cPanel plugin to access this API function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200557 import InlineResponse200557
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
    api_instance = clientapi_cpanel.WordPressBackupApi(api_client)
    site = clientapi_cpanel.Site() # Site | The WordPress site's URL without the protocol prefix.

    try:
        # Stop WordPress site backup
        api_response = api_instance.cancel(site)
        print("The response of WordPressBackupApi->cancel:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WordPressBackupApi->cancel: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site** | **Site**| The WordPress site&#39;s URL without the protocol prefix. | 

### Return type

[**InlineResponse200557**](InlineResponse200557.md)

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

# **cleanup**
> InlineResponse200558 cleanup(site)

Delete WordPress backup temporary files

This function releases any system resources from a previous WordPress® site backup.

**Note:**

You **must** install the [WordPress Manager](https://go.cpanel.net/wordpressmanager) cPanel plugin to access this API function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200558 import InlineResponse200558
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
    api_instance = clientapi_cpanel.WordPressBackupApi(api_client)
    site = 'example.com/wordpress' # str | The WordPress site's URL **without** the protocol prefix.

    try:
        # Delete WordPress backup temporary files
        api_response = api_instance.cleanup(site)
        print("The response of WordPressBackupApi->cleanup:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WordPressBackupApi->cleanup: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site** | **str**| The WordPress site&#39;s URL **without** the protocol prefix. | 

### Return type

[**InlineResponse200558**](InlineResponse200558.md)

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

# **get_available_backups**
> InlineResponse200559 get_available_backups(site)

Return WordPress site backups

This function retrieves a list of available WordPress® site backups of a single site.

**Note:**

You **must** install the [WordPress Manager](https://go.cpanel.net/wordpressmanager) cPanel plugin to access this API function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200559 import InlineResponse200559
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
    api_instance = clientapi_cpanel.WordPressBackupApi(api_client)
    site = 'example.com/wordpress' # str | The WordPress site's URL **without** the protocol prefix.

    try:
        # Return WordPress site backups
        api_response = api_instance.get_available_backups(site)
        print("The response of WordPressBackupApi->get_available_backups:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WordPressBackupApi->get_available_backups: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site** | **str**| The WordPress site&#39;s URL **without** the protocol prefix. | 

### Return type

[**InlineResponse200559**](InlineResponse200559.md)

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

# **is_running**
> InlineResponse200560 is_running(site)

Return WordPress site backup status

This function checks for an active WordPress® site backup.

**Note:**

You **must** install the [WordPress Manager](https://go.cpanel.net/wordpressmanager) cPanel plugin to access this API function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200560 import InlineResponse200560
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
    api_instance = clientapi_cpanel.WordPressBackupApi(api_client)
    site = 'example.com  example.com/wordpress' # str | The WordPress site's URL **without** `http://`.

    try:
        # Return WordPress site backup status
        api_response = api_instance.is_running(site)
        print("The response of WordPressBackupApi->is_running:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WordPressBackupApi->is_running: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site** | **str**| The WordPress site&#39;s URL **without** &#x60;http://&#x60;. | 

### Return type

[**InlineResponse200560**](InlineResponse200560.md)

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

# **start**
> InlineResponse200561 start(site)

Backup WordPress site

This function starts a single WordPress® site backup.

**Note:**

You **must** install the [WordPress Manager](https://go.cpanel.net/wordpressmanager) cPanel plugin to access this API function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200561 import InlineResponse200561
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
    api_instance = clientapi_cpanel.WordPressBackupApi(api_client)
    site = clientapi_cpanel.Site1() # Site1 | The WordPress site's URL without the protocol prefix.

    try:
        # Backup WordPress site
        api_response = api_instance.start(site)
        print("The response of WordPressBackupApi->start:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WordPressBackupApi->start: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site** | **Site1**| The WordPress site&#39;s URL without the protocol prefix. | 

### Return type

[**InlineResponse200561**](InlineResponse200561.md)

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

