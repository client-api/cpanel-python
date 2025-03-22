# InlineResponse200264


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**apiversion** | **int** | The version of the API. | [optional] 
**func** | **str** | The name of the method called. | [optional] 
**module** | **str** | The name of the module called. | [optional] 
**result** | [**InlineResponse200264Result**](InlineResponse200264Result.md) |  | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200264 import InlineResponse200264

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200264 from a JSON string
inline_response200264_instance = InlineResponse200264.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200264.to_json())

# convert the object into a dict
inline_response200264_dict = inline_response200264_instance.to_dict()
# create an instance of InlineResponse200264 from a dict
inline_response200264_from_dict = InlineResponse200264.from_dict(inline_response200264_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


