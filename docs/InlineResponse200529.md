# InlineResponse200529


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**apiversion** | **int** | The version of the API. | [optional] 
**func** | **str** | The name of the method called. | [optional] 
**module** | **str** | The name of the module called. | [optional] 
**result** | [**InlineResponse200529Result**](InlineResponse200529Result.md) |  | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200529 import InlineResponse200529

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200529 from a JSON string
inline_response200529_instance = InlineResponse200529.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200529.to_json())

# convert the object into a dict
inline_response200529_dict = inline_response200529_instance.to_dict()
# create an instance of InlineResponse200529 from a dict
inline_response200529_from_dict = InlineResponse200529.from_dict(inline_response200529_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


