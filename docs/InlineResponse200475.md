# InlineResponse200475


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**apiversion** | **int** | The version of the API. | [optional] 
**func** | **str** | The name of the method called. | [optional] 
**module** | **str** | The name of the module called. | [optional] 
**result** | [**InlineResponse200475Result**](InlineResponse200475Result.md) |  | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200475 import InlineResponse200475

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200475 from a JSON string
inline_response200475_instance = InlineResponse200475.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200475.to_json())

# convert the object into a dict
inline_response200475_dict = inline_response200475_instance.to_dict()
# create an instance of InlineResponse200475 from a dict
inline_response200475_from_dict = InlineResponse200475.from_dict(inline_response200475_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


