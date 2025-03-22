# clientapi_cpanel.DomainInfoApi

All URIs are relative to *https://cpanel-server.tld:2083/execute*

Method | HTTP request | Description
------------- | ------------- | -------------
[**domains_data**](DomainInfoApi.md#domains_data) | **GET** /DomainInfo/domains_data | Return all domains&#39; hosting configuration
[**list_domains**](DomainInfoApi.md#list_domains) | **GET** /DomainInfo/list_domains | Return cPanel account&#39;s domains
[**main_domain_builtin_subdomain_aliases**](DomainInfoApi.md#main_domain_builtin_subdomain_aliases) | **GET** /DomainInfo/main_domain_builtin_subdomain_aliases | Return built-in subdomain aliases
[**single_domain_data**](DomainInfoApi.md#single_domain_data) | **GET** /DomainInfo/single_domain_data | Return domain&#39;s hosting configuration


# **domains_data**
> InlineResponse200110 domains_data(format=format, return_https_redirects_status=return_https_redirects_status)

Return all domains' hosting configuration

This function lists user data for the cPanel account's domains.

**Note:**

This function retrieves data from the `/var/cpanel/userdata/user/domain` file, where `user`
represents the cPanel account username and `domain` represents the domain. For this reason,
actual output may not contain all of the returns that this document lists.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200110 import InlineResponse200110
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
    api_instance = clientapi_cpanel.DomainInfoApi(api_client)
    format = hash # str | The function's return format.  * `hash` — Use a hash format. The function will return objects based on the domain type. * `list` — Use a list format. The function will return an array of objects, where each object is a domain. (optional) (default to hash)
    return_https_redirects_status = 0 # int | Whether to return the secure redirect status of the addon domains.  * `1` — Return the status. * `0` — Do **not** return the status. (optional) (default to 0)

    try:
        # Return all domains' hosting configuration
        api_response = api_instance.domains_data(format=format, return_https_redirects_status=return_https_redirects_status)
        print("The response of DomainInfoApi->domains_data:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DomainInfoApi->domains_data: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | **str**| The function&#39;s return format.  * &#x60;hash&#x60; — Use a hash format. The function will return objects based on the domain type. * &#x60;list&#x60; — Use a list format. The function will return an array of objects, where each object is a domain. | [optional] [default to hash]
 **return_https_redirects_status** | **int**| Whether to return the secure redirect status of the addon domains.  * &#x60;1&#x60; — Return the status. * &#x60;0&#x60; — Do **not** return the status. | [optional] [default to 0]

### Return type

[**InlineResponse200110**](InlineResponse200110.md)

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

# **list_domains**
> InlineResponse200111 list_domains()

Return cPanel account's domains

This function lists the cPanel account's domains.

**Note:**

For this function to succeed, the `/var/cpanel/userdata/username/main` file (where `username` represents the authenticated user) **must** possess the correct permissions. If a permissions error occurs, this function returns blank values for **all** of its returns and does **not** return an error message.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200111 import InlineResponse200111
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
    api_instance = clientapi_cpanel.DomainInfoApi(api_client)

    try:
        # Return cPanel account's domains
        api_response = api_instance.list_domains()
        print("The response of DomainInfoApi->list_domains:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DomainInfoApi->list_domains: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**InlineResponse200111**](InlineResponse200111.md)

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

# **main_domain_builtin_subdomain_aliases**
> InlineResponse200112 main_domain_builtin_subdomain_aliases()

Return built-in subdomain aliases

This function returns the built-in subdomain aliases for an account's main domain.

**Note:**

  This function retrieves data from the `/var/cpanel/userdata/user/domain` file, where `user` represents the cPanel account username and `domain` represents the domain. For this reason, actual output may not contain all of the returns that this document lists.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200112 import InlineResponse200112
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
    api_instance = clientapi_cpanel.DomainInfoApi(api_client)

    try:
        # Return built-in subdomain aliases
        api_response = api_instance.main_domain_builtin_subdomain_aliases()
        print("The response of DomainInfoApi->main_domain_builtin_subdomain_aliases:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DomainInfoApi->main_domain_builtin_subdomain_aliases: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**InlineResponse200112**](InlineResponse200112.md)

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

# **single_domain_data**
> InlineResponse200113 single_domain_data(domain, return_https_redirect_status=return_https_redirect_status)

Return domain's hosting configuration

This function lists user data for a domain.

**Important:**

  This function retrieves data from the `/var/cpanel/userdata/user/domain` file, where `user` represents the cPanel account username and `domain` represents the domain.
  * Because aliases (parked domains) do **not** use a user data file, this function **cannot** query information for aliases. To retrieve information for an alias, specify the associated main or addon domain.
  * Due to differences in user data files, the function's actual output may not contain all of the returns that this document lists.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200113 import InlineResponse200113
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
    api_instance = clientapi_cpanel.DomainInfoApi(api_client)
    domain = 'example.com' # str | The domain on the cPanel account.  **Important:**  Do **not** specify an alias (parked domain).
    return_https_redirect_status = 0 # int | Whether to return the secure redirect status of the addon domains. * `1` - Return status. * `0` - Do **not** return status. (optional) (default to 0)

    try:
        # Return domain's hosting configuration
        api_response = api_instance.single_domain_data(domain, return_https_redirect_status=return_https_redirect_status)
        print("The response of DomainInfoApi->single_domain_data:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DomainInfoApi->single_domain_data: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**| The domain on the cPanel account.  **Important:**  Do **not** specify an alias (parked domain). | 
 **return_https_redirect_status** | **int**| Whether to return the secure redirect status of the addon domains. * &#x60;1&#x60; - Return status. * &#x60;0&#x60; - Do **not** return status. | [optional] [default to 0]

### Return type

[**InlineResponse200113**](InlineResponse200113.md)

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

