# clientapi_cpanel.TwoFactorAuthApi

All URIs are relative to *https://cpanel-server.tld:2083/execute*

Method | HTTP request | Description
------------- | ------------- | -------------
[**generate_user_configuration**](TwoFactorAuthApi.md#generate_user_configuration) | **GET** /TwoFactorAuth/generate_user_configuration | Create 2FA authentication code
[**get_team_user_configuration**](TwoFactorAuthApi.md#get_team_user_configuration) | **GET** /TwoFactorAuth/get_team_user_configuration | Return team user 2FA config
[**get_user_configuration**](TwoFactorAuthApi.md#get_user_configuration) | **GET** /TwoFactorAuth/get_user_configuration | Return cPanel account 2FA config
[**remove_user_configuration**](TwoFactorAuthApi.md#remove_user_configuration) | **GET** /TwoFactorAuth/remove_user_configuration | Remove 2FA config
[**set_user_configuration**](TwoFactorAuthApi.md#set_user_configuration) | **GET** /TwoFactorAuth/set_user_configuration | Save 2FA config


# **generate_user_configuration**
> InlineResponse200521 generate_user_configuration()

Create 2FA authentication code

This function generates an authentication code to enable configuration of two-factor authentication.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200521 import InlineResponse200521
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
    api_instance = clientapi_cpanel.TwoFactorAuthApi(api_client)

    try:
        # Create 2FA authentication code
        api_response = api_instance.generate_user_configuration()
        print("The response of TwoFactorAuthApi->generate_user_configuration:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TwoFactorAuthApi->generate_user_configuration: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**InlineResponse200521**](InlineResponse200521.md)

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

# **get_team_user_configuration**
> InlineResponse200522 get_team_user_configuration(team_user)

Return team user 2FA config

This function retrieves a [team user's](https://go.cpanel.net/manage-team) configuration settings for two-factor authentication.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200522 import InlineResponse200522
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
    api_instance = clientapi_cpanel.TwoFactorAuthApi(api_client)
    team_user = 'user@example.com' # str | The team user's username.  **Note:**  The username will always precede the cPanel account's primary domain.

    try:
        # Return team user 2FA config
        api_response = api_instance.get_team_user_configuration(team_user)
        print("The response of TwoFactorAuthApi->get_team_user_configuration:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TwoFactorAuthApi->get_team_user_configuration: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_user** | **str**| The team user&#39;s username.  **Note:**  The username will always precede the cPanel account&#39;s primary domain. | 

### Return type

[**InlineResponse200522**](InlineResponse200522.md)

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

# **get_user_configuration**
> InlineResponse200523 get_user_configuration()

Return cPanel account 2FA config

This function retrieves the cPanel account user's configuration settings for two-factor authentication.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200523 import InlineResponse200523
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
    api_instance = clientapi_cpanel.TwoFactorAuthApi(api_client)

    try:
        # Return cPanel account 2FA config
        api_response = api_instance.get_user_configuration()
        print("The response of TwoFactorAuthApi->get_user_configuration:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TwoFactorAuthApi->get_user_configuration: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**InlineResponse200523**](InlineResponse200523.md)

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

# **remove_user_configuration**
> InlineResponse200524 remove_user_configuration()

Remove 2FA config

This function removes the user from the two-factor authentication `userdata` file.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200524 import InlineResponse200524
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
    api_instance = clientapi_cpanel.TwoFactorAuthApi(api_client)

    try:
        # Remove 2FA config
        api_response = api_instance.remove_user_configuration()
        print("The response of TwoFactorAuthApi->remove_user_configuration:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TwoFactorAuthApi->remove_user_configuration: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**InlineResponse200524**](InlineResponse200524.md)

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

# **set_user_configuration**
> InlineResponse200525 set_user_configuration(secret, tfa_token)

Save 2FA config

This function configures the two-factor authentication settings for an account.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200525 import InlineResponse200525
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
    api_instance = clientapi_cpanel.TwoFactorAuthApi(api_client)
    secret = 'JBSWY3DPEHPK3PXP' # str | The 16-character string that UAPI's `TwoFactorAuth::generate_user_configuration` function generates.
    tfa_token = 528112 # int | The six-digit security code that the time-based one-time password (TOTP) authentication app generates.

    try:
        # Save 2FA config
        api_response = api_instance.set_user_configuration(secret, tfa_token)
        print("The response of TwoFactorAuthApi->set_user_configuration:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TwoFactorAuthApi->set_user_configuration: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **secret** | **str**| The 16-character string that UAPI&#39;s &#x60;TwoFactorAuth::generate_user_configuration&#x60; function generates. | 
 **tfa_token** | **int**| The six-digit security code that the time-based one-time password (TOTP) authentication app generates. | 

### Return type

[**InlineResponse200525**](InlineResponse200525.md)

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

