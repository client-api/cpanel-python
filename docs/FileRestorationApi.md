# clientapi_cpanel.FileRestorationApi

All URIs are relative to *https://cpanel-server.tld:2083/execute*

Method | HTTP request | Description
------------- | ------------- | -------------
[**directory_listing**](FileRestorationApi.md#directory_listing) | **GET** /Restore/directory_listing | Return backups in home directory
[**get_users**](FileRestorationApi.md#get_users) | **GET** /Restore/get_users | Return cPanel accounts with backup metadata
[**query_file_info**](FileRestorationApi.md#query_file_info) | **GET** /Restore/query_file_info | Return backup storage locations
[**restore_databases**](FileRestorationApi.md#restore_databases) | **POST** /Backup/restore_databases | Restore databases
[**restore_email_filters**](FileRestorationApi.md#restore_email_filters) | **POST** /Backup/restore_email_filters | Restore email filters
[**restore_email_forwarders**](FileRestorationApi.md#restore_email_forwarders) | **POST** /Backup/restore_email_forwarders | Restore email forwarders
[**restore_file**](FileRestorationApi.md#restore_file) | **GET** /Restore/restore_file | Restore file or directory
[**restore_files**](FileRestorationApi.md#restore_files) | **POST** /Backup/restore_files | Restore files


# **directory_listing**
> InlineResponse200397 directory_listing(path)

Return backups in home directory

This function lists all of the backup files and directories in the user's home directory.

**Important:**

When you disable the [File Storage role](https://go.cpanel.net/serverroles), the system **disables** this function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200397 import InlineResponse200397
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
    api_instance = clientapi_cpanel.FileRestorationApi(api_client)
    path = '/public_html/' # str | A path to a subdirectory within the user's home directory, or any level below it.  **Note:**  The value of this parameter **must** begin and end with a forward slash (`/`) for security purposes.

    try:
        # Return backups in home directory
        api_response = api_instance.directory_listing(path)
        print("The response of FileRestorationApi->directory_listing:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FileRestorationApi->directory_listing: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**| A path to a subdirectory within the user&#39;s home directory, or any level below it.  **Note:**  The value of this parameter **must** begin and end with a forward slash (&#x60;/&#x60;) for security purposes. | 

### Return type

[**InlineResponse200397**](InlineResponse200397.md)

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

# **get_users**
> InlineResponse200398 get_users()

Return cPanel accounts with backup metadata

This function lists a reseller's users that have existing backup metadata.

**Note:**

When you disable the [File Storage role](https://go.cpanel.net/serverroles), the system **disables** this function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200398 import InlineResponse200398
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
    api_instance = clientapi_cpanel.FileRestorationApi(api_client)

    try:
        # Return cPanel accounts with backup metadata
        api_response = api_instance.get_users()
        print("The response of FileRestorationApi->get_users:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FileRestorationApi->get_users: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**InlineResponse200398**](InlineResponse200398.md)

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

# **query_file_info**
> InlineResponse200399 query_file_info(path, exists=exists)

Return backup storage locations

This function lists all of an item's backup locations. An item can be a file, a directory, or a symlink.

**Important:**

When you disable the [File Storage role](https://go.cpanel.net/serverroles#roles), the system **disables** this function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200399 import InlineResponse200399
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
    api_instance = clientapi_cpanel.FileRestorationApi(api_client)
    path = '/public_html/index.php' # str | A file, directory, or symlink in the user's directory tree.  **Note:**  The value of this parameter **must** begin with a forward slash (`/`).
    exists = 0 # int | Whether to show the `exist` return, which indicates whether the item exists in the local disk or only in the backup.  * `1` — Show the `exist` return's value. * `0` — Do **not** show the `exists` return's value. (optional) (default to 0)

    try:
        # Return backup storage locations
        api_response = api_instance.query_file_info(path, exists=exists)
        print("The response of FileRestorationApi->query_file_info:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FileRestorationApi->query_file_info: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**| A file, directory, or symlink in the user&#39;s directory tree.  **Note:**  The value of this parameter **must** begin with a forward slash (&#x60;/&#x60;). | 
 **exists** | **int**| Whether to show the &#x60;exist&#x60; return, which indicates whether the item exists in the local disk or only in the backup.  * &#x60;1&#x60; — Show the &#x60;exist&#x60; return&#39;s value. * &#x60;0&#x60; — Do **not** show the &#x60;exists&#x60; return&#39;s value. | [optional] [default to 0]

### Return type

[**InlineResponse200399**](InlineResponse200399.md)

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

# **restore_databases**
> InlineResponse2007 restore_databases(backup=backup, timeout=timeout, verbose=verbose, file=file)

Restore databases

This function restores a database's backup files.

**Important:**

When the [MySQL Client role](https://go.cpanel.net/howtouseserverprofiles#roles) is disabled, the system also **disables** this function.

**Note:**

You **must** pass either the `file` **or** `backup` parameter.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response2007 import InlineResponse2007
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
    api_instance = clientapi_cpanel.FileRestorationApi(api_client)
    backup = 'backup-1=home/user/user_db1.sql.gz backup-2=home/user/user_db2.sql.gz backup-3=home/user/user_db3.sql.gz' # str | The database backup file to restore.  **Important:**  **Only** pass this parameter to restore files already on the server.  **Note:**  To restore multiple database backup files, increment the parameter name. For example: `backup-1`, `backup-2`, and `backup-3`. (optional)
    timeout = 7200 # int | The maximum number of seconds to try to restore the file. * `0` - The system will not time out the file restoration. (optional) (default to 7200)
    verbose = 0 # int | Whether to return additional information from the `/usr/local/cpanel/logs/cpbackup` log file. * `1` - Return additional information. * `0` - Do **not** return additional information. (optional) (default to 0)
    file = None # bytearray |  (optional)

    try:
        # Restore databases
        api_response = api_instance.restore_databases(backup=backup, timeout=timeout, verbose=verbose, file=file)
        print("The response of FileRestorationApi->restore_databases:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FileRestorationApi->restore_databases: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **backup** | **str**| The database backup file to restore.  **Important:**  **Only** pass this parameter to restore files already on the server.  **Note:**  To restore multiple database backup files, increment the parameter name. For example: &#x60;backup-1&#x60;, &#x60;backup-2&#x60;, and &#x60;backup-3&#x60;. | [optional] 
 **timeout** | **int**| The maximum number of seconds to try to restore the file. * &#x60;0&#x60; - The system will not time out the file restoration. | [optional] [default to 7200]
 **verbose** | **int**| Whether to return additional information from the &#x60;/usr/local/cpanel/logs/cpbackup&#x60; log file. * &#x60;1&#x60; - Return additional information. * &#x60;0&#x60; - Do **not** return additional information. | [optional] [default to 0]
 **file** | **bytearray**|  | [optional] 

### Return type

[**InlineResponse2007**](InlineResponse2007.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | HTTP Request was successful. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **restore_email_filters**
> InlineResponse2008 restore_email_filters(backup=backup, timeout=timeout, verbose=verbose, backup2=backup2)

Restore email filters

This function restores an account's email filters.

**Important:**

When the [Receive Mail role](https://go.cpanel.net/howtouseserverprofiles#roles) is disabled, the system also **disables** this function.

**Note:**

You **must** use the `backup` parameter when you call this function in one of the following formats:
* As part of a `multipart/form-data` request body to upload and restore a backup file to the server.
* As a query parameter to restore an existing file on the server.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response2008 import InlineResponse2008
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
    api_instance = clientapi_cpanel.FileRestorationApi(api_client)
    backup = 'backup-1=/home/user/filter_info1.username.yaml.gz backup-2=/home/user/filter_info2.username.yaml.gz backup-3=/home/user/filter_info3.username.yaml.gz' # str | The email filter file to restore.  **Important:**  **Only** pass this parameter to restore email filter files that already exist on the server.  **Note:**  To restore multiple email filter files, increment the parameter name. For example: `backup-1`, `backup-2`, and `backup-3`. (optional)
    timeout = 7200 # int | The maximum number of seconds to try to restore the file. * `0` - The system will not time out the file restoration. (optional) (default to 7200)
    verbose = 0 # int | Whether to return additional information from the `/home/cpuser/.cpanel/logs/restore-email-filters` log files. * `1` - Return additional information. * `0` - Do not return additional information. (optional) (default to 0)
    backup2 = None # bytearray |  (optional)

    try:
        # Restore email filters
        api_response = api_instance.restore_email_filters(backup=backup, timeout=timeout, verbose=verbose, backup2=backup2)
        print("The response of FileRestorationApi->restore_email_filters:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FileRestorationApi->restore_email_filters: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **backup** | **str**| The email filter file to restore.  **Important:**  **Only** pass this parameter to restore email filter files that already exist on the server.  **Note:**  To restore multiple email filter files, increment the parameter name. For example: &#x60;backup-1&#x60;, &#x60;backup-2&#x60;, and &#x60;backup-3&#x60;. | [optional] 
 **timeout** | **int**| The maximum number of seconds to try to restore the file. * &#x60;0&#x60; - The system will not time out the file restoration. | [optional] [default to 7200]
 **verbose** | **int**| Whether to return additional information from the &#x60;/home/cpuser/.cpanel/logs/restore-email-filters&#x60; log files. * &#x60;1&#x60; - Return additional information. * &#x60;0&#x60; - Do not return additional information. | [optional] [default to 0]
 **backup2** | **bytearray**|  | [optional] 

### Return type

[**InlineResponse2008**](InlineResponse2008.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | HTTP Request was successful. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **restore_email_forwarders**
> InlineResponse2009 restore_email_forwarders(backup=backup, timeout=timeout, verbose=verbose, backup2=backup2)

Restore email forwarders

This function restores an account's email forwarders.

**Important:**

When the [Receive Mail role](https://go.cpanel.net/howtouseserverprofiles#roles) is disabled, the system also **disables** this function.

**Note:**

You **must** use the `backup` parameter when you call this function in one of the following formats:
* As part of a `multipart/form-data` request body to upload and restore a backup file to the server. For more information about this structure, read Mozilla's [POST Method](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods/POST) documentation.
* As a query parameter to restore an existing file on the server.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response2009 import InlineResponse2009
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
    api_instance = clientapi_cpanel.FileRestorationApi(api_client)
    backup = 'backup-1=/home/user/aliases-example1.com.gz backup-2=/home/user/aliases-example2.com.gz backup-3=/home/user/aliases-example3.com.gz' # str | The email forwarder file to restore.  **Important:**  **Only** pass this parameter to restore email forwarder files that already exist on the server.  **Note:**  To restore multiple email filter files, increment the parameter name. For example: `backup-1`, `backup-2`, and `backup-3`. (optional)
    timeout = 7200 # int | The maximum number of seconds to try to restore the file. * `0` - The system will not time out the file restoration. (optional) (default to 7200)
    verbose = 0 # int | Whether to return additional information from the `/home/cpuser/.cpanel/logs/restore-email-forwarders` log files. * `1` - Return additional information. * `0` - Do not return additional information. (optional) (default to 0)
    backup2 = None # bytearray |  (optional)

    try:
        # Restore email forwarders
        api_response = api_instance.restore_email_forwarders(backup=backup, timeout=timeout, verbose=verbose, backup2=backup2)
        print("The response of FileRestorationApi->restore_email_forwarders:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FileRestorationApi->restore_email_forwarders: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **backup** | **str**| The email forwarder file to restore.  **Important:**  **Only** pass this parameter to restore email forwarder files that already exist on the server.  **Note:**  To restore multiple email filter files, increment the parameter name. For example: &#x60;backup-1&#x60;, &#x60;backup-2&#x60;, and &#x60;backup-3&#x60;. | [optional] 
 **timeout** | **int**| The maximum number of seconds to try to restore the file. * &#x60;0&#x60; - The system will not time out the file restoration. | [optional] [default to 7200]
 **verbose** | **int**| Whether to return additional information from the &#x60;/home/cpuser/.cpanel/logs/restore-email-forwarders&#x60; log files. * &#x60;1&#x60; - Return additional information. * &#x60;0&#x60; - Do not return additional information. | [optional] [default to 0]
 **backup2** | **bytearray**|  | [optional] 

### Return type

[**InlineResponse2009**](InlineResponse2009.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | HTTP Request was successful. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **restore_file**
> InlineResponse200400 restore_file(backup_id, overwrite, path)

Restore file or directory

This function restores a file or directory from a backup to the file or directory's original location.

**Important:**

When you disable the [File Storage role](https://go.cpanel.net/serverroles#roles), the system **disables** this function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200400 import InlineResponse200400
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
    api_instance = clientapi_cpanel.FileRestorationApi(api_client)
    backup_id = clientapi_cpanel.BackupID() # BackupID | The backup's identification.  * `YYYY-MM-DD` — Restore a daily backup from the specified backup date. * `incremental` — Restore a daily incremental backup. * `weekly/YYYY-MM-DD` — Restore a weekly backup from the specified backup date. * `monthly/YYYY-MM-DD` — Restore a monthly backup from the specified backup date. * `weekly/incremental` — Restore a weekly incremental backup. * `monthly/incremental` — Restore a monthly incremental backup.
    overwrite = 1 # int | Whether to overwrite the file or directory on the disc with its backup replacement.  * `1` — Overwrite the file or directory. * `0` — Do **not** overwrite the file or directory.
    path = '/public_html/index.php' # str | The absolute file or directory's path, within a backup, that you wish to restore.  **Important:**  * The value of this parameter **must** begin with a forward slash (/). * You **must** parse filenames properly to prevent a cross-site scripting (XSS) attack.

    try:
        # Restore file or directory
        api_response = api_instance.restore_file(backup_id, overwrite, path)
        print("The response of FileRestorationApi->restore_file:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FileRestorationApi->restore_file: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **backup_id** | [**BackupID**](.md)| The backup&#39;s identification.  * &#x60;YYYY-MM-DD&#x60; — Restore a daily backup from the specified backup date. * &#x60;incremental&#x60; — Restore a daily incremental backup. * &#x60;weekly/YYYY-MM-DD&#x60; — Restore a weekly backup from the specified backup date. * &#x60;monthly/YYYY-MM-DD&#x60; — Restore a monthly backup from the specified backup date. * &#x60;weekly/incremental&#x60; — Restore a weekly incremental backup. * &#x60;monthly/incremental&#x60; — Restore a monthly incremental backup. | 
 **overwrite** | **int**| Whether to overwrite the file or directory on the disc with its backup replacement.  * &#x60;1&#x60; — Overwrite the file or directory. * &#x60;0&#x60; — Do **not** overwrite the file or directory. | 
 **path** | **str**| The absolute file or directory&#39;s path, within a backup, that you wish to restore.  **Important:**  * The value of this parameter **must** begin with a forward slash (/). * You **must** parse filenames properly to prevent a cross-site scripting (XSS) attack. | 

### Return type

[**InlineResponse200400**](InlineResponse200400.md)

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

# **restore_files**
> InlineResponse20010 restore_files(backup=backup, directory=directory, timeout=timeout, verbose=verbose, backup2=backup2)

Restore files

This function restores an account's files.

**Important:**

When the [File Storage role](https://go.cpanel.net/howtouseserverprofiles#roles) is disabled, the system also **disables** this function.

**Note:**

You **must** use the `backup` parameter when you call this function in one of the following formats:
* As part of a `multipart/form-data` request body to upload and restore a backup file to the server. For more information about this structure, read Mozilla's [POST Method](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods/POST) documentation.
* As a query parameter to restore an existing file on the server.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response20010 import InlineResponse20010
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
    api_instance = clientapi_cpanel.FileRestorationApi(api_client)
    backup = 'backup-1=/home/cpuser/backup-cpuser.tld-9-10-2019_1.tar.gz backup-2=/home/cpuser/backup-cpuser.tld-9-10-2019_2.tar.gz' # str | The backup file to restore.  **Important:**  **Only** pass this parameter to restore backup files that already exist on the server.  **Note:**  To restore multiple backup files, increment the parameter name. For example: `backup-1`, `backup-2`, and `backup-3`. (optional)
    directory = '/home/user/example' # str | The directory to which to restore the file. The default is the user's `home` directory. (optional)
    timeout = 172800 # int | The maximum number of seconds to try to restore the file. * `0` - The system will not time out the file restoration. (optional) (default to 172800)
    verbose = 0 # int | Whether to return additional information from the `/home/cptest/.cpanel/logs/restorefiles` log files. * `1` - Return additional information. * `0` - Do not return additional information. (optional) (default to 0)
    backup2 = None # bytearray |  (optional)

    try:
        # Restore files
        api_response = api_instance.restore_files(backup=backup, directory=directory, timeout=timeout, verbose=verbose, backup2=backup2)
        print("The response of FileRestorationApi->restore_files:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FileRestorationApi->restore_files: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **backup** | **str**| The backup file to restore.  **Important:**  **Only** pass this parameter to restore backup files that already exist on the server.  **Note:**  To restore multiple backup files, increment the parameter name. For example: &#x60;backup-1&#x60;, &#x60;backup-2&#x60;, and &#x60;backup-3&#x60;. | [optional] 
 **directory** | **str**| The directory to which to restore the file. The default is the user&#39;s &#x60;home&#x60; directory. | [optional] 
 **timeout** | **int**| The maximum number of seconds to try to restore the file. * &#x60;0&#x60; - The system will not time out the file restoration. | [optional] [default to 172800]
 **verbose** | **int**| Whether to return additional information from the &#x60;/home/cptest/.cpanel/logs/restorefiles&#x60; log files. * &#x60;1&#x60; - Return additional information. * &#x60;0&#x60; - Do not return additional information. | [optional] [default to 0]
 **backup2** | **bytearray**|  | [optional] 

### Return type

[**InlineResponse20010**](InlineResponse20010.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | HTTP Request was successful. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

