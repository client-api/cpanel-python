# InlineResponse20014


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**apiversion** | **int** | The version of the API. | [optional] 
**func** | **str** | The name of the method called. | [optional] 
**module** | **str** | The name of the module called. | [optional] 
**result** | [**InlineResponse20014Result**](InlineResponse20014Result.md) |  | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response20014 import InlineResponse20014

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse20014 from a JSON string
inline_response20014_instance = InlineResponse20014.from_json(json)
# print the JSON string representation of the object
print(InlineResponse20014.to_json())

# convert the object into a dict
inline_response20014_dict = inline_response20014_instance.to_dict()
# create an instance of InlineResponse20014 from a dict
inline_response20014_from_dict = InlineResponse20014.from_dict(inline_response20014_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


