# clientapi_cpanel.BackupApi

All URIs are relative to *https://cpanel-server.tld:2083/execute*

Method | HTTP request | Description
------------- | ------------- | -------------
[**fullbackup_to_ftp**](BackupApi.md#fullbackup_to_ftp) | **GET** /Backup/fullbackup_to_ftp | Back up cPanel account via FTP
[**fullbackup_to_homedir**](BackupApi.md#fullbackup_to_homedir) | **GET** /Backup/fullbackup_to_homedir | Back up cPanel account to home directory
[**fullbackup_to_scp_with_key**](BackupApi.md#fullbackup_to_scp_with_key) | **GET** /Backup/fullbackup_to_scp_with_key | Back up cPanel account via SCP with SSH key
[**fullbackup_to_scp_with_password**](BackupApi.md#fullbackup_to_scp_with_password) | **GET** /Backup/fullbackup_to_scp_with_password | Back up cPanel account via SCP with password
[**list_backups**](BackupApi.md#list_backups) | **GET** /Backup/list_backups | Return backup files


# **fullbackup_to_ftp**
> InlineResponse2002 fullbackup_to_ftp(host, password, username, directory=directory, email=email, homedir=homedir, port=port, variant=variant)

Back up cPanel account via FTP

This function creates a full backup to the remote server via File Transfer Protocol (FTP). The system creates a file in the `backup-MM.DD.YYYY_HH-mm-ss.tar.gz` filename format.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response2002 import InlineResponse2002
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
    api_instance = clientapi_cpanel.BackupApi(api_client)
    host = clientapi_cpanel.Host() # Host | The remote server's hostname or IP address.
    password = 'luggage123456' # str | The remote server account's password.
    username = 'username' # str | The remote server account's username.
    directory = '/public_ftp' # str | The directory on the remote server that will store the backup.  **Note:**  * This value defaults to the remote server account's default login directory. * Enter the directory relative to the FTP user's login directory. For example, enter `/public_ftp` not `/home/username/public_ftp`. (optional)
    email = 'username@example.com' # str | The email address to receive a confirmation email when the backup completes.  **Note:**   The system does **not** provide confirmation if you do **not** pass this parameter. (optional)
    homedir = include # str | How to manage the home directory in the backup.  * `include` — Include the home directory in the backup. * `skip` — Omit the home directory from the backup. (optional) (default to include)
    port = 21 # int | The port number to use during the transfer. (optional) (default to 21)
    variant = active # str | Whether to use the `active` or `passive` FTP variant to connect to the remote server. For more information about FTP variants, read our How to [Enable FTP Passive Mode](https://go.cpanel.net/HowtoEnableFTPPassiveMode) documentation. * `active` — The FTP server responds to the connection attempt and returns a connection request from a different port to the FTP client. * `passive` — The FTP client initiates connection attempts. (optional) (default to active)

    try:
        # Back up cPanel account via FTP
        api_response = api_instance.fullbackup_to_ftp(host, password, username, directory=directory, email=email, homedir=homedir, port=port, variant=variant)
        print("The response of BackupApi->fullbackup_to_ftp:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BackupApi->fullbackup_to_ftp: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **host** | **Host**| The remote server&#39;s hostname or IP address. | 
 **password** | **str**| The remote server account&#39;s password. | 
 **username** | **str**| The remote server account&#39;s username. | 
 **directory** | **str**| The directory on the remote server that will store the backup.  **Note:**  * This value defaults to the remote server account&#39;s default login directory. * Enter the directory relative to the FTP user&#39;s login directory. For example, enter &#x60;/public_ftp&#x60; not &#x60;/home/username/public_ftp&#x60;. | [optional] 
 **email** | **str**| The email address to receive a confirmation email when the backup completes.  **Note:**   The system does **not** provide confirmation if you do **not** pass this parameter. | [optional] 
 **homedir** | **str**| How to manage the home directory in the backup.  * &#x60;include&#x60; — Include the home directory in the backup. * &#x60;skip&#x60; — Omit the home directory from the backup. | [optional] [default to include]
 **port** | **int**| The port number to use during the transfer. | [optional] [default to 21]
 **variant** | **str**| Whether to use the &#x60;active&#x60; or &#x60;passive&#x60; FTP variant to connect to the remote server. For more information about FTP variants, read our How to [Enable FTP Passive Mode](https://go.cpanel.net/HowtoEnableFTPPassiveMode) documentation. * &#x60;active&#x60; — The FTP server responds to the connection attempt and returns a connection request from a different port to the FTP client. * &#x60;passive&#x60; — The FTP client initiates connection attempts. | [optional] [default to active]

### Return type

[**InlineResponse2002**](InlineResponse2002.md)

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

# **fullbackup_to_homedir**
> InlineResponse2003 fullbackup_to_homedir(email=email, homedir=homedir)

Back up cPanel account to home directory

This function creates a full backup to the user's home directory. The system creates a file in the `backup-MM.DD.YYYY_HH-mm-ss_username.tar.gz` filename format.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response2003 import InlineResponse2003
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
    api_instance = clientapi_cpanel.BackupApi(api_client)
    email = 'username@example.com' # str | The email address to receive a confirmation email when the backup process completes.  **Note:**  The system does **not** provide confirmation if you do not pass this parameter. (optional)
    homedir = include # str | How to manage the home directory in the backup.  * `include` — Include the home directory in the backup. * `skip` — Omit the home directory from the backup. (optional) (default to include)

    try:
        # Back up cPanel account to home directory
        api_response = api_instance.fullbackup_to_homedir(email=email, homedir=homedir)
        print("The response of BackupApi->fullbackup_to_homedir:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BackupApi->fullbackup_to_homedir: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**| The email address to receive a confirmation email when the backup process completes.  **Note:**  The system does **not** provide confirmation if you do not pass this parameter. | [optional] 
 **homedir** | **str**| How to manage the home directory in the backup.  * &#x60;include&#x60; — Include the home directory in the backup. * &#x60;skip&#x60; — Omit the home directory from the backup. | [optional] [default to include]

### Return type

[**InlineResponse2003**](InlineResponse2003.md)

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

# **fullbackup_to_scp_with_key**
> InlineResponse2004 fullbackup_to_scp_with_key(host, key_name, key_passphrase, directory=directory, email=email, homedir=homedir, port=port)

Back up cPanel account via SCP with SSH key

This function creates a full backup to a remote server with a private SSH key via the secure copy protocol (scp) command. The system creates a file in the `backup-MM.DD.YYYY_HH-mm-ss_username.tar.gz` filename format.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response2004 import InlineResponse2004
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
    api_instance = clientapi_cpanel.BackupApi(api_client)
    host = clientapi_cpanel.Host1() # Host1 | The remote server's hostname or IP address.
    key_name = 'examplesshkey' # str | The SSH key's name.  **Notes:**  * To generate a private SSH key, use the UAPI `SSL::generate_key` function. * To import an existing SSH key, use the cPanel API 2 `SSH::importkey` function.
    key_passphrase = '123456luggage' # str | The SSH key's password.
    directory = '/user' # str | The directory on the remote server that will store the backup.  **Note:**  This parameter defaults to the remote server account's default login directory. (optional)
    email = 'username@example.com' # str | The email address to receive a confirmation email when the backup completes.  **Note:**  The system does **not** provide confirmation if you do not pass this parameter. (optional)
    homedir = include # str | How to manage the home directory in the backup.  * `include` — Include the home directory in the backup. * `skip` — Omit the home directory from the backup. (optional) (default to include)
    port = 22 # int | The port to use during the transfer. (optional) (default to 22)

    try:
        # Back up cPanel account via SCP with SSH key
        api_response = api_instance.fullbackup_to_scp_with_key(host, key_name, key_passphrase, directory=directory, email=email, homedir=homedir, port=port)
        print("The response of BackupApi->fullbackup_to_scp_with_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BackupApi->fullbackup_to_scp_with_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **host** | **Host1**| The remote server&#39;s hostname or IP address. | 
 **key_name** | **str**| The SSH key&#39;s name.  **Notes:**  * To generate a private SSH key, use the UAPI &#x60;SSL::generate_key&#x60; function. * To import an existing SSH key, use the cPanel API 2 &#x60;SSH::importkey&#x60; function. | 
 **key_passphrase** | **str**| The SSH key&#39;s password. | 
 **directory** | **str**| The directory on the remote server that will store the backup.  **Note:**  This parameter defaults to the remote server account&#39;s default login directory. | [optional] 
 **email** | **str**| The email address to receive a confirmation email when the backup completes.  **Note:**  The system does **not** provide confirmation if you do not pass this parameter. | [optional] 
 **homedir** | **str**| How to manage the home directory in the backup.  * &#x60;include&#x60; — Include the home directory in the backup. * &#x60;skip&#x60; — Omit the home directory from the backup. | [optional] [default to include]
 **port** | **int**| The port to use during the transfer. | [optional] [default to 22]

### Return type

[**InlineResponse2004**](InlineResponse2004.md)

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

# **fullbackup_to_scp_with_password**
> InlineResponse2005 fullbackup_to_scp_with_password(host, password, username, directory=directory, email=email, homedir=homedir, port=port)

Back up cPanel account via SCP with password

This function creates a full backup to a remote server via the secure copy protocol (`scp`) command with a password. The system creates a file in the `backup-MM.DD.YYYY_HH-mm-ss.tar.gz` filename format.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response2005 import InlineResponse2005
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
    api_instance = clientapi_cpanel.BackupApi(api_client)
    host = clientapi_cpanel.Host2() # Host2 | The remote server's hostname or IP address.
    password = 'luggage123456' # str | The remote server account's password.
    username = 'username' # str | The remote server account's username.
    directory = '/user' # str | The directory on the remote server that will store the backup.  **Note:**  This parameter defaults to the remote server account's default login directory. (optional)
    email = 'username@example.com' # str | The email address to receive a confirmation email when the backup completes.  **Note:**  The system does **not** provide confirmation if you do **not** pass this parameter. (optional)
    homedir = include # str | How to manage the home directory in the backup.  * `include` — Include the home directory in the backup. * `skip` — Omit the home directory from the backup. (optional) (default to include)
    port = 22 # int | The port to use during the transfer. (optional) (default to 22)

    try:
        # Back up cPanel account via SCP with password
        api_response = api_instance.fullbackup_to_scp_with_password(host, password, username, directory=directory, email=email, homedir=homedir, port=port)
        print("The response of BackupApi->fullbackup_to_scp_with_password:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BackupApi->fullbackup_to_scp_with_password: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **host** | **Host2**| The remote server&#39;s hostname or IP address. | 
 **password** | **str**| The remote server account&#39;s password. | 
 **username** | **str**| The remote server account&#39;s username. | 
 **directory** | **str**| The directory on the remote server that will store the backup.  **Note:**  This parameter defaults to the remote server account&#39;s default login directory. | [optional] 
 **email** | **str**| The email address to receive a confirmation email when the backup completes.  **Note:**  The system does **not** provide confirmation if you do **not** pass this parameter. | [optional] 
 **homedir** | **str**| How to manage the home directory in the backup.  * &#x60;include&#x60; — Include the home directory in the backup. * &#x60;skip&#x60; — Omit the home directory from the backup. | [optional] [default to include]
 **port** | **int**| The port to use during the transfer. | [optional] [default to 22]

### Return type

[**InlineResponse2005**](InlineResponse2005.md)

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

# **list_backups**
> InlineResponse2006 list_backups()

Return backup files

This function lists the account's backup files.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response2006 import InlineResponse2006
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
    api_instance = clientapi_cpanel.BackupApi(api_client)

    try:
        # Return backup files
        api_response = api_instance.list_backups()
        print("The response of BackupApi->list_backups:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BackupApi->list_backups: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**InlineResponse2006**](InlineResponse2006.md)

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

