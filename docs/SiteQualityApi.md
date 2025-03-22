# clientapi_cpanel.SiteQualityApi

All URIs are relative to *https://cpanel-server.tld:2083/execute*

Method | HTTP request | Description
------------- | ------------- | -------------
[**site_quality_create_project**](SiteQualityApi.md#site_quality_create_project) | **POST** /SiteQuality/create_project | Add domain to monitoring
[**site_quality_create_site_quality_user**](SiteQualityApi.md#site_quality_create_site_quality_user) | **POST** /SiteQuality/create_site_quality_user | Register cPanel user for monitoring
[**site_quality_delete_site_quality_user**](SiteQualityApi.md#site_quality_delete_site_quality_user) | **GET** /SiteQuality/delete_site_quality_user | Delete Site Quality Monitoring account
[**site_quality_get_all_scores**](SiteQualityApi.md#site_quality_get_all_scores) | **POST** /SiteQuality/get_all_scores | Return all projects&#39; monitoring results
[**site_quality_get_app_token**](SiteQualityApi.md#site_quality_get_app_token) | **GET** /SiteQuality/get_app_token | Return koality authentication token
[**site_quality_has_site_quality_user**](SiteQualityApi.md#site_quality_has_site_quality_user) | **GET** /SiteQuality/has_site_quality_user | Validate monitoring account existence
[**site_quality_is_site_quality_user_enabled**](SiteQualityApi.md#site_quality_is_site_quality_user_enabled) | **GET** /SiteQuality/is_site_quality_user_enabled | Validate monitoring account enablement
[**site_quality_reset_config**](SiteQualityApi.md#site_quality_reset_config) | **GET** /SiteQuality/reset_config | Remove monitoring user from cPanel configuration
[**site_quality_send_activation_email**](SiteQualityApi.md#site_quality_send_activation_email) | **GET** /SiteQuality/send_activation_email | Request activation email
[**site_quality_verify_code**](SiteQualityApi.md#site_quality_verify_code) | **GET** /SiteQuality/verify_code | Validate activation code


# **site_quality_create_project**
> InlineResponse200459 site_quality_create_project(name, url, standard_alerting=standard_alerting, system_type=system_type)

Add domain to monitoring

This function creates a Site Quality Monitoring project. A project bundles together one or more URLs with a shared domain for monitoring.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200459 import InlineResponse200459
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
    api_instance = clientapi_cpanel.SiteQualityApi(api_client)
    name = 'MyProject' # str | The name of the project to create.
    url = 'https://example.com' # str | The URL to monitor.
    standard_alerting = 0 # int | Whether to enable standard email alerts.   * `1` - Enable standard alerting.   * `0` - Do not enable standard alerting.   * `null` - Do not enable standard alerting. (optional)
    system_type = 'Website' # str | The monitoring template to use for the project. (optional) (default to 'Website')

    try:
        # Add domain to monitoring
        api_response = api_instance.site_quality_create_project(name, url, standard_alerting=standard_alerting, system_type=system_type)
        print("The response of SiteQualityApi->site_quality_create_project:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SiteQualityApi->site_quality_create_project: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the project to create. | 
 **url** | **str**| The URL to monitor. | 
 **standard_alerting** | **int**| Whether to enable standard email alerts.   * &#x60;1&#x60; - Enable standard alerting.   * &#x60;0&#x60; - Do not enable standard alerting.   * &#x60;null&#x60; - Do not enable standard alerting. | [optional] 
 **system_type** | **str**| The monitoring template to use for the project. | [optional] [default to &#39;Website&#39;]

### Return type

[**InlineResponse200459**](InlineResponse200459.md)

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

# **site_quality_create_site_quality_user**
> InlineResponse200460 site_quality_create_site_quality_user(email, password=password)

Register cPanel user for monitoring

This function creates a Site Quality Monitoring user account associated with a cPanel user account.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200460 import InlineResponse200460
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
    api_instance = clientapi_cpanel.SiteQualityApi(api_client)
    email = 'username@example.com' # str | The cPanel account's email address.
    password = 'An3xample!?' # str | The account's password.  **Note:**  If no password is given, one is auto-generated.  The system does not save this value. (optional)

    try:
        # Register cPanel user for monitoring
        api_response = api_instance.site_quality_create_site_quality_user(email, password=password)
        print("The response of SiteQualityApi->site_quality_create_site_quality_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SiteQualityApi->site_quality_create_site_quality_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**| The cPanel account&#39;s email address. | 
 **password** | **str**| The account&#39;s password.  **Note:**  If no password is given, one is auto-generated.  The system does not save this value. | [optional] 

### Return type

[**InlineResponse200460**](InlineResponse200460.md)

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

# **site_quality_delete_site_quality_user**
> InlineResponse200461 site_quality_delete_site_quality_user()

Delete Site Quality Monitoring account

This function initiates the deletion of the Site Quality Monitoring user account associated with a cPanel user account.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200461 import InlineResponse200461
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
    api_instance = clientapi_cpanel.SiteQualityApi(api_client)

    try:
        # Delete Site Quality Monitoring account
        api_response = api_instance.site_quality_delete_site_quality_user()
        print("The response of SiteQualityApi->site_quality_delete_site_quality_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SiteQualityApi->site_quality_delete_site_quality_user: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**InlineResponse200461**](InlineResponse200461.md)

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

# **site_quality_get_all_scores**
> InlineResponse200462 site_quality_get_all_scores(verbose)

Return all projects' monitoring results

This function returns information about the cPanel user's Site Quality Monitoring projects' most recent monitoring check results.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200462 import InlineResponse200462
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
    api_instance = clientapi_cpanel.SiteQualityApi(api_client)
    verbose = 1 # int | Whether to enable verbose output.  ** Note: **  This includes information about the user's Site Quality Monitoring project's most recent results in each monitoring check subcategory.

    try:
        # Return all projects' monitoring results
        api_response = api_instance.site_quality_get_all_scores(verbose)
        print("The response of SiteQualityApi->site_quality_get_all_scores:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SiteQualityApi->site_quality_get_all_scores: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **verbose** | **int**| Whether to enable verbose output.  ** Note: **  This includes information about the user&#39;s Site Quality Monitoring project&#39;s most recent results in each monitoring check subcategory. | 

### Return type

[**InlineResponse200462**](InlineResponse200462.md)

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

# **site_quality_get_app_token**
> InlineResponse200463 site_quality_get_app_token()

Return koality authentication token

This function returns the long-lived application token used to authenticate with <a href="https://go.cpanel.net/5k" target="_blank">koality's</a> authentication servers.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200463 import InlineResponse200463
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
    api_instance = clientapi_cpanel.SiteQualityApi(api_client)

    try:
        # Return koality authentication token
        api_response = api_instance.site_quality_get_app_token()
        print("The response of SiteQualityApi->site_quality_get_app_token:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SiteQualityApi->site_quality_get_app_token: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**InlineResponse200463**](InlineResponse200463.md)

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

# **site_quality_has_site_quality_user**
> InlineResponse200464 site_quality_has_site_quality_user()

Validate monitoring account existence

This function returns whether the cPanel user has an associated Site Quality Monitoring account.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200464 import InlineResponse200464
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
    api_instance = clientapi_cpanel.SiteQualityApi(api_client)

    try:
        # Validate monitoring account existence
        api_response = api_instance.site_quality_has_site_quality_user()
        print("The response of SiteQualityApi->site_quality_has_site_quality_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SiteQualityApi->site_quality_has_site_quality_user: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**InlineResponse200464**](InlineResponse200464.md)

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

# **site_quality_is_site_quality_user_enabled**
> InlineResponse200465 site_quality_is_site_quality_user_enabled()

Validate monitoring account enablement

This function verifies that <a href="https://go.cpanel.net/5k" target="_blank">koality</a> has enabled the cPanel user's Site Quality Monitoring account.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200465 import InlineResponse200465
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
    api_instance = clientapi_cpanel.SiteQualityApi(api_client)

    try:
        # Validate monitoring account enablement
        api_response = api_instance.site_quality_is_site_quality_user_enabled()
        print("The response of SiteQualityApi->site_quality_is_site_quality_user_enabled:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SiteQualityApi->site_quality_is_site_quality_user_enabled: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**InlineResponse200465**](InlineResponse200465.md)

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

# **site_quality_reset_config**
> InlineResponse200466 site_quality_reset_config()

Remove monitoring user from cPanel configuration

This function will remove Site Quality Monitoring account data from the cPanel user's configuration.

**Note:**
* This function will prevent cPanel & WHM from automatically logging the user into their Site Quality Monitoring account.
* This function does not delete the Site Quality Monitoring account from the <a href="https://go.cpanel.net/5k" target="_blank">koality</a> servers.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200466 import InlineResponse200466
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
    api_instance = clientapi_cpanel.SiteQualityApi(api_client)

    try:
        # Remove monitoring user from cPanel configuration
        api_response = api_instance.site_quality_reset_config()
        print("The response of SiteQualityApi->site_quality_reset_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SiteQualityApi->site_quality_reset_config: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**InlineResponse200466**](InlineResponse200466.md)

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

# **site_quality_send_activation_email**
> InlineResponse200467 site_quality_send_activation_email()

Request activation email

This function sends a Site Quality Monitoring activation email to the currently-authenticated Site Quality Monitoring user.

**Note:**
This email contains the Site Quality Monitoring activation code.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200467 import InlineResponse200467
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
    api_instance = clientapi_cpanel.SiteQualityApi(api_client)

    try:
        # Request activation email
        api_response = api_instance.site_quality_send_activation_email()
        print("The response of SiteQualityApi->site_quality_send_activation_email:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SiteQualityApi->site_quality_send_activation_email: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**InlineResponse200467**](InlineResponse200467.md)

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

# **site_quality_verify_code**
> InlineResponse200468 site_quality_verify_code(code)

Validate activation code

This function validates the activation code in a cPanel user's Site Quality Monitoring registration email.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200468 import InlineResponse200468
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
    api_instance = clientapi_cpanel.SiteQualityApi(api_client)
    code = '123456' # str | The user's Site Quality Monitoring activation code.  **Note:**  A user will receive an email with their activation code when they create a Site Quality Monitoring user account.

    try:
        # Validate activation code
        api_response = api_instance.site_quality_verify_code(code)
        print("The response of SiteQualityApi->site_quality_verify_code:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SiteQualityApi->site_quality_verify_code: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**| The user&#39;s Site Quality Monitoring activation code.  **Note:**  A user will receive an email with their activation code when they create a Site Quality Monitoring user account. | 

### Return type

[**InlineResponse200468**](InlineResponse200468.md)

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

