# clientapi_cpanel.MailingListsApi

All URIs are relative to *https://cpanel-server.tld:2083/execute*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_list**](MailingListsApi.md#add_list) | **GET** /Email/add_list | Create mailing list
[**add_mailman_delegates**](MailingListsApi.md#add_mailman_delegates) | **GET** /Email/add_mailman_delegates | Add administrators to mailing list
[**count_lists**](MailingListsApi.md#count_lists) | **GET** /Email/count_lists | Return cPanel account&#39;s mailing list total
[**delete_list**](MailingListsApi.md#delete_list) | **GET** /Email/delete_list | Delete mailing list
[**export_lists**](MailingListsApi.md#export_lists) | **GET** /Email/export_lists | Export cPanel account&#39;s Mailman mailing lists to a file
[**generate_mailman_otp**](MailingListsApi.md#generate_mailman_otp) | **GET** /Email/generate_mailman_otp | Create one-time password for a mailing list
[**get_lists_total_disk_usage**](MailingListsApi.md#get_lists_total_disk_usage) | **GET** /Email/get_lists_total_disk_usage | Return cPanel account&#39;s mailing list disk usage
[**get_mailman_delegates**](MailingListsApi.md#get_mailman_delegates) | **GET** /Email/get_mailman_delegates | Return mailing list administrators
[**has_delegated_mailman_lists**](MailingListsApi.md#has_delegated_mailman_lists) | **GET** /Email/has_delegated_mailman_lists | Return email account&#39;s mailing list privileges
[**list_lists**](MailingListsApi.md#list_lists) | **GET** /Email/list_lists | Return cPanel account&#39;s mailing lists
[**passwd_list**](MailingListsApi.md#passwd_list) | **GET** /Email/passwd_list | Update mailing list password
[**remove_mailman_delegates**](MailingListsApi.md#remove_mailman_delegates) | **GET** /Email/remove_mailman_delegates | Remove account mailing list admin privileges
[**set_list_privacy_options**](MailingListsApi.md#set_list_privacy_options) | **GET** /Email/set_list_privacy_options | Update mailing list privacy options


# **add_list**
> InlineResponse200123 add_list(domain, list, password, private=private, rebuildonly=rebuildonly)

Create mailing list

This function creates a Mailman mailing list.

**Important:**

  When you disable the [*Receive Mail* role](https://go.cpanel.net/serverroles), the system **disables** this function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200123 import InlineResponse200123
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
    api_instance = clientapi_cpanel.MailingListsApi(api_client)
    domain = 'example.com' # str | The domain.
    list = 'newlist' # str | The mailing list name.
    password = '12345luggage' # str | The mailing list password.
    private = 0 # int | Whether the mailing list is private. * `1` — Private. * `0` — Public. (optional) (default to 0)
    rebuildonly = 0 # int | Whether to rebuild the mailing list. * `1` — Rebuild the mailing list. * `0` — Do **not** rebuild the mailing list. (optional) (default to 0)

    try:
        # Create mailing list
        api_response = api_instance.add_list(domain, list, password, private=private, rebuildonly=rebuildonly)
        print("The response of MailingListsApi->add_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MailingListsApi->add_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**| The domain. | 
 **list** | **str**| The mailing list name. | 
 **password** | **str**| The mailing list password. | 
 **private** | **int**| Whether the mailing list is private. * &#x60;1&#x60; — Private. * &#x60;0&#x60; — Public. | [optional] [default to 0]
 **rebuildonly** | **int**| Whether to rebuild the mailing list. * &#x60;1&#x60; — Rebuild the mailing list. * &#x60;0&#x60; — Do **not** rebuild the mailing list. | [optional] [default to 0]

### Return type

[**InlineResponse200123**](InlineResponse200123.md)

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

# **add_mailman_delegates**
> InlineResponse200124 add_mailman_delegates(delegates, list)

Add administrators to mailing list

This function grants mailing list administrative privileges to users.

**Important:**

  When you disable the [*Receive Mail* role](https://go.cpanel.net/serverroles), the system **disables** this function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200124 import InlineResponse200124
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
    api_instance = clientapi_cpanel.MailingListsApi(api_client)
    delegates = 'delegates=user@example.com,admin@example.com' # str | A list of the administrators to add.  **Note:**    Separate multiple email addresses with commas.
    list = 'mylist' # str | The mailing list.

    try:
        # Add administrators to mailing list
        api_response = api_instance.add_mailman_delegates(delegates, list)
        print("The response of MailingListsApi->add_mailman_delegates:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MailingListsApi->add_mailman_delegates: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delegates** | **str**| A list of the administrators to add.  **Note:**    Separate multiple email addresses with commas. | 
 **list** | **str**| The mailing list. | 

### Return type

[**InlineResponse200124**](InlineResponse200124.md)

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

# **count_lists**
> InlineResponse200134 count_lists()

Return cPanel account's mailing list total

This function returns the number of [mailing lists](https://go.cpanel.net/MailingLists) for every email address on a cPanel account.

**Important:**

  When you disable the [*Receive Mail* role](https://go.cpanel.net/serverroles#roles), the system **disables** this function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200134 import InlineResponse200134
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
    api_instance = clientapi_cpanel.MailingListsApi(api_client)

    try:
        # Return cPanel account's mailing list total
        api_response = api_instance.count_lists()
        print("The response of MailingListsApi->count_lists:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MailingListsApi->count_lists: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**InlineResponse200134**](InlineResponse200134.md)

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

# **delete_list**
> InlineResponse200141 delete_list(list)

Delete mailing list

This function deletes a Mailman mailing list.

**Important:**

  When you disable the [*Receive Mail* role](https://go.cpanel.net/serverroles), the system **disables** this function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200141 import InlineResponse200141
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
    api_instance = clientapi_cpanel.MailingListsApi(api_client)
    list = 'mylist' # str | The mailing list.

    try:
        # Delete mailing list
        api_response = api_instance.delete_list(list)
        print("The response of MailingListsApi->delete_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MailingListsApi->delete_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **list** | **str**| The mailing list. | 

### Return type

[**InlineResponse200141**](InlineResponse200141.md)

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

# **export_lists**
> InlineResponse200155 export_lists()

Export cPanel account's Mailman mailing lists to a file

This function exports a cPanel account's Mailman mailing lists into a CSV file.
This file is located in mail/exported_lists under the user's home directory.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200155 import InlineResponse200155
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
    api_instance = clientapi_cpanel.MailingListsApi(api_client)

    try:
        # Export cPanel account's Mailman mailing lists to a file
        api_response = api_instance.export_lists()
        print("The response of MailingListsApi->export_lists:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MailingListsApi->export_lists: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**InlineResponse200155**](InlineResponse200155.md)

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

# **generate_mailman_otp**
> InlineResponse200158 generate_mailman_otp(list)

Create one-time password for a mailing list

This function generates a one-time password (OTP) for a mailing list.

**Note:**

The generated password expires after one use.

**Important:**

When you disable the [Receive Mail role](https://go.cpanel.net/serverroles), the system **disables** this function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200158 import InlineResponse200158
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
    api_instance = clientapi_cpanel.MailingListsApi(api_client)
    list = 'mylist' # str | The mailing list.

    try:
        # Create one-time password for a mailing list
        api_response = api_instance.generate_mailman_otp(list)
        print("The response of MailingListsApi->generate_mailman_otp:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MailingListsApi->generate_mailman_otp: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **list** | **str**| The mailing list. | 

### Return type

[**InlineResponse200158**](InlineResponse200158.md)

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

# **get_lists_total_disk_usage**
> InlineResponse200167 get_lists_total_disk_usage()

Return cPanel account's mailing list disk usage

This function returns the total disk usage for the [mailing lists](https://go.cpanel.net/cpaneldocsMailingLists) of a cPanel account.

**Important:**

When you disable the [Receive Mail role](https://go.cpanel.net/serverroles), the system **disables** this function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200167 import InlineResponse200167
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
    api_instance = clientapi_cpanel.MailingListsApi(api_client)

    try:
        # Return cPanel account's mailing list disk usage
        api_response = api_instance.get_lists_total_disk_usage()
        print("The response of MailingListsApi->get_lists_total_disk_usage:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MailingListsApi->get_lists_total_disk_usage: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**InlineResponse200167**](InlineResponse200167.md)

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

# **get_mailman_delegates**
> InlineResponse200169 get_mailman_delegates(list)

Return mailing list administrators

This function lists a mailing list's administrators.

**Important:**

When you disable the [Receive Mail](https://go.cpanel.net/serverroles) role, the system **disables** this function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200169 import InlineResponse200169
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
    api_instance = clientapi_cpanel.MailingListsApi(api_client)
    list = 'mylist' # str | The name of a Mailman mailing list on the cPanel account.

    try:
        # Return mailing list administrators
        api_response = api_instance.get_mailman_delegates(list)
        print("The response of MailingListsApi->get_mailman_delegates:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MailingListsApi->get_mailman_delegates: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **list** | **str**| The name of a Mailman mailing list on the cPanel account. | 

### Return type

[**InlineResponse200169**](InlineResponse200169.md)

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

# **has_delegated_mailman_lists**
> InlineResponse200177 has_delegated_mailman_lists(delegate)

Return email account's mailing list privileges

This function checks an account's administrative privileges on mailing lists.

**Important:**

When you disable the [Receive Mail role](https://go.cpanel.net/serverroles), the system **disables** this function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200177 import InlineResponse200177
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
    api_instance = clientapi_cpanel.MailingListsApi(api_client)
    delegate = 'user@example.com' # str | The email address.

    try:
        # Return email account's mailing list privileges
        api_response = api_instance.has_delegated_mailman_lists(delegate)
        print("The response of MailingListsApi->has_delegated_mailman_lists:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MailingListsApi->has_delegated_mailman_lists: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delegate** | **str**| The email address. | 

### Return type

[**InlineResponse200177**](InlineResponse200177.md)

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

# **list_lists**
> InlineResponse200187 list_lists(domain=domain, regex=regex)

Return cPanel account's mailing lists

This function lists the account's Mailman mailing lists.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200187 import InlineResponse200187
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
    api_instance = clientapi_cpanel.MailingListsApi(api_client)
    domain = 'example.com' # str | The domain to query. If you do **not** use this parameter, the function lists mailing lists for all of the cPanel account's domains. (optional)
    regex = 'user' # str | A [Perl Compatible Regular Expression (PCRE)](https://en.wikipedia.org/wiki/Perl_Compatible_Regular_Expressions) that filters the results. (optional)

    try:
        # Return cPanel account's mailing lists
        api_response = api_instance.list_lists(domain=domain, regex=regex)
        print("The response of MailingListsApi->list_lists:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MailingListsApi->list_lists: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**| The domain to query. If you do **not** use this parameter, the function lists mailing lists for all of the cPanel account&#39;s domains. | [optional] 
 **regex** | **str**| A [Perl Compatible Regular Expression (PCRE)](https://en.wikipedia.org/wiki/Perl_Compatible_Regular_Expressions) that filters the results. | [optional] 

### Return type

[**InlineResponse200187**](InlineResponse200187.md)

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

# **passwd_list**
> InlineResponse200193 passwd_list(list, password)

Update mailing list password

This function changes a mailing list's password.

**Important:**

When you disable the [_Receive Mail_](https://go.cpanel.net/serverroles) role, the system **disables** this function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200193 import InlineResponse200193
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
    api_instance = clientapi_cpanel.MailingListsApi(api_client)
    list = 'mylist@example.com' # str | The full name (including the domain) of a Mailman mailing list on the cPanel account.
    password = '12345luggage' # str | The new password.

    try:
        # Update mailing list password
        api_response = api_instance.passwd_list(list, password)
        print("The response of MailingListsApi->passwd_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MailingListsApi->passwd_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **list** | **str**| The full name (including the domain) of a Mailman mailing list on the cPanel account. | 
 **password** | **str**| The new password. | 

### Return type

[**InlineResponse200193**](InlineResponse200193.md)

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

# **remove_mailman_delegates**
> InlineResponse200196 remove_mailman_delegates(delegates, list)

Remove account mailing list admin privileges

This function removes an account's mailing list administrative privileges.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200196 import InlineResponse200196
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
    api_instance = clientapi_cpanel.MailingListsApi(api_client)
    delegates = 'user@example.com,admin@example.com' # str | list of the administrators to remove.
    list = 'mylist' # str | The mailing list.

    try:
        # Remove account mailing list admin privileges
        api_response = api_instance.remove_mailman_delegates(delegates, list)
        print("The response of MailingListsApi->remove_mailman_delegates:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MailingListsApi->remove_mailman_delegates: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delegates** | **str**| list of the administrators to remove. | 
 **list** | **str**| The mailing list. | 

### Return type

[**InlineResponse200196**](InlineResponse200196.md)

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

# **set_list_privacy_options**
> InlineResponse200200 set_list_privacy_options(advertised, archive_private, list, subscribe_policy)

Update mailing list privacy options

This function modifies a Mailman mailing list's privacy options.

**Important:**

When you disable the [Receive Mail role](https://go.cpanel.net/serverroles), the system **disables** this function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200200 import InlineResponse200200
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
    api_instance = clientapi_cpanel.MailingListsApi(api_client)
    advertised = 1 # int | Whether the Mailman directory page displays the list. * `1` - Display. * `0` - Does **not** display.
    archive_private = 1 # int | Whether the mailing list archive is private. * `1` - Private. * `0` - Public.
    list = 'mylist' # str | The mailing list name.
    subscribe_policy = 1 # int | The level of control that the mailing list administrator has over new subscribers. * `1` - Anyone can subscribe. The system sends a confirmation email. * `2` - The administrator **must** approve subscriptions. The system does **not** send a confirmation email. * `3` - The administrator **must** approve subscriptions. The system sends a confirmation email.

    try:
        # Update mailing list privacy options
        api_response = api_instance.set_list_privacy_options(advertised, archive_private, list, subscribe_policy)
        print("The response of MailingListsApi->set_list_privacy_options:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MailingListsApi->set_list_privacy_options: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **advertised** | **int**| Whether the Mailman directory page displays the list. * &#x60;1&#x60; - Display. * &#x60;0&#x60; - Does **not** display. | 
 **archive_private** | **int**| Whether the mailing list archive is private. * &#x60;1&#x60; - Private. * &#x60;0&#x60; - Public. | 
 **list** | **str**| The mailing list name. | 
 **subscribe_policy** | **int**| The level of control that the mailing list administrator has over new subscribers. * &#x60;1&#x60; - Anyone can subscribe. The system sends a confirmation email. * &#x60;2&#x60; - The administrator **must** approve subscriptions. The system does **not** send a confirmation email. * &#x60;3&#x60; - The administrator **must** approve subscriptions. The system sends a confirmation email. | 

### Return type

[**InlineResponse200200**](InlineResponse200200.md)

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

