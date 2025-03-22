# InlineResponse200297


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**apiversion** | **int** | The version of the API. | [optional] 
**func** | **str** | The name of the method called. | [optional] 
**module** | **str** | The name of the module called. | [optional] 
**result** | [**InlineResponse200293Result**](InlineResponse200293Result.md) |  | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200297 import InlineResponse200297

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200297 from a JSON string
inline_response200297_instance = InlineResponse200297.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200297.to_json())

# convert the object into a dict
inline_response200297_dict = inline_response200297_instance.to_dict()
# create an instance of InlineResponse200297 from a dict
inline_response200297_from_dict = InlineResponse200297.from_dict(inline_response200297_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


