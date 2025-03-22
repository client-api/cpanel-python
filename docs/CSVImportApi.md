# clientapi_cpanel.CSVImportApi

All URIs are relative to *https://cpanel-server.tld:2083/execute*

Method | HTTP request | Description
------------- | ------------- | -------------
[**c_sv_import_doimport**](CSVImportApi.md#c_sv_import_doimport) | **GET** /CSVImport/doimport | Import email accounts from CSV file


# **c_sv_import_doimport**
> InlineResponse20057 c_sv_import_doimport(domain, id, type)

Import email accounts from CSV file

This function imports email accounts from an already uploaded CSV file.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response20057 import InlineResponse20057
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
    api_instance = clientapi_cpanel.CSVImportApi(api_client)
    domain = 'example.com' # str | The domain under which to add the email accounts.
    id = 'Leq58oid3sF3Moye3_YbJGqoMvCb7M4j' # str | The unique ID of the import operation. The cPanel API 2 CSVImport::uploadimport function generates this ID and stores it in the `CPVAR` attribute named `csvimportid`.
    type = 'email' # str | The type of email address to add.  * `email` — A regular email account. * `fwd` — A forwarder.

    try:
        # Import email accounts from CSV file
        api_response = api_instance.c_sv_import_doimport(domain, id, type)
        print("The response of CSVImportApi->c_sv_import_doimport:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CSVImportApi->c_sv_import_doimport: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**| The domain under which to add the email accounts. | 
 **id** | **str**| The unique ID of the import operation. The cPanel API 2 CSVImport::uploadimport function generates this ID and stores it in the &#x60;CPVAR&#x60; attribute named &#x60;csvimportid&#x60;. | 
 **type** | **str**| The type of email address to add.  * &#x60;email&#x60; — A regular email account. * &#x60;fwd&#x60; — A forwarder. | 

### Return type

[**InlineResponse20057**](InlineResponse20057.md)

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

