# clientapi_cpanel.VersionControlDeploymentApi

All URIs are relative to *https://cpanel-server.tld:2083/execute*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete**](VersionControlDeploymentApi.md#delete) | **GET** /VersionControlDeployment/delete | Delete Git deployment task
[**version_control_deployment_create**](VersionControlDeploymentApi.md#version_control_deployment_create) | **GET** /VersionControlDeployment/create | Create Git deployment task
[**version_control_deployment_retrieve**](VersionControlDeploymentApi.md#version_control_deployment_retrieve) | **GET** /VersionControlDeployment/retrieve | Return Git deployment task status


# **delete**
> InlineResponse200547 delete(deploy_id)

Delete Git deployment task

This function deletes a deployment task. For more information, read our [Guide to Git - Deployment](https://go.cpanel.net/GitDeployment) documentation.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200547 import InlineResponse200547
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
    api_instance = clientapi_cpanel.VersionControlDeploymentApi(api_client)
    deploy_id = '13' # str | The [Task Queue system's](https://go.cpanel.net/whmdocsTaskQueueMonitor) task ID number.

    try:
        # Delete Git deployment task
        api_response = api_instance.delete(deploy_id)
        print("The response of VersionControlDeploymentApi->delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VersionControlDeploymentApi->delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **deploy_id** | **str**| The [Task Queue system&#39;s](https://go.cpanel.net/whmdocsTaskQueueMonitor) task ID number. | 

### Return type

[**InlineResponse200547**](InlineResponse200547.md)

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

# **version_control_deployment_create**
> InlineResponse200546 version_control_deployment_create(repository_root)

Create Git deployment task

This function deploys the changes from a cPanel-managed repository.

**Important:**

The system logs messages for this function in the `~/.cpanel/logs/vc_TIMESTAMP_git_deploy.log` file, where TIMESTAMP represents the time in Unix epoch time. The system pulls changes with the `--ff-only` option and will only succeed if the branch's HEAD commit is up-to-date or Git can fast forward it. For more information about our suggested deployment configuration and how users can set it up, read our [Guide to Git™ - Deployment](https://go.cpanel.net/GitDeployment) documentation. Before deployment, repositories must meet the following requirements:
  * A valid checked-in `.cpanel.yml` file in the top-level directory.
  * One or more local or remote branches.
  * A clean working tree.

If a repository does **not** meet these requirements, the system will **not** display deployment information. Also, it will disable deployment functionality. For more information, read our [Guide to Git™ - Deployment](https://go.cpanel.net/GitDeployment) documentation.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200546 import InlineResponse200546
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
    api_instance = clientapi_cpanel.VersionControlDeploymentApi(api_client)
    repository_root = '/home/user/public_html/example' # str | The repository's directory.

    try:
        # Create Git deployment task
        api_response = api_instance.version_control_deployment_create(repository_root)
        print("The response of VersionControlDeploymentApi->version_control_deployment_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VersionControlDeploymentApi->version_control_deployment_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repository_root** | **str**| The repository&#39;s directory. | 

### Return type

[**InlineResponse200546**](InlineResponse200546.md)

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

# **version_control_deployment_retrieve**
> InlineResponse200548 version_control_deployment_retrieve()

Return Git deployment task status

This function retrieves the status of deployment tasks. Before deployment, repositories must meet the following requirements:
  * A valid checked-in `.cpanel.yml` file in the top-level directory.
  * One or more local or remote branches.
  * A clean working tree.

If a repository does **not** meet these requirements, the system will **not** display deployment information. Also, it will disable deployment functionality. For more information, read our [Guide to Git™ - Deployment](https://go.cpanel.net/GitDeployment) documentation.

**Important:**

The system logs messages for this function in the `~/.cpanel/logs/vc_TIMESTAMP_git_deploy.log` file, where `TIMESTAMP` represents the time in Unix epoch time.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200548 import InlineResponse200548
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
    api_instance = clientapi_cpanel.VersionControlDeploymentApi(api_client)

    try:
        # Return Git deployment task status
        api_response = api_instance.version_control_deployment_retrieve()
        print("The response of VersionControlDeploymentApi->version_control_deployment_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VersionControlDeploymentApi->version_control_deployment_retrieve: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**InlineResponse200548**](InlineResponse200548.md)

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

