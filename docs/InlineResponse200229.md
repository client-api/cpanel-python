# InlineResponse200229


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**apiversion** | **int** | The version of the API. | [optional] 
**func** | **str** | The name of the method called. | [optional] 
**module** | **str** | The name of the module called. | [optional] 
**result** | [**InlineResponse200229Result**](InlineResponse200229Result.md) |  | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200229 import InlineResponse200229

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200229 from a JSON string
inline_response200229_instance = InlineResponse200229.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200229.to_json())

# convert the object into a dict
inline_response200229_dict = inline_response200229_instance.to_dict()
# create an instance of InlineResponse200229 from a dict
inline_response200229_from_dict = InlineResponse200229.from_dict(inline_response200229_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


