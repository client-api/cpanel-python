# clientapi_cpanel.CalendarAndContactsDAVApi

All URIs are relative to *https://cpanel-server.tld:2083/execute*

Method | HTTP request | Description
------------- | ------------- | -------------
[**c_pdavd_add_delegate**](CalendarAndContactsDAVApi.md#c_pdavd_add_delegate) | **GET** /CPDAVD/add_delegate | Share a calendar
[**c_pdavd_list_delegates**](CalendarAndContactsDAVApi.md#c_pdavd_list_delegates) | **GET** /CPDAVD/list_delegates | List calendar sharing.
[**c_pdavd_list_users**](CalendarAndContactsDAVApi.md#c_pdavd_list_users) | **GET** /CPDAVD/list_users | Update calendar sharing
[**c_pdavd_manage_collection**](CalendarAndContactsDAVApi.md#c_pdavd_manage_collection) | **GET** /CPDAVD/manage_collection | Perform an operation on a calendar or address book.
[**c_pdavd_remove_delegate**](CalendarAndContactsDAVApi.md#c_pdavd_remove_delegate) | **GET** /CPDAVD/remove_delegate | Remove a share.
[**c_pdavd_update_delegate**](CalendarAndContactsDAVApi.md#c_pdavd_update_delegate) | **GET** /CPDAVD/update_delegate | Update calendar sharing.
[**disable_shared_global_addressbook**](CalendarAndContactsDAVApi.md#disable_shared_global_addressbook) | **GET** /DAV/disable_shared_global_addressbook | Disable global address book
[**enable_shared_global_addressbook**](CalendarAndContactsDAVApi.md#enable_shared_global_addressbook) | **GET** /DAV/enable_shared_global_addressbook | Enable global address book
[**get_calendar_contacts_config**](CalendarAndContactsDAVApi.md#get_calendar_contacts_config) | **GET** /DAV/get_calendar_contacts_config | Return CalDAV and CardDAV connection information
[**has_shared_global_addressbook**](CalendarAndContactsDAVApi.md#has_shared_global_addressbook) | **GET** /DAV/has_shared_global_addressbook | Return whether global address book is enabled
[**is_dav_service_enabled**](CalendarAndContactsDAVApi.md#is_dav_service_enabled) | **GET** /DAV/is_dav_service_enabled | Return whether DAV is enabled
[**is_horde_enabled**](CalendarAndContactsDAVApi.md#is_horde_enabled) | **GET** /DAV/is_horde_enabled | Return whether Horde is enabled


# **c_pdavd_add_delegate**
> InlineResponse20051 c_pdavd_add_delegate(calendar, delegatee, delegator, readonly=readonly)

Share a calendar

This function adds a share for the specified calendar.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response20051 import InlineResponse20051
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
    api_instance = clientapi_cpanel.CalendarAndContactsDAVApi(api_client)
    calendar = 'calendar' # str | The calendar to share.
    delegatee = 'second@example.com' # str | The person to whom you will share the calendar.
    delegator = 'first@example.com' # str | The owner of the calendar, who wishes to share it to another user.
    readonly = 1 # int | If set, the provided access will be read-only. (optional)

    try:
        # Share a calendar
        api_response = api_instance.c_pdavd_add_delegate(calendar, delegatee, delegator, readonly=readonly)
        print("The response of CalendarAndContactsDAVApi->c_pdavd_add_delegate:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CalendarAndContactsDAVApi->c_pdavd_add_delegate: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **calendar** | **str**| The calendar to share. | 
 **delegatee** | **str**| The person to whom you will share the calendar. | 
 **delegator** | **str**| The owner of the calendar, who wishes to share it to another user. | 
 **readonly** | **int**| If set, the provided access will be read-only. | [optional] 

### Return type

[**InlineResponse20051**](InlineResponse20051.md)

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

# **c_pdavd_list_delegates**
> InlineResponse20052 c_pdavd_list_delegates()

List calendar sharing.

This function lists the sharing configuration in calendars for this account.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response20052 import InlineResponse20052
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
    api_instance = clientapi_cpanel.CalendarAndContactsDAVApi(api_client)

    try:
        # List calendar sharing.
        api_response = api_instance.c_pdavd_list_delegates()
        print("The response of CalendarAndContactsDAVApi->c_pdavd_list_delegates:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CalendarAndContactsDAVApi->c_pdavd_list_delegates: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**InlineResponse20052**](InlineResponse20052.md)

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

# **c_pdavd_list_users**
> InlineResponse20053 c_pdavd_list_users()

Update calendar sharing

This function lists the users that are available for use with CalDAV and CardDAV

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response20053 import InlineResponse20053
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
    api_instance = clientapi_cpanel.CalendarAndContactsDAVApi(api_client)

    try:
        # Update calendar sharing
        api_response = api_instance.c_pdavd_list_users()
        print("The response of CalendarAndContactsDAVApi->c_pdavd_list_users:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CalendarAndContactsDAVApi->c_pdavd_list_users: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**InlineResponse20053**](InlineResponse20053.md)

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

# **c_pdavd_manage_collection**
> InlineResponse20054 c_pdavd_manage_collection(account, action, collection_type, path, calendar_color=calendar_color, description=description, name=name)

Perform an operation on a calendar or address book.

This function creates, updates, or deletes a collection.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response20054 import InlineResponse20054
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
    api_instance = clientapi_cpanel.CalendarAndContactsDAVApi(api_client)
    account = 'user@example.com' # str | The owner of the calendar.
    action = 'delete' # str | The action to perform (create, update, or delete a collection).
    collection_type = 'calendar' # str | The collection type.
    path = '/calendars/user@example.com/mycalendar' # str | The path to the collection.
    calendar_color = '#ee5555' # str | The color of the calendar, if applicable. (optional)
    description = 'This is my calendar.' # str | The description of the collection. (optional)
    name = 'My Calendar' # str | The name of the collection. Required when creating a collection. (optional)

    try:
        # Perform an operation on a calendar or address book.
        api_response = api_instance.c_pdavd_manage_collection(account, action, collection_type, path, calendar_color=calendar_color, description=description, name=name)
        print("The response of CalendarAndContactsDAVApi->c_pdavd_manage_collection:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CalendarAndContactsDAVApi->c_pdavd_manage_collection: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account** | **str**| The owner of the calendar. | 
 **action** | **str**| The action to perform (create, update, or delete a collection). | 
 **collection_type** | **str**| The collection type. | 
 **path** | **str**| The path to the collection. | 
 **calendar_color** | **str**| The color of the calendar, if applicable. | [optional] 
 **description** | **str**| The description of the collection. | [optional] 
 **name** | **str**| The name of the collection. Required when creating a collection. | [optional] 

### Return type

[**InlineResponse20054**](InlineResponse20054.md)

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

# **c_pdavd_remove_delegate**
> InlineResponse20055 c_pdavd_remove_delegate(calendar, delegatee, delegator)

Remove a share.

This function removes a share for the specified calendar.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response20055 import InlineResponse20055
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
    api_instance = clientapi_cpanel.CalendarAndContactsDAVApi(api_client)
    calendar = 'calendar' # str | The calendar that was shared.
    delegatee = 'second@example.com' # str | The person to whom the calendar was shared.
    delegator = 'first@example.com' # str | The owner of the calendar, who wishes to remove the sharing.

    try:
        # Remove a share.
        api_response = api_instance.c_pdavd_remove_delegate(calendar, delegatee, delegator)
        print("The response of CalendarAndContactsDAVApi->c_pdavd_remove_delegate:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CalendarAndContactsDAVApi->c_pdavd_remove_delegate: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **calendar** | **str**| The calendar that was shared. | 
 **delegatee** | **str**| The person to whom the calendar was shared. | 
 **delegator** | **str**| The owner of the calendar, who wishes to remove the sharing. | 

### Return type

[**InlineResponse20055**](InlineResponse20055.md)

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

# **c_pdavd_update_delegate**
> InlineResponse20056 c_pdavd_update_delegate(calendar, delegatee, delegator, readonly=readonly)

Update calendar sharing.

This function updates a share for the specified calendar.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response20056 import InlineResponse20056
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
    api_instance = clientapi_cpanel.CalendarAndContactsDAVApi(api_client)
    calendar = 'calendar' # str | The calendar to share.
    delegatee = 'second@example.com' # str | The person to whom you will share the calendar.
    delegator = 'first@example.com' # str | The owner of the calendar, who wishes to change the details of the sharing.
    readonly = 1 # int | If set, the provided access will be read-only. (optional)

    try:
        # Update calendar sharing.
        api_response = api_instance.c_pdavd_update_delegate(calendar, delegatee, delegator, readonly=readonly)
        print("The response of CalendarAndContactsDAVApi->c_pdavd_update_delegate:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CalendarAndContactsDAVApi->c_pdavd_update_delegate: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **calendar** | **str**| The calendar to share. | 
 **delegatee** | **str**| The person to whom you will share the calendar. | 
 **delegator** | **str**| The owner of the calendar, who wishes to change the details of the sharing. | 
 **readonly** | **int**| If set, the provided access will be read-only. | [optional] 

### Return type

[**InlineResponse20056**](InlineResponse20056.md)

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

# **disable_shared_global_addressbook**
> InlineResponse20072 disable_shared_global_addressbook(name=name)

Disable global address book

This function disables the shared global address book for the current cPanel account's webmail accounts.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response20072 import InlineResponse20072
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
    api_instance = clientapi_cpanel.CalendarAndContactsDAVApi(api_client)
    name = 'user' # str | cPanel account username or a Webmail user's email address. If you do **not** specify a user, this parameter defaults to the currently-authenticated user. (optional)

    try:
        # Disable global address book
        api_response = api_instance.disable_shared_global_addressbook(name=name)
        print("The response of CalendarAndContactsDAVApi->disable_shared_global_addressbook:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CalendarAndContactsDAVApi->disable_shared_global_addressbook: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| cPanel account username or a Webmail user&#39;s email address. If you do **not** specify a user, this parameter defaults to the currently-authenticated user. | [optional] 

### Return type

[**InlineResponse20072**](InlineResponse20072.md)

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

# **enable_shared_global_addressbook**
> InlineResponse20073 enable_shared_global_addressbook(name=name)

Enable global address book

This function enables the shared global address book for the current cPanel account's webmail accounts.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response20073 import InlineResponse20073
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
    api_instance = clientapi_cpanel.CalendarAndContactsDAVApi(api_client)
    name = 'user' # str | cPanel account username or a Webmail user's email address. If you do **not** specify a user, this parameter defaults to the currently-authenticated user. (optional)

    try:
        # Enable global address book
        api_response = api_instance.enable_shared_global_addressbook(name=name)
        print("The response of CalendarAndContactsDAVApi->enable_shared_global_addressbook:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CalendarAndContactsDAVApi->enable_shared_global_addressbook: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| cPanel account username or a Webmail user&#39;s email address. If you do **not** specify a user, this parameter defaults to the currently-authenticated user. | [optional] 

### Return type

[**InlineResponse20073**](InlineResponse20073.md)

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

# **get_calendar_contacts_config**
> InlineResponse20074 get_calendar_contacts_config(user=user)

Return CalDAV and CardDAV connection information

This function returns the connection information to set up the CalDAV and CardDAV clients.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response20074 import InlineResponse20074
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
    api_instance = clientapi_cpanel.CalendarAndContactsDAVApi(api_client)
    user = clientapi_cpanel.User() # User | A cPanel account or valid email account user.  If you do **not** include this parameter, the function defaults to the current authenticated user. (optional)

    try:
        # Return CalDAV and CardDAV connection information
        api_response = api_instance.get_calendar_contacts_config(user=user)
        print("The response of CalendarAndContactsDAVApi->get_calendar_contacts_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CalendarAndContactsDAVApi->get_calendar_contacts_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | [**User**](.md)| A cPanel account or valid email account user.  If you do **not** include this parameter, the function defaults to the current authenticated user. | [optional] 

### Return type

[**InlineResponse20074**](InlineResponse20074.md)

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

# **has_shared_global_addressbook**
> InlineResponse20075 has_shared_global_addressbook(name=name)

Return whether global address book is enabled

This function checks whether the shared global address book is enabled on the current cPanel account's webmail accounts.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response20075 import InlineResponse20075
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
    api_instance = clientapi_cpanel.CalendarAndContactsDAVApi(api_client)
    name = 'user' # str | cPanel account user name or a Webmail user's email address. If you do **not** specify a user, this parameter defaults to the currently-authenticated user. (optional)

    try:
        # Return whether global address book is enabled
        api_response = api_instance.has_shared_global_addressbook(name=name)
        print("The response of CalendarAndContactsDAVApi->has_shared_global_addressbook:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CalendarAndContactsDAVApi->has_shared_global_addressbook: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| cPanel account user name or a Webmail user&#39;s email address. If you do **not** specify a user, this parameter defaults to the currently-authenticated user. | [optional] 

### Return type

[**InlineResponse20075**](InlineResponse20075.md)

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

# **is_dav_service_enabled**
> InlineResponse20076 is_dav_service_enabled()

Return whether DAV is enabled

This function checks whether the DAV service is enabled.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response20076 import InlineResponse20076
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
    api_instance = clientapi_cpanel.CalendarAndContactsDAVApi(api_client)

    try:
        # Return whether DAV is enabled
        api_response = api_instance.is_dav_service_enabled()
        print("The response of CalendarAndContactsDAVApi->is_dav_service_enabled:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CalendarAndContactsDAVApi->is_dav_service_enabled: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**InlineResponse20076**](InlineResponse20076.md)

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

# **is_horde_enabled**
> InlineResponse20077 is_horde_enabled()

Return whether Horde is enabled

This function checks whether Horde is enabled. Since Horde is no longer installed with the product, the return value will only ever be 0.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response20077 import InlineResponse20077
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
    api_instance = clientapi_cpanel.CalendarAndContactsDAVApi(api_client)

    try:
        # Return whether Horde is enabled
        api_response = api_instance.is_horde_enabled()
        print("The response of CalendarAndContactsDAVApi->is_horde_enabled:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CalendarAndContactsDAVApi->is_horde_enabled: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**InlineResponse20077**](InlineResponse20077.md)

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

