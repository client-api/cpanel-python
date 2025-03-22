# clientapi_cpanel.SpamManagementApi

All URIs are relative to *https://cpanel-server.tld:2083/execute*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_spam_filter**](SpamManagementApi.md#add_spam_filter) | **GET** /Email/add_spam_filter | Update minimum spam score threshold value
[**clear_spam_box**](SpamManagementApi.md#clear_spam_box) | **GET** /SpamAssassin/clear_spam_box | Delete spam box contents
[**disable_spam_assassin**](SpamManagementApi.md#disable_spam_assassin) | **GET** /Email/disable_spam_assassin | Disable Apache SpamAssassin for cPanel account
[**disable_spam_autodelete**](SpamManagementApi.md#disable_spam_autodelete) | **GET** /Email/disable_spam_autodelete | Disable spam box filtering auto-delete
[**disable_spam_box**](SpamManagementApi.md#disable_spam_box) | **GET** /Email/disable_spam_box | Disable spam box filtering for cPanel account
[**enable_spam_assassin**](SpamManagementApi.md#enable_spam_assassin) | **GET** /Email/enable_spam_assassin | Enable Apache SpamAssassin for cPanel account
[**enable_spam_box**](SpamManagementApi.md#enable_spam_box) | **GET** /Email/enable_spam_box | Enable spam box filtering for cPanel account
[**get_spam_settings**](SpamManagementApi.md#get_spam_settings) | **GET** /Email/get_spam_settings | Return email account Apache SpamAssassin settings
[**get_symbolic_test_names**](SpamManagementApi.md#get_symbolic_test_names) | **GET** /SpamAssassin/get_symbolic_test_names | Return SpamAssassin™ symbolic test scores
[**get_user_preferences**](SpamManagementApi.md#get_user_preferences) | **GET** /SpamAssassin/get_user_preferences | Return SpamAssassin™ settings
[**update_user_preference**](SpamManagementApi.md#update_user_preference) | **GET** /SpamAssassin/update_user_preference | Update SpamAssassin™ settings


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
    api_instance = clientapi_cpanel.SpamManagementApi(api_client)
    account = 'username@example.com' # str | The email account to apply a spam score threshold value.  **Note:**    If you do **not** specify a value, the function applies the new spam score threshold value to **all** accounts. (optional)
    required_score = '5' # str | Set a spam score threshold value.  **Notes:**    * You **must** specify a value greater than `0`, and lower than the domain owner's spam score threshold value.   * You **cannot** enter `0` as a value for this parameter.   * You can retrieve the domain owner‘s spam score threshold value via the `cpuser_spam_auto_delete_score` return from the UAPI `Email::get_spam_settings` function.   * The default value, `5`, is an aggressive spam score.   * The lower the spam score, the more likely that Apache SpamAssassin will label messages as spam and delete them.   * Some systems may wish to use a more lenient spam score (for example, `8` or `10`). (optional) (default to '5')

    try:
        # Update minimum spam score threshold value
        api_response = api_instance.add_spam_filter(account=account, required_score=required_score)
        print("The response of SpamManagementApi->add_spam_filter:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SpamManagementApi->add_spam_filter: %s\n" % e)
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

# **clear_spam_box**
> InlineResponse200484 clear_spam_box()

Delete spam box contents

This function clears the spam box of all its contents for all email accounts.

**Important:**

This function deletes the Spam Box folder contents for every email address on the account, which includes the system user email account.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200484 import InlineResponse200484
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
    api_instance = clientapi_cpanel.SpamManagementApi(api_client)

    try:
        # Delete spam box contents
        api_response = api_instance.clear_spam_box()
        print("The response of SpamManagementApi->clear_spam_box:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SpamManagementApi->clear_spam_box: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**InlineResponse200484**](InlineResponse200484.md)

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
    api_instance = clientapi_cpanel.SpamManagementApi(api_client)

    try:
        # Disable Apache SpamAssassin for cPanel account
        api_response = api_instance.disable_spam_assassin()
        print("The response of SpamManagementApi->disable_spam_assassin:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SpamManagementApi->disable_spam_assassin: %s\n" % e)
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
    api_instance = clientapi_cpanel.SpamManagementApi(api_client)

    try:
        # Disable spam box filtering auto-delete
        api_response = api_instance.disable_spam_autodelete()
        print("The response of SpamManagementApi->disable_spam_autodelete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SpamManagementApi->disable_spam_autodelete: %s\n" % e)
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
    api_instance = clientapi_cpanel.SpamManagementApi(api_client)

    try:
        # Disable spam box filtering for cPanel account
        api_response = api_instance.disable_spam_box()
        print("The response of SpamManagementApi->disable_spam_box:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SpamManagementApi->disable_spam_box: %s\n" % e)
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
    api_instance = clientapi_cpanel.SpamManagementApi(api_client)

    try:
        # Enable Apache SpamAssassin for cPanel account
        api_response = api_instance.enable_spam_assassin()
        print("The response of SpamManagementApi->enable_spam_assassin:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SpamManagementApi->enable_spam_assassin: %s\n" % e)
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
    api_instance = clientapi_cpanel.SpamManagementApi(api_client)

    try:
        # Enable spam box filtering for cPanel account
        api_response = api_instance.enable_spam_box()
        print("The response of SpamManagementApi->enable_spam_box:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SpamManagementApi->enable_spam_box: %s\n" % e)
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
    api_instance = clientapi_cpanel.SpamManagementApi(api_client)
    account = 'username@example.com' # str | Retrieve a specific user account's SpamAssassin settings.  **Note:**  If you do **not** specify this parameter, the function returns the settings for [the default email account](https://go.cpanel.net/DefaultAddress). (optional)

    try:
        # Return email account Apache SpamAssassin settings
        api_response = api_instance.get_spam_settings(account=account)
        print("The response of SpamManagementApi->get_spam_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SpamManagementApi->get_spam_settings: %s\n" % e)
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

# **get_symbolic_test_names**
> InlineResponse200485 get_symbolic_test_names()

Return SpamAssassin™ symbolic test scores

This function lists the Apache SpamAssassin™ scores for each symbolic test.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200485 import InlineResponse200485
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
    api_instance = clientapi_cpanel.SpamManagementApi(api_client)

    try:
        # Return SpamAssassin™ symbolic test scores
        api_response = api_instance.get_symbolic_test_names()
        print("The response of SpamManagementApi->get_symbolic_test_names:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SpamManagementApi->get_symbolic_test_names: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**InlineResponse200485**](InlineResponse200485.md)

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

# **get_user_preferences**
> InlineResponse200486 get_user_preferences()

Return SpamAssassin™ settings

This function lists the Apache SpamAssassin™ settings for the account.

**Note:**

Additional customizations may appear in the returns. Form more information read the [Apache SpamAssassin™ configuration file](https://spamassassin.apache.org/full/3.1.x/doc/Mail_SpamAssassin_Conf.html#user_preferences) documentation.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200486 import InlineResponse200486
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
    api_instance = clientapi_cpanel.SpamManagementApi(api_client)

    try:
        # Return SpamAssassin™ settings
        api_response = api_instance.get_user_preferences()
        print("The response of SpamManagementApi->get_user_preferences:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SpamManagementApi->get_user_preferences: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**InlineResponse200486**](InlineResponse200486.md)

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

# **update_user_preference**
> InlineResponse200487 update_user_preference(preference, value=value)

Update SpamAssassin™ settings

This function sets the Apache SpamAssassin™ settings for the account.

**Note:**

Additional customizations may appear in the function's return. For more information,
read the [Apache SpamAssassin configuration file documentation](https://spamassassin.apache.org/full/3.1.x/doc/Mail_SpamAssassin_Conf.html#user_preferences).

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200487 import InlineResponse200487
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
    api_instance = clientapi_cpanel.SpamManagementApi(api_client)
    preference = 'score' # str | The variable that you want to manipulate.  * `score` * `required_score` * `whitelist_from` * `blacklist_from` * A [custom SpamAssassin variable](https://spamassassin.apache.org/full/3.1.x/doc/Mail_SpamAssassin_Conf.html#user_preferences).  **Important:**  * You can **only** choose one of these possible values per call. * If you enter a value for the `preference` parameter, but you do **not** define a value for the `value` parameter, the function will remove any previous settings.
    value = 'value-0=ACT_NOW_CAPS 5.0 value-1=INVALID_DATE 3.2' # str | The value for the preference of the variable that you want to manipulate.  * A valid SpamAssassin \"`TEST_NAME SCORE`\" value when the value of the `preference` parameter is `score`, where:      * `TEST_NAME` represents the symbolic name of the test. For list of symbolic test names, run the UAPI `SpamAssassin::get_symbolic_test_names` function.     * `SCORE` represents the floating-point value that SpamAssassin assigns to the mail when the test result is true. The score value must be greater than `0`, and less than `1000`.  * A valid floating-point number if the value of the `preference` parameter is `required_score`. * A valid email address if the value of the `preference` parameter is `whitelist_from` or `blacklist_from`. * A [custom SpamAssassin variable](https://spamassassin.apache.org/full/3.1.x/doc/Mail_SpamAssassin_Conf.html#user_preferences) value.  **Note:**  To enter multiple values, increment the parameter name. For example, use the `value-0` and `value-1` parameters. (optional)

    try:
        # Update SpamAssassin™ settings
        api_response = api_instance.update_user_preference(preference, value=value)
        print("The response of SpamManagementApi->update_user_preference:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SpamManagementApi->update_user_preference: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **preference** | **str**| The variable that you want to manipulate.  * &#x60;score&#x60; * &#x60;required_score&#x60; * &#x60;whitelist_from&#x60; * &#x60;blacklist_from&#x60; * A [custom SpamAssassin variable](https://spamassassin.apache.org/full/3.1.x/doc/Mail_SpamAssassin_Conf.html#user_preferences).  **Important:**  * You can **only** choose one of these possible values per call. * If you enter a value for the &#x60;preference&#x60; parameter, but you do **not** define a value for the &#x60;value&#x60; parameter, the function will remove any previous settings. | 
 **value** | **str**| The value for the preference of the variable that you want to manipulate.  * A valid SpamAssassin \&quot;&#x60;TEST_NAME SCORE&#x60;\&quot; value when the value of the &#x60;preference&#x60; parameter is &#x60;score&#x60;, where:      * &#x60;TEST_NAME&#x60; represents the symbolic name of the test. For list of symbolic test names, run the UAPI &#x60;SpamAssassin::get_symbolic_test_names&#x60; function.     * &#x60;SCORE&#x60; represents the floating-point value that SpamAssassin assigns to the mail when the test result is true. The score value must be greater than &#x60;0&#x60;, and less than &#x60;1000&#x60;.  * A valid floating-point number if the value of the &#x60;preference&#x60; parameter is &#x60;required_score&#x60;. * A valid email address if the value of the &#x60;preference&#x60; parameter is &#x60;whitelist_from&#x60; or &#x60;blacklist_from&#x60;. * A [custom SpamAssassin variable](https://spamassassin.apache.org/full/3.1.x/doc/Mail_SpamAssassin_Conf.html#user_preferences) value.  **Note:**  To enter multiple values, increment the parameter name. For example, use the &#x60;value-0&#x60; and &#x60;value-1&#x60; parameters. | [optional] 

### Return type

[**InlineResponse200487**](InlineResponse200487.md)

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

