# clientapi_cpanel.ApplicationManagerApi

All URIs are relative to *https://cpanel-server.tld:2083/execute*

Method | HTTP request | Description
------------- | ------------- | -------------
[**disable_application**](ApplicationManagerApi.md#disable_application) | **GET** /PassengerApps/disable_application | Disable Passenger application
[**edit_application**](ApplicationManagerApi.md#edit_application) | **GET** /PassengerApps/edit_application | Update Passenger application settings
[**enable_application**](ApplicationManagerApi.md#enable_application) | **GET** /PassengerApps/enable_application | Enable Passenger application
[**ensure_deps**](ApplicationManagerApi.md#ensure_deps) | **GET** /PassengerApps/ensure_deps | Install Passenger application dependencies
[**list_applications**](ApplicationManagerApi.md#list_applications) | **GET** /PassengerApps/list_applications | Return Passenger applications
[**register_application**](ApplicationManagerApi.md#register_application) | **GET** /PassengerApps/register_application | Register Passenger application
[**unregister_application**](ApplicationManagerApi.md#unregister_application) | **GET** /PassengerApps/unregister_application | Unregister Passenger application


# **disable_application**
> InlineResponse200367 disable_application(name)

Disable Passenger application

This function disables a Passenger application on an account.

**Important:**

  When you disable the [Web Server role](https://go.cpanel.net/serverroles#roles), the system **disables** this function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200367 import InlineResponse200367
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
    api_instance = clientapi_cpanel.ApplicationManagerApi(api_client)
    name = 'slippers' # str | The application to disable.

    try:
        # Disable Passenger application
        api_response = api_instance.disable_application(name)
        print("The response of ApplicationManagerApi->disable_application:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationManagerApi->disable_application: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The application to disable. | 

### Return type

[**InlineResponse200367**](InlineResponse200367.md)

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

# **edit_application**
> InlineResponse200368 edit_application(name, clear_envvars=clear_envvars, deployment_mode=deployment_mode, domain=domain, enabled=enabled, envvar_name=envvar_name, envvar_value=envvar_value, new_name=new_name, path=path)

Update Passenger application settings

This function edits a Passenger application for an account.

**Note**:

  When you disable the [Web Server role](https://go.cpanel.net/serverroles), the system **disables** this function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200368 import InlineResponse200368
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
    api_instance = clientapi_cpanel.ApplicationManagerApi(api_client)
    name = 'Ruby Slippers' # str | The application’s current name.
    clear_envvars = 0 # int | Whether to clear the application’s environment variables. (optional) (default to 0)
    deployment_mode = 'production' # str | The new server environment in which to run the application. If you do not use this parameter, the function does not change the application’s server environment.    * `development` — Sets the application to run in a development environment.   * `production` — Sets the application to run in a production environment. (optional)
    domain = 'toto.com' # str | The application’s new domain. If you do not use this parameter, the function does not change the application’s domain. (optional)
    enabled = 1 # int | Whether to enable the application and generate the web server configuration for it.    * `1` — Enable the application and generate the web server configuration.   * `0` — Don’t enable the application and generate the web server configuration. (optional) (default to 1)
    envvar_name = ['[\"SCARECROW\",\"TINMAN\",\"LION\"]'] # List[str] | New set of environment variables for the application.  **Important**:   The function replaces all current environment variables with the variables that you pass in this parameter.  **Note**:    For each `envvar_name` parameter you send you **must** include an `envvar_value` parameter. (optional)
    envvar_value = ['[\"brain\",\"heart\",\"courage\"]'] # List[str] | Each environment variable’s value.  **Note**:    For each `envvar_name` parameter you send you **must** include an `envvar_value` parameter. (optional)
    new_name = 'Little Dog' # str | The application’s new name. If you do not use this parameter, the function does not change the application's name. (optional)
    path = '/home/dorothy/littledog' # str | The application’s new filepath. If you do not use this parameter, the function does not change the application’s filepath. (optional)

    try:
        # Update Passenger application settings
        api_response = api_instance.edit_application(name, clear_envvars=clear_envvars, deployment_mode=deployment_mode, domain=domain, enabled=enabled, envvar_name=envvar_name, envvar_value=envvar_value, new_name=new_name, path=path)
        print("The response of ApplicationManagerApi->edit_application:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationManagerApi->edit_application: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The application’s current name. | 
 **clear_envvars** | **int**| Whether to clear the application’s environment variables. | [optional] [default to 0]
 **deployment_mode** | **str**| The new server environment in which to run the application. If you do not use this parameter, the function does not change the application’s server environment.    * &#x60;development&#x60; — Sets the application to run in a development environment.   * &#x60;production&#x60; — Sets the application to run in a production environment. | [optional] 
 **domain** | **str**| The application’s new domain. If you do not use this parameter, the function does not change the application’s domain. | [optional] 
 **enabled** | **int**| Whether to enable the application and generate the web server configuration for it.    * &#x60;1&#x60; — Enable the application and generate the web server configuration.   * &#x60;0&#x60; — Don’t enable the application and generate the web server configuration. | [optional] [default to 1]
 **envvar_name** | [**List[str]**](str.md)| New set of environment variables for the application.  **Important**:   The function replaces all current environment variables with the variables that you pass in this parameter.  **Note**:    For each &#x60;envvar_name&#x60; parameter you send you **must** include an &#x60;envvar_value&#x60; parameter. | [optional] 
 **envvar_value** | [**List[str]**](str.md)| Each environment variable’s value.  **Note**:    For each &#x60;envvar_name&#x60; parameter you send you **must** include an &#x60;envvar_value&#x60; parameter. | [optional] 
 **new_name** | **str**| The application’s new name. If you do not use this parameter, the function does not change the application&#39;s name. | [optional] 
 **path** | **str**| The application’s new filepath. If you do not use this parameter, the function does not change the application’s filepath. | [optional] 

### Return type

[**InlineResponse200368**](InlineResponse200368.md)

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

# **enable_application**
> InlineResponse200369 enable_application(name)

Enable Passenger application

This function enables a Passenger application and generates the Apache configuration on an account.

**Important:**

When you disable the [Web Server role](https://go.cpanel.net/howtouseserverprofiles#roles), the system **disables** this function. 

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200369 import InlineResponse200369
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
    api_instance = clientapi_cpanel.ApplicationManagerApi(api_client)
    name = 'slippers' # str | The Passenger application to enable on the account.

    try:
        # Enable Passenger application
        api_response = api_instance.enable_application(name)
        print("The response of ApplicationManagerApi->enable_application:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationManagerApi->enable_application: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The Passenger application to enable on the account. | 

### Return type

[**InlineResponse200369**](InlineResponse200369.md)

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

# **ensure_deps**
> InlineResponse200370 ensure_deps(app_path, type)

Install Passenger application dependencies

This function installs the dependencies for a Passenger application.

**Note**:

  This function starts the installation process. This may take a long time to complete.

**Important**:

  When you disable the [Web Server role](https://go.cpanel.net/serverroles), the system **disables** this function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200370 import InlineResponse200370
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
    api_instance = clientapi_cpanel.ApplicationManagerApi(api_client)
    app_path = '/home/example/my-app/' # str | The application’s filepath.
    type = 'npm' # str | The application’s type.  * `gem` — Ensure ruby gems in the application’s `Gemfile` file. * `npm` — Ensure node packages in the application’s `package.json` file. * `pip` — Ensure python pips in the application’s `requirements.txt` file.

    try:
        # Install Passenger application dependencies
        api_response = api_instance.ensure_deps(app_path, type)
        print("The response of ApplicationManagerApi->ensure_deps:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationManagerApi->ensure_deps: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_path** | **str**| The application’s filepath. | 
 **type** | **str**| The application’s type.  * &#x60;gem&#x60; — Ensure ruby gems in the application’s &#x60;Gemfile&#x60; file. * &#x60;npm&#x60; — Ensure node packages in the application’s &#x60;package.json&#x60; file. * &#x60;pip&#x60; — Ensure python pips in the application’s &#x60;requirements.txt&#x60; file. | 

### Return type

[**InlineResponse200370**](InlineResponse200370.md)

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

# **list_applications**
> InlineResponse200371 list_applications()

Return Passenger applications

This function lists an account’s Passenger applications.

**Important:**

  When you disable the [Web Server role](https://go.cpanel.net/serverroles), the system **disables** this function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200371 import InlineResponse200371
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
    api_instance = clientapi_cpanel.ApplicationManagerApi(api_client)

    try:
        # Return Passenger applications
        api_response = api_instance.list_applications()
        print("The response of ApplicationManagerApi->list_applications:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationManagerApi->list_applications: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**InlineResponse200371**](InlineResponse200371.md)

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

# **register_application**
> InlineResponse200372 register_application(domain, name, path, base_uri=base_uri, deployment_mode=deployment_mode, enabled=enabled, envvar_name=envvar_name, envvar_value=envvar_value)

Register Passenger application

This function registers a Passenger application for an account.

**Important**:

  * This function **only** registers an application. It does **not** create the application. You **must** create an application **before** you register the application. For an example of how to do this, read our [How to Create Ruby Web Applications](https://go.cpanel.net/howtocreaterubyapps) documentation.
  * When you disable the [Web Server role](https://go.cpanel.net/serverroles), the system **disables** this function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200372 import InlineResponse200372
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
    api_instance = clientapi_cpanel.ApplicationManagerApi(api_client)
    domain = 'dorothy.com' # str | The domain for which to register the application.
    name = 'Name of Application' # str | The application’s name.
    path = '/slippers' # str | The application’s filepath relative to the user’s home directory.
    base_uri = '/' # str | The application’s base URI. (optional) (default to '/')
    deployment_mode = production # str | The type of server environment in which to run the application.    * `development` — Sets the application to run in a development environment.   * `production` — Sets the application to run in a production environment. (optional) (default to production)
    enabled = 1 # int | Whether to enable the application and generate the web server configuration for it.    * `1` — Enable the application and generate the web server configuration.   * `0` — Don’t enable the application and generate the web server configuration. (optional) (default to 1)
    envvar_name = ['[\"SHOES\",\"TINMAN\"]'] # List[str] | Environment variables that the application needs.  **Note**:    For each `envvar_name` parameter you send, you **must** include an `envvar_value` parameter.    This parameter's value can only contain letters, numbers, underscores, and dashes, and cannot begin with a number. This parameter's value must also not exceed 256 characters. (optional)
    envvar_value = ['[\"ruby\",\"heart\"]'] # List[str] | Each environment variable’s value.  **Note**:    For each `envvar_name` parameter you send, you **must** include an `envvar_value` parameter.    An environment variable value must contain 1024 or fewer ASCII-printable characters. (optional)

    try:
        # Register Passenger application
        api_response = api_instance.register_application(domain, name, path, base_uri=base_uri, deployment_mode=deployment_mode, enabled=enabled, envvar_name=envvar_name, envvar_value=envvar_value)
        print("The response of ApplicationManagerApi->register_application:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationManagerApi->register_application: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**| The domain for which to register the application. | 
 **name** | **str**| The application’s name. | 
 **path** | **str**| The application’s filepath relative to the user’s home directory. | 
 **base_uri** | **str**| The application’s base URI. | [optional] [default to &#39;/&#39;]
 **deployment_mode** | **str**| The type of server environment in which to run the application.    * &#x60;development&#x60; — Sets the application to run in a development environment.   * &#x60;production&#x60; — Sets the application to run in a production environment. | [optional] [default to production]
 **enabled** | **int**| Whether to enable the application and generate the web server configuration for it.    * &#x60;1&#x60; — Enable the application and generate the web server configuration.   * &#x60;0&#x60; — Don’t enable the application and generate the web server configuration. | [optional] [default to 1]
 **envvar_name** | [**List[str]**](str.md)| Environment variables that the application needs.  **Note**:    For each &#x60;envvar_name&#x60; parameter you send, you **must** include an &#x60;envvar_value&#x60; parameter.    This parameter&#39;s value can only contain letters, numbers, underscores, and dashes, and cannot begin with a number. This parameter&#39;s value must also not exceed 256 characters. | [optional] 
 **envvar_value** | [**List[str]**](str.md)| Each environment variable’s value.  **Note**:    For each &#x60;envvar_name&#x60; parameter you send, you **must** include an &#x60;envvar_value&#x60; parameter.    An environment variable value must contain 1024 or fewer ASCII-printable characters. | [optional] 

### Return type

[**InlineResponse200372**](InlineResponse200372.md)

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

# **unregister_application**
> InlineResponse200373 unregister_application(name)

Unregister Passenger application

This function unregisters a [Passenger application](https://go.cpanel.net/cpaneldocsApplicationManager) on an account.

**Note:**

  * This function **only** unregisters an application. It does **not** delete the application. You **must** manually delete the application from your system.
  * When you disable the [Web Server role](https://go.cpanel.net/serverroles), the system **disables** this function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200373 import InlineResponse200373
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
    api_instance = clientapi_cpanel.ApplicationManagerApi(api_client)
    name = 'slippers' # str | The application to unregister.

    try:
        # Unregister Passenger application
        api_response = api_instance.unregister_application(name)
        print("The response of ApplicationManagerApi->unregister_application:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationManagerApi->unregister_application: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The application to unregister. | 

### Return type

[**InlineResponse200373**](InlineResponse200373.md)

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

