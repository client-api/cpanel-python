# InlineResponse20026


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**apiversion** | **int** | The version of the API. | [optional] 
**func** | **str** | The name of the method called. | [optional] 
**module** | **str** | The name of the module called. | [optional] 
**result** | [**InlineResponse20026Result**](InlineResponse20026Result.md) |  | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response20026 import InlineResponse20026

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse20026 from a JSON string
inline_response20026_instance = InlineResponse20026.from_json(json)
# print the JSON string representation of the object
print(InlineResponse20026.to_json())

# convert the object into a dict
inline_response20026_dict = inline_response20026_instance.to_dict()
# create an instance of InlineResponse20026 from a dict
inline_response20026_from_dict = InlineResponse20026.from_dict(inline_response20026_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


