# InlineResponse20022


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**apiversion** | **int** | The version of the API. | [optional] 
**func** | **str** | The name of the method called. | [optional] 
**module** | **str** | The name of the module called. | [optional] 
**result** | [**InlineResponse20022Result**](InlineResponse20022Result.md) |  | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response20022 import InlineResponse20022

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse20022 from a JSON string
inline_response20022_instance = InlineResponse20022.from_json(json)
# print the JSON string representation of the object
print(InlineResponse20022.to_json())

# convert the object into a dict
inline_response20022_dict = inline_response20022_instance.to_dict()
# create an instance of InlineResponse20022 from a dict
inline_response20022_from_dict = InlineResponse20022.from_dict(inline_response20022_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


