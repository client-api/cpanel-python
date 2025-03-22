# clientapi_cpanel.DomainRedirectionApi

All URIs are relative to *https://cpanel-server.tld:2083/execute*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_redirect**](DomainRedirectionApi.md#add_redirect) | **GET** /Mime/add_redirect | Add redirect to domain
[**delete_redirect**](DomainRedirectionApi.md#delete_redirect) | **GET** /Mime/delete_redirect | Remove redirect from domain
[**get_redirect**](DomainRedirectionApi.md#get_redirect) | **GET** /Mime/get_redirect | Return redirect URL for domain
[**list_redirects**](DomainRedirectionApi.md#list_redirects) | **GET** /Mime/list_redirects | Return .htaccess files&#39; redirects


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
    api_instance = clientapi_cpanel.DomainRedirectionApi(api_client)
    domain = 'example.com' # str | The domain from which to redirect.
    redirect = 'http://example.com/' # str | The URL to which to redirect.
    redirect_wildcard = 0 # int | Whether to redirect all files within a directory to the same filename within the destination directory. * `1` - Redirect all files within the directory. * `0` - Do **not** redirect all files within the directory. (optional) (default to 0)
    redirect_www = 0 # int | Whether to redirect domains with or without `www`. * `2` - Redirect with `www`. * `1` - Redirect without `www`. * `0` - Redirect with **and** without `www`. (optional) (default to 0)
    src = '/' # str | A specific page from which to redirect. (optional) (default to '/')
    type = permanent # str | Whether the redirect is temporary.  * `permanent`  * `temp` (optional) (default to permanent)

    try:
        # Add redirect to domain
        api_response = api_instance.add_redirect(domain, redirect, redirect_wildcard=redirect_wildcard, redirect_www=redirect_www, src=src, type=type)
        print("The response of DomainRedirectionApi->add_redirect:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DomainRedirectionApi->add_redirect: %s\n" % e)
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
    api_instance = clientapi_cpanel.DomainRedirectionApi(api_client)
    domain = 'example.com' # str | The domain name.
    args = '' # str | An argument string that contains the arguments of a `Redirect` or `RedirectMatch` directives. (optional) (default to '')
    docroot = '/home/example/public_html/' # str | The absolute file path to the document root containing the `.htaccess` file to change.  If you don't pass this parameter, the system looks up the document root from the `domain` parameter's value. (optional)
    src = '' # str | The specific page that redirects visitors. (optional) (default to '')

    try:
        # Remove redirect from domain
        api_response = api_instance.delete_redirect(domain, args=args, docroot=docroot, src=src)
        print("The response of DomainRedirectionApi->delete_redirect:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DomainRedirectionApi->delete_redirect: %s\n" % e)
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
    api_instance = clientapi_cpanel.DomainRedirectionApi(api_client)
    domain = 'example.com' # str | The domain's name.

    try:
        # Return redirect URL for domain
        api_response = api_instance.get_redirect(domain)
        print("The response of DomainRedirectionApi->get_redirect:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DomainRedirectionApi->get_redirect: %s\n" % e)
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
    api_instance = clientapi_cpanel.DomainRedirectionApi(api_client)
    destination = 'http://example.tld' # str | The string with which to filter results.  ** Note: **  This will **only** return results that match the `destination` parameter **exactly**. (optional)
    regex = '\"^[a-z0-9_-]{6,18}$\"' # str | A Perl regular expression that filters the results. The system matches the regular expression to the `sourceurl` return value. (optional)

    try:
        # Return .htaccess files' redirects
        api_response = api_instance.list_redirects(destination=destination, regex=regex)
        print("The response of DomainRedirectionApi->list_redirects:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DomainRedirectionApi->list_redirects: %s\n" % e)
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

