# clientapi_cpanel.DatabaseManagementApi

All URIs are relative to *https://cpanel-server.tld:2083/execute*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_database**](DatabaseManagementApi.md#create_database) | **GET** /Mysql/create_database | Create MySQL database
[**delete_database**](DatabaseManagementApi.md#delete_database) | **GET** /Mysql/delete_database | Delete MySQL database
[**dump_database_schema**](DatabaseManagementApi.md#dump_database_schema) | **GET** /Mysql/dump_database_schema | Return MySQL database schema
[**list_databases**](DatabaseManagementApi.md#list_databases) | **GET** /Mysql/list_databases | Return MySQL databases
[**mysql_check_database**](DatabaseManagementApi.md#mysql_check_database) | **GET** /Mysql/check_database | Validate MySQL database integrity
[**mysql_rename_database**](DatabaseManagementApi.md#mysql_rename_database) | **GET** /Mysql/rename_database | Update MySQL database name
[**mysql_update_privileges**](DatabaseManagementApi.md#mysql_update_privileges) | **GET** /Mysql/update_privileges | Update MySQL® privileges
[**repair_database**](DatabaseManagementApi.md#repair_database) | **GET** /Mysql/repair_database | Repair MySQL database tables
[**setup_db_and_user**](DatabaseManagementApi.md#setup_db_and_user) | **GET** /Mysql/setup_db_and_user | Create a randomly named MySQL username/database set.


# **create_database**
> InlineResponse200339 create_database(name, prefix_size=prefix_size)

Create MySQL database

This function creates a MySQL® database.

**Important:**

  When you disable the [MySQL/MariaDB role](https://go.cpanel.net/howtouseserverprofiles#roles) **and** remote MySQL is **not** already configured, the system **disables** this function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200339 import InlineResponse200339
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
    api_instance = clientapi_cpanel.DatabaseManagementApi(api_client)
    name = 'newdb' # str | The new database's name.
    prefix_size = 16 # int | The desired prefix size. (optional) (default to 16)

    try:
        # Create MySQL database
        api_response = api_instance.create_database(name, prefix_size=prefix_size)
        print("The response of DatabaseManagementApi->create_database:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatabaseManagementApi->create_database: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The new database&#39;s name. | 
 **prefix_size** | **int**| The desired prefix size. | [optional] [default to 16]

### Return type

[**InlineResponse200339**](InlineResponse200339.md)

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

# **delete_database**
> InlineResponse200341 delete_database(name)

Delete MySQL database

This function deletes a MySQL® database.

**Important:**

when you disable the [MySQL/MariaDB role](https://go.cpanel.net/serverroles#roles) **and**
remote MySQL is **not** already configured, the system **disables** this function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200341 import InlineResponse200341
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
    api_instance = clientapi_cpanel.DatabaseManagementApi(api_client)
    name = 'example' # str | The database's name.

    try:
        # Delete MySQL database
        api_response = api_instance.delete_database(name)
        print("The response of DatabaseManagementApi->delete_database:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatabaseManagementApi->delete_database: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The database&#39;s name. | 

### Return type

[**InlineResponse200341**](InlineResponse200341.md)

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

# **dump_database_schema**
> InlineResponse200344 dump_database_schema(dbname)

Return MySQL database schema

This function returns a string that you can give to MySQL® to recreate a particular database’s schema.

**Important:**

  When you disable the [MySQL/MariaDB role](https://go.cpanel.net/serverroles) **and** remote MySQL is **not** configured, the system **disables** this function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200344 import InlineResponse200344
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
    api_instance = clientapi_cpanel.DatabaseManagementApi(api_client)
    dbname = 'username_example_db' # str | The database's name.

    try:
        # Return MySQL database schema
        api_response = api_instance.dump_database_schema(dbname)
        print("The response of DatabaseManagementApi->dump_database_schema:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatabaseManagementApi->dump_database_schema: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dbname** | **str**| The database&#39;s name. | 

### Return type

[**InlineResponse200344**](InlineResponse200344.md)

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

# **list_databases**
> InlineResponse200349 list_databases()

Return MySQL databases

This function lists an account's MySQL® databases.

**Important:**

When you disable the [*MySQL/MariaDB* role](https://go.cpanel.net/serverroles) **and** remote MySQL is **not** configured, the system **disables** this function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200349 import InlineResponse200349
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
    api_instance = clientapi_cpanel.DatabaseManagementApi(api_client)

    try:
        # Return MySQL databases
        api_response = api_instance.list_databases()
        print("The response of DatabaseManagementApi->list_databases:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatabaseManagementApi->list_databases: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**InlineResponse200349**](InlineResponse200349.md)

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

# **mysql_check_database**
> InlineResponse200338 mysql_check_database(name)

Validate MySQL database integrity

This function checks for errors in all of the tables in a MySQL® database.

**Important:**

When you disable the [MySQL role](https://go.cpanel.net/serverroles) **and**
remote MySQL is **not** already configured, the system **disables** this function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200338 import InlineResponse200338
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
    api_instance = clientapi_cpanel.DatabaseManagementApi(api_client)
    name = 'example_test' # str | The database's name.

    try:
        # Validate MySQL database integrity
        api_response = api_instance.mysql_check_database(name)
        print("The response of DatabaseManagementApi->mysql_check_database:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatabaseManagementApi->mysql_check_database: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The database&#39;s name. | 

### Return type

[**InlineResponse200338**](InlineResponse200338.md)

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

# **mysql_rename_database**
> InlineResponse200353 mysql_rename_database(newname, oldname)

Update MySQL database name

This function renames a MySQL® database.

MySQL does not allow you to rename a database. When cPanel & WHM "renames" a database, the
system performs the following steps:
1. The system creates a new database.
2. The system moves data from the old database to the new database.
3. The system recreates grants and stored code in the new database.
4. The system deletes the old database and its grants.

**Warning:**

* It is potentially dangerous to rename a MySQL database. We **strongly** recommend that you
perform a backup of the database before you attempt to rename it.
* If any of the first three steps fail, the system returns an error and attempts to restore the database's original state.
 If the restoration process fails, the API function's error response describes these additional failures.
* In rare cases, the system creates the second database successfully, but fails to delete the old database or grants.
 The system treats the rename action as a success; however,
 the API function returns warnings that describe the failure to delete the old database or grants.

**Important:**

When you disable the [MySQL/MariaDB role](https://go.cpanel.net/serverroles)
**and** remote MySQL is **not** already configured, the system **disables** this function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200353 import InlineResponse200353
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
    api_instance = clientapi_cpanel.DatabaseManagementApi(api_client)
    newname = 'newlyrenamed' # str | The database's new name.  **Important:**  * If database prefixing is enabled, you **must** prefix this value with the account prefix and an underscore (`_`). For example, for the `dbuser` database on the user cPanel account, pass in a value of `user_dbuser`. * The maximum length of the database name is 64 characters. However, due to the method that cPanel & WHM uses to store MySQL database names, each underscore character requires two characters of that limit. Therefore, if you enable database prefixing, the maximum length of the database name is 63 characters, which includes both the database prefix and the underscore character. Each additional underscore requires another two characters of that limit.
    oldname = 'mydb' # str | The database's current name.

    try:
        # Update MySQL database name
        api_response = api_instance.mysql_rename_database(newname, oldname)
        print("The response of DatabaseManagementApi->mysql_rename_database:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatabaseManagementApi->mysql_rename_database: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **newname** | **str**| The database&#39;s new name.  **Important:**  * If database prefixing is enabled, you **must** prefix this value with the account prefix and an underscore (&#x60;_&#x60;). For example, for the &#x60;dbuser&#x60; database on the user cPanel account, pass in a value of &#x60;user_dbuser&#x60;. * The maximum length of the database name is 64 characters. However, due to the method that cPanel &amp; WHM uses to store MySQL database names, each underscore character requires two characters of that limit. Therefore, if you enable database prefixing, the maximum length of the database name is 63 characters, which includes both the database prefix and the underscore character. Each additional underscore requires another two characters of that limit. | 
 **oldname** | **str**| The database&#39;s current name. | 

### Return type

[**InlineResponse200353**](InlineResponse200353.md)

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

# **mysql_update_privileges**
> InlineResponse200360 mysql_update_privileges()

Update MySQL® privileges

This function updates privileges for all MySQL® databases and users on an account.

**Important:**

When you disable the [MySQL/MariaDB role](https://go.cpanel.net/serverroles) **and**
remote MySQL is **not** configured, the system **disables** this function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200360 import InlineResponse200360
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
    api_instance = clientapi_cpanel.DatabaseManagementApi(api_client)

    try:
        # Update MySQL® privileges
        api_response = api_instance.mysql_update_privileges()
        print("The response of DatabaseManagementApi->mysql_update_privileges:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatabaseManagementApi->mysql_update_privileges: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**InlineResponse200360**](InlineResponse200360.md)

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

# **repair_database**
> InlineResponse200355 repair_database(name)

Repair MySQL database tables

This function repairs all of the tables in a MySQL® database.

**Important:**

When you disable the [MySQL/MariaDB role](https://go.cpanel.net/serverroles)
**and** remote MySQL is **not** already configured, the system **disables** this function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200355 import InlineResponse200355
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
    api_instance = clientapi_cpanel.DatabaseManagementApi(api_client)
    name = 'example_db' # str | The database's name.

    try:
        # Repair MySQL database tables
        api_response = api_instance.repair_database(name)
        print("The response of DatabaseManagementApi->repair_database:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatabaseManagementApi->repair_database: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The database&#39;s name. | 

### Return type

[**InlineResponse200355**](InlineResponse200355.md)

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

# **setup_db_and_user**
> InlineResponse200359 setup_db_and_user(prefix=prefix)

Create a randomly named MySQL username/database set.

This function creates a randomly named MySQL® database and user. This allows a 3rdparty tool to create its own DB without needing any knowledge of cPanel internals such as quotas or other limits. These will simply be passed back as an error.

**Important:**

  When you disable the [MySQL/MariaDB role](https://go.cpanel.net/howtouseserverprofiles#roles) **and** remote MySQL is **not** already configured, the system **disables** this function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200359 import InlineResponse200359
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
    api_instance = clientapi_cpanel.DatabaseManagementApi(api_client)
    prefix = 'wp' # str | An optional string to prepend to the randomly generated database name. This is in addition to the cPanel user which will appear prior to this. The prefix should be 6 characters or less and be only alphanumeric characters. WARNING: longer prexies lead to less entropy in the random username. Keep it short if you can! (optional)

    try:
        # Create a randomly named MySQL username/database set.
        api_response = api_instance.setup_db_and_user(prefix=prefix)
        print("The response of DatabaseManagementApi->setup_db_and_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatabaseManagementApi->setup_db_and_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **prefix** | **str**| An optional string to prepend to the randomly generated database name. This is in addition to the cPanel user which will appear prior to this. The prefix should be 6 characters or less and be only alphanumeric characters. WARNING: longer prexies lead to less entropy in the random username. Keep it short if you can! | [optional] 

### Return type

[**InlineResponse200359**](InlineResponse200359.md)

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

