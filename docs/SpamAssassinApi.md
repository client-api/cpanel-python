# clientapi_cpanel.SpamAssassinApi

All URIs are relative to *https://cpanel-server.tld:2083/execute*

Method | HTTP request | Description
------------- | ------------- | -------------
[**clear_spam_box**](SpamAssassinApi.md#clear_spam_box) | **GET** /SpamAssassin/clear_spam_box | Delete spam box contents
[**get_symbolic_test_names**](SpamAssassinApi.md#get_symbolic_test_names) | **GET** /SpamAssassin/get_symbolic_test_names | Return SpamAssassin™ symbolic test scores
[**get_user_preferences**](SpamAssassinApi.md#get_user_preferences) | **GET** /SpamAssassin/get_user_preferences | Return SpamAssassin™ settings
[**update_user_preference**](SpamAssassinApi.md#update_user_preference) | **GET** /SpamAssassin/update_user_preference | Update SpamAssassin™ settings


# **clear_spam_box**
> InlineResponse200484 clear_spam_box()

Delete spam box contents

This function clears the spam box of all its contents for all email accounts.

**Important:**

This function deletes the Spam Box folder contents for every email address on the account, which includes the system user email account.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200484 import InlineResponse200484
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
    api_instance = clientapi_cpanel.SpamAssassinApi(api_client)

    try:
        # Delete spam box contents
        api_response = api_instance.clear_spam_box()
        print("The response of SpamAssassinApi->clear_spam_box:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SpamAssassinApi->clear_spam_box: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**InlineResponse200484**](InlineResponse200484.md)

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

# **get_symbolic_test_names**
> InlineResponse200485 get_symbolic_test_names()

Return SpamAssassin™ symbolic test scores

This function lists the Apache SpamAssassin™ scores for each symbolic test.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200485 import InlineResponse200485
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
    api_instance = clientapi_cpanel.SpamAssassinApi(api_client)

    try:
        # Return SpamAssassin™ symbolic test scores
        api_response = api_instance.get_symbolic_test_names()
        print("The response of SpamAssassinApi->get_symbolic_test_names:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SpamAssassinApi->get_symbolic_test_names: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**InlineResponse200485**](InlineResponse200485.md)

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

# **get_user_preferences**
> InlineResponse200486 get_user_preferences()

Return SpamAssassin™ settings

This function lists the Apache SpamAssassin™ settings for the account.

**Note:**

Additional customizations may appear in the returns. Form more information read the [Apache SpamAssassin™ configuration file](https://spamassassin.apache.org/full/3.1.x/doc/Mail_SpamAssassin_Conf.html#user_preferences) documentation.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200486 import InlineResponse200486
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
    api_instance = clientapi_cpanel.SpamAssassinApi(api_client)

    try:
        # Return SpamAssassin™ settings
        api_response = api_instance.get_user_preferences()
        print("The response of SpamAssassinApi->get_user_preferences:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SpamAssassinApi->get_user_preferences: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**InlineResponse200486**](InlineResponse200486.md)

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

# **update_user_preference**
> InlineResponse200487 update_user_preference(preference, value=value)

Update SpamAssassin™ settings

This function sets the Apache SpamAssassin™ settings for the account.

**Note:**

Additional customizations may appear in the function's return. For more information,
read the [Apache SpamAssassin configuration file documentation](https://spamassassin.apache.org/full/3.1.x/doc/Mail_SpamAssassin_Conf.html#user_preferences).

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200487 import InlineResponse200487
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
    api_instance = clientapi_cpanel.SpamAssassinApi(api_client)
    preference = 'score' # str | The variable that you want to manipulate.  * `score` * `required_score` * `whitelist_from` * `blacklist_from` * A [custom SpamAssassin variable](https://spamassassin.apache.org/full/3.1.x/doc/Mail_SpamAssassin_Conf.html#user_preferences).  **Important:**  * You can **only** choose one of these possible values per call. * If you enter a value for the `preference` parameter, but you do **not** define a value for the `value` parameter, the function will remove any previous settings.
    value = 'value-0=ACT_NOW_CAPS 5.0 value-1=INVALID_DATE 3.2' # str | The value for the preference of the variable that you want to manipulate.  * A valid SpamAssassin \"`TEST_NAME SCORE`\" value when the value of the `preference` parameter is `score`, where:      * `TEST_NAME` represents the symbolic name of the test. For list of symbolic test names, run the UAPI `SpamAssassin::get_symbolic_test_names` function.     * `SCORE` represents the floating-point value that SpamAssassin assigns to the mail when the test result is true. The score value must be greater than `0`, and less than `1000`.  * A valid floating-point number if the value of the `preference` parameter is `required_score`. * A valid email address if the value of the `preference` parameter is `whitelist_from` or `blacklist_from`. * A [custom SpamAssassin variable](https://spamassassin.apache.org/full/3.1.x/doc/Mail_SpamAssassin_Conf.html#user_preferences) value.  **Note:**  To enter multiple values, increment the parameter name. For example, use the `value-0` and `value-1` parameters. (optional)

    try:
        # Update SpamAssassin™ settings
        api_response = api_instance.update_user_preference(preference, value=value)
        print("The response of SpamAssassinApi->update_user_preference:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SpamAssassinApi->update_user_preference: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **preference** | **str**| The variable that you want to manipulate.  * &#x60;score&#x60; * &#x60;required_score&#x60; * &#x60;whitelist_from&#x60; * &#x60;blacklist_from&#x60; * A [custom SpamAssassin variable](https://spamassassin.apache.org/full/3.1.x/doc/Mail_SpamAssassin_Conf.html#user_preferences).  **Important:**  * You can **only** choose one of these possible values per call. * If you enter a value for the &#x60;preference&#x60; parameter, but you do **not** define a value for the &#x60;value&#x60; parameter, the function will remove any previous settings. | 
 **value** | **str**| The value for the preference of the variable that you want to manipulate.  * A valid SpamAssassin \&quot;&#x60;TEST_NAME SCORE&#x60;\&quot; value when the value of the &#x60;preference&#x60; parameter is &#x60;score&#x60;, where:      * &#x60;TEST_NAME&#x60; represents the symbolic name of the test. For list of symbolic test names, run the UAPI &#x60;SpamAssassin::get_symbolic_test_names&#x60; function.     * &#x60;SCORE&#x60; represents the floating-point value that SpamAssassin assigns to the mail when the test result is true. The score value must be greater than &#x60;0&#x60;, and less than &#x60;1000&#x60;.  * A valid floating-point number if the value of the &#x60;preference&#x60; parameter is &#x60;required_score&#x60;. * A valid email address if the value of the &#x60;preference&#x60; parameter is &#x60;whitelist_from&#x60; or &#x60;blacklist_from&#x60;. * A [custom SpamAssassin variable](https://spamassassin.apache.org/full/3.1.x/doc/Mail_SpamAssassin_Conf.html#user_preferences) value.  **Note:**  To enter multiple values, increment the parameter name. For example, use the &#x60;value-0&#x60; and &#x60;value-1&#x60; parameters. | [optional] 

### Return type

[**InlineResponse200487**](InlineResponse200487.md)

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

