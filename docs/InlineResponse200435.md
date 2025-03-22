# InlineResponse200435


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**apiversion** | **int** | The version of the API. | [optional] 
**func** | **str** | The name of the method called. | [optional] 
**module** | **str** | The name of the module called. | [optional] 
**result** | [**InlineResponse200435Result**](InlineResponse200435Result.md) |  | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200435 import InlineResponse200435

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200435 from a JSON string
inline_response200435_instance = InlineResponse200435.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200435.to_json())

# convert the object into a dict
inline_response200435_dict = inline_response200435_instance.to_dict()
# create an instance of InlineResponse200435 from a dict
inline_response200435_from_dict = InlineResponse200435.from_dict(inline_response200435_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


