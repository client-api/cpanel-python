# clientapi_cpanel.SigningAndEncryptionGnuPGKeysApi

All URIs are relative to *https://cpanel-server.tld:2083/execute*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_keypair**](SigningAndEncryptionGnuPGKeysApi.md#delete_keypair) | **GET** /GPG/delete_keypair | Delete GnuPG key pair
[**export_public_key**](SigningAndEncryptionGnuPGKeysApi.md#export_public_key) | **GET** /GPG/export_public_key | Export GnuPG public key
[**export_secret_key**](SigningAndEncryptionGnuPGKeysApi.md#export_secret_key) | **GET** /GPG/export_secret_key | Export GnuPG secret key
[**generate_key**](SigningAndEncryptionGnuPGKeysApi.md#generate_key) | **GET** /GPG/generate_key | Create GnuPG key
[**import_key**](SigningAndEncryptionGnuPGKeysApi.md#import_key) | **GET** /GPG/import_key | Import GnuPG key
[**list_public_keys**](SigningAndEncryptionGnuPGKeysApi.md#list_public_keys) | **GET** /GPG/list_public_keys | Return current user&#39;s GnuPG public keys
[**list_secret_keys**](SigningAndEncryptionGnuPGKeysApi.md#list_secret_keys) | **GET** /GPG/list_secret_keys | Return current user&#39;s GnuPG secret keys


# **delete_keypair**
> InlineResponse200263 delete_keypair(key_id)

Delete GnuPG key pair

This function deletes a GnuPG (GPG) key pair.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200263 import InlineResponse200263
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
    api_instance = clientapi_cpanel.SigningAndEncryptionGnuPGKeysApi(api_client)
    key_id = 'ACFFDB37176B680D' # str | The ID of the GPG key that you wish to delete.  **Note:**  * The function will delete **all** keys that match this ID.   * If you set this parameter to a public key, the function will delete the public key.    * If you set this parameter to a public and private key pair, the function will delete the public and private keys. * To obtain the desired key, call the UAPI `GPG::list_secret_keys` function.

    try:
        # Delete GnuPG key pair
        api_response = api_instance.delete_keypair(key_id)
        print("The response of SigningAndEncryptionGnuPGKeysApi->delete_keypair:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SigningAndEncryptionGnuPGKeysApi->delete_keypair: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key_id** | **str**| The ID of the GPG key that you wish to delete.  **Note:**  * The function will delete **all** keys that match this ID.   * If you set this parameter to a public key, the function will delete the public key.    * If you set this parameter to a public and private key pair, the function will delete the public and private keys. * To obtain the desired key, call the UAPI &#x60;GPG::list_secret_keys&#x60; function. | 

### Return type

[**InlineResponse200263**](InlineResponse200263.md)

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

# **export_public_key**
> InlineResponse200264 export_public_key(key_id)

Export GnuPG public key

This function exports a GnuPG (GPG) public key.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200264 import InlineResponse200264
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
    api_instance = clientapi_cpanel.SigningAndEncryptionGnuPGKeysApi(api_client)
    key_id = '48BEA5A16FCA746E' # str | The ID of the GPG key.

    try:
        # Export GnuPG public key
        api_response = api_instance.export_public_key(key_id)
        print("The response of SigningAndEncryptionGnuPGKeysApi->export_public_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SigningAndEncryptionGnuPGKeysApi->export_public_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key_id** | **str**| The ID of the GPG key. | 

### Return type

[**InlineResponse200264**](InlineResponse200264.md)

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

# **export_secret_key**
> InlineResponse200265 export_secret_key(key_id, passphrase=passphrase)

Export GnuPG secret key

This function exports a GnuPG (GPG) secret key.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200265 import InlineResponse200265
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
    api_instance = clientapi_cpanel.SigningAndEncryptionGnuPGKeysApi(api_client)
    key_id = '48BEA5A16FCA746E' # str | The ID of the GPG secret key that you wish to retrieve.
    passphrase = 'whatever' # str | The passphrase of the GPG secret key that you wish to retrieve. (optional)

    try:
        # Export GnuPG secret key
        api_response = api_instance.export_secret_key(key_id, passphrase=passphrase)
        print("The response of SigningAndEncryptionGnuPGKeysApi->export_secret_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SigningAndEncryptionGnuPGKeysApi->export_secret_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key_id** | **str**| The ID of the GPG secret key that you wish to retrieve. | 
 **passphrase** | **str**| The passphrase of the GPG secret key that you wish to retrieve. | [optional] 

### Return type

[**InlineResponse200265**](InlineResponse200265.md)

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

# **generate_key**
> InlineResponse200266 generate_key(email, name, passphrase, comment=comment, expire=expire, keysize=keysize, no_expire=no_expire)

Create GnuPG key

This function generates a GnuPG (GPG) key. The system saves the key in the user's `.gnupg` directory.

**Note:**

This function uses [the system's entropy](https://en.wikipedia.org/wiki/Entropy_(computing)) to generate the key. Systems with low entropy levels may cause long generation times or timeouts.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200266 import InlineResponse200266
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
    api_instance = clientapi_cpanel.SigningAndEncryptionGnuPGKeysApi(api_client)
    email = 'user@example.com' # str | The user's email address.
    name = 'username' # str | The name of the user for whom to generate the key.
    passphrase = '123456luggage' # str | The key's password.
    comment = 'Username\'s Key' # str | A comment about the key. (optional)
    expire = '1560363242' # str | The desired expiration date of the key as a timestamp in [Unix time format](http://en.wikipedia.org/wiki/Unix_time).  **Note:**  This will default to one year from the current date. (optional)
    keysize = 2048 # int | The new key's size, in bytes.  **Note:**  Large keys require more time to generate. (optional) (default to 2048)
    no_expire = 0 # int | Whether to generate the key without an expiration date.  * `0` - The key will expire. * `1` - The key will **not** expire. (optional) (default to 0)

    try:
        # Create GnuPG key
        api_response = api_instance.generate_key(email, name, passphrase, comment=comment, expire=expire, keysize=keysize, no_expire=no_expire)
        print("The response of SigningAndEncryptionGnuPGKeysApi->generate_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SigningAndEncryptionGnuPGKeysApi->generate_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**| The user&#39;s email address. | 
 **name** | **str**| The name of the user for whom to generate the key. | 
 **passphrase** | **str**| The key&#39;s password. | 
 **comment** | **str**| A comment about the key. | [optional] 
 **expire** | **str**| The desired expiration date of the key as a timestamp in [Unix time format](http://en.wikipedia.org/wiki/Unix_time).  **Note:**  This will default to one year from the current date. | [optional] 
 **keysize** | **int**| The new key&#39;s size, in bytes.  **Note:**  Large keys require more time to generate. | [optional] [default to 2048]
 **no_expire** | **int**| Whether to generate the key without an expiration date.  * &#x60;0&#x60; - The key will expire. * &#x60;1&#x60; - The key will **not** expire. | [optional] [default to 0]

### Return type

[**InlineResponse200266**](InlineResponse200266.md)

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

# **import_key**
> InlineResponse200267 import_key(key_data)

Import GnuPG key

This function imports a GnuPG (GPG) key.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200267 import InlineResponse200267
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
    api_instance = clientapi_cpanel.SigningAndEncryptionGnuPGKeysApi(api_client)
    key_data = '%0A-----BEGIN%20PGP%20PUBLIC%20KEY%20BLOCK-----%0AVersion%3A%20GnuPG%20v2.0.14%20(GNU%2FLinux)%0A%0AmQENBFN0%2BOsBCADoFvyf8gHIKZ%2F%2B5KwbWb3Ht%2Fz1ukyQqFNGpBVIqHossmjmyF9e%0APn6iiZ0fHnt7r6XGGXaP%2BKKjIxAcqOTiFiP%2BHIx6GQubzVih6Ol0YNjzmK%2Ft4f%2B4%0AfSElEVnyzeyJa4LmC%2Fui%2FvvtptJ8JX6su7f11BwUTSyuqnk204AfN5uVpAcZNPT0%0A0qNNky1bxYvPUxU6Imvi1q3NtpFzqsQ4u%2FyZuLpUe7uwmgMPeO0lAms1kCa3Guot%0A3mfSt0vrUAMdcV4drY1FGtYZdYSa4rSTzpFuB7o9Ze%2BE3fUbCWs1%2B0FiN3JQNGO1%0AS2lnqjEqbpz2nHtA50elJRGqxZLEi8zkFqlTABEBAAG0Z2NQYW5lbCBTZWN1cml0%0AeSBUZWFtIC0gVEVTVCAoVEhJUyBJUyBBIFRFU1QgS0VZOyBETyBOT1QgVVNFIEZP%0AUiBBTllUSElORyBSRUFMISkgPHNlY3RlYW1zaXhAY3BhbmVsLm5ldD6JAT4EEwEC%0AACgFAlN0%2BOsCGwMFCQHhM4AGCwkIBwMCBhUIAgkKCwQWAgMBAh4BAheAAAoJEOhU%0A60c9RtoRkhMIAIe2yDKj55mGD3zbuGqxx6NNNIyiuEujw31N8yOS9BKTqGtIiK9i%0AGu4lzrzmHISKi0rjKmJdbckap7OouUoo9WR3ewjN6S5EHyjKfrrMwMzTWMPZOkTj%0A7A698X0vGc9yZ6KyBj8mM8J9duvNtRS285hfXfQxYO%2FuiyrJGBedI%2FWVZ3a7mcfq%0A7FhC8t6jU6sz9uIvYHAzywcVdmhEK5rS%2FuE%2F9e37h46jn2%2BkzlIWEe%2FYgpa%2BuWdT%0AO%2BOyqteW51LEjXLWMyP8AJEq8EoqbqKnm4Q1g0etOQ9trrkLUnPxaSwD5R6i4KLH%0AMR%2Fh7m%2FOoz8yOhUlrCGJwX7v9qDEdaYYFLQ%3D%0A%3DMEFZ%0A-----END%20PGP%20PUBLIC%20KEY%20BLOCK-----%0A' # str | The key to import.  **Note:**  You must URI-encode this value.

    try:
        # Import GnuPG key
        api_response = api_instance.import_key(key_data)
        print("The response of SigningAndEncryptionGnuPGKeysApi->import_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SigningAndEncryptionGnuPGKeysApi->import_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key_data** | **str**| The key to import.  **Note:**  You must URI-encode this value. | 

### Return type

[**InlineResponse200267**](InlineResponse200267.md)

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

# **list_public_keys**
> InlineResponse200268 list_public_keys()

Return current user's GnuPG public keys

This function lists the GnuPG (GPG) public keys for the
currently-authenticated account.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200268 import InlineResponse200268
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
    api_instance = clientapi_cpanel.SigningAndEncryptionGnuPGKeysApi(api_client)

    try:
        # Return current user's GnuPG public keys
        api_response = api_instance.list_public_keys()
        print("The response of SigningAndEncryptionGnuPGKeysApi->list_public_keys:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SigningAndEncryptionGnuPGKeysApi->list_public_keys: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**InlineResponse200268**](InlineResponse200268.md)

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

# **list_secret_keys**
> InlineResponse200269 list_secret_keys()

Return current user's GnuPG secret keys

This function lists the GnuPG (GPG) secret keys for the currently-authenticated account.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200269 import InlineResponse200269
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
    api_instance = clientapi_cpanel.SigningAndEncryptionGnuPGKeysApi(api_client)

    try:
        # Return current user's GnuPG secret keys
        api_response = api_instance.list_secret_keys()
        print("The response of SigningAndEncryptionGnuPGKeysApi->list_secret_keys:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SigningAndEncryptionGnuPGKeysApi->list_secret_keys: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**InlineResponse200269**](InlineResponse200269.md)

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

