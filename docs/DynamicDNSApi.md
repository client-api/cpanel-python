# clientapi_cpanel.DynamicDNSApi

All URIs are relative to *https://cpanel-server.tld:2083/execute*

Method | HTTP request | Description
------------- | ------------- | -------------
[**dynamicdns_create**](DynamicDNSApi.md#dynamicdns_create) | **GET** /DynamicDNS/create | Create Dynamic DNS domain
[**dynamicdns_delete**](DynamicDNSApi.md#dynamicdns_delete) | **GET** /DynamicDNS/delete | Delete Dynamic DNS domain
[**dynamicdns_list**](DynamicDNSApi.md#dynamicdns_list) | **GET** /DynamicDNS/list | Return Dynamic DNS domains
[**dynamicdns_recreate**](DynamicDNSApi.md#dynamicdns_recreate) | **GET** /DynamicDNS/recreate | Update Dynamic DNS domain ID
[**dynamicdns_set_description**](DynamicDNSApi.md#dynamicdns_set_description) | **GET** /DynamicDNS/set_description | Update Dynamic DNS domain description


# **dynamicdns_create**
> InlineResponse200114 dynamicdns_create(domain, description=description)

Create Dynamic DNS domain

This function creates a Dynamic DNS (DDNS) domain.

**Important:**

When you disable the [_DNS_ role](https://go.cpanel.net/serverroles), the system disables this function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200114 import InlineResponse200114
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
    api_instance = clientapi_cpanel.DynamicDNSApi(api_client)
    domain = 'home.example.com' # str | The fully-qualified domain name to create as a DDNS domain.
    description = 'Home network' # str | A human-readable string that describes the domain. (optional)

    try:
        # Create Dynamic DNS domain
        api_response = api_instance.dynamicdns_create(domain, description=description)
        print("The response of DynamicDNSApi->dynamicdns_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DynamicDNSApi->dynamicdns_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**| The fully-qualified domain name to create as a DDNS domain. | 
 **description** | **str**| A human-readable string that describes the domain. | [optional] 

### Return type

[**InlineResponse200114**](InlineResponse200114.md)

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

# **dynamicdns_delete**
> InlineResponse200115 dynamicdns_delete(id)

Delete Dynamic DNS domain

This function deletes an existing Dynamic DNS (DDNS) domain.

**Important:**

When you disable the [_DNS_ role](https://go.cpanel.net/serverroles), the system disables this function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200115 import InlineResponse200115
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
    api_instance = clientapi_cpanel.DynamicDNSApi(api_client)
    id = 'ggiugyxxjwnkmqtwysgmvrurplmafxpq' # str | The DDNS domain’s ID.

    try:
        # Delete Dynamic DNS domain
        api_response = api_instance.dynamicdns_delete(id)
        print("The response of DynamicDNSApi->dynamicdns_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DynamicDNSApi->dynamicdns_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The DDNS domain’s ID. | 

### Return type

[**InlineResponse200115**](InlineResponse200115.md)

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

# **dynamicdns_list**
> InlineResponse200116 dynamicdns_list()

Return Dynamic DNS domains

This function lists the user’s Dynamic DNS (DDNS) domains.

**Important:**

When you disable the [_DNS_ role](https://go.cpanel.net/serverroles), the system disables this function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200116 import InlineResponse200116
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
    api_instance = clientapi_cpanel.DynamicDNSApi(api_client)

    try:
        # Return Dynamic DNS domains
        api_response = api_instance.dynamicdns_list()
        print("The response of DynamicDNSApi->dynamicdns_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DynamicDNSApi->dynamicdns_list: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**InlineResponse200116**](InlineResponse200116.md)

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

# **dynamicdns_recreate**
> InlineResponse200117 dynamicdns_recreate(id)

Update Dynamic DNS domain ID

This function gives a new, randomly-generated ID to an existing Dynamic DNS (DDNS) domain.

**Important:**

When you disable the [_DNS_ role](https://go.cpanel.net/serverroles), the system disables this function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200117 import InlineResponse200117
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
    api_instance = clientapi_cpanel.DynamicDNSApi(api_client)
    id = 'ggiugyxxjwnkmqtwysgmvrurplmafxpq' # str | The DDNS domain’s ID.

    try:
        # Update Dynamic DNS domain ID
        api_response = api_instance.dynamicdns_recreate(id)
        print("The response of DynamicDNSApi->dynamicdns_recreate:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DynamicDNSApi->dynamicdns_recreate: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The DDNS domain’s ID. | 

### Return type

[**InlineResponse200117**](InlineResponse200117.md)

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

# **dynamicdns_set_description**
> InlineResponse200118 dynamicdns_set_description(description, id)

Update Dynamic DNS domain description

This function sets the description on a user’s Dynamic DNS (DDNS) domain.

**Important:**

When you disable the [_DNS_ role](https://go.cpanel.net/serverroles), the system disables this function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200118 import InlineResponse200118
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
    api_instance = clientapi_cpanel.DynamicDNSApi(api_client)
    description = 'Home network' # str | A human-readable string that describes the domain.
    id = 'ggiugyxxjwnkmqtwysgmvrurplmafxpq' # str | The DDNS domain’s ID.

    try:
        # Update Dynamic DNS domain description
        api_response = api_instance.dynamicdns_set_description(description, id)
        print("The response of DynamicDNSApi->dynamicdns_set_description:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DynamicDNSApi->dynamicdns_set_description: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **description** | **str**| A human-readable string that describes the domain. | 
 **id** | **str**| The DDNS domain’s ID. | 

### Return type

[**InlineResponse200118**](InlineResponse200118.md)

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

