# InlineResponse200143


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**apiversion** | **int** | The version of the API. | [optional] 
**func** | **str** | The name of the method called. | [optional] 
**module** | **str** | The name of the module called. | [optional] 
**result** | [**InlineResponse200120Result**](InlineResponse200120Result.md) |  | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200143 import InlineResponse200143

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200143 from a JSON string
inline_response200143_instance = InlineResponse200143.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200143.to_json())

# convert the object into a dict
inline_response200143_dict = inline_response200143_instance.to_dict()
# create an instance of InlineResponse200143 from a dict
inline_response200143_from_dict = InlineResponse200143.from_dict(inline_response200143_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


