# InlineResponse200461


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**apiversion** | **int** | The version of the API. | [optional] 
**func** | **str** | The name of the method called. | [optional] 
**module** | **str** | The name of the module called. | [optional] 
**result** | [**InlineResponse200461Result**](InlineResponse200461Result.md) |  | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200461 import InlineResponse200461

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200461 from a JSON string
inline_response200461_instance = InlineResponse200461.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200461.to_json())

# convert the object into a dict
inline_response200461_dict = inline_response200461_instance.to_dict()
# create an instance of InlineResponse200461 from a dict
inline_response200461_from_dict = InlineResponse200461.from_dict(inline_response200461_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


