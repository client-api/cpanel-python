# InlineResponse200529ResultDataServices

Information about the account's access to email, FTP, and Web Disk.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | [**InlineResponse200529ResultDataServicesEmail**](InlineResponse200529ResultDataServicesEmail.md) |  | [optional] 
**ftp** | [**InlineResponse200529ResultDataServicesFtp**](InlineResponse200529ResultDataServicesFtp.md) |  | [optional] 
**webdisk** | [**InlineResponse200529ResultDataServicesWebdisk**](InlineResponse200529ResultDataServicesWebdisk.md) |  | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200529_result_data_services import InlineResponse200529ResultDataServices

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200529ResultDataServices from a JSON string
inline_response200529_result_data_services_instance = InlineResponse200529ResultDataServices.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200529ResultDataServices.to_json())

# convert the object into a dict
inline_response200529_result_data_services_dict = inline_response200529_result_data_services_instance.to_dict()
# create an instance of InlineResponse200529ResultDataServices from a dict
inline_response200529_result_data_services_from_dict = InlineResponse200529ResultDataServices.from_dict(inline_response200529_result_data_services_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


