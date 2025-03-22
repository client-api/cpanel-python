# clientapi_cpanel.WebmailSessionsApi

All URIs are relative to *https://cpanel-server.tld:2083/execute*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_temp_user**](WebmailSessionsApi.md#create_temp_user) | **GET** /Session/create_temp_user | Create user session with existing session
[**create_webmail_session_for_mail_user**](WebmailSessionsApi.md#create_webmail_session_for_mail_user) | **GET** /Session/create_webmail_session_for_mail_user | Create Webmail session
[**create_webmail_session_for_mail_user_check_password**](WebmailSessionsApi.md#create_webmail_session_for_mail_user_check_password) | **GET** /Session/create_webmail_session_for_mail_user_check_password | Create Webmail session with credentials
[**create_webmail_session_for_self**](WebmailSessionsApi.md#create_webmail_session_for_self) | **GET** /Session/create_webmail_session_for_self | Create Webmail session for current user


# **create_temp_user**
> InlineResponse200455 create_temp_user()

Create user session with existing session

This function creates a temporary user session.

**Important:**

* Because this function requires a valid cPanel session ID, you **must** call it via a cPanel or Webmail session URL. If you call this function via the command line or Template Toolkit, it will **not** create a temporary user session. You **must** use the WHM API 1 `create_user_session` function to create a temporary user session.
* Third-party plugins that require access to temporary MySQL users **must** call this function via the URL. It will create the temporary users before they are available. You can find these users in the `$ENV{'REMOTE_DBOWNER'}` environment variable.
* If you **cannot** update your system, update your scripts to call the `Cgi::phpmyadminlink` function. This will create a temporary user session for you.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200455 import InlineResponse200455
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
    api_instance = clientapi_cpanel.WebmailSessionsApi(api_client)

    try:
        # Create user session with existing session
        api_response = api_instance.create_temp_user()
        print("The response of WebmailSessionsApi->create_temp_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebmailSessionsApi->create_temp_user: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**InlineResponse200455**](InlineResponse200455.md)

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

# **create_webmail_session_for_mail_user**
> InlineResponse200456 create_webmail_session_for_mail_user(domain, login, locale=locale, remote_address=remote_address)

Create Webmail session

Create a temporary session for a cPanel user to connect to Webmail.

**Note:**

The cPanel user must own the Webmail account.

### How to use this API

After you successfully call this API, you will need to log in to [Webmail](https://go.cpanel.net/webmailinterface).
To do this, send an HTTP POST to `https://$URL_AUTHTY:2096$token/login` with a message body of `session=$session` where:

* `$URL_AUTHTY` represents the value from the `hostname` return.
  * If the `hostname` return value is `null`, enter the hostname of the server that answered the API function.
  * `$token` represents the value from the token return.
* `$session` represents the value of the session return.

For example, an HTTP POST may resemble the following:

```https://hostname.example.com:2096/cpsess2462418786/login```

With a message body of:

```session=username:D7NiAZv1nf4bXeg9:CREATE_WEBMAIL_SESSION_FOR_MAIL_USER,728fb86a7df1cf20690c65f349ac3137```

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200456 import InlineResponse200456
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
    api_instance = clientapi_cpanel.WebmailSessionsApi(api_client)
    domain = 'example.com' # str | The domain for the Webmail account.
    login = 'username' # str | The Webmail account's username.
    locale = 'en' # str | The [locale](https://go.cpanel.net/localedocs) that the new session will use.  **Note:**  * You must **only** enter lowercase characters. * This parameter defaults to the cPanel user's locale. (optional)
    remote_address = '192.168.0.1' # str | The session's client IP address.  **Note:**  * If you run this function from the command line, this parameter is **required**. * This parameter defaults to the API caller's IP address. (optional)

    try:
        # Create Webmail session
        api_response = api_instance.create_webmail_session_for_mail_user(domain, login, locale=locale, remote_address=remote_address)
        print("The response of WebmailSessionsApi->create_webmail_session_for_mail_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebmailSessionsApi->create_webmail_session_for_mail_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**| The domain for the Webmail account. | 
 **login** | **str**| The Webmail account&#39;s username. | 
 **locale** | **str**| The [locale](https://go.cpanel.net/localedocs) that the new session will use.  **Note:**  * You must **only** enter lowercase characters. * This parameter defaults to the cPanel user&#39;s locale. | [optional] 
 **remote_address** | **str**| The session&#39;s client IP address.  **Note:**  * If you run this function from the command line, this parameter is **required**. * This parameter defaults to the API caller&#39;s IP address. | [optional] 

### Return type

[**InlineResponse200456**](InlineResponse200456.md)

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

# **create_webmail_session_for_mail_user_check_password**
> InlineResponse200457 create_webmail_session_for_mail_user_check_password(domain, login, password, locale=locale, remote_address=remote_address)

Create Webmail session with credentials

This function creates a temporary session with a password for the calling cPanel user to connect to Webmail.

**Note:**

* The cPanel user must own the Webmail account.
* This function works like the UAPI Session::create_webmail_session_for_mail_user function with one exception. This function requires a correct password to create the Webmail session. If you use an incorrect password or attempt to connect to a suspended account, the login will fail.

### How to use this API

After you successfully call this API, you will need to log in to [Webmail](https://go.cpanel.net/webmailinterface).
To do this, send an HTTP POST to `https://$URL_AUTHTY:2096$token/login` with a message body of `session=$session` where:

* `$URL_AUTHTY` represents the value from the `hostname` return.
  * If the `hostname` return value is `null`, enter the hostname of the server that answered the API function.
  * `$token` represents the value from the token return.
* `$session` represents the value of the session return.

For example, an HTTP POST may resemble the following:

```https://hostname.example.com:2096/cpsess2462418786/login```

With a message body of:

```session=username:D7NiAZv1nf4bXeg9:CREATE_WEBMAIL_SESSION_FOR_MAIL_USER,728fb86a7df1cf20690c65f349ac3137```

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200457 import InlineResponse200457
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
    api_instance = clientapi_cpanel.WebmailSessionsApi(api_client)
    domain = 'example.com' # str | The domain for the Webmail account.
    login = 'username' # str | The Webmail account's username.
    password = 'luggage12345' # str | The password for the Webmail account.
    locale = 'en' # str | The [locale](https://go.cpanel.net/localedocs) that the new session will use.  **Note:**  * You must **only** enter lowercase characters. * This parameter defaults to the cPanel user's locale. (optional)
    remote_address = '192.168.0.1' # str | The session's account's client IP address.  **Note:**  * If you run this function from the command line, this parameter is **required**. * This parameter defaults to the API caller's IP address. (optional)

    try:
        # Create Webmail session with credentials
        api_response = api_instance.create_webmail_session_for_mail_user_check_password(domain, login, password, locale=locale, remote_address=remote_address)
        print("The response of WebmailSessionsApi->create_webmail_session_for_mail_user_check_password:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebmailSessionsApi->create_webmail_session_for_mail_user_check_password: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**| The domain for the Webmail account. | 
 **login** | **str**| The Webmail account&#39;s username. | 
 **password** | **str**| The password for the Webmail account. | 
 **locale** | **str**| The [locale](https://go.cpanel.net/localedocs) that the new session will use.  **Note:**  * You must **only** enter lowercase characters. * This parameter defaults to the cPanel user&#39;s locale. | [optional] 
 **remote_address** | **str**| The session&#39;s account&#39;s client IP address.  **Note:**  * If you run this function from the command line, this parameter is **required**. * This parameter defaults to the API caller&#39;s IP address. | [optional] 

### Return type

[**InlineResponse200457**](InlineResponse200457.md)

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

# **create_webmail_session_for_self**
> InlineResponse200458 create_webmail_session_for_self(locale=locale, remote_address=remote_address)

Create Webmail session for current user

Create a temporary session to connect to Webmail for the authenticated cPanel user.

### How to use this API

After you successfully call this API, you will need to log in to [Webmail](https://go.cpanel.net/webmailinterface).
To do this, send an HTTP POST to `https://$URL_AUTHTY:2096$token/login` with a message body of `session=$session` where:

* `$URL_AUTHTY` represents the value from the `hostname` return.
  * If the `hostname` return value is `null`, enter the hostname of the server that answered the API function.
  * `$token` represents the value from the token return.
* `$session` represents the value of the session return.

For example, an HTTP POST may resemble the following:

```https://hostname.example.com:2096/cpsess2462418786/login```

With a message body of:

```session=username:D7NiAZv1nf4bXeg9:CREATE_WEBMAIL_SESSION_FOR_MAIL_USER,728fb86a7df1cf20690c65f349ac3137```

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200458 import InlineResponse200458
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
    api_instance = clientapi_cpanel.WebmailSessionsApi(api_client)
    locale = 'en' # str | The [locale](https://go.cpanel.net/localedocs) that the new session will use.  Use UAPI `Locale::list_locales` to see a list of valid locales.  **Note:**  * You must **only** enter lowercase characters. * This parameter defaults to the cPanel user's locale. (optional)
    remote_address = '192.168.0.1' # str | The session's client IP address.  **Note:**  * If you run this function from the command line, this parameter is **required**. * This parameter defaults to the API caller's IP address. (optional)

    try:
        # Create Webmail session for current user
        api_response = api_instance.create_webmail_session_for_self(locale=locale, remote_address=remote_address)
        print("The response of WebmailSessionsApi->create_webmail_session_for_self:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebmailSessionsApi->create_webmail_session_for_self: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **locale** | **str**| The [locale](https://go.cpanel.net/localedocs) that the new session will use.  Use UAPI &#x60;Locale::list_locales&#x60; to see a list of valid locales.  **Note:**  * You must **only** enter lowercase characters. * This parameter defaults to the cPanel user&#39;s locale. | [optional] 
 **remote_address** | **str**| The session&#39;s client IP address.  **Note:**  * If you run this function from the command line, this parameter is **required**. * This parameter defaults to the API caller&#39;s IP address. | [optional] 

### Return type

[**InlineResponse200458**](InlineResponse200458.md)

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

