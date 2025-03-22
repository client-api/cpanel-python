# InlineResponse20069


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**apiversion** | **int** | The version of the API. | [optional] 
**func** | **str** | The name of the method called. | [optional] 
**module** | **str** | The name of the module called. | [optional] 
**result** | [**InlineResponse20069Result**](InlineResponse20069Result.md) |  | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response20069 import InlineResponse20069

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse20069 from a JSON string
inline_response20069_instance = InlineResponse20069.from_json(json)
# print the JSON string representation of the object
print(InlineResponse20069.to_json())

# convert the object into a dict
inline_response20069_dict = inline_response20069_instance.to_dict()
# create an instance of InlineResponse20069 from a dict
inline_response20069_from_dict = InlineResponse20069.from_dict(inline_response20069_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


