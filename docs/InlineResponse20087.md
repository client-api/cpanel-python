# InlineResponse20087


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**apiversion** | **int** | The version of the API. | [optional] 
**func** | **str** | The name of the method called. | [optional] 
**module** | **str** | The name of the module called. | [optional] 
**result** | [**InlineResponse20087Result**](InlineResponse20087Result.md) |  | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response20087 import InlineResponse20087

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse20087 from a JSON string
inline_response20087_instance = InlineResponse20087.from_json(json)
# print the JSON string representation of the object
print(InlineResponse20087.to_json())

# convert the object into a dict
inline_response20087_dict = inline_response20087_instance.to_dict()
# create an instance of InlineResponse20087 from a dict
inline_response20087_from_dict = InlineResponse20087.from_dict(inline_response20087_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


