# clientapi_cpanel.SSLCertificateManagementApi

All URIs are relative to *https://cpanel-server.tld:2083/execute*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_cert**](SSLCertificateManagementApi.md#delete_cert) | **GET** /SSL/delete_cert | Delete SSL certificate
[**delete_csr**](SSLCertificateManagementApi.md#delete_csr) | **GET** /SSL/delete_csr | Delete certificate signing request
[**delete_key**](SSLCertificateManagementApi.md#delete_key) | **GET** /SSL/delete_key | Delete private key
[**generate_cert**](SSLCertificateManagementApi.md#generate_cert) | **GET** /SSL/generate_cert | Create self-signed SSL certificate
[**generate_csr**](SSLCertificateManagementApi.md#generate_csr) | **GET** /SSL/generate_csr | Create certificate signing request
[**install_ssl**](SSLCertificateManagementApi.md#install_ssl) | **GET** /SSL/install_ssl | Install SSL certificate
[**s_sl_generate_key**](SSLCertificateManagementApi.md#s_sl_generate_key) | **GET** /SSL/generate_key | Create private key
[**set_cert_friendly_name**](SSLCertificateManagementApi.md#set_cert_friendly_name) | **GET** /SSL/set_cert_friendly_name | Update SSL certificate&#39;s friendly name
[**set_csr_friendly_name**](SSLCertificateManagementApi.md#set_csr_friendly_name) | **GET** /SSL/set_csr_friendly_name | Update certificate signing request&#39;s friendly name
[**set_key_friendly_name**](SSLCertificateManagementApi.md#set_key_friendly_name) | **GET** /SSL/set_key_friendly_name | Update private key&#39;s friendly name
[**set_primary_ssl**](SSLCertificateManagementApi.md#set_primary_ssl) | **GET** /SSL/set_primary_ssl | Update SSL website for dedicated IP address
[**show_cert**](SSLCertificateManagementApi.md#show_cert) | **GET** /SSL/show_cert | Export SSL certificate
[**show_csr**](SSLCertificateManagementApi.md#show_csr) | **GET** /SSL/show_csr | Export certificate signing request
[**show_key**](SSLCertificateManagementApi.md#show_key) | **GET** /SSL/show_key | Export private key
[**upload_cert**](SSLCertificateManagementApi.md#upload_cert) | **POST** /SSL/upload_cert | Import SSL certificate
[**upload_key**](SSLCertificateManagementApi.md#upload_key) | **POST** /SSL/upload_key | Import private key


# **delete_cert**
> InlineResponse200405 delete_cert(friendly_name=friendly_name, id=id)

Delete SSL certificate

This function deletes an SSL certificate.

**Note:**

* When you call this function, you **must** include the `id` or the `friendly_name`
parameter.
* This function **only** deletes certificates from SSL storage. To end SSL
coverage for a domain, use the UAPI `SSL::delete_ssl` function instead.

**Important:**

When you disable the Calendars and Contacts, Receive Mail, Web Disk, Webmail,
and Web Server [roles](https://go.cpanel.net/howtouseserverprofiles#roles),
the system **disables** this function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200405 import InlineResponse200405
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
    api_instance = clientapi_cpanel.SSLCertificateManagementApi(api_client)
    friendly_name = 'TestCert' # str | The certificate's friendly name. (optional)
    id = 'example_com_cb497_a394d_1397249671_d1272da8f13a1fd837493a5ad1f0a0f3' # str | The certificate's ID. (optional)

    try:
        # Delete SSL certificate
        api_response = api_instance.delete_cert(friendly_name=friendly_name, id=id)
        print("The response of SSLCertificateManagementApi->delete_cert:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SSLCertificateManagementApi->delete_cert: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **friendly_name** | **str**| The certificate&#39;s friendly name. | [optional] 
 **id** | **str**| The certificate&#39;s ID. | [optional] 

### Return type

[**InlineResponse200405**](InlineResponse200405.md)

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

# **delete_csr**
> InlineResponse200406 delete_csr(friendly_name=friendly_name, id=id)

Delete certificate signing request

This function deletes a certificate signing request (CSR).

**Note:**

* When you call this function, you **must** include the `id` or the `friendly_name`
parameter.
* To delete a private key, use the UAPI `SSL::delete_key` function instead.

**Important:**

When you disable the Calendars and Contacts, Receive Mail, Web Disk, Webmail,
and Web Server [roles](https://go.cpanel.net/howtouseserverprofiles#roles),
the system **disables** this function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200406 import InlineResponse200406
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
    api_instance = clientapi_cpanel.SSLCertificateManagementApi(api_client)
    friendly_name = 'TestCSR' # str | The CSR's friendly name. (optional)
    id = 'example_com_e095f_0ab2f_ebcbe4a571276f48562241411556647f' # str | The CSR's ID. (optional)

    try:
        # Delete certificate signing request
        api_response = api_instance.delete_csr(friendly_name=friendly_name, id=id)
        print("The response of SSLCertificateManagementApi->delete_csr:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SSLCertificateManagementApi->delete_csr: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **friendly_name** | **str**| The CSR&#39;s friendly name. | [optional] 
 **id** | **str**| The CSR&#39;s ID. | [optional] 

### Return type

[**InlineResponse200406**](InlineResponse200406.md)

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

# **delete_key**
> InlineResponse200407 delete_key(friendly_name=friendly_name, id=id)

Delete private key

This function deletes a private key.

**Note:**

* When you call this function, you **must** include the `id` or the `friendly_name`
parameter.
* To delete a certificate signing request (CSR), use the UAPI `SSL::delete_csr`
function instead.

**Important:**

When you disable the Calendars and Contacts, Receive Mail, Web Disk, Webmail,
and Web Server [roles](https://go.cpanel.net/howtouseserverprofiles#roles),
the system **disables** this function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200407 import InlineResponse200407
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
    api_instance = clientapi_cpanel.SSLCertificateManagementApi(api_client)
    friendly_name = 'TestKey' # str | The private key's friendly name. (optional)
    id = 'example_com_e095f_0ab2f_ebcbe4a571276f48562241411556647f' # str | The private key's ID. (optional)

    try:
        # Delete private key
        api_response = api_instance.delete_key(friendly_name=friendly_name, id=id)
        print("The response of SSLCertificateManagementApi->delete_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SSLCertificateManagementApi->delete_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **friendly_name** | **str**| The private key&#39;s friendly name. | [optional] 
 **id** | **str**| The private key&#39;s ID. | [optional] 

### Return type

[**InlineResponse200407**](InlineResponse200407.md)

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

# **generate_cert**
> InlineResponse200417 generate_cert(country_name, domains, key_id, locality_name, organization_name, state_or_province_name, email_address=email_address, friendly_name=friendly_name, organizational_unit_name=organizational_unit_name)

Create self-signed SSL certificate

This function generates a self-signed SSL certificate.

**Important:**

When you disable the Calendars and Contacts, Receive Mail, Web Disk, Webmail,
and Web Server [roles](https://go.cpanel.net/howtouseserverprofiles#roles),
the system **disables** this function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200417 import InlineResponse200417
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
    api_instance = clientapi_cpanel.SSLCertificateManagementApi(api_client)
    country_name = 'US' # str | The two-letter country code.
    domains = 'domains=example1.com,example2.com,example3.com' # str | A comma-separated list of domains for which to generate the certificate.
    key_id = 'example_com_cb497_a394d_1397249671_d1272da8f13a1fd837493a5ad1f0a0f3' # str | The key's ID.
    locality_name = 'Houston' # str | The certificate's city or locality name.
    organization_name = 'Organization' # str | The certificate's Organization Name.
    state_or_province_name = 'TX' # str | The two-letter state or locality abbreviation.
    email_address = '' # str | An email address to associate with the certificate. (optional) (default to '')
    friendly_name = 'TestCert' # str | A friendly name for the new certificate.  This parameter defaults to the domain's name for which you generated the certificate. (optional)
    organizational_unit_name = '' # str | The certificate's organizational unit or department name. (optional) (default to '')

    try:
        # Create self-signed SSL certificate
        api_response = api_instance.generate_cert(country_name, domains, key_id, locality_name, organization_name, state_or_province_name, email_address=email_address, friendly_name=friendly_name, organizational_unit_name=organizational_unit_name)
        print("The response of SSLCertificateManagementApi->generate_cert:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SSLCertificateManagementApi->generate_cert: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **country_name** | **str**| The two-letter country code. | 
 **domains** | **str**| A comma-separated list of domains for which to generate the certificate. | 
 **key_id** | **str**| The key&#39;s ID. | 
 **locality_name** | **str**| The certificate&#39;s city or locality name. | 
 **organization_name** | **str**| The certificate&#39;s Organization Name. | 
 **state_or_province_name** | **str**| The two-letter state or locality abbreviation. | 
 **email_address** | **str**| An email address to associate with the certificate. | [optional] [default to &#39;&#39;]
 **friendly_name** | **str**| A friendly name for the new certificate.  This parameter defaults to the domain&#39;s name for which you generated the certificate. | [optional] 
 **organizational_unit_name** | **str**| The certificate&#39;s organizational unit or department name. | [optional] [default to &#39;&#39;]

### Return type

[**InlineResponse200417**](InlineResponse200417.md)

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

# **generate_csr**
> InlineResponse200418 generate_csr(country_name, domains, key_id, locality_name, organization_name, state_or_province_name, email_address=email_address, friendly_name=friendly_name, organizational_unit_name=organizational_unit_name)

Create certificate signing request

This function generates a certificate signing request (CSR).

**Note:**

This function **requires** a valid key in the account's `ssl` directory.
You can generate a key with UAPI's `SSL::generate_key` function.

**Important:**

When you disable the Calendars and Contacts, Receive Mail, Web Disk, Webmail,
and WebServer [roles](https://go.cpanel.net/howtouseserverprofiles#roles),
the system **disables** this function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200418 import InlineResponse200418
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
    api_instance = clientapi_cpanel.SSLCertificateManagementApi(api_client)
    country_name = 'US' # str | The two-letter country code.
    domains = 'domains=example-1.com,example-1.com,example-2.com' # str | A comma-separated list of the domains for which to generate the certificate.
    key_id = 'example_com_cb497_a394d_1397249671_d1272da8f13a1fd837493a5ad1f0a0f3' # str | The key's ID.
    locality_name = 'Houston' # str | The certificate's city or locality name.
    organization_name = 'Organization' # str | The certificate's organization.
    state_or_province_name = 'Texas' # str | The certificate's state or locality name.
    email_address = '' # str | An email address to associate with the certificate. (optional) (default to '')
    friendly_name = 'TestCert' # str | A friendly name for the new certificate.  This parameter defaults to the domain name for which you generated the certificate. (optional)
    organizational_unit_name = '' # str | The certificate's organizational unit or department name. (optional) (default to '')

    try:
        # Create certificate signing request
        api_response = api_instance.generate_csr(country_name, domains, key_id, locality_name, organization_name, state_or_province_name, email_address=email_address, friendly_name=friendly_name, organizational_unit_name=organizational_unit_name)
        print("The response of SSLCertificateManagementApi->generate_csr:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SSLCertificateManagementApi->generate_csr: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **country_name** | **str**| The two-letter country code. | 
 **domains** | **str**| A comma-separated list of the domains for which to generate the certificate. | 
 **key_id** | **str**| The key&#39;s ID. | 
 **locality_name** | **str**| The certificate&#39;s city or locality name. | 
 **organization_name** | **str**| The certificate&#39;s organization. | 
 **state_or_province_name** | **str**| The certificate&#39;s state or locality name. | 
 **email_address** | **str**| An email address to associate with the certificate. | [optional] [default to &#39;&#39;]
 **friendly_name** | **str**| A friendly name for the new certificate.  This parameter defaults to the domain name for which you generated the certificate. | [optional] 
 **organizational_unit_name** | **str**| The certificate&#39;s organizational unit or department name. | [optional] [default to &#39;&#39;]

### Return type

[**InlineResponse200418**](InlineResponse200418.md)

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

# **install_ssl**
> InlineResponse200424 install_ssl(cert, domain, key, cabundle=cabundle)

Install SSL certificate

This function installs an SSL certificate.

**Note:**

Due to their inherent complexities, SSL-related functions often present problems for third-party developers. For the additional steps required to successfully call this function, read our [Call UAPI's SSL::install_ssl Function in Custom Code](https://go.cpanel.net/tutorial-call-uapis-ssl-install-ssl-function-in-custom-code) documentation.

**Important:**

When you disable the *Calendars and Contacts*, *Receive Mail*, *Web Disk*, *Webmail*, and *Web Server* [roles](https://go.cpanel.net/serverroles), the system **disables** this function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200424 import InlineResponse200424
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
    api_instance = clientapi_cpanel.SSLCertificateManagementApi(api_client)
    cert = '-----BEGIN%20CERTIFICATE-----%0AMIIEEzCCAvugAwIBAgIJALF%2FjFpw6p1bMA0GCSqGSIb3DQEBBQUAMIGfMRYwFAYD%0AVQQDEw10ZXN0c2ltb24uY29tMRYwFAYDVQQLEw1Eb2N1bWVudGF0aW9uMQswCQYD%0AVQQGEwJVUzEoMCYGCSqGSIb3DQEJARYZbGF1cmVuY2Uuc2ltb25AY3BhbmVsLm5l%0AdDEUMBIGA1UEChMLY1BhbmVsIEluYy4xDjAMBgNVBAgTBVRleGFzMRAwDgYDVQQH%0AEwdIb3VzdG9uMB4XDTEzMDUxNzE2MTMwN1oXDTE0MDUxNzE2MTMwN1owgZ8xFjAU%0ABgNVBAMTDXRlc3RzaW1vbi5jb20xFjAUBgNVBAsTDURvY3VtZW50YXRpb24xCzAJ%0ABgNVBAYTAlVTMSgwJgYJKoZIhvcNAQkBFhlsYXVyZW5jZS5zaW1vbkBjcGFuZWwu%0AbmV0MRQwEgYDVQQKEwtjUGFuZWwgSW5jLjEOMAwGA1UECBMFVGV4YXMxEDAOBgNV%0ABAcTB0hvdXN0b24wggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAwggEKAoIBAQDRO0AP%0AN5XtjDqkEyJ6ctfYqUtt9yUXyRuCETFjW6opNLSmZSHeF6L2aZka646lhj02CFyl%0AkzsNSxysN66tY%2BWZcTmvgPisJdQFpFvjroJZgDjYRV0QqokKdRy%2F5BU0%2BtHXoYpj%0A9JOQlbvEWxiGR3R80sL1ma4AfSE6Gv8M%2FPULTadan51eHaikXqjOXdPJQKuWP3g9%0AFnIuf38WRYwzGrre88qsZrpsMrADX5dotHWgqAf7Tap6xfA4CUAgQo9tldariuVi%0ABz%2BsRJ%2FSjgxnhw1HYWGttBuBZFhMpdHpPnTJ7DIFMd%2FFN5gG%2Ftah30SapWpo35Ux%0A3BpJcdUjtazy82K5AgMBAAGjUDBOMB0GA1UdDgQWBBQAlv7%2FtALOYb7zAXbYG2%2B9%0AAMI3xjAfBgNVHSMEGDAWgBQAlv7%2FtALOYb7zAXbYG2%2B9AMI3xjAMBgNVHRMEBTAD%0AAQH%2FMA0GCSqGSIb3DQEBBQUAA4IBAQCxzpe71Hc7Es0dqIN7bhIFYIIgcr6wxM6a%0Aa9d%2BQG%2BQPH0x0KAqV8EgUbZysvyxEF0bPxW3ZAr1Is1wk80PMuU3bToFFVbFFIIr%0AHRNfKLGvxiMXnZA1c6L4N0lowvXHgZxTTUXtDFLXyrcwrLsvUErEV7rbizuxqfPw%0AcaRtXn4uc%2Bt6HYuW7yWesBauCWnJNiKbjN%2FF%2BuCTurN3QMAeWf3ZJtsfkAgk8dyq%0AR%2F83a3kDtSPrpt%2BjX%2BqdjKEpRtQ5Qpm6XT2gCOQPgnfiUtOCH419pp922P%2FAAGc%2B%0AZUhYoWcRWKw%2Fy6gI7Ru%2B%2B9%2B8%2BwkadL9EbKMZxhVwD5qVm4ZlWK2a%5Cr%5Cn%0A-----END%20CERTIFICATE-----' # str | The certificate to install.  **Note:**  * You **must** URI-encode this value. * You can use a Perl command to URI-encode your SSL certificate for this parameter. For example, you can use the following string, where `CERT.FILE` is the SSL certificate file:    ```$(perl -MURI::Escape -ne 'print uri_escape($_);' CERT.FILE)```
    domain = 'example.com' # str | The domain name.
    key = '-----BEGIN%20RSA%20PRIVATE%20KEY-----%0AMIIEpAIBAAKCAQEA4AVM6J4Qg3DIFWr%2FeJ5GRmIATYsJIepKbrDy70sq%2BudcO8R8%0Axxak0oMZ%2F9mUdpjSNK%2FfLVTuCO0kxTfQ9VUWJllX7ThD6Zh9ZvlC%2Fnf%2FOEZLm3Zb%0ABgu8rbC8E9wuDOkKbJLnINgdhtowIydLK2MJ%2B%2Bq62bFV89jkHWTMcKyyqHENo3h%0Ac%2Blkpd9vnp8rZTinaVb7nX26uQqAFZYRo%2BWU0G%2FNPsq40QVSMoqPxyEz4qXo0hvu%0AIlCXmzFZq%2F6fCVPEKPLhQgMmpdBkMz4dVOazREfqXdjMD2%2BQXSNiA1AwWr8l0r4r%0AtzlxEYDJIR41yXp0xMl3KoolxMyvLBqZy32niQIDAQABAoIBAQCmbGmhWmPsMeoC%0At1WJFxQgD4goE0U6k%2BKt7vjbOt14Pk6v%2FB2yjaju1wSGpO59WLS4%2FXrwI2se6IXr%0Amba7u3VUEgWXLriNHoLy7%2FSMNTs%2BZEKhAMG36eNe3tVdT7busTag31r6sEMGGwCs%0AIwpU%2Bazosk0oylWLEX%2Fm%2FuHWEs1eaIEWWWtgHB%2BKZrrP7Rr9RYfVQ144DxmOxS3C%0Aa9%2BmST62WqAVPR6POWGEfZqnZl%2FePWZPcQYbFrhwnnefNoYBl%2FbnLZBo8rbNWxAq%0AOEOuKfkrBzglKG%2F39WKPw8rj4JIVzY0yOuFCW6xCDWRkOrhU8Ol%2F3FvwDa3uJpkp%0AmgPr4TgxAoGBAPGPLmxSuOYR97mDAXxrs037F2GCbqWvI6m7%2FezWe9yn%2BbMpjSIW%0Afsgtq4FsyqzPueEkDdQWi3xh6nu2WI%2F1Tl875opGAqEIJMqss%2Fu11tnva5wzu1cC%0AL6H85A5%2BHMOBvP3sm6CObKcVw92h7kxynVIUJJWhjfeZMN8gBFFpKIVFAoGBAO1p%0AtXBmXLC%2FYKKvtHI3M16%2FZopvM8ZqU2HcAHaw214Refw9JJ%2Fe3%2FxTNfSerVTyCAQO%0A1AdWTzJKBN8jmSYv1Mk1D3RpQPNR7wVzi46KR081AU41uMpqIGVOwHtyVnW%2FZfLr%0Ac1DLIK8Cx8aHfoxffwzoMO5SEQSooeZfOLhsfDN1AoGBAKQTUEINsj%2B75psgbAr6%0AELGgItJ9yPBLVRr%2BcUzEpx9LDWVvjMihpP4NX1gq8EOPWT%2BewLHVmmsjCyV6xw8J%0AXXF8e2xif3in0m3D%2FwCzE7u2T06rKM3B017hKnrZmGoHnrqPU2osM4sOUpshWX6d%0Av1Q4EF1%2BfbK3YCW%2BVpCBsB9NAoGAQo%2BuhNLODee56iKkzpjXWCsFTq6ar3hD5F3P%0A63buKdNwhd2GlSPhXFbf%2B7M5GWW6BZk6rMvv7EOAVice2uvyFm8%2F4%2F1WbmF8R%2BT7%0ALX1rPLO5p%2Fm701QpvP11TabiwqRkqtSEQhSRF0AKTojSW%2FyyHCZFAawUhV%2FZ9EKi%0AHmKb97kCgYAyzmFc2it0HqnsOnRybop603nqMtWGTQO4cxa93HUDpYajuK2K3Dfr%0AxUj6lG3z%2FoKJGGE2JqgZ6LBAhNJtJWJu2ox3pKGE63QjLJnVwb8y1NFYpe%2FcrbLe%0APuBwIR0L7drXxfv7O5btY7h6QI2d1%2FUIAQPAWbxLoTM%2BndQ%2FuPEdfA%3D%3D%0A-----END%20RSA%20PRIVATE%20KEY-----' # str | The certificate's key.  **Note:**  * You **must** URI-encode this value. * You can use a Perl command to URI-encode your SSL certificate for this parameter. For example, you can use the following string, where `KEY.FILE` is the SSL certificate file:    ```$(perl -MURI::Escape -ne 'print uri_escape($_);' KEY.FILE)```
    cabundle = '-----BEGIN%20CERTIFICATE-----%0AMIIB%2BjCCAWMCAgGjMA0GCSqGSIb3DQEBBAUAMEUxCzAJBgNVBAYTAlVTMRgwFgYD%0AVQQKEw9HVEUgQ29ycG9yYXRpb24xHDAaBgNVBAMTE0dURSBDeWJlclRydXN0IFJv%0Ab3QwHhcNOTYwMjIzMjMwMTAwWhcNMDYwMjIzMjM1OTAwWjBFMQswCQYDVQQGEwJV%0AUzEYMBYGA1UEChMPR1RFIENvcnBvcmF0aW9uMRwwGgYDVQQDExNHVEUgQ3liZXJU%0AcnVzdCBSb290MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQC45k%2B625h8cXyv%0ARLfTD0bZZOWTwUKOx7pJjTUteueLveUFMVnGsS8KDPufpz%2BiCWaEVh43KRuH6X4M%0AypqfpX%2F1FZSj1aJGgthoTNE3FQZor734sLPwKfWVWgkWYXcKIiXUT0Wqx73llt%2F5%0A1KiOQswkwB6RJ0q1bQaAYznEol44AwIDAQABMA0GCSqGSIb3DQEBBAUAA4GBABKz%0AdcZfHeFhVYAA1IFLezEPI2PnPfMD%2BfQ2qLvZ46WXTeorKeDWanOB5sCJo9Px4KWl%0AIjeaY8JIILTbcuPI9tl8vrGvU9oUtCG41tWW4%2F5ODFlitppK%2BULdjG%2BBqXH%2F9Apy%0AbW1EDp3zdHSo1TRJ6V6e6bR64eVaH4QwnNOfpSXY%0A-----END%20CERTIFICATE-----' # str | The Certificate Authority (CA) bundle data, if the certificate requires it.  **Note:**  * You **must** URI-encode this value. * You can use a Perl command to URI-encode your SSL certificate for this parameter. For example, you can use the following string, where `CABUNDLE.FILE` is the SSL certificate file:    ```$(perl -MURI::Escape -ne 'print uri_escape($_);' CABUNDLE.FILE)``` (optional)

    try:
        # Install SSL certificate
        api_response = api_instance.install_ssl(cert, domain, key, cabundle=cabundle)
        print("The response of SSLCertificateManagementApi->install_ssl:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SSLCertificateManagementApi->install_ssl: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cert** | **str**| The certificate to install.  **Note:**  * You **must** URI-encode this value. * You can use a Perl command to URI-encode your SSL certificate for this parameter. For example, you can use the following string, where &#x60;CERT.FILE&#x60; is the SSL certificate file:    &#x60;&#x60;&#x60;$(perl -MURI::Escape -ne &#39;print uri_escape($_);&#39; CERT.FILE)&#x60;&#x60;&#x60; | 
 **domain** | **str**| The domain name. | 
 **key** | **str**| The certificate&#39;s key.  **Note:**  * You **must** URI-encode this value. * You can use a Perl command to URI-encode your SSL certificate for this parameter. For example, you can use the following string, where &#x60;KEY.FILE&#x60; is the SSL certificate file:    &#x60;&#x60;&#x60;$(perl -MURI::Escape -ne &#39;print uri_escape($_);&#39; KEY.FILE)&#x60;&#x60;&#x60; | 
 **cabundle** | **str**| The Certificate Authority (CA) bundle data, if the certificate requires it.  **Note:**  * You **must** URI-encode this value. * You can use a Perl command to URI-encode your SSL certificate for this parameter. For example, you can use the following string, where &#x60;CABUNDLE.FILE&#x60; is the SSL certificate file:    &#x60;&#x60;&#x60;$(perl -MURI::Escape -ne &#39;print uri_escape($_);&#39; CABUNDLE.FILE)&#x60;&#x60;&#x60; | [optional] 

### Return type

[**InlineResponse200424**](InlineResponse200424.md)

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

# **s_sl_generate_key**
> InlineResponse200419 s_sl_generate_key(friendly_name=friendly_name, keysize=keysize, keytype=keytype)

Create private key

This function generates a private key.

**Important:**

* You **cannot** call both the `keytype` and `keysize` parameters in a single call.
* When you disable the Calendars and Contacts, Receive Mail, Web Disk, Webmail, **and**
Web Server [roles](https://go.cpanel.net/howtouseserverprofiles#roles),
the system **disables** this function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200419 import InlineResponse200419
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
    api_instance = clientapi_cpanel.SSLCertificateManagementApi(api_client)
    friendly_name = 'TestKey' # str | A friendly name for the new key.  This parameter defaults to the key's type, creation date, and creation time. (optional)
    keysize = 2048 # int | The key's modulus size.  **Note:**  Use the `keytype` parameter. (optional) (default to 2048)
    keytype = 'rsa-2048' # str | The key's type.  * `system` — The system's default value. * `rsa-2048` — 2,408-bit RSA. * `rsa-4096` — 4,096-bit RSA. * `ecdsa-prime256v1` — ECDSA prime256v1 (\"P-256\"). * `ecdsa-secp384r1` — ECDSA secp384r1 (\"P-384\").  This parameter defaults to the user's [default SSL/TLS key type](https://go.cpanel.net/cpaneldocsSSLTLS#default-ssl-tls-key-type).  **Note:**  If you do **not** use this parameter, the system defaults to the `keysize` parameter's default value. (optional)

    try:
        # Create private key
        api_response = api_instance.s_sl_generate_key(friendly_name=friendly_name, keysize=keysize, keytype=keytype)
        print("The response of SSLCertificateManagementApi->s_sl_generate_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SSLCertificateManagementApi->s_sl_generate_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **friendly_name** | **str**| A friendly name for the new key.  This parameter defaults to the key&#39;s type, creation date, and creation time. | [optional] 
 **keysize** | **int**| The key&#39;s modulus size.  **Note:**  Use the &#x60;keytype&#x60; parameter. | [optional] [default to 2048]
 **keytype** | **str**| The key&#39;s type.  * &#x60;system&#x60; — The system&#39;s default value. * &#x60;rsa-2048&#x60; — 2,408-bit RSA. * &#x60;rsa-4096&#x60; — 4,096-bit RSA. * &#x60;ecdsa-prime256v1&#x60; — ECDSA prime256v1 (\&quot;P-256\&quot;). * &#x60;ecdsa-secp384r1&#x60; — ECDSA secp384r1 (\&quot;P-384\&quot;).  This parameter defaults to the user&#39;s [default SSL/TLS key type](https://go.cpanel.net/cpaneldocsSSLTLS#default-ssl-tls-key-type).  **Note:**  If you do **not** use this parameter, the system defaults to the &#x60;keysize&#x60; parameter&#39;s default value. | [optional] 

### Return type

[**InlineResponse200419**](InlineResponse200419.md)

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

# **set_cert_friendly_name**
> InlineResponse200439 set_cert_friendly_name(friendly_name, new_friendly_name)

Update SSL certificate's friendly name

This function changes a certificate's friendly name.

**Important:**

When you disable the [Calendars and Contacts, Receive Mail, Web Disk, Webmail, and Web Server roles](https://go.cpanel.net/serverroles), the system **disables** this function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200439 import InlineResponse200439
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
    api_instance = clientapi_cpanel.SSLCertificateManagementApi(api_client)
    friendly_name = 'TestCert' # str | The certificate's friendly name.
    new_friendly_name = 'TestCert2' # str | The certificate's new friendly name.

    try:
        # Update SSL certificate's friendly name
        api_response = api_instance.set_cert_friendly_name(friendly_name, new_friendly_name)
        print("The response of SSLCertificateManagementApi->set_cert_friendly_name:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SSLCertificateManagementApi->set_cert_friendly_name: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **friendly_name** | **str**| The certificate&#39;s friendly name. | 
 **new_friendly_name** | **str**| The certificate&#39;s new friendly name. | 

### Return type

[**InlineResponse200439**](InlineResponse200439.md)

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

# **set_csr_friendly_name**
> InlineResponse200440 set_csr_friendly_name(friendly_name, id, new_friendly_name)

Update certificate signing request's friendly name

This function changes a certificate signing request's (CSR) friendly name.

**Important:**

* You **must** call either the `friendly_name` or `id` parameter.
* When you disable the Calendars and Contacts, Receive Mail, Web Disk, Webmail, and Web Server [roles](https://go.cpanel.net/serverroles), the system **disables** this function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200440 import InlineResponse200440
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
    api_instance = clientapi_cpanel.SSLCertificateManagementApi(api_client)
    friendly_name = 'TestCSR' # str | The CSR's friendly name.
    id = 'example_com_eda9d_543fb_a3009b4b01a592390866ab3a47c0df18' # str | The CSR's ID.  **Note:**  To retrieve a CSR's ID, use the UAPI `list_csrs` function.
    new_friendly_name = 'TestCSR2' # str | The CSR's new friendly name.

    try:
        # Update certificate signing request's friendly name
        api_response = api_instance.set_csr_friendly_name(friendly_name, id, new_friendly_name)
        print("The response of SSLCertificateManagementApi->set_csr_friendly_name:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SSLCertificateManagementApi->set_csr_friendly_name: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **friendly_name** | **str**| The CSR&#39;s friendly name. | 
 **id** | **str**| The CSR&#39;s ID.  **Note:**  To retrieve a CSR&#39;s ID, use the UAPI &#x60;list_csrs&#x60; function. | 
 **new_friendly_name** | **str**| The CSR&#39;s new friendly name. | 

### Return type

[**InlineResponse200440**](InlineResponse200440.md)

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

# **set_key_friendly_name**
> InlineResponse200442 set_key_friendly_name(friendly_name, id, new_friendly_name)

Update private key's friendly name

This function changes a key's friendly name.

**Important:**

* You **must** call either the `friendly_name` or `id` parameter.
* When you disable the Calendars and Contacts, Receive Mail, Web Disk, Webmail, and Web Server [roles](https://go.cpanel.net/serverroles), the system **disables** this function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200442 import InlineResponse200442
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
    api_instance = clientapi_cpanel.SSLCertificateManagementApi(api_client)
    friendly_name = 'TestKey' # str | The key's friendly name.
    id = 'a9b72_63971_2cb6d8897b362cfb1548e047d8428b8d' # str | The key's ID.
    new_friendly_name = 'TestKey2' # str | The key's new friendly name.

    try:
        # Update private key's friendly name
        api_response = api_instance.set_key_friendly_name(friendly_name, id, new_friendly_name)
        print("The response of SSLCertificateManagementApi->set_key_friendly_name:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SSLCertificateManagementApi->set_key_friendly_name: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **friendly_name** | **str**| The key&#39;s friendly name. | 
 **id** | **str**| The key&#39;s ID. | 
 **new_friendly_name** | **str**| The key&#39;s new friendly name. | 

### Return type

[**InlineResponse200442**](InlineResponse200442.md)

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

# **set_primary_ssl**
> InlineResponse200443 set_primary_ssl(servername)

Update SSL website for dedicated IP address

This function sets a new primary SSL website for a dedicated IP address.

**Important:**

When you disable the [Calendars and Contacts, Receive Mail, Web Disk, Webmail, and Web Server roles](https://go.cpanel.net/serverroles), the system **disables** this function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200443 import InlineResponse200443
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
    api_instance = clientapi_cpanel.SSLCertificateManagementApi(api_client)
    servername = 'hostname.example.com' # str | The primary SSL website's servername.

    try:
        # Update SSL website for dedicated IP address
        api_response = api_instance.set_primary_ssl(servername)
        print("The response of SSLCertificateManagementApi->set_primary_ssl:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SSLCertificateManagementApi->set_primary_ssl: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **servername** | **str**| The primary SSL website&#39;s servername. | 

### Return type

[**InlineResponse200443**](InlineResponse200443.md)

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

# **show_cert**
> InlineResponse200444 show_cert(friendly_name=friendly_name, id=id)

Export SSL certificate

This function retrieves a certificate.

**Note:**

When you call this parameter, you **must** include either the `id` or
the `friendly_name` parameter.

**Important:**

When you disable the Calendars and Contacts, Receive Mail, Web Disk,
Webmail, **and** Web Server [roles](https://go.cpanel.net/howtouseserverprofiles#roles),
the system **disables** this function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200444 import InlineResponse200444
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
    api_instance = clientapi_cpanel.SSLCertificateManagementApi(api_client)
    friendly_name = 'TestCert' # str | The certificate's friendly name. (optional)
    id = 'example_com_c69ce_37ff5_1397169490_169c717cb2c260281df792788accf041' # str | The certificate's ID. (optional)

    try:
        # Export SSL certificate
        api_response = api_instance.show_cert(friendly_name=friendly_name, id=id)
        print("The response of SSLCertificateManagementApi->show_cert:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SSLCertificateManagementApi->show_cert: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **friendly_name** | **str**| The certificate&#39;s friendly name. | [optional] 
 **id** | **str**| The certificate&#39;s ID. | [optional] 

### Return type

[**InlineResponse200444**](InlineResponse200444.md)

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

# **show_csr**
> InlineResponse200445 show_csr(friendly_name=friendly_name, id=id)

Export certificate signing request

This function retrieves a certificate signing request (CSR).

**Important:**

When you disable the Calendars and Contacts, Receive Mail, Web Disk, Webmail,
and Web Server [roles](https://go.cpanel.net/howtouseserverprofiles#roles),
the system **disables** this function.

**Note:**

When you call this function, you **must** include either the `id`
or the `friendly_name` parameter.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200445 import InlineResponse200445
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
    api_instance = clientapi_cpanel.SSLCertificateManagementApi(api_client)
    friendly_name = 'TestCSR' # str | The CSR's friendly name. (optional)
    id = 'example_com_e095f_0ab2f_ebcbe4a571276f48562241411556647f' # str | The CSR's ID. (optional)

    try:
        # Export certificate signing request
        api_response = api_instance.show_csr(friendly_name=friendly_name, id=id)
        print("The response of SSLCertificateManagementApi->show_csr:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SSLCertificateManagementApi->show_csr: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **friendly_name** | **str**| The CSR&#39;s friendly name. | [optional] 
 **id** | **str**| The CSR&#39;s ID. | [optional] 

### Return type

[**InlineResponse200445**](InlineResponse200445.md)

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

# **show_key**
> InlineResponse200446 show_key(friendly_name=friendly_name, id=id)

Export private key

This function retrieves a private key.

**Important:**

When you disable the Calendars and Contacts, Receive Mail, Web Disk, Webmail, **and** Web Server [roles](https://go.cpanel.net/serverroles), the system **disables** this function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200446 import InlineResponse200446
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
    api_instance = clientapi_cpanel.SSLCertificateManagementApi(api_client)
    friendly_name = 'TestKey' # str | The key's friendly name.  **Note:**  You **must** use either the `id` or the `friendly_name` parameter. (optional)
    id = 'example_com_c69ce_37ff5_1397169490_169c717cb2c260281df792788accf041' # str | The key's ID.  **Note:**  You **must** use either the `id` or the `friendly_name` parameter. (optional)

    try:
        # Export private key
        api_response = api_instance.show_key(friendly_name=friendly_name, id=id)
        print("The response of SSLCertificateManagementApi->show_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SSLCertificateManagementApi->show_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **friendly_name** | **str**| The key&#39;s friendly name.  **Note:**  You **must** use either the &#x60;id&#x60; or the &#x60;friendly_name&#x60; parameter. | [optional] 
 **id** | **str**| The key&#39;s ID.  **Note:**  You **must** use either the &#x60;id&#x60; or the &#x60;friendly_name&#x60; parameter. | [optional] 

### Return type

[**InlineResponse200446**](InlineResponse200446.md)

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

# **upload_cert**
> InlineResponse200449 upload_cert(crt, friendly_name=friendly_name, crt2=crt2, friendly_name2=friendly_name2)

Import SSL certificate

This function uploads a certificate.

**Important:**

* Due to the limited field length of HTTP GET method calls, you **must** use the HTTP
POST method. For this reason, you **cannot** use a cPanel or Webmail session URL to
call this function.
* When you disable the Calendar and Contacts, Receive Mail, Web Disk, Webmail, and
Web Server [roles](https://go.cpanel.net/howtouseserverprofiles#roles),
the system **disables** this function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200449 import InlineResponse200449
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
    api_instance = clientapi_cpanel.SSLCertificateManagementApi(api_client)
    crt = '\"-----BEGIN CERTIFICATE-----/nMIIDcTCCAlmgAwIBAgIFAU+BNVgwDQYJKoZIhvcNAQEFBQAwUTESMBAGA1UEAwwJc2lza28udGxkMQswCQYDVQQGEwJVUzEPMA0GA1UECgwGY1BhbmVsMQswCQYDVQQIDAJUWDEQMA4GA1UEBwwHSG91c3RvbjAeFw0xNDEwMDYyMjI2MTlaFw0xNTEwMDYyMjI2MTlaMFExEjAQBgNVBAMMCXNpc2tvLnRsZDELMAkGA1UEBhMCVVMxDzANBgNVBAoMBmNQYW5lbDELMAkGA1UECAwCVFgxEDAOBgNVBAcMB0hvdXN0b24wggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAwggEKAoIBAQC9zx6zGiHdmWA0dKtoXmJiWXpZ9E3PXx3YHsjFEWW7e5pH0vZ+jVMzDmm5nsJ7RXrAkZO1IvpIpVLvoQfiJOWVvkD+o9fWvoK1tWJS72FSgPju+58mA2ieBuc87A790Pzuv1P3NR3zFLAjUR99zkHR1fpri/daM3PBWO8ET48FWkyU1kOeZaUlF67/+wrEiNgg+t1qhKOCAB61PdNVkLaSGHimksuC+Czk8Kq9nuS0E0TCnDtjjEyJ455FUcaCfczlTb8xkB/F9ORe74yTzD+vlk0tFMG6PLj/ajIwWqwO0qmQ8wX3NRxkWgGz5kVO1wrVJarKQ5EYQ3/mgvit0v6dAgMBAAGjUDBOMB0GA1UdDgQWBBRw+wKBo34+bgexjAa3EMDsgSCd7zAfBgNVHSMEGDAWgBRw+wKBo34+bgexjAa3EMDsgSCd7zAMBgNVHRMEBTADAQH/MA0GCSqGSIb3DQEBBQUAA4IBAQCHRXIs53opzKM2rM8Qe8lcw524WK6hqy2EWrZHp78N7rU7/6DQ/I3hv3WhcDDIO04I2/Xhe88MLBaLoM367Ya+vy7CaLr14aLi/SfQszMA0ALBvMao+Fis0iVwFYq/NLgSXw+fgnpFskt8v8iQZ+4Kaal8U8e9sVgu8m0RgO7rzym1eRiIKpsKd1rh/SD7LbSN7M7TRL3QqF7ltw9sQhAAsQcRaBBF21pdWrqhiGZ+Eioo3hhgwNavH2agqz78ddHwrFpHFwrEeUk1OfpPb76MYIce7xIy/4oQNdg6fOq4l/FrajBv+WkzDVPaKm6r7YmwfLN/YMZBHXSR58oOGP9W/n-----END CERTIFICATE-----\"' # str | The certificate's contents.
    friendly_name = 'TestCert' # str | The certificate's friendly name. (optional)
    crt2 = 'crt_example' # str | The certificate file. (optional)
    friendly_name2 = 'friendly_name_example' # str | The certificate's friendly name. (optional)

    try:
        # Import SSL certificate
        api_response = api_instance.upload_cert(crt, friendly_name=friendly_name, crt2=crt2, friendly_name2=friendly_name2)
        print("The response of SSLCertificateManagementApi->upload_cert:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SSLCertificateManagementApi->upload_cert: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **crt** | **str**| The certificate&#39;s contents. | 
 **friendly_name** | **str**| The certificate&#39;s friendly name. | [optional] 
 **crt2** | **str**| The certificate file. | [optional] 
 **friendly_name2** | **str**| The certificate&#39;s friendly name. | [optional] 

### Return type

[**InlineResponse200449**](InlineResponse200449.md)

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

# **upload_key**
> InlineResponse200450 upload_key(key, friendly_name=friendly_name, crt=crt, friendly_name2=friendly_name2)

Import private key

This function uploads a private key.

**Note:**

Due to the limited field length of HTTP GET method calls, you **must** use
the HTTP POST method. For this reason, you **cannot** use a cPanel or Webmail
session URL to call this function.

**Important:**

When you disable the Calendars and Contacts, Receive Mail, Web Disk, Webmail,
**and** Web Server [roles](https://go.cpanel.net/howtouseserverprofiles#roles),
the system **disables** this function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200450 import InlineResponse200450
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
    api_instance = clientapi_cpanel.SSLCertificateManagementApi(api_client)
    key = '\"-----BEGIN RSA PRIVATE KEY-----\\nMIIEowIBAAKCAQEAyeiHvMuJuVk8ZEY6wMzUS1g0eWaHaIWmIRe+Qrn6SwiRrm1p\\npsJCiGPPPQGOSg4FzrMXqE0zsi/Tk3hUO/EEsi7CcZe8cUanjlUeXhiwrb86FCMF\\nOb9siRHQvlss7VCg8ZGXXTWZgf5yD3A1xPwdayYwF2Tc7GkNcZGUAI58geuYaq+U\\nGiLczRGZep1IQ0b1cZnqDvGMx6AS6hiDqLISjnmXYY2OhG6Uyp+SuinjYzLPJ6eO\\nN/7i9qqbcGmt0ssddmhR897+bTEom5SlSuyi03KZ9Rn4ZmNJgOsup9MclSBGxBys\\nb6MuuM3N0/tF5QuwmDc8H6h2rNBP9vGV7RTTXQIDAQABAoIBAFS/WVoRRLmbjxG3\\nuKl8UA9f8oaSVnu0vUpeoOl5Dmm4Kw2/tvzbxPlii3Xb1VGYGS/tVBy8atp74J6h\\nfxm5zHLN1afAPMR/F41ShPCSBHapMUOKf4MBqhjOdYOw2Way1RsQNSxWdxxtJIr+\\nWlNYTzDOUpk/KMvCPHZS2IBzTidpcFpDQ3pyDXjOoKJJH0EQWPtvxJNGrFqmU29D\\n9WBqQemHnDrzg3s7JzQ5cGpbbCE+QX8IckNkslAkyhm771CtqWdeo+c45e6YfGcx\\nKuAy1zGSVzQBuitzYoMUOL5olXLEj8fHzXd/cZP4yCyyabcGz2vi6luxF+28l1OL\\nG1axyLECgYEA+bD5B+Y/Dp5hZ/uVR1bbvyraQpwbDesS1zgnJ53KOIl926dnWzIt\\nUvM46+c9IF+UJrtzwIB6IvjAQioNFrK36bHgNGzNf9WQ54NN172qveaFLdW34z/i\\nGR2ix/efm9OC41QREQ/5IKV07TibCwVazVBWascMPkH7FnguTvTCiosCgYEAzwJ+\\nGPlIWjK+sqkK5JMUyuH43qAvgVfkZV906JpNRQH0Mob3bC0nXN95EoTwWXk68ULT\\no1GHv9XLbj8e+Ok7kpJQZT5vEZnDN+cy3jdTLCvcjU5Q3ToImOTp9isSAFWRTbtk\\nyabLNoIIsTR/ZwwPFTZcRiK2d8k7ZhcRKdfGnrcCgYAPZ06FoTukoDqsGoYkB4S4\\n72DVmSHGIwlfg5ROylouULUV9ubWZmsLYfvR+cr4k0zlcsz6RDLEs4nQyx1RmCbm\\nYNXPBiNLTpaI4b3MoGPHIVB3+mZEu60sFXr0UR9kkpDRi18eKVkaHXrwI3zVGjh2\\n0Az0u2DS+mkOAs4AivLxbwKBgQC0XPqbLc+Bb0dCCREJmLD8GCkrZ6wcaQUB4krN\\nQ2vhnVM0Fu5K3Yi3XapynUuA2aSmgtA9MxMw7MkjlHGa9DPIgBz2KZDCaBN0iMeE\\nX/XivZCbucmxBxhohsLmjh5QFj3U2Vp2bBIQuvlx1EjQ8uvNUqDRJvuOoNFVIPH+\\nYBeZPwKBgA//kXfNtNMHOpch699i3rgTzbRFDmGwsr1otzvJsXw7Pr2bM4WIzUJy\\nG2SUSUlQRSZK4+BBKT9S0d7TynJD6X/6R7IBotZbfXs1myYxEsKj89/BQmr47x2h\\nHjYVCClNoJlsbd5C2yu1R3PikweWGoVaxE3c+AN5knqjwJ0g21Cf\\n-----END RSA PRIVATE KEY-----\"' # str | The key's contents.
    friendly_name = 'TestKey' # str | The key's friendly name. (optional)
    crt = 'crt_example' # str | The key's contents. (optional)
    friendly_name2 = 'friendly_name_example' # str | The key's friendly name. (optional)

    try:
        # Import private key
        api_response = api_instance.upload_key(key, friendly_name=friendly_name, crt=crt, friendly_name2=friendly_name2)
        print("The response of SSLCertificateManagementApi->upload_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SSLCertificateManagementApi->upload_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| The key&#39;s contents. | 
 **friendly_name** | **str**| The key&#39;s friendly name. | [optional] 
 **crt** | **str**| The key&#39;s contents. | [optional] 
 **friendly_name2** | **str**| The key&#39;s friendly name. | [optional] 

### Return type

[**InlineResponse200450**](InlineResponse200450.md)

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

