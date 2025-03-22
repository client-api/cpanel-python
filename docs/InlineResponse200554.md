# InlineResponse200554


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**apiversion** | **int** | The version of the API. | [optional] 
**func** | **str** | The name of the method called. | [optional] 
**module** | **str** | The name of the module called. | [optional] 
**result** | [**InlineResponse200554Result**](InlineResponse200554Result.md) |  | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200554 import InlineResponse200554

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200554 from a JSON string
inline_response200554_instance = InlineResponse200554.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200554.to_json())

# convert the object into a dict
inline_response200554_dict = inline_response200554_instance.to_dict()
# create an instance of InlineResponse200554 from a dict
inline_response200554_from_dict = InlineResponse200554.from_dict(inline_response200554_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


