# InlineResponse200254


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**apiversion** | **int** | The version of the API. | [optional] 
**func** | **str** | The name of the method called. | [optional] 
**module** | **str** | The name of the module called. | [optional] 
**result** | [**InlineResponse200254Result**](InlineResponse200254Result.md) |  | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200254 import InlineResponse200254

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200254 from a JSON string
inline_response200254_instance = InlineResponse200254.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200254.to_json())

# convert the object into a dict
inline_response200254_dict = inline_response200254_instance.to_dict()
# create an instance of InlineResponse200254 from a dict
inline_response200254_from_dict = InlineResponse200254.from_dict(inline_response200254_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


