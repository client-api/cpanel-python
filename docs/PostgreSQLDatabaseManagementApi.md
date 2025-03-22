# clientapi_cpanel.PostgreSQLDatabaseManagementApi

All URIs are relative to *https://cpanel-server.tld:2083/execute*

Method | HTTP request | Description
------------- | ------------- | -------------
[**postgresql_create_database**](PostgreSQLDatabaseManagementApi.md#postgresql_create_database) | **GET** /Postgresql/create_database | Create PostgreSQL database
[**postgresql_delete_database**](PostgreSQLDatabaseManagementApi.md#postgresql_delete_database) | **GET** /Postgresql/delete_database | Delete PostgreSQL database
[**postgresql_get_restrictions**](PostgreSQLDatabaseManagementApi.md#postgresql_get_restrictions) | **GET** /Postgresql/get_restrictions | Return PostgreSQL name length restrictions
[**postgresql_list_databases**](PostgreSQLDatabaseManagementApi.md#postgresql_list_databases) | **GET** /Postgresql/list_databases | Return PostgreSQL databases
[**rename_database**](PostgreSQLDatabaseManagementApi.md#rename_database) | **GET** /Postgresql/rename_database | Update PostgreSQL database name


# **postgresql_create_database**
> InlineResponse200378 postgresql_create_database(name)

Create PostgreSQL database

This function creates a PostgreSQL® database.

**Important:**

When you disable the [PostgreSQL role](https://go.cpanel.net/howtouseserverprofiles#roles), the system **disables** this function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200378 import InlineResponse200378
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
    api_instance = clientapi_cpanel.PostgreSQLDatabaseManagementApi(api_client)
    name = 'database' # str | The database's name.  **Note**:    If database prefixing is enabled, this parameter **must** include the database prefix for the account.

    try:
        # Create PostgreSQL database
        api_response = api_instance.postgresql_create_database(name)
        print("The response of PostgreSQLDatabaseManagementApi->postgresql_create_database:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PostgreSQLDatabaseManagementApi->postgresql_create_database: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The database&#39;s name.  **Note**:    If database prefixing is enabled, this parameter **must** include the database prefix for the account. | 

### Return type

[**InlineResponse200378**](InlineResponse200378.md)

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

# **postgresql_delete_database**
> InlineResponse200380 postgresql_delete_database(name)

Delete PostgreSQL database

This function deletes a PostgreSQL® database.

**Important:**

  When you disable the [Postgres role](https://go.cpanel.net/serverroles), the system **disables** this function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200380 import InlineResponse200380
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
    api_instance = clientapi_cpanel.PostgreSQLDatabaseManagementApi(api_client)
    name = 'database' # str | The database's name.

    try:
        # Delete PostgreSQL database
        api_response = api_instance.postgresql_delete_database(name)
        print("The response of PostgreSQLDatabaseManagementApi->postgresql_delete_database:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PostgreSQLDatabaseManagementApi->postgresql_delete_database: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The database&#39;s name. | 

### Return type

[**InlineResponse200380**](InlineResponse200380.md)

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

# **postgresql_get_restrictions**
> InlineResponse200382 postgresql_get_restrictions()

Return PostgreSQL name length restrictions

This function retrieves the PostgreSQL® user and database name length restrictions.

**Important:**

When you disable the [*PostgreSQL* role](https://go.cpanel.net/serverroles), the system **disables** this function.      

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200382 import InlineResponse200382
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
    api_instance = clientapi_cpanel.PostgreSQLDatabaseManagementApi(api_client)

    try:
        # Return PostgreSQL name length restrictions
        api_response = api_instance.postgresql_get_restrictions()
        print("The response of PostgreSQLDatabaseManagementApi->postgresql_get_restrictions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PostgreSQLDatabaseManagementApi->postgresql_get_restrictions: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**InlineResponse200382**](InlineResponse200382.md)

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

# **postgresql_list_databases**
> InlineResponse200384 postgresql_list_databases()

Return PostgreSQL databases

This function lists an account's PostgreSQL® databases.

**Important:**

  When you disable the [*Postgres* role](https://go.cpanel.net/serverroles), the system **disables** this function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200384 import InlineResponse200384
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
    api_instance = clientapi_cpanel.PostgreSQLDatabaseManagementApi(api_client)

    try:
        # Return PostgreSQL databases
        api_response = api_instance.postgresql_list_databases()
        print("The response of PostgreSQLDatabaseManagementApi->postgresql_list_databases:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PostgreSQLDatabaseManagementApi->postgresql_list_databases: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**InlineResponse200384**](InlineResponse200384.md)

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

# **rename_database**
> InlineResponse200386 rename_database(newname, oldname)

Update PostgreSQL database name

This function renames a PostgreSQL® database.

**Important:**

When you disable the [*PostgreSQL* role](https://go.cpanel.net/serverroles), the system **disables** this function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200386 import InlineResponse200386
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
    api_instance = clientapi_cpanel.PostgreSQLDatabaseManagementApi(api_client)
    newname = 'database2' # str | The database's new name.  **Note:**  If database prefixing is enabled, this parameter **must** include the database prefix for the account.
    oldname = 'database' # str | The database's current name.  **Note:**  If database prefixing is enabled, this parameter **must** include the database prefix for the account.

    try:
        # Update PostgreSQL database name
        api_response = api_instance.rename_database(newname, oldname)
        print("The response of PostgreSQLDatabaseManagementApi->rename_database:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PostgreSQLDatabaseManagementApi->rename_database: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **newname** | **str**| The database&#39;s new name.  **Note:**  If database prefixing is enabled, this parameter **must** include the database prefix for the account. | 
 **oldname** | **str**| The database&#39;s current name.  **Note:**  If database prefixing is enabled, this parameter **must** include the database prefix for the account. | 

### Return type

[**InlineResponse200386**](InlineResponse200386.md)

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

