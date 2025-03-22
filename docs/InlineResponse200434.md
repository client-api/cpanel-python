# InlineResponse200434


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**apiversion** | **int** | The version of the API. | [optional] 
**func** | **str** | The name of the method called. | [optional] 
**module** | **str** | The name of the module called. | [optional] 
**result** | [**InlineResponse200434Result**](InlineResponse200434Result.md) |  | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200434 import InlineResponse200434

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200434 from a JSON string
inline_response200434_instance = InlineResponse200434.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200434.to_json())

# convert the object into a dict
inline_response200434_dict = inline_response200434_instance.to_dict()
# create an instance of InlineResponse200434 from a dict
inline_response200434_from_dict = InlineResponse200434.from_dict(inline_response200434_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


