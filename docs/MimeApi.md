# clientapi_cpanel.MimeApi

All URIs are relative to *https://cpanel-server.tld:2083/execute*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_handler**](MimeApi.md#add_handler) | **GET** /Mime/add_handler | Add web server MIME type handler
[**add_hotlink**](MimeApi.md#add_hotlink) | **GET** /Mime/add_hotlink | Enable hotlink protection
[**add_mime**](MimeApi.md#add_mime) | **GET** /Mime/add_mime | Add MIME type to web server
[**add_redirect**](MimeApi.md#add_redirect) | **GET** /Mime/add_redirect | Add redirect to domain
[**delete_handler**](MimeApi.md#delete_handler) | **GET** /Mime/delete_handler | Remove web server MIME type handler
[**delete_hotlink**](MimeApi.md#delete_hotlink) | **GET** /Mime/delete_hotlink | Disable hotlink protection
[**delete_mime**](MimeApi.md#delete_mime) | **GET** /Mime/delete_mime | Remove MIME type from web server
[**delete_redirect**](MimeApi.md#delete_redirect) | **GET** /Mime/delete_redirect | Remove redirect from domain
[**get_redirect**](MimeApi.md#get_redirect) | **GET** /Mime/get_redirect | Return redirect URL for domain
[**list_handlers**](MimeApi.md#list_handlers) | **GET** /Mime/list_handlers | Return web server&#39;s MIME handlers
[**list_hotlinks**](MimeApi.md#list_hotlinks) | **GET** /Mime/list_hotlinks | Return domains with hotlink protection
[**list_mime**](MimeApi.md#list_mime) | **GET** /Mime/list_mime | Return web server&#39;s MIME types
[**list_redirects**](MimeApi.md#list_redirects) | **GET** /Mime/list_redirects | Return .htaccess files&#39; redirects
[**redirect_info**](MimeApi.md#redirect_info) | **GET** /Mime/redirect_info | Return redirect information


# **add_handler**
> InlineResponse200316 add_handler(extension, handler)

Add web server MIME type handler

This function creates an Apache MIME type handler for a file extension.

**Important:**

When you disable the [Web Server](https://go.cpanel.net/serverroles) role, the system **disables** this function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200316 import InlineResponse200316
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
    api_instance = clientapi_cpanel.MimeApi(api_client)
    extension = '.foo' # str | The file extension.
    handler = 'txt-foo' # str | The Apache MIME handler.

    try:
        # Add web server MIME type handler
        api_response = api_instance.add_handler(extension, handler)
        print("The response of MimeApi->add_handler:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MimeApi->add_handler: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **extension** | **str**| The file extension. | 
 **handler** | **str**| The Apache MIME handler. | 

### Return type

[**InlineResponse200316**](InlineResponse200316.md)

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

# **add_hotlink**
> InlineResponse200317 add_hotlink(extensions, redirect_url, urls, allow_null=allow_null)

Enable hotlink protection

This function adds hotlink protection for a site. Hotlink protection will redirect users to another URL if they navigate to a file with a specified extension, but an allowed URL did not refer them.

**Important:**

  When you disable the [WebServer role](https://go.cpanel.net/serverroles), the system **disables** this function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200317 import InlineResponse200317
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
    api_instance = clientapi_cpanel.MimeApi(api_client)
    extensions = 'foo,bar' # str | File types to hotlink protect.  **Note:**  To protect multiple file types, use a comma-separated list.
    redirect_url = 'http://redirect.example.com/' # str | The URL to which the system sends hotlinkers.
    urls = 'http://example.com/ http://foobar.com/' # str | The site to hotlink protect.  **Note:**  To protect multiple URLs, separate each URL with a newline character.
    allow_null = 1 # int | Whether the domain allows hotlinks. * `1` - Allows. * `0` - Does **not** allow. (optional)

    try:
        # Enable hotlink protection
        api_response = api_instance.add_hotlink(extensions, redirect_url, urls, allow_null=allow_null)
        print("The response of MimeApi->add_hotlink:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MimeApi->add_hotlink: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **extensions** | **str**| File types to hotlink protect.  **Note:**  To protect multiple file types, use a comma-separated list. | 
 **redirect_url** | **str**| The URL to which the system sends hotlinkers. | 
 **urls** | **str**| The site to hotlink protect.  **Note:**  To protect multiple URLs, separate each URL with a newline character. | 
 **allow_null** | **int**| Whether the domain allows hotlinks. * &#x60;1&#x60; - Allows. * &#x60;0&#x60; - Does **not** allow. | [optional] 

### Return type

[**InlineResponse200317**](InlineResponse200317.md)

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

# **add_mime**
> InlineResponse200318 add_mime(extension, type)

Add MIME type to web server

This function adds a MIME type to Apache.

**Important:**

When you disable the [Web Server](https://go.cpanel.net/serverroles) role, the system **disables** this function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200318 import InlineResponse200318
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
    api_instance = clientapi_cpanel.MimeApi(api_client)
    extension = '.foo' # str | The file extension.
    type = 'text/foo' # str | The MIME type.

    try:
        # Add MIME type to web server
        api_response = api_instance.add_mime(extension, type)
        print("The response of MimeApi->add_mime:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MimeApi->add_mime: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **extension** | **str**| The file extension. | 
 **type** | **str**| The MIME type. | 

### Return type

[**InlineResponse200318**](InlineResponse200318.md)

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

# **add_redirect**
> InlineResponse200319 add_redirect(domain, redirect, redirect_wildcard=redirect_wildcard, redirect_www=redirect_www, src=src, type=type)

Add redirect to domain

This function adds a redirect to a domain.

**Important:**

  When you disable the [*Web Server* role](https://go.cpanel.net/serverroles), the system **disables** this function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200319 import InlineResponse200319
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
    api_instance = clientapi_cpanel.MimeApi(api_client)
    domain = 'example.com' # str | The domain from which to redirect.
    redirect = 'http://example.com/' # str | The URL to which to redirect.
    redirect_wildcard = 0 # int | Whether to redirect all files within a directory to the same filename within the destination directory. * `1` - Redirect all files within the directory. * `0` - Do **not** redirect all files within the directory. (optional) (default to 0)
    redirect_www = 0 # int | Whether to redirect domains with or without `www`. * `2` - Redirect with `www`. * `1` - Redirect without `www`. * `0` - Redirect with **and** without `www`. (optional) (default to 0)
    src = '/' # str | A specific page from which to redirect. (optional) (default to '/')
    type = permanent # str | Whether the redirect is temporary.  * `permanent`  * `temp` (optional) (default to permanent)

    try:
        # Add redirect to domain
        api_response = api_instance.add_redirect(domain, redirect, redirect_wildcard=redirect_wildcard, redirect_www=redirect_www, src=src, type=type)
        print("The response of MimeApi->add_redirect:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MimeApi->add_redirect: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**| The domain from which to redirect. | 
 **redirect** | **str**| The URL to which to redirect. | 
 **redirect_wildcard** | **int**| Whether to redirect all files within a directory to the same filename within the destination directory. * &#x60;1&#x60; - Redirect all files within the directory. * &#x60;0&#x60; - Do **not** redirect all files within the directory. | [optional] [default to 0]
 **redirect_www** | **int**| Whether to redirect domains with or without &#x60;www&#x60;. * &#x60;2&#x60; - Redirect with &#x60;www&#x60;. * &#x60;1&#x60; - Redirect without &#x60;www&#x60;. * &#x60;0&#x60; - Redirect with **and** without &#x60;www&#x60;. | [optional] [default to 0]
 **src** | **str**| A specific page from which to redirect. | [optional] [default to &#39;/&#39;]
 **type** | **str**| Whether the redirect is temporary.  * &#x60;permanent&#x60;  * &#x60;temp&#x60; | [optional] [default to permanent]

### Return type

[**InlineResponse200319**](InlineResponse200319.md)

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

# **delete_handler**
> InlineResponse200320 delete_handler(extension)

Remove web server MIME type handler

This function deletes an Apache MIME type handler.

**Important:**

  When you disable the [WebServer role](https://go.cpanel.net/serverroles), the system **disables** this function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200320 import InlineResponse200320
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
    api_instance = clientapi_cpanel.MimeApi(api_client)
    extension = '.foo' # str | The file extension.

    try:
        # Remove web server MIME type handler
        api_response = api_instance.delete_handler(extension)
        print("The response of MimeApi->delete_handler:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MimeApi->delete_handler: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **extension** | **str**| The file extension. | 

### Return type

[**InlineResponse200320**](InlineResponse200320.md)

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

# **delete_hotlink**
> InlineResponse200321 delete_hotlink()

Disable hotlink protection

This function removes hotlink protection.

**Important:**

  When you disable the [Web Server](https://go.cpanel.net/serverroles) role, the system **disables** this function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200321 import InlineResponse200321
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
    api_instance = clientapi_cpanel.MimeApi(api_client)

    try:
        # Disable hotlink protection
        api_response = api_instance.delete_hotlink()
        print("The response of MimeApi->delete_hotlink:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MimeApi->delete_hotlink: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**InlineResponse200321**](InlineResponse200321.md)

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

# **delete_mime**
> InlineResponse200322 delete_mime(type)

Remove MIME type from web server

This function removes a MIME type from Apache.

**Important:**

  When you disable the [WebServer role](https://go.cpanel.net/serverroles), the system **disables** this function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200322 import InlineResponse200322
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
    api_instance = clientapi_cpanel.MimeApi(api_client)
    type = 'text/foo' # str | The MIME type.

    try:
        # Remove MIME type from web server
        api_response = api_instance.delete_mime(type)
        print("The response of MimeApi->delete_mime:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MimeApi->delete_mime: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| The MIME type. | 

### Return type

[**InlineResponse200322**](InlineResponse200322.md)

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

# **delete_redirect**
> InlineResponse200323 delete_redirect(domain, args=args, docroot=docroot, src=src)

Remove redirect from domain

This function removes a redirect from a domain.

**Important:**

When you disable the [Web Server role](https://go.cpanel.net/serverroles#roles), the system **disables** this function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200323 import InlineResponse200323
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
    api_instance = clientapi_cpanel.MimeApi(api_client)
    domain = 'example.com' # str | The domain name.
    args = '' # str | An argument string that contains the arguments of a `Redirect` or `RedirectMatch` directives. (optional) (default to '')
    docroot = '/home/example/public_html/' # str | The absolute file path to the document root containing the `.htaccess` file to change.  If you don't pass this parameter, the system looks up the document root from the `domain` parameter's value. (optional)
    src = '' # str | The specific page that redirects visitors. (optional) (default to '')

    try:
        # Remove redirect from domain
        api_response = api_instance.delete_redirect(domain, args=args, docroot=docroot, src=src)
        print("The response of MimeApi->delete_redirect:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MimeApi->delete_redirect: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**| The domain name. | 
 **args** | **str**| An argument string that contains the arguments of a &#x60;Redirect&#x60; or &#x60;RedirectMatch&#x60; directives. | [optional] [default to &#39;&#39;]
 **docroot** | **str**| The absolute file path to the document root containing the &#x60;.htaccess&#x60; file to change.  If you don&#39;t pass this parameter, the system looks up the document root from the &#x60;domain&#x60; parameter&#39;s value. | [optional] 
 **src** | **str**| The specific page that redirects visitors. | [optional] [default to &#39;&#39;]

### Return type

[**InlineResponse200323**](InlineResponse200323.md)

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

# **get_redirect**
> InlineResponse200324 get_redirect(domain)

Return redirect URL for domain

This function retrieves a redirection URL for a domain.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200324 import InlineResponse200324
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
    api_instance = clientapi_cpanel.MimeApi(api_client)
    domain = 'example.com' # str | The domain's name.

    try:
        # Return redirect URL for domain
        api_response = api_instance.get_redirect(domain)
        print("The response of MimeApi->get_redirect:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MimeApi->get_redirect: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**| The domain&#39;s name. | 

### Return type

[**InlineResponse200324**](InlineResponse200324.md)

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

# **list_handlers**
> InlineResponse200325 list_handlers(type)

Return web server's MIME handlers

This function lists all of Apache's MIME handlers.

**Important:**

  When you disable the [WebServer role](https://go.cpanel.net/serverroles),
  the system **disables** this function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200325 import InlineResponse200325
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
    api_instance = clientapi_cpanel.MimeApi(api_client)
    type = 'user' # str | Whether to retrieve system or user handlers.

    try:
        # Return web server's MIME handlers
        api_response = api_instance.list_handlers(type)
        print("The response of MimeApi->list_handlers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MimeApi->list_handlers: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| Whether to retrieve system or user handlers. | 

### Return type

[**InlineResponse200325**](InlineResponse200325.md)

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

# **list_hotlinks**
> InlineResponse200326 list_hotlinks()

Return domains with hotlink protection

This function lists domains with hotlink protection.

**Important:**

When you **disable** the [Web Server](https://go.cpanel.net/serverroles) role, the system **disables** this function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200326 import InlineResponse200326
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
    api_instance = clientapi_cpanel.MimeApi(api_client)

    try:
        # Return domains with hotlink protection
        api_response = api_instance.list_hotlinks()
        print("The response of MimeApi->list_hotlinks:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MimeApi->list_hotlinks: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**InlineResponse200326**](InlineResponse200326.md)

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

# **list_mime**
> InlineResponse200327 list_mime(type)

Return web server's MIME types

This function lists all of Apache's MIME types.

**Note:**

  This function does **not** list PHP versions with MIME types when the user or domain enables PHP-FPM. The system displays **only** custom MIME types.

**Important:**

  When you disable the [Web Server role](https://go.cpanel.net/serverroles), the system **disables** this function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200327 import InlineResponse200327
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
    api_instance = clientapi_cpanel.MimeApi(api_client)
    type = 'user' # str | The MIME types to list. * `system` — List the Apache system MIME types. * `user` — List the Apache user MIME types.

    try:
        # Return web server's MIME types
        api_response = api_instance.list_mime(type)
        print("The response of MimeApi->list_mime:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MimeApi->list_mime: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| The MIME types to list. * &#x60;system&#x60; — List the Apache system MIME types. * &#x60;user&#x60; — List the Apache user MIME types. | 

### Return type

[**InlineResponse200327**](InlineResponse200327.md)

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

# **list_redirects**
> InlineResponse200328 list_redirects(destination=destination, regex=regex)

Return .htaccess files' redirects

This function lists the redirects in an account's .htaccess files.

**Important:**

When you disable the [Web Server role](https://go.cpanel.net/serverroles#roles), the system **disables** this function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200328 import InlineResponse200328
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
    api_instance = clientapi_cpanel.MimeApi(api_client)
    destination = 'http://example.tld' # str | The string with which to filter results.  ** Note: **  This will **only** return results that match the `destination` parameter **exactly**. (optional)
    regex = '\"^[a-z0-9_-]{6,18}$\"' # str | A Perl regular expression that filters the results. The system matches the regular expression to the `sourceurl` return value. (optional)

    try:
        # Return .htaccess files' redirects
        api_response = api_instance.list_redirects(destination=destination, regex=regex)
        print("The response of MimeApi->list_redirects:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MimeApi->list_redirects: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **destination** | **str**| The string with which to filter results.  ** Note: **  This will **only** return results that match the &#x60;destination&#x60; parameter **exactly**. | [optional] 
 **regex** | **str**| A Perl regular expression that filters the results. The system matches the regular expression to the &#x60;sourceurl&#x60; return value. | [optional] 

### Return type

[**InlineResponse200328**](InlineResponse200328.md)

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

# **redirect_info**
> InlineResponse200329 redirect_info(domain, url)

Return redirect information

This function retrieves redirect information for a URL or `** All Public Domains **`.

**Important:**

When you disable the [Web Server role](https://go.cpanel.net/serverroles), the system **disables** this function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200329 import InlineResponse200329
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
    api_instance = clientapi_cpanel.MimeApi(api_client)
    domain = 'example.com' # str | The domain for which to retrieve redirector information.
    url = 'http://redirect.example.com' # str | The URL for which to retrieve redirector information.

    try:
        # Return redirect information
        api_response = api_instance.redirect_info(domain, url)
        print("The response of MimeApi->redirect_info:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MimeApi->redirect_info: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**| The domain for which to retrieve redirector information. | 
 **url** | **str**| The URL for which to retrieve redirector information. | 

### Return type

[**InlineResponse200329**](InlineResponse200329.md)

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

