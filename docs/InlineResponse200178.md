# InlineResponse200178


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**apiversion** | **int** | The version of the API. | [optional] 
**func** | **str** | The name of the method called. | [optional] 
**module** | **str** | The name of the module called. | [optional] 
**result** | [**InlineResponse200178Result**](InlineResponse200178Result.md) |  | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200178 import InlineResponse200178

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200178 from a JSON string
inline_response200178_instance = InlineResponse200178.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200178.to_json())

# convert the object into a dict
inline_response200178_dict = inline_response200178_instance.to_dict()
# create an instance of InlineResponse200178 from a dict
inline_response200178_from_dict = InlineResponse200178.from_dict(inline_response200178_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


