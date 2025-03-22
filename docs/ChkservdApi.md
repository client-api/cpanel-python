# clientapi_cpanel.ChkservdApi

All URIs are relative to *https://cpanel-server.tld:2083/execute*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_exim_ports**](ChkservdApi.md#get_exim_ports) | **GET** /Chkservd/get_exim_ports | Return outgoing (SMTP) mail port
[**get_exim_ports_ssl**](ChkservdApi.md#get_exim_ports_ssl) | **GET** /Chkservd/get_exim_ports_ssl | Return outgoing mail (SMTP) SSL-secured port


# **get_exim_ports**
> InlineResponse20060 get_exim_ports()

Return outgoing (SMTP) mail port

This function lists the ports on which Exim listens.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response20060 import InlineResponse20060
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
    api_instance = clientapi_cpanel.ChkservdApi(api_client)

    try:
        # Return outgoing (SMTP) mail port
        api_response = api_instance.get_exim_ports()
        print("The response of ChkservdApi->get_exim_ports:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChkservdApi->get_exim_ports: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**InlineResponse20060**](InlineResponse20060.md)

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

# **get_exim_ports_ssl**
> InlineResponse20061 get_exim_ports_ssl()

Return outgoing mail (SMTP) SSL-secured port

This function retrieves Exim's SSL port.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response20061 import InlineResponse20061
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
    api_instance = clientapi_cpanel.ChkservdApi(api_client)

    try:
        # Return outgoing mail (SMTP) SSL-secured port
        api_response = api_instance.get_exim_ports_ssl()
        print("The response of ChkservdApi->get_exim_ports_ssl:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChkservdApi->get_exim_ports_ssl: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**InlineResponse20061**](InlineResponse20061.md)

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

