# InlineResponse200547


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**apiversion** | **int** | The version of the API. | [optional] 
**func** | **str** | The name of the method called. | [optional] 
**module** | **str** | The name of the module called. | [optional] 
**result** | [**InlineResponse200252Result**](InlineResponse200252Result.md) |  | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200547 import InlineResponse200547

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200547 from a JSON string
inline_response200547_instance = InlineResponse200547.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200547.to_json())

# convert the object into a dict
inline_response200547_dict = inline_response200547_instance.to_dict()
# create an instance of InlineResponse200547 from a dict
inline_response200547_from_dict = InlineResponse200547.from_dict(inline_response200547_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


