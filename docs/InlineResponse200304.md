# InlineResponse200304


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**apiversion** | **int** | The version of the API. | [optional] 
**func** | **str** | The name of the method called. | [optional] 
**module** | **str** | The name of the module called. | [optional] 
**result** | [**InlineResponse200304Result**](InlineResponse200304Result.md) |  | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200304 import InlineResponse200304

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200304 from a JSON string
inline_response200304_instance = InlineResponse200304.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200304.to_json())

# convert the object into a dict
inline_response200304_dict = inline_response200304_instance.to_dict()
# create an instance of InlineResponse200304 from a dict
inline_response200304_from_dict = InlineResponse200304.from_dict(inline_response200304_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


