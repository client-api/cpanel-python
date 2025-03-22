# InlineResponse200150


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**apiversion** | **int** | The version of the API. | [optional] 
**func** | **str** | The name of the method called. | [optional] 
**module** | **str** | The name of the module called. | [optional] 
**result** | [**InlineResponse200150Result**](InlineResponse200150Result.md) |  | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200150 import InlineResponse200150

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200150 from a JSON string
inline_response200150_instance = InlineResponse200150.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200150.to_json())

# convert the object into a dict
inline_response200150_dict = inline_response200150_instance.to_dict()
# create an instance of InlineResponse200150 from a dict
inline_response200150_from_dict = InlineResponse200150.from_dict(inline_response200150_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


