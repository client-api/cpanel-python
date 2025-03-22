# clientapi_cpanel.SSLCertificatesApi

All URIs are relative to *https://cpanel-server.tld:2083/execute*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancel_pending_ssl_certificate**](SSLCertificatesApi.md#cancel_pending_ssl_certificate) | **GET** /Market/cancel_pending_ssl_certificate | Delete an order
[**get_certificate_status_details**](SSLCertificatesApi.md#get_certificate_status_details) | **GET** /Market/get_certificate_status_details | Return provider&#39;s SSL certificate request status
[**get_pending_ssl_certificates**](SSLCertificatesApi.md#get_pending_ssl_certificates) | **GET** /Market/get_pending_ssl_certificates | Return provider&#39;s pending SSL certificates
[**get_ssl_certificate_if_available**](SSLCertificatesApi.md#get_ssl_certificate_if_available) | **GET** /Market/get_ssl_certificate_if_available | Return provider&#39;s available SSL certificates
[**market_get_provider_specific_dcv_constraints**](SSLCertificatesApi.md#market_get_provider_specific_dcv_constraints) | **GET** /Market/get_provider_specific_dcv_constraints | Return provider&#39;s DCV filename requirements
[**process_ssl_pending_queue**](SSLCertificatesApi.md#process_ssl_pending_queue) | **GET** /Market/process_ssl_pending_queue | Start processing pending queue&#39;s SSL certificates
[**request_ssl_certificates**](SSLCertificatesApi.md#request_ssl_certificates) | **GET** /Market/request_ssl_certificates | Request SSL certificate order


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
    api_instance = clientapi_cpanel.SSLCertificatesApi(api_client)
    order_item_id = '10427508' # str | The ID of the ordered item to cancel.
    provider = 'cPStore' # str | The cPanel Market provider's name.

    try:
        # Delete an order
        api_response = api_instance.cancel_pending_ssl_certificate(order_item_id, provider)
        print("The response of SSLCertificatesApi->cancel_pending_ssl_certificate:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SSLCertificatesApi->cancel_pending_ssl_certificate: %s\n" % e)
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
    api_instance = clientapi_cpanel.SSLCertificatesApi(api_client)
    order_item_id = 1234567890 # int | The order ID that the cPanel Market provider assigned.
    provider = 'cPStore' # str | The cPanel Market provider's name.

    try:
        # Return provider's SSL certificate request status
        api_response = api_instance.get_certificate_status_details(order_item_id, provider)
        print("The response of SSLCertificatesApi->get_certificate_status_details:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SSLCertificatesApi->get_certificate_status_details: %s\n" % e)
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
    api_instance = clientapi_cpanel.SSLCertificatesApi(api_client)
    provider = 'cPStore' # str | The cPanel Market provider's name.

    try:
        # Return provider's pending SSL certificates
        api_response = api_instance.get_pending_ssl_certificates(provider)
        print("The response of SSLCertificatesApi->get_pending_ssl_certificates:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SSLCertificatesApi->get_pending_ssl_certificates: %s\n" % e)
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
    api_instance = clientapi_cpanel.SSLCertificatesApi(api_client)
    order_item_id = '8675309' # str | The order item for which to poll.
    provider = 'cPStore' # str | The cPanel Market provider's name.

    try:
        # Return provider's available SSL certificates
        api_response = api_instance.get_ssl_certificate_if_available(order_item_id, provider)
        print("The response of SSLCertificatesApi->get_ssl_certificate_if_available:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SSLCertificatesApi->get_ssl_certificate_if_available: %s\n" % e)
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
    api_instance = clientapi_cpanel.SSLCertificatesApi(api_client)
    provider = 'cPStore' # str | The cPanel Market provider's name.

    try:
        # Return provider's DCV filename requirements
        api_response = api_instance.market_get_provider_specific_dcv_constraints(provider)
        print("The response of SSLCertificatesApi->market_get_provider_specific_dcv_constraints:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SSLCertificatesApi->market_get_provider_specific_dcv_constraints: %s\n" % e)
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
    api_instance = clientapi_cpanel.SSLCertificatesApi(api_client)

    try:
        # Start processing pending queue's SSL certificates
        api_response = api_instance.process_ssl_pending_queue()
        print("The response of SSLCertificatesApi->process_ssl_pending_queue:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SSLCertificatesApi->process_ssl_pending_queue: %s\n" % e)
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
    api_instance = clientapi_cpanel.SSLCertificatesApi(api_client)
    access_token = '725431a1-d5bc-11e5-a28b-8b0e09a93f05' # str | The access token for the session to the cPanel Market provider.
    certificate = None # object | A JSON-encoded string that contains the details of the certificate.  **Note:**  To request multiple certificates, duplicate or increment the parameter name. For example, to request three certificates, use the `certificate` parameter multiple times or use the `certificate-1`, `certificate-2`, and `certificate-3` parameters.
    provider = 'cPStore' # str | The cPanel Market provider's name.
    identity_verification = None # object | An object containing the required information for an EV or OV certificate. This information depends on the provider of the certificate.  **Note:**  The function returns this object for OV or EV certificate requests. (optional)
    url_after_checkout = 'http://checkout.example.com' # str | The URL to send the browser after the user checks out.  **Note:**  This URL does **not** contain a query string. (optional)

    try:
        # Request SSL certificate order
        api_response = api_instance.request_ssl_certificates(access_token, certificate, provider, identity_verification=identity_verification, url_after_checkout=url_after_checkout)
        print("The response of SSLCertificatesApi->request_ssl_certificates:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SSLCertificatesApi->request_ssl_certificates: %s\n" % e)
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

