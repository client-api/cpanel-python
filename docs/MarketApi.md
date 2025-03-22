# clientapi_cpanel.MarketApi

All URIs are relative to *https://cpanel-server.tld:2083/execute*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancel_pending_ssl_certificate**](MarketApi.md#cancel_pending_ssl_certificate) | **GET** /Market/cancel_pending_ssl_certificate | Delete an order
[**create_shopping_cart**](MarketApi.md#create_shopping_cart) | **GET** /Market/create_shopping_cart | Create shopping cart
[**get_certificate_status_details**](MarketApi.md#get_certificate_status_details) | **GET** /Market/get_certificate_status_details | Return provider&#39;s SSL certificate request status
[**get_login_url**](MarketApi.md#get_login_url) | **GET** /Market/get_login_url | Return provider&#39;s login URL
[**get_pending_ssl_certificates**](MarketApi.md#get_pending_ssl_certificates) | **GET** /Market/get_pending_ssl_certificates | Return provider&#39;s pending SSL certificates
[**get_ssl_certificate_if_available**](MarketApi.md#get_ssl_certificate_if_available) | **GET** /Market/get_ssl_certificate_if_available | Return provider&#39;s available SSL certificates
[**market_get_all_products**](MarketApi.md#market_get_all_products) | **GET** /Market/get_all_products | Return provider&#39;s available products
[**market_get_provider_specific_dcv_constraints**](MarketApi.md#market_get_provider_specific_dcv_constraints) | **GET** /Market/get_provider_specific_dcv_constraints | Return provider&#39;s DCV filename requirements
[**market_get_providers_list**](MarketApi.md#market_get_providers_list) | **GET** /Market/get_providers_list | Return enabled providers
[**process_ssl_pending_queue**](MarketApi.md#process_ssl_pending_queue) | **GET** /Market/process_ssl_pending_queue | Start processing pending queue&#39;s SSL certificates
[**request_ssl_certificates**](MarketApi.md#request_ssl_certificates) | **GET** /Market/request_ssl_certificates | Request SSL certificate order
[**set_status_of_pending_queue_items**](MarketApi.md#set_status_of_pending_queue_items) | **GET** /Market/set_status_of_pending_queue_items | Update status of items in pending queue
[**set_url_after_checkout**](MarketApi.md#set_url_after_checkout) | **GET** /Market/set_url_after_checkout | Update URL after checkout
[**validate_login_token**](MarketApi.md#validate_login_token) | **GET** /Market/validate_login_token | Validate login token


# **cancel_pending_ssl_certificate**
> InlineResponse200302 cancel_pending_ssl_certificate(order_item_id, provider)

Delete an order

This function cancels an order and removes the polling for a pending certificate.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200302 import InlineResponse200302
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
    api_instance = clientapi_cpanel.MarketApi(api_client)
    order_item_id = '10427508' # str | The ID of the ordered item to cancel.
    provider = 'cPStore' # str | The cPanel Market provider's name.

    try:
        # Delete an order
        api_response = api_instance.cancel_pending_ssl_certificate(order_item_id, provider)
        print("The response of MarketApi->cancel_pending_ssl_certificate:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketApi->cancel_pending_ssl_certificate: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_item_id** | **str**| The ID of the ordered item to cancel. | 
 **provider** | **str**| The cPanel Market provider&#39;s name. | 

### Return type

[**InlineResponse200302**](InlineResponse200302.md)

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

# **create_shopping_cart**
> InlineResponse200303 create_shopping_cart(access_token, item, provider, url_after_checkout)

Create shopping cart

This function creates a shopping cart with which the system sends an order to the cPanel Store. Typically, the system will send shopping cart orders for SSL certificates to UAPI’s `Market::request_ssl_certificates` function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200303 import InlineResponse200303
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
    api_instance = clientapi_cpanel.MarketApi(api_client)
    access_token = '1a676e6f-99fc-11e6-9ab6-e60a769b73bc' # str | The access token to connect to the provider.
    item = ['[\"{\\\"product_id\\\":123456,\\\"provider-specfic-key\\\":\\\"provider-specfic-value\\\",\\\"another-provider-specfic-key\\\":\\\"another-provider-specfic-value\\\"}\",\"{\\\"product_id\\\":123457,\\\"provider-specfic-key\\\":\\\"provider-specfic-value\\\",\\\"another-provider-specfic-key\\\":\\\"another-provider-specfic-value\\\"}\"]'] # List[str] | The items to add to the shopping cart.  **Note**:    The value is a JSON string.    This object has one required key, `product_id`, which is a string.    The other keys/values in this object vary depending on the provider.
    provider = 'cPStore' # str | The cPanel Market provider’s name.
    url_after_checkout = 'http://www.example.com/thenextplace' # str | The location to which the provider directs the user after the checkout process is complete.

    try:
        # Create shopping cart
        api_response = api_instance.create_shopping_cart(access_token, item, provider, url_after_checkout)
        print("The response of MarketApi->create_shopping_cart:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketApi->create_shopping_cart: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_token** | **str**| The access token to connect to the provider. | 
 **item** | [**List[str]**](str.md)| The items to add to the shopping cart.  **Note**:    The value is a JSON string.    This object has one required key, &#x60;product_id&#x60;, which is a string.    The other keys/values in this object vary depending on the provider. | 
 **provider** | **str**| The cPanel Market provider’s name. | 
 **url_after_checkout** | **str**| The location to which the provider directs the user after the checkout process is complete. | 

### Return type

[**InlineResponse200303**](InlineResponse200303.md)

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

# **get_certificate_status_details**
> InlineResponse200305 get_certificate_status_details(order_item_id, provider)

Return provider's SSL certificate request status

This function returns the status of an SSL certificate request. The returns include
actionable URLs for users to expedite the validation process, if applicable.

**Important:**

Because this function returns data from a dynamic source, the returns in each
object can vary.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200305 import InlineResponse200305
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
    api_instance = clientapi_cpanel.MarketApi(api_client)
    order_item_id = 1234567890 # int | The order ID that the cPanel Market provider assigned.
    provider = 'cPStore' # str | The cPanel Market provider's name.

    try:
        # Return provider's SSL certificate request status
        api_response = api_instance.get_certificate_status_details(order_item_id, provider)
        print("The response of MarketApi->get_certificate_status_details:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketApi->get_certificate_status_details: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_item_id** | **int**| The order ID that the cPanel Market provider assigned. | 
 **provider** | **str**| The cPanel Market provider&#39;s name. | 

### Return type

[**InlineResponse200305**](InlineResponse200305.md)

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

# **get_login_url**
> InlineResponse200306 get_login_url(provider, url_after_login)

Return provider's login URL

This function retrieves the login URL for the cPanel Market provider.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200306 import InlineResponse200306
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
    api_instance = clientapi_cpanel.MarketApi(api_client)
    provider = 'cPStore' # str | The cPanel Market provider's name.
    url_after_login = 'http://hostname.example.com/redirectionlocation.cgi?state' # str | Where the cPanel Market provider redirects the user's browser after they log in.

    try:
        # Return provider's login URL
        api_response = api_instance.get_login_url(provider, url_after_login)
        print("The response of MarketApi->get_login_url:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketApi->get_login_url: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider** | **str**| The cPanel Market provider&#39;s name. | 
 **url_after_login** | **str**| Where the cPanel Market provider redirects the user&#39;s browser after they log in. | 

### Return type

[**InlineResponse200306**](InlineResponse200306.md)

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

# **get_pending_ssl_certificates**
> InlineResponse200307 get_pending_ssl_certificates(provider)

Return provider's pending SSL certificates

This function lists all pending SSL certificates from a cPanel Market provider for which the system currently polls.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200307 import InlineResponse200307
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
    api_instance = clientapi_cpanel.MarketApi(api_client)
    provider = 'cPStore' # str | The cPanel Market provider's name.

    try:
        # Return provider's pending SSL certificates
        api_response = api_instance.get_pending_ssl_certificates(provider)
        print("The response of MarketApi->get_pending_ssl_certificates:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketApi->get_pending_ssl_certificates: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider** | **str**| The cPanel Market provider&#39;s name. | 

### Return type

[**InlineResponse200307**](InlineResponse200307.md)

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

# **get_ssl_certificate_if_available**
> InlineResponse200310 get_ssl_certificate_if_available(order_item_id, provider)

Return provider's available SSL certificates

This function retrieves SSL certificates when they are available from the cPanel Market provider.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200310 import InlineResponse200310
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
    api_instance = clientapi_cpanel.MarketApi(api_client)
    order_item_id = '8675309' # str | The order item for which to poll.
    provider = 'cPStore' # str | The cPanel Market provider's name.

    try:
        # Return provider's available SSL certificates
        api_response = api_instance.get_ssl_certificate_if_available(order_item_id, provider)
        print("The response of MarketApi->get_ssl_certificate_if_available:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketApi->get_ssl_certificate_if_available: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_item_id** | **str**| The order item for which to poll. | 
 **provider** | **str**| The cPanel Market provider&#39;s name. | 

### Return type

[**InlineResponse200310**](InlineResponse200310.md)

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

# **market_get_all_products**
> InlineResponse200304 market_get_all_products()

Return provider's available products

This function lists all products available through all enabled cPanel Market providers.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200304 import InlineResponse200304
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
    api_instance = clientapi_cpanel.MarketApi(api_client)

    try:
        # Return provider's available products
        api_response = api_instance.market_get_all_products()
        print("The response of MarketApi->market_get_all_products:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketApi->market_get_all_products: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**InlineResponse200304**](InlineResponse200304.md)

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

# **market_get_provider_specific_dcv_constraints**
> InlineResponse200308 market_get_provider_specific_dcv_constraints(provider)

Return provider's DCV filename requirements

This function returns the provider's filename requirements for Domain Control Validation (DCV) checks.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200308 import InlineResponse200308
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
    api_instance = clientapi_cpanel.MarketApi(api_client)
    provider = 'cPStore' # str | The cPanel Market provider's name.

    try:
        # Return provider's DCV filename requirements
        api_response = api_instance.market_get_provider_specific_dcv_constraints(provider)
        print("The response of MarketApi->market_get_provider_specific_dcv_constraints:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketApi->market_get_provider_specific_dcv_constraints: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider** | **str**| The cPanel Market provider&#39;s name. | 

### Return type

[**InlineResponse200308**](InlineResponse200308.md)

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

# **market_get_providers_list**
> InlineResponse200309 market_get_providers_list()

Return enabled providers

This function lists the names of enabled cPanel Market providers.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200309 import InlineResponse200309
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
    api_instance = clientapi_cpanel.MarketApi(api_client)

    try:
        # Return enabled providers
        api_response = api_instance.market_get_providers_list()
        print("The response of MarketApi->market_get_providers_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketApi->market_get_providers_list: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**InlineResponse200309**](InlineResponse200309.md)

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

# **process_ssl_pending_queue**
> InlineResponse200311 process_ssl_pending_queue()

Start processing pending queue's SSL certificates

This function manually processes the cPanel Market's SSL certificate request pending queue.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200311 import InlineResponse200311
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
    api_instance = clientapi_cpanel.MarketApi(api_client)

    try:
        # Start processing pending queue's SSL certificates
        api_response = api_instance.process_ssl_pending_queue()
        print("The response of MarketApi->process_ssl_pending_queue:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketApi->process_ssl_pending_queue: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**InlineResponse200311**](InlineResponse200311.md)

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

# **request_ssl_certificates**
> InlineResponse200312 request_ssl_certificates(access_token, certificate, provider, identity_verification=identity_verification, url_after_checkout=url_after_checkout)

Request SSL certificate order

This function submits a request for a certificate order to the cPanel Market provider.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200312 import InlineResponse200312
from clientapi_cpanel.models.object import object
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
    api_instance = clientapi_cpanel.MarketApi(api_client)
    access_token = '725431a1-d5bc-11e5-a28b-8b0e09a93f05' # str | The access token for the session to the cPanel Market provider.
    certificate = None # object | A JSON-encoded string that contains the details of the certificate.  **Note:**  To request multiple certificates, duplicate or increment the parameter name. For example, to request three certificates, use the `certificate` parameter multiple times or use the `certificate-1`, `certificate-2`, and `certificate-3` parameters.
    provider = 'cPStore' # str | The cPanel Market provider's name.
    identity_verification = None # object | An object containing the required information for an EV or OV certificate. This information depends on the provider of the certificate.  **Note:**  The function returns this object for OV or EV certificate requests. (optional)
    url_after_checkout = 'http://checkout.example.com' # str | The URL to send the browser after the user checks out.  **Note:**  This URL does **not** contain a query string. (optional)

    try:
        # Request SSL certificate order
        api_response = api_instance.request_ssl_certificates(access_token, certificate, provider, identity_verification=identity_verification, url_after_checkout=url_after_checkout)
        print("The response of MarketApi->request_ssl_certificates:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketApi->request_ssl_certificates: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_token** | **str**| The access token for the session to the cPanel Market provider. | 
 **certificate** | [**object**](.md)| A JSON-encoded string that contains the details of the certificate.  **Note:**  To request multiple certificates, duplicate or increment the parameter name. For example, to request three certificates, use the &#x60;certificate&#x60; parameter multiple times or use the &#x60;certificate-1&#x60;, &#x60;certificate-2&#x60;, and &#x60;certificate-3&#x60; parameters. | 
 **provider** | **str**| The cPanel Market provider&#39;s name. | 
 **identity_verification** | [**object**](.md)| An object containing the required information for an EV or OV certificate. This information depends on the provider of the certificate.  **Note:**  The function returns this object for OV or EV certificate requests. | [optional] 
 **url_after_checkout** | **str**| The URL to send the browser after the user checks out.  **Note:**  This URL does **not** contain a query string. | [optional] 

### Return type

[**InlineResponse200312**](InlineResponse200312.md)

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

# **set_status_of_pending_queue_items**
> InlineResponse200313 set_status_of_pending_queue_items(order_item_id, provider, status)

Update status of items in pending queue

This function sets the status of an item or items in the cPanel Market pending queue.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200313 import InlineResponse200313
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
    api_instance = clientapi_cpanel.MarketApi(api_client)
    order_item_id = 'order_item_id-1=12345&order_item_id-2=12346&order_item_id-3=12347' # str | The ID of the ordered item.  **Note:**  To set the status for multiple items, duplicate or increment the parameter name. For example, to change the status for three certificates, use the `order_item_id` parameter multiple times or use the `order_item_id-1`, `order_item_id-2`, and `order_item_id-3` parameters.
    provider = 'cPStore' # str | The cPanel Market provider's name.
    status = 'confirmed' # str | The new status of the item in the cPanel Market pending queue.  * `confirmed` — The system confirmed payment for the item with the provider.

    try:
        # Update status of items in pending queue
        api_response = api_instance.set_status_of_pending_queue_items(order_item_id, provider, status)
        print("The response of MarketApi->set_status_of_pending_queue_items:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketApi->set_status_of_pending_queue_items: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_item_id** | **str**| The ID of the ordered item.  **Note:**  To set the status for multiple items, duplicate or increment the parameter name. For example, to change the status for three certificates, use the &#x60;order_item_id&#x60; parameter multiple times or use the &#x60;order_item_id-1&#x60;, &#x60;order_item_id-2&#x60;, and &#x60;order_item_id-3&#x60; parameters. | 
 **provider** | **str**| The cPanel Market provider&#39;s name. | 
 **status** | **str**| The new status of the item in the cPanel Market pending queue.  * &#x60;confirmed&#x60; — The system confirmed payment for the item with the provider. | 

### Return type

[**InlineResponse200313**](InlineResponse200313.md)

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

# **set_url_after_checkout**
> InlineResponse200314 set_url_after_checkout(access_token, order_id, provider, url_after_checkout)

Update URL after checkout

This function updates the URL to which a provider sends a user after they check out.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200314 import InlineResponse200314
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
    api_instance = clientapi_cpanel.MarketApi(api_client)
    access_token = '725431a1-d5bc-11e5-a28b-8b0e09a93f05' # str | The access token for the session to the cPanel Market provider.
    order_id = 123456 # int | The order ID that the cPanel Market provider assigned.
    provider = 'cPStore' # str | The cPanel Market provider's name.
    url_after_checkout = 'http://checkout.example.com' # str | The URL to send the browser after the user checks out.

    try:
        # Update URL after checkout
        api_response = api_instance.set_url_after_checkout(access_token, order_id, provider, url_after_checkout)
        print("The response of MarketApi->set_url_after_checkout:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketApi->set_url_after_checkout: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_token** | **str**| The access token for the session to the cPanel Market provider. | 
 **order_id** | **int**| The order ID that the cPanel Market provider assigned. | 
 **provider** | **str**| The cPanel Market provider&#39;s name. | 
 **url_after_checkout** | **str**| The URL to send the browser after the user checks out. | 

### Return type

[**InlineResponse200314**](InlineResponse200314.md)

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

# **validate_login_token**
> InlineResponse200315 validate_login_token(login_token, provider, url_after_login)

Validate login token

This function validates a login token to a cPanel Market provider and returns an access token.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200315 import InlineResponse200315
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
    api_instance = clientapi_cpanel.MarketApi(api_client)
    login_token = '8675309' # str | The login token for the cPanel Market provider.
    provider = 'cPStore' # str | The name of the cPanel Market provider.
    url_after_login = 'http://hostname.example.com/redirectionlocation.cgi?state' # str | The `url_after_login` value that you sent to UAPI's `Market::get_login_url` function.

    try:
        # Validate login token
        api_response = api_instance.validate_login_token(login_token, provider, url_after_login)
        print("The response of MarketApi->validate_login_token:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketApi->validate_login_token: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **login_token** | **str**| The login token for the cPanel Market provider. | 
 **provider** | **str**| The name of the cPanel Market provider. | 
 **url_after_login** | **str**| The &#x60;url_after_login&#x60; value that you sent to UAPI&#39;s &#x60;Market::get_login_url&#x60; function. | 

### Return type

[**InlineResponse200315**](InlineResponse200315.md)

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

