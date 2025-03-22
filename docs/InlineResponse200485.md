# InlineResponse200485


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**apiversion** | **int** | The version of the API. | [optional] 
**errors** | **object** |  | [optional] 
**func** | **str** | The name of the method called. | [optional] 
**messages** | **object** |  | [optional] 
**module** | **str** | The name of the module called. | [optional] 
**result** | [**InlineResponse200485Result**](InlineResponse200485Result.md) |  | [optional] 
**status** | **object** |  | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200485 import InlineResponse200485

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200485 from a JSON string
inline_response200485_instance = InlineResponse200485.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200485.to_json())

# convert the object into a dict
inline_response200485_dict = inline_response200485_instance.to_dict()
# create an instance of InlineResponse200485 from a dict
inline_response200485_from_dict = InlineResponse200485.from_dict(inline_response200485_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


