# InlineResponse200283


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**apiversion** | **int** | The version of the API. | [optional] 
**func** | **str** | The name of the method called. | [optional] 
**module** | **str** | The name of the module called. | [optional] 
**result** | [**InlineResponse200283Result**](InlineResponse200283Result.md) |  | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200283 import InlineResponse200283

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200283 from a JSON string
inline_response200283_instance = InlineResponse200283.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200283.to_json())

# convert the object into a dict
inline_response200283_dict = inline_response200283_instance.to_dict()
# create an instance of InlineResponse200283 from a dict
inline_response200283_from_dict = InlineResponse200283.from_dict(inline_response200283_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


