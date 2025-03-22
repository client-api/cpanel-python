# InlineResponse200532ResultServices

An object containing information about the subaccount's access to email, FTP, and Web Disk.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | [**InlineResponse200532ResultServicesEmail**](InlineResponse200532ResultServicesEmail.md) |  | [optional] 
**ftp** | [**InlineResponse200532ResultServicesFtp**](InlineResponse200532ResultServicesFtp.md) |  | [optional] 
**special** | **int** | Whether the account is a system-created special account that the user cannot remove. * &#x60;1&#x60; - A special account. * &#x60;0&#x60; - **Not** a special account. | [optional] 
**webdisk** | [**InlineResponse200532ResultServicesWebdisk**](InlineResponse200532ResultServicesWebdisk.md) |  | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200532_result_services import InlineResponse200532ResultServices

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200532ResultServices from a JSON string
inline_response200532_result_services_instance = InlineResponse200532ResultServices.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200532ResultServices.to_json())

# convert the object into a dict
inline_response200532_result_services_dict = inline_response200532_result_services_instance.to_dict()
# create an instance of InlineResponse200532ResultServices from a dict
inline_response200532_result_services_from_dict = InlineResponse200532ResultServices.from_dict(inline_response200532_result_services_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


