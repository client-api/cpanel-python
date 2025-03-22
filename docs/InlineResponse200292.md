# InlineResponse200292


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**apiversion** | **int** | The version of the API. | [optional] 
**func** | **str** | The name of the method called. | [optional] 
**module** | **str** | The name of the module called. | [optional] 
**result** | [**InlineResponse200292Result**](InlineResponse200292Result.md) |  | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200292 import InlineResponse200292

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200292 from a JSON string
inline_response200292_instance = InlineResponse200292.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200292.to_json())

# convert the object into a dict
inline_response200292_dict = inline_response200292_instance.to_dict()
# create an instance of InlineResponse200292 from a dict
inline_response200292_from_dict = InlineResponse200292.from_dict(inline_response200292_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


