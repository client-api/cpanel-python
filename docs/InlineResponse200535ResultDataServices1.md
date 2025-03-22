# InlineResponse200535ResultDataServices1

This object contains information about the subaccount's access to email, FTP, and Web Disk.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | [**InlineResponse200535ResultDataServicesEmail**](InlineResponse200535ResultDataServicesEmail.md) |  | [optional] 
**ftp** | [**InlineResponse200535ResultDataServicesFtp**](InlineResponse200535ResultDataServicesFtp.md) |  | [optional] 
**webdisk** | [**InlineResponse200535ResultDataServices1Webdisk**](InlineResponse200535ResultDataServices1Webdisk.md) |  | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200535_result_data_services1 import InlineResponse200535ResultDataServices1

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200535ResultDataServices1 from a JSON string
inline_response200535_result_data_services1_instance = InlineResponse200535ResultDataServices1.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200535ResultDataServices1.to_json())

# convert the object into a dict
inline_response200535_result_data_services1_dict = inline_response200535_result_data_services1_instance.to_dict()
# create an instance of InlineResponse200535ResultDataServices1 from a dict
inline_response200535_result_data_services1_from_dict = InlineResponse200535ResultDataServices1.from_dict(inline_response200535_result_data_services1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


