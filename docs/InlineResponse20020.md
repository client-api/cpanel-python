# InlineResponse20020


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**apiversion** | **int** | The version of the API. | [optional] 
**func** | **str** | The name of the method called. | [optional] 
**module** | **str** | The name of the module called. | [optional] 
**result** | [**InlineResponse20020Result**](InlineResponse20020Result.md) |  | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response20020 import InlineResponse20020

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse20020 from a JSON string
inline_response20020_instance = InlineResponse20020.from_json(json)
# print the JSON string representation of the object
print(InlineResponse20020.to_json())

# convert the object into a dict
inline_response20020_dict = inline_response20020_instance.to_dict()
# create an instance of InlineResponse20020 from a dict
inline_response20020_from_dict = InlineResponse20020.from_dict(inline_response20020_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


