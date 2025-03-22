# InlineResponse200416


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**apiversion** | **int** | The version of the API. | [optional] 
**func** | **str** | The name of the method called. | [optional] 
**module** | **str** | The name of the module called. | [optional] 
**result** | [**InlineResponse200416Result**](InlineResponse200416Result.md) |  | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200416 import InlineResponse200416

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200416 from a JSON string
inline_response200416_instance = InlineResponse200416.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200416.to_json())

# convert the object into a dict
inline_response200416_dict = inline_response200416_instance.to_dict()
# create an instance of InlineResponse200416 from a dict
inline_response200416_from_dict = InlineResponse200416.from_dict(inline_response200416_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


