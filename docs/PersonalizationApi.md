# clientapi_cpanel.PersonalizationApi

All URIs are relative to *https://cpanel-server.tld:2083/execute*

Method | HTTP request | Description
------------- | ------------- | -------------
[**personalization_get**](PersonalizationApi.md#personalization_get) | **POST** /Personalization/get | Retrieve NVData data from file
[**personalization_set**](PersonalizationApi.md#personalization_set) | **POST** /Personalization/set | Save NVData data to file


# **personalization_get**
> InlineResponse200375 personalization_get(personalization_get_body)

Retrieve NVData data from file

This function retrieves the data from an NVData file on disk. cPanel
NVData is a per-account configuration storage mechanism that you can use to
maintain persistent cPanel & WHM settings across multiple sessions. This includes
custom settings for your own themes and plugins.

**Note:**

NVData keys and values are limited to 128 and 2048 bytes, respectively.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200375 import InlineResponse200375
from clientapi_cpanel.models.personalization_get_body import PersonalizationGetBody
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
    api_instance = clientapi_cpanel.PersonalizationApi(api_client)
    personalization_get_body = clientapi_cpanel.PersonalizationGetBody() # PersonalizationGetBody | 

    try:
        # Retrieve NVData data from file
        api_response = api_instance.personalization_get(personalization_get_body)
        print("The response of PersonalizationApi->personalization_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PersonalizationApi->personalization_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **personalization_get_body** | [**PersonalizationGetBody**](PersonalizationGetBody.md)|  | 

### Return type

[**InlineResponse200375**](InlineResponse200375.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | HTTP Request was successful. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **personalization_set**
> InlineResponse200376 personalization_set(personalization_set_body)

Save NVData data to file

This function saves its data to an NVData file on disk. cPanel
NVData is a per-account configuration storage mechanism that you can use to
maintain persistent cPanel & WHM settings across multiple sessions. This includes
custom settings for your own themes and plugins.

**Note:**

NVData keys and values are limited to 128 and 2048 bytes, respectively.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200376 import InlineResponse200376
from clientapi_cpanel.models.personalization_set_body import PersonalizationSetBody
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
    api_instance = clientapi_cpanel.PersonalizationApi(api_client)
    personalization_set_body = clientapi_cpanel.PersonalizationSetBody() # PersonalizationSetBody | 

    try:
        # Save NVData data to file
        api_response = api_instance.personalization_set(personalization_set_body)
        print("The response of PersonalizationApi->personalization_set:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PersonalizationApi->personalization_set: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **personalization_set_body** | [**PersonalizationSetBody**](PersonalizationSetBody.md)|  | 

### Return type

[**InlineResponse200376**](InlineResponse200376.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | HTTP Request was successful. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

