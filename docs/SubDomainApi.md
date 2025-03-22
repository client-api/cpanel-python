# clientapi_cpanel.SubDomainApi

All URIs are relative to *https://cpanel-server.tld:2083/execute*

Method | HTTP request | Description
------------- | ------------- | -------------
[**addsubdomain**](SubDomainApi.md#addsubdomain) | **GET** /SubDomain/addsubdomain | Create subdomain


# **addsubdomain**
> InlineResponse200495 addsubdomain(domain, rootdomain, canoff=canoff, dir=dir, disallowdot=disallowdot)

Create subdomain

This function creates a subdomain.

**Important:**

When you disable the [Web Server role](https://go.cpanel.net/serverroles#roles), the system **disables** this function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200495 import InlineResponse200495
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
    api_instance = clientapi_cpanel.SubDomainApi(api_client)
    domain = 'subdomain' # str | The subdomain name to create.
    rootdomain = 'example.com' # str | The domain on which to create the new subdomain.  The domain **must** already exist on the cPanel account.
    canoff = 1 # int | Whether to use a canonical name (CNAME) in the [Apache® configuration for self-referential URLs](https://httpd.apache.org/docs/2.4/mod/core.html#usecanonicalname). * `1` - Use the CNAME. * `0` - Do **not** use the CNAME. (optional) (default to 1)
    dir = '/public_html/directory_name' # str | The subdomain's document `root` within the home directory, given as a valid directory path relative to the user's home directory.  This value defaults to the user's home directory `/public_html/` path.  **Note:**  If the *Restrict document roots to public_html* value is set to *Off* in WHM's [*Tweak Settings*](https://go.cpanel.net/whmdocsTweakSettings#domains) interface (*WHM >> Home >> Server Configuration >> Tweak Settings*), this parameter defaults to the `/username/` path. For example, the `username` user's subdomain `example` would default to the `/home/username/example` path. (optional)
    disallowdot = 0 # int | Whether to remove the dot (`.`) characters from the `domain` value. * `1` - Remove dots from the domain. * `0` - Do **not** remove dots from the domain. (optional) (default to 0)

    try:
        # Create subdomain
        api_response = api_instance.addsubdomain(domain, rootdomain, canoff=canoff, dir=dir, disallowdot=disallowdot)
        print("The response of SubDomainApi->addsubdomain:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubDomainApi->addsubdomain: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**| The subdomain name to create. | 
 **rootdomain** | **str**| The domain on which to create the new subdomain.  The domain **must** already exist on the cPanel account. | 
 **canoff** | **int**| Whether to use a canonical name (CNAME) in the [Apache® configuration for self-referential URLs](https://httpd.apache.org/docs/2.4/mod/core.html#usecanonicalname). * &#x60;1&#x60; - Use the CNAME. * &#x60;0&#x60; - Do **not** use the CNAME. | [optional] [default to 1]
 **dir** | **str**| The subdomain&#39;s document &#x60;root&#x60; within the home directory, given as a valid directory path relative to the user&#39;s home directory.  This value defaults to the user&#39;s home directory &#x60;/public_html/&#x60; path.  **Note:**  If the *Restrict document roots to public_html* value is set to *Off* in WHM&#39;s [*Tweak Settings*](https://go.cpanel.net/whmdocsTweakSettings#domains) interface (*WHM &gt;&gt; Home &gt;&gt; Server Configuration &gt;&gt; Tweak Settings*), this parameter defaults to the &#x60;/username/&#x60; path. For example, the &#x60;username&#x60; user&#39;s subdomain &#x60;example&#x60; would default to the &#x60;/home/username/example&#x60; path. | [optional] 
 **disallowdot** | **int**| Whether to remove the dot (&#x60;.&#x60;) characters from the &#x60;domain&#x60; value. * &#x60;1&#x60; - Remove dots from the domain. * &#x60;0&#x60; - Do **not** remove dots from the domain. | [optional] [default to 0]

### Return type

[**InlineResponse200495**](InlineResponse200495.md)

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

