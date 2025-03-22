# InlineResponse200352ResultData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_remote** | **int** | Whether the host is a remote MySQL server. * &#x60;1&#x60; - Remote host. * &#x60;0&#x60; - Local host. | [optional] 
**remote_host** | [**InlineResponse200352ResultDataRemoteHost**](InlineResponse200352ResultDataRemoteHost.md) |  | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200352_result_data import InlineResponse200352ResultData

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200352ResultData from a JSON string
inline_response200352_result_data_instance = InlineResponse200352ResultData.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200352ResultData.to_json())

# convert the object into a dict
inline_response200352_result_data_dict = inline_response200352_result_data_instance.to_dict()
# create an instance of InlineResponse200352ResultData from a dict
inline_response200352_result_data_from_dict = InlineResponse200352ResultData.from_dict(inline_response200352_result_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


