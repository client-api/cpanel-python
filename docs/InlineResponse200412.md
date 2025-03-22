# InlineResponse200412


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**apiversion** | **int** | The version of the API. | [optional] 
**func** | **str** | The name of the method called. | [optional] 
**module** | **str** | The name of the module called. | [optional] 
**result** | [**InlineResponse200412Result**](InlineResponse200412Result.md) |  | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200412 import InlineResponse200412

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200412 from a JSON string
inline_response200412_instance = InlineResponse200412.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200412.to_json())

# convert the object into a dict
inline_response200412_dict = inline_response200412_instance.to_dict()
# create an instance of InlineResponse200412 from a dict
inline_response200412_from_dict = InlineResponse200412.from_dict(inline_response200412_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


