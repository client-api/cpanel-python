# InlineResponse200428


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**apiversion** | **int** | The version of the API. | [optional] 
**func** | **str** | The name of the method called. | [optional] 
**module** | **str** | The name of the module called. | [optional] 
**result** | [**InlineResponse200428Result**](InlineResponse200428Result.md) |  | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200428 import InlineResponse200428

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200428 from a JSON string
inline_response200428_instance = InlineResponse200428.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200428.to_json())

# convert the object into a dict
inline_response200428_dict = inline_response200428_instance.to_dict()
# create an instance of InlineResponse200428 from a dict
inline_response200428_from_dict = InlineResponse200428.from_dict(inline_response200428_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


