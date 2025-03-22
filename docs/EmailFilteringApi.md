# clientapi_cpanel.EmailFilteringApi

All URIs are relative to *https://cpanel-server.tld:2083/execute*

Method | HTTP request | Description
------------- | ------------- | -------------
[**count_filters**](EmailFilteringApi.md#count_filters) | **GET** /Email/count_filters | Return cPanel account&#39;s email filters total
[**delete_filter**](EmailFilteringApi.md#delete_filter) | **GET** /Email/delete_filter | Delete email account&#39;s email filter
[**disable_filter**](EmailFilteringApi.md#disable_filter) | **GET** /Email/disable_filter | Disable email filter for email account
[**enable_filter**](EmailFilteringApi.md#enable_filter) | **GET** /Email/enable_filter | Enable email filter for email account
[**get_filter**](EmailFilteringApi.md#get_filter) | **GET** /Email/get_filter | Return email filter&#39;s information
[**list_filters**](EmailFilteringApi.md#list_filters) | **GET** /Email/list_filters | Return account-level email filters
[**list_filters_backups**](EmailFilteringApi.md#list_filters_backups) | **GET** /Email/list_filters_backups | Return domains with domain-level email filters
[**list_system_filter_info**](EmailFilteringApi.md#list_system_filter_info) | **GET** /Email/list_system_filter_info | Return system-level email filter file information
[**reorder_filters**](EmailFilteringApi.md#reorder_filters) | **GET** /Email/reorder_filters | Update email address&#39;s email filter order
[**store_filter**](EmailFilteringApi.md#store_filter) | **GET** /Email/store_filter | Create email filter
[**trace_filter**](EmailFilteringApi.md#trace_filter) | **GET** /Email/trace_filter | Run test for main domain email filters


# **count_filters**
> InlineResponse200132 count_filters()

Return cPanel account's email filters total

This function returns the number of [email filters](https://go.cpanel.net/cpaneldocsEmailFilters) for every email address on a cPanel account.

**Important:**

  When you disable the [*Receive Mail* role](https://go.cpanel.net/serverroles) or the [*IP Blocker*](https://go.cpanel.net/whmdocsFeatureManager) feature, the system **disables** this function. For more information, read our [How to Use Server Profiles](https://go.cpanel.net/howtouseserverprofiles) documentation.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200132 import InlineResponse200132
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
    api_instance = clientapi_cpanel.EmailFilteringApi(api_client)

    try:
        # Return cPanel account's email filters total
        api_response = api_instance.count_filters()
        print("The response of EmailFilteringApi->count_filters:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailFilteringApi->count_filters: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**InlineResponse200132**](InlineResponse200132.md)

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

# **delete_filter**
> InlineResponse200138 delete_filter(account, filtername)

Delete email account's email filter

This function deletes an email filter.

**Important:**

  When you disable the [*Receive Mail* role](https://go.cpanel.net/serverroles), the system **disables** this function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200138 import InlineResponse200138
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
    api_instance = clientapi_cpanel.EmailFilteringApi(api_client)
    account = 'user@example.com' # str | The email address that owns the filter.
    filtername = 'coffee' # str | The filter's name.

    try:
        # Delete email account's email filter
        api_response = api_instance.delete_filter(account, filtername)
        print("The response of EmailFilteringApi->delete_filter:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailFilteringApi->delete_filter: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account** | **str**| The email address that owns the filter. | 
 **filtername** | **str**| The filter&#39;s name. | 

### Return type

[**InlineResponse200138**](InlineResponse200138.md)

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

# **disable_filter**
> InlineResponse200144 disable_filter(account, filtername)

Disable email filter for email account

This function disables an email filter.

**Important:**

  When you disable the [*Receive Mail* role](https://go.cpanel.net/serverroles), the system **disables** this function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200144 import InlineResponse200144
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
    api_instance = clientapi_cpanel.EmailFilteringApi(api_client)
    account = 'user@example.com' # str | The email address that owns the filter.
    filtername = 'coffee' # str | The filter's name.

    try:
        # Disable email filter for email account
        api_response = api_instance.disable_filter(account, filtername)
        print("The response of EmailFilteringApi->disable_filter:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailFilteringApi->disable_filter: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account** | **str**| The email address that owns the filter. | 
 **filtername** | **str**| The filter&#39;s name. | 

### Return type

[**InlineResponse200144**](InlineResponse200144.md)

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

# **enable_filter**
> InlineResponse200151 enable_filter(account, filtername)

Enable email filter for email account

This function enables an email filter.

**Important:**

  When you disable the [Receive Mail role](https://go.cpanel.net/serverroles), the system **disables** this function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200151 import InlineResponse200151
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
    api_instance = clientapi_cpanel.EmailFilteringApi(api_client)
    account = 'username@example.com' # str | The email address that owns the filter.
    filtername = 'coffee' # str | The filter's name.

    try:
        # Enable email filter for email account
        api_response = api_instance.enable_filter(account, filtername)
        print("The response of EmailFilteringApi->enable_filter:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailFilteringApi->enable_filter: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account** | **str**| The email address that owns the filter. | 
 **filtername** | **str**| The filter&#39;s name. | 

### Return type

[**InlineResponse200151**](InlineResponse200151.md)

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

# **get_filter**
> InlineResponse200165 get_filter(account, filtername)

Return email filter's information

This function retrieves an email filter's information.

**Important:**

When you disable the [Receive Mail](https://go.cpanel.net/serverroles) role, the system **disables** this function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200165 import InlineResponse200165
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
    api_instance = clientapi_cpanel.EmailFilteringApi(api_client)
    account = 'user@example.com' # str | The email address that owns the filter.
    filtername = 'coffee' # str | The filter's name.

    try:
        # Return email filter's information
        api_response = api_instance.get_filter(account, filtername)
        print("The response of EmailFilteringApi->get_filter:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailFilteringApi->get_filter: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account** | **str**| The email address that owns the filter. | 
 **filtername** | **str**| The filter&#39;s name. | 

### Return type

[**InlineResponse200165**](InlineResponse200165.md)

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

# **list_filters**
> InlineResponse200183 list_filters(account=account)

Return account-level email filters

This function lists account-level mail filters. For more information about Exim filters, read [Exim’s documentation](http://www.exim.org/exim-html-3.30/doc/html/filter.html).

**Important**:

  When you disable the [Mail Receive role](https://go.cpanel.net/serverroles), the system **disables** this function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200183 import InlineResponse200183
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
    api_instance = clientapi_cpanel.EmailFilteringApi(api_client)
    account = clientapi_cpanel.Account2() # Account2 | The email address or cPanel account username for which to return a list of filters. If you do not specify this value, the function lists all of the cPanel account’s account-level filters. (optional)

    try:
        # Return account-level email filters
        api_response = api_instance.list_filters(account=account)
        print("The response of EmailFilteringApi->list_filters:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailFilteringApi->list_filters: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account** | [**Account2**](.md)| The email address or cPanel account username for which to return a list of filters. If you do not specify this value, the function lists all of the cPanel account’s account-level filters. | [optional] 

### Return type

[**InlineResponse200183**](InlineResponse200183.md)

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

# **list_filters_backups**
> InlineResponse200184 list_filters_backups()

Return domains with domain-level email filters

This function lists all of the cPanel account's domains that use domain-level filters.

**Important:**

  When you disable the [*Receive Mail* role](https://go.cpanel.net/serverroles), the system **disables** this function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200184 import InlineResponse200184
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
    api_instance = clientapi_cpanel.EmailFilteringApi(api_client)

    try:
        # Return domains with domain-level email filters
        api_response = api_instance.list_filters_backups()
        print("The response of EmailFilteringApi->list_filters_backups:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailFilteringApi->list_filters_backups: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**InlineResponse200184**](InlineResponse200184.md)

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

# **list_system_filter_info**
> InlineResponse200192 list_system_filter_info()

Return system-level email filter file information

This function retrieves a `.yaml.gz` file that contains system-level filter information.

**Important:**

  When you disable the [*Receive Mail* role](https://go.cpanel.net/serverroles), the system **disables** this function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200192 import InlineResponse200192
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
    api_instance = clientapi_cpanel.EmailFilteringApi(api_client)

    try:
        # Return system-level email filter file information
        api_response = api_instance.list_system_filter_info()
        print("The response of EmailFilteringApi->list_system_filter_info:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailFilteringApi->list_system_filter_info: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**InlineResponse200192**](InlineResponse200192.md)

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

# **reorder_filters**
> InlineResponse200197 reorder_filters(filter, mailbox)

Update email address's email filter order

This function modifies the filter order for an email address. For more information about Exim filters, read [Exim's documentation](http://www.exim.org/exim-html-3.30/doc/html/filter.html).

**Important:**

When you disable the [_Receive Mail_ role](https://go.cpanel.net/serverroles), the system **disables** this function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200197 import InlineResponse200197
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
    api_instance = clientapi_cpanel.EmailFilteringApi(api_client)
    filter = 'coffee' # str | A mail filter name.  For each mail filter to reorder, supply a `filter*` parameter, where `*` is a number that represents the filter's order.  For example, to set `coffee` as the first email filter and `cheesecloth` as the second, set `coffee` as the `filter1` parameter's value, and `cheesecloth` as the value for the `filter2` parameter.
    mailbox = 'user@example.com' # str | The email address.

    try:
        # Update email address's email filter order
        api_response = api_instance.reorder_filters(filter, mailbox)
        print("The response of EmailFilteringApi->reorder_filters:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailFilteringApi->reorder_filters: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| A mail filter name.  For each mail filter to reorder, supply a &#x60;filter*&#x60; parameter, where &#x60;*&#x60; is a number that represents the filter&#39;s order.  For example, to set &#x60;coffee&#x60; as the first email filter and &#x60;cheesecloth&#x60; as the second, set &#x60;coffee&#x60; as the &#x60;filter1&#x60; parameter&#39;s value, and &#x60;cheesecloth&#x60; as the value for the &#x60;filter2&#x60; parameter. | 
 **mailbox** | **str**| The email address. | 

### Return type

[**InlineResponse200197**](InlineResponse200197.md)

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

# **store_filter**
> InlineResponse200203 store_filter(action, filtername, match, part, val, account=account, dest=dest, oldfiltername=oldfiltername, opt=opt)

Create email filter

This function creates a new email filter. For more information about Exim filters, read [Exim's documentation](http://www.exim.org/exim-html-3.30/doc/html/filter.html).

**Important:**

When you disable the [*Receive Mail* role](https://docs.cpanel.net/knowledge-base/general-systems-administration/how-to-use-server-profiles/#roles), the system **disables** this function.

### Create multiple rules

You may create up to 4,096 separate sets of conditions in one filter. To do this, append numbers to the parameter names.

To create a filter with two sets of actions and conditions, use the following parameters:
  * Assign the information for the first filter rule to the `action1`, `dest1`, `match1`, `opt1`, `part1`, and `val1` parameters.
  * Assign the information for the second filter rule to the `action2`, `dest2`, `match2`, `opt2`, `part2`, and `val2` parameters.

To create a filter that uses one set of actions but two sets of conditions, use the following parameters:
  * Assign the actions to the `action1` and `dest1` parameters.
  * Assign the first set of conditions to the `match1`, `opt1`, `part1`, and `val1` parameters.
  * Assign the second set of conditions to the `match2`, `opt2`, `part2`, and `val2` parameters.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.action import Action
from clientapi_cpanel.models.inline_response200203 import InlineResponse200203
from clientapi_cpanel.models.match import Match
from clientapi_cpanel.models.opt import Opt
from clientapi_cpanel.models.part import Part
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
    api_instance = clientapi_cpanel.EmailFilteringApi(api_client)
    action = clientapi_cpanel.Action() # Action | The filter's action.  * `deliver` - Deliver the message to the `dest*` address. * `fail` - Force a delivery failure. * `finish` - Stop processing the message. * `save` - Save the message to the `dest*` file. * `pipe` - Pipe the message to the `dest*` application.  **Important:**  * You **must** increment each action. For example, pass the first action as `action1` and the second action as `action2`. * This value **requires** the `FileStorage` role. For more information, read our [How to Use Server Profiles](https://docs.cpanel.net/knowledge-base/general-systems-administration/how-to-use-server-profiles) documentation.
    filtername = 'coffee' # str | The filter name.
    match = clientapi_cpanel.Match() # Match | The filter's [match type](http://www.exim.org/exim-html-current/doc/html/spec_html/filter_ch-exim_filter_files.html). * If the `val*` parameter is a string, use a string operator. * If the `val*` parameter is an integer, use a numeric operator.  String operators:  * `is` * `matches` * `contains` * `does not contain` * `begins` * `does not begin` * `ends` * `does not end` * `does not match`  Numeric operators:  * `is above` * `is not above` * `is below` * `is not below`  **Important:**   You **must** increment each match type. For example, pass the first match type as `match1` and the second match type as `match2`.
    part = clientapi_cpanel.Part() # Part | The email section to query.   * `$h_x-Spam-Bar:` - Match against the message's spam score value, measured in plus(`+`) characters.  * `$h_x-Spam-Score:` - Match against the message's spam score value.  * `$h_X-Spam-Status:` - Match against whether the system detected the message as spam.  * `$h_List-Id:` - Match against the message's `List-ID` header value.  * `$header_from:` - Match against the `From:` section.  * `$header_subject:` - Match against the `Subject:` section.  * `$header_to:` - Match against the `To:` section.  * `$reply_address:` - Match against the `Reply To:` section.  * `$message_body:` - Match against the message's body.  * `$message_headers:` - Match against the message's headers.  * `foranyaddress $h_to:, $h_cc:` - Match against all message recipients.  * `not delivered` - Match if the message is not queued for delivery.  * `error_message` - Match if the incoming message is bounced.  **Important:**  You **must** increment each section. For example, pass the first section as `part1` and the second section as `part2`.  **Note:**  Generally, the recipient does **not** receive the `BCC` field in an email's header. For this reason you **cannot** use the `BCC` field in a filter.
    val = clientapi_cpanel.Val() # Val | The value to match.  **Important:**  You **must** increment each value. For example, pass the first value as `val1` and the second value as `val2`.
    account = 'user@example.com' # str | The email address, for user-level filters. If you do not use this parameter, the function creates an account-level filter. (optional)
    dest = clientapi_cpanel.Dest() # Dest | The destination for filtered mail.  **Important:**   * This parameter is **required** if the action value is `deliver`, `save`, or `pipe`.  * You **must** increment each destination. For example, pass the first destination as `dest1` and the second destination as `dest2`. (optional)
    oldfiltername = 'pool' # str | The name of an existing filter, to rename it. If you do not use this parameter, the function creates a new filter. (optional)
    opt = clientapi_cpanel.Opt() # Opt | The connection between multiple conditions.  **Important:**  You **must** increment each connection. For example, pass the first connection as `opt1` and the second connection as `opt2`. (optional)

    try:
        # Create email filter
        api_response = api_instance.store_filter(action, filtername, match, part, val, account=account, dest=dest, oldfiltername=oldfiltername, opt=opt)
        print("The response of EmailFilteringApi->store_filter:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailFilteringApi->store_filter: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **action** | [**Action**](.md)| The filter&#39;s action.  * &#x60;deliver&#x60; - Deliver the message to the &#x60;dest*&#x60; address. * &#x60;fail&#x60; - Force a delivery failure. * &#x60;finish&#x60; - Stop processing the message. * &#x60;save&#x60; - Save the message to the &#x60;dest*&#x60; file. * &#x60;pipe&#x60; - Pipe the message to the &#x60;dest*&#x60; application.  **Important:**  * You **must** increment each action. For example, pass the first action as &#x60;action1&#x60; and the second action as &#x60;action2&#x60;. * This value **requires** the &#x60;FileStorage&#x60; role. For more information, read our [How to Use Server Profiles](https://docs.cpanel.net/knowledge-base/general-systems-administration/how-to-use-server-profiles) documentation. | 
 **filtername** | **str**| The filter name. | 
 **match** | [**Match**](.md)| The filter&#39;s [match type](http://www.exim.org/exim-html-current/doc/html/spec_html/filter_ch-exim_filter_files.html). * If the &#x60;val*&#x60; parameter is a string, use a string operator. * If the &#x60;val*&#x60; parameter is an integer, use a numeric operator.  String operators:  * &#x60;is&#x60; * &#x60;matches&#x60; * &#x60;contains&#x60; * &#x60;does not contain&#x60; * &#x60;begins&#x60; * &#x60;does not begin&#x60; * &#x60;ends&#x60; * &#x60;does not end&#x60; * &#x60;does not match&#x60;  Numeric operators:  * &#x60;is above&#x60; * &#x60;is not above&#x60; * &#x60;is below&#x60; * &#x60;is not below&#x60;  **Important:**   You **must** increment each match type. For example, pass the first match type as &#x60;match1&#x60; and the second match type as &#x60;match2&#x60;. | 
 **part** | [**Part**](.md)| The email section to query.   * &#x60;$h_x-Spam-Bar:&#x60; - Match against the message&#39;s spam score value, measured in plus(&#x60;+&#x60;) characters.  * &#x60;$h_x-Spam-Score:&#x60; - Match against the message&#39;s spam score value.  * &#x60;$h_X-Spam-Status:&#x60; - Match against whether the system detected the message as spam.  * &#x60;$h_List-Id:&#x60; - Match against the message&#39;s &#x60;List-ID&#x60; header value.  * &#x60;$header_from:&#x60; - Match against the &#x60;From:&#x60; section.  * &#x60;$header_subject:&#x60; - Match against the &#x60;Subject:&#x60; section.  * &#x60;$header_to:&#x60; - Match against the &#x60;To:&#x60; section.  * &#x60;$reply_address:&#x60; - Match against the &#x60;Reply To:&#x60; section.  * &#x60;$message_body:&#x60; - Match against the message&#39;s body.  * &#x60;$message_headers:&#x60; - Match against the message&#39;s headers.  * &#x60;foranyaddress $h_to:, $h_cc:&#x60; - Match against all message recipients.  * &#x60;not delivered&#x60; - Match if the message is not queued for delivery.  * &#x60;error_message&#x60; - Match if the incoming message is bounced.  **Important:**  You **must** increment each section. For example, pass the first section as &#x60;part1&#x60; and the second section as &#x60;part2&#x60;.  **Note:**  Generally, the recipient does **not** receive the &#x60;BCC&#x60; field in an email&#39;s header. For this reason you **cannot** use the &#x60;BCC&#x60; field in a filter. | 
 **val** | [**Val**](.md)| The value to match.  **Important:**  You **must** increment each value. For example, pass the first value as &#x60;val1&#x60; and the second value as &#x60;val2&#x60;. | 
 **account** | **str**| The email address, for user-level filters. If you do not use this parameter, the function creates an account-level filter. | [optional] 
 **dest** | [**Dest**](.md)| The destination for filtered mail.  **Important:**   * This parameter is **required** if the action value is &#x60;deliver&#x60;, &#x60;save&#x60;, or &#x60;pipe&#x60;.  * You **must** increment each destination. For example, pass the first destination as &#x60;dest1&#x60; and the second destination as &#x60;dest2&#x60;. | [optional] 
 **oldfiltername** | **str**| The name of an existing filter, to rename it. If you do not use this parameter, the function creates a new filter. | [optional] 
 **opt** | [**Opt**](.md)| The connection between multiple conditions.  **Important:**  You **must** increment each connection. For example, pass the first connection as &#x60;opt1&#x60; and the second connection as &#x60;opt2&#x60;. | [optional] 

### Return type

[**InlineResponse200203**](InlineResponse200203.md)

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

# **trace_filter**
> InlineResponse200209 trace_filter(msg, account=account)

Run test for main domain email filters

This function tests mail filters. The function **only** tests filters for the cPanel account's main domain, and only tests against the message's body. For more information about Exim filters, read [Exim's documentation](http://www.exim.org/exim-html-3.30/doc/html/filter.html).

**Note:**

If the domain or account does not contain a filter file, this function will fail.

**Important:**

When you disable the [Receive Mail](https://go.cpanel.net/serverroles) role, the system **disables** this function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200209 import InlineResponse200209
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
    api_instance = clientapi_cpanel.EmailFilteringApi(api_client)
    msg = 'Test' # str | The string to test. The function uses this string as the body of an email message, to check whether filters would match the string.
    account = 'user@example.com' # str | The email address, to test legacy cPanel filters in the filters directory. If you do not use this parameter, the function tests the main domain's filters in the `/etc/vfilters` directory. (optional)

    try:
        # Run test for main domain email filters
        api_response = api_instance.trace_filter(msg, account=account)
        print("The response of EmailFilteringApi->trace_filter:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailFilteringApi->trace_filter: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **msg** | **str**| The string to test. The function uses this string as the body of an email message, to check whether filters would match the string. | 
 **account** | **str**| The email address, to test legacy cPanel filters in the filters directory. If you do not use this parameter, the function tests the main domain&#39;s filters in the &#x60;/etc/vfilters&#x60; directory. | [optional] 

### Return type

[**InlineResponse200209**](InlineResponse200209.md)

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

