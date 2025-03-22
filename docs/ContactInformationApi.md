# clientapi_cpanel.ContactInformationApi

All URIs are relative to *https://cpanel-server.tld:2083/execute*

Method | HTTP request | Description
------------- | ------------- | -------------
[**contactinformation_set_email_addresses**](ContactInformationApi.md#contactinformation_set_email_addresses) | **GET** /ContactInformation/set_email_addresses | Set contact email address(es)
[**contactinformation_unset_email_addresses**](ContactInformationApi.md#contactinformation_unset_email_addresses) | **GET** /ContactInformation/unset_email_addresses | Unset contact email addresses
[**is_enabled**](ContactInformationApi.md#is_enabled) | **GET** /Contactus/is_enabled | Return whether contact option is enabled


# **contactinformation_set_email_addresses**
> InlineResponse20069 contactinformation_set_email_addresses(address, old_address, password)

Set contact email address(es)

Use this function to set an account's contact email address(es).

To unset all contact email addresses, call `unset_email_addresses`.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response20069 import InlineResponse20069
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
    api_instance = clientapi_cpanel.ContactInformationApi(api_client)
    address = ['[\"foo@example.com\",\"bar@example.com\"]'] # List[str] | The account’s new contact email addresses.
    old_address = ['[\"old1@example.com\"]'] # List[str] | The account’s existing contact email addresses.  If this list does not match the account’s current current email address(es), then the request will fail. This control is here to prevent race conditions.
    password = 'q1df%D9<z0ShqdxRP%^' # str | The account’s password.

    try:
        # Set contact email address(es)
        api_response = api_instance.contactinformation_set_email_addresses(address, old_address, password)
        print("The response of ContactInformationApi->contactinformation_set_email_addresses:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContactInformationApi->contactinformation_set_email_addresses: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address** | [**List[str]**](str.md)| The account’s new contact email addresses. | 
 **old_address** | [**List[str]**](str.md)| The account’s existing contact email addresses.  If this list does not match the account’s current current email address(es), then the request will fail. This control is here to prevent race conditions. | 
 **password** | **str**| The account’s password. | 

### Return type

[**InlineResponse20069**](InlineResponse20069.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Request was successful. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **contactinformation_unset_email_addresses**
> InlineResponse20070 contactinformation_unset_email_addresses(old_address, password)

Unset contact email addresses

Use this function to unset all contact email address for an account.

To set contact email address(es), call `set_email_addresses`.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response20070 import InlineResponse20070
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
    api_instance = clientapi_cpanel.ContactInformationApi(api_client)
    old_address = ['[\"old1@example.com\"]'] # List[str] | The account’s existing contact email addresses.  If this list does not match the account’s current current email address(es), then the request will fail. This control is here to prevent race conditions.
    password = 'q1df%D9<z0ShqdxRP%^' # str | The account’s password.

    try:
        # Unset contact email addresses
        api_response = api_instance.contactinformation_unset_email_addresses(old_address, password)
        print("The response of ContactInformationApi->contactinformation_unset_email_addresses:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContactInformationApi->contactinformation_unset_email_addresses: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **old_address** | [**List[str]**](str.md)| The account’s existing contact email addresses.  If this list does not match the account’s current current email address(es), then the request will fail. This control is here to prevent race conditions. | 
 **password** | **str**| The account’s password. | 

### Return type

[**InlineResponse20070**](InlineResponse20070.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Request was successful. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **is_enabled**
> InlineResponse20071 is_enabled()

Return whether contact option is enabled

This function checks whether the cPanel account can contact their hosting provider from the cPanel interface.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response20071 import InlineResponse20071
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
    api_instance = clientapi_cpanel.ContactInformationApi(api_client)

    try:
        # Return whether contact option is enabled
        api_response = api_instance.is_enabled()
        print("The response of ContactInformationApi->is_enabled:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContactInformationApi->is_enabled: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**InlineResponse20071**](InlineResponse20071.md)

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

