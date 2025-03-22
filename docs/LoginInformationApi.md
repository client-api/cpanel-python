# clientapi_cpanel.LoginInformationApi

All URIs are relative to *https://cpanel-server.tld:2083/execute*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_last_or_current_logged_in_ip**](LoginInformationApi.md#get_last_or_current_logged_in_ip) | **GET** /LastLogin/get_last_or_current_logged_in_ip | Return last authenticated login IP address
[**get_session_information**](LoginInformationApi.md#get_session_information) | **GET** /Variables/get_session_information | Return web server&#39;s hostname


# **get_last_or_current_logged_in_ip**
> InlineResponse200290 get_last_or_current_logged_in_ip()

Return last authenticated login IP address

This function returns the IP address of the user who most recently logged in.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200290 import InlineResponse200290
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
    api_instance = clientapi_cpanel.LoginInformationApi(api_client)

    try:
        # Return last authenticated login IP address
        api_response = api_instance.get_last_or_current_logged_in_ip()
        print("The response of LoginInformationApi->get_last_or_current_logged_in_ip:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LoginInformationApi->get_last_or_current_logged_in_ip: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**InlineResponse200290**](InlineResponse200290.md)

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

# **get_session_information**
> InlineResponse200540 get_session_information(name=name)

Return web server's hostname

This function retrieves a web server's hostname.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200540 import InlineResponse200540
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
    api_instance = clientapi_cpanel.LoginInformationApi(api_client)
    name = host # str | The web server environment variable to retrieve. You can **only** retrieve the web server's hostname.  * `host` is the only possible value. (optional) (default to host)

    try:
        # Return web server's hostname
        api_response = api_instance.get_session_information(name=name)
        print("The response of LoginInformationApi->get_session_information:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LoginInformationApi->get_session_information: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The web server environment variable to retrieve. You can **only** retrieve the web server&#39;s hostname.  * &#x60;host&#x60; is the only possible value. | [optional] [default to host]

### Return type

[**InlineResponse200540**](InlineResponse200540.md)

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

