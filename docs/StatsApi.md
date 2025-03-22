# clientapi_cpanel.StatsApi

All URIs are relative to *https://cpanel-server.tld:2083/execute*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_bandwidth**](StatsApi.md#get_bandwidth) | **GET** /Stats/get_bandwidth | Return bandwidth statistics for all domains
[**get_site_errors**](StatsApi.md#get_site_errors) | **GET** /Stats/get_site_errors | Return specified domain access log
[**list_sites**](StatsApi.md#list_sites) | **GET** /Stats/list_sites | Return Analog statistics for all domains
[**list_stats_by_domain**](StatsApi.md#list_stats_by_domain) | **GET** /Stats/list_stats_by_domain | Return Analog statistics for specified domain


# **get_bandwidth**
> InlineResponse200488 get_bandwidth(timezone=timezone)

Return bandwidth statistics for all domains

This function retrieves a list of bandwidth records for the domains on a cPanel account.

**Note:**

This function also returns the bandwidth use of a [distributed cPanel account](https://docs.cpanel.net/knowledge-base/cpanel-product/cpanel-glossary#distributed-cpanel-account).

**Warning:**

This function requires the _Bandwidth Stats_ feature. To enable this feature, use WHM's [_Feature Manager_](https://go.cpanel.net/whmdocsFeatureManager)
interface (_WHM >> Home >> Packages >> Feature Manager_).

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200488 import InlineResponse200488
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
    api_instance = clientapi_cpanel.StatsApi(api_client)
    timezone = 'America/Chicago' # str | The timezone in which to report the data, in [Olson tz format](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones).  **Note:**  This parameter defaults to the server's timezone. (optional)

    try:
        # Return bandwidth statistics for all domains
        api_response = api_instance.get_bandwidth(timezone=timezone)
        print("The response of StatsApi->get_bandwidth:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StatsApi->get_bandwidth: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timezone** | **str**| The timezone in which to report the data, in [Olson tz format](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones).  **Note:**  This parameter defaults to the server&#39;s timezone. | [optional] 

### Return type

[**InlineResponse200488**](InlineResponse200488.md)

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

# **get_site_errors**
> InlineResponse200489 get_site_errors(domain, log=log, maxlines=maxlines)

Return specified domain access log

This function returns entries from a domain's error log.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200489 import InlineResponse200489
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
    api_instance = clientapi_cpanel.StatsApi(api_client)
    domain = 'example.com' # str | The domain for which to return error log entries.
    log = 'suexec' # str | The [Apache log file](https://go.cpanel.net/cpanellogfiles) to query. This parameter defaults to error.  * `error` - The `/var/log/apache2/error_log` file. * `suexec` - The `/var/log/apache2/suexec_log` file. (optional)
    maxlines = 300 # int | The number of lines to retrieve from the error log. (optional) (default to 300)

    try:
        # Return specified domain access log
        api_response = api_instance.get_site_errors(domain, log=log, maxlines=maxlines)
        print("The response of StatsApi->get_site_errors:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StatsApi->get_site_errors: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**| The domain for which to return error log entries. | 
 **log** | **str**| The [Apache log file](https://go.cpanel.net/cpanellogfiles) to query. This parameter defaults to error.  * &#x60;error&#x60; - The &#x60;/var/log/apache2/error_log&#x60; file. * &#x60;suexec&#x60; - The &#x60;/var/log/apache2/suexec_log&#x60; file. | [optional] 
 **maxlines** | **int**| The number of lines to retrieve from the error log. | [optional] [default to 300]

### Return type

[**InlineResponse200489**](InlineResponse200489.md)

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

# **list_sites**
> InlineResponse200490 list_sites(engine, traffic=traffic)

Return Analog statistics for all domains

This function displays the Analog statistics for the domains on a cPanel account.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200490 import InlineResponse200490
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
    api_instance = clientapi_cpanel.StatsApi(api_client)
    engine = 'webalizer' # str | The statistics engine. * `webalizer` * `analog`
    traffic = http # str | The web traffic type.  * `http`  * `ftp` (optional) (default to http)

    try:
        # Return Analog statistics for all domains
        api_response = api_instance.list_sites(engine, traffic=traffic)
        print("The response of StatsApi->list_sites:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StatsApi->list_sites: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **engine** | **str**| The statistics engine. * &#x60;webalizer&#x60; * &#x60;analog&#x60; | 
 **traffic** | **str**| The web traffic type.  * &#x60;http&#x60;  * &#x60;ftp&#x60; | [optional] [default to http]

### Return type

[**InlineResponse200490**](InlineResponse200490.md)

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

# **list_stats_by_domain**
> InlineResponse200491 list_stats_by_domain(domain, engine, ssl=ssl)

Return Analog statistics for specified domain

This function returns a domain's Analog statistics.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200491 import InlineResponse200491
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
    api_instance = clientapi_cpanel.StatsApi(api_client)
    domain = 'example.com' # str | The domain from which to retrieve statistics.
    engine = 'analog' # str | The statistics engine. `analog` is the only possible value.
    ssl = 1 # int | Whether to return statistics from SSL requests.   * `1` - Return statistics for SSL requests.   * `0` - Return statistics for non-SSL requests. (optional) (default to 1)

    try:
        # Return Analog statistics for specified domain
        api_response = api_instance.list_stats_by_domain(domain, engine, ssl=ssl)
        print("The response of StatsApi->list_stats_by_domain:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StatsApi->list_stats_by_domain: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**| The domain from which to retrieve statistics. | 
 **engine** | **str**| The statistics engine. &#x60;analog&#x60; is the only possible value. | 
 **ssl** | **int**| Whether to return statistics from SSL requests.   * &#x60;1&#x60; - Return statistics for SSL requests.   * &#x60;0&#x60; - Return statistics for non-SSL requests. | [optional] [default to 1]

### Return type

[**InlineResponse200491**](InlineResponse200491.md)

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

