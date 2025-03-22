# InlineResponse20094


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**apiversion** | **int** | The version of the API. | [optional] 
**func** | **str** | The name of the method called. | [optional] 
**module** | **str** | The name of the module called. | [optional] 
**result** | [**InlineResponse20094Result**](InlineResponse20094Result.md) |  | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response20094 import InlineResponse20094

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse20094 from a JSON string
inline_response20094_instance = InlineResponse20094.from_json(json)
# print the JSON string representation of the object
print(InlineResponse20094.to_json())

# convert the object into a dict
inline_response20094_dict = inline_response20094_instance.to_dict()
# create an instance of InlineResponse20094 from a dict
inline_response20094_from_dict = InlineResponse20094.from_dict(inline_response20094_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


