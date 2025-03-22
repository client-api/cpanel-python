# clientapi_cpanel.TokensApi

All URIs are relative to *https://cpanel-server.tld:2083/execute*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_full_access**](TokensApi.md#create_full_access) | **GET** /Tokens/create_full_access | Create cPanel API token
[**rename**](TokensApi.md#rename) | **GET** /Tokens/rename | Update cPanel API token&#39;s name
[**revoke**](TokensApi.md#revoke) | **GET** /Tokens/revoke | Remove cPanel API token
[**tokens_list**](TokensApi.md#tokens_list) | **GET** /Tokens/list | Return cPanel API tokens


# **create_full_access**
> InlineResponse200517 create_full_access(name, expires_at=expires_at)

Create cPanel API token

This function creates a new API token with full access to all of a cPanel account's features.

**Note:**

The token **only** grants access to the features that the account has access to. For example,
if you disable the [*File Manager*](https://go.cpanel.net/cpaneldocsFileManager) feature, the
token can't access it.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200517 import InlineResponse200517
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
    api_instance = clientapi_cpanel.TokensApi(api_client)
    name = 'example' # str | The API token's name.  **Note:**  The name may **only** contain alphanumeric characters, dashes (`-`), and underscores (`_`).
    expires_at = 1609372800 # int | The API token's expiration time.  **Important:**  * When an API token expires the system does **not** delete it. You **must** manually delete expired API tokens. * If you do not use this parameter, the API token will **not** expire. (optional)

    try:
        # Create cPanel API token
        api_response = api_instance.create_full_access(name, expires_at=expires_at)
        print("The response of TokensApi->create_full_access:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TokensApi->create_full_access: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The API token&#39;s name.  **Note:**  The name may **only** contain alphanumeric characters, dashes (&#x60;-&#x60;), and underscores (&#x60;_&#x60;). | 
 **expires_at** | **int**| The API token&#39;s expiration time.  **Important:**  * When an API token expires the system does **not** delete it. You **must** manually delete expired API tokens. * If you do not use this parameter, the API token will **not** expire. | [optional] 

### Return type

[**InlineResponse200517**](InlineResponse200517.md)

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

# **rename**
> InlineResponse200519 rename(name, new_name)

Update cPanel API token's name

This function renames a cPanel account's existing API token.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200519 import InlineResponse200519
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
    api_instance = clientapi_cpanel.TokensApi(api_client)
    name = 'example' # str | The API token's name.
    new_name = 'newexample' # str | The new name for the API token.  **Note:**  The name may only contain alphanumeric characters, dashes (`-`), and underscores (`_`).

    try:
        # Update cPanel API token's name
        api_response = api_instance.rename(name, new_name)
        print("The response of TokensApi->rename:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TokensApi->rename: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The API token&#39;s name. | 
 **new_name** | **str**| The new name for the API token.  **Note:**  The name may only contain alphanumeric characters, dashes (&#x60;-&#x60;), and underscores (&#x60;_&#x60;). | 

### Return type

[**InlineResponse200519**](InlineResponse200519.md)

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

# **revoke**
> InlineResponse200520 revoke(name)

Remove cPanel API token

This function removes an API token from a cPanel account.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200520 import InlineResponse200520
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
    api_instance = clientapi_cpanel.TokensApi(api_client)
    name = 'example' # str | The API token to remove.

    try:
        # Remove cPanel API token
        api_response = api_instance.revoke(name)
        print("The response of TokensApi->revoke:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TokensApi->revoke: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The API token to remove. | 

### Return type

[**InlineResponse200520**](InlineResponse200520.md)

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

# **tokens_list**
> InlineResponse200518 tokens_list()

Return cPanel API tokens

This function returns a list of a cPanel account's API tokens.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200518 import InlineResponse200518
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
    api_instance = clientapi_cpanel.TokensApi(api_client)

    try:
        # Return cPanel API tokens
        api_response = api_instance.tokens_list()
        print("The response of TokensApi->tokens_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TokensApi->tokens_list: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**InlineResponse200518**](InlineResponse200518.md)

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

