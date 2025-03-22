# InlineResponse200318


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**apiversion** | **int** | The version of the API. | [optional] 
**func** | **str** | The name of the method called. | [optional] 
**module** | **str** | The name of the module called. | [optional] 
**result** | [**InlineResponse20035Result**](InlineResponse20035Result.md) |  | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200318 import InlineResponse200318

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200318 from a JSON string
inline_response200318_instance = InlineResponse200318.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200318.to_json())

# convert the object into a dict
inline_response200318_dict = inline_response200318_instance.to_dict()
# create an instance of InlineResponse200318 from a dict
inline_response200318_from_dict = InlineResponse200318.from_dict(inline_response200318_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


