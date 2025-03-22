# clientapi_cpanel.WordPressInstanceManagerApi

All URIs are relative to *https://cpanel-server.tld:2083/execute*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancel_scan**](WordPressInstanceManagerApi.md#cancel_scan) | **GET** /WordPressInstanceManager/cancel_scan | Stop WordPress site scan
[**change_admin_password**](WordPressInstanceManagerApi.md#change_admin_password) | **GET** /WordPressInstanceManager/change_admin_password | Update WordPress site admin password
[**cleanup_scan**](WordPressInstanceManagerApi.md#cleanup_scan) | **GET** /WordPressInstanceManager/cleanup_scan | Remove scan log after completed scan
[**configure_autoupdate**](WordPressInstanceManagerApi.md#configure_autoupdate) | **GET** /WordPressInstanceManager/configure_autoupdate | Update WordPress site automatic update settings
[**get_api_version**](WordPressInstanceManagerApi.md#get_api_version) | **GET** /WordPressInstanceManager/get_api_version | Return WordPress Manager plugin version
[**get_instance_by_id**](WordPressInstanceManagerApi.md#get_instance_by_id) | **GET** /WordPressInstanceManager/get_instance_by_id | Return WordPress site settings
[**get_instances**](WordPressInstanceManagerApi.md#get_instances) | **GET** /WordPressInstanceManager/get_instances | Return WordPress sites
[**get_latest_wordpress_version_from_wordpress_org**](WordPressInstanceManagerApi.md#get_latest_wordpress_version_from_wordpress_org) | **GET** /WordPressInstanceManager/get_latest_wordpress_version_from_wordpress_org | Return latest wordpress.org updates
[**get_scan_results**](WordPressInstanceManagerApi.md#get_scan_results) | **GET** /WordPressInstanceManager/get_scan_results | Return WordPress site scan results
[**is_installable_addon_available**](WordPressInstanceManagerApi.md#is_installable_addon_available) | **GET** /WordPressInstanceManager/is_installable_addon_available | Verify WordPress cPAddon availability
[**word_press_instance_manager_start_scan**](WordPressInstanceManagerApi.md#word_press_instance_manager_start_scan) | **GET** /WordPressInstanceManager/start_scan | Start WordPress sites scan


# **cancel_scan**
> InlineResponse200562 cancel_scan()

Stop WordPress site scan

This function cancels a scan that you start with the `WordPressInstanceManager::start_scan` function.

**Note:**

  You **must** install the [WordPress Manager](https://go.cpanel.net/wordpressmanager) cPanel plugin to access this API function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200562 import InlineResponse200562
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
    api_instance = clientapi_cpanel.WordPressInstanceManagerApi(api_client)

    try:
        # Stop WordPress site scan
        api_response = api_instance.cancel_scan()
        print("The response of WordPressInstanceManagerApi->cancel_scan:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WordPressInstanceManagerApi->cancel_scan: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**InlineResponse200562**](InlineResponse200562.md)

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

# **change_admin_password**
> InlineResponse200563 change_admin_password(id, password)

Update WordPress site admin password

This function updates a WordPress® cPAddon instance's administrator password.

**Note:**

  You **must** install the [WordPress Manager](https://go.cpanel.net/wordpressmanager) cPanel plugin to access this API function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200563 import InlineResponse200563
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
    api_instance = clientapi_cpanel.WordPressInstanceManagerApi(api_client)
    id = 'cPanel__Blogs__WordPressX.0.1491917088' # str | The cPAddon instance's unique ID.  **Note:**   You can retrieve an instance ID with the `get_instances` function.
    password = 'luggage12345' # str | The cPAddon instance's new administrator password.

    try:
        # Update WordPress site admin password
        api_response = api_instance.change_admin_password(id, password)
        print("The response of WordPressInstanceManagerApi->change_admin_password:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WordPressInstanceManagerApi->change_admin_password: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The cPAddon instance&#39;s unique ID.  **Note:**   You can retrieve an instance ID with the &#x60;get_instances&#x60; function. | 
 **password** | **str**| The cPAddon instance&#39;s new administrator password. | 

### Return type

[**InlineResponse200563**](InlineResponse200563.md)

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

# **cleanup_scan**
> InlineResponse200564 cleanup_scan(guid)

Remove scan log after completed scan

This function cleans up the scan log file after you complete a scan with the WordPressInstanceManager::start_scan function. To read more information about the complete scan process, read our UAPI Functions - WordPressInstanceManager::start_scan documentation.

**Note:**

  You **must** install the [WordPress Manager](https://go.cpanel.net/wordpressmanager) cPanel plugin to access this API function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200564 import InlineResponse200564
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
    api_instance = clientapi_cpanel.WordPressInstanceManagerApi(api_client)
    guid = 'B3A27B96-51F7-11E8-92E3-CC90C4F823F0' # str | The scan’s unique ID.

    try:
        # Remove scan log after completed scan
        api_response = api_instance.cleanup_scan(guid)
        print("The response of WordPressInstanceManagerApi->cleanup_scan:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WordPressInstanceManagerApi->cleanup_scan: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guid** | **str**| The scan’s unique ID. | 

### Return type

[**InlineResponse200564**](InlineResponse200564.md)

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

# **configure_autoupdate**
> InlineResponse200565 configure_autoupdate(autoupdate_core_major, autoupdate_core_minor, id)

Update WordPress site automatic update settings

This function configures a WordPress cPAddon instance's automatic updates settings. If you enable automatic updates for a legacy WordPress cPAddon instance, the function will convert it to use the RPM-based WordPress cPAddon.

**Important:**

  This function changes the instance's automatic update setting in the `wp-config.php` file. Before you run this function, you should verify that a filter does **not** exist for the automatic update settings. Use the `get_instance_by_id` function and view the `autoupdate.core.has_filter` return to determine if a filter exists.

**Note:**

  You **must** install the [WordPress Manager](https://go.cpanel.net/wordpressmanager) cPanel plugin to access this API function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200565 import InlineResponse200565
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
    api_instance = clientapi_cpanel.WordPressInstanceManagerApi(api_client)
    autoupdate_core_major = 0 # int | Whether to enable automatic updates for major releases. * `1` - Enable. * `0` - Disable.
    autoupdate_core_minor = 0 # int | Whether to enable automatic updates for minor releases. * `1` - Enable. * `0` - Disable.
    id = 'cPanel__Blogs__WordPressX.0.1491917088' # str | The cPAddon instance's unique ID.  **Note:**   You can retrieve an instance ID with the `get_instances` function.

    try:
        # Update WordPress site automatic update settings
        api_response = api_instance.configure_autoupdate(autoupdate_core_major, autoupdate_core_minor, id)
        print("The response of WordPressInstanceManagerApi->configure_autoupdate:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WordPressInstanceManagerApi->configure_autoupdate: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **autoupdate_core_major** | **int**| Whether to enable automatic updates for major releases. * &#x60;1&#x60; - Enable. * &#x60;0&#x60; - Disable. | 
 **autoupdate_core_minor** | **int**| Whether to enable automatic updates for minor releases. * &#x60;1&#x60; - Enable. * &#x60;0&#x60; - Disable. | 
 **id** | **str**| The cPAddon instance&#39;s unique ID.  **Note:**   You can retrieve an instance ID with the &#x60;get_instances&#x60; function. | 

### Return type

[**InlineResponse200565**](InlineResponse200565.md)

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

# **get_api_version**
> InlineResponse200566 get_api_version()

Return WordPress Manager plugin version

This function retrieves the WordPress Manager plugin's version.

**Note:**

  You **must** install the [WordPress Manager](https://go.cpanel.net/wordpressmanager) cPanel plugin to access this API function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200566 import InlineResponse200566
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
    api_instance = clientapi_cpanel.WordPressInstanceManagerApi(api_client)

    try:
        # Return WordPress Manager plugin version
        api_response = api_instance.get_api_version()
        print("The response of WordPressInstanceManagerApi->get_api_version:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WordPressInstanceManagerApi->get_api_version: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**InlineResponse200566**](InlineResponse200566.md)

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

# **get_instance_by_id**
> InlineResponse200567 get_instance_by_id(id)

Return WordPress site settings

This function retrieves a WordPress® instance's configuration.

**Note:**

* You **must** install the [WordPress Manager](https://go.cpanel.net/wordpressmanager) cPanel plugin to access this API function.
* This function retrieves some data that the system stored during the WordPress installation. That data may not reflect the most recent user changes.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200567 import InlineResponse200567
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
    api_instance = clientapi_cpanel.WordPressInstanceManagerApi(api_client)
    id = 'cPanel__Blogs__WordPressX.0.1528208546' # str | The WordPress instance's unique ID.  **Note:**   You can retrieve an instance ID with the `get_instances` function.

    try:
        # Return WordPress site settings
        api_response = api_instance.get_instance_by_id(id)
        print("The response of WordPressInstanceManagerApi->get_instance_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WordPressInstanceManagerApi->get_instance_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The WordPress instance&#39;s unique ID.  **Note:**   You can retrieve an instance ID with the &#x60;get_instances&#x60; function. | 

### Return type

[**InlineResponse200567**](InlineResponse200567.md)

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

# **get_instances**
> InlineResponse200568 get_instances()

Return WordPress sites

This function lists an account's WordPress® instances.

**Note:**

* You **must** install the [WordPress Manager](https://go.cpanel.net/wordpressmanager) cPanel plugin to access this API function.
* This function retrieves data that the system stored during the WordPress installation. That data may not reflect the most recent user changes.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200568 import InlineResponse200568
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
    api_instance = clientapi_cpanel.WordPressInstanceManagerApi(api_client)

    try:
        # Return WordPress sites
        api_response = api_instance.get_instances()
        print("The response of WordPressInstanceManagerApi->get_instances:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WordPressInstanceManagerApi->get_instances: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**InlineResponse200568**](InlineResponse200568.md)

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

# **get_latest_wordpress_version_from_wordpress_org**
> InlineResponse200569 get_latest_wordpress_version_from_wordpress_org(cache_time=cache_time, force=force)

Return latest wordpress.org updates

This function returns the available WordPress® updates from wordpress.org.

**Note:**

  You **must** install the [WordPress Manager](https://go.cpanel.net/wordpressmanager) cPanel plugin to access this API function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200569 import InlineResponse200569
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
    api_instance = clientapi_cpanel.WordPressInstanceManagerApi(api_client)
    cache_time = 86400 # int | The length of time in seconds to cache the database between requests to wordpress.org. (optional) (default to 86400)
    force = 0 # int | Whether to force a reload from the remote API. Otherwise, the function returns information stored in local cache. * `1` — Force reload * `0` — Read local cashe. (optional) (default to 0)

    try:
        # Return latest wordpress.org updates
        api_response = api_instance.get_latest_wordpress_version_from_wordpress_org(cache_time=cache_time, force=force)
        print("The response of WordPressInstanceManagerApi->get_latest_wordpress_version_from_wordpress_org:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WordPressInstanceManagerApi->get_latest_wordpress_version_from_wordpress_org: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cache_time** | **int**| The length of time in seconds to cache the database between requests to wordpress.org. | [optional] [default to 86400]
 **force** | **int**| Whether to force a reload from the remote API. Otherwise, the function returns information stored in local cache. * &#x60;1&#x60; — Force reload * &#x60;0&#x60; — Read local cashe. | [optional] [default to 0]

### Return type

[**InlineResponse200569**](InlineResponse200569.md)

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

# **get_scan_results**
> InlineResponse200570 get_scan_results()

Return WordPress site scan results

This function checks the status of a completed scan and reports the results. To find more information about the scan process, read our UAPI documentation for `WordPressInstanceManager::start_scan`.

**Note:**

  You **must** install the [WordPress Manager](https://go.cpanel.net/wordpressmanager) cPanel plugin to access this API function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200570 import InlineResponse200570
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
    api_instance = clientapi_cpanel.WordPressInstanceManagerApi(api_client)

    try:
        # Return WordPress site scan results
        api_response = api_instance.get_scan_results()
        print("The response of WordPressInstanceManagerApi->get_scan_results:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WordPressInstanceManagerApi->get_scan_results: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**InlineResponse200570**](InlineResponse200570.md)

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

# **is_installable_addon_available**
> InlineResponse200571 is_installable_addon_available()

Verify WordPress cPAddon availability

This function verifies that the RPM-based WordPress® cPAddon exists on the system.

**Note:**

  You must install the WordPress Manager cPanel plugin to access this API function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200571 import InlineResponse200571
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
    api_instance = clientapi_cpanel.WordPressInstanceManagerApi(api_client)

    try:
        # Verify WordPress cPAddon availability
        api_response = api_instance.is_installable_addon_available()
        print("The response of WordPressInstanceManagerApi->is_installable_addon_available:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WordPressInstanceManagerApi->is_installable_addon_available: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**InlineResponse200571**](InlineResponse200571.md)

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

# **word_press_instance_manager_start_scan**
> InlineResponse200572 word_press_instance_manager_start_scan()

Start WordPress sites scan

This function scans for WordPress® instances installed on a cPanel account. The system will populate cPanel's WordPress Manager interface with any newly discovered instances.

**Note:**

You **must** install the [WordPress Manager](https://go.cpanel.net/wordpressmanager) cPanel plugin to access this API function.

### Server Sent Events (SSE)

This function uses the following SSE events:

* `register` — The scan operation discovered a WordPress instance and registered it. The data is a
JSON-encoded object containing the attributes of the instance, with the same format used in the
UAPI `get_instances` and UAPI `get_instance_by_id` functions.
* `found` — The scan operation found a WordPress instance. If the WordPress instance is newly
discovered, the system will also generate a `register` event for the instance. The data is a
JSON-encoded object containing the following:
  * `path` — The absolute file path to the instance.
* `done` — The scan is finished. The data is a JSON-encoded object that contains:
  * `found` — An array of strings that represents the absolute path to the discovered instances and
  any instances that the system already registered.
  * `converted` — An array of converted instances that the system returns in the same format
  provided in the UAPI `get_instances` and UAPI `get_instance_by_id` functions.
* `terminated` — The system or user terminated the scan.	
* `timedout` — The scan timed out before it completed.
* `register-failed` — The system failed to build the instance registry.	The data is a JSON-encoded
string that contains the error message.
* `register-load-failed` — The system could not load the registry after building the instance
registry. The data is a JSON-encoded string that contains the error message.

For more information about server sent events, read Mozilla's [Using server-sent events](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events/Using_server-sent_events) documentation.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200572 import InlineResponse200572
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
    api_instance = clientapi_cpanel.WordPressInstanceManagerApi(api_client)

    try:
        # Start WordPress sites scan
        api_response = api_instance.word_press_instance_manager_start_scan()
        print("The response of WordPressInstanceManagerApi->word_press_instance_manager_start_scan:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WordPressInstanceManagerApi->word_press_instance_manager_start_scan: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**InlineResponse200572**](InlineResponse200572.md)

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

