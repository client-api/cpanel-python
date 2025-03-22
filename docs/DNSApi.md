# clientapi_cpanel.DNSApi

All URIs are relative to *https://cpanel-server.tld:2083/execute*

Method | HTTP request | Description
------------- | ------------- | -------------
[**d_ns_swap_ip_in_zones**](DNSApi.md#d_ns_swap_ip_in_zones) | **GET** /DNS/swap_ip_in_zones | Update IP addresses in zone files
[**d_nsis_alias_available**](DNSApi.md#d_nsis_alias_available) | **GET** /DNS/is_alias_available | Return &#x60;ALIAS&#x60; DNS record availability &amp; resolver
[**dns_lookup**](DNSApi.md#dns_lookup) | **GET** /DNS/lookup | Return domain&#39;s DNS information
[**dns_mass_edit_zone**](DNSApi.md#dns_mass_edit_zone) | **GET** /DNS/mass_edit_zone | Update a DNS zone
[**dns_parse_zone**](DNSApi.md#dns_parse_zone) | **GET** /DNS/parse_zone | Return a parsed DNS zone
[**ensure_domains_reside_only_locally**](DNSApi.md#ensure_domains_reside_only_locally) | **GET** /DNS/ensure_domains_reside_only_locally | Return whether domains only resolve locally
[**has_local_authority**](DNSApi.md#has_local_authority) | **GET** /DNS/has_local_authority | Return whether local DNS server is authoritative


# **d_ns_swap_ip_in_zones**
> InlineResponse20087 d_ns_swap_ip_in_zones(dest_ip, domain, ftp_ip=ftp_ip, source_ip=source_ip)

Update IP addresses in zone files

This function replaces a domain's IPv4 address in the DNS zone
file with the specified destination IPv4 address.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response20087 import InlineResponse20087
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
    api_instance = clientapi_cpanel.DNSApi(api_client)
    dest_ip = '192.0.2.1' # str | The IPv4 address to use as the replacement in the zone files.
    domain = 'example.com domain-1=example1.com domain-2=example2.com' # str | The domain to perform the zone file updates on.  **Note:**  To update multiple domains, increment or duplicate the parameter name. For example, `domain-0`, `domain-1`, and `domain-2`.
    ftp_ip = '192.0.2.1' # str | The IPv4 address to use as the replacement for FTP records in the zone files.  If this parameter is **not** provided, then the system will use the `dest_ip` value. (optional)
    source_ip = '192.0.2.0' # str | The IPv4 address to replace in the zone files. The detected source IPv4 address is one of:  * If there is an A record for the root of the zone **and** the IP address is **not** a loopback address, then the system will use its address. * If there are any A records in the zone whose addresses are **not** loopback addresses, then the system will use the address of the first such A record in the zone file. * If no A records exist in the zone **or** all A records have loopback addresses, then the system will **not** update the zone file.  If you do **not** call this parameter, the system will automatically detect the IP addresses in the zone files. (optional)

    try:
        # Update IP addresses in zone files
        api_response = api_instance.d_ns_swap_ip_in_zones(dest_ip, domain, ftp_ip=ftp_ip, source_ip=source_ip)
        print("The response of DNSApi->d_ns_swap_ip_in_zones:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DNSApi->d_ns_swap_ip_in_zones: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dest_ip** | **str**| The IPv4 address to use as the replacement in the zone files. | 
 **domain** | **str**| The domain to perform the zone file updates on.  **Note:**  To update multiple domains, increment or duplicate the parameter name. For example, &#x60;domain-0&#x60;, &#x60;domain-1&#x60;, and &#x60;domain-2&#x60;. | 
 **ftp_ip** | **str**| The IPv4 address to use as the replacement for FTP records in the zone files.  If this parameter is **not** provided, then the system will use the &#x60;dest_ip&#x60; value. | [optional] 
 **source_ip** | **str**| The IPv4 address to replace in the zone files. The detected source IPv4 address is one of:  * If there is an A record for the root of the zone **and** the IP address is **not** a loopback address, then the system will use its address. * If there are any A records in the zone whose addresses are **not** loopback addresses, then the system will use the address of the first such A record in the zone file. * If no A records exist in the zone **or** all A records have loopback addresses, then the system will **not** update the zone file.  If you do **not** call this parameter, the system will automatically detect the IP addresses in the zone files. | [optional] 

### Return type

[**InlineResponse20087**](InlineResponse20087.md)

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

# **d_nsis_alias_available**
> InlineResponse20083 d_nsis_alias_available()

Return `ALIAS` DNS record availability & resolver

This function returns whether `ALIAS` and `ANAME` records are available and the value of the running PowerDNS (PDNS) `resolver` setting, if any exists.
For more information, read our [`ALIAS` documentation](https://go.cpanel.net/dns-alias-record).

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response20083 import InlineResponse20083
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
    api_instance = clientapi_cpanel.DNSApi(api_client)

    try:
        # Return `ALIAS` DNS record availability & resolver
        api_response = api_instance.d_nsis_alias_available()
        print("The response of DNSApi->d_nsis_alias_available:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DNSApi->d_nsis_alias_available: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**InlineResponse20083**](InlineResponse20083.md)

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

# **dns_lookup**
> InlineResponse20084 dns_lookup(domain)

Return domain's DNS information

This function returns DNS zone information about a domain.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response20084 import InlineResponse20084
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
    api_instance = clientapi_cpanel.DNSApi(api_client)
    domain = 'example.com' # str | A fully qualified domain name.

    try:
        # Return domain's DNS information
        api_response = api_instance.dns_lookup(domain)
        print("The response of DNSApi->dns_lookup:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DNSApi->dns_lookup: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**| A fully qualified domain name. | 

### Return type

[**InlineResponse20084**](InlineResponse20084.md)

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

# **dns_mass_edit_zone**
> InlineResponse20085 dns_mass_edit_zone(serial, zone, add=add, edit=edit, remove=remove)

Update a DNS zone

This function updates a given DNS zone. It can add, edit,
and remove many records in a single call. It also ensures
that each record not removed will occupy the same
number of lines after the edit as it did before the edit.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response20085 import InlineResponse20085
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
    api_instance = clientapi_cpanel.DNSApi(api_client)
    serial = 202001010100 # int | The current serial number in the DNS zone’s SOA (Start of Authority) record. If this value does not match the zone’s current state, the request fails.
    zone = 'example.com' # str | The name of one of the user’s DNS zones.
    add = ['\'{\"dname\":\"example\", \"ttl\":14400, \"record_type\":\"A\", \"data\":[\"11.22.33.44\"]}\''] # List[str] | The records to add to the zone. Each item must be a serialized JSON object that contains:  * `dname` — The record’s name. * `ttl` — The record’s TTL (Time-To-Live) value. * `record_type` — The record’s type. For example, `A` or `TXT`. * `data` — An array of strings. The format and number of the   strings depend on the `record_type` value. (optional)
    edit = ['edit_example'] # List[str] | The records to edit in the zone. Each item must be a serialized JSON object that contains:  * `line_index` — The line number in the DNS zone where the record starts.   This is a 0-based index, so to edit the first line in the file   use the `0` value. To edit the second line, give `1`, and so forth. * `dname` — The record’s name. * `ttl` — The record’s TTL (Time-To-Live) value. * `record_type` — The record’s new type. For example, `A` or `TXT`. * `data` — An array of strings. The format and number of the   strings depend on the `record_type` value. (optional)
    remove = [56] # List[int] | The line indexes of records to remove from the zone. (optional)

    try:
        # Update a DNS zone
        api_response = api_instance.dns_mass_edit_zone(serial, zone, add=add, edit=edit, remove=remove)
        print("The response of DNSApi->dns_mass_edit_zone:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DNSApi->dns_mass_edit_zone: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **serial** | **int**| The current serial number in the DNS zone’s SOA (Start of Authority) record. If this value does not match the zone’s current state, the request fails. | 
 **zone** | **str**| The name of one of the user’s DNS zones. | 
 **add** | [**List[str]**](str.md)| The records to add to the zone. Each item must be a serialized JSON object that contains:  * &#x60;dname&#x60; — The record’s name. * &#x60;ttl&#x60; — The record’s TTL (Time-To-Live) value. * &#x60;record_type&#x60; — The record’s type. For example, &#x60;A&#x60; or &#x60;TXT&#x60;. * &#x60;data&#x60; — An array of strings. The format and number of the   strings depend on the &#x60;record_type&#x60; value. | [optional] 
 **edit** | [**List[str]**](str.md)| The records to edit in the zone. Each item must be a serialized JSON object that contains:  * &#x60;line_index&#x60; — The line number in the DNS zone where the record starts.   This is a 0-based index, so to edit the first line in the file   use the &#x60;0&#x60; value. To edit the second line, give &#x60;1&#x60;, and so forth. * &#x60;dname&#x60; — The record’s name. * &#x60;ttl&#x60; — The record’s TTL (Time-To-Live) value. * &#x60;record_type&#x60; — The record’s new type. For example, &#x60;A&#x60; or &#x60;TXT&#x60;. * &#x60;data&#x60; — An array of strings. The format and number of the   strings depend on the &#x60;record_type&#x60; value. | [optional] 
 **remove** | [**List[int]**](int.md)| The line indexes of records to remove from the zone. | [optional] 

### Return type

[**InlineResponse20085**](InlineResponse20085.md)

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

# **dns_parse_zone**
> InlineResponse20086 dns_parse_zone(zone)

Return a parsed DNS zone

This function parses a given DNS zone.

**Important:**

Most DNS zones contain only 7-bit ASCII. However, it is possible for
DNS zones to contain any binary sequence. An application that decodes
this function's base64 output **must** be able to handle cases
where the decoded octets do not match any specific character
encoding.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response20086 import InlineResponse20086
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
    api_instance = clientapi_cpanel.DNSApi(api_client)
    zone = 'example.com' # str | The name of one of the user’s DNS zones.

    try:
        # Return a parsed DNS zone
        api_response = api_instance.dns_parse_zone(zone)
        print("The response of DNSApi->dns_parse_zone:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DNSApi->dns_parse_zone: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **zone** | **str**| The name of one of the user’s DNS zones. | 

### Return type

[**InlineResponse20086**](InlineResponse20086.md)

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

# **ensure_domains_reside_only_locally**
> InlineResponse20081 ensure_domains_reside_only_locally(domain)

Return whether domains only resolve locally

This function indicates whether the account's domains resolve exclusively to this server.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response20081 import InlineResponse20081
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
    api_instance = clientapi_cpanel.DNSApi(api_client)
    domain = 'domain=example.com&domain-1=example1.com&domain-2=example2.com' # str | The domain to check.  **Note:**  To check multiple domains, duplicate or increment the parameter name. For example, to exclude three domains, you could: * Use the `domain` parameter multiple times. * Use the `domain`, `domain-1`, and `domain-2` parameters.

    try:
        # Return whether domains only resolve locally
        api_response = api_instance.ensure_domains_reside_only_locally(domain)
        print("The response of DNSApi->ensure_domains_reside_only_locally:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DNSApi->ensure_domains_reside_only_locally: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**| The domain to check.  **Note:**  To check multiple domains, duplicate or increment the parameter name. For example, to exclude three domains, you could: * Use the &#x60;domain&#x60; parameter multiple times. * Use the &#x60;domain&#x60;, &#x60;domain-1&#x60;, and &#x60;domain-2&#x60; parameters. | 

### Return type

[**InlineResponse20081**](InlineResponse20081.md)

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

# **has_local_authority**
> InlineResponse20082 has_local_authority(domain)

Return whether local DNS server is authoritative

This function checks whether the local server is authoritative for the domain's DNS records.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response20082 import InlineResponse20082
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
    api_instance = clientapi_cpanel.DNSApi(api_client)
    domain = 'domain-0=example.com domain-1=example1.com domain-2=example2.com' # str | The domain to check whether the local server is authoritative for the domain's DNS records.  **Note:**  To check multiple domains, increment or duplicate the parameter name. For example, `domain-0`, `domain-1`, and `domain-2`.

    try:
        # Return whether local DNS server is authoritative
        api_response = api_instance.has_local_authority(domain)
        print("The response of DNSApi->has_local_authority:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DNSApi->has_local_authority: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**| The domain to check whether the local server is authoritative for the domain&#39;s DNS records.  **Note:**  To check multiple domains, increment or duplicate the parameter name. For example, &#x60;domain-0&#x60;, &#x60;domain-1&#x60;, and &#x60;domain-2&#x60;. | 

### Return type

[**InlineResponse20082**](InlineResponse20082.md)

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

