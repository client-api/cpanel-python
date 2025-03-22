# clientapi_cpanel.UserManagementApi

All URIs are relative to *https://cpanel-server.tld:2083/execute*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_restrictions**](UserManagementApi.md#get_restrictions) | **GET** /Mysql/get_restrictions | Return MySQL name length restrictions
[**list_routines**](UserManagementApi.md#list_routines) | **GET** /Mysql/list_routines | Return MySQL user routines
[**mysql_create_user**](UserManagementApi.md#mysql_create_user) | **GET** /Mysql/create_user | Create MySQL user
[**mysql_delete_user**](UserManagementApi.md#mysql_delete_user) | **GET** /Mysql/delete_user | Delete MySQL user
[**mysql_get_privileges_on_database**](UserManagementApi.md#mysql_get_privileges_on_database) | **GET** /Mysql/get_privileges_on_database | Return MySQL user privileges
[**mysql_list_users**](UserManagementApi.md#mysql_list_users) | **GET** /Mysql/list_users | Return MySQL users
[**mysql_set_password**](UserManagementApi.md#mysql_set_password) | **GET** /Mysql/set_password | Update MySQL user password
[**rename_user**](UserManagementApi.md#rename_user) | **GET** /Mysql/rename_user | Update MySQL username
[**revoke_access_to_database**](UserManagementApi.md#revoke_access_to_database) | **GET** /Mysql/revoke_access_to_database | Remove MySQL user privileges
[**set_privileges_on_database**](UserManagementApi.md#set_privileges_on_database) | **GET** /Mysql/set_privileges_on_database | Update MySQL user privileges


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
    api_instance = clientapi_cpanel.UserManagementApi(api_client)

    try:
        # Return MySQL name length restrictions
        api_response = api_instance.get_restrictions()
        print("The response of UserManagementApi->get_restrictions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserManagementApi->get_restrictions: %s\n" % e)
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
    api_instance = clientapi_cpanel.UserManagementApi(api_client)
    database_user = 'db_user' # str | The database user for whom to return MySQL routines. If you don't specify a database user, this function returns the MySQL routines for all database users. (optional)

    try:
        # Return MySQL user routines
        api_response = api_instance.list_routines(database_user=database_user)
        print("The response of UserManagementApi->list_routines:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserManagementApi->list_routines: %s\n" % e)
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
    api_instance = clientapi_cpanel.UserManagementApi(api_client)
    name = 'dbuser' # str | A valid database username.  Important: ====  To learn more about database username limits, check your database type:  MySQL 5.6 ----  MySQL version 5.6 limits the database username to 16 characters. The server uses the first nine characters of this limit for the database prefix. The database prefix uses the cPanel account's username and an underscore (`_`). The server only applies the first eight characters of the cPanel account's username.  For example:  * A `db_` database prefix allows MySQL usernames of up to 13 characters. * An `example_` database prefix allows MySQL usernames of up to eight characters.  MySQL 5.7+ ----  MySQL versions 5.7 and later limit the database username to 32 characters. The server uses the first nine characters of this limit for the database prefix. The database prefix uses the cPanel account's username and an underscore (`_`). The server only applies the first eight characters of the cPanel account's username.  For example:  * A `db_` database prefix allows MySQL usernames of up to 29 characters. * An `example_` database prefix allows MySQL usernames of up to 24 characters.  MariaDB ----  MariaDB limits the database username to 47 characters. The server uses the first nine characters of this limit for the database prefix. The database prefix uses the cPanel account's username and an underscore (`_`). The server only applies the first eight characters of the cPanel account's username.  For example:  * A `db_` database prefix allows MariaDB usernames of up to 44 characters. * An `example_` database prefix allows MariaDB usernames of up to 39 characters.
    password = '12345luggage' # str | The new user's password.
    prefix_size = 16 # int | The desired prefix size. (optional) (default to 16)

    try:
        # Create MySQL user
        api_response = api_instance.mysql_create_user(name, password, prefix_size=prefix_size)
        print("The response of UserManagementApi->mysql_create_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserManagementApi->mysql_create_user: %s\n" % e)
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
    api_instance = clientapi_cpanel.UserManagementApi(api_client)
    name = 'example' # str | The MySQL user's name.

    try:
        # Delete MySQL user
        api_response = api_instance.mysql_delete_user(name)
        print("The response of UserManagementApi->mysql_delete_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserManagementApi->mysql_delete_user: %s\n" % e)
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
    api_instance = clientapi_cpanel.UserManagementApi(api_client)
    database = 'mydb' # str | The database name.
    user = 'dbuser' # str | The database user's name.  **Important:**  If database prefixing is enabled, you **must** prefix this value with the account prefix and an underscore (`_`).  For example, for the `dbuser` user on the `user` cPanel account, pass in a value of `user_dbuser`.

    try:
        # Return MySQL user privileges
        api_response = api_instance.mysql_get_privileges_on_database(database, user)
        print("The response of UserManagementApi->mysql_get_privileges_on_database:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserManagementApi->mysql_get_privileges_on_database: %s\n" % e)
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
    api_instance = clientapi_cpanel.UserManagementApi(api_client)

    try:
        # Return MySQL users
        api_response = api_instance.mysql_list_users()
        print("The response of UserManagementApi->mysql_list_users:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserManagementApi->mysql_list_users: %s\n" % e)
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
    api_instance = clientapi_cpanel.UserManagementApi(api_client)
    password = '12345luggage' # str | The user's new password.
    user = 'dbuser' # str | The MySQL database user.

    try:
        # Update MySQL user password
        api_response = api_instance.mysql_set_password(password, user)
        print("The response of UserManagementApi->mysql_set_password:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserManagementApi->mysql_set_password: %s\n" % e)
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
    api_instance = clientapi_cpanel.UserManagementApi(api_client)
    newname = 'mynewusername' # str | The user's new name.  Important: ====  To learn more about database username limits, check your database type:  MySQL 5.6 ----  MySQL version 5.6 limits the database username to 16 characters. The server uses the first nine characters of this limit for the database prefix. The database prefix uses the cPanel account's username and an underscore (`_`). The server only applies the first eight characters of the cPanel account's username.  For example:  * A `db_` database prefix allows MySQL usernames of up to 13 characters. * An `example_` database prefix allows MySQL usernames of up to eight characters.  MySQL 5.7+ ----  MySQL versions 5.7 and later limit the database username to 32 characters. The server uses the first nine characters of this limit for the database prefix. The database prefix uses the cPanel account's username and an underscore (`_`). The server only applies the first eight characters of the cPanel account's username.  For example:  * A `db_` database prefix allows MySQL usernames of up to 29 characters. * An `example_` database prefix allows MySQL usernames of up to 24 characters.  MariaDB ----  MariaDB limits the database username to 47 characters. The server uses the first nine characters of this limit for the database prefix. The database prefix uses the cPanel account's username and an underscore (`_`). The server only applies the first eight characters of the cPanel account's username.  For example:  * A `db_` database prefix allows MariaDB usernames of up to 44 characters. * An `example_` database prefix allows MariaDB usernames of up to 39 characters.
    oldname = 'dbuser' # str | The user's current name.

    try:
        # Update MySQL username
        api_response = api_instance.rename_user(newname, oldname)
        print("The response of UserManagementApi->rename_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserManagementApi->rename_user: %s\n" % e)
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
    api_instance = clientapi_cpanel.UserManagementApi(api_client)
    database = 'mydb' # str | The database's name.
    user = 'dbuser' # str | The database user's name.  **Important:**  If database prefixing is enabled, you **must** prefix this value with the account prefix and an underscore (`_`).  For example, for the `dbuser` user on the `user` cPanel account, pass in a value of `user_dbuser`. 

    try:
        # Remove MySQL user privileges
        api_response = api_instance.revoke_access_to_database(database, user)
        print("The response of UserManagementApi->revoke_access_to_database:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserManagementApi->revoke_access_to_database: %s\n" % e)
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
    api_instance = clientapi_cpanel.UserManagementApi(api_client)
    database = 'cpuser_dbname' # str | The database's name.  **Important:**  If database prefixing is enabled, you **must** prefix this value with the account prefix and an underscore (`_`). For example, for the `db` database on the `user` cPanel account, pass in a value of `user_db`.
    user = 'cpuser_dbuser' # str | The database user's name.  **Important:**  If database prefixing is enabled, you **must** prefix this value with the account prefix and an underscore (`_`). For example, for the `dbuser` user on the `user` cPanel account, pass in a value of `user_dbuser`.
    privileges = 'DELETE,UPDATE,CREATE,ALTER' # str | * `ALL PRIVILEGES` * A comma-separated list of one or more of the following individual privileges:   * `ALTER`   * `ALTER ROUTINE`   * `CREATE`   * `CREATE ROUTINE`   * `CREATE TEMPORARY TABLES`   * `CREATE VIEW`   * `DELETE`   * `DROP`   * `EVENT`   * `EXECUTE`   * `INDEX`   * `INSERT`   * `LOCK TABLES`   * `REFERENCES`   * `SELECT`   * `SHOW VIEW`   * `TRIGGER`   * `UPDATE`  **Note:**  * This list replaces, rather than adds to, the existing privilege list. * In browser-based and command line calls, separate multiple values with `%2C` and replace spaces with `%20`. (optional)

    try:
        # Update MySQL user privileges
        api_response = api_instance.set_privileges_on_database(database, user, privileges=privileges)
        print("The response of UserManagementApi->set_privileges_on_database:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserManagementApi->set_privileges_on_database: %s\n" % e)
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

