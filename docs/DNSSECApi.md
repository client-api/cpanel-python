# clientapi_cpanel.DNSSECApi

All URIs are relative to *https://cpanel-server.tld:2083/execute*

Method | HTTP request | Description
------------- | ------------- | -------------
[**activate_zone_key**](DNSSECApi.md#activate_zone_key) | **GET** /DNSSEC/activate_zone_key | Enable DNSSEC security key
[**add_zone_key**](DNSSECApi.md#add_zone_key) | **GET** /DNSSEC/add_zone_key | Create DNSSEC security key
[**deactivate_zone_key**](DNSSECApi.md#deactivate_zone_key) | **GET** /DNSSEC/deactivate_zone_key | Disable DNSSEC security key
[**disable_dnssec**](DNSSECApi.md#disable_dnssec) | **GET** /DNSSEC/disable_dnssec | Disable DNSSEC
[**enable_dnssec**](DNSSECApi.md#enable_dnssec) | **GET** /DNSSEC/enable_dnssec | Enable DNSSEC
[**export_zone_dnskey**](DNSSECApi.md#export_zone_dnskey) | **GET** /DNSSEC/export_zone_dnskey | Export DNSKEY record value
[**export_zone_key**](DNSSECApi.md#export_zone_key) | **GET** /DNSSEC/export_zone_key | Export DNSSEC security key
[**fetch_ds_records**](DNSSECApi.md#fetch_ds_records) | **GET** /DNSSEC/fetch_ds_records | Return domain&#39;s DS records
[**import_zone_key**](DNSSECApi.md#import_zone_key) | **GET** /DNSSEC/import_zone_key | Add DNSSEC security key
[**remove_zone_key**](DNSSECApi.md#remove_zone_key) | **GET** /DNSSEC/remove_zone_key | Remove DNSSEC security key
[**set_nsec3**](DNSSECApi.md#set_nsec3) | **GET** /DNSSEC/set_nsec3 | Update domain to use NSEC3
[**unset_nsec3**](DNSSECApi.md#unset_nsec3) | **GET** /DNSSEC/unset_nsec3 | Update domain to use NSEC


# **activate_zone_key**
> InlineResponse20088 activate_zone_key(domain, key_id)

Enable DNSSEC security key

This function activates a DNSSEC security key.

**Important:**

When you disable the [DNS role](https://go.cpanel.net/serverroles), the system **disables** this function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response20088 import InlineResponse20088
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
    api_instance = clientapi_cpanel.DNSSECApi(api_client)
    domain = 'example.com' # str | The security key's domain.
    key_id = 1 # int | The security key's ID.

    try:
        # Enable DNSSEC security key
        api_response = api_instance.activate_zone_key(domain, key_id)
        print("The response of DNSSECApi->activate_zone_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DNSSECApi->activate_zone_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**| The security key&#39;s domain. | 
 **key_id** | **int**| The security key&#39;s ID. | 

### Return type

[**InlineResponse20088**](InlineResponse20088.md)

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

# **add_zone_key**
> InlineResponse20089 add_zone_key(algo_num, domain, key_type, active=active, key_size=key_size)

Create DNSSEC security key

This function generates a DNSSEC zone key for a domain.

**Note:**

* After you enable DNSSEC on the domain, you **must** add the DS records to your registrar.
* You **cannot** modify the DNSSEC security key. To make any changes, you **must** disable (and delete) and re-create the DNSSEC security key.

**Important:**

When you disable the [DNS role](https://go.cpanel.net/serverroles), the system **disables** this function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response20089 import InlineResponse20089
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
    api_instance = clientapi_cpanel.DNSSECApi(api_client)
    algo_num = 8 # int | The algorithm that the system uses to generate the security key.  * `5` — RSA/SHA-1 * `6` — DSA-NSEC3-SHA1 * `7` — RSASHA1-NSEC3-SHA1 * `8` — RSA/SHA-256 * `10` — RSA/SHA-512 * `13` — ECDSA Curve P-256 with SHA-256 * `14` — ECDSA Curve P-384 with SHA-384  **Note:**  We recommend that you use 'ECDSA Curve P-256 with SHA-256' if your registrar supports it.
    domain = 'example.com' # str | The domain on which to enable DNSSEC.
    key_type = 'ksk' # str | The type of key to add.  * `ksk` * `zsk`
    active = 1 # int | Whether to activate the newly-created key.  * `1` — Activate the key. * `0` — Do **not** activate the key. (optional) (default to 1)
    key_size = 2048 # int | The key's size, in bits.  **Note:**  For the following `algo_num` and `key_type` parameters, the `key_size` defaults to the following values: * `5` — ksk `2048` zsk `1024` * `6` — ksk `2048` zsk `1024` * `7` — ksk `2048` zsk `1024` * `8` — ksk `2048` zsk `1024` * `10` — ksk `2048` zsk `1024` * `13` — ksk `256` zsk `256` * `14` — ksk `384` zsk `384`  (optional)

    try:
        # Create DNSSEC security key
        api_response = api_instance.add_zone_key(algo_num, domain, key_type, active=active, key_size=key_size)
        print("The response of DNSSECApi->add_zone_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DNSSECApi->add_zone_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **algo_num** | **int**| The algorithm that the system uses to generate the security key.  * &#x60;5&#x60; — RSA/SHA-1 * &#x60;6&#x60; — DSA-NSEC3-SHA1 * &#x60;7&#x60; — RSASHA1-NSEC3-SHA1 * &#x60;8&#x60; — RSA/SHA-256 * &#x60;10&#x60; — RSA/SHA-512 * &#x60;13&#x60; — ECDSA Curve P-256 with SHA-256 * &#x60;14&#x60; — ECDSA Curve P-384 with SHA-384  **Note:**  We recommend that you use &#39;ECDSA Curve P-256 with SHA-256&#39; if your registrar supports it. | 
 **domain** | **str**| The domain on which to enable DNSSEC. | 
 **key_type** | **str**| The type of key to add.  * &#x60;ksk&#x60; * &#x60;zsk&#x60; | 
 **active** | **int**| Whether to activate the newly-created key.  * &#x60;1&#x60; — Activate the key. * &#x60;0&#x60; — Do **not** activate the key. | [optional] [default to 1]
 **key_size** | **int**| The key&#39;s size, in bits.  **Note:**  For the following &#x60;algo_num&#x60; and &#x60;key_type&#x60; parameters, the &#x60;key_size&#x60; defaults to the following values: * &#x60;5&#x60; — ksk &#x60;2048&#x60; zsk &#x60;1024&#x60; * &#x60;6&#x60; — ksk &#x60;2048&#x60; zsk &#x60;1024&#x60; * &#x60;7&#x60; — ksk &#x60;2048&#x60; zsk &#x60;1024&#x60; * &#x60;8&#x60; — ksk &#x60;2048&#x60; zsk &#x60;1024&#x60; * &#x60;10&#x60; — ksk &#x60;2048&#x60; zsk &#x60;1024&#x60; * &#x60;13&#x60; — ksk &#x60;256&#x60; zsk &#x60;256&#x60; * &#x60;14&#x60; — ksk &#x60;384&#x60; zsk &#x60;384&#x60;  | [optional] 

### Return type

[**InlineResponse20089**](InlineResponse20089.md)

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

# **deactivate_zone_key**
> InlineResponse20090 deactivate_zone_key(domain, key_id)

Disable DNSSEC security key

This function deactivates a DNSSEC security key.

**Important:**

When you disable the [*DNS* role](https://go.cpanel.net/serverroles/), the system **disables** this function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response20090 import InlineResponse20090
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
    api_instance = clientapi_cpanel.DNSSECApi(api_client)
    domain = 'example.com' # str | The security key's domain.
    key_id = 1 # int | The security key's ID.

    try:
        # Disable DNSSEC security key
        api_response = api_instance.deactivate_zone_key(domain, key_id)
        print("The response of DNSSECApi->deactivate_zone_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DNSSECApi->deactivate_zone_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**| The security key&#39;s domain. | 
 **key_id** | **int**| The security key&#39;s ID. | 

### Return type

[**InlineResponse20090**](InlineResponse20090.md)

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

# **disable_dnssec**
> InlineResponse20091 disable_dnssec(domain)

Disable DNSSEC

This function disables DNSSEC on the domain.

**Warning:**

 * This action is **irreversible**. If you disable DNSSEC on the domain, you will lose the associated keys. You can only retrieve the previous state with a full backup.
 * If you disable DNSSEC, you **must** remove the DNS records at the registrar.

**Important:**

  When you disable the [DNS role](https://go.cpanel.net/serverroles), the system **disables** this function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response20091 import InlineResponse20091
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
    api_instance = clientapi_cpanel.DNSSECApi(api_client)
    domain = 'domain-0=example0.com&domain-1=example1.com&domain-2=example2.com' # str | The domain on which to disable DNSSEC.  **Note:**   To enable DNSSEC on multiple domains, increment the parameter name. For example: `domain-0`, `domain-1`, `domain-2`.

    try:
        # Disable DNSSEC
        api_response = api_instance.disable_dnssec(domain)
        print("The response of DNSSECApi->disable_dnssec:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DNSSECApi->disable_dnssec: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**| The domain on which to disable DNSSEC.  **Note:**   To enable DNSSEC on multiple domains, increment the parameter name. For example: &#x60;domain-0&#x60;, &#x60;domain-1&#x60;, &#x60;domain-2&#x60;. | 

### Return type

[**InlineResponse20091**](InlineResponse20091.md)

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

# **enable_dnssec**
> InlineResponse20092 enable_dnssec(domain, active=active, algo_num=algo_num, key_setup=key_setup, nsec3_iterations=nsec3_iterations, nsec3_narrow=nsec3_narrow, nsec3_opt_out=nsec3_opt_out, nsec3_salt=nsec3_salt, use_nsec3=use_nsec3)

Enable DNSSEC

This function enables DNSSEC on the domain.

**Note:**

 * After you enable DNSSEC on the domain, you **must** add the DNS records to your registrar.
 * You **cannot** modify the DNSSEC security key. To make any changes, you **must** disable (and delete) and re-create the DNSSEC security key.

**Important:**

  When you disable the [DNS role](https://go.cpanel.net/serverroles), the system **disables** this function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response20092 import InlineResponse20092
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
    api_instance = clientapi_cpanel.DNSSECApi(api_client)
    domain = 'domain-0=example0.com&domain-1=example1.com&domain-2=example2.com' # str | The domain on which to enable DNSSEC.  **Note:**   To enable DNSSEC on multiple domains, increment the parameter name. For example: `domain-0`, `domain-1`, `domain-2`.
    active = 1 # int | Whether to activate the newly-created key.  * `1` — Activate the key. * `0` — Do **not** activate the key. (optional) (default to 1)
    algo_num = 8 # int | The algorithm that the system uses to generate the security key.  * `5` — RSA/SHA-1 * `6` — DSA-NSEC3-SHA1 * `7` — RSASHA1-NSEC3-SHA1 * `8` — RSA/SHA-256 * `10` — RSA/SHA-512 * `13` — ECDSA Curve P-256 with SHA-256 * `14` — ECDSA Curve P-384 with SHA-384  **Note:**   We recommend that you use `ECDSA Curve P-256 with SHA-256` if your registrar supports it. (optional) (default to 8)
    key_setup = classic # str | The manner in which the system creates the security key.  * `simple` — Use a single key for both KSK and ZSK. Use this value when the `algo_nom` parameter is greater than `8`. * `classic` — Use separate keys for KSK and ZSK. Use this value when the `algo_nom` parameter is equal to or less than `8`. (optional) (default to classic)
    nsec3_iterations = 7 # int | The number of times that the system rehashes the first resource record hash operation.  A positive integer less than `501`. (optional) (default to 7)
    nsec3_narrow = 1 # int | Whether NSEC3 will operate in Narrow or Inclusive mode.  In Narrow mode, PowerDNS sends out white lies about the next secure record. Rather than query the resource record in the database, PowerDNS sends the hash plus `1` as the next secure record.  * `1` — Narrow mode. * `0` — Inclusive mode. (optional) (default to 1)
    nsec3_opt_out = 0 # int | Whether the system will create records for all delegations.  * `1` — Create records for all delegations. * `0` — Create records only for secure delegations.  **Note:**   **Only** select `1` if you **must** create records for all delegations. (optional) (default to 0)
    nsec3_salt = '1A2B3C4D5E6F' # str | A hexadecimal string that the system appends to the domain name before it applies the hash function to the name. For more information about the salt value, read the [RFC 5155](https://tools.ietf.org/html/rfc5155#section-3.1.5) documentation.  If you do not declare a value, the system defaults to a random 64-bit value. (optional)
    use_nsec3 = 1 # int | Whether the domain will use [Next Secure Record](https://tools.ietf.org/html/rfc4470) (NSEC) or NSEC3 semantics.  * `1` — Use NSEC3 semantics. * `0` — Use NSEC semantics.  **Note:**   If you use NSEC semantics (`0`), the system ignores the other NSEC3 options. (optional) (default to 1)

    try:
        # Enable DNSSEC
        api_response = api_instance.enable_dnssec(domain, active=active, algo_num=algo_num, key_setup=key_setup, nsec3_iterations=nsec3_iterations, nsec3_narrow=nsec3_narrow, nsec3_opt_out=nsec3_opt_out, nsec3_salt=nsec3_salt, use_nsec3=use_nsec3)
        print("The response of DNSSECApi->enable_dnssec:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DNSSECApi->enable_dnssec: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**| The domain on which to enable DNSSEC.  **Note:**   To enable DNSSEC on multiple domains, increment the parameter name. For example: &#x60;domain-0&#x60;, &#x60;domain-1&#x60;, &#x60;domain-2&#x60;. | 
 **active** | **int**| Whether to activate the newly-created key.  * &#x60;1&#x60; — Activate the key. * &#x60;0&#x60; — Do **not** activate the key. | [optional] [default to 1]
 **algo_num** | **int**| The algorithm that the system uses to generate the security key.  * &#x60;5&#x60; — RSA/SHA-1 * &#x60;6&#x60; — DSA-NSEC3-SHA1 * &#x60;7&#x60; — RSASHA1-NSEC3-SHA1 * &#x60;8&#x60; — RSA/SHA-256 * &#x60;10&#x60; — RSA/SHA-512 * &#x60;13&#x60; — ECDSA Curve P-256 with SHA-256 * &#x60;14&#x60; — ECDSA Curve P-384 with SHA-384  **Note:**   We recommend that you use &#x60;ECDSA Curve P-256 with SHA-256&#x60; if your registrar supports it. | [optional] [default to 8]
 **key_setup** | **str**| The manner in which the system creates the security key.  * &#x60;simple&#x60; — Use a single key for both KSK and ZSK. Use this value when the &#x60;algo_nom&#x60; parameter is greater than &#x60;8&#x60;. * &#x60;classic&#x60; — Use separate keys for KSK and ZSK. Use this value when the &#x60;algo_nom&#x60; parameter is equal to or less than &#x60;8&#x60;. | [optional] [default to classic]
 **nsec3_iterations** | **int**| The number of times that the system rehashes the first resource record hash operation.  A positive integer less than &#x60;501&#x60;. | [optional] [default to 7]
 **nsec3_narrow** | **int**| Whether NSEC3 will operate in Narrow or Inclusive mode.  In Narrow mode, PowerDNS sends out white lies about the next secure record. Rather than query the resource record in the database, PowerDNS sends the hash plus &#x60;1&#x60; as the next secure record.  * &#x60;1&#x60; — Narrow mode. * &#x60;0&#x60; — Inclusive mode. | [optional] [default to 1]
 **nsec3_opt_out** | **int**| Whether the system will create records for all delegations.  * &#x60;1&#x60; — Create records for all delegations. * &#x60;0&#x60; — Create records only for secure delegations.  **Note:**   **Only** select &#x60;1&#x60; if you **must** create records for all delegations. | [optional] [default to 0]
 **nsec3_salt** | **str**| A hexadecimal string that the system appends to the domain name before it applies the hash function to the name. For more information about the salt value, read the [RFC 5155](https://tools.ietf.org/html/rfc5155#section-3.1.5) documentation.  If you do not declare a value, the system defaults to a random 64-bit value. | [optional] 
 **use_nsec3** | **int**| Whether the domain will use [Next Secure Record](https://tools.ietf.org/html/rfc4470) (NSEC) or NSEC3 semantics.  * &#x60;1&#x60; — Use NSEC3 semantics. * &#x60;0&#x60; — Use NSEC semantics.  **Note:**   If you use NSEC semantics (&#x60;0&#x60;), the system ignores the other NSEC3 options. | [optional] [default to 1]

### Return type

[**InlineResponse20092**](InlineResponse20092.md)

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

# **export_zone_dnskey**
> InlineResponse20093 export_zone_dnskey(domain, key_id)

Export DNSKEY record value

This function exports a domain's DNSKEY record value.

**Important:**

When you disable the [_DNS_ role](https://go.cpanel.net/serverroles), the system **disables** this function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response20093 import InlineResponse20093
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
    api_instance = clientapi_cpanel.DNSSECApi(api_client)
    domain = 'example.com' # str | The domain from which to fetch the DNSKEY record value.
    key_id = 12345 # int | The DNSSEC record's ID.

    try:
        # Export DNSKEY record value
        api_response = api_instance.export_zone_dnskey(domain, key_id)
        print("The response of DNSSECApi->export_zone_dnskey:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DNSSECApi->export_zone_dnskey: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**| The domain from which to fetch the DNSKEY record value. | 
 **key_id** | **int**| The DNSSEC record&#39;s ID. | 

### Return type

[**InlineResponse20093**](InlineResponse20093.md)

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

# **export_zone_key**
> InlineResponse20094 export_zone_key(domain, key_id)

Export DNSSEC security key

This function exports a DNSSEC security key.

**Important:**

When you disable the [DNS](https://go.cpanel.net/serverroles) role, the system **disables** this function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response20094 import InlineResponse20094
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
    api_instance = clientapi_cpanel.DNSSECApi(api_client)
    domain = 'example.com' # str | The security key's domain.
    key_id = 12345 # int | The security key's ID.

    try:
        # Export DNSSEC security key
        api_response = api_instance.export_zone_key(domain, key_id)
        print("The response of DNSSECApi->export_zone_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DNSSECApi->export_zone_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**| The security key&#39;s domain. | 
 **key_id** | **int**| The security key&#39;s ID. | 

### Return type

[**InlineResponse20094**](InlineResponse20094.md)

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

# **fetch_ds_records**
> InlineResponse20095 fetch_ds_records(domain)

Return domain's DS records

This function fetches a domain's Delegation of Signing (DS) records.

**Important:**

When you disable the [DNS role](https://go.cpanel.net/serverroles), the system **disables** this function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response20095 import InlineResponse20095
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
    api_instance = clientapi_cpanel.DNSSECApi(api_client)
    domain = 'domain-0=example0.com&domain-1=example1.com&domain-2=example2.com' # str | The domain from which to fetch DS records.  **Note:**   To enable DNSSEC on multiple domains, increment the parameter name. For example: `domain-0`, `domain-1`, `domain-2`.

    try:
        # Return domain's DS records
        api_response = api_instance.fetch_ds_records(domain)
        print("The response of DNSSECApi->fetch_ds_records:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DNSSECApi->fetch_ds_records: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**| The domain from which to fetch DS records.  **Note:**   To enable DNSSEC on multiple domains, increment the parameter name. For example: &#x60;domain-0&#x60;, &#x60;domain-1&#x60;, &#x60;domain-2&#x60;. | 

### Return type

[**InlineResponse20095**](InlineResponse20095.md)

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

# **import_zone_key**
> InlineResponse20096 import_zone_key(domain, key_data, key_type)

Add DNSSEC security key

This function imports a DNSSEC security key.

**Important:**

When you disable the [DNS role](https://go.cpanel.net/serverroles), the system **disables** this function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response20096 import InlineResponse20096
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
    api_instance = clientapi_cpanel.DNSSECApi(api_client)
    domain = 'example.com' # str | The security key's domain.
    key_data = 'Private-key-format:%20v1.2%0AAlgorithm:%2013%20\\(ECDSAP256SHA256\\)%0APrivateKey:%20xCM281KtWE9oCsUX8fP1hDZ02/X7JCjp4QZA/DZjfX0=%0A%0A' # str | The security key data that the [`pdnsutil`](https://doc.powerdns.com/authoritative/manpages/pdnsutil.1.html) utility's `export-zone-key` call returns.
    key_type = 'ksk' # str | The security key's type.  * `ksk` * `zsk`

    try:
        # Add DNSSEC security key
        api_response = api_instance.import_zone_key(domain, key_data, key_type)
        print("The response of DNSSECApi->import_zone_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DNSSECApi->import_zone_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**| The security key&#39;s domain. | 
 **key_data** | **str**| The security key data that the [&#x60;pdnsutil&#x60;](https://doc.powerdns.com/authoritative/manpages/pdnsutil.1.html) utility&#39;s &#x60;export-zone-key&#x60; call returns. | 
 **key_type** | **str**| The security key&#39;s type.  * &#x60;ksk&#x60; * &#x60;zsk&#x60; | 

### Return type

[**InlineResponse20096**](InlineResponse20096.md)

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

# **remove_zone_key**
> InlineResponse20097 remove_zone_key(domain, key_id)

Remove DNSSEC security key

This function removes a DNSSEC security key.

**Important:**

When you disable the [DNS role](https://go.cpanel.net/serverroles), the system **disables** this function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response20097 import InlineResponse20097
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
    api_instance = clientapi_cpanel.DNSSECApi(api_client)
    domain = 'example.com' # str | The security key's domain.
    key_id = 1 # int | The security key's ID.

    try:
        # Remove DNSSEC security key
        api_response = api_instance.remove_zone_key(domain, key_id)
        print("The response of DNSSECApi->remove_zone_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DNSSECApi->remove_zone_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**| The security key&#39;s domain. | 
 **key_id** | **int**| The security key&#39;s ID. | 

### Return type

[**InlineResponse20097**](InlineResponse20097.md)

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

# **set_nsec3**
> InlineResponse20098 set_nsec3(domain, nsec3_iterations, nsec3_narrow, nsec3_opt_out, nsec3_salt)

Update domain to use NSEC3

This function configures the domain to use [Next Secure Record 3](https://tools.ietf.org/html/rfc4470) (NSEC3) semantics.

**Important:**

  When you disable the [DNS role](https://go.cpanel.net/howtouseserverprofiles#roles), the system **disables** this function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response20098 import InlineResponse20098
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
    api_instance = clientapi_cpanel.DNSSECApi(api_client)
    domain = 'example.com' # str | The domain on which to enable NSEC3 semantics.
    nsec3_iterations = 7 # int | The number of times that the system re-executes the first resource record hash operation.
    nsec3_narrow = 1 # int | Whether NSEC3 will operate in Narrow mode or Inclusive mode. In Narrow mode, PowerDNS sends out white lies about the next secure record. Rather than query the resource record in the database, PowerDNS sends the hash plus 1 as the next secure record. * `1` - Narrow mode. * `0` - Inclusive mode.
    nsec3_opt_out = 0 # int | Whether the system will create records for all delegations.  * `1` - Create records for all delegations. * `0` - Create records **only** for secure delegations.  **Note:**    **Only** select `1` if you **must** create records for all delegations.
    nsec3_salt = '1A2B3C4D5E6F' # str | The salt value that PowerDNS uses in the hashes. For more information about the salt value, read the [RFC 5155 documentation](https://tools.ietf.org/html/rfc5155).

    try:
        # Update domain to use NSEC3
        api_response = api_instance.set_nsec3(domain, nsec3_iterations, nsec3_narrow, nsec3_opt_out, nsec3_salt)
        print("The response of DNSSECApi->set_nsec3:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DNSSECApi->set_nsec3: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**| The domain on which to enable NSEC3 semantics. | 
 **nsec3_iterations** | **int**| The number of times that the system re-executes the first resource record hash operation. | 
 **nsec3_narrow** | **int**| Whether NSEC3 will operate in Narrow mode or Inclusive mode. In Narrow mode, PowerDNS sends out white lies about the next secure record. Rather than query the resource record in the database, PowerDNS sends the hash plus 1 as the next secure record. * &#x60;1&#x60; - Narrow mode. * &#x60;0&#x60; - Inclusive mode. | 
 **nsec3_opt_out** | **int**| Whether the system will create records for all delegations.  * &#x60;1&#x60; - Create records for all delegations. * &#x60;0&#x60; - Create records **only** for secure delegations.  **Note:**    **Only** select &#x60;1&#x60; if you **must** create records for all delegations. | 
 **nsec3_salt** | **str**| The salt value that PowerDNS uses in the hashes. For more information about the salt value, read the [RFC 5155 documentation](https://tools.ietf.org/html/rfc5155). | 

### Return type

[**InlineResponse20098**](InlineResponse20098.md)

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

# **unset_nsec3**
> InlineResponse20099 unset_nsec3(domain)

Update domain to use NSEC

This function configures the domain to use [Next Secure Record](https://tools.ietf.org/html/rfc4470) (NSEC) semantics instead of Next Secure Record 3 (NSEC3) semantics.

**Important:**

  When you disable the [DNS role](https://go.cpanel.net/serverroles), the system **disables** this function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response20099 import InlineResponse20099
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
    api_instance = clientapi_cpanel.DNSSECApi(api_client)
    domain = 'example.com' # str | The domain on which to disable NSEC3 semantics and use NSEC semantics.

    try:
        # Update domain to use NSEC
        api_response = api_instance.unset_nsec3(domain)
        print("The response of DNSSECApi->unset_nsec3:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DNSSECApi->unset_nsec3: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**| The domain on which to disable NSEC3 semantics and use NSEC semantics. | 

### Return type

[**InlineResponse20099**](InlineResponse20099.md)

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

