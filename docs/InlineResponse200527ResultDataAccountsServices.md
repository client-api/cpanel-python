# InlineResponse200527ResultDataAccountsServices

Information about the Subaccount's access to email, FTP, and Web Disk.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | [**InlineResponse200527ResultDataAccountsServicesEmail**](InlineResponse200527ResultDataAccountsServicesEmail.md) |  | [optional] 
**ftp** | [**InlineResponse200527ResultDataAccountsServicesFtp**](InlineResponse200527ResultDataAccountsServicesFtp.md) |  | [optional] 
**webdisk** | [**InlineResponse200527ResultDataAccountsServicesWebdisk**](InlineResponse200527ResultDataAccountsServicesWebdisk.md) |  | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200527_result_data_accounts_services import InlineResponse200527ResultDataAccountsServices

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200527ResultDataAccountsServices from a JSON string
inline_response200527_result_data_accounts_services_instance = InlineResponse200527ResultDataAccountsServices.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200527ResultDataAccountsServices.to_json())

# convert the object into a dict
inline_response200527_result_data_accounts_services_dict = inline_response200527_result_data_accounts_services_instance.to_dict()
# create an instance of InlineResponse200527ResultDataAccountsServices from a dict
inline_response200527_result_data_accounts_services_from_dict = InlineResponse200527ResultDataAccountsServices.from_dict(inline_response200527_result_data_accounts_services_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


