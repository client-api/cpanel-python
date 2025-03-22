# InlineResponse200122


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**apiversion** | **int** | The version of the API. | [optional] 
**func** | **str** | The name of the method called. | [optional] 
**module** | **str** | The name of the module called. | [optional] 
**result** | [**InlineResponse200122Result**](InlineResponse200122Result.md) |  | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200122 import InlineResponse200122

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200122 from a JSON string
inline_response200122_instance = InlineResponse200122.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200122.to_json())

# convert the object into a dict
inline_response200122_dict = inline_response200122_instance.to_dict()
# create an instance of InlineResponse200122 from a dict
inline_response200122_from_dict = InlineResponse200122.from_dict(inline_response200122_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


