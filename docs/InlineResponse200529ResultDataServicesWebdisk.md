# InlineResponse200529ResultDataServicesWebdisk

Information about the account's Web Disk status.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **int** | Whether the account can access Web Disk. * &#x60;1&#x60; - Can access. * &#x60;0&#x60; - **Cannot** access. | [optional] 
**homedir** | **str** | The account&#39;s Web Disk directory. * A valid path, relative to the cPanel account&#39;s home directory. | [optional] 
**perms** | **str** | Whether to grant write permissions to the account. * &#x60;ro&#x60; - Read-only permissions. * &#x60;rw&#x60; - Read and write permissions. | [optional] 
**private** | **int** | Whether to set the Web Disk directory&#39;s permissions to public or private. * &#x60;1&#x60; - Private (0700). * &#x60;0&#x60; - Public (0755). | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200529_result_data_services_webdisk import InlineResponse200529ResultDataServicesWebdisk

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200529ResultDataServicesWebdisk from a JSON string
inline_response200529_result_data_services_webdisk_instance = InlineResponse200529ResultDataServicesWebdisk.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200529ResultDataServicesWebdisk.to_json())

# convert the object into a dict
inline_response200529_result_data_services_webdisk_dict = inline_response200529_result_data_services_webdisk_instance.to_dict()
# create an instance of InlineResponse200529ResultDataServicesWebdisk from a dict
inline_response200529_result_data_services_webdisk_from_dict = InlineResponse200529ResultDataServicesWebdisk.from_dict(inline_response200529_result_data_services_webdisk_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


