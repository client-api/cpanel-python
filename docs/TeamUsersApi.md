# clientapi_cpanel.TeamUsersApi

All URIs are relative to *https://cpanel-server.tld:2083/execute*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_roles**](TeamUsersApi.md#add_roles) | **GET** /Team/add_roles | Add roles to a team user
[**add_team_user**](TeamUsersApi.md#add_team_user) | **GET** /Team/add_team_user | Add a team user
[**cancel_expire**](TeamUsersApi.md#cancel_expire) | **GET** /Team/cancel_expire | Stop a team user from expiring
[**edit_team_user**](TeamUsersApi.md#edit_team_user) | **GET** /Team/edit_team_user | Edit a team user
[**get_team_users_with_roles_count**](TeamUsersApi.md#get_team_users_with_roles_count) | **GET** /Team/get_team_users_with_roles_count | Get number of team users with roles
[**list_team**](TeamUsersApi.md#list_team) | **GET** /Team/list_team | List Team Users
[**password_reset_request**](TeamUsersApi.md#password_reset_request) | **GET** /Team/password_reset_request | Sends a password reset request link to team user.
[**reinstate_team_user**](TeamUsersApi.md#reinstate_team_user) | **GET** /Team/reinstate_team_user | Reinstate a team user
[**remove_roles**](TeamUsersApi.md#remove_roles) | **GET** /Team/remove_roles | Remove roles from a team user
[**remove_team_user**](TeamUsersApi.md#remove_team_user) | **GET** /Team/remove_team_user | Remove a team user
[**set_expire**](TeamUsersApi.md#set_expire) | **GET** /Team/set_expire | Set a team user to expire
[**set_roles**](TeamUsersApi.md#set_roles) | **GET** /Team/set_roles | Set roles for a team user
[**set_team_user_contact_email**](TeamUsersApi.md#set_team_user_contact_email) | **GET** /Team/set_contact_email | Set a contact email address for a team user
[**set_team_user_notes**](TeamUsersApi.md#set_team_user_notes) | **GET** /Team/set_notes | Set notes for a team user
[**set_team_user_password**](TeamUsersApi.md#set_team_user_password) | **GET** /Team/set_password | Set password for a team user
[**suspend_team_user**](TeamUsersApi.md#suspend_team_user) | **GET** /Team/suspend_team_user | Suspend a team user
[**team_set_locale**](TeamUsersApi.md#team_set_locale) | **GET** /Team/set_locale | Set locale for a team user


# **add_roles**
> InlineResponse200496 add_roles(role, user)

Add roles to a team user

This function adds roles to a team user.

**Note:**

  This action may result in team users gaining access to team owner level privileges.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200496 import InlineResponse200496
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
    api_instance = clientapi_cpanel.TeamUsersApi(api_client)
    role = 'database' # str | The role or roles to add to the team user. Current roles include admin, database, email, web.
    user = 'teamuser' # str | The username of the team user.

    try:
        # Add roles to a team user
        api_response = api_instance.add_roles(role, user)
        print("The response of TeamUsersApi->add_roles:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TeamUsersApi->add_roles: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role** | **str**| The role or roles to add to the team user. Current roles include admin, database, email, web. | 
 **user** | **str**| The username of the team user. | 

### Return type

[**InlineResponse200496**](InlineResponse200496.md)

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

# **add_team_user**
> InlineResponse200497 add_team_user(email1, user, activation_email=activation_email, email2=email2, expire_date=expire_date, expire_reason=expire_reason, notes=notes, password=password, roles=roles, services_email_enabled=services_email_enabled, services_email_quota=services_email_quota, services_ftp_enabled=services_ftp_enabled, services_ftp_homedir=services_ftp_homedir, services_webdisk_enabled=services_webdisk_enabled, services_webdisk_enabledigest=services_webdisk_enabledigest, services_webdisk_homedir=services_webdisk_homedir, services_webdisk_perms=services_webdisk_perms, services_webdisk_private=services_webdisk_private)

Add a team user

This function creates and adds a new team user.

**Note:**

  This action may result in team users gaining access to team owner level privileges.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200497 import InlineResponse200497
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
    api_instance = clientapi_cpanel.TeamUsersApi(api_client)
    email1 = 'teamuser@example.com' # str | The contact email for the new team user.
    user = 'teamuser' # str | The username of the team user. Follows cPanel standards.
    activation_email = 1 # int | Send an email to the team user that allows them to set their own password. * `1` - Enabled.  **Note:**   * You must pass either the `password` or `activation_email` parameter. (optional)
    email2 = 'teamuser-backup@example.com' # str | The secondary email for the new team user. (optional)
    expire_date = clientapi_cpanel.ExpireDate() # ExpireDate | The epoch time on which the team user account expires, or the offset from the current time, in days. Integers are treated as Unix Epoch Time unless followed by 'days'. (optional)
    expire_reason = 'teamUser gave a two week notice.' # str | The reason for expiration. (optional)
    notes = 'This is a note about teamuser' # str | Notes about the new team user. This field should not contain private information. Maximum of 100 characters. (optional)
    password = 'securepassword' # str | The password to set for the new team user.  **Note:**   * You must pass either the `password` or `activation_email` parameter. (optional)
    roles = 'email,database' # str | A comma-separated list of roles assigned to the new team user. Current roles include admin, database, email, web. (optional)
    services_email_enabled = 0 # int | Whether to create an email subaccount for the team user. A subaccount is always created for a team user, but it does not have any associated service subaccounts by default.  * `1` - Create an email subaccount. * `0` - **Do Not** create an email subaccount. (optional) (default to 0)
    services_email_quota = '500' # str | The maximum amount of disk space, in megabytes (MB), allocated to the team user's email account.  * `0` or `unlimited` - The subaccount has unlimited disk space.  This value defaults to the defined system value.  **Note:**  This value **cannot** be larger than the system's maximum email quota. (optional)
    services_ftp_enabled = 0 # int | Whether to create an FTP subaccount for the team user. A subaccount is always created for a team user, but it does not have any associated service subaccounts by default.  * `1` - Create an FTP subaccount. * `0` - **Do Not** create an FTP subaccount. (optional) (default to 0)
    services_ftp_homedir = '/Teamusername' # str | The team user's FTP home directory, relative to the cPanel account's home directory.  **Note:**  * This parameter is **required** if you enabled the `services.ftp.homedir` parameter. * The directory **must** exist. (optional)
    services_webdisk_enabled = 0 # int | Whether to create a Web Disk subaccount for the team user. A subaccount is always created for a team user, but it does not have any associated service subaccounts by default.  * `1` - Create a Web Disk subaccount. * `0` - **Do Not** create a Web Disk subaccount. (optional) (default to 0)
    services_webdisk_enabledigest = 0 # int | Whether to enable the Web Disk Digest Authentication.  * `1` - Enabled. * `0` - Disabled.  **Note:**  * **Only** enable Digest Authentication for clients that require additional compatibility support on   certain versions of Windows® operating systems. This compatibility support is **only** required on servers   that use a self-signed certificate for the `cpsrvd` and `cpdavd` daemons. * We recommend that you do **not** use Digest Authentication. (optional) (default to 0)
    services_webdisk_homedir = '/Teamusername' # str | The team user's Web Disk home directory, relative to the cPanel account's home directory.  **Note:**  This parameter is **required** if you enable the `services.webdisk.enabled` parameter. (optional)
    services_webdisk_perms = 'rw' # str | The team user's file permissions for its Web Disk home directory.  * `ro` - Read-only permissions. * `rw` - Read and write permissions.  **Note:**   The `services.webdisk.homedir` parameter determines the team user's Web Disk home directory. (optional) (default to 'rw')
    services_webdisk_private = 0 # int | Whether to set the directory's permissions to public or private.  * `1` - Private (`0700`). * `0` - Public (`0755`). (optional) (default to 0)

    try:
        # Add a team user
        api_response = api_instance.add_team_user(email1, user, activation_email=activation_email, email2=email2, expire_date=expire_date, expire_reason=expire_reason, notes=notes, password=password, roles=roles, services_email_enabled=services_email_enabled, services_email_quota=services_email_quota, services_ftp_enabled=services_ftp_enabled, services_ftp_homedir=services_ftp_homedir, services_webdisk_enabled=services_webdisk_enabled, services_webdisk_enabledigest=services_webdisk_enabledigest, services_webdisk_homedir=services_webdisk_homedir, services_webdisk_perms=services_webdisk_perms, services_webdisk_private=services_webdisk_private)
        print("The response of TeamUsersApi->add_team_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TeamUsersApi->add_team_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email1** | **str**| The contact email for the new team user. | 
 **user** | **str**| The username of the team user. Follows cPanel standards. | 
 **activation_email** | **int**| Send an email to the team user that allows them to set their own password. * &#x60;1&#x60; - Enabled.  **Note:**   * You must pass either the &#x60;password&#x60; or &#x60;activation_email&#x60; parameter. | [optional] 
 **email2** | **str**| The secondary email for the new team user. | [optional] 
 **expire_date** | [**ExpireDate**](.md)| The epoch time on which the team user account expires, or the offset from the current time, in days. Integers are treated as Unix Epoch Time unless followed by &#39;days&#39;. | [optional] 
 **expire_reason** | **str**| The reason for expiration. | [optional] 
 **notes** | **str**| Notes about the new team user. This field should not contain private information. Maximum of 100 characters. | [optional] 
 **password** | **str**| The password to set for the new team user.  **Note:**   * You must pass either the &#x60;password&#x60; or &#x60;activation_email&#x60; parameter. | [optional] 
 **roles** | **str**| A comma-separated list of roles assigned to the new team user. Current roles include admin, database, email, web. | [optional] 
 **services_email_enabled** | **int**| Whether to create an email subaccount for the team user. A subaccount is always created for a team user, but it does not have any associated service subaccounts by default.  * &#x60;1&#x60; - Create an email subaccount. * &#x60;0&#x60; - **Do Not** create an email subaccount. | [optional] [default to 0]
 **services_email_quota** | **str**| The maximum amount of disk space, in megabytes (MB), allocated to the team user&#39;s email account.  * &#x60;0&#x60; or &#x60;unlimited&#x60; - The subaccount has unlimited disk space.  This value defaults to the defined system value.  **Note:**  This value **cannot** be larger than the system&#39;s maximum email quota. | [optional] 
 **services_ftp_enabled** | **int**| Whether to create an FTP subaccount for the team user. A subaccount is always created for a team user, but it does not have any associated service subaccounts by default.  * &#x60;1&#x60; - Create an FTP subaccount. * &#x60;0&#x60; - **Do Not** create an FTP subaccount. | [optional] [default to 0]
 **services_ftp_homedir** | **str**| The team user&#39;s FTP home directory, relative to the cPanel account&#39;s home directory.  **Note:**  * This parameter is **required** if you enabled the &#x60;services.ftp.homedir&#x60; parameter. * The directory **must** exist. | [optional] 
 **services_webdisk_enabled** | **int**| Whether to create a Web Disk subaccount for the team user. A subaccount is always created for a team user, but it does not have any associated service subaccounts by default.  * &#x60;1&#x60; - Create a Web Disk subaccount. * &#x60;0&#x60; - **Do Not** create a Web Disk subaccount. | [optional] [default to 0]
 **services_webdisk_enabledigest** | **int**| Whether to enable the Web Disk Digest Authentication.  * &#x60;1&#x60; - Enabled. * &#x60;0&#x60; - Disabled.  **Note:**  * **Only** enable Digest Authentication for clients that require additional compatibility support on   certain versions of Windows® operating systems. This compatibility support is **only** required on servers   that use a self-signed certificate for the &#x60;cpsrvd&#x60; and &#x60;cpdavd&#x60; daemons. * We recommend that you do **not** use Digest Authentication. | [optional] [default to 0]
 **services_webdisk_homedir** | **str**| The team user&#39;s Web Disk home directory, relative to the cPanel account&#39;s home directory.  **Note:**  This parameter is **required** if you enable the &#x60;services.webdisk.enabled&#x60; parameter. | [optional] 
 **services_webdisk_perms** | **str**| The team user&#39;s file permissions for its Web Disk home directory.  * &#x60;ro&#x60; - Read-only permissions. * &#x60;rw&#x60; - Read and write permissions.  **Note:**   The &#x60;services.webdisk.homedir&#x60; parameter determines the team user&#39;s Web Disk home directory. | [optional] [default to &#39;rw&#39;]
 **services_webdisk_private** | **int**| Whether to set the directory&#39;s permissions to public or private.  * &#x60;1&#x60; - Private (&#x60;0700&#x60;). * &#x60;0&#x60; - Public (&#x60;0755&#x60;). | [optional] [default to 0]

### Return type

[**InlineResponse200497**](InlineResponse200497.md)

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

# **cancel_expire**
> InlineResponse200498 cancel_expire(user)

Stop a team user from expiring

This function stops a team user from expiring.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200498 import InlineResponse200498
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
    api_instance = clientapi_cpanel.TeamUsersApi(api_client)
    user = 'teamUser' # str | The username of the team user.

    try:
        # Stop a team user from expiring
        api_response = api_instance.cancel_expire(user)
        print("The response of TeamUsersApi->cancel_expire:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TeamUsersApi->cancel_expire: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | **str**| The username of the team user. | 

### Return type

[**InlineResponse200498**](InlineResponse200498.md)

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

# **edit_team_user**
> InlineResponse200499 edit_team_user(user, add_role=add_role, email1=email1, email2=email2, expire_reason=expire_reason, notes=notes, password=password, remove_role=remove_role, services_email_enabled=services_email_enabled, services_email_quota=services_email_quota, services_ftp_enabled=services_ftp_enabled, services_ftp_homedir=services_ftp_homedir, services_webdisk_enabled=services_webdisk_enabled, services_webdisk_enabledigest=services_webdisk_enabledigest, services_webdisk_homedir=services_webdisk_homedir, services_webdisk_perms=services_webdisk_perms, services_webdisk_private=services_webdisk_private, set_expire=set_expire, set_role=set_role)

Edit a team user

This function modifies a team user.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200499 import InlineResponse200499
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
    api_instance = clientapi_cpanel.TeamUsersApi(api_client)
    user = 'teamUser' # str | The username of the team user.
    add_role = 'database' # str | The role or roles to add to the team user. (optional)
    email1 = 'teamuser@example.com' # str | The primary contact email address to set for the team user. (optional)
    email2 = 'teamuser@example.com' # str | The secondary contact email address to set for the team user. (optional)
    expire_reason = 'teamUser gave a two week notice.' # str | The reason for expiration. (optional)
    notes = 'This is a note about teamUser' # str | Notes about the new team user. This field should not contain private information. (optional)
    password = 'securepassword' # str | The password to set for the team user. (optional)
    remove_role = 'database' # str | The role or roles to remove from the team user. (optional)
    services_email_enabled = 0 # int | Whether to create or remove an email subaccount for the team user. A subaccount is always created for a team user, but it does not have any associated service subaccounts by default.  * `1` - Create and associate an email subaccount. * `0` - Remove any associated email subaccounts. (optional) (default to 0)
    services_email_quota = '500' # str | The maximum amount of disk space, in megabytes (MB), allocated to the team user's email account.  * `0` or `unlimited` - The subaccount has unlimited disk space.  This value defaults to the defined system value.  **Note:**  This value **cannot** be larger than the system's maximum email quota. (optional)
    services_ftp_enabled = 0 # int | Whether to create or remove an FTP subaccount for the team user. A subaccount is always created for a team user, but it does not have any associated service subaccounts by default.  * `1` - Create and associate an FTP subaccount. * `0` - Remove any associated FTP subaccounts. (optional) (default to 0)
    services_ftp_homedir = '/Teamusername' # str | The team user's FTP home directory, relative to the cPanel account's home directory.  **Note:**  * This parameter is **required** if you enabled the `services.ftp.homedir` parameter. * The directory **must** exist. (optional)
    services_webdisk_enabled = 0 # int | Whether to create or remove a Web Disk subaccount for the team user. A subaccount is always created for a team user, but it does not have any associated service subaccounts by default.  * `1` - Create and associate a Web Disk subaccount. * `0` - Remove any associated Web Disk subaccounts. (optional) (default to 0)
    services_webdisk_enabledigest = 0 # int | Whether to enable the Web Disk Digest Authentication.  * `1` - Enabled. * `0` - Disabled.  **Note:**  * **Only** enable Digest Authentication for clients that require additional compatibility support on   certain versions of Windows® operating systems. This compatibility support is **only** required on servers   that use a self-signed certificate for the `cpsrvd` and `cpdavd` daemons. * We recommend that you do **not** use Digest Authentication. (optional) (default to 0)
    services_webdisk_homedir = '/Teamusername' # str | The team user's Web Disk home directory, relative to the cPanel account's home directory.  **Note:**  This parameter is **required** if you enable the `services.webdisk.enabled` parameter. (optional)
    services_webdisk_perms = 'rw' # str | The team user's file permissions for its Web Disk home directory.  * `ro` - Read-only permissions. * `rw` - Read and write permissions.  **Note:**   The `services.webdisk.homedir` parameter determines the team user's Web Disk home directory. (optional) (default to 'rw')
    services_webdisk_private = 0 # int | Whether to set the directory's permissions to public or private.  * `1` - Private (`0700`). * `0` - Public (`0755`). (optional) (default to 0)
    set_expire = clientapi_cpanel.SetExpire() # SetExpire | The epoch time the team user account expires on or the offset in days. (optional)
    set_role = 'email' # str | The role or roles to set for the team user. (optional)

    try:
        # Edit a team user
        api_response = api_instance.edit_team_user(user, add_role=add_role, email1=email1, email2=email2, expire_reason=expire_reason, notes=notes, password=password, remove_role=remove_role, services_email_enabled=services_email_enabled, services_email_quota=services_email_quota, services_ftp_enabled=services_ftp_enabled, services_ftp_homedir=services_ftp_homedir, services_webdisk_enabled=services_webdisk_enabled, services_webdisk_enabledigest=services_webdisk_enabledigest, services_webdisk_homedir=services_webdisk_homedir, services_webdisk_perms=services_webdisk_perms, services_webdisk_private=services_webdisk_private, set_expire=set_expire, set_role=set_role)
        print("The response of TeamUsersApi->edit_team_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TeamUsersApi->edit_team_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | **str**| The username of the team user. | 
 **add_role** | **str**| The role or roles to add to the team user. | [optional] 
 **email1** | **str**| The primary contact email address to set for the team user. | [optional] 
 **email2** | **str**| The secondary contact email address to set for the team user. | [optional] 
 **expire_reason** | **str**| The reason for expiration. | [optional] 
 **notes** | **str**| Notes about the new team user. This field should not contain private information. | [optional] 
 **password** | **str**| The password to set for the team user. | [optional] 
 **remove_role** | **str**| The role or roles to remove from the team user. | [optional] 
 **services_email_enabled** | **int**| Whether to create or remove an email subaccount for the team user. A subaccount is always created for a team user, but it does not have any associated service subaccounts by default.  * &#x60;1&#x60; - Create and associate an email subaccount. * &#x60;0&#x60; - Remove any associated email subaccounts. | [optional] [default to 0]
 **services_email_quota** | **str**| The maximum amount of disk space, in megabytes (MB), allocated to the team user&#39;s email account.  * &#x60;0&#x60; or &#x60;unlimited&#x60; - The subaccount has unlimited disk space.  This value defaults to the defined system value.  **Note:**  This value **cannot** be larger than the system&#39;s maximum email quota. | [optional] 
 **services_ftp_enabled** | **int**| Whether to create or remove an FTP subaccount for the team user. A subaccount is always created for a team user, but it does not have any associated service subaccounts by default.  * &#x60;1&#x60; - Create and associate an FTP subaccount. * &#x60;0&#x60; - Remove any associated FTP subaccounts. | [optional] [default to 0]
 **services_ftp_homedir** | **str**| The team user&#39;s FTP home directory, relative to the cPanel account&#39;s home directory.  **Note:**  * This parameter is **required** if you enabled the &#x60;services.ftp.homedir&#x60; parameter. * The directory **must** exist. | [optional] 
 **services_webdisk_enabled** | **int**| Whether to create or remove a Web Disk subaccount for the team user. A subaccount is always created for a team user, but it does not have any associated service subaccounts by default.  * &#x60;1&#x60; - Create and associate a Web Disk subaccount. * &#x60;0&#x60; - Remove any associated Web Disk subaccounts. | [optional] [default to 0]
 **services_webdisk_enabledigest** | **int**| Whether to enable the Web Disk Digest Authentication.  * &#x60;1&#x60; - Enabled. * &#x60;0&#x60; - Disabled.  **Note:**  * **Only** enable Digest Authentication for clients that require additional compatibility support on   certain versions of Windows® operating systems. This compatibility support is **only** required on servers   that use a self-signed certificate for the &#x60;cpsrvd&#x60; and &#x60;cpdavd&#x60; daemons. * We recommend that you do **not** use Digest Authentication. | [optional] [default to 0]
 **services_webdisk_homedir** | **str**| The team user&#39;s Web Disk home directory, relative to the cPanel account&#39;s home directory.  **Note:**  This parameter is **required** if you enable the &#x60;services.webdisk.enabled&#x60; parameter. | [optional] 
 **services_webdisk_perms** | **str**| The team user&#39;s file permissions for its Web Disk home directory.  * &#x60;ro&#x60; - Read-only permissions. * &#x60;rw&#x60; - Read and write permissions.  **Note:**   The &#x60;services.webdisk.homedir&#x60; parameter determines the team user&#39;s Web Disk home directory. | [optional] [default to &#39;rw&#39;]
 **services_webdisk_private** | **int**| Whether to set the directory&#39;s permissions to public or private.  * &#x60;1&#x60; - Private (&#x60;0700&#x60;). * &#x60;0&#x60; - Public (&#x60;0755&#x60;). | [optional] [default to 0]
 **set_expire** | [**SetExpire**](.md)| The epoch time the team user account expires on or the offset in days. | [optional] 
 **set_role** | **str**| The role or roles to set for the team user. | [optional] 

### Return type

[**InlineResponse200499**](InlineResponse200499.md)

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

# **get_team_users_with_roles_count**
> InlineResponse200500 get_team_users_with_roles_count()

Get number of team users with roles

This function returns the current and maximum number of team users with roles.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200500 import InlineResponse200500
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
    api_instance = clientapi_cpanel.TeamUsersApi(api_client)

    try:
        # Get number of team users with roles
        api_response = api_instance.get_team_users_with_roles_count()
        print("The response of TeamUsersApi->get_team_users_with_roles_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TeamUsersApi->get_team_users_with_roles_count: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**InlineResponse200500**](InlineResponse200500.md)

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

# **list_team**
> InlineResponse200501 list_team(format=format)

List Team Users

This function lists the team users connected to a cPanel account.
This list is given in an array by default, but can be given in a hash.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200501 import InlineResponse200501
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
    api_instance = clientapi_cpanel.TeamUsersApi(api_client)
    format = 'array' # str | The format in which the team data is listed. (optional)

    try:
        # List Team Users
        api_response = api_instance.list_team(format=format)
        print("The response of TeamUsersApi->list_team:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TeamUsersApi->list_team: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | **str**| The format in which the team data is listed. | [optional] 

### Return type

[**InlineResponse200501**](InlineResponse200501.md)

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

# **password_reset_request**
> InlineResponse200502 password_reset_request(user)

Sends a password reset request link to team user.

This function enables a team user to reset the password by sending a password reset request link.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200502 import InlineResponse200502
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
    api_instance = clientapi_cpanel.TeamUsersApi(api_client)
    user = 'teamuser' # str | The username of the team user.

    try:
        # Sends a password reset request link to team user.
        api_response = api_instance.password_reset_request(user)
        print("The response of TeamUsersApi->password_reset_request:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TeamUsersApi->password_reset_request: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | **str**| The username of the team user. | 

### Return type

[**InlineResponse200502**](InlineResponse200502.md)

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

# **reinstate_team_user**
> InlineResponse200503 reinstate_team_user(user)

Reinstate a team user

This function reinstates a team user by removing any suspended or expired statuses. The reason field is also cleared.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200503 import InlineResponse200503
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
    api_instance = clientapi_cpanel.TeamUsersApi(api_client)
    user = 'teamUser' # str | The username of the team user.

    try:
        # Reinstate a team user
        api_response = api_instance.reinstate_team_user(user)
        print("The response of TeamUsersApi->reinstate_team_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TeamUsersApi->reinstate_team_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | **str**| The username of the team user. | 

### Return type

[**InlineResponse200503**](InlineResponse200503.md)

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

# **remove_roles**
> InlineResponse200504 remove_roles(role, user)

Remove roles from a team user

This function removes roles from a team user.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200504 import InlineResponse200504
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
    api_instance = clientapi_cpanel.TeamUsersApi(api_client)
    role = 'database' # str | The role or roles to remove from the team user.
    user = 'teamuser' # str | The username of the team user.

    try:
        # Remove roles from a team user
        api_response = api_instance.remove_roles(role, user)
        print("The response of TeamUsersApi->remove_roles:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TeamUsersApi->remove_roles: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role** | **str**| The role or roles to remove from the team user. | 
 **user** | **str**| The username of the team user. | 

### Return type

[**InlineResponse200504**](InlineResponse200504.md)

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

# **remove_team_user**
> InlineResponse200505 remove_team_user(user)

Remove a team user

This function removes a team user.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200505 import InlineResponse200505
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
    api_instance = clientapi_cpanel.TeamUsersApi(api_client)
    user = 'teamuser' # str | The username of the team user.

    try:
        # Remove a team user
        api_response = api_instance.remove_team_user(user)
        print("The response of TeamUsersApi->remove_team_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TeamUsersApi->remove_team_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | **str**| The username of the team user. | 

### Return type

[**InlineResponse200505**](InlineResponse200505.md)

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

# **set_expire**
> InlineResponse200507 set_expire(var_date, user, reason=reason)

Set a team user to expire

This function expires a team user after a specified amount of time.

If the team user already has an expire date set, it's replaced with a new date and reason.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200507 import InlineResponse200507
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
    api_instance = clientapi_cpanel.TeamUsersApi(api_client)
    var_date = clientapi_cpanel.ModelDate() # ModelDate | The epoch time on which the team user account expires, or the offset from the current time, in days. Integers are treated as Unix Epoch Time unless followed by 'days'.
    user = 'teamUser' # str | The username of the team user.
    reason = 'teamUser gave a two week notice.' # str | The reason for expiration. (optional)

    try:
        # Set a team user to expire
        api_response = api_instance.set_expire(var_date, user, reason=reason)
        print("The response of TeamUsersApi->set_expire:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TeamUsersApi->set_expire: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **var_date** | [**ModelDate**](.md)| The epoch time on which the team user account expires, or the offset from the current time, in days. Integers are treated as Unix Epoch Time unless followed by &#39;days&#39;. | 
 **user** | **str**| The username of the team user. | 
 **reason** | **str**| The reason for expiration. | [optional] 

### Return type

[**InlineResponse200507**](InlineResponse200507.md)

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

# **set_roles**
> InlineResponse200511 set_roles(user, role=role)

Set roles for a team user

This function sets roles for a team user.

**Note:**

  This action may result in team users gaining access to team owner level privileges.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200511 import InlineResponse200511
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
    api_instance = clientapi_cpanel.TeamUsersApi(api_client)
    user = 'teamuser' # str | The username of the team user.
    role = 'database' # str | The role or roles to set for the team user. Current roles include admin, database, email, web. (optional)

    try:
        # Set roles for a team user
        api_response = api_instance.set_roles(user, role=role)
        print("The response of TeamUsersApi->set_roles:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TeamUsersApi->set_roles: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | **str**| The username of the team user. | 
 **role** | **str**| The role or roles to set for the team user. Current roles include admin, database, email, web. | [optional] 

### Return type

[**InlineResponse200511**](InlineResponse200511.md)

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

# **set_team_user_contact_email**
> InlineResponse200506 set_team_user_contact_email(user, email1=email1, email2=email2)

Set a contact email address for a team user

This function sets or changes primary and secondary email addresses.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200506 import InlineResponse200506
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
    api_instance = clientapi_cpanel.TeamUsersApi(api_client)
    user = 'teamUser' # str | The username of the team user.
    email1 = 'email1@example.com' # str | The primary contact email address to set for the team user. (optional)
    email2 = 'email2@example.com' # str | The secondary contact email address to set for the team user. (optional)

    try:
        # Set a contact email address for a team user
        api_response = api_instance.set_team_user_contact_email(user, email1=email1, email2=email2)
        print("The response of TeamUsersApi->set_team_user_contact_email:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TeamUsersApi->set_team_user_contact_email: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | **str**| The username of the team user. | 
 **email1** | **str**| The primary contact email address to set for the team user. | [optional] 
 **email2** | **str**| The secondary contact email address to set for the team user. | [optional] 

### Return type

[**InlineResponse200506**](InlineResponse200506.md)

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

# **set_team_user_notes**
> InlineResponse200509 set_team_user_notes(notes, user)

Set notes for a team user

This function replaces the current notes field with new text.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200509 import InlineResponse200509
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
    api_instance = clientapi_cpanel.TeamUsersApi(api_client)
    notes = 'teamUser is a good employee' # str | The content of the notes field.
    user = 'teamUser' # str | The username of the team user.

    try:
        # Set notes for a team user
        api_response = api_instance.set_team_user_notes(notes, user)
        print("The response of TeamUsersApi->set_team_user_notes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TeamUsersApi->set_team_user_notes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **notes** | **str**| The content of the notes field. | 
 **user** | **str**| The username of the team user. | 

### Return type

[**InlineResponse200509**](InlineResponse200509.md)

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

# **set_team_user_password**
> InlineResponse200510 set_team_user_password(password, user)

Set password for a team user

This function replaces the current password with a new one.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200510 import InlineResponse200510
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
    api_instance = clientapi_cpanel.TeamUsersApi(api_client)
    password = 'securepassword' # str | The password to set for the team user.
    user = 'teamuser' # str | The username of the team user.

    try:
        # Set password for a team user
        api_response = api_instance.set_team_user_password(password, user)
        print("The response of TeamUsersApi->set_team_user_password:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TeamUsersApi->set_team_user_password: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **password** | **str**| The password to set for the team user. | 
 **user** | **str**| The username of the team user. | 

### Return type

[**InlineResponse200510**](InlineResponse200510.md)

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

# **suspend_team_user**
> InlineResponse200512 suspend_team_user(user, reason=reason)

Suspend a team user

This function immediately suspends a team user.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200512 import InlineResponse200512
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
    api_instance = clientapi_cpanel.TeamUsersApi(api_client)
    user = 'teamuser' # str | The username of the team user.
    reason = 'teamuser is on vacation' # str | The reason for suspension. (optional)

    try:
        # Suspend a team user
        api_response = api_instance.suspend_team_user(user, reason=reason)
        print("The response of TeamUsersApi->suspend_team_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TeamUsersApi->suspend_team_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | **str**| The username of the team user. | 
 **reason** | **str**| The reason for suspension. | [optional] 

### Return type

[**InlineResponse200512**](InlineResponse200512.md)

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

# **team_set_locale**
> InlineResponse200508 team_set_locale(locale, user)

Set locale for a team user

This function sets locale for a team user.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200508 import InlineResponse200508
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
    api_instance = clientapi_cpanel.TeamUsersApi(api_client)
    locale = 'es_es' # str | The new locale for the team user.
    user = 'teamuser' # str | The username of the team user.

    try:
        # Set locale for a team user
        api_response = api_instance.team_set_locale(locale, user)
        print("The response of TeamUsersApi->team_set_locale:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TeamUsersApi->team_set_locale: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **locale** | **str**| The new locale for the team user. | 
 **user** | **str**| The username of the team user. | 

### Return type

[**InlineResponse200508**](InlineResponse200508.md)

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

