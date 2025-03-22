# InlineResponse200573


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**apiversion** | **int** | The version of the API. | [optional] 
**func** | **str** | The name of the method called. | [optional] 
**module** | **str** | The name of the module called. | [optional] 
**result** | [**InlineResponse200573Result**](InlineResponse200573Result.md) |  | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200573 import InlineResponse200573

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200573 from a JSON string
inline_response200573_instance = InlineResponse200573.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200573.to_json())

# convert the object into a dict
inline_response200573_dict = inline_response200573_instance.to_dict()
# create an instance of InlineResponse200573 from a dict
inline_response200573_from_dict = InlineResponse200573.from_dict(inline_response200573_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


