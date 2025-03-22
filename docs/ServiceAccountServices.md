# ServiceAccountServices

Information about the subaccount's access to email, FTP, and Web Disk.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | [**ServiceAccountServicesEmail**](ServiceAccountServicesEmail.md) |  | [optional] 
**ftp** | [**ServiceAccountServicesFtp**](ServiceAccountServicesFtp.md) |  | [optional] 
**special** | **int** | Whether the account is a system-created special account that the user cannot remove. * &#x60;1&#x60; - A special account. * &#x60;0&#x60; - Not a special account. | [optional] 
**webdisk** | [**ServiceAccountServicesWebdisk**](ServiceAccountServicesWebdisk.md) |  | [optional] 

## Example

```python
from clientapi_cpanel.models.service_account_services import ServiceAccountServices

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceAccountServices from a JSON string
service_account_services_instance = ServiceAccountServices.from_json(json)
# print the JSON string representation of the object
print(ServiceAccountServices.to_json())

# convert the object into a dict
service_account_services_dict = service_account_services_instance.to_dict()
# create an instance of ServiceAccountServices from a dict
service_account_services_from_dict = ServiceAccountServices.from_dict(service_account_services_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


