# clientapi_cpanel.MailboxManagementApi

All URIs are relative to *https://cpanel-server.tld:2083/execute*

Method | HTTP request | Description
------------- | ------------- | -------------
[**expunge_mailbox_messages**](MailboxManagementApi.md#expunge_mailbox_messages) | **GET** /Mailboxes/expunge_mailbox_messages | Delete selected messages in mailbox
[**expunge_messages_for_mailbox_guid**](MailboxManagementApi.md#expunge_messages_for_mailbox_guid) | **GET** /Mailboxes/expunge_messages_for_mailbox_guid | Delete selected messages in mailbox by GUID
[**get_mailbox_status_list**](MailboxManagementApi.md#get_mailbox_status_list) | **GET** /Mailboxes/get_mailbox_status_list | Return cPanel account&#39;s mailbox status
[**has_utf8_mailbox_names**](MailboxManagementApi.md#has_utf8_mailbox_names) | **GET** /Mailboxes/has_utf8_mailbox_names | Return if cPanel account&#39;s mailboxes use UTF-8
[**set_utf8_mailbox_names**](MailboxManagementApi.md#set_utf8_mailbox_names) | **GET** /Mailboxes/set_utf8_mailbox_names | Enable or disable Webmail mailbox UTF-8 encoding


# **expunge_mailbox_messages**
> InlineResponse200297 expunge_mailbox_messages(account, mailbox, query)

Delete selected messages in mailbox

This function marks the selected mail messages as deleted.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200297 import InlineResponse200297
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
    api_instance = clientapi_cpanel.MailboxManagementApi(api_client)
    account = clientapi_cpanel.Account3() # Account3 | The email account's name.
    mailbox = 'INBOX.user@example_com' # str | The mailbox to operate on.  **Note:**  * Use the `Mailboxes::get_mailbox_status_list` function to list possible values for the mailbox parameter. * Because you cannot escape wildcard characters such as (`*`), we recommend that you use functions that use the `mailbox_guid` parameter instead. For example, the `Mailboxes::expunge_messages_for_mailbox_guid` function.
    query = 'savedbefore 52w' # str | The Dovecot query to execute.  **Note:**  The query parameter prevents accidental removal of all messages in the mailbox. For more information, read Dovecot's [Search Query](http://wiki2.dovecot.org/Tools/Doveadm/SearchQuery) documentation.

    try:
        # Delete selected messages in mailbox
        api_response = api_instance.expunge_mailbox_messages(account, mailbox, query)
        print("The response of MailboxManagementApi->expunge_mailbox_messages:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MailboxManagementApi->expunge_mailbox_messages: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account** | [**Account3**](.md)| The email account&#39;s name. | 
 **mailbox** | **str**| The mailbox to operate on.  **Note:**  * Use the &#x60;Mailboxes::get_mailbox_status_list&#x60; function to list possible values for the mailbox parameter. * Because you cannot escape wildcard characters such as (&#x60;*&#x60;), we recommend that you use functions that use the &#x60;mailbox_guid&#x60; parameter instead. For example, the &#x60;Mailboxes::expunge_messages_for_mailbox_guid&#x60; function. | 
 **query** | **str**| The Dovecot query to execute.  **Note:**  The query parameter prevents accidental removal of all messages in the mailbox. For more information, read Dovecot&#39;s [Search Query](http://wiki2.dovecot.org/Tools/Doveadm/SearchQuery) documentation. | 

### Return type

[**InlineResponse200297**](InlineResponse200297.md)

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

# **expunge_messages_for_mailbox_guid**
> InlineResponse200298 expunge_messages_for_mailbox_guid(account, mailbox_guid, query)

Delete selected messages in mailbox by GUID

This function marks the selected mailbox's messages as deleted.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200298 import InlineResponse200298
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
    api_instance = clientapi_cpanel.MailboxManagementApi(api_client)
    account = clientapi_cpanel.Account4() # Account4 | The email account's name.
    mailbox_guid = '2550860f0c58d158c92a000044f0d230' # str | The mailbox's globally unique identifier (GUID).  Use the `Mailboxes::get_mailbox_status_list` function to list possible values for the `mailbox_guid` parameter.
    query = 'savedbefore 52w' # str | The query to select which messages you wish to remove from the mailbox.

    try:
        # Delete selected messages in mailbox by GUID
        api_response = api_instance.expunge_messages_for_mailbox_guid(account, mailbox_guid, query)
        print("The response of MailboxManagementApi->expunge_messages_for_mailbox_guid:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MailboxManagementApi->expunge_messages_for_mailbox_guid: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account** | [**Account4**](.md)| The email account&#39;s name. | 
 **mailbox_guid** | **str**| The mailbox&#39;s globally unique identifier (GUID).  Use the &#x60;Mailboxes::get_mailbox_status_list&#x60; function to list possible values for the &#x60;mailbox_guid&#x60; parameter. | 
 **query** | **str**| The query to select which messages you wish to remove from the mailbox. | 

### Return type

[**InlineResponse200298**](InlineResponse200298.md)

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

# **get_mailbox_status_list**
> InlineResponse200299 get_mailbox_status_list(account)

Return cPanel account's mailbox status

This function lists the account's mailbox size and globally unique identifier (GUID) by folder.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200299 import InlineResponse200299
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
    api_instance = clientapi_cpanel.MailboxManagementApi(api_client)
    account = 'user@example.com' # str | The email account for which you you wish to request the status.

    try:
        # Return cPanel account's mailbox status
        api_response = api_instance.get_mailbox_status_list(account)
        print("The response of MailboxManagementApi->get_mailbox_status_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MailboxManagementApi->get_mailbox_status_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account** | **str**| The email account for which you you wish to request the status. | 

### Return type

[**InlineResponse200299**](InlineResponse200299.md)

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

# **has_utf8_mailbox_names**
> InlineResponse200300 has_utf8_mailbox_names(user=user)

Return if cPanel account's mailboxes use UTF-8

This function determines whether a cPanel user currently uses UTF-8 character-encoded mailbox names.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200300 import InlineResponse200300
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
    api_instance = clientapi_cpanel.MailboxManagementApi(api_client)
    user = 'user' # str | The user for whom to determine whether they currently use UTF-8 character-encoded mailbox names.  **Note:**  This parameter defaults to the currently-logged in user. (optional)

    try:
        # Return if cPanel account's mailboxes use UTF-8
        api_response = api_instance.has_utf8_mailbox_names(user=user)
        print("The response of MailboxManagementApi->has_utf8_mailbox_names:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MailboxManagementApi->has_utf8_mailbox_names: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | **str**| The user for whom to determine whether they currently use UTF-8 character-encoded mailbox names.  **Note:**  This parameter defaults to the currently-logged in user. | [optional] 

### Return type

[**InlineResponse200300**](InlineResponse200300.md)

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

# **set_utf8_mailbox_names**
> InlineResponse200301 set_utf8_mailbox_names(enabled)

Enable or disable Webmail mailbox UTF-8 encoding

This function enables or disables UTF-8-encoded mailbox names on Roundcube webmail for a cPanel user's email accounts.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200301 import InlineResponse200301
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
    api_instance = clientapi_cpanel.MailboxManagementApi(api_client)
    enabled = 1 # int | Whether to enable or disable UTF-8 character-encoded mailbox names.  * `1` - Enable UTF-8 encoded mailbox names. * `0` - Disable UTF-8 encoded mailbox names.

    try:
        # Enable or disable Webmail mailbox UTF-8 encoding
        api_response = api_instance.set_utf8_mailbox_names(enabled)
        print("The response of MailboxManagementApi->set_utf8_mailbox_names:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MailboxManagementApi->set_utf8_mailbox_names: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **enabled** | **int**| Whether to enable or disable UTF-8 character-encoded mailbox names.  * &#x60;1&#x60; - Enable UTF-8 encoded mailbox names. * &#x60;0&#x60; - Disable UTF-8 encoded mailbox names. | 

### Return type

[**InlineResponse200301**](InlineResponse200301.md)

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

