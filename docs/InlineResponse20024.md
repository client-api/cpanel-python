# InlineResponse20024


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**apiversion** | **int** | The version of the API. | [optional] 
**func** | **str** | The name of the method called. | [optional] 
**module** | **str** | The name of the module called. | [optional] 
**result** | [**InlineResponse20024Result**](InlineResponse20024Result.md) |  | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response20024 import InlineResponse20024

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse20024 from a JSON string
inline_response20024_instance = InlineResponse20024.from_json(json)
# print the JSON string representation of the object
print(InlineResponse20024.to_json())

# convert the object into a dict
inline_response20024_dict = inline_response20024_instance.to_dict()
# create an instance of InlineResponse20024 from a dict
inline_response20024_from_dict = InlineResponse20024.from_dict(inline_response20024_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


