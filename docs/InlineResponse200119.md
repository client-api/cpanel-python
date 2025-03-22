# InlineResponse200119


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**apiversion** | **int** | The version of the API. | [optional] 
**func** | **str** | The name of the method called. | [optional] 
**module** | **str** | The name of the module called. | [optional] 
**result** | [**InlineResponse200119Result**](InlineResponse200119Result.md) |  | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200119 import InlineResponse200119

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200119 from a JSON string
inline_response200119_instance = InlineResponse200119.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200119.to_json())

# convert the object into a dict
inline_response200119_dict = inline_response200119_instance.to_dict()
# create an instance of InlineResponse200119 from a dict
inline_response200119_from_dict = InlineResponse200119.from_dict(inline_response200119_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


