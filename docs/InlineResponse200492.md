# InlineResponse200492


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**apiversion** | **int** | The version of the API. | [optional] 
**func** | **str** | The name of the method called. | [optional] 
**module** | **str** | The name of the module called. | [optional] 
**result** | [**InlineResponse200492Result**](InlineResponse200492Result.md) |  | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200492 import InlineResponse200492

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200492 from a JSON string
inline_response200492_instance = InlineResponse200492.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200492.to_json())

# convert the object into a dict
inline_response200492_dict = inline_response200492_instance.to_dict()
# create an instance of InlineResponse200492 from a dict
inline_response200492_from_dict = InlineResponse200492.from_dict(inline_response200492_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


