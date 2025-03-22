# EditUserSubaccountBaseServices

This object contains information about the subaccount's access to email, FTP, and Web Disk.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | [**EditUserSubaccountBaseServicesEmail**](EditUserSubaccountBaseServicesEmail.md) |  | [optional] 
**ftp** | [**EditUserSubaccountBaseServicesFtp**](EditUserSubaccountBaseServicesFtp.md) |  | [optional] 
**webdisk** | [**EditUserSubaccountBaseServicesWebdisk**](EditUserSubaccountBaseServicesWebdisk.md) |  | [optional] 

## Example

```python
from clientapi_cpanel.models.edit_user_subaccount_base_services import EditUserSubaccountBaseServices

# TODO update the JSON string below
json = "{}"
# create an instance of EditUserSubaccountBaseServices from a JSON string
edit_user_subaccount_base_services_instance = EditUserSubaccountBaseServices.from_json(json)
# print the JSON string representation of the object
print(EditUserSubaccountBaseServices.to_json())

# convert the object into a dict
edit_user_subaccount_base_services_dict = edit_user_subaccount_base_services_instance.to_dict()
# create an instance of EditUserSubaccountBaseServices from a dict
edit_user_subaccount_base_services_from_dict = EditUserSubaccountBaseServices.from_dict(edit_user_subaccount_base_services_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


