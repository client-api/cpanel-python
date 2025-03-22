# InlineResponse200262


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**apiversion** | **int** | The version of the API. | [optional] 
**func** | **str** | The name of the method called. | [optional] 
**module** | **str** | The name of the module called. | [optional] 
**result** | [**InlineResponse20035Result**](InlineResponse20035Result.md) |  | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200262 import InlineResponse200262

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200262 from a JSON string
inline_response200262_instance = InlineResponse200262.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200262.to_json())

# convert the object into a dict
inline_response200262_dict = inline_response200262_instance.to_dict()
# create an instance of InlineResponse200262 from a dict
inline_response200262_from_dict = InlineResponse200262.from_dict(inline_response200262_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


