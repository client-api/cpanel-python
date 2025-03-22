# clientapi_cpanel.EmailSuspensionsApi

All URIs are relative to *https://cpanel-server.tld:2083/execute*

Method | HTTP request | Description
------------- | ------------- | -------------
[**suspend_incoming**](EmailSuspensionsApi.md#suspend_incoming) | **GET** /Email/suspend_incoming | Suspend email account incoming (SMTP) mail
[**suspend_login**](EmailSuspensionsApi.md#suspend_login) | **GET** /Email/suspend_login | Suspend email account login
[**suspend_outgoing**](EmailSuspensionsApi.md#suspend_outgoing) | **GET** /Email/suspend_outgoing | Suspend email account outgoing mail
[**unsuspend_incoming**](EmailSuspensionsApi.md#unsuspend_incoming) | **GET** /Email/unsuspend_incoming | Unsuspend email account incoming mail
[**unsuspend_login**](EmailSuspensionsApi.md#unsuspend_login) | **GET** /Email/unsuspend_login | Unsuspend email account login
[**unsuspend_outgoing**](EmailSuspensionsApi.md#unsuspend_outgoing) | **GET** /Email/unsuspend_outgoing | Unsuspend email account outgoing mail


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
    api_instance = clientapi_cpanel.EmailSuspensionsApi(api_client)
    email = 'user@example.com' # str | The email user's account name. (optional)

    try:
        # Suspend email account incoming (SMTP) mail
        api_response = api_instance.suspend_incoming(email=email)
        print("The response of EmailSuspensionsApi->suspend_incoming:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailSuspensionsApi->suspend_incoming: %s\n" % e)
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
    api_instance = clientapi_cpanel.EmailSuspensionsApi(api_client)
    email = 'user@example.com' # str | The email user's account name.

    try:
        # Suspend email account login
        api_response = api_instance.suspend_login(email)
        print("The response of EmailSuspensionsApi->suspend_login:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailSuspensionsApi->suspend_login: %s\n" % e)
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
    api_instance = clientapi_cpanel.EmailSuspensionsApi(api_client)
    email = 'username@example.com' # str | The email account's username.

    try:
        # Suspend email account outgoing mail
        api_response = api_instance.suspend_outgoing(email)
        print("The response of EmailSuspensionsApi->suspend_outgoing:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailSuspensionsApi->suspend_outgoing: %s\n" % e)
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
    api_instance = clientapi_cpanel.EmailSuspensionsApi(api_client)
    email = 'user@example.com' # str | The email user's account name. (optional)

    try:
        # Unsuspend email account incoming mail
        api_response = api_instance.unsuspend_incoming(email=email)
        print("The response of EmailSuspensionsApi->unsuspend_incoming:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailSuspensionsApi->unsuspend_incoming: %s\n" % e)
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
    api_instance = clientapi_cpanel.EmailSuspensionsApi(api_client)
    email = 'username@example.com' # str | The email user's account name. (optional)

    try:
        # Unsuspend email account login
        api_response = api_instance.unsuspend_login(email=email)
        print("The response of EmailSuspensionsApi->unsuspend_login:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailSuspensionsApi->unsuspend_login: %s\n" % e)
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
    api_instance = clientapi_cpanel.EmailSuspensionsApi(api_client)
    email = 'username@example.com' # str | The email account's username.

    try:
        # Unsuspend email account outgoing mail
        api_response = api_instance.unsuspend_outgoing(email)
        print("The response of EmailSuspensionsApi->unsuspend_outgoing:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailSuspensionsApi->unsuspend_outgoing: %s\n" % e)
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

