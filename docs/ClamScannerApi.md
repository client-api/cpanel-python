# clientapi_cpanel.ClamScannerApi

All URIs are relative to *https://cpanel-server.tld:2083/execute*

Method | HTTP request | Description
------------- | ------------- | -------------
[**clam_scanner_check_disinfection_status**](ClamScannerApi.md#clam_scanner_check_disinfection_status) | **GET** /ClamScanner/check_disinfection_status | Request disinfection process status
[**clam_scanner_get_scan_paths**](ClamScannerApi.md#clam_scanner_get_scan_paths) | **GET** /ClamScanner/get_scan_paths | Return virus scan types
[**clam_scanner_get_scan_status**](ClamScannerApi.md#clam_scanner_get_scan_status) | **GET** /ClamScanner/get_scan_status | Request virus scan status
[**clam_scanner_list_infected_files**](ClamScannerApi.md#clam_scanner_list_infected_files) | **GET** /ClamScanner/list_infected_files | Return infected file list
[**clam_scanner_start_scan**](ClamScannerApi.md#clam_scanner_start_scan) | **GET** /ClamScanner/start_scan | Start virus scan
[**disinfect_files**](ClamScannerApi.md#disinfect_files) | **POST** /ClamScanner/disinfect_files | Start disinfecting files with viruses


# **clam_scanner_check_disinfection_status**
> InlineResponse20063 clam_scanner_check_disinfection_status(last_id=last_id)

Request disinfection process status

This function checks the status of the previously queued disinfection
of infected files.

**Note:**

You must run the APIs in this order:

1. Run [`ClamScanner::start_scan`](https://go.cpanel.net/ClamScanner-start-scan) to start the virus scan.
2. Run [`ClamScanner::get_scan_status`](https://go.cpanel.net/ClamScanner-get-scan-status) in a loop until the scan is finished.
3. Run [`ClamScanner::list_infected_files`](https://go.cpanel.net/ClamScanner-list-infected-files) to get a report of the complete list of infected files.
4. Decide how you want to handle each infected file.
5. Run [`ClamScanner::disinfect_files`](https://go.cpanel.net/ClamScanner-disinfect-files) to queue the disinfection of the files.
6. Run [`ClamScanner::check_disinfection_status`](https://go.cpanel.net/ClamScanner-check-disinfection-status) in a loop until you get a done status.

If you want to display the progress, you can render the `ClamScanner::check_disinfection_status` returned 'result{data}{details}' array where the `type` is `step`.

Each `step` record indicates the action taken on a specific file in the set being processed.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response20063 import InlineResponse20063
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
    api_instance = clientapi_cpanel.ClamScannerApi(api_client)
    last_id = 10 # int | The unique `id` of the message you last received from this same log.  The API will return only the records after the specified `last_id`.  If this parameter is not provided, the entire log is returned.  **Note:**  For improved performance, we recommend applications include the last record ID (last_id) from a previous call to this API, so only messages since the previous API call are returned. (optional)

    try:
        # Request disinfection process status
        api_response = api_instance.clam_scanner_check_disinfection_status(last_id=last_id)
        print("The response of ClamScannerApi->clam_scanner_check_disinfection_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClamScannerApi->clam_scanner_check_disinfection_status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **last_id** | **int**| The unique &#x60;id&#x60; of the message you last received from this same log.  The API will return only the records after the specified &#x60;last_id&#x60;.  If this parameter is not provided, the entire log is returned.  **Note:**  For improved performance, we recommend applications include the last record ID (last_id) from a previous call to this API, so only messages since the previous API call are returned. | [optional] 

### Return type

[**InlineResponse20063**](InlineResponse20063.md)

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

# **clam_scanner_get_scan_paths**
> InlineResponse20065 clam_scanner_get_scan_paths()

Return virus scan types

This function gets the available local paths that a cPanel account is permitted to scan.

**Note**:

The system determines the available scan types based on what the system administrator has set in WHM's [Configure ClamAV®](https://go.cpanel.net/configureclamavscanner) page.

**Note**:

You must run the APIs in this order:

1. Run [`ClamScanner::start_scan`](https://go.cpanel.net/ClamScanner-start-scan) to start the virus scan.
2. Run [`ClamScanner::get_scan_status`](https://go.cpanel.net/ClamScanner-get-scan-status) in a loop until the scan is finished.
3. Run [`ClamScanner::list_infected_files`](https://go.cpanel.net/ClamScanner-list-infected-files) to get a report of the complete list of infected files.
4. Decide how you want to handle each infected file.
5. Run [`ClamScanner::disinfect_files`](https://go.cpanel.net/ClamScanner-disinfect-files) to queue the disinfection of the files.
6. Run [`ClamScanner::check_disinfection_status`](https://go.cpanel.net/ClamScanner-check-disinfection-status) in a loop until you get a done status.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response20065 import InlineResponse20065
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
    api_instance = clientapi_cpanel.ClamScannerApi(api_client)

    try:
        # Return virus scan types
        api_response = api_instance.clam_scanner_get_scan_paths()
        print("The response of ClamScannerApi->clam_scanner_get_scan_paths:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClamScannerApi->clam_scanner_get_scan_paths: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**InlineResponse20065**](InlineResponse20065.md)

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

# **clam_scanner_get_scan_status**
> InlineResponse20066 clam_scanner_get_scan_status()

Request virus scan status

This function gets the status of a ClamAV® scan on a directory.

**Note**:

You must run the APIs in this order:

1. Run [`ClamScanner::start_scan`](https://go.cpanel.net/ClamScanner-start-scan) to start the virus scan.
2. Run [`ClamScanner::get_scan_status`](https://go.cpanel.net/ClamScanner-get-scan-status) in a loop until the scan is finished.
3. Run [`ClamScanner::list_infected_files`](https://go.cpanel.net/ClamScanner-list-infected-files) to get a report of the complete list of infected files.
4. Decide how you want to handle each infected file.
5. Run [`ClamScanner::disinfect_files`](https://go.cpanel.net/ClamScanner-disinfect-files) to queue the disinfection of the files.
6. Run [`ClamScanner::check_disinfection_status`](https://go.cpanel.net/ClamScanner-check-disinfection-status) in a loop until you get a done status.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response20066 import InlineResponse20066
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
    api_instance = clientapi_cpanel.ClamScannerApi(api_client)

    try:
        # Request virus scan status
        api_response = api_instance.clam_scanner_get_scan_status()
        print("The response of ClamScannerApi->clam_scanner_get_scan_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClamScannerApi->clam_scanner_get_scan_status: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**InlineResponse20066**](InlineResponse20066.md)

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

# **clam_scanner_list_infected_files**
> InlineResponse20067 clam_scanner_list_infected_files()

Return infected file list

This function lists infected files from a ClamAV® virus scan.

**Note**:

You must run the APIs in this order:

1. Run [`ClamScanner::start_scan`](https://go.cpanel.net/ClamScanner-start-scan) to start the virus scan.
2. Run [`ClamScanner::get_scan_status`](https://go.cpanel.net/ClamScanner-get-scan-status) in a loop until the scan is finished.
3. Run [`ClamScanner::list_infected_files`](https://go.cpanel.net/ClamScanner-list-infected-files) to get a report of the complete list of infected files.
4. Decide how you want to handle each infected file.
5. Run [`ClamScanner::disinfect_files`](https://go.cpanel.net/ClamScanner-disinfect-files) to queue the disinfection of the files.
6. Run [`ClamScanner::check_disinfection_status`](https://go.cpanel.net/ClamScanner-check-disinfection-status) in a loop until you get a done status.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response20067 import InlineResponse20067
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
    api_instance = clientapi_cpanel.ClamScannerApi(api_client)

    try:
        # Return infected file list
        api_response = api_instance.clam_scanner_list_infected_files()
        print("The response of ClamScannerApi->clam_scanner_list_infected_files:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClamScannerApi->clam_scanner_list_infected_files: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**InlineResponse20067**](InlineResponse20067.md)

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

# **clam_scanner_start_scan**
> InlineResponse20068 clam_scanner_start_scan(scan_type)

Start virus scan

This function starts a ClamAV® scan on a directory.

**Note**:

You must run the APIs in this order:

1. Run [`ClamScanner::start_scan`](https://go.cpanel.net/ClamScanner-start-scan) to start the virus scan.
2. Run [`ClamScanner::get_scan_status`](https://go.cpanel.net/ClamScanner-get-scan-status) in a loop until the scan is finished.
3. Run [`ClamScanner::list_infected_files`](https://go.cpanel.net/ClamScanner-list-infected-files) to get a report of the complete list of infected files.
4. Decide how you want to handle each infected file.
5. Run [`ClamScanner::disinfect_files`](https://go.cpanel.net/ClamScanner-disinfect-files) to queue the disinfection of the files.
6. Run [`ClamScanner::check_disinfection_status`](https://go.cpanel.net/ClamScanner-check-disinfection-status) in a loop until you get a done status.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response20068 import InlineResponse20068
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
    api_instance = clientapi_cpanel.ClamScannerApi(api_client)
    scan_type = 'home' # str | The type of directory to scan.  * `home` — User's entire home directory * `mail` — User's email directory * `public_html` — User's web directory * `public_ftp` — User's ftp directory

    try:
        # Start virus scan
        api_response = api_instance.clam_scanner_start_scan(scan_type)
        print("The response of ClamScannerApi->clam_scanner_start_scan:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClamScannerApi->clam_scanner_start_scan: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scan_type** | **str**| The type of directory to scan.  * &#x60;home&#x60; — User&#39;s entire home directory * &#x60;mail&#x60; — User&#39;s email directory * &#x60;public_html&#x60; — User&#39;s web directory * &#x60;public_ftp&#x60; — User&#39;s ftp directory | 

### Return type

[**InlineResponse20068**](InlineResponse20068.md)

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

# **disinfect_files**
> InlineResponse20064 disinfect_files(clam_scanner_disinfect_files_body=clam_scanner_disinfect_files_body)

Start disinfecting files with viruses

This function applies the disinfection option selected by the user
for each infected file.

**Note:**

You must run the APIs in this order:

1. Run [`ClamScanner::start_scan`](https://go.cpanel.net/ClamScanner-start-scan) to start the virus scan.
2. Run [`ClamScanner::get_scan_status`](https://go.cpanel.net/ClamScanner-get-scan-status) in a loop until the scan is finished.
3. Run [`ClamScanner::list_infected_files`](https://go.cpanel.net/ClamScanner-list-infected-files) to get a report of the complete list of infected files.
4. Decide how you want to handle each infected file.
5. Run [`ClamScanner::disinfect_files`](https://go.cpanel.net/ClamScanner-disinfect-files) to queue the disinfection of the files.
6. Run [`ClamScanner::check_disinfection_status`](https://go.cpanel.net/ClamScanner-check-disinfection-status) in a loop until you get a done status.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.clam_scanner_disinfect_files_body import ClamScannerDisinfectFilesBody
from clientapi_cpanel.models.inline_response20064 import InlineResponse20064
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
    api_instance = clientapi_cpanel.ClamScannerApi(api_client)
    clam_scanner_disinfect_files_body = clientapi_cpanel.ClamScannerDisinfectFilesBody() # ClamScannerDisinfectFilesBody |  (optional)

    try:
        # Start disinfecting files with viruses
        api_response = api_instance.disinfect_files(clam_scanner_disinfect_files_body=clam_scanner_disinfect_files_body)
        print("The response of ClamScannerApi->disinfect_files:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClamScannerApi->disinfect_files: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **clam_scanner_disinfect_files_body** | [**ClamScannerDisinfectFilesBody**](ClamScannerDisinfectFilesBody.md)|  | [optional] 

### Return type

[**InlineResponse20064**](InlineResponse20064.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | HTTP Request was successful. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

