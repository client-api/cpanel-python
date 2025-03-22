# InlineResponse200368


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**apiversion** | **int** | The version of the API. | [optional] 
**func** | **str** | The name of the method called. | [optional] 
**module** | **str** | The name of the module called. | [optional] 
**result** | [**InlineResponse200368Result**](InlineResponse200368Result.md) |  | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200368 import InlineResponse200368

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200368 from a JSON string
inline_response200368_instance = InlineResponse200368.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200368.to_json())

# convert the object into a dict
inline_response200368_dict = inline_response200368_instance.to_dict()
# create an instance of InlineResponse200368 from a dict
inline_response200368_from_dict = InlineResponse200368.from_dict(inline_response200368_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


