# clientapi_cpanel.BandwidthApi

All URIs are relative to *https://cpanel-server.tld:2083/execute*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_enabled_protocols**](BandwidthApi.md#get_enabled_protocols) | **GET** /Bandwidth/get_enabled_protocols | Return services monitored in bandwidth data
[**get_retention_periods**](BandwidthApi.md#get_retention_periods) | **GET** /Bandwidth/get_retention_periods | Return bandwidth retention period
[**query**](BandwidthApi.md#query) | **GET** /Bandwidth/query | Return cPanel account&#39;s bandwidth usage report


# **get_enabled_protocols**
> InlineResponse20011 get_enabled_protocols()

Return services monitored in bandwidth data

This function returns a list of the server's enabled protocols.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response20011 import InlineResponse20011
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
    api_instance = clientapi_cpanel.BandwidthApi(api_client)

    try:
        # Return services monitored in bandwidth data
        api_response = api_instance.get_enabled_protocols()
        print("The response of BandwidthApi->get_enabled_protocols:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BandwidthApi->get_enabled_protocols: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**InlineResponse20011**](InlineResponse20011.md)

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

# **get_retention_periods**
> InlineResponse20012 get_retention_periods()

Return bandwidth retention period

This function retrieves the retention periods for bandwidth data.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response20012 import InlineResponse20012
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
    api_instance = clientapi_cpanel.BandwidthApi(api_client)

    try:
        # Return bandwidth retention period
        api_response = api_instance.get_retention_periods()
        print("The response of BandwidthApi->get_retention_periods:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BandwidthApi->get_retention_periods: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**InlineResponse20012**](InlineResponse20012.md)

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

# **query**
> InlineResponse20013 query(grouping, domains=domains, end=end, interval=interval, protocols=protocols, start=start, timezone=timezone)

Return cPanel account's bandwidth usage report

This function queries an account's bandwidth data and returns a report.

**Note:**

This function also returns the bandwidth use of a [distributed cPanel account](https://go.cpanel.net/cPanelGlossary#distributed-cpanel-account).

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response20013 import InlineResponse20013
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
    api_instance = clientapi_cpanel.BandwidthApi(api_client)
    grouping = clientapi_cpanel.Grouping() # Grouping | How to group the data in the report, in pipe-separated format. This list **must** contain one or both of the following parameters:  A pipe-separated list that contains one or both of the following parameters: * `domain` * `protocol`  This parameter can also include only **one** of the following start time interval types: * `year` * `year_month` * `year_month_day` * `year_month_day_hour` * `year_month_day_mour_minute`  **Note:**  * This parameter accepts a maximum of three values. * The function nests the return objects in the order that you declare the values in this parameter.
    domains = 'domains=example.com|subdomain.example.com|subdomain2.example.com|parkedexample.com|UNKNOWN' # str | A pipe-separated list of domains for which to provided data.  **Note:**  * If you do not include this parameter, the function will return data for all domains on the cPanel account. * The `UNKNOWN` \"pseudo-domain\" refers to data recorded without a specific domain. All traffic except HTTP traffic is recorded without a specific domain. (optional)
    end = 1446664809 # int | The end date of the report window. (optional)
    interval = daily # str | Length of time between bandwidth data samples.  * `daily` * `hourly` * `5min`  **Note:**  The interval's retention period determines availability of the interval's data. Use the `Bandwidth::get_retention_periods` API to determine an interval's retention period. (optional) (default to daily)
    protocols = 'protocols=http|imap|smtp|pop3|ftp' # str | A pipe-separated list of the protocols for which to provide data. * `http` * `imap` * `smtp` * `pop3` * `ftp` (optional)
    start = 1445664609 # int | The start date of the report window. (optional)
    timezone = 'America/Chicago' # str | The timezone in which to report the data. (optional)

    try:
        # Return cPanel account's bandwidth usage report
        api_response = api_instance.query(grouping, domains=domains, end=end, interval=interval, protocols=protocols, start=start, timezone=timezone)
        print("The response of BandwidthApi->query:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BandwidthApi->query: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **grouping** | [**Grouping**](.md)| How to group the data in the report, in pipe-separated format. This list **must** contain one or both of the following parameters:  A pipe-separated list that contains one or both of the following parameters: * &#x60;domain&#x60; * &#x60;protocol&#x60;  This parameter can also include only **one** of the following start time interval types: * &#x60;year&#x60; * &#x60;year_month&#x60; * &#x60;year_month_day&#x60; * &#x60;year_month_day_hour&#x60; * &#x60;year_month_day_mour_minute&#x60;  **Note:**  * This parameter accepts a maximum of three values. * The function nests the return objects in the order that you declare the values in this parameter. | 
 **domains** | **str**| A pipe-separated list of domains for which to provided data.  **Note:**  * If you do not include this parameter, the function will return data for all domains on the cPanel account. * The &#x60;UNKNOWN&#x60; \&quot;pseudo-domain\&quot; refers to data recorded without a specific domain. All traffic except HTTP traffic is recorded without a specific domain. | [optional] 
 **end** | **int**| The end date of the report window. | [optional] 
 **interval** | **str**| Length of time between bandwidth data samples.  * &#x60;daily&#x60; * &#x60;hourly&#x60; * &#x60;5min&#x60;  **Note:**  The interval&#39;s retention period determines availability of the interval&#39;s data. Use the &#x60;Bandwidth::get_retention_periods&#x60; API to determine an interval&#39;s retention period. | [optional] [default to daily]
 **protocols** | **str**| A pipe-separated list of the protocols for which to provide data. * &#x60;http&#x60; * &#x60;imap&#x60; * &#x60;smtp&#x60; * &#x60;pop3&#x60; * &#x60;ftp&#x60; | [optional] 
 **start** | **int**| The start date of the report window. | [optional] 
 **timezone** | **str**| The timezone in which to report the data. | [optional] 

### Return type

[**InlineResponse20013**](InlineResponse20013.md)

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

