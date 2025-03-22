# InlineResponse20059


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**apiversion** | **int** | The version of the API. | [optional] 
**func** | **str** | The name of the method called. | [optional] 
**module** | **str** | The name of the module called. | [optional] 
**result** | [**InlineResponse20059Result**](InlineResponse20059Result.md) |  | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response20059 import InlineResponse20059

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse20059 from a JSON string
inline_response20059_instance = InlineResponse20059.from_json(json)
# print the JSON string representation of the object
print(InlineResponse20059.to_json())

# convert the object into a dict
inline_response20059_dict = inline_response20059_instance.to_dict()
# create an instance of InlineResponse20059 from a dict
inline_response20059_from_dict = InlineResponse20059.from_dict(inline_response20059_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


