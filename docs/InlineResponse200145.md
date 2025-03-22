# InlineResponse200145


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**apiversion** | **int** | The version of the API. | [optional] 
**func** | **str** | The name of the method called. | [optional] 
**module** | **str** | The name of the module called. | [optional] 
**result** | [**InlineResponse200145Result**](InlineResponse200145Result.md) |  | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200145 import InlineResponse200145

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200145 from a JSON string
inline_response200145_instance = InlineResponse200145.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200145.to_json())

# convert the object into a dict
inline_response200145_dict = inline_response200145_instance.to_dict()
# create an instance of InlineResponse200145 from a dict
inline_response200145_from_dict = InlineResponse200145.from_dict(inline_response200145_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


