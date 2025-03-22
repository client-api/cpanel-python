# clientapi_cpanel.EmailAccountsApi

All URIs are relative to *https://cpanel-server.tld:2083/execute*

Method | HTTP request | Description
------------- | ------------- | -------------
[**account_name**](EmailAccountsApi.md#account_name) | **GET** /Email/account_name | Return current user&#39;s account name
[**add_auto_responder**](EmailAccountsApi.md#add_auto_responder) | **GET** /Email/add_auto_responder | Create email account&#39;s autoresponder
[**add_pop**](EmailAccountsApi.md#add_pop) | **GET** /Email/add_pop | Create email address
[**browse_mailbox**](EmailAccountsApi.md#browse_mailbox) | **GET** /Email/browse_mailbox | Return mail directory&#39;s subdirectories and files
[**c_sv_import_doimport**](EmailAccountsApi.md#c_sv_import_doimport) | **GET** /CSVImport/doimport | Import email accounts from CSV file
[**count_auto_responders**](EmailAccountsApi.md#count_auto_responders) | **GET** /Email/count_auto_responders | Return cPanel account&#39;s autoresponders total
[**count_pops**](EmailAccountsApi.md#count_pops) | **GET** /Email/count_pops | Return cPanel account&#39;s email account total
[**delete_auto_responder**](EmailAccountsApi.md#delete_auto_responder) | **GET** /Email/delete_auto_responder | Delete email account&#39;s autoresponder
[**delete_held_messages**](EmailAccountsApi.md#delete_held_messages) | **GET** /Email/delete_held_messages | Delete email account&#39;s outgoing messages
[**delete_pop**](EmailAccountsApi.md#delete_pop) | **GET** /Email/delete_pop | Delete email address
[**dispatch_client_settings**](EmailAccountsApi.md#dispatch_client_settings) | **GET** /Email/dispatch_client_settings | Send email client settings to an email address
[**edit_pop_quota**](EmailAccountsApi.md#edit_pop_quota) | **GET** /Email/edit_pop_quota | Update email account&#39;s quota
[**email_terminate_mailbox_sessions**](EmailAccountsApi.md#email_terminate_mailbox_sessions) | **GET** /Email/terminate_mailbox_sessions | Stop cPanel account IMAP and POP3 connections
[**get_auto_responder**](EmailAccountsApi.md#get_auto_responder) | **GET** /Email/get_auto_responder | Return email account&#39;s autoresponder information
[**get_client_settings**](EmailAccountsApi.md#get_client_settings) | **GET** /Email/get_client_settings | Return email account&#39;s client settings
[**get_default_email_quota**](EmailAccountsApi.md#get_default_email_quota) | **GET** /Email/get_default_email_quota | Return email account&#39;s default email quota
[**get_default_email_quota_mib**](EmailAccountsApi.md#get_default_email_quota_mib) | **GET** /Email/get_default_email_quota_mib | Return email account&#39;s default email quota in MiB
[**get_disk_usage**](EmailAccountsApi.md#get_disk_usage) | **GET** /Email/get_disk_usage | Return email account&#39;s disk usage
[**get_held_message_count**](EmailAccountsApi.md#get_held_message_count) | **GET** /Email/get_held_message_count | Return email account&#39;s outgoing message count
[**get_main_account_disk_usage**](EmailAccountsApi.md#get_main_account_disk_usage) | **GET** /Email/get_main_account_disk_usage | Return primary email account&#39;s disk usage
[**get_main_account_disk_usage_bytes**](EmailAccountsApi.md#get_main_account_disk_usage_bytes) | **GET** /Email/get_main_account_disk_usage_bytes | Return primary email account&#39;s disk usage in bytes
[**get_max_email_quota**](EmailAccountsApi.md#get_max_email_quota) | **GET** /Email/get_max_email_quota | Return email account&#39;s max quota size
[**get_max_email_quota_mib**](EmailAccountsApi.md#get_max_email_quota_mib) | **GET** /Email/get_max_email_quota_mib | Return email account&#39;s max quota size in MiB
[**get_pop_quota**](EmailAccountsApi.md#get_pop_quota) | **GET** /Email/get_pop_quota | Return email account&#39;s quota
[**get_webmail_settings**](EmailAccountsApi.md#get_webmail_settings) | **GET** /Email/get_webmail_settings | Return email account&#39;s Webmail settings
[**hold_outgoing**](EmailAccountsApi.md#hold_outgoing) | **GET** /Email/hold_outgoing | Stop email account&#39;s outgoing mail
[**list_auto_responders**](EmailAccountsApi.md#list_auto_responders) | **GET** /Email/list_auto_responders | Return domain&#39;s autoresponders
[**list_default_address**](EmailAccountsApi.md#list_default_address) | **GET** /Email/list_default_address | Return domain&#39;s default email address
[**list_mail_domains**](EmailAccountsApi.md#list_mail_domains) | **GET** /Email/list_mail_domains | Return cPanel account&#39;s mail domains
[**list_pops**](EmailAccountsApi.md#list_pops) | **GET** /Email/list_pops | Return email accounts
[**list_pops_with_disk**](EmailAccountsApi.md#list_pops_with_disk) | **GET** /Email/list_pops_with_disk | Return email accounts with disk information
[**passwd_pop**](EmailAccountsApi.md#passwd_pop) | **GET** /Email/passwd_pop | Update email account password
[**release_outgoing**](EmailAccountsApi.md#release_outgoing) | **GET** /Email/release_outgoing | Start email account outgoing mail
[**set_default_address**](EmailAccountsApi.md#set_default_address) | **GET** /Email/set_default_address | Create default email address
[**set_manual_mx_redirects**](EmailAccountsApi.md#set_manual_mx_redirects) | **GET** /Email/set_manual_mx_redirects | Add manual MX redirection
[**trace_delivery**](EmailAccountsApi.md#trace_delivery) | **GET** /Email/trace_delivery | Run email delivery route trace
[**unset_manual_mx_redirects**](EmailAccountsApi.md#unset_manual_mx_redirects) | **GET** /Email/unset_manual_mx_redirects | Remove manual MX redirection
[**verify_password**](EmailAccountsApi.md#verify_password) | **GET** /Email/verify_password | Validate email account password


# **account_name**
> InlineResponse200119 account_name(account=account, display=display)

Return current user's account name

This function returns the provided value. This function works with other functions to display form data within a user interface.

**Note:**

  If you call this function from a Webmail session URL, the system will **only** access data for that email account.

**Important:**

  When you disable the [*Receive Mail* role](https://go.cpanel.net/serverroles), the system **disables** this function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200119 import InlineResponse200119
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
    api_instance = clientapi_cpanel.EmailAccountsApi(api_client)
    account = 'user' # str | The function will return this value in the data return. If you do **not** include this parameter, the function returns `All Mail On The Account` or a blank value. * A valid string. * An empty value.  **Note:**   The function does **not** validate this parameter's value. (optional)
    display = 'any_value' # str | Include this parameter to cause the function to return `All Mail On The Account` if the account parameter is blank or does not exist. If you do **not** include this parameter and the account value is blank or does not exist, the function returns a blank data value. (optional)

    try:
        # Return current user's account name
        api_response = api_instance.account_name(account=account, display=display)
        print("The response of EmailAccountsApi->account_name:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailAccountsApi->account_name: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account** | **str**| The function will return this value in the data return. If you do **not** include this parameter, the function returns &#x60;All Mail On The Account&#x60; or a blank value. * A valid string. * An empty value.  **Note:**   The function does **not** validate this parameter&#39;s value. | [optional] 
 **display** | **str**| Include this parameter to cause the function to return &#x60;All Mail On The Account&#x60; if the account parameter is blank or does not exist. If you do **not** include this parameter and the account value is blank or does not exist, the function returns a blank data value. | [optional] 

### Return type

[**InlineResponse200119**](InlineResponse200119.md)

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

# **add_auto_responder**
> InlineResponse200120 add_auto_responder(body, domain, email, var_from, interval, is_html, start, stop, subject, charset=charset)

Create email account's autoresponder

This function creates an autoresponder for an email account.

**Important:**

  When you disable the [*Receive Mail* role](https://go.cpanel.net/serverroles), the system **disables** this function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200120 import InlineResponse200120
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
    api_instance = clientapi_cpanel.EmailAccountsApi(api_client)
    body = 'This is an autoresponder message.' # str | The contents of the autoresponder message's `Body` section.
    domain = 'example.com' # str | The email account's domain. For example, `example.com` if the email address is `user@example.com`.
    email = 'user' # str | The email account name. For example, `user` if the email address is `user@example.com`.
    var_from = 'User Name' # str | The contents of the autoresponder message's `From:` field.
    interval = 24 # int | The amount of time, in hours, that the server waits between autoresponder messages to the same address.  **Note:**    If you specify `0`, the system sends a message for each received email.
    is_html = 1 # int | Whether the body of the autoresponder message begins with an [HTML Content-Type declaration](https://en.wikipedia.org/wiki/Character_encodings_in_HTML#Specifying_the_document.27s_character_encoding). * `1` — Include an HTML content type declaration. * `0` — Do **not** include an HTML content type declaration.
    start = 1410277881 # int | When to enable the autoresponder.
    stop = 1410300000 # int | When to disable the autoresponder. A time that is after the `start` time.
    subject = 'Autoresponder Subject' # str | The contents of the autoresponder message's `Subject:` field.
    charset = 'utf-8' # str | The [character set](https://en.wikipedia.org/wiki/Character_encoding). (optional) (default to 'utf-8')

    try:
        # Create email account's autoresponder
        api_response = api_instance.add_auto_responder(body, domain, email, var_from, interval, is_html, start, stop, subject, charset=charset)
        print("The response of EmailAccountsApi->add_auto_responder:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailAccountsApi->add_auto_responder: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **str**| The contents of the autoresponder message&#39;s &#x60;Body&#x60; section. | 
 **domain** | **str**| The email account&#39;s domain. For example, &#x60;example.com&#x60; if the email address is &#x60;user@example.com&#x60;. | 
 **email** | **str**| The email account name. For example, &#x60;user&#x60; if the email address is &#x60;user@example.com&#x60;. | 
 **var_from** | **str**| The contents of the autoresponder message&#39;s &#x60;From:&#x60; field. | 
 **interval** | **int**| The amount of time, in hours, that the server waits between autoresponder messages to the same address.  **Note:**    If you specify &#x60;0&#x60;, the system sends a message for each received email. | 
 **is_html** | **int**| Whether the body of the autoresponder message begins with an [HTML Content-Type declaration](https://en.wikipedia.org/wiki/Character_encodings_in_HTML#Specifying_the_document.27s_character_encoding). * &#x60;1&#x60; — Include an HTML content type declaration. * &#x60;0&#x60; — Do **not** include an HTML content type declaration. | 
 **start** | **int**| When to enable the autoresponder. | 
 **stop** | **int**| When to disable the autoresponder. A time that is after the &#x60;start&#x60; time. | 
 **subject** | **str**| The contents of the autoresponder message&#39;s &#x60;Subject:&#x60; field. | 
 **charset** | **str**| The [character set](https://en.wikipedia.org/wiki/Character_encoding). | [optional] [default to &#39;utf-8&#39;]

### Return type

[**InlineResponse200120**](InlineResponse200120.md)

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

# **add_pop**
> InlineResponse200126 add_pop(email, password, domain=domain, password_hash=password_hash, quota=quota, send_welcome_email=send_welcome_email, skip_update_db=skip_update_db)

Create email address

This function creates an email address.

**Important:**

  * When you disable the [*Receive Mail* role](https://go.cpanel.net/serverroles), the system **disables** this function.
  * We recommend that you use the UAPI `UserManager::create_user` function to create an email address instead of this function. This function is incompatible with [the *Reset Password* feature](https://go.cpanel.net/resetpassdocs).
  * You **must** URI-encode values when using the CLI.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200126 import InlineResponse200126
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
    api_instance = clientapi_cpanel.EmailAccountsApi(api_client)
    email = clientapi_cpanel.Email2() # Email2 | The email account username or address. * A valid email account username. For example, `user` to create `user@example.com`. * A valid email address.  **Note:**    You **cannot** enter `cpanel` as an account name when you create an email account.
    password = '123456luggage' # str | The email account password.
    domain = 'The cPanel account's main domain.' # str | The email account's domain. For example, `example.com` to create `user@example.com`. (optional) (default to 'The cPanel account's main domain.')
    password_hash = '$6$1sOyHP5ZDYp3pGUz$R0TSgfPRHfDjT5PP5RJGv39FhiGTNNPvM7IFpCBjXijMmlMZk9yI8T3LqGuntc9fdKb5eX.lGL7wBS9e4DAWn/' # str | The account's password hash.  **Notes:**    * You can use this parameter instead of the `password` parameter. However, you cannot use both `password` and `password_hash` parameters in the same request.   * You can find your server's hash type in the `/etc/sysconfig/authconfig` file. (optional)
    quota = clientapi_cpanel.Quota() # Quota | The maximum amount of disk space that the new email account may use. * A positive integer that represents the maximum amount of disk space, in megabytes (MB). * `0` or `unlimited` — The account possesses unlimited disk space.  **Note:**    * The positive integer value **cannot** exceed the maximum email quota.   * The `0` or `unlimited` value is **only** available to users **without** a maximum email account quota. (optional)
    send_welcome_email = 0 # int | Whether to send client configuration instructions to the account. * `1` — Send the instructions. * `0` — Do **not** send the instructions. (optional) (default to 0)
    skip_update_db = 0 # int | Whether to skip the update of the email accounts database's cache. * `1` — Skip the update. * `0` — Perform the update. (optional) (default to 0)

    try:
        # Create email address
        api_response = api_instance.add_pop(email, password, domain=domain, password_hash=password_hash, quota=quota, send_welcome_email=send_welcome_email, skip_update_db=skip_update_db)
        print("The response of EmailAccountsApi->add_pop:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailAccountsApi->add_pop: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | [**Email2**](.md)| The email account username or address. * A valid email account username. For example, &#x60;user&#x60; to create &#x60;user@example.com&#x60;. * A valid email address.  **Note:**    You **cannot** enter &#x60;cpanel&#x60; as an account name when you create an email account. | 
 **password** | **str**| The email account password. | 
 **domain** | **str**| The email account&#39;s domain. For example, &#x60;example.com&#x60; to create &#x60;user@example.com&#x60;. | [optional] [default to &#39;The cPanel account&#39;s main domain.&#39;]
 **password_hash** | **str**| The account&#39;s password hash.  **Notes:**    * You can use this parameter instead of the &#x60;password&#x60; parameter. However, you cannot use both &#x60;password&#x60; and &#x60;password_hash&#x60; parameters in the same request.   * You can find your server&#39;s hash type in the &#x60;/etc/sysconfig/authconfig&#x60; file. | [optional] 
 **quota** | [**Quota**](.md)| The maximum amount of disk space that the new email account may use. * A positive integer that represents the maximum amount of disk space, in megabytes (MB). * &#x60;0&#x60; or &#x60;unlimited&#x60; — The account possesses unlimited disk space.  **Note:**    * The positive integer value **cannot** exceed the maximum email quota.   * The &#x60;0&#x60; or &#x60;unlimited&#x60; value is **only** available to users **without** a maximum email account quota. | [optional] 
 **send_welcome_email** | **int**| Whether to send client configuration instructions to the account. * &#x60;1&#x60; — Send the instructions. * &#x60;0&#x60; — Do **not** send the instructions. | [optional] [default to 0]
 **skip_update_db** | **int**| Whether to skip the update of the email accounts database&#39;s cache. * &#x60;1&#x60; — Skip the update. * &#x60;0&#x60; — Perform the update. | [optional] [default to 0]

### Return type

[**InlineResponse200126**](InlineResponse200126.md)

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

# **browse_mailbox**
> InlineResponse200128 browse_mailbox(account=account, dir=dir, showdotfiles=showdotfiles)

Return mail directory's subdirectories and files

This function lists the mail directory's subdirectories (boxes) and files.

**Important:**

  When you disable the [*Receive Mail* role](https://go.cpanel.net/serverroles#roles), the system **disables** this function.

**Notes:**

  If you do not use any input parameters, the function returns a list of items in the cPanel account's main mail directory.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200128 import InlineResponse200128
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
    api_instance = clientapi_cpanel.EmailAccountsApi(api_client)
    account = 'user@example.com' # str | An email address, to limit the function's results. (optional)
    dir = 'maildir' # str | A mail directory name, to limit results to specific directories.  **Note:**    If you pass the `default` or `mail` values, the function lists information for all mail directories. (optional)
    showdotfiles = 0 # int | Whether to include hidden files and directories. * `1` — Include hidden items. * `0` — Do **not** include hidden items. (optional) (default to 0)

    try:
        # Return mail directory's subdirectories and files
        api_response = api_instance.browse_mailbox(account=account, dir=dir, showdotfiles=showdotfiles)
        print("The response of EmailAccountsApi->browse_mailbox:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailAccountsApi->browse_mailbox: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account** | **str**| An email address, to limit the function&#39;s results. | [optional] 
 **dir** | **str**| A mail directory name, to limit results to specific directories.  **Note:**    If you pass the &#x60;default&#x60; or &#x60;mail&#x60; values, the function lists information for all mail directories. | [optional] 
 **showdotfiles** | **int**| Whether to include hidden files and directories. * &#x60;1&#x60; — Include hidden items. * &#x60;0&#x60; — Do **not** include hidden items. | [optional] [default to 0]

### Return type

[**InlineResponse200128**](InlineResponse200128.md)

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

# **c_sv_import_doimport**
> InlineResponse20057 c_sv_import_doimport(domain, id, type)

Import email accounts from CSV file

This function imports email accounts from an already uploaded CSV file.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response20057 import InlineResponse20057
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
    api_instance = clientapi_cpanel.EmailAccountsApi(api_client)
    domain = 'example.com' # str | The domain under which to add the email accounts.
    id = 'Leq58oid3sF3Moye3_YbJGqoMvCb7M4j' # str | The unique ID of the import operation. The cPanel API 2 CSVImport::uploadimport function generates this ID and stores it in the `CPVAR` attribute named `csvimportid`.
    type = 'email' # str | The type of email address to add.  * `email` — A regular email account. * `fwd` — A forwarder.

    try:
        # Import email accounts from CSV file
        api_response = api_instance.c_sv_import_doimport(domain, id, type)
        print("The response of EmailAccountsApi->c_sv_import_doimport:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailAccountsApi->c_sv_import_doimport: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**| The domain under which to add the email accounts. | 
 **id** | **str**| The unique ID of the import operation. The cPanel API 2 CSVImport::uploadimport function generates this ID and stores it in the &#x60;CPVAR&#x60; attribute named &#x60;csvimportid&#x60;. | 
 **type** | **str**| The type of email address to add.  * &#x60;email&#x60; — A regular email account. * &#x60;fwd&#x60; — A forwarder. | 

### Return type

[**InlineResponse20057**](InlineResponse20057.md)

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

# **count_auto_responders**
> InlineResponse200131 count_auto_responders()

Return cPanel account's autoresponders total

This function returns the number of [autoresponders](https://go.cpanel.net/Autoresponders) for every email address on a cPanel account.

**Important:**

  When you disable the [*Receive Mail* role](https://go.cpanel.net/serverroles#roles), the system **disables** this function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200131 import InlineResponse200131
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
    api_instance = clientapi_cpanel.EmailAccountsApi(api_client)

    try:
        # Return cPanel account's autoresponders total
        api_response = api_instance.count_auto_responders()
        print("The response of EmailAccountsApi->count_auto_responders:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailAccountsApi->count_auto_responders: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**InlineResponse200131**](InlineResponse200131.md)

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

# **count_pops**
> InlineResponse200135 count_pops()

Return cPanel account's email account total

This function returns the number of [email accounts](https://go.cpanel.net/cpaneldocsEmailAccounts) for a cPanel account.

**Important:**

  When you disable the [*Receive Mail* role](https://go.cpanel.net/serverroles#roles), the system **disables** this function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200135 import InlineResponse200135
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
    api_instance = clientapi_cpanel.EmailAccountsApi(api_client)

    try:
        # Return cPanel account's email account total
        api_response = api_instance.count_pops()
        print("The response of EmailAccountsApi->count_pops:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailAccountsApi->count_pops: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**InlineResponse200135**](InlineResponse200135.md)

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

# **delete_auto_responder**
> InlineResponse200136 delete_auto_responder(email)

Delete email account's autoresponder

This function deletes an autoresponder.

**Important:**

  When you disable the [*Receive Mail* role](https://go.cpanel.net/serverroles#roles), the system **disables** this function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200136 import InlineResponse200136
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
    api_instance = clientapi_cpanel.EmailAccountsApi(api_client)
    email = 'user@example.com' # str | The email account.

    try:
        # Delete email account's autoresponder
        api_response = api_instance.delete_auto_responder(email)
        print("The response of EmailAccountsApi->delete_auto_responder:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailAccountsApi->delete_auto_responder: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**| The email account. | 

### Return type

[**InlineResponse200136**](InlineResponse200136.md)

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

# **delete_held_messages**
> InlineResponse200140 delete_held_messages(email)

Delete email account's outgoing messages

This function deletes all outbound email messages held in the mail queue for the specified email account.

**Important:**

  When you disable the [*Receive Mail* role](https://go.cpanel.net/serverroles), the system **disables** this function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200140 import InlineResponse200140
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
    api_instance = clientapi_cpanel.EmailAccountsApi(api_client)
    email = 'username@example.com' # str | The email address to query.

    try:
        # Delete email account's outgoing messages
        api_response = api_instance.delete_held_messages(email)
        print("The response of EmailAccountsApi->delete_held_messages:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailAccountsApi->delete_held_messages: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**| The email address to query. | 

### Return type

[**InlineResponse200140**](InlineResponse200140.md)

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

# **delete_pop**
> InlineResponse200143 delete_pop(email, domain=domain, flags=flags, skip_quota=skip_quota)

Delete email address

This function deletes an email address.

**Important:**

  When you disable the [*Receive Mail* role](https://go.cpanel.net/serverroles), the system **disables** this function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200143 import InlineResponse200143
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
    api_instance = clientapi_cpanel.EmailAccountsApi(api_client)
    email = clientapi_cpanel.Email3() # Email3 | The email account username or address. * A valid email account username. For example, `user` if the email address is `user@example.com`. * A valid email address.
    domain = 'The cPanel account's main domain.' # str | The email account's domain. For example, `example.com` if the email address is `user@example.com`. (optional) (default to 'The cPanel account's main domain.')
    flags = 'passwd' # str | Whether to remove the mail account's home mail directory. If you do not specify a value, the function removes the mail account's home directory. * `passwd` — Preserve the mail account's home directory. * Any other value — Remove the mail account's home directory. (optional)
    skip_quota = 0 # int | Whether to modify the mail account's quota file. * `1` — Do **not** modify. * `0` — Modify. (optional) (default to 0)

    try:
        # Delete email address
        api_response = api_instance.delete_pop(email, domain=domain, flags=flags, skip_quota=skip_quota)
        print("The response of EmailAccountsApi->delete_pop:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailAccountsApi->delete_pop: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | [**Email3**](.md)| The email account username or address. * A valid email account username. For example, &#x60;user&#x60; if the email address is &#x60;user@example.com&#x60;. * A valid email address. | 
 **domain** | **str**| The email account&#39;s domain. For example, &#x60;example.com&#x60; if the email address is &#x60;user@example.com&#x60;. | [optional] [default to &#39;The cPanel account&#39;s main domain.&#39;]
 **flags** | **str**| Whether to remove the mail account&#39;s home mail directory. If you do not specify a value, the function removes the mail account&#39;s home directory. * &#x60;passwd&#x60; — Preserve the mail account&#39;s home directory. * Any other value — Remove the mail account&#39;s home directory. | [optional] 
 **skip_quota** | **int**| Whether to modify the mail account&#39;s quota file. * &#x60;1&#x60; — Do **not** modify. * &#x60;0&#x60; — Modify. | [optional] [default to 0]

### Return type

[**InlineResponse200143**](InlineResponse200143.md)

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

# **dispatch_client_settings**
> InlineResponse200149 dispatch_client_settings(account, to)

Send email client settings to an email address

This function sends an email account's client settings to an email address.

**Important:**

When you disable the [Receive Mail role](https://go.cpanel.net/serverroles), the system **disables** this function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200149 import InlineResponse200149
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
    api_instance = clientapi_cpanel.EmailAccountsApi(api_client)
    account = clientapi_cpanel.Account() # Account | The email account username or address for which to send client settings.
    to = 'user@example.com' # str | The email address to send client settings.

    try:
        # Send email client settings to an email address
        api_response = api_instance.dispatch_client_settings(account, to)
        print("The response of EmailAccountsApi->dispatch_client_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailAccountsApi->dispatch_client_settings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account** | [**Account**](.md)| The email account username or address for which to send client settings. | 
 **to** | **str**| The email address to send client settings. | 

### Return type

[**InlineResponse200149**](InlineResponse200149.md)

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

# **edit_pop_quota**
> InlineResponse200150 edit_pop_quota(domain, email, quota=quota)

Update email account's quota

This function changes an email address's quota.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200150 import InlineResponse200150
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
    api_instance = clientapi_cpanel.EmailAccountsApi(api_client)
    domain = 'example.com' # str | The email account's domain. Defaults to the cPanel account's main domain.
    email = 'user' # str | The email account username.
    quota = '500' # str | The maximum amount of disk space that the new email account may use. Defaults to the system value. * A positive integer that represents the maximum amount of disk space, in megabytes (MB).  **Note:**  You **cannot** enter a value that exceeds the maximum email quota. * `0` or `unlimited` — The account possesses unlimited disk space.  If the email account's quota value is set higher (or unlimited) than the account's max quota, the account's max quota will be applied instead of the value entered.  **Note:**  This value is only available to users without a maximum email account quota. (optional)

    try:
        # Update email account's quota
        api_response = api_instance.edit_pop_quota(domain, email, quota=quota)
        print("The response of EmailAccountsApi->edit_pop_quota:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailAccountsApi->edit_pop_quota: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**| The email account&#39;s domain. Defaults to the cPanel account&#39;s main domain. | 
 **email** | **str**| The email account username. | 
 **quota** | **str**| The maximum amount of disk space that the new email account may use. Defaults to the system value. * A positive integer that represents the maximum amount of disk space, in megabytes (MB).  **Note:**  You **cannot** enter a value that exceeds the maximum email quota. * &#x60;0&#x60; or &#x60;unlimited&#x60; — The account possesses unlimited disk space.  If the email account&#39;s quota value is set higher (or unlimited) than the account&#39;s max quota, the account&#39;s max quota will be applied instead of the value entered.  **Note:**  This value is only available to users without a maximum email account quota. | [optional] 

### Return type

[**InlineResponse200150**](InlineResponse200150.md)

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

# **email_terminate_mailbox_sessions**
> InlineResponse200207 email_terminate_mailbox_sessions()

Stop cPanel account IMAP and POP3 connections

This function terminates all IMAP and POP3 connections for a cPanel account.

**Note:**

This function ends connections for every email address, which includes the [default address](https://go.cpanel.net/cpaneldocsDefaultAddress).

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200207 import InlineResponse200207
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
    api_instance = clientapi_cpanel.EmailAccountsApi(api_client)

    try:
        # Stop cPanel account IMAP and POP3 connections
        api_response = api_instance.email_terminate_mailbox_sessions()
        print("The response of EmailAccountsApi->email_terminate_mailbox_sessions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailAccountsApi->email_terminate_mailbox_sessions: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**InlineResponse200207**](InlineResponse200207.md)

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

# **get_auto_responder**
> InlineResponse200159 get_auto_responder(email, temp_charset=temp_charset)

Return email account's autoresponder information

This function retrieves autoresponder information.

**Important:**

When you disable the [Receive Mail role](https://go.cpanel.net/serverroles), the system **disables** this function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200159 import InlineResponse200159
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
    api_instance = clientapi_cpanel.EmailAccountsApi(api_client)
    email = 'user' # str | The email account name.
    temp_charset = 'utf-8' # str | The autoresponder's [character set](https://en.wikipedia.org/wiki/Character_encoding). (optional) (default to 'utf-8')

    try:
        # Return email account's autoresponder information
        api_response = api_instance.get_auto_responder(email, temp_charset=temp_charset)
        print("The response of EmailAccountsApi->get_auto_responder:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailAccountsApi->get_auto_responder: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**| The email account name. | 
 **temp_charset** | **str**| The autoresponder&#39;s [character set](https://en.wikipedia.org/wiki/Character_encoding). | [optional] [default to &#39;utf-8&#39;]

### Return type

[**InlineResponse200159**](InlineResponse200159.md)

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

# **get_client_settings**
> InlineResponse200161 get_client_settings(account=account)

Return email account's client settings

This function retrieves an email account's client settings.

**Important:**

When you disable the [Receive Mail role](https://go.cpanel.net/serverroles), the system **disables** this function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200161 import InlineResponse200161
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
    api_instance = clientapi_cpanel.EmailAccountsApi(api_client)
    account = 'username@example.com' # str | The email address for which to send client settings.  **Note:**  This parameter defaults to the [system default email account](https://go.cpanel.net/systemdefaultemailaccount).  (optional)

    try:
        # Return email account's client settings
        api_response = api_instance.get_client_settings(account=account)
        print("The response of EmailAccountsApi->get_client_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailAccountsApi->get_client_settings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account** | **str**| The email address for which to send client settings.  **Note:**  This parameter defaults to the [system default email account](https://go.cpanel.net/systemdefaultemailaccount).  | [optional] 

### Return type

[**InlineResponse200161**](InlineResponse200161.md)

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

# **get_default_email_quota**
> InlineResponse200162 get_default_email_quota()

Return email account's default email quota

This function retrieves the account's default email quota size, in bytes format.

**Important:**

When you disable the [Receive Mail](https://go.cpanel.net/serverroles) role, the system **disables** this function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200162 import InlineResponse200162
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
    api_instance = clientapi_cpanel.EmailAccountsApi(api_client)

    try:
        # Return email account's default email quota
        api_response = api_instance.get_default_email_quota()
        print("The response of EmailAccountsApi->get_default_email_quota:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailAccountsApi->get_default_email_quota: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**InlineResponse200162**](InlineResponse200162.md)

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

# **get_default_email_quota_mib**
> InlineResponse200163 get_default_email_quota_mib()

Return email account's default email quota in MiB

This function retrieves the account's default email quota size in [mebibytes](https://en.wikipedia.org/wiki/Mebibyte) (MiB).

**Important:**

When you disable the [Receive Mail](https://go.cpanel.net/serverroles) role, the system **disables** this function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200163 import InlineResponse200163
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
    api_instance = clientapi_cpanel.EmailAccountsApi(api_client)

    try:
        # Return email account's default email quota in MiB
        api_response = api_instance.get_default_email_quota_mib()
        print("The response of EmailAccountsApi->get_default_email_quota_mib:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailAccountsApi->get_default_email_quota_mib: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**InlineResponse200163**](InlineResponse200163.md)

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

# **get_disk_usage**
> InlineResponse200164 get_disk_usage(domain, user)

Return email account's disk usage

This function retrieves the disk space that an email account uses.

**Important:**

When you disable the [Receive Mail role](https://go.cpanel.net/serverroles), the system **disables** this function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200164 import InlineResponse200164
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
    api_instance = clientapi_cpanel.EmailAccountsApi(api_client)
    domain = 'example.com' # str | The email account's domain.
    user = 'user' # str | The email account username.

    try:
        # Return email account's disk usage
        api_response = api_instance.get_disk_usage(domain, user)
        print("The response of EmailAccountsApi->get_disk_usage:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailAccountsApi->get_disk_usage: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**| The email account&#39;s domain. | 
 **user** | **str**| The email account username. | 

### Return type

[**InlineResponse200164**](InlineResponse200164.md)

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

# **get_held_message_count**
> InlineResponse200166 get_held_message_count(email=email)

Return email account's outgoing message count

This function returns the count of outbound email messages held in the mail queue for the specified email account.

**Important:**

When you disable the [Receive Mail role](https://go.cpanel.net/serverroles), the system **disables** this function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200166 import InlineResponse200166
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
    api_instance = clientapi_cpanel.EmailAccountsApi(api_client)
    email = 'username@example.com' # str | The email address to query. (optional)

    try:
        # Return email account's outgoing message count
        api_response = api_instance.get_held_message_count(email=email)
        print("The response of EmailAccountsApi->get_held_message_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailAccountsApi->get_held_message_count: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**| The email address to query. | [optional] 

### Return type

[**InlineResponse200166**](InlineResponse200166.md)

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

# **get_main_account_disk_usage**
> InlineResponse200170 get_main_account_disk_usage()

Return primary email account's disk usage

This function returns the disk space that the main account uses.

**Important:**

When you disable the [Receive Mail role](https://go.cpanel.net/serverroles), the system **disables** this function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200170 import InlineResponse200170
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
    api_instance = clientapi_cpanel.EmailAccountsApi(api_client)

    try:
        # Return primary email account's disk usage
        api_response = api_instance.get_main_account_disk_usage()
        print("The response of EmailAccountsApi->get_main_account_disk_usage:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailAccountsApi->get_main_account_disk_usage: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**InlineResponse200170**](InlineResponse200170.md)

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

# **get_main_account_disk_usage_bytes**
> InlineResponse200171 get_main_account_disk_usage_bytes()

Return primary email account's disk usage in bytes

This function returns the disk space that the cPanel account uses.

**Important:**

When you disable the [Receive Mail](https://go.cpanel.net/serverroles) role, the system **disables** this function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200171 import InlineResponse200171
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
    api_instance = clientapi_cpanel.EmailAccountsApi(api_client)

    try:
        # Return primary email account's disk usage in bytes
        api_response = api_instance.get_main_account_disk_usage_bytes()
        print("The response of EmailAccountsApi->get_main_account_disk_usage_bytes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailAccountsApi->get_main_account_disk_usage_bytes: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**InlineResponse200171**](InlineResponse200171.md)

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

# **get_max_email_quota**
> InlineResponse200172 get_max_email_quota()

Return email account's max quota size

This function retrieves the account's maximum email quota size, in bytes format.

**Important:**

  When you disable the [Receive Mail](https://go.cpanel.net/serverroles) role, the system **disables** this function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200172 import InlineResponse200172
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
    api_instance = clientapi_cpanel.EmailAccountsApi(api_client)

    try:
        # Return email account's max quota size
        api_response = api_instance.get_max_email_quota()
        print("The response of EmailAccountsApi->get_max_email_quota:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailAccountsApi->get_max_email_quota: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**InlineResponse200172**](InlineResponse200172.md)

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

# **get_max_email_quota_mib**
> InlineResponse200173 get_max_email_quota_mib()

Return email account's max quota size in MiB

This function retrieves the account's maximum email account quota size, in
[Mebibytes (MiB)](https://en.wikipedia.org/wiki/Mebibyte) format.

**Important:**

When you disable the [Receive Mail role](https://go.cpanel.net/howtouseserverprofiles#roles),
the system **disables** this function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200173 import InlineResponse200173
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
    api_instance = clientapi_cpanel.EmailAccountsApi(api_client)

    try:
        # Return email account's max quota size in MiB
        api_response = api_instance.get_max_email_quota_mib()
        print("The response of EmailAccountsApi->get_max_email_quota_mib:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailAccountsApi->get_max_email_quota_mib: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**InlineResponse200173**](InlineResponse200173.md)

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

# **get_pop_quota**
> InlineResponse200174 get_pop_quota(email, as_bytes=as_bytes, domain=domain)

Return email account's quota

This function retrieves an email account's quota.

**Important:**

When you disable the [Receive Mail](https://go.cpanel.net/serverroles) role, the system **disables** this function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200174 import InlineResponse200174
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
    api_instance = clientapi_cpanel.EmailAccountsApi(api_client)
    email = 'user' # str | The email account username.  For example, user if the email address is user@example.com.
    as_bytes = 0 # int | Whether to return the quota as bytes.  * `1` — Return the quota as bytes. * `0` — Return the quota as megabytes (MB). (optional) (default to 0)
    domain = 'example.com' # str | The email account's domain. This parameter defaults to the cPanel account's main domain. (optional)

    try:
        # Return email account's quota
        api_response = api_instance.get_pop_quota(email, as_bytes=as_bytes, domain=domain)
        print("The response of EmailAccountsApi->get_pop_quota:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailAccountsApi->get_pop_quota: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**| The email account username.  For example, user if the email address is user@example.com. | 
 **as_bytes** | **int**| Whether to return the quota as bytes.  * &#x60;1&#x60; — Return the quota as bytes. * &#x60;0&#x60; — Return the quota as megabytes (MB). | [optional] [default to 0]
 **domain** | **str**| The email account&#39;s domain. This parameter defaults to the cPanel account&#39;s main domain. | [optional] 

### Return type

[**InlineResponse200174**](InlineResponse200174.md)

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

# **get_webmail_settings**
> InlineResponse200176 get_webmail_settings(account=account)

Return email account's Webmail settings

This function retrieves an email account's Webmail settings.

**Important:**

When you disable the [_Receive Mail_ role](https://go.cpanel.net/serverroles), the system **disables** this function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200176 import InlineResponse200176
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
    api_instance = clientapi_cpanel.EmailAccountsApi(api_client)
    account = clientapi_cpanel.Account1() # Account1 | The email account.  **Note:**  If you do **not** specify a value, the function retrieves settings for the cPanel account's default mail account. (optional)

    try:
        # Return email account's Webmail settings
        api_response = api_instance.get_webmail_settings(account=account)
        print("The response of EmailAccountsApi->get_webmail_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailAccountsApi->get_webmail_settings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account** | [**Account1**](.md)| The email account.  **Note:**  If you do **not** specify a value, the function retrieves settings for the cPanel account&#39;s default mail account. | [optional] 

### Return type

[**InlineResponse200176**](InlineResponse200176.md)

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

# **hold_outgoing**
> InlineResponse200179 hold_outgoing(email)

Stop email account's outgoing mail

This function sets Exim's queue to not send outgoing mail from an email account.

**Notes:**

* To send all mail from the queue, use the UAPI `Email::release_outgoing` function.
* To reject outgoing mail and not place mail in a queue, use the UAPI `Email::suspend_outgoing` function.
* This function does **not** hold local outgoing mail.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200179 import InlineResponse200179
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
    api_instance = clientapi_cpanel.EmailAccountsApi(api_client)
    email = 'username@example.com' # str | The email account's username.

    try:
        # Stop email account's outgoing mail
        api_response = api_instance.hold_outgoing(email)
        print("The response of EmailAccountsApi->hold_outgoing:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailAccountsApi->hold_outgoing: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**| The email account&#39;s username. | 

### Return type

[**InlineResponse200179**](InlineResponse200179.md)

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

# **list_auto_responders**
> InlineResponse200180 list_auto_responders(domain, regex=regex)

Return domain's autoresponders

This function lists a domain's autoresponders.

**Important:**

  When you disable the [*Receive Mail* role](https://go.cpanel.net/serverroles), the system **disables** this function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200180 import InlineResponse200180
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
    api_instance = clientapi_cpanel.EmailAccountsApi(api_client)
    domain = 'example.com' # str | The domain name.
    regex = 'user' # str | A [Perl Compatible Regular Expression (PCRE)](https://en.wikipedia.org/wiki/Perl_Compatible_Regular_Expressions) that filters the results. (optional)

    try:
        # Return domain's autoresponders
        api_response = api_instance.list_auto_responders(domain, regex=regex)
        print("The response of EmailAccountsApi->list_auto_responders:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailAccountsApi->list_auto_responders: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**| The domain name. | 
 **regex** | **str**| A [Perl Compatible Regular Expression (PCRE)](https://en.wikipedia.org/wiki/Perl_Compatible_Regular_Expressions) that filters the results. | [optional] 

### Return type

[**InlineResponse200180**](InlineResponse200180.md)

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

# **list_default_address**
> InlineResponse200181 list_default_address(user, domain=domain)

Return domain's default email address

This function retrieves a domain's default address.

**Important:**

  When you disable the [*Receive Mail* role](https://go.cpanel.net/serverroles), the system **disables** this function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200181 import InlineResponse200181
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
    api_instance = clientapi_cpanel.EmailAccountsApi(api_client)
    user = 'user' # str | The user whose default addresses to list.
    domain = 'example.com' # str | The domain. If you do not specify a value, the function lists default addresses for all of the cPanel account's domains. (optional)

    try:
        # Return domain's default email address
        api_response = api_instance.list_default_address(user, domain=domain)
        print("The response of EmailAccountsApi->list_default_address:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailAccountsApi->list_default_address: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | **str**| The user whose default addresses to list. | 
 **domain** | **str**| The domain. If you do not specify a value, the function lists default addresses for all of the cPanel account&#39;s domains. | [optional] 

### Return type

[**InlineResponse200181**](InlineResponse200181.md)

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

# **list_mail_domains**
> InlineResponse200188 list_mail_domains(add_www=add_www, include_wildcard=include_wildcard, select=select)

Return cPanel account's mail domains

This function lists the account's mail domains.

**Important:**

  When you disable the [*Receive Mail* role](https://go.cpanel.net/serverroles), the system **disables** this function.

**Note:**

  This function **always** returns the account's main domain first.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200188 import InlineResponse200188
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
    api_instance = clientapi_cpanel.EmailAccountsApi(api_client)
    add_www = 0 # int | Whether to list `www.` addresses. * `1` — List `www.` addresses. * `0` — Do **not** list `www.` addresses. For example, if you specify `1`, the function's output would include both `example.com` and `www.example.com`. If you specify `0`, the output would include **only** `example.com`. (optional) (default to 0)
    include_wildcard = 0 # int | Whether to list wildcard addresses. * `1` — List wildcard addresses. * `0` — Do **not** list wildcard addresses. For example, if you specify `1`, the function's output would include both `example.com` and `*.example.com`. If you specify `0`, the output would include **only** `example.com`. (optional) (default to 0)
    select = 'example.com' # str | The name of the domain that the function returns with the `select `output parameter. If you do **not** use this parameter, the function will **not** return the `select` parameter with any domains. (optional)

    try:
        # Return cPanel account's mail domains
        api_response = api_instance.list_mail_domains(add_www=add_www, include_wildcard=include_wildcard, select=select)
        print("The response of EmailAccountsApi->list_mail_domains:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailAccountsApi->list_mail_domains: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **add_www** | **int**| Whether to list &#x60;www.&#x60; addresses. * &#x60;1&#x60; — List &#x60;www.&#x60; addresses. * &#x60;0&#x60; — Do **not** list &#x60;www.&#x60; addresses. For example, if you specify &#x60;1&#x60;, the function&#39;s output would include both &#x60;example.com&#x60; and &#x60;www.example.com&#x60;. If you specify &#x60;0&#x60;, the output would include **only** &#x60;example.com&#x60;. | [optional] [default to 0]
 **include_wildcard** | **int**| Whether to list wildcard addresses. * &#x60;1&#x60; — List wildcard addresses. * &#x60;0&#x60; — Do **not** list wildcard addresses. For example, if you specify &#x60;1&#x60;, the function&#39;s output would include both &#x60;example.com&#x60; and &#x60;*.example.com&#x60;. If you specify &#x60;0&#x60;, the output would include **only** &#x60;example.com&#x60;. | [optional] [default to 0]
 **select** | **str**| The name of the domain that the function returns with the &#x60;select &#x60;output parameter. If you do **not** use this parameter, the function will **not** return the &#x60;select&#x60; parameter with any domains. | [optional] 

### Return type

[**InlineResponse200188**](InlineResponse200188.md)

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

# **list_pops**
> InlineResponse200190 list_pops(no_validate=no_validate, regex=regex, skip_main=skip_main)

Return email accounts

This function lists the cPanel account's email accounts.

**Important:**

  When you disable the [*Receive Mail* role](https://go.cpanel.net/serverroles), the system **disables** this function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200190 import InlineResponse200190
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
    api_instance = clientapi_cpanel.EmailAccountsApi(api_client)
    no_validate = 0 # int | Whether to skip the email database's validation check. * `1` — Skip the validation check. * `0` — Run the validation check. (optional) (default to 0)
    regex = 'user' # str | A [Perl Compatible Regular Expression (PCRE)](https://en.wikipedia.org/wiki/Perl_Compatible_Regular_Expressions) that filters the results. (optional)
    skip_main = 0 # int | Whether to exclude the cPanel account's main account from the results. * `1` — Exclude the main account. * `0` — Include the main account. (optional) (default to 0)

    try:
        # Return email accounts
        api_response = api_instance.list_pops(no_validate=no_validate, regex=regex, skip_main=skip_main)
        print("The response of EmailAccountsApi->list_pops:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailAccountsApi->list_pops: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **no_validate** | **int**| Whether to skip the email database&#39;s validation check. * &#x60;1&#x60; — Skip the validation check. * &#x60;0&#x60; — Run the validation check. | [optional] [default to 0]
 **regex** | **str**| A [Perl Compatible Regular Expression (PCRE)](https://en.wikipedia.org/wiki/Perl_Compatible_Regular_Expressions) that filters the results. | [optional] 
 **skip_main** | **int**| Whether to exclude the cPanel account&#39;s main account from the results. * &#x60;1&#x60; — Exclude the main account. * &#x60;0&#x60; — Include the main account. | [optional] [default to 0]

### Return type

[**InlineResponse200190**](InlineResponse200190.md)

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

# **list_pops_with_disk**
> InlineResponse200191 list_pops_with_disk(domain=domain, email=email, get_restrictions=get_restrictions, infinityimg=infinityimg, infinitylang=infinitylang, maxaccounts=maxaccounts, no_disk=no_disk, no_validate=no_validate, regex=regex)

Return email accounts with disk information

This function lists the cPanel account's email accounts with disk information.

**Important:**

  When you disable the [*Receive Mail* role](https://go.cpanel.net/serverroles), the system **disables** this function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200191 import InlineResponse200191
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
    api_instance = clientapi_cpanel.EmailAccountsApi(api_client)
    domain = 'example.com' # str | A domain name to filter the results by. If you do **not** use this parameter, the function returns **all** of the cPanel account's email addresses. (optional)
    email = 'user' # str | The cPanel user account to query. If you do **not** use this parameter, the function returns the email addresses for **all** cPanel accounts that the user owns.  **Note:**   To retrieve information for a single email address, add the domain parameter. For example, `email=user&domain=example.com` will return information for the email address `user@example.com`. (optional)
    get_restrictions = 0 # int | Whether to display restriction status for each of the email addresses. * `1` — Display. * `0` — Do **not** display. (optional) (default to 0)
    infinityimg = 'images/myimg.jpg' # str | An image to display for email addresses with an unlimited quota. If you specify an `infinityimg` value, the function returns HTML code to display that image as the `diskquota` parameter's value. (optional)
    infinitylang = 0 # int | Whether to return the `∞` character for email addresses with an unlimited quota. * `1` — Return the `∞` character for unlimited `diskquota` values. * `0` — Return the string `unlimited` for unlimited `diskquota` values.  **Note:**   If you specify `1` for this parameter **and** the `infinityimg` parameter, the function ignores **this** parameter and returns HTML code for unlimited `diskquota` values. (optional) (default to 0)
    maxaccounts = 500 # int | The maximum number of email addresses to return. If you do not use this parameter, the function returns an unlimited number of email addresses. (optional)
    no_disk = 0 # int | Whether to skip the collection of disk usage information. * `1` — Do **not** collect. * `0` — Collect. (optional) (default to 0)
    no_validate = 0 # int | Whether to skip email database validation. * `1` — Skip validation. * `0` — Perform the validation. (optional) (default to 0)
    regex = 'An empty string' # str | A [Perl Compatible Regular Expression (PCRE)](https://en.wikipedia.org/wiki/Perl_Compatible_Regular_Expressions) that filters the results. For example, `/^[a-z0-9_-]{6,18}$/` matches the local portion of an email address, if it contains between six and 18 characters. (optional) (default to 'An empty string')

    try:
        # Return email accounts with disk information
        api_response = api_instance.list_pops_with_disk(domain=domain, email=email, get_restrictions=get_restrictions, infinityimg=infinityimg, infinitylang=infinitylang, maxaccounts=maxaccounts, no_disk=no_disk, no_validate=no_validate, regex=regex)
        print("The response of EmailAccountsApi->list_pops_with_disk:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailAccountsApi->list_pops_with_disk: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**| A domain name to filter the results by. If you do **not** use this parameter, the function returns **all** of the cPanel account&#39;s email addresses. | [optional] 
 **email** | **str**| The cPanel user account to query. If you do **not** use this parameter, the function returns the email addresses for **all** cPanel accounts that the user owns.  **Note:**   To retrieve information for a single email address, add the domain parameter. For example, &#x60;email&#x3D;user&amp;domain&#x3D;example.com&#x60; will return information for the email address &#x60;user@example.com&#x60;. | [optional] 
 **get_restrictions** | **int**| Whether to display restriction status for each of the email addresses. * &#x60;1&#x60; — Display. * &#x60;0&#x60; — Do **not** display. | [optional] [default to 0]
 **infinityimg** | **str**| An image to display for email addresses with an unlimited quota. If you specify an &#x60;infinityimg&#x60; value, the function returns HTML code to display that image as the &#x60;diskquota&#x60; parameter&#39;s value. | [optional] 
 **infinitylang** | **int**| Whether to return the &#x60;∞&#x60; character for email addresses with an unlimited quota. * &#x60;1&#x60; — Return the &#x60;∞&#x60; character for unlimited &#x60;diskquota&#x60; values. * &#x60;0&#x60; — Return the string &#x60;unlimited&#x60; for unlimited &#x60;diskquota&#x60; values.  **Note:**   If you specify &#x60;1&#x60; for this parameter **and** the &#x60;infinityimg&#x60; parameter, the function ignores **this** parameter and returns HTML code for unlimited &#x60;diskquota&#x60; values. | [optional] [default to 0]
 **maxaccounts** | **int**| The maximum number of email addresses to return. If you do not use this parameter, the function returns an unlimited number of email addresses. | [optional] 
 **no_disk** | **int**| Whether to skip the collection of disk usage information. * &#x60;1&#x60; — Do **not** collect. * &#x60;0&#x60; — Collect. | [optional] [default to 0]
 **no_validate** | **int**| Whether to skip email database validation. * &#x60;1&#x60; — Skip validation. * &#x60;0&#x60; — Perform the validation. | [optional] [default to 0]
 **regex** | **str**| A [Perl Compatible Regular Expression (PCRE)](https://en.wikipedia.org/wiki/Perl_Compatible_Regular_Expressions) that filters the results. For example, &#x60;/^[a-z0-9_-]{6,18}$/&#x60; matches the local portion of an email address, if it contains between six and 18 characters. | [optional] [default to &#39;An empty string&#39;]

### Return type

[**InlineResponse200191**](InlineResponse200191.md)

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

# **passwd_pop**
> InlineResponse200194 passwd_pop(email, password, domain=domain)

Update email account password

This function changes an email account's password.

**Important:**

When you disable the [Receive Mail role](https://go.cpanel.net/serverroles), the system **disables** this function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200194 import InlineResponse200194
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
    api_instance = clientapi_cpanel.EmailAccountsApi(api_client)
    email = clientapi_cpanel.Email4() # Email4 | The email account username or address.
    password = '12345luggage' # str | The email account password.
    domain = 'the cPanel account's main domain' # str | The email account's domain. (optional) (default to 'the cPanel account's main domain')

    try:
        # Update email account password
        api_response = api_instance.passwd_pop(email, password, domain=domain)
        print("The response of EmailAccountsApi->passwd_pop:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailAccountsApi->passwd_pop: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | [**Email4**](.md)| The email account username or address. | 
 **password** | **str**| The email account password. | 
 **domain** | **str**| The email account&#39;s domain. | [optional] [default to &#39;the cPanel account&#39;s main domain&#39;]

### Return type

[**InlineResponse200194**](InlineResponse200194.md)

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

# **release_outgoing**
> InlineResponse200195 release_outgoing(email)

Start email account outgoing mail

This function sends all of the outgoing mail from Exim's queue for an email account.

**Note:**

To set Exim to queue all outgoing mail for an email account, use the UAPI `Email::hold_outgoing` function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200195 import InlineResponse200195
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
    api_instance = clientapi_cpanel.EmailAccountsApi(api_client)
    email = 'username@example.com' # str | The email account's username.

    try:
        # Start email account outgoing mail
        api_response = api_instance.release_outgoing(email)
        print("The response of EmailAccountsApi->release_outgoing:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailAccountsApi->release_outgoing: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**| The email account&#39;s username. | 

### Return type

[**InlineResponse200195**](InlineResponse200195.md)

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

# **set_default_address**
> InlineResponse200199 set_default_address(fwdopt, domain=domain, failmsgs=failmsgs, fwdemail=fwdemail, pipefwd=pipefwd)

Create default email address

This function configures a default (catchall) email address.

**Important**:

  When you disable the [Mail Receive role](https://go.cpanel.net/serverroles), the system **disables** this function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200199 import InlineResponse200199
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
    api_instance = clientapi_cpanel.EmailAccountsApi(api_client)
    fwdopt = 'fwd' # str | The method to use to handle unroutable mail. * `fwd` — Forward messages to the `fwdemail` parameter’s address. * `fail` — Bounce messages back to the sender, and include the `failmsgs` parameter’s failure message. * `blackhole` — Send messages to the `/dev/null/` directory. This method does **not** generate a failure notice. * `pipe` — Pipe mail to the `pipefwd` parameter’s application. This parameter requires the [File Storage role](https://go.cpanel.net/serverroles).
    domain = 'example.com' # str | The domain whose default email behavior you want to configure.  **Note**:    This parameter defaults to the cPanel account’s main domain. (optional)
    failmsgs = 'No such person at this address' # str | The failure message for the message’s sender.  **Note**:   Use this parameter if you used the `fail` method for the `fwdopt` parameter. (optional) (default to 'No such person at this address')
    fwdemail = 'admin@example.com' # str | The email address to which the system forwards messages.  **Note**:   Use this parameter if you used the `fwd` method for the `fwdopt` parameter. (optional)
    pipefwd = 'mailscript.pl' # str | The application to which the system pipes messages.  **Note**:    Use this parameter if you used the `pipe` method for the `fwdopt` parameter.  **Important**:    This parameter requires the [File Storage role](https://go.cpanel.net/serverroles). (optional)

    try:
        # Create default email address
        api_response = api_instance.set_default_address(fwdopt, domain=domain, failmsgs=failmsgs, fwdemail=fwdemail, pipefwd=pipefwd)
        print("The response of EmailAccountsApi->set_default_address:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailAccountsApi->set_default_address: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fwdopt** | **str**| The method to use to handle unroutable mail. * &#x60;fwd&#x60; — Forward messages to the &#x60;fwdemail&#x60; parameter’s address. * &#x60;fail&#x60; — Bounce messages back to the sender, and include the &#x60;failmsgs&#x60; parameter’s failure message. * &#x60;blackhole&#x60; — Send messages to the &#x60;/dev/null/&#x60; directory. This method does **not** generate a failure notice. * &#x60;pipe&#x60; — Pipe mail to the &#x60;pipefwd&#x60; parameter’s application. This parameter requires the [File Storage role](https://go.cpanel.net/serverroles). | 
 **domain** | **str**| The domain whose default email behavior you want to configure.  **Note**:    This parameter defaults to the cPanel account’s main domain. | [optional] 
 **failmsgs** | **str**| The failure message for the message’s sender.  **Note**:   Use this parameter if you used the &#x60;fail&#x60; method for the &#x60;fwdopt&#x60; parameter. | [optional] [default to &#39;No such person at this address&#39;]
 **fwdemail** | **str**| The email address to which the system forwards messages.  **Note**:   Use this parameter if you used the &#x60;fwd&#x60; method for the &#x60;fwdopt&#x60; parameter. | [optional] 
 **pipefwd** | **str**| The application to which the system pipes messages.  **Note**:    Use this parameter if you used the &#x60;pipe&#x60; method for the &#x60;fwdopt&#x60; parameter.  **Important**:    This parameter requires the [File Storage role](https://go.cpanel.net/serverroles). | [optional] 

### Return type

[**InlineResponse200199**](InlineResponse200199.md)

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

# **set_manual_mx_redirects**
> InlineResponse200201 set_manual_mx_redirects(domain, mx_host)

Add manual MX redirection

This function lets you create a manual Exim mail exchanger (MX) redirect for a domain.
An MX redirection lets you bypass the domain's MX lookup via the Domain Name System (DNS).
This function adds the manual redirect entries to the `/etc/manualmx` file.

**Note:**

  To remove a domain's manual MX redirection, use the UAPI Email `unset_manual_mx_redirect` function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200201 import InlineResponse200201
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
    api_instance = clientapi_cpanel.EmailAccountsApi(api_client)
    domain = '\'example.com\'' # str | The domain for which to add a manual MX redirect entry.  **Note:**  * To add multiple domain entries, increment the parameter. For example, use the `domain`, `domain-1`, and `domain-2` parameters. * For multiple domains, you **must** include its corresponding `mx_host` value.
    mx_host = clientapi_cpanel.MxHost() # MxHost | The domain, IPv4, or IPv6 address to redirect the domain value's emails to.  **Note:**   * To add multiple MX hosts, increment the parameter. For example, use the `mx_host`, `mx_host-1`, and `mx_host-2` parameters.  * For multiple MX hosts, you **must** include its corresponding `domain` value.

    try:
        # Add manual MX redirection
        api_response = api_instance.set_manual_mx_redirects(domain, mx_host)
        print("The response of EmailAccountsApi->set_manual_mx_redirects:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailAccountsApi->set_manual_mx_redirects: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**| The domain for which to add a manual MX redirect entry.  **Note:**  * To add multiple domain entries, increment the parameter. For example, use the &#x60;domain&#x60;, &#x60;domain-1&#x60;, and &#x60;domain-2&#x60; parameters. * For multiple domains, you **must** include its corresponding &#x60;mx_host&#x60; value. | 
 **mx_host** | [**MxHost**](.md)| The domain, IPv4, or IPv6 address to redirect the domain value&#39;s emails to.  **Note:**   * To add multiple MX hosts, increment the parameter. For example, use the &#x60;mx_host&#x60;, &#x60;mx_host-1&#x60;, and &#x60;mx_host-2&#x60; parameters.  * For multiple MX hosts, you **must** include its corresponding &#x60;domain&#x60; value. | 

### Return type

[**InlineResponse200201**](InlineResponse200201.md)

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

# **trace_delivery**
> InlineResponse200208 trace_delivery(recipient)

Run email delivery route trace

This function traces the email delivery route to an email account.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200208 import InlineResponse200208
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
    api_instance = clientapi_cpanel.EmailAccountsApi(api_client)
    recipient = 'username@example.com' # str | The email address to which to trace a message delivery path.

    try:
        # Run email delivery route trace
        api_response = api_instance.trace_delivery(recipient)
        print("The response of EmailAccountsApi->trace_delivery:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailAccountsApi->trace_delivery: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **recipient** | **str**| The email address to which to trace a message delivery path. | 

### Return type

[**InlineResponse200208**](InlineResponse200208.md)

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

# **unset_manual_mx_redirects**
> InlineResponse200210 unset_manual_mx_redirects(domain)

Remove manual MX redirection

This function lets you create a manual Exim mail exchanger (MX) redirect for a domain.
An MX redirection lets you bypass the domain's MX lookup via the Domain Name System (DNS).
This function adds the manual redirect entries to the `/etc/manualmx` file.

**Note:**

  To remove a domain's manual MX redirection, use the UAPI Email `unset_manual_mx_redirect` function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200210 import InlineResponse200210
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
    api_instance = clientapi_cpanel.EmailAccountsApi(api_client)
    domain = '\'example.com\'' # str | The domain for which to add a manual MX redirect entry.  **Note:**  * To add multiple domain entries, increment the parameter. For example, use the `domain`, `domain-1`, and `domain-2` parameters. * For multiple domains, you **must** include its corresponding `mx_host` value.

    try:
        # Remove manual MX redirection
        api_response = api_instance.unset_manual_mx_redirects(domain)
        print("The response of EmailAccountsApi->unset_manual_mx_redirects:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailAccountsApi->unset_manual_mx_redirects: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**| The domain for which to add a manual MX redirect entry.  **Note:**  * To add multiple domain entries, increment the parameter. For example, use the &#x60;domain&#x60;, &#x60;domain-1&#x60;, and &#x60;domain-2&#x60; parameters. * For multiple domains, you **must** include its corresponding &#x60;mx_host&#x60; value. | 

### Return type

[**InlineResponse200210**](InlineResponse200210.md)

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

# **verify_password**
> InlineResponse200214 verify_password(email, password)

Validate email account password

This function verifies the password for an email account.

**Important:**

When you disable the [Receive Mail role](https://go.cpanel.net/serverroles), the system **disables** this function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200214 import InlineResponse200214
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
    api_instance = clientapi_cpanel.EmailAccountsApi(api_client)
    email = 'username@example.com' # str | The email account address.
    password = '123456luggage' # str | The email account password.

    try:
        # Validate email account password
        api_response = api_instance.verify_password(email, password)
        print("The response of EmailAccountsApi->verify_password:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailAccountsApi->verify_password: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**| The email account address. | 
 **password** | **str**| The email account password. | 

### Return type

[**InlineResponse200214**](InlineResponse200214.md)

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

