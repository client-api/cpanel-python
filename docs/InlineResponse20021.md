# InlineResponse20021


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**apiversion** | **int** | The version of the API. | [optional] 
**func** | **str** | The name of the method called. | [optional] 
**module** | **str** | The name of the module called. | [optional] 
**result** | [**InlineResponse20021Result**](InlineResponse20021Result.md) |  | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response20021 import InlineResponse20021

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse20021 from a JSON string
inline_response20021_instance = InlineResponse20021.from_json(json)
# print the JSON string representation of the object
print(InlineResponse20021.to_json())

# convert the object into a dict
inline_response20021_dict = inline_response20021_instance.to_dict()
# create an instance of InlineResponse20021 from a dict
inline_response20021_from_dict = InlineResponse20021.from_dict(inline_response20021_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


