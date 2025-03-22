# clientapi_cpanel.EmailAuthApi

All URIs are relative to *https://cpanel-server.tld:2083/execute*

Method | HTTP request | Description
------------- | ------------- | -------------
[**disable_dkim**](EmailAuthApi.md#disable_dkim) | **GET** /EmailAuth/disable_dkim | Remove domains&#39; DKIM records
[**email_auth_apply_dmarc**](EmailAuthApi.md#email_auth_apply_dmarc) | **GET** /EmailAuth/apply_dmarc | Apply DMARC records to domains.
[**email_auth_remove_dmarc**](EmailAuthApi.md#email_auth_remove_dmarc) | **GET** /EmailAuth/remove_dmarc | Remove DMARC record from domain(s)
[**email_auth_validate_current_dmarcs**](EmailAuthApi.md#email_auth_validate_current_dmarcs) | **GET** /EmailAuth/validate_current_dmarcs | Validate domains&#39; DMARC records
[**enable_dkim**](EmailAuthApi.md#enable_dkim) | **GET** /EmailAuth/enable_dkim | Enable domains&#39; DKIM records
[**ensure_dkim_keys_exist**](EmailAuthApi.md#ensure_dkim_keys_exist) | **GET** /EmailAuth/ensure_dkim_keys_exist | Validate domains&#39; DKIM private keys
[**fetch_dkim_private_keys**](EmailAuthApi.md#fetch_dkim_private_keys) | **GET** /EmailAuth/fetch_dkim_private_keys | Return domains&#39; DKIM private keys
[**install_dkim_private_keys**](EmailAuthApi.md#install_dkim_private_keys) | **GET** /EmailAuth/install_dkim_private_keys | Add domains&#39; DKIM record keys
[**install_spf_records**](EmailAuthApi.md#install_spf_records) | **GET** /EmailAuth/install_spf_records | Add domains&#39; SPF records
[**validate_current_dkims**](EmailAuthApi.md#validate_current_dkims) | **GET** /EmailAuth/validate_current_dkims | Validate domains&#39; DKIM records
[**validate_current_ptrs**](EmailAuthApi.md#validate_current_ptrs) | **GET** /EmailAuth/validate_current_ptrs | Validate domains&#39; PTR records
[**validate_current_spfs**](EmailAuthApi.md#validate_current_spfs) | **GET** /EmailAuth/validate_current_spfs | Validate domains&#39; SPF records


# **disable_dkim**
> InlineResponse200216 disable_dkim(domain)

Remove domains' DKIM records

This function removes the DomainKeys Identified Mail (DKIM) records on the DNS server for one or more domains.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200216 import InlineResponse200216
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
    api_instance = clientapi_cpanel.EmailAuthApi(api_client)
    domain = 'domain=example.com&domain=example2.com&domain=example.com' # str | The domain for which to remove DKIM records on the DNS server.  **Note:**  To remove multiple domain DKIM records, duplicate the parameter name. For example, use the `domain=example.com`, `domain=example2.com`, and `domain=example3.com` parameters.

    try:
        # Remove domains' DKIM records
        api_response = api_instance.disable_dkim(domain)
        print("The response of EmailAuthApi->disable_dkim:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailAuthApi->disable_dkim: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**| The domain for which to remove DKIM records on the DNS server.  **Note:**  To remove multiple domain DKIM records, duplicate the parameter name. For example, use the &#x60;domain&#x3D;example.com&#x60;, &#x60;domain&#x3D;example2.com&#x60;, and &#x60;domain&#x3D;example3.com&#x60; parameters. | 

### Return type

[**InlineResponse200216**](InlineResponse200216.md)

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

# **email_auth_apply_dmarc**
> InlineResponse200215 email_auth_apply_dmarc(policy, domain=domain)

Apply DMARC records to domains.

This function applies a DMARC record to the specified domain(s)

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200215 import InlineResponse200215
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
    api_instance = clientapi_cpanel.EmailAuthApi(api_client)
    policy = 'v=DMARC1;p=reject;pct=100;rua=mailto:postmaster@example.com' # str | The DMARC record to apply to the requested domains.  **Note:**  Visit the following link for more information about the DMARC record specification: https://dmarc.org/resources/specification/
    domain = 'domain-1=example1.com domain-2=example2.com domain-3=example3.com' # str | The domain for which to apply the DMARC record.  **Note:**  To enable multiple domain DMARC records, duplicate or increment the parameter. For example, to enable DMARC records for three domains, perform either of the following actions:  * Use the `domain` parameter three times. * Use the `domain`, `domain-1`, and `domain-2` parameters.  If you do not include this argument, the system applies the DMARC record to all the user's domains. (optional)

    try:
        # Apply DMARC records to domains.
        api_response = api_instance.email_auth_apply_dmarc(policy, domain=domain)
        print("The response of EmailAuthApi->email_auth_apply_dmarc:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailAuthApi->email_auth_apply_dmarc: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy** | **str**| The DMARC record to apply to the requested domains.  **Note:**  Visit the following link for more information about the DMARC record specification: https://dmarc.org/resources/specification/ | 
 **domain** | **str**| The domain for which to apply the DMARC record.  **Note:**  To enable multiple domain DMARC records, duplicate or increment the parameter. For example, to enable DMARC records for three domains, perform either of the following actions:  * Use the &#x60;domain&#x60; parameter three times. * Use the &#x60;domain&#x60;, &#x60;domain-1&#x60;, and &#x60;domain-2&#x60; parameters.  If you do not include this argument, the system applies the DMARC record to all the user&#39;s domains. | [optional] 

### Return type

[**InlineResponse200215**](InlineResponse200215.md)

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

# **email_auth_remove_dmarc**
> InlineResponse200222 email_auth_remove_dmarc(domain=domain)

Remove DMARC record from domain(s)

This function removes the DMARC record for domains.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200222 import InlineResponse200222
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
    api_instance = clientapi_cpanel.EmailAuthApi(api_client)
    domain = 'domain=example.com&domain=example2.com&domain=example.com' # str | The domain from which to remove the DMARC record.  **Note:**  If you do not include this argument, the system will remove **all** DMARC records from **all** domains owned by the user.  To remove multiple domain DMARC records, duplicate the parameter name. For example, use the `domain=example.com`, `domain=example2.com`, and `domain=example3.com` parameters. (optional)

    try:
        # Remove DMARC record from domain(s)
        api_response = api_instance.email_auth_remove_dmarc(domain=domain)
        print("The response of EmailAuthApi->email_auth_remove_dmarc:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailAuthApi->email_auth_remove_dmarc: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**| The domain from which to remove the DMARC record.  **Note:**  If you do not include this argument, the system will remove **all** DMARC records from **all** domains owned by the user.  To remove multiple domain DMARC records, duplicate the parameter name. For example, use the &#x60;domain&#x3D;example.com&#x60;, &#x60;domain&#x3D;example2.com&#x60;, and &#x60;domain&#x3D;example3.com&#x60; parameters. | [optional] 

### Return type

[**InlineResponse200222**](InlineResponse200222.md)

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

# **email_auth_validate_current_dmarcs**
> InlineResponse200224 email_auth_validate_current_dmarcs(domain=domain)

Validate domains' DMARC records

This function checks the validity of the current DMARC record for one or more domains.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200224 import InlineResponse200224
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
    api_instance = clientapi_cpanel.EmailAuthApi(api_client)
    domain = 'domain=example.com,domain=another.com,domain=yetanother.com' # str | The domain for which to check the DMARC record.  **Note:**  If you do not include this argument, the system will validate DMARC records for all domains owned by the user. (optional)

    try:
        # Validate domains' DMARC records
        api_response = api_instance.email_auth_validate_current_dmarcs(domain=domain)
        print("The response of EmailAuthApi->email_auth_validate_current_dmarcs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailAuthApi->email_auth_validate_current_dmarcs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**| The domain for which to check the DMARC record.  **Note:**  If you do not include this argument, the system will validate DMARC records for all domains owned by the user. | [optional] 

### Return type

[**InlineResponse200224**](InlineResponse200224.md)

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

# **enable_dkim**
> InlineResponse200217 enable_dkim(domain)

Enable domains' DKIM records

This function enables DomainKeys Identified Mail (DKIM) records on the DNS server for one or more domains.

**Note:**

If a DKIM record does **not** exist on the server, this function will install a new DKIM record.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200217 import InlineResponse200217
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
    api_instance = clientapi_cpanel.EmailAuthApi(api_client)
    domain = 'domain-1=example1.com domain-2=example2.com domain-3=example3.com' # str | The domain for which to enable DKIM records on the DNS server.  **Note:**  To enable multiple domain DKIM records, duplicate or increment the parameter. For example, to perform this for three domains, you could:  * Use the `domain` parameter multiple times. * Use the `domain`, `domain-1`, and `domain-2` parameters.

    try:
        # Enable domains' DKIM records
        api_response = api_instance.enable_dkim(domain)
        print("The response of EmailAuthApi->enable_dkim:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailAuthApi->enable_dkim: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**| The domain for which to enable DKIM records on the DNS server.  **Note:**  To enable multiple domain DKIM records, duplicate or increment the parameter. For example, to perform this for three domains, you could:  * Use the &#x60;domain&#x60; parameter multiple times. * Use the &#x60;domain&#x60;, &#x60;domain-1&#x60;, and &#x60;domain-2&#x60; parameters. | 

### Return type

[**InlineResponse200217**](InlineResponse200217.md)

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

# **ensure_dkim_keys_exist**
> InlineResponse200218 ensure_dkim_keys_exist(domain)

Validate domains' DKIM private keys

This function confirms the validity of a DomainKeys Identified Mail (DKIM) key for one or more domains.

**Notes:**

* If an existing DKIM key does **not** meet the server's security requirements, the system replaces the existing DKIM key.
* If no DKIM key exists, the system creates a new key for the domain.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200218 import InlineResponse200218
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
    api_instance = clientapi_cpanel.EmailAuthApi(api_client)
    domain = 'domain=example.com&domain=example2.com&domain=example3.com' # str | The domain for which to confirm a valid DKIM key exists.  **Note:**   To check the DKIM key validity for multiple domains, duplicate the parameter name. For example, use the `domain=example.com`, `domain=example2.com`, and `domain=example3.com` parameters.

    try:
        # Validate domains' DKIM private keys
        api_response = api_instance.ensure_dkim_keys_exist(domain)
        print("The response of EmailAuthApi->ensure_dkim_keys_exist:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailAuthApi->ensure_dkim_keys_exist: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**| The domain for which to confirm a valid DKIM key exists.  **Note:**   To check the DKIM key validity for multiple domains, duplicate the parameter name. For example, use the &#x60;domain&#x3D;example.com&#x60;, &#x60;domain&#x3D;example2.com&#x60;, and &#x60;domain&#x3D;example3.com&#x60; parameters. | 

### Return type

[**InlineResponse200218**](InlineResponse200218.md)

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

# **fetch_dkim_private_keys**
> InlineResponse200219 fetch_dkim_private_keys(domain)

Return domains' DKIM private keys

This function returns a domain's installed DKIM private key in [Privacy-Enhanced Mail (PEM)](https://en.wikipedia.org/wiki/Privacy-Enhanced_Mail) format.

**Warning:**

We **strongly** recommend that you protect your private key. If others obtain your private DKIM key, they could sign emails and impersonate you as a sender.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200219 import InlineResponse200219
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
    api_instance = clientapi_cpanel.EmailAuthApi(api_client)
    domain = 'domain=example.com&domain=example2.com&domain=example3.com' # str | The domain for which to retrieve the installed DKIM private key.  **Note:**  To retrieve multiple domain DKIM keys, duplicate the parameter name. For example, use the `domain=example.com`, `domain=example2.com`, and `domain=example3.com` parameters.

    try:
        # Return domains' DKIM private keys
        api_response = api_instance.fetch_dkim_private_keys(domain)
        print("The response of EmailAuthApi->fetch_dkim_private_keys:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailAuthApi->fetch_dkim_private_keys: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**| The domain for which to retrieve the installed DKIM private key.  **Note:**  To retrieve multiple domain DKIM keys, duplicate the parameter name. For example, use the &#x60;domain&#x3D;example.com&#x60;, &#x60;domain&#x3D;example2.com&#x60;, and &#x60;domain&#x3D;example3.com&#x60; parameters. | 

### Return type

[**InlineResponse200219**](InlineResponse200219.md)

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

# **install_dkim_private_keys**
> InlineResponse200220 install_dkim_private_keys(domain, key)

Add domains' DKIM record keys

This function installs existing keys for use in a DomainKeys Identified Mail (DKIM) record. This is useful if you do not want the system to generate keys for DKIM records.

**Note:**

* This function does **not** update the local DNS server's records.
* If the local DNS server is authoritative for the domain's DNS records, use the UAPI `EmailAuth::enable_dkim` function to update the local DNS server's DNS records.
  * We recommend that you use the UAPI `EmailAuth::install_dkim_private_keys` and `EmailAuth::enable_dkim functions` in a batch UAPI call.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200220 import InlineResponse200220
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
    api_instance = clientapi_cpanel.EmailAuthApi(api_client)
    domain = 'domain=example&domain=example2.com&domain=example3.com' # str | The domain for which to install a DKIM private key on the local server.  **Note:**  To install multiple RSA private keys for multiple domains, duplicate the parameter name. For example, use the `domain=example.com`, `domain=example2.com`, and `domain=example3.com` parameters.
    key = '-----BEGIN%20RSA%20PRIVATE%20KEY-----%0aAAAAB3NzaC1yc2EAAAABIwAAAQEA5kSivOqhs0U9ZMN20nxFe27QZ3t0lT2zbH7OSXylKd%0a1rjAjYXGnSXC9j2uaZlemHlptBKVziMJC86ha7Hcj6dVOVrDQ6vF4q34bOCjtKLphQ0IjB%0azVIvqILH9eLJdRaOrS34CmgmPaisrCk5wKVlakygvUfcj3HzaTKS6THyZDGx5shdTpa9lb%0ay8tpOD3JceV7ay4w8r0DipoKPC0OLpvS4EABEeMo9sx8zQEaKv03XygjNCCYtFvxlQQIRG%0alVoL7mPaHSaL3anI05RpNbm/PS+9BhZg+BqNjU4ofHBbfkXk5MiN6M7ieR4Sk5BquccboG%0aF13U5slNgmCEekdt0amw%0a-----END%20RSA%20PRIVATE%20KEY-----%0a' # str | An RSA key in [Privacy-Enhanced Mail (PEM)](https://en.wikipedia.org/wiki/Privacy-Enhanced_Mail) format.  **Note:**  You **must** provide this parameter for each `domain` parameter.

    try:
        # Add domains' DKIM record keys
        api_response = api_instance.install_dkim_private_keys(domain, key)
        print("The response of EmailAuthApi->install_dkim_private_keys:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailAuthApi->install_dkim_private_keys: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**| The domain for which to install a DKIM private key on the local server.  **Note:**  To install multiple RSA private keys for multiple domains, duplicate the parameter name. For example, use the &#x60;domain&#x3D;example.com&#x60;, &#x60;domain&#x3D;example2.com&#x60;, and &#x60;domain&#x3D;example3.com&#x60; parameters. | 
 **key** | **str**| An RSA key in [Privacy-Enhanced Mail (PEM)](https://en.wikipedia.org/wiki/Privacy-Enhanced_Mail) format.  **Note:**  You **must** provide this parameter for each &#x60;domain&#x60; parameter. | 

### Return type

[**InlineResponse200220**](InlineResponse200220.md)

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

# **install_spf_records**
> InlineResponse200221 install_spf_records(domain, record)

Add domains' SPF records

This function installs a Sender Policy Framework (SPF) record for a domain on the DNS server.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200221 import InlineResponse200221
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
    api_instance = clientapi_cpanel.EmailAuthApi(api_client)
    domain = 'domain=example.com&domain=example2.com&domain=example3.com' # str | The domain for which to install an SPF record on the DNS server.  **Note:**  To install multiple SPF records, duplicate the parameter name. For example, use the `domain=example.com`, `domain=example2.com`, and `domain=example3.com` parameters.
    record = '\"v=spf1 ip4:10.0.0.1 %2Ba %2Bmx %2Bip4:10.0.0.2 %2Bip4:10.0.0.3 -all\"' # str | An SPF record.  **Note:**  You **must** provide this parameter for each `domain` parameter.

    try:
        # Add domains' SPF records
        api_response = api_instance.install_spf_records(domain, record)
        print("The response of EmailAuthApi->install_spf_records:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailAuthApi->install_spf_records: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**| The domain for which to install an SPF record on the DNS server.  **Note:**  To install multiple SPF records, duplicate the parameter name. For example, use the &#x60;domain&#x3D;example.com&#x60;, &#x60;domain&#x3D;example2.com&#x60;, and &#x60;domain&#x3D;example3.com&#x60; parameters. | 
 **record** | **str**| An SPF record.  **Note:**  You **must** provide this parameter for each &#x60;domain&#x60; parameter. | 

### Return type

[**InlineResponse200221**](InlineResponse200221.md)

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

# **validate_current_dkims**
> InlineResponse200223 validate_current_dkims(domain)

Validate domains' DKIM records

This function retrieves and checks the DomainKeys Identified Mail
(DKIM) records for one or more domains.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200223 import InlineResponse200223
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
    api_instance = clientapi_cpanel.EmailAuthApi(api_client)
    domain = 'domain=example.com,domain=another.com,domain=yetanother.com domain=example.com,domain-1=another.com,domain-2=yetanother.com' # str | The domain for which to check the DKIM records.

    try:
        # Validate domains' DKIM records
        api_response = api_instance.validate_current_dkims(domain)
        print("The response of EmailAuthApi->validate_current_dkims:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailAuthApi->validate_current_dkims: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**| The domain for which to check the DKIM records. | 

### Return type

[**InlineResponse200223**](InlineResponse200223.md)

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

# **validate_current_ptrs**
> InlineResponse200225 validate_current_ptrs(domain)

Validate domains' PTR records

This function validates the pointer records (PTR) for IPv4 and
IPv6 addresses that the account's domains send mail from. It retrieves the
PTR records for each IP address and determines which of the domain's IP addresses
send mail. It then validates the PTR records for each IP address and validates
the A or AAAA records pointing to each domain. This function also ensures
that at least one of that domain's A or AAAA records points back to the IP
address.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200225 import InlineResponse200225
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
    api_instance = clientapi_cpanel.EmailAuthApi(api_client)
    domain = '`domain`=example.com,`domain`=another.com,`domain`=yetanother.com `domain`=example.com,`domain-1`=another.com,`domain-2`=yetanother.com' # str | The domain for which to validate the PTR records.

    try:
        # Validate domains' PTR records
        api_response = api_instance.validate_current_ptrs(domain)
        print("The response of EmailAuthApi->validate_current_ptrs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailAuthApi->validate_current_ptrs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**| The domain for which to validate the PTR records. | 

### Return type

[**InlineResponse200225**](InlineResponse200225.md)

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

# **validate_current_spfs**
> InlineResponse200226 validate_current_spfs(domain)

Validate domains' SPF records

This function retrieves the the Sender Policy Framework (SPF) records
for one or more domains.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200226 import InlineResponse200226
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
    api_instance = clientapi_cpanel.EmailAuthApi(api_client)
    domain = '`domain`=example.com,`domain`=another.com,`domain`=yetanother.com `domain`=example.com,`domain-1`=another.com,`domain-2`=yetanother.com' # str | The domain for which to check the `SPF` records.

    try:
        # Validate domains' SPF records
        api_response = api_instance.validate_current_spfs(domain)
        print("The response of EmailAuthApi->validate_current_spfs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailAuthApi->validate_current_spfs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**| The domain for which to check the &#x60;SPF&#x60; records. | 

### Return type

[**InlineResponse200226**](InlineResponse200226.md)

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

