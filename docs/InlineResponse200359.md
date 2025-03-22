# InlineResponse200359


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**apiversion** | **int** | The version of the API. | [optional] 
**func** | **str** | The name of the method called. | [optional] 
**module** | **str** | The name of the module called. | [optional] 
**result** | [**InlineResponse200359Result**](InlineResponse200359Result.md) |  | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200359 import InlineResponse200359

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200359 from a JSON string
inline_response200359_instance = InlineResponse200359.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200359.to_json())

# convert the object into a dict
inline_response200359_dict = inline_response200359_instance.to_dict()
# create an instance of InlineResponse200359 from a dict
inline_response200359_from_dict = InlineResponse200359.from_dict(inline_response200359_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


