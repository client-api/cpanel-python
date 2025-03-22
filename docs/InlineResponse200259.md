# InlineResponse200259


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**apiversion** | **int** | The version of the API. | [optional] 
**func** | **str** | The name of the method called. | [optional] 
**module** | **str** | The name of the module called. | [optional] 
**result** | [**InlineResponse20035Result**](InlineResponse20035Result.md) |  | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200259 import InlineResponse200259

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200259 from a JSON string
inline_response200259_instance = InlineResponse200259.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200259.to_json())

# convert the object into a dict
inline_response200259_dict = inline_response200259_instance.to_dict()
# create an instance of InlineResponse200259 from a dict
inline_response200259_from_dict = InlineResponse200259.from_dict(inline_response200259_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


