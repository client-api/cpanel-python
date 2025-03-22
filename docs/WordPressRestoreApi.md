# clientapi_cpanel.WordPressRestoreApi

All URIs are relative to *https://cpanel-server.tld:2083/execute*

Method | HTTP request | Description
------------- | ------------- | -------------
[**word_press_restore_any_running**](WordPressRestoreApi.md#word_press_restore_any_running) | **GET** /WordPressRestore/any_running | Return WordPress site restore status
[**word_press_restore_cleanup**](WordPressRestoreApi.md#word_press_restore_cleanup) | **GET** /WordPressRestore/cleanup | Delete restored WordPress site&#39;s temporary files
[**word_press_restore_start**](WordPressRestoreApi.md#word_press_restore_start) | **GET** /WordPressRestore/start | Restore WordPress site


# **word_press_restore_any_running**
> InlineResponse200573 word_press_restore_any_running()

Return WordPress site restore status

This function returns whether a WordPress® site backup restoration is in progress.

**Note:**

* You **must** install the [WordPress Manager](https://go.cpanel.net/wordpressmanager) cPanel plugin to access this API function.
* The output of this function changes, depending on the state of the backup restoration.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200573 import InlineResponse200573
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
    api_instance = clientapi_cpanel.WordPressRestoreApi(api_client)

    try:
        # Return WordPress site restore status
        api_response = api_instance.word_press_restore_any_running()
        print("The response of WordPressRestoreApi->word_press_restore_any_running:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WordPressRestoreApi->word_press_restore_any_running: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**InlineResponse200573**](InlineResponse200573.md)

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

# **word_press_restore_cleanup**
> InlineResponse200574 word_press_restore_cleanup(site)

Delete restored WordPress site's temporary files

This function cleans up any temporary system resources after a WordPress® site backup restoration.

**Note:**

You **must** install the [WordPress Manager](https://go.cpanel.net/wordpressmanager) cPanel plugin to access this API function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200574 import InlineResponse200574
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
    api_instance = clientapi_cpanel.WordPressRestoreApi(api_client)
    site = 'example.com' # str | The WordPress site's URL **without** the protocol prefix.

    try:
        # Delete restored WordPress site's temporary files
        api_response = api_instance.word_press_restore_cleanup(site)
        print("The response of WordPressRestoreApi->word_press_restore_cleanup:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WordPressRestoreApi->word_press_restore_cleanup: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site** | **str**| The WordPress site&#39;s URL **without** the protocol prefix. | 

### Return type

[**InlineResponse200574**](InlineResponse200574.md)

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

# **word_press_restore_start**
> InlineResponse200575 word_press_restore_start(backup_path, site)

Restore WordPress site

This function starts a single WordPress® site backup restoration.

**Note:**

You **must** install the [WordPress Manager](https://go.cpanel.net/wordpressmanager) cPanel plugin to access this API function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200575 import InlineResponse200575
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
    api_instance = clientapi_cpanel.WordPressRestoreApi(api_client)
    backup_path = '/home/example/wordpress-backups/example.com__2018-11-13T11:11:31-0600.tar.gz' # str | The file path to the backup archive.
    site = 'example.com' # str | The WordPress site's URL to restore.

    try:
        # Restore WordPress site
        api_response = api_instance.word_press_restore_start(backup_path, site)
        print("The response of WordPressRestoreApi->word_press_restore_start:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WordPressRestoreApi->word_press_restore_start: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **backup_path** | **str**| The file path to the backup archive. | 
 **site** | **str**| The WordPress site&#39;s URL to restore. | 

### Return type

[**InlineResponse200575**](InlineResponse200575.md)

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

