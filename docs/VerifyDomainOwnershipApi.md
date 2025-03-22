# clientapi_cpanel.VerifyDomainOwnershipApi

All URIs are relative to *https://cpanel-server.tld:2083/execute*

Method | HTTP request | Description
------------- | ------------- | -------------
[**check_domains_via_dns**](VerifyDomainOwnershipApi.md#check_domains_via_dns) | **POST** /DCV/check_domains_via_dns | Verify domain ownership via DNS
[**check_domains_via_http**](VerifyDomainOwnershipApi.md#check_domains_via_http) | **GET** /DCV/check_domains_via_http | Verify domain ownership via HTTP
[**ensure_domains_can_pass_dcv**](VerifyDomainOwnershipApi.md#ensure_domains_can_pass_dcv) | **GET** /DCV/ensure_domains_can_pass_dcv | Verify domain ownership


# **check_domains_via_dns**
> InlineResponse20078 check_domains_via_dns(domain)

Verify domain ownership via DNS

This function checks whether the account's domains can pass Domain Control Validation (DCV) via a DNS request.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response20078 import InlineResponse20078
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
    api_instance = clientapi_cpanel.VerifyDomainOwnershipApi(api_client)
    domain = 'domain-0=example.com&domain-1=example2.com' # str | The domain or domains to check.  **Note:**   To check multiple domains, increment the parameter name. For example, `domain-0`, `domain-1`, and `domain-2`.

    try:
        # Verify domain ownership via DNS
        api_response = api_instance.check_domains_via_dns(domain)
        print("The response of VerifyDomainOwnershipApi->check_domains_via_dns:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VerifyDomainOwnershipApi->check_domains_via_dns: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**| The domain or domains to check.  **Note:**   To check multiple domains, increment the parameter name. For example, &#x60;domain-0&#x60;, &#x60;domain-1&#x60;, and &#x60;domain-2&#x60;. | 

### Return type

[**InlineResponse20078**](InlineResponse20078.md)

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

# **check_domains_via_http**
> InlineResponse20079 check_domains_via_http(domain, dcv_file_allowed_characters=dcv_file_allowed_characters, dcv_file_extension=dcv_file_extension, dcv_file_random_character_count=dcv_file_random_character_count, dcv_file_relative_path=dcv_file_relative_path, dcv_max_redirects=dcv_max_redirects, dcv_user_agent_string=dcv_user_agent_string)

Verify domain ownership via HTTP

This function checks whether the account's domains can pass Domain Control Validation (DCV) via an HTTP request.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response20079 import InlineResponse20079
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
    api_instance = clientapi_cpanel.VerifyDomainOwnershipApi(api_client)
    domain = 'domain-1=example.com&domain-2=example2.com&domain-3=example2.com' # str | The domains to check.  **Note:**  To check more than one domain, repeat or increment the parameter name. For example, `domain-1`, `domain-2`, and `domain-3`.
    dcv_file_allowed_characters = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z",0,1,2,3,4,5,6,7,8,9] # List[str] | An array of characters that the certificate provider allows in the DCV check file's filename. (optional) (default to ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z",0,1,2,3,4,5,6,7,8,9])
    dcv_file_extension = '' # str | The DCV check file extension that the certificate provider requires. (optional) (default to '')
    dcv_file_random_character_count = 100 # int | The number of characters that the certificate provider allows in the DCV check file's filename. (optional) (default to 100)
    dcv_file_relative_path = '.well-known/pki-validation' # str | The DCV check file's file path, relative to the domain's document `root` directory. (optional) (default to '.well-known/pki-validation')
    dcv_max_redirects = 2 # int | The number of domain redirects the system permits the DCV check to follow. The function checks the provider's supported number of redirects. It will then return the `redirect` array of objects for the passed value, plus one. This ensures the function will display any redirects causing DCV failures, if any exist.  **Note:**  * If you pass a `0` value, this function does **not** limit the number of redirect returns. * Use the `Market::get_provider_specific_dcv_constraints` UAPI function to list a provider's supported number of redirects. (optional)
    dcv_user_agent_string = 'SECTIGO+DCV' # str | The [user agent string](https://wikipedia.org/wiki/User_agent) that the system uses for the imitated local DCV check.  **Important:**  The default value can change at any time. (optional)

    try:
        # Verify domain ownership via HTTP
        api_response = api_instance.check_domains_via_http(domain, dcv_file_allowed_characters=dcv_file_allowed_characters, dcv_file_extension=dcv_file_extension, dcv_file_random_character_count=dcv_file_random_character_count, dcv_file_relative_path=dcv_file_relative_path, dcv_max_redirects=dcv_max_redirects, dcv_user_agent_string=dcv_user_agent_string)
        print("The response of VerifyDomainOwnershipApi->check_domains_via_http:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VerifyDomainOwnershipApi->check_domains_via_http: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**| The domains to check.  **Note:**  To check more than one domain, repeat or increment the parameter name. For example, &#x60;domain-1&#x60;, &#x60;domain-2&#x60;, and &#x60;domain-3&#x60;. | 
 **dcv_file_allowed_characters** | [**List[str]**](str.md)| An array of characters that the certificate provider allows in the DCV check file&#39;s filename. | [optional] [default to [&quot;A&quot;,&quot;B&quot;,&quot;C&quot;,&quot;D&quot;,&quot;E&quot;,&quot;F&quot;,&quot;G&quot;,&quot;H&quot;,&quot;I&quot;,&quot;J&quot;,&quot;K&quot;,&quot;L&quot;,&quot;M&quot;,&quot;N&quot;,&quot;O&quot;,&quot;P&quot;,&quot;Q&quot;,&quot;R&quot;,&quot;S&quot;,&quot;T&quot;,&quot;U&quot;,&quot;V&quot;,&quot;W&quot;,&quot;X&quot;,&quot;Y&quot;,&quot;Z&quot;,0,1,2,3,4,5,6,7,8,9]]
 **dcv_file_extension** | **str**| The DCV check file extension that the certificate provider requires. | [optional] [default to &#39;&#39;]
 **dcv_file_random_character_count** | **int**| The number of characters that the certificate provider allows in the DCV check file&#39;s filename. | [optional] [default to 100]
 **dcv_file_relative_path** | **str**| The DCV check file&#39;s file path, relative to the domain&#39;s document &#x60;root&#x60; directory. | [optional] [default to &#39;.well-known/pki-validation&#39;]
 **dcv_max_redirects** | **int**| The number of domain redirects the system permits the DCV check to follow. The function checks the provider&#39;s supported number of redirects. It will then return the &#x60;redirect&#x60; array of objects for the passed value, plus one. This ensures the function will display any redirects causing DCV failures, if any exist.  **Note:**  * If you pass a &#x60;0&#x60; value, this function does **not** limit the number of redirect returns. * Use the &#x60;Market::get_provider_specific_dcv_constraints&#x60; UAPI function to list a provider&#39;s supported number of redirects. | [optional] 
 **dcv_user_agent_string** | **str**| The [user agent string](https://wikipedia.org/wiki/User_agent) that the system uses for the imitated local DCV check.  **Important:**  The default value can change at any time. | [optional] 

### Return type

[**InlineResponse20079**](InlineResponse20079.md)

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

# **ensure_domains_can_pass_dcv**
> InlineResponse20080 ensure_domains_can_pass_dcv(domain)

Verify domain ownership

This function indicates whether the account's domains can pass a Domain Control
Validation (DCV) check.

**Warning:**

We deprecated this function. Use UAPI's `DCV::check_domains_via_http` function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response20080 import InlineResponse20080
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
    api_instance = clientapi_cpanel.VerifyDomainOwnershipApi(api_client)
    domain = 'domain-1=example1.com domain-2=example2.com domain-3=example3.com' # str | The domains to check.  **Note:**   To check multiple domains, duplicate or increment the parameter name. For example,  `domain-1`, `domain-2`, and `domain-3`.

    try:
        # Verify domain ownership
        api_response = api_instance.ensure_domains_can_pass_dcv(domain)
        print("The response of VerifyDomainOwnershipApi->ensure_domains_can_pass_dcv:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VerifyDomainOwnershipApi->ensure_domains_can_pass_dcv: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**| The domains to check.  **Note:**   To check multiple domains, duplicate or increment the parameter name. For example,  &#x60;domain-1&#x60;, &#x60;domain-2&#x60;, and &#x60;domain-3&#x60;. | 

### Return type

[**InlineResponse20080**](InlineResponse20080.md)

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

