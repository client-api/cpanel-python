# InlineResponse200159


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**apiversion** | **int** | The version of the API. | [optional] 
**func** | **str** | The name of the method called. | [optional] 
**module** | **str** | The name of the module called. | [optional] 
**result** | [**InlineResponse200159Result**](InlineResponse200159Result.md) |  | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200159 import InlineResponse200159

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200159 from a JSON string
inline_response200159_instance = InlineResponse200159.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200159.to_json())

# convert the object into a dict
inline_response200159_dict = inline_response200159_instance.to_dict()
# create an instance of InlineResponse200159 from a dict
inline_response200159_from_dict = InlineResponse200159.from_dict(inline_response200159_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


