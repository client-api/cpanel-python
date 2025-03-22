# clientapi_cpanel.EmailForwardingApi

All URIs are relative to *https://cpanel-server.tld:2083/execute*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_domain_forwarder**](EmailForwardingApi.md#add_domain_forwarder) | **GET** /Email/add_domain_forwarder | Create domain-level forwarder
[**add_forwarder**](EmailForwardingApi.md#add_forwarder) | **GET** /Email/add_forwarder | Create email account forwarder
[**count_forwarders**](EmailForwardingApi.md#count_forwarders) | **GET** /Email/count_forwarders | Return cPanel account&#39;s mail forwarder total
[**delete_domain_forwarder**](EmailForwardingApi.md#delete_domain_forwarder) | **GET** /Email/delete_domain_forwarder | Delete domain-level forwarder
[**delete_forwarder**](EmailForwardingApi.md#delete_forwarder) | **GET** /Email/delete_forwarder | Delete email account&#39;s email forwarder
[**list_domain_forwarders**](EmailForwardingApi.md#list_domain_forwarders) | **GET** /Email/list_domain_forwarders | Return domain-level forwarders
[**list_forwarders**](EmailForwardingApi.md#list_forwarders) | **GET** /Email/list_forwarders | Return domain&#39;s forwarders
[**list_forwarders_backups**](EmailForwardingApi.md#list_forwarders_backups) | **GET** /Email/list_forwarders_backups | Return domains with domain-level forwarders


# **add_domain_forwarder**
> InlineResponse200121 add_domain_forwarder(destdomain, domain)

Create domain-level forwarder

This function creates a domain-level forwarder.

**Important:**

  When you disable the [*Receive Mail* role](https://go.cpanel.net/serverroles), the system **disables** this function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200121 import InlineResponse200121
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
    api_instance = clientapi_cpanel.EmailForwardingApi(api_client)
    destdomain = 'forwardtome.com' # str | The domain to receive forwarded mail.
    domain = 'example.com' # str | The domain on the cPanel account from which to forward mail.

    try:
        # Create domain-level forwarder
        api_response = api_instance.add_domain_forwarder(destdomain, domain)
        print("The response of EmailForwardingApi->add_domain_forwarder:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailForwardingApi->add_domain_forwarder: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **destdomain** | **str**| The domain to receive forwarded mail. | 
 **domain** | **str**| The domain on the cPanel account from which to forward mail. | 

### Return type

[**InlineResponse200121**](InlineResponse200121.md)

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

# **add_forwarder**
> InlineResponse200122 add_forwarder(domain, email, fwdopt, failmsgs=failmsgs, fwdemail=fwdemail, fwdsystem=fwdsystem, pipefwd=pipefwd)

Create email account forwarder

This function creates an email forwarder.

**Important:**

  When you disable the MailReceive role, the system disables this function. 
  For more information, read our [How to Use Server Profiles](https://go.cpanel.net/howtouseserverprofiles) 
  documentation.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200122 import InlineResponse200122
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
    api_instance = clientapi_cpanel.EmailForwardingApi(api_client)
    domain = 'example.com' # str | The domain.
    email = 'forwardme@example.com' # str | The email address to forward.
    fwdopt = 'fwd' # str | The method to use to handle the email address's mail.
    failmsgs = 'No such person at this address' # str | The failure message for the message's sender.  **Note:**   Use this parameter if you used the fail method for the fwdopt parameter. (optional) (default to 'No such person at this address')
    fwdemail = 'fwdtome@example.com' # str | The email address to which the system forwards messages.  **Note:**   You must use this parameter if you used the fwd method for the fwdopt parameter. You can pass multiple addresses to this parameter as a comma-separated list. (optional)
    fwdsystem = 'user' # str | The system user to whom the system forwards messages.  **Note:**   You must use this parameter if you used the system method for the fwdopt parameter. (optional)
    pipefwd = 'mailscript.pl' # str | The application to which the system pipes messages.  **Note:**   You must use this parameter if you used the pipe method for the fwdopt parameter.  **Important:**    This parameter requires the FileStorage role. For more information, read our    [How to Use Server Profiles](https://go.cpanel.net/howtouseserverprofiles) documentation. (optional)

    try:
        # Create email account forwarder
        api_response = api_instance.add_forwarder(domain, email, fwdopt, failmsgs=failmsgs, fwdemail=fwdemail, fwdsystem=fwdsystem, pipefwd=pipefwd)
        print("The response of EmailForwardingApi->add_forwarder:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailForwardingApi->add_forwarder: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**| The domain. | 
 **email** | **str**| The email address to forward. | 
 **fwdopt** | **str**| The method to use to handle the email address&#39;s mail. | 
 **failmsgs** | **str**| The failure message for the message&#39;s sender.  **Note:**   Use this parameter if you used the fail method for the fwdopt parameter. | [optional] [default to &#39;No such person at this address&#39;]
 **fwdemail** | **str**| The email address to which the system forwards messages.  **Note:**   You must use this parameter if you used the fwd method for the fwdopt parameter. You can pass multiple addresses to this parameter as a comma-separated list. | [optional] 
 **fwdsystem** | **str**| The system user to whom the system forwards messages.  **Note:**   You must use this parameter if you used the system method for the fwdopt parameter. | [optional] 
 **pipefwd** | **str**| The application to which the system pipes messages.  **Note:**   You must use this parameter if you used the pipe method for the fwdopt parameter.  **Important:**    This parameter requires the FileStorage role. For more information, read our    [How to Use Server Profiles](https://go.cpanel.net/howtouseserverprofiles) documentation. | [optional] 

### Return type

[**InlineResponse200122**](InlineResponse200122.md)

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

# **count_forwarders**
> InlineResponse200133 count_forwarders()

Return cPanel account's mail forwarder total

This function returns the number of [forwarders](https://go.cpanel.net/Forwarders) for every email address on a cPanel account.

**Important:**

  When you disable the [*Receive Mail* role](https://go.cpanel.net/serverroles#roles), the system **disables** this function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200133 import InlineResponse200133
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
    api_instance = clientapi_cpanel.EmailForwardingApi(api_client)

    try:
        # Return cPanel account's mail forwarder total
        api_response = api_instance.count_forwarders()
        print("The response of EmailForwardingApi->count_forwarders:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailForwardingApi->count_forwarders: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**InlineResponse200133**](InlineResponse200133.md)

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

# **delete_domain_forwarder**
> InlineResponse200137 delete_domain_forwarder(domain)

Delete domain-level forwarder

This function deletes a domain-level forwarder.

**Important:**

  When you disable the [*Receive Mail* role](https://go.cpanel.net/serverroles), the system **disables** this function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200137 import InlineResponse200137
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
    api_instance = clientapi_cpanel.EmailForwardingApi(api_client)
    domain = 'example.com' # str | The domain name.

    try:
        # Delete domain-level forwarder
        api_response = api_instance.delete_domain_forwarder(domain)
        print("The response of EmailForwardingApi->delete_domain_forwarder:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailForwardingApi->delete_domain_forwarder: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**| The domain name. | 

### Return type

[**InlineResponse200137**](InlineResponse200137.md)

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

# **delete_forwarder**
> InlineResponse200139 delete_forwarder(address, forwarder)

Delete email account's email forwarder

This function deletes an email forwarder.

**Important:**

  When you disable the [*Receive Mail* role](https://go.cpanel.net/serverroles), the system **disables** this function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200139 import InlineResponse200139
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
    api_instance = clientapi_cpanel.EmailForwardingApi(api_client)
    address = 'user@example.com' # str | The forwarder's email address.
    forwarder = 'fwdtome@example.com' # str | The forwarder's destination. * A valid email address. * A script location. * A system account.

    try:
        # Delete email account's email forwarder
        api_response = api_instance.delete_forwarder(address, forwarder)
        print("The response of EmailForwardingApi->delete_forwarder:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailForwardingApi->delete_forwarder: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address** | **str**| The forwarder&#39;s email address. | 
 **forwarder** | **str**| The forwarder&#39;s destination. * A valid email address. * A script location. * A system account. | 

### Return type

[**InlineResponse200139**](InlineResponse200139.md)

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

# **list_domain_forwarders**
> InlineResponse200182 list_domain_forwarders(domain=domain)

Return domain-level forwarders

This function lists domain-level forwarders.

**Important:**

  When you disable the [*Receive Mail* role](https://go.cpanel.net/serverroles), the system **disables** this function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200182 import InlineResponse200182
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
    api_instance = clientapi_cpanel.EmailForwardingApi(api_client)
    domain = 'example.com' # str | The domain name to query. If you do not use this parameter, the function returns all domain-level forwarders on the cPanel account. (optional)

    try:
        # Return domain-level forwarders
        api_response = api_instance.list_domain_forwarders(domain=domain)
        print("The response of EmailForwardingApi->list_domain_forwarders:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailForwardingApi->list_domain_forwarders: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**| The domain name to query. If you do not use this parameter, the function returns all domain-level forwarders on the cPanel account. | [optional] 

### Return type

[**InlineResponse200182**](InlineResponse200182.md)

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

# **list_forwarders**
> InlineResponse200185 list_forwarders(domain, regex=regex)

Return domain's forwarders

This function lists a domain's forwarders.

**Important:**

  When you disable the [*Receive Mail* role](https://go.cpanel.net/serverroles), the system **disables** this function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200185 import InlineResponse200185
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
    api_instance = clientapi_cpanel.EmailForwardingApi(api_client)
    domain = 'example.com' # str | The domain.
    regex = 'user' # str | A [Perl Compatible Regular Expression (PCRE)](https://en.wikipedia.org/wiki/Perl_Compatible_Regular_Expressions) that filters the results. If you do **not** use this parameter, the function returns results for all of the account's filters. (optional)

    try:
        # Return domain's forwarders
        api_response = api_instance.list_forwarders(domain, regex=regex)
        print("The response of EmailForwardingApi->list_forwarders:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailForwardingApi->list_forwarders: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**| The domain. | 
 **regex** | **str**| A [Perl Compatible Regular Expression (PCRE)](https://en.wikipedia.org/wiki/Perl_Compatible_Regular_Expressions) that filters the results. If you do **not** use this parameter, the function returns results for all of the account&#39;s filters. | [optional] 

### Return type

[**InlineResponse200185**](InlineResponse200185.md)

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

# **list_forwarders_backups**
> InlineResponse200186 list_forwarders_backups()

Return domains with domain-level forwarders

This function lists the domains with domain-level forwarders.

**Important:**

  When you disable the [*Receive Mail* role](https://go.cpanel.net/serverroles), the system **disables** this function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200186 import InlineResponse200186
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
    api_instance = clientapi_cpanel.EmailForwardingApi(api_client)

    try:
        # Return domains with domain-level forwarders
        api_response = api_instance.list_forwarders_backups()
        print("The response of EmailForwardingApi->list_forwarders_backups:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailForwardingApi->list_forwarders_backups: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**InlineResponse200186**](InlineResponse200186.md)

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

