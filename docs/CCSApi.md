# clientapi_cpanel.CCSApi

All URIs are relative to *https://cpanel-server.tld:2083/execute*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_delegate**](CCSApi.md#add_delegate) | **GET** /CCS/add_delegate | Add calendar delegation
[**list_delegates**](CCSApi.md#list_delegates) | **GET** /CCS/list_delegates | List cPanel account&#39;s calendar delegates
[**list_users**](CCSApi.md#list_users) | **GET** /CCS/list_users | List cPanel account&#39;s calendar users
[**remove_delegate**](CCSApi.md#remove_delegate) | **GET** /CCS/remove_delegate | Remove calendar delegation
[**update_delegate**](CCSApi.md#update_delegate) | **GET** /CCS/update_delegate | Update calendar delegation


# **add_delegate**
> InlineResponse20046 add_delegate(delegatee, delegator, readonly=readonly)

Add calendar delegation

This function delegates a user's calendar to another user.

**Note:**

You **must** install the [Calendar and Contacts Server](https://go.cpanel.net/CalendarAndContactsServer) cPanel plugin to access this API function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response20046 import InlineResponse20046
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
    api_instance = clientapi_cpanel.CCSApi(api_client)
    delegatee = 'delegatee@cptest.test' # str | The user to whom you wish to delegate the calendar.
    delegator = 'delegator@cptest.test' # str | The calendar's owner.
    readonly = 0 # int | Whether the delegatee will only have read-only access on the calendar. * `1` - Read-only access. * `0` - Full access. (optional) (default to 0)

    try:
        # Add calendar delegation
        api_response = api_instance.add_delegate(delegatee, delegator, readonly=readonly)
        print("The response of CCSApi->add_delegate:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CCSApi->add_delegate: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delegatee** | **str**| The user to whom you wish to delegate the calendar. | 
 **delegator** | **str**| The calendar&#39;s owner. | 
 **readonly** | **int**| Whether the delegatee will only have read-only access on the calendar. * &#x60;1&#x60; - Read-only access. * &#x60;0&#x60; - Full access. | [optional] [default to 0]

### Return type

[**InlineResponse20046**](InlineResponse20046.md)

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

# **list_delegates**
> InlineResponse20047 list_delegates()

List cPanel account's calendar delegates

This function lists all [calendar delegates](https://docs.cpanel.net/cpanel/email/calendar-delegation/) on the cPanel account.

**Note:**

You **must** install the [Calendar and Contacts Server](https://go.cpanel.net/CalendarAndContactsServer) cPanel plugin to access this API function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response20047 import InlineResponse20047
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
    api_instance = clientapi_cpanel.CCSApi(api_client)

    try:
        # List cPanel account's calendar delegates
        api_response = api_instance.list_delegates()
        print("The response of CCSApi->list_delegates:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CCSApi->list_delegates: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**InlineResponse20047**](InlineResponse20047.md)

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

# **list_users**
> InlineResponse20048 list_users()

List cPanel account's calendar users

This function lists all calendar users on the cPanel account.

**Note:**

You **must** install the [Calendar and Contacts Server](https://go.cpanel.net/CalendarAndContactsServer) cPanel plugin to access this API function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response20048 import InlineResponse20048
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
    api_instance = clientapi_cpanel.CCSApi(api_client)

    try:
        # List cPanel account's calendar users
        api_response = api_instance.list_users()
        print("The response of CCSApi->list_users:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CCSApi->list_users: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**InlineResponse20048**](InlineResponse20048.md)

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

# **remove_delegate**
> InlineResponse20049 remove_delegate(delegatee, delegator)

Remove calendar delegation

This function removes a delegate from another user's calendar.

**Note:**

You **must** install the [Calendar and Contacts Server](https://go.cpanel.net/CalendarAndContactsServer) cPanel plugin to access this API function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response20049 import InlineResponse20049
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
    api_instance = clientapi_cpanel.CCSApi(api_client)
    delegatee = 'user2@example.com' # str | The user from whom you wish to remove delegation rights.
    delegator = 'user1@example.com' # str | The calendar's owner.

    try:
        # Remove calendar delegation
        api_response = api_instance.remove_delegate(delegatee, delegator)
        print("The response of CCSApi->remove_delegate:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CCSApi->remove_delegate: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delegatee** | **str**| The user from whom you wish to remove delegation rights. | 
 **delegator** | **str**| The calendar&#39;s owner. | 

### Return type

[**InlineResponse20049**](InlineResponse20049.md)

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

# **update_delegate**
> InlineResponse20050 update_delegate(delegatee, delegator, readonly=readonly)

Update calendar delegation

This function updates the delegation of a user's calendar to another user.

**Note:**

You **must** install the [Calendar and Contacts Server](https://go.cpanel.net/CalendarAndContactsServer) cPanel plugin to access this API function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response20050 import InlineResponse20050
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
    api_instance = clientapi_cpanel.CCSApi(api_client)
    delegatee = 'user2@example.com' # str | The user to whom you delegated the calendar.
    delegator = 'user1@example.com' # str | The calendar's owner.
    readonly = 0 # int | Whether the delegatee will only have read-only access on the calendar. * `1` - Read-only access. * `0` - Full access. (optional) (default to 0)

    try:
        # Update calendar delegation
        api_response = api_instance.update_delegate(delegatee, delegator, readonly=readonly)
        print("The response of CCSApi->update_delegate:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CCSApi->update_delegate: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delegatee** | **str**| The user to whom you delegated the calendar. | 
 **delegator** | **str**| The calendar&#39;s owner. | 
 **readonly** | **int**| Whether the delegatee will only have read-only access on the calendar. * &#x60;1&#x60; - Read-only access. * &#x60;0&#x60; - Full access. | [optional] [default to 0]

### Return type

[**InlineResponse20050**](InlineResponse20050.md)

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

