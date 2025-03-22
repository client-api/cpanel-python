# InlineResponse200521


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**apiversion** | **int** | The version of the API. | [optional] 
**func** | **str** | The name of the method called. | [optional] 
**module** | **str** | The name of the module called. | [optional] 
**result** | [**InlineResponse200521Result**](InlineResponse200521Result.md) |  | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200521 import InlineResponse200521

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200521 from a JSON string
inline_response200521_instance = InlineResponse200521.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200521.to_json())

# convert the object into a dict
inline_response200521_dict = inline_response200521_instance.to_dict()
# create an instance of InlineResponse200521 from a dict
inline_response200521_from_dict = InlineResponse200521.from_dict(inline_response200521_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


