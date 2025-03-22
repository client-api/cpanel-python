# InlineResponse200372


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**apiversion** | **int** | The version of the API. | [optional] 
**func** | **str** | The name of the method called. | [optional] 
**module** | **str** | The name of the module called. | [optional] 
**result** | [**InlineResponse200372Result**](InlineResponse200372Result.md) |  | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200372 import InlineResponse200372

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200372 from a JSON string
inline_response200372_instance = InlineResponse200372.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200372.to_json())

# convert the object into a dict
inline_response200372_dict = inline_response200372_instance.to_dict()
# create an instance of InlineResponse200372 from a dict
inline_response200372_from_dict = InlineResponse200372.from_dict(inline_response200372_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


