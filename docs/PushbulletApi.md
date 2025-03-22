# clientapi_cpanel.PushbulletApi

All URIs are relative to *https://cpanel-server.tld:2083/execute*

Method | HTTP request | Description
------------- | ------------- | -------------
[**send_test_message**](PushbulletApi.md#send_test_message) | **GET** /Pushbullet/send_test_message | Validate Pushbullet token


# **send_test_message**
> InlineResponse200392 send_test_message(access_token)

Validate Pushbullet token

This function sends a Pushbullet™ test message to determine that the token is valid and that the account holder can receive the message.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200392 import InlineResponse200392
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
    api_instance = clientapi_cpanel.PushbulletApi(api_client)
    access_token = 'a1b2c3d4e5f6g7h8i9j0' # str | The Pushbullet access token.  **Note:**  * Your Pushbullet token is available on [Pushbullet's My Account](https://www.pushbullet.com/account) page under the *Access Token* heading. * This is confidential information that your server sends via a secure channel.

    try:
        # Validate Pushbullet token
        api_response = api_instance.send_test_message(access_token)
        print("The response of PushbulletApi->send_test_message:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PushbulletApi->send_test_message: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_token** | **str**| The Pushbullet access token.  **Note:**  * Your Pushbullet token is available on [Pushbullet&#39;s My Account](https://www.pushbullet.com/account) page under the *Access Token* heading. * This is confidential information that your server sends via a secure channel. | 

### Return type

[**InlineResponse200392**](InlineResponse200392.md)

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

