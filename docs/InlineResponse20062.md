# InlineResponse20062


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**apiversion** | **int** | The version of the API. | [optional] 
**func** | **str** | The name of the method called. | [optional] 
**module** | **str** | The name of the module called. | [optional] 
**result** | [**InlineResponse20062Result**](InlineResponse20062Result.md) |  | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response20062 import InlineResponse20062

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse20062 from a JSON string
inline_response20062_instance = InlineResponse20062.from_json(json)
# print the JSON string representation of the object
print(InlineResponse20062.to_json())

# convert the object into a dict
inline_response20062_dict = inline_response20062_instance.to_dict()
# create an instance of InlineResponse20062 from a dict
inline_response20062_from_dict = InlineResponse20062.from_dict(inline_response20062_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


