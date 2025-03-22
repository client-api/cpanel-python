# InlineResponse20085


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**apiversion** | **int** | The version of the API. | [optional] 
**func** | **str** | The name of the method called. | [optional] 
**module** | **str** | The name of the module called. | [optional] 
**result** | [**InlineResponse20085Result**](InlineResponse20085Result.md) |  | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response20085 import InlineResponse20085

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse20085 from a JSON string
inline_response20085_instance = InlineResponse20085.from_json(json)
# print the JSON string representation of the object
print(InlineResponse20085.to_json())

# convert the object into a dict
inline_response20085_dict = inline_response20085_instance.to_dict()
# create an instance of InlineResponse20085 from a dict
inline_response20085_from_dict = InlineResponse20085.from_dict(inline_response20085_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


