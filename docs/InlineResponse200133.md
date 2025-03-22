# InlineResponse200133


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**apiversion** | **int** | The version of the API. | [optional] 
**func** | **str** | The name of the method called. | [optional] 
**module** | **str** | The name of the module called. | [optional] 
**result** | [**InlineResponse200133Result**](InlineResponse200133Result.md) |  | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200133 import InlineResponse200133

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200133 from a JSON string
inline_response200133_instance = InlineResponse200133.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200133.to_json())

# convert the object into a dict
inline_response200133_dict = inline_response200133_instance.to_dict()
# create an instance of InlineResponse200133 from a dict
inline_response200133_from_dict = InlineResponse200133.from_dict(inline_response200133_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


