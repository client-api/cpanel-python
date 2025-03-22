# InlineResponse200170


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**apiversion** | **int** | The version of the API. | [optional] 
**func** | **str** | The name of the method called. | [optional] 
**module** | **str** | The name of the module called. | [optional] 
**result** | [**InlineResponse200170Result**](InlineResponse200170Result.md) |  | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200170 import InlineResponse200170

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200170 from a JSON string
inline_response200170_instance = InlineResponse200170.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200170.to_json())

# convert the object into a dict
inline_response200170_dict = inline_response200170_instance.to_dict()
# create an instance of InlineResponse200170 from a dict
inline_response200170_from_dict = InlineResponse200170.from_dict(inline_response200170_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


