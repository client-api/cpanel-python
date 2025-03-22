# clientapi_cpanel.EmailApi

All URIs are relative to *https://cpanel-server.tld:2083/execute*

Method | HTTP request | Description
------------- | ------------- | -------------
[**account_name**](EmailApi.md#account_name) | **GET** /Email/account_name | Return current user&#39;s account name
[**add_auto_responder**](EmailApi.md#add_auto_responder) | **GET** /Email/add_auto_responder | Create email account&#39;s autoresponder
[**add_domain_forwarder**](EmailApi.md#add_domain_forwarder) | **GET** /Email/add_domain_forwarder | Create domain-level forwarder
[**add_forwarder**](EmailApi.md#add_forwarder) | **GET** /Email/add_forwarder | Create email account forwarder
[**add_list**](EmailApi.md#add_list) | **GET** /Email/add_list | Create mailing list
[**add_mailman_delegates**](EmailApi.md#add_mailman_delegates) | **GET** /Email/add_mailman_delegates | Add administrators to mailing list
[**add_pop**](EmailApi.md#add_pop) | **GET** /Email/add_pop | Create email address
[**add_spam_filter**](EmailApi.md#add_spam_filter) | **GET** /Email/add_spam_filter | Update minimum spam score threshold value
[**browse_mailbox**](EmailApi.md#browse_mailbox) | **GET** /Email/browse_mailbox | Return mail directory&#39;s subdirectories and files
[**check_fastmail**](EmailApi.md#check_fastmail) | **GET** /Email/check_fastmail | Return BlackBerry FastMail support status
[**count_auto_responders**](EmailApi.md#count_auto_responders) | **GET** /Email/count_auto_responders | Return cPanel account&#39;s autoresponders total
[**count_filters**](EmailApi.md#count_filters) | **GET** /Email/count_filters | Return cPanel account&#39;s email filters total
[**count_forwarders**](EmailApi.md#count_forwarders) | **GET** /Email/count_forwarders | Return cPanel account&#39;s mail forwarder total
[**count_lists**](EmailApi.md#count_lists) | **GET** /Email/count_lists | Return cPanel account&#39;s mailing list total
[**count_pops**](EmailApi.md#count_pops) | **GET** /Email/count_pops | Return cPanel account&#39;s email account total
[**delete_auto_responder**](EmailApi.md#delete_auto_responder) | **GET** /Email/delete_auto_responder | Delete email account&#39;s autoresponder
[**delete_domain_forwarder**](EmailApi.md#delete_domain_forwarder) | **GET** /Email/delete_domain_forwarder | Delete domain-level forwarder
[**delete_filter**](EmailApi.md#delete_filter) | **GET** /Email/delete_filter | Delete email account&#39;s email filter
[**delete_forwarder**](EmailApi.md#delete_forwarder) | **GET** /Email/delete_forwarder | Delete email account&#39;s email forwarder
[**delete_held_messages**](EmailApi.md#delete_held_messages) | **GET** /Email/delete_held_messages | Delete email account&#39;s outgoing messages
[**delete_list**](EmailApi.md#delete_list) | **GET** /Email/delete_list | Delete mailing list
[**delete_pop**](EmailApi.md#delete_pop) | **GET** /Email/delete_pop | Delete email address
[**disable_filter**](EmailApi.md#disable_filter) | **GET** /Email/disable_filter | Disable email filter for email account
[**disable_mailbox_autocreate**](EmailApi.md#disable_mailbox_autocreate) | **GET** /Email/disable_mailbox_autocreate | Disable cPanel account mailbox autocreation
[**disable_spam_assassin**](EmailApi.md#disable_spam_assassin) | **GET** /Email/disable_spam_assassin | Disable Apache SpamAssassin for cPanel account
[**disable_spam_autodelete**](EmailApi.md#disable_spam_autodelete) | **GET** /Email/disable_spam_autodelete | Disable spam box filtering auto-delete
[**disable_spam_box**](EmailApi.md#disable_spam_box) | **GET** /Email/disable_spam_box | Disable spam box filtering for cPanel account
[**dispatch_client_settings**](EmailApi.md#dispatch_client_settings) | **GET** /Email/dispatch_client_settings | Send email client settings to an email address
[**edit_pop_quota**](EmailApi.md#edit_pop_quota) | **GET** /Email/edit_pop_quota | Update email account&#39;s quota
[**email_terminate_mailbox_sessions**](EmailApi.md#email_terminate_mailbox_sessions) | **GET** /Email/terminate_mailbox_sessions | Stop cPanel account IMAP and POP3 connections
[**enable_filter**](EmailApi.md#enable_filter) | **GET** /Email/enable_filter | Enable email filter for email account
[**enable_mailbox_autocreate**](EmailApi.md#enable_mailbox_autocreate) | **GET** /Email/enable_mailbox_autocreate | Enable cPanel account mailbox autocreation
[**enable_spam_assassin**](EmailApi.md#enable_spam_assassin) | **GET** /Email/enable_spam_assassin | Enable Apache SpamAssassin for cPanel account
[**enable_spam_box**](EmailApi.md#enable_spam_box) | **GET** /Email/enable_spam_box | Enable spam box filtering for cPanel account
[**export_lists**](EmailApi.md#export_lists) | **GET** /Email/export_lists | Export cPanel account&#39;s Mailman mailing lists to a file
[**fetch_charmaps**](EmailApi.md#fetch_charmaps) | **GET** /Email/fetch_charmaps | Return server&#39;s supported character encodings
[**fts_rescan_mailbox**](EmailApi.md#fts_rescan_mailbox) | **GET** /Email/fts_rescan_mailbox | Start IMAP Full-Text Search scan for email account
[**generate_mailman_otp**](EmailApi.md#generate_mailman_otp) | **GET** /Email/generate_mailman_otp | Create one-time password for a mailing list
[**get_auto_responder**](EmailApi.md#get_auto_responder) | **GET** /Email/get_auto_responder | Return email account&#39;s autoresponder information
[**get_charsets**](EmailApi.md#get_charsets) | **GET** /Email/get_charsets | Return mail server&#39;s supported character encodings
[**get_client_settings**](EmailApi.md#get_client_settings) | **GET** /Email/get_client_settings | Return email account&#39;s client settings
[**get_default_email_quota**](EmailApi.md#get_default_email_quota) | **GET** /Email/get_default_email_quota | Return email account&#39;s default email quota
[**get_default_email_quota_mib**](EmailApi.md#get_default_email_quota_mib) | **GET** /Email/get_default_email_quota_mib | Return email account&#39;s default email quota in MiB
[**get_disk_usage**](EmailApi.md#get_disk_usage) | **GET** /Email/get_disk_usage | Return email account&#39;s disk usage
[**get_filter**](EmailApi.md#get_filter) | **GET** /Email/get_filter | Return email filter&#39;s information
[**get_held_message_count**](EmailApi.md#get_held_message_count) | **GET** /Email/get_held_message_count | Return email account&#39;s outgoing message count
[**get_lists_total_disk_usage**](EmailApi.md#get_lists_total_disk_usage) | **GET** /Email/get_lists_total_disk_usage | Return cPanel account&#39;s mailing list disk usage
[**get_mailbox_autocreate**](EmailApi.md#get_mailbox_autocreate) | **GET** /Email/get_mailbox_autocreate | Return cPanel account&#39;s mailbox autocreate status
[**get_mailman_delegates**](EmailApi.md#get_mailman_delegates) | **GET** /Email/get_mailman_delegates | Return mailing list administrators
[**get_main_account_disk_usage**](EmailApi.md#get_main_account_disk_usage) | **GET** /Email/get_main_account_disk_usage | Return primary email account&#39;s disk usage
[**get_main_account_disk_usage_bytes**](EmailApi.md#get_main_account_disk_usage_bytes) | **GET** /Email/get_main_account_disk_usage_bytes | Return primary email account&#39;s disk usage in bytes
[**get_max_email_quota**](EmailApi.md#get_max_email_quota) | **GET** /Email/get_max_email_quota | Return email account&#39;s max quota size
[**get_max_email_quota_mib**](EmailApi.md#get_max_email_quota_mib) | **GET** /Email/get_max_email_quota_mib | Return email account&#39;s max quota size in MiB
[**get_pop_quota**](EmailApi.md#get_pop_quota) | **GET** /Email/get_pop_quota | Return email account&#39;s quota
[**get_spam_settings**](EmailApi.md#get_spam_settings) | **GET** /Email/get_spam_settings | Return email account Apache SpamAssassin settings
[**get_webmail_settings**](EmailApi.md#get_webmail_settings) | **GET** /Email/get_webmail_settings | Return email account&#39;s Webmail settings
[**has_delegated_mailman_lists**](EmailApi.md#has_delegated_mailman_lists) | **GET** /Email/has_delegated_mailman_lists | Return email account&#39;s mailing list privileges
[**has_plaintext_authentication**](EmailApi.md#has_plaintext_authentication) | **GET** /Email/has_plaintext_authentication | Return whether plaintext authentication is enabled
[**hold_outgoing**](EmailApi.md#hold_outgoing) | **GET** /Email/hold_outgoing | Stop email account&#39;s outgoing mail
[**list_auto_responders**](EmailApi.md#list_auto_responders) | **GET** /Email/list_auto_responders | Return domain&#39;s autoresponders
[**list_default_address**](EmailApi.md#list_default_address) | **GET** /Email/list_default_address | Return domain&#39;s default email address
[**list_domain_forwarders**](EmailApi.md#list_domain_forwarders) | **GET** /Email/list_domain_forwarders | Return domain-level forwarders
[**list_filters**](EmailApi.md#list_filters) | **GET** /Email/list_filters | Return account-level email filters
[**list_filters_backups**](EmailApi.md#list_filters_backups) | **GET** /Email/list_filters_backups | Return domains with domain-level email filters
[**list_forwarders**](EmailApi.md#list_forwarders) | **GET** /Email/list_forwarders | Return domain&#39;s forwarders
[**list_forwarders_backups**](EmailApi.md#list_forwarders_backups) | **GET** /Email/list_forwarders_backups | Return domains with domain-level forwarders
[**list_lists**](EmailApi.md#list_lists) | **GET** /Email/list_lists | Return cPanel account&#39;s mailing lists
[**list_mail_domains**](EmailApi.md#list_mail_domains) | **GET** /Email/list_mail_domains | Return cPanel account&#39;s mail domains
[**list_pops**](EmailApi.md#list_pops) | **GET** /Email/list_pops | Return email accounts
[**list_pops_with_disk**](EmailApi.md#list_pops_with_disk) | **GET** /Email/list_pops_with_disk | Return email accounts with disk information
[**list_system_filter_info**](EmailApi.md#list_system_filter_info) | **GET** /Email/list_system_filter_info | Return system-level email filter file information
[**passwd_list**](EmailApi.md#passwd_list) | **GET** /Email/passwd_list | Update mailing list password
[**passwd_pop**](EmailApi.md#passwd_pop) | **GET** /Email/passwd_pop | Update email account password
[**release_outgoing**](EmailApi.md#release_outgoing) | **GET** /Email/release_outgoing | Start email account outgoing mail
[**remove_mailman_delegates**](EmailApi.md#remove_mailman_delegates) | **GET** /Email/remove_mailman_delegates | Remove account mailing list admin privileges
[**reorder_filters**](EmailApi.md#reorder_filters) | **GET** /Email/reorder_filters | Update email address&#39;s email filter order
[**set_always_accept**](EmailApi.md#set_always_accept) | **GET** /Email/set_always_accept | Update Mail Exchanger type
[**set_default_address**](EmailApi.md#set_default_address) | **GET** /Email/set_default_address | Create default email address
[**set_list_privacy_options**](EmailApi.md#set_list_privacy_options) | **GET** /Email/set_list_privacy_options | Update mailing list privacy options
[**set_manual_mx_redirects**](EmailApi.md#set_manual_mx_redirects) | **GET** /Email/set_manual_mx_redirects | Add manual MX redirection
[**stats_db_status**](EmailApi.md#stats_db_status) | **GET** /Email/stats_db_status | Return eximstats SQLite database status
[**store_filter**](EmailApi.md#store_filter) | **GET** /Email/store_filter | Create email filter
[**suspend_incoming**](EmailApi.md#suspend_incoming) | **GET** /Email/suspend_incoming | Suspend email account incoming (SMTP) mail
[**suspend_login**](EmailApi.md#suspend_login) | **GET** /Email/suspend_login | Suspend email account login
[**suspend_outgoing**](EmailApi.md#suspend_outgoing) | **GET** /Email/suspend_outgoing | Suspend email account outgoing mail
[**trace_delivery**](EmailApi.md#trace_delivery) | **GET** /Email/trace_delivery | Run email delivery route trace
[**trace_filter**](EmailApi.md#trace_filter) | **GET** /Email/trace_filter | Run test for main domain email filters
[**unset_manual_mx_redirects**](EmailApi.md#unset_manual_mx_redirects) | **GET** /Email/unset_manual_mx_redirects | Remove manual MX redirection
[**unsuspend_incoming**](EmailApi.md#unsuspend_incoming) | **GET** /Email/unsuspend_incoming | Unsuspend email account incoming mail
[**unsuspend_login**](EmailApi.md#unsuspend_login) | **GET** /Email/unsuspend_login | Unsuspend email account login
[**unsuspend_outgoing**](EmailApi.md#unsuspend_outgoing) | **GET** /Email/unsuspend_outgoing | Unsuspend email account outgoing mail
[**verify_password**](EmailApi.md#verify_password) | **GET** /Email/verify_password | Validate email account password


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
    api_instance = clientapi_cpanel.EmailApi(api_client)
    account = 'user' # str | The function will return this value in the data return. If you do **not** include this parameter, the function returns `All Mail On The Account` or a blank value. * A valid string. * An empty value.  **Note:**   The function does **not** validate this parameter's value. (optional)
    display = 'any_value' # str | Include this parameter to cause the function to return `All Mail On The Account` if the account parameter is blank or does not exist. If you do **not** include this parameter and the account value is blank or does not exist, the function returns a blank data value. (optional)

    try:
        # Return current user's account name
        api_response = api_instance.account_name(account=account, display=display)
        print("The response of EmailApi->account_name:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailApi->account_name: %s\n" % e)
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
    api_instance = clientapi_cpanel.EmailApi(api_client)
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
        print("The response of EmailApi->add_auto_responder:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailApi->add_auto_responder: %s\n" % e)
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

# **add_domain_forwarder**
> InlineResponse200121 add_domain_forwarder(destdomain, domain)

Create domain-level forwarder

This function creates a domain-level forwarder.

**Important:**

  When you disable the [*Receive Mail* role](https://go.cpanel.net/serverroles), the system **disables** this function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200121 import InlineResponse200121
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
    api_instance = clientapi_cpanel.EmailApi(api_client)
    destdomain = 'forwardtome.com' # str | The domain to receive forwarded mail.
    domain = 'example.com' # str | The domain on the cPanel account from which to forward mail.

    try:
        # Create domain-level forwarder
        api_response = api_instance.add_domain_forwarder(destdomain, domain)
        print("The response of EmailApi->add_domain_forwarder:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailApi->add_domain_forwarder: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **destdomain** | **str**| The domain to receive forwarded mail. | 
 **domain** | **str**| The domain on the cPanel account from which to forward mail. | 

### Return type

[**InlineResponse200121**](InlineResponse200121.md)

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

# **add_forwarder**
> InlineResponse200122 add_forwarder(domain, email, fwdopt, failmsgs=failmsgs, fwdemail=fwdemail, fwdsystem=fwdsystem, pipefwd=pipefwd)

Create email account forwarder

This function creates an email forwarder.

**Important:**

  When you disable the MailReceive role, the system disables this function. 
  For more information, read our [How to Use Server Profiles](https://go.cpanel.net/howtouseserverprofiles) 
  documentation.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200122 import InlineResponse200122
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
    api_instance = clientapi_cpanel.EmailApi(api_client)
    domain = 'example.com' # str | The domain.
    email = 'forwardme@example.com' # str | The email address to forward.
    fwdopt = 'fwd' # str | The method to use to handle the email address's mail.
    failmsgs = 'No such person at this address' # str | The failure message for the message's sender.  **Note:**   Use this parameter if you used the fail method for the fwdopt parameter. (optional) (default to 'No such person at this address')
    fwdemail = 'fwdtome@example.com' # str | The email address to which the system forwards messages.  **Note:**   You must use this parameter if you used the fwd method for the fwdopt parameter. You can pass multiple addresses to this parameter as a comma-separated list. (optional)
    fwdsystem = 'user' # str | The system user to whom the system forwards messages.  **Note:**   You must use this parameter if you used the system method for the fwdopt parameter. (optional)
    pipefwd = 'mailscript.pl' # str | The application to which the system pipes messages.  **Note:**   You must use this parameter if you used the pipe method for the fwdopt parameter.  **Important:**    This parameter requires the FileStorage role. For more information, read our    [How to Use Server Profiles](https://go.cpanel.net/howtouseserverprofiles) documentation. (optional)

    try:
        # Create email account forwarder
        api_response = api_instance.add_forwarder(domain, email, fwdopt, failmsgs=failmsgs, fwdemail=fwdemail, fwdsystem=fwdsystem, pipefwd=pipefwd)
        print("The response of EmailApi->add_forwarder:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailApi->add_forwarder: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**| The domain. | 
 **email** | **str**| The email address to forward. | 
 **fwdopt** | **str**| The method to use to handle the email address&#39;s mail. | 
 **failmsgs** | **str**| The failure message for the message&#39;s sender.  **Note:**   Use this parameter if you used the fail method for the fwdopt parameter. | [optional] [default to &#39;No such person at this address&#39;]
 **fwdemail** | **str**| The email address to which the system forwards messages.  **Note:**   You must use this parameter if you used the fwd method for the fwdopt parameter. You can pass multiple addresses to this parameter as a comma-separated list. | [optional] 
 **fwdsystem** | **str**| The system user to whom the system forwards messages.  **Note:**   You must use this parameter if you used the system method for the fwdopt parameter. | [optional] 
 **pipefwd** | **str**| The application to which the system pipes messages.  **Note:**   You must use this parameter if you used the pipe method for the fwdopt parameter.  **Important:**    This parameter requires the FileStorage role. For more information, read our    [How to Use Server Profiles](https://go.cpanel.net/howtouseserverprofiles) documentation. | [optional] 

### Return type

[**InlineResponse200122**](InlineResponse200122.md)

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
    api_instance = clientapi_cpanel.EmailApi(api_client)
    domain = 'example.com' # str | The domain.
    list = 'newlist' # str | The mailing list name.
    password = '12345luggage' # str | The mailing list password.
    private = 0 # int | Whether the mailing list is private. * `1` — Private. * `0` — Public. (optional) (default to 0)
    rebuildonly = 0 # int | Whether to rebuild the mailing list. * `1` — Rebuild the mailing list. * `0` — Do **not** rebuild the mailing list. (optional) (default to 0)

    try:
        # Create mailing list
        api_response = api_instance.add_list(domain, list, password, private=private, rebuildonly=rebuildonly)
        print("The response of EmailApi->add_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailApi->add_list: %s\n" % e)
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
    api_instance = clientapi_cpanel.EmailApi(api_client)
    delegates = 'delegates=user@example.com,admin@example.com' # str | A list of the administrators to add.  **Note:**    Separate multiple email addresses with commas.
    list = 'mylist' # str | The mailing list.

    try:
        # Add administrators to mailing list
        api_response = api_instance.add_mailman_delegates(delegates, list)
        print("The response of EmailApi->add_mailman_delegates:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailApi->add_mailman_delegates: %s\n" % e)
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
    api_instance = clientapi_cpanel.EmailApi(api_client)
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
        print("The response of EmailApi->add_pop:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailApi->add_pop: %s\n" % e)
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

# **add_spam_filter**
> InlineResponse200127 add_spam_filter(account=account, required_score=required_score)

Update minimum spam score threshold value

This function sets a new minimum Apache SpamAssassin™ spam score threshold value.

**Notes:**

  * To disable spam filtering, use the UAPI `Email::disable_spam_autodelete` fuction.
  * For more information, read our [Spam Filters](https://go.cpanel.net/cpaneldocsSpamFilters) documentation.

**Important:**

  * When you disable the [*Spam Filter* role](https://go.cpanel.net/serverroles#roles), the system **disables** this function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200127 import InlineResponse200127
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
    api_instance = clientapi_cpanel.EmailApi(api_client)
    account = 'username@example.com' # str | The email account to apply a spam score threshold value.  **Note:**    If you do **not** specify a value, the function applies the new spam score threshold value to **all** accounts. (optional)
    required_score = '5' # str | Set a spam score threshold value.  **Notes:**    * You **must** specify a value greater than `0`, and lower than the domain owner's spam score threshold value.   * You **cannot** enter `0` as a value for this parameter.   * You can retrieve the domain owner‘s spam score threshold value via the `cpuser_spam_auto_delete_score` return from the UAPI `Email::get_spam_settings` function.   * The default value, `5`, is an aggressive spam score.   * The lower the spam score, the more likely that Apache SpamAssassin will label messages as spam and delete them.   * Some systems may wish to use a more lenient spam score (for example, `8` or `10`). (optional) (default to '5')

    try:
        # Update minimum spam score threshold value
        api_response = api_instance.add_spam_filter(account=account, required_score=required_score)
        print("The response of EmailApi->add_spam_filter:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailApi->add_spam_filter: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account** | **str**| The email account to apply a spam score threshold value.  **Note:**    If you do **not** specify a value, the function applies the new spam score threshold value to **all** accounts. | [optional] 
 **required_score** | **str**| Set a spam score threshold value.  **Notes:**    * You **must** specify a value greater than &#x60;0&#x60;, and lower than the domain owner&#39;s spam score threshold value.   * You **cannot** enter &#x60;0&#x60; as a value for this parameter.   * You can retrieve the domain owner‘s spam score threshold value via the &#x60;cpuser_spam_auto_delete_score&#x60; return from the UAPI &#x60;Email::get_spam_settings&#x60; function.   * The default value, &#x60;5&#x60;, is an aggressive spam score.   * The lower the spam score, the more likely that Apache SpamAssassin will label messages as spam and delete them.   * Some systems may wish to use a more lenient spam score (for example, &#x60;8&#x60; or &#x60;10&#x60;). | [optional] [default to &#39;5&#39;]

### Return type

[**InlineResponse200127**](InlineResponse200127.md)

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
    api_instance = clientapi_cpanel.EmailApi(api_client)
    account = 'user@example.com' # str | An email address, to limit the function's results. (optional)
    dir = 'maildir' # str | A mail directory name, to limit results to specific directories.  **Note:**    If you pass the `default` or `mail` values, the function lists information for all mail directories. (optional)
    showdotfiles = 0 # int | Whether to include hidden files and directories. * `1` — Include hidden items. * `0` — Do **not** include hidden items. (optional) (default to 0)

    try:
        # Return mail directory's subdirectories and files
        api_response = api_instance.browse_mailbox(account=account, dir=dir, showdotfiles=showdotfiles)
        print("The response of EmailApi->browse_mailbox:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailApi->browse_mailbox: %s\n" % e)
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

# **check_fastmail**
> InlineResponse200130 check_fastmail()

Return BlackBerry FastMail support status

This function checks whether [BlackBerry® FastMail](https://go.cpanel.net/blackberryfastmail) support is enabled.

**Important:**

  When you disable the [*Receive Mail* role](https://go.cpanel.net/serverroles#roles), the system **disables** this function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200130 import InlineResponse200130
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
    api_instance = clientapi_cpanel.EmailApi(api_client)

    try:
        # Return BlackBerry FastMail support status
        api_response = api_instance.check_fastmail()
        print("The response of EmailApi->check_fastmail:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailApi->check_fastmail: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**InlineResponse200130**](InlineResponse200130.md)

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
    api_instance = clientapi_cpanel.EmailApi(api_client)

    try:
        # Return cPanel account's autoresponders total
        api_response = api_instance.count_auto_responders()
        print("The response of EmailApi->count_auto_responders:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailApi->count_auto_responders: %s\n" % e)
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
    api_instance = clientapi_cpanel.EmailApi(api_client)

    try:
        # Return cPanel account's email filters total
        api_response = api_instance.count_filters()
        print("The response of EmailApi->count_filters:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailApi->count_filters: %s\n" % e)
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

# **count_forwarders**
> InlineResponse200133 count_forwarders()

Return cPanel account's mail forwarder total

This function returns the number of [forwarders](https://go.cpanel.net/Forwarders) for every email address on a cPanel account.

**Important:**

  When you disable the [*Receive Mail* role](https://go.cpanel.net/serverroles#roles), the system **disables** this function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200133 import InlineResponse200133
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
    api_instance = clientapi_cpanel.EmailApi(api_client)

    try:
        # Return cPanel account's mail forwarder total
        api_response = api_instance.count_forwarders()
        print("The response of EmailApi->count_forwarders:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailApi->count_forwarders: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**InlineResponse200133**](InlineResponse200133.md)

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
    api_instance = clientapi_cpanel.EmailApi(api_client)

    try:
        # Return cPanel account's mailing list total
        api_response = api_instance.count_lists()
        print("The response of EmailApi->count_lists:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailApi->count_lists: %s\n" % e)
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
    api_instance = clientapi_cpanel.EmailApi(api_client)

    try:
        # Return cPanel account's email account total
        api_response = api_instance.count_pops()
        print("The response of EmailApi->count_pops:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailApi->count_pops: %s\n" % e)
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
    api_instance = clientapi_cpanel.EmailApi(api_client)
    email = 'user@example.com' # str | The email account.

    try:
        # Delete email account's autoresponder
        api_response = api_instance.delete_auto_responder(email)
        print("The response of EmailApi->delete_auto_responder:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailApi->delete_auto_responder: %s\n" % e)
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

# **delete_domain_forwarder**
> InlineResponse200137 delete_domain_forwarder(domain)

Delete domain-level forwarder

This function deletes a domain-level forwarder.

**Important:**

  When you disable the [*Receive Mail* role](https://go.cpanel.net/serverroles), the system **disables** this function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200137 import InlineResponse200137
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
    api_instance = clientapi_cpanel.EmailApi(api_client)
    domain = 'example.com' # str | The domain name.

    try:
        # Delete domain-level forwarder
        api_response = api_instance.delete_domain_forwarder(domain)
        print("The response of EmailApi->delete_domain_forwarder:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailApi->delete_domain_forwarder: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**| The domain name. | 

### Return type

[**InlineResponse200137**](InlineResponse200137.md)

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
    api_instance = clientapi_cpanel.EmailApi(api_client)
    account = 'user@example.com' # str | The email address that owns the filter.
    filtername = 'coffee' # str | The filter's name.

    try:
        # Delete email account's email filter
        api_response = api_instance.delete_filter(account, filtername)
        print("The response of EmailApi->delete_filter:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailApi->delete_filter: %s\n" % e)
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

# **delete_forwarder**
> InlineResponse200139 delete_forwarder(address, forwarder)

Delete email account's email forwarder

This function deletes an email forwarder.

**Important:**

  When you disable the [*Receive Mail* role](https://go.cpanel.net/serverroles), the system **disables** this function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200139 import InlineResponse200139
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
    api_instance = clientapi_cpanel.EmailApi(api_client)
    address = 'user@example.com' # str | The forwarder's email address.
    forwarder = 'fwdtome@example.com' # str | The forwarder's destination. * A valid email address. * A script location. * A system account.

    try:
        # Delete email account's email forwarder
        api_response = api_instance.delete_forwarder(address, forwarder)
        print("The response of EmailApi->delete_forwarder:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailApi->delete_forwarder: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address** | **str**| The forwarder&#39;s email address. | 
 **forwarder** | **str**| The forwarder&#39;s destination. * A valid email address. * A script location. * A system account. | 

### Return type

[**InlineResponse200139**](InlineResponse200139.md)

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
    api_instance = clientapi_cpanel.EmailApi(api_client)
    email = 'username@example.com' # str | The email address to query.

    try:
        # Delete email account's outgoing messages
        api_response = api_instance.delete_held_messages(email)
        print("The response of EmailApi->delete_held_messages:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailApi->delete_held_messages: %s\n" % e)
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
    api_instance = clientapi_cpanel.EmailApi(api_client)
    list = 'mylist' # str | The mailing list.

    try:
        # Delete mailing list
        api_response = api_instance.delete_list(list)
        print("The response of EmailApi->delete_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailApi->delete_list: %s\n" % e)
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
    api_instance = clientapi_cpanel.EmailApi(api_client)
    email = clientapi_cpanel.Email3() # Email3 | The email account username or address. * A valid email account username. For example, `user` if the email address is `user@example.com`. * A valid email address.
    domain = 'The cPanel account's main domain.' # str | The email account's domain. For example, `example.com` if the email address is `user@example.com`. (optional) (default to 'The cPanel account's main domain.')
    flags = 'passwd' # str | Whether to remove the mail account's home mail directory. If you do not specify a value, the function removes the mail account's home directory. * `passwd` — Preserve the mail account's home directory. * Any other value — Remove the mail account's home directory. (optional)
    skip_quota = 0 # int | Whether to modify the mail account's quota file. * `1` — Do **not** modify. * `0` — Modify. (optional) (default to 0)

    try:
        # Delete email address
        api_response = api_instance.delete_pop(email, domain=domain, flags=flags, skip_quota=skip_quota)
        print("The response of EmailApi->delete_pop:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailApi->delete_pop: %s\n" % e)
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
    api_instance = clientapi_cpanel.EmailApi(api_client)
    account = 'user@example.com' # str | The email address that owns the filter.
    filtername = 'coffee' # str | The filter's name.

    try:
        # Disable email filter for email account
        api_response = api_instance.disable_filter(account, filtername)
        print("The response of EmailApi->disable_filter:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailApi->disable_filter: %s\n" % e)
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

# **disable_mailbox_autocreate**
> InlineResponse200145 disable_mailbox_autocreate(email)

Disable cPanel account mailbox autocreation

This function disables the system's ability to automatically create mailboxes for a cPanel account.

**Note:**

  When you **enable** the UAPI's `Email::enable_mailbox_autocreate` function, the system automatically creates mailboxes. The system creates a new mailbox when it receives an email address in [plus address format](https://en.wikipedia.org/wiki/Email_address#Sub-addressing) and that mailbox does **not** exist. For example, receiving an email from the `user+newmailbox@example.com` address creates the `newmailbox` mailbox if the `newmailbox` mailbox does not exist.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200145 import InlineResponse200145
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
    api_instance = clientapi_cpanel.EmailApi(api_client)
    email = 'username@example.com' # str | The email account address for which to disable mailbox autocreation.

    try:
        # Disable cPanel account mailbox autocreation
        api_response = api_instance.disable_mailbox_autocreate(email)
        print("The response of EmailApi->disable_mailbox_autocreate:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailApi->disable_mailbox_autocreate: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**| The email account address for which to disable mailbox autocreation. | 

### Return type

[**InlineResponse200145**](InlineResponse200145.md)

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

# **disable_spam_assassin**
> InlineResponse200146 disable_spam_assassin()

Disable Apache SpamAssassin for cPanel account

This function disables Apache SpamAssassin™ for a cPanel account.

**Important:**

  When you disable the [*Spam Filter* role](https://go.cpanel.net/serverroles), the system **disables** this function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200146 import InlineResponse200146
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
    api_instance = clientapi_cpanel.EmailApi(api_client)

    try:
        # Disable Apache SpamAssassin for cPanel account
        api_response = api_instance.disable_spam_assassin()
        print("The response of EmailApi->disable_spam_assassin:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailApi->disable_spam_assassin: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**InlineResponse200146**](InlineResponse200146.md)

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

# **disable_spam_autodelete**
> InlineResponse200147 disable_spam_autodelete()

Disable spam box filtering auto-delete

This function disables the Apache SpamAssassin™ auto-delete spam feature.

**Important:**

  When you disable the [*Receive Mail* role](https://go.cpanel.net/serverroles), the system **disables** this function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200147 import InlineResponse200147
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
    api_instance = clientapi_cpanel.EmailApi(api_client)

    try:
        # Disable spam box filtering auto-delete
        api_response = api_instance.disable_spam_autodelete()
        print("The response of EmailApi->disable_spam_autodelete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailApi->disable_spam_autodelete: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**InlineResponse200147**](InlineResponse200147.md)

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

# **disable_spam_box**
> InlineResponse200148 disable_spam_box()

Disable spam box filtering for cPanel account

This function disables spam box filtering for a cPanel account. When you disable spam box filtering, the system sends all messages to the account's inbox.

**Notes:**

  * This function **requires** that your hosting provider enables Apache SpamAssassin™ on the server.
  * To **enable** spam box filtering, use the UAPI `Email::enable_spam_box` function.
  * For more information, read our [Spam Filters](https://go.cpanel.net/cpaneldocsSpamFilters) documentation.

**Important:**

  When you disable the [*Spam Filter* role](https://go.cpanel.net/serverroles), the system **disables** this function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200148 import InlineResponse200148
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
    api_instance = clientapi_cpanel.EmailApi(api_client)

    try:
        # Disable spam box filtering for cPanel account
        api_response = api_instance.disable_spam_box()
        print("The response of EmailApi->disable_spam_box:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailApi->disable_spam_box: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**InlineResponse200148**](InlineResponse200148.md)

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
    api_instance = clientapi_cpanel.EmailApi(api_client)
    account = clientapi_cpanel.Account() # Account | The email account username or address for which to send client settings.
    to = 'user@example.com' # str | The email address to send client settings.

    try:
        # Send email client settings to an email address
        api_response = api_instance.dispatch_client_settings(account, to)
        print("The response of EmailApi->dispatch_client_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailApi->dispatch_client_settings: %s\n" % e)
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
    api_instance = clientapi_cpanel.EmailApi(api_client)
    domain = 'example.com' # str | The email account's domain. Defaults to the cPanel account's main domain.
    email = 'user' # str | The email account username.
    quota = '500' # str | The maximum amount of disk space that the new email account may use. Defaults to the system value. * A positive integer that represents the maximum amount of disk space, in megabytes (MB).  **Note:**  You **cannot** enter a value that exceeds the maximum email quota. * `0` or `unlimited` — The account possesses unlimited disk space.  If the email account's quota value is set higher (or unlimited) than the account's max quota, the account's max quota will be applied instead of the value entered.  **Note:**  This value is only available to users without a maximum email account quota. (optional)

    try:
        # Update email account's quota
        api_response = api_instance.edit_pop_quota(domain, email, quota=quota)
        print("The response of EmailApi->edit_pop_quota:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailApi->edit_pop_quota: %s\n" % e)
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
    api_instance = clientapi_cpanel.EmailApi(api_client)

    try:
        # Stop cPanel account IMAP and POP3 connections
        api_response = api_instance.email_terminate_mailbox_sessions()
        print("The response of EmailApi->email_terminate_mailbox_sessions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailApi->email_terminate_mailbox_sessions: %s\n" % e)
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
    api_instance = clientapi_cpanel.EmailApi(api_client)
    account = 'username@example.com' # str | The email address that owns the filter.
    filtername = 'coffee' # str | The filter's name.

    try:
        # Enable email filter for email account
        api_response = api_instance.enable_filter(account, filtername)
        print("The response of EmailApi->enable_filter:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailApi->enable_filter: %s\n" % e)
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

# **enable_mailbox_autocreate**
> InlineResponse200152 enable_mailbox_autocreate(email)

Enable cPanel account mailbox autocreation

This function allows the system to automatically create mailboxes for a cPanel account. The system will create a new mailbox when it receives an email address in plus address format and that mailbox does not exist. For example, receiving an email from the user+newmailbox@example.com address creates the newmailbox mailbox if the newmailbox mailbox does not exist.

**Note:**

  To disable this functionality, use the UAPI Email::disable_mailbox_autocreate function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200152 import InlineResponse200152
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
    api_instance = clientapi_cpanel.EmailApi(api_client)
    email = 'username@example.com' # str | The email account for which to enable mailbox autocreation.

    try:
        # Enable cPanel account mailbox autocreation
        api_response = api_instance.enable_mailbox_autocreate(email)
        print("The response of EmailApi->enable_mailbox_autocreate:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailApi->enable_mailbox_autocreate: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**| The email account for which to enable mailbox autocreation. | 

### Return type

[**InlineResponse200152**](InlineResponse200152.md)

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

# **enable_spam_assassin**
> InlineResponse200153 enable_spam_assassin()

Enable Apache SpamAssassin for cPanel account

This function enables Apache SpamAssassin™ for the account.

**Important:**

When you disable the [Spam Filter role](https://go.cpanel.net/serverroles), the system **disables** this function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200153 import InlineResponse200153
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
    api_instance = clientapi_cpanel.EmailApi(api_client)

    try:
        # Enable Apache SpamAssassin for cPanel account
        api_response = api_instance.enable_spam_assassin()
        print("The response of EmailApi->enable_spam_assassin:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailApi->enable_spam_assassin: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**InlineResponse200153**](InlineResponse200153.md)

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

# **enable_spam_box**
> InlineResponse200154 enable_spam_box()

Enable spam box filtering for cPanel account

This function enables spam box filtering for a cPanel account. When you enable spam box filtering, the system sends messages marked as spam to a spam folder.

**Notes:**

* This function **requires** that your hosting provider enables Apache SpamAssassin on the server.
* To **disable** spam box filtering, use the UAPI `Email::disable_spam_box` function.
* For more information, read our [Spam Filters](https://go.cpanel.net/cpaneldocsSpamFilters) documentation.

**Important:**

When you disable the [Spam Filter](https://go.cpanel.net/serverroles) role, the system **disables** this function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200154 import InlineResponse200154
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
    api_instance = clientapi_cpanel.EmailApi(api_client)

    try:
        # Enable spam box filtering for cPanel account
        api_response = api_instance.enable_spam_box()
        print("The response of EmailApi->enable_spam_box:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailApi->enable_spam_box: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**InlineResponse200154**](InlineResponse200154.md)

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
    api_instance = clientapi_cpanel.EmailApi(api_client)

    try:
        # Export cPanel account's Mailman mailing lists to a file
        api_response = api_instance.export_lists()
        print("The response of EmailApi->export_lists:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailApi->export_lists: %s\n" % e)
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

# **fetch_charmaps**
> InlineResponse200156 fetch_charmaps()

Return server's supported character encodings

This function lists the available character encodings.

**Important:**

When you disable the [Receive Mail role](https://go.cpanel.net/serverroles), the system **disables** this function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200156 import InlineResponse200156
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
    api_instance = clientapi_cpanel.EmailApi(api_client)

    try:
        # Return server's supported character encodings
        api_response = api_instance.fetch_charmaps()
        print("The response of EmailApi->fetch_charmaps:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailApi->fetch_charmaps: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**InlineResponse200156**](InlineResponse200156.md)

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

# **fts_rescan_mailbox**
> InlineResponse200157 fts_rescan_mailbox(account)

Start IMAP Full-Text Search scan for email account

This function requests that the IMAP Full-Text Search Indexing (powered by Apache Solr™) plugin rescan an email account.

**Note:**

To enable this function, you **must** install the *IMAP Full-Text Search Indexing (powered by Apache Solr™)* plugin in WHM's [*Manage Plugins*](https://go.cpanel.net/whmdocsManagePlugins) interface (*WHM >> Home >> cPanel >> Manage Plugins*). For more information, read our [install_dovecot_fts script](https://go.cpanel.net/installdovecotftsscript) documentation.

**Important:**

When you disable the [Receive Mail role](https://go.cpanel.net/serverroles), the system disables this function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200157 import InlineResponse200157
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
    api_instance = clientapi_cpanel.EmailApi(api_client)
    account = 'username@example.com' # str | The email user's account name.  **Note:**  If you do not enter an email address, the function rescans the default email account.

    try:
        # Start IMAP Full-Text Search scan for email account
        api_response = api_instance.fts_rescan_mailbox(account)
        print("The response of EmailApi->fts_rescan_mailbox:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailApi->fts_rescan_mailbox: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account** | **str**| The email user&#39;s account name.  **Note:**  If you do not enter an email address, the function rescans the default email account. | 

### Return type

[**InlineResponse200157**](InlineResponse200157.md)

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
    api_instance = clientapi_cpanel.EmailApi(api_client)
    list = 'mylist' # str | The mailing list.

    try:
        # Create one-time password for a mailing list
        api_response = api_instance.generate_mailman_otp(list)
        print("The response of EmailApi->generate_mailman_otp:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailApi->generate_mailman_otp: %s\n" % e)
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
    api_instance = clientapi_cpanel.EmailApi(api_client)
    email = 'user' # str | The email account name.
    temp_charset = 'utf-8' # str | The autoresponder's [character set](https://en.wikipedia.org/wiki/Character_encoding). (optional) (default to 'utf-8')

    try:
        # Return email account's autoresponder information
        api_response = api_instance.get_auto_responder(email, temp_charset=temp_charset)
        print("The response of EmailApi->get_auto_responder:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailApi->get_auto_responder: %s\n" % e)
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

# **get_charsets**
> InlineResponse200160 get_charsets()

Return mail server's supported character encodings

This function lists character encodings that the mail server supports.

**Important:**

When you disable the [Receive Mail role](https://go.cpanel.net/serverroles), the system **disables** this function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200160 import InlineResponse200160
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
    api_instance = clientapi_cpanel.EmailApi(api_client)

    try:
        # Return mail server's supported character encodings
        api_response = api_instance.get_charsets()
        print("The response of EmailApi->get_charsets:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailApi->get_charsets: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**InlineResponse200160**](InlineResponse200160.md)

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
    api_instance = clientapi_cpanel.EmailApi(api_client)
    account = 'username@example.com' # str | The email address for which to send client settings.  **Note:**  This parameter defaults to the [system default email account](https://go.cpanel.net/systemdefaultemailaccount).  (optional)

    try:
        # Return email account's client settings
        api_response = api_instance.get_client_settings(account=account)
        print("The response of EmailApi->get_client_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailApi->get_client_settings: %s\n" % e)
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
    api_instance = clientapi_cpanel.EmailApi(api_client)

    try:
        # Return email account's default email quota
        api_response = api_instance.get_default_email_quota()
        print("The response of EmailApi->get_default_email_quota:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailApi->get_default_email_quota: %s\n" % e)
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
    api_instance = clientapi_cpanel.EmailApi(api_client)

    try:
        # Return email account's default email quota in MiB
        api_response = api_instance.get_default_email_quota_mib()
        print("The response of EmailApi->get_default_email_quota_mib:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailApi->get_default_email_quota_mib: %s\n" % e)
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
    api_instance = clientapi_cpanel.EmailApi(api_client)
    domain = 'example.com' # str | The email account's domain.
    user = 'user' # str | The email account username.

    try:
        # Return email account's disk usage
        api_response = api_instance.get_disk_usage(domain, user)
        print("The response of EmailApi->get_disk_usage:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailApi->get_disk_usage: %s\n" % e)
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
    api_instance = clientapi_cpanel.EmailApi(api_client)
    account = 'user@example.com' # str | The email address that owns the filter.
    filtername = 'coffee' # str | The filter's name.

    try:
        # Return email filter's information
        api_response = api_instance.get_filter(account, filtername)
        print("The response of EmailApi->get_filter:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailApi->get_filter: %s\n" % e)
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
    api_instance = clientapi_cpanel.EmailApi(api_client)
    email = 'username@example.com' # str | The email address to query. (optional)

    try:
        # Return email account's outgoing message count
        api_response = api_instance.get_held_message_count(email=email)
        print("The response of EmailApi->get_held_message_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailApi->get_held_message_count: %s\n" % e)
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
    api_instance = clientapi_cpanel.EmailApi(api_client)

    try:
        # Return cPanel account's mailing list disk usage
        api_response = api_instance.get_lists_total_disk_usage()
        print("The response of EmailApi->get_lists_total_disk_usage:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailApi->get_lists_total_disk_usage: %s\n" % e)
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

# **get_mailbox_autocreate**
> InlineResponse200168 get_mailbox_autocreate(email)

Return cPanel account's mailbox autocreate status

This function checks whether a cPanel account will automatically create mailboxes when it receives an email address in [plus address format](https://en.wikipedia.org/wiki/Email_address#Sub-addressing).

**Note:**

To enable or disable this functionality, use the UAPI's `Email::enable_mailbox_autocreate` and `Email::disable_mailbox_autocreate` functions.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200168 import InlineResponse200168
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
    api_instance = clientapi_cpanel.EmailApi(api_client)
    email = 'username@example.com' # str | The email account address to query.

    try:
        # Return cPanel account's mailbox autocreate status
        api_response = api_instance.get_mailbox_autocreate(email)
        print("The response of EmailApi->get_mailbox_autocreate:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailApi->get_mailbox_autocreate: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**| The email account address to query. | 

### Return type

[**InlineResponse200168**](InlineResponse200168.md)

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
    api_instance = clientapi_cpanel.EmailApi(api_client)
    list = 'mylist' # str | The name of a Mailman mailing list on the cPanel account.

    try:
        # Return mailing list administrators
        api_response = api_instance.get_mailman_delegates(list)
        print("The response of EmailApi->get_mailman_delegates:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailApi->get_mailman_delegates: %s\n" % e)
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
    api_instance = clientapi_cpanel.EmailApi(api_client)

    try:
        # Return primary email account's disk usage
        api_response = api_instance.get_main_account_disk_usage()
        print("The response of EmailApi->get_main_account_disk_usage:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailApi->get_main_account_disk_usage: %s\n" % e)
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
    api_instance = clientapi_cpanel.EmailApi(api_client)

    try:
        # Return primary email account's disk usage in bytes
        api_response = api_instance.get_main_account_disk_usage_bytes()
        print("The response of EmailApi->get_main_account_disk_usage_bytes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailApi->get_main_account_disk_usage_bytes: %s\n" % e)
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
    api_instance = clientapi_cpanel.EmailApi(api_client)

    try:
        # Return email account's max quota size
        api_response = api_instance.get_max_email_quota()
        print("The response of EmailApi->get_max_email_quota:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailApi->get_max_email_quota: %s\n" % e)
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
    api_instance = clientapi_cpanel.EmailApi(api_client)

    try:
        # Return email account's max quota size in MiB
        api_response = api_instance.get_max_email_quota_mib()
        print("The response of EmailApi->get_max_email_quota_mib:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailApi->get_max_email_quota_mib: %s\n" % e)
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
    api_instance = clientapi_cpanel.EmailApi(api_client)
    email = 'user' # str | The email account username.  For example, user if the email address is user@example.com.
    as_bytes = 0 # int | Whether to return the quota as bytes.  * `1` — Return the quota as bytes. * `0` — Return the quota as megabytes (MB). (optional) (default to 0)
    domain = 'example.com' # str | The email account's domain. This parameter defaults to the cPanel account's main domain. (optional)

    try:
        # Return email account's quota
        api_response = api_instance.get_pop_quota(email, as_bytes=as_bytes, domain=domain)
        print("The response of EmailApi->get_pop_quota:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailApi->get_pop_quota: %s\n" % e)
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

# **get_spam_settings**
> InlineResponse200175 get_spam_settings(account=account)

Return email account Apache SpamAssassin settings

This function retrieves the Apache SpamAssassin™ settings for the account.

**Important:**

When you disable the [SpamFilter role](https://go.cpanel.net/serverroles), the system **disables** this function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200175 import InlineResponse200175
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
    api_instance = clientapi_cpanel.EmailApi(api_client)
    account = 'username@example.com' # str | Retrieve a specific user account's SpamAssassin settings.  **Note:**  If you do **not** specify this parameter, the function returns the settings for [the default email account](https://go.cpanel.net/DefaultAddress). (optional)

    try:
        # Return email account Apache SpamAssassin settings
        api_response = api_instance.get_spam_settings(account=account)
        print("The response of EmailApi->get_spam_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailApi->get_spam_settings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account** | **str**| Retrieve a specific user account&#39;s SpamAssassin settings.  **Note:**  If you do **not** specify this parameter, the function returns the settings for [the default email account](https://go.cpanel.net/DefaultAddress). | [optional] 

### Return type

[**InlineResponse200175**](InlineResponse200175.md)

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
    api_instance = clientapi_cpanel.EmailApi(api_client)
    account = clientapi_cpanel.Account1() # Account1 | The email account.  **Note:**  If you do **not** specify a value, the function retrieves settings for the cPanel account's default mail account. (optional)

    try:
        # Return email account's Webmail settings
        api_response = api_instance.get_webmail_settings(account=account)
        print("The response of EmailApi->get_webmail_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailApi->get_webmail_settings: %s\n" % e)
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
    api_instance = clientapi_cpanel.EmailApi(api_client)
    delegate = 'user@example.com' # str | The email address.

    try:
        # Return email account's mailing list privileges
        api_response = api_instance.has_delegated_mailman_lists(delegate)
        print("The response of EmailApi->has_delegated_mailman_lists:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailApi->has_delegated_mailman_lists: %s\n" % e)
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

# **has_plaintext_authentication**
> InlineResponse200178 has_plaintext_authentication()

Return whether plaintext authentication is enabled

This function checks whether plaintext authentication is enabled on the Dovecot mail server.

**Important:**

  When you disable the [Receive Mail role](https://go.cpanel.net/serverroles), the system **disables** this function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200178 import InlineResponse200178
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
    api_instance = clientapi_cpanel.EmailApi(api_client)

    try:
        # Return whether plaintext authentication is enabled
        api_response = api_instance.has_plaintext_authentication()
        print("The response of EmailApi->has_plaintext_authentication:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailApi->has_plaintext_authentication: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**InlineResponse200178**](InlineResponse200178.md)

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
    api_instance = clientapi_cpanel.EmailApi(api_client)
    email = 'username@example.com' # str | The email account's username.

    try:
        # Stop email account's outgoing mail
        api_response = api_instance.hold_outgoing(email)
        print("The response of EmailApi->hold_outgoing:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailApi->hold_outgoing: %s\n" % e)
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
    api_instance = clientapi_cpanel.EmailApi(api_client)
    domain = 'example.com' # str | The domain name.
    regex = 'user' # str | A [Perl Compatible Regular Expression (PCRE)](https://en.wikipedia.org/wiki/Perl_Compatible_Regular_Expressions) that filters the results. (optional)

    try:
        # Return domain's autoresponders
        api_response = api_instance.list_auto_responders(domain, regex=regex)
        print("The response of EmailApi->list_auto_responders:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailApi->list_auto_responders: %s\n" % e)
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
    api_instance = clientapi_cpanel.EmailApi(api_client)
    user = 'user' # str | The user whose default addresses to list.
    domain = 'example.com' # str | The domain. If you do not specify a value, the function lists default addresses for all of the cPanel account's domains. (optional)

    try:
        # Return domain's default email address
        api_response = api_instance.list_default_address(user, domain=domain)
        print("The response of EmailApi->list_default_address:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailApi->list_default_address: %s\n" % e)
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

# **list_domain_forwarders**
> InlineResponse200182 list_domain_forwarders(domain=domain)

Return domain-level forwarders

This function lists domain-level forwarders.

**Important:**

  When you disable the [*Receive Mail* role](https://go.cpanel.net/serverroles), the system **disables** this function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200182 import InlineResponse200182
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
    api_instance = clientapi_cpanel.EmailApi(api_client)
    domain = 'example.com' # str | The domain name to query. If you do not use this parameter, the function returns all domain-level forwarders on the cPanel account. (optional)

    try:
        # Return domain-level forwarders
        api_response = api_instance.list_domain_forwarders(domain=domain)
        print("The response of EmailApi->list_domain_forwarders:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailApi->list_domain_forwarders: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**| The domain name to query. If you do not use this parameter, the function returns all domain-level forwarders on the cPanel account. | [optional] 

### Return type

[**InlineResponse200182**](InlineResponse200182.md)

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
    api_instance = clientapi_cpanel.EmailApi(api_client)
    account = clientapi_cpanel.Account2() # Account2 | The email address or cPanel account username for which to return a list of filters. If you do not specify this value, the function lists all of the cPanel account’s account-level filters. (optional)

    try:
        # Return account-level email filters
        api_response = api_instance.list_filters(account=account)
        print("The response of EmailApi->list_filters:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailApi->list_filters: %s\n" % e)
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
    api_instance = clientapi_cpanel.EmailApi(api_client)

    try:
        # Return domains with domain-level email filters
        api_response = api_instance.list_filters_backups()
        print("The response of EmailApi->list_filters_backups:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailApi->list_filters_backups: %s\n" % e)
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

# **list_forwarders**
> InlineResponse200185 list_forwarders(domain, regex=regex)

Return domain's forwarders

This function lists a domain's forwarders.

**Important:**

  When you disable the [*Receive Mail* role](https://go.cpanel.net/serverroles), the system **disables** this function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200185 import InlineResponse200185
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
    api_instance = clientapi_cpanel.EmailApi(api_client)
    domain = 'example.com' # str | The domain.
    regex = 'user' # str | A [Perl Compatible Regular Expression (PCRE)](https://en.wikipedia.org/wiki/Perl_Compatible_Regular_Expressions) that filters the results. If you do **not** use this parameter, the function returns results for all of the account's filters. (optional)

    try:
        # Return domain's forwarders
        api_response = api_instance.list_forwarders(domain, regex=regex)
        print("The response of EmailApi->list_forwarders:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailApi->list_forwarders: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**| The domain. | 
 **regex** | **str**| A [Perl Compatible Regular Expression (PCRE)](https://en.wikipedia.org/wiki/Perl_Compatible_Regular_Expressions) that filters the results. If you do **not** use this parameter, the function returns results for all of the account&#39;s filters. | [optional] 

### Return type

[**InlineResponse200185**](InlineResponse200185.md)

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

# **list_forwarders_backups**
> InlineResponse200186 list_forwarders_backups()

Return domains with domain-level forwarders

This function lists the domains with domain-level forwarders.

**Important:**

  When you disable the [*Receive Mail* role](https://go.cpanel.net/serverroles), the system **disables** this function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200186 import InlineResponse200186
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
    api_instance = clientapi_cpanel.EmailApi(api_client)

    try:
        # Return domains with domain-level forwarders
        api_response = api_instance.list_forwarders_backups()
        print("The response of EmailApi->list_forwarders_backups:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailApi->list_forwarders_backups: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**InlineResponse200186**](InlineResponse200186.md)

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
    api_instance = clientapi_cpanel.EmailApi(api_client)
    domain = 'example.com' # str | The domain to query. If you do **not** use this parameter, the function lists mailing lists for all of the cPanel account's domains. (optional)
    regex = 'user' # str | A [Perl Compatible Regular Expression (PCRE)](https://en.wikipedia.org/wiki/Perl_Compatible_Regular_Expressions) that filters the results. (optional)

    try:
        # Return cPanel account's mailing lists
        api_response = api_instance.list_lists(domain=domain, regex=regex)
        print("The response of EmailApi->list_lists:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailApi->list_lists: %s\n" % e)
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
    api_instance = clientapi_cpanel.EmailApi(api_client)
    add_www = 0 # int | Whether to list `www.` addresses. * `1` — List `www.` addresses. * `0` — Do **not** list `www.` addresses. For example, if you specify `1`, the function's output would include both `example.com` and `www.example.com`. If you specify `0`, the output would include **only** `example.com`. (optional) (default to 0)
    include_wildcard = 0 # int | Whether to list wildcard addresses. * `1` — List wildcard addresses. * `0` — Do **not** list wildcard addresses. For example, if you specify `1`, the function's output would include both `example.com` and `*.example.com`. If you specify `0`, the output would include **only** `example.com`. (optional) (default to 0)
    select = 'example.com' # str | The name of the domain that the function returns with the `select `output parameter. If you do **not** use this parameter, the function will **not** return the `select` parameter with any domains. (optional)

    try:
        # Return cPanel account's mail domains
        api_response = api_instance.list_mail_domains(add_www=add_www, include_wildcard=include_wildcard, select=select)
        print("The response of EmailApi->list_mail_domains:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailApi->list_mail_domains: %s\n" % e)
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
    api_instance = clientapi_cpanel.EmailApi(api_client)
    no_validate = 0 # int | Whether to skip the email database's validation check. * `1` — Skip the validation check. * `0` — Run the validation check. (optional) (default to 0)
    regex = 'user' # str | A [Perl Compatible Regular Expression (PCRE)](https://en.wikipedia.org/wiki/Perl_Compatible_Regular_Expressions) that filters the results. (optional)
    skip_main = 0 # int | Whether to exclude the cPanel account's main account from the results. * `1` — Exclude the main account. * `0` — Include the main account. (optional) (default to 0)

    try:
        # Return email accounts
        api_response = api_instance.list_pops(no_validate=no_validate, regex=regex, skip_main=skip_main)
        print("The response of EmailApi->list_pops:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailApi->list_pops: %s\n" % e)
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
    api_instance = clientapi_cpanel.EmailApi(api_client)
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
        print("The response of EmailApi->list_pops_with_disk:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailApi->list_pops_with_disk: %s\n" % e)
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
    api_instance = clientapi_cpanel.EmailApi(api_client)

    try:
        # Return system-level email filter file information
        api_response = api_instance.list_system_filter_info()
        print("The response of EmailApi->list_system_filter_info:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailApi->list_system_filter_info: %s\n" % e)
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
    api_instance = clientapi_cpanel.EmailApi(api_client)
    list = 'mylist@example.com' # str | The full name (including the domain) of a Mailman mailing list on the cPanel account.
    password = '12345luggage' # str | The new password.

    try:
        # Update mailing list password
        api_response = api_instance.passwd_list(list, password)
        print("The response of EmailApi->passwd_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailApi->passwd_list: %s\n" % e)
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
    api_instance = clientapi_cpanel.EmailApi(api_client)
    email = clientapi_cpanel.Email4() # Email4 | The email account username or address.
    password = '12345luggage' # str | The email account password.
    domain = 'the cPanel account's main domain' # str | The email account's domain. (optional) (default to 'the cPanel account's main domain')

    try:
        # Update email account password
        api_response = api_instance.passwd_pop(email, password, domain=domain)
        print("The response of EmailApi->passwd_pop:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailApi->passwd_pop: %s\n" % e)
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
    api_instance = clientapi_cpanel.EmailApi(api_client)
    email = 'username@example.com' # str | The email account's username.

    try:
        # Start email account outgoing mail
        api_response = api_instance.release_outgoing(email)
        print("The response of EmailApi->release_outgoing:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailApi->release_outgoing: %s\n" % e)
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
    api_instance = clientapi_cpanel.EmailApi(api_client)
    delegates = 'user@example.com,admin@example.com' # str | list of the administrators to remove.
    list = 'mylist' # str | The mailing list.

    try:
        # Remove account mailing list admin privileges
        api_response = api_instance.remove_mailman_delegates(delegates, list)
        print("The response of EmailApi->remove_mailman_delegates:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailApi->remove_mailman_delegates: %s\n" % e)
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
    api_instance = clientapi_cpanel.EmailApi(api_client)
    filter = 'coffee' # str | A mail filter name.  For each mail filter to reorder, supply a `filter*` parameter, where `*` is a number that represents the filter's order.  For example, to set `coffee` as the first email filter and `cheesecloth` as the second, set `coffee` as the `filter1` parameter's value, and `cheesecloth` as the value for the `filter2` parameter.
    mailbox = 'user@example.com' # str | The email address.

    try:
        # Update email address's email filter order
        api_response = api_instance.reorder_filters(filter, mailbox)
        print("The response of EmailApi->reorder_filters:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailApi->reorder_filters: %s\n" % e)
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

# **set_always_accept**
> InlineResponse200198 set_always_accept(domain, alwaysaccept=alwaysaccept, mxcheck=mxcheck)

Update Mail Exchanger type

This function sets the Mail Exchanger (MX) type.

**Note:**

  This function **only** affects the cPanel configuration. You **must** configure the mail exchanger's DNS entry separately.

**Important:**

When you disable the [DNS role](https://go.cpanel.net/howtouseserverprofiles#roles), the system **disables** this function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200198 import InlineResponse200198
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
    api_instance = clientapi_cpanel.EmailApi(api_client)
    domain = 'example.com' # str | The mail exchanger's domain.
    alwaysaccept = auto # str | The mail exchanger type. * `auto` — Allow cPanel to determine the appropriate role. * `local` — Always accept the domain's mail. * `secondary` — Accept mail until a higher priority mail server is available. * `remote` — Do **not** accept mail.  **Note:**  This parameter is redundant with the `mxcheck` parameter. Do **not** enter the `mxcheck` and `alwaysaccept` parameters at the same time. [Undefined behavior](https://en.wikipedia.org/wiki/Undefined_behavior) may occur if this happens. (optional) (default to auto)
    mxcheck = auto # str | The mail exchanger type. * `auto` — Allow cPanel to determine the appropriate role. * `local` — Always accept the domain's mail. * `secondary` — Accept mail until a higher priority mail server is available. * `remote` — Do **not** accept mail.  **Note:**  This parameter is redundant with the `alwaysaccept` parameter. Do **not** enter the `mxcheck` and `alwaysaccept` parameters at the same time. [Undefined behavior](https://en.wikipedia.org/wiki/Undefined_behavior) may occur if this happens. (optional) (default to auto)

    try:
        # Update Mail Exchanger type
        api_response = api_instance.set_always_accept(domain, alwaysaccept=alwaysaccept, mxcheck=mxcheck)
        print("The response of EmailApi->set_always_accept:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailApi->set_always_accept: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**| The mail exchanger&#39;s domain. | 
 **alwaysaccept** | **str**| The mail exchanger type. * &#x60;auto&#x60; — Allow cPanel to determine the appropriate role. * &#x60;local&#x60; — Always accept the domain&#39;s mail. * &#x60;secondary&#x60; — Accept mail until a higher priority mail server is available. * &#x60;remote&#x60; — Do **not** accept mail.  **Note:**  This parameter is redundant with the &#x60;mxcheck&#x60; parameter. Do **not** enter the &#x60;mxcheck&#x60; and &#x60;alwaysaccept&#x60; parameters at the same time. [Undefined behavior](https://en.wikipedia.org/wiki/Undefined_behavior) may occur if this happens. | [optional] [default to auto]
 **mxcheck** | **str**| The mail exchanger type. * &#x60;auto&#x60; — Allow cPanel to determine the appropriate role. * &#x60;local&#x60; — Always accept the domain&#39;s mail. * &#x60;secondary&#x60; — Accept mail until a higher priority mail server is available. * &#x60;remote&#x60; — Do **not** accept mail.  **Note:**  This parameter is redundant with the &#x60;alwaysaccept&#x60; parameter. Do **not** enter the &#x60;mxcheck&#x60; and &#x60;alwaysaccept&#x60; parameters at the same time. [Undefined behavior](https://en.wikipedia.org/wiki/Undefined_behavior) may occur if this happens. | [optional] [default to auto]

### Return type

[**InlineResponse200198**](InlineResponse200198.md)

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
    api_instance = clientapi_cpanel.EmailApi(api_client)
    fwdopt = 'fwd' # str | The method to use to handle unroutable mail. * `fwd` — Forward messages to the `fwdemail` parameter’s address. * `fail` — Bounce messages back to the sender, and include the `failmsgs` parameter’s failure message. * `blackhole` — Send messages to the `/dev/null/` directory. This method does **not** generate a failure notice. * `pipe` — Pipe mail to the `pipefwd` parameter’s application. This parameter requires the [File Storage role](https://go.cpanel.net/serverroles).
    domain = 'example.com' # str | The domain whose default email behavior you want to configure.  **Note**:    This parameter defaults to the cPanel account’s main domain. (optional)
    failmsgs = 'No such person at this address' # str | The failure message for the message’s sender.  **Note**:   Use this parameter if you used the `fail` method for the `fwdopt` parameter. (optional) (default to 'No such person at this address')
    fwdemail = 'admin@example.com' # str | The email address to which the system forwards messages.  **Note**:   Use this parameter if you used the `fwd` method for the `fwdopt` parameter. (optional)
    pipefwd = 'mailscript.pl' # str | The application to which the system pipes messages.  **Note**:    Use this parameter if you used the `pipe` method for the `fwdopt` parameter.  **Important**:    This parameter requires the [File Storage role](https://go.cpanel.net/serverroles). (optional)

    try:
        # Create default email address
        api_response = api_instance.set_default_address(fwdopt, domain=domain, failmsgs=failmsgs, fwdemail=fwdemail, pipefwd=pipefwd)
        print("The response of EmailApi->set_default_address:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailApi->set_default_address: %s\n" % e)
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
    api_instance = clientapi_cpanel.EmailApi(api_client)
    advertised = 1 # int | Whether the Mailman directory page displays the list. * `1` - Display. * `0` - Does **not** display.
    archive_private = 1 # int | Whether the mailing list archive is private. * `1` - Private. * `0` - Public.
    list = 'mylist' # str | The mailing list name.
    subscribe_policy = 1 # int | The level of control that the mailing list administrator has over new subscribers. * `1` - Anyone can subscribe. The system sends a confirmation email. * `2` - The administrator **must** approve subscriptions. The system does **not** send a confirmation email. * `3` - The administrator **must** approve subscriptions. The system sends a confirmation email.

    try:
        # Update mailing list privacy options
        api_response = api_instance.set_list_privacy_options(advertised, archive_private, list, subscribe_policy)
        print("The response of EmailApi->set_list_privacy_options:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailApi->set_list_privacy_options: %s\n" % e)
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
    api_instance = clientapi_cpanel.EmailApi(api_client)
    domain = '\'example.com\'' # str | The domain for which to add a manual MX redirect entry.  **Note:**  * To add multiple domain entries, increment the parameter. For example, use the `domain`, `domain-1`, and `domain-2` parameters. * For multiple domains, you **must** include its corresponding `mx_host` value.
    mx_host = clientapi_cpanel.MxHost() # MxHost | The domain, IPv4, or IPv6 address to redirect the domain value's emails to.  **Note:**   * To add multiple MX hosts, increment the parameter. For example, use the `mx_host`, `mx_host-1`, and `mx_host-2` parameters.  * For multiple MX hosts, you **must** include its corresponding `domain` value.

    try:
        # Add manual MX redirection
        api_response = api_instance.set_manual_mx_redirects(domain, mx_host)
        print("The response of EmailApi->set_manual_mx_redirects:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailApi->set_manual_mx_redirects: %s\n" % e)
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

# **stats_db_status**
> InlineResponse200202 stats_db_status()

Return eximstats SQLite database status

This function returns the status of the eximstats SQLite Database.

**Important:**

When you disable the [Receive Mail role](https://go.cpanel.net/serverroles), the system **disables** this function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200202 import InlineResponse200202
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
    api_instance = clientapi_cpanel.EmailApi(api_client)

    try:
        # Return eximstats SQLite database status
        api_response = api_instance.stats_db_status()
        print("The response of EmailApi->stats_db_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailApi->stats_db_status: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**InlineResponse200202**](InlineResponse200202.md)

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
    api_instance = clientapi_cpanel.EmailApi(api_client)
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
        print("The response of EmailApi->store_filter:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailApi->store_filter: %s\n" % e)
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

# **suspend_incoming**
> InlineResponse200204 suspend_incoming(email=email)

Suspend email account incoming (SMTP) mail

This function suspends incoming email for an account. The system will reject incoming email while the account is suspended.

**Notes:**

* The user can still log in to the email account. To suspend a user's ability to log in to, send mail from, and read their account, use the UAPI `Email::suspend_login` function.
* Use the UAPI `Email::unsuspend_incoming` function to allow the account to receive email.

**Important:**

When you disable the [Receive Mail role](https://go.cpanel.net/serverroles), the system **disables** this function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200204 import InlineResponse200204
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
    api_instance = clientapi_cpanel.EmailApi(api_client)
    email = 'user@example.com' # str | The email user's account name. (optional)

    try:
        # Suspend email account incoming (SMTP) mail
        api_response = api_instance.suspend_incoming(email=email)
        print("The response of EmailApi->suspend_incoming:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailApi->suspend_incoming: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**| The email user&#39;s account name. | [optional] 

### Return type

[**InlineResponse200204**](InlineResponse200204.md)

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

# **suspend_login**
> InlineResponse200205 suspend_login(email)

Suspend email account login

This function suspends a user's ability to log in to their email account. This function immediately suspends the user's login credentials and prevents future authenticated connections to the email account.

**Notes:**

* When you suspend an account, the user's account still receives email.
* To suspend incoming email for an account, use the UAPI `Email::suspend_incoming` function.
* To remove the login suspension for an account, use the UAPI `Email::unsuspend_login` function.

**Important:**

When you disable the [Receive Mail role](https://go.cpanel.net/serverroles), the system **disables** this function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200205 import InlineResponse200205
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
    api_instance = clientapi_cpanel.EmailApi(api_client)
    email = 'user@example.com' # str | The email user's account name.

    try:
        # Suspend email account login
        api_response = api_instance.suspend_login(email)
        print("The response of EmailApi->suspend_login:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailApi->suspend_login: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**| The email user&#39;s account name. | 

### Return type

[**InlineResponse200205**](InlineResponse200205.md)

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

# **suspend_outgoing**
> InlineResponse200206 suspend_outgoing(email)

Suspend email account outgoing mail

This function rejects outgoing mail for a suspended email account. This function does **not** disable a user's login credentials or access permissions to their email account.

**Notes:**

* To suspend a user's login credentials and prevent authenticated connections to the email account, use the UAPI `Email::suspend_login` function.
* To allow an email account to send mail, use the UAPI `Email::unsuspend_outgoing` function.
* To hold outgoing mail in Exim's queue, use the UAPI `Email::hold_outgoing` function.

**Important:**

When you disable the [Send Mail role](https://go.cpanel.net/serverroles), the system **disables** this function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200206 import InlineResponse200206
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
    api_instance = clientapi_cpanel.EmailApi(api_client)
    email = 'username@example.com' # str | The email account's username.

    try:
        # Suspend email account outgoing mail
        api_response = api_instance.suspend_outgoing(email)
        print("The response of EmailApi->suspend_outgoing:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailApi->suspend_outgoing: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**| The email account&#39;s username. | 

### Return type

[**InlineResponse200206**](InlineResponse200206.md)

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
    api_instance = clientapi_cpanel.EmailApi(api_client)
    recipient = 'username@example.com' # str | The email address to which to trace a message delivery path.

    try:
        # Run email delivery route trace
        api_response = api_instance.trace_delivery(recipient)
        print("The response of EmailApi->trace_delivery:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailApi->trace_delivery: %s\n" % e)
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
    api_instance = clientapi_cpanel.EmailApi(api_client)
    msg = 'Test' # str | The string to test. The function uses this string as the body of an email message, to check whether filters would match the string.
    account = 'user@example.com' # str | The email address, to test legacy cPanel filters in the filters directory. If you do not use this parameter, the function tests the main domain's filters in the `/etc/vfilters` directory. (optional)

    try:
        # Run test for main domain email filters
        api_response = api_instance.trace_filter(msg, account=account)
        print("The response of EmailApi->trace_filter:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailApi->trace_filter: %s\n" % e)
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
    api_instance = clientapi_cpanel.EmailApi(api_client)
    domain = '\'example.com\'' # str | The domain for which to add a manual MX redirect entry.  **Note:**  * To add multiple domain entries, increment the parameter. For example, use the `domain`, `domain-1`, and `domain-2` parameters. * For multiple domains, you **must** include its corresponding `mx_host` value.

    try:
        # Remove manual MX redirection
        api_response = api_instance.unset_manual_mx_redirects(domain)
        print("The response of EmailApi->unset_manual_mx_redirects:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailApi->unset_manual_mx_redirects: %s\n" % e)
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

# **unsuspend_incoming**
> InlineResponse200211 unsuspend_incoming(email=email)

Unsuspend email account incoming mail

This function unsuspends incoming email for an email account.

**Important:**

When you disable the [Receive Mail role](https://go.cpanel.net/serverroles), the system **disables** this function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200211 import InlineResponse200211
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
    api_instance = clientapi_cpanel.EmailApi(api_client)
    email = 'user@example.com' # str | The email user's account name. (optional)

    try:
        # Unsuspend email account incoming mail
        api_response = api_instance.unsuspend_incoming(email=email)
        print("The response of EmailApi->unsuspend_incoming:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailApi->unsuspend_incoming: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**| The email user&#39;s account name. | [optional] 

### Return type

[**InlineResponse200211**](InlineResponse200211.md)

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

# **unsuspend_login**
> InlineResponse200212 unsuspend_login(email=email)

Unsuspend email account login

This function restores a user's ability to log in to their email account.

**Note:**

* To suspend a user's ability to log in, use the UAPI `Email::suspend_login` function.
* To suspend incoming email for an account, use the UAPI `Email::suspend_incoming` function.

**Important:**

When you disable the [Receive Mail role](https://go.cpanel.net/serverroles#roles), the system **disables** this function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200212 import InlineResponse200212
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
    api_instance = clientapi_cpanel.EmailApi(api_client)
    email = 'username@example.com' # str | The email user's account name. (optional)

    try:
        # Unsuspend email account login
        api_response = api_instance.unsuspend_login(email=email)
        print("The response of EmailApi->unsuspend_login:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailApi->unsuspend_login: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**| The email user&#39;s account name. | [optional] 

### Return type

[**InlineResponse200212**](InlineResponse200212.md)

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

# **unsuspend_outgoing**
> InlineResponse200213 unsuspend_outgoing(email)

Unsuspend email account outgoing mail

This function cancels the suspension action put in place by the UAPI `Email::suspend_outgoing`
function for outgoing mail for an email account.

**Note:**

To suspend an email account and reject all outgoing mail, use the UAPI `Email::suspend_outgoing` function.        

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200213 import InlineResponse200213
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
    api_instance = clientapi_cpanel.EmailApi(api_client)
    email = 'username@example.com' # str | The email account's username.

    try:
        # Unsuspend email account outgoing mail
        api_response = api_instance.unsuspend_outgoing(email)
        print("The response of EmailApi->unsuspend_outgoing:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailApi->unsuspend_outgoing: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**| The email account&#39;s username. | 

### Return type

[**InlineResponse200213**](InlineResponse200213.md)

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
    api_instance = clientapi_cpanel.EmailApi(api_client)
    email = 'username@example.com' # str | The email account address.
    password = '123456luggage' # str | The email account password.

    try:
        # Validate email account password
        api_response = api_instance.verify_password(email, password)
        print("The response of EmailApi->verify_password:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailApi->verify_password: %s\n" % e)
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

