# InlineResponse200132


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**apiversion** | **int** | The version of the API. | [optional] 
**func** | **str** | The name of the method called. | [optional] 
**module** | **str** | The name of the module called. | [optional] 
**result** | [**InlineResponse200132Result**](InlineResponse200132Result.md) |  | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200132 import InlineResponse200132

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200132 from a JSON string
inline_response200132_instance = InlineResponse200132.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200132.to_json())

# convert the object into a dict
inline_response200132_dict = inline_response200132_instance.to_dict()
# create an instance of InlineResponse200132 from a dict
inline_response200132_from_dict = InlineResponse200132.from_dict(inline_response200132_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


