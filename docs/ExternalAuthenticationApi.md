# clientapi_cpanel.ExternalAuthenticationApi

All URIs are relative to *https://cpanel-server.tld:2083/execute*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_authn_link**](ExternalAuthenticationApi.md#add_authn_link) | **GET** /ExternalAuthentication/add_authn_link | Add external authentication link
[**configured_modules**](ExternalAuthenticationApi.md#configured_modules) | **GET** /ExternalAuthentication/configured_modules | Return server&#39;s external authentication providers
[**get_authn_links**](ExternalAuthenticationApi.md#get_authn_links) | **GET** /ExternalAuthentication/get_authn_links | Return external authentication links
[**has_external_auth_modules_configured**](ExternalAuthenticationApi.md#has_external_auth_modules_configured) | **GET** /ExternalAuthentication/has_external_auth_modules_configured | Return external authentication user status
[**remove_authn_link**](ExternalAuthenticationApi.md#remove_authn_link) | **GET** /ExternalAuthentication/remove_authn_link | Remove external authentication link


# **add_authn_link**
> InlineResponse200227 add_authn_link(preferred_username, provider_id, subject_unique_identifier, username)

Add external authentication link

This function adds an External Authentication authorization link to an account.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200227 import InlineResponse200227
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
    api_instance = clientapi_cpanel.ExternalAuthenticationApi(api_client)
    preferred_username = 'Example' # str | The preferred username of the account on the identity provider.
    provider_id = 'google' # str | The name of the identity provider.
    subject_unique_identifier = '123456789012345678901' # str | The unique identifier for the user at the identity provider.
    username = 'example' # str | The username.

    try:
        # Add external authentication link
        api_response = api_instance.add_authn_link(preferred_username, provider_id, subject_unique_identifier, username)
        print("The response of ExternalAuthenticationApi->add_authn_link:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExternalAuthenticationApi->add_authn_link: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **preferred_username** | **str**| The preferred username of the account on the identity provider. | 
 **provider_id** | **str**| The name of the identity provider. | 
 **subject_unique_identifier** | **str**| The unique identifier for the user at the identity provider. | 
 **username** | **str**| The username. | 

### Return type

[**InlineResponse200227**](InlineResponse200227.md)

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

# **configured_modules**
> InlineResponse200228 configured_modules()

Return server's external authentication providers

This function lists the display information for your server's available and configured external authentication identity provider modules.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200228 import InlineResponse200228
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
    api_instance = clientapi_cpanel.ExternalAuthenticationApi(api_client)

    try:
        # Return server's external authentication providers
        api_response = api_instance.configured_modules()
        print("The response of ExternalAuthenticationApi->configured_modules:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExternalAuthenticationApi->configured_modules: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**InlineResponse200228**](InlineResponse200228.md)

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

# **get_authn_links**
> InlineResponse200229 get_authn_links()

Return external authentication links

This function lists the external authentication links to the current cPanel account.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200229 import InlineResponse200229
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
    api_instance = clientapi_cpanel.ExternalAuthenticationApi(api_client)

    try:
        # Return external authentication links
        api_response = api_instance.get_authn_links()
        print("The response of ExternalAuthenticationApi->get_authn_links:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExternalAuthenticationApi->get_authn_links: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**InlineResponse200229**](InlineResponse200229.md)

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

# **has_external_auth_modules_configured**
> InlineResponse200230 has_external_auth_modules_configured()

Return external authentication user status

This function determines whether the user enabled external authentication modules.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200230 import InlineResponse200230
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
    api_instance = clientapi_cpanel.ExternalAuthenticationApi(api_client)

    try:
        # Return external authentication user status
        api_response = api_instance.has_external_auth_modules_configured()
        print("The response of ExternalAuthenticationApi->has_external_auth_modules_configured:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExternalAuthenticationApi->has_external_auth_modules_configured: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**InlineResponse200230**](InlineResponse200230.md)

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

# **remove_authn_link**
> InlineResponse200231 remove_authn_link(provider, subject_unique_identifier)

Remove external authentication link

This function removes a link to an account at an external authentication identity provider.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200231 import InlineResponse200231
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
    api_instance = clientapi_cpanel.ExternalAuthenticationApi(api_client)
    provider = 'cpanelid' # str | The name of the identity provider.
    subject_unique_identifier = '123456789012345678901' # str | The unique identifier for the user at the identity provider.

    try:
        # Remove external authentication link
        api_response = api_instance.remove_authn_link(provider, subject_unique_identifier)
        print("The response of ExternalAuthenticationApi->remove_authn_link:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExternalAuthenticationApi->remove_authn_link: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider** | **str**| The name of the identity provider. | 
 **subject_unique_identifier** | **str**| The unique identifier for the user at the identity provider. | 

### Return type

[**InlineResponse200231**](InlineResponse200231.md)

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

