# clientapi_cpanel.MarketIntegrationApi

All URIs are relative to *https://cpanel-server.tld:2083/execute*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_shopping_cart**](MarketIntegrationApi.md#create_shopping_cart) | **GET** /Market/create_shopping_cart | Create shopping cart
[**get_login_url**](MarketIntegrationApi.md#get_login_url) | **GET** /Market/get_login_url | Return provider&#39;s login URL
[**market_get_all_products**](MarketIntegrationApi.md#market_get_all_products) | **GET** /Market/get_all_products | Return provider&#39;s available products
[**market_get_providers_list**](MarketIntegrationApi.md#market_get_providers_list) | **GET** /Market/get_providers_list | Return enabled providers
[**set_status_of_pending_queue_items**](MarketIntegrationApi.md#set_status_of_pending_queue_items) | **GET** /Market/set_status_of_pending_queue_items | Update status of items in pending queue
[**set_url_after_checkout**](MarketIntegrationApi.md#set_url_after_checkout) | **GET** /Market/set_url_after_checkout | Update URL after checkout
[**validate_login_token**](MarketIntegrationApi.md#validate_login_token) | **GET** /Market/validate_login_token | Validate login token


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
    api_instance = clientapi_cpanel.MarketIntegrationApi(api_client)
    access_token = '1a676e6f-99fc-11e6-9ab6-e60a769b73bc' # str | The access token to connect to the provider.
    item = ['[\"{\\\"product_id\\\":123456,\\\"provider-specfic-key\\\":\\\"provider-specfic-value\\\",\\\"another-provider-specfic-key\\\":\\\"another-provider-specfic-value\\\"}\",\"{\\\"product_id\\\":123457,\\\"provider-specfic-key\\\":\\\"provider-specfic-value\\\",\\\"another-provider-specfic-key\\\":\\\"another-provider-specfic-value\\\"}\"]'] # List[str] | The items to add to the shopping cart.  **Note**:    The value is a JSON string.    This object has one required key, `product_id`, which is a string.    The other keys/values in this object vary depending on the provider.
    provider = 'cPStore' # str | The cPanel Market provider’s name.
    url_after_checkout = 'http://www.example.com/thenextplace' # str | The location to which the provider directs the user after the checkout process is complete.

    try:
        # Create shopping cart
        api_response = api_instance.create_shopping_cart(access_token, item, provider, url_after_checkout)
        print("The response of MarketIntegrationApi->create_shopping_cart:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketIntegrationApi->create_shopping_cart: %s\n" % e)
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
    api_instance = clientapi_cpanel.MarketIntegrationApi(api_client)
    provider = 'cPStore' # str | The cPanel Market provider's name.
    url_after_login = 'http://hostname.example.com/redirectionlocation.cgi?state' # str | Where the cPanel Market provider redirects the user's browser after they log in.

    try:
        # Return provider's login URL
        api_response = api_instance.get_login_url(provider, url_after_login)
        print("The response of MarketIntegrationApi->get_login_url:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketIntegrationApi->get_login_url: %s\n" % e)
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
    api_instance = clientapi_cpanel.MarketIntegrationApi(api_client)

    try:
        # Return provider's available products
        api_response = api_instance.market_get_all_products()
        print("The response of MarketIntegrationApi->market_get_all_products:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketIntegrationApi->market_get_all_products: %s\n" % e)
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
    api_instance = clientapi_cpanel.MarketIntegrationApi(api_client)

    try:
        # Return enabled providers
        api_response = api_instance.market_get_providers_list()
        print("The response of MarketIntegrationApi->market_get_providers_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketIntegrationApi->market_get_providers_list: %s\n" % e)
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
    api_instance = clientapi_cpanel.MarketIntegrationApi(api_client)
    order_item_id = 'order_item_id-1=12345&order_item_id-2=12346&order_item_id-3=12347' # str | The ID of the ordered item.  **Note:**  To set the status for multiple items, duplicate or increment the parameter name. For example, to change the status for three certificates, use the `order_item_id` parameter multiple times or use the `order_item_id-1`, `order_item_id-2`, and `order_item_id-3` parameters.
    provider = 'cPStore' # str | The cPanel Market provider's name.
    status = 'confirmed' # str | The new status of the item in the cPanel Market pending queue.  * `confirmed` — The system confirmed payment for the item with the provider.

    try:
        # Update status of items in pending queue
        api_response = api_instance.set_status_of_pending_queue_items(order_item_id, provider, status)
        print("The response of MarketIntegrationApi->set_status_of_pending_queue_items:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketIntegrationApi->set_status_of_pending_queue_items: %s\n" % e)
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
    api_instance = clientapi_cpanel.MarketIntegrationApi(api_client)
    access_token = '725431a1-d5bc-11e5-a28b-8b0e09a93f05' # str | The access token for the session to the cPanel Market provider.
    order_id = 123456 # int | The order ID that the cPanel Market provider assigned.
    provider = 'cPStore' # str | The cPanel Market provider's name.
    url_after_checkout = 'http://checkout.example.com' # str | The URL to send the browser after the user checks out.

    try:
        # Update URL after checkout
        api_response = api_instance.set_url_after_checkout(access_token, order_id, provider, url_after_checkout)
        print("The response of MarketIntegrationApi->set_url_after_checkout:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketIntegrationApi->set_url_after_checkout: %s\n" % e)
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
    api_instance = clientapi_cpanel.MarketIntegrationApi(api_client)
    login_token = '8675309' # str | The login token for the cPanel Market provider.
    provider = 'cPStore' # str | The name of the cPanel Market provider.
    url_after_login = 'http://hostname.example.com/redirectionlocation.cgi?state' # str | The `url_after_login` value that you sent to UAPI's `Market::get_login_url` function.

    try:
        # Validate login token
        api_response = api_instance.validate_login_token(login_token, provider, url_after_login)
        print("The response of MarketIntegrationApi->validate_login_token:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketIntegrationApi->validate_login_token: %s\n" % e)
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

