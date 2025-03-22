# clientapi_cpanel.WebDiskApi

All URIs are relative to *https://cpanel-server.tld:2083/execute*

Method | HTTP request | Description
------------- | ------------- | -------------
[**set_permissions**](WebDiskApi.md#set_permissions) | **GET** /WebDisk/set_permissions | Update Web Disk home directory permissions
[**web_disk_delete_user**](WebDiskApi.md#web_disk_delete_user) | **GET** /WebDisk/delete_user | Delete Web Disk account
[**web_disk_set_homedir**](WebDiskApi.md#web_disk_set_homedir) | **GET** /WebDisk/set_homedir | Update Web Disk home directory location
[**web_disk_set_password**](WebDiskApi.md#web_disk_set_password) | **GET** /WebDisk/set_password | Update Web Disk account password


# **set_permissions**
> InlineResponse200552 set_permissions(perms, user)

Update Web Disk home directory permissions

This function changes the Web Disk home directory's permissions.

**Important:**

When you disable the [Web Disk role](https://go.cpanel.net/serverroles), the system **disables** this function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200552 import InlineResponse200552
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
    api_instance = clientapi_cpanel.WebDiskApi(api_client)
    perms = 'rw' # str | The Web Disk account's home directory file permissions.  * `ro` — Read-only permissions. * `rw` — Read and write permissions.
    user = 'example1@example.com' # str | The Web Disk account's username.

    try:
        # Update Web Disk home directory permissions
        api_response = api_instance.set_permissions(perms, user)
        print("The response of WebDiskApi->set_permissions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebDiskApi->set_permissions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **perms** | **str**| The Web Disk account&#39;s home directory file permissions.  * &#x60;ro&#x60; — Read-only permissions. * &#x60;rw&#x60; — Read and write permissions. | 
 **user** | **str**| The Web Disk account&#39;s username. | 

### Return type

[**InlineResponse200552**](InlineResponse200552.md)

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

# **web_disk_delete_user**
> InlineResponse200549 web_disk_delete_user(destroy, user)

Delete Web Disk account

This function deletes a Web Disk account.

**Important:**

When you disable the [Web Disk role](https://go.cpanel.net/serverroles), the system **disables** this function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200549 import InlineResponse200549
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
    api_instance = clientapi_cpanel.WebDiskApi(api_client)
    destroy = 1 # int | Whether to recursively delete the Web Disk account's folder and all of its contents.  * `1` - Delete the folder for the Web Disk account * `0` - Do **not** delete the folder for the Web Disk account.
    user = 'example1@example.com' # str | The Web Disk account username.

    try:
        # Delete Web Disk account
        api_response = api_instance.web_disk_delete_user(destroy, user)
        print("The response of WebDiskApi->web_disk_delete_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebDiskApi->web_disk_delete_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **destroy** | **int**| Whether to recursively delete the Web Disk account&#39;s folder and all of its contents.  * &#x60;1&#x60; - Delete the folder for the Web Disk account * &#x60;0&#x60; - Do **not** delete the folder for the Web Disk account. | 
 **user** | **str**| The Web Disk account username. | 

### Return type

[**InlineResponse200549**](InlineResponse200549.md)

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

# **web_disk_set_homedir**
> InlineResponse200550 web_disk_set_homedir(homedir, user, private=private)

Update Web Disk home directory location

This function changes the home directory for a Web Disk account.

**Important:**

When you disable the [Web Disk role](https://go.cpanel.net/serveroles), the system **disables** this function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200550 import InlineResponse200550
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
    api_instance = clientapi_cpanel.WebDiskApi(api_client)
    homedir = 'example1/' # str | The Web Disk account's home directory.
    user = 'example1@example.com' # str | The Web Disk account username.
    private = 0 # int | Whether to set the Web Disk directory's permissions to public or private.  * `1` - Private (`0700`) * `0` - Public (`0755`) (optional) (default to 0)

    try:
        # Update Web Disk home directory location
        api_response = api_instance.web_disk_set_homedir(homedir, user, private=private)
        print("The response of WebDiskApi->web_disk_set_homedir:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebDiskApi->web_disk_set_homedir: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **homedir** | **str**| The Web Disk account&#39;s home directory. | 
 **user** | **str**| The Web Disk account username. | 
 **private** | **int**| Whether to set the Web Disk directory&#39;s permissions to public or private.  * &#x60;1&#x60; - Private (&#x60;0700&#x60;) * &#x60;0&#x60; - Public (&#x60;0755&#x60;) | [optional] [default to 0]

### Return type

[**InlineResponse200550**](InlineResponse200550.md)

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

# **web_disk_set_password**
> InlineResponse200551 web_disk_set_password(password, user, enabledigest=enabledigest)

Update Web Disk account password

This function changes the Web Disk account's password.

**Important:**

When you disable the [Web Disk role](https://go.cpanel.net/serverroles), the system **disables** this function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200551 import InlineResponse200551
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
    api_instance = clientapi_cpanel.WebDiskApi(api_client)
    password = '123456luggage' # str | The Web Disk account's password.
    user = 'example1@example.com' # str | The Web Disk account username.
    enabledigest = 0 # int | Whether to enable Digest Authentication.  * `1` - Enable Digest Authentication. * `0` - Disable Digest Authentication. (optional) (default to 0)

    try:
        # Update Web Disk account password
        api_response = api_instance.web_disk_set_password(password, user, enabledigest=enabledigest)
        print("The response of WebDiskApi->web_disk_set_password:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebDiskApi->web_disk_set_password: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **password** | **str**| The Web Disk account&#39;s password. | 
 **user** | **str**| The Web Disk account username. | 
 **enabledigest** | **int**| Whether to enable Digest Authentication.  * &#x60;1&#x60; - Enable Digest Authentication. * &#x60;0&#x60; - Disable Digest Authentication. | [optional] [default to 0]

### Return type

[**InlineResponse200551**](InlineResponse200551.md)

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

