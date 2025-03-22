# InlineResponse20086


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**apiversion** | **int** | The version of the API. | [optional] 
**func** | **str** | The name of the method called. | [optional] 
**module** | **str** | The name of the module called. | [optional] 
**result** | [**InlineResponse20086Result**](InlineResponse20086Result.md) |  | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response20086 import InlineResponse20086

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse20086 from a JSON string
inline_response20086_instance = InlineResponse20086.from_json(json)
# print the JSON string representation of the object
print(InlineResponse20086.to_json())

# convert the object into a dict
inline_response20086_dict = inline_response20086_instance.to_dict()
# create an instance of InlineResponse20086 from a dict
inline_response20086_from_dict = InlineResponse20086.from_dict(inline_response20086_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


