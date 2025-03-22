# InlineResponse200476


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**apiversion** | **int** | The version of the API. | [optional] 
**func** | **str** | The name of the method called. | [optional] 
**module** | **str** | The name of the module called. | [optional] 
**result** | [**InlineResponse200476Result**](InlineResponse200476Result.md) |  | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200476 import InlineResponse200476

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200476 from a JSON string
inline_response200476_instance = InlineResponse200476.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200476.to_json())

# convert the object into a dict
inline_response200476_dict = inline_response200476_instance.to_dict()
# create an instance of InlineResponse200476 from a dict
inline_response200476_from_dict = InlineResponse200476.from_dict(inline_response200476_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


