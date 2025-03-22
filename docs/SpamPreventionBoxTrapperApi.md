# clientapi_cpanel.SpamPreventionBoxTrapperApi

All URIs are relative to *https://cpanel-server.tld:2083/execute*

Method | HTTP request | Description
------------- | ------------- | -------------
[**blacklist_messages**](SpamPreventionBoxTrapperApi.md#blacklist_messages) | **GET** /BoxTrapper/blacklist_messages | Add email address to BoxTrapper blocked senders
[**box_trapper_get_allowlist**](SpamPreventionBoxTrapperApi.md#box_trapper_get_allowlist) | **GET** /BoxTrapper/get_allowlist | Return account BoxTrapper allowlist rules
[**box_trapper_get_blocklist**](SpamPreventionBoxTrapperApi.md#box_trapper_get_blocklist) | **GET** /BoxTrapper/get_blocklist | Return account BoxTrapper blocklist rules
[**box_trapper_get_ignorelist**](SpamPreventionBoxTrapperApi.md#box_trapper_get_ignorelist) | **GET** /BoxTrapper/get_ignorelist | Return account BoxTrapper ignorelist rules
[**box_trapper_set_allowlist**](SpamPreventionBoxTrapperApi.md#box_trapper_set_allowlist) | **GET** /BoxTrapper/set_allowlist | Update account BoxTrapper allowlist
[**box_trapper_set_blocklist**](SpamPreventionBoxTrapperApi.md#box_trapper_set_blocklist) | **GET** /BoxTrapper/set_blocklist | Update account BoxTrapper blocklist
[**box_trapper_set_ignorelist**](SpamPreventionBoxTrapperApi.md#box_trapper_set_ignorelist) | **GET** /BoxTrapper/set_ignorelist | Update account BoxTrapper ignorelist
[**delete_messages**](SpamPreventionBoxTrapperApi.md#delete_messages) | **GET** /BoxTrapper/delete_messages | Delete messages in the BoxTrapper queue
[**deliver_messages**](SpamPreventionBoxTrapperApi.md#deliver_messages) | **GET** /BoxTrapper/deliver_messages | Send messages in the BoxTrapper queue
[**get_configuration**](SpamPreventionBoxTrapperApi.md#get_configuration) | **GET** /BoxTrapper/get_configuration | Return email account&#39;s BoxTrapper configuration
[**get_email_template**](SpamPreventionBoxTrapperApi.md#get_email_template) | **GET** /BoxTrapper/get_email_template | Return specified BoxTrapper email template
[**get_forwarders**](SpamPreventionBoxTrapperApi.md#get_forwarders) | **GET** /BoxTrapper/get_forwarders | Return all BoxTrapper forwarders
[**get_log**](SpamPreventionBoxTrapperApi.md#get_log) | **GET** /BoxTrapper/get_log | Return BoxTrapper log file and contents
[**get_message**](SpamPreventionBoxTrapperApi.md#get_message) | **GET** /BoxTrapper/get_message | Return message&#39;s top 200 lines in BoxTrapper queue
[**get_status**](SpamPreventionBoxTrapperApi.md#get_status) | **GET** /BoxTrapper/get_status | Return whether email account uses BoxTrapper
[**ignore_messages**](SpamPreventionBoxTrapperApi.md#ignore_messages) | **GET** /BoxTrapper/ignore_messages | Add email account to Exim ignore list
[**list_email_templates**](SpamPreventionBoxTrapperApi.md#list_email_templates) | **GET** /BoxTrapper/list_email_templates | Return BoxTrapper email templates
[**list_queued_messages**](SpamPreventionBoxTrapperApi.md#list_queued_messages) | **GET** /BoxTrapper/list_queued_messages | Return email account&#39;s BoxTrapper queued messages
[**process_messages**](SpamPreventionBoxTrapperApi.md#process_messages) | **GET** /BoxTrapper/process_messages | Run a specific BoxTrapper action for a message
[**reset_email_template**](SpamPreventionBoxTrapperApi.md#reset_email_template) | **GET** /BoxTrapper/reset_email_template | Restore default BoxTrapper email message template
[**save_configuration**](SpamPreventionBoxTrapperApi.md#save_configuration) | **GET** /BoxTrapper/save_configuration | Update email account&#39;s BoxTrapper configuration
[**save_email_template**](SpamPreventionBoxTrapperApi.md#save_email_template) | **GET** /BoxTrapper/save_email_template | Save BoxTrapper message template contents
[**set_forwarders**](SpamPreventionBoxTrapperApi.md#set_forwarders) | **GET** /BoxTrapper/set_forwarders | Add email address to BoxTrapper forwarders
[**set_status**](SpamPreventionBoxTrapperApi.md#set_status) | **GET** /BoxTrapper/set_status | Enable or disable BoxTrapper for email account
[**whitelist_messages**](SpamPreventionBoxTrapperApi.md#whitelist_messages) | **GET** /BoxTrapper/whitelist_messages | Add email address to BoxTrapper allowed senders


# **blacklist_messages**
> InlineResponse20017 blacklist_messages(email, queuefile)

Add email address to BoxTrapper blocked senders

This function blacklists email message senders.

**Important:**

  When you disable the [Receive Mail](https://go.cpanel.net/serverroles) role, the system disables this function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response20017 import InlineResponse20017
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
    api_instance = clientapi_cpanel.SpamPreventionBoxTrapperApi(api_client)
    email = 'user@example.com' # str | The email address for which to blacklist messages.  **Warning:**  If you call this function in Webmail, the system ignores this parameter and defaults to the currently-authenticated user.
    queuefile = 'queuefile=file1&queuefile=file2' # str | The filename of the email message to blacklist.

    try:
        # Add email address to BoxTrapper blocked senders
        api_response = api_instance.blacklist_messages(email, queuefile)
        print("The response of SpamPreventionBoxTrapperApi->blacklist_messages:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SpamPreventionBoxTrapperApi->blacklist_messages: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**| The email address for which to blacklist messages.  **Warning:**  If you call this function in Webmail, the system ignores this parameter and defaults to the currently-authenticated user. | 
 **queuefile** | **str**| The filename of the email message to blacklist. | 

### Return type

[**InlineResponse20017**](InlineResponse20017.md)

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

# **box_trapper_get_allowlist**
> InlineResponse20020 box_trapper_get_allowlist(email)

Return account BoxTrapper allowlist rules

This function retrieves a list of BoxTrapper allowlist configuration rules. BoxTrapper will deliver emails that match these rules.

**Important:**

When you disable the
[*Receive Mail* role](https://go.cpanel.net/serverroles),
the system **disables** this function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response20020 import InlineResponse20020
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
    api_instance = clientapi_cpanel.SpamPreventionBoxTrapperApi(api_client)
    email = 'user@example.com' # str | A valid email address on the cPanel account.  **Warning:**  If you call this function in Webmail, the system overrides this parameter. This parameter defaults to the current email address.

    try:
        # Return account BoxTrapper allowlist rules
        api_response = api_instance.box_trapper_get_allowlist(email)
        print("The response of SpamPreventionBoxTrapperApi->box_trapper_get_allowlist:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SpamPreventionBoxTrapperApi->box_trapper_get_allowlist: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**| A valid email address on the cPanel account.  **Warning:**  If you call this function in Webmail, the system overrides this parameter. This parameter defaults to the current email address. | 

### Return type

[**InlineResponse20020**](InlineResponse20020.md)

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

# **box_trapper_get_blocklist**
> InlineResponse20021 box_trapper_get_blocklist(email)

Return account BoxTrapper blocklist rules

This function retrieves a list of BoxTrapper blocklist configuration rules. BoxTrapper will delete messages that match these rules and send a notification to the sender.

**Important:**

When you disable the
[*Receive Mail* role](https://go.cpanel.net/serverroles),
the system **disables** this function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response20021 import InlineResponse20021
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
    api_instance = clientapi_cpanel.SpamPreventionBoxTrapperApi(api_client)
    email = 'user@example.com' # str | A valid email address on the cPanel account.  **Warning:**  If you call this function in Webmail, the system overrides this parameter. This parameter defaults to the current email address.

    try:
        # Return account BoxTrapper blocklist rules
        api_response = api_instance.box_trapper_get_blocklist(email)
        print("The response of SpamPreventionBoxTrapperApi->box_trapper_get_blocklist:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SpamPreventionBoxTrapperApi->box_trapper_get_blocklist: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**| A valid email address on the cPanel account.  **Warning:**  If you call this function in Webmail, the system overrides this parameter. This parameter defaults to the current email address. | 

### Return type

[**InlineResponse20021**](InlineResponse20021.md)

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

# **box_trapper_get_ignorelist**
> InlineResponse20025 box_trapper_get_ignorelist(email)

Return account BoxTrapper ignorelist rules

This function retrieves a list of BoxTrapper ignorelist configuration rules. BoxTrapper will delete messages that match these rules without sending a notification to the sender.

**Important:**

When you disable the
[*Receive Mail* role](https://go.cpanel.net/serverroles),
the system **disables** this function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response20025 import InlineResponse20025
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
    api_instance = clientapi_cpanel.SpamPreventionBoxTrapperApi(api_client)
    email = 'user@example.com' # str | A valid email address on the cPanel account.  **Warning:**  If you call this function in Webmail, the system overrides this parameter. This parameter defaults to the current email address.

    try:
        # Return account BoxTrapper ignorelist rules
        api_response = api_instance.box_trapper_get_ignorelist(email)
        print("The response of SpamPreventionBoxTrapperApi->box_trapper_get_ignorelist:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SpamPreventionBoxTrapperApi->box_trapper_get_ignorelist: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**| A valid email address on the cPanel account.  **Warning:**  If you call this function in Webmail, the system overrides this parameter. This parameter defaults to the current email address. | 

### Return type

[**InlineResponse20025**](InlineResponse20025.md)

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

# **box_trapper_set_allowlist**
> InlineResponse20036 box_trapper_set_allowlist(email, rules)

Update account BoxTrapper allowlist

This function sets the BoxTrapper allowlist configuration rules. BoxTrapper will deliver emails that match these rules.

**Important:**

When you disable the
[*Receive Mail* role](https://go.cpanel.net/serverroles),
the system **disables** this function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response20036 import InlineResponse20036
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
    api_instance = clientapi_cpanel.SpamPreventionBoxTrapperApi(api_client)
    email = 'user@example.com' # str | A valid email address on the cPanel account.  **Warning:**  If you call this function in Webmail, the system overrides this parameter. This parameter defaults to the current email address.
    rules = ['rules-1=\'allowlisted-email\\@domain\\.com\' rules-2=\'from allowlisted-email2\\@domain\\.com\' rules-3=\'to domain2\\.com\''] # List[str] | An array of allowlist rules.  **Note:**  You can set multiple allowlist rules, duplicate or increment the parameter name. For example, `rules-1`, `rules-2`, and `rules-3`.

    try:
        # Update account BoxTrapper allowlist
        api_response = api_instance.box_trapper_set_allowlist(email, rules)
        print("The response of SpamPreventionBoxTrapperApi->box_trapper_set_allowlist:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SpamPreventionBoxTrapperApi->box_trapper_set_allowlist: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**| A valid email address on the cPanel account.  **Warning:**  If you call this function in Webmail, the system overrides this parameter. This parameter defaults to the current email address. | 
 **rules** | [**List[str]**](str.md)| An array of allowlist rules.  **Note:**  You can set multiple allowlist rules, duplicate or increment the parameter name. For example, &#x60;rules-1&#x60;, &#x60;rules-2&#x60;, and &#x60;rules-3&#x60;. | 

### Return type

[**InlineResponse20036**](InlineResponse20036.md)

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

# **box_trapper_set_blocklist**
> InlineResponse20037 box_trapper_set_blocklist(email, rules)

Update account BoxTrapper blocklist

This function sets the BoxTrapper blocklist configuration rules. BoxTrapper will delete messages that match these rules and send a notification to the sender.

**Important:**

When you disable the
[*Receive Mail* role](https://go.cpanel.net/serverroles),
the system **disables** this function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response20037 import InlineResponse20037
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
    api_instance = clientapi_cpanel.SpamPreventionBoxTrapperApi(api_client)
    email = 'user@example.com' # str | A valid email address on the cPanel account.  **Warning:**  If you call this function in Webmail, the system overrides this parameter. This parameter defaults to the current email address.
    rules = ['rules-1=\'blocklisted-email\\@domain\\.com\' rules-2=\'from blocklisted-email2\\@domain\\.com\' rules-3=\'to domain2\\.com\''] # List[str] | An array of blocklist rules.  **Note:**  You can set multiple block rules, duplicate or increment the parameter name. For example, `rules-1`, `rules-2`, and `rules-3`.

    try:
        # Update account BoxTrapper blocklist
        api_response = api_instance.box_trapper_set_blocklist(email, rules)
        print("The response of SpamPreventionBoxTrapperApi->box_trapper_set_blocklist:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SpamPreventionBoxTrapperApi->box_trapper_set_blocklist: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**| A valid email address on the cPanel account.  **Warning:**  If you call this function in Webmail, the system overrides this parameter. This parameter defaults to the current email address. | 
 **rules** | [**List[str]**](str.md)| An array of blocklist rules.  **Note:**  You can set multiple block rules, duplicate or increment the parameter name. For example, &#x60;rules-1&#x60;, &#x60;rules-2&#x60;, and &#x60;rules-3&#x60;. | 

### Return type

[**InlineResponse20037**](InlineResponse20037.md)

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

# **box_trapper_set_ignorelist**
> InlineResponse20039 box_trapper_set_ignorelist(email, rules)

Update account BoxTrapper ignorelist

This function sets the BoxTrapper ignorelist configuration rules. BoxTrapper will delete messages that match these rules without sending a notification to the sender.

**Important:**

When you disable the
[*Receive Mail* role](https://go.cpanel.net/serverroles),
the system **disables** this function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response20039 import InlineResponse20039
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
    api_instance = clientapi_cpanel.SpamPreventionBoxTrapperApi(api_client)
    email = 'user@example.com' # str | A valid email address on the cPanel account.  **Warning:**  If you call this function in Webmail, the system overrides this parameter. This parameter defaults to the current email address.
    rules = ['rules-1=\'ignored-email\\@domain\\.com\' rules-2=\'from ignored-email2\\@domain\\.com\' rules-3=\'to domain2\\.com\''] # List[str] | An array of ignorelist rules.  **Note:**  You can set multiple ignore rules, duplicate or increment the parameter name. For example, `rules-1`, `rules-2`, and `rules-3`.

    try:
        # Update account BoxTrapper ignorelist
        api_response = api_instance.box_trapper_set_ignorelist(email, rules)
        print("The response of SpamPreventionBoxTrapperApi->box_trapper_set_ignorelist:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SpamPreventionBoxTrapperApi->box_trapper_set_ignorelist: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**| A valid email address on the cPanel account.  **Warning:**  If you call this function in Webmail, the system overrides this parameter. This parameter defaults to the current email address. | 
 **rules** | [**List[str]**](str.md)| An array of ignorelist rules.  **Note:**  You can set multiple ignore rules, duplicate or increment the parameter name. For example, &#x60;rules-1&#x60;, &#x60;rules-2&#x60;, and &#x60;rules-3&#x60;. | 

### Return type

[**InlineResponse20039**](InlineResponse20039.md)

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

# **delete_messages**
> InlineResponse20018 delete_messages(email, queuefile, all_like=all_like)

Delete messages in the BoxTrapper queue

This function deletes messages in the BoxTrapper queue.

**Important:**

When you disable the [Receive Mail](https://go.cpanel.net/serverroles) role, the system disables this function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response20018 import InlineResponse20018
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
    api_instance = clientapi_cpanel.SpamPreventionBoxTrapperApi(api_client)
    email = 'user@example.com' # str | The account's email address.  **Warning:**  If you call this function in Webmail, the system ignores this parameter and defaults to the currently-authenticated email address.
    queuefile = 'queuefile=file1.msg&queuefile=file2.msg' # str | The filename of the email message who's sender to delete.    **Warning:**   To delete multiple email message senders, duplicate the parameter name.
    all_like = 0 # int | Whether to delete all messages that resemble the `queuefile` parameter's value.  * `1` - Delete all messages resembling the `queuefile` parameter. * `0` - Do **not** delete all messages resembling the `queuefile` parameter. (optional) (default to 0)

    try:
        # Delete messages in the BoxTrapper queue
        api_response = api_instance.delete_messages(email, queuefile, all_like=all_like)
        print("The response of SpamPreventionBoxTrapperApi->delete_messages:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SpamPreventionBoxTrapperApi->delete_messages: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**| The account&#39;s email address.  **Warning:**  If you call this function in Webmail, the system ignores this parameter and defaults to the currently-authenticated email address. | 
 **queuefile** | **str**| The filename of the email message who&#39;s sender to delete.    **Warning:**   To delete multiple email message senders, duplicate the parameter name. | 
 **all_like** | **int**| Whether to delete all messages that resemble the &#x60;queuefile&#x60; parameter&#39;s value.  * &#x60;1&#x60; - Delete all messages resembling the &#x60;queuefile&#x60; parameter. * &#x60;0&#x60; - Do **not** delete all messages resembling the &#x60;queuefile&#x60; parameter. | [optional] [default to 0]

### Return type

[**InlineResponse20018**](InlineResponse20018.md)

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

# **deliver_messages**
> InlineResponse20019 deliver_messages(email, queuefile, all_like=all_like)

Send messages in the BoxTrapper queue

This function delivers messages in the BoxTrapper queue.

**Important:**

When you disable the
[*Receive Mail* role](https://docs.cpanel.net/knowledge-base/general-systems-administration/how-to-use-server-profiles/#roles),
the system **disables** this function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response20019 import InlineResponse20019
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
    api_instance = clientapi_cpanel.SpamPreventionBoxTrapperApi(api_client)
    email = 'user@example.com' # str | The sender's cPanel account email address for which to deliver email messages.  **Warning:**  If you call this function in Webmail, the system ignores this parameter and defaults to the currently-authenticated email address.
    queuefile = 'queuefile=example.msg&queuefile=example1.msg&queuefile=example2.msg' # str | The filename of the email messages to deliver.  **Note:**  To deliver multiple email messages, pass this parameter multiple times.
    all_like = 0 # int | Whether to deliver all messages that resemble the `queuefile` parameter's value.  * `1` - Deliver all similar messages. * `0` - Don't deliver all similar messages. (optional) (default to 0)

    try:
        # Send messages in the BoxTrapper queue
        api_response = api_instance.deliver_messages(email, queuefile, all_like=all_like)
        print("The response of SpamPreventionBoxTrapperApi->deliver_messages:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SpamPreventionBoxTrapperApi->deliver_messages: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**| The sender&#39;s cPanel account email address for which to deliver email messages.  **Warning:**  If you call this function in Webmail, the system ignores this parameter and defaults to the currently-authenticated email address. | 
 **queuefile** | **str**| The filename of the email messages to deliver.  **Note:**  To deliver multiple email messages, pass this parameter multiple times. | 
 **all_like** | **int**| Whether to deliver all messages that resemble the &#x60;queuefile&#x60; parameter&#39;s value.  * &#x60;1&#x60; - Deliver all similar messages. * &#x60;0&#x60; - Don&#39;t deliver all similar messages. | [optional] [default to 0]

### Return type

[**InlineResponse20019**](InlineResponse20019.md)

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

# **get_configuration**
> InlineResponse20022 get_configuration(email)

Return email account's BoxTrapper configuration

This function retrieves an account's BoxTrapper configuration.

**Important:**

  When you disable the [Receive Mail](https://go.cpanel.net/serverroles) role, the system disables this function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response20022 import InlineResponse20022
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
    api_instance = clientapi_cpanel.SpamPreventionBoxTrapperApi(api_client)
    email = 'user@example.com' # str | The account's email address.  **Warning:**  If you call this function in Webmail, the system ignores this parameter and defaults to the currently-authenticated email address.

    try:
        # Return email account's BoxTrapper configuration
        api_response = api_instance.get_configuration(email)
        print("The response of SpamPreventionBoxTrapperApi->get_configuration:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SpamPreventionBoxTrapperApi->get_configuration: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**| The account&#39;s email address.  **Warning:**  If you call this function in Webmail, the system ignores this parameter and defaults to the currently-authenticated email address. | 

### Return type

[**InlineResponse20022**](InlineResponse20022.md)

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

# **get_email_template**
> InlineResponse20023 get_email_template(email, template)

Return specified BoxTrapper email template

This function retrieves a BoxTrapper email message template.

**Important:**

  When you disable the
  [*Receive Mail* role](https://go.cpanel.net/serverroles),
  the system **disables** this function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response20023 import InlineResponse20023
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
    api_instance = clientapi_cpanel.SpamPreventionBoxTrapperApi(api_client)
    email = 'user@example.com' # str | A valid email address on the cPanel account.  **Warning:**  If you call this function in Webmail, the system overrides this parameter. This parameter defaults to the current email address.
    template = 'verify' # str | The message template.  * `blacklist` * `returnverify` * `verifyreleased` * `verify`  **Note:**  For more information on each template, read our [BoxTrapper](https://go.cpanel.net/cpaneldocsBoxTrapper) documentation.

    try:
        # Return specified BoxTrapper email template
        api_response = api_instance.get_email_template(email, template)
        print("The response of SpamPreventionBoxTrapperApi->get_email_template:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SpamPreventionBoxTrapperApi->get_email_template: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**| A valid email address on the cPanel account.  **Warning:**  If you call this function in Webmail, the system overrides this parameter. This parameter defaults to the current email address. | 
 **template** | **str**| The message template.  * &#x60;blacklist&#x60; * &#x60;returnverify&#x60; * &#x60;verifyreleased&#x60; * &#x60;verify&#x60;  **Note:**  For more information on each template, read our [BoxTrapper](https://go.cpanel.net/cpaneldocsBoxTrapper) documentation. | 

### Return type

[**InlineResponse20023**](InlineResponse20023.md)

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

# **get_forwarders**
> InlineResponse20024 get_forwarders(email)

Return all BoxTrapper forwarders

This function retrieves a list of email addresses to which BoxTrapper forwards email messages.

**Important:**

When you disable the [Receive Mail](https://go.cpanel.net/serverroles) role, the system **disables** this function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response20024 import InlineResponse20024
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
    api_instance = clientapi_cpanel.SpamPreventionBoxTrapperApi(api_client)
    email = 'user@example.com' # str | The account's email address.  **Important:**  If you call this function in Webmail, the system ignores this parameter and defaults to the currently-authenticated email address.

    try:
        # Return all BoxTrapper forwarders
        api_response = api_instance.get_forwarders(email)
        print("The response of SpamPreventionBoxTrapperApi->get_forwarders:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SpamPreventionBoxTrapperApi->get_forwarders: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**| The account&#39;s email address.  **Important:**  If you call this function in Webmail, the system ignores this parameter and defaults to the currently-authenticated email address. | 

### Return type

[**InlineResponse20024**](InlineResponse20024.md)

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

# **get_log**
> InlineResponse20026 get_log(email, var_date=var_date)

Return BoxTrapper log file and contents

This function returns the account's BoxTrapper log file and its contents.

**Important:**

When you disable the [Receive Mail role](https://docs.cpanel.net/knowledge-base/general-systems-administration/how-to-use-server-profiles/#roles), the system **disables** this function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response20026 import InlineResponse20026
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
    api_instance = clientapi_cpanel.SpamPreventionBoxTrapperApi(api_client)
    email = 'user@example.com' # str | The account's email address.  **Important:**  If you call this function in Webmail, the system ignores this parameter and defaults to the currently authenticated email address.
    var_date = 1556812881 # int | The date for which to return the log file and its contents.  **Note:**  This parameter defaults to the current date. (optional)

    try:
        # Return BoxTrapper log file and contents
        api_response = api_instance.get_log(email, var_date=var_date)
        print("The response of SpamPreventionBoxTrapperApi->get_log:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SpamPreventionBoxTrapperApi->get_log: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**| The account&#39;s email address.  **Important:**  If you call this function in Webmail, the system ignores this parameter and defaults to the currently authenticated email address. | 
 **var_date** | **int**| The date for which to return the log file and its contents.  **Note:**  This parameter defaults to the current date. | [optional] 

### Return type

[**InlineResponse20026**](InlineResponse20026.md)

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

# **get_message**
> InlineResponse20027 get_message(email, queuefile)

Return message's top 200 lines in BoxTrapper queue

This function returns the first 200 lines of an email in the BoxTrapper queue.

**Important:**

When you disable the [Receive Mail](https://go.cpanel.net/serverroles) role, the system **disables** this function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response20027 import InlineResponse20027
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
    api_instance = clientapi_cpanel.SpamPreventionBoxTrapperApi(api_client)
    email = clientapi_cpanel.Email() # Email | The account’s name, either an email address or the cPanel user’s username.  **Important:**   If you call this function in Webmail, the system ignores this parameter.
    queuefile = 'example.msg' # str | The message's filename.

    try:
        # Return message's top 200 lines in BoxTrapper queue
        api_response = api_instance.get_message(email, queuefile)
        print("The response of SpamPreventionBoxTrapperApi->get_message:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SpamPreventionBoxTrapperApi->get_message: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | [**Email**](.md)| The account’s name, either an email address or the cPanel user’s username.  **Important:**   If you call this function in Webmail, the system ignores this parameter. | 
 **queuefile** | **str**| The message&#39;s filename. | 

### Return type

[**InlineResponse20027**](InlineResponse20027.md)

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

# **get_status**
> InlineResponse20028 get_status(email)

Return whether email account uses BoxTrapper

This function checks whether BoxTrapper is enabled for an email account.

**Important:**

When you disable the [Receive Mail role](https://docs.cpanel.net/knowledge-base/general-systems-administration/how-to-use-server-profiles/#roles), the system **disables** this function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response20028 import InlineResponse20028
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
    api_instance = clientapi_cpanel.SpamPreventionBoxTrapperApi(api_client)
    email = 'user@example.com' # str | The account's email address.  **Important:**  If you call this function in Webmail, the system ignores this parameter.

    try:
        # Return whether email account uses BoxTrapper
        api_response = api_instance.get_status(email)
        print("The response of SpamPreventionBoxTrapperApi->get_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SpamPreventionBoxTrapperApi->get_status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**| The account&#39;s email address.  **Important:**  If you call this function in Webmail, the system ignores this parameter. | 

### Return type

[**InlineResponse20028**](InlineResponse20028.md)

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

# **ignore_messages**
> InlineResponse20029 ignore_messages(email, queuefile)

Add email account to Exim ignore list

This function marks email message senders for Exim to ignore.

**Important:**

When you disable the [Receive Mail role](https://go.cpanel.net/howtouseserverprofiles#roles), the system **disables** this function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response20029 import InlineResponse20029
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
    api_instance = clientapi_cpanel.SpamPreventionBoxTrapperApi(api_client)
    email = 'user@example.com' # str | The cPanel email account from which to ignore messages.  **Warning:**   If you call this function in Webmail, the system ignores this parameter and defaults to the currently-authenticated email address.
    queuefile = 'queuefile-1=example1.msg queuefile-2=example2.msg queuefile-3=example3.msg' # str | The filename of the email message to ignore.  **Note:**   To ignore multiple email messages, duplicate this parameter.

    try:
        # Add email account to Exim ignore list
        api_response = api_instance.ignore_messages(email, queuefile)
        print("The response of SpamPreventionBoxTrapperApi->ignore_messages:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SpamPreventionBoxTrapperApi->ignore_messages: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**| The cPanel email account from which to ignore messages.  **Warning:**   If you call this function in Webmail, the system ignores this parameter and defaults to the currently-authenticated email address. | 
 **queuefile** | **str**| The filename of the email message to ignore.  **Note:**   To ignore multiple email messages, duplicate this parameter. | 

### Return type

[**InlineResponse20029**](InlineResponse20029.md)

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

# **list_email_templates**
> InlineResponse20030 list_email_templates()

Return BoxTrapper email templates

This function lists the BoxTrapper email templates.

**Important:**

When you **disable** the [Receive Mail](https://go.cpanel.net/serverroles) role, the system disables this function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response20030 import InlineResponse20030
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
    api_instance = clientapi_cpanel.SpamPreventionBoxTrapperApi(api_client)

    try:
        # Return BoxTrapper email templates
        api_response = api_instance.list_email_templates()
        print("The response of SpamPreventionBoxTrapperApi->list_email_templates:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SpamPreventionBoxTrapperApi->list_email_templates: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**InlineResponse20030**](InlineResponse20030.md)

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

# **list_queued_messages**
> InlineResponse20031 list_queued_messages(email, var_date=var_date)

Return email account's BoxTrapper queued messages

This function returns a list of messages in the account's BoxTrapper queue.

**Important:**

  When you disable the [*Receive Mail* role](https://go.cpanel.net/serverroles), the system **disables**
  this function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response20031 import InlineResponse20031
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
    api_instance = clientapi_cpanel.SpamPreventionBoxTrapperApi(api_client)
    email = 'user@example.com' # str | The email account for which to retrieve queued messages.  **Important:**  If you call this function in Webmail, the system ignores this parameter and defaults to the currently authenticated email address.
    var_date = 1556812881 # int | The date for which to return queued messages. (optional)

    try:
        # Return email account's BoxTrapper queued messages
        api_response = api_instance.list_queued_messages(email, var_date=var_date)
        print("The response of SpamPreventionBoxTrapperApi->list_queued_messages:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SpamPreventionBoxTrapperApi->list_queued_messages: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**| The email account for which to retrieve queued messages.  **Important:**  If you call this function in Webmail, the system ignores this parameter and defaults to the currently authenticated email address. | 
 **var_date** | **int**| The date for which to return queued messages. | [optional] 

### Return type

[**InlineResponse20031**](InlineResponse20031.md)

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

# **process_messages**
> InlineResponse20032 process_messages(action, queuefile, email=email)

Run a specific BoxTrapper action for a message

This function performs a specified action on messages in the BoxTrapper queue.

**Important:**

When you disable the [*Receive Mail*](https://go.cpanel.net/serverroles#roles) role, the system **disables** this function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response20032 import InlineResponse20032
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
    api_instance = clientapi_cpanel.SpamPreventionBoxTrapperApi(api_client)
    action = 'action=blacklist action=deleteall' # str | The action to perform on the email message file. To perform multiple actions on the specified email messages, pass this parameter multiple times.  * `deliver` — Deliver a specific message. * `deliverall` — Deliver all messages from a sender. * `delete` — Delete a message. * `deleteall` — Delete all messages from a sender. * `blacklist` — Blacklist the sender of an email message. * `whitelist` — Whitelist the sender of an email message. * `ignore` — Ignore email messages from a sender.  **Note:**  The function performs the actions on the email messages files in the order that you pass each action.
    queuefile = 'email=example.msg email=example1.msg email=example2.msg' # str | The filename of the email message to process. To process multiple email messages, pass this parameter multiple times.
    email = 'user@example.com' # str | The account's email address.  **Warning:**  * The `email` parameter is required when this function is called **outside** of Webmail. * If you call this function in Webmail, the `email` parameter is **not** required, and the system overrides this parameter with the current authenticated user's email address. (optional)

    try:
        # Run a specific BoxTrapper action for a message
        api_response = api_instance.process_messages(action, queuefile, email=email)
        print("The response of SpamPreventionBoxTrapperApi->process_messages:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SpamPreventionBoxTrapperApi->process_messages: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **action** | **str**| The action to perform on the email message file. To perform multiple actions on the specified email messages, pass this parameter multiple times.  * &#x60;deliver&#x60; — Deliver a specific message. * &#x60;deliverall&#x60; — Deliver all messages from a sender. * &#x60;delete&#x60; — Delete a message. * &#x60;deleteall&#x60; — Delete all messages from a sender. * &#x60;blacklist&#x60; — Blacklist the sender of an email message. * &#x60;whitelist&#x60; — Whitelist the sender of an email message. * &#x60;ignore&#x60; — Ignore email messages from a sender.  **Note:**  The function performs the actions on the email messages files in the order that you pass each action. | 
 **queuefile** | **str**| The filename of the email message to process. To process multiple email messages, pass this parameter multiple times. | 
 **email** | **str**| The account&#39;s email address.  **Warning:**  * The &#x60;email&#x60; parameter is required when this function is called **outside** of Webmail. * If you call this function in Webmail, the &#x60;email&#x60; parameter is **not** required, and the system overrides this parameter with the current authenticated user&#39;s email address. | [optional] 

### Return type

[**InlineResponse20032**](InlineResponse20032.md)

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

# **reset_email_template**
> InlineResponse20033 reset_email_template(template, email=email)

Restore default BoxTrapper email message template

This function restores the BoxTrapper email message templates to the system default setting.

**Important:**

When you **disable** the [Receive Mail](https://go.cpanel.net/serverroles) role, the system disables this function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response20033 import InlineResponse20033
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
    api_instance = clientapi_cpanel.SpamPreventionBoxTrapperApi(api_client)
    template = 'verify' # str | The message template. Possible values: * `blacklist` - BoxTrapper responds with this message when a blacklisted address sends an email. * `verify` - BoxTrapper responds with this message when an address that does not exist on the whitelist or blacklist sends an email. This message requests a response to confirm that the sender is legitimate. * `verifyreleased` - BoxTrapper responds with this message when a person responds to the verify message with an email or a click on the verification link. * `returnverify` - BoxTrapper responds with this message when the verification process fails.
    email = 'user@example.com' # str | The account's email address.  **Warning:**  The `email` parameter is required when this function is called outside of webmail. If you call this function in Webmail, the `email` parameter is not required, and the system overrides this parameter with the current authenticated user's email address. (optional)

    try:
        # Restore default BoxTrapper email message template
        api_response = api_instance.reset_email_template(template, email=email)
        print("The response of SpamPreventionBoxTrapperApi->reset_email_template:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SpamPreventionBoxTrapperApi->reset_email_template: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template** | **str**| The message template. Possible values: * &#x60;blacklist&#x60; - BoxTrapper responds with this message when a blacklisted address sends an email. * &#x60;verify&#x60; - BoxTrapper responds with this message when an address that does not exist on the whitelist or blacklist sends an email. This message requests a response to confirm that the sender is legitimate. * &#x60;verifyreleased&#x60; - BoxTrapper responds with this message when a person responds to the verify message with an email or a click on the verification link. * &#x60;returnverify&#x60; - BoxTrapper responds with this message when the verification process fails. | 
 **email** | **str**| The account&#39;s email address.  **Warning:**  The &#x60;email&#x60; parameter is required when this function is called outside of webmail. If you call this function in Webmail, the &#x60;email&#x60; parameter is not required, and the system overrides this parameter with the current authenticated user&#39;s email address. | [optional] 

### Return type

[**InlineResponse20033**](InlineResponse20033.md)

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

# **save_configuration**
> InlineResponse20034 save_configuration(email, enable_auto_whitelist, from_addresses, queue_days, whitelist_by_association, from_name=from_name, spam_score=spam_score)

Update email account's BoxTrapper configuration

This function modifies an account's BoxTrapper configuration.

**Important:**

When you disable the [Receive Mail](https://go.cpanel.net/serverroles) role, the system **disables** this function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response20034 import InlineResponse20034
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
    api_instance = clientapi_cpanel.SpamPreventionBoxTrapperApi(api_client)
    email = 'user@example.com' # str | The account's email address.  **Warning:**  If you call this function in Webmail, the system ignores this parameter and defaults to the currently-authenticated email address.
    enable_auto_whitelist = 1 # int | Whether to enable automatic whitelisting for the account.  * `1` - Enable. * `0` - Disable.
    from_addresses = 'sender1@test.com,sender2@test.com' # str | A comma-separated list of email addresses that the system uses when it sends messages back to the original message senders.
    queue_days = 14 # int | The number of days to retain log files and queued messages.
    whitelist_by_association = 1 # int | Whether to whitelist the email addresses in a message's *To* and *From* sections, including carbon-copied (CC) recipients.  * `1` - Whitelist. * `0` - Do **not** whitelist.
    from_name = 'User' # str | The name of the person who owns the email account. (optional)
    spam_score = 2.5 # float | The account's Apache SpamAssassin™ threshold score. For more information about Apache SpamAssassin threshold scores, read our [Spam Filters](https://go.cpanel.net/cpaneldocsSpamFilters) documentation.  **Note:**  This parameter defaults to the account's current configuration. (optional)

    try:
        # Update email account's BoxTrapper configuration
        api_response = api_instance.save_configuration(email, enable_auto_whitelist, from_addresses, queue_days, whitelist_by_association, from_name=from_name, spam_score=spam_score)
        print("The response of SpamPreventionBoxTrapperApi->save_configuration:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SpamPreventionBoxTrapperApi->save_configuration: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**| The account&#39;s email address.  **Warning:**  If you call this function in Webmail, the system ignores this parameter and defaults to the currently-authenticated email address. | 
 **enable_auto_whitelist** | **int**| Whether to enable automatic whitelisting for the account.  * &#x60;1&#x60; - Enable. * &#x60;0&#x60; - Disable. | 
 **from_addresses** | **str**| A comma-separated list of email addresses that the system uses when it sends messages back to the original message senders. | 
 **queue_days** | **int**| The number of days to retain log files and queued messages. | 
 **whitelist_by_association** | **int**| Whether to whitelist the email addresses in a message&#39;s *To* and *From* sections, including carbon-copied (CC) recipients.  * &#x60;1&#x60; - Whitelist. * &#x60;0&#x60; - Do **not** whitelist. | 
 **from_name** | **str**| The name of the person who owns the email account. | [optional] 
 **spam_score** | **float**| The account&#39;s Apache SpamAssassin™ threshold score. For more information about Apache SpamAssassin threshold scores, read our [Spam Filters](https://go.cpanel.net/cpaneldocsSpamFilters) documentation.  **Note:**  This parameter defaults to the account&#39;s current configuration. | [optional] 

### Return type

[**InlineResponse20034**](InlineResponse20034.md)

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

# **save_email_template**
> InlineResponse20035 save_email_template(contents, email, template)

Save BoxTrapper message template contents

This function saves the contents of a BoxTrapper message template.

**Important:**

When you disable the [_Receive Mail_ role](https://go.cpanel.net/howtouseserverprofiles#roles),
the system **disables** this function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response20035 import InlineResponse20035
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
    api_instance = clientapi_cpanel.SpamPreventionBoxTrapperApi(api_client)
    contents = 'To: %email% Subject: Re: %subject%  The user %acct% does not accept mail from your address.  The headers of the message sent from your address are shown below:  %headers%' # str | The template file's contents.  You can use [variables](https://go.cpanel.net/cpaneldocsBoxTrapper) in the template to include details about the original message.  **Important:**  * You **must** include `To: %email%` in this parameter's value. * If you use the `verify` template, you **must** include `Subject: verify#%msgid%` in this parameter's value. * This value cannot exceed four kilobytes (KB). * You **must** URI-encode this parameter's value when using the CLI.
    email = 'user@example.com' # str | The account's email address.  **Warning:**  If you call this function in Webmail, the system overrides this parameter.  **Note:**  This parameter defaults to the current email address.
    template = 'blacklist' # str | The message template.  * `blacklist` * `returnverify` * `verifyreleased` * `verify`  **Important:**  If you use the `verify` template, you **must** include `Subject: verify#%msgid%` in this parameter's value.  **Note:**  For more information about each template, read our [BoxTrapper documentation](https://go.cpanel.net/cpaneldocsBoxTrapper).

    try:
        # Save BoxTrapper message template contents
        api_response = api_instance.save_email_template(contents, email, template)
        print("The response of SpamPreventionBoxTrapperApi->save_email_template:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SpamPreventionBoxTrapperApi->save_email_template: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contents** | **str**| The template file&#39;s contents.  You can use [variables](https://go.cpanel.net/cpaneldocsBoxTrapper) in the template to include details about the original message.  **Important:**  * You **must** include &#x60;To: %email%&#x60; in this parameter&#39;s value. * If you use the &#x60;verify&#x60; template, you **must** include &#x60;Subject: verify#%msgid%&#x60; in this parameter&#39;s value. * This value cannot exceed four kilobytes (KB). * You **must** URI-encode this parameter&#39;s value when using the CLI. | 
 **email** | **str**| The account&#39;s email address.  **Warning:**  If you call this function in Webmail, the system overrides this parameter.  **Note:**  This parameter defaults to the current email address. | 
 **template** | **str**| The message template.  * &#x60;blacklist&#x60; * &#x60;returnverify&#x60; * &#x60;verifyreleased&#x60; * &#x60;verify&#x60;  **Important:**  If you use the &#x60;verify&#x60; template, you **must** include &#x60;Subject: verify#%msgid%&#x60; in this parameter&#39;s value.  **Note:**  For more information about each template, read our [BoxTrapper documentation](https://go.cpanel.net/cpaneldocsBoxTrapper). | 

### Return type

[**InlineResponse20035**](InlineResponse20035.md)

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

# **set_forwarders**
> InlineResponse20038 set_forwarders(email, forwarder)

Add email address to BoxTrapper forwarders

This function adds a list of email addresses to which BoxTrapper forwards email messages.

**Important:**

  When you disable the [Receive Mail](https://go.cpanel.net/serverroles) role, the system **disables** this function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response20038 import InlineResponse20038
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
    api_instance = clientapi_cpanel.SpamPreventionBoxTrapperApi(api_client)
    email = 'user@example.com' # str | The account's email address.  **Warning:**  If you call this function in Webmail, the system ignores this parameter and uses the currently-authenticated email address.
    forwarder = [["user1@example.com"]] # List[object] | The email addresses to which to forward email messages.

    try:
        # Add email address to BoxTrapper forwarders
        api_response = api_instance.set_forwarders(email, forwarder)
        print("The response of SpamPreventionBoxTrapperApi->set_forwarders:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SpamPreventionBoxTrapperApi->set_forwarders: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**| The account&#39;s email address.  **Warning:**  If you call this function in Webmail, the system ignores this parameter and uses the currently-authenticated email address. | 
 **forwarder** | [**List[object]**](object.md)| The email addresses to which to forward email messages. | 

### Return type

[**InlineResponse20038**](InlineResponse20038.md)

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

# **set_status**
> InlineResponse20040 set_status(email, enabled)

Enable or disable BoxTrapper for email account

This function enables or disables BoxTrapper for an email account.

**Important:**

  When you disable the [Receive Mail](https://go.cpanel.net/serverroles) role, the system **disables** this function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response20040 import InlineResponse20040
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
    api_instance = clientapi_cpanel.SpamPreventionBoxTrapperApi(api_client)
    email = clientapi_cpanel.Email1() # Email1 | The account's name. This can be an email address or the cPanel user’s username.  **Warning:**  If you call this function in Webmail, the system ignores this parameter and defaults to the currently-authenticated email address.
    enabled = 1 # int | Whether to enable or disable BoxTrapper for the email account.  * `1` - Enable BoxTrapper. * `0` - **Disable** BoxTrapper.

    try:
        # Enable or disable BoxTrapper for email account
        api_response = api_instance.set_status(email, enabled)
        print("The response of SpamPreventionBoxTrapperApi->set_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SpamPreventionBoxTrapperApi->set_status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | [**Email1**](.md)| The account&#39;s name. This can be an email address or the cPanel user’s username.  **Warning:**  If you call this function in Webmail, the system ignores this parameter and defaults to the currently-authenticated email address. | 
 **enabled** | **int**| Whether to enable or disable BoxTrapper for the email account.  * &#x60;1&#x60; - Enable BoxTrapper. * &#x60;0&#x60; - **Disable** BoxTrapper. | 

### Return type

[**InlineResponse20040**](InlineResponse20040.md)

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

# **whitelist_messages**
> InlineResponse20041 whitelist_messages(queuefile, email=email)

Add email address to BoxTrapper allowed senders

This function whitelists email messages.

**Important:**

When you disable the [Receive Mail](https://go.cpanel.net/serverroles) role, the system **disables** this function.

**Note:**

To retrieve email messages in the BoxTrapper queue from senders that you did not previously whitelist, use the UAPI `BoxTrapper::deliver_messages` function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response20041 import InlineResponse20041
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
    api_instance = clientapi_cpanel.SpamPreventionBoxTrapperApi(api_client)
    queuefile = 'queuefile=ex1.msg&queuefile=ex2.msg&queuefile=ex3.msg' # str | The filename of the email message to whitelist.  **Note:**  To get a list of filenames in an account's BoxTrapper queue, use the UAPI `BoxTrapper::list_queued_messages` function.  **Note:**  To whitelist multiple email messages, duplicate this parameter.
    email = 'user@example.com' # str | The cPanel account email address for which to whitelist messages.  **Warning**  If you call this function in Webmail, the system ignores this parameter and defaults to the currently-authenticated email address. (optional)

    try:
        # Add email address to BoxTrapper allowed senders
        api_response = api_instance.whitelist_messages(queuefile, email=email)
        print("The response of SpamPreventionBoxTrapperApi->whitelist_messages:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SpamPreventionBoxTrapperApi->whitelist_messages: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **queuefile** | **str**| The filename of the email message to whitelist.  **Note:**  To get a list of filenames in an account&#39;s BoxTrapper queue, use the UAPI &#x60;BoxTrapper::list_queued_messages&#x60; function.  **Note:**  To whitelist multiple email messages, duplicate this parameter. | 
 **email** | **str**| The cPanel account email address for which to whitelist messages.  **Warning**  If you call this function in Webmail, the system ignores this parameter and defaults to the currently-authenticated email address. | [optional] 

### Return type

[**InlineResponse20041**](InlineResponse20041.md)

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

