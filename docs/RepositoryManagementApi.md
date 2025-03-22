# clientapi_cpanel.RepositoryManagementApi

All URIs are relative to *https://cpanel-server.tld:2083/execute*

Method | HTTP request | Description
------------- | ------------- | -------------
[**version_control_create**](RepositoryManagementApi.md#version_control_create) | **GET** /VersionControl/create | Create Git repository
[**version_control_delete**](RepositoryManagementApi.md#version_control_delete) | **GET** /VersionControl/delete | Delete Git repository
[**version_control_retrieve**](RepositoryManagementApi.md#version_control_retrieve) | **GET** /VersionControl/retrieve | Return Git repositories
[**version_control_update**](RepositoryManagementApi.md#version_control_update) | **GET** /VersionControl/update | Update Git repository settings


# **version_control_create**
> InlineResponse200542 version_control_create(name, repository_root, type, source_repository=source_repository)

Create Git repository

This function creates a new Git™ repository on a cPanel account.

* For more information about support for version control in cPanel & WHM, read our
[Git Version Control](https://go.cpanel.net/GitVersionControl) and
[Guide to Git](https://go.cpanel.net/GitDeployment) documentation.
* For a list of configuration changes, repository restrictions, and troubleshooting steps,
read our [Guide to Git - For System Administrators](https://go.cpanel.net/GuidetoGitForSystemAdministrators) documentation.

**Important:**

The system logs errors for this function in the `~/.cpanel/logs/vc_TIMESTAMP_git_create.log`
file, where `TIMESTAMP` represents the time of the error in Unix epoch time.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200542 import InlineResponse200542
from clientapi_cpanel.models.object import object
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
    api_instance = clientapi_cpanel.RepositoryManagementApi(api_client)
    name = 'example' # str | The new repository's display name.
    repository_root = '/home/user/public_html/example' # str | The absolute path to the directory in which to store the repository, relative to the user's `home` directory.  **Note:**  * If the directory does **not** exist, the system will create it. * If the specified directory already contains a repository, the system will automatically add it to the list of cPanel-managed repositories. * This feature enforces several restrictions on repository paths. For more information, read our [Guide to Git - For System Administrators](https://go.cpanel.net/GuidetoGitForSystemAdministrators) documentation.
    type = 'git' # str | The repository type.  * `git` — A [Git](https://git-scm.com/) repository.  **Note:**  `git` is the only possible value.
    source_repository = None # object | A JSON-formatted object containing information about the source repository that the system will clone.  **Note:**  If you do **not** include source repository data, the function creates an empty repository. (optional)

    try:
        # Create Git repository
        api_response = api_instance.version_control_create(name, repository_root, type, source_repository=source_repository)
        print("The response of RepositoryManagementApi->version_control_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RepositoryManagementApi->version_control_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The new repository&#39;s display name. | 
 **repository_root** | **str**| The absolute path to the directory in which to store the repository, relative to the user&#39;s &#x60;home&#x60; directory.  **Note:**  * If the directory does **not** exist, the system will create it. * If the specified directory already contains a repository, the system will automatically add it to the list of cPanel-managed repositories. * This feature enforces several restrictions on repository paths. For more information, read our [Guide to Git - For System Administrators](https://go.cpanel.net/GuidetoGitForSystemAdministrators) documentation. | 
 **type** | **str**| The repository type.  * &#x60;git&#x60; — A [Git](https://git-scm.com/) repository.  **Note:**  &#x60;git&#x60; is the only possible value. | 
 **source_repository** | [**object**](.md)| A JSON-formatted object containing information about the source repository that the system will clone.  **Note:**  If you do **not** include source repository data, the function creates an empty repository. | [optional] 

### Return type

[**InlineResponse200542**](InlineResponse200542.md)

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

# **version_control_delete**
> InlineResponse200543 version_control_delete(repository_root)

Delete Git repository

This function deletes a cPanel account's Git™ repository. For more information about
support for version control in cPanel & WHM, read our
[Git Version Control](https://go.cpanel.net/GitVersionControl) and
[Guide to Git](https://go.cpanel.net/GitDeployment) documentation.

**Warning:**

* When you call this function, the system **permanently deletes** the entire contents
of the specified directory. You **cannot** recover this data after deletion.
* You **cannot** use this function to delete any repositories that do not appear in
the cache of repositories (for example, repositories that contain invalid characters or
exist within cPanel-controlled directories).

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200543 import InlineResponse200543
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
    api_instance = clientapi_cpanel.RepositoryManagementApi(api_client)
    repository_root = '/home/user/example' # str | The absolute directory path in the user's `home` directory containing the repository to delete.

    try:
        # Delete Git repository
        api_response = api_instance.version_control_delete(repository_root)
        print("The response of RepositoryManagementApi->version_control_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RepositoryManagementApi->version_control_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repository_root** | **str**| The absolute directory path in the user&#39;s &#x60;home&#x60; directory containing the repository to delete. | 

### Return type

[**InlineResponse200543**](InlineResponse200543.md)

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

# **version_control_retrieve**
> InlineResponse200544 version_control_retrieve(fields=fields)

Return Git repositories

This function lists Git™ repositories on a cPanel account. For more information
about support for version control in cPanel & WHM, read our
[Git Version Control](https://go.cpanel.net/GitVersionControl) and
[Guide to Git](https://go.cpanel.net/GitDeployment) documentation.

**Important:**

* This feature does **not** allow the following characters in repository paths:
  ``\ * | " ' < > & @ ` $ { } [ ] ( ) ; ? : = % #``
* This function does **not** allow repositories that exist in the following
cPanel-controlled directories:

  * `.cpanel`
  * `.htpasswds`
  * `.ssh`
  * `.trash`
  * `access-logs`
  * `cgi-bin`
  * `etc`
  * `logs`
  * `perl5`
  * `mail`
  * `spamassassin`
  * `ssl`
  * `tmp`
  * `var`

Users can create repositories in some of these directories on the command line.
They may appear in the list of repositories in Gitweb, but users may see an error
message if they try to access them.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200544 import InlineResponse200544
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
    api_instance = clientapi_cpanel.RepositoryManagementApi(api_client)
    fields = '*' # str | A comma-separated list of desired return values.  **Note:**  Use a wildcard (`*`) to list all possible return values. (optional) (default to '*')

    try:
        # Return Git repositories
        api_response = api_instance.version_control_retrieve(fields=fields)
        print("The response of RepositoryManagementApi->version_control_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RepositoryManagementApi->version_control_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | **str**| A comma-separated list of desired return values.  **Note:**  Use a wildcard (&#x60;*&#x60;) to list all possible return values. | [optional] [default to &#39;*&#39;]

### Return type

[**InlineResponse200544**](InlineResponse200544.md)

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

# **version_control_update**
> InlineResponse200545 version_control_update(repository_root, branch=branch, name=name, source_repository=source_repository)

Update Git repository settings

This function modifies a Git™ repository's basic settings. For more information about support
for version control in cPanel & WHM, read our
[Git Version Control](https://go.cpanel.net/GitVersionControl)
and [Guide to Git](https://go.cpanel.net/GitDeployment) documentation.

**Note:**

* This function **only** pulls changes from the remote repository if you specify a `branch` value.
* You **cannot** modify the `type`, `repository_root`, or `url` values for existing repositories.
* You **must** include the `repository_root` parameter in order to identify the repository to
update.
* All other input parameters are **optional**. Use them to assign the **new** values to the
account. If you do not include a parameter or specify its existing value, no change will occur.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200545 import InlineResponse200545
from clientapi_cpanel.models.object import object
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
    api_instance = clientapi_cpanel.RepositoryManagementApi(api_client)
    repository_root = '/home/user/public_html/example' # str | The absolute directory path that contains the repository to update.
    branch = 'master' # str | The new branch to use.  If you do not specify a value, the function does **not** update this parameter.  **Remember:**  This function **only** pulls changes from the remote repository if you specify this value. (optional)
    name = 'example' # str | The repository's new display name.  If you do not specify a value, the function does **not** update this parameter. (optional)
    source_repository = None # object | A JSON-encoded object containing information about the source repository.  If you do not specify a value, the function does **not** update this parameter.  **Important:**  * You **cannot** modify the source repository's URL. * You **must** JSON-encode the contents of this object. (optional)

    try:
        # Update Git repository settings
        api_response = api_instance.version_control_update(repository_root, branch=branch, name=name, source_repository=source_repository)
        print("The response of RepositoryManagementApi->version_control_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RepositoryManagementApi->version_control_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repository_root** | **str**| The absolute directory path that contains the repository to update. | 
 **branch** | **str**| The new branch to use.  If you do not specify a value, the function does **not** update this parameter.  **Remember:**  This function **only** pulls changes from the remote repository if you specify this value. | [optional] 
 **name** | **str**| The repository&#39;s new display name.  If you do not specify a value, the function does **not** update this parameter. | [optional] 
 **source_repository** | [**object**](.md)| A JSON-encoded object containing information about the source repository.  If you do not specify a value, the function does **not** update this parameter.  **Important:**  * You **cannot** modify the source repository&#39;s URL. * You **must** JSON-encode the contents of this object. | [optional] 

### Return type

[**InlineResponse200545**](InlineResponse200545.md)

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

