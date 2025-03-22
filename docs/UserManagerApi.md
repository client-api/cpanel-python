# clientapi_cpanel.UserManagerApi

All URIs are relative to *https://cpanel-server.tld:2083/execute*

Method | HTTP request | Description
------------- | ------------- | -------------
[**change_password**](UserManagerApi.md#change_password) | **GET** /UserManager/change_password | Update cPanel account password
[**check_account_conflicts**](UserManagerApi.md#check_account_conflicts) | **GET** /UserManager/check_account_conflicts | Return Subaccounts and service accounts conflicts
[**dismiss_merge**](UserManagerApi.md#dismiss_merge) | **GET** /UserManager/dismiss_merge | Remove service account link request
[**edit_user**](UserManagerApi.md#edit_user) | **GET** /UserManager/edit_user | Update Subaccount settings
[**lookup_service_account**](UserManagerApi.md#lookup_service_account) | **GET** /UserManager/lookup_service_account | Return service account&#39;s information
[**lookup_user**](UserManagerApi.md#lookup_user) | **GET** /UserManager/lookup_user | Return Subaccount&#39;s information
[**merge_service_account**](UserManagerApi.md#merge_service_account) | **GET** /UserManager/merge_service_account | Register service account to Subaccount
[**unlink_service_account**](UserManagerApi.md#unlink_service_account) | **GET** /UserManager/unlink_service_account | Unregister service account from Subaccount
[**user_manager_create_user**](UserManagerApi.md#user_manager_create_user) | **GET** /UserManager/create_user | Create Subaccount
[**user_manager_delete_user**](UserManagerApi.md#user_manager_delete_user) | **GET** /UserManager/delete_user | Delete Subaccount
[**user_manager_list_users**](UserManagerApi.md#user_manager_list_users) | **GET** /UserManager/list_users | Return cPanel account&#39;s Subaccounts


# **change_password**
> InlineResponse200526 change_password(newpass, oldpass, enablemysql=enablemysql)

Update cPanel account password

This function updates the cPanel account's password.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200526 import InlineResponse200526
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
    api_instance = clientapi_cpanel.UserManagerApi(api_client)
    newpass = 'MyNewPassw0rd!' # str | The new password.
    oldpass = 'ThisWasMyPassword!' # str | The current password.
    enablemysql = 0 # int | Whether to update the cPanel account's MySQL password. * `1` - Update MySQL password. * `0` - Do not update MySQL passowrd. (optional) (default to 0)

    try:
        # Update cPanel account password
        api_response = api_instance.change_password(newpass, oldpass, enablemysql=enablemysql)
        print("The response of UserManagerApi->change_password:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserManagerApi->change_password: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **newpass** | **str**| The new password. | 
 **oldpass** | **str**| The current password. | 
 **enablemysql** | **int**| Whether to update the cPanel account&#39;s MySQL password. * &#x60;1&#x60; - Update MySQL password. * &#x60;0&#x60; - Do not update MySQL passowrd. | [optional] [default to 0]

### Return type

[**InlineResponse200526**](InlineResponse200526.md)

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

# **check_account_conflicts**
> InlineResponse200527 check_account_conflicts(full_username)

Return Subaccounts and service accounts conflicts

This function lists the other Subaccounts or services accounts that conflict
with the specified username.

**Note:**

If the function returns more than one account, it will return some values
multiple times within the return arrays.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200527 import InlineResponse200527
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
    api_instance = clientapi_cpanel.UserManagerApi(api_client)
    full_username = 'username@example.com' # str | The Subaccount's username and domain name.

    try:
        # Return Subaccounts and service accounts conflicts
        api_response = api_instance.check_account_conflicts(full_username)
        print("The response of UserManagerApi->check_account_conflicts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserManagerApi->check_account_conflicts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **full_username** | **str**| The Subaccount&#39;s username and domain name. | 

### Return type

[**InlineResponse200527**](InlineResponse200527.md)

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

# **dismiss_merge**
> InlineResponse200530 dismiss_merge(domain, username, services_email_dismiss=services_email_dismiss, services_ftp_dismiss=services_ftp_dismiss, services_webdisk_dismiss=services_webdisk_dismiss)

Remove service account link request

This function removes a service account as a link candidate to create a subaccount or
link to a subaccount. When you use this function, the system removes the *Link* option in
cPanel's [*User Manager*](https://go.cpanel.net/cpaneldocsUserManager) interface (_cPanel >> Home >> Preferences >> User Manager_).

**Note:**

You **must** use at least one of the following parameters:
* `services.email.dismiss`
* `services.ftp.dismiss`
* `services.webdisk.dismiss`

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200530 import InlineResponse200530
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
    api_instance = clientapi_cpanel.UserManagerApi(api_client)
    domain = 'example.com' # str | The service account's associated domain.
    username = 'example1' # str | The username for the service account.  **Note:**  This parameter does **not** include the domain name.
    services_email_dismiss = 0 # int | Whether to dismiss the merge of the email service account.  * `1` - Dismiss. * `0` - Do **not** dismiss. (optional) (default to 0)
    services_ftp_dismiss = 0 # int | Whether to dismiss the merge of the FTP service account.  * `1` - Dismiss. * `0` - Do **not** dismiss. (optional) (default to 0)
    services_webdisk_dismiss = 0 # int | Whether to dismiss the merge of the Web Disk service account.  * `1` - Dismiss. * `0` - Do **not** dismiss. (optional) (default to 0)

    try:
        # Remove service account link request
        api_response = api_instance.dismiss_merge(domain, username, services_email_dismiss=services_email_dismiss, services_ftp_dismiss=services_ftp_dismiss, services_webdisk_dismiss=services_webdisk_dismiss)
        print("The response of UserManagerApi->dismiss_merge:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserManagerApi->dismiss_merge: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**| The service account&#39;s associated domain. | 
 **username** | **str**| The username for the service account.  **Note:**  This parameter does **not** include the domain name. | 
 **services_email_dismiss** | **int**| Whether to dismiss the merge of the email service account.  * &#x60;1&#x60; - Dismiss. * &#x60;0&#x60; - Do **not** dismiss. | [optional] [default to 0]
 **services_ftp_dismiss** | **int**| Whether to dismiss the merge of the FTP service account.  * &#x60;1&#x60; - Dismiss. * &#x60;0&#x60; - Do **not** dismiss. | [optional] [default to 0]
 **services_webdisk_dismiss** | **int**| Whether to dismiss the merge of the Web Disk service account.  * &#x60;1&#x60; - Dismiss. * &#x60;0&#x60; - Do **not** dismiss. | [optional] [default to 0]

### Return type

[**InlineResponse200530**](InlineResponse200530.md)

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

# **edit_user**
> InlineResponse200531 edit_user(domain, username, alternate_email=alternate_email, avatar_url=avatar_url, password=password, phone_number=phone_number, real_name=real_name, services_email_enabled=services_email_enabled, services_email_quota=services_email_quota, services_ftp_enabled=services_ftp_enabled, services_ftp_homedir=services_ftp_homedir, services_webdisk_enabled=services_webdisk_enabled, services_webdisk_enabledigest=services_webdisk_enabledigest, services_webdisk_homedir=services_webdisk_homedir, services_webdisk_perms=services_webdisk_perms, services_webdisk_private=services_webdisk_private, type=type)

Update Subaccount settings

This function edits a Subaccount.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200531 import InlineResponse200531
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
    api_instance = clientapi_cpanel.UserManagerApi(api_client)
    domain = 'example.com' # str | The Subaccount user's associated domain.  A domain that the cPanel account owns.
    username = 'example' # str | The Subaccount's username.  * Length - 64 characters. * Characters - `a-z`, `A-Z`, `0-9`, dot (`.`), hyphen (`-`), underscore (`_`).  **Note:**   This value does **not** include the domain name.
    alternate_email = 'user@example.com' # str | An alternate email address for the Subaccount's user.  **Note:**   The cPanel account user could use this email address to contact the Subaccount user if their primary email address's domain is unavailable. (optional)
    avatar_url = 'https://img.example.com/avatars/example.jpg' # str | **Warning:**   We reserved this parameter for future use. Do **not** use this parameter.  The user's Subaccount profile photo.  **Note:**   You **must** use the HTTPS protocol to prevent mixed content warnings when users view the photo from another HTTPS URL. (optional)
    password = '12345luggage' # str | The Subaccount's new password.  **Note:**   The Subaccount uses this password for email, FTP, and Web Disk services. (optional)
    phone_number = '+15551234567' # str | The Subaccount user's phone number.  **Warning:**   We reserved this parameter for future use. Do **not** use this parameter.  The number conforms to the [ITU-T](https://en.wikipedia.org/wiki/ITU-T)'s [E.164](https://en.wikipedia.org/wiki/E.164)-recommended standard for the representation of telephone numbers. (optional)
    real_name = 'John Doe' # str | The Subaccount user's name.  * A first name. * A last name. * A first name and last name. * An empty string. (optional)
    services_email_enabled = 0 # int | Whether to grant the Subaccount email access.  * `1` - Can access. * `0` - **Cannot** access. (optional) (default to 0)
    services_email_quota = 500 # int | The maximum amount of disk space, in megabytes (MB), that the subaccount's email account may use.  If you do not declare a value, the system defaults to the defined system value.  **Note:**   This value **cannot** be greater than the maximum email quota.  * `0` or `unlimited` - The subaccount possesses unlimited disk space. (optional)
    services_ftp_enabled = 0 # int | Whether to grant the Subaccount FTP access.  * `1` - Can access. * `0` - **Cannot** access. (optional) (default to 0)
    services_ftp_homedir = '/Subaccount' # str | The Subaccount's FTP home directory.  **Note:**   This parameter is **required** if you enable FTP access.  A relative path from the cPanel account's home directory.  **Note:**   The specified directory **must** exist. (optional)
    services_webdisk_enabled = 0 # int | Whether to grant the Subaccount Web Disk access.  * `1` - Can access. * `0` - **Cannot** access. (optional) (default to 0)
    services_webdisk_enabledigest = 0 # int | Whether to enable Web Disk digest authentication.  **Notes:**   * **Only** enable Digest Authentication for clients that require additional compatibility support on certain versions of Windows® operating systems. This compatibility support is **only** required on servers that use a self-signed certificate for the `cpsrvd` and `cpdavd` daemons.  * We recommend that you do **not** use Digest Authentication.   * `1` - Enabled * `0` - Disabled. (optional) (default to 0)
    services_webdisk_homedir = '/Subaccount' # str | The Subaccount's Web Disk home directory.  **Note:**   This parameter is **required** if you enable Web Disk access.  A relative path from the cPanel account's home directory. (optional)
    services_webdisk_perms = rw # str | Whether to grant write permissions to the Subaccount.  **Note:**   The `services.webdisk.homedir` parameter determines the Subaccount's Web Disk home directory.  * `ro` - Read-only permissions. * `rw` - Read and write permissions. (optional) (default to rw)
    services_webdisk_private = 0 # int | Whether to set the Web Disk directory's permissions to public or private.  * `1` - Private (`0700`). * `0` - Public (`0755`). (optional) (default to 0)
    type = sub # str | The type of account.  * `sub` - A Subaccount. (optional) (default to sub)

    try:
        # Update Subaccount settings
        api_response = api_instance.edit_user(domain, username, alternate_email=alternate_email, avatar_url=avatar_url, password=password, phone_number=phone_number, real_name=real_name, services_email_enabled=services_email_enabled, services_email_quota=services_email_quota, services_ftp_enabled=services_ftp_enabled, services_ftp_homedir=services_ftp_homedir, services_webdisk_enabled=services_webdisk_enabled, services_webdisk_enabledigest=services_webdisk_enabledigest, services_webdisk_homedir=services_webdisk_homedir, services_webdisk_perms=services_webdisk_perms, services_webdisk_private=services_webdisk_private, type=type)
        print("The response of UserManagerApi->edit_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserManagerApi->edit_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**| The Subaccount user&#39;s associated domain.  A domain that the cPanel account owns. | 
 **username** | **str**| The Subaccount&#39;s username.  * Length - 64 characters. * Characters - &#x60;a-z&#x60;, &#x60;A-Z&#x60;, &#x60;0-9&#x60;, dot (&#x60;.&#x60;), hyphen (&#x60;-&#x60;), underscore (&#x60;_&#x60;).  **Note:**   This value does **not** include the domain name. | 
 **alternate_email** | **str**| An alternate email address for the Subaccount&#39;s user.  **Note:**   The cPanel account user could use this email address to contact the Subaccount user if their primary email address&#39;s domain is unavailable. | [optional] 
 **avatar_url** | **str**| **Warning:**   We reserved this parameter for future use. Do **not** use this parameter.  The user&#39;s Subaccount profile photo.  **Note:**   You **must** use the HTTPS protocol to prevent mixed content warnings when users view the photo from another HTTPS URL. | [optional] 
 **password** | **str**| The Subaccount&#39;s new password.  **Note:**   The Subaccount uses this password for email, FTP, and Web Disk services. | [optional] 
 **phone_number** | **str**| The Subaccount user&#39;s phone number.  **Warning:**   We reserved this parameter for future use. Do **not** use this parameter.  The number conforms to the [ITU-T](https://en.wikipedia.org/wiki/ITU-T)&#39;s [E.164](https://en.wikipedia.org/wiki/E.164)-recommended standard for the representation of telephone numbers. | [optional] 
 **real_name** | **str**| The Subaccount user&#39;s name.  * A first name. * A last name. * A first name and last name. * An empty string. | [optional] 
 **services_email_enabled** | **int**| Whether to grant the Subaccount email access.  * &#x60;1&#x60; - Can access. * &#x60;0&#x60; - **Cannot** access. | [optional] [default to 0]
 **services_email_quota** | **int**| The maximum amount of disk space, in megabytes (MB), that the subaccount&#39;s email account may use.  If you do not declare a value, the system defaults to the defined system value.  **Note:**   This value **cannot** be greater than the maximum email quota.  * &#x60;0&#x60; or &#x60;unlimited&#x60; - The subaccount possesses unlimited disk space. | [optional] 
 **services_ftp_enabled** | **int**| Whether to grant the Subaccount FTP access.  * &#x60;1&#x60; - Can access. * &#x60;0&#x60; - **Cannot** access. | [optional] [default to 0]
 **services_ftp_homedir** | **str**| The Subaccount&#39;s FTP home directory.  **Note:**   This parameter is **required** if you enable FTP access.  A relative path from the cPanel account&#39;s home directory.  **Note:**   The specified directory **must** exist. | [optional] 
 **services_webdisk_enabled** | **int**| Whether to grant the Subaccount Web Disk access.  * &#x60;1&#x60; - Can access. * &#x60;0&#x60; - **Cannot** access. | [optional] [default to 0]
 **services_webdisk_enabledigest** | **int**| Whether to enable Web Disk digest authentication.  **Notes:**   * **Only** enable Digest Authentication for clients that require additional compatibility support on certain versions of Windows® operating systems. This compatibility support is **only** required on servers that use a self-signed certificate for the &#x60;cpsrvd&#x60; and &#x60;cpdavd&#x60; daemons.  * We recommend that you do **not** use Digest Authentication.   * &#x60;1&#x60; - Enabled * &#x60;0&#x60; - Disabled. | [optional] [default to 0]
 **services_webdisk_homedir** | **str**| The Subaccount&#39;s Web Disk home directory.  **Note:**   This parameter is **required** if you enable Web Disk access.  A relative path from the cPanel account&#39;s home directory. | [optional] 
 **services_webdisk_perms** | **str**| Whether to grant write permissions to the Subaccount.  **Note:**   The &#x60;services.webdisk.homedir&#x60; parameter determines the Subaccount&#39;s Web Disk home directory.  * &#x60;ro&#x60; - Read-only permissions. * &#x60;rw&#x60; - Read and write permissions. | [optional] [default to rw]
 **services_webdisk_private** | **int**| Whether to set the Web Disk directory&#39;s permissions to public or private.  * &#x60;1&#x60; - Private (&#x60;0700&#x60;). * &#x60;0&#x60; - Public (&#x60;0755&#x60;). | [optional] [default to 0]
 **type** | **str**| The type of account.  * &#x60;sub&#x60; - A Subaccount. | [optional] [default to sub]

### Return type

[**InlineResponse200531**](InlineResponse200531.md)

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

# **lookup_service_account**
> InlineResponse200533 lookup_service_account(full_username, type)

Return service account's information

This function lists a service account's information.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200533 import InlineResponse200533
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
    api_instance = clientapi_cpanel.UserManagerApi(api_client)
    full_username = 'username@example.com' # str | The full username for the system account.
    type = 'email' # str | The type of system account. * `email` * `ftp` * `webdisk`

    try:
        # Return service account's information
        api_response = api_instance.lookup_service_account(full_username, type)
        print("The response of UserManagerApi->lookup_service_account:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserManagerApi->lookup_service_account: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **full_username** | **str**| The full username for the system account. | 
 **type** | **str**| The type of system account. * &#x60;email&#x60; * &#x60;ftp&#x60; * &#x60;webdisk&#x60; | 

### Return type

[**InlineResponse200533**](InlineResponse200533.md)

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

# **lookup_user**
> InlineResponse200534 lookup_user(guid)

Return Subaccount's information

This function lists a single Subaccount's information.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200534 import InlineResponse200534
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
    api_instance = clientapi_cpanel.UserManagerApi(api_client)
    guid = 'EXAMPLE1:EXAMPLE.COM:564CD663%3AFE50072F2620B50988EA4E5F46022546FBE6BDDE3C36C2F2534F4967C661EC37' # str | The Subaccount's unique identifier.

    try:
        # Return Subaccount's information
        api_response = api_instance.lookup_user(guid)
        print("The response of UserManagerApi->lookup_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserManagerApi->lookup_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guid** | **str**| The Subaccount&#39;s unique identifier. | 

### Return type

[**InlineResponse200534**](InlineResponse200534.md)

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

# **merge_service_account**
> InlineResponse200535 merge_service_account(domain, username, services_email_merge=services_email_merge, services_ftp_merge=services_ftp_merge, services_webdisk_merge=services_webdisk_merge)

Register service account to Subaccount

This function links service accounts to subaccounts and creates a subaccount if one does not exist.

**Note:**

You can only link email, FTP, or Web Disk accounts.

**Important**

You must use at least **one** of the following parameters:

* services.email.merge
* services.ftp.merge
* services.webdisk.merge

To link multiple service accounts, the service accounts **must** share the same username and domain.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200535 import InlineResponse200535
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
    api_instance = clientapi_cpanel.UserManagerApi(api_client)
    domain = 'example.com' # str | The service account's associated domain.
    username = 'example' # str | The username for the service account that meets the account name limitations.  * Length - 64 characters * Characters — `a-z`, `A-Z`, `0-9`, dot (`.`), hyphen (`-`), underscore (`_`).  **Note:**  This value does **not** include the domain name.
    services_email_merge = 0 # int | Whether to link the email account to the subaccount.  * `1` - Merge. * `0` - Do **not** merge. (optional) (default to 0)
    services_ftp_merge = 0 # int | Whether to link the FTP account to the subaccount.  * `1` - Merge. * `0` - Do **not** merge. (optional) (default to 0)
    services_webdisk_merge = 0 # int | Whether to link the Web Disk account to the subaccount.  * `1` - Merge. * `0` - Do **not** merge. (optional) (default to 0)

    try:
        # Register service account to Subaccount
        api_response = api_instance.merge_service_account(domain, username, services_email_merge=services_email_merge, services_ftp_merge=services_ftp_merge, services_webdisk_merge=services_webdisk_merge)
        print("The response of UserManagerApi->merge_service_account:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserManagerApi->merge_service_account: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**| The service account&#39;s associated domain. | 
 **username** | **str**| The username for the service account that meets the account name limitations.  * Length - 64 characters * Characters — &#x60;a-z&#x60;, &#x60;A-Z&#x60;, &#x60;0-9&#x60;, dot (&#x60;.&#x60;), hyphen (&#x60;-&#x60;), underscore (&#x60;_&#x60;).  **Note:**  This value does **not** include the domain name. | 
 **services_email_merge** | **int**| Whether to link the email account to the subaccount.  * &#x60;1&#x60; - Merge. * &#x60;0&#x60; - Do **not** merge. | [optional] [default to 0]
 **services_ftp_merge** | **int**| Whether to link the FTP account to the subaccount.  * &#x60;1&#x60; - Merge. * &#x60;0&#x60; - Do **not** merge. | [optional] [default to 0]
 **services_webdisk_merge** | **int**| Whether to link the Web Disk account to the subaccount.  * &#x60;1&#x60; - Merge. * &#x60;0&#x60; - Do **not** merge. | [optional] [default to 0]

### Return type

[**InlineResponse200535**](InlineResponse200535.md)

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

# **unlink_service_account**
> InlineResponse200536 unlink_service_account(domain, service, username, dismiss=dismiss)

Unregister service account from Subaccount

This function unlinks a service account from a subaccount.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200536 import InlineResponse200536
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
    api_instance = clientapi_cpanel.UserManagerApi(api_client)
    domain = 'example.com' # str | The subaccount's associated domain.
    service = 'ftp' # str | The service to unlink.  * `email` * `ftp` * `webdisk`
    username = 'example' # str | The subaccount's username.  **Note:**  This value does **not** include the domain name.
    dismiss = 0 # int | Whether to dismiss the service account as a merge candidate. * `1` - Dismiss as merge candidate. * `0` - Display as merge candidate.  **Note:**   If any email, FTP, or Web Disk accounts use the same username, cPanel's [*User Manager*](https://go.cpanel.net/cpaneldocsUserManager) interface (*cPanel >> Home >> Preferences >> User Manager*) allows you to merge those accounts into a subaccount. (optional) (default to 0)

    try:
        # Unregister service account from Subaccount
        api_response = api_instance.unlink_service_account(domain, service, username, dismiss=dismiss)
        print("The response of UserManagerApi->unlink_service_account:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserManagerApi->unlink_service_account: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**| The subaccount&#39;s associated domain. | 
 **service** | **str**| The service to unlink.  * &#x60;email&#x60; * &#x60;ftp&#x60; * &#x60;webdisk&#x60; | 
 **username** | **str**| The subaccount&#39;s username.  **Note:**  This value does **not** include the domain name. | 
 **dismiss** | **int**| Whether to dismiss the service account as a merge candidate. * &#x60;1&#x60; - Dismiss as merge candidate. * &#x60;0&#x60; - Display as merge candidate.  **Note:**   If any email, FTP, or Web Disk accounts use the same username, cPanel&#39;s [*User Manager*](https://go.cpanel.net/cpaneldocsUserManager) interface (*cPanel &gt;&gt; Home &gt;&gt; Preferences &gt;&gt; User Manager*) allows you to merge those accounts into a subaccount. | [optional] [default to 0]

### Return type

[**InlineResponse200536**](InlineResponse200536.md)

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

# **user_manager_create_user**
> InlineResponse200528 user_manager_create_user(domain, password, username, alternate_email=alternate_email, avatar_url=avatar_url, phone_number=phone_number, real_name=real_name, send_invite=send_invite, services_email_enabled=services_email_enabled, services_email_quota=services_email_quota, services_email_send_welcome_email=services_email_send_welcome_email, services_ftp_enabled=services_ftp_enabled, services_ftp_homedir=services_ftp_homedir, services_webdisk_enabled=services_webdisk_enabled, services_webdisk_enabledigest=services_webdisk_enabledigest, services_webdisk_homedir=services_webdisk_homedir, services_webdisk_perms=services_webdisk_perms, services_webdisk_private=services_webdisk_private, type=type)

Create Subaccount

This function creates a Subaccount.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200528 import InlineResponse200528
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
    api_instance = clientapi_cpanel.UserManagerApi(api_client)
    domain = 'example.com' # str | The Subaccount user's associated domain that the cPanel account owns.
    password = '123456luggage' # str | The Subaccount's password.  **Note:**   Email, FTP, and Web Disk services use this password.
    username = 'example' # str | The username for the Subaccount. The username can only contain alphanumeric characters, dots (`.`), hyphens (`-`), and underscores (`_`).  **Note:**  This value does **not** include the domain name.
    alternate_email = 'user@example.com' # str | An alternate email address for the Subaccount's user.  **Note:**   You **must** use this parameter if you set the `send_invite` value to `1`. (optional)
    avatar_url = 'https://img.example.com/avatars/example.jpg' # str | The URL path to the user's Subaccount profile photo.  **Note:**  You **must** use the HTTPS protocol to prevent mixed content warnings when users view the image from another HTTPS URL.  **Warning:**  We reserved this parameter for future use. Do **not** use this parameter. (optional)
    phone_number = '+15551234567' # str | A phone number for the Subaccount user that conforms to [ITU-T](https://en.wikipedia.org/wiki/ITU-T)'s [E.164](https://en.wikipedia.org/wiki/E.164) standards.  **Warning:**  We reserved this parameter for future use. Do **not** use this parameter. (optional)
    real_name = 'John Doe' # str | The Subaccount user's first and/or last name. (optional)
    send_invite = 0 # int | Whether to send a reset password email to the Subaccount's alternate email address.  * `1` - Send. * `0` - Do not send. (optional) (default to 0)
    services_email_enabled = 0 # int | Whether to grant the Subaccount email access.  * `1` - Can access. * `0` - **Cannot** access. (optional) (default to 0)
    services_email_quota = '500' # str | The maximum amount of disk space, in megabytes (MB), allocated to Subaccount's email account.  * `0` or `unlimited` - The subaccount has unlimited disk space.  This value defaults to the defined system value.  **Note:**  This value **cannot** be larger than the system's maximum email quota. (optional)
    services_email_send_welcome_email = 0 # int | Whether to send client configuration instructions to the account.  * `1` - Send the instructions. * `0` - Do **not** send the instructions. (optional) (default to 0)
    services_ftp_enabled = 0 # int | Whether to grant the Subaccount FTP access.  * `1` - Can access. * `0` - **Cannot** access. (optional) (default to 0)
    services_ftp_homedir = '/Subaccount' # str | The Subaccount's FTP home directory, relative to the cPanel account's home directory.  **Note:**  * This parameter is **required** if you enabled the `services.ftp.homedir` parameter. * The directory **must** exist. (optional)
    services_webdisk_enabled = 0 # int | Whether to grant the Subaccount Web Disk access.  * `1` _ Can access. * `0` - **Cannot** access. (optional) (default to 0)
    services_webdisk_enabledigest = 0 # int | Whether to enable the Web Disk Digest Authentication.  * `1` - Enabled. * `0` - Disabled.  **Note:**  * **Only** enable Digest Authentication for clients that require additional compatibility support on   certain versions of Windows® operating systems. This compatibility support is **only** required on servers   that use a self-signed certificate for the `cpsrvd` and `cpdavd` daemons. * We recommend that you do **not** use Digest Authentication. (optional) (default to 0)
    services_webdisk_homedir = '/Subaccount' # str | The Subaccount's Web Disk home directory, relative to the cPanel account's home directory.  **Note:**  This parameter is **required** if you enable the `services.webdisk.enabled` parameter. (optional)
    services_webdisk_perms = 'rw' # str | The Subaccount's file permissions for its Web Disk home directory.  * `ro` - Read-only permissions. * `rw` - Read and write permissions.  **Note:**   The `services.webdisk.homedir` parameter determines the Subaccount's Web Disk home directory. (optional) (default to 'rw')
    services_webdisk_private = 0 # int | Whether to set the directory's permissions to public or private.  * `1` - Private (`0700`). * `0` - Public (`0755`). (optional) (default to 0)
    type = sub # str | The type of account.  * `sub` - A Subaccount. (optional) (default to sub)

    try:
        # Create Subaccount
        api_response = api_instance.user_manager_create_user(domain, password, username, alternate_email=alternate_email, avatar_url=avatar_url, phone_number=phone_number, real_name=real_name, send_invite=send_invite, services_email_enabled=services_email_enabled, services_email_quota=services_email_quota, services_email_send_welcome_email=services_email_send_welcome_email, services_ftp_enabled=services_ftp_enabled, services_ftp_homedir=services_ftp_homedir, services_webdisk_enabled=services_webdisk_enabled, services_webdisk_enabledigest=services_webdisk_enabledigest, services_webdisk_homedir=services_webdisk_homedir, services_webdisk_perms=services_webdisk_perms, services_webdisk_private=services_webdisk_private, type=type)
        print("The response of UserManagerApi->user_manager_create_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserManagerApi->user_manager_create_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**| The Subaccount user&#39;s associated domain that the cPanel account owns. | 
 **password** | **str**| The Subaccount&#39;s password.  **Note:**   Email, FTP, and Web Disk services use this password. | 
 **username** | **str**| The username for the Subaccount. The username can only contain alphanumeric characters, dots (&#x60;.&#x60;), hyphens (&#x60;-&#x60;), and underscores (&#x60;_&#x60;).  **Note:**  This value does **not** include the domain name. | 
 **alternate_email** | **str**| An alternate email address for the Subaccount&#39;s user.  **Note:**   You **must** use this parameter if you set the &#x60;send_invite&#x60; value to &#x60;1&#x60;. | [optional] 
 **avatar_url** | **str**| The URL path to the user&#39;s Subaccount profile photo.  **Note:**  You **must** use the HTTPS protocol to prevent mixed content warnings when users view the image from another HTTPS URL.  **Warning:**  We reserved this parameter for future use. Do **not** use this parameter. | [optional] 
 **phone_number** | **str**| A phone number for the Subaccount user that conforms to [ITU-T](https://en.wikipedia.org/wiki/ITU-T)&#39;s [E.164](https://en.wikipedia.org/wiki/E.164) standards.  **Warning:**  We reserved this parameter for future use. Do **not** use this parameter. | [optional] 
 **real_name** | **str**| The Subaccount user&#39;s first and/or last name. | [optional] 
 **send_invite** | **int**| Whether to send a reset password email to the Subaccount&#39;s alternate email address.  * &#x60;1&#x60; - Send. * &#x60;0&#x60; - Do not send. | [optional] [default to 0]
 **services_email_enabled** | **int**| Whether to grant the Subaccount email access.  * &#x60;1&#x60; - Can access. * &#x60;0&#x60; - **Cannot** access. | [optional] [default to 0]
 **services_email_quota** | **str**| The maximum amount of disk space, in megabytes (MB), allocated to Subaccount&#39;s email account.  * &#x60;0&#x60; or &#x60;unlimited&#x60; - The subaccount has unlimited disk space.  This value defaults to the defined system value.  **Note:**  This value **cannot** be larger than the system&#39;s maximum email quota. | [optional] 
 **services_email_send_welcome_email** | **int**| Whether to send client configuration instructions to the account.  * &#x60;1&#x60; - Send the instructions. * &#x60;0&#x60; - Do **not** send the instructions. | [optional] [default to 0]
 **services_ftp_enabled** | **int**| Whether to grant the Subaccount FTP access.  * &#x60;1&#x60; - Can access. * &#x60;0&#x60; - **Cannot** access. | [optional] [default to 0]
 **services_ftp_homedir** | **str**| The Subaccount&#39;s FTP home directory, relative to the cPanel account&#39;s home directory.  **Note:**  * This parameter is **required** if you enabled the &#x60;services.ftp.homedir&#x60; parameter. * The directory **must** exist. | [optional] 
 **services_webdisk_enabled** | **int**| Whether to grant the Subaccount Web Disk access.  * &#x60;1&#x60; _ Can access. * &#x60;0&#x60; - **Cannot** access. | [optional] [default to 0]
 **services_webdisk_enabledigest** | **int**| Whether to enable the Web Disk Digest Authentication.  * &#x60;1&#x60; - Enabled. * &#x60;0&#x60; - Disabled.  **Note:**  * **Only** enable Digest Authentication for clients that require additional compatibility support on   certain versions of Windows® operating systems. This compatibility support is **only** required on servers   that use a self-signed certificate for the &#x60;cpsrvd&#x60; and &#x60;cpdavd&#x60; daemons. * We recommend that you do **not** use Digest Authentication. | [optional] [default to 0]
 **services_webdisk_homedir** | **str**| The Subaccount&#39;s Web Disk home directory, relative to the cPanel account&#39;s home directory.  **Note:**  This parameter is **required** if you enable the &#x60;services.webdisk.enabled&#x60; parameter. | [optional] 
 **services_webdisk_perms** | **str**| The Subaccount&#39;s file permissions for its Web Disk home directory.  * &#x60;ro&#x60; - Read-only permissions. * &#x60;rw&#x60; - Read and write permissions.  **Note:**   The &#x60;services.webdisk.homedir&#x60; parameter determines the Subaccount&#39;s Web Disk home directory. | [optional] [default to &#39;rw&#39;]
 **services_webdisk_private** | **int**| Whether to set the directory&#39;s permissions to public or private.  * &#x60;1&#x60; - Private (&#x60;0700&#x60;). * &#x60;0&#x60; - Public (&#x60;0755&#x60;). | [optional] [default to 0]
 **type** | **str**| The type of account.  * &#x60;sub&#x60; - A Subaccount. | [optional] [default to sub]

### Return type

[**InlineResponse200528**](InlineResponse200528.md)

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

# **user_manager_delete_user**
> InlineResponse200529 user_manager_delete_user(domain, username)

Delete Subaccount

This function deletes a Subaccount. This function returns only metadata if no other service accounts exist with the same username and domain.
* If one service account uses the same username and domain, the function returns the service account's information.
* If two or more service accounts use the same username and domain, the function returns a hypothetical Subaccount.

**Note:**

* A hypothetical Subaccount consists of two or more service accounts that use the same username and domain.
* This function returns only metadata if the specified username and domain do **not** match any service accounts or hypothetical Subaccounts.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200529 import InlineResponse200529
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
    api_instance = clientapi_cpanel.UserManagerApi(api_client)
    domain = 'example.com' # str | The Subaccount's associated domain.  The domain **must** be one that the cPanel account owns.
    username = 'example' # str | The Subaccount's username. * Characters — `a-z`, `A-Z`, `0-9`, dot (`.`), hyphen (`-`), underscore (`_`)  **Note:**  This value does **not** include the domain name.

    try:
        # Delete Subaccount
        api_response = api_instance.user_manager_delete_user(domain, username)
        print("The response of UserManagerApi->user_manager_delete_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserManagerApi->user_manager_delete_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**| The Subaccount&#39;s associated domain.  The domain **must** be one that the cPanel account owns. | 
 **username** | **str**| The Subaccount&#39;s username. * Characters — &#x60;a-z&#x60;, &#x60;A-Z&#x60;, &#x60;0-9&#x60;, dot (&#x60;.&#x60;), hyphen (&#x60;-&#x60;), underscore (&#x60;_&#x60;)  **Note:**  This value does **not** include the domain name. | 

### Return type

[**InlineResponse200529**](InlineResponse200529.md)

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

# **user_manager_list_users**
> InlineResponse200532 user_manager_list_users(flat=flat)

Return cPanel account's Subaccounts

This function lists the cPanel account's Subaccounts.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200532 import InlineResponse200532
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
    api_instance = clientapi_cpanel.UserManagerApi(api_client)
    flat = 0 # int | Whether to return Subaccounts with the same name under the merge_candidates array. * `1` - Do **not** return. * `0` - Return. (optional) (default to 0)

    try:
        # Return cPanel account's Subaccounts
        api_response = api_instance.user_manager_list_users(flat=flat)
        print("The response of UserManagerApi->user_manager_list_users:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserManagerApi->user_manager_list_users: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **flat** | **int**| Whether to return Subaccounts with the same name under the merge_candidates array. * &#x60;1&#x60; - Do **not** return. * &#x60;0&#x60; - Return. | [optional] [default to 0]

### Return type

[**InlineResponse200532**](InlineResponse200532.md)

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

