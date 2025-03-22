# clientapi_cpanel.ThemeSettingsApi

All URIs are relative to *https://cpanel-server.tld:2083/execute*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_theme_base**](ThemeSettingsApi.md#get_theme_base) | **GET** /Themes/get_theme_base | Return current theme
[**themes_list**](ThemeSettingsApi.md#themes_list) | **GET** /Themes/list | Return available themes
[**themes_update**](ThemeSettingsApi.md#themes_update) | **GET** /Themes/update | Update current theme


# **get_theme_base**
> InlineResponse200514 get_theme_base()

Return current theme

This function is deprecated and does not return useful output.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200514 import InlineResponse200514
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
    api_instance = clientapi_cpanel.ThemeSettingsApi(api_client)

    try:
        # Return current theme
        api_response = api_instance.get_theme_base()
        print("The response of ThemeSettingsApi->get_theme_base:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ThemeSettingsApi->get_theme_base: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**InlineResponse200514**](InlineResponse200514.md)

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

# **themes_list**
> InlineResponse200515 themes_list(show_mail_themes=show_mail_themes)

Return available themes

This function lists available themes.

**Note:**

  The `/usr/local/cpanel/scripts/modify_accounts` script allows you to modify the style and theme for many or all accounts on the server. For more information, read our [The modify_accounts Script](https://go.cpanel.net/modifyaccounts) documentation.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200515 import InlineResponse200515
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
    api_instance = clientapi_cpanel.ThemeSettingsApi(api_client)
    show_mail_themes = 0 # int | Whether to list the account's mail themes. * `1` — List mail themes. * `0` — Do **not** list mail themes. (optional) (default to 0)

    try:
        # Return available themes
        api_response = api_instance.themes_list(show_mail_themes=show_mail_themes)
        print("The response of ThemeSettingsApi->themes_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ThemeSettingsApi->themes_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **show_mail_themes** | **int**| Whether to list the account&#39;s mail themes. * &#x60;1&#x60; — List mail themes. * &#x60;0&#x60; — Do **not** list mail themes. | [optional] [default to 0]

### Return type

[**InlineResponse200515**](InlineResponse200515.md)

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

# **themes_update**
> InlineResponse200516 themes_update(theme)

Update current theme

This function applies a new theme to the cPanel interface.

**Note:**

  The `/usr/local/cpanel/scripts/modify_accounts` script allows you to modify the theme for many or all accounts on the server. For more information, read our [The modify_accounts Script](https://go.cpanel.net/modifyaccounts) documentation.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200516 import InlineResponse200516
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
    api_instance = clientapi_cpanel.ThemeSettingsApi(api_client)
    theme = 'jupiter' # str | The theme name.

    try:
        # Update current theme
        api_response = api_instance.themes_update(theme)
        print("The response of ThemeSettingsApi->themes_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ThemeSettingsApi->themes_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **theme** | **str**| The theme name. | 

### Return type

[**InlineResponse200516**](InlineResponse200516.md)

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

