# SubaccountBaseServices

Information about the subaccount's access to email, FTP, and Web Disk.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | [**SubaccountBaseServicesEmail**](SubaccountBaseServicesEmail.md) |  | [optional] 
**ftp** | [**SubaccountBaseServicesFtp**](SubaccountBaseServicesFtp.md) |  | [optional] 
**webdisk** | [**SubaccountBaseServicesWebdisk**](SubaccountBaseServicesWebdisk.md) |  | [optional] 

## Example

```python
from clientapi_cpanel.models.subaccount_base_services import SubaccountBaseServices

# TODO update the JSON string below
json = "{}"
# create an instance of SubaccountBaseServices from a JSON string
subaccount_base_services_instance = SubaccountBaseServices.from_json(json)
# print the JSON string representation of the object
print(SubaccountBaseServices.to_json())

# convert the object into a dict
subaccount_base_services_dict = subaccount_base_services_instance.to_dict()
# create an instance of SubaccountBaseServices from a dict
subaccount_base_services_from_dict = SubaccountBaseServices.from_dict(subaccount_base_services_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


