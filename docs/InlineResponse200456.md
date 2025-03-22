# InlineResponse200456


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**apiversion** | **int** | The version of the API. | [optional] 
**func** | **str** | The name of the method called. | [optional] 
**module** | **str** | The name of the module called. | [optional] 
**result** | [**InlineResponse200456Result**](InlineResponse200456Result.md) |  | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200456 import InlineResponse200456

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200456 from a JSON string
inline_response200456_instance = InlineResponse200456.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200456.to_json())

# convert the object into a dict
inline_response200456_dict = inline_response200456_instance.to_dict()
# create an instance of InlineResponse200456 from a dict
inline_response200456_from_dict = InlineResponse200456.from_dict(inline_response200456_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


