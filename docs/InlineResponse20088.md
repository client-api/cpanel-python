# InlineResponse20088


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**apiversion** | **int** | The version of the API. | [optional] 
**func** | **str** | The name of the method called. | [optional] 
**module** | **str** | The name of the module called. | [optional] 
**result** | [**InlineResponse20088Result**](InlineResponse20088Result.md) |  | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response20088 import InlineResponse20088

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse20088 from a JSON string
inline_response20088_instance = InlineResponse20088.from_json(json)
# print the JSON string representation of the object
print(InlineResponse20088.to_json())

# convert the object into a dict
inline_response20088_dict = inline_response20088_instance.to_dict()
# create an instance of InlineResponse20088 from a dict
inline_response20088_from_dict = InlineResponse20088.from_dict(inline_response20088_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


