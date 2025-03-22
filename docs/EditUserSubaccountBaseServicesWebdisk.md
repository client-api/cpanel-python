# EditUserSubaccountBaseServicesWebdisk

This object contains information that indicates the subaccount's Web Disk status.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **int** | Whether the subaccount can access Web Disk.  * &#x60;1&#x60; - Can access. * &#x60;0&#x60; - **Cannot** access. | [optional] 
**homedir** | **str** | The subaccount&#39;s Web Disk home directory. | [optional] 
**perms** | **str** | Whether to grant write permissions to the subaccount.  * &#x60;ro&#x60; - Read-only permissions. * &#x60;rw&#x60; - Read and write permissions. | [optional] 
**private** | **int** | Whether to set the Web Disk directory&#39;s permissions to public or private.  * &#x60;1&#x60; - Private (&#x60;0700&#x60;). * &#x60;0&#x60; - Public (&#x60;0755&#x60;). | [optional] 

## Example

```python
from clientapi_cpanel.models.edit_user_subaccount_base_services_webdisk import EditUserSubaccountBaseServicesWebdisk

# TODO update the JSON string below
json = "{}"
# create an instance of EditUserSubaccountBaseServicesWebdisk from a JSON string
edit_user_subaccount_base_services_webdisk_instance = EditUserSubaccountBaseServicesWebdisk.from_json(json)
# print the JSON string representation of the object
print(EditUserSubaccountBaseServicesWebdisk.to_json())

# convert the object into a dict
edit_user_subaccount_base_services_webdisk_dict = edit_user_subaccount_base_services_webdisk_instance.to_dict()
# create an instance of EditUserSubaccountBaseServicesWebdisk from a dict
edit_user_subaccount_base_services_webdisk_from_dict = EditUserSubaccountBaseServicesWebdisk.from_dict(edit_user_subaccount_base_services_webdisk_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


