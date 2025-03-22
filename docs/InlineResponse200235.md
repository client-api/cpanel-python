# InlineResponse200235


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**apiversion** | **int** | The version of the API. | [optional] 
**func** | **str** | The name of the method called. | [optional] 
**module** | **str** | The name of the module called. | [optional] 
**result** | [**InlineResponse200235Result**](InlineResponse200235Result.md) |  | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200235 import InlineResponse200235

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200235 from a JSON string
inline_response200235_instance = InlineResponse200235.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200235.to_json())

# convert the object into a dict
inline_response200235_dict = inline_response200235_instance.to_dict()
# create an instance of InlineResponse200235 from a dict
inline_response200235_from_dict = InlineResponse200235.from_dict(inline_response200235_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


