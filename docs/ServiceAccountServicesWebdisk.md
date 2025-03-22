# ServiceAccountServicesWebdisk

This object contains information that indicates the subaccount's Web Disk status.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **int** | Whether the subaccount can access Web Disk. * &#x60;1&#x60; - Can access. * &#x60;0&#x60; - Cannot access. | [optional] 
**enabledigest** | **int** | Whether the subaccount&#39;s Web Disk service has enabled Digest Authentication. * &#x60;1&#x60; - Digest Authentication is enabled. * &#x60;0&#x60; - Digest Authentication is not enabled. | [optional] 
**homedir** | **str** | The subaccount&#39;s Web Disk home directory, relative to the cPanel account&#39;s home directory. | [optional] 
**perms** | **str** | Whether to grant write permissions to the subaccount. * &#x60;ro&#x60; - Read-only permissions. * &#x60;rw&#x60; - Read and write permissions. | [optional] 
**private** | **int** | Whether to set the Web Disk directory&#39;s permissions to public or private. * &#x60;1&#x60; - Private (0700). * &#x60;0&#x60; - Public (0755). | [optional] 

## Example

```python
from clientapi_cpanel.models.service_account_services_webdisk import ServiceAccountServicesWebdisk

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceAccountServicesWebdisk from a JSON string
service_account_services_webdisk_instance = ServiceAccountServicesWebdisk.from_json(json)
# print the JSON string representation of the object
print(ServiceAccountServicesWebdisk.to_json())

# convert the object into a dict
service_account_services_webdisk_dict = service_account_services_webdisk_instance.to_dict()
# create an instance of ServiceAccountServicesWebdisk from a dict
service_account_services_webdisk_from_dict = ServiceAccountServicesWebdisk.from_dict(service_account_services_webdisk_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


