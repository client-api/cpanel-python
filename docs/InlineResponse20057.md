# InlineResponse20057


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**apiversion** | **int** | The version of the API. | [optional] 
**func** | **str** | The name of the method called. | [optional] 
**module** | **str** | The name of the module called. | [optional] 
**result** | [**InlineResponse20057Result**](InlineResponse20057Result.md) |  | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response20057 import InlineResponse20057

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse20057 from a JSON string
inline_response20057_instance = InlineResponse20057.from_json(json)
# print the JSON string representation of the object
print(InlineResponse20057.to_json())

# convert the object into a dict
inline_response20057_dict = inline_response20057_instance.to_dict()
# create an instance of InlineResponse20057 from a dict
inline_response20057_from_dict = InlineResponse20057.from_dict(inline_response20057_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


