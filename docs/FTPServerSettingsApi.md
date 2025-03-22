# clientapi_cpanel.FTPServerSettingsApi

All URIs are relative to *https://cpanel-server.tld:2083/execute*

Method | HTTP request | Description
------------- | ------------- | -------------
[**allows_anonymous_ftp**](FTPServerSettingsApi.md#allows_anonymous_ftp) | **GET** /Ftp/allows_anonymous_ftp | Return if anonymous FTP connections allowed
[**allows_anonymous_ftp_incoming**](FTPServerSettingsApi.md#allows_anonymous_ftp_incoming) | **GET** /Ftp/allows_anonymous_ftp_incoming | Return if anonymous FTP transfers allowed
[**get_ftp_daemon_info**](FTPServerSettingsApi.md#get_ftp_daemon_info) | **GET** /Ftp/get_ftp_daemon_info | Return FTP server&#39;s information
[**get_port**](FTPServerSettingsApi.md#get_port) | **GET** /Ftp/get_port | Return FTP server&#39;s port
[**kill_session**](FTPServerSettingsApi.md#kill_session) | **GET** /Ftp/kill_session | Stop FTP session
[**list_sessions**](FTPServerSettingsApi.md#list_sessions) | **GET** /Ftp/list_sessions | Return FTP server&#39;s active sessions
[**server_name**](FTPServerSettingsApi.md#server_name) | **GET** /Ftp/server_name | Return whether server uses ProFTPD or Pure-FTPd
[**set_anonymous_ftp**](FTPServerSettingsApi.md#set_anonymous_ftp) | **GET** /Ftp/set_anonymous_ftp | Enable or disable anonymous FTP logins
[**set_anonymous_ftp_incoming**](FTPServerSettingsApi.md#set_anonymous_ftp_incoming) | **GET** /Ftp/set_anonymous_ftp_incoming | Enable or disable anonymous incoming FTP transfers


# **allows_anonymous_ftp**
> InlineResponse200244 allows_anonymous_ftp()

Return if anonymous FTP connections allowed

This function checks whether the account allows anonymous FTP connections.

**Important:**

When you disable the [*FTP* role](https://go.cpanel.net/serverroles), the system **disables** this function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200244 import InlineResponse200244
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
    api_instance = clientapi_cpanel.FTPServerSettingsApi(api_client)

    try:
        # Return if anonymous FTP connections allowed
        api_response = api_instance.allows_anonymous_ftp()
        print("The response of FTPServerSettingsApi->allows_anonymous_ftp:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FTPServerSettingsApi->allows_anonymous_ftp: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**InlineResponse200244**](InlineResponse200244.md)

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

# **allows_anonymous_ftp_incoming**
> InlineResponse200245 allows_anonymous_ftp_incoming()

Return if anonymous FTP transfers allowed

This function checks whether the account allows inbound anonymous FTP transfers.

**Important:**

  When you disable the [*FTP* role](https://go.cpanel.net/howtouseserverprofiles#roles), the system **disables** this function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200245 import InlineResponse200245
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
    api_instance = clientapi_cpanel.FTPServerSettingsApi(api_client)

    try:
        # Return if anonymous FTP transfers allowed
        api_response = api_instance.allows_anonymous_ftp_incoming()
        print("The response of FTPServerSettingsApi->allows_anonymous_ftp_incoming:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FTPServerSettingsApi->allows_anonymous_ftp_incoming: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**InlineResponse200245**](InlineResponse200245.md)

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

# **get_ftp_daemon_info**
> InlineResponse200248 get_ftp_daemon_info()

Return FTP server's information

This function retrieves the extended information about the server's FTP daemon.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200248 import InlineResponse200248
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
    api_instance = clientapi_cpanel.FTPServerSettingsApi(api_client)

    try:
        # Return FTP server's information
        api_response = api_instance.get_ftp_daemon_info()
        print("The response of FTPServerSettingsApi->get_ftp_daemon_info:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FTPServerSettingsApi->get_ftp_daemon_info: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**InlineResponse200248**](InlineResponse200248.md)

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

# **get_port**
> InlineResponse200249 get_port()

Return FTP server's port

This function returns the FTP port.

**Important:**

  When you disable the [*FTP* role](https://go.cpanel.net/serverroles), the system **disables** this function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200249 import InlineResponse200249
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
    api_instance = clientapi_cpanel.FTPServerSettingsApi(api_client)

    try:
        # Return FTP server's port
        api_response = api_instance.get_port()
        print("The response of FTPServerSettingsApi->get_port:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FTPServerSettingsApi->get_port: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**InlineResponse200249**](InlineResponse200249.md)

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

# **kill_session**
> InlineResponse200252 kill_session(login=login)

Stop FTP session

This function kills FTP sessions.

**Important:**

  When you disable the [*FTP* Role](https://go.cpanel.net/serverroles), the system **disables** this function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200252 import InlineResponse200252
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
    api_instance = clientapi_cpanel.FTPServerSettingsApi(api_client)
    login = 'all' # str | The username for the session's FTP account.  **Note:**    To stop all FTP sessions for the cPanel account, set this parameter to the `all` value. (optional) (default to 'all')

    try:
        # Stop FTP session
        api_response = api_instance.kill_session(login=login)
        print("The response of FTPServerSettingsApi->kill_session:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FTPServerSettingsApi->kill_session: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **login** | **str**| The username for the session&#39;s FTP account.  **Note:**    To stop all FTP sessions for the cPanel account, set this parameter to the &#x60;all&#x60; value. | [optional] [default to &#39;all&#39;]

### Return type

[**InlineResponse200252**](InlineResponse200252.md)

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

# **list_sessions**
> InlineResponse200255 list_sessions()

Return FTP server's active sessions

This function lists the FTP server's active sessions.

**Important:**

  When you disable the [FTP role](https://go.cpanel.net/serverroles), the system **disables** this function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200255 import InlineResponse200255
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
    api_instance = clientapi_cpanel.FTPServerSettingsApi(api_client)

    try:
        # Return FTP server's active sessions
        api_response = api_instance.list_sessions()
        print("The response of FTPServerSettingsApi->list_sessions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FTPServerSettingsApi->list_sessions: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**InlineResponse200255**](InlineResponse200255.md)

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

# **server_name**
> InlineResponse200257 server_name()

Return whether server uses ProFTPD or Pure-FTPd

This function checks whether the server uses ProFTPD or Pure-FTPd.

**Important:**

When you disable the [FTP role](https://go.cpanel.net/serverroles), the system **disables** this function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200257 import InlineResponse200257
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
    api_instance = clientapi_cpanel.FTPServerSettingsApi(api_client)

    try:
        # Return whether server uses ProFTPD or Pure-FTPd
        api_response = api_instance.server_name()
        print("The response of FTPServerSettingsApi->server_name:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FTPServerSettingsApi->server_name: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**InlineResponse200257**](InlineResponse200257.md)

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

# **set_anonymous_ftp**
> InlineResponse200258 set_anonymous_ftp(set=set)

Enable or disable anonymous FTP logins

This function enables or disables anonymous FTP logins.

**Important:**

When you disable the [FTP role](https://go.cpanel.net/serverroles), the system **disables** this function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200258 import InlineResponse200258
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
    api_instance = clientapi_cpanel.FTPServerSettingsApi(api_client)
    set = 0 # int | Whether to enable or disable anonymous FTP logins.  * `1` - Enable. * `0` - Disable. (optional) (default to 0)

    try:
        # Enable or disable anonymous FTP logins
        api_response = api_instance.set_anonymous_ftp(set=set)
        print("The response of FTPServerSettingsApi->set_anonymous_ftp:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FTPServerSettingsApi->set_anonymous_ftp: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **set** | **int**| Whether to enable or disable anonymous FTP logins.  * &#x60;1&#x60; - Enable. * &#x60;0&#x60; - Disable. | [optional] [default to 0]

### Return type

[**InlineResponse200258**](InlineResponse200258.md)

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

# **set_anonymous_ftp_incoming**
> InlineResponse200259 set_anonymous_ftp_incoming(set=set)

Enable or disable anonymous incoming FTP transfers

This function enables or disables inbound anonymous FTP transfers.

**Important:**

When you disable the [FTP role](https://go.cpanel.net/serverroles), the system **disables** this function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200259 import InlineResponse200259
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
    api_instance = clientapi_cpanel.FTPServerSettingsApi(api_client)
    set = 0 # int | Whether to enable or disable inbound anonymous FTP transfers.  * `1` - Enable. * `0` - Disable. (optional) (default to 0)

    try:
        # Enable or disable anonymous incoming FTP transfers
        api_response = api_instance.set_anonymous_ftp_incoming(set=set)
        print("The response of FTPServerSettingsApi->set_anonymous_ftp_incoming:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FTPServerSettingsApi->set_anonymous_ftp_incoming: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **set** | **int**| Whether to enable or disable inbound anonymous FTP transfers.  * &#x60;1&#x60; - Enable. * &#x60;0&#x60; - Disable. | [optional] [default to 0]

### Return type

[**InlineResponse200259**](InlineResponse200259.md)

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

