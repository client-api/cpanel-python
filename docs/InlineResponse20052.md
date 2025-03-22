# InlineResponse20052


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**apiversion** | **int** | The version of the API. | [optional] 
**func** | **str** | The name of the method called. | [optional] 
**module** | **str** | The name of the module called. | [optional] 
**result** | [**InlineResponse20052Result**](InlineResponse20052Result.md) |  | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response20052 import InlineResponse20052

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse20052 from a JSON string
inline_response20052_instance = InlineResponse20052.from_json(json)
# print the JSON string representation of the object
print(InlineResponse20052.to_json())

# convert the object into a dict
inline_response20052_dict = inline_response20052_instance.to_dict()
# create an instance of InlineResponse20052 from a dict
inline_response20052_from_dict = InlineResponse20052.from_dict(inline_response20052_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


