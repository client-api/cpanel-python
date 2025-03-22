# InlineResponse200520


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**apiversion** | **int** | The version of the API. | [optional] 
**func** | **str** | The name of the method called. | [optional] 
**module** | **str** | The name of the module called. | [optional] 
**result** | [**InlineResponse200520Result**](InlineResponse200520Result.md) |  | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200520 import InlineResponse200520

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200520 from a JSON string
inline_response200520_instance = InlineResponse200520.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200520.to_json())

# convert the object into a dict
inline_response200520_dict = inline_response200520_instance.to_dict()
# create an instance of InlineResponse200520 from a dict
inline_response200520_from_dict = InlineResponse200520.from_dict(inline_response200520_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


