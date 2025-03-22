# SubaccountBaseServicesWebdisk

Information about the subaccount's Web Disk status.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **int** | Whether the subaccount can access Web Disk. * &#x60;1&#x60; - Can access. * &#x60;0&#x60; - **Cannot** access. | [optional] 
**homedir** | **str** | The subaccount&#39;s Web Disk home directory, relative to the cPanel account&#39;s home directory. | [optional] 
**perms** | **str** | Whether the subaccount has read-only or read and write permissions.  * &#x60;ro&#x60; - Read-only permissions. * &#x60;rw&#x60; - Read and write permissions. | [optional] 
**private** | **int** | Whether the subaccount&#39;s Web Disk directory permissions are public or private.  * &#x60;1&#x60; - Private (&#x60;0700&#x60;). * &#x60;0&#x60; - Public (&#x60;0755&#x60;). | [optional] 

## Example

```python
from clientapi_cpanel.models.subaccount_base_services_webdisk import SubaccountBaseServicesWebdisk

# TODO update the JSON string below
json = "{}"
# create an instance of SubaccountBaseServicesWebdisk from a JSON string
subaccount_base_services_webdisk_instance = SubaccountBaseServicesWebdisk.from_json(json)
# print the JSON string representation of the object
print(SubaccountBaseServicesWebdisk.to_json())

# convert the object into a dict
subaccount_base_services_webdisk_dict = subaccount_base_services_webdisk_instance.to_dict()
# create an instance of SubaccountBaseServicesWebdisk from a dict
subaccount_base_services_webdisk_from_dict = SubaccountBaseServicesWebdisk.from_dict(subaccount_base_services_webdisk_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


