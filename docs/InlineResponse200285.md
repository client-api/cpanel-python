# InlineResponse200285


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**apiversion** | **int** | The version of the API. | [optional] 
**func** | **str** | The name of the method called. | [optional] 
**module** | **str** | The name of the module called. | [optional] 
**result** | [**InlineResponse200285Result**](InlineResponse200285Result.md) |  | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200285 import InlineResponse200285

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200285 from a JSON string
inline_response200285_instance = InlineResponse200285.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200285.to_json())

# convert the object into a dict
inline_response200285_dict = inline_response200285_instance.to_dict()
# create an instance of InlineResponse200285 from a dict
inline_response200285_from_dict = InlineResponse200285.from_dict(inline_response200285_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


