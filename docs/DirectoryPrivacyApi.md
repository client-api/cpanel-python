# clientapi_cpanel.DirectoryPrivacyApi

All URIs are relative to *https://cpanel-server.tld:2083/execute*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_user**](DirectoryPrivacyApi.md#add_user) | **GET** /DirectoryPrivacy/add_user | Add authorized user for protected directory
[**configure_directory_protection**](DirectoryPrivacyApi.md#configure_directory_protection) | **GET** /DirectoryPrivacy/configure_directory_protection | Enable or disable protected directory
[**delete_user**](DirectoryPrivacyApi.md#delete_user) | **GET** /DirectoryPrivacy/delete_user | Delete authorized user for protected directory
[**directory_privacy_list_directories**](DirectoryPrivacyApi.md#directory_privacy_list_directories) | **GET** /DirectoryPrivacy/list_directories | Return privacy status of subdirectories
[**directory_privacy_list_users**](DirectoryPrivacyApi.md#directory_privacy_list_users) | **GET** /DirectoryPrivacy/list_users | Return authorized users for protected directory
[**is_directory_protected**](DirectoryPrivacyApi.md#is_directory_protected) | **GET** /DirectoryPrivacy/is_directory_protected | Return whether directory uses password protection


# **add_user**
> InlineResponse200103 add_user(dir, password, user)

Add authorized user for protected directory

This function adds a user who can access a protected directory on the cPanel account.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200103 import InlineResponse200103
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
    api_instance = clientapi_cpanel.DirectoryPrivacyApi(api_client)
    dir = '/home/example/example.com' # str | The directory to add users to.
    password = '123456luggage' # str | The password for the user.
    user = 'example1' # str | The username of the user who can access the directory.

    try:
        # Add authorized user for protected directory
        api_response = api_instance.add_user(dir, password, user)
        print("The response of DirectoryPrivacyApi->add_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DirectoryPrivacyApi->add_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dir** | **str**| The directory to add users to. | 
 **password** | **str**| The password for the user. | 
 **user** | **str**| The username of the user who can access the directory. | 

### Return type

[**InlineResponse200103**](InlineResponse200103.md)

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

# **configure_directory_protection**
> InlineResponse200104 configure_directory_protection(authname, dir, enabled)

Enable or disable protected directory

This function enables or disables password protection for a directory on the cPanel account.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200104 import InlineResponse200104
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
    api_instance = clientapi_cpanel.DirectoryPrivacyApi(api_client)
    authname = 'protectandserve' # str | The name of the directory protection authorization instance.  **Note:**  **Only** use this parameter when you enable password protection.
    dir = '/home/example/example.com' # str | The absolute or relative directory path for which to enable or disable password protection.
    enabled = 1 # int | Whether to enable password protection for the directory. * `1` - Enable. * `0` - Disable.

    try:
        # Enable or disable protected directory
        api_response = api_instance.configure_directory_protection(authname, dir, enabled)
        print("The response of DirectoryPrivacyApi->configure_directory_protection:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DirectoryPrivacyApi->configure_directory_protection: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authname** | **str**| The name of the directory protection authorization instance.  **Note:**  **Only** use this parameter when you enable password protection. | 
 **dir** | **str**| The absolute or relative directory path for which to enable or disable password protection. | 
 **enabled** | **int**| Whether to enable password protection for the directory. * &#x60;1&#x60; - Enable. * &#x60;0&#x60; - Disable. | 

### Return type

[**InlineResponse200104**](InlineResponse200104.md)

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

# **delete_user**
> InlineResponse200105 delete_user(dir, user)

Delete authorized user for protected directory

This function deletes a user who can access a protected directory on the cPanel account.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200105 import InlineResponse200105
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
    api_instance = clientapi_cpanel.DirectoryPrivacyApi(api_client)
    dir = '/home/example/example.com' # str | The absolute directory path on the cPanel account from which to remove a user.
    user = 'example1' # str | The username to remove from the directory.

    try:
        # Delete authorized user for protected directory
        api_response = api_instance.delete_user(dir, user)
        print("The response of DirectoryPrivacyApi->delete_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DirectoryPrivacyApi->delete_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dir** | **str**| The absolute directory path on the cPanel account from which to remove a user. | 
 **user** | **str**| The username to remove from the directory. | 

### Return type

[**InlineResponse200105**](InlineResponse200105.md)

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

# **directory_privacy_list_directories**
> InlineResponse200107 directory_privacy_list_directories(dir)

Return privacy status of subdirectories

This function returns the privacy status of the subdirectories in a directory.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200107 import InlineResponse200107
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
    api_instance = clientapi_cpanel.DirectoryPrivacyApi(api_client)
    dir = '/home/example/example.com' # str | The directory path for which to return the subdirectories' privacy information.

    try:
        # Return privacy status of subdirectories
        api_response = api_instance.directory_privacy_list_directories(dir)
        print("The response of DirectoryPrivacyApi->directory_privacy_list_directories:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DirectoryPrivacyApi->directory_privacy_list_directories: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dir** | **str**| The directory path for which to return the subdirectories&#39; privacy information. | 

### Return type

[**InlineResponse200107**](InlineResponse200107.md)

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

# **directory_privacy_list_users**
> InlineResponse200108 directory_privacy_list_users(dir)

Return authorized users for protected directory

This function returns the users who can access a password-protected directory on the cPanel account.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200108 import InlineResponse200108
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
    api_instance = clientapi_cpanel.DirectoryPrivacyApi(api_client)
    dir = '/home/example/example.com' # str | The password-protected directory for which to return authorized users.

    try:
        # Return authorized users for protected directory
        api_response = api_instance.directory_privacy_list_users(dir)
        print("The response of DirectoryPrivacyApi->directory_privacy_list_users:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DirectoryPrivacyApi->directory_privacy_list_users: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dir** | **str**| The password-protected directory for which to return authorized users. | 

### Return type

[**InlineResponse200108**](InlineResponse200108.md)

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

# **is_directory_protected**
> InlineResponse200106 is_directory_protected(dir)

Return whether directory uses password protection

This function confirms whether a directory uses password protection.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200106 import InlineResponse200106
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
    api_instance = clientapi_cpanel.DirectoryPrivacyApi(api_client)
    dir = '/home/example/example.com' # str | The absolute directory path on the cPanel account to check for password protection.

    try:
        # Return whether directory uses password protection
        api_response = api_instance.is_directory_protected(dir)
        print("The response of DirectoryPrivacyApi->is_directory_protected:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DirectoryPrivacyApi->is_directory_protected: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dir** | **str**| The absolute directory path on the cPanel account to check for password protection. | 

### Return type

[**InlineResponse200106**](InlineResponse200106.md)

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

