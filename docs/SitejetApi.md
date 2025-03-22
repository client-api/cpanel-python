# clientapi_cpanel.SitejetApi

All URIs are relative to *https://cpanel-server.tld:2083/execute*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_sitejet_api_token**](SitejetApi.md#add_sitejet_api_token) | **GET** /Sitejet/add_api_token | Add an existing Sitejet API token.
[**create_restore_point**](SitejetApi.md#create_restore_point) | **GET** /Sitejet/create_restore_point | Create a restore point.
[**create_sitejet_account**](SitejetApi.md#create_sitejet_account) | **GET** /Sitejet/create_account | Generate a Sitejet API key.
[**create_sitejet_website**](SitejetApi.md#create_sitejet_website) | **GET** /Sitejet/create_website | Create Sitejet domain ID
[**get_all_user_sitejet_info**](SitejetApi.md#get_all_user_sitejet_info) | **GET** /Sitejet/get_all_user_sitejet_info | Return Sitejet domains
[**get_sitejet_api_token**](SitejetApi.md#get_sitejet_api_token) | **GET** /Sitejet/get_api_token | Return Sitejet API token
[**get_sitejet_preview_url**](SitejetApi.md#get_sitejet_preview_url) | **GET** /Sitejet/get_preview_url | Return Sitejet preview URL
[**get_sitejet_sso_link**](SitejetApi.md#get_sitejet_sso_link) | **GET** /Sitejet/get_sso_link | Return Sitejet SSO URL
[**get_sitejet_templates**](SitejetApi.md#get_sitejet_templates) | **GET** /Sitejet/get_templates | Return Sitejet templates
[**restore_document_root**](SitejetApi.md#restore_document_root) | **GET** /Sitejet/restore_document_root | Restore a domain from the restore point.
[**set_sitejet_template**](SitejetApi.md#set_sitejet_template) | **GET** /Sitejet/set_template | Update Sitejet template
[**start_publish_sitejet**](SitejetApi.md#start_publish_sitejet) | **GET** /Sitejet/start_publish | Publish Sitejet domain


# **add_sitejet_api_token**
> InlineResponse200472 add_sitejet_api_token(api_token)

Add an existing Sitejet API token.

This function adds an existing Sitejet API token to a cPanel user.

**Note:** 

You can create a Sitejet API token with the `Sitejet:create_account` function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200472 import InlineResponse200472
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
    api_instance = clientapi_cpanel.SitejetApi(api_client)
    api_token = 'd35d8ea651007ccd25f96486cdcdXXXX' # str | The Sitejet API token to add.

    try:
        # Add an existing Sitejet API token.
        api_response = api_instance.add_sitejet_api_token(api_token)
        print("The response of SitejetApi->add_sitejet_api_token:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SitejetApi->add_sitejet_api_token: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_token** | **str**| The Sitejet API token to add. | 

### Return type

[**InlineResponse200472**](InlineResponse200472.md)

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

# **create_restore_point**
> InlineResponse200474 create_restore_point(domain)

Create a restore point.

This function creates a restore point for a domain's document root and removes the domain's files.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200474 import InlineResponse200474
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
    api_instance = clientapi_cpanel.SitejetApi(api_client)
    domain = 'example.com' # str | A cPanel account's domain.

    try:
        # Create a restore point.
        api_response = api_instance.create_restore_point(domain)
        print("The response of SitejetApi->create_restore_point:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SitejetApi->create_restore_point: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**| A cPanel account&#39;s domain. | 

### Return type

[**InlineResponse200474**](InlineResponse200474.md)

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

# **create_sitejet_account**
> InlineResponse200473 create_sitejet_account()

Generate a Sitejet API key.

This function creates a Sitejet API token for a cPanel account.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200473 import InlineResponse200473
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
    api_instance = clientapi_cpanel.SitejetApi(api_client)

    try:
        # Generate a Sitejet API key.
        api_response = api_instance.create_sitejet_account()
        print("The response of SitejetApi->create_sitejet_account:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SitejetApi->create_sitejet_account: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**InlineResponse200473**](InlineResponse200473.md)

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

# **create_sitejet_website**
> InlineResponse200475 create_sitejet_website(company, domain, assign_to=assign_to, city=city, country=country, email=email, firstname=firstname, language=language, lastname=lastname, metadata=metadata, note=note, phone=phone, street=street, title=title, zip=zip)

Create Sitejet domain ID

This function creates a Sitejet ID for the specified domain.

**Note:**

A unique Sitejet ID is assigned to each domain on the cPanel account.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200475 import InlineResponse200475
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
    api_instance = clientapi_cpanel.SitejetApi(api_client)
    company = 'cPanel' # str | The name of the company the website represents.
    domain = 'example.com' # str | A cPanel account's domain.
    assign_to = 'SallySmith@example.com' # str | Assign website to other user. (optional)
    city = 'Capitol City' # str | The city where the company or website owner is located. (optional)
    country = 'US' # str | The country where the company or website owner is located. (optional)
    email = 'JohnSmith@example.com' # str | The email address of the website owner. (optional)
    firstname = 'John' # str | The first name of the website owner. (optional)
    language = 'en' # str | The language to use for the Sitejet Website Builder. (optional)
    lastname = 'Smith' # str | The last name of the website owner. (optional)
    metadata = '{\"Attribute1\":9,\"Attribute2\":3,\"Attribute3\":5}' # str | Additional metadata for the website. (optional)
    note = 'This is my website for my business.' # str | Additional notes about the website. (optional)
    phone = '000-123-4567' # str | The phone number of the company or website owner. (optional)
    street = '1234 Main St' # str | The street address of the company or website owner. (optional)
    title = 'Example Website' # str | The website title. (optional)
    zip = '99999' # str | The zip code where the company or website owner is located. (optional)

    try:
        # Create Sitejet domain ID
        api_response = api_instance.create_sitejet_website(company, domain, assign_to=assign_to, city=city, country=country, email=email, firstname=firstname, language=language, lastname=lastname, metadata=metadata, note=note, phone=phone, street=street, title=title, zip=zip)
        print("The response of SitejetApi->create_sitejet_website:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SitejetApi->create_sitejet_website: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company** | **str**| The name of the company the website represents. | 
 **domain** | **str**| A cPanel account&#39;s domain. | 
 **assign_to** | **str**| Assign website to other user. | [optional] 
 **city** | **str**| The city where the company or website owner is located. | [optional] 
 **country** | **str**| The country where the company or website owner is located. | [optional] 
 **email** | **str**| The email address of the website owner. | [optional] 
 **firstname** | **str**| The first name of the website owner. | [optional] 
 **language** | **str**| The language to use for the Sitejet Website Builder. | [optional] 
 **lastname** | **str**| The last name of the website owner. | [optional] 
 **metadata** | **str**| Additional metadata for the website. | [optional] 
 **note** | **str**| Additional notes about the website. | [optional] 
 **phone** | **str**| The phone number of the company or website owner. | [optional] 
 **street** | **str**| The street address of the company or website owner. | [optional] 
 **title** | **str**| The website title. | [optional] 
 **zip** | **str**| The zip code where the company or website owner is located. | [optional] 

### Return type

[**InlineResponse200475**](InlineResponse200475.md)

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

# **get_all_user_sitejet_info**
> InlineResponse200476 get_all_user_sitejet_info(domain=domain)

Return Sitejet domains

This function returns the Sitejet domains' information for the cPanel account.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200476 import InlineResponse200476
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
    api_instance = clientapi_cpanel.SitejetApi(api_client)
    domain = 'example.com' # str | The single domain to return Sitejet information. (optional)

    try:
        # Return Sitejet domains
        api_response = api_instance.get_all_user_sitejet_info(domain=domain)
        print("The response of SitejetApi->get_all_user_sitejet_info:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SitejetApi->get_all_user_sitejet_info: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**| The single domain to return Sitejet information. | [optional] 

### Return type

[**InlineResponse200476**](InlineResponse200476.md)

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

# **get_sitejet_api_token**
> InlineResponse200477 get_sitejet_api_token()

Return Sitejet API token

This function returns the cPanel account's Sitejet API token.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200477 import InlineResponse200477
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
    api_instance = clientapi_cpanel.SitejetApi(api_client)

    try:
        # Return Sitejet API token
        api_response = api_instance.get_sitejet_api_token()
        print("The response of SitejetApi->get_sitejet_api_token:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SitejetApi->get_sitejet_api_token: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**InlineResponse200477**](InlineResponse200477.md)

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

# **get_sitejet_preview_url**
> InlineResponse200478 get_sitejet_preview_url(website_id)

Return Sitejet preview URL

This function returns a Sitejet website's preview URL.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200478 import InlineResponse200478
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
    api_instance = clientapi_cpanel.SitejetApi(api_client)
    website_id = 123456 # int | The Sitejet website ID for the domain.

    try:
        # Return Sitejet preview URL
        api_response = api_instance.get_sitejet_preview_url(website_id)
        print("The response of SitejetApi->get_sitejet_preview_url:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SitejetApi->get_sitejet_preview_url: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **website_id** | **int**| The Sitejet website ID for the domain. | 

### Return type

[**InlineResponse200478**](InlineResponse200478.md)

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

# **get_sitejet_sso_link**
> InlineResponse200479 get_sitejet_sso_link(domain, referrer)

Return Sitejet SSO URL

This function returns a Sitejet website's SSO URL.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200479 import InlineResponse200479
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
    api_instance = clientapi_cpanel.SitejetApi(api_client)
    domain = 'example.com' # str | The cPanel account's Sitejet domain.
    referrer = 'https://example.com:2083/cpsess##########/frontend/jupiter/sitejet/index.html%23' # str | The cPanel interface referral URL.

    try:
        # Return Sitejet SSO URL
        api_response = api_instance.get_sitejet_sso_link(domain, referrer)
        print("The response of SitejetApi->get_sitejet_sso_link:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SitejetApi->get_sitejet_sso_link: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**| The cPanel account&#39;s Sitejet domain. | 
 **referrer** | **str**| The cPanel interface referral URL. | 

### Return type

[**InlineResponse200479**](InlineResponse200479.md)

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

# **get_sitejet_templates**
> InlineResponse200480 get_sitejet_templates()

Return Sitejet templates

This function fetches the list of available Sitejet templates.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200480 import InlineResponse200480
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
    api_instance = clientapi_cpanel.SitejetApi(api_client)

    try:
        # Return Sitejet templates
        api_response = api_instance.get_sitejet_templates()
        print("The response of SitejetApi->get_sitejet_templates:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SitejetApi->get_sitejet_templates: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**InlineResponse200480**](InlineResponse200480.md)

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

# **restore_document_root**
> InlineResponse200481 restore_document_root(domain)

Restore a domain from the restore point.

This function reverts a document root to the restore point.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200481 import InlineResponse200481
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
    api_instance = clientapi_cpanel.SitejetApi(api_client)
    domain = 'example.com' # str | A cPanel account's domain.

    try:
        # Restore a domain from the restore point.
        api_response = api_instance.restore_document_root(domain)
        print("The response of SitejetApi->restore_document_root:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SitejetApi->restore_document_root: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**| A cPanel account&#39;s domain. | 

### Return type

[**InlineResponse200481**](InlineResponse200481.md)

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

# **set_sitejet_template**
> InlineResponse200482 set_sitejet_template(domain, template_id, template_name)

Update Sitejet template

This function sets a Sitejet website's template.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200482 import InlineResponse200482
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
    api_instance = clientapi_cpanel.SitejetApi(api_client)
    domain = 'example.com' # str | A cPanel account's domain.
    template_id = '12345' # str | The Sitejet template's ID.
    template_name = 'A great template' # str | The Sitejet template name.

    try:
        # Update Sitejet template
        api_response = api_instance.set_sitejet_template(domain, template_id, template_name)
        print("The response of SitejetApi->set_sitejet_template:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SitejetApi->set_sitejet_template: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**| A cPanel account&#39;s domain. | 
 **template_id** | **str**| The Sitejet template&#39;s ID. | 
 **template_name** | **str**| The Sitejet template name. | 

### Return type

[**InlineResponse200482**](InlineResponse200482.md)

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

# **start_publish_sitejet**
> InlineResponse200483 start_publish_sitejet(domain, cleanup=cleanup)

Publish Sitejet domain

This function publishes a domain's Sitejet website.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200483 import InlineResponse200483
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
    api_instance = clientapi_cpanel.SitejetApi(api_client)
    domain = 'example.com' # str | The domain for the Sitejet website.
    cleanup = 1 # int | Whether to cleanup the domain's `document_root` directory during the publication process. * `1` — Remove previous files in domain's `document_root` directory during the publication process. * `0` — Do **not** remove any files in domain's `document_root` directory during the publication process. (optional)

    try:
        # Publish Sitejet domain
        api_response = api_instance.start_publish_sitejet(domain, cleanup=cleanup)
        print("The response of SitejetApi->start_publish_sitejet:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SitejetApi->start_publish_sitejet: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**| The domain for the Sitejet website. | 
 **cleanup** | **int**| Whether to cleanup the domain&#39;s &#x60;document_root&#x60; directory during the publication process. * &#x60;1&#x60; — Remove previous files in domain&#39;s &#x60;document_root&#x60; directory during the publication process. * &#x60;0&#x60; — Do **not** remove any files in domain&#39;s &#x60;document_root&#x60; directory during the publication process. | [optional] 

### Return type

[**InlineResponse200483**](InlineResponse200483.md)

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

