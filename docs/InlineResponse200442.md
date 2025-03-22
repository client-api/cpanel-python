# InlineResponse200442


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**apiversion** | **int** | The version of the API. | [optional] 
**func** | **str** | The name of the method called. | [optional] 
**module** | **str** | The name of the module called. | [optional] 
**result** | [**InlineResponse20035Result**](InlineResponse20035Result.md) |  | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200442 import InlineResponse200442

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200442 from a JSON string
inline_response200442_instance = InlineResponse200442.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200442.to_json())

# convert the object into a dict
inline_response200442_dict = inline_response200442_instance.to_dict()
# create an instance of InlineResponse200442 from a dict
inline_response200442_from_dict = InlineResponse200442.from_dict(inline_response200442_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


