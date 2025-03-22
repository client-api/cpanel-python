# InlineResponse20058


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**apiversion** | **int** | The version of the API. | [optional] 
**func** | **str** | The name of the method called. | [optional] 
**module** | **str** | The name of the module called. | [optional] 
**result** | [**InlineResponse20058Result**](InlineResponse20058Result.md) |  | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response20058 import InlineResponse20058

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse20058 from a JSON string
inline_response20058_instance = InlineResponse20058.from_json(json)
# print the JSON string representation of the object
print(InlineResponse20058.to_json())

# convert the object into a dict
inline_response20058_dict = inline_response20058_instance.to_dict()
# create an instance of InlineResponse20058 from a dict
inline_response20058_from_dict = InlineResponse20058.from_dict(inline_response20058_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


