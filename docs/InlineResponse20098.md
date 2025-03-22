# InlineResponse20098


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**apiversion** | **int** | The version of the API. | [optional] 
**func** | **str** | The name of the method called. | [optional] 
**module** | **str** | The name of the module called. | [optional] 
**result** | [**InlineResponse20098Result**](InlineResponse20098Result.md) |  | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response20098 import InlineResponse20098

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse20098 from a JSON string
inline_response20098_instance = InlineResponse20098.from_json(json)
# print the JSON string representation of the object
print(InlineResponse20098.to_json())

# convert the object into a dict
inline_response20098_dict = inline_response20098_instance.to_dict()
# create an instance of InlineResponse20098 from a dict
inline_response20098_from_dict = InlineResponse20098.from_dict(inline_response20098_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


