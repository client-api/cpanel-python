# clientapi_cpanel.PostgresqlApi

All URIs are relative to *https://cpanel-server.tld:2083/execute*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_user**](PostgresqlApi.md#create_user) | **GET** /Postgresql/create_user | Create PostgreSQL user
[**grant_all_privileges**](PostgresqlApi.md#grant_all_privileges) | **GET** /Postgresql/grant_all_privileges | Enable all user privileges on PostgreSQL database
[**postgresql_create_database**](PostgresqlApi.md#postgresql_create_database) | **GET** /Postgresql/create_database | Create PostgreSQL database
[**postgresql_delete_database**](PostgresqlApi.md#postgresql_delete_database) | **GET** /Postgresql/delete_database | Delete PostgreSQL database
[**postgresql_delete_user**](PostgresqlApi.md#postgresql_delete_user) | **GET** /Postgresql/delete_user | Delete PostgreSQL user
[**postgresql_get_restrictions**](PostgresqlApi.md#postgresql_get_restrictions) | **GET** /Postgresql/get_restrictions | Return PostgreSQL name length restrictions
[**postgresql_list_databases**](PostgresqlApi.md#postgresql_list_databases) | **GET** /Postgresql/list_databases | Return PostgreSQL databases
[**postgresql_list_users**](PostgresqlApi.md#postgresql_list_users) | **GET** /Postgresql/list_users | Return PostgreSQL users
[**postgresql_rename_user**](PostgresqlApi.md#postgresql_rename_user) | **GET** /Postgresql/rename_user | Update PostgreSQL username
[**postgresql_update_privileges**](PostgresqlApi.md#postgresql_update_privileges) | **GET** /Postgresql/update_privileges | Update PostgreSQL® privileges
[**rename_database**](PostgresqlApi.md#rename_database) | **GET** /Postgresql/rename_database | Update PostgreSQL database name
[**rename_user_no_password**](PostgresqlApi.md#rename_user_no_password) | **GET** /Postgresql/rename_user_no_password | Update PostgreSQL username without password
[**revoke_all_privileges**](PostgresqlApi.md#revoke_all_privileges) | **GET** /Postgresql/revoke_all_privileges | Remove PostgreSQL user privileges
[**set_password**](PostgresqlApi.md#set_password) | **GET** /Postgresql/set_password | Update PostgreSQL user password


# **create_user**
> InlineResponse200379 create_user(name, password)

Create PostgreSQL user

This function creates a PostgreSQL® database user.

**Important:**

When you disable the [*PostgreSQL* role](https://go.cpanel.net/serverroles), the system **disables** this function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200379 import InlineResponse200379
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
    api_instance = clientapi_cpanel.PostgresqlApi(api_client)
    name = 'dbuser' # str | The database user's name.  **Note:**  If database prefixing is enabled, this parameter **must** include the database prefix for the account.
    password = '123456luggage' # str | The new user's password.

    try:
        # Create PostgreSQL user
        api_response = api_instance.create_user(name, password)
        print("The response of PostgresqlApi->create_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PostgresqlApi->create_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The database user&#39;s name.  **Note:**  If database prefixing is enabled, this parameter **must** include the database prefix for the account. | 
 **password** | **str**| The new user&#39;s password. | 

### Return type

[**InlineResponse200379**](InlineResponse200379.md)

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

# **grant_all_privileges**
> InlineResponse200383 grant_all_privileges(database, user)

Enable all user privileges on PostgreSQL database

This function grants all privileges for a PostgreSQL® database to a database user.

**Important:**

When you disable the [*PostgreSQL* role](https://go.cpanel.net/howtouseserverprofiles#roles), the system **disables** this function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200383 import InlineResponse200383
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
    api_instance = clientapi_cpanel.PostgresqlApi(api_client)
    database = 'example_database' # str | The database's name.  **Note**  If database prefixing is enabled, this value **must** include the database prefix for the account.
    user = 'example_dbuser' # str | The database user's name.  **Note**  If database prefixing is enabled, this value **must** include the database prefix for the account.

    try:
        # Enable all user privileges on PostgreSQL database
        api_response = api_instance.grant_all_privileges(database, user)
        print("The response of PostgresqlApi->grant_all_privileges:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PostgresqlApi->grant_all_privileges: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **database** | **str**| The database&#39;s name.  **Note**  If database prefixing is enabled, this value **must** include the database prefix for the account. | 
 **user** | **str**| The database user&#39;s name.  **Note**  If database prefixing is enabled, this value **must** include the database prefix for the account. | 

### Return type

[**InlineResponse200383**](InlineResponse200383.md)

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
    api_instance = clientapi_cpanel.PostgresqlApi(api_client)
    name = 'database' # str | The database's name.  **Note**:    If database prefixing is enabled, this parameter **must** include the database prefix for the account.

    try:
        # Create PostgreSQL database
        api_response = api_instance.postgresql_create_database(name)
        print("The response of PostgresqlApi->postgresql_create_database:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PostgresqlApi->postgresql_create_database: %s\n" % e)
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
    api_instance = clientapi_cpanel.PostgresqlApi(api_client)
    name = 'database' # str | The database's name.

    try:
        # Delete PostgreSQL database
        api_response = api_instance.postgresql_delete_database(name)
        print("The response of PostgresqlApi->postgresql_delete_database:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PostgresqlApi->postgresql_delete_database: %s\n" % e)
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

# **postgresql_delete_user**
> InlineResponse200381 postgresql_delete_user(name)

Delete PostgreSQL user

This function deletes a PostgreSQL® user.

**Important:**

  When you disable the [PostgreSQL role](https://go.cpanel.net/serverroles), the system **disables** this function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200381 import InlineResponse200381
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
    api_instance = clientapi_cpanel.PostgresqlApi(api_client)
    name = 'example' # str | The PostgreSQL user's name.

    try:
        # Delete PostgreSQL user
        api_response = api_instance.postgresql_delete_user(name)
        print("The response of PostgresqlApi->postgresql_delete_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PostgresqlApi->postgresql_delete_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The PostgreSQL user&#39;s name. | 

### Return type

[**InlineResponse200381**](InlineResponse200381.md)

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
    api_instance = clientapi_cpanel.PostgresqlApi(api_client)

    try:
        # Return PostgreSQL name length restrictions
        api_response = api_instance.postgresql_get_restrictions()
        print("The response of PostgresqlApi->postgresql_get_restrictions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PostgresqlApi->postgresql_get_restrictions: %s\n" % e)
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
    api_instance = clientapi_cpanel.PostgresqlApi(api_client)

    try:
        # Return PostgreSQL databases
        api_response = api_instance.postgresql_list_databases()
        print("The response of PostgresqlApi->postgresql_list_databases:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PostgresqlApi->postgresql_list_databases: %s\n" % e)
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

# **postgresql_list_users**
> InlineResponse200385 postgresql_list_users()

Return PostgreSQL users

This function lists an account's PostgreSQL® database users.

**Important:**

When you disable the [*PostgreSQL* role](https://go.cpanel.net/serverroles), the system **disables** this function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200385 import InlineResponse200385
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
    api_instance = clientapi_cpanel.PostgresqlApi(api_client)

    try:
        # Return PostgreSQL users
        api_response = api_instance.postgresql_list_users()
        print("The response of PostgresqlApi->postgresql_list_users:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PostgresqlApi->postgresql_list_users: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**InlineResponse200385**](InlineResponse200385.md)

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

# **postgresql_rename_user**
> InlineResponse200387 postgresql_rename_user(newname, oldname, password)

Update PostgreSQL username

This function renames a PostgreSQL® database user.

**Important:**

When you disable the [*PostgreSQL* role](https://go.cpanel.net/serverroles), the system **disables** this function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200387 import InlineResponse200387
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
    api_instance = clientapi_cpanel.PostgresqlApi(api_client)
    newname = 'dbuser2' # str | The database user's new name.  **Note:**  If database prefixing is enabled, this parameter **must** include the database prefix for the account.
    oldname = 'dbuser' # str | The database user's current name.  **Note:**  If database prefixing is enabled, this parameter **must** include the database prefix for the account.
    password = '123456luggage' # str | The database user's new password.

    try:
        # Update PostgreSQL username
        api_response = api_instance.postgresql_rename_user(newname, oldname, password)
        print("The response of PostgresqlApi->postgresql_rename_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PostgresqlApi->postgresql_rename_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **newname** | **str**| The database user&#39;s new name.  **Note:**  If database prefixing is enabled, this parameter **must** include the database prefix for the account. | 
 **oldname** | **str**| The database user&#39;s current name.  **Note:**  If database prefixing is enabled, this parameter **must** include the database prefix for the account. | 
 **password** | **str**| The database user&#39;s new password. | 

### Return type

[**InlineResponse200387**](InlineResponse200387.md)

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

# **postgresql_update_privileges**
> InlineResponse200391 postgresql_update_privileges()

Update PostgreSQL® privileges

This function synchronizes PostgreSQL® database user privileges on an account.

Some versions of PostgreSQL are ANSI SQL-92 compliant and do not support recursive grants,
wildcard grants, or future grants. If you use phpPgAdmin, or manually create new tables, and
you want multiple PostgreSQL users to access your PostgreSQL tables, you may either call this
API function or click _Synchronize Grants_ in the _PostgreSQL Databases_ interface
(_Home >> Databases >> PostgreSQL Databases_) after you add a table.

**Important:**

When you disable the [PostgreSQL role](https://go.cpanel.net/serverroles), the system **disables** this function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200391 import InlineResponse200391
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
    api_instance = clientapi_cpanel.PostgresqlApi(api_client)

    try:
        # Update PostgreSQL® privileges
        api_response = api_instance.postgresql_update_privileges()
        print("The response of PostgresqlApi->postgresql_update_privileges:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PostgresqlApi->postgresql_update_privileges: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**InlineResponse200391**](InlineResponse200391.md)

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
    api_instance = clientapi_cpanel.PostgresqlApi(api_client)
    newname = 'database2' # str | The database's new name.  **Note:**  If database prefixing is enabled, this parameter **must** include the database prefix for the account.
    oldname = 'database' # str | The database's current name.  **Note:**  If database prefixing is enabled, this parameter **must** include the database prefix for the account.

    try:
        # Update PostgreSQL database name
        api_response = api_instance.rename_database(newname, oldname)
        print("The response of PostgresqlApi->rename_database:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PostgresqlApi->rename_database: %s\n" % e)
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

# **rename_user_no_password**
> InlineResponse200388 rename_user_no_password(newname, oldname)

Update PostgreSQL username without password

This function renames a PostgreSQL® database user.

**Warning:**

* If you rename a PostgreSQL user, you **must** set the password for the database user. This is required because of the md5 hash that PostgreSQL creates to store user passwords.
* We **strongly** recommend that you use the `Postgresql::rename_user function` instead of this one.

**Important:**

When you disable the  [*PostgreSQL* role](https://go.cpanel.net/serverroles), the system **disables** this function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200388 import InlineResponse200388
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
    api_instance = clientapi_cpanel.PostgresqlApi(api_client)
    newname = 'dbuser2' # str | The database user's new name.  **Note:**  If database prefixing is enabled, this parameter **must** include the database prefix for the account.
    oldname = 'dbuser' # str | The database user's current name.  **Note:**  If database prefixing is enabled, this parameter **must** include the database prefix for the account.

    try:
        # Update PostgreSQL username without password
        api_response = api_instance.rename_user_no_password(newname, oldname)
        print("The response of PostgresqlApi->rename_user_no_password:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PostgresqlApi->rename_user_no_password: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **newname** | **str**| The database user&#39;s new name.  **Note:**  If database prefixing is enabled, this parameter **must** include the database prefix for the account. | 
 **oldname** | **str**| The database user&#39;s current name.  **Note:**  If database prefixing is enabled, this parameter **must** include the database prefix for the account. | 

### Return type

[**InlineResponse200388**](InlineResponse200388.md)

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

# **revoke_all_privileges**
> InlineResponse200389 revoke_all_privileges(database, user)

Remove PostgreSQL user privileges

This function revokes all privileges for a PostgreSQL® database from a database user.

**Important:**

When you disable the [*PostgreSQL* role](https://go.cpanel.net/serverroles), the system **disables** this function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200389 import InlineResponse200389
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
    api_instance = clientapi_cpanel.PostgresqlApi(api_client)
    database = 'example_database' # str | The database's name.  **Note**  If database prefixing is enabled, this value **must** include the database prefix for the account.
    user = 'example_dbuser' # str | The database user's name.  **Note**  If database prefixing is enabled, this value **must** include the database prefix for the account.

    try:
        # Remove PostgreSQL user privileges
        api_response = api_instance.revoke_all_privileges(database, user)
        print("The response of PostgresqlApi->revoke_all_privileges:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PostgresqlApi->revoke_all_privileges: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **database** | **str**| The database&#39;s name.  **Note**  If database prefixing is enabled, this value **must** include the database prefix for the account. | 
 **user** | **str**| The database user&#39;s name.  **Note**  If database prefixing is enabled, this value **must** include the database prefix for the account. | 

### Return type

[**InlineResponse200389**](InlineResponse200389.md)

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

# **set_password**
> InlineResponse200390 set_password(password, user)

Update PostgreSQL user password

This function changes a PostgreSQL® database user's password.

**Important:**

  When you disable the [Postgres role](https://go.cpanel.net/serverroles), the system **disables** this function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200390 import InlineResponse200390
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
    api_instance = clientapi_cpanel.PostgresqlApi(api_client)
    password = '12345luggage' # str | The user's new password.
    user = 'dbuser' # str | The database user's name.  **Note:**  If database prefixing is enabled, this parameter **must** include the database prefix for the account.

    try:
        # Update PostgreSQL user password
        api_response = api_instance.set_password(password, user)
        print("The response of PostgresqlApi->set_password:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PostgresqlApi->set_password: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **password** | **str**| The user&#39;s new password. | 
 **user** | **str**| The database user&#39;s name.  **Note:**  If database prefixing is enabled, this parameter **must** include the database prefix for the account. | 

### Return type

[**InlineResponse200390**](InlineResponse200390.md)

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

