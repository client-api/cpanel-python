# InlineResponse200479


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**apiversion** | **int** | The version of the API. | [optional] 
**func** | **str** | The name of the method called. | [optional] 
**module** | **str** | The name of the module called. | [optional] 
**result** | [**InlineResponse200479Result**](InlineResponse200479Result.md) |  | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200479 import InlineResponse200479

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200479 from a JSON string
inline_response200479_instance = InlineResponse200479.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200479.to_json())

# convert the object into a dict
inline_response200479_dict = inline_response200479_instance.to_dict()
# create an instance of InlineResponse200479 from a dict
inline_response200479_from_dict = InlineResponse200479.from_dict(inline_response200479_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


