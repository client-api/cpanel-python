# clientapi_cpanel.ResourceUsageAndStatisticsApi

All URIs are relative to *https://cpanel-server.tld:2083/execute*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_stats**](ResourceUsageAndStatisticsApi.md#get_stats) | **GET** /StatsBar/get_stats | Return cPanel account statistics
[**get_usages**](ResourceUsageAndStatisticsApi.md#get_usages) | **GET** /ResourceUsage/get_usages | Return resource usage and custom statistics


# **get_stats**
> InlineResponse200492 get_stats(display, infinityimg=infinityimg, infinitylang=infinitylang, rowcounter=rowcounter, warninglevel=warninglevel, warnings=warnings, warnout=warnout)

Return cPanel account statistics

This function retrieves a cPanel account's statistics.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200492 import InlineResponse200492
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
    api_instance = clientapi_cpanel.ResourceUsageAndStatisticsApi(api_client)
    display = 'bandwidthusage|diskusage' # str | A pipe-delimited list of the account's statistics.  <details>   <summary>Click for a list of available display parameters.</summary>    * `addondomains` — Information about the account's addon domains.   * `apacheversion` — The server's Apache version.   * `autoresponders` — Information about the account's auto-responders.   * `bandwidthusage` — Information about the account's bandwidth usage.   * `cachedlistdiskusage` — The amount of cached mailing list disk space the account currently uses.   * `cachedmysqldiskusage` — The amount of cached disk space that the account's MySQL® databases currently use.   * `cachedpostgresdiskusage` — The amount of cached disk space that the account's PostgreSQL databases use.   * `cpanelversion` — The server's cPanel version.   * `dedicatedip` — Account websites that use dedicated IP addresses.   * `diskusage` — Information the account's disk space usage.   * `emailaccounts` — Information about the account's email accounts.   * `emailfilters` — Information the account's email filters.   * `emailforwarders` — Information about the account's forwarders.   * `fileusage` — Information about the account's file usage.   * `ftpaccounts` — Information about the account's FTP accounts.   * `hostingpackage` — The account's hosting package.   * `hostname` — The server's hostname.   * `kernelversion` — The operating system's kernel version.   * `localip` — Account websites that use local IP addresses.   * `machinetype` — The type of operating system that the server uses.   * `mailinglists` — Information the account's mailing lists.   * `mysqldatabases` — The number of MySQL databases the account possesses.   * `mysqldiskusage` — The amount of disk space that the account's MySQL databases use.   * `mysqlversion` — The server's MySQL version.   * `operatingsystem` — The server's operating system.   * `parkeddomains` — Information about the account's parked domains (aliases).   * `perlpath` — The Perl binary's absolute path.   * `perlversion` — The server's Perl version.   * `phpversion` — The server's PHP version.   * `postgresqldatabases` — The number of PostgreSQL databases the cPanel account possesses.   * `postgresdiskusage` — The amount of disk space that the cPanel account's PostgreSQL databases use.   * `sendmailpath` — The path to the system's sendmail binary.   * `sharedip` — Any of the account's websites that use a shared IP address.   * `shorthostname` — The short version of your server's hostname.   * `sqldatabases` — Information about the all of the account's SQL databases.   * `subdomains` — Information about the account's subdomains.   * `theme` — The account's current theme. </details>  **Note:**  * This function may require URI-encode format (`%7C`) or quotes (`\"`) in some contexts, such as the command line tool. * Some display parameters may be unavailable based on the server's configuration.
    infinityimg = '/home/example/infinity.png' # str | The absolute file path to an alternative infinity symbol image. (optional)
    infinitylang = 'infinity' # str | A phrase to represent infinity that the locales system can use. (optional)
    rowcounter = 'even' # str | The type of row.  * `odd` * `even` (optional)
    warninglevel = 87 # int | The minimum level at which to return warnings. (optional)
    warnings = 0 # int | Whether to return all results with a warning.  * `1` — Return only warnings that **exceed** the `warninglevel` parameter's value. * `0` — Return all results. (optional)
    warnout = 0 # int | Whether to display results with a value of `100%`.  * `1` — Display results with a value of `100%`. * `0` — Hide results with a value of `100%`. (optional)

    try:
        # Return cPanel account statistics
        api_response = api_instance.get_stats(display, infinityimg=infinityimg, infinitylang=infinitylang, rowcounter=rowcounter, warninglevel=warninglevel, warnings=warnings, warnout=warnout)
        print("The response of ResourceUsageAndStatisticsApi->get_stats:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ResourceUsageAndStatisticsApi->get_stats: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **display** | **str**| A pipe-delimited list of the account&#39;s statistics.  &lt;details&gt;   &lt;summary&gt;Click for a list of available display parameters.&lt;/summary&gt;    * &#x60;addondomains&#x60; — Information about the account&#39;s addon domains.   * &#x60;apacheversion&#x60; — The server&#39;s Apache version.   * &#x60;autoresponders&#x60; — Information about the account&#39;s auto-responders.   * &#x60;bandwidthusage&#x60; — Information about the account&#39;s bandwidth usage.   * &#x60;cachedlistdiskusage&#x60; — The amount of cached mailing list disk space the account currently uses.   * &#x60;cachedmysqldiskusage&#x60; — The amount of cached disk space that the account&#39;s MySQL® databases currently use.   * &#x60;cachedpostgresdiskusage&#x60; — The amount of cached disk space that the account&#39;s PostgreSQL databases use.   * &#x60;cpanelversion&#x60; — The server&#39;s cPanel version.   * &#x60;dedicatedip&#x60; — Account websites that use dedicated IP addresses.   * &#x60;diskusage&#x60; — Information the account&#39;s disk space usage.   * &#x60;emailaccounts&#x60; — Information about the account&#39;s email accounts.   * &#x60;emailfilters&#x60; — Information the account&#39;s email filters.   * &#x60;emailforwarders&#x60; — Information about the account&#39;s forwarders.   * &#x60;fileusage&#x60; — Information about the account&#39;s file usage.   * &#x60;ftpaccounts&#x60; — Information about the account&#39;s FTP accounts.   * &#x60;hostingpackage&#x60; — The account&#39;s hosting package.   * &#x60;hostname&#x60; — The server&#39;s hostname.   * &#x60;kernelversion&#x60; — The operating system&#39;s kernel version.   * &#x60;localip&#x60; — Account websites that use local IP addresses.   * &#x60;machinetype&#x60; — The type of operating system that the server uses.   * &#x60;mailinglists&#x60; — Information the account&#39;s mailing lists.   * &#x60;mysqldatabases&#x60; — The number of MySQL databases the account possesses.   * &#x60;mysqldiskusage&#x60; — The amount of disk space that the account&#39;s MySQL databases use.   * &#x60;mysqlversion&#x60; — The server&#39;s MySQL version.   * &#x60;operatingsystem&#x60; — The server&#39;s operating system.   * &#x60;parkeddomains&#x60; — Information about the account&#39;s parked domains (aliases).   * &#x60;perlpath&#x60; — The Perl binary&#39;s absolute path.   * &#x60;perlversion&#x60; — The server&#39;s Perl version.   * &#x60;phpversion&#x60; — The server&#39;s PHP version.   * &#x60;postgresqldatabases&#x60; — The number of PostgreSQL databases the cPanel account possesses.   * &#x60;postgresdiskusage&#x60; — The amount of disk space that the cPanel account&#39;s PostgreSQL databases use.   * &#x60;sendmailpath&#x60; — The path to the system&#39;s sendmail binary.   * &#x60;sharedip&#x60; — Any of the account&#39;s websites that use a shared IP address.   * &#x60;shorthostname&#x60; — The short version of your server&#39;s hostname.   * &#x60;sqldatabases&#x60; — Information about the all of the account&#39;s SQL databases.   * &#x60;subdomains&#x60; — Information about the account&#39;s subdomains.   * &#x60;theme&#x60; — The account&#39;s current theme. &lt;/details&gt;  **Note:**  * This function may require URI-encode format (&#x60;%7C&#x60;) or quotes (&#x60;\&quot;&#x60;) in some contexts, such as the command line tool. * Some display parameters may be unavailable based on the server&#39;s configuration. | 
 **infinityimg** | **str**| The absolute file path to an alternative infinity symbol image. | [optional] 
 **infinitylang** | **str**| A phrase to represent infinity that the locales system can use. | [optional] 
 **rowcounter** | **str**| The type of row.  * &#x60;odd&#x60; * &#x60;even&#x60; | [optional] 
 **warninglevel** | **int**| The minimum level at which to return warnings. | [optional] 
 **warnings** | **int**| Whether to return all results with a warning.  * &#x60;1&#x60; — Return only warnings that **exceed** the &#x60;warninglevel&#x60; parameter&#39;s value. * &#x60;0&#x60; — Return all results. | [optional] 
 **warnout** | **int**| Whether to display results with a value of &#x60;100%&#x60;.  * &#x60;1&#x60; — Display results with a value of &#x60;100%&#x60;. * &#x60;0&#x60; — Hide results with a value of &#x60;100%&#x60;. | [optional] 

### Return type

[**InlineResponse200492**](InlineResponse200492.md)

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

# **get_usages**
> InlineResponse200396 get_usages()

Return resource usage and custom statistics

This function retrieves resource usage and custom statistics for a cPanel user account.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200396 import InlineResponse200396
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
    api_instance = clientapi_cpanel.ResourceUsageAndStatisticsApi(api_client)

    try:
        # Return resource usage and custom statistics
        api_response = api_instance.get_usages()
        print("The response of ResourceUsageAndStatisticsApi->get_usages:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ResourceUsageAndStatisticsApi->get_usages: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**InlineResponse200396**](InlineResponse200396.md)

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

