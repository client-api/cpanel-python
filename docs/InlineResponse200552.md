# InlineResponse200552


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**apiversion** | **int** | The version of the API. | [optional] 
**func** | **str** | The name of the method called. | [optional] 
**module** | **str** | The name of the module called. | [optional] 
**result** | [**InlineResponse20035Result**](InlineResponse20035Result.md) |  | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200552 import InlineResponse200552

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200552 from a JSON string
inline_response200552_instance = InlineResponse200552.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200552.to_json())

# convert the object into a dict
inline_response200552_dict = inline_response200552_instance.to_dict()
# create an instance of InlineResponse200552 from a dict
inline_response200552_from_dict = InlineResponse200552.from_dict(inline_response200552_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


