# clientapi_cpanel.MysqlApi

All URIs are relative to *https://cpanel-server.tld:2083/execute*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_host**](MysqlApi.md#add_host) | **GET** /Mysql/add_host | Enable remote MySQL host access
[**create_database**](MysqlApi.md#create_database) | **GET** /Mysql/create_database | Create MySQL database
[**delete_database**](MysqlApi.md#delete_database) | **GET** /Mysql/delete_database | Delete MySQL database
[**delete_host**](MysqlApi.md#delete_host) | **GET** /Mysql/delete_host | Disable remote MySQL host access
[**dump_database_schema**](MysqlApi.md#dump_database_schema) | **GET** /Mysql/dump_database_schema | Return MySQL database schema
[**get_host_notes**](MysqlApi.md#get_host_notes) | **GET** /Mysql/get_host_notes | Return remote MySQL host notes
[**get_restrictions**](MysqlApi.md#get_restrictions) | **GET** /Mysql/get_restrictions | Return MySQL name length restrictions
[**get_server_information**](MysqlApi.md#get_server_information) | **GET** /Mysql/get_server_information | Return MySQL server host information and version
[**list_databases**](MysqlApi.md#list_databases) | **GET** /Mysql/list_databases | Return MySQL databases
[**list_routines**](MysqlApi.md#list_routines) | **GET** /Mysql/list_routines | Return MySQL user routines
[**locate_server**](MysqlApi.md#locate_server) | **GET** /Mysql/locate_server | Return MySQL server host information
[**mysql_add_host_note**](MysqlApi.md#mysql_add_host_note) | **GET** /Mysql/add_host_note | Add remote MySQL host note
[**mysql_check_database**](MysqlApi.md#mysql_check_database) | **GET** /Mysql/check_database | Validate MySQL database integrity
[**mysql_create_user**](MysqlApi.md#mysql_create_user) | **GET** /Mysql/create_user | Create MySQL user
[**mysql_delete_user**](MysqlApi.md#mysql_delete_user) | **GET** /Mysql/delete_user | Delete MySQL user
[**mysql_get_privileges_on_database**](MysqlApi.md#mysql_get_privileges_on_database) | **GET** /Mysql/get_privileges_on_database | Return MySQL user privileges
[**mysql_list_users**](MysqlApi.md#mysql_list_users) | **GET** /Mysql/list_users | Return MySQL users
[**mysql_rename_database**](MysqlApi.md#mysql_rename_database) | **GET** /Mysql/rename_database | Update MySQL database name
[**mysql_set_password**](MysqlApi.md#mysql_set_password) | **GET** /Mysql/set_password | Update MySQL user password
[**mysql_update_privileges**](MysqlApi.md#mysql_update_privileges) | **GET** /Mysql/update_privileges | Update MySQL® privileges
[**rename_user**](MysqlApi.md#rename_user) | **GET** /Mysql/rename_user | Update MySQL username
[**repair_database**](MysqlApi.md#repair_database) | **GET** /Mysql/repair_database | Repair MySQL database tables
[**revoke_access_to_database**](MysqlApi.md#revoke_access_to_database) | **GET** /Mysql/revoke_access_to_database | Remove MySQL user privileges
[**set_privileges_on_database**](MysqlApi.md#set_privileges_on_database) | **GET** /Mysql/set_privileges_on_database | Update MySQL user privileges
[**setup_db_and_user**](MysqlApi.md#setup_db_and_user) | **GET** /Mysql/setup_db_and_user | Create a randomly named MySQL username/database set.


# **add_host**
> InlineResponse200336 add_host(host)

Enable remote MySQL host access

This function authorizes a remote MySQL® host to access the account's databases.

**Important:**

When you disable the [MySQL role](https://go.cpanel.net/serverroles)
 and remote MySQL is **not** already configured,
 the system **disables** this function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200336 import InlineResponse200336
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
    api_instance = clientapi_cpanel.MysqlApi(api_client)
    host = clientapi_cpanel.Host3() # Host3 | The remote MySQL server's hostname or IP address.  You may use the following IP address formats:  * `192.168.1.6` — IP address. * `192.168.%.%` — Range with the percent (%) symbol as a wildcard. * `192.168.0.0/16` — Range in CIDR format.

    try:
        # Enable remote MySQL host access
        api_response = api_instance.add_host(host)
        print("The response of MysqlApi->add_host:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MysqlApi->add_host: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **host** | [**Host3**](.md)| The remote MySQL server&#39;s hostname or IP address.  You may use the following IP address formats:  * &#x60;192.168.1.6&#x60; — IP address. * &#x60;192.168.%.%&#x60; — Range with the percent (%) symbol as a wildcard. * &#x60;192.168.0.0/16&#x60; — Range in CIDR format. | 

### Return type

[**InlineResponse200336**](InlineResponse200336.md)

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
    api_instance = clientapi_cpanel.MysqlApi(api_client)
    name = 'newdb' # str | The new database's name.
    prefix_size = 16 # int | The desired prefix size. (optional) (default to 16)

    try:
        # Create MySQL database
        api_response = api_instance.create_database(name, prefix_size=prefix_size)
        print("The response of MysqlApi->create_database:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MysqlApi->create_database: %s\n" % e)
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
    api_instance = clientapi_cpanel.MysqlApi(api_client)
    name = 'example' # str | The database's name.

    try:
        # Delete MySQL database
        api_response = api_instance.delete_database(name)
        print("The response of MysqlApi->delete_database:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MysqlApi->delete_database: %s\n" % e)
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

# **delete_host**
> InlineResponse200342 delete_host(host)

Disable remote MySQL host access

This function removes a remote MySQL® host's access to the account's databases.

**Important:**

When you disable the [MySQL role](https://go.cpanel.net/serverroles) and remote MySQL is not already configured, the system **disables** this function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200342 import InlineResponse200342
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
    api_instance = clientapi_cpanel.MysqlApi(api_client)
    host = 'remote.example.com' # str | The remote MySQL server's hostname, IP Address, or IP address range.  **Note:** You may use the following IP address formats:  192.168.1.6 — IP address. 192.168.%.% — Range with the percent (%) symbol as a wildcard. 192.168.0.0/16 — Range in CIDR format.

    try:
        # Disable remote MySQL host access
        api_response = api_instance.delete_host(host)
        print("The response of MysqlApi->delete_host:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MysqlApi->delete_host: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **host** | **str**| The remote MySQL server&#39;s hostname, IP Address, or IP address range.  **Note:** You may use the following IP address formats:  192.168.1.6 — IP address. 192.168.%.% — Range with the percent (%) symbol as a wildcard. 192.168.0.0/16 — Range in CIDR format. | 

### Return type

[**InlineResponse200342**](InlineResponse200342.md)

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
    api_instance = clientapi_cpanel.MysqlApi(api_client)
    dbname = 'username_example_db' # str | The database's name.

    try:
        # Return MySQL database schema
        api_response = api_instance.dump_database_schema(dbname)
        print("The response of MysqlApi->dump_database_schema:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MysqlApi->dump_database_schema: %s\n" % e)
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

# **get_host_notes**
> InlineResponse200345 get_host_notes()

Return remote MySQL host notes

This function returns the notes associated with the account's remote MySQL® hosts.

**Important:**

  When you disable the [*MySQL/MariaDB* role](https://go.cpanel.net/serverroles)
  **and** remote MySQL is **not** already configured, the system **disables** this function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200345 import InlineResponse200345
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
    api_instance = clientapi_cpanel.MysqlApi(api_client)

    try:
        # Return remote MySQL host notes
        api_response = api_instance.get_host_notes()
        print("The response of MysqlApi->get_host_notes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MysqlApi->get_host_notes: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**InlineResponse200345**](InlineResponse200345.md)

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

# **get_restrictions**
> InlineResponse200347 get_restrictions()

Return MySQL name length restrictions

This function lists a MySQL® database's name, username length restrictions, and database prefix.

**Important:**

  When you disable the [*MySQL/MariaDB* role](https://go.cpanel.net/serverroles)
  **and** remote MySQL is **not** already configured, the system **disables** this function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200347 import InlineResponse200347
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
    api_instance = clientapi_cpanel.MysqlApi(api_client)

    try:
        # Return MySQL name length restrictions
        api_response = api_instance.get_restrictions()
        print("The response of MysqlApi->get_restrictions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MysqlApi->get_restrictions: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**InlineResponse200347**](InlineResponse200347.md)

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

# **get_server_information**
> InlineResponse200348 get_server_information()

Return MySQL server host information and version

This function returns information about the account's MySQL® host.

**Important:**

  When you disable the [MySQL role](https://go.cpanel.net/serverroles) **and** remote MySQL is **not** already configured, the system **disables** this function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200348 import InlineResponse200348
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
    api_instance = clientapi_cpanel.MysqlApi(api_client)

    try:
        # Return MySQL server host information and version
        api_response = api_instance.get_server_information()
        print("The response of MysqlApi->get_server_information:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MysqlApi->get_server_information: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**InlineResponse200348**](InlineResponse200348.md)

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
    api_instance = clientapi_cpanel.MysqlApi(api_client)

    try:
        # Return MySQL databases
        api_response = api_instance.list_databases()
        print("The response of MysqlApi->list_databases:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MysqlApi->list_databases: %s\n" % e)
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

# **list_routines**
> InlineResponse200350 list_routines(database_user=database_user)

Return MySQL user routines

This function returns a database user's MySQL® routines.

**Important:**

  When you disable the [MySQL/MariaDB role](https://go.cpanel.net/serverroles) **and**
  remote MySQL is **not** configured, the system **disables** this function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200350 import InlineResponse200350
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
    api_instance = clientapi_cpanel.MysqlApi(api_client)
    database_user = 'db_user' # str | The database user for whom to return MySQL routines. If you don't specify a database user, this function returns the MySQL routines for all database users. (optional)

    try:
        # Return MySQL user routines
        api_response = api_instance.list_routines(database_user=database_user)
        print("The response of MysqlApi->list_routines:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MysqlApi->list_routines: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **database_user** | **str**| The database user for whom to return MySQL routines. If you don&#39;t specify a database user, this function returns the MySQL routines for all database users. | [optional] 

### Return type

[**InlineResponse200350**](InlineResponse200350.md)

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

# **locate_server**
> InlineResponse200352 locate_server()

Return MySQL server host information

This function returns information about the account's MySQL® host.

**Important:**

When you disable the [MySQL/MariaDB role](https://go.cpanel.net/serverroles#roles) **and** remote MySQL is **not** already configured, the system **disables** this function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200352 import InlineResponse200352
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
    api_instance = clientapi_cpanel.MysqlApi(api_client)

    try:
        # Return MySQL server host information
        api_response = api_instance.locate_server()
        print("The response of MysqlApi->locate_server:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MysqlApi->locate_server: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**InlineResponse200352**](InlineResponse200352.md)

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

# **mysql_add_host_note**
> InlineResponse200337 mysql_add_host_note(host, note)

Add remote MySQL host note

This function adds a note about a remote MySQL® server.

**Important:**

* If you attempt to add a note to an unauthorized remote MySQL server, the function will fail.
* When you **disable** the [MySQL role](https://go.cpanel.net/serverroles), the system disables this function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200337 import InlineResponse200337
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
    api_instance = clientapi_cpanel.MysqlApi(api_client)
    host = clientapi_cpanel.Host4() # Host4 | The remote MySQL server's hostname or IP address.  You may use the following IP address formats:  * `192.168.1.6` — IP address. * `192.168.%.%` — Range with the percent (%) symbol as a wildcard. * `192.168.0.0/16` — Range in CIDR format.
    note = 'A remote mysql server for storing my data' # str | note that describes the remote MySQL server.

    try:
        # Add remote MySQL host note
        api_response = api_instance.mysql_add_host_note(host, note)
        print("The response of MysqlApi->mysql_add_host_note:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MysqlApi->mysql_add_host_note: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **host** | [**Host4**](.md)| The remote MySQL server&#39;s hostname or IP address.  You may use the following IP address formats:  * &#x60;192.168.1.6&#x60; — IP address. * &#x60;192.168.%.%&#x60; — Range with the percent (%) symbol as a wildcard. * &#x60;192.168.0.0/16&#x60; — Range in CIDR format. | 
 **note** | **str**| note that describes the remote MySQL server. | 

### Return type

[**InlineResponse200337**](InlineResponse200337.md)

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
    api_instance = clientapi_cpanel.MysqlApi(api_client)
    name = 'example_test' # str | The database's name.

    try:
        # Validate MySQL database integrity
        api_response = api_instance.mysql_check_database(name)
        print("The response of MysqlApi->mysql_check_database:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MysqlApi->mysql_check_database: %s\n" % e)
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

# **mysql_create_user**
> InlineResponse200340 mysql_create_user(name, password, prefix_size=prefix_size)

Create MySQL user

This function creates a MySQL® database user.

**Important:**

When you **disable** the [MySQL role](https://go.cpanel.net/serverroles) and remote MySQL is not already configured, the system disables this function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200340 import InlineResponse200340
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
    api_instance = clientapi_cpanel.MysqlApi(api_client)
    name = 'dbuser' # str | A valid database username.  Important: ====  To learn more about database username limits, check your database type:  MySQL 5.6 ----  MySQL version 5.6 limits the database username to 16 characters. The server uses the first nine characters of this limit for the database prefix. The database prefix uses the cPanel account's username and an underscore (`_`). The server only applies the first eight characters of the cPanel account's username.  For example:  * A `db_` database prefix allows MySQL usernames of up to 13 characters. * An `example_` database prefix allows MySQL usernames of up to eight characters.  MySQL 5.7+ ----  MySQL versions 5.7 and later limit the database username to 32 characters. The server uses the first nine characters of this limit for the database prefix. The database prefix uses the cPanel account's username and an underscore (`_`). The server only applies the first eight characters of the cPanel account's username.  For example:  * A `db_` database prefix allows MySQL usernames of up to 29 characters. * An `example_` database prefix allows MySQL usernames of up to 24 characters.  MariaDB ----  MariaDB limits the database username to 47 characters. The server uses the first nine characters of this limit for the database prefix. The database prefix uses the cPanel account's username and an underscore (`_`). The server only applies the first eight characters of the cPanel account's username.  For example:  * A `db_` database prefix allows MariaDB usernames of up to 44 characters. * An `example_` database prefix allows MariaDB usernames of up to 39 characters.
    password = '12345luggage' # str | The new user's password.
    prefix_size = 16 # int | The desired prefix size. (optional) (default to 16)

    try:
        # Create MySQL user
        api_response = api_instance.mysql_create_user(name, password, prefix_size=prefix_size)
        print("The response of MysqlApi->mysql_create_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MysqlApi->mysql_create_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| A valid database username.  Important: &#x3D;&#x3D;&#x3D;&#x3D;  To learn more about database username limits, check your database type:  MySQL 5.6 ----  MySQL version 5.6 limits the database username to 16 characters. The server uses the first nine characters of this limit for the database prefix. The database prefix uses the cPanel account&#39;s username and an underscore (&#x60;_&#x60;). The server only applies the first eight characters of the cPanel account&#39;s username.  For example:  * A &#x60;db_&#x60; database prefix allows MySQL usernames of up to 13 characters. * An &#x60;example_&#x60; database prefix allows MySQL usernames of up to eight characters.  MySQL 5.7+ ----  MySQL versions 5.7 and later limit the database username to 32 characters. The server uses the first nine characters of this limit for the database prefix. The database prefix uses the cPanel account&#39;s username and an underscore (&#x60;_&#x60;). The server only applies the first eight characters of the cPanel account&#39;s username.  For example:  * A &#x60;db_&#x60; database prefix allows MySQL usernames of up to 29 characters. * An &#x60;example_&#x60; database prefix allows MySQL usernames of up to 24 characters.  MariaDB ----  MariaDB limits the database username to 47 characters. The server uses the first nine characters of this limit for the database prefix. The database prefix uses the cPanel account&#39;s username and an underscore (&#x60;_&#x60;). The server only applies the first eight characters of the cPanel account&#39;s username.  For example:  * A &#x60;db_&#x60; database prefix allows MariaDB usernames of up to 44 characters. * An &#x60;example_&#x60; database prefix allows MariaDB usernames of up to 39 characters. | 
 **password** | **str**| The new user&#39;s password. | 
 **prefix_size** | **int**| The desired prefix size. | [optional] [default to 16]

### Return type

[**InlineResponse200340**](InlineResponse200340.md)

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

# **mysql_delete_user**
> InlineResponse200343 mysql_delete_user(name)

Delete MySQL user

This function deletes a MySQL® user.

**Important:**

When you disable the [MySQL role](https://go.cpanel.net/serverroles) and remote MySQL is not already configured, the system **disables** this function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200343 import InlineResponse200343
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
    api_instance = clientapi_cpanel.MysqlApi(api_client)
    name = 'example' # str | The MySQL user's name.

    try:
        # Delete MySQL user
        api_response = api_instance.mysql_delete_user(name)
        print("The response of MysqlApi->mysql_delete_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MysqlApi->mysql_delete_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The MySQL user&#39;s name. | 

### Return type

[**InlineResponse200343**](InlineResponse200343.md)

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

# **mysql_get_privileges_on_database**
> InlineResponse200346 mysql_get_privileges_on_database(database, user)

Return MySQL user privileges

This function lists a MySQL® database user's privileges.

**Important:**

When you disable the [MySQL role](https://go.cpanel.net/serverroles)
and remote MySQL is not already configured, the system disables this function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200346 import InlineResponse200346
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
    api_instance = clientapi_cpanel.MysqlApi(api_client)
    database = 'mydb' # str | The database name.
    user = 'dbuser' # str | The database user's name.  **Important:**  If database prefixing is enabled, you **must** prefix this value with the account prefix and an underscore (`_`).  For example, for the `dbuser` user on the `user` cPanel account, pass in a value of `user_dbuser`.

    try:
        # Return MySQL user privileges
        api_response = api_instance.mysql_get_privileges_on_database(database, user)
        print("The response of MysqlApi->mysql_get_privileges_on_database:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MysqlApi->mysql_get_privileges_on_database: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **database** | **str**| The database name. | 
 **user** | **str**| The database user&#39;s name.  **Important:**  If database prefixing is enabled, you **must** prefix this value with the account prefix and an underscore (&#x60;_&#x60;).  For example, for the &#x60;dbuser&#x60; user on the &#x60;user&#x60; cPanel account, pass in a value of &#x60;user_dbuser&#x60;. | 

### Return type

[**InlineResponse200346**](InlineResponse200346.md)

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

# **mysql_list_users**
> InlineResponse200351 mysql_list_users()

Return MySQL users

This function lists an account's MySQL® database users.

**Important:**

  When you disable the [MySQL/MariaDB role](https://go.cpanel.net/serverroles) **and**
  remote MySQL is **not** configured, the system **disables** this function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200351 import InlineResponse200351
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
    api_instance = clientapi_cpanel.MysqlApi(api_client)

    try:
        # Return MySQL users
        api_response = api_instance.mysql_list_users()
        print("The response of MysqlApi->mysql_list_users:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MysqlApi->mysql_list_users: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**InlineResponse200351**](InlineResponse200351.md)

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
    api_instance = clientapi_cpanel.MysqlApi(api_client)
    newname = 'newlyrenamed' # str | The database's new name.  **Important:**  * If database prefixing is enabled, you **must** prefix this value with the account prefix and an underscore (`_`). For example, for the `dbuser` database on the user cPanel account, pass in a value of `user_dbuser`. * The maximum length of the database name is 64 characters. However, due to the method that cPanel & WHM uses to store MySQL database names, each underscore character requires two characters of that limit. Therefore, if you enable database prefixing, the maximum length of the database name is 63 characters, which includes both the database prefix and the underscore character. Each additional underscore requires another two characters of that limit.
    oldname = 'mydb' # str | The database's current name.

    try:
        # Update MySQL database name
        api_response = api_instance.mysql_rename_database(newname, oldname)
        print("The response of MysqlApi->mysql_rename_database:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MysqlApi->mysql_rename_database: %s\n" % e)
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

# **mysql_set_password**
> InlineResponse200357 mysql_set_password(password, user)

Update MySQL user password

This function sets a MySQL® database user's password.

**Important:**

When you disable the [MySQL role](https://go.cpanel.net/serverroles)
 and remote MySQL is **not** already configured,
 the system **disables** this function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200357 import InlineResponse200357
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
    api_instance = clientapi_cpanel.MysqlApi(api_client)
    password = '12345luggage' # str | The user's new password.
    user = 'dbuser' # str | The MySQL database user.

    try:
        # Update MySQL user password
        api_response = api_instance.mysql_set_password(password, user)
        print("The response of MysqlApi->mysql_set_password:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MysqlApi->mysql_set_password: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **password** | **str**| The user&#39;s new password. | 
 **user** | **str**| The MySQL database user. | 

### Return type

[**InlineResponse200357**](InlineResponse200357.md)

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
    api_instance = clientapi_cpanel.MysqlApi(api_client)

    try:
        # Update MySQL® privileges
        api_response = api_instance.mysql_update_privileges()
        print("The response of MysqlApi->mysql_update_privileges:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MysqlApi->mysql_update_privileges: %s\n" % e)
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

# **rename_user**
> InlineResponse200354 rename_user(newname, oldname)

Update MySQL username

This function renames a MySQL® database user.

**Important:**

When you disable the [MySQL role](https://go.cpanel.net/serverroles)
 and remote MySQL is **not** already configured,
 the system **disables** this function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200354 import InlineResponse200354
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
    api_instance = clientapi_cpanel.MysqlApi(api_client)
    newname = 'mynewusername' # str | The user's new name.  Important: ====  To learn more about database username limits, check your database type:  MySQL 5.6 ----  MySQL version 5.6 limits the database username to 16 characters. The server uses the first nine characters of this limit for the database prefix. The database prefix uses the cPanel account's username and an underscore (`_`). The server only applies the first eight characters of the cPanel account's username.  For example:  * A `db_` database prefix allows MySQL usernames of up to 13 characters. * An `example_` database prefix allows MySQL usernames of up to eight characters.  MySQL 5.7+ ----  MySQL versions 5.7 and later limit the database username to 32 characters. The server uses the first nine characters of this limit for the database prefix. The database prefix uses the cPanel account's username and an underscore (`_`). The server only applies the first eight characters of the cPanel account's username.  For example:  * A `db_` database prefix allows MySQL usernames of up to 29 characters. * An `example_` database prefix allows MySQL usernames of up to 24 characters.  MariaDB ----  MariaDB limits the database username to 47 characters. The server uses the first nine characters of this limit for the database prefix. The database prefix uses the cPanel account's username and an underscore (`_`). The server only applies the first eight characters of the cPanel account's username.  For example:  * A `db_` database prefix allows MariaDB usernames of up to 44 characters. * An `example_` database prefix allows MariaDB usernames of up to 39 characters.
    oldname = 'dbuser' # str | The user's current name.

    try:
        # Update MySQL username
        api_response = api_instance.rename_user(newname, oldname)
        print("The response of MysqlApi->rename_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MysqlApi->rename_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **newname** | **str**| The user&#39;s new name.  Important: &#x3D;&#x3D;&#x3D;&#x3D;  To learn more about database username limits, check your database type:  MySQL 5.6 ----  MySQL version 5.6 limits the database username to 16 characters. The server uses the first nine characters of this limit for the database prefix. The database prefix uses the cPanel account&#39;s username and an underscore (&#x60;_&#x60;). The server only applies the first eight characters of the cPanel account&#39;s username.  For example:  * A &#x60;db_&#x60; database prefix allows MySQL usernames of up to 13 characters. * An &#x60;example_&#x60; database prefix allows MySQL usernames of up to eight characters.  MySQL 5.7+ ----  MySQL versions 5.7 and later limit the database username to 32 characters. The server uses the first nine characters of this limit for the database prefix. The database prefix uses the cPanel account&#39;s username and an underscore (&#x60;_&#x60;). The server only applies the first eight characters of the cPanel account&#39;s username.  For example:  * A &#x60;db_&#x60; database prefix allows MySQL usernames of up to 29 characters. * An &#x60;example_&#x60; database prefix allows MySQL usernames of up to 24 characters.  MariaDB ----  MariaDB limits the database username to 47 characters. The server uses the first nine characters of this limit for the database prefix. The database prefix uses the cPanel account&#39;s username and an underscore (&#x60;_&#x60;). The server only applies the first eight characters of the cPanel account&#39;s username.  For example:  * A &#x60;db_&#x60; database prefix allows MariaDB usernames of up to 44 characters. * An &#x60;example_&#x60; database prefix allows MariaDB usernames of up to 39 characters. | 
 **oldname** | **str**| The user&#39;s current name. | 

### Return type

[**InlineResponse200354**](InlineResponse200354.md)

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
    api_instance = clientapi_cpanel.MysqlApi(api_client)
    name = 'example_db' # str | The database's name.

    try:
        # Repair MySQL database tables
        api_response = api_instance.repair_database(name)
        print("The response of MysqlApi->repair_database:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MysqlApi->repair_database: %s\n" % e)
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

# **revoke_access_to_database**
> InlineResponse200356 revoke_access_to_database(database, user)

Remove MySQL user privileges

This function revokes a MySQL® database user's privileges.

**Important:**

When you disable the [MySQL role](https://go.cpanel.net/serverroles) **and**
remote MySQL is **not** already configured, the system **disables** this function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200356 import InlineResponse200356
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
    api_instance = clientapi_cpanel.MysqlApi(api_client)
    database = 'mydb' # str | The database's name.
    user = 'dbuser' # str | The database user's name.  **Important:**  If database prefixing is enabled, you **must** prefix this value with the account prefix and an underscore (`_`).  For example, for the `dbuser` user on the `user` cPanel account, pass in a value of `user_dbuser`. 

    try:
        # Remove MySQL user privileges
        api_response = api_instance.revoke_access_to_database(database, user)
        print("The response of MysqlApi->revoke_access_to_database:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MysqlApi->revoke_access_to_database: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **database** | **str**| The database&#39;s name. | 
 **user** | **str**| The database user&#39;s name.  **Important:**  If database prefixing is enabled, you **must** prefix this value with the account prefix and an underscore (&#x60;_&#x60;).  For example, for the &#x60;dbuser&#x60; user on the &#x60;user&#x60; cPanel account, pass in a value of &#x60;user_dbuser&#x60;.  | 

### Return type

[**InlineResponse200356**](InlineResponse200356.md)

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

# **set_privileges_on_database**
> InlineResponse200358 set_privileges_on_database(database, user, privileges=privileges)

Update MySQL user privileges

This function sets a MySQL® database user's privileges.

**Important:**

When you disable the [*MySQL/MariaDB* role](https://go.cpanel.net/serverroles), **and** remote MySQL is **not** already configured, the system **disables** this function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200358 import InlineResponse200358
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
    api_instance = clientapi_cpanel.MysqlApi(api_client)
    database = 'cpuser_dbname' # str | The database's name.  **Important:**  If database prefixing is enabled, you **must** prefix this value with the account prefix and an underscore (`_`). For example, for the `db` database on the `user` cPanel account, pass in a value of `user_db`.
    user = 'cpuser_dbuser' # str | The database user's name.  **Important:**  If database prefixing is enabled, you **must** prefix this value with the account prefix and an underscore (`_`). For example, for the `dbuser` user on the `user` cPanel account, pass in a value of `user_dbuser`.
    privileges = 'DELETE,UPDATE,CREATE,ALTER' # str | * `ALL PRIVILEGES` * A comma-separated list of one or more of the following individual privileges:   * `ALTER`   * `ALTER ROUTINE`   * `CREATE`   * `CREATE ROUTINE`   * `CREATE TEMPORARY TABLES`   * `CREATE VIEW`   * `DELETE`   * `DROP`   * `EVENT`   * `EXECUTE`   * `INDEX`   * `INSERT`   * `LOCK TABLES`   * `REFERENCES`   * `SELECT`   * `SHOW VIEW`   * `TRIGGER`   * `UPDATE`  **Note:**  * This list replaces, rather than adds to, the existing privilege list. * In browser-based and command line calls, separate multiple values with `%2C` and replace spaces with `%20`. (optional)

    try:
        # Update MySQL user privileges
        api_response = api_instance.set_privileges_on_database(database, user, privileges=privileges)
        print("The response of MysqlApi->set_privileges_on_database:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MysqlApi->set_privileges_on_database: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **database** | **str**| The database&#39;s name.  **Important:**  If database prefixing is enabled, you **must** prefix this value with the account prefix and an underscore (&#x60;_&#x60;). For example, for the &#x60;db&#x60; database on the &#x60;user&#x60; cPanel account, pass in a value of &#x60;user_db&#x60;. | 
 **user** | **str**| The database user&#39;s name.  **Important:**  If database prefixing is enabled, you **must** prefix this value with the account prefix and an underscore (&#x60;_&#x60;). For example, for the &#x60;dbuser&#x60; user on the &#x60;user&#x60; cPanel account, pass in a value of &#x60;user_dbuser&#x60;. | 
 **privileges** | **str**| * &#x60;ALL PRIVILEGES&#x60; * A comma-separated list of one or more of the following individual privileges:   * &#x60;ALTER&#x60;   * &#x60;ALTER ROUTINE&#x60;   * &#x60;CREATE&#x60;   * &#x60;CREATE ROUTINE&#x60;   * &#x60;CREATE TEMPORARY TABLES&#x60;   * &#x60;CREATE VIEW&#x60;   * &#x60;DELETE&#x60;   * &#x60;DROP&#x60;   * &#x60;EVENT&#x60;   * &#x60;EXECUTE&#x60;   * &#x60;INDEX&#x60;   * &#x60;INSERT&#x60;   * &#x60;LOCK TABLES&#x60;   * &#x60;REFERENCES&#x60;   * &#x60;SELECT&#x60;   * &#x60;SHOW VIEW&#x60;   * &#x60;TRIGGER&#x60;   * &#x60;UPDATE&#x60;  **Note:**  * This list replaces, rather than adds to, the existing privilege list. * In browser-based and command line calls, separate multiple values with &#x60;%2C&#x60; and replace spaces with &#x60;%20&#x60;. | [optional] 

### Return type

[**InlineResponse200358**](InlineResponse200358.md)

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
    api_instance = clientapi_cpanel.MysqlApi(api_client)
    prefix = 'wp' # str | An optional string to prepend to the randomly generated database name. This is in addition to the cPanel user which will appear prior to this. The prefix should be 6 characters or less and be only alphanumeric characters. WARNING: longer prexies lead to less entropy in the random username. Keep it short if you can! (optional)

    try:
        # Create a randomly named MySQL username/database set.
        api_response = api_instance.setup_db_and_user(prefix=prefix)
        print("The response of MysqlApi->setup_db_and_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MysqlApi->setup_db_and_user: %s\n" % e)
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

