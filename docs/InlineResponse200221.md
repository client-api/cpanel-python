# InlineResponse200221


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**apiversion** | **int** | The version of the API. | [optional] 
**func** | **str** | The name of the method called. | [optional] 
**module** | **str** | The name of the module called. | [optional] 
**result** | [**InlineResponse200221Result**](InlineResponse200221Result.md) |  | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200221 import InlineResponse200221

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200221 from a JSON string
inline_response200221_instance = InlineResponse200221.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200221.to_json())

# convert the object into a dict
inline_response200221_dict = inline_response200221_instance.to_dict()
# create an instance of InlineResponse200221 from a dict
inline_response200221_from_dict = InlineResponse200221.from_dict(inline_response200221_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


