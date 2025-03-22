# InlineResponse200565


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**apiversion** | **int** | The version of the API. | [optional] 
**func** | **str** | The name of the method called. | [optional] 
**module** | **str** | The name of the module called. | [optional] 
**result** | [**InlineResponse200565Result**](InlineResponse200565Result.md) |  | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200565 import InlineResponse200565

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200565 from a JSON string
inline_response200565_instance = InlineResponse200565.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200565.to_json())

# convert the object into a dict
inline_response200565_dict = inline_response200565_instance.to_dict()
# create an instance of InlineResponse200565 from a dict
inline_response200565_from_dict = InlineResponse200565.from_dict(inline_response200565_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


