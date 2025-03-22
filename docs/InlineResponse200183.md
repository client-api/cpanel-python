# InlineResponse200183


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**apiversion** | **int** | The version of the API. | [optional] 
**func** | **str** | The name of the method called. | [optional] 
**module** | **str** | The name of the module called. | [optional] 
**result** | [**InlineResponse200183Result**](InlineResponse200183Result.md) |  | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200183 import InlineResponse200183

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200183 from a JSON string
inline_response200183_instance = InlineResponse200183.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200183.to_json())

# convert the object into a dict
inline_response200183_dict = inline_response200183_instance.to_dict()
# create an instance of InlineResponse200183 from a dict
inline_response200183_from_dict = InlineResponse200183.from_dict(inline_response200183_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


