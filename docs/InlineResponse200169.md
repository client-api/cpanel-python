# InlineResponse200169


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**apiversion** | **int** | The version of the API. | [optional] 
**func** | **str** | The name of the method called. | [optional] 
**module** | **str** | The name of the module called. | [optional] 
**result** | [**InlineResponse200169Result**](InlineResponse200169Result.md) |  | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200169 import InlineResponse200169

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200169 from a JSON string
inline_response200169_instance = InlineResponse200169.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200169.to_json())

# convert the object into a dict
inline_response200169_dict = inline_response200169_instance.to_dict()
# create an instance of InlineResponse200169 from a dict
inline_response200169_from_dict = InlineResponse200169.from_dict(inline_response200169_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


