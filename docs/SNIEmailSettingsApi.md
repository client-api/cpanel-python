# clientapi_cpanel.SNIEmailSettingsApi

All URIs are relative to *https://cpanel-server.tld:2083/execute*

Method | HTTP request | Description
------------- | ------------- | -------------
[**disable_mail_sni**](SNIEmailSettingsApi.md#disable_mail_sni) | **GET** /SSL/disable_mail_sni | Disable SNI mail services for domain
[**enable_mail_sni**](SNIEmailSettingsApi.md#enable_mail_sni) | **GET** /SSL/enable_mail_sni | Enable SNI mail services for domain
[**is_mail_sni_supported**](SNIEmailSettingsApi.md#is_mail_sni_supported) | **GET** /SSL/is_mail_sni_supported | Return whether mail SNI is enabled
[**is_sni_supported**](SNIEmailSettingsApi.md#is_sni_supported) | **GET** /SSL/is_sni_supported | Return whether Apache web server supports mail SNI
[**mail_sni_status**](SNIEmailSettingsApi.md#mail_sni_status) | **GET** /SSL/mail_sni_status | Return status of domain&#39;s SNI mail services
[**rebuild_mail_sni_config**](SNIEmailSettingsApi.md#rebuild_mail_sni_config) | **GET** /SSL/rebuild_mail_sni_config | Start SNI configuration files rebuild


# **disable_mail_sni**
> InlineResponse200409 disable_mail_sni(domains)

Disable SNI mail services for domain

This function disables SNI mail services on the specified domains.

**Note:**

  Mail SNI is **always** enabled.

  * After you change the SNI status, you **must** run UAPI's `rebuild_mail_sni_config` function.
  * Functions that enable Mail SNI succeed with a warning that Mail SNI is always enabled.
  * Functions that disable Mail SNI fail and make no changes.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200409 import InlineResponse200409
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
    api_instance = clientapi_cpanel.SNIEmailSettingsApi(api_client)
    domains = 'example.com|example1.com|example2.com' # str | A pipe-delimited list of the account's domains.

    try:
        # Disable SNI mail services for domain
        api_response = api_instance.disable_mail_sni(domains)
        print("The response of SNIEmailSettingsApi->disable_mail_sni:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SNIEmailSettingsApi->disable_mail_sni: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domains** | **str**| A pipe-delimited list of the account&#39;s domains. | 

### Return type

[**InlineResponse200409**](InlineResponse200409.md)

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

# **enable_mail_sni**
> InlineResponse200410 enable_mail_sni(domains)

Enable SNI mail services for domain

This function enables SNI mail services on the specified domains.

**Warning:**

Mail SNI is **always** enabled.
* Mail SNI is **not** compatible with Webmail and will **not** function for any Webmail connection. Webmail connections use the cPanel service SSL certificate.
* Functions that enable Mail SNI succeed with a warning that Mail SNI is always enabled.
* Functions that disable Mail SNI fail and make no changes.

**Important:**

  When you disable the *Calendars and Contacts*, *Mail Receive*, *Web Disk*, *Webmail*, **and** *Web Server* [roles](https://go.cpanel.net/howtouseserverprofiles#roles), the system **disables** this function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200410 import InlineResponse200410
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
    api_instance = clientapi_cpanel.SNIEmailSettingsApi(api_client)
    domains = 'example.com|example1.com|example2.com' # str | A pipe-delimited list of the account's domains.

    try:
        # Enable SNI mail services for domain
        api_response = api_instance.enable_mail_sni(domains)
        print("The response of SNIEmailSettingsApi->enable_mail_sni:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SNIEmailSettingsApi->enable_mail_sni: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domains** | **str**| A pipe-delimited list of the account&#39;s domains. | 

### Return type

[**InlineResponse200410**](InlineResponse200410.md)

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

# **is_mail_sni_supported**
> InlineResponse200428 is_mail_sni_supported()

Return whether mail SNI is enabled

This function checks whether the sslinstall feature is enabled.

**Warning:**

Mail SNI is always enabled.
* Mail SNI is **not** compatible with Webmail and will **not** function for any Webmail connection. Webmail connections use the cPanel service SSL certificate.
* Functions that enable Mail SNI succeed with a warning that Mail SNI is always enabled.
* Functions that disable Mail SNI will fail and make no changes.

**Important:**

When you disable the [Calendars and Contacts, Receive Mail, Web Disk, Webmail, and Web Server roles](https://go.cpanel.net/serverroles), the system **disables** this function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200428 import InlineResponse200428
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
    api_instance = clientapi_cpanel.SNIEmailSettingsApi(api_client)

    try:
        # Return whether mail SNI is enabled
        api_response = api_instance.is_mail_sni_supported()
        print("The response of SNIEmailSettingsApi->is_mail_sni_supported:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SNIEmailSettingsApi->is_mail_sni_supported: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**InlineResponse200428**](InlineResponse200428.md)

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

# **is_sni_supported**
> InlineResponse200429 is_sni_supported()

Return whether Apache web server supports mail SNI

This function checks whether the Apache web server supports SNI.

**Important:**

When you disable the [Calendars and Contacts, Receive Mail, Web Disk, Webmail, and Web Server roles](https://go.cpanel.net/serverroles), the system **disables** this function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200429 import InlineResponse200429
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
    api_instance = clientapi_cpanel.SNIEmailSettingsApi(api_client)

    try:
        # Return whether Apache web server supports mail SNI
        api_response = api_instance.is_sni_supported()
        print("The response of SNIEmailSettingsApi->is_sni_supported:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SNIEmailSettingsApi->is_sni_supported: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**InlineResponse200429**](InlineResponse200429.md)

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

# **mail_sni_status**
> InlineResponse200434 mail_sni_status(domain)

Return status of domain's SNI mail services

This function retrieves the status of the domain's SNI mail services.

**Warning:**

Mail SNI is **not** compatible with Webmail and will not function for any Webmail connection. Webmail connections use the cPanel service SSL certificate.

**Note:**

Mail SNI is always enabled.
* Functions that enable Mail SNI succeed with a warning that Mail SNI is always enabled.
* Functions that disable Mail SNI fail and make no changes.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200434 import InlineResponse200434
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
    api_instance = clientapi_cpanel.SNIEmailSettingsApi(api_client)
    domain = 'example.com' # str | The account's domain.

    try:
        # Return status of domain's SNI mail services
        api_response = api_instance.mail_sni_status(domain)
        print("The response of SNIEmailSettingsApi->mail_sni_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SNIEmailSettingsApi->mail_sni_status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**| The account&#39;s domain. | 

### Return type

[**InlineResponse200434**](InlineResponse200434.md)

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

# **rebuild_mail_sni_config**
> InlineResponse200435 rebuild_mail_sni_config(reload_dovecot=reload_dovecot)

Start SNI configuration files rebuild

This function rebuilds the SNI configuration files.

**Note:**

* You **must** run this function after you change the SNI status through the UAPI's `enable_mail_sni` or `disable_mail_sni` functions.
* Mail SNI is **always** enabled.
  * Functions that enable Mail SNI succeed with a warning that Mail SNI is always enabled. Functions that disable Mail SNI fail and make no changes.
  * Functions that disable Mail SNI will fail and make no changes.

**Important:**

 When you disable the _Calendars and Contacts_, _Receive Mail_, _Web Disk_, _Webmail_, **and**  _Web Server_ [roles](https://go.cpanel.net/serverroles), the system **disables** this function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200435 import InlineResponse200435
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
    api_instance = clientapi_cpanel.SNIEmailSettingsApi(api_client)
    reload_dovecot = 1 # int | Whether to reload the Dovecot service after the system rebuilds the configuration files. * `1` - Reload Dovecot. * `0` - Do **not** reload Dovecot. (optional) (default to 1)

    try:
        # Start SNI configuration files rebuild
        api_response = api_instance.rebuild_mail_sni_config(reload_dovecot=reload_dovecot)
        print("The response of SNIEmailSettingsApi->rebuild_mail_sni_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SNIEmailSettingsApi->rebuild_mail_sni_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **reload_dovecot** | **int**| Whether to reload the Dovecot service after the system rebuilds the configuration files. * &#x60;1&#x60; - Reload Dovecot. * &#x60;0&#x60; - Do **not** reload Dovecot. | [optional] [default to 1]

### Return type

[**InlineResponse200435**](InlineResponse200435.md)

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

