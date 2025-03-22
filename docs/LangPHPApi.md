# clientapi_cpanel.LangPHPApi

All URIs are relative to *https://cpanel-server.tld:2083/execute*

Method | HTTP request | Description
------------- | ------------- | -------------
[**php_get_domain_handler**](LangPHPApi.md#php_get_domain_handler) | **GET** /LangPHP/php_get_domain_handler | Return PHP version&#39;s handler
[**php_get_impacted_domains**](LangPHPApi.md#php_get_impacted_domains) | **GET** /LangPHP/php_get_impacted_domains | Return domains that shared PHP configuration
[**php_get_installed_versions**](LangPHPApi.md#php_get_installed_versions) | **GET** /LangPHP/php_get_installed_versions | Return installed PHP versions
[**php_get_system_default_version**](LangPHPApi.md#php_get_system_default_version) | **GET** /LangPHP/php_get_system_default_version | Return default PHP version
[**php_get_vhost_versions**](LangPHPApi.md#php_get_vhost_versions) | **GET** /LangPHP/php_get_vhost_versions | Return virtual host&#39;s PHP version
[**php_ini_get_user_basic_directives**](LangPHPApi.md#php_ini_get_user_basic_directives) | **GET** /LangPHP/php_ini_get_user_basic_directives | Return basic PHP directives
[**php_ini_get_user_content**](LangPHPApi.md#php_ini_get_user_content) | **GET** /LangPHP/php_ini_get_user_content | Return virtual host&#39;s php.ini content
[**php_ini_get_user_paths**](LangPHPApi.md#php_ini_get_user_paths) | **GET** /LangPHP/php_ini_get_user_paths | Return php.ini file paths
[**php_ini_set_user_basic_directives**](LangPHPApi.md#php_ini_set_user_basic_directives) | **GET** /LangPHP/php_ini_set_user_basic_directives | Update basic PHP directives
[**php_ini_set_user_content**](LangPHPApi.md#php_ini_set_user_content) | **GET** /LangPHP/php_ini_set_user_content | Update virtual host&#39;s php.ini content
[**php_set_vhost_versions**](LangPHPApi.md#php_set_vhost_versions) | **GET** /LangPHP/php_set_vhost_versions | Update virtual host&#39;s PHP version


# **php_get_domain_handler**
> InlineResponse200279 php_get_domain_handler(type, vhost=vhost)

Return PHP version's handler

This function returns a PHP version's assigned PHP handler.

**Note:**

  This document **only** applies to systems that run EasyApache 4.

**Important:**

  When you disable the [WebServer role](https://go.cpanel.net/howtouseserverprofiles#roles), the system disables this function. For more information, read our How to Use Server Profiles documentation.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200279 import InlineResponse200279
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
    api_instance = clientapi_cpanel.LangPHPApi(api_client)
    type = 'vhost' # str | The type of `php.ini` file.  * `home` * `vhost`  **Important:**   * If you set this parameter to `vhost`, you **must** also include the vhost parameter.  * If you set this parameter to `home`, the system returns the system default PHP handler.
    vhost = 'clearly.com' # str | The name of a virtual host.  **Important:**   If the `type` value is `vhost`, you **must** use this parameter. (optional)

    try:
        # Return PHP version's handler
        api_response = api_instance.php_get_domain_handler(type, vhost=vhost)
        print("The response of LangPHPApi->php_get_domain_handler:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LangPHPApi->php_get_domain_handler: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| The type of &#x60;php.ini&#x60; file.  * &#x60;home&#x60; * &#x60;vhost&#x60;  **Important:**   * If you set this parameter to &#x60;vhost&#x60;, you **must** also include the vhost parameter.  * If you set this parameter to &#x60;home&#x60;, the system returns the system default PHP handler. | 
 **vhost** | **str**| The name of a virtual host.  **Important:**   If the &#x60;type&#x60; value is &#x60;vhost&#x60;, you **must** use this parameter. | [optional] 

### Return type

[**InlineResponse200279**](InlineResponse200279.md)

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

# **php_get_impacted_domains**
> InlineResponse200280 php_get_impacted_domains(domain=domain, system_default=system_default)

Return domains that shared PHP configuration

This function lists domains that obtain their PHP version from a specified PHP configuration.

**Note:**

  This document **only** applies to systems that run EasyApache 4.

**Important:**

  When you disable the [WebServer role](https://go.cpanel.net/howtouseserverprofiles#roles), the system **disables** this function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200280 import InlineResponse200280
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
    api_instance = clientapi_cpanel.LangPHPApi(api_client)
    domain = 'example.com' # str | A domain on the system.  **Note:**   * You must pass either the `system_default` or `domain` parameters, or both.  * You can pass this parameter multiple times.  * You **cannot** pass the name of a parked domain. (optional)
    system_default = 1 # int | Whether to return domains that inherit the system's default PHP version.  * `1` - Return domains that inherit the system's default PHP version. * `0` - Do **not** return domains that inherit the system's default PHP version.  **Note:**  If you pass this parameter with a false value and do **not** also pass the domain parameter, the function returns an error. (optional)

    try:
        # Return domains that shared PHP configuration
        api_response = api_instance.php_get_impacted_domains(domain=domain, system_default=system_default)
        print("The response of LangPHPApi->php_get_impacted_domains:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LangPHPApi->php_get_impacted_domains: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**| A domain on the system.  **Note:**   * You must pass either the &#x60;system_default&#x60; or &#x60;domain&#x60; parameters, or both.  * You can pass this parameter multiple times.  * You **cannot** pass the name of a parked domain. | [optional] 
 **system_default** | **int**| Whether to return domains that inherit the system&#39;s default PHP version.  * &#x60;1&#x60; - Return domains that inherit the system&#39;s default PHP version. * &#x60;0&#x60; - Do **not** return domains that inherit the system&#39;s default PHP version.  **Note:**  If you pass this parameter with a false value and do **not** also pass the domain parameter, the function returns an error. | [optional] 

### Return type

[**InlineResponse200280**](InlineResponse200280.md)

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

# **php_get_installed_versions**
> InlineResponse200281 php_get_installed_versions()

Return installed PHP versions

This function lists the system's PHP versions.

**Note:**

  This document **only** applies to systems that run EasyApache 4.

**Important:**

  When you disable the [WebServer role](https://go.cpanel.net/howtouseserverprofiles#roles), the system **disables** this function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200281 import InlineResponse200281
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
    api_instance = clientapi_cpanel.LangPHPApi(api_client)

    try:
        # Return installed PHP versions
        api_response = api_instance.php_get_installed_versions()
        print("The response of LangPHPApi->php_get_installed_versions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LangPHPApi->php_get_installed_versions: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**InlineResponse200281**](InlineResponse200281.md)

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

# **php_get_system_default_version**
> InlineResponse200282 php_get_system_default_version()

Return default PHP version

This function lists the system’s default PHP version.

**Important**:

  When you disable the [Web Server role](https://go.cpanel.net/serverroles), the system **disables** this function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200282 import InlineResponse200282
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
    api_instance = clientapi_cpanel.LangPHPApi(api_client)

    try:
        # Return default PHP version
        api_response = api_instance.php_get_system_default_version()
        print("The response of LangPHPApi->php_get_system_default_version:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LangPHPApi->php_get_system_default_version: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**InlineResponse200282**](InlineResponse200282.md)

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

# **php_get_vhost_versions**
> InlineResponse200283 php_get_vhost_versions(vhost=vhost)

Return virtual host's PHP version

This function returns the PHP version of every virtual host that a reseller controls.

You can get the version of a single virtual host by providing an optional `vhost` name.

**Note:**

  This document **only** applies to systems that run EasyApache 4.

**Important:**

  When you disable the [Web Server role](https://go.cpanel.net/howtouseserverprofiles#roles), the system **disables** this function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200283 import InlineResponse200283
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
    api_instance = clientapi_cpanel.LangPHPApi(api_client)
    vhost = 'your-domain.test' # str | The PHP Virtual Hostname. (optional)

    try:
        # Return virtual host's PHP version
        api_response = api_instance.php_get_vhost_versions(vhost=vhost)
        print("The response of LangPHPApi->php_get_vhost_versions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LangPHPApi->php_get_vhost_versions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vhost** | **str**| The PHP Virtual Hostname. | [optional] 

### Return type

[**InlineResponse200283**](InlineResponse200283.md)

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

# **php_ini_get_user_basic_directives**
> InlineResponse200284 php_ini_get_user_basic_directives(type, vhost=vhost)

Return basic PHP directives

This function lists a virtual host's basic PHP directives. The Basic Mode section of cPanel's [MultiPHP INI Editor](https://go.cpanel.net/cPanelMultiPHPINI)  interface (Home >> Software >> MultiPHP INI Editor) also lists these directives.

**Note:**

  This document **only** applies to systems that run EasyApache 4 with MultiPHP enabled.

**Important:**

  When you disable the [WebServer role](https://go.cpanel.net/howtouseserverprofiles#roles), the system **disables** this function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200284 import InlineResponse200284
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
    api_instance = clientapi_cpanel.LangPHPApi(api_client)
    type = 'vhost' # str | The type of `php.ini` file.  - `home` - `vhost`  **Important:**   If you set this parameter to `vhost`, you **must** also include the `vhost` parameter.
    vhost = 'clearly.com' # str | The name of a virtual host.  **Important:**   If the type value is `vhost`, you **must** use this parameter. (optional)

    try:
        # Return basic PHP directives
        api_response = api_instance.php_ini_get_user_basic_directives(type, vhost=vhost)
        print("The response of LangPHPApi->php_ini_get_user_basic_directives:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LangPHPApi->php_ini_get_user_basic_directives: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| The type of &#x60;php.ini&#x60; file.  - &#x60;home&#x60; - &#x60;vhost&#x60;  **Important:**   If you set this parameter to &#x60;vhost&#x60;, you **must** also include the &#x60;vhost&#x60; parameter. | 
 **vhost** | **str**| The name of a virtual host.  **Important:**   If the type value is &#x60;vhost&#x60;, you **must** use this parameter. | [optional] 

### Return type

[**InlineResponse200284**](InlineResponse200284.md)

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

# **php_ini_get_user_content**
> InlineResponse200285 php_ini_get_user_content(type, vhost=vhost)

Return virtual host's php.ini content

This function returns the contents of a virtual host's `php.ini` file.

**Note:**

  This document **only** applies to systems that run EasyApache 4 with MultiPHP enabled.

**Important:**

  When you disable the [WebServer role](https://go.cpanel.net/howtouseserverprofiles#roles), the system **disables** this function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200285 import InlineResponse200285
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
    api_instance = clientapi_cpanel.LangPHPApi(api_client)
    type = 'vhost' # str | The type of `php.ini` file.  * `home` * `vhost`  **Important:**  If you set this parameter to `vhost`, you **must** also include the `vhost` parameter.
    vhost = 'clearly.com' # str | The name of a virtual host.  **Important:**   If the type value is `vhost`, you **must** use this parameter. (optional)

    try:
        # Return virtual host's php.ini content
        api_response = api_instance.php_ini_get_user_content(type, vhost=vhost)
        print("The response of LangPHPApi->php_ini_get_user_content:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LangPHPApi->php_ini_get_user_content: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| The type of &#x60;php.ini&#x60; file.  * &#x60;home&#x60; * &#x60;vhost&#x60;  **Important:**  If you set this parameter to &#x60;vhost&#x60;, you **must** also include the &#x60;vhost&#x60; parameter. | 
 **vhost** | **str**| The name of a virtual host.  **Important:**   If the type value is &#x60;vhost&#x60;, you **must** use this parameter. | [optional] 

### Return type

[**InlineResponse200285**](InlineResponse200285.md)

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

# **php_ini_get_user_paths**
> InlineResponse200286 php_ini_get_user_paths()

Return php.ini file paths

This function lists the `php.ini` file paths for the user's home directory and virtual host document roots.

**Note:**

  This document **only** applies to systems that run EasyApache 4 with MultiPHP enabled.

**Important:**

  When you disable the [WebServer role](https://go.cpanel.net/howtouseserverprofiles#roles), the system **disables** this function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200286 import InlineResponse200286
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
    api_instance = clientapi_cpanel.LangPHPApi(api_client)

    try:
        # Return php.ini file paths
        api_response = api_instance.php_ini_get_user_paths()
        print("The response of LangPHPApi->php_ini_get_user_paths:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LangPHPApi->php_ini_get_user_paths: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**InlineResponse200286**](InlineResponse200286.md)

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

# **php_ini_set_user_basic_directives**
> InlineResponse200287 php_ini_set_user_basic_directives(directive, type, vhost=vhost)

Update basic PHP directives

This function sets the values of any basic PHP directive. The *Basic Mode* section of cPanel's
[*MultiPHP INI Editor*](https://go.cpanel.net/whmdocsMultiPHPINIEditor) interface (*WHM >> Home >> Software >> MultiPHP INI Editor*) lists these directives.

**Note:**

  This document **only** applies to systems that run EasyApache 4 with MultiPHP enabled.

**Important:**

  When you disable the [Web Server role](https://go.cpanel.net/serverroles), the system **disables** this function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200287 import InlineResponse200287
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
    api_instance = clientapi_cpanel.LangPHPApi(api_client)
    directive = 'directive-1=allow_url_fopen%3A0&directive-2=upload_max_filesize%3A4M&directive-3=post_max_size' # str | The name of a PHP directive and its value.  **Note:**  * To change the directive's value for multiple PHP directives, increment the parameter name. For example, the `directive-1`, `directive-2`, and `directive-3` parameters. * You **must** format values as `<directive>:<value>`  
    type = 'vhost' # str | The type of `php.ini` file.  * `home` * `vhost`  **Important:**   If you set this parameter to `vhost`, you **must** also include the `vhost` parameter.
    vhost = 'clearly.com' # str | The name of a virtual host.  **Important:**   If the `type` value is `vhost`, you **must** use this parameter. (optional)

    try:
        # Update basic PHP directives
        api_response = api_instance.php_ini_set_user_basic_directives(directive, type, vhost=vhost)
        print("The response of LangPHPApi->php_ini_set_user_basic_directives:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LangPHPApi->php_ini_set_user_basic_directives: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **directive** | **str**| The name of a PHP directive and its value.  **Note:**  * To change the directive&#39;s value for multiple PHP directives, increment the parameter name. For example, the &#x60;directive-1&#x60;, &#x60;directive-2&#x60;, and &#x60;directive-3&#x60; parameters. * You **must** format values as &#x60;&lt;directive&gt;:&lt;value&gt;&#x60;   | 
 **type** | **str**| The type of &#x60;php.ini&#x60; file.  * &#x60;home&#x60; * &#x60;vhost&#x60;  **Important:**   If you set this parameter to &#x60;vhost&#x60;, you **must** also include the &#x60;vhost&#x60; parameter. | 
 **vhost** | **str**| The name of a virtual host.  **Important:**   If the &#x60;type&#x60; value is &#x60;vhost&#x60;, you **must** use this parameter. | [optional] 

### Return type

[**InlineResponse200287**](InlineResponse200287.md)

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

# **php_ini_set_user_content**
> InlineResponse200288 php_ini_set_user_content(content, type, vhost=vhost)

Update virtual host's php.ini content

This function changes the contents of a virtual host's `php.ini` file.

**Note:**

  This document **only** applies to systems that run EasyApache 4 with MultiPHP enabled.

**Important:**

  When you disable the [WebServer role](https://go.cpanel.net/howtouseserverprofiles#roles), the system **disables** this function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200288 import InlineResponse200288
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
    api_instance = clientapi_cpanel.LangPHPApi(api_client)
    content = '%5BPHP%5D%0D%0A%3B+About+php.ini%0D%0A%3B+php.ini+is+responsible+for+configuring+many+of+the+aspects+of+PHP%27s+behavior.%0D%0Apcre.backtrack_limit%3D100000' # str | The content of the `php.ini` file to change.
    type = 'vhost' # str | The type of `php.ini` file.  * `home` * `vhost`  **Important:**   If you set this parameter to `vhost`, you **must** also include the `vhost` parameter.
    vhost = 'clearly.com' # str | The name of a virtual host.  **Important:**   If the type value is `vhost` , you **must** use this parameter. (optional)

    try:
        # Update virtual host's php.ini content
        api_response = api_instance.php_ini_set_user_content(content, type, vhost=vhost)
        print("The response of LangPHPApi->php_ini_set_user_content:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LangPHPApi->php_ini_set_user_content: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content** | **str**| The content of the &#x60;php.ini&#x60; file to change. | 
 **type** | **str**| The type of &#x60;php.ini&#x60; file.  * &#x60;home&#x60; * &#x60;vhost&#x60;  **Important:**   If you set this parameter to &#x60;vhost&#x60;, you **must** also include the &#x60;vhost&#x60; parameter. | 
 **vhost** | **str**| The name of a virtual host.  **Important:**   If the type value is &#x60;vhost&#x60; , you **must** use this parameter. | [optional] 

### Return type

[**InlineResponse200288**](InlineResponse200288.md)

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

# **php_set_vhost_versions**
> InlineResponse200289 php_set_vhost_versions(version, vhost)

Update virtual host's PHP version

This function sets a virtual host's PHP version.

**Note:**

  This document **only** applies to systems that run EasyApache 4.

**Important:**

  When you disable the [WebServer role](https://go.cpanel.net/howtouseserverprofiles#roles), the system **disables** this function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200289 import InlineResponse200289
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
    api_instance = clientapi_cpanel.LangPHPApi(api_client)
    version = 'ea-php72' # str | The PHP version of a virtual host.
    vhost = 'vhost-1=example.com&vhost-2=example2.com&vhost-3=example3.com' # str | The virtual host's name.  **Note:**    To change the PHP version of multiple virtual hosts, duplicate or increment the parameter name. For example, `vhost-1`, `vhost-2`, and `vhost-3`.

    try:
        # Update virtual host's PHP version
        api_response = api_instance.php_set_vhost_versions(version, vhost)
        print("The response of LangPHPApi->php_set_vhost_versions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LangPHPApi->php_set_vhost_versions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**| The PHP version of a virtual host. | 
 **vhost** | **str**| The virtual host&#39;s name.  **Note:**    To change the PHP version of multiple virtual hosts, duplicate or increment the parameter name. For example, &#x60;vhost-1&#x60;, &#x60;vhost-2&#x60;, and &#x60;vhost-3&#x60;. | 

### Return type

[**InlineResponse200289**](InlineResponse200289.md)

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

