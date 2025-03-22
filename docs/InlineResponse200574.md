# InlineResponse200574


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**apiversion** | **int** | The version of the API. | [optional] 
**func** | **str** | The name of the method called. | [optional] 
**module** | **str** | The name of the module called. | [optional] 
**result** | [**InlineResponse200574Result**](InlineResponse200574Result.md) |  | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200574 import InlineResponse200574

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200574 from a JSON string
inline_response200574_instance = InlineResponse200574.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200574.to_json())

# convert the object into a dict
inline_response200574_dict = inline_response200574_instance.to_dict()
# create an instance of InlineResponse200574 from a dict
inline_response200574_from_dict = InlineResponse200574.from_dict(inline_response200574_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


