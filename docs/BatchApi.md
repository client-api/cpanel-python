# clientapi_cpanel.BatchApi

All URIs are relative to *https://cpanel-server.tld:2083/execute*

Method | HTTP request | Description
------------- | ------------- | -------------
[**strict**](BatchApi.md#strict) | **GET** /Batch/strict | Run multiple UAPI functions in order


# **strict**
> InlineResponse20014 strict(command)

Run multiple UAPI functions in order

This function combines calls for multiple UAPI functions and performs them in order.

**Note:**

* If a function call in the list fails, the `Batch::strict` function does not run further function calls in the list.
* Due to the potential length of calls of this function, we recommend that you use the HTTP POST method for extremely long batch commands.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response20014 import InlineResponse20014
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
    api_instance = clientapi_cpanel.BatchApi(api_client)
    command = [clientapi_cpanel.OneOfstringmap()] # List[OneOfstringmap] | A UAPI function call, encoded as a JSON array with two or three items:  * The UAPI module. * The UAPI function. * A JSON object containing the parameters to pass to this function. You can omit this value if you do not pass any parameters to the function.  To submit multiple commands, duplicate the parameter name, or index all parameter names and increment the index for each one.  * When using the cPanel LiveAPI PHP Library, you **must** increment the parameter name when you submit the arguments in an associative array. For example: use `command-0`, `command-1`, and `command-2`. * When using the cPanel LiveAPI Perl Library, you **must** increment the parameter name when you submit the arguments in a hash. For example: use `command-0`, `command-1`, and `command-2`. * You do **not** need to add an index to `command` parameters for query string calls of this function.

    try:
        # Run multiple UAPI functions in order
        api_response = api_instance.strict(command)
        print("The response of BatchApi->strict:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BatchApi->strict: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **command** | [**List[OneOfstringmap]**](OneOfstringmap.md)| A UAPI function call, encoded as a JSON array with two or three items:  * The UAPI module. * The UAPI function. * A JSON object containing the parameters to pass to this function. You can omit this value if you do not pass any parameters to the function.  To submit multiple commands, duplicate the parameter name, or index all parameter names and increment the index for each one.  * When using the cPanel LiveAPI PHP Library, you **must** increment the parameter name when you submit the arguments in an associative array. For example: use &#x60;command-0&#x60;, &#x60;command-1&#x60;, and &#x60;command-2&#x60;. * When using the cPanel LiveAPI Perl Library, you **must** increment the parameter name when you submit the arguments in a hash. For example: use &#x60;command-0&#x60;, &#x60;command-1&#x60;, and &#x60;command-2&#x60;. * You do **not** need to add an index to &#x60;command&#x60; parameters for query string calls of this function. | 

### Return type

[**InlineResponse20014**](InlineResponse20014.md)

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

