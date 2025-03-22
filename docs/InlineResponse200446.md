# InlineResponse200446


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**apiversion** | **int** | The version of the API. | [optional] 
**func** | **str** | The name of the method called. | [optional] 
**module** | **str** | The name of the module called. | [optional] 
**result** | [**InlineResponse200446Result**](InlineResponse200446Result.md) |  | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200446 import InlineResponse200446

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200446 from a JSON string
inline_response200446_instance = InlineResponse200446.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200446.to_json())

# convert the object into a dict
inline_response200446_dict = inline_response200446_instance.to_dict()
# create an instance of InlineResponse200446 from a dict
inline_response200446_from_dict = InlineResponse200446.from_dict(inline_response200446_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


