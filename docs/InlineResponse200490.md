# InlineResponse200490


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**apiversion** | **int** | The version of the API. | [optional] 
**func** | **str** | The name of the method called. | [optional] 
**module** | **str** | The name of the module called. | [optional] 
**result** | [**InlineResponse200490Result**](InlineResponse200490Result.md) |  | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200490 import InlineResponse200490

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200490 from a JSON string
inline_response200490_instance = InlineResponse200490.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200490.to_json())

# convert the object into a dict
inline_response200490_dict = inline_response200490_instance.to_dict()
# create an instance of InlineResponse200490 from a dict
inline_response200490_from_dict = InlineResponse200490.from_dict(inline_response200490_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


