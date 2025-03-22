# InlineResponse200188


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**apiversion** | **int** | The version of the API. | [optional] 
**func** | **str** | The name of the method called. | [optional] 
**module** | **str** | The name of the module called. | [optional] 
**result** | [**InlineResponse200188Result**](InlineResponse200188Result.md) |  | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200188 import InlineResponse200188

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200188 from a JSON string
inline_response200188_instance = InlineResponse200188.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200188.to_json())

# convert the object into a dict
inline_response200188_dict = inline_response200188_instance.to_dict()
# create an instance of InlineResponse200188 from a dict
inline_response200188_from_dict = InlineResponse200188.from_dict(inline_response200188_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


