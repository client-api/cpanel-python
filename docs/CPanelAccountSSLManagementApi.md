# clientapi_cpanel.CPanelAccountSSLManagementApi

All URIs are relative to *https://cpanel-server.tld:2083/execute*

Method | HTTP request | Description
------------- | ------------- | -------------
[**can_ssl_redirect**](CPanelAccountSSLManagementApi.md#can_ssl_redirect) | **GET** /SSL/can_ssl_redirect | Return whether domains can redirect to secure URL
[**check_shared_cert**](CPanelAccountSSLManagementApi.md#check_shared_cert) | **GET** /SSL/check_shared_cert | Return whether shared SSL certificate exists
[**delete_ssl**](CPanelAccountSSLManagementApi.md#delete_ssl) | **GET** /SSL/delete_ssl | Remove SSL for domain
[**fetch_best_for_domain**](CPanelAccountSSLManagementApi.md#fetch_best_for_domain) | **GET** /SSL/fetch_best_for_domain | Request best SSL certificate
[**fetch_cert_info**](CPanelAccountSSLManagementApi.md#fetch_cert_info) | **GET** /SSL/fetch_cert_info | Return SSL certificate information
[**fetch_certificates_for_fqdns**](CPanelAccountSSLManagementApi.md#fetch_certificates_for_fqdns) | **GET** /SSL/fetch_certificates_for_fqdns | Return SSL certificate information for all FQDN
[**fetch_key_and_cabundle_for_certificate**](CPanelAccountSSLManagementApi.md#fetch_key_and_cabundle_for_certificate) | **POST** /SSL/fetch_key_and_cabundle_for_certificate | Return private key and CA bundle
[**find_certificates_for_key**](CPanelAccountSSLManagementApi.md#find_certificates_for_key) | **GET** /SSL/find_certificates_for_key | Return SSL certificate for private key
[**find_csrs_for_key**](CPanelAccountSSLManagementApi.md#find_csrs_for_key) | **GET** /SSL/find_csrs_for_key | Return private key&#39;s certificate signing requests
[**get_cabundle**](CPanelAccountSSLManagementApi.md#get_cabundle) | **GET** /SSL/get_cabundle | Return certificate&#39;s CA bundle and hostname
[**get_cn_name**](CPanelAccountSSLManagementApi.md#get_cn_name) | **GET** /SSL/get_cn_name | Request best SSL domain for service
[**installed_host**](CPanelAccountSSLManagementApi.md#installed_host) | **GET** /SSL/installed_host | Return SSL certificate&#39;s info for dedicated IP
[**installed_hosts**](CPanelAccountSSLManagementApi.md#installed_hosts) | **GET** /SSL/installed_hosts | Return domains with SSL certificate information
[**list_certs**](CPanelAccountSSLManagementApi.md#list_certs) | **GET** /SSL/list_certs | Return all SSL certificates
[**list_csrs**](CPanelAccountSSLManagementApi.md#list_csrs) | **GET** /SSL/list_csrs | Return all certificate signing requests
[**list_keys**](CPanelAccountSSLManagementApi.md#list_keys) | **GET** /SSL/list_keys | Return all private keys
[**list_ssl_items**](CPanelAccountSSLManagementApi.md#list_ssl_items) | **GET** /SSL/list_ssl_items | Return SSL-related items
[**rebuildssldb**](CPanelAccountSSLManagementApi.md#rebuildssldb) | **GET** /SSL/rebuildssldb | Start SSL database rebuild
[**s_sl_set_default_key_type**](CPanelAccountSSLManagementApi.md#s_sl_set_default_key_type) | **GET** /SSL/set_default_key_type | Update SSL TLS key type
[**toggle_ssl_redirect_for_domains**](CPanelAccountSSLManagementApi.md#toggle_ssl_redirect_for_domains) | **GET** /SSL/toggle_ssl_redirect_for_domains | Enable or disable secure redirects


# **can_ssl_redirect**
> InlineResponse200403 can_ssl_redirect()

Return whether domains can redirect to secure URL

This function determines whether the system can automatically redirect domains on a cPanel account to use SSL.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200403 import InlineResponse200403
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
    api_instance = clientapi_cpanel.CPanelAccountSSLManagementApi(api_client)

    try:
        # Return whether domains can redirect to secure URL
        api_response = api_instance.can_ssl_redirect()
        print("The response of CPanelAccountSSLManagementApi->can_ssl_redirect:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CPanelAccountSSLManagementApi->can_ssl_redirect: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**InlineResponse200403**](InlineResponse200403.md)

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

# **check_shared_cert**
> InlineResponse200404 check_shared_cert()

Return whether shared SSL certificate exists

This function checks whether a shared SSL certificate is associated with the account.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200404 import InlineResponse200404
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
    api_instance = clientapi_cpanel.CPanelAccountSSLManagementApi(api_client)

    try:
        # Return whether shared SSL certificate exists
        api_response = api_instance.check_shared_cert()
        print("The response of CPanelAccountSSLManagementApi->check_shared_cert:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CPanelAccountSSLManagementApi->check_shared_cert: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**InlineResponse200404**](InlineResponse200404.md)

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

# **delete_ssl**
> InlineResponse200408 delete_ssl(domain)

Remove SSL for domain

This function removes SSL from a domain.

**Note:**

This function removes domains from the current certificate to end SSL coverage for those
domains. To delete certificates from SSL storage, use the UAPI function `SSL::delete_cert`
instead.

**Important:**

When you disable the Calendars and Contacts, Receive Mail, Web Disk, Webmail, **and** Web Server
[roles](https://go.cpanel.net/serverroles), the system **disables** this function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200408 import InlineResponse200408
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
    api_instance = clientapi_cpanel.CPanelAccountSSLManagementApi(api_client)
    domain = 'example.com' # str | The domain name.

    try:
        # Remove SSL for domain
        api_response = api_instance.delete_ssl(domain)
        print("The response of CPanelAccountSSLManagementApi->delete_ssl:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CPanelAccountSSLManagementApi->delete_ssl: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**| The domain name. | 

### Return type

[**InlineResponse200408**](InlineResponse200408.md)

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

# **fetch_best_for_domain**
> InlineResponse200411 fetch_best_for_domain(domain)

Request best SSL certificate

This function retrieves the best-available certificate for the domain. The function also
retrieves the certificate's associated private key and CA bundle, if available.

**Important:**

When you disable the [Calendars and Contacts, Receive Mail, Web Disk, Webmail, and Web Server roles](https://go.cpanel.net/serverroles), the system **disables** this function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200411 import InlineResponse200411
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
    api_instance = clientapi_cpanel.CPanelAccountSSLManagementApi(api_client)
    domain = 'example.com' # str | The domain name.

    try:
        # Request best SSL certificate
        api_response = api_instance.fetch_best_for_domain(domain)
        print("The response of CPanelAccountSSLManagementApi->fetch_best_for_domain:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CPanelAccountSSLManagementApi->fetch_best_for_domain: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**| The domain name. | 

### Return type

[**InlineResponse200411**](InlineResponse200411.md)

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

# **fetch_cert_info**
> InlineResponse200412 fetch_cert_info(friendly_name, id)

Return SSL certificate information

This function retrieves all of a certificate's available information.

**Important:**

* You **must** call either the `friendly_name` or `id` parameter.
* When you disable the Calendars and Contacts, Receive Mail, Web Disk, Webmail, and Web Server [roles](https://go.cpanel.net/serverroles), the system **disables** this function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200412 import InlineResponse200412
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
    api_instance = clientapi_cpanel.CPanelAccountSSLManagementApi(api_client)
    friendly_name = 'TestCert' # str | The certificate's human readable name.
    id = 'example_com_cb497_a394d_1397249671_d1272da8f13a1fd837493a5ad1f0a0f3' # str | The certificate's ID.

    try:
        # Return SSL certificate information
        api_response = api_instance.fetch_cert_info(friendly_name, id)
        print("The response of CPanelAccountSSLManagementApi->fetch_cert_info:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CPanelAccountSSLManagementApi->fetch_cert_info: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **friendly_name** | **str**| The certificate&#39;s human readable name. | 
 **id** | **str**| The certificate&#39;s ID. | 

### Return type

[**InlineResponse200412**](InlineResponse200412.md)

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

# **fetch_certificates_for_fqdns**
> InlineResponse200413 fetch_certificates_for_fqdns(domains)

Return SSL certificate information for all FQDN

This function retrieves the certificate information for all fully qualified domain names (FQDNs) that the account owns.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200413 import InlineResponse200413
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
    api_instance = clientapi_cpanel.CPanelAccountSSLManagementApi(api_client)
    domains = 'domains=example1.com,example2.com' # str | A domain or comma-delimited list of domains for which to retrieve information.

    try:
        # Return SSL certificate information for all FQDN
        api_response = api_instance.fetch_certificates_for_fqdns(domains)
        print("The response of CPanelAccountSSLManagementApi->fetch_certificates_for_fqdns:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CPanelAccountSSLManagementApi->fetch_certificates_for_fqdns: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domains** | **str**| A domain or comma-delimited list of domains for which to retrieve information. | 

### Return type

[**InlineResponse200413**](InlineResponse200413.md)

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

# **fetch_key_and_cabundle_for_certificate**
> InlineResponse200414 fetch_key_and_cabundle_for_certificate(certificate, certificate2=certificate2)

Return private key and CA bundle

This function extracts the private key and CA bundle information from a certificate.

**Note:**

Due to the limited field length of `HTTP GET` method calls, you **must** use the `HTTP POST` method. For this reason, you **cannot** use a cPanel or Webmail session URL to call this function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200414 import InlineResponse200414
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
    api_instance = clientapi_cpanel.CPanelAccountSSLManagementApi(api_client)
    certificate = '-----BEGIN CERTIFICATE-----MIIDcTCCAlmgAwIBAgIFAU+BNVgwDQYJKoZIhvcNAQEFBQAwUTESMBAGA1UEAwwJc2lza28udGxkMQswCQYDVQQGEwJVUzEPMA0GA1UECgwGY1BhbmVsMQswCQYDVQQIDAJUWDEQMA4GA1UEBwwHSG91c3RvbjAeFw0xNDEwMDYyMjI2MTlaFw0xNTEwMDYyMjI2MTlaMFExEjAQBgNVBAMMCXNpc2tvLnRsZDELMAkGA1UEBhMCVVMxDzANBgNVBAoMBmNQYW5lbDELMAkGA1UECAwCVFgxEDAOBgNVBAcMB0hvdXN0b24wggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAwggEKAoIBAQC9zx6zGiHdmWA0dKtoXmJiWXpZ9E3PXx3YHsjFEWW7e5pH0vZ+jVMzDmm5nsJ7RXrAkZO1IvpIpVLvoQfiJOWVvkD+o9fWvoK1tWJS72FSgPju+58mA2ieBuc87A790Pzuv1P3NR3zFLAjUR99zkHR1fpri/daM3PBWO8ET48FWkyU1kOeZaUlF67/+wrEiNgg+t1qhKOCAB61PdNVkLaSGHimksuC+Czk8Kq9nuS0E0TCnDtjjEyJ455FUcaCfczlTb8xkB/F9ORe74yTzD+vlk0tFMG6PLj/ajIwWqwO0qmQ8wX3NRxkWgGz5kVO1wrVJarKQ5EYQ3/mgvit0v6dAgMBAAGjUDBOMB0GA1UdDgQWBBRw+wKBo34+bgexjAa3EMDsgSCd7zAfBgNVHSMEGDAWgBRw+wKBo34+bgexjAa3EMDsgSCd7zAMBgNVHRMEBTADAQH/MA0GCSqGSIb3DQEBBQUAA4IBAQCHRXIs53opzKM2rM8Qe8lcw524WK6hqy2EWrZHp78N7rU7/6DQ/I3hv3WhcDDIO04I2/Xhe88MLBaLoM367Ya+vy7CaLr14aLi/SfQszMA0ALBvMao+Fis0iVwFYq/NLgSXw+fgnpFskt8v8iQZ+4Kaal8U8e9sVgu8m0RgO7rzym1eRiIKpsKd1rh/SD7LbSN7M7TRL3QqF7ltw9sQhAAsQcRaBBF21pdWrqhiGZ+Eioo3hhgwNavH2agqz78ddHwrFpHFwrEeUk1OfpPb76MYIce7xIy/4oQNdg6fOq4l/FrajBv+WkzDVPaKm6r7YmwfLN/YMZBHXSR58oOGP9W-----END CERTIFICATE-----' # str | An SSL certificate.
    certificate2 = 'certificate_example' # str | The certificate file. (optional)

    try:
        # Return private key and CA bundle
        api_response = api_instance.fetch_key_and_cabundle_for_certificate(certificate, certificate2=certificate2)
        print("The response of CPanelAccountSSLManagementApi->fetch_key_and_cabundle_for_certificate:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CPanelAccountSSLManagementApi->fetch_key_and_cabundle_for_certificate: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **certificate** | **str**| An SSL certificate. | 
 **certificate2** | **str**| The certificate file. | [optional] 

### Return type

[**InlineResponse200414**](InlineResponse200414.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | HTTP Request was successful. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_certificates_for_key**
> InlineResponse200415 find_certificates_for_key(friendly_name=friendly_name, id=id)

Return SSL certificate for private key

This function retrieves SSL certificates for a private key.

**Note:**

When you call this function, you **must** include either the `id`
**or** the `friendly_name` parameter.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200415 import InlineResponse200415
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
    api_instance = clientapi_cpanel.CPanelAccountSSLManagementApi(api_client)
    friendly_name = 'TestKey' # str | The key's friendly name. (optional)
    id = 'example_com_cb497_a394d_1397249671_d1272da8f13a1fd837493a5ad1f0a0f3' # str | The key's ID. (optional)

    try:
        # Return SSL certificate for private key
        api_response = api_instance.find_certificates_for_key(friendly_name=friendly_name, id=id)
        print("The response of CPanelAccountSSLManagementApi->find_certificates_for_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CPanelAccountSSLManagementApi->find_certificates_for_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **friendly_name** | **str**| The key&#39;s friendly name. | [optional] 
 **id** | **str**| The key&#39;s ID. | [optional] 

### Return type

[**InlineResponse200415**](InlineResponse200415.md)

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

# **find_csrs_for_key**
> InlineResponse200416 find_csrs_for_key(friendly_name=friendly_name, id=id)

Return private key's certificate signing requests

This function retrieves certificate signing requests (CSR) for
a private key.

**Note:**

When you call this function, you **must** include either the `id`
or the `friendly_name` parameter.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200416 import InlineResponse200416
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
    api_instance = clientapi_cpanel.CPanelAccountSSLManagementApi(api_client)
    friendly_name = 'TestKey' # str | The key's friendly name. (optional)
    id = 'example_com_cb497_a394d_1397249671_d1272da8f13a1fd837493a5ad1f0a0f3' # str | The key's ID. (optional)

    try:
        # Return private key's certificate signing requests
        api_response = api_instance.find_csrs_for_key(friendly_name=friendly_name, id=id)
        print("The response of CPanelAccountSSLManagementApi->find_csrs_for_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CPanelAccountSSLManagementApi->find_csrs_for_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **friendly_name** | **str**| The key&#39;s friendly name. | [optional] 
 **id** | **str**| The key&#39;s ID. | [optional] 

### Return type

[**InlineResponse200416**](InlineResponse200416.md)

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

# **get_cabundle**
> InlineResponse200422 get_cabundle(cert)

Return certificate's CA bundle and hostname

This function retrieves a certificate's Certificate Authority (CA) bundle and hostname.

**Important:**

When you disable the Calendars and Contacts, Receive Mail, Web Disk, Webmail, and Web Server [roles](https://go.cpanel.net/serverroles), the system **disables** this function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200422 import InlineResponse200422
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
    api_instance = clientapi_cpanel.CPanelAccountSSLManagementApi(api_client)
    cert = '-----BEGIN CERTIFICATE-----\\r\\nMIIDcTCCAlmgAwIBAgIFAU+BNVgwDQYJKoZIhvcNAQEFBQAwUTESMBAGA1UEAwwJ\\r\\nc2lza28udGxkMQswCQYDVQQGEwJVUzEPMA0GA1UECgwGY1BhbmVsMQswCQYDVQQI\\r\\nDAJUWDEQMA4GA1UEBwwHSG91c3RvbjAeFw0xNDEwMDYyMjI2MTlaFw0xNTEwMDYy\\r\\nMjI2MTlaMFExEjAQBgNVBAMMCXNpc2tvLnRsZDELMAkGA1UEBhMCVVMxDzANBgNV\\r\\nBAoMBmNQYW5lbDELMAkGA1UECAwCVFgxEDAOBgNVBAcMB0hvdXN0b24wggEiMA0G\\r\\nCSqGSIb3DQEBAQUAA4IBDwAwggEKAoIBAQC9zx6zGiHdmWA0dKtoXmJiWXpZ9E3P\\r\\nXx3YHsjFEWW7e5pH0vZ+jVMzDmm5nsJ7RXrAkZO1IvpIpVLvoQfiJOWVvkD+o9fW\\r\\nvoK1tWJS72FSgPju+58mA2ieBuc87A790Pzuv1P3NR3zFLAjUR99zkHR1fpri/da\\r\\nM3PBWO8ET48FWkyU1kOeZaUlF67/+wrEiNgg+t1qhKOCAB61PdNVkLaSGHimksuC\\r\\n+Czk8Kq9nuS0E0TCnDtjjEyJ455FUcaCfczlTb8xkB/F9ORe74yTzD+vlk0tFMG6\\r\\nPLj/ajIwWqwO0qmQ8wX3NRxkWgGz5kVO1wrVJarKQ5EYQ3/mgvit0v6dAgMBAAGj\\r\\nUDBOMB0GA1UdDgQWBBRw+wKBo34+bgexjAa3EMDsgSCd7zAfBgNVHSMEGDAWgBRw\\r\\n+wKBo34+bgexjAa3EMDsgSCd7zAMBgNVHRMEBTADAQH/MA0GCSqGSIb3DQEBBQUA\\r\\nA4IBAQCHRXIs53opzKM2rM8Qe8lcw524WK6hqy2EWrZHp78N7rU7/6DQ/I3hv3Wh\\r\\ncDDIO04I2/Xhe88MLBaLoM367Ya+vy7CaLr14aLi/SfQszMA0ALBvMao+Fis0iVw\\r\\nFYq/NLgSXw+fgnpFskt8v8iQZ+4Kaal8U8e9sVgu8m0RgO7rzym1eRiIKpsKd1rh\\r\\n/SD7LbSN7M7TRL3QqF7ltw9sQhAAsQcRaBBF21pdWrqhiGZ+Eioo3hhgwNavH2ag\\r\\nqz78ddHwrFpHFwrEeUk1OfpPb76MYIce7xIy/4oQNdg6fOq4l/FrajBv+WkzDVPa\\r\\nKm6r7YmwfLN/YMZBHXSR58oOGP9W\\r\\n-----END CERTIFICATE-----' # str | The certificate's text.

    try:
        # Return certificate's CA bundle and hostname
        api_response = api_instance.get_cabundle(cert)
        print("The response of CPanelAccountSSLManagementApi->get_cabundle:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CPanelAccountSSLManagementApi->get_cabundle: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cert** | **str**| The certificate&#39;s text. | 

### Return type

[**InlineResponse200422**](InlineResponse200422.md)

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

# **get_cn_name**
> InlineResponse200423 get_cn_name(domain, service, add_mail_subdomain=add_mail_subdomain)

Request best SSL domain for service

This function retrieves the most secure domain for a service.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200423 import InlineResponse200423
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
    api_instance = clientapi_cpanel.CPanelAccountSSLManagementApi(api_client)
    domain = clientapi_cpanel.Domain() # Domain | A domain name, cPanel username, or email address.
    service = 'cpanel' # str | The service's name.  * `cpanel` * `imap` * `pop3` * `smtp`
    add_mail_subdomain = 0 # int | Whether to append `mail` to the `domain` value to find the best match.  For example, if you specify the domain `example.com` and call this parameter, the function only searches the `mail.example.com` service domains.  * `1` — Append `mail` to the `domain` value during the search. * `0` — Match on the specified `domain` value **only**. (optional) (default to 0)

    try:
        # Request best SSL domain for service
        api_response = api_instance.get_cn_name(domain, service, add_mail_subdomain=add_mail_subdomain)
        print("The response of CPanelAccountSSLManagementApi->get_cn_name:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CPanelAccountSSLManagementApi->get_cn_name: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | [**Domain**](.md)| A domain name, cPanel username, or email address. | 
 **service** | **str**| The service&#39;s name.  * &#x60;cpanel&#x60; * &#x60;imap&#x60; * &#x60;pop3&#x60; * &#x60;smtp&#x60; | 
 **add_mail_subdomain** | **int**| Whether to append &#x60;mail&#x60; to the &#x60;domain&#x60; value to find the best match.  For example, if you specify the domain &#x60;example.com&#x60; and call this parameter, the function only searches the &#x60;mail.example.com&#x60; service domains.  * &#x60;1&#x60; — Append &#x60;mail&#x60; to the &#x60;domain&#x60; value during the search. * &#x60;0&#x60; — Match on the specified &#x60;domain&#x60; value **only**. | [optional] [default to 0]

### Return type

[**InlineResponse200423**](InlineResponse200423.md)

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

# **installed_host**
> InlineResponse200425 installed_host(domain=domain, verify_certificate=verify_certificate)

Return SSL certificate's info for dedicated IP

This function retrieves information about a certificate that is installed on a domain's dedicated IP address.

**Important:**

  * If you do **not** possess a dedicated IP address, this function will **fail**. For non-dedicated IP addresses, use the `SSL::installed_hosts` function.
  * When you disable the _Calendars and Contacts_, _Receive Mail_, _Web Disk_ , _Webmail_ , **and**  _Web Server_ [roles](https://go.cpanel.net/howtouseserverprofiles#roles), the system **disables** this function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200425 import InlineResponse200425
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
    api_instance = clientapi_cpanel.CPanelAccountSSLManagementApi(api_client)
    domain = 'example.com' # str | The domain name.  **Note:**  The parameter defaults to the account's main domain. (optional)
    verify_certificate = 0 # int | Verify the certificate. * `1` — Verify the certificate. * `0` — Do **not** verify the certificate. (optional) (default to 0)

    try:
        # Return SSL certificate's info for dedicated IP
        api_response = api_instance.installed_host(domain=domain, verify_certificate=verify_certificate)
        print("The response of CPanelAccountSSLManagementApi->installed_host:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CPanelAccountSSLManagementApi->installed_host: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**| The domain name.  **Note:**  The parameter defaults to the account&#39;s main domain. | [optional] 
 **verify_certificate** | **int**| Verify the certificate. * &#x60;1&#x60; — Verify the certificate. * &#x60;0&#x60; — Do **not** verify the certificate. | [optional] [default to 0]

### Return type

[**InlineResponse200425**](InlineResponse200425.md)

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

# **installed_hosts**
> InlineResponse200426 installed_hosts()

Return domains with SSL certificate information

This function retrieves a list of the account's websites, their domains, and certificate information.

**Important:**

  For a dedicated IP address, use the UAPI `SSL::installed_host` function.

**Important:**

 When you disable the *CalendarContact* , *MailReceive* , *WebDisk* , *Webmail* , and  *WebServer* [roles](https://go.cpanel.net/serverroles), the system **disables** this function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200426 import InlineResponse200426
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
    api_instance = clientapi_cpanel.CPanelAccountSSLManagementApi(api_client)

    try:
        # Return domains with SSL certificate information
        api_response = api_instance.installed_hosts()
        print("The response of CPanelAccountSSLManagementApi->installed_hosts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CPanelAccountSSLManagementApi->installed_hosts: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**InlineResponse200426**](InlineResponse200426.md)

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

# **list_certs**
> InlineResponse200430 list_certs()

Return all SSL certificates

This function lists an account's certificates.

**Important:**

When you disable the Calendars and Contacts, Receive Mail, Web Disk, Webmail,
and Web Server [roles](https://go.cpanel.net/howtouseserverprofiles#roles),
the system **disables** this function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200430 import InlineResponse200430
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
    api_instance = clientapi_cpanel.CPanelAccountSSLManagementApi(api_client)

    try:
        # Return all SSL certificates
        api_response = api_instance.list_certs()
        print("The response of CPanelAccountSSLManagementApi->list_certs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CPanelAccountSSLManagementApi->list_certs: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**InlineResponse200430**](InlineResponse200430.md)

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

# **list_csrs**
> InlineResponse200431 list_csrs()

Return all certificate signing requests

This function lists an account's certificate signing requests (CSR).

**Important:**

When you disable the Calendars and Contacts, Receive Mail, Web Disk,
Webmail, and Web Server
[roles](https://go.cpanel.net/howtouseserverprofiles#roles),
the system **disables** this function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200431 import InlineResponse200431
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
    api_instance = clientapi_cpanel.CPanelAccountSSLManagementApi(api_client)

    try:
        # Return all certificate signing requests
        api_response = api_instance.list_csrs()
        print("The response of CPanelAccountSSLManagementApi->list_csrs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CPanelAccountSSLManagementApi->list_csrs: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**InlineResponse200431**](InlineResponse200431.md)

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

# **list_keys**
> InlineResponse200432 list_keys()

Return all private keys

This function lists an account's private keys.

**Important:**

When you disable the Calendars and Contacts, Receive Mail, Web Disk, Webmail,
and Web Server [roles](https://go.cpanel.net/howtouseserverprofiles#roles),
the system **disables** this function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200432 import InlineResponse200432
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
    api_instance = clientapi_cpanel.CPanelAccountSSLManagementApi(api_client)

    try:
        # Return all private keys
        api_response = api_instance.list_keys()
        print("The response of CPanelAccountSSLManagementApi->list_keys:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CPanelAccountSSLManagementApi->list_keys: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**InlineResponse200432**](InlineResponse200432.md)

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

# **list_ssl_items**
> InlineResponse200433 list_ssl_items(domains=domains, item=item)

Return SSL-related items

This function lists SSL-related items on a domain.

**Important:**

When you disable the [Calendars and Contacts, Receive Mail, Web Disk, Webmail, and Web Server roles](https://go.cpanel.com/serverroles), the system **disables** this function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200433 import InlineResponse200433
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
    api_instance = clientapi_cpanel.CPanelAccountSSLManagementApi(api_client)
    domains = 'domains=example1.com|example2.com' # str | The domain name or names. (optional)
    item = 'key' # str | The SSL item type or types. * `key` * `csr` * `crt` (optional) (default to 'key')

    try:
        # Return SSL-related items
        api_response = api_instance.list_ssl_items(domains=domains, item=item)
        print("The response of CPanelAccountSSLManagementApi->list_ssl_items:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CPanelAccountSSLManagementApi->list_ssl_items: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domains** | **str**| The domain name or names. | [optional] 
 **item** | **str**| The SSL item type or types. * &#x60;key&#x60; * &#x60;csr&#x60; * &#x60;crt&#x60; | [optional] [default to &#39;key&#39;]

### Return type

[**InlineResponse200433**](InlineResponse200433.md)

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

# **rebuildssldb**
> InlineResponse200436 rebuildssldb()

Start SSL database rebuild

This function rebuilds the account's SSL database.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200436 import InlineResponse200436
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
    api_instance = clientapi_cpanel.CPanelAccountSSLManagementApi(api_client)

    try:
        # Start SSL database rebuild
        api_response = api_instance.rebuildssldb()
        print("The response of CPanelAccountSSLManagementApi->rebuildssldb:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CPanelAccountSSLManagementApi->rebuildssldb: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**InlineResponse200436**](InlineResponse200436.md)

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

# **s_sl_set_default_key_type**
> InlineResponse200441 s_sl_set_default_key_type(type)

Update SSL TLS key type

This function sets a user’s preferred SSL/TLS key type.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200441 import InlineResponse200441
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
    api_instance = clientapi_cpanel.CPanelAccountSSLManagementApi(api_client)
    type = 'ecdsa-prime256v1' # str | The key type to set.  * `system` — Use the system’s `ssl_default_key_type` value. * `rsa-2048` — 2,048-bit RSA. * `rsa-4096` — 4,096-bit RSA. * `ecdsa-prime256v1` — ECDSA prime256v1 (“P-256”). * `ecdsa-secp384r1` — ECDSA secp384r1 (“P-384”).

    try:
        # Update SSL TLS key type
        api_response = api_instance.s_sl_set_default_key_type(type)
        print("The response of CPanelAccountSSLManagementApi->s_sl_set_default_key_type:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CPanelAccountSSLManagementApi->s_sl_set_default_key_type: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| The key type to set.  * &#x60;system&#x60; — Use the system’s &#x60;ssl_default_key_type&#x60; value. * &#x60;rsa-2048&#x60; — 2,048-bit RSA. * &#x60;rsa-4096&#x60; — 4,096-bit RSA. * &#x60;ecdsa-prime256v1&#x60; — ECDSA prime256v1 (“P-256”). * &#x60;ecdsa-secp384r1&#x60; — ECDSA secp384r1 (“P-384”). | 

### Return type

[**InlineResponse200441**](InlineResponse200441.md)

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

# **toggle_ssl_redirect_for_domains**
> InlineResponse200448 toggle_ssl_redirect_for_domains(domains, state)

Enable or disable secure redirects

This function enables or disables secure redirects (HTTPS) for the cPanel account's domains that you specify.

**Important:**

To call this function, one of the following conditions **must** exist:

* AutoSSL **must** exist on the domains for which you enable secure redirects.
* A valid SSL certificate **must** exist for each domain for which you wish to enable secure redirects.
* You **must** own the domains for which you wish to enable secure redirects.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200448 import InlineResponse200448
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
    api_instance = clientapi_cpanel.CPanelAccountSSLManagementApi(api_client)
    domains = 'main.example,addon.example,addon.main.example' # str | A comma-separated list of the cPanel account's domains for which to enable or disable secure redirects.  **Important:**  To enable or disable redirects for addon domains, you **must** pass the addon domain **and** its subdomain.
    state = 1 # int | Whether to enable or disable redirects for the specified domains.  * `1` — Enable. * `0` — Disable.

    try:
        # Enable or disable secure redirects
        api_response = api_instance.toggle_ssl_redirect_for_domains(domains, state)
        print("The response of CPanelAccountSSLManagementApi->toggle_ssl_redirect_for_domains:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CPanelAccountSSLManagementApi->toggle_ssl_redirect_for_domains: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domains** | **str**| A comma-separated list of the cPanel account&#39;s domains for which to enable or disable secure redirects.  **Important:**  To enable or disable redirects for addon domains, you **must** pass the addon domain **and** its subdomain. | 
 **state** | **int**| Whether to enable or disable redirects for the specified domains.  * &#x60;1&#x60; — Enable. * &#x60;0&#x60; — Disable. | 

### Return type

[**InlineResponse200448**](InlineResponse200448.md)

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

