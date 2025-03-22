# clientapi_cpanel.FTPAccountsApi

All URIs are relative to *https://cpanel-server.tld:2083/execute*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_ftp**](FTPAccountsApi.md#add_ftp) | **GET** /Ftp/add_ftp | Create FTP account
[**delete_ftp**](FTPAccountsApi.md#delete_ftp) | **GET** /Ftp/delete_ftp | Delete FTP account
[**ftp_exists**](FTPAccountsApi.md#ftp_exists) | **GET** /Ftp/ftp_exists | Return whether an FTP account exists
[**get_quota**](FTPAccountsApi.md#get_quota) | **GET** /Ftp/get_quota | Return FTP account&#39;s quota
[**get_welcome_message**](FTPAccountsApi.md#get_welcome_message) | **GET** /Ftp/get_welcome_message | Return FTP account&#39;s welcome message
[**list_ftp**](FTPAccountsApi.md#list_ftp) | **GET** /Ftp/list_ftp | Return FTP accounts
[**list_ftp_with_disk**](FTPAccountsApi.md#list_ftp_with_disk) | **GET** /Ftp/list_ftp_with_disk | Return FTP accounts and disk usage
[**passwd**](FTPAccountsApi.md#passwd) | **GET** /Ftp/passwd | Update FTP account&#39;s password
[**set_homedir**](FTPAccountsApi.md#set_homedir) | **GET** /Ftp/set_homedir | Update FTP account&#39;s home directory
[**set_quota**](FTPAccountsApi.md#set_quota) | **GET** /Ftp/set_quota | Update FTP account&#39;s quota
[**set_welcome_message**](FTPAccountsApi.md#set_welcome_message) | **GET** /Ftp/set_welcome_message | Update FTP welcome message


# **add_ftp**
> InlineResponse200243 add_ftp(user, disallowdot=disallowdot, domain=domain, homedir=homedir, var_pass=var_pass, pass_hash=pass_hash, quota=quota)

Create FTP account

This function creates an FTP account.

**Important:**

When you disable the [FTP role](https://go.cpanel.net/serverroles), the system **disables** this function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200243 import InlineResponse200243
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
    api_instance = clientapi_cpanel.FTPAccountsApi(api_client)
    user = 'username' # str | The new FTP account username.
    disallowdot = 1 # int | Whether to strip dots (`.`) from the username.  * `1` — Strip dots. * `0` — Do **not** strip dots. (optional) (default to 1)
    domain = 'example.com' # str | The FTP user's associated domain. This must be a domain that the cPanel account owns.  **Note:**  This parameter defaults to the cPanel account's primary domain. (optional)
    homedir = 'exampleftp' # str | The path to the FTP account's root directory, relative to the cPanel account's home directory. If you don't set this, it defaults to a directory with the same name as the FTP account. (optional)
    var_pass = '123456luggage' # str | The new FTP account password.  **Note:**  You can use the `pass_hash` parameter in place of this parameter. However, you **cannot** use both the `pass` and `pass_hash` parameters in the same request. (optional)
    pass_hash = '' # str | The account's password hash.  **Note:**  * You can use this parameter in place of the `pass` parameter. However, you **cannot** use both the `pass` and `pass_hash` parameters in the same request. * You can find your server's password hash type in the `/etc/sysconfig/authconfig` file. (optional) (default to '')
    quota = 0 # int | The FTP account's maximum disk usage quota, in megabytes (MB).  **Note:**  A value of `0` grants the FTP account unlimited disk space. (optional) (default to 0)

    try:
        # Create FTP account
        api_response = api_instance.add_ftp(user, disallowdot=disallowdot, domain=domain, homedir=homedir, var_pass=var_pass, pass_hash=pass_hash, quota=quota)
        print("The response of FTPAccountsApi->add_ftp:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FTPAccountsApi->add_ftp: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | **str**| The new FTP account username. | 
 **disallowdot** | **int**| Whether to strip dots (&#x60;.&#x60;) from the username.  * &#x60;1&#x60; — Strip dots. * &#x60;0&#x60; — Do **not** strip dots. | [optional] [default to 1]
 **domain** | **str**| The FTP user&#39;s associated domain. This must be a domain that the cPanel account owns.  **Note:**  This parameter defaults to the cPanel account&#39;s primary domain. | [optional] 
 **homedir** | **str**| The path to the FTP account&#39;s root directory, relative to the cPanel account&#39;s home directory. If you don&#39;t set this, it defaults to a directory with the same name as the FTP account. | [optional] 
 **var_pass** | **str**| The new FTP account password.  **Note:**  You can use the &#x60;pass_hash&#x60; parameter in place of this parameter. However, you **cannot** use both the &#x60;pass&#x60; and &#x60;pass_hash&#x60; parameters in the same request. | [optional] 
 **pass_hash** | **str**| The account&#39;s password hash.  **Note:**  * You can use this parameter in place of the &#x60;pass&#x60; parameter. However, you **cannot** use both the &#x60;pass&#x60; and &#x60;pass_hash&#x60; parameters in the same request. * You can find your server&#39;s password hash type in the &#x60;/etc/sysconfig/authconfig&#x60; file. | [optional] [default to &#39;&#39;]
 **quota** | **int**| The FTP account&#39;s maximum disk usage quota, in megabytes (MB).  **Note:**  A value of &#x60;0&#x60; grants the FTP account unlimited disk space. | [optional] [default to 0]

### Return type

[**InlineResponse200243**](InlineResponse200243.md)

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

# **delete_ftp**
> InlineResponse200246 delete_ftp(user, destroy=destroy, domain=domain)

Delete FTP account

This function deletes an FTP account.

**Important:**

When you disable the [*FTP* role](https://go.cpanel.net/serverroles), the system **disables** this function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200246 import InlineResponse200246
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
    api_instance = clientapi_cpanel.FTPAccountsApi(api_client)
    user = 'username' # str | The FTP account's username.
    destroy = 0 # int | Whether to delete the FTP account's home directory.  * `1` — Delete the home directory. * `0` — Do **not** delete the home directory. (optional) (default to 0)
    domain = 'example.com' # str | The user's associated domain.  **Note:**  This parameter defaults to the cPanel account's primary domain. (optional)

    try:
        # Delete FTP account
        api_response = api_instance.delete_ftp(user, destroy=destroy, domain=domain)
        print("The response of FTPAccountsApi->delete_ftp:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FTPAccountsApi->delete_ftp: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | **str**| The FTP account&#39;s username. | 
 **destroy** | **int**| Whether to delete the FTP account&#39;s home directory.  * &#x60;1&#x60; — Delete the home directory. * &#x60;0&#x60; — Do **not** delete the home directory. | [optional] [default to 0]
 **domain** | **str**| The user&#39;s associated domain.  **Note:**  This parameter defaults to the cPanel account&#39;s primary domain. | [optional] 

### Return type

[**InlineResponse200246**](InlineResponse200246.md)

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

# **ftp_exists**
> InlineResponse200247 ftp_exists(user, domain=domain)

Return whether an FTP account exists

This function checks whether an FTP account exists.

**Note:**

This function returns only metadata if the FTP account exists, or an error if the FTP account does **not** exist.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200247 import InlineResponse200247
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
    api_instance = clientapi_cpanel.FTPAccountsApi(api_client)
    user = 'us_chickens' # str | The FTP account's username.
    domain = 'example.com' # str | The user's associated domain.  **Note:**  This parameter defaults to the cPanel account's primary domain. (optional)

    try:
        # Return whether an FTP account exists
        api_response = api_instance.ftp_exists(user, domain=domain)
        print("The response of FTPAccountsApi->ftp_exists:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FTPAccountsApi->ftp_exists: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | **str**| The FTP account&#39;s username. | 
 **domain** | **str**| The user&#39;s associated domain.  **Note:**  This parameter defaults to the cPanel account&#39;s primary domain. | [optional] 

### Return type

[**InlineResponse200247**](InlineResponse200247.md)

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

# **get_quota**
> InlineResponse200250 get_quota(account, domain=domain)

Return FTP account's quota

This function checks an FTP account's quota.

**Important:**

  When you disable the [_FTP role_](https://go.cpanel.net/serverroles), the system **disables** this function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200250 import InlineResponse200250
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
    api_instance = clientapi_cpanel.FTPAccountsApi(api_client)
    account = 'user1' # str | The FTP account's username.
    domain = 'example.com' # str | The user's associated domain.  **Note:**  This parameter defaults to the cPanel account's primary domain. (optional)

    try:
        # Return FTP account's quota
        api_response = api_instance.get_quota(account, domain=domain)
        print("The response of FTPAccountsApi->get_quota:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FTPAccountsApi->get_quota: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account** | **str**| The FTP account&#39;s username. | 
 **domain** | **str**| The user&#39;s associated domain.  **Note:**  This parameter defaults to the cPanel account&#39;s primary domain. | [optional] 

### Return type

[**InlineResponse200250**](InlineResponse200250.md)

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

# **get_welcome_message**
> InlineResponse200251 get_welcome_message()

Return FTP account's welcome message

This function retrieves the cPanel account's FTP welcome message.

**Important:**

  When you disable the [*FTP* role](https://go.cpanel.net/serverroles), the system **disables** this function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200251 import InlineResponse200251
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
    api_instance = clientapi_cpanel.FTPAccountsApi(api_client)

    try:
        # Return FTP account's welcome message
        api_response = api_instance.get_welcome_message()
        print("The response of FTPAccountsApi->get_welcome_message:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FTPAccountsApi->get_welcome_message: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**InlineResponse200251**](InlineResponse200251.md)

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

# **list_ftp**
> InlineResponse200253 list_ftp(include_acct_types=include_acct_types, skip_acct_types=skip_acct_types)

Return FTP accounts

This function lists FTP account information.

**Important:**

When you disable the [*FTP* role](https://go.cpanel.net/howtouseserverprofiles#roles), the system **disables** this function. For more information, read our How to Use Server Profiles documentation.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200253 import InlineResponse200253
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
    api_instance = clientapi_cpanel.FTPAccountsApi(api_client)
    include_acct_types = 'main|anonymous' # str | A list of the FTP account types to include in the function's results.  * `anonymous` * `logaccess` * `main` * `sub`  If you do not specify this parameter, this function returns all FTP account types.  **Note:**  * Separate multiple types with the pipe character (`|`). * In browser-based calls, use `%7C`. (optional)
    skip_acct_types = 'main|anonymous' # str | A list of the FTP account types to exclude from the function's results.  * `anonymous` * `logaccess` * `main` * `sub`  If you do not specify this parameter, this function does **not** exclude any account types.  **Note:**  * Separate multiple types with the pipe character (`|`). * In browser-based calls, use `%7C`. (optional)

    try:
        # Return FTP accounts
        api_response = api_instance.list_ftp(include_acct_types=include_acct_types, skip_acct_types=skip_acct_types)
        print("The response of FTPAccountsApi->list_ftp:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FTPAccountsApi->list_ftp: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **include_acct_types** | **str**| A list of the FTP account types to include in the function&#39;s results.  * &#x60;anonymous&#x60; * &#x60;logaccess&#x60; * &#x60;main&#x60; * &#x60;sub&#x60;  If you do not specify this parameter, this function returns all FTP account types.  **Note:**  * Separate multiple types with the pipe character (&#x60;|&#x60;). * In browser-based calls, use &#x60;%7C&#x60;. | [optional] 
 **skip_acct_types** | **str**| A list of the FTP account types to exclude from the function&#39;s results.  * &#x60;anonymous&#x60; * &#x60;logaccess&#x60; * &#x60;main&#x60; * &#x60;sub&#x60;  If you do not specify this parameter, this function does **not** exclude any account types.  **Note:**  * Separate multiple types with the pipe character (&#x60;|&#x60;). * In browser-based calls, use &#x60;%7C&#x60;. | [optional] 

### Return type

[**InlineResponse200253**](InlineResponse200253.md)

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

# **list_ftp_with_disk**
> InlineResponse200254 list_ftp_with_disk(include_acct_types=include_acct_types, skip_acct_types=skip_acct_types)

Return FTP accounts and disk usage

This function lists FTP account and disk usage information.

**Important:**

When you disable the [FTP role](https://go.cpanel.net/serverroles), the system **disables** this function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200254 import InlineResponse200254
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
    api_instance = clientapi_cpanel.FTPAccountsApi(api_client)
    include_acct_types = 'main|anonymous' # str | A pipe-delimited list of the FTP account types to include in the function's results. If you do not specify this parameter, the function returns all FTP account types.  Valid types for this list are:  * `anonymous` * `logaccess` * `main` * `sub` (optional)
    skip_acct_types = 'main|anonymous' # str | A pipe-delimited list of the FTP account types to exclude from the function's results. If you do not specify this parameter, the function does **not** exclude any account types.  Valid types for this list are:  * `anonymous` * `logaccess` * `main` * `sub` (optional)

    try:
        # Return FTP accounts and disk usage
        api_response = api_instance.list_ftp_with_disk(include_acct_types=include_acct_types, skip_acct_types=skip_acct_types)
        print("The response of FTPAccountsApi->list_ftp_with_disk:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FTPAccountsApi->list_ftp_with_disk: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **include_acct_types** | **str**| A pipe-delimited list of the FTP account types to include in the function&#39;s results. If you do not specify this parameter, the function returns all FTP account types.  Valid types for this list are:  * &#x60;anonymous&#x60; * &#x60;logaccess&#x60; * &#x60;main&#x60; * &#x60;sub&#x60; | [optional] 
 **skip_acct_types** | **str**| A pipe-delimited list of the FTP account types to exclude from the function&#39;s results. If you do not specify this parameter, the function does **not** exclude any account types.  Valid types for this list are:  * &#x60;anonymous&#x60; * &#x60;logaccess&#x60; * &#x60;main&#x60; * &#x60;sub&#x60; | [optional] 

### Return type

[**InlineResponse200254**](InlineResponse200254.md)

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

# **passwd**
> InlineResponse200256 passwd(var_pass, user, domain=domain)

Update FTP account's password

This function changes an FTP account's password.

**Important:**

When you disable the [FTP role](https://go.cpanel.net/serverroles), the system **disables** this function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200256 import InlineResponse200256
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
    api_instance = clientapi_cpanel.FTPAccountsApi(api_client)
    var_pass = '12345luggage' # str | The FTP account's new password.
    user = 'ftpaccount' # str | The FTP account username.
    domain = 'example.com' # str | The user's associated domain.  **Note:**  This parameter defaults to the cPanel account's primary domain (optional)

    try:
        # Update FTP account's password
        api_response = api_instance.passwd(var_pass, user, domain=domain)
        print("The response of FTPAccountsApi->passwd:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FTPAccountsApi->passwd: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **var_pass** | **str**| The FTP account&#39;s new password. | 
 **user** | **str**| The FTP account username. | 
 **domain** | **str**| The user&#39;s associated domain.  **Note:**  This parameter defaults to the cPanel account&#39;s primary domain | [optional] 

### Return type

[**InlineResponse200256**](InlineResponse200256.md)

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

# **set_homedir**
> InlineResponse200260 set_homedir(user, domain=domain, homedir=homedir)

Update FTP account's home directory

This function changes the home directory for FTP accounts.

**Important:**

When you disable the [FTP role](https://go.cpanel.net/serverroles), the system **disables** this function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200260 import InlineResponse200260
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
    api_instance = clientapi_cpanel.FTPAccountsApi(api_client)
    user = 'example1' # str | The FTP account username.
    domain = 'example.com' # str | The user's associated domain.  **Note:**  The default value is the cPanel account's primary domain. (optional)
    homedir = 'user@domain/' # str | The FTP account's home directory  **Note:**  This parameter defaults to the `user@domain` subdirectory in the cPanel account's home directory with the name, where user and domain represent the `user` and `domain` parameters. (optional) (default to 'user@domain/')

    try:
        # Update FTP account's home directory
        api_response = api_instance.set_homedir(user, domain=domain, homedir=homedir)
        print("The response of FTPAccountsApi->set_homedir:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FTPAccountsApi->set_homedir: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | **str**| The FTP account username. | 
 **domain** | **str**| The user&#39;s associated domain.  **Note:**  The default value is the cPanel account&#39;s primary domain. | [optional] 
 **homedir** | **str**| The FTP account&#39;s home directory  **Note:**  This parameter defaults to the &#x60;user@domain&#x60; subdirectory in the cPanel account&#39;s home directory with the name, where user and domain represent the &#x60;user&#x60; and &#x60;domain&#x60; parameters. | [optional] [default to &#39;user@domain/&#39;]

### Return type

[**InlineResponse200260**](InlineResponse200260.md)

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

# **set_quota**
> InlineResponse200261 set_quota(user, domain=domain, kill=kill, quota=quota)

Update FTP account's quota

This function changes an FTP account's quota.

**Important:**

When you disable the [FTP role](https://go.cpanel.net/serverroles), the system **disables** this function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200261 import InlineResponse200261
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
    api_instance = clientapi_cpanel.FTPAccountsApi(api_client)
    user = 'ftpaccount' # str | The FTP account username.
    domain = 'example.com' # str | The user's associated domain.  **Note:**  The default value is the cPanel account's primary domain. (optional)
    kill = 0 # int | Whether to disable quotas for the FTP account. * `1` - Disable quotas. * `0` - Enable quotas.  **Note:**   If you disable quotas for an FTP account, you grant that account unlimited disk space. (optional) (default to 0)
    quota = 0 # int | The new quota, in megabytes.  **Note:**  Setting this parameter to `0` grants the account unlimited disk space. (optional) (default to 0)

    try:
        # Update FTP account's quota
        api_response = api_instance.set_quota(user, domain=domain, kill=kill, quota=quota)
        print("The response of FTPAccountsApi->set_quota:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FTPAccountsApi->set_quota: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | **str**| The FTP account username. | 
 **domain** | **str**| The user&#39;s associated domain.  **Note:**  The default value is the cPanel account&#39;s primary domain. | [optional] 
 **kill** | **int**| Whether to disable quotas for the FTP account. * &#x60;1&#x60; - Disable quotas. * &#x60;0&#x60; - Enable quotas.  **Note:**   If you disable quotas for an FTP account, you grant that account unlimited disk space. | [optional] [default to 0]
 **quota** | **int**| The new quota, in megabytes.  **Note:**  Setting this parameter to &#x60;0&#x60; grants the account unlimited disk space. | [optional] [default to 0]

### Return type

[**InlineResponse200261**](InlineResponse200261.md)

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

# **set_welcome_message**
> InlineResponse200262 set_welcome_message(message)

Update FTP welcome message

This function sets the FTP welcome message.

**Important:**

When you disable the [FTP role](https://go.cpanel.net/serverroles), the system **disables** this function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200262 import InlineResponse200262
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
    api_instance = clientapi_cpanel.FTPAccountsApi(api_client)
    message = 'Greetings, Professor Falken.' # str | The cPanel account's new FTP welcome message.

    try:
        # Update FTP welcome message
        api_response = api_instance.set_welcome_message(message)
        print("The response of FTPAccountsApi->set_welcome_message:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FTPAccountsApi->set_welcome_message: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **message** | **str**| The cPanel account&#39;s new FTP welcome message. | 

### Return type

[**InlineResponse200262**](InlineResponse200262.md)

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

