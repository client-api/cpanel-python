# InlineResponse200344


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**apiversion** | **int** | The version of the API. | [optional] 
**func** | **str** | The name of the method called. | [optional] 
**module** | **str** | The name of the module called. | [optional] 
**result** | [**InlineResponse200344Result**](InlineResponse200344Result.md) |  | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200344 import InlineResponse200344

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200344 from a JSON string
inline_response200344_instance = InlineResponse200344.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200344.to_json())

# convert the object into a dict
inline_response200344_dict = inline_response200344_instance.to_dict()
# create an instance of InlineResponse200344 from a dict
inline_response200344_from_dict = InlineResponse200344.from_dict(inline_response200344_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


