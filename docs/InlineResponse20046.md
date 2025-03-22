# InlineResponse20046


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**apiversion** | **int** | The version of the API. | [optional] 
**func** | **str** | The name of the method called. | [optional] 
**module** | **str** | The name of the module called. | [optional] 
**result** | [**InlineResponse20046Result**](InlineResponse20046Result.md) |  | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response20046 import InlineResponse20046

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse20046 from a JSON string
inline_response20046_instance = InlineResponse20046.from_json(json)
# print the JSON string representation of the object
print(InlineResponse20046.to_json())

# convert the object into a dict
inline_response20046_dict = inline_response20046_instance.to_dict()
# create an instance of InlineResponse20046 from a dict
inline_response20046_from_dict = InlineResponse20046.from_dict(inline_response20046_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


