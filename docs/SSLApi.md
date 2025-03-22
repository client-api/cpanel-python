# clientapi_cpanel.SSLApi

All URIs are relative to *https://cpanel-server.tld:2083/execute*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_autossl_excluded_domains**](SSLApi.md#add_autossl_excluded_domains) | **GET** /SSL/add_autossl_excluded_domains | Disable AutoSSL for domains
[**can_ssl_redirect**](SSLApi.md#can_ssl_redirect) | **GET** /SSL/can_ssl_redirect | Return whether domains can redirect to secure URL
[**check_shared_cert**](SSLApi.md#check_shared_cert) | **GET** /SSL/check_shared_cert | Return whether shared SSL certificate exists
[**delete_cert**](SSLApi.md#delete_cert) | **GET** /SSL/delete_cert | Delete SSL certificate
[**delete_csr**](SSLApi.md#delete_csr) | **GET** /SSL/delete_csr | Delete certificate signing request
[**delete_key**](SSLApi.md#delete_key) | **GET** /SSL/delete_key | Delete private key
[**delete_ssl**](SSLApi.md#delete_ssl) | **GET** /SSL/delete_ssl | Remove SSL for domain
[**disable_mail_sni**](SSLApi.md#disable_mail_sni) | **GET** /SSL/disable_mail_sni | Disable SNI mail services for domain
[**enable_mail_sni**](SSLApi.md#enable_mail_sni) | **GET** /SSL/enable_mail_sni | Enable SNI mail services for domain
[**fetch_best_for_domain**](SSLApi.md#fetch_best_for_domain) | **GET** /SSL/fetch_best_for_domain | Request best SSL certificate
[**fetch_cert_info**](SSLApi.md#fetch_cert_info) | **GET** /SSL/fetch_cert_info | Return SSL certificate information
[**fetch_certificates_for_fqdns**](SSLApi.md#fetch_certificates_for_fqdns) | **GET** /SSL/fetch_certificates_for_fqdns | Return SSL certificate information for all FQDN
[**fetch_key_and_cabundle_for_certificate**](SSLApi.md#fetch_key_and_cabundle_for_certificate) | **POST** /SSL/fetch_key_and_cabundle_for_certificate | Return private key and CA bundle
[**find_certificates_for_key**](SSLApi.md#find_certificates_for_key) | **GET** /SSL/find_certificates_for_key | Return SSL certificate for private key
[**find_csrs_for_key**](SSLApi.md#find_csrs_for_key) | **GET** /SSL/find_csrs_for_key | Return private key&#39;s certificate signing requests
[**generate_cert**](SSLApi.md#generate_cert) | **GET** /SSL/generate_cert | Create self-signed SSL certificate
[**generate_csr**](SSLApi.md#generate_csr) | **GET** /SSL/generate_csr | Create certificate signing request
[**get_autossl_excluded_domains**](SSLApi.md#get_autossl_excluded_domains) | **GET** /SSL/get_autossl_excluded_domains | Return AutoSSL disabled domains
[**get_autossl_problems**](SSLApi.md#get_autossl_problems) | **GET** /SSL/get_autossl_problems | Return domains with AutoSSL problems
[**get_cabundle**](SSLApi.md#get_cabundle) | **GET** /SSL/get_cabundle | Return certificate&#39;s CA bundle and hostname
[**get_cn_name**](SSLApi.md#get_cn_name) | **GET** /SSL/get_cn_name | Request best SSL domain for service
[**install_ssl**](SSLApi.md#install_ssl) | **GET** /SSL/install_ssl | Install SSL certificate
[**installed_host**](SSLApi.md#installed_host) | **GET** /SSL/installed_host | Return SSL certificate&#39;s info for dedicated IP
[**installed_hosts**](SSLApi.md#installed_hosts) | **GET** /SSL/installed_hosts | Return domains with SSL certificate information
[**is_autossl_check_in_progress**](SSLApi.md#is_autossl_check_in_progress) | **GET** /SSL/is_autossl_check_in_progress | Return whether AutoSSL check in progress
[**is_mail_sni_supported**](SSLApi.md#is_mail_sni_supported) | **GET** /SSL/is_mail_sni_supported | Return whether mail SNI is enabled
[**is_sni_supported**](SSLApi.md#is_sni_supported) | **GET** /SSL/is_sni_supported | Return whether Apache web server supports mail SNI
[**list_certs**](SSLApi.md#list_certs) | **GET** /SSL/list_certs | Return all SSL certificates
[**list_csrs**](SSLApi.md#list_csrs) | **GET** /SSL/list_csrs | Return all certificate signing requests
[**list_keys**](SSLApi.md#list_keys) | **GET** /SSL/list_keys | Return all private keys
[**list_ssl_items**](SSLApi.md#list_ssl_items) | **GET** /SSL/list_ssl_items | Return SSL-related items
[**mail_sni_status**](SSLApi.md#mail_sni_status) | **GET** /SSL/mail_sni_status | Return status of domain&#39;s SNI mail services
[**rebuild_mail_sni_config**](SSLApi.md#rebuild_mail_sni_config) | **GET** /SSL/rebuild_mail_sni_config | Start SNI configuration files rebuild
[**rebuildssldb**](SSLApi.md#rebuildssldb) | **GET** /SSL/rebuildssldb | Start SSL database rebuild
[**remove_autossl_excluded_domains**](SSLApi.md#remove_autossl_excluded_domains) | **GET** /SSL/remove_autossl_excluded_domains | Enable AutoSSL for specifed domains
[**s_sl_generate_key**](SSLApi.md#s_sl_generate_key) | **GET** /SSL/generate_key | Create private key
[**s_sl_set_default_key_type**](SSLApi.md#s_sl_set_default_key_type) | **GET** /SSL/set_default_key_type | Update SSL TLS key type
[**set_autossl_excluded_domains**](SSLApi.md#set_autossl_excluded_domains) | **GET** /SSL/set_autossl_excluded_domains | Disable AutoSSL for specifed domains
[**set_cert_friendly_name**](SSLApi.md#set_cert_friendly_name) | **GET** /SSL/set_cert_friendly_name | Update SSL certificate&#39;s friendly name
[**set_csr_friendly_name**](SSLApi.md#set_csr_friendly_name) | **GET** /SSL/set_csr_friendly_name | Update certificate signing request&#39;s friendly name
[**set_key_friendly_name**](SSLApi.md#set_key_friendly_name) | **GET** /SSL/set_key_friendly_name | Update private key&#39;s friendly name
[**set_primary_ssl**](SSLApi.md#set_primary_ssl) | **GET** /SSL/set_primary_ssl | Update SSL website for dedicated IP address
[**show_cert**](SSLApi.md#show_cert) | **GET** /SSL/show_cert | Export SSL certificate
[**show_csr**](SSLApi.md#show_csr) | **GET** /SSL/show_csr | Export certificate signing request
[**show_key**](SSLApi.md#show_key) | **GET** /SSL/show_key | Export private key
[**start_autossl_check**](SSLApi.md#start_autossl_check) | **GET** /SSL/start_autossl_check | Start AutoSSL for current user
[**toggle_ssl_redirect_for_domains**](SSLApi.md#toggle_ssl_redirect_for_domains) | **GET** /SSL/toggle_ssl_redirect_for_domains | Enable or disable secure redirects
[**upload_cert**](SSLApi.md#upload_cert) | **POST** /SSL/upload_cert | Import SSL certificate
[**upload_key**](SSLApi.md#upload_key) | **POST** /SSL/upload_key | Import private key


# **add_autossl_excluded_domains**
> InlineResponse200402 add_autossl_excluded_domains(domains)

Disable AutoSSL for domains

This function disables AutoSSL for the domains that you specify.

**Important:**

When you disable the Calendars and Contacts, Receive Mail, Web Disk, Webmail, and Web Server [roles](https://go.cpanel.net/serverroles), the system **disables** this function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200402 import InlineResponse200402
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
    api_instance = clientapi_cpanel.SSLApi(api_client)
    domains = 'example.com,example2.com' # str | A comma-separated list of domains for which to disable AutoSSL.  **Note:**  For browser-based calls, use a URI encoded comma (`%2C`).

    try:
        # Disable AutoSSL for domains
        api_response = api_instance.add_autossl_excluded_domains(domains)
        print("The response of SSLApi->add_autossl_excluded_domains:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SSLApi->add_autossl_excluded_domains: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domains** | **str**| A comma-separated list of domains for which to disable AutoSSL.  **Note:**  For browser-based calls, use a URI encoded comma (&#x60;%2C&#x60;). | 

### Return type

[**InlineResponse200402**](InlineResponse200402.md)

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
    api_instance = clientapi_cpanel.SSLApi(api_client)

    try:
        # Return whether domains can redirect to secure URL
        api_response = api_instance.can_ssl_redirect()
        print("The response of SSLApi->can_ssl_redirect:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SSLApi->can_ssl_redirect: %s\n" % e)
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
    api_instance = clientapi_cpanel.SSLApi(api_client)

    try:
        # Return whether shared SSL certificate exists
        api_response = api_instance.check_shared_cert()
        print("The response of SSLApi->check_shared_cert:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SSLApi->check_shared_cert: %s\n" % e)
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
    api_instance = clientapi_cpanel.SSLApi(api_client)
    friendly_name = 'TestCert' # str | The certificate's friendly name. (optional)
    id = 'example_com_cb497_a394d_1397249671_d1272da8f13a1fd837493a5ad1f0a0f3' # str | The certificate's ID. (optional)

    try:
        # Delete SSL certificate
        api_response = api_instance.delete_cert(friendly_name=friendly_name, id=id)
        print("The response of SSLApi->delete_cert:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SSLApi->delete_cert: %s\n" % e)
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
    api_instance = clientapi_cpanel.SSLApi(api_client)
    friendly_name = 'TestCSR' # str | The CSR's friendly name. (optional)
    id = 'example_com_e095f_0ab2f_ebcbe4a571276f48562241411556647f' # str | The CSR's ID. (optional)

    try:
        # Delete certificate signing request
        api_response = api_instance.delete_csr(friendly_name=friendly_name, id=id)
        print("The response of SSLApi->delete_csr:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SSLApi->delete_csr: %s\n" % e)
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
    api_instance = clientapi_cpanel.SSLApi(api_client)
    friendly_name = 'TestKey' # str | The private key's friendly name. (optional)
    id = 'example_com_e095f_0ab2f_ebcbe4a571276f48562241411556647f' # str | The private key's ID. (optional)

    try:
        # Delete private key
        api_response = api_instance.delete_key(friendly_name=friendly_name, id=id)
        print("The response of SSLApi->delete_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SSLApi->delete_key: %s\n" % e)
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
    api_instance = clientapi_cpanel.SSLApi(api_client)
    domain = 'example.com' # str | The domain name.

    try:
        # Remove SSL for domain
        api_response = api_instance.delete_ssl(domain)
        print("The response of SSLApi->delete_ssl:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SSLApi->delete_ssl: %s\n" % e)
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

# **disable_mail_sni**
> InlineResponse200409 disable_mail_sni(domains)

Disable SNI mail services for domain

This function disables SNI mail services on the specified domains.

**Note:**

  Mail SNI is **always** enabled.

  * After you change the SNI status, you **must** run UAPI's `rebuild_mail_sni_config` function.
  * Functions that enable Mail SNI succeed with a warning that Mail SNI is always enabled.
  * Functions that disable Mail SNI fail and make no changes.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200409 import InlineResponse200409
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
    api_instance = clientapi_cpanel.SSLApi(api_client)
    domains = 'example.com|example1.com|example2.com' # str | A pipe-delimited list of the account's domains.

    try:
        # Disable SNI mail services for domain
        api_response = api_instance.disable_mail_sni(domains)
        print("The response of SSLApi->disable_mail_sni:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SSLApi->disable_mail_sni: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domains** | **str**| A pipe-delimited list of the account&#39;s domains. | 

### Return type

[**InlineResponse200409**](InlineResponse200409.md)

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

# **enable_mail_sni**
> InlineResponse200410 enable_mail_sni(domains)

Enable SNI mail services for domain

This function enables SNI mail services on the specified domains.

**Warning:**

Mail SNI is **always** enabled.
* Mail SNI is **not** compatible with Webmail and will **not** function for any Webmail connection. Webmail connections use the cPanel service SSL certificate.
* Functions that enable Mail SNI succeed with a warning that Mail SNI is always enabled.
* Functions that disable Mail SNI fail and make no changes.

**Important:**

  When you disable the *Calendars and Contacts*, *Mail Receive*, *Web Disk*, *Webmail*, **and** *Web Server* [roles](https://go.cpanel.net/howtouseserverprofiles#roles), the system **disables** this function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200410 import InlineResponse200410
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
    api_instance = clientapi_cpanel.SSLApi(api_client)
    domains = 'example.com|example1.com|example2.com' # str | A pipe-delimited list of the account's domains.

    try:
        # Enable SNI mail services for domain
        api_response = api_instance.enable_mail_sni(domains)
        print("The response of SSLApi->enable_mail_sni:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SSLApi->enable_mail_sni: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domains** | **str**| A pipe-delimited list of the account&#39;s domains. | 

### Return type

[**InlineResponse200410**](InlineResponse200410.md)

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
    api_instance = clientapi_cpanel.SSLApi(api_client)
    domain = 'example.com' # str | The domain name.

    try:
        # Request best SSL certificate
        api_response = api_instance.fetch_best_for_domain(domain)
        print("The response of SSLApi->fetch_best_for_domain:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SSLApi->fetch_best_for_domain: %s\n" % e)
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
    api_instance = clientapi_cpanel.SSLApi(api_client)
    friendly_name = 'TestCert' # str | The certificate's human readable name.
    id = 'example_com_cb497_a394d_1397249671_d1272da8f13a1fd837493a5ad1f0a0f3' # str | The certificate's ID.

    try:
        # Return SSL certificate information
        api_response = api_instance.fetch_cert_info(friendly_name, id)
        print("The response of SSLApi->fetch_cert_info:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SSLApi->fetch_cert_info: %s\n" % e)
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
    api_instance = clientapi_cpanel.SSLApi(api_client)
    domains = 'domains=example1.com,example2.com' # str | A domain or comma-delimited list of domains for which to retrieve information.

    try:
        # Return SSL certificate information for all FQDN
        api_response = api_instance.fetch_certificates_for_fqdns(domains)
        print("The response of SSLApi->fetch_certificates_for_fqdns:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SSLApi->fetch_certificates_for_fqdns: %s\n" % e)
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
    api_instance = clientapi_cpanel.SSLApi(api_client)
    certificate = '-----BEGIN CERTIFICATE-----MIIDcTCCAlmgAwIBAgIFAU+BNVgwDQYJKoZIhvcNAQEFBQAwUTESMBAGA1UEAwwJc2lza28udGxkMQswCQYDVQQGEwJVUzEPMA0GA1UECgwGY1BhbmVsMQswCQYDVQQIDAJUWDEQMA4GA1UEBwwHSG91c3RvbjAeFw0xNDEwMDYyMjI2MTlaFw0xNTEwMDYyMjI2MTlaMFExEjAQBgNVBAMMCXNpc2tvLnRsZDELMAkGA1UEBhMCVVMxDzANBgNVBAoMBmNQYW5lbDELMAkGA1UECAwCVFgxEDAOBgNVBAcMB0hvdXN0b24wggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAwggEKAoIBAQC9zx6zGiHdmWA0dKtoXmJiWXpZ9E3PXx3YHsjFEWW7e5pH0vZ+jVMzDmm5nsJ7RXrAkZO1IvpIpVLvoQfiJOWVvkD+o9fWvoK1tWJS72FSgPju+58mA2ieBuc87A790Pzuv1P3NR3zFLAjUR99zkHR1fpri/daM3PBWO8ET48FWkyU1kOeZaUlF67/+wrEiNgg+t1qhKOCAB61PdNVkLaSGHimksuC+Czk8Kq9nuS0E0TCnDtjjEyJ455FUcaCfczlTb8xkB/F9ORe74yTzD+vlk0tFMG6PLj/ajIwWqwO0qmQ8wX3NRxkWgGz5kVO1wrVJarKQ5EYQ3/mgvit0v6dAgMBAAGjUDBOMB0GA1UdDgQWBBRw+wKBo34+bgexjAa3EMDsgSCd7zAfBgNVHSMEGDAWgBRw+wKBo34+bgexjAa3EMDsgSCd7zAMBgNVHRMEBTADAQH/MA0GCSqGSIb3DQEBBQUAA4IBAQCHRXIs53opzKM2rM8Qe8lcw524WK6hqy2EWrZHp78N7rU7/6DQ/I3hv3WhcDDIO04I2/Xhe88MLBaLoM367Ya+vy7CaLr14aLi/SfQszMA0ALBvMao+Fis0iVwFYq/NLgSXw+fgnpFskt8v8iQZ+4Kaal8U8e9sVgu8m0RgO7rzym1eRiIKpsKd1rh/SD7LbSN7M7TRL3QqF7ltw9sQhAAsQcRaBBF21pdWrqhiGZ+Eioo3hhgwNavH2agqz78ddHwrFpHFwrEeUk1OfpPb76MYIce7xIy/4oQNdg6fOq4l/FrajBv+WkzDVPaKm6r7YmwfLN/YMZBHXSR58oOGP9W-----END CERTIFICATE-----' # str | An SSL certificate.
    certificate2 = 'certificate_example' # str | The certificate file. (optional)

    try:
        # Return private key and CA bundle
        api_response = api_instance.fetch_key_and_cabundle_for_certificate(certificate, certificate2=certificate2)
        print("The response of SSLApi->fetch_key_and_cabundle_for_certificate:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SSLApi->fetch_key_and_cabundle_for_certificate: %s\n" % e)
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
    api_instance = clientapi_cpanel.SSLApi(api_client)
    friendly_name = 'TestKey' # str | The key's friendly name. (optional)
    id = 'example_com_cb497_a394d_1397249671_d1272da8f13a1fd837493a5ad1f0a0f3' # str | The key's ID. (optional)

    try:
        # Return SSL certificate for private key
        api_response = api_instance.find_certificates_for_key(friendly_name=friendly_name, id=id)
        print("The response of SSLApi->find_certificates_for_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SSLApi->find_certificates_for_key: %s\n" % e)
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
    api_instance = clientapi_cpanel.SSLApi(api_client)
    friendly_name = 'TestKey' # str | The key's friendly name. (optional)
    id = 'example_com_cb497_a394d_1397249671_d1272da8f13a1fd837493a5ad1f0a0f3' # str | The key's ID. (optional)

    try:
        # Return private key's certificate signing requests
        api_response = api_instance.find_csrs_for_key(friendly_name=friendly_name, id=id)
        print("The response of SSLApi->find_csrs_for_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SSLApi->find_csrs_for_key: %s\n" % e)
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
    api_instance = clientapi_cpanel.SSLApi(api_client)
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
        print("The response of SSLApi->generate_cert:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SSLApi->generate_cert: %s\n" % e)
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
    api_instance = clientapi_cpanel.SSLApi(api_client)
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
        print("The response of SSLApi->generate_csr:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SSLApi->generate_csr: %s\n" % e)
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

# **get_autossl_excluded_domains**
> InlineResponse200420 get_autossl_excluded_domains()

Return AutoSSL disabled domains

This function lists the domains with AutoSSL disabled.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200420 import InlineResponse200420
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
    api_instance = clientapi_cpanel.SSLApi(api_client)

    try:
        # Return AutoSSL disabled domains
        api_response = api_instance.get_autossl_excluded_domains()
        print("The response of SSLApi->get_autossl_excluded_domains:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SSLApi->get_autossl_excluded_domains: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**InlineResponse200420**](InlineResponse200420.md)

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

# **get_autossl_problems**
> InlineResponse200421 get_autossl_problems()

Return domains with AutoSSL problems

This function retrieves a list of domains that possess AutoSSL problems.

**Important:**

When you disable the [Calendars and Contacts, Receive Mail, Web Disk, Webmail, and Web Server roles](https://go.cpanel.net/serverroles), the system **disables** this function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200421 import InlineResponse200421
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
    api_instance = clientapi_cpanel.SSLApi(api_client)

    try:
        # Return domains with AutoSSL problems
        api_response = api_instance.get_autossl_problems()
        print("The response of SSLApi->get_autossl_problems:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SSLApi->get_autossl_problems: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**InlineResponse200421**](InlineResponse200421.md)

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
    api_instance = clientapi_cpanel.SSLApi(api_client)
    cert = '-----BEGIN CERTIFICATE-----\\r\\nMIIDcTCCAlmgAwIBAgIFAU+BNVgwDQYJKoZIhvcNAQEFBQAwUTESMBAGA1UEAwwJ\\r\\nc2lza28udGxkMQswCQYDVQQGEwJVUzEPMA0GA1UECgwGY1BhbmVsMQswCQYDVQQI\\r\\nDAJUWDEQMA4GA1UEBwwHSG91c3RvbjAeFw0xNDEwMDYyMjI2MTlaFw0xNTEwMDYy\\r\\nMjI2MTlaMFExEjAQBgNVBAMMCXNpc2tvLnRsZDELMAkGA1UEBhMCVVMxDzANBgNV\\r\\nBAoMBmNQYW5lbDELMAkGA1UECAwCVFgxEDAOBgNVBAcMB0hvdXN0b24wggEiMA0G\\r\\nCSqGSIb3DQEBAQUAA4IBDwAwggEKAoIBAQC9zx6zGiHdmWA0dKtoXmJiWXpZ9E3P\\r\\nXx3YHsjFEWW7e5pH0vZ+jVMzDmm5nsJ7RXrAkZO1IvpIpVLvoQfiJOWVvkD+o9fW\\r\\nvoK1tWJS72FSgPju+58mA2ieBuc87A790Pzuv1P3NR3zFLAjUR99zkHR1fpri/da\\r\\nM3PBWO8ET48FWkyU1kOeZaUlF67/+wrEiNgg+t1qhKOCAB61PdNVkLaSGHimksuC\\r\\n+Czk8Kq9nuS0E0TCnDtjjEyJ455FUcaCfczlTb8xkB/F9ORe74yTzD+vlk0tFMG6\\r\\nPLj/ajIwWqwO0qmQ8wX3NRxkWgGz5kVO1wrVJarKQ5EYQ3/mgvit0v6dAgMBAAGj\\r\\nUDBOMB0GA1UdDgQWBBRw+wKBo34+bgexjAa3EMDsgSCd7zAfBgNVHSMEGDAWgBRw\\r\\n+wKBo34+bgexjAa3EMDsgSCd7zAMBgNVHRMEBTADAQH/MA0GCSqGSIb3DQEBBQUA\\r\\nA4IBAQCHRXIs53opzKM2rM8Qe8lcw524WK6hqy2EWrZHp78N7rU7/6DQ/I3hv3Wh\\r\\ncDDIO04I2/Xhe88MLBaLoM367Ya+vy7CaLr14aLi/SfQszMA0ALBvMao+Fis0iVw\\r\\nFYq/NLgSXw+fgnpFskt8v8iQZ+4Kaal8U8e9sVgu8m0RgO7rzym1eRiIKpsKd1rh\\r\\n/SD7LbSN7M7TRL3QqF7ltw9sQhAAsQcRaBBF21pdWrqhiGZ+Eioo3hhgwNavH2ag\\r\\nqz78ddHwrFpHFwrEeUk1OfpPb76MYIce7xIy/4oQNdg6fOq4l/FrajBv+WkzDVPa\\r\\nKm6r7YmwfLN/YMZBHXSR58oOGP9W\\r\\n-----END CERTIFICATE-----' # str | The certificate's text.

    try:
        # Return certificate's CA bundle and hostname
        api_response = api_instance.get_cabundle(cert)
        print("The response of SSLApi->get_cabundle:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SSLApi->get_cabundle: %s\n" % e)
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
    api_instance = clientapi_cpanel.SSLApi(api_client)
    domain = clientapi_cpanel.Domain() # Domain | A domain name, cPanel username, or email address.
    service = 'cpanel' # str | The service's name.  * `cpanel` * `imap` * `pop3` * `smtp`
    add_mail_subdomain = 0 # int | Whether to append `mail` to the `domain` value to find the best match.  For example, if you specify the domain `example.com` and call this parameter, the function only searches the `mail.example.com` service domains.  * `1` — Append `mail` to the `domain` value during the search. * `0` — Match on the specified `domain` value **only**. (optional) (default to 0)

    try:
        # Request best SSL domain for service
        api_response = api_instance.get_cn_name(domain, service, add_mail_subdomain=add_mail_subdomain)
        print("The response of SSLApi->get_cn_name:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SSLApi->get_cn_name: %s\n" % e)
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
    api_instance = clientapi_cpanel.SSLApi(api_client)
    cert = '-----BEGIN%20CERTIFICATE-----%0AMIIEEzCCAvugAwIBAgIJALF%2FjFpw6p1bMA0GCSqGSIb3DQEBBQUAMIGfMRYwFAYD%0AVQQDEw10ZXN0c2ltb24uY29tMRYwFAYDVQQLEw1Eb2N1bWVudGF0aW9uMQswCQYD%0AVQQGEwJVUzEoMCYGCSqGSIb3DQEJARYZbGF1cmVuY2Uuc2ltb25AY3BhbmVsLm5l%0AdDEUMBIGA1UEChMLY1BhbmVsIEluYy4xDjAMBgNVBAgTBVRleGFzMRAwDgYDVQQH%0AEwdIb3VzdG9uMB4XDTEzMDUxNzE2MTMwN1oXDTE0MDUxNzE2MTMwN1owgZ8xFjAU%0ABgNVBAMTDXRlc3RzaW1vbi5jb20xFjAUBgNVBAsTDURvY3VtZW50YXRpb24xCzAJ%0ABgNVBAYTAlVTMSgwJgYJKoZIhvcNAQkBFhlsYXVyZW5jZS5zaW1vbkBjcGFuZWwu%0AbmV0MRQwEgYDVQQKEwtjUGFuZWwgSW5jLjEOMAwGA1UECBMFVGV4YXMxEDAOBgNV%0ABAcTB0hvdXN0b24wggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAwggEKAoIBAQDRO0AP%0AN5XtjDqkEyJ6ctfYqUtt9yUXyRuCETFjW6opNLSmZSHeF6L2aZka646lhj02CFyl%0AkzsNSxysN66tY%2BWZcTmvgPisJdQFpFvjroJZgDjYRV0QqokKdRy%2F5BU0%2BtHXoYpj%0A9JOQlbvEWxiGR3R80sL1ma4AfSE6Gv8M%2FPULTadan51eHaikXqjOXdPJQKuWP3g9%0AFnIuf38WRYwzGrre88qsZrpsMrADX5dotHWgqAf7Tap6xfA4CUAgQo9tldariuVi%0ABz%2BsRJ%2FSjgxnhw1HYWGttBuBZFhMpdHpPnTJ7DIFMd%2FFN5gG%2Ftah30SapWpo35Ux%0A3BpJcdUjtazy82K5AgMBAAGjUDBOMB0GA1UdDgQWBBQAlv7%2FtALOYb7zAXbYG2%2B9%0AAMI3xjAfBgNVHSMEGDAWgBQAlv7%2FtALOYb7zAXbYG2%2B9AMI3xjAMBgNVHRMEBTAD%0AAQH%2FMA0GCSqGSIb3DQEBBQUAA4IBAQCxzpe71Hc7Es0dqIN7bhIFYIIgcr6wxM6a%0Aa9d%2BQG%2BQPH0x0KAqV8EgUbZysvyxEF0bPxW3ZAr1Is1wk80PMuU3bToFFVbFFIIr%0AHRNfKLGvxiMXnZA1c6L4N0lowvXHgZxTTUXtDFLXyrcwrLsvUErEV7rbizuxqfPw%0AcaRtXn4uc%2Bt6HYuW7yWesBauCWnJNiKbjN%2FF%2BuCTurN3QMAeWf3ZJtsfkAgk8dyq%0AR%2F83a3kDtSPrpt%2BjX%2BqdjKEpRtQ5Qpm6XT2gCOQPgnfiUtOCH419pp922P%2FAAGc%2B%0AZUhYoWcRWKw%2Fy6gI7Ru%2B%2B9%2B8%2BwkadL9EbKMZxhVwD5qVm4ZlWK2a%5Cr%5Cn%0A-----END%20CERTIFICATE-----' # str | The certificate to install.  **Note:**  * You **must** URI-encode this value. * You can use a Perl command to URI-encode your SSL certificate for this parameter. For example, you can use the following string, where `CERT.FILE` is the SSL certificate file:    ```$(perl -MURI::Escape -ne 'print uri_escape($_);' CERT.FILE)```
    domain = 'example.com' # str | The domain name.
    key = '-----BEGIN%20RSA%20PRIVATE%20KEY-----%0AMIIEpAIBAAKCAQEA4AVM6J4Qg3DIFWr%2FeJ5GRmIATYsJIepKbrDy70sq%2BudcO8R8%0Axxak0oMZ%2F9mUdpjSNK%2FfLVTuCO0kxTfQ9VUWJllX7ThD6Zh9ZvlC%2Fnf%2FOEZLm3Zb%0ABgu8rbC8E9wuDOkKbJLnINgdhtowIydLK2MJ%2B%2Bq62bFV89jkHWTMcKyyqHENo3h%0Ac%2Blkpd9vnp8rZTinaVb7nX26uQqAFZYRo%2BWU0G%2FNPsq40QVSMoqPxyEz4qXo0hvu%0AIlCXmzFZq%2F6fCVPEKPLhQgMmpdBkMz4dVOazREfqXdjMD2%2BQXSNiA1AwWr8l0r4r%0AtzlxEYDJIR41yXp0xMl3KoolxMyvLBqZy32niQIDAQABAoIBAQCmbGmhWmPsMeoC%0At1WJFxQgD4goE0U6k%2BKt7vjbOt14Pk6v%2FB2yjaju1wSGpO59WLS4%2FXrwI2se6IXr%0Amba7u3VUEgWXLriNHoLy7%2FSMNTs%2BZEKhAMG36eNe3tVdT7busTag31r6sEMGGwCs%0AIwpU%2Bazosk0oylWLEX%2Fm%2FuHWEs1eaIEWWWtgHB%2BKZrrP7Rr9RYfVQ144DxmOxS3C%0Aa9%2BmST62WqAVPR6POWGEfZqnZl%2FePWZPcQYbFrhwnnefNoYBl%2FbnLZBo8rbNWxAq%0AOEOuKfkrBzglKG%2F39WKPw8rj4JIVzY0yOuFCW6xCDWRkOrhU8Ol%2F3FvwDa3uJpkp%0AmgPr4TgxAoGBAPGPLmxSuOYR97mDAXxrs037F2GCbqWvI6m7%2FezWe9yn%2BbMpjSIW%0Afsgtq4FsyqzPueEkDdQWi3xh6nu2WI%2F1Tl875opGAqEIJMqss%2Fu11tnva5wzu1cC%0AL6H85A5%2BHMOBvP3sm6CObKcVw92h7kxynVIUJJWhjfeZMN8gBFFpKIVFAoGBAO1p%0AtXBmXLC%2FYKKvtHI3M16%2FZopvM8ZqU2HcAHaw214Refw9JJ%2Fe3%2FxTNfSerVTyCAQO%0A1AdWTzJKBN8jmSYv1Mk1D3RpQPNR7wVzi46KR081AU41uMpqIGVOwHtyVnW%2FZfLr%0Ac1DLIK8Cx8aHfoxffwzoMO5SEQSooeZfOLhsfDN1AoGBAKQTUEINsj%2B75psgbAr6%0AELGgItJ9yPBLVRr%2BcUzEpx9LDWVvjMihpP4NX1gq8EOPWT%2BewLHVmmsjCyV6xw8J%0AXXF8e2xif3in0m3D%2FwCzE7u2T06rKM3B017hKnrZmGoHnrqPU2osM4sOUpshWX6d%0Av1Q4EF1%2BfbK3YCW%2BVpCBsB9NAoGAQo%2BuhNLODee56iKkzpjXWCsFTq6ar3hD5F3P%0A63buKdNwhd2GlSPhXFbf%2B7M5GWW6BZk6rMvv7EOAVice2uvyFm8%2F4%2F1WbmF8R%2BT7%0ALX1rPLO5p%2Fm701QpvP11TabiwqRkqtSEQhSRF0AKTojSW%2FyyHCZFAawUhV%2FZ9EKi%0AHmKb97kCgYAyzmFc2it0HqnsOnRybop603nqMtWGTQO4cxa93HUDpYajuK2K3Dfr%0AxUj6lG3z%2FoKJGGE2JqgZ6LBAhNJtJWJu2ox3pKGE63QjLJnVwb8y1NFYpe%2FcrbLe%0APuBwIR0L7drXxfv7O5btY7h6QI2d1%2FUIAQPAWbxLoTM%2BndQ%2FuPEdfA%3D%3D%0A-----END%20RSA%20PRIVATE%20KEY-----' # str | The certificate's key.  **Note:**  * You **must** URI-encode this value. * You can use a Perl command to URI-encode your SSL certificate for this parameter. For example, you can use the following string, where `KEY.FILE` is the SSL certificate file:    ```$(perl -MURI::Escape -ne 'print uri_escape($_);' KEY.FILE)```
    cabundle = '-----BEGIN%20CERTIFICATE-----%0AMIIB%2BjCCAWMCAgGjMA0GCSqGSIb3DQEBBAUAMEUxCzAJBgNVBAYTAlVTMRgwFgYD%0AVQQKEw9HVEUgQ29ycG9yYXRpb24xHDAaBgNVBAMTE0dURSBDeWJlclRydXN0IFJv%0Ab3QwHhcNOTYwMjIzMjMwMTAwWhcNMDYwMjIzMjM1OTAwWjBFMQswCQYDVQQGEwJV%0AUzEYMBYGA1UEChMPR1RFIENvcnBvcmF0aW9uMRwwGgYDVQQDExNHVEUgQ3liZXJU%0AcnVzdCBSb290MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQC45k%2B625h8cXyv%0ARLfTD0bZZOWTwUKOx7pJjTUteueLveUFMVnGsS8KDPufpz%2BiCWaEVh43KRuH6X4M%0AypqfpX%2F1FZSj1aJGgthoTNE3FQZor734sLPwKfWVWgkWYXcKIiXUT0Wqx73llt%2F5%0A1KiOQswkwB6RJ0q1bQaAYznEol44AwIDAQABMA0GCSqGSIb3DQEBBAUAA4GBABKz%0AdcZfHeFhVYAA1IFLezEPI2PnPfMD%2BfQ2qLvZ46WXTeorKeDWanOB5sCJo9Px4KWl%0AIjeaY8JIILTbcuPI9tl8vrGvU9oUtCG41tWW4%2F5ODFlitppK%2BULdjG%2BBqXH%2F9Apy%0AbW1EDp3zdHSo1TRJ6V6e6bR64eVaH4QwnNOfpSXY%0A-----END%20CERTIFICATE-----' # str | The Certificate Authority (CA) bundle data, if the certificate requires it.  **Note:**  * You **must** URI-encode this value. * You can use a Perl command to URI-encode your SSL certificate for this parameter. For example, you can use the following string, where `CABUNDLE.FILE` is the SSL certificate file:    ```$(perl -MURI::Escape -ne 'print uri_escape($_);' CABUNDLE.FILE)``` (optional)

    try:
        # Install SSL certificate
        api_response = api_instance.install_ssl(cert, domain, key, cabundle=cabundle)
        print("The response of SSLApi->install_ssl:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SSLApi->install_ssl: %s\n" % e)
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
    api_instance = clientapi_cpanel.SSLApi(api_client)
    domain = 'example.com' # str | The domain name.  **Note:**  The parameter defaults to the account's main domain. (optional)
    verify_certificate = 0 # int | Verify the certificate. * `1` — Verify the certificate. * `0` — Do **not** verify the certificate. (optional) (default to 0)

    try:
        # Return SSL certificate's info for dedicated IP
        api_response = api_instance.installed_host(domain=domain, verify_certificate=verify_certificate)
        print("The response of SSLApi->installed_host:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SSLApi->installed_host: %s\n" % e)
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
    api_instance = clientapi_cpanel.SSLApi(api_client)

    try:
        # Return domains with SSL certificate information
        api_response = api_instance.installed_hosts()
        print("The response of SSLApi->installed_hosts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SSLApi->installed_hosts: %s\n" % e)
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

# **is_autossl_check_in_progress**
> InlineResponse200427 is_autossl_check_in_progress()

Return whether AutoSSL check in progress

This function verifies whether the `autossl_check` task is in progress for the current user.

**Important:**

When you disable the [Calendars and Contacts, Receive Mail, Web Disk, Webmail, and Web Server roles](https://go.cpanel.net/serverroles), the system **disables** this function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200427 import InlineResponse200427
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
    api_instance = clientapi_cpanel.SSLApi(api_client)

    try:
        # Return whether AutoSSL check in progress
        api_response = api_instance.is_autossl_check_in_progress()
        print("The response of SSLApi->is_autossl_check_in_progress:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SSLApi->is_autossl_check_in_progress: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**InlineResponse200427**](InlineResponse200427.md)

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

# **is_mail_sni_supported**
> InlineResponse200428 is_mail_sni_supported()

Return whether mail SNI is enabled

This function checks whether the sslinstall feature is enabled.

**Warning:**

Mail SNI is always enabled.
* Mail SNI is **not** compatible with Webmail and will **not** function for any Webmail connection. Webmail connections use the cPanel service SSL certificate.
* Functions that enable Mail SNI succeed with a warning that Mail SNI is always enabled.
* Functions that disable Mail SNI will fail and make no changes.

**Important:**

When you disable the [Calendars and Contacts, Receive Mail, Web Disk, Webmail, and Web Server roles](https://go.cpanel.net/serverroles), the system **disables** this function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200428 import InlineResponse200428
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
    api_instance = clientapi_cpanel.SSLApi(api_client)

    try:
        # Return whether mail SNI is enabled
        api_response = api_instance.is_mail_sni_supported()
        print("The response of SSLApi->is_mail_sni_supported:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SSLApi->is_mail_sni_supported: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**InlineResponse200428**](InlineResponse200428.md)

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

# **is_sni_supported**
> InlineResponse200429 is_sni_supported()

Return whether Apache web server supports mail SNI

This function checks whether the Apache web server supports SNI.

**Important:**

When you disable the [Calendars and Contacts, Receive Mail, Web Disk, Webmail, and Web Server roles](https://go.cpanel.net/serverroles), the system **disables** this function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200429 import InlineResponse200429
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
    api_instance = clientapi_cpanel.SSLApi(api_client)

    try:
        # Return whether Apache web server supports mail SNI
        api_response = api_instance.is_sni_supported()
        print("The response of SSLApi->is_sni_supported:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SSLApi->is_sni_supported: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**InlineResponse200429**](InlineResponse200429.md)

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
    api_instance = clientapi_cpanel.SSLApi(api_client)

    try:
        # Return all SSL certificates
        api_response = api_instance.list_certs()
        print("The response of SSLApi->list_certs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SSLApi->list_certs: %s\n" % e)
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
    api_instance = clientapi_cpanel.SSLApi(api_client)

    try:
        # Return all certificate signing requests
        api_response = api_instance.list_csrs()
        print("The response of SSLApi->list_csrs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SSLApi->list_csrs: %s\n" % e)
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
    api_instance = clientapi_cpanel.SSLApi(api_client)

    try:
        # Return all private keys
        api_response = api_instance.list_keys()
        print("The response of SSLApi->list_keys:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SSLApi->list_keys: %s\n" % e)
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
    api_instance = clientapi_cpanel.SSLApi(api_client)
    domains = 'domains=example1.com|example2.com' # str | The domain name or names. (optional)
    item = 'key' # str | The SSL item type or types. * `key` * `csr` * `crt` (optional) (default to 'key')

    try:
        # Return SSL-related items
        api_response = api_instance.list_ssl_items(domains=domains, item=item)
        print("The response of SSLApi->list_ssl_items:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SSLApi->list_ssl_items: %s\n" % e)
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

# **mail_sni_status**
> InlineResponse200434 mail_sni_status(domain)

Return status of domain's SNI mail services

This function retrieves the status of the domain's SNI mail services.

**Warning:**

Mail SNI is **not** compatible with Webmail and will not function for any Webmail connection. Webmail connections use the cPanel service SSL certificate.

**Note:**

Mail SNI is always enabled.
* Functions that enable Mail SNI succeed with a warning that Mail SNI is always enabled.
* Functions that disable Mail SNI fail and make no changes.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200434 import InlineResponse200434
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
    api_instance = clientapi_cpanel.SSLApi(api_client)
    domain = 'example.com' # str | The account's domain.

    try:
        # Return status of domain's SNI mail services
        api_response = api_instance.mail_sni_status(domain)
        print("The response of SSLApi->mail_sni_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SSLApi->mail_sni_status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**| The account&#39;s domain. | 

### Return type

[**InlineResponse200434**](InlineResponse200434.md)

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

# **rebuild_mail_sni_config**
> InlineResponse200435 rebuild_mail_sni_config(reload_dovecot=reload_dovecot)

Start SNI configuration files rebuild

This function rebuilds the SNI configuration files.

**Note:**

* You **must** run this function after you change the SNI status through the UAPI's `enable_mail_sni` or `disable_mail_sni` functions.
* Mail SNI is **always** enabled.
  * Functions that enable Mail SNI succeed with a warning that Mail SNI is always enabled. Functions that disable Mail SNI fail and make no changes.
  * Functions that disable Mail SNI will fail and make no changes.

**Important:**

 When you disable the _Calendars and Contacts_, _Receive Mail_, _Web Disk_, _Webmail_, **and**  _Web Server_ [roles](https://go.cpanel.net/serverroles), the system **disables** this function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200435 import InlineResponse200435
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
    api_instance = clientapi_cpanel.SSLApi(api_client)
    reload_dovecot = 1 # int | Whether to reload the Dovecot service after the system rebuilds the configuration files. * `1` - Reload Dovecot. * `0` - Do **not** reload Dovecot. (optional) (default to 1)

    try:
        # Start SNI configuration files rebuild
        api_response = api_instance.rebuild_mail_sni_config(reload_dovecot=reload_dovecot)
        print("The response of SSLApi->rebuild_mail_sni_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SSLApi->rebuild_mail_sni_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **reload_dovecot** | **int**| Whether to reload the Dovecot service after the system rebuilds the configuration files. * &#x60;1&#x60; - Reload Dovecot. * &#x60;0&#x60; - Do **not** reload Dovecot. | [optional] [default to 1]

### Return type

[**InlineResponse200435**](InlineResponse200435.md)

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
    api_instance = clientapi_cpanel.SSLApi(api_client)

    try:
        # Start SSL database rebuild
        api_response = api_instance.rebuildssldb()
        print("The response of SSLApi->rebuildssldb:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SSLApi->rebuildssldb: %s\n" % e)
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

# **remove_autossl_excluded_domains**
> InlineResponse200437 remove_autossl_excluded_domains(domains)

Enable AutoSSL for specifed domains

This function enables AutoSSL for the domains that you specify.

**Important:**

When you disable the [Calendars and Contacts, Receive Mail, Web Disk, Webmail, and Web Server roles](https://go.cpanel.net/serverroles), the system **disables** this function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200437 import InlineResponse200437
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
    api_instance = clientapi_cpanel.SSLApi(api_client)
    domains = 'domains=example1.com,example2.com' # str | Enable AutoSSL for this domain.

    try:
        # Enable AutoSSL for specifed domains
        api_response = api_instance.remove_autossl_excluded_domains(domains)
        print("The response of SSLApi->remove_autossl_excluded_domains:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SSLApi->remove_autossl_excluded_domains: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domains** | **str**| Enable AutoSSL for this domain. | 

### Return type

[**InlineResponse200437**](InlineResponse200437.md)

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
    api_instance = clientapi_cpanel.SSLApi(api_client)
    friendly_name = 'TestKey' # str | A friendly name for the new key.  This parameter defaults to the key's type, creation date, and creation time. (optional)
    keysize = 2048 # int | The key's modulus size.  **Note:**  Use the `keytype` parameter. (optional) (default to 2048)
    keytype = 'rsa-2048' # str | The key's type.  * `system` — The system's default value. * `rsa-2048` — 2,408-bit RSA. * `rsa-4096` — 4,096-bit RSA. * `ecdsa-prime256v1` — ECDSA prime256v1 (\"P-256\"). * `ecdsa-secp384r1` — ECDSA secp384r1 (\"P-384\").  This parameter defaults to the user's [default SSL/TLS key type](https://go.cpanel.net/cpaneldocsSSLTLS#default-ssl-tls-key-type).  **Note:**  If you do **not** use this parameter, the system defaults to the `keysize` parameter's default value. (optional)

    try:
        # Create private key
        api_response = api_instance.s_sl_generate_key(friendly_name=friendly_name, keysize=keysize, keytype=keytype)
        print("The response of SSLApi->s_sl_generate_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SSLApi->s_sl_generate_key: %s\n" % e)
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
    api_instance = clientapi_cpanel.SSLApi(api_client)
    type = 'ecdsa-prime256v1' # str | The key type to set.  * `system` — Use the system’s `ssl_default_key_type` value. * `rsa-2048` — 2,048-bit RSA. * `rsa-4096` — 4,096-bit RSA. * `ecdsa-prime256v1` — ECDSA prime256v1 (“P-256”). * `ecdsa-secp384r1` — ECDSA secp384r1 (“P-384”).

    try:
        # Update SSL TLS key type
        api_response = api_instance.s_sl_set_default_key_type(type)
        print("The response of SSLApi->s_sl_set_default_key_type:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SSLApi->s_sl_set_default_key_type: %s\n" % e)
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

# **set_autossl_excluded_domains**
> InlineResponse200438 set_autossl_excluded_domains(domains=domains)

Disable AutoSSL for specifed domains

This function disables AutoSSL for every domain that you specify.

**Warning:**

This function **replaces** the list of any domains that you previously excluded. To add domains to the list of excluded domains, use the UAPI function `SSL::add_autossl_excluded_domains`.

**Important:**

When you disable the the [Calendar and Contacts, Receive Mail, Web Disk, Webmail, and Web Server roles](https://go.cpanel.net/serverroles), the system **disables** this function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200438 import InlineResponse200438
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
    api_instance = clientapi_cpanel.SSLApi(api_client)
    domains = 'example.com,example.net' # str | A comma-separated list of domains for which to disable AutoSSL.  **Note:**  If you do not include this parameter, the function will **enable** AutoSSL for every domain on the account. (optional)

    try:
        # Disable AutoSSL for specifed domains
        api_response = api_instance.set_autossl_excluded_domains(domains=domains)
        print("The response of SSLApi->set_autossl_excluded_domains:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SSLApi->set_autossl_excluded_domains: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domains** | **str**| A comma-separated list of domains for which to disable AutoSSL.  **Note:**  If you do not include this parameter, the function will **enable** AutoSSL for every domain on the account. | [optional] 

### Return type

[**InlineResponse200438**](InlineResponse200438.md)

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
    api_instance = clientapi_cpanel.SSLApi(api_client)
    friendly_name = 'TestCert' # str | The certificate's friendly name.
    new_friendly_name = 'TestCert2' # str | The certificate's new friendly name.

    try:
        # Update SSL certificate's friendly name
        api_response = api_instance.set_cert_friendly_name(friendly_name, new_friendly_name)
        print("The response of SSLApi->set_cert_friendly_name:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SSLApi->set_cert_friendly_name: %s\n" % e)
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
    api_instance = clientapi_cpanel.SSLApi(api_client)
    friendly_name = 'TestCSR' # str | The CSR's friendly name.
    id = 'example_com_eda9d_543fb_a3009b4b01a592390866ab3a47c0df18' # str | The CSR's ID.  **Note:**  To retrieve a CSR's ID, use the UAPI `list_csrs` function.
    new_friendly_name = 'TestCSR2' # str | The CSR's new friendly name.

    try:
        # Update certificate signing request's friendly name
        api_response = api_instance.set_csr_friendly_name(friendly_name, id, new_friendly_name)
        print("The response of SSLApi->set_csr_friendly_name:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SSLApi->set_csr_friendly_name: %s\n" % e)
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
    api_instance = clientapi_cpanel.SSLApi(api_client)
    friendly_name = 'TestKey' # str | The key's friendly name.
    id = 'a9b72_63971_2cb6d8897b362cfb1548e047d8428b8d' # str | The key's ID.
    new_friendly_name = 'TestKey2' # str | The key's new friendly name.

    try:
        # Update private key's friendly name
        api_response = api_instance.set_key_friendly_name(friendly_name, id, new_friendly_name)
        print("The response of SSLApi->set_key_friendly_name:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SSLApi->set_key_friendly_name: %s\n" % e)
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
    api_instance = clientapi_cpanel.SSLApi(api_client)
    servername = 'hostname.example.com' # str | The primary SSL website's servername.

    try:
        # Update SSL website for dedicated IP address
        api_response = api_instance.set_primary_ssl(servername)
        print("The response of SSLApi->set_primary_ssl:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SSLApi->set_primary_ssl: %s\n" % e)
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
    api_instance = clientapi_cpanel.SSLApi(api_client)
    friendly_name = 'TestCert' # str | The certificate's friendly name. (optional)
    id = 'example_com_c69ce_37ff5_1397169490_169c717cb2c260281df792788accf041' # str | The certificate's ID. (optional)

    try:
        # Export SSL certificate
        api_response = api_instance.show_cert(friendly_name=friendly_name, id=id)
        print("The response of SSLApi->show_cert:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SSLApi->show_cert: %s\n" % e)
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
    api_instance = clientapi_cpanel.SSLApi(api_client)
    friendly_name = 'TestCSR' # str | The CSR's friendly name. (optional)
    id = 'example_com_e095f_0ab2f_ebcbe4a571276f48562241411556647f' # str | The CSR's ID. (optional)

    try:
        # Export certificate signing request
        api_response = api_instance.show_csr(friendly_name=friendly_name, id=id)
        print("The response of SSLApi->show_csr:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SSLApi->show_csr: %s\n" % e)
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
    api_instance = clientapi_cpanel.SSLApi(api_client)
    friendly_name = 'TestKey' # str | The key's friendly name.  **Note:**  You **must** use either the `id` or the `friendly_name` parameter. (optional)
    id = 'example_com_c69ce_37ff5_1397169490_169c717cb2c260281df792788accf041' # str | The key's ID.  **Note:**  You **must** use either the `id` or the `friendly_name` parameter. (optional)

    try:
        # Export private key
        api_response = api_instance.show_key(friendly_name=friendly_name, id=id)
        print("The response of SSLApi->show_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SSLApi->show_key: %s\n" % e)
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

# **start_autossl_check**
> InlineResponse200447 start_autossl_check()

Start AutoSSL for current user

This function initiates an [AutoSSL](https://go.cpanel.net/whmdocsManageAutoSSL) check for the user.

**Important:**

When you disable the Calendars and Contacts, Receive Mail, Web Disk, Webmail, and  Web Server [roles](https://go.cpanel.net/serverroles), the system **disables** this function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200447 import InlineResponse200447
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
    api_instance = clientapi_cpanel.SSLApi(api_client)

    try:
        # Start AutoSSL for current user
        api_response = api_instance.start_autossl_check()
        print("The response of SSLApi->start_autossl_check:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SSLApi->start_autossl_check: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**InlineResponse200447**](InlineResponse200447.md)

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
    api_instance = clientapi_cpanel.SSLApi(api_client)
    domains = 'main.example,addon.example,addon.main.example' # str | A comma-separated list of the cPanel account's domains for which to enable or disable secure redirects.  **Important:**  To enable or disable redirects for addon domains, you **must** pass the addon domain **and** its subdomain.
    state = 1 # int | Whether to enable or disable redirects for the specified domains.  * `1` — Enable. * `0` — Disable.

    try:
        # Enable or disable secure redirects
        api_response = api_instance.toggle_ssl_redirect_for_domains(domains, state)
        print("The response of SSLApi->toggle_ssl_redirect_for_domains:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SSLApi->toggle_ssl_redirect_for_domains: %s\n" % e)
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
    api_instance = clientapi_cpanel.SSLApi(api_client)
    crt = '\"-----BEGIN CERTIFICATE-----/nMIIDcTCCAlmgAwIBAgIFAU+BNVgwDQYJKoZIhvcNAQEFBQAwUTESMBAGA1UEAwwJc2lza28udGxkMQswCQYDVQQGEwJVUzEPMA0GA1UECgwGY1BhbmVsMQswCQYDVQQIDAJUWDEQMA4GA1UEBwwHSG91c3RvbjAeFw0xNDEwMDYyMjI2MTlaFw0xNTEwMDYyMjI2MTlaMFExEjAQBgNVBAMMCXNpc2tvLnRsZDELMAkGA1UEBhMCVVMxDzANBgNVBAoMBmNQYW5lbDELMAkGA1UECAwCVFgxEDAOBgNVBAcMB0hvdXN0b24wggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAwggEKAoIBAQC9zx6zGiHdmWA0dKtoXmJiWXpZ9E3PXx3YHsjFEWW7e5pH0vZ+jVMzDmm5nsJ7RXrAkZO1IvpIpVLvoQfiJOWVvkD+o9fWvoK1tWJS72FSgPju+58mA2ieBuc87A790Pzuv1P3NR3zFLAjUR99zkHR1fpri/daM3PBWO8ET48FWkyU1kOeZaUlF67/+wrEiNgg+t1qhKOCAB61PdNVkLaSGHimksuC+Czk8Kq9nuS0E0TCnDtjjEyJ455FUcaCfczlTb8xkB/F9ORe74yTzD+vlk0tFMG6PLj/ajIwWqwO0qmQ8wX3NRxkWgGz5kVO1wrVJarKQ5EYQ3/mgvit0v6dAgMBAAGjUDBOMB0GA1UdDgQWBBRw+wKBo34+bgexjAa3EMDsgSCd7zAfBgNVHSMEGDAWgBRw+wKBo34+bgexjAa3EMDsgSCd7zAMBgNVHRMEBTADAQH/MA0GCSqGSIb3DQEBBQUAA4IBAQCHRXIs53opzKM2rM8Qe8lcw524WK6hqy2EWrZHp78N7rU7/6DQ/I3hv3WhcDDIO04I2/Xhe88MLBaLoM367Ya+vy7CaLr14aLi/SfQszMA0ALBvMao+Fis0iVwFYq/NLgSXw+fgnpFskt8v8iQZ+4Kaal8U8e9sVgu8m0RgO7rzym1eRiIKpsKd1rh/SD7LbSN7M7TRL3QqF7ltw9sQhAAsQcRaBBF21pdWrqhiGZ+Eioo3hhgwNavH2agqz78ddHwrFpHFwrEeUk1OfpPb76MYIce7xIy/4oQNdg6fOq4l/FrajBv+WkzDVPaKm6r7YmwfLN/YMZBHXSR58oOGP9W/n-----END CERTIFICATE-----\"' # str | The certificate's contents.
    friendly_name = 'TestCert' # str | The certificate's friendly name. (optional)
    crt2 = 'crt_example' # str | The certificate file. (optional)
    friendly_name2 = 'friendly_name_example' # str | The certificate's friendly name. (optional)

    try:
        # Import SSL certificate
        api_response = api_instance.upload_cert(crt, friendly_name=friendly_name, crt2=crt2, friendly_name2=friendly_name2)
        print("The response of SSLApi->upload_cert:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SSLApi->upload_cert: %s\n" % e)
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
    api_instance = clientapi_cpanel.SSLApi(api_client)
    key = '\"-----BEGIN RSA PRIVATE KEY-----\\nMIIEowIBAAKCAQEAyeiHvMuJuVk8ZEY6wMzUS1g0eWaHaIWmIRe+Qrn6SwiRrm1p\\npsJCiGPPPQGOSg4FzrMXqE0zsi/Tk3hUO/EEsi7CcZe8cUanjlUeXhiwrb86FCMF\\nOb9siRHQvlss7VCg8ZGXXTWZgf5yD3A1xPwdayYwF2Tc7GkNcZGUAI58geuYaq+U\\nGiLczRGZep1IQ0b1cZnqDvGMx6AS6hiDqLISjnmXYY2OhG6Uyp+SuinjYzLPJ6eO\\nN/7i9qqbcGmt0ssddmhR897+bTEom5SlSuyi03KZ9Rn4ZmNJgOsup9MclSBGxBys\\nb6MuuM3N0/tF5QuwmDc8H6h2rNBP9vGV7RTTXQIDAQABAoIBAFS/WVoRRLmbjxG3\\nuKl8UA9f8oaSVnu0vUpeoOl5Dmm4Kw2/tvzbxPlii3Xb1VGYGS/tVBy8atp74J6h\\nfxm5zHLN1afAPMR/F41ShPCSBHapMUOKf4MBqhjOdYOw2Way1RsQNSxWdxxtJIr+\\nWlNYTzDOUpk/KMvCPHZS2IBzTidpcFpDQ3pyDXjOoKJJH0EQWPtvxJNGrFqmU29D\\n9WBqQemHnDrzg3s7JzQ5cGpbbCE+QX8IckNkslAkyhm771CtqWdeo+c45e6YfGcx\\nKuAy1zGSVzQBuitzYoMUOL5olXLEj8fHzXd/cZP4yCyyabcGz2vi6luxF+28l1OL\\nG1axyLECgYEA+bD5B+Y/Dp5hZ/uVR1bbvyraQpwbDesS1zgnJ53KOIl926dnWzIt\\nUvM46+c9IF+UJrtzwIB6IvjAQioNFrK36bHgNGzNf9WQ54NN172qveaFLdW34z/i\\nGR2ix/efm9OC41QREQ/5IKV07TibCwVazVBWascMPkH7FnguTvTCiosCgYEAzwJ+\\nGPlIWjK+sqkK5JMUyuH43qAvgVfkZV906JpNRQH0Mob3bC0nXN95EoTwWXk68ULT\\no1GHv9XLbj8e+Ok7kpJQZT5vEZnDN+cy3jdTLCvcjU5Q3ToImOTp9isSAFWRTbtk\\nyabLNoIIsTR/ZwwPFTZcRiK2d8k7ZhcRKdfGnrcCgYAPZ06FoTukoDqsGoYkB4S4\\n72DVmSHGIwlfg5ROylouULUV9ubWZmsLYfvR+cr4k0zlcsz6RDLEs4nQyx1RmCbm\\nYNXPBiNLTpaI4b3MoGPHIVB3+mZEu60sFXr0UR9kkpDRi18eKVkaHXrwI3zVGjh2\\n0Az0u2DS+mkOAs4AivLxbwKBgQC0XPqbLc+Bb0dCCREJmLD8GCkrZ6wcaQUB4krN\\nQ2vhnVM0Fu5K3Yi3XapynUuA2aSmgtA9MxMw7MkjlHGa9DPIgBz2KZDCaBN0iMeE\\nX/XivZCbucmxBxhohsLmjh5QFj3U2Vp2bBIQuvlx1EjQ8uvNUqDRJvuOoNFVIPH+\\nYBeZPwKBgA//kXfNtNMHOpch699i3rgTzbRFDmGwsr1otzvJsXw7Pr2bM4WIzUJy\\nG2SUSUlQRSZK4+BBKT9S0d7TynJD6X/6R7IBotZbfXs1myYxEsKj89/BQmr47x2h\\nHjYVCClNoJlsbd5C2yu1R3PikweWGoVaxE3c+AN5knqjwJ0g21Cf\\n-----END RSA PRIVATE KEY-----\"' # str | The key's contents.
    friendly_name = 'TestKey' # str | The key's friendly name. (optional)
    crt = 'crt_example' # str | The key's contents. (optional)
    friendly_name2 = 'friendly_name_example' # str | The key's friendly name. (optional)

    try:
        # Import private key
        api_response = api_instance.upload_key(key, friendly_name=friendly_name, crt=crt, friendly_name2=friendly_name2)
        print("The response of SSLApi->upload_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SSLApi->upload_key: %s\n" % e)
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

