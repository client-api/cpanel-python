# InlineResponse200216


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**apiversion** | **int** | The version of the API. | [optional] 
**func** | **str** | The name of the method called. | [optional] 
**module** | **str** | The name of the module called. | [optional] 
**result** | [**InlineResponse200216Result**](InlineResponse200216Result.md) |  | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200216 import InlineResponse200216

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200216 from a JSON string
inline_response200216_instance = InlineResponse200216.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200216.to_json())

# convert the object into a dict
inline_response200216_dict = inline_response200216_instance.to_dict()
# create an instance of InlineResponse200216 from a dict
inline_response200216_from_dict = InlineResponse200216.from_dict(inline_response200216_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


