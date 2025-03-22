# InlineResponse200139


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**apiversion** | **int** | The version of the API. | [optional] 
**func** | **str** | The name of the method called. | [optional] 
**module** | **str** | The name of the module called. | [optional] 
**result** | [**InlineResponse200120Result**](InlineResponse200120Result.md) |  | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200139 import InlineResponse200139

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200139 from a JSON string
inline_response200139_instance = InlineResponse200139.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200139.to_json())

# convert the object into a dict
inline_response200139_dict = inline_response200139_instance.to_dict()
# create an instance of InlineResponse200139 from a dict
inline_response200139_from_dict = InlineResponse200139.from_dict(inline_response200139_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


