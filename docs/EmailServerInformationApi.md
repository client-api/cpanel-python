# clientapi_cpanel.EmailServerInformationApi

All URIs are relative to *https://cpanel-server.tld:2083/execute*

Method | HTTP request | Description
------------- | ------------- | -------------
[**check_fastmail**](EmailServerInformationApi.md#check_fastmail) | **GET** /Email/check_fastmail | Return BlackBerry FastMail support status
[**disable_mailbox_autocreate**](EmailServerInformationApi.md#disable_mailbox_autocreate) | **GET** /Email/disable_mailbox_autocreate | Disable cPanel account mailbox autocreation
[**enable_mailbox_autocreate**](EmailServerInformationApi.md#enable_mailbox_autocreate) | **GET** /Email/enable_mailbox_autocreate | Enable cPanel account mailbox autocreation
[**fetch_charmaps**](EmailServerInformationApi.md#fetch_charmaps) | **GET** /Email/fetch_charmaps | Return server&#39;s supported character encodings
[**fts_rescan_mailbox**](EmailServerInformationApi.md#fts_rescan_mailbox) | **GET** /Email/fts_rescan_mailbox | Start IMAP Full-Text Search scan for email account
[**get_charsets**](EmailServerInformationApi.md#get_charsets) | **GET** /Email/get_charsets | Return mail server&#39;s supported character encodings
[**get_mailbox_autocreate**](EmailServerInformationApi.md#get_mailbox_autocreate) | **GET** /Email/get_mailbox_autocreate | Return cPanel account&#39;s mailbox autocreate status
[**has_plaintext_authentication**](EmailServerInformationApi.md#has_plaintext_authentication) | **GET** /Email/has_plaintext_authentication | Return whether plaintext authentication is enabled
[**set_always_accept**](EmailServerInformationApi.md#set_always_accept) | **GET** /Email/set_always_accept | Update Mail Exchanger type
[**stats_db_status**](EmailServerInformationApi.md#stats_db_status) | **GET** /Email/stats_db_status | Return eximstats SQLite database status


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
    api_instance = clientapi_cpanel.EmailServerInformationApi(api_client)

    try:
        # Return BlackBerry FastMail support status
        api_response = api_instance.check_fastmail()
        print("The response of EmailServerInformationApi->check_fastmail:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailServerInformationApi->check_fastmail: %s\n" % e)
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
    api_instance = clientapi_cpanel.EmailServerInformationApi(api_client)
    email = 'username@example.com' # str | The email account address for which to disable mailbox autocreation.

    try:
        # Disable cPanel account mailbox autocreation
        api_response = api_instance.disable_mailbox_autocreate(email)
        print("The response of EmailServerInformationApi->disable_mailbox_autocreate:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailServerInformationApi->disable_mailbox_autocreate: %s\n" % e)
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
    api_instance = clientapi_cpanel.EmailServerInformationApi(api_client)
    email = 'username@example.com' # str | The email account for which to enable mailbox autocreation.

    try:
        # Enable cPanel account mailbox autocreation
        api_response = api_instance.enable_mailbox_autocreate(email)
        print("The response of EmailServerInformationApi->enable_mailbox_autocreate:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailServerInformationApi->enable_mailbox_autocreate: %s\n" % e)
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
    api_instance = clientapi_cpanel.EmailServerInformationApi(api_client)

    try:
        # Return server's supported character encodings
        api_response = api_instance.fetch_charmaps()
        print("The response of EmailServerInformationApi->fetch_charmaps:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailServerInformationApi->fetch_charmaps: %s\n" % e)
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
    api_instance = clientapi_cpanel.EmailServerInformationApi(api_client)
    account = 'username@example.com' # str | The email user's account name.  **Note:**  If you do not enter an email address, the function rescans the default email account.

    try:
        # Start IMAP Full-Text Search scan for email account
        api_response = api_instance.fts_rescan_mailbox(account)
        print("The response of EmailServerInformationApi->fts_rescan_mailbox:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailServerInformationApi->fts_rescan_mailbox: %s\n" % e)
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
    api_instance = clientapi_cpanel.EmailServerInformationApi(api_client)

    try:
        # Return mail server's supported character encodings
        api_response = api_instance.get_charsets()
        print("The response of EmailServerInformationApi->get_charsets:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailServerInformationApi->get_charsets: %s\n" % e)
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
    api_instance = clientapi_cpanel.EmailServerInformationApi(api_client)
    email = 'username@example.com' # str | The email account address to query.

    try:
        # Return cPanel account's mailbox autocreate status
        api_response = api_instance.get_mailbox_autocreate(email)
        print("The response of EmailServerInformationApi->get_mailbox_autocreate:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailServerInformationApi->get_mailbox_autocreate: %s\n" % e)
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
    api_instance = clientapi_cpanel.EmailServerInformationApi(api_client)

    try:
        # Return whether plaintext authentication is enabled
        api_response = api_instance.has_plaintext_authentication()
        print("The response of EmailServerInformationApi->has_plaintext_authentication:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailServerInformationApi->has_plaintext_authentication: %s\n" % e)
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
    api_instance = clientapi_cpanel.EmailServerInformationApi(api_client)
    domain = 'example.com' # str | The mail exchanger's domain.
    alwaysaccept = auto # str | The mail exchanger type. * `auto` — Allow cPanel to determine the appropriate role. * `local` — Always accept the domain's mail. * `secondary` — Accept mail until a higher priority mail server is available. * `remote` — Do **not** accept mail.  **Note:**  This parameter is redundant with the `mxcheck` parameter. Do **not** enter the `mxcheck` and `alwaysaccept` parameters at the same time. [Undefined behavior](https://en.wikipedia.org/wiki/Undefined_behavior) may occur if this happens. (optional) (default to auto)
    mxcheck = auto # str | The mail exchanger type. * `auto` — Allow cPanel to determine the appropriate role. * `local` — Always accept the domain's mail. * `secondary` — Accept mail until a higher priority mail server is available. * `remote` — Do **not** accept mail.  **Note:**  This parameter is redundant with the `alwaysaccept` parameter. Do **not** enter the `mxcheck` and `alwaysaccept` parameters at the same time. [Undefined behavior](https://en.wikipedia.org/wiki/Undefined_behavior) may occur if this happens. (optional) (default to auto)

    try:
        # Update Mail Exchanger type
        api_response = api_instance.set_always_accept(domain, alwaysaccept=alwaysaccept, mxcheck=mxcheck)
        print("The response of EmailServerInformationApi->set_always_accept:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailServerInformationApi->set_always_accept: %s\n" % e)
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
    api_instance = clientapi_cpanel.EmailServerInformationApi(api_client)

    try:
        # Return eximstats SQLite database status
        api_response = api_instance.stats_db_status()
        print("The response of EmailServerInformationApi->stats_db_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailServerInformationApi->stats_db_status: %s\n" % e)
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

