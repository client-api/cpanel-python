# InlineResponse200419


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**apiversion** | **int** | The version of the API. | [optional] 
**func** | **str** | The name of the method called. | [optional] 
**module** | **str** | The name of the module called. | [optional] 
**result** | [**InlineResponse200419Result**](InlineResponse200419Result.md) |  | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200419 import InlineResponse200419

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200419 from a JSON string
inline_response200419_instance = InlineResponse200419.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200419.to_json())

# convert the object into a dict
inline_response200419_dict = inline_response200419_instance.to_dict()
# create an instance of InlineResponse200419 from a dict
inline_response200419_from_dict = InlineResponse200419.from_dict(inline_response200419_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


