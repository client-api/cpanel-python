# InlineResponse20054


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**apiversion** | **int** | The version of the API. | [optional] 
**func** | **str** | The name of the method called. | [optional] 
**module** | **str** | The name of the module called. | [optional] 
**result** | [**InlineResponse20054Result**](InlineResponse20054Result.md) |  | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response20054 import InlineResponse20054

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse20054 from a JSON string
inline_response20054_instance = InlineResponse20054.from_json(json)
# print the JSON string representation of the object
print(InlineResponse20054.to_json())

# convert the object into a dict
inline_response20054_dict = inline_response20054_instance.to_dict()
# create an instance of InlineResponse20054 from a dict
inline_response20054_from_dict = InlineResponse20054.from_dict(inline_response20054_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


