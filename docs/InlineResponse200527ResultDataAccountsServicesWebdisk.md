# InlineResponse200527ResultDataAccountsServicesWebdisk

Information about the Subaccount's Web Disk status.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **int** | Whether the Subaccount can access Web Disk.  * &#x60;1&#x60; — Has Web Disk service access. * &#x60;0&#x60; — Does **not** have Web Disk service access. | [optional] 
**homedir** | **str** | The Subaccount&#39;s Web Disk directory, relative to the cPanel account&#39;s home directory. | [optional] 
**perms** | **str** | Whether the Web Disk has read or read and write permissions.  * &#x60;ro&#x60; — Read-only permissions. * &#x60;rw&#x60; — Read and write permissions. | [optional] 
**private** | **int** | Whether the Web Disk directory permissions are public or private.  * &#x60;1&#x60; — Private (&#x60;0700&#x60;). * &#x60;0&#x60; — Public (&#x60;0755&#x60;). | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200527_result_data_accounts_services_webdisk import InlineResponse200527ResultDataAccountsServicesWebdisk

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200527ResultDataAccountsServicesWebdisk from a JSON string
inline_response200527_result_data_accounts_services_webdisk_instance = InlineResponse200527ResultDataAccountsServicesWebdisk.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200527ResultDataAccountsServicesWebdisk.to_json())

# convert the object into a dict
inline_response200527_result_data_accounts_services_webdisk_dict = inline_response200527_result_data_accounts_services_webdisk_instance.to_dict()
# create an instance of InlineResponse200527ResultDataAccountsServicesWebdisk from a dict
inline_response200527_result_data_accounts_services_webdisk_from_dict = InlineResponse200527ResultDataAccountsServicesWebdisk.from_dict(inline_response200527_result_data_accounts_services_webdisk_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


